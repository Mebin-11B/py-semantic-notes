---
title: "Get Shit Done: A Meta-Prompting, Context Engineering and Spec-Driven Dev System"
url: https://github.com/gsd-build/get-shit-done
clipped: 2026-06-17 01:31:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Get Shit Done: A Meta-Prompting, Context Engineering and Spec-Driven Dev System](https://github.com/gsd-build/get-shit-done)

## Digest Summary
The repository provides “Get‑Shit‑Done” (GSD), a lightweight meta‑prompting and context‑engineering framework for Claude Code and other code‑generation models (OpenCode, Gemini CLI, Codex, Copilot, Antigravity). It mitigates “context rot” by supplying each model with a complete, XML‑formatted prompt that includes specifications, requirements, and verification steps, keeping the model’s context window small and fresh. Installation is via `npx get-shit-done-cc@latest`, with options for runtime selection (Claude, OpenCode, Gemini, etc.) and global or local deployment. The workflow consists of:

* `gsd:map-codebase` – parallel agents analyze the existing codebase.  
* `gsd:new-project` – creates PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md and a planning directory.  
* Phase execution (`gsd:discuss-phase`, `gsd:plan-phase`, `gsd:execute-phase`, `gsd:verify-work`) iteratively gathers detailed specifications, performs domain research, generates atomic XML‑based task plans, runs them in parallel “waves”, and commits each task separately.  

Verification checks code presence and test results, spawning debug agents for failures. Additional commands support quick mode, milestone management, branching strategies, and sensitive‑file protection via Claude settings. The system is open‑source (MIT) and used by engineers at major tech companies.

## Discussion Summary
Comments show a mixed view of AI‑assisted coding frameworks. Users note that planning‑heavy tools like GSD or Superpowers can boost productivity for simple or green‑field tasks but often consume many tokens, add ceremony, and struggle with larger, evolving codebases. Many cite the need for plan and work review agents, better memory handling, and robust verification to avoid security lapses. A recurring demand is for concrete production examples and benchmarks. While some report successful deployments and speed gains, others find the overhead outweighs benefits and prefer direct prompting or simpler workflows.

---

## Full Article

This repository is no longer the active home for GSD development.

The project now continues as **GSD Core** in the Open GSD repository:

<https://github.com/open-gsd/gsd-core>

Use the new repository for current source code, issues, releases, and contribution
work.