---
title: "Agent-to-Agent Pair Programming"
url: https://axeldelafosse.com/blog/agent-to-agent-pair-programming
clipped: 2026-06-17 01:26:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Agent-to-Agent Pair Programming](https://axeldelafosse.com/blog/agent-to-agent-pair-programming)

## Digest Summary
The author proposes “loop,” a CLI tool that runs Claude and Codex side‑by‑side in tmux and bridges their communication to emulate pair programming. Drawing on research from Cursor on multi‑agent orchestration, the system designates one model as primary worker and the other as reviewer, allowing subagents to exchange feedback directly. Observations indicate that when both agents agree on a review comment, the signal is strong enough to address 100 % of the feedback, while divergent comments provide additional insight. Loop preserves context across iterations, enables proactive agent interaction, and lets a human operator intervene via the interactive TUI. The author highlights open questions for integrating this workflow into pull‑request processes, such as splitting work across PRs, sharing planning documents, and presenting proof of work. The broader claim is that multi‑agent harnesses should treat agent‑to‑agent communication as a core feature, offering benefits like vendor‑agnostic flexibility and diverse model strengths. The tool is available at https://github.com/axeldelafosse/loop.

## Discussion Summary
The discussion emphasizes a workflow that pairs different language models for distinct tasks, preferring one for creative generation and another for precise, detail‑oriented work. Users report that initial model outputs are frequently low quality, but employing self‑review mechanisms and dedicated reviewer agents markedly improves results. While the primary model is generally regarded as effective and enjoyable to use, occasional misunderstandings are noted, prompting reliance on the secondary model for direct editing and correction. Overall, the combined approach is viewed as beneficial.

---

## Full Article

Agent-to-agent pair programming
===============================

What if you could let Claude and Codex work together as pair programmers, talking to each other directly? One of them as the main worker and the other as a reviewer.

It is amusing how the best agentic workflows often look a lot like human collaboration. Researchers at Cursor discovered this in their work on long-running coding agents. That work led them to create a multi-agent workflow with a main orchestrator assigning tasks to workers. This is similar to how most human teams operate. Claude Code “Agent teams” and Codex “Multi-agent” features work similarly, with subagents reporting back to the main agent. And in the future, subagents could interact with each other, like humans do.

I wanted to pursue the idea of mimicking human collaboration with multiple agent harnesses and another workflow used by programmers: pair programming. While building a code review agent using Claude and Codex side-by-side, I found something interesting: they gave different feedback -- but even when they gave the same feedback, it wasn’t annoying: it was in fact a very strong signal. Our team addresses 100% of the feedback when both reviewers agree. Code reviews are great because they happen on a multiplayer app where humans and agents collaborate, but they are slowing down the feedback loop and can become noisy.

That’s why I built `loop`: a dead-simple CLI that launches `claude` and `codex` side-by-side in tmux, with a bridge that lets them talk to each other. It makes this feedback loop faster and more natural, while preserving context across iterations. It’s interesting because it enables the agents to be more proactive, since the interaction between them is more natural (and I expect that to only get better as the models get better too). Because `loop` runs the interactive TUIs, you can stay in the loop, steer, answer questions, and follow up if needed.

The future of agentic workflows may look less like magic automation and more like familiar teamwork. And I’m sure that there are some great observations to apply to this pair programming workflow. Some open questions around how to make the human handoff and PR review easier:

* Should we split the work across multiple PRs?
* Should we share the PLAN.md in git or in the PR description?
* Should we share a screenshot or video recording as a proof of work?

Letting the agents loop can result in more changes than expected, which are usually welcome -- but unfortunately it makes the human review harder.

A lot of people are using multiple agent harnesses for a variety of reasons: to avoid vendor lock-in, to use and contribute to an open-source project, to max out their subscriptions, or to get different perspectives, strengths, and results. Multi-agent harness apps should probably treat agent-to-agent communication as a first-class feature. I’d love to see them adopt this approach.

Try it out: <https://github.com/axeldelafosse/loop>

**Thanks** to Léna Deloizy Delafosse, Will Horn, Tian Wang and Ferruccio Balestreri for reading drafts of this.