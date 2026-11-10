---
title: "GenCAD"
url: https://gencad.github.io/
clipped: 2026-06-17 01:01:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GenCAD](https://gencad.github.io/)

## Digest Summary
GenCAD is an image‑conditional generative model that produces fully parameterized CAD programs, not just 3D solids. It addresses the difficulty of training AI on complex CAD data structures (e.g., B‑rep) by learning joint representations of CAD command sequences and reference images. The architecture comprises four stages: (1) an autoregressive transformer encoder for latent encoding of CAD command sequences; (2) a contrastive learning module that aligns latent spaces of CAD commands and CAD images; (3) a latent diffusion model that generates CAD‑latent vectors conditioned on images; and (4) a decoder that translates these latents into executable parametric CAD commands. By outputting the complete CAD command history, GenCAD enables accurate, modifiable models suitable for engineering, manufacturing, and design space exploration, surpassing mesh, voxel, or point‑cloud approximations.

## Discussion Summary
The feedback is largely skeptical, noting that while the demo appears interesting, it offers limited practical value for complex CAD work. Commenters emphasize that essential steps such as defining dimensions, tolerances, and constraints remain unresolved, and the tool struggles with real‑world or hand‑drawn images. Setup difficulties, sparse examples, and poor mobile rendering further diminish confidence. Comparisons to established solutions like OpenSCAD highlight a preference for more mature workflows, and there is interest in tighter LLM integration and broader format support, but overall the utility is viewed as limited.

---

## Full Article

We present GenCAD, an image-conditional CAD generation model. Our model not only generates the 3D CAD but also the
entire parameterized CAD command history, CAD program, as output.

The complexity of CAD data structures such as boundary representation (B-rep) makes it difficult to train efficient
AI models. Due to the ease of data availability, common approaches often resort to representations
like meshes, voxels, or point clouds, which sacrifice the accuracy and modifiability of true CAD
models that are critical for engineering tasks, manufacturing and design space exploration. Here we
propose GenCAD, an image conditional generative model that generates parametric CAD command
sequences, also known as CAD programs, that can be converted to a 3D solid model using a geometry
kernel. At the core of GenCAD, we develop a strong representation learning framework for multiple
modalities of computational engineering designs.

Our proposed GenCAD architecture is a combination of four critical steps; 1) an autoregressive transformer encoder is used for learning the latent representation
of the CAD command sequences, 2) a contrastive learning-based model is used to learn the joint
representations of the latent spaces between CAD command sequences and CAD-images, 3) a latent
diffusion model that can generate the latent representation of CAD command sequences conditioned
on CAD-images, and 4) finally, a decoder model that can convert cad latents into a sequence of
parametric CAD commands. Most importantly, GenCAD does not merely generate a 3D solid but also the entire CAD program. Our work represents a step forward in CAD, offering more precise and
modifiable 3D modeling from images, potentially enhancing automated design processes.