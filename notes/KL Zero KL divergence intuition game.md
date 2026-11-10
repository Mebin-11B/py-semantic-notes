---
title: "KL Zero: KL divergence intuition game"
url: "https://klzero.sarna.dev"
clipped: 2026-06-17 00:54:09
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - kullback-leibler divergence
  - probability distributions
  - information theory
  - gamified learning
related:
  - "[[Machine Learning Intuition]]"
  - "[[Data Visualization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** KL Zero is an interactive web game designed to build intuitive understanding of Kullback-Leibler (KL) divergence by drawing probability distributions.
>
> **Key points:**
> - Provides a gamified interface where users draw distributions to match a specified target KL divergence value.
> - Emphasizes rapid, 10-second estimation of probability masses and relative entropy over exact calculations.
> - Focuses on the concept of KL divergence as a measure of surprise when comparing distributions P and Q.
> - Receives community feedback suggesting Wasserstein distance alternatives and improved coordinate labels.
>
> **Concept links:** [[Kullback-Leibler Divergence]], [[Probability Distributions]], [[Information Theory]], [[Gamified Learning]]
>
> **Suggested connections:**
> - [[Kullback-Leibler Divergence]] — is the core mathematical concept evaluated by the game.
> - [[Information Theory]] — relative entropy and divergence are fundamental concepts in information theory.
<!-- ai-summary:end -->

# [KL Zero: KL divergence intuition game](https://klzero.sarna.dev)

## Digest Summary
KL divergence quantifies how surprising a probability distribution P appears when evaluated with a different reference distribution Q. It is defined as the expected logarithmic difference between the probabilities assigned by P and Q over the shared support, assuming both distributions sum to (or approximate) one. The task described requires constructing any probability distribution whose total mass is close to 1 and whose KL divergence relative to a given target value matches that target as closely as possible. The user must complete this construction within a ten‑second time limit, emphasizing rapid approximation rather than exact optimization. The core requirements are: (1) maintain near‑unit normalization of the drawn distribution, and (2) achieve a KL divergence value that approximates the specified target.

## Discussion Summary
The comments express a mix of constructive feedback and uncertainty. A suggestion is made to include a Wasserstein distance option, while another remark notes difficulty understanding the material, describing it as intriguing yet confusing. A separate comment points out a lack of labeling on the x‑axis, making it impossible to assess proximity to the correct probability mass. Overall, the feedback highlights a desire for additional features and clearer presentation to aid comprehension.

---

## Full Article

**Draw to the target KL.**

KL divergence measures how surprising the blue distribution P would look if your green distribution Q were used instead.

Draw any probability distribution that sums close to 1 and gets as close as possible to the target KL divergence number.

You have 10 seconds to do it. Go!

Start
