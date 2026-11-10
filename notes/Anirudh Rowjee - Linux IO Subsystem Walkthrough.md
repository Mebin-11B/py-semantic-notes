---
title: "Anirudh Rowjee - Linux IO Subsystem Walkthrough"
source: "https://rowjee.com/blog/linux_io_subsystem_walkthrough"
author:
published:
created: 2026-06-01
description:
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Operating Systems
  - Linux Kernel
  - Virtual File System
  - Page Cache
  - Block Layer
  - I/O Scheduling
related:
  - "Operating Systems"
  - "Serving files over HTTP three ways synchronous, epoll, and io_uring.md"
  - "When idle isn't idle how a Linux kernel optimization became a QUIC bug.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A detailed technical walkthrough of the Linux I/O subsystem, trace-inspecting the path of file operations from system calls through the Virtual File System (VFS), page cache, block layer, and device drivers.
>
> **Key points:**
> - Traces standard library calls like fopen to the under-the-hood Linux kernel system calls (open, read, write).
> - Explains the role of the Virtual File System (VFS) as an abstraction layer providing a uniform API for different physical filesystems like ext4 or xfs.
> - Details filesystem metadata structures in Linux, highlighting how inodes store file metadata and data block pointers, while dentries map paths to inodes.
> - Discusses caching and storage layout mechanisms, including the page cache, block layers, I/O schedulers, and device drivers that interface with physical hardware.
>
> **Concept links:** [[Operating Systems]], [[Linux Kernel]], [[Virtual File System]], [[Page Cache]], [[Block Layer]], [[I/O Scheduling]]
>
> **Suggested connections:**
> - [[Operating Systems]] — provides the core context for kernel resource management and abstractions.
> - [[Serving files over HTTP three ways synchronous, epoll, and io_uring.md]] — connects block-level I/O to higher-level network I/O subsystems and asynchronous handling.
> - [[When idle isn't idle how a Linux kernel optimization became a QUIC bug.md]] — shows another detailed look at Linux kernel optimization behaviors and bug tracing.
<!-- ai-summary:end -->

![](https://www.thomas-krenn.com/en/wikiEN/images/d/d1/Linux-storage-stack-diagram_v6.18.png)

This post hopes to walk through some basics of how IO works in Linux. For now, we'll only be considering the interaction of applications with block-based Filesystems, and how they interact with the rest of the subsystems beneath them, more specifically the Block Layer, the Block IO Scheduler, and the request-based device drivers.

The goal here is for both me, and you, dear reader, to understand how the IO subsystem works. To write this post, I will be using two primary sources of information on how this works:

1. Other blog posts and articles about how the IO subsystem works, including, but not limited to, kernel documentation
2. A debugging session that'll trace through what actually goes on when we `open`, `read`, and `write` a file.

Roughly, this is what we're looking at for this blog post.

```
#mermaid-1780253919193{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1780253919193 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1780253919193 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1780253919193 .error-icon{fill:#552222;}#mermaid-1780253919193 .error-text{fill:#552222;stroke:#552222;}#mermaid-1780253919193 .edge-thickness-normal{stroke-width:1px;}#mermaid-1780253919193 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1780253919193 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1780253919193 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1780253919193 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1780253919193 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1780253919193 .marker{fill:#333333;stroke:#333333;}#mermaid-1780253919193 .marker.cross{stroke:#333333;}#mermaid-1780253919193 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1780253919193 p{margin:0;}#mermaid-1780253919193 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#mermaid-1780253919193 .cluster-label text{fill:#333;}#mermaid-1780253919193 .cluster-label span{color:#333;}#mermaid-1780253919193 .cluster-label span p{background-color:transparent;}#mermaid-1780253919193 .label text,#mermaid-1780253919193 span{fill:#333;color:#333;}#mermaid-1780253919193 .node rect,#mermaid-1780253919193 .node circle,#mermaid-1780253919193 .node ellipse,#mermaid-1780253919193 .node polygon,#mermaid-1780253919193 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1780253919193 .rough-node .label text,#mermaid-1780253919193 .node .label text,#mermaid-1780253919193 .image-shape .label,#mermaid-1780253919193 .icon-shape .label{text-anchor:middle;}#mermaid-1780253919193 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1780253919193 .rough-node .label,#mermaid-1780253919193 .node .label,#mermaid-1780253919193 .image-shape .label,#mermaid-1780253919193 .icon-shape .label{text-align:center;}#mermaid-1780253919193 .node.clickable{cursor:pointer;}#mermaid-1780253919193 .root .anchor path{fill:#333333!important;stroke-width:0;stroke:#333333;}#mermaid-1780253919193 .arrowheadPath{fill:#333333;}#mermaid-1780253919193 .edgePath .path{stroke:#333333;stroke-width:1px;}#mermaid-1780253919193 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1780253919193 .edgeLabel{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1780253919193 .edgeLabel p{background-color:rgba(232,232,232, 0.8);}#mermaid-1780253919193 .edgeLabel rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1780253919193 .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#mermaid-1780253919193 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1780253919193 .cluster text{fill:#333;}#mermaid-1780253919193 .cluster span{color:#333;}#mermaid-1780253919193 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1780253919193 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-1780253919193 rect.text{fill:none;stroke-width:0;}#mermaid-1780253919193 .icon-shape,#mermaid-1780253919193 .image-shape{background-color:rgba(232,232,232, 0.8);text-align:center;}#mermaid-1780253919193 .icon-shape p,#mermaid-1780253919193 .image-shape p{background-color:rgba(232,232,232, 0.8);padding:2px;}#mermaid-1780253919193 .icon-shape .label rect,#mermaid-1780253919193 .image-shape .label rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#mermaid-1780253919193 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1780253919193 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1780253919193 .node .neo-node{stroke:#9370DB;}#mermaid-1780253919193 [data-look="neo"].node rect,#mermaid-1780253919193 [data-look="neo"].cluster rect,#mermaid-1780253919193 [data-look="neo"].node polygon{stroke:#9370DB;filter:drop-shadow(1px 2px 2px rgba(185, 185, 185, 1));}#mermaid-1780253919193 [data-look="neo"].node path{stroke:#9370DB;stroke-width:1px;}#mermaid-1780253919193 [data-look="neo"].node .outer-path{filter:drop-shadow(1px 2px 2px rgba(185, 185, 185, 1));}#mermaid-1780253919193 [data-look="neo"].node .neo-line path{stroke:#9370DB;filter:none;}#mermaid-1780253919193 [data-look="neo"].node circle{stroke:#9370DB;filter:drop-shadow(1px 2px 2px rgba(185, 185, 185, 1));}#mermaid-1780253919193 [data-look="neo"].node circle .state-start{fill:#000000;}#mermaid-1780253919193 [data-look="neo"].icon-shape .icon{fill:#9370DB;filter:drop-shadow(1px 2px 2px rgba(185, 185, 185, 1));}#mermaid-1780253919193 [data-look="neo"].icon-shape .icon-neo path{stroke:#9370DB;filter:drop-shadow(1px 2px 2px rgba(185, 185, 185, 1));}#mermaid-1780253919193 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}read(2), write(2), open(2), chmod(2)ApplicationVFS LayerBlock-based FS ext4Block Layer with IO SchedulerRequest-Based Disk Driver
```

## Design constraints faced by the kernel

Let's consider for a moment that the kernel's job is to make a finite amount of resources (files, memory, CPU) appear as though it's infinite. To this end, the kernel will need to wrap many of the underlying subsystems in abstractions to maintain the "illusion of infinity". For example, the application doesn't know that the memory layout exists a certain way in the actual hardware; it simply assumes that the memory it asks for is given to it, with a far more limited error handling surface than the kernel actually has to deal with.

The point I'm trying to make is that underneath every seemingly simple operation there's a lot of complexity. The application doesn't (and need not) know how all the files on disk are organized relative to each other; it should simply be able to ask to read a file and get it.

## System Calls

How does a program make something happen on the host computer? For example, while it is reasonable for us to expect a program to be able to work on its unique functionality, some actions (such as allocating memory, reading/writing from/to files on disk, displaying an image on the monitor) are left in the hands of the Kernel, whose sole function is to perform these duties. This is accomplished by exposing various kernel APIs to the programs, so that when the program wishes to, say, allocate some memory, it can "ask" or "call into" the kernel to do so.

This is known as a system call, or a syscall. These are specialized types of functions that don't exist in the application source code, but are instead run by the kernel. If you've programmed in C before, there's a good chance you've directly used some of these syscalls before - remember `malloc`?

(more about how system calls work here, if patience permits)

Now, why are system calls important? Doing IO is something we must ask the kernel to do for us, which is why every IO operation happens via a syscall. `open`, `read`, `write` are all syscalls.

## Some code

Even in C, we'll usually access these syscalls via a standard library of some sort. Here, it's `stdio.h`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  FILE *myfile = NULL;
  myfile = fopen("hello.txt", "w+"); // <- HERE
  // elided error handling

  char *text = "hello, world!\0";
  size_t stat = 0;

  stat = fwrite(text, sizeof(char), 14, myfile);
  // elided error handling

  // read the same data
  char *newdata = malloc(sizeof(char) * 14);
  // elided error handling

  fseek(myfile, 0, SEEK_SET);

  stat = fread(newdata, sizeof(char), 14, myfile);
  // elided error handling

  size_t cmpres = strncmp(newdata, text, 14);
  // elided error handling

  free(newdata);
  return 0;
}
```

In the first part that we're concerned about, we'll look at the `FILE` object, which points to a file descriptor under the hood.

```c
FILE *myfile = NULL;
myfile = fopen("hello.txt", "w+"); // <- HERE
```

When we call `fopen`, the IO library `stdio` does the following:

~~I'm currently on MacOS, so here's the source to apple libc's implementation of `fopen`: [https://github.com/apple-open-source-mirror/Libc/blob/5e566be7a7047360adfb35ffc44c6a019a854bea/stdio/FreeBSD/fopen.c#L60](https://github.com/apple-open-source-mirror/Libc/blob/5e566be7a7047360adfb35ffc44c6a019a854bea/stdio/FreeBSD/fopen.c#L60) ~~

I feel it'll be better to trace the code via `glibc` so we can see what's going on in Linux, not FreeBSD.

[https://github.com/torvalds/linux/blob/32a92f8c89326985e05dce8b22d3f0aa07a3e1bd/fs/open.c#L1076](https://github.com/torvalds/linux/blob/32a92f8c89326985e05dce8b22d3f0aa07a3e1bd/fs/open.c#L1076) `vfs_open`

here we first see that we set the path of the new file struct to the path passed in, and then we call into `do_dentry_open`.

do\_dentry\_open - this seems like where most of the work is happening: [https://github.com/torvalds/linux/blob/32a92f8c89326985e05dce8b22d3f0aa07a3e1bd/fs/open.c#L887](https://github.com/torvalds/linux/blob/32a92f8c89326985e05dce8b22d3f0aa07a3e1bd/fs/open.c#L887)

## The VFS Layer

> A file system is an organization of data and metadata on a storage device. With a vague definition like that, you know that the code required to support this will be interesting.
> 
> *" [Anatomy of the Linux File System](https://developer.ibm.com/tutorials/l-linux-filesystem/) " by M. Tim Jones*

The bit of software that manages how the data is physically laid out on disk - i.e. which bits in a file map to which physical locations on disk - is called the **Filesystem**. You may have heard of multiple filesystems like `xfs`, `ext4`, `btrfs`, and so on. All of these filesystems have their own way of representing your files physically. The Linux Kernel provides an abstraction called the VFS to ensure that applications need only one codepath for the Virtual File System (VFS) layer, while the VFS calls into the underlying filesystems. the VFS layer implements multiple syscalls such as `open`, `stat`, `read`, `write`, and `chmod` [^1].

The VFS layer also contains two caches, one for `dentry` s and one for `inode` s. What are `dentry` and `inode`? Both are filesystem objects used to represent items present in the filesystem.

### inode

An Inode represents a file on the disk (We need to keep in mind that in linux, directories are files too, just special kinds of files). They store metadata about a file, as well as the locations of the disk blocks that make up the file. The inodes are stored on the disk. They notably do not contain the filename. Each inode has an inode number, which is unique within a filesystem.

The inode contains (by a number of means) a list of disk block locations that comprise the file. An important point to consider is that the same way the inode for a file points to other (data) blocks on disk, the inode structure can be reused to be a directory that points to multiple other inode blocks on disk.

[https://www.linfo.org/inode.html](https://www.linfo.org/inode.html)

### dentry

so, given that we don't have filenames defined yet, and directories are just files, how do we figure out what our filesystem looks like? The answer to this is the `dentry`. These are in-memory objects that are created on boot by the kernel walking the filesystem, which map directories to paths, such that if you would like to look at all the folders on your disk, you simply need to look at all the dentries in memory.

So, the VFS layer caches both inodes and dentries. This allows us to speed up a number of operations on disk.

is there a buffer cache as well?

## The Filesystem

The filesystem determines how data is ultimately organized on disk and how it's updated. It follows that the type of filesystem you use (and its many features) will end up determining application performance and other run-time characteristics. Some common filesystems that are used today are `ext3`, `ext4`, `xfs` and `btrfs`.

Each filesystem has a **superblock** which has a list of all the inodes present on the filesystem. This superblock is usually located at exactly the same location in every partition/disk.

[https://blogs.oracle.com/linux/understanding-ext4-disk-layout-part-1](https://blogs.oracle.com/linux/understanding-ext4-disk-layout-part-1) GDT? BDT?

## The Block Layer

The linux kernel must manage many block devices. It is possible for a physical disk to have multiple partitions (each can be considered a disk in its own right), each with its own partition on it - this means that though there's a very real hardware bottleneck that exists in the bandwidth of the disk, the kernel must schedule block IO in such a way that the bandwidth of the disk is distributed "Fairly". To that end, there are also multiple IO Schedulers that exist to manage all the inflow of IO onto the disk. Some schedulers are the `kyber` scheduler, `mq` scheduler, and `deadline` scheduler. [https://www.cs.cornell.edu/courses/cs4410/2021fa/assets/material/lecture24\_blk\_layer.pdf](https://www.cs.cornell.edu/courses/cs4410/2021fa/assets/material/lecture24_blk_layer.pdf)

BIOs -> Block IOs

what is the device mapper?

\[superblock \]\[inode section\]\[data section\]

[^1]: [https://www.kernel.org/doc/html/latest/filesystems/vfs.html#introduction](https://www.kernel.org/doc/html/latest/filesystems/vfs.html#introduction)