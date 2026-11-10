---
title: "Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded"
url: https://twitter.com/lemire/status/2091894299289874926
clipped: 2026-08-31 13:52:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Xiaomi: New CPU matches Apple cores single threaded, much faster multithreaded](https://twitter.com/lemire/status/2091894299289874926)

## Digest Summary
Xiaomi’s new Xring O3 processor, highlighted by Daniel Lemire, positions the company’s smartphones as direct competitors to Apple’s iPhones. Benchmarks show the chip matching Apple cores on single‑threaded workloads (≈3,945 Geekbench score) while substantially outpacing them in multithreaded performance (≈15,221 score). Key architectural features include a massive 44 MB cache—larger than typical laptop CPUs—and the C1‑Ultra cores, which support SME2 (Scalable Matrix Extension 2) for AI acceleration and SVE2 for SIMD data parallelism. The design incorporates 21 execution ports, six dedicated to 128‑bit SIMD operations, exceeding the execution‑port count of current Intel/AMD processors; AMD’s Zen 5 can issue 4×512‑bit operations, whereas the Xring O3 offers the best‑available 6×128‑bit SIMD on ARM. This reflects a broader trend toward highly parallel cores with abundant execution units and cache, concentrating transistors on these capabilities.

---

## Full Article

## Post

[Log in](https://twitter.com/i/jf/onboarding/web?mode=login&redirect_after_login=%2Flemire%2Fstatus%2F2091894299289874926)[Sign up](https://twitter.com/i/jf/onboarding/web?mode=signup&redirect_after_login=%2Flemire%2Fstatus%2F2091894299289874926)

## Post

# Daniel Lemire on X: "Xiaomi is the Chinese tech giant. Their phones compete with iPhones.

Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And"

[Daniel Lemire](https://x.com/lemire)[@lemire](https://x.com/lemire)Xiaomi is the Chinese tech giant. Their phones compete with iPhones.

Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And you may find it it difficult to find a phone with the next CPU (Xring O3).

But the new Xiaomi processor is worth discussing further as it reveals an important trend.

The chip has a lot of cache (44 MB in total). It is more than most laptop CPUs. If you have an Intel processor in your laptop, chances are good that you have less cache.

The biggest cores on the the Xring O3 are the C1-Ultra. C1-Ultra really powerful cores. They support SME2 (Scalable Matrix Extension 2) for matrix/AI acceleration, SVE2 for data parallelism (SIMD).

It is astonishingly wide, with 21 execution ports, six of which support SIMD operations (128 bits).

This is more execution ports than you have on your Intel/AMD processor. The AMD Zen 5 has the  upper hand because it can do 4x512-bit but 6x128-bit is the best you can do on an ARM chip as far as I know.

So the trend is clear. We are getting cores that are massively parallel in terms of the number of execution units. We get better SIMD (more units) and many more units capable of doing arithmetic.

This means that you can do many, many independent additions or multiplications per cycle. And much more cache.

This is where all the transistors go.[Ice Universe](https://x.com/UniverseIce)[@UniverseIce](https://x.com/UniverseIce)[Aug 24](https://twitter.com/UniverseIce/status/2091770325927411955)Xiaomi’s Xring O3 delivers a massive performance leap, scoring 3,945 in Geekbench single-core and an unprecedented 15,221 in multi-core.[2:24 PM · Aug 24, 2026](https://twitter.com/lemire/status/2091894299289874926)[93.2KViews](https://twitter.com/lemire/status/2091894299289874926)3694834306
- [Daniel Lemire](https://x.com/lemire)[@lemire](https://x.com/lemire)Xiaomi is the Chinese tech giant. Their phones compete with iPhones.

Their new CPU roughly matches Apple cores on single threaded tasks, and is much faster in multithreaded execution. Of course, Apple may soon announce their next processor, so this edge may not last long. And you may find it it difficult to find a phone with the next CPU (Xring O3).

But the new Xiaomi processor is worth discussing further as it reveals an important trend.

The chip has a lot of cache (44 MB in total). It is more than most laptop CPUs. If you have an Intel processor in your laptop, chances are good that you have less cache.

The biggest cores on the the Xring O3 are the C1-Ultra. C1-Ultra really powerful cores. They support SME2 (Scalable Matrix Extension 2) for matrix/AI acceleration, SVE2 for data parallelism (SIMD).

It is astonishingly wide, with 21 execution ports, six of which support SIMD operations (128 bits).

This is more execution ports than you have on your Intel/AMD processor. The AMD Zen 5 has the  upper hand because it can do 4x512-bit but 6x128-bit is the best you can do on an ARM chip as far as I know.

So the trend is clear. We are getting cores that are massively parallel in terms of the number of execution units. We get better SIMD (more units) and many more units capable of doing arithmetic.

This means that you can do many, many independent additions or multiplications per cycle. And much more cache.

This is where all the transistors go.[Ice Universe](https://x.com/UniverseIce)[@UniverseIce](https://x.com/UniverseIce)[Aug 24](https://twitter.com/UniverseIce/status/2091770325927411955)Xiaomi’s Xring O3 delivers a massive performance leap, scoring 3,945 in Geekbench single-core and an unprecedented 15,221 in multi-core.[2:24 PM · Aug 24, 2026](https://twitter.com/lemire/status/2091894299289874926)[93.2KViews](https://twitter.com/lemire/status/2091894299289874926)3694834306
- [Jon Clegg](https://x.com/jonclegg77)[@jonclegg77](https://x.com/jonclegg77)[Aug 24](https://twitter.com/jonclegg77/status/2091914018524926079)This smells somewhat legitimate and somewhat BS. The architecture itself looks impressive — TSMC 3nm, a 4+ GHz prime core, tons of cache, and a very wide execution engine. And the claimed Geekbench numbers, around 3,945 single-core and 15,221 multi-cor, are especially impressive, Show more5285.3K
- [noname](https://x.com/l1bertypr1me)[@l1bertypr1me](https://x.com/l1bertypr1me)[Aug 24](https://twitter.com/l1bertypr1me/status/2091923327077978124)Tensor G6 also has C1-Ultra core, but can only get ~2700 single core. Something feels off here.3166.7K
- [Chris Allen](https://x.com/theodorvaryag)[@theodorvaryag](https://x.com/theodorvaryag)[Aug 24](https://twitter.com/theodorvaryag/status/2091912756353995230)SVE2 with 21 execution ports? good golly miss molly I could make that thing scream.82.7K
