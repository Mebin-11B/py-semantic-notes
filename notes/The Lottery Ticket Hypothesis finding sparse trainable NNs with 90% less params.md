---
title: "The Lottery Ticket Hypothesis: finding sparse trainable NNs with 90% less params"
url: https://arxiv.org/abs/1803.03635
clipped: 2026-06-17 02:03:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Lottery Ticket Hypothesis: finding sparse trainable NNs with 90% less params](https://arxiv.org/abs/1803.03635)

## Digest Summary
The paper investigates why heavily pruned neural networks, which can retain >90 % of original performance with far fewer parameters, are hard to train from scratch. Using a standard magnitude‑based pruning method, the authors discover subnetworks whose initial random weights enable effective training when isolated. This leads to the “lottery ticket hypothesis”: dense, randomly initialized feed‑forward networks contain sparse subnetworks (“winning tickets”) that, with their original initializations, achieve test accuracy comparable to the full network within a similar training budget. An algorithm is proposed to locate such tickets by iteratively training, pruning, and resetting weights to their initial values. Experiments on fully‑connected and convolutional architectures for MNIST and CIFAR‑10 consistently find winning tickets comprising 10‑20 % of the original parameters. These tickets train faster and often surpass the unpruned network’s accuracy, highlighting the critical role of fortunate initial weight configurations in sparse, trainable networks.

## Discussion Summary
The comment treats the lottery‑ticket hypothesis as an informal observation rather than a proven principle, arguing that over‑parameterized networks possess a vast space of interchangeable configurations that can approximate a target function. It frames neural‑network behavior in terms of gauge invariance and suggests that many “good enough” arrangements exist, limiting the hypothesis’s practical advantage, especially for final performance gains. The author proposes that optimizer strategies, specific initializations, and potential hardware adaptations could exploit this redundancy, and mentions the possibility of pruning and distilling oversized models after locating effective configurations.

---

## Full Article

[Submitted on 9 Mar 2018 (

[v1](https://arxiv.org/abs/1803.03635v1)

), last revised 4 Mar 2019 (this version, v5)]

Title:The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks
==============================================================================

View a PDF of the paper titled The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks, by Jonathan Frankle and Michael Carbin

[View PDF](https://arxiv.org/pdf/1803.03635)
[HTML (experimental)](https://arxiv.org/html/1803.03635v5)
> Abstract:Neural network pruning techniques can reduce the parameter counts of trained networks by over 90%, decreasing storage requirements and improving computational performance of inference without compromising accuracy. However, contemporary experience is that the sparse architectures produced by pruning are difficult to train from the start, which would similarly improve training performance.
>   
> We find that a standard pruning technique naturally uncovers subnetworks whose initializations made them capable of training effectively. Based on these results, we articulate the "lottery ticket hypothesis:" dense, randomly-initialized, feed-forward networks contain subnetworks ("winning tickets") that - when trained in isolation - reach test accuracy comparable to the original network in a similar number of iterations. The winning tickets we find have won the initialization lottery: their connections have initial weights that make training particularly effective.
>   
> We present an algorithm to identify winning tickets and a series of experiments that support the lottery ticket hypothesis and the importance of these fortuitous initializations. We consistently find winning tickets that are less than 10-20% of the size of several fully-connected and convolutional feed-forward architectures for MNIST and CIFAR10. Above this size, the winning tickets that we find learn faster than the original network and reach higher test accuracy.

Submission history
------------------

From: Jonathan Frankle [

[view email](https://arxiv.org/show-email/1e6cec2c/1803.03635)

]

**[[v1]](https://arxiv.org/abs/1803.03635v1)**

Fri, 9 Mar 2018 18:51:28 UTC (6,917 KB)

**[[v2]](https://arxiv.org/abs/1803.03635v2)**

Mon, 23 Apr 2018 19:58:09 UTC (8,072 KB)

**[[v3]](https://arxiv.org/abs/1803.03635v3)**

Sun, 20 May 2018 19:46:47 UTC (8,173 KB)

**[[v4]](https://arxiv.org/abs/1803.03635v4)**

Tue, 27 Nov 2018 20:03:01 UTC (7,782 KB)

**[v5]**

Mon, 4 Mar 2019 15:51:11 UTC (2,029 KB)