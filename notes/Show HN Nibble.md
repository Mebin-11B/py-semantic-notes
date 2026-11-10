---
title: "Show HN: Nibble"
url: https://github.com/glouw/nibble
clipped: 2026-06-17 01:03:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Nibble](https://github.com/glouw/nibble)

## Digest Summary
Nibble is a C‑like systems language implemented in ~3 000 lines of C to showcase LLVM IR generation without heap allocation or external libraries. The compiler emits IR in a single top‑down pass, freely inserting `alloca` instructions—including inside loops—resulting in simpler front‑end code but causing stack‑overflow issues when Clang’s optimizer hoists or expands these allocations. Nibble supports defer statements, recursion, integer, floating‑point, and boolean types, named struct types with GLSL‑style operators, raw pointers, function pointers, conditional branching, loops, static type checking, and basic C interop via generic pointers, all with clear error messages. The repository includes four SDL2‑based graphical demos (two multithreaded shader‑toy ports, a red‑black tree example, and a basic game‑programming setup). Building requires SDL2, Clang, and `make`; Clang compiles `main.c` into the Nibble compiler, which then compiles and runs the demos. The author notes a plan to explore stack‑save/restore mechanisms, but considers the current compiler feature‑complete.

## Discussion Summary
None

---

## Full Article

[![](https://github.com/glouw/nibble/raw/master/img/logo.png)](https://github.com/glouw/nibble/blob/master/img/logo.png)

Nibble is C-like systems programming language.

[![](https://github.com/glouw/nibble/raw/master/img/art.gif)](https://github.com/glouw/nibble/blob/master/img/art.gif)

Nibble was written in 3000 lines of C to demonstrate an approach to LLVM IR
generation without relying on external dependencies or heap allocations.

[![](https://github.com/glouw/nibble/raw/master/img/tree.gif)](https://github.com/glouw/nibble/blob/master/img/tree.gif)

Nibble supports defer, recursion, integer, floating, and boolean types,
structs (simply named types), GLSL-like struct operators, pointers,
function pointers, branching, loops, type checking, basic C interoperability via generic pointers,
and reasonable error messages.

[![](https://github.com/glouw/nibble/raw/master/img/creation.gif)](https://github.com/glouw/nibble/blob/master/img/creation.gif)

Included are these four graphical demos demonstrating Nibble's ability. To try
them out, ensure SDL2 is first installed, as well as Clang, and then run `make`.
Clang will compile `main.c` and output the `nibble` compiler, and `nibble` will
then compile and run the graphical demos. Of these four demos, two demos are multithreaded software renditions
of popular shader-toy demos, one demo is a demonstration of a red-black tree implementation, and the final
demo demonstrates a basic setup for game programming.

[![](https://github.com/glouw/nibble/raw/master/img/chickens.gif)](https://github.com/glouw/nibble/blob/master/img/chickens.gif)

Nibble compiles top down in a single pass and allocas freely, even within loops,
by design. This simplified front-end design greatly improves `main.c` readability but causes
stack overflows with lower (and sometimes even higher) clang back-end optimizations.
I *was* under the impression clang's back-end optimizer would hoist all allocas to a function's top level,
but so we learn in life. I have been meaning to explore stacksave/stackrestore but my LLVM
curiosity has more or less been satisfied, and I deem this compiler momentarily complete.