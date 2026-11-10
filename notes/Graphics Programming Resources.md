---
title: "Graphics Programming Resources"
url: https://develop--gpvm-website.netlify.app/resources/
clipped: 2026-06-17 01:36:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Graphics Programming Resources](https://develop--gpvm-website.netlify.app/resources/)

## Digest Summary
An overview of variance‑reduction methods for Monte‑Carlo rendering includes:

- **Bidirectional Path Tracing** – connects eye and light sub‑paths to capture difficult lighting such as indirect illumination and caustics, improving convergence over unidirectional tracing.  
- **Metropolis‑Hastings** – employs a Markov‑Chain Monte‑Carlo scheme that mutates sample paths, focusing computation on high‑contribution regions and reducing variance in complex scenes.  
- **Multiple‑Importance Sampling (MIS)** – combines several sampling strategies with weighted balances to minimize estimator variance across diverse integrands.  
- **Stratified Sampling** – partitions the domain into strata and draws one sample per stratum, guaranteeing more uniform coverage than pure random sampling.  
- **Low‑Discrepancy Sequences** – use deterministic quasi‑random point sets (e.g., Halton, Sobol) to achieve faster error decay than stochastic sampling.  
- **Blue‑Noise Sampling** – generates patterns with minimal low‑frequency power, yielding visually pleasing noise and improved convergence for image‑plane sampling.  
- **Photon Mapping** – a two‑pass global illumination technique that stores photon contributions in a spatial map, allowing efficient evaluation of indirect lighting.  
- **Finite‑Element Radiosity** – solves the radiosity integral using discretized surface elements, providing deterministic, low‑variance illumination for diffuse interreflections.

## Discussion Summary
None

---

## Full Article

[Lecture 19: Variance Reduction (CMU 15-462/662)](https://youtu.be/IQhLk_XaFc8) 

An overview various variance reduction techniques for Monte Carlo rendering, covering bidirectional path tracing, Metropolis-Hastings algorithm, MIS, stratified Sampling, low-discrepancy sampling, blue noise, photon mapping, and finite element radiosity