---
title: "Do transformers need three projections? Systematic study of QKV variants"
url: https://arxiv.org/abs/2606.04032
clipped: 2026-06-17 00:52:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - transformer models
  - attention mechanism
  - model optimization
  - edge inference
  - linear projections
related:
  - "[[Transformer Models]]"
  - "[[Model Optimization]]"
  - "[[Edge Inference]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A systematic study of QKV variants in Transformers shows that sharing key-value projections (Q-K=V) maintains performance while reducing cache size by 50%.
>
> **Key points:**
> - Investigates projection-sharing schemes in attention mechanisms: shared key-value, shared query-key, and fully shared.
> - Evaluates variant models across synthetic tasks, vision datasets, and large-scale language models up to 1.2 billion parameters.
> - Demonstrates that the Q-K=V scheme reduces KV cache storage requirements by 50% with minor perplexity increases.
> - Combines projection sharing with Grouped Query Attention (GQA) to reach a cache size reduction of up to 96.9%, assisting on-device inference.
>
> **Concept links:** [[Transformer Models]], [[Attention Mechanism]], [[Model Optimization]], [[Edge Inference]], [[Linear Projections]]
>
> **Suggested connections:**
> - [[Transformer Models]] — optimizing internal tensor dimensions to decrease compute overhead in deep neural networks.
> - [[Model Optimization]] — using weight-tying techniques to reduce memory footprints during inference.
<!-- ai-summary:end -->


# [Do transformers need three projections? Systematic study of QKV variants](https://arxiv.org/abs/2606.04032)

## Digest Summary
The paper systematically investigates the necessity of three separate linear projections (query, key, value – QKV) in Transformer attention. It evaluates three projection‑sharing schemes: (a) shared key‑value (Q‑K = V), (b) shared query‑key (Q = K‑V), and (c) a single shared projection (Q = K = V). Since the latter two produce symmetric attention maps, the authors also test asymmetric attention using 2‑D positional encodings. Experiments cover synthetic tasks, vision datasets (MNIST, CIFAR, TinyImageNet, anomaly detection) and large‑scale language modeling (300 M and 1.2 B‑parameter models trained on 10 B tokens). Findings include: – Transformers with Q‑K = V perform on par with or slightly better than standard QKV models. – In language modeling, Q‑K = V reduces key‑value cache size by 50 % with only a 3.1 % increase in perplexity. – Combining projection sharing with head sharing (GQA‑4 or MQA) yields up to 96.9 % cache reduction, facilitating on‑device inference. – The authors attribute the success of Q‑K = V to overlapping representational spaces for keys and values and low‑rank attention dynamics, whereas Q = K‑V disrupts directional attention. The study positions projection sharing as a practical weight‑tying technique for memory‑efficient Transformers.

## Discussion Summary
The comments express mixed reactions, noting that the paper’s notation is confusing and that “‑” should be read as subtraction rather than “and also.” Readers find the K = V simplification surprisingly effective yet question its theoretical justification and the lack of benchmark results for the more interesting Q = K‑V case. There is curiosity about imposing broader linear constraints on attention matrices, but also skepticism about the findings’ generalizability given the modest training regime. Overall, the work is seen as entertaining but potentially limited in scalability and depth.

---

## Full Article

[Submitted on 1 Jun 2026 (

[v1](https://arxiv.org/abs/2606.04032v1)

), last revised 4 Jun 2026 (this version, v2)]

Title:Do Transformers Need Three Projections? Systematic Study of QKV Variants
==============================================================================

View a PDF of the paper titled Do Transformers Need Three Projections? Systematic Study of QKV Variants, by Ali Kayyam and 2 other authors

[View PDF](https://arxiv.org/pdf/2606.04032)
[HTML (experimental)](https://arxiv.org/html/2606.04032v2)
> Abstract:Transformers have become the standard solution for various AI tasks, with the query, key, and value (QKV) attention formulation playing a central role. However, the individual contribution of these three projections and the impact of omitting some remain poorly understood. We systematically evaluate three projection sharing constraints: a) Q-K=V (shared key-value), b) Q=K-V (shared query-key), and c) Q=K=V (single projection). The last two variants produce symmetric attention maps; to address this, we also explore asymmetric attention via 2D positional encodings. Through experiments spanning synthetic tasks, vision (MNIST, CIFAR, TinyImageNet, anomaly), and language modeling (300M and 1.2B parameter models on 10B tokens), we discovered that our transformers perform on par or occasionally better than the QKV transformer. In language modeling, Q-K=V projection sharing achieves 50% KV cache reduction with only 3.1% perplexity degradation. Crucially, projection sharing is complementary to head sharing (GQA/MQA): combining Q-K=V with GQA-4 yields 87.5% cache reduction, while Q-K=V + MQA achieves 96.9%, enabling practical on-device inference. We show that Q-K=V preserves quality because keys and values can occupy similar representational spaces and attention operates in a low-rank regime, whereas Q=K-V breaks attention directionality. Our results systematically characterize projection sharing as an underexplored instance of weight tying in attention, with direct, quantifiable inference memory benefits, particularly valuable for edge deployment. The code is publicly available at [this https URL](https://github.com/Brainchip-Inc/Do-Transformers-Need-3-Projections)

Submission history
------------------

From: Anusha Madan Gopal [

[view email](https://arxiv.org/show-email/278822ff/2606.04032)

]

**[[v1]](https://arxiv.org/abs/2606.04032v1)**

Mon, 1 Jun 2026 20:59:05 UTC (2,017 KB)

**[v2]**

Thu, 4 Jun 2026 17:08:43 UTC (2,017 KB)