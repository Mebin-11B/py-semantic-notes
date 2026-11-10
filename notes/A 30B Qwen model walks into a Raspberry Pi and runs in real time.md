---
title: "A 30B Qwen model walks into a Raspberry Pi and runs in real time"
url: https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/
clipped: 2026-06-17 02:02:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - Local AI Inference
  - Model Quantization
  - Datatype Learning
  - Raspberry Pi
  - GPU Compute Kernels
  - Edge Computing
related:
  - '[[Running local models on an M4 with 24GB memory]]'
  - '[[Can I run AI locally]]'
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** ByteShape uses its ShapeLearn datatype learning method to run the 30B Qwen-3 model in real-time on a Raspberry Pi 5 by optimizing the speed-versus-quality tradeoff.
>
> **Key points:**
> - Optimizes per-tensor weight datatypes to fit available RAM while maximizing speed (TPS) and output quality.
> - On Raspberry Pi 5, the model reaches 8 TPS with ~94% accuracy, crossing the real-time usability threshold.
> - On high-end CPUs (Intel i7) and GPUs (RTX 5090/4080), ByteShape outperforms Unsloth and MagicQuant on accuracy and speed.
> - Highlights that lower bitlengths don't automatically increase speed due to GPU warp constraints and decoding overhead in llama.cpp.
>
> **Concept links:** [[Local AI Inference]], [[Model Quantization]], [[Datatype Learning]], [[Raspberry Pi]], [[GPU Compute Kernels]], [[Edge Computing]]
>
> **Suggested connections:**
> - [[Running local models on an M4 with 24GB memory]] — both explore options and constraints for running LLMs on consumer/edge hardware.
> - [[Can I run AI locally]] — provides the hardware-specific answer and configuration details for edge LLM execution.
<!-- ai-summary:end -->

# [A 30B Qwen model walks into a Raspberry Pi and runs in real time](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/)

## Digest Summary
The release uses ShapeLearn, a per‑tensor bit‑length learning method, to select weight datatypes for Qwen‑3‑30B‑A3B‑Instruct‑2507 that maximize tokens‑per‑second (TPS) and output quality while fitting device memory.  

**CPU results** – On a Raspberry Pi 5 (16 GB) the model Q3_K_S‑2.70 bpw (KQ‑2) reaches 8 TPS with ≈ 94 % baseline accuracy, crossing the real‑time threshold. For pure accuracy, ByteShape models achieve ~98.8 % (≈1.1‑1.3 % relative error), outperforming Unsloth’s best (~97.9 %). On an Intel i7 (64 GB) ByteShape’s IQ4_XS‑4.67 bpw (KQ‑9) attains 0.25 % error (99.75 % accuracy) at 273 TPS, surpassing Unsloth and MagicQuant both in speed and error. The balanced point Q3_K_S‑3.25 bpw (KQ‑5) offers ~98 % accuracy at 23 TPS.  

**GPU results** – RTX 5090 (32 GB) shows a ~4‑bit sweet spot: Unsloth Q4_0, IQ4_XS and MagicQuant iq4_nl run ~302 TPS at 98.4‑98.9 % accuracy. ByteShape’s IQ4_XS‑4.67 bpw reaches 273 TPS with 99.75 % accuracy, the highest‑quality model. RTX 4080 (16 GB) cannot fit the 4‑bit set; ByteShape’s IQ4_XS‑3.87 bpw delivers 215 TPS at 98.66 % accuracy, a 1.59× lower error and ~9 % higher TPS than the best Unsloth alternative.  

Overall, treating memory as a constraint and applying ShapeLearn yields models that consistently dominate Unsloth and MagicQuant on the TPS‑quality trade‑off across CPUs and GPUs.

## Discussion Summary
The discussion expresses enthusiasm for a privacy‑focused, locally hosted smart‑assistant system that combines voice‑controlled speakers, mesh networking, and a home‑server for storage and inference, while criticizing the lack of standardized, plug‑and‑play integration among existing components. It also seeks guidance on comparing model sizes and performance, noting uncertainty about practical limits for running useful AI on modest hardware. Frustration is voiced over failed attempts to run large models on a Raspberry Pi, with requests for clearer documentation and realistic expectations of accuracy metrics.

---

## Full Article

For this release, we optimize for what people actually experience when they run a model:
**fast, high-quality responses on a specific target device**.

We use ShapeLearn, our datatype learning method to choose weight datatypes for
**Qwen3-30B-A3B-Instruct-2507** that maximize performance in terms of
tokens per second (TPS) and output quality, with one practical constraint: the model
must fit comfortably in the available memory. Once it fits, making the file smaller
isn't a goal by itself. We only shrink further when it also improves the real tradeoff
people care about: **speed vs. quality**.

Approaching datatype learning this way matters because in llama.cpp, "fewer bits" doesn't
automatically mean "more speed." Different quantization formats can trigger different kernels
and overheads, and on some GPUs, **going lower-bit can even get slower**, despite
using less memory.

**Bottom line:** treat memory as a **budget** to meet, then optimize what
matters most: **TPS and quality**.

CPUs
----

On CPUs, reducing footprint via shorter bitlengths affects the TPS and accuracy
tradeoff as one would expect: once the model fits, reducing footprint tends to increase
TPS in a fairly monotonic way. If datatypes are selected correctly, you can trade a bit
of quality for speed predictably, which makes it much easier to pick a point on the
curve that matches your constraints.

We'll start with the most memory-constrained CPU case (Raspberry Pi 5 16GB), where
"fits in RAM" is the limiting factor, then move to an Intel i7 with 64GB, where
everything fits.

### Raspberry Pi 5

The figure below shows TPS vs. normalized accuracy for the models that fit in RAM on
the Raspberry Pi 5 16GB.

![Raspberry Pi 5 performance: tokens per second vs quality](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/images/averagen_bubble_chart_bpw_size_pi.png)


Raspberry Pi 5: Tokens per second vs quality (bubble size = model footprint)
Tap *Show Legend* below for model details.




Raspberry Pi 5: Tokens per second vs quality (bubble size = model footprint)
Hover over the bubbles, or click *Show Legend* below, for model details.


Show Legend

| # | Model | Acc | TPS | BPW |
| --- | --- | --- | --- | --- |
| ByteShape | | | | |
| CPU-1 | 2.66bpw | 0.9284 | 8.48 | 2.66 |
| CPU-2 | 2.70bpw | 0.9418 | 8.03 | 2.70 |
| CPU-3 | 2.85bpw | 0.9549 | 7.22 | 2.85 |
| CPU-4 | 3.18bpw | 0.9697 | 6.93 | 3.18 |
| CPU-5 | 3.25bpw | 0.9797 | 6.68 | 3.25 |
| CPU-6 | 3.61bpw | 0.9875 | 5.94 | 3.61 |
| CPU-7 | 3.92bpw | 0.9886 | 5.30 | 3.92 |
| Unsloth | | | | |
| 1 | TQ1\_0 | 0.8503 | 5.28 | 2.12 |
| 2 | IQ2\_M | 0.9659 | 5.44 | 2.84 |
| 3 | Q2\_K | 0.9390 | 7.40 | 2.95 |
| 4 | Q2\_K\_L | 0.9470 | 7.23 | 2.97 |
| 5 | Q2\_K\_XL | 0.9665 | 6.45 | 3.09 |
| 6 | IQ3\_XXS | 0.9778 | 5.03 | 3.38 |
| 7 | Q3\_K\_S | 0.9654 | 6.98 | 3.48 |
| 8 | Q3\_K\_XL | 0.9787 | 6.28 | 3.62 |
| 9 | Q3\_K\_M | 0.9759 | 6.29 | 3.85 |

Notably, sustaining **8.5 TPS at 92%+ baseline accuracy** with a 30B model on a
Raspberry Pi reshapes expectations for Pi-class systems. Overall, the trend shows that ShapeLearn
consistently produces better models, with ByteShape trending up and to the right of Unsloth,
achieving higher tokens per second at the same quality, or higher quality at the same throughput.

We highlight choices for two primary objectives: accuracy or response time.

* **Optimizing for response time while maintaining accuracy:** For interactive,
  on-device use, perceived responsiveness is driven by how quickly text appears, not peak
  throughput. In practice, generation feels real-time once it reaches roughly **8 TPS**,
  comfortably above typical reading speed. In this Raspberry Pi real-time regime,
  `Q3_K_S-2.70bpw [KQ-2]`
  (2.70 BPW, 8.03 TPS, 94.18% accuracy) is our go-to recommendation: it crosses the
  real-time threshold while maintaining high accuracy. Compared
  to Unsloth models at similar quality, ByteShape achieves real-time performance at lower BPW
  and higher TPS, making it the more efficient choice for interactive edge deployment.
* **Accuracy above all:** The table below lists the models that achieve the highest
  accuracy while still being able to run on a Raspberry Pi. Within this set, ByteShape models
  make the best use of the available resources to maximize accuracy, occupying the
  **lowest-error rows** (~1.1â1.3% relative error, ~98.8% accuracy), while the
  strongest Unsloth entries remain around 2.1â2.2% error (~97.9% accuracy). Compared to Unsloth's
  `UD-Q3_K_XL [8]`, ByteShape achieves up to a **1.87Ã lower error rate**
  while still operating at **~5â6 TPS**, comfortably within TPS-norms on Raspberry PI
  making it the better choice when accuracy is the priority.   
  Even when prioritizing maximum speed with some reduction in accuracy,
  `Q3_K_S-3.25bpw [KQ-5]`
  offers a better tradeoff: **more accurate, smaller, and faster** than
  the fastest Unsloth model.

Many other Unsloth and MagicQuant models (some of ours too!) are not in this chart. We compare
them in other sections, but they're not applicable in the Raspberry Pi case. They simply don't fit!

### Intel i7

Next, we move to the Intel i7 with 64GB RAM. The figure below shows TPS vs
normalized accuracy for all models.

![Intel i7 performance: tokens per second vs quality](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/images/averagen_bubble_chart_bpw_size_i7.png)


Intel i7: Tokens per second vs quality (bubble size = model footprint)
Tap *Show Legend* below for model details.




Intel i7: Tokens per second vs quality (bubble size = model footprint)
Hover over the bubbles, or click *Show Legend* below, for model details.


Show Legend

| # | Model | Acc | TPS | BPW |
| --- | --- | --- | --- | --- |
| ByteShape | | | | |
| CPU-1 | 2.66bpw | 0.9284 | 28.25 | 2.66 |
| CPU-2 | 2.70bpw | 0.9418 | 27.57 | 2.70 |
| CPU-3 | 2.85bpw | 0.9549 | 25.48 | 2.85 |
| CPU-4 | 3.18bpw | 0.9697 | 24.19 | 3.18 |
| CPU-5 | 3.25bpw | 0.9797 | 23.09 | 3.25 |
| CPU-6 | 3.61bpw | 0.9875 | 20.47 | 3.61 |
| CPU-7 | 3.92bpw | 0.9886 | 19.23 | 3.92 |
| CPU-8 | 4.41bpw | 0.9934 | 18.30 | 4.41 |
| CPU-9 | 4.67bpw | 0.9975 | 17.02 | 4.67 |
| MagicQuant | | | | |
| 1 | IQ4NL | 0.9837 | 19.69 | 4.51 |
| 2 | IQ4\_NL | 0.9869 | 19.69 | 4.57 |
| 3 | Q6K | 0.9932 | 13.12 | 5.46 |
| 4 | Q5\_K | 0.9867 | 17.08 | 5.69 |
| 5 | Q8\_0 | 0.9903 | 12.76 | 8.51 |
| Unsloth | | | | |
| 1 | TQ1\_0 | 0.8503 | 22.41 | 2.12 |
| 2 | IQ2\_M | 0.9659 | 21.38 | 2.84 |
| 3 | Q2\_K | 0.9390 | 25.20 | 2.95 |
| 4 | Q2\_K\_L | 0.9470 | 25.05 | 2.97 |
| 5 | Q2\_K\_XL | 0.9665 | 22.28 | 3.09 |
| 6 | IQ3\_XXS | 0.9778 | 19.84 | 3.38 |
| 7 | Q3\_K\_S | 0.9654 | 22.63 | 3.48 |
| 8 | Q3\_K\_XL | 0.9787 | 20.84 | 3.62 |
| 9 | Q3\_K\_M | 0.9759 | 21.16 | 3.85 |
| 10 | IQ4\_XS | 0.9880 | 20.52 | 4.29 |
| 11 | IQ4\_NL | 0.9882 | 19.76 | 4.53 |
| 12 | Q4\_0 | 0.9885 | 19.78 | 4.55 |
| 13 | Q4\_K\_S | 0.9905 | 18.89 | 4.57 |
| 14 | Q4\_K\_XL | 0.9851 | 18.61 | 4.63 |
| 15 | Q4\_K\_M | 0.9854 | 18.32 | 4.86 |
| 16 | Q4\_1 | 0.9844 | 18.56 | 5.03 |
| 17 | Q5\_K\_S | 0.9903 | 17.62 | 5.52 |
| 18 | Q5\_K\_M | 0.9956 | 17.07 | 5.69 |
| 19 | Q5\_K\_XL | 0.9941 | 16.82 | 5.69 |
| 20 | Q6\_K | 0.9964 | 15.14 | 6.57 |
| 21 | Q6\_K\_XL | 0.9929 | 14.17 | 6.90 |
| 22 | Q8\_0 | 0.9948 | 12.73 | 8.51 |
| 23 | Q8\_K\_XL | 0.9936 | 11.08 | 9.43 |

Overall, ByteShape models outperform both Unsloth and MagicQuant, delivering higher quality at
comparable throughput using fewer bits per parameter. Only ByteShape offers models that run in
the 26+ TPS range, extending performance well beyond the other methods.

**Highlights:**

* **Quality-first:** At the high-accuracy end of the table,
  `IQ4_XS-4.67bpw [KQ-9]`
  achieves the lowest relative error (0.25%), outperforming the best-running Unsloth
  models (`Q6_K [20]` and `Q5_K_M [18]` whose
  relative errors are 0.36% and 0.44%). Compared directly, ByteShape delivers up to a 1.44Ã lower
  error rate with higher throughput than `Q6_K [20]`, and a 1.76Ã lower error rate at
  essentially the same speed as `Q5_K_M [18]`. MagicQuant `mxfp4 [3]` trails
  in this regime, with both higher error and lower TPS.
* **Balanced point:** In the mid-accuracy, high-throughput region,
  `Q3_K_S-3.25bpw [KQ-5]`
  combines ~98% accuracy with 23.1 TPS at just 3.25 BPW, offering the best overall
  balance in the table. Matching or exceeding this accuracy with Unsloth
  (`IQ4_XS [10]`) requires higher BPW and lower TPS, while choosing an Unsloth model
  closer in speed (`Q3_K_S [7]`) incurs a 1.73Ã higher error rate. MagicQuant does not
  offer a competitive model in this range; its fastest entry (`IQ4_NL [2]`) is behind both
  ByteShape and Unsloth in accuracy and throughput.

**Takeaway:** Across both quality-first and balanced settings, ByteShape consistently
converts the available bit budget into either higher accuracy or higher TPS, and is the only approach
that simultaneously covers the high-quality and 26+ TPS balanced-performance regions in this comparison.

GPUs: RTX5090/32GB and RTX4080/16GB
-----------------------------------

On GPUs, performance depends as much on **kernel choice** as on raw memory footprint.
For matmul/matvec, llama.cpp's quantization-specific GPU decode paths incur very different overheads,
so fewer bits per weight do **not** reliably translate to higher TPS. Instead, TPS often
peaks at quantization-specific sweet spots. Pushing BPW lower can even **increase VRAM traffic
and instruction count**, hurting performance rather than improving it. We dig into this behavior in
more detail right after the GPU results section, where the kernel-level tradeoffs become more apparent.

We evaluate on two GPUs: an **RTX 5090 (32 GB)**, which can run models
**above 4 BPW** and typically reach the fastest sweet spots, and an
**RTX 4080 (16 GB)**, where **>4 BPW models do not fit**, forcing
different trade-offs and making the device-optimized curve easier to see.

### RTX 5090 (32GB of VRAM)

Let's start with the 5090, which has enough VRAM to support all of the quantized models. The figure
below shows TPS vs normalized accuracy.

![RTX 5090 performance: tokens per second vs quality](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/images/averagen_bubble_chart_bpw_size_5090.png)


RTX 5090: Tokens per second vs quality (bubble size = model footprint)
Tap *Show Legend* below for model details.




RTX 5090: Tokens per second vs quality (bubble size = model footprint)
Hover over the bubbles, or click *Show Legend* below, for model details.


Show Legend

| # | Model | Acc | TPS | BPW |
| --- | --- | --- | --- | --- |
| ByteShape | | | | |
| GPU-1 | 2.69bpw | 0.9424 | 312.64 | 2.69 |
| GPU-2 | 2.75bpw | 0.9548 | 314.24 | 2.75 |
| GPU-3 | 3.02bpw | 0.9583 | 309.96 | 3.02 |
| GPU-4 | 3.29bpw | 0.9735 | 305.24 | 3.29 |
| GPU-5 | 3.63bpw | 0.9774 | 304.20 | 3.63 |
| GPU-6 | 3.87bpw | 0.9866 | 302.57 | 3.87 |
| GPU-7 | 4.41bpw | 0.9934 | 285.12 | 4.41 |
| GPU-8 | 4.67bpw | 0.9975 | 272.98 | 4.67 |
| MagicQuant | | | | |
| 1 | IQ4NL | 0.9837 | 303.12 | 4.51 |
| 2 | IQ4\_NL | 0.9869 | 299.17 | 4.57 |
| 3 | Q6K | 0.9932 | 240.42 | 5.46 |
| 4 | Q5\_K | 0.9867 | 282.48 | 5.69 |
| 5 | Q8\_0 | 0.9903 | 246.99 | 8.51 |
| Unsloth | | | | |
| 1 | TQ1\_0 | 0.8503 | 294.87 | 2.12 |
| 2 | IQ2\_M | 0.9659 | 298.51 | 2.84 |
| 3 | Q2\_K | 0.9390 | 273.69 | 2.95 |
| 4 | Q2\_K\_L | 0.9470 | 273.88 | 2.97 |
| 5 | Q2\_K\_XL | 0.9665 | 280.03 | 3.09 |
| 6 | IQ3\_XXS | 0.9778 | 294.66 | 3.38 |
| 7 | Q3\_K\_S | 0.9654 | 254.06 | 3.48 |
| 8 | Q3\_K\_XL | 0.9787 | 266.38 | 3.62 |
| 9 | Q3\_K\_M | 0.9759 | 276.67 | 3.85 |
| 10 | IQ4\_XS | 0.9880 | 303.03 | 4.29 |
| 11 | IQ4\_NL | 0.9882 | 299.65 | 4.53 |
| 12 | Q4\_0 | 0.9885 | 302.01 | 4.55 |
| 13 | Q4\_K\_S | 0.9905 | 293.13 | 4.57 |
| 14 | Q4\_K\_XL | 0.9851 | 292.03 | 4.63 |
| 15 | Q4\_K\_M | 0.9854 | 292.64 | 4.86 |
| 16 | Q4\_1 | 0.9844 | 293.60 | 5.03 |
| 17 | Q5\_K\_S | 0.9903 | 284.39 | 5.52 |
| 18 | Q5\_K\_M | 0.9956 | 284.10 | 5.69 |
| 19 | Q5\_K\_XL | 0.9941 | 282.40 | 5.69 |
| 20 | Q6\_K | 0.9964 | 264.88 | 6.57 |
| 21 | Q6\_K\_XL | 0.9929 | 255.85 | 6.90 |
| 22 | Q8\_0 | 0.9948 | 247.35 | 8.51 |

Two things stand out immediately:  
First, this GPU shows a clear **~4-bit sweet spot**: several ~4b models
cluster at very high TPS with nearly identical quality. Examples include
`Unsloth Q4_0 [12]`, `Unsloth IQ4_XS [10]`,
`IQ4_XS-3.87bpw [IQ-6]`
, and MagicQuant `iq4_nl-EHQKOUD-IQ4NL [1]`, all running around ~302â303 TPS
at ~98.4â98.9% accuracy. Within
this tight cluster, Unsloth edges out slightly in throughput and quality.

Second, outside of that sweet spot, the tradeoff becomes much more uneven:

* Many other Unsloth and Magic Quant models show **significantly lower TPS**, regardless
  of whether they are quantized more or less aggressively.
* Past the ~4b region, only ByteShape continues to increase TPS with a more predictable reduction in quality.

**Accuracy-critical workloads:** when output quality is paramount,
ByteShape delivers the most accurate model on the 5090:
`IQ4_XS-4.67bpw [IQ-8]`
(4.67 BPW, 272.98 TPS, 99.75% accuracy). It surpasses `Unsloth Q6_K [20]` (6.57 BPW, 264.88 TPS, 99.64% accuracy)
while using fewer bits and achieving slightly higher throughput, and it clearly outperforms MagicQuant
`mxfp4_moe-H-B16-EUR-IQ4NL-KO-Q5K-QD-Q6K [3]` (5.46 BPW, 240.42 TPS, 99.32% accuracy) in both
accuracy and speed, making it the strongest choice when accuracy is a task-critical deployment requirement.

**Practical takeaway.** If your GPU has enough VRAM to run a strong ~4b model that
already meets your speed and accuracy requirements, that cluster is an excellent default. The curve becomes
more interesting when task-critical deployment constraints demand higher accuracy or smaller models as for
example, under tighter memory budgets or constrained environments (as we'll see on the 4080).

### RTX 4080 (16GB of VRAM)

Next, let's move to a more accessible GPU, especially in these memory-challenged times. The biggest
stumbling block for the 4080 is its 16GB of VRAM, which is not sufficient to support the "magical"
~4b quantizations for a 30B model. How convenient!This "avoids" the 5090's ~4b sweet
spot and forces a more "real-world" comparison under a hard VRAM budget. The figure below shows TPS versus
normalized accuracy for all models that fit on the 4080.

![RTX 4080 performance: tokens per second vs quality](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/images/averagen_bubble_chart_bpw_size_4080.png)


RTX 4080: Tokens per second vs quality (bubble size = model footprint)
Tap *Show Legend* below for model details.




RTX 4080: Tokens per second vs quality (bubble size = model footprint)
Hover over the bubbles, or click *Show Legend* below, for model details.


Show Legend

| # | Model | Acc | TPS | BPW |
| --- | --- | --- | --- | --- |
| ByteShape | | | | |
| GPU-1 | 2.69bpw | 0.9424 | 243.68 | 2.69 |
| GPU-2 | 2.75bpw | 0.9548 | 238.24 | 2.75 |
| GPU-3 | 3.02bpw | 0.9583 | 230.61 | 3.02 |
| GPU-4 | 3.29bpw | 0.9735 | 225.26 | 3.29 |
| GPU-5 | 3.63bpw | 0.9774 | 221.32 | 3.63 |
| GPU-6 | 3.87bpw | 0.9866 | 214.81 | 3.87 |
| Unsloth | | | | |
| 1 | TQ1\_0 | 0.8503 | 229.00 | 2.12 |
| 2 | IQ2\_M | 0.9659 | 214.79 | 2.84 |
| 3 | Q2\_K | 0.9390 | 216.12 | 2.95 |
| 4 | Q2\_K\_L | 0.9470 | 216.24 | 2.97 |
| 5 | Q2\_K\_XL | 0.9665 | 212.41 | 3.09 |
| 6 | IQ3\_XXS | 0.9778 | 213.06 | 3.38 |
| 7 | Q3\_K\_S | 0.9654 | 193.66 | 3.48 |
| 8 | Q3\_K\_XL | 0.9787 | 196.42 | 3.62 |
| 9 | Q3\_K\_M | 0.9759 | 207.84 | 3.85 |

On the RTX 4080, ByteShape consistently outperforms Unsloth under the same 16 GB VRAM constraint,
delivering a better TPSâquality tradeoff.

In particular, ByteShape's highest-quality model that fits,
`IQ4_XS-3.87bpw [IQ-6]`
(3.87 BPW, 214.81 TPS, 98.66% accuracy) delivers:

* a 1.59Ã lower error rate and 9.4% higher TPS vs. `Unsloth Q3_K_XL [8]` (3.62 BPW, 196.42 TPS,
  97.87% accuracy).
* a 2.54Ã lower error rate at the same TPS vs. `Unsloth IQ2_M [2]` (2.84 BPW, 214.79 TPS,
  96.59% accuracy).

As we move to higher throughput, ByteShape's maintains accuracy, while Unsloth's error rate experiences a cliff.

### The Elephant in the Room: When 3-bits is not just 3-bits

There is an inconvenient truth hiding in these results. On several setups, around 4 bpw is already
flying, and pushing quantization harder does not make things faster. It just manages to be smaller
and slower at the same time.

Reducing the size of data doesn't automatically speed things up. While using fewer bits to store each
number seems like it should reduce memory traffic and speed up computation, GPUs don't work that way.
NVIDIA GPUs process work in fixed groups of 32 threads called "warps," which move through instructions
together in near lock-step. The GPU hardware is optimized for specific data formats, memory access patterns,
and operations that the chip's circuits are physically designed to handle efficiently. When your workload
matches these "golden paths", you get peak performance. Step outside them, and you hit slowdowns. This isn't
a design flaw, it's a deliberate tradeoff. Supporting more flexibility would require additional circuitry:
more wires, more transistors, more complexity. That extra hardware consumes more power and adds latency to
every operation, whether a program needs that flexibility or not.

Here a few examples of relevant hardware "quirks": VRAM is read in aligned 32-byte blocks, so reading one
or 32 bytes consumes the same memory bandwidth. Both on-chip and off-chip memories can also suffer contention
depending on how data is laid out, meaning that a warp's accesses may complete in a single step or, in the
worst case, be serialized into 32 steps. And of course, decoding quantized values before computation can
require extra instructions, with the cost depending on the quantization scheme.

This explains the behaviour we observe: 4-bit kernels use VRAM bandwidth more efficiently than 3- or 2-bit
kernels and require fewer decode steps before computation. At the same time, 4-bit kernels exploit subword
parallelism just as effectively as lower-bit kernels, and all rely primarily on dynamic caches rather than
shared memory to take advantage of data reuse when possible.

So why llama.cpp hasn't been optimized to deliver peak speed for **every** bit-length? Our understanding
is that llama.cpp prioritizes **portable, space-efficient quantization** that can run across a
wide range of hardware. That design goal limits how aggressively backends can reshape data layouts or reorder
computation in ways that might help one GPU or one bit-width.

A key example is its choice to store quantized weights in fixed blocks of 256 values. Each block is
self-contained (it carries everything needed to decode it) and sits at a simple, predictable offset in the
tensor, which makes the format easy to implement and fast to locate.

The tradeoff is that GPUs often need to **decode many blocks in parallel** to keep their wide
compute units busy. With many independent 256-value blocks, those parallel decodes can translate into more
scattered or fragmented VRAM reads and extra decode overhead, reducing bandwidth efficiency, especially for
some lower-bit formats.

**Point for example on RTX 5090:** a matrix multiply [256, 768] Ã [768, 2048] takes
**~54Âµs with** `iq4_xs`datatype, but **~62Âµs with** 
`iq3_xxs`(mul\_mat\_q()+mul\_mat\_q\_stream\_k\_fixup()). In other words,
**cutting nearly 1.2 bits per weight** (a reduction of more than 25% in weight footprint) leads
to a **~13% slowdown**, directly hurting user experience.

An excellent reminder that datatype learning matters: Heuristics can get us part of the way, but not all
the way. ShapeLearn makes deliberate, per-tensor datatype choices that improve speed without sacrificing accuracy.

Methodology (brief recap)
-------------------------

If you're wondering how we are scoring these points, the full methodology is discussed in our previous
[blog post](https://byteshape.com/blogs/Qwen3-4B-I-2507/). This post is intentionally focused on the curves and
device tradeoffs, so here is the quick version.

For each quantized variant, we measure **throughput (TPS)** on the target device and
compute a single **normalized quality** score relative to the **BF16 baseline**,
using the same evaluation harness and prompts as the methodology post. The quality score aggregates
standard benchmarks (MMLU, GSM8K, IFEval, LiveCodeBench V4) into one number so you can compare points
directly. In other words, every dot in the plots answers two questions: how fast does it run on this
device, and how much quality does it retain compared to BF16, with memory fit as the first constraint.

We also want to thank all for the many, excellent suggestions on our recent Reddit post for improving
and extending this evaluation strategy, and weâre actively working through them. Right now, evaluation
is the main bottleneck and not datatype learning/quantization.
Careful evaluation is essential to clearly communicate the strengths of each model.

Wrapping up
-----------

**First, thank you for your tenacity.** You made it through all of this without giving up.
We are sincerely flattered!

**The takeaway is simple:** treat **memory as a constraint, not a goal**. Once
a model fits on your device, what matters is the tradeoff curve, **TPS versus quality**.
Across CPUs and GPUs, **ByteShape** consistently lands on the better side of that curve,
delivering either **more speed at the same quality** or **higher quality at the same
speed**.

If you're deploying on a **Raspberry Pi 5 (16 GB)** and want a genuinely
interactive experience, start with
`Q3_K_S-2.70bpw [KQ-2]`
. On larger CPUs or GPUs, you can move up the curve toward higher-quality points with
little loss in throughput, the same rule applies:
**fit first, then optimize the tradeoff**.

We'll keep releasing more device-targeted variants (and more plots). If your system can't run a 30B
model smoothly, don't blame the model or the silicon. **Blame the datatypes.**