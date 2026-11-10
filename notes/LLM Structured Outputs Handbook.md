---
title: "LLM Structured Outputs Handbook"
url: https://nanonets.com/cookbooks/structured-llm-outputs
clipped: 2026-06-17 01:57:37
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [LLM Structured Outputs Handbook](https://nanonets.com/cookbooks/structured-llm-outputs)

## Digest Summary
The handbook addresses the challenge that large language models (LLMs) sometimes produce malformed structured data (e.g., JSON, XML, code) due to their probabilistic generation, which hampers programmatic uses such as data extraction, code generation, and tool calling. It provides developers with a comprehensive guide covering: the internal mechanisms of LLM output generation; the most effective tools and techniques for enforcing deterministic, well‑formed outputs; criteria for selecting appropriate methods; strategies for building, deploying, and scaling such systems; and approaches to minimize latency and cost while improving output quality. The document is intended as a regularly updated reference, usable either as a full read‑through or as a lookup resource. It is authored by the maintainers of Nanonets‑OCR models (vision‑language models for converting documents to structured Markdown) and the docstrange open‑source document‑processing library. A newsletter offers bi‑monthly updates on developer insights, breakthroughs, and tools.

## Discussion Summary
The comments collectively praise the guide as clear, well‑illustrated, and valuable for understanding grammar‑constrained generation, highlighting its usefulness for reliable structured outputs in pipelines and on limited hardware. Contributors note that structured generation is under‑utilized, reference several related libraries, papers, and blog posts, and agree that deterministic formats like JSON are crucial for production agents, while acknowledging occasional parsing challenges and questioning the need for unconstrained JSON when outputs target humans. Overall sentiment is strongly positive with minor technical reservations.

---

## Full Article

LLMs mostly produce syntactically valid outputs when we try generating JSON, XML, code, etc., but they can occasionally fail due to their probabilistic nature. This is a problem for developers as we use LLMs programmatically, for tasks like data extraction, code generation, tool calling, etc.

![breaktasks](https://nanonets.com/cookbooks/structured-llm-outputs/assets/images/pipedream-a9e6cafdfc5a2b271cc2ff623cc21e68.png)

LLMs came with the promise of agents and automation. But without structured outputs, it’s just a pipe dream.

There are many deterministic ways to ensure structured LLM outputs. If you are a developer, this handbook covers everything you need.

* What happens under-the-hood?
* What are the best tools & techniques?
* How to pick the right tools & techniques?
* How to build, deploy, and scale systems?
* How to optimize for latency and cost?
* How to improve the quality of output?

Motivation[​](https://nanonets.com/cookbooks/structured-llm-outputs#motivation "Direct link to Motivation")
-----------------------------------------------------------------------------------------------------------

Structured generation is moving too fast. Most resources you find today are already outdated. You have to dig through multiple academic papers, blogs, GitHub repos, and other resources.

This handbook brings it all together in a living document that updates regularly.

How to use this[​](https://nanonets.com/cookbooks/structured-llm-outputs#how-to-use-this "Direct link to How to use this")
--------------------------------------------------------------------------------------------------------------------------

You can read it start-to-finish, or treat it like a lookup table.

Who are we?[​](https://nanonets.com/cookbooks/structured-llm-outputs#who-are-we "Direct link to Who are we?")
-------------------------------------------------------------------------------------------------------------

We're the maintainers of [Nanonets-OCR models](https://huggingface.co/nanonets/models) (VLMs to convert documents into clean, structured Markdown) and [docstrange](https://github.com/NanoNets/docstrange) (open-source document processing library).

### Subscribe to our newsletter

Updates from the LLM developer community in your inbox. Twice a month.

* Developer insights
* Latest breakthroughs
* Useful tools & techniques