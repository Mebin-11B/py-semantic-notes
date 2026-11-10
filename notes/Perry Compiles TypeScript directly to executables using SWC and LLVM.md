---
title: "Perry Compiles TypeScript directly to executables using SWC and LLVM"
url: https://www.perryts.com/
clipped: 2026-06-17 00:55:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Perry Compiles TypeScript directly to executables using SWC and LLVM](https://www.perryts.com/)

## Digest Summary
Perry v0.5.306 is a TypeScript-to-native compiler that produces GUI and CLI binaries for macOS, iPadOS, iOS, Android, Linux, Windows, watchOS, tvOS, WebAssembly, and the Web. It eliminates runtime dependencies such as Electron, delivering native performance with a generational garbage collector and lazy JSON tape handling, which benchmarks faster than Node.js and Bun on most tests. A single TypeScript codebase can target all supported platforms, generating compact executables (e.g., a 2.3 MB binary for a “Hello, World!” program). The tool is invoked via `perrycompile`, producing ready‑to‑run native files without additional packaging steps.

## Discussion Summary
The remarks express cautious interest in a cross‑platform TypeScript approach while questioning the project's breadth, particularly the inclusion of native UI libraries alongside TypeScript compilation. Concerns are raised about performance trade‑offs of NaN‑boxing, the claim of “no runtime,” and the disparity with C‑level speed demonstrated by Zig. Skepticism also targets the stability of AI‑generated Rust code and the credibility of the project's marketing language, balancing optimism about potential wasm integration with doubts over practicality and execution efficiency.

---

## Full Article

v0.5.1146 â real npm packages now compile: axios, zod, express, fastify, hono

One Codebase. Every Platform. Native Performance.
=================================================

Perry compiles TypeScript to native GUI and CLI apps on macOS, iPadOS, iOS, Android, Linux, Windows, watchOS, tvOS, WebAssembly, and the Web. No runtime. No Electron. Just native binaries.

$ perry compile main.ts

Compiling main.ts...

â Compiled executable: main (2.3 MB)

$ ./main

Hello, World!