---
title: "LiteLLM (YC W23): Founding Reliability Engineer – $200K-$270K and 0.5-1.0% equity"
url: https://www.ycombinator.com/companies/litellm/jobs/unlCynJ-founding-reliability-performance-engineer
clipped: 2026-06-17 01:39:41
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [LiteLLM (YC W23): Founding Reliability Engineer – $200K-$270K and 0.5-1.0% equity](https://www.ycombinator.com/companies/litellm/jobs/unlCynJ-founding-reliability-performance-engineer)

## Digest Summary
LiteLLM is an open‑source AI gateway (36 K+ GitHub stars) handling hundreds of millions of LLM API calls daily for enterprises such as NASA, Adobe, Netflix, Stripe, and Nvidia. The company, now at $7 M ARR with a 10‑person YC W23 team, seeks its first dedicated reliability and performance engineer.

The role splits roughly 60 % operational reliability and 40 % performance engineering. Core duties include on‑call incident response, blameless post‑mortems, customer escalation support, and building self‑healing mechanisms for DB/Redis outages. Performance tasks cover memory‑leak detection, hot‑path optimization (target < 10 ms overhead at >5 k RPS), latency benchmarking (P50/P95/P99), and profiling of async Python components (aiohttp/httpx, event loop, connection pools). The engineer will also design observability (structured logs, distributed tracing, Prometheus metrics), release safety (canary deployments, automated rollback), and SLO tracking.

Required experience: ≥2 years running production Python services, deep knowledge of asyncio, PostgreSQL tuning, and Kubernetes pod management; prior on‑call experience. Preferred background includes work on proxies/API gateways, infrastructure roles at large tech firms, early‑stage reliability hires, or open‑source contributions. The position offers high impact on critical AI infrastructure, visible open‑source work, and equity in a fast‑growing startup.

## Discussion Summary
None

---

## Full Article

### **TLDR**

LiteLLM is an open-source AI gateway (36K+ GitHub stars) that routes hundreds of millions of LLM API calls daily for companies like NASA, Adobe, Netflix, Stripe, and Nvidia. We're at $7M ARR, 10 people, YC W23.

When LiteLLM goes down, our customers' entire AI stack goes down. We need someone who makes sure that doesn't happen.

You'd be the first dedicated reliability hire. You'll own reliability, performance, and production stability end-to-end. Nobody will tell you how to do it

### What this job actually is

We'll be straight with you: this role is roughly 60% operational reliability and 40% deep performance engineering. On any given week you might be:

* Hunting a memory leak in our async streaming handler that causes OOMs after 4 hours under load
* Fixing a race condition where PodLockManager releases another pod's lock
* Profiling why `update_database()` does 7 deep copies per request in the spend tracking hot path
* Helping a Fortune 500 customer debug why their 20-pod deployment is exhausting Postgres connections
* Building soak tests that catch degradation before a release goes out
* Reviewing a PR that touches the request hot path and saying "this will add 50ms at P99, here's why"

If you're looking for a pure optimization role where you sit in a profiler all day — this isn't it. If you want to own production health for one of the most widely deployed AI infrastructure projects in the world — keep reading.

Why this matters
----------------

We route traffic for some of the largest AI deployments on the planet. One customer is scaling from 20M to 200M daily AI calls through our gateway. Another has 150K users hitting us daily. When we ship a bad release, it doesn't just break a dashboard — it breaks production AI systems at companies you've heard of.

The problems here are genuinely hard:

* **Memory management in long-running Python async services** — our proxy handles thousands of concurrent streaming connections. HTTP client sessions, response iterators, and background tasks all need careful lifecycle management.
* **Database at scale** — spend logging, auth, and rate limiting all interact with Postgres. At 100K+ requests/day, naive patterns fall apart.
* **100+ provider surface area** — we translate between OpenAI, Anthropic, Bedrock, Vertex, and 100+ other APIs. Each has unique streaming behavior. A refactor that fixes one provider can break three others.

You won't run out of interesting problems.

What you'll own
---------------

**Production reliability**

* On-call for critical issues (shared rotation with the team, not solo)
* Incident response and blameless post-mortems
* Customer escalation support for enterprise deployments
* Making the proxy self-healing when DB/Redis is temporarily unavailable

**Performance engineering**

* Memory leak detection and prevention (soak tests, CI integration)
* Hot path optimization — our target is <10ms overhead at 5K+ RPS
* P50/P95/P99 latency benchmarks that block releases on regression
* Profiling and fixing bottlenecks (Pydantic validation, connection pools, async task scheduling)

**Observability & release safety**

* Structured logging, distributed tracing, correlation IDs
* Prometheus metrics that are actually accurate and actionable
* Building toward canary deployments and automated rollback
* SLO definition and tracking for enterprise customers

Who you are
-----------

**Must have:**

* 2+ years of experience running Python services in production, with real exposure to debugging things that break at scale
* Strong understanding of Python async internals — asyncio event loop, aiohttp/httpx session management, connection pooling
* Experience debugging production memory leaks, OOMs, or latency degradation (bonus if you've used memray, py-spy, or tracemalloc)
* Solid PostgreSQL knowledge — connection pool tuning, query optimization, understanding how DB operations on the request path degrade under load
* Comfort with Kubernetes at an operational level — pod lifecycle, resource limits, health probes
* You've been on-call before and you didn't hate it

**Strong signals:**

* You've worked on a proxy, API gateway, load balancer, or middleware service where *overhead itself* is what you optimize
* You've worked at Meta (Production Engineering), Cloudflare, Fastly, Datadog, Stripe, or a similar infrastructure company
* You've been an early reliability/infra hire at a startup and built production practices from scratch
* You've contributed to open-source infrastructure projects
* You understand HTTP/2, streaming responses (SSE), and how async Python handles them under concurrency

Why LiteLLM
-----------

* **Scale & impact**: Your work is in the critical path for hundreds of millions of AI API calls daily. NASA, Netflix, Adobe, Stripe depend on this.
* **Open source visibility**: 36K GitHub stars. Your contributions are visible to the entire AI infrastructure community. Your GitHub profile will look incredible.
* **Ownership**: First dedicated reliability hire. You define what reliability means here. No bureaucracy, no tickets — you see a problem, you fix it.
* **Trajectory**: $7M ARR growing fast, 10-person team, YC W23. Meaningful equity at a stage where it can matter.