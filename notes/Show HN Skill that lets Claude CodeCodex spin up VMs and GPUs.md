---
title: "Show HN: Skill that lets Claude Code/Codex spin up VMs and GPUs"
url: https://cloudrouter.dev/
clipped: 2026-06-17 01:46:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Skill that lets Claude Code/Codex spin up VMs and GPUs](https://cloudrouter.dev/)

## Digest Summary
cloudrouter provides a CLI for creating and managing cloud development sandboxes with optional GPU resources and browser automation. Core commands include `cloudrouter start` (to launch a sandbox, syncing the current directory by default), `cloudrouter ls` (list sandboxes), `cloudrouter code|jupyter|vnc|pty` (to open VS Code, Jupyter Lab, VNC desktop, or a terminal), and `cloudrouter stop|resume|delete` (to control lifecycle). Size presets (small‑large‑xlarge) and GPU flags (T4, L4, A10G, A100, H100, etc.) configure compute; custom CPU, memory, disk, image, and timeout are also supported. File transfer uses `cloudrouter upload/download` with a `-r` remote‑path flag. Browser automation wraps agent‑browser via `cloudrouter browser` commands (open, snapshot ‑i, click, fill, wait, screenshot, etc.) and requires snapshotting before interaction. Concurrency is limited to ten active sandboxes; users should extend, pause, or delete sandboxes responsibly. Secure URLs (VS Code, VNC, Jupyter) are safe to share, whereas public E2B port‑forward URLs must never be exposed. Authentication is performed with `cloudrouter login`.

## Discussion Summary
The feedback is largely positive, praising the demo and concept while noting several areas for improvement. Reviewers request clearer documentation on required providers and authentication flow, and suggest emphasizing provider compatibility. Concerns are raised about security practices, cost controls, and the monolithic design of the Docker template, with a preference for modular, loosely coupled components. Several alternative infrastructure‑as‑code tools and platforms are mentioned as complementary options, and suggestions include tighter guardrails and more composable architecture.

---

## Full Article

Manaflow
========

Open source applied AI lab building next-gen devtools.

The open source terminal built for coding agents.

![cmux — the terminal built for coding agents](https://cloudrouter.dev/cmux-screenshot.webp)