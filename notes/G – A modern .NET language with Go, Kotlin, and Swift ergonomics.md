---
title: "G# – A modern .NET language with Go, Kotlin, and Swift ergonomics"
url: https://davidobando.github.io/gsharp/
clipped: 2026-08-31 12:22:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [G# – A modern .NET language with Go, Kotlin, and Swift ergonomics](https://davidobando.github.io/gsharp/)

## Digest Summary
G# is a .NET language designed to incorporate ergonomics from Go, Kotlin, and Swift. It introduces language constructs such as `packages` for modular organization, `func` for function declarations, and `data class` for concise immutable data structures. Nullable types are handled using an `if let` syntax, mirroring Kotlin’s approach to safe null checks. Structured concurrency is supported through a `scope` construct, enabling scoped asynchronous execution similar to Swift’s concurrency model. The language compiles directly to managed .NET assemblies, allowing G# code to run on the existing .NET runtime without additional tooling. Overall, G# aims to provide modern, expressive syntax while leveraging the performance and ecosystem of the .NET platform.

---

## Full Article

[Skip to main content](https://davidobando.github.io/gsharp/#__docusaurus_skipToContent_fallback)

### 

 ``  ``  ``  `` [⚡Modern, familiar syntaxPackages and imports, func declarations, sealed classes and discriminated enums, arrow lambdas, if let nullable handling, and pattern-based switch. Recognisable from Go, Kotlin, Swift, and TypeScript.](https://davidobando.github.io/gsharp/docs/tour)

### 

[🔷Runs on .NETG# compiles straight to managed assemblies and runs on the modern .NET runtime. Import any CLR type, call its methods, and ship a normal executable.](https://davidobando.github.io/gsharp/docs/ref/clr-interop)

### 

 ``  ``  ``  ``  `` [🧵Concurrency built inStructured concurrency with scope, async/await over Task[T], and async sequence[T] async streams. Channels and goroutines ship as an opt-in extension.](https://davidobando.github.io/gsharp/docs/tour/concurrency)

### 

 ``  ``  `` [🔢Precise numeric typesWidth-bearing primitives like int32, uint64, and float64 make the size of every value explicit — no guessing.](https://davidobando.github.io/gsharp/docs/guide/types-and-values)

### 

 `` [🛠️Real toolingA command-line compiler (gsc), an MSBuild SDK, a VS Code extension, a language server, and Portable PDB debugging.](https://davidobando.github.io/gsharp/docs/tooling/gsc)

### 

[📘A complete specificationLearn the language from a single, implementation-grounded specification, plus tutorials and an "Effective G#" idioms guide.](https://davidobando.github.io/gsharp/docs/ref/spec)
