---
title: "All elementary functions from a single binary operator"
url: https://arxiv.org/abs/2603.21852
clipped: 2026-06-17 01:17:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [All elementary functions from a single binary operator](https://arxiv.org/abs/2603.21852)

## Digest Summary
The paper introduces a single binary operator eml(x, y) = exp(x) − ln(y) together with the constant 1, and proves that this primitive can generate the full set of elementary functions typically available on a scientific calculator. Using eml, the author constructs constants (e, π, i), arithmetic operations (addition, subtraction, multiplication, division, exponentiation), and transcendental functions (sin, cos, sqrt, log, etc.) via explicit formulas—for instance, exp(x) = eml(x, 1) and ln(x) = eml(1, eml(eml(1, x), 1)). The resulting expressions form uniform binary trees described by the simple grammar S → 1 | eml(S, S). This uniformity enables gradient‑based symbolic regression: treating EML trees as trainable circuits optimized with Adam, the method can exactly recover closed‑form elementary formulas from numerical data for tree depths up to 4, while also fitting arbitrary data. The work was submitted on 23 Mar 2026 and revised on 4 Apr 2026.

## Discussion Summary
The comments express curiosity about the EML formulation, with several users asking for comprehensive tables of mathematical operations expressed in the eml(x, y) form and questioning whether the required gate combinations are simpler than existing primitives. There is interest in potential hardware realizations, including analog calculators, and comparisons to traditional math coprocessors, alongside remarks that the concept feels novel yet abstract. While some find the idea intriguing and promising, others remain uncertain about practical implementation and complexity.

---

## Full Article

[Submitted on 23 Mar 2026 (

[v1](https://arxiv.org/abs/2603.21852v1)

), last revised 4 Apr 2026 (this version, v2)]

Title:All elementary functions from a single binary operator
============================================================

View a PDF of the paper titled All elementary functions from a single binary operator, by Andrzej Odrzywo{\l}ek

[View PDF](https://arxiv.org/pdf/2603.21852)
[HTML (experimental)](https://arxiv.org/html/2603.21852v2)
> Abstract:A single two-input gate suffices for all of Boolean logic in digital hardware. No comparable primitive has been known for continuous mathematics: computing elementary functions such as sin, cos, sqrt, and log has always required multiple distinct operations. Here I show that a single binary operator, eml(x,y)=exp(x)-ln(y), together with the constant 1, generates the standard repertoire of a scientific calculator. This includes constants such as e, pi, and i; arithmetic operations including addition, subtraction, multiplication, division, and exponentiation as well as the usual transcendental and algebraic functions. For example, exp(x)=eml(x,1), ln(x)=eml(1,eml(eml(1,x),1)), and likewise for all other operations. That such an operator exists was not anticipated; I found it by systematic exhaustive search and established constructively that it suffices for the concrete scientific-calculator basis. In EML (Exp-Minus-Log) form, every such expression becomes a binary tree of identical nodes, yielding a grammar as simple as S -> 1 | eml(S,S). This uniform structure also enables gradient-based symbolic regression: using EML trees as trainable circuits with standard optimizers (Adam), I demonstrate the feasibility of exact recovery of closed-form elementary functions from numerical data at shallow tree depths up to 4. The same architecture can fit arbitrary data, but when the generating law is elementary, it may recover the exact formula.

Submission history
------------------

From: Andrzej Odrzywolek [

[view email](https://arxiv.org/show-email/a915ff5b/2603.21852)

]

**[[v1]](https://arxiv.org/abs/2603.21852v1)**

Mon, 23 Mar 2026 11:40:24 UTC (1,393 KB)

**[v2]**

Sat, 4 Apr 2026 06:31:05 UTC (1,245 KB)