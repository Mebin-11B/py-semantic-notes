---
title: "Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring"
url: https://bustermq.sh/
clipped: 2026-06-17 02:05:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: BusterMQ, Thread-per-core NATS server in Zig with io_uring](https://bustermq.sh/)

## Digest Summary
BusterMQ performance benchmarks focus on a fan‑out scenario with 10 publishers and 100 subscribers (10 per topic) across 10 topics, transmitting 50 million messages of 128‑byte payload each. Tests run on a local AMD Ryzen 9 9950X (16‑core) system. Four configurations are evaluated: the standard default using io_uring, a BusyPoll mode employing a spin‑loop, a Route mode with shard‑aware routing, and a combined Route + BusyPoll configuration identified as the optimal setup. Additional benchmark results are forthcoming.

## Discussion Summary
The comments raise technical queries about the project’s setup, asking where the testing machine was sourced and why the Zig language was chosen over alternatives like Rust. They also suggest improving documentation by aligning the ASCII flowchart in the repository’s README. The tone is inquisitive with mild criticism, indicating a desire for clearer implementation details and better presentation, while expressing skepticism about current automated tools handling the formatting correctly.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: HTTPSConnectionPool(host='bustermq.sh', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection(host='bustermq.sh', port=443): Failed to resolve 'bustermq.sh' ([Errno 8] nodename nor servname provided, or not known)"))
> You can view the original article page directly [here](https://bustermq.sh/).