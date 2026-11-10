---
title: "Torch.ts – building PyTorch in TypeScript from scratch to learn"
url: https://github.com/13point5/torch.ts
clipped: 2026-06-17 02:04:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - machine learning library
  - typescript programming
  - tensor computation
related:
  - "[[Machine Learning Library]]"
  - "[[TypeScript Programming]]"
  - "[[Tensor Computation]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Torch.ts is a learning-focused open-source project implementing deep learning and tensor manipulation primitives in TypeScript from scratch.
>
> **Key points:**
> - Aims to build core PyTorch concepts—tensors, automatic differentiation, and neural network layers—directly in TypeScript.
> - Avoids external mathematical libraries to provide a hands-on, low-level learning experience regarding matrix math and memory strides.
> - Demonstrates standard JavaScript/TypeScript usage, such as instantiating a Tensor and retrieving shapes, strides, and indexed elements.
> - The developer community responds positively, sharing enthusiasm for writing tensor engines and automatic differentiation from the ground up.
>
> **Concept links:** [[Machine Learning Library]], [[TypeScript Programming]], [[Tensor Computation]], [[Educational Software]], [[Low-level Implementation]], [[Automatic Differentiation]]
>
> **Suggested connections:**
> - [[Tensor Computation]] — mathematical operations and data structures for multidimensional arrays.
> - [[TypeScript Programming]] — developing strongly-typed applications for Web and Node.js environments.
<!-- ai-summary:end -->

# [Torch.ts – building PyTorch in TypeScript from scratch to learn](https://github.com/13point5/torch.ts)

## Digest Summary
The referenced page concerns the GitHub repository **13point5/torch.ts**, which is described as an implementation of PyTorch built from scratch in TypeScript. The project’s goal is to provide core deep‑learning primitives—tensors, automatic differentiation, and neural‑network layers—using the TypeScript language, enabling integration with JavaScript ecosystems and web‑based environments. However, the attempt to retrieve detailed content from the repository failed, yielding the message “You can’t perform that action at this time.” Consequently, no further technical specifications, code examples, documentation, or usage instructions are available from the scraped source. The summary therefore reflects only the repository’s intended purpose and the lack of accessible content at the time of scraping.

## Discussion Summary
The discussion highlights enthusiasm for developing a tensor manipulation library, noting progress in implementing core operations such as matrix multiplication and stride handling manually. Participants express satisfaction with the learning experience gained from low‑level coding without relying on external libraries like NumPy, and they anticipate expanding the project by integrating an automatic differentiation engine in the near future. The overall tone conveys optimism and a constructive outlook toward continued development.

---

## Full Article

A simple version of pytorch in TypeScript from scratch as a learning project.

Run the main entry point:

```
import { Tensor } from "./tensor";

// Create tensors
const t = new Tensor([
  [1, 2, 3],
  [4, 5, 6],
]);

// Access tensor properties
console.log(t.shape); // [2, 3]
console.log(t.strides); // [3, 1]
console.log(t.flatData); // [1, 2, 3, 4, 5, 6]

// Access elements by multi-dimensional index
console.log(t.pos([0, 0])); // 1
console.log(t.pos([0, 2])); // 3
console.log(t.pos([1, 1])); // 5
```