---
title: "“Design me a highly resilient database”"
url: https://nikogura.com/DatabaseDesign.html
clipped: 2026-06-17 01:33:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [“Design me a highly resilient database”](https://nikogura.com/DatabaseDesign.html)

## Digest Summary
The post argues that “design a highly resilient database” is an ill‑posed product question that cannot be answered without context. It stresses that database choice depends on data model, query patterns, consistency, availability, durability, failure scenarios, regulatory constraints, and budget. The author contrasts ACID‑compliant relational systems (PostgreSQL/MySQL) – suitable for financial ledgers requiring strong consistency and auditability – with eventually consistent NoSQL stores (Cassandra, ScyllaDB) that excel at write‑heavy, partition‑tolerant workloads such as IoT time‑series data. Additional tools like Redis, Elasticsearch, DynamoDB, ClickHouse, and TimescaleDB serve specific roles (caching, search, key‑value, analytics) but are not universal system‑of‑record solutions. The author shares a real‑world implementation: CloudNativePG on Kubernetes with S3‑based WAL archiving, providing automated failover, point‑in‑time recovery, and 11‑nine durability for financial transactions. The key takeaway is that resilient database design starts with probing questions to define requirements, after which the appropriate technology can be selected.

## Discussion Summary
The comments collectively discuss interview practices, emphasizing the value of probing candidates on topics they know well to gauge depth of thinking, while critiquing overly generic or adversarial questions. Several remarks highlight the pitfalls of interviewers lacking technical knowledge, such as disputes over the CAP theorem and inappropriate reliance on Cassandra for certain use cases. A recurring complaint concerns the prevalence of AI‑generated content, which many find distracting or inauthentic. Overall, the discussion reflects frustration with poor interview design, a desire for clearer technical assessment, and skepticism toward AI‑driven writing.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: 404 Client Error: Not Found for url: https://nikogura.com/DatabaseDesign.html
> You can view the original article page directly [here](https://nikogura.com/DatabaseDesign.html).