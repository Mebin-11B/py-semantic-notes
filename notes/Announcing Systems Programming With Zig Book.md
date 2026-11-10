---
title: "Announcing Systems Programming With Zig Book"
source: "https://www.mtsoukalos.eu/2026/06/announcing-systems-programming-with-zig-book/"
author:
  - "[[Mihalis Tsoukalos]]"
published: 2026-06-17
created: 2026-06-19
description: "After months of writing, breaking changes in Zig, reviewing and refining, I am delighted to announce the publication of Systems Programming with Zig — a hands-on guide to building real-world systems software using the Zig programming language.  What the book is about          Link to heading  This is not an introduction to Zig syntax. The book assumes you already know how to write Zig code and picks up from there, putting the language to work on the kind of problems that systems programmers face every day: process management, filesystem interaction, network services, concurrent data structures, asynchronous I/O, database integration and language implementation."
tags:
  - "clippings"
---
After months of writing, breaking changes in Zig, reviewing and refining, I am delighted to announce the publication of *Systems Programming with Zig* — a hands-on guide to building real-world systems software using the Zig programming language.

## What the book is about

This is not an introduction to Zig syntax. The book assumes you already know how to write Zig code and picks up from there, putting the language to work on the kind of problems that systems programmers face every day: process management, filesystem interaction, network services, concurrent data structures, asynchronous I/O, database integration and language implementation.

Every chapter builds something real. By the time you reach the last page, you will have written UNIX command-line tools, TCP and UDP servers, a file indexer, an in-memory cache server, a note-taking service backed by SQLite3 and a working interpreter for a small programming language — all in Zig.

The book covers Zig 0.16 throughout and pays particular attention to the new `std.Io` API, the async and await model introduced in that release and the practical implications of Zig’s explicit memory management model for systems-level design.

## Who it is for

The book is written for software developers, systems programmers, UNIX engineers and backend engineers who already understand Zig fundamentals and want to build production-grade systems software. Familiarity with languages such as C, C++, Rust, Go or Python will help you get the most from it.

## Chapter overview

The twelve chapters form a deliberate progression — from foundational tooling through networking, concurrency and asynchronous I/O to database integration and language design.

**Chapter 1 — Building Essential UNIX Tools** Builds three real UNIX utilities from day one: a `tee(1)` clone, a `which(1)` clone and a program that calls C code directly via `@cImport()`.

**Chapter 2 — Systems Infrastructure: Builds, Testing and Distribution** Treats `build.zig` as a first-class systems programming concern. Covers memory allocators, unit testing, `std.fmt` and Zig package publishing.

**Chapter 3 — Direct Memory Access and Binary Formats** Digs into pointer arithmetic, custom allocators, endianness and binary file parsing, culminating in `zunzip`, a Zip file lister built from raw bytes.

**Chapter 4 — Processing Streams, Buffers and Data Encoding** Examines I/O efficiency through `zcat`, `zwc` and `z64`, covering buffering strategies, system call costs and SIMD-accelerated data processing.

**Chapter 5 — Navigating Directories and Filesystem Events** Builds `ztree`, a recursive directory visualizer, and `zwatch`, a real-time file monitoring utility backed by `inotify` on Linux and `kqueue` on BSD.

**Chapter 6 — Programming the Network Stack** Works from raw sockets to a complete System Monitor API, building TCP and UDP servers and clients, Docker images and a minimal HTTP service.

**Chapter 7 — Managing Threads, Processes and Signals** Covers UNIX signal handling, `fork(2)`, `execve(2)` and process management, all converging in `zcron`, a minimal `cron(8)` -style job scheduler.

**Chapter 8 — Orchestrating Concurrency and Synchronization** Covers mutexes, atomics, condition variables, thread pools and the Producer-Consumer pattern, culminating in `zlocate`, a concurrent file indexer.

**Chapter 9 — Implementing Asynchronous I/O** Introduces Zig 0.16’s async and await model, builds an asynchronous TCP proxy and examines `io_uring` on Linux and `kqueue` on macOS directly.

**Chapter 10 — Building a High-Performance In-Memory Cache Server** Constructs `zcache`, a non-trivial cache server with an LRU storage engine, a custom binary wire protocol (ZEMP) and a thread-per-connection networking layer.

**Chapter 11 — Persisting Structured Data with SQLite3** Integrates SQLite3 through Zig’s C interoperability layer, building a complete note-taking service with an HTTP API, a CLI client and `comptime` SQL generation.

**Chapter 12 — Developing a Domain Specific Language** Closes the book by building `zcalc`, a small interpreted language with a Lexer, Parser, tree-walking Evaluator and an interactive REPL — a capstone that draws on every technique introduced across the book.

## Source code

All source code from the book is available on GitHub:

[https://github.com/mactsouk/zigSP](https://github.com/mactsouk/zigSP)

Each chapter has its own directory. The code is written for Zig 0.16 and has been tested on macOS and Linux.