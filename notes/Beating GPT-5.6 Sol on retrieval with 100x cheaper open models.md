---
title: "Beating GPT-5.6 Sol on retrieval with 100x cheaper open models"
url: https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency
clipped: 2026-08-31 12:22:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Beating GPT-5.6 Sol on retrieval with 100x cheaper open models](https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency)

## Digest Summary
Castform integrates with Neon’s Lakebase (Postgres) search extensions to combine context retrieval and model training for agentic LLM workflows. While early RAG pipelines relied on static embedding similarity, recent multi‑hop “agentic” searches require repeated model calls, inflating latency (&gt;10 s) and cost (~$0.03 per request) for frontier models such as gpt‑5.6‑sol. Castform enables reinforcement‑learning (RL) post‑training of open‑weight models—up to 100× cheaper—by automatically converting proprietary corpora (docs, support articles, wikis, etc.) into synthetic question‑answer pairs, defining a reward function (retrieval accuracy, citation correctness, answer correctness), and looping through Neon’s hybrid text/vector search (bm25 + vector via lakebase_text / lakebase_vector). The platform provides full observability of reward progress and per‑task debugging, while Neon’s dynamic compute scaling, branching, and time‑travel queries handle bursty, stateful rollouts without provisioning permanent capacity. Overall, Castform lets developers fine‑tune open‑source models to outperform frontier APIs at far lower inference cost and latency.

---

## Full Article

[A deep dive on the lakebase storage: S3 + WAL for the era of agents](https://neon.com/blog/wal-s3-lakebase-storage-for-the-era-of-agents)[Back to Blog](https://neon.com/blog)/[Product](https://neon.com/blog/category/product)

# Training 100x Cheaper Retrieval models Neon and Castform

Using data in your Postgres (Neon + Lakebase Search) to train a 4B open-source model to be as accurate as GPT-5.6 SolPranav Aurora, Ying Hang Seah, Angel PanAug 05, 2026

## Subscribe to our changelog

Receive only our latest updates. No spam, guaranteed.Subscribe

“Most teams' best training data is just sitting in their databases. The problem is that turning raw data into something usable is hard, and letting agents read, search, and mutate data cheaply at scale requires advanced infra. Pointing Castform at Neon skips both.”Ying Hang Seah, cofounder, Castform

A "good agent" needs to be strong in 2 areas:

- Context: can we provide the tools to find the right data?

- Model: can the model decide what to search for?

[Neon](https://neon.com/) (Lakebase Postgres) and their new [Search](https://neon.com/blog/lakebase-search-on-neon) extensions solve the first; [Castform](https://castform.com/) solves the second.

## Evolution of agentic search

In ~2022, the industry was going all in on embedding search. Every database provider added one, and pgvector was Neon's most downloaded extension. To provide context to LLMs, engineers handcrafted RAG pipelines, which in essence, is some form of embedding similarity search.

In ~2025, agents started to gain more traction. Developers started creating multi-hop search workflows, decomposing big problems into smaller ones. Retrieval has shifted from the one-shot search systems to agentic retrieval. Instead of issuing a single query, models plan and search multiple times in a loop. Every loop iteration meant another call to the frontier model, increasing the overall cost and latency per user request.

Concretely, a typical multi-turn search request with gpt-5.6-sol takes >10s and costs ~$0.03 end-to-end, making it prohibitively slow and expensive.

Meanwhile, small open-weights models are 100x cheaper. But, out of the box, their capabilities lag behind closed api models. RL post-training helps bridge this gap. On specific tasks like search, post-trained open-source models can match & beat frontier models while costing orders of magnitude less per request.

That is why we built Castform: to enable developers to RL post-train models without having to deal with machine learning & gpu internals. The goal's to make post-training as approachable as prompt engineering.

## How does Castform use Neon?

Castform's pipeline runs against Neon via Lakebase Search:
StageNeon + Lakebase SearchCorpus storageRaw documents live in Postgres on NeonSynthetic data generationCastform training pipeline uses  `lakebase_text`  and  `lakebase_vector`  to write training tasksRL TrainingEvery rollout's search tool call uses Lakebase Search on NeonProduction InferenceThe final model uses the same search tool call during inference

## Your best training data already exists

To perform RL post-training effectively, you need a task (e.g. answer a user's question), the environment for the agent to run in (e.g. a search tool for your corpus) and a reward function (e.g. is the answer correct?).

With all 3 pieces in place, the RL post-training is a loop of trial and error: the model attempts the task given the tools, the reward function scores the attempt, and the feedback signal guides the model on how to hill-climb its way to optimal performance.

Yet, most companies do not have a clean dataset of tasks and reward functions ready for post-training.

Enterprises do have a large set of proprietary data:

- internal documentation

- product records

- support articles

- customer interactions

- wikis

- operational databases

This data contains the knowledge an agent needs, but turning it into an effective training dataset normally requires substantial data engineering and manual labeling.

That leads many teams to dismiss post-training for one of two reasons:

- "We don't have the training data."

- "Fine-tuning is too difficult and requires infrastructure we don't have."

Castform addresses both. It turns an [existing corpus into training tasks](https://castform.com/blog/rag-to-riches/), then manages the RL loop needed to teach an open-source model how to use that data effectively.

## Using Castform

With Castform, you can turn your company knowledge base into a model:

- Document (from your data): Trains booked through Navan will be paid by GitLab travel card. Train rides must be standard cabin class with 14 day booking lead time

- Ground truth (inferred from your data): Train rides must be standard cabin class with a 14 day booking lead time.

- Question (synthetically generated): When booking a rail trip in Navan, what are the rules for how early I need to reserve it and which seating level I'm expected to choose?

With the generated question-answer dataset, Castform lets you scaffold the training run by specifying the tools the agent has access to and a reward function.

The reward function specifies what you want your model to get good at. In our case, we want it to retrieve the correct chunks, cite the right sources along with providing the right final answer.
 ` `def run_tool(tool, tool_args):
    """Single tool: hybrid search over Lakebase."""
    if tool == "search":
        query = tool_args["query"]
        bm25 = neon.lakebase_text(query, k)
        vector = neon.lakebase_vector(query, k)
        return rrf_merge(bm25, vector, k)

def reward(trace, ground_truth):
    """Grade a trace against the ground-truth answer."""
    answer = parse_trace(trace)
    retrieval = ...     # did it retrieve the right source
    citation = ...      # did it cite the right chunk
    correctness = ...   # did it land on the right answer
    return retrieval + citation + correctness` ` 

See a comprehensive code example [here](https://github.com/castform-ai/benchmax/tree/main/examples/neon_rag).

## Observability: Watch the model learn

Castform gives you full observability into your RL run. You can monitor your reward climb with each step, but more importantly you can drop into individual tasks/prompts to watch how the model performs qualitatively, allowing you to debug problems such as broken tools or reward hacking.

For more details on how to monitor your training runs, you can check out the [Castform blog here](https://castform.com/blog/monitoring-rl-runs/). You can also check out our [example training run here](https://app.castform.com/train/a7a898f6-d802-4908-b044-acb812f14a48?tab=train).
Average reward

## Why Neon 'just works'

During training, the agent repeatedly calls Lakebase Search until it has enough context to answer. Across thousands of parallel rollouts, each potentially making dozens of calls, this creates a highly bursty workload.

Neon's dynamic compute scaling absorbs these peaks without requiring Castform to provision for maximum capacity around the clock. Training runs get low-latency search when demand spikes, while compute scales down during idle periods.

This infrastructure becomes even more valuable as agents move beyond search and begin modifying data. Training stateful agents requires isolated environments that can be created and reset cheaply, preventing one rollout's actions from affecting another or touching production.

[Neon branching](https://neon.com/docs/introduction/branching) can give each rollout an isolated database state, while time-travel queries make it possible to reconstruct and inspect the state an agent encountered. Combined with autoscaling and scale-to-zero, this creates a path toward training thousands of stateful agent rollouts without maintaining thousands of continuously running environments.

Castform makes it easy for any developer to post-train open-source models to be cheaper, faster, better than the frontier. Post-train your first model today at [castform.com](https://castform.com).Share:

## More from Neon

[Product](https://neon.com/blog/category/product)Aug 25, 2026

# 

[Just landed in the Neon CLI](https://neon.com/blog/just-landed-in-the-neon-cli)[Engineering](https://neon.com/blog/category/engineering)Aug 24, 2026

# 

[WAL + S3: Lakebase storage for the era of agents](https://neon.com/blog/wal-s3-lakebase-storage-for-the-era-of-agents)[Product](https://neon.com/blog/category/product)Aug 20, 2026

# 

[Open-weight models are fast on Neon AI Gateway. Here's why](https://neon.com/blog/open-weight-models-are-fast-on-neon-ai-gateway)
