---
title: "A Erlang style pure Scheme Webserver and further"
url: https://igropyr.com
clipped: 2026-08-31 12:22:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A Erlang style pure Scheme Webserver and further](https://igropyr.com)

## Digest Summary
Igropyr is a fault‑tolerant web server written entirely in Chez Scheme, separating a minimal core (exposed via `http‑listen`) from an optional Express‑like layer (`create‑app`, `app‑get`, `send‑json!`). It runs thousands of lightweight green processes on a single OS thread, using continuation‑based preemptive scheduling; processes communicate via pure message passing (`spawn`, `send`, `receive`, `link`, `monitor`) with no shared state. A fixed worker pool under a supervisor automatically restarts crashed workers and retries tasks up to three times, killing workers stalled >30 s. Failure hooks can return structured JSON instead of plain 500 responses.

Key features include:
- Per‑dialogue green processes that preserve state across multi‑request conversations, with guaranteed rollback on crash or TTL.
- Hot code swapping of handlers/routes without dropping connections.
- WebSocket (RFC 6455) support, streaming/SSE via `res‑begin!`/`res‑write!`/`res‑end!`, and a full OTP‑style toolkit (`gen‑server`, process registry, PubSub).
- Robust JSON parser/writer, form and cookie handling, middleware suite (sessions, CORS, security headers, access logging).
- Non‑blocking Redis/MySQL clients, outbound HTTP/WebSocket clients, async file reads via libuv, gzip compression, transparent chunked decoding.
- Rate limiting, global error handling, Prometheus metrics (`/metrics`), runtime introspection (`http‑stats`), graceful shutdown, and multi‑process scaling via `SO_REUSEPORT`. Benchmarks report ≈35 k req/s at 500 concurrent connections on an Apple Silicon laptop.

---

## Full Article

λ

# Igropyr

Origins

The Igropyr project contains two parts: [Igropyr](https://igropyr.dev) on the backend, and [Goeteia](https://goeteia.dev) in the browser.

I started Igropyr back in 2018 simply because I wanted to write Scheme. I was hunting for a modern, production-ready Scheme web server—something that wasn't just an academic toy—and came up completely empty. Even now, most Scheme web servers still treat HTTP like glorified string concatenation. They're missing all the baseline stuff a real backend needs today: proper JSON handling, real concurrency, async I/O.

So I hacked something together. I tried Apache with CGI for a bit, then looked at Node and wrote a thin wrapper over libuv. That was the first real prototype.

Later on, I fell down the Erlang rabbit hole and got hooked on its philosophy: message passing and let it crash. Around that time, Swish came out with an Erlang-style system on top of Chez Scheme. It was brilliant, but its network layer was still stuck in that primitive string-building era. Still, Swish was the push I needed. It convinced me to tear Igropyr down and rebuild it from scratch.

Today's Igropyr goes a lot further. If a handler crashes or times out, it doesn't just silently drop the connection; it tells the client exactly what went wrong and hands back the steering wheel. The client can retry, tweak parameters, or bail out. In practice, this hides server-side hiccups from the user and cuts down wait times. Better yet, it talks natively in s-expressions. When both ends speak Scheme, you don't need a codec. Data just crosses the wire exactly as it is, down to the exact integers. Scheme finally has its own JSON.

It actually pulled off continuation-based web programming, too—that old pipe dream of the functional programming world. You wouldn't use it for a simple web form, but for strictly transactional flows? It's magic. A single transaction can stretch right across the wire, parked and waiting between the server and the client. At this point, it's packed with what you'd expect from a modern backend: JWT, non-blocking DB and Redis clients, auto-clustering, hot code swapping, and even BLAS-accelerated vector search.

Then there's Goeteia, which came from the itch to write the frontend in pure Scheme, too. I messed around with Scheme-to-JS compilers at first, but targeting WebAssembly ended up being the real answer. And I didn't even lose JS support in the process: the compiler spits out both from the same source. If a browser is too old for Wasm GC, it gracefully falls back to a generated JS twin. You never have to manually sync them.

The Goeteia compiler itself is a tiny 50kB footprint that runs directly in the browser, heavily dialed in for 3D. It can render heavy web effects on the fly straight from Scheme, or precompile them if you need raw speed and game-level performance. I also took a weird, distinctly Scheme approach to the DOM. Instead of a heavy virtual DOM tree, it uses macro-based state management and pretext effects.

Lately, Goeteia has kind of outgrown its original scope. Because everything about it is so small and fast—compiles take milliseconds, and testing logic requires zero GPU overhead, just pure math—you can run a ton of instances side by side. I'm currently using it to drive highly concurrent AI pipelines. You feed it video footage, and it extracts the skeleton, textures, skinning, and motion data. Stuff that used to require a mocap suit and a soundstage now just needs a raw video file.

AI is already great at generating reference art, turntables, and motion video. The missing link was getting from those pixels to actual, usable 3D assets. Goeteia is that last piece of the puzzle. Like any AI workflow, it's not a one-shot process; it loops, tweaking and converging on the target until the code decides it's right.

Both parts of this project are fully open source and free for anything, including commercial use. Have fun with it.
