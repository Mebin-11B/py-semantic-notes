---
title: "Tinybox – Offline AI device 120B parameters"
url: https://tinygrad.org/#tinybox
clipped: 2026-06-17 01:29:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tinybox – Offline AI device 120B parameters](https://tinygrad.org/#tinybox)

## Digest Summary
tinygrad is a minimalist neural‑network framework that reduces complex models to three core operation types. It generates a custom kernel for each operation, enabling extreme shape specialization, while tensors are lazy, allowing aggressive operation fusion. The backend is deliberately simple—over ten times less complex than typical frameworks—so optimizing a single kernel yields broad performance gains across the library. The project is maintained by tiny corp, which also markets the “tinybox” computer, available in red, green, and an upcoming “exa” variant. The framework’s design emphasizes simplicity, high specialization, and rapid optimization through a streamlined kernel compilation approach.

## Discussion Summary
The comments express widespread skepticism about the hardware’s pricing, performance claims, and target market, questioning whether the devices can run large models efficiently and at useful speeds while noting the high cost compared to DIY alternatives. Concerns recur about lack of customization, limited ordering options, potential overheating, and reliance on a software stack still maturing. Nonetheless, a minority view appreciates the concept of turnkey AI boxes and locally‑trained models, suggesting leasing, colocation, or recycling options, but overall sentiment remains doubtful about value and practicality.

---

## Full Article

---

tinygrad
--------

We write and maintain [tinygrad](https://github.com/tinygrad/tinygrad), the fastest growing neural
network framework

It's extremely simple, and breaks down the most [complex](https://github.com/tinygrad/tinygrad/blob/master/examples/llama.py) [networks](https://github.com/geohot/tinygrad/blob/master/examples/stable_diffusion.py) into 3 [OpTypes](https://github.com/geohot/tinygrad/blob/master/tinygrad/uop/ops.py)

**ElementwiseOps** are UnaryOps, BinaryOps, and TernaryOps.  
They operate on 1-3 tensors and run elementwise.  
example: SQRT, LOG2, ADD, MUL, WHERE, etc...  
  
**ReduceOps** operate on one tensor and return a smaller tensor.  
example: SUM, MAX  
  
**MovementOps** are virtual ops that operate on one tensor and move the data around copy-free.  
example: RESHAPE, PERMUTE, EXPAND, etc...  
  

But how...where are your CONVs and MATMULs? Read the code to solve this mystery.

---

Work at tiny corp
-----------------

We [are now funded](https://geohot.github.io/blog/jekyll/update/2023/05/24/the-tiny-corp-raised-5M.html) and **hiring** full time software engineers. Very talented interns okay.  
  
See [our bounty page](https://docs.google.com/spreadsheets/d/1WKHbT-7KOgjEawq5h5Ic1qUWzpfAzuD_J06N1JwOCGs/edit?usp=sharing) to judge if you might be a good fit. Bounties pay you while judging that fit.  
  
We are also hiring for operations and hardware, but if you haven't contributed to tinygrad your application won't be considered.

---

tinybox (now shipping)
----------------------

![](https://tinygrad.org/assets/tinybox.jpg)

We sell a computer called the tinybox. It comes in red, green, pro, and soon, exa.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **red v2** | **green v2 blackwell** | **exabox** |
| FP16 (FP32 acc) FLOPS | 778 TFLOPS | 3086 TFLOPS | ~1 EXAFLOP |
| GPU Model | 4x 9070XT | 4x RTX PRO 6000 Blackwell | 720x RDNA5 AT0 XL |
| GPU RAM | 64 GB | 384 GB | 25,920 GB |
| GPU RAM bandwidth | 2560 GB/s | 7168 GB/s | 1244 TB/s |
| GPU link bandwidth | full fabric PCIe 4.0 x16 | full fabric PCIe 5.0 x16 | full fabric 400 GbE |
| CPU | 32 core AMD EPYC | 32 core AMD GENOA | 120x 32 core AMD GENOA |
| System RAM | 128 GB | 192 GB | 23,040 GB |
| System RAM bandwidth | 204.8 GB/s | 460.8 GB/s | 55.2 TB/s |
| Disk size | 2 TB fast NVMe | 4 TB raid + 1 TB boot | 480 TB raid |
| Disk read bandwidth | 7.3 GB/s | 59.3 GB/s | 7.1 TB/s |
| Networking | 2x 1GbE + OCP3.0 | 2x 10GbE + OCP3.0 PCIe5 | 3.2 TB/s scale out |
| Noise | < 50 dB, 31 low speed fans | | 65 db @ 10 meters |
| Power Supply | one 1600W, 100V~240V | 2x 1600W, 100V~240V | 600 kW, 200V~240V |
| BMC | AST2500 | AST2600 | custom |
| Operating System | Ubuntu 24.04 | | |
| Dimensions | 12U, 16.25" deep, 60-90 lbs | | 20x8x8.5 ft, 20,000 lbs |
| Rack? | Freestanding or rack [mount](https://rackmountmart.store.turbify.net/26slidrailfo.html) | | concrete slab |
| Driver Quality | Good | Great | functions as single GPU |
| SHIPPING | [IN STOCK](https://tinycorp.myshopify.com/products/tinybox-red-v2) | [MADE TO ORDER](https://tinycorp.myshopify.com/products/tinybox-green-v2-with-4x-rtx-pro-6000-blackwell) | [PREORDER FOR 2027](https://tinycorp.myshopify.com/products/exabox-preorder) |

  

more [products on the shop](https://tinycorp.myshopify.com/). for updates on products and inventory, [sign up for the mailing list](https://tinycorp.myshopify.com/pages/mailing-list)


---

FAQ
---

What is a tinybox?
:   It is a very powerful computer for deep learning, and likely the best performance/$. It was [benchmarked](https://public.tableau.com/views/MLCommons-Training_16993769118290/MLCommons-Training) in MLPerf Training 4.0 vs computers that cost 10x as much. And of course, anything that can train can do inference.

How do I get a tinybox?
:   Place an order through the links above. The factory is up and running, and it will ship within one week of us receiving the payment unless otherwise specified. Currently offering pickup in San Diego + shipping worldwide.

Where can I learn more about the tinybox?
:   We have a lot of content on our [Twitter](https://x.com/__tinygrad__), we also have a [tinybox docs page](https://docs.tinygrad.org/tinybox/) and a #tinybox discord channel.

Can I customize my tinybox?
:   In order to keep prices low and quality high, we don't offer any customization to the box or ordering process. Of course, after you buy the tinybox, it's yours and you are welcome to do whatever you want with it!

Can you fill out this supplier onboarding form?
:   In order to keep prices low and quality high, we don't offer any customization to the box or ordering process. If you aren't capable of ordering through the website, I'm sorry but we won't be able to help.

Can I pay with something besides wire transfer?
:   In order to keep prices low and quality high, we don't offer any customization to the box or ordering process. Wire transfer is the only accepted form of payment.

Can I contact someone at tiny to discuss my needs?
:   In order to keep prices low and quality high, we don't employ any sales people. We sell boxes through the website. The upside of this is that our pricing is simple and transparent.

Can I get a W-9 for this purchase?
:   Yes, you can [download that here](https://tinygrad.org/assets/fw9.pdf).

Is tinygrad used anywhere?
:   tinygrad is used in [openpilot](https://github.com/commaai/openpilot) to run the driving model on the Snapdragon 845 GPU. It replaces [SNPE](https://developer.qualcomm.com/sites/default/files/docs/snpe/overview.html), is faster, supports loading onnx files, supports training, and allows for attention (SNPE only allows fixed weights).

Is tinygrad inference only?
:   No! It supports full forward and backward passes with autodiff. [This](https://github.com/tinygrad/tinygrad/blob/master/tinygrad/gradient.py) is implemented at a level of abstraction higher than the accelerator specific code, so a tinygrad port gets you this for free.

How can I use tinygrad for my next ML project?
:   Follow the installation instructions on [the tinygrad repo](https://github.com/tinygrad/tinygrad). It has a similar API to PyTorch, yet simpler and more refined. Less stable though while tinygrad is in alpha, so be warned, though it's been fairly stable for a while.

When will tinygrad leave alpha?
:   When we can reproduce a common set of papers on 1 NVIDIA GPU 2x faster than PyTorch. We also want the speed to be good on the M1. ETA, Q2 next year.

How is tinygrad faster than PyTorch?
:   For most use cases it isn't yet, but it will be. It has three advantages:- It compiles a custom kernel for every operation, allowing extreme shape specialization.
    - All tensors are lazy, so it can aggressively fuse operations.
    - The backend is 10x+ simpler, meaning optimizing one kernel makes everything fast.

Where is tinygrad development happening?
:   On GitHub and [on Discord](https://discord.com/invite/ZjZadyC7PK)

How can the tiny corp work for me?
:   Email me, george@tinygrad.org. We are looking for contracts and sponsorships to improve various aspects of
    tinygrad.

How can I work for the tiny corp?
:   See **hiring** above. Contributions to [tinygrad](https://github.com/tinygrad/tinygrad) on GitHub
    always
    welcome, and a good way to get hired.

Can I invest in the tiny corp?
:   Invest with your PRs.

What's the goal of the tiny corp?
:   To accelerate. We will commoditize the petaflop and enable AI for everyone.