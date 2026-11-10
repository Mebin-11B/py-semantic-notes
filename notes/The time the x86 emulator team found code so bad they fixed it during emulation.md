---
title: "The time the x86 emulator team found code so bad they fixed it during emulation"
url: https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419
clipped: 2026-06-17 00:42:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The time the x86 emulator team found code so bad they fixed it during emulation](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419)

## Digest Summary
During Windows’ era of an x86‑32 processor emulator that used binary translation (JIT‑style code generation), the team encountered a function that allocated ~64 KB on the stack and zero‑filled it. The compiler handling that function unrolled the initialization loop, emitting 65,536 separate “store byte” instructions—each 4 bytes—resulting in ~256 KB of generated code to initialize 64 KB of data. The emulator’s translators detected this pathological pattern and replaced it with a compact loop that performed the same initialization, restoring expected performance and code size. This incident illustrates how aggressive loop‑unrolling optimizations can produce inefficient code for large memory operations, prompting runtime systems to add corrective translation logic.

## Discussion Summary
The discussion references historical compiler behavior, suggesting that past optimization flags could unconditionally unroll loops, while questioning why modern compilers would support such options. It notes that current compatibility layers like Proton and Wine can apply hot‑fixes to improve game performance, contrasting this with earlier patches that addressed bugs directly in the operating system rather than requiring developers to ship fixes. Anecdotes about architecture support and specialized translator optimizations are mentioned, alongside the idea of disabling problematic optimizations for specific code sections.

---

## Full Article

During an exchange of war stories, a colleague of mine told one from back in the days when Windows included a processor emulator for x86-32 on systems that natively ran some other processor. (This has happened many times. And no, I don’t know which processor this particular story applied to.)

This particular emulator employed binary translation, generating native code to perform the equivalent operations of the original x86-32 code. This offered a significant performance improvement over emulation via interpreter. You can imagine that x86-32 is just a bytecode, and the emulator is a JIT compiler.

Anyway, my colleague found that there was one program that needed to allocate around 64KB of memory on the stack and initialize it. The standard way of doing this is to  [perform a stack probe to ensure that 64KB of memory is available](https://devblogs.microsoft.com/oldnewthing/20260311-00/?p=112134 "How do compilers ensure that large stack allocations do not skip over the guard page?"), then subtracting 65536 from the stack pointer, and then initializing the memory in a small, tight loop.

But using a loop to initialize the memory was too mundane for whatever compiler was used to compile this code. Instead of generating a loop to initialize each byte of the buffer, the compiler “optimized” the code by unrolling the loop into 65,536 individual “write byte to memory” instructions, each 4 bytes long.

All in all, it took this program 256 kilobytes of code to initialize 64 kilobytes of data.

This offended the team so much that they added special code to the translator to detect this horrible function and replace it with the equivalent tight loop.