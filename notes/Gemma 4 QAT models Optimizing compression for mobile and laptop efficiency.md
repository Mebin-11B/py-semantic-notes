---
title: "Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency"
url: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
clipped: 2026-06-17 00:52:00
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)

## Digest Summary
Gemma 4, released two months ago, now includes checkpoints optimized with Quantization‑Aware Training (QAT). QAT simulates quantization during training, minimizing quality loss compared with standard Post‑Training Quantization (PTQ). The update provides:

- QAT models for the widely used Q4_0 quantization format, delivering higher overall quality than PTQ baselines.
- A new mobile‑specialized quantization schema applied to the edge models (E2B and E4B), reducing the Gemma 4 E2B checkpoint to a 1 GB memory footprint, enabling deployment on consumer GPUs and edge devices.
- Approximate VRAM requirements for loading each model (details omitted), demonstrating significant reductions in both VRAM and storage.

The release follows earlier enhancements, including Multi‑Token Prediction (MTP) for faster inference and a 12 B model positioned between the 4 B and 26 B MOE variants. Overall, QAT‑trained checkpoints preserve Gemma 4’s capabilities while substantially lowering hardware requirements.

## Discussion Summary
The comments show strong enthusiasm for recent Gemma releases, especially the quantized models that enable 12‑billion‑parameter inference on modest GPUs and even phones, with many noting impressive speed, low VRAM usage and successful multimodal experiments. At the same time, several contributors express skepticism about the practical utility of smaller instruction‑tuned models, citing limited capabilities, lack of robust agents for tasks like web browsing, and concerns about hardware demands. There is also curiosity about Google’s partnership with Apple and a desire for broader model availability and documentation.

---

## Full Article

Since releasing [Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) two months ago, we've been continuously working to expand its capabilities. First, we introduced [Multi-Token Prediction](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) (MTP) to accelerate inference, and just a couple of days ago, we released [a 12B model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) to bridge the gap between our E4B and 26B MOE models.

Today, we are releasing new checkpoints optimized with Quantization-Aware Training (QAT) to make Gemma 4 even more efficient, so you can run models locally on everyday edge devices and consumer GPUs.

By simulating quantization during training, QAT minimizes quality loss when the model is compressed. This release includes QAT checkpoints for the popular Q4\_0 quantization format as well as a novel quantization format specialized for mobile use cases. Using this mobile format, we’ve reduced the memory footprint of Gemma 4 E2B to 1GB. Together, these dramatically reduce memory requirements while preserving the capabilities and quality you expect from Gemma 4.

**Keeping model quality while making them smaller**
---------------------------------------------------

Quantization is a key technology to run models on consumer hardware by reducing their memory footprint while also accelerating decode speed. However, standard Post-Training Quantization (PTQ) often leads to performance degradation. Instead of simply quantizing the model after training, QAT integrates the quantization process directly into training. While PTQ is already effective at preserving quality, our QAT results yield even higher overall quality compared to standard PTQ baselines.

We applied this QAT recipe to the popular Q4\_0 format to maximize performance for all the models. For the edge models (E2B and E4B), we rethought how we approach quantization with a special mobile-specialized quantization schema.

**Saving on VRAM and Storage**
------------------------------

Below are the approximate memory requirements indicating how much VRAM is required to load the models: