---
title: "Why LLM Inference Is Disaggregating Its Memory"
source: "https://medium.com/@sseshadri/why-llm-inference-is-disaggregating-its-memory-2d9d299d931a"
author:
  - "[[Srinivasan Seshadri]]"
published: 2026-05-29
created: 2026-05-31
description: "The KV cache spilled out of GPU memory two years ago. The next move — fleet-wide shared storage — is a different kind of shift, driven by tw"
tags:
  - "clippings"
processed: true
processed_at: 2026-05-31
summary_status: done
concepts:
  - LLM Inference
  - KV Cache
  - Disaggregated Memory
  - GPU Infrastructure
  - Prefill vs Decode
  - RAG
  - System Prompts
  - Storage Hierarchy
  - Distributed Systems
related:
  - "[[How flat is replacing fat in AWS data center networks.md]]"
  - "[[Cloud Computing Infrastructure]]"
  - "[[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** LLM inference architecture is shifting from local KV caching to fleet-wide disaggregated memory to enable cross-user prefix reuse and optimize separate prefill and decode phases.
>
> **Key points:**
> - Chronicles the spillover of KV cache from GPU HBM into CPU RAM, local NVMe, and finally into networked, disaggregated storage shared across entire worker fleets.
> - Addresses the "per-worker" constraint: disaggregation allows workers to share cache for common prefixes (system prompts, RAG context) which account for 97% of reuse in business API traffic.
> - Motivates the transition via "disaggregated prefill and decode," where different hardware pools specialize in compute-bound prefill and memory-bound decode, using the shared cache as a data plane.
> - Evaluates the economics of disaggregation, finding that shared storage media is orders of magnitude cheaper than GPU recomputation (FLOPs).
> - Notes that while KV compression (e.g., TurboQuant) increases efficiency, it doesn't remove the structural requirement for cross-worker state sharing.
>
> **Concept links:** [[LLM Inference]], [[KV Cache]], [[Disaggregated Memory]], [[GPU Infrastructure]], [[Prefill vs Decode]], [[RAG]], [[System Prompts]], [[Storage Hierarchy]], [[Distributed Systems]]
>
> **Suggested connections:**
> - [[How flat is replacing fat in AWS data center networks.md]] — both explore architectural shifts in large-scale data center and cloud infrastructure.
> - [[Cloud Computing Infrastructure]] — the broader context for the deployment of these next-generation AI serving stacks.
> - [[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]] — relevant to discussions on context management and efficient retrieval for LLMs.
<!-- ai-summary:end -->

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bkvoLrmWGuQ1bGev-SD-Hw.png)

*The KV cache spilled out of GPU memory two years ago. The next move — fleet-wide shared storage — is a different kind of shift, driven by two forces working in the same direction.*

The KV cache has been moving down the storage hierarchy for two years. First it spilled from HBM into CPU RAM — vLLM’s CPU offload, late 2023, routine engineering. Then it spilled further into local NVMe — bigger capacity, persistence across worker restarts, around mid-2024, also routine. Each step was deeper and slower but conceptually the same shape: local storage that one inference worker could see.

The next step is not that shape. The next step is *disaggregation* — a tier visible to every worker in the fleet, on machines separate from the inference servers themselves. A wave of products has matured around this layer over the last twelve to eighteen months. Mooncake’s paper introduced a KVCache-centric disaggregated architecture in mid-2024 and went on to win the FAST ’25 best paper award. LMCache moved from UChicago research project to PyTorch Ecosystem dependency over roughly the same window. InfiniStore is building on RDMA fabrics. The major AI labs are widely understood to run in-house equivalents. NVIDIA’s Dynamo ships with disaggregated prefill and decode as a first-class deployment shape on Blackwell. SemiAnalysis’s InferenceX benchmarks (formerly InferenceMAX) now measure aggregated and disaggregated configurations side by side because both are production patterns.

This piece is about why the disaggregation step is happening, why it is qualitatively different from the previous two, and why the forces driving it are compounding rather than fading. Earlier tiers extended local memory. Disaggregation changes the role of the KV cache itself — from a local optimization artifact into shared system state on the critical path between machines.

## What the KV cache is, briefly

Transformers attend. At every layer, every token in the sequence produces three vectors — Query, Key, and Value — through learned projections. Attention matches each token’s Query against every other token’s Key, and the result is a weighted combination of those tokens’ Values. The K and V vectors are the persistent state of the computation: once computed for a token at a layer, they get read by every subsequent token at that layer.

Inference proceeds in two distinct phases with very different characteristics. *Prefill* is the one-shot pass that processes the user’s entire prompt at once — every token’s K and V vectors get computed in parallel, the cache is built, and a single first output token is produced. Prefill is compute-heavy, absorbs large batches efficiently, and is bounded by the GPU’s arithmetic throughput. *Decode* generates the rest of the response one token at a time. Each step reads the entire cache to produce one new K, V, and output token, then appends them. Decode is memory-bandwidth-heavy, runs at much lower arithmetic intensity, and is the part of inference users actually wait through. Their distinct resource profiles also motivate splitting them onto separate machines — we will come back to that as one of the two main drivers of disaggregated storage.

Storing the K and V vectors is the difference between feasible and infeasible inference. Without the cache, generating each new token would require recomputing K and V for every prior token — quadratic blowup that makes long-context generation impractical. So far, this is an internal optimization, designed to avoid recomputation within a single request, on a single GPU. The interesting story begins where the cache stops fitting that picture: when it is too large to live in HBM, too valuable to recompute on a restart, and — most importantly for what follows — too useful across worker boundaries to leave stranded on whichever GPU happened to fill it first.

## The hierarchy we already built

HBM has three production constraints that have been pushing the cache outward. (Throughout what follows, an *inference worker* is a single physical node — one or more GPUs plus the host CPU, system RAM, and any locally attached storage. The constraints below are properties of that node.)

**HBM is small.** An H100 has 80 GB. An H200 has 141 GB. A B200 has 192 GB. For a model like Llama-3.1–70B at BF16, KV cache burns roughly 320 KB per token. A 32K context fits a single user’s cache in about 10 GB. Twenty concurrent users with long contexts fills the device.

**HBM is volatile.** A worker restart — for any reason — wipes the cache. Every recent conversation, every warmed system prompt, every cached retrieval, gone. The next request pays full prefill cost from cold.

**HBM is per-worker.** Each worker holds its own HBM, its own host RAM, its own local NVMe. None of them share. If Worker 12 just processed a request that included the same 4,000-token system prompt the next request needs, and the load balancer routes that next request to Worker 37, the cache hit is invisible. The work gets redone.

The first two constraints were solved quietly over the last two years. Capacity got addressed by spilling into CPU RAM around late 2023 and into local NVMe around mid-2024. Volatility got addressed by the same NVMe step. Both moves were routine extensions of an existing pattern — deeper local tiers, same shape.

The third constraint has not been solved by anything local. CPU RAM is still on the same node. Local NVMe is still on the same node. You can stack as many tiers as you like inside the worker boundary and the per-worker problem does not go away — every node holds its own copy of the same hot prefix, and the load balancer routes around all of them.

To solve per-worker requires a tier visible to every worker. That is not a deeper local layer. That is a categorically different kind of storage. Two forces are now driving production deployments toward it.

## First motivation: cross-user prefix reuse

For the per-worker constraint to matter, the workload has to have cross-worker reuse. If every request is unique — different system prompt, different context, different user — then no amount of fleet-wide sharing helps. Each worker is doing its own thing and the architecture is fine.

The empirical question, then, is whether production AI traffic has cross-worker reuse strong enough to justify a shared tier. Until recently, that question was open. The answer, from Wang et al., “KVCache Cache in the Wild” (USENIX ATC ’25), is sharper than I expected when I first read it.

The authors analyzed traces from Aliyun’s production LLM serving — both consumer chatbots and business API workloads. The headline finding: for business API traffic, **97% of all KV cache reuses are single-turn.**

Single-turn means the reuse does not come from the same user’s conversation history. It comes from *different* users hitting the same shared prefix. The dominant reuse pattern in production business AI traffic is cross-user, not within-user.

That number is high enough to be worth explaining qualitatively. Production AI workloads concentrate on shared content by construction.

- **System prompts** are baked into a product and prepended to every user query. Modern system prompts often run several thousand tokens — they bundle the assistant persona, capability and refusal rules, tool definitions with JSON schemas and examples, formatting guidelines, and safety scaffolding into a single fixed prefix. A coding assistant might prepend the same 4,000-token bundle to every conversation across millions of users. Every cache block of that prefix is identical from one user to the next, and every prefill that runs the prefix from cold is doing work that has already been done elsewhere in the fleet.
- **RAG pipelines** retrieve top-k chunks from the same corpus in response to similar queries. Two users asking about the same product feature get many of the same documents pulled into their context. The reuse pattern here is messier than the system-prompt case — chunk ordering varies across queries, so it isn’t a strict prefix match — and capturing it efficiently is itself an active research area (CacheBlend, from the UChicago group behind LMCache, is one well-known approach that reuses precomputed KV caches regardless of prefix position by selectively recomputing a small fraction of cross-attention tokens). But the underlying repetition is real and substantial, and only a shared cache tier makes it capturable at all.

Across both patterns, cross-user repetition is structurally present, and the 97% reflects what prefix-level caching captures of it. The exact share is one well-measured workload; the structural drivers — large shared prefixes, repeated retrieval contexts, common scaffolding — appear across most production AI traffic, even when the precise reuse fraction differs by workload.

## Get Srinivasan Seshadri’s stories in your inbox

Join Medium for free to get updates from this writer.

The architectural consequence is direct. If reuse were within-user, you could solve most of it with sticky routing — pin each user to a worker, let the local cache accumulate that user’s history, get respectable hit rates without disaggregation. Per-worker caches scale that way. But cross-user reuse is structurally fleet-shared. Sticky routing captures some of it at the cost of routing flexibility — you give up load-balancing freedom and fragment cache state across the fleet, and the reuse you keep is bounded by how often the routing decision happens to align with cache locality. The cleaner answer is a tier every worker can see, which decouples cache state from routing entirely.

## Second motivation: disaggregated prefill and decode

The second motivation is architectural rather than empirical. Not every production deployment disaggregates prefill and decode today — but the pattern has moved from emerging idea to first-class deployment shape inside of eighteen months, and the resource asymmetry between the phases sharpens with scale.

The starting point is the asymmetry between prefill and decode that we introduced earlier. Prefill is compute-bound; decode is memory-bandwidth-bound. Running them on the same machine forces a compromise. Prefill saturates compute and leaves HBM bandwidth largely unused; decode saturates HBM bandwidth and leaves compute largely unused. A GPU sized for one phase carries an idle resource through the other, and the two phases interfere with each other’s batching strategies in awkward ways. Splitting them onto separate hardware pools, each tuned for its dominant resource, restores efficiency. *Disaggregated prefill and decode* is the architecture that does this — prefill workers optimized for compute throughput, decode workers optimized for memory bandwidth, connected by the KV cache as the medium of exchange.

Mooncake (Qin et al., 2024) introduced the architecture publicly; production systems at Kimi, in-house stacks at the major labs, and now NVIDIA Dynamo on Blackwell adopt it as the default deployment shape. vLLM and SGLang have first-class support through LMCache and NIXL.

The consequence for the storage tier is unambiguous. In a disaggregated deployment, the prefill machine produces KV state that the decode machine consumes. They are not the same machine, so the cache cannot live locally on either of them. A shared tier visible to both worker pools is not an optimization; it is the wire format of the system. The cache stops being an offload artifact and becomes an active data plane.

This argument is independent of the cross-user one. A deployment with no cross-user reuse at all — say, every request fully unique — still needs the shared tier the moment it disaggregates prefill from decode. The growing share of production deployments adopting disaggregation inherit the shared-tier requirement by construction.

Two forces. Same direction. Each is sufficient on its own; together they make local-only inference the choice that needs the justification.

## Why the economics work

Disaggregation has costs that the local tiers did not. There is a network hop on every fetch. There is an operationally separate system to deploy, scale, and monitor. There is coordination overhead between the inference servers and the cache tier. Each of these matters at production scale, and the question is whether the workload economics absorb them.

They do, for four reasons that compound.

**Cost asymmetry.** An H100 hour runs four to six dollars in 2026 cloud pricing. Holding the same gigabytes of cached KV state on shared SSD or networked RAM costs a small fraction of a cent per hour in pure media terms — and even after loading in the network, replication, and operational costs real storage systems carry, raw capacity economics favor storage over GPU recomputation by orders of magnitude. Every cache hit returns GPU FLOPs to the pool, where they become either headroom for more concurrent requests or a smaller fleet at fixed throughput.

**Latency asymmetry — the average request barely notices.** User-visible latency in chat-style workloads is dominated by decode, not prefill. A 1,000-token response at 20 ms per token is roughly twenty seconds of decode against maybe one or two seconds of prefill. The prefill slot is fungible — you can pay it in compute (run the prefill) or in I/O (fetch the cache). Even when a network fetch from a shared tier is *slower* than the GPU recomputation it replaces, the typical request barely moves, because prefill is a small fraction of total response time to begin with, and a fast networked tier delivers low-millisecond first-byte latency well inside that budget for typical prompt sizes. The real risk lives in the tails — incast, hot-key contention, and degraded network conditions can push fetch times outside the prefill budget, and production deployments earn their wins here by investing in topology, replication, and tail-latency engineering.

**Pipelined cache loading — throughput per dollar holds up.** The cache fetch sits on the critical path of the *request* that needs it, but at the *system* level continuous batching keeps the GPU busy with decode steps for other requests in the active batch. The fetch happens in parallel with productive work. You save the GPU cost of recomputing the prefill while the GPU continues to bill against decode work for other requests. The overlap is rarely perfect — batch fragmentation, scheduling friction, and queue fluctuation all eat into it — but in steady-state production traffic the unit economics improve in both dimensions.

**Throughput and time-to-first-token gains under high reuse.** Published benchmarks from the LMCache project — integrated into llm-d, KServe, and the vLLM Production Stack — report 3–10× reductions in time-to-first-token and up to 15× throughput improvements when a shared KV cache layer is added to vLLM, across workloads with substantial prefix reuse like multi-round question answering and document analysis. These are not marginal improvements; they are the kind of numbers that justify deploying and operating a separate tier — for the right workload.

And the shape of the working set fits a tiered cache well. The Aliyun trace data shows roughly 10% of cache blocks contributing 77% of reuses, and a P99 KV cache lifespan in business API workloads of just 97 seconds. The working set is hot, Pareto-shaped, and short-lived. A small amount of fast capacity in front of a larger warm tier captures most of the value — a workload that responds well to investment in tier design.

## A trend worth naming honestly

KV compression is sometimes invoked as evidence that the case for a separate shared tier is fragile. The trend is real and significant. INT8 and INT4 quantization cut per-token KV storage by 2 to 4x. Architectural changes like Multi-head Latent Attention, used in DeepSeek-V3, cut it further. Google’s TurboQuant (ICLR 2026) — based on online vector quantization with random orthogonal projections — achieves roughly 6x compression at near-lossless quality with no calibration data required, and has rapidly become the most-discussed answer to the KV memory bottleneck NVIDIA’s Dynamo launch at GTC 2026 put center stage. Compression is going to keep coming.

The honest read of what compression changes is this: it makes *any* cache tier more efficient. A local cache holds more useful prefixes per gigabyte. A shared cache holds more useful prefixes per gigabyte too. The benefit is symmetric across the local-vs-shared dimension.

What compression does *not* change is the cross-user reuse property. The 97% finding is about *which workers can see which prefixes*, not about how many bytes each prefix takes. No level of compression makes a local cache see another worker’s data. And no level of compression eliminates the wire-format role of the cache in disaggregated prefill/decode. If 97% of the available reuse is cross-user, then 97% of the reuse value is still captured only by a tier every worker can see — at any compression level. Compression makes the working set fit more comfortably in the shared tier. It does not move the local-versus-shared decision.

## From offload to data plane

The shift worth naming, after all this, is conceptual.

Two years ago, the KV cache was an offload artifact — bytes you stored to avoid recomputing them later. In any disaggregated deployment today, it is a data plane: an active producer-consumer flow between machines, on the critical path of every request, with throughput requirements that scale linearly with inference traffic. Same physical thing. Different role.

Two forces, working in the same direction, account for the shift. Cross-user reuse is a structural property of the workload — production AI traffic concentrates on shared prefixes, and a fleet-visible tier is the cleanest way to capture that reuse. Disaggregated prefill and decode is an architectural choice spreading fast — by construction, the deployment shape demands a shared cache tier between the worker pools. Neither argument requires the other; both lead to the same place. Compression makes the tier more efficient without dissolving the question.

The interesting question is no longer whether this tier exists. It exists. The harder question is what kind of system should fill it. The workload says a lot about the shape of the answer: high aggregate throughput, hot-key skew, fleet-wide concurrency, tail-latency-sensitive reads, billions of cache blocks with short reuse windows. Object storage, parallel file systems, and operational databases all have credible cases. Which architecture wins in practice will depend on workload mix, scale, and the operational priorities of the team building the stack.

The first question, though, is largely settled. The KV cache has become shared system state rather than local optimization — and the systems that serve it are no longer optional.

*Disclosure: I’m Chief Innovation Officer at Aerospike, an operational database company. Subsequent pieces will examine how* [*Aerospike’s*](http://www.aerospike.com/) *architecture maps to the workload shapes described here. The analysis in this piece stands on its own — no specific system is recommended.*