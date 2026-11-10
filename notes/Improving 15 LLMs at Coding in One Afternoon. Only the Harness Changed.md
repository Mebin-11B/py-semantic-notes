---
title: "Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed"
url: http://blog.can.ac/2026/02/12/the-harness-problem/
clipped: 2026-06-17 01:46:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Coding Agents
  - Harness Engineering
  - Hashline Edit Format
  - Benchmark Evaluation
  - Developer Tooling
  - API Vendor Restrictions
related:
  - "[[Using AI to write better code more slowly]]"
  - "[[Learn Claude Code by doing, not reading]]"
  - "[[Chroma Context-1 Training a Self-Editing Search Agent]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article introduces "hashline," a line-level hashing harness that dramatically increases LLM coding success rates and reduces token costs by simplifying edit matching logic.
>
> **Key points:**
> - The "harness"—the interface through which an LLM reads and modifies files—is often a bigger bottleneck than the model's intelligence.
> - Traditional edit mechanisms (diff patches and search-and-replace strings) fail frequently because models struggle with exact formatting and whitespace replication.
> - "hashline" resolves this by appending unique hashes to each line in the source file, allowing models to reference target lines by ID.
> - In benchmarks, hashline improved edit success rates across 15 models, showing the largest gains in weaker models (e.g. Grok-Code-Fast from 6.7% to 68.3%) and cutting token usage by up to 61%.
> - The author notes that cloud API provider restrictions and account suspensions hinder open-source harness benchmarking, urging the community to focus on open client-side developer tools.
>
> **Concept links:** [[Coding Agents]], [[Harness Engineering]], [[Hashline Edit Format]], [[Benchmark Evaluation]], [[Developer Tooling]], [[API Vendor Restrictions]]
>
> **Suggested connections:**
> - [[Using AI to write better code more slowly]] — Focuses on AI coding performance, quality, and the developer interface.
> - [[Learn Claude Code by doing, not reading]] — Directly relates to developer agents (Claude Code) and edit harnesses.
> - [[Chroma Context-1 Training a Self-Editing Search Agent]] — Another developer tool project optimizing agent-based codebase editing.
<!-- ai-summary:end -->

# [Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed](http://blog.can.ac/2026/02/12/the-harness-problem/)

## Digest Summary
The article argues that coding‑assistant performance depends more on the harness—the interface that presents files, applies edits, and manages state—than on the underlying LLM. Existing agents use three main edit formats: OpenAI‑style `apply_patch` diffs, simple `str_replace` substitutions, and a dedicated cursor model (e.g., Aider). These formats often fail because they require exact token‑level reproduction of source text, leading to high patch‑failure rates (e.g., 50 % for Grok‑4, 46 % for GLM‑4.7).  

The author introduces “hashline”, a line‑level tagging scheme where each line receives a short content hash (e.g., `2:f1`). Edits reference these tags instead of raw text, allowing the harness to verify line identity before applying changes and eliminating dependence on whitespace or exact matches.

A benchmark generated 180 mutated React files per run, described in plain English, and evaluated 16 models with three edit tools. Results show hashline consistently outperforms patch and often beats replace; weaker models gain the most (e.g., Grok‑Code‑Fast 1 improves from 6.7 % to 68.3 %). Token usage drops up to 61 % due to fewer retries.  

The author notes vendor restrictions (Anthropic blocking OpenCode, Google disabling a Gemini account) hinder community‑driven harness improvements, emphasizing that open‑source harness engineering offers the highest‑leverage path to more reliable coding tools. All code and benchmark data are released under the “oh‑my‑pi” project.

## Discussion Summary
The discussion emphasizes that tooling and harness design are as crucial as model quality, with many participants citing concrete gains from better edit formats, structured diffs, and AST‑based tools. While some view reported improvements as modest or overstated, a majority agrees that engineering refinements can outweigh raw model advances and that open‑source, customizable harnesses are needed. Concerns are raised about token waste, platform bans, and benchmark inflation, yet overall sentiment is that focused harness work offers significant, under‑exploited efficiency and reliability benefits.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: 520 Server Error: <none> for url: http://blog.can.ac/2026/02/12/the-harness-problem/
> You can view the original article page directly [here](http://blog.can.ac/2026/02/12/the-harness-problem/).