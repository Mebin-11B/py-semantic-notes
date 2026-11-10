---
title: "Zvec: A lightweight, fast, in-process vector database"
url: https://github.com/alibaba/zvec
clipped: 2026-06-17 01:45:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Zvec: A lightweight, fast, in-process vector database](https://github.com/alibaba/zvec)

## Digest Summary
GitHub repository “alibaba/zvec” implements a lightweight, in‑process vector database. The page includes CI status badges for Linux x64, Linux ARM64, and macOS ARM64 builds, a code‑coverage indicator, PyPI release version, supported Python versions, and a license badge. Additional badges display performance‑benchmark results and QR codes for DingTalk and WeChat contact. No further textual description of features, architecture, or usage is provided in the scraped content.

## Discussion Summary
The comments express skepticism toward the reported benchmark results, requesting independent verification and clarification of the methods that yield the claimed performance advantage. They note the absence of comparisons with newer serverless vector databases such as Pinecone Serverless, Turbopuffer, and distributed Chroma, emphasizing the importance of evaluating cost versus performance on comparable hardware. Additional points raised include curiosity about how the system’s CPU and memory usage affect query speed, its relationship to DuckDB’s vector extensions, and the relevance of similarity searches for text classification tasks.

---

## Full Article

English | [中文](https://github.com/alibaba/zvec/blob/main/README_CN.md)

[![Code Coverage](https://camo.githubusercontent.com/db0b79407c09375fcac6311844f4b74855dbd3f745543e1ea66e5f77630374d2/68747470733a2f2f636f6465636f762e696f2f6769746875622f616c69626162612f7a7665632f67726170682f62616467652e7376673f746f6b656e3d4f383143543435423636)](https://codecov.io/github/alibaba/zvec)
[![Main](https://github.com/alibaba/zvec/actions/workflows/01-ci-pipeline.yml/badge.svg?branch=main)](https://github.com/alibaba/zvec/actions/workflows/01-ci-pipeline.yml)
[![License](https://camo.githubusercontent.com/b29de0acdfd19013f1f02689b15c933e4a6c145be9efa718288f88ba3280b1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c75652e737667)](https://github.com/alibaba/zvec/blob/main/LICENSE)
[![PyPI Release](https://camo.githubusercontent.com/0614676dbf9da2116c7f94ad863dd5f4e7aff036252d57e21ace1cbfe1142149/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7a7665632e737667)](https://pypi.org/project/zvec/)
[![Python Versions](https://camo.githubusercontent.com/53dad38b9eb32a88bc109757b47d7a7830cd90480b56b372297a44febacd6ec3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31302532307e253230332e31342d626c75652e737667)](https://pypi.org/project/zvec/)
[![npm Release](https://camo.githubusercontent.com/423b655a2ea0749003b94e261c9b3b1d2d5aa8246be79db7531e20f7657d278f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f407a7665632f7a7665632e737667)](https://www.npmjs.com/package/@zvec/zvec)

[![alibaba%2Fzvec | Trendshift](https://camo.githubusercontent.com/1955d7d654e34d2f53cb25301436996f83cafbad9d69d5a0df65356ca34af334/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3230383330)](https://trendshift.io/repositories/20830)

[🚀 **Quickstart**](https://zvec.org/en/docs/db/quickstart/)  |
[🏠 **Home**](https://zvec.org/en/)  |
[📚 **Docs**](https://zvec.org/en/docs/db/)  |
[📊 **Benchmarks**](https://zvec.org/en/docs/db/benchmarks/)  |
[🔎 **DeepWiki**](https://deepwiki.com/alibaba/zvec)  |
[🎮 **Discord**](https://discord.gg/rKddFBBu9z)  |
[🐦 **X (Twitter)**](https://x.com/ZvecAI)

**Zvec** is an open-source, in-process vector database — lightweight, lightning-fast, and designed to embed directly into applications. Battle-tested within Alibaba Group, it delivers production-grade, low-latency and scalable similarity search with minimal setup.

Important

🚀 **v0.5.0 (June 12, 2026)**

* **Full-Text Search (FTS)**: Native full-text search — attach an FTS index to any string field and query it with natural-language or structured expressions, no external search engine required.
* **Hybrid Retrieval**: Combine full-text and vector search in a single `MultiQuery` across dense vectors, sparse vectors, scalar filters, and text.
* **DiskANN Index**: New on-disk index that keeps the bulk of the index on disk, drastically cutting memory usage for large-scale datasets.
* **Ecosystem & Platforms**: New official [Go](https://github.com/zvec-ai/zvec-go) / [Rust](https://github.com/zvec-ai/zvec-rust) SDKs, the [Zvec Studio](https://github.com/zvec-ai/zvec-studio) visual tool, and RISC-V support.

👉 [Read the Release Notes](https://github.com/alibaba/zvec/releases/tag/v0.5.0) | [View Roadmap 📍](https://github.com/alibaba/zvec/issues/309)

* **Blazing Fast**: Searches billions of vectors in milliseconds.
* **Simple, Just Works**: [Install](https://github.com/alibaba/zvec#-installation) and start searching in seconds. Pure local, no servers, no config, no fuss.
* **Dense + Sparse Vectors**: Support dense and sparse embeddings, multi-vector queries, and a rich selection of [vector index types](https://zvec.org/en/docs/db/concepts/vector-index/#vector-index-types) that scale from memory to disk.
* **Full-Text Search (FTS)**: Native keyword-based full-text search — query string fields with natural-language or structured expressions.
* **Hybrid Search**: Fuse vector similarity, full-text search, and structured filters in a single query for precise results.
* **Durable Storage**: Write-ahead logging (WAL) guarantees persistence — data is never lost, even on process crash or power failure.
* **Concurrent Access**: Multiple processes can read the same collection simultaneously; writes are single-process exclusive.
* **Runs Anywhere**: As an in-process library, Zvec runs wherever your code runs — notebooks, servers, CLI tools, or even edge devices.

Zvec offers official SDKs across multiple languages:

* **[Python](https://pypi.org/project/zvec/)**: `pip install zvec` (requires Python 3.10–3.14)
* **[Node.js](https://www.npmjs.com/package/@zvec/zvec)**: `npm install @zvec/zvec`
* **[Go](https://github.com/zvec-ai/zvec-go)**: High-performance Go bindings.
* **[Rust](https://github.com/zvec-ai/zvec-rust)**: High-performance Rust bindings.
* **[Dart/Flutter](https://pub.dev/packages/zvec)**: `flutter pub add zvec`

Prefer a visual tool? Try **[Zvec Studio](https://github.com/zvec-ai/zvec-studio)** to browse data and debug queries — no code required.

* Linux (x86\_64, ARM64)
* macOS (ARM64)
* Windows (x86\_64)

If you prefer to build Zvec from source, please check the [Building from Source](https://zvec.org/en/docs/db/build/) guide.

```
import zvec

# Define collection schema
schema = zvec.CollectionSchema(
    name="example",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 4),
)

# Create collection
collection = zvec.create_and_open(path="./zvec_example", schema=schema)

# Insert documents
collection.insert([
    zvec.Doc(id="doc_1", vectors={"embedding": [0.1, 0.2, 0.3, 0.4]}),
    zvec.Doc(id="doc_2", vectors={"embedding": [0.2, 0.3, 0.4, 0.1]}),
])

# Search by vector similarity
results = collection.query(
    zvec.VectorQuery("embedding", vector=[0.4, 0.3, 0.3, 0.1]),
    topk=10
)

# Results: list of {'id': str, 'score': float, ...}, sorted by relevance
print(results)
```

Zvec delivers exceptional speed and efficiency, making it ideal for demanding production workloads.

[![Zvec Performance Benchmarks](https://camo.githubusercontent.com/04f41c5eb156827e64769555ed83ead209c980b3185b99a00af73369ca7e9c65/68747470733a2f2f7a7665632e6f73732d636e2d686f6e676b6f6e672e616c6979756e63732e636f6d2f7170735f31304d2e737667)](https://camo.githubusercontent.com/04f41c5eb156827e64769555ed83ead209c980b3185b99a00af73369ca7e9c65/68747470733a2f2f7a7665632e6f73732d636e2d686f6e676b6f6e672e616c6979756e63732e636f6d2f7170735f31304d2e737667)

For detailed benchmark methodology, configurations, and complete results, please see our [Benchmarks documentation](https://zvec.org/en/docs/db/benchmarks/).

🤝 Join Our Community
--------------------

| 💬 DingTalk | 📱 WeChat | 🎮 Discord | X (Twitter) |
| --- | --- | --- | --- |
| [DingTalk QR Code](https://camo.githubusercontent.com/0e2caadfb524e50941273644e074f662622f2a81ebe5387e2ddec3599a4ec18b/68747470733a2f2f7a7665632e6f73732d636e2d686f6e676b6f6e672e616c6979756e63732e636f6d2f7172636f64652f64696e6764696e672e706e67) | [WeChat QR Code](https://camo.githubusercontent.com/cba00b0088bebfd7a583eab67758b2cb841c12d304e85fc6098af9f966b771c0/68747470733a2f2f7a7665632e6f73732d636e2d686f6e676b6f6e672e616c6979756e63732e636f6d2f7172636f64652f7765636861742e706e673f763d36) | [Discord](https://discord.gg/rKddFBBu9z) | [X (formerly Twitter) Follow](https://x.com/ZvecAI) |
| Scan to join | Scan to join | Click to join | Click to follow |

We welcome and appreciate contributions from the community! Whether you're fixing a bug, adding a feature, or improving documentation, your help makes Zvec better for everyone.

Check out our [Contributing Guide](https://github.com/alibaba/zvec/blob/main/CONTRIBUTING.md) to get started!