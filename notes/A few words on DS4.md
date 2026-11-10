---
title: "A few words on DS4"
url: https://antirez.com/news/165
clipped: 2026-06-17 01:02:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A few words on DS4](https://antirez.com/news/165)

## Digest Summary
DS4 (DwarfStar 4) quickly gained popularity as a single‑model, locally integrated AI solution. Its success stems from the availability of a large, fast “quasi‑frontier” model—DeepSeek v4 Flash—combined with an aggressive 2‑bit/8‑bit quantization that allows inference on systems with 96–128 GB RAM. The author reports intense development effort (≈14 h/day) and notes that DS4 now handles tasks previously reserved for cloud services like Claude or GPT, especially when enhanced with vector steering. Future directions include: updating the core model to newer checkpoints (potentially domain‑tuned versions for coding, legal, medical), expanding quality benchmarks, adding a coding agent, establishing a home CI hardware setup for long‑term testing, increasing platform ports, and implementing distributed inference (serial and parallel). The author emphasizes that AI should not remain solely a provided service and thanks the community for support.

## Discussion Summary
Comments highlight strong interest in DwarfStar4’s ability to run DeepSeek 4 locally, noting impressive long‑context reasoning, tool‑calling reliability, and coding assistance that some users find comparable to proprietary models. Many point out the high VRAM and memory requirements, questioning practicality on commodity hardware and the value of a model‑specific engine versus broader llama.cpp integrations. Comparisons with other open‑weight models such as Qwen 3.6 reveal mixed performance and efficiency trade‑offs. Overall sentiment blends enthusiasm for the technical progress with cautious concern about resource demands and future relevance.

---

## Full Article

[antirez](https://antirez.com/user/antirez) 32 days ago. 188940 views. 

```
I didn’t expect DwarfStar 4 (https://github.com/antirez/ds4) to become so popular so fast. It is clear that there was a need for single-model integration focused local AI experience, and that a few things happened together: the release of a quasi-frontier model that is large and fast enough to change the game of local inference, and the fact that it works extremely well with an extremely asymmetric quants recipe of 2/8 bit, so that 96 or 128GB of RAM are enough to run it. And, of course: all the experience produced by the local AI movement in the latest years, that can be leveraged more promptly because of GPT 5.5 (otherwise you can’t build DS4 in one week — and even with all this help you need to know how to gently talk to LLMs).

The last week was funny and also tiring, I worked 14 hours per day on average. My normal average is 4/6 since early Redis times, but the first few months of Redis were like that.

So, what’s next? Is this a project that starts and ends with DeepSeek v4 Flash? Nope, the model can change over time. The space will be occupied, in my vision, by the best current open weights model that is *practically fast* on a high end Mac or “GPU in a box” gear (like the DGX Spark and other similar setups). I bet that the next contender is DeepSeek v4 Flash itself, in the new checkpoint that will be released and, hopefully, a version specifically tuned for coding, and who knows, other expert-variants (not in the sense of MoE experts) maybe. For local inference, to have a ds4-coding, ds4-legal, ds4-medical models make a lot of sense, after all. You just load what you need depending on the question.

It is the first time since I play with local inference (I play with it since the start) that I find myself using a local model for serious stuff that I would normally ask to Claude / GPT. This, I think, is really a big thing. It is also the first time that using vector steering I can enjoy an experience where the LLM can be used with more freedom. DeepSeek v4 Flash is really an impressive model, no doubt about that. If you can imagine in your mind the small good local model experience as A, and the frontier model you use online as B, DS4 is a lot more B than A. I can’t wait for the new releases, honestly (btw, thank you DeepSeek).

So, after those chaotic first days, I hope the project will focus on: quality benchmarks, potentially adding a coding agent that is also part of the project, a hardware setup here in my home that can run the CI test in order to ensure long term quality, more ports, and finally but as a very important point: distributed inference (both serial and parallel).

For now, thank you for all the support: it was really appreciated :) AI is too critical to be just a provided service.
```