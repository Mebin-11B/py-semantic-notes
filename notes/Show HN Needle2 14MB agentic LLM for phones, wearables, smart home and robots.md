---
title: "Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots"
url: https://cactuscompute.com/needle
clipped: 2026-08-31 12:22:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots](https://cactuscompute.com/needle)

## Digest Summary
Needle 2 is a 14 MB, 45 M‑parameter LLM designed for ultra‑low‑cost edge devices (&lt; $200) that lack GPUs/NPUs and have only a few hundred megabytes of RAM. Its architecture focuses on function‑call grounding: user utterances are mapped to typed API calls rather than generating open‑ended text, allowing a small model to handle device control, document extraction, and structured output tasks. Each interaction is constrained by a byte‑level grammar derived from declared schemas; an empty call signals refusal, and a learned confidence score determines whether to act locally or defer to a cloud model. The model is trained with lossless 2‑bit quantization (Cactus Quants) from pre‑training through KV‑cache, preserving accuracy while fitting into 14 MB. Deployment consists of a single, dependency‑free C++ binary that auto‑selects optimal kernels across Cortex‑M, x86, and WebAssembly platforms. Fine‑tuning can be performed on a standard Mac/PC using provided Python tools, enabling customization to device‑specific vocabularies.

---

## Full Article

# Cactus NeedleAgentic LLM for tiny devices

An open 14MB model for tool calling, device use, and structured extraction.Needle 2 Sandboxloading model...Defined toolsDefined tools · 3 toolsQueryRunTry an exampleSmart home2 calls · parallelRobot3-step sequenceGallery2-step chainDevice control3 browser actionsExtract → emailstructured callCurrencylive APIDocumentfield extractionSentimentclassification12 toolsroutingRepeated callssame tool · 2 callsArray argument1 batched callFlightform fillingOff-topicempty call · refusalAction previewno actionModel loading…Result `` 45MParams800+ tok/sPi5 prefill500+ tok/sPi5 decodeCQ2-bitCompression14 MBFile size28 MBSession RAM

### Size–quality frontier: mobile-class and below

Figure 1. Ordered strict exact match on Mobile-Actions (google/mobile-actions eval split, 961 rows) against total parameters, over the smallest models designed for smart devices, mobile and below. Needle 2 is measured end-to-end through the shipped binary at CQ2-bit deployment precision with tool retrieval on; baselines run the released checkpoints under vLLM, and Apple FM runs on-device.

## Our Bet

Bringing On-Device AI to <$200 Devices: Edge AI has lately meant Macs and PCs, but the true edge is mostly cheap hardware: there are more than 21 billion IoT devices against roughly 1.5 billion PCs. Most phones in emerging markets ship under $200. Count budget phones, Raspberry Pis, microcontrollers, wearables, small robots like Reachy Mini, and connected home devices - and roughly four in five edge devices cost under $200. That is the hardware Needle targets: no GPU, no NPU, a few dozen MB of RAM.

Function Call & Device Use: Turning on a light does not need a frontier model. Smartwatches, home assistants and robots already expose their abilities as functions with typed parameters, so the only hard part is mapping a messy sentence onto them: which function, and which arguments. Framed that way, the problem needs no world knowledge and no open-ended prose. That is why 45M parameters suffice whereas chat requires billions. That smaller formulation is the bet everything else follows from.

Extraction & Structured Outputs: Needle treats extraction as another form of tool calling. With a schema and a document, it returns typed fields: enums for classification, arrays for lists, and objects for structured records. We compile grammar from the schema, preventing malformed JSON and invalid structures. This way, the model focuses its 45M parameters on choosing the right values and grounding them in the user's words.

Edge-Cloud Collaboration: No small model is perfect, and Needle says so instead of guessing. Off-topic requests return an empty call, and every response carries a learned confidence score. Set your own confidence threshold: act above it, ask again, or escalate to the cloud below it. Most device use requests can be handled locally, so escalation is rare and the default path remains private, fast, and free.

Lossless 2bit Quantization: Small models break under post-hoc quantization, so we never quantize post-hoc: Needle 2 trains against Cactus Quants from pretraining through post-training – weights, activations, and KV cache alike. The 2bit model you deploy is the model that was trained. That is what fits 45M parameters into 14MB with nothing lost on our benchmarks.

Co-designed Model & Inference: Every architectural element was benchmarked on the target hardware before it earned its parameters. This is why we don't just ship the weights – we package a single dependency-free C++ binary that probes the CPU at startup and picks its kernels, with the model, tokenizer, and grammar compiler sealed inside. One artifact runs from Cortex-M to x86 to WebAssembly. There is nothing extra to install or to download.

Fine-tune on your Mac/PC: Every product has its own tool vocabulary, and a 45M model is small enough to retrain where it runs: the repo and python package tune and test on your own computer in minutes to a few hours. Ship a Needle that speaks your device's tools, not a generic assistant.

## Production

Needle is production-ready for products that require a minimal RAM footprint, low latency, privacy, and offline reliability. Pebble - the pioneer of the modern wearable industry - runs it locally in the Index 01 app to turn spoken requests into actions without depending on a network connection.“

The Pebble Index Ring has no screen. So when you speak to it, the action just has to happen, every time, with or without internet connection. We run Cactus Needle locally in the app, instead of relying on the cloud. The model's footprint is tiny and the performance never lets us down.

## Architecture

### The Simple Attention Network

Figure 2. The Simple Attention Network. Each block carries its update rule. Here x̂ is the RMS-normalised flattening of the four residual streams, H the orthonormal Walsh-Hadamard transform—a fixed matrix, applied in n log n time with no weights to read—(kᵢ, vᵢ) rows gathered from hashed n-gram tables, and P the doubly-stochastic normalisation of the routing logits A, computed by Sinkhorn iteration; a, b, g and all σ-gates are learned and input-dependent. Both attention and MLP residuals are sandwich-normed and gated, the engram sites fire at two layers, and decoding is constrained by a byte-level grammar compiled from the declared schemas.

Needle 2 is pretrained on a proprietary 115B-token corpus and post-trained on 38B tokens with compact reasoning traces and careful dataset distribution design. For scale: LFM2.5-230M was pretrained on 19 trillion tokens, roughly 120× Needle's total, and the evaluation below shows the two trading wins. Each component exists to buy capability without buying bandwidth:
- The Hadamard MLP replaces the usual dense up-and-down projections with a fixed Walsh transform and learned diagonals, so the channel mixing that dominates a small model's weight reads costs almost no parameters at all.
- The engram moves world knowledge out of the stack into hashed n-gram tables that are read a few rows per token: capacity that is nearly free at decode time, which matters on devices where every megabyte read from flash is latency and battery.
- The multi-lane residual streams give a 27-layer, 512-wide network the routing flexibility of a much wider one, at the cost of a few dot products per layer rather than more attention or MLP volume.

The memory system is designed backwards from fixed-RAM devices. Attention uses a 256-token sliding window so the KV cache is bounded no matter how long a session runs, and the system prompt and tool declarations are pinned as permanent sinks so the one thing a tool-calling model must never forget — its tools — is structurally unable to be evicted. The cache itself is trained with QAT, and weights are stored in Cactus Quants at a mixed bits per weight averaging 2bit. The result is that quality decisions and deployment decisions stay decoupled: one trained model, specialized to whatever precision and window a target device can afford.

The engine earns its speed from what it refuses to compute. Weights never decompress into RAM: the 2-bit codes are expanded inside vector registers, fused into integer dot products, so resident memory stays at blob size and the arithmetic path is int8 end to end—activations, KV cache, and the lane routing tables alike. The grammar is an optimization, not just a guarantee: because the matcher knows which tokens are legal before the logits exist, the engine computes output scores only for candidate rows, skipping up to 98% of the vocabulary projection on structural tokens, and skips it entirely on steps whose output is already forced. One universal binary probes the CPU at startup and self-selects its kernel tier—SDOT, NEON, AVX2, RISC-V vectors, wasm SIMD, or scalar—and the thread pool spins through the short serial sections of a token instead of sleeping, which alone nearly doubled decode. None of this changes a single output: every trick is either exact or validated token-for-token against the reference path.

All of it is ultimately an energy argument. On device silicon, moving a byte out of flash or DRAM costs orders of magnitude more than a multiply-accumulate, so the budget that matters is FLOPs per token and bytes per token together. The architecture cuts the first: a conventional transformer of Needle's width and depth spends 164 MFLOPs per token, and even one squeezed down to Needle's parameter count spends 87, because every parameter it owns must be exercised through a matmul. Needle spends 70, and keeps a fifth of its parameters as gathered memory that costs no arithmetic at all. The binary cuts the second, as the engine section showed: nothing rematerializes, the arithmetic stays int8 end to end, and the grammar prunes compute outright, so decoding a token reads at most the 14MB blob once, and on structural tokens meaningfully less. This is what battery life is made of. Even on a high-end phone, an always-on assistant lives inside a power budget; every MFLOP is milliwatt-hours, and Needle spends 7× to 85× fewer of them per token than the models it is benchmarked against.

### Compute per token

ModelParamsMatmul-activeMFLOPs / tokenNeedle 245M35M70Same-shape transformer, dense MLP82M82M164Transformer at matched params43M43M87LFM2.5 230M230M230M460FunctionGemma 270M270M270M540Apple FM~3B~3B~6,000Counting 2 FLOPs per multiply-accumulate over matmul-active parameters, with embeddings tied in all rows; attention terms are equal across rows at matched context and excluded. The gap between Needle's two columns is the engram: 8M parameters read by gather, costing no arithmetic. Baseline rows count every parameter as matmul-active, which is exact for both: LFM2.5's eight short-conv blocks hold their parameters in dense gate and projection matmuls that run every token—the depthwise conv kernels themselves are negligible—and what short convolutions save is the context-dependent attention term, already excluded for every row. Tied embeddings count once as the output head. FunctionGemma's 540 is dominated by that head: 170M of its 270M parameters are a 262k-token embedding table.

Bounded session memory is what puts microcontrollers in reach. Because the sliding window caps state, Needle 2's RAM is a deterministic 28MB ceiling, not a curve that grows with conversation length. That fits MCU-class parts with external RAM, such as ESP32-P4 with 32MB of PSRAM, or STM32H7 and NXP i.MX RT boards with SDRAM. The engine compiles single-threaded for bare metal and ships as a static library for Cortex-M4, M7, and M55.

## Evaluation

We evaluate on five public function-calling benchmarks: Google's Mobile Actions, DroidCall, the Seal-Tools in-domain and out-of-domain tests, and BFCL v4 single-turn. Scoring is ordered strict exact match: a row passes only if the function names, the call order, and every argument value match. All Needle 2 numbers are measured end-to-end through the shipped C++ engine in its production configuration: CQ2-bit weights, tool retrieval on, and the 256-token sliding KV window. Nothing is relaxed for benchmarking; the numbers reflect the exact engine a device runs, window eviction included. Baselines run the released checkpoints under vLLM at full context, and Apple FM runs on-device.

Two asymmetries make this comparison hard, and we state both upfront. Precision: the baselines stay at f16 deliberately, because conventional post-training quantization to 2 bits collapses models that were never trained for aggressive compression, while Cactus Quants is baked into Needle's training from the ground up. That skew favors the baselines. Scope: Needle is trained specifically for agentic tool calling and nothing else, while every baseline is a general language model carrying chat, prose, and world knowledge alongside its tool calling. That skew favors Needle. There is no clean way to level both at once, so we do not try. The tables answer one narrow question: which model executes tool calls correctly within an on-device budget. We accept the skew; it still paints the picture we intend.

### Mobile Actions (961 rows)

ModelAccuracyName acc.Non-empty1-call2-callLFM2.5 230M (f16, vLLM)69.193.098.976.155.0FunctionGemma 270M (f16, vLLM)64.087.398.973.046.2Needle 2 (CQ2-bit)63.798.399.471.348.4Apple FM (on-device)57.694.295.564.543.8Google Mobile Actions eval split, ordered strict exact match; function names, call order, and every argument must match.

### DroidCall test split (200 rows)

ModelAccuracyName acc.Non-empty1-call2-callFunctionGemma 270M (f16, vLLM)17.537.559.522.70.0Needle 2 (CQ2-bit)17.036.547.522.10.0LFM2.5 230M (f16, vLLM)11.021.522.514.30.0Android intent-style function calls, ordered strict exact match; 1-call rows n=154, 2-call rows n=24.

### Seal-Tools in-domain (700 rows)

ModelAccuracyName acc.1-call2–3-call4+-callNeedle 2 (CQ2-bit)32.664.963.021.814.6LFM2.5 230M (f16, vLLM)26.945.454.517.110.4FunctionGemma 270M (f16, vLLM)16.356.047.04.52.1Large candidate tool lists with a majority of multi-call rows.

### Seal-Tools out-of-domain (654 rows)

ModelAccuracyName acc.1-call2–3-call4+-callNeedle 2 (CQ2-bit)28.758.756.427.115.4LFM2.5 230M (f16, vLLM)17.035.042.613.79.8FunctionGemma 270M (f16, vLLM)15.648.950.011.06.3Entire tool domains are held out of training, testing schema generalization.

Needle was not trained for general function calling: its corpus is consumer device actions—smart home, mobile, wearables, TV, car—plus structured extraction, and BFCL's general-purpose and enterprise API surfaces, including the Java and JavaScript SDK categories, sit entirely outside that distribution. It extrapolates nonetheless: on Python simple calls it lands within a point of FunctionGemma, a model six times larger trained for exactly this task, and it keeps a 93.4 well-formed rate across all 3,641 rows. The gap concentrates where its training data has never been: Java, JavaScript, and the parallel multi-call categories.

### BFCL v4 single-turn (3,641 rows)

CategoryApple FMon-deviceLFM2.5 230Mf16 · vLLMFunctionGemma 270Mf16 · vLLMNeedle 2CQ2-bitSimple73.363.248.140.8— Python86.885.562.361.2— Java67.048.038.029.0— JavaScript66.056.044.032.0Multiple84.078.560.057.0Parallel65.064.036.530.0Parallel multiple52.051.530.522.5Live simple70.545.033.736.8Live multiple45.947.825.227.9Live parallel50.043.818.825.0Live parallel multiple58.345.825.029.2Relevance100.068.881.281.2Irrelevance28.377.772.160.8Overall61.760.846.142.6Well-formed rate95.094.2100.093.4Official BFCL v4 single-turn scorer. Overall is the collector's unweighted mean over all 13 raw categories; bold values mark the best result in each row.

## Fine-tuning

Every number so far was reported for the base model: one generic checkpoint, measured on benchmarks it never saw. This evaluates Needle on real-world, "hard" tasks. But Needle is meant to be fine-tuned - and you can do this locally, on your own laptop. Let's see how Needle's performance improves when we fine-tune it for a given task:

### Needle 2 base vs. fine-tuned

- Needle 2 base
- FunctionGemma 270M
- LFM2.5 230M
- DeepSeek V4 Flash
- Needle 2 fine-tunedFigure 3. Needle 2 before and after fine-tuning, next to other small-model baselines as well as DeepSeek V4 Flash.[Get Started with Fine-Tuning](https://cactuscompute.com/dashboard)

Fine-tuning lifts accuracy by 21 to 58 points and puts Needle 2 ahead of DeepSeek V4 Flash, a frontier cloud model, on three of the four benchmarks. The reason is narrow scope: your product exposes a fixed, limited set of tools, so a small specialist model trained on exactly those tools beats a large generalist one.

You can do the same for your own environment. Supply your own data (or generate synthetic traces), run  `needle finetune`  and export the resulting  `.cact`  file. Get started below.

Explore Needle 2[Hugging Face](https://huggingface.co/Cactus-Compute/needle-2)[GitHub](https://github.com/cactus-compute/needle)[Research paper](https://arxiv.org/abs/2607.18363)

## Building on-device actions into hardware?

Needle is Apache 2.0-licensed. For custom tool schemas, hardware tuning, and post-training, we'd love to talk.[Talk to us](https://calendly.com/roman-cactuscompute/intro-cactus-hybrid-cloud)[Read the docs](https://github.com/cactus-compute/needle)
