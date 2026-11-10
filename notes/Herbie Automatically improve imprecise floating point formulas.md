---
title: "Herbie: Automatically improve imprecise floating point formulas"
url: https://herbie.uwplse.org/doc/latest/tutorial.html
clipped: 2026-06-17 01:23:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Herbie: Automatically improve imprecise floating point formulas](https://herbie.uwplse.org/doc/latest/tutorial.html)

## Digest Summary
Herbie is a tool that automatically rewrites floating‑point expressions to improve numerical accuracy. Users start it with `racket -l herbie web` (or `herbie`) and interact through a browser UI. An example (`sqrt(x+1)‑sqrt(x)`) shows Herbie increasing accuracy from 53.2 % to 99.7 % and sometimes reducing runtime.

The tutorial demonstrates fixing bug 208 in JavaScript’s `math.js` complex square‑root implementation. The core computation:

```js
var r = Math.sqrt(x.re*x.re + x.im*x.im);
0.5 * Math.sqrt(2.0 * (r + x.re))
```

is extracted, with `x.re` and `x.im` treated as independent float inputs and each branch (non‑negative/negative `x.im`) submitted separately. Input ranges are limited (e.g., `x.im ≥ 0`, `x.re` up to 1.79e308).

Herbie generates several alternatives; the most accurate (≈84.6 %) inserts an `if` to avoid cancellation and replaces `sqrt` with `Math.hypot`. The resulting code snippet includes the conditional and uses `hypot` for a more stable distance calculation. Users can translate alternatives to target languages via the UI and repeat the process for other branches.

## Discussion Summary
The feedback expresses uncertainty about the tool’s capabilities, questioning whether reformulations can be limited to non‑branching forms and seeking clarification on whether reported speedups refer to latency or throughput. Users are skeptical about the relevance of improvements when operating with values already scaled to a typical numeric range, and they doubt the accuracy gains shown in examples, noting apparent inconsistencies. The commentary also calls for clearer explanations of the problems addressed, suggests integrating robust accuracy enhancements into the language rather than relying on a separate library, and warns that reliance on such a tool might introduce additional errors.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: HTTPSConnectionPool(host='herbie.uwplse.org', port=443): Max retries exceeded with url: /doc/latest/tutorial.html (Caused by ConnectTimeoutError(<HTTPSConnection(host='herbie.uwplse.org', port=443) at 0x10af64910>, 'Connection to herbie.uwplse.org timed out. (connect timeout=10)'))
> You can view the original article page directly [here](https://herbie.uwplse.org/doc/latest/tutorial.html).