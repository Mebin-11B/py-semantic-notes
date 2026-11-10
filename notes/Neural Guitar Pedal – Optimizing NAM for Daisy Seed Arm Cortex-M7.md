---
title: "Neural Guitar Pedal – Optimizing NAM for Daisy Seed Arm Cortex-M7"
url: https://www.tone3000.com/blog/running-nam-on-embedded-hardware
clipped: 2026-06-17 01:37:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Neural Guitar Pedal – Optimizing NAM for Daisy Seed Arm Cortex-M7](https://www.tone3000.com/blog/running-nam-on-embedded-hardware)

## Digest Summary
- NAM (Neural Amp Modeler) was adapted from a desktop plugin to run on embedded platforms such as the Electrosmith Daisy Seed (ARM Cortex‑M7).  
- The original NeuralAmpModelerCore library assumed ample RAM, an OS, and no real‑time deadline, leading to excessive latency (≈5 s to process 2 s of audio) on the Daisy Seed.  
- Three primary obstacles were identified: (1) model size exceeding embedded memory limits, (2) inefficient small‑matrix operations in Eigen, and (3) costly parsing of the JSON‑based .nam format on a constrained device.  
- Solutions implemented: profiling to locate bottlenecks; custom matrix‑multiplication routines optimized for NAM’s fixed‑size matrices; a compact binary model format (.namb) generated on a companion PC/phone and transferred via Bluetooth or USB; and replacing tanh with ReLU activation in the A1‑nano model to reduce computation.  
- After optimization, processing time dropped to ≈1.5 s for 2 s of audio, providing headroom for additional effects. The findings informed the design of Architecture 2, including a “Slimmable NAM” concept that dynamically adjusts compute load. Source code and tools for these optimizations have been released publicly.

## Discussion Summary
The comments convey strong enthusiasm for the technical challenge of adapting the Neural Amp Modeler DSP to run real‑time inference on the Daisy Seed’s ARM Cortex‑M7 processor. They highlight hands‑on work such as crafting custom GEMM kernels for small matrices and examining generated assembly, indicating appreciation for low‑level optimization and the satisfaction derived from detailed code analysis. The overall tone is positive and focused on the intricacies of performance tuning.

---

## Full Article

NAM has come a long way from its origins as a desktop plugin. Today it runs on single-board computers, guitar pedals like the [Darkglass Anagram](https://www.tone3000.com/blog/unveiling-anagram-darkglass-electronics), and even [web browsers](https://www.tone3000.com/blog/introducing-the-nam-web-player). As we work on [Architecture 2](https://www.tone3000.com/blog/a2-next-generation-neural-amp-modeler) — our next-generation NAM architecture built specifically to run on more hardware — we wanted to go hands-on and understand exactly what embedded NAM deployment looks like in practice.

So we built a NAM loader for the [Electrosmith Daisy Seed](https://daisy.audio/hardware/Seed/): an ARM Cortex-M7 board that's become a popular foundation for DSP-based audio products, from eurorack modules to commercial guitar pedals.

Here's what we found...

The challenge: NeuralAmpModelerCore wasn't designed for this
------------------------------------------------------------

The NeuralAmpModelerCore library has been battle-tested in the NAM plugin — but that plugin runs on a desktop with gigabytes of RAM, an operating system, and no hard deadline on how long processing can take. Embedded hardware is a completely different world: tight memory limits, no OS, and a strict real-time budget that audio simply cannot exceed.

When we first ran our implementation on the Daisy Seed, using a model small enough to fit on the device (A1-Nano with the tanh activation replaced by ReLU) , processing 2 seconds of audio took over 5 seconds of compute time. For a guitar pedal, that's obviously a non-starter.

The problems broke down into three areas: model size (neural networks carry a memory footprint that needs to fit within embedded constraints), compute efficiency (the linear algebra library the codebase relies on wasn't optimized for the small matrix sizes NAM actually uses), and model loading (parsing the standard .nam JSON format on a device with no OS and very limited RAM is harder than it sounds).

What we did about it
--------------------

We started by profiling the code to understand exactly where time was being spent, rather than guessing. The main bottleneck turned out to be [Eigen](https://eigen.tuxfamily.org/) — specifically, how it handles matrix multiplications for small, fixed-size matrices, which is exactly what NAM inference uses. We added specialized routines tuned to the matrix sizes that actually appear in NAM models, alongside several other targeted improvements.

For the loading problem, we developed a new compact binary model format (which we called “.namb”) designed as a drop-in alternative to .nam for use on embedded devices. The idea is that a companion app — running on your phone or desktop — converts .nam files from the TONE3000 library into the compact format, then transfers them to the device over Bluetooth or USB. No model conversion, no quality loss, just a leaner representation that works within the device's constraints.

For this initial exploration, we used a smaller model variant (A1-nano) with a ReLU activation function in place of tanh, a well-established swap that cuts compute cost significantly. (If you want the full technical breakdown of all of this, including what we tried that didn't work, check out our engineering post.)

Results
-------

After optimization, the same model that originally took over 5 seconds to process 2 seconds of audio now runs in approximately 1.5 seconds — with compute headroom left over for effects processing before and after the NAM block.

More importantly, this work gave us a concrete picture of the embedded NAM problem that directly feeds into A2 design. [Slimmable NAM](https://www.tone3000.com/blog/slimmable-nam-the-future-of-neural-amp-modeler) — our approach to letting a single model adapt its compute requirements to the hardware it's running on — is a direct result of what we learned from our partners and observed in this experiment.

If you are interested in more details on these experiments, we are publishing all of the source code that was developed for them, including:

1. Merging the numerical optimizations directly into [NeuralAmpModelerCore](https://github.com/sdatkinson/NeuralAmpModelerCore/commit/a0c93c0c3934abec0bca80d2e9e592ac86217db4)
2. Publishing the [nam-binary-loader](https://github.com/tone-3000/nam-binary-loader) tools and library
3. Publishing the example Daisy code as a blueprint for the development of other NAM pedals at [nam-pedal](https://github.com/tone-3000/nam-pedal)
4. Detailed discussion of the microbenchmarks, (what worked, what didn't work) at [João's blog](https://jfsantos.dev/blog/nam-a2-embedded)