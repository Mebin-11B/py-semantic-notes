---
title: "Dotted Version Vectors: Logical Clocks for Optimistic Replication"
source: "https://arxiv.org/abs/1011.5808"
author:
  - "[[Nuno Preguiça]]"
  - "[[Carlos Baquero]]"
  - "[[Paulo Sérgio Almeida]]"
  - "[[Victor Fonte]]"
  - "[[Ricardo Gonçalves]]"
published:
created: 2026-06-18
description: "Abstract page for arXiv paper 1011.5808: Dotted Version Vectors: Logical Clocks for Optimistic Replication"
tags:
  - "clippings"
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - distributed systems
  - eventual consistency
  - logical clocks
  - version vectors
  - causality tracking
  - optimistic replication
related:
  - "[[Distributed Systems]]"
  - "[[Eventual Consistency]]"
  - "[[Version Vectors]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An abstract page of the arXiv research paper introducing Dotted Version Vectors, a scalable logical clock mechanism designed for causality tracking in replicated databases.
>
> **Key points:**
> - Replicated distributed storage engines targeting high availability use optimistic replication and settle for eventual consistency.
> - Capturing causality accurately in such databases is essential to identify concurrent and conflicting updates.
> - Classic version vectors do not scale because their metadata grows linearly with the total number of clients or update transactions.
> - The authors propose Dotted Version Vectors, which capture causality while capping metadata growth to scale linearly only with the active writing servers.
>
> **Concept links:** [[Distributed Systems]], [[Eventual Consistency]], [[Logical Clocks]], [[Version Vectors]], [[Causality Tracking]], [[Optimistic Replication]]
>
> **Suggested connections:**
> - [[Distributed Systems]] — The infrastructure paradigm hosting highly available, partition-tolerant databases.
> - [[Eventual Consistency]] — The structural consistency model that demands conflict resolution algorithms.
> - [[Version Vectors]] — The vector clock construct optimized by the paper's dotted logical design.
<!-- ai-summary:end -->

## Title:Dotted Version Vectors: Logical Clocks for Optimistic Replication

[View PDF](https://arxiv.org/pdf/1011.5808)

> Abstract:In cloud computing environments, a large number of users access data stored in highly available storage systems. To provide good performance to geographically disperse users and allow operation even in the presence of failures or network partitions, these systems often rely on optimistic replication solutions that guarantee only eventual consistency. In this scenario, it is important to be able to accurately and efficiently identify updates executed concurrently. In this paper, first we review, and expose problems with current approaches to causality tracking in optimistic replication: these either lose information about causality or do not scale, as they require replicas to maintain information that grows linearly with the number of clients or updates. Then, we propose a novel solution that fully captures causality while being very concise in that it maintains information that grows linearly only with the number of servers that register updates for a given data element, bounded by the degree of replication.

| Comments: |
| --- |
| Subjects: | Distributed, Parallel, and Cluster Computing (cs.DC) |
| ACM classes: | C.2.4; E.1 |
| Cite as: | [arXiv:1011.5808](https://arxiv.org/abs/1011.5808) \[cs.DC\] |
|  | (or [arXiv:1011.5808v1](https://arxiv.org/abs/1011.5808v1) \[cs.DC\] for this version) |
|  | [https://doi.org/10.48550/arXiv.1011.5808](https://doi.org/10.48550/arXiv.1011.5808) |

## Submission history

From: Carlos Baquero \[[view email](https://arxiv.org/show-email/afb5b9be/1011.5808)\]  
**\[v1\]** Fri, 26 Nov 2010 14:45:53 UTC (391 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/1011.5808) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))