---
title: "How to Write to SSDs [pdf]"
url: https://www.vldb.org/pvldb/vol19/p1469-lee.pdf
clipped: 2026-06-17 01:02:17
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - ssd storage
  - database engines
  - sequential writes
  - smr drives
  - storage optimization
related:
  - "[[SSD Storage]]"
  - "[[Database Engines]]"
  - "[[Storage Optimization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A HackerNews digest of a VLDB paper on optimizing sequential write access patterns to solid-state drives (SSDs).
>
> **Key points:**
> - The source document is a VLDB research paper on SSD writing techniques (content was not directly scraped due to binary PDF format).
> - Discussions compare these optimizations with write patterns in SMR (Shingled Magnetic Recording) hard drives.
> - Developers focus on how low-level SSD optimizations can inspire new design patterns in database storage engines and systems like PostgreSQL.
> - Several comments express frustration and amusement at the PDF download link executing a write operation to their SSD to read about SSD writes.
>
> **Concept links:** [[SSD Storage]], [[Database Engines]], [[Sequential Writes]], [[SMR Drives]], [[Storage Optimization]]
>
> **Suggested connections:**
> - [[SSD Storage]] — The primary medium whose endurance and performance characteristics are analyzed.
> - [[Database Engines]] — Software architectures that require high-performance, predictable storage write semantics.
<!-- ai-summary:end -->


# [How to Write to SSDs [pdf]](https://www.vldb.org/pvldb/vol19/p1469-lee.pdf)

## Digest Summary
None

## Discussion Summary
The comments express curiosity about the distinct access patterns required for SMR drives and question whether optimizations for large sequential writes would benefit other storage media. There is interest in the potential for such research to inspire new database architectures or heavily tuned PostgreSQL implementations. At the same time, users feel misled by a link that initiates a PDF download, realizing it writes to their SSD, which leads to frustration over the unexpected behavior. Overall, the discussion balances technical intrigue with disappointment in the presentation.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: All strings must be XML compatible: Unicode or ASCII, no NULL bytes or control characters
> You can view the original article page directly [here](https://www.vldb.org/pvldb/vol19/p1469-lee.pdf).