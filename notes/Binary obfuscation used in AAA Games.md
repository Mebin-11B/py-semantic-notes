---
title: Binary obfuscation used in AAA Games
url: https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html
clipped: 2026-06-17 01:20:52
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - binary obfuscation
  - reverse engineering
  - compiler optimization
  - anti-piracy
related:
  - "[[Binary Obfuscation]]"
  - "[[Reverse Engineering]]"
  - "[[Compiler Optimization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A summary of binary obfuscation techniques designed to protect game code from piracy and reverse-engineering while maintaining Link-Time Optimization (LTO).
>
> **Key points:**
> - Traditional binary obfuscation often breaks compiler-level optimizations like Link-Time Optimization (LTO).
> - Summarizes techniques to perform obfuscation post-LTO or embed it into the compilation process safely.
> - Aims to preserve symbol information and handle indirect branches without degrading runtime execution performance.
> - Community discussion raises skepticism about "security through obscurity" and questions performance impacts like FPS loss.
>
> **Concept links:** [[Binary Obfuscation]], [[Reverse Engineering]], [[Compiler Optimization]], [[Anti-Piracy]]
>
> **Suggested connections:**
> - [[Compiler Optimization]] — Explores the trade-offs between optimization passes (LTO) and code obfuscation tools.
> - [[Reverse Engineering]] — Discusses the mechanisms used by developers to deter static and dynamic analysis of binaries.
<!-- ai-summary:end -->

# [Binary obfuscation used in AAA Games](https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html)

## Digest Summary
The blog post recaps a Thotcon presentation on binary obfuscation techniques that maintain compatibility with Link‑Time Optimization (LTO). It outlines the problem that conventional obfuscation often disrupts LTO, reducing the benefits of compiler‑level optimizations. The author describes approaches for applying obfuscation after LTO or integrating it into the compilation pipeline so that the optimizer’s analysis and transformations remain intact. Key points include preserving symbol information, handling indirect branches, and ensuring that the resulting binary remains functional while being harder to reverse‑engineer. The post also references practical considerations such as toolchain support and performance impact, providing a concise summary of methods that achieve obfuscation without sacrificing LTO‑derived performance gains.

## Discussion Summary
The comment expresses strong skepticism toward “security through obscurity,” arguing that competent security researchers generally view it unfavorably and suggesting it may serve more as a legal stance than a genuine protective measure. It questions the practicality of employing such techniques, asks why they would be used, and raises concerns about potential performance drawbacks, specifically inquiring about any impact on frame‑rate.

---

## Full Article
