---
title: "Accelerating Gemma 4: faster inference with multi-token prediction drafters"
url: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
clipped: 2026-06-17 01:07:04
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Accelerating Gemma 4: faster inference with multi-token prediction drafters](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

## Digest Summary
Multi-token prediction (MTP) in Gemma 4 uses speculative decoding to reduce the latency of large‑language‑model inference, which is typically memory‑bandwidth bound. A lightweight “drafter” model generates a sequence of candidate tokens, while the full‑size target model (e.g., Gemma 4 31B) verifies the draft in a single forward pass, simultaneously producing an additional token. This decouples token prediction from verification, allowing idle compute to be used for parallel token generation and cutting the time per output token. Benefits include:
- Lower latency for real‑time chat, voice, and agentic workflows.  
- Faster execution of large dense (31B) and MoE (26B) Gemma 4 models on consumer GPUs and edge devices.  
- No loss in model quality, since the target model performs final verification.  
The approach is positioned as a means to run high‑performance LLMs locally with improved responsiveness and reduced power consumption.

## Discussion Summary
Comments highlight that Gemma 4 models achieve markedly higher token efficiency and inference speed than competing open‑source models, often delivering comparable benchmark performance with a fraction of the compute time. Users report successful integration with llama.cpp, vLLM, Ollama, and Google AI Edge, noting substantial cost and latency benefits for solo developers. However, several remarks mention accuracy trade‑offs, especially in smaller variants, and stress the need for high‑end hardware or quantization challenges. Opinions on Google’s strategy emphasize a focus on compute efficiency over raw performance, generating both praise for rapid progress and caution about deployment constraints.

---

## Full Article

### **Why speculative decoding?**

The technical reality is that standard LLM inference is memory-bandwidth bound, creating a significant latency bottleneck. The processor spends the majority of its time moving billions of parameters from VRAM to the compute units just to generate a single token. This leads to under-utilized compute and high latency, especially on consumer-grade hardware.

Speculative decoding decouples token generation from verification. By pairing a heavy target model (e.g., Gemma 4 31B) with a lightweight drafter (the MTP model), we can utilize idle compute to “predict” several future tokens at once with the drafter in less time than it takes for the target model to process just one token. The target model then verifies all of these suggested tokens in parallel.

### **How speculative decoding works**

Standard large language models generate text autoregressively, producing exactly one token at a time. While effective, this process dedicates the same amount of computation to predicting an obvious continuation (like predicting “words” after “Actions speak louder than…”) as it does to solving a complex logic puzzle.

MTP mitigates this inefficiency through speculative decoding, a technique introduced by Google researchers in [*Fast Inference from Transformers via Speculative Decoding*](https://arxiv.org/abs/2211.17192). If the target model agrees with the draft, it accepts the entire sequence in a single forward pass —and even generates an additional token of its own in the process. This means your application can output the full drafted sequence plus one token in the time it usually takes to generate a single one.

### **Unlocking faster AI from the edge to the workstation**

For developers, inference speed is often the primary bottleneck for production deployment. Whether you are building coding assistants, autonomous agents that require rapid multi-step planning, or responsive mobile applications running entirely on-device, every millisecond matters.

By pairing a Gemma 4 model with its corresponding drafter, developers can achieve:

* **Improved responsiveness:** Drastically reduce latency for near real-time chat, immersive voice applications and agentic workflows.
* **Supercharged local development:** Run our 26B MoE and 31B Dense models on personal computers and consumer GPUs with unprecedented speed, powering seamless, complex offline coding and agentic workflows.
* **Enhanced on-device performance:** Maximize the utility of our E2B and E4B models on edge devices by generating outputs faster, which in turn preserves valuable battery life.
* **Zero quality degradation:** Because the primary Gemma 4 model retains the final verification, you get identical frontier-class reasoning and accuracy, just delivered significantly faster.