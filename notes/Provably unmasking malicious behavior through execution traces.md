---
title: "Provably unmasking malicious behavior through execution traces"
url: https://arxiv.org/abs/2512.13821
clipped: 2026-06-17 01:55:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Provably unmasking malicious behavior through execution traces](https://arxiv.org/abs/2512.13821)

## Digest Summary
The document consists of a title—“The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces”—and a series of image placeholders with alt‑text labels. The images reference institutional and platform logos: Cornell University, the arXiv preprint service (shown twice), a licensing icon, BibSonomy, and Reddit. No abstract, introduction, methodology, results, or discussion sections are included in the provided excerpt, so no technical details, experimental data, or conclusions about code world models, execution‑trace analysis, or malicious behavior detection are available for summarization.

## Discussion Summary
The comments convey strong skepticism toward the presented method, arguing it performs worse than a simple random‑number test and does not improve detection without raising false positives. The high 98.8 % false‑positive rate is seen as unacceptable, leading to the view that further mathematical analysis is not worthwhile. Additionally, there is confusion over inconsistencies between the text and the tables, prompting a request for clarification.

---

## Full Article

[Submitted on 15 Dec 2025 (

[v1](https://arxiv.org/abs/2512.13821v1)

), last revised 5 Feb 2026 (this version, v2)]

Title:The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces
==========================================================================================================

View a PDF of the paper titled The Double Life of Code World Models: Provably Unmasking Malicious Behavior Through Execution Traces, by Subramanyam Sahoo

[View PDF](https://arxiv.org/pdf/2512.13821)
[HTML (experimental)](https://arxiv.org/html/2512.13821v2)
> Abstract:Large language models (LLMs) increasingly generate code with minimal human oversight, raising critical concerns about backdoor injection and malicious behavior. We present Cross-Trace Verification Protocol (CTVP), a novel AI control framework that verifies untrusted code-generating models through semantic orbit analysis. Rather than directly executing potentially malicious code, CTVP leverages the model's own predictions of execution traces across semantically equivalent program transformations. By analyzing consistency patterns in these predicted traces, we detect behavioral anomalies indicative of backdoors. Our approach introduces the Adversarial Robustness Quotient (ARQ), which quantifies the computational cost of verification relative to baseline generation, demonstrating exponential growth with orbit size. Theoretical analysis establishes information-theoretic bounds showing non-gamifiability - adversaries cannot improve through training due to fundamental space complexity constraints. This work demonstrates that semantic orbit analysis provides a theoretically grounded approach to AI control for code generation tasks, though practical deployment requires addressing the high false positive rates observed in initial evaluations.

Submission history
------------------

From: Subramanyam Sahoo [

[view email](https://arxiv.org/show-email/b56d70da/2512.13821)

]

**[[v1]](https://arxiv.org/abs/2512.13821v1)**

Mon, 15 Dec 2025 19:05:37 UTC (315 KB)

**[v2]**

Thu, 5 Feb 2026 16:40:19 UTC (317 KB)