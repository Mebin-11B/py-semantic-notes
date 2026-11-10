---
title: "Agents need control flow, not more prompts"
url: https://bsuh.bearblog.dev/agents-need-control-flow/
clipped: 2026-06-17 01:06:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Agents need control flow, not more prompts](https://bsuh.bearblog.dev/agents-need-control-flow/)

## Digest Summary
The article argues that reliable AI agents handling complex tasks require deterministic control flow implemented in software rather than increasingly elaborate prompt chains. Prompt-based approaches become non‑deterministic, poorly specified, and hard to verify as task complexity grows, leading to unreliable reasoning and silent failures. By contrast, software architectures built from libraries, modules, and functions provide explicit state transitions, validation checkpoints, and composability that enable local reasoning and predictable behavior. The author recommends treating the language model as a component within a deterministic orchestration layer and adding aggressive error‑detection mechanisms. In systems where silent failure is possible, three mitigation strategies are outlined: (1) a human‑in‑the‑loop “babysitter” to catch errors early, (2) post‑run exhaustive verification (“auditor”), and (3) reliance on outputs without verification (“prayer”). The central claim is that moving logic from prose prompts into runtime code is essential for scaling reliable AI agents.

## Discussion Summary
The comments converge on the view that relying solely on large language‑model agents for complex, repeatable workflows is unreliable; they often miss files, repeat work, or diverge from intended control flow. Contributors stress adding deterministic scaffolding—such as external harnesses, orchestrators, quality‑gate nodes, or code‑generation steps—to capture the LLM’s creative strengths while ensuring repeatability and safety. Many advocate a layered architecture with supervisory, orchestrating, and worker agents, and note that future progress will require architectures that enforce constraints and memory beyond pure LLM prompting.

---

## Full Article

agents need control flow, not more prompts
==========================================

*07 May, 2026*

**Thesis: reliable agents tackling complex tasks need deterministic control flow encoded in software, not increasingly elaborate prompt chains**

If you’ve ever resorted to **MANDATORY** or **DO NOT SKIP**, you’ve hit the ceiling of prompting.

Imagine a programming language where statements are **suggestions** and functions return “Success” while **hallucinating**. Reasoning becomes impossible; reliability collapses as complexity grows.

Software scales through recursive composability: systems built from libraries, modules, and functions. It’s code all the way down. Code exposes predictable behavior, enabling local reasoning. Prompt chains lack this property. While useful for narrow tasks, prompts are non-deterministic, weakly specified, and difficult to verify.

Reliability requires moving logic out of prose and into runtime. We need deterministic scaffolds: explicit state transitions and validation checkpoints that treat the LLM as a component, not the system.

But deterministic orchestration is only half the battle. In a system prone to silent failure, an agent without aggressive error detection is just a fast way to reach the wrong conclusion. Without programmatic verification, we are left with three options:

1. **Babysitter**: Keep a human in the loop to catch errors before they propagate.
2. **Auditor**: Perform exhaustive end-to-end verification after the run.
3. **Prayer**: Vibe accept the outputs.