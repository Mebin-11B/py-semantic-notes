---
title: "Ternary Bonsai: Top Intelligence at 1.58 Bits"
url: https://prismml.com/news/ternary-bonsai
clipped: 2026-06-17 01:14:26
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Ternary Bonsai: Top Intelligence at 1.58 Bits](https://prismml.com/news/ternary-bonsai)

## Digest Summary
PrismML announced Ternary Bonsai, a family of 1.58‑bit language models (8 B, 4 B, 1.7 B parameters) that use ternary weights {-s, 0, +s} encoded as {-1, 0, +1} with a shared FP16 scale per 128‑weight group. This representation yields a memory footprint ~9× smaller than standard 16‑bit models while maintaining full‑network quantization (embeddings, attention, MLPs, LM head). Benchmarking shows the 8 B model scores 75.5 average, 5 points higher than the 1‑bit Bonsai 8 B (70.5) and approaches Qwen3 8 B performance, despite using only 1.75 GB (vs 16.38 GB). Throughput reaches 82 tokens/s on Apple M4 Pro and 27 tokens/s on iPhone 17 Pro Max, with energy use of 0.105 mWh/tok (M4 Pro) and 0.132 mWh/tok (iPhone). Models run natively on Apple devices via MLX, are released under Apache 2.0, and extend the Pareto frontier for capability versus size, offering a trade‑off between the ultra‑compact 1‑bit Bonsai and higher‑quality models.

## Discussion Summary
The comments highlight enthusiasm for the ternary‑Bonsai model’s speed, low memory use and strong benchmark results, especially its efficiency on edge hardware and the absence of multiplications during inference. Many note that accuracy‑per‑byte compares favorably to larger 16‑bit models, while also questioning why comparisons are limited to unquantized baselines rather than other low‑bit quantizations. Users express interest in scaling the approach to larger parameter counts, curiosity about practical deployment constraints such as KV‑cache benefits, and some critique the model’s overly literal responses.

---

## Full Article

Today, we’re announcing Ternary Bonsai, a new family of 1.58-bit language models designed to balance strict memory constraints with high accuracy requirements.   
  
This release builds on the efficiency frontier we began exploring with the recently released 1-bit Bonsai models. The 1-bit family showed that extreme compression could still produce commercially useful language models. Ternary Bonsai targets a different point on that curve: a modest increase in size for a meaningful gain in performance.

The models are available in three sizes: 8B, 4B, and 1.7B parameters. By using ternary weights {-1, 0, +1}, these models achieve a memory footprint approximately 9x smaller than standard 16-bit models while outperforming most peers in their respective parameter classes on standard benchmarks.

A true ternary model
--------------------

Ternary Bonsai implements 1.58-bit representation throughout the entire network architecture. There are no higher-precision escape hatches. Embeddings, attention layers, MLPs, and the LM head all use the same 1.58-bit representation.

The models employ a group-wise quantization scheme in which each weight is constrained to one of three values: {-s, 0, +s}. These three states are encoded as (-1, 0, +1) using 1.58 bits per weight, together with a shared FP16 scale factor (s) for each group of 128 weights.

Benchmark performance
---------------------

Compared to the 1-bit Bonsai 8B, the Ternary Bonsai 8B scores 5 points higher on average across benchmarks, while requiring only 600MB more memory.

Ternary Bonsai 8B (1.75 GB) reaches 75.5 average benchmark score, compared with 70.5 for 1-bit Bonsai 8B (1.15 GB). Among its peers, it is only behind Qwen3 8B (16.38 GB) and outperforms all other models, despite being 9-10x smaller than them.  It posts competitive results across MMLU Redux, MuSR, GSM8K, HumanEval+, IFEval, and BFCLv3, showing that the gain is broad rather than concentrated in a single benchmark.

> *Fig I: The benchmark scores of Ternary Bonsai 8B compared to other models in the same parameter class.*

The intelligence density of Ternary Bonsai models continue to significantly outperform other models in their comparable parameter classes.

Fig II: Intelligence density (per GB) of Ternary Bonsai 8B compared to other models in the same parameter class.

Extending the Pareto frontier
-----------------------------

Fig III: Performance vs size (log scale) comparison of the 1-bit Bonsai family relative to models across multiple size classes.

Our earlier 1-bit Bonsai models established a new Pareto frontier for language model capability versus size. Ternary Bonsai shifts that frontier even further left.

That makes it a useful addition to the Bonsai family, and not a replacement for 1-bit Bonsai. In settings where the smallest possible footprint is the priority, 1-bit remains the right choice. However, where a small increase in memory can justify a substantially stronger model, Ternary Bonsai offers an alternative tradeoff. The 1.7B, 4B, and 8B variants extend that tradeoff across multiple deployment tiers, giving developers more flexibility in how they allocate memory, throughput, and model quality.

Throughput and energy use
-------------------------

Fig IV: Throughput (toks/sec) and energy consumption (mWh/tok) across various hardware platforms.

The new models also deliver strong throughput in practice. On M4 Pro, Ternary Bonsai 8B runs at 82 toks/sec, roughly 5x faster than a 16-bit 8B model and on iPhone 17 Pro Max, it runs at 27 toks/sec. They use substantially less energy than their 16-bit full-precision counterparts, delivering roughly 3-4x better energy efficiency. On the M4 Pro, Ternary Bonsai 8B requires 0.105 mWh/tok and on the iPhone 17 Pro Max, it only requires 0.132 mWh/tok.

Platform Coverage
-----------------

Ternary Bonsai models run natively on Apple devices (Mac, iPhone, iPad) via MLX. Model weights are available today under the Apache 2.0 License.

Full technical details of our training, evaluation, and benchmarking processes are available in our [whitepaper](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/ternary-bonsai-8b-whitepaper.pdf).

Join Us
-------

PrismML emerged from a team of Caltech researchers and was founded with support from Khosla Ventures, Cerberus and Google. We’ve spent years tackling one of the field’s hardest problems: compressing neural networks without sacrificing their reasoning ability.

If you want to help build the next generation of state-of-the-art AI, we’d love to hear from you. Check out our [careers page](https://prismml.com/#careers).