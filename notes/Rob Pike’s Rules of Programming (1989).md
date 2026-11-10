---
title: "Rob Pike’s Rules of Programming (1989)"
url: https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html
clipped: 2026-06-17 01:30:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Rob Pike’s Rules of Programming (1989)](https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html)

## Digest Summary
Rob Pike’s five programming rules emphasize pragmatic performance and simplicity:  

1. **Unpredictable bottlenecks** – don’t assume where a program will spend time; avoid premature speed hacks.  
2. **Measure before optimizing** – only tune after profiling and when a single part dominates runtime.  
3. **Avoid fancy algorithms for small n** – complex algorithms have large constant factors; use simple approaches unless large inputs are proven.  
4. **Prefer simple algorithms and data structures** – they are less error‑prone and easier to implement.  
5. **Data structures dominate** – well‑chosen structures and organization make algorithms evident; focus on data, not clever algorithms.  

Pike’s first two rules echo Hoare’s “premature optimization is the root of all evil.” Thompson paraphrases rules 3‑4 as “when in doubt, use brute force,” reflecting the KISS principle. Rule 5 parallels Brooks’s advice from *The Mythical Man‑Month*: write straightforward code that leverages robust data abstractions.

## Discussion Summary
The comments converge on strong support for prioritizing good data structures and avoiding premature optimization, especially emphasizing Rule 5’s focus on “data dominates.” Contributors cite personal experience that refactoring to simpler, well‑organized data often yields speed, size and maintainability gains, while early abstraction or micro‑optimizations tend to increase complexity and future cost. There is agreement that measuring performance after a reasonable design is essential, and that the rules remain useful but may need contextual adjustment for modern workloads, tooling and large‑scale systems.

---

## Full Article

Rob Pike's 5 Rules of Programming
=================================

1. **Rule 1.** You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't try to second guess and put in a speed hack until you've proven that's where the bottleneck is.
  
2. **Rule 2.** Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest.
  
3. **Rule 3.** Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy. (Even if n does get big, use Rule 2 first.)
  
4. **Rule 4.** Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms as well as simple data structures.
  
5. **Rule 5.** Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming.

Pike's rules 1 and 2 restate Tony Hoare's famous maxim
"Premature optimization is the root of all evil."

Ken Thompson rephrased Pike's rules 3 and 4 as "When in doubt,
use brute force.".

Rules 3 and 4 are instances of the design philosophy KISS.

Rule 5 was previously stated by Fred Brooks in The Mythical
Man-Month. Rule 5 is often shortened to "write stupid code that
uses smart objects".