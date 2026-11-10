---
title: "Serving files over HTTP three ways: synchronous, epoll, and io_uring"
source: "https://theconsensus.dev/p/2026/05/18/serving-files-three-ways.html"
author:
  - "[[Phil Eaton·May 18]]"
  - "[[2026]]"
published: 2026-05-18
created: 2026-06-01
description: "We take a tour of epoll and io_uring through the lens of an HTTP file server, starting off first with a synchronous thread-per-request server as a baseline."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Computer Networking
  - Systems Programming
  - Linux Kernel
  - Asynchronous I/O
  - io_uring
  - epoll
related:
  - "Computer Networking"
  - "Anirudh Rowjee - Linux IO Subsystem Walkthrough.md"
  - "When idle isn't idle how a Linux kernel optimization became a QUIC bug.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A practical C walkthrough comparing three Linux I/O patterns (synchronous threads, epoll event loops, and io_uring) through the implementation of an HTTP file server.
>
> **Key points:**
> - Implements a baseline synchronous multi-threaded server using standard blocking sockets, where thread overhead scales with client count.
> - Demonstrates an event-loop design with non-blocking sockets using epoll, highlighting its limitation where disk I/O remains blocking on standard Linux filesystems.
> - Details io_uring implementation, utilizing submission and completion queues to achieve true asynchronous operations for both socket and disk I/O.
> - Explores optimization differences in connection handling, state machines, and system call overhead reductions across the three methods.
>
> **Concept links:** [[Computer Networking]], [[Systems Programming]], [[Linux Kernel]], [[Asynchronous I/O]], [[io_uring]], [[epoll]]
>
> **Suggested connections:**
> - [[Anirudh Rowjee - Linux IO Subsystem Walkthrough.md]] — provides the under-the-hood context of the Linux kernel I/O path, system calls, and page caches behind these server implementations.
> - [[When idle isn't idle how a Linux kernel optimization became a QUIC bug.md]] — connects server socket multiplexing and performance loops to kernel optimization analysis.
<!-- ai-summary:end -->

A file server is a nice path through which to explore IO methods because we can write a relatively simple program that still does both network and disk IO. And we can, though in this article we won’t, spend no end of time enhancing and optimizing it (on-the-fly compression, integrity checks, keep-alive, uploads, memory usage, etc.)

Let's start with some shared code across IO methods.

No matter the IO method, we’ll need to be able to listen on a port.

```
#pragma once

#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define DOCROOT  "./"
#define MAX_REQ_BUF  4096
#define IO_BUF   16384

static inline int listen_socket(uint16_t port) {
  int fd = socket(AF_INET, SOCK_STREAM, 0);
  if (fd < 0) { perror("socket"); exit(1); }

  int yes = 1;
  setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));

  struct sockaddr_in addr = {0};
  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = htonl(INADDR_ANY);
  addr.sin_port = htons(port);

  if (bind(fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
    perror("bind"); exit(1);
  }
  if (listen(fd, 128) < 0) { perror("listen"); exit(1); }
  return fd;
}
```

common.h

We’ll need to be able to pull the path out of a GET HTTP request.

```
static inline int parse_http_get(const char *req, size_t len, char *out, size_t n) {
  if (len < 5 || strncmp(req, "GET ", 4) != 0) return -1;

  const char *p = req + 4;
  const char *sp = memchr(p, ' ', len - 4);
  if (!sp) return -1;

  size_t plen = (size_t)(sp - p);
  if (plen == 0 || plen >= n) return -1;
  if (p[0] != '/') return -1;

  memcpy(out, p, plen);
  out[plen] = 0;

  if (plen == 1) {
    if (n < sizeof("/index.html")) return -1;
    memcpy(out, "/index.html", sizeof("/index.html"));
  }
  return 0;
}
```

common.h

We’ll need to be able to map file extensions (for files that are requested) to MIME types.

```
static inline const char *mime_for(const char *path) {
  const char *dot = strrchr(path, '.');
  if (!dot) return "application/octet-stream";
  if (!strncmp(dot, ".html", sizeof(".html"))) return "text/html";
  if (!strncmp(dot, ".css",  sizeof(".css")))  return "text/css";
  if (!strncmp(dot, ".js",   sizeof(".js")))   return "application/javascript";
  if (!strncmp(dot, ".json", sizeof(".json"))) return "application/json";
  if (!strncmp(dot, ".png",  sizeof(".png")))  return "image/png";
  if (!strncmp(dot, ".jpg",  sizeof(".jpg")) ||
      !strncmp(dot, ".jpeg", sizeof(".jpeg"))) return "image/jpeg";
  if (!strncmp(dot, ".txt",  sizeof(".txt")))  return "text/plain";
  return "application/octet-stream";
}
```

common.h

And we’ll need to be able to format HTTP responses, good and bad.

```
static inline int build_ok_headers(char *buf, size_t n, const char *mime) {
  return snprintf(buf, n,
                  "HTTP/1.1 200 OK\r\n"
                  "Content-Type: %s\r\n"
                  "Connection: close\r\n"
                  "\r\n",
                  mime);
}

static inline int build_404(char *buf, size_t n) {
  return snprintf(buf, n,
                  "HTTP/1.1 404 Not Found\r\n"
                  "Content-Type: text/plain\r\n"
                  "Connection: close\r\n"
                  "\r\n"
                  "404 Not Found\n");
}
```

With all of that we can build a simple, synchronous, thread-per-request file server. (There are numerous edge cases I just won’t worry about.)

Let’s start at the bottom and make our way up. We create a server and we give each new accepted connection its own thread.

```
int main(int argc, char **argv) {
  signal(SIGPIPE, SIG_IGN);

  uint16_t port = (argc > 1) ? (uint16_t)atoi(argv[1]) : 8080;
  int sfd = listen_socket(port);
  fprintf(stderr, "sync (thread per request) server on :%u\n", port);

  pthread_attr_t attr;
  pthread_attr_init(&attr);
  pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);

  for (;;) {
    int conn = accept(sfd, NULL, NULL);
    if (conn < 0) {
      if (errno == EINTR)
        continue;

      perror("accept");
      break;
    }

    pthread_t tid;
    if (pthread_create(&tid, &attr, serve, (void *)(intptr_t)conn) != 0) {
      perror("pthread_create");
      close(conn);
    }
  }
  pthread_attr_destroy(&attr);
  return 0;
}
```

sync.c

The `serve` method reads and parses the request and builds a response and writes it.

```
static void *serve(void *arg) {
  int conn = (int)(intptr_t)arg;
  char path[1024];
  int rc = parse_request(conn, path, sizeof(path));
  if (rc == 0)
    send_response(conn, path);
  else if (rc == -1) // Connection died, do nothing.
    {}
  else if (rc == -2) // Request malformed, send 404.
    send_response(conn, NULL);

  close(conn);
  return NULL;
}
```

sync.c

The `parse_request` method reads all headers and fills in the `path` of the request. It returns -1 if the connection closes early and -2 if the headers cannot be parsed.

```
static int parse_request(int conn, char *path, size_t path_size) {
  char req_buf[MAX_REQ_BUF];
  size_t offset = 0;

  while (offset < sizeof(req_buf)) {
    ssize_t r = read(conn, req_buf + offset, sizeof(req_buf) - offset);
    if (r < 0) {
      if (errno == EINTR)
        continue;

      return -1;
    }
    if (r == 0)
      return -1;
    offset += (size_t)r;
    if (offset >= 4 && memmem(req_buf, offset, "\r\n\r\n", 4))
      break;
  }

  if (parse_http_get(req_buf, offset, path, path_size) < 0)
    return -2;
  return 0;
}
```

sync.c

The `send_response` method reads the requested file from disk and writes it back on the connection.

```
static void send_response(int conn, const char *path) {
  char headers[512];
  int file_fd = -1;
  if (path != NULL) {
    char full[2048];
    snprintf(full, sizeof(full), "%s%s", DOCROOT, path);
    file_fd = open(full, O_RDONLY);
  }

  if (file_fd < 0) {
    int header_length = build_404(headers, sizeof(headers));
    write_all(conn, headers, header_length);
    return;
  }

  int header_length = build_ok_headers(headers, sizeof(headers), mime_for(path));
  if (write_all(conn, headers, header_length) < 0) {
    close(file_fd);
    return;
  }

  char body_buf[IO_BUF];
  for (;;) {
    ssize_t r = read(file_fd, body_buf, sizeof(body_buf));
    if (r < 0) {
      if (errno == EINTR)
        continue;

      break;
    }
    if (r == 0)
      break;
    if (write_all(conn, body_buf, r) < 0)
      break;
  }
  close(file_fd);
}
```

sync.c

Finally, we have our headers and our `write_all` helper.

```
#include "common.h"
#include <pthread.h>
#include <signal.h>

static int write_all(int fd, const void *buf, size_t towrite) {
  const char *p = buf;
  while (towrite) {
    ssize_t w = write(fd, p, towrite);
    if (w < 0) {
      if (errno == EINTR)
        continue;

      return -1;
    }
    p += w;
    towrite -= (size_t)w;
  }
  return 0;
}
```

sync.c

Compile it and try it out.

```
sudo apt-get update -y && sudo apt-get install clang
clang sync.c -o sync_file_server
./sync_file_server &
curl localhost:8080/common.h
kill %1
```

Synchronous I/O is pretty simple! While we could write this server without threads, we’d not be able to accept multiple concurrent connections. Each new connection will wait to be `accept` -ed until any existing accepted connection completes.

We also maybe could have used [pread](https://man7.org/linux/man-pages/man2/pread.2.html?from_theconsensus=1) or [readv](https://man7.org/linux/man-pages/man2/readv.2.html?from_theconsensus=1) to read the file, or [sendfile](https://man7.org/linux/man-pages/man2/sendfile.2.html?from_theconsensus=1) for minimizing copies, but there are only few variations of synchronous operations and they all look pretty similar. The synchronous server doesn’t get that exotic.

Things get a little more exciting when we review our options on Linux. We’ll look at just two: epoll and io\_uring.

## epoll

With epoll, you register file descriptors and epoll will tell you when the file descriptor is ready with data to read or with space available to write. This only works for some file descriptors (like sockets), not file descriptors for actual files on disk where epoll [will return](https://man7.org/linux/man-pages/man2/epoll_ctl.2.html?from_theconsensus=1#:~:text=EPERM%20%20The%20target%20file%20fd%20does%20not%20support%20epoll.%20%20This%20error%20can%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20occur%20if%20fd%20refers%20to%2C%20for%20example%2C%20a%20regular%20file%20or%20a%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20directory.) EPERM:

> The target file fd does not support epoll. This error can occur if fd refers to, for example, a regular file or a directory.

We can see this happen for ourselves if we try to register listeners for `common.h`.

```
#include <fcntl.h>
#include <stdio.h>
#include <sys/epoll.h>

int main(int argc, char **argv) {
  int file_fd = open("common.h", O_RDONLY);
  if (file_fd < 0)
    return 1;

  int epoll_fd = epoll_create1(0);
  if (epoll_fd < 0)
    return 2;

  struct epoll_event ev = { .events = EPOLLIN, .data.fd = file_fd };
  int rc = epoll_ctl(epoll_fd, EPOLL_CTL_ADD, file_fd, &ev);
  if (rc < 0) {
    printf("epoll add common.h failed\n");
    return 3;
  }

  printf("epoll add common.h ok\n");
  return 0;
}
```

epoll\_check.c

Compile and run it.

```
$ clang epoll_check.c
$ ./a.out
epoll add common.h failed
```

All of this matters because, as kernel developer Jens Axboe says in [Efficient IO with io\_uring](https://kernel.dk/io_uring.pdf?from_theconsensus=1):

> Even if you satisfy all the constraints for IO to be async, it's sometimes not. There are a number of ways that the IO submission can end up blocking - if meta data is required to perform IO, the submission will block waiting for that. For storage devices, there are a fixed number of request slots available. If those slots are currently all in use, submission will block waiting for one to become available. These uncertainties mean that applications that rely on submission always being async are still forced to offload that part.

So while we can be reasonably sure that our `send` / `recv` calls will not block for a long time with epoll, we have no such assurance about our `read` / `write` calls. We’d have to use something like a thread pool for disk I/O to achieve non-blocking I/O for disk, even with epoll.

In any case, let’s take a look at our file-server ported to epoll, starting from the top again. We create a socket, bind and listen on a port. But instead of accepting connections directly, we pass the socket file descriptor to epoll and loop forever (where our logic for handling both new connections and existing ones will go).

```
int main(int argc, char **argv) {
  uint16_t port = (argc > 1) ? (uint16_t)atoi(argv[1]) : 8080;
  int socket_fd = listen_socket(port);
  int sfl = fcntl(socket_fd, F_GETFL, 0);
  fcntl(socket_fd, F_SETFL, sfl | O_NONBLOCK);

  epoll_fd = epoll_create1(0);
  if (epoll_fd < 0) {
    perror("epoll_create1");
    return 1;
  }

  struct epoll_event lev = {
    .events = EPOLLIN,
    .data.ptr = NULL, // Our indication to ourselves this is the socket_fd not a conn_fd.
  };
  epoll_ctl(epoll_fd, EPOLL_CTL_ADD, socket_fd, &lev);
  fprintf(stderr, "epoll server on :%u\n", port);

  for (;;)
    epoll_step(socket_fd);
}
```

epoll.c

We pass in our own user data. For the *socket* we’ll learn about readiness for `accept` -ing new requests. For an existing *connection* we’ll learn about readiness for `recv` -ing from it or `send` -ing to it.

In the `epoll_step` we pass control to epoll to wait for readiness events. When we get control back we iterate through readiness events and 1) `accept` if the event refers to the *socket* (event user data is NULL) and tell epoll to track the new connection or 2) read from or write to what must otherwise be a *connection*.

```
static void epoll_step(int socket_fd) {
  struct epoll_event evs[64];
  int n = epoll_wait(epoll_fd, evs, 64, -1);
  for (int i = 0; i < n; i++) {
    if (evs[i].data.ptr == NULL) {
      // Event refers to socket. Accept any waiting connections.
      for (;;) {
        int conn_fd = accept(socket_fd, NULL, NULL);
        if (conn_fd < 0) {
          // Socket is non-blocking, so <0 means error or no more waiting connections.
          break;
        }

        int cfl = fcntl(conn_fd, F_GETFL, 0);
        fcntl(conn_fd, F_SETFL, cfl | O_NONBLOCK);
        struct conn *c = calloc(1, sizeof(*c));
        c->conn_fd = conn_fd;
        c->file_fd = -1;
        struct epoll_event ev = { .events = EPOLLIN, .data.ptr = c };
        epoll_ctl(epoll_fd, EPOLL_CTL_ADD, conn_fd, &ev);
      }
      continue;
    }

    // Event refers to a connection. Read from, write to, or close the connection.
    struct conn *c = evs[i].data.ptr;
    if (evs[i].events & EPOLLIN)
      on_readable(c);
    else if (evs[i].events & EPOLLOUT)
      on_writable(c);
    else
      conn_close(c);
  }
}
```

epoll.c

An interesting thing to note about epoll is that we can register notifications for reads (`.events = EPOLLIN`) or writes (`.events = EPOLLOUT`) or both (`.events = EPOLLIN | EPOLLOUT`). In the context of an HTTP server we can optimize notifications by only registering reads at first. When we’re done reading we’ll tell epoll to switch to only notifying us about write-readiness on this connection.

As you can see, the system is already event-driven and it’s going to continue like this. In the `on_readable` method we’ll keep accumulating data until we reach the end of the headers. Then we’ll kick off responding to the request.

```
static void on_readable(struct conn *c) {
  while (c->req_offset < sizeof(c->req)) {
    ssize_t r = read(c->conn_fd, c->req + c->req_offset, sizeof(c->req) - c->req_offset);
    if (r == 0) {
      conn_close(c);
      return;
    }
    if (r < 0) {
      if (errno == EAGAIN || errno == EWOULDBLOCK)
        return;

      conn_close(c);
      return;
    }
    c->req_offset += (size_t)r;
    if (memmem(c->req, c->req_offset, "\r\n\r\n", 4)) {
      start_response(c);
      return;
    }
  }
  conn_close(c);
}
```

epoll.c

In `start_response`, now that we’ve read at least all headers, we’ll parse the request and try to open the referred-to file. We’ll also switch epoll readiness checks from reads to writes.

```
static void start_response(struct conn *c) {
  char path[1024];
  int rc = parse_http_get(c->req, c->req_offset, path, sizeof(path));

  if (rc < 0) {
    c->out_len = build_404(c->out, sizeof(c->out));
    c->out_offset = 0;
    c->file_eof = 1;
  } else {
    char full[2048];
    snprintf(full, sizeof(full), "%s%s", DOCROOT, path);
    c->file_fd = open(full, O_RDONLY);
    if (c->file_fd < 0) {
      c->out_len = build_404(c->out, sizeof(c->out));
      c->out_offset = 0;
      c->file_eof = 1;
    } else {
      c->out_len = build_ok_headers(c->out, sizeof(c->out), mime_for(path));
      c->out_offset = 0;
    }
  }
  struct epoll_event ev = { .events = EPOLLOUT, .data.ptr = c };
  epoll_ctl(epoll_fd, EPOLL_CTL_MOD, c->conn_fd, &ev);
}
```

epoll.c

We don’t actually write anything yet because the connection is not necessarily ready for writes. That will happen next in `on_writable`, where we actually read the file (which again epoll won’t help us with) and write until we’re told the write would block (which happens because we previously set the *connection* to non-blocking).

```
static void on_writable(struct conn *c) {
  for (;;) {
    if (c->out_offset >= c->out_len) {
      if (c->file_eof) {
        conn_close(c);
        return;
      }

      ssize_t r = read(c->file_fd, c->out, sizeof(c->out));
      if (r <= 0) {
        conn_close(c);
        return;
      }

      c->out_offset = 0;
      c->out_len = (size_t)r;
    }
    ssize_t w = write(c->conn_fd, c->out + c->out_offset, c->out_len - c->out_offset);
    if (w < 0) {
      if (errno == EAGAIN || errno == EWOULDBLOCK)
        return;

      conn_close(c);
      return;
    }
    c->out_offset += (size_t)w;
  }
}
```

epoll.c

And lastly helpers, globals, structs, and includes.

```
#include "common.h"
#include <sys/epoll.h>

struct conn {
  int conn_fd;
  int file_fd;

  char req[MAX_REQ_BUF];
  size_t req_offset;

  char out[IO_BUF];
  size_t out_offset, out_len;
  int file_eof;
};

static int epoll_fd;

static void conn_close(struct conn *c) {
  epoll_ctl(epoll_fd, EPOLL_CTL_DEL, c->conn_fd, NULL);
  close(c->conn_fd);
  if (c->file_fd >= 0)
    close(c->file_fd);

  free(c);
}
```

epoll.c

Compile it and try it out.

```
clang epoll.c -o epoll_file_server
./epoll_file_server &
curl localhost:8080/common.h
kill %1
```

Now let’s check out io\_uring.

## io\_uring

In epoll we do the I/O ourselves when epoll tells us the file descriptor is *ready*. With io\_uring we submit a chunk of I/O requests to the kernel to do for us and we receive completion events back as I/O *completes*. Usually completion events are 1:1 with submission queue entries, but “multishot” submissions are a way to request the I/O to keep happening indefinitely, with a new completion happening each time.

io\_uring has the lovely advantage that it works not just on “blocking” file descriptors like network sockets but even for files on disk.

Let’s look at the io\_uring file server implementation, starting at the bottom. We’ll use the multishot feature for submitting a single request for `accept` s to happen on our socket file descriptor, so io\_uring will keep `accept` -ing new connections for us as they come in, indefinitely. And we’ll store a callback and argument pointer in the submission event’s user data field so we can know how to deal with its completion event.

```
int main(int argc, char **argv) {
    uint16_t port = (argc > 1) ? (uint16_t)atoi(argv[1]) : 8080;
    listen_fd = listen_socket(port);

    struct io_uring ring;
    if (io_uring_queue_init(256, &ring, 0) < 0) {
        perror("queue_init");
        return 1;
    }
    fprintf(stderr, "uring server on :%u\n", port);

    io_uring_prep_multishot_accept(sqe_with_cb(&ring, on_accept, NULL),
                                   listen_fd, NULL, NULL, 0);
    for (;;) {
        io_uring_submit_and_wait(&ring, 1);

        struct io_uring_cqe *cqe;
        unsigned head, count = 0;
        io_uring_for_each_cqe(&ring, head, cqe) {
            struct cb_ctx *ctx = io_uring_cqe_get_data(cqe);
            ctx->cb(ctx->ring, cqe, ctx->ud);
            // F_MORE here implies multishot, so don't free the context.
            if (!(cqe->flags & IORING_CQE_F_MORE))
                free(ctx);
            count++;
        }
        io_uring_cq_advance(&ring, count);
    }
}
```

uring.c

Since we can submit all kinds of I/O to io\_uring and since io\_uring won't itself tell us the type of a completion event, we will encode a callback in io\_uring's opaque user data field so we can know what to do with the completion event. The user data is passed by the user in the submission event and passed back to the user by the kernel in the completion event.

Again, like epoll, the architecture is fully event-driven.

Let’s take a look at how we prepare submissions for io\_uring in `sqe_with_cb`. We grab an io\_uring submission queue entry, allocate a context with our callback and user data, and assign the context as data to the entry.

```
static struct io_uring_sqe *sqe_with_cb(struct io_uring *ring, ev_cb cb, void *ud) {
  struct io_uring_sqe *sqe = io_uring_get_sqe(ring);
  if (!sqe) {
    io_uring_submit(ring);
    sqe = io_uring_get_sqe(ring);
  }
  struct cb_ctx *ctx = malloc(sizeof(*ctx));
  ctx->cb = cb;
  ctx->ud = ud;
  ctx->ring = ring;
  io_uring_sqe_set_data(sqe, ctx);
  return sqe;
}
```

uring.c

This context is freed in the loop in `main`.

In `main` we also kicked off the process by scheduling `accept`:

```
io_uring_prep_multishot_accept(sqe_with_cb(&ring, on_accept, NULL),
                               listen_fd, NULL, NULL, 0);
```

So let’s look at the `on_accept` callback. In most cases it is solely a matter of assigning the connection to the context and scheduling `recv` with io\_uring. But occasionally we also need to restart the `accept` multishot process itself.

```
static void on_accept(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  (void)ud;
  // Submit additional accept multishot if F_MORE is clear.
  if (!(cqe->flags & IORING_CQE_F_MORE))
    io_uring_prep_multishot_accept(sqe_with_cb(ring, on_accept, NULL),
                                   listen_fd, NULL, NULL, 0);

  if (cqe->res < 0)
    return;

  struct conn *c = calloc(1, sizeof(*c));
  c->conn_fd = cqe->res;
  c->file_fd = -1;
  io_uring_prep_recv(sqe_with_cb(ring, on_recv, c),
                     c->conn_fd, c->req, sizeof(c->req), 0);
}
```

uring.c

Importantly, in the last line where we schedule the `recv`, we tell io\_uring to put the data from the `recv` into `c->req`.

Next up let’s look at the `on_recv` callback we register. The data from the `recv` will already be in `c->req` so we just need to check the completion event’s `res` field which contains the length of the data read by `recv`. If it’s negative (error), or too large, we schedule the connection to be closed. If we reached the end of the header section we switch to handling the response, otherwise we schedule `recv` again.

```
static void on_recv(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  struct conn *c = ud;
  if (cqe->res <= 0) {
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
    return;
  }

  c->req_offset += (size_t)cqe->res;
  if (memmem(c->req, c->req_offset, "\r\n\r\n", 4))
    start_response(ring, c);
  else if (c->req_offset >= sizeof(c->req))
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
  else
    io_uring_prep_recv(sqe_with_cb(ring, on_recv, c),
                       c->conn_fd, c->req + c->req_offset,
                       sizeof(c->req) - c->req_offset, 0);
}
```

uring.c

The `on_close` callback is just cleanup.

```
static void on_close(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  (void)ring;
  (void)cqe;
  struct conn *c = ud;
  if (c->file_fd >= 0)
    close(c->file_fd);

  free(c);
}
```

uring.c

So next let’s look at `start_response`. This simply parses the request (since we’ve called `recv` already until we read all headers), writes response headers into our context buffer (`c->headers`), and schedules a `send` of this buffer back to the client. If the file is valid we also open it but we won’t start reading it until after we write headers.

```
static void start_response(struct io_uring *ring, struct conn *c) {
  char path[1024];
  int rc = parse_http_get(c->req, c->req_offset, path, sizeof(path));
  if (rc < 0) {
    c->headers_len = build_404(c->headers, sizeof(c->headers));
    c->file_eof = 1;
    io_uring_prep_send(sqe_with_cb(ring, on_write_headers, c),
                       c->conn_fd, c->headers, c->headers_len, 0);
    return;
  }

  char full[2048];
  snprintf(full, sizeof(full), "%s%s", DOCROOT, path);
  c->file_fd = open(full, O_RDONLY);
  if (c->file_fd < 0) {
    c->headers_len = build_404(c->headers, sizeof(c->headers));
    c->file_eof = 1;
  } else {
    c->headers_len = build_ok_headers(c->headers, sizeof(c->headers), mime_for(path));
  }
  io_uring_prep_send(sqe_with_cb(ring, on_write_headers, c),
                     c->conn_fd, c->headers, c->headers_len, 0);
}
```

uring.c

Inside `on_write_headers`, we’ll keep scheduling more writes of headers and then we’ll start scheduling reads of the file we’re sending back to the client.

```
static void on_write_headers(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  struct conn *c = ud;
  if (cqe->res <= 0) {
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
    return;
  }

  c->headers_offset += (size_t)cqe->res;
  if (c->headers_offset < c->headers_len) {
    io_uring_prep_send(sqe_with_cb(ring, on_write_headers, c),
                       c->conn_fd, c->headers + c->headers_offset,
                       c->headers_len - c->headers_offset, 0);
    return;
  }
  if (c->file_eof) {
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
    return;
  }
  io_uring_prep_read(sqe_with_cb(ring, on_read_file, c),
                     c->file_fd, c->buf, sizeof(c->buf), -1);
}
```

uring.c

In `on_read_file` we schedule the buffer we read to be sent back to the client.

```
static void on_read_file(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  struct conn *c = ud;
  if (cqe->res <= 0) {
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
    return;
  }

  c->buf_len = (size_t)cqe->res;
  c->buf_offset = 0;
  io_uring_prep_send(sqe_with_cb(ring, on_write_file, c),
                     c->conn_fd, c->buf, c->buf_len, 0);
}
```

uring.c

In `on_write_file` we schedule more reads.

```
static void on_write_file(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud) {
  struct conn *c = ud;
  if (cqe->res <= 0) {
    io_uring_prep_close(sqe_with_cb(ring, on_close, c), c->conn_fd);
    return;
  }

  c->buf_offset += (size_t)cqe->res;
  if (c->buf_offset < c->buf_len) {
    io_uring_prep_send(sqe_with_cb(ring, on_write_file, c),
                       c->conn_fd, c->buf + c->buf_offset,
                       c->buf_len - c->buf_offset, 0);
    return;
  }
  io_uring_prep_read(sqe_with_cb(ring, on_read_file, c),
                     c->file_fd, c->buf, sizeof(c->buf), -1);
}
```

uring.c

Which leaves us with just type and forward declarations and includes.

```
#include "common.h"
#include <liburing.h>

typedef void (*ev_cb)(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud);

struct cb_ctx {
  ev_cb cb;
  void *ud;
  struct io_uring *ring;
};

struct conn {
  int conn_fd;
  int file_fd;

  char req[MAX_REQ_BUF];
  size_t req_offset;

  char headers[512];
  size_t headers_len, headers_offset;

  char buf[IO_BUF];
  size_t buf_len, buf_offset;

  int file_eof;
};

static int listen_fd;

static struct io_uring_sqe *sqe_with_cb(struct io_uring *ring, ev_cb cb, void *ud);
static void on_write_file(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud);
static void on_close(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud);
static void on_read_file(struct io_uring *ring, struct io_uring_cqe *cqe, void *ud);
```

uring.c

Build it and run.

```
sudo apt-get update -y && sudo apt-get install liburing-dev
clang uring.c -o uring_file_server -luring
./uring_file_server &
curl localhost:8080/common.h
kill %1
```

Cool! But now let’s take a step back.

### The ring

We’re adding events to a ring-buffer… ring-buffers are usually a fixed size. What happens if we run out of space?

We omitted checking it but if `io_uring_get_sqe()` ever returns `NULL`, we’re out of space. We could handle this situation by keeping an in-memory list of io\_uring requests that need to be scheduled. In the loop in `main` we first schedule any pending requests before scheduling new ones.

## Why use io\_uring?

io\_uring is pretty exciting. It handles disk I/O unlike epoll, making it more of a universal API. It also reduces the cost of each I/O operation we do because rather than doing N syscalls directly, we batch up to `$QUEUE_DEPTH` syscalls into a single io\_uring submit syscall.

We’d expect applications to perform better than epoll on disk I/O since our user threads will not be blocked while it’s happening. We could offload disk I/O to worker threads in an epoll implementation to get similar performance, but io\_uring assures us our own thread won’t block without that extra work. (Even though it might also be using kernel worker threads under the hood.)

We’d expect that applications with higher concurrency and more clients perform better with io\_uring with its ability to batch and multiplex I/O. Whereas at lower concurrency levels and fewer clients, or if you cannot find a way to batch I/O, we’d expect to see few advantages.

Even in the case of low concurrency, the universality of io\_uring makes it a compelling default.

In another article we’ll have to look at both who has prohibited the use of io\_uring ([Google](https://i.blackhat.com/BH-US-23/Presentations/US-23-Lin-bad_io_uring.pdf?from_theconsensus=1) \[slide 10\], [Docker by default](https://github.com/docker/for-mac/issues/7707?from_theconsensus=1#issuecomment-3012477323)) and who still uses io\_uring anyway (Postgres, though [not by default](https://www.postgresql.org/docs/18/runtime-config-resource.html?from_theconsensus=1#GUC-IO-METHOD)). The story is not simple and worth looking more closely at.