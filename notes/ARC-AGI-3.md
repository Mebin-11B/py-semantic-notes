---
title: "ARC-AGI-3"
url: https://arcprize.org/arc-agi/3
clipped: 2026-06-17 01:27:09
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [ARC-AGI-3](https://arcprize.org/arc-agi/3)

## Digest Summary
ARC-AGI-3 is an interactive reasoning benchmark designed to evaluate AI agents’ ability to explore novel environments, acquire goals dynamically, construct adaptable world models, and engage in continuous learning. Unlike static puzzles, agents must perceive relevant information, select actions, and adjust strategies based solely on experience, without natural‑language instructions. Performance metrics include 100 % human‑solvable environments, skill‑acquisition efficiency over time, long‑horizon planning with sparse feedback, and experience‑driven adaptation across multiple steps. The benchmark quantifies the gap between AI and human learning by measuring planning horizons, memory compression, and belief updating as new evidence arises. Design principles prioritize ease of human onboarding, absence of pre‑loaded knowledge or hidden prompts, clear goals with meaningful feedback, and novelty that prevents brute‑force memorization. A perfect score indicates an AI can match human efficiency across all tested games.

## Discussion Summary
Comments show mixed reactions to ARC‑AGI‑3. Many criticize the scoring system as overly complex, biased toward the second‑best human and unsuitable for judging true AGI, noting that human baselines and action‑count limits distort results. Some appreciate the benchmark’s novelty, cost‑aware design, and its role in probing LLM reasoning, while others find the “no‑tools” constraint odd and question whether visual‑puzzle tasks reflect general intelligence. Overall, the community acknowledges the benchmark’s ingenuity but doubts its adequacy as a definitive measure of artificial general intelligence.

---

## Full Article

### What is ARC-AGI-3?

ARC-AGI-3 is an interactive reasoning benchmark which challenges AI agents to explore novel environments, acquire goals on the fly, build adaptable world models, and learn continuously.

A 100% score means AI agents can beat every game as efficiently as humans.

Instead of solving static puzzles, agents must learn from experience inside each environment—perceiving what matters, selecting actions, and adapting their strategy without relying on natural-language instructions.

#### How it measures intelligence

* 100% human-solvable environments
* Skill-acquisition efficiency over time
* Long-horizon planning with sparse feedback
* Experience-driven adaptation across multiple steps

---

As long as there is a gap between AI and human learning, we do not have AGI.

ARC-AGI-3 makes that gap measurable by testing intelligence across time, not just final answers—capturing planning horizons, memory compression, and the ability to update beliefs as new evidence appears.

#### Design principles

* Easy for humans to pick up quickly
* No pre-loaded knowledge or hidden prompts
* Clear goals + meaningful feedback
* Novelty that prevents brute-force memorization