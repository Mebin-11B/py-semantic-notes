---
title: "Ex-GitHub CEO launches a new developer platform for AI agents"
url: https://entire.io/blog/hello-entire-world/
clipped: 2026-06-17 01:46:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Developer Tools
  - Version Control
  - Multi-Agent Systems
  - Software Development Lifecycle
  - Semantic Reasoning
  - Git Metadata
related:
  - "[[Claude Code for Infrastructure]]"
  - "[[CLI agents make self-hosting on a home server easier and fun]]"
  - "[[Chroma Context-1 Training a Self-Editing Search Agent]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Former GitHub CEO Thomas Dohmke has launched Entire, a developer platform for AI agents backed by a $60M seed round, starting with an open-source CLI to version-control agent reasoning and transcripts alongside Git commits.
>
> **Key points:**
> - Entire is founded to address the limitations of the traditional human-centric software development lifecycle in the era of high-velocity AI code generation.
> - The company's platform features a git-compatible database for code and reasoning, a universal semantic reasoning layer, and an AI-native SDLC.
> - The first release, Entire CLI, introduces "Checkpoints" to save ephemeral agent context (prompts, tool calls, transcripts) as metadata associated with Git commits.
> - Checkpoints are pushed to a dedicated branch (`entire/checkpoints/v1`), providing an append-only audit log that lets humans and agents review the intent and context behind code changes.
> - Funded with a $60M seed investment, the startup plans to extend Entire CLI support across multiple coding agents to enable collaborative multi-agent memory.
>
> **Concept links:** [[Developer Tools]], [[Version Control]], [[Multi-Agent Systems]], [[Software Development Lifecycle]], [[Semantic Reasoning]], [[Git Metadata]]
>
> **Suggested connections:**
> - [[Claude Code for Infrastructure]] — Related to agentic terminal-based coding tools like Claude Code mentioned in the article.
> - [[CLI agents make self-hosting on a home server easier and fun]] — Another discussion of command line AI agents.
> - [[Chroma Context-1 Training a Self-Editing Search Agent]] — Another perspective on versioning or managing agent-based editing context.
<!-- ai-summary:end -->

# [Ex-GitHub CEO launches a new developer platform for AI agents](https://entire.io/blog/hello-entire-world/)

## Digest Summary
The provided text consists solely of a heading: “Hello Entire World · Entire,” with no additional narrative, data, or technical information. No further content is available to summarize.

## Discussion Summary
Comments show a split between recognition of a genuine need for better observability and provenance of agent‑generated code and skepticism that the proposed solution adds real value beyond existing git‑based practices. Proponents highlight auditability, debugging across sessions, and the scarcity of tools that capture full reasoning, while critics point to storage overhead, adoption friction, redundant functionality, and the hype surrounding large funding rounds. Many cite similar open‑source attempts and suggest tighter integration with current workflows, concluding that the idea has merit but its necessity and market fit remain uncertain.

---

## Full Article

> **\*TLDR:** Today, we are announcing our new company, Entire, backed by a [$60 million seed round to build the world's next developer platform](https://entire.io/news/former-github-ceo-thomas-dohmke-raises-60-million-seed-round). We are also shipping our first product as open source CLI to tie agent context into Git on every push.\*

The game has changed. The system is cracking.
---------------------------------------------

In the last few months alone, the fundamental role of a developer has been refactored. From Anthropic's Claude Code with Opus 4.6, to OpenAI's latest GPT-5.3-Codex agentic coding model, to Cursor's Composer 1.5 and more, advancements in agentic intelligence have turned the flow of coding on its head. The terminal is becoming the new center of gravity, as developers prompt fleets of agents across multiple terminal windows at once. Spec-driven development is becoming the primary driver of code generation. Agents now interoperate in parallel, generating and evaluating hundreds of variants simultaneously. As a result, massive volumes of code are being generated faster than any human can reasonably understand.

**Yet today, we still rely on a software development lifecycle built before the era of the cloud, inherently designed for human-to-human collaboration.** And the cracks are forming. Issues were designed for human planning and tracking, not as structured, machine-readable units of work. Git repositories were never extended to version everything developers build with in the AI era. Pull requests simply do not scale for large monorepos. Every day, agents are being choked and throttled by centralized API capacity and rate limits. The truth is: the entire software ecosystem is being bottlenecked by a manual system of production that was never designed for the era of AI in the first place. A system that cannot be retrofitted for what's ahead.

Just like when automotive companies replaced the traditional craft-based production system with the moving assembly line, we must now reimagine the entire software development lifecycle for a world where machines are the primary producers of code. Creating the assembly line for the era of agents.

Announcing Entire: The world's next developer platform
------------------------------------------------------

**This is the purpose of our new company [Entire](https://entire.io/vision), to build the world's next developer platform where agents and humans can collaborate, learn, and ship together.** A platform that will be open, scalable, and independent for every developer, no matter which agent or model you use.

Entire will be based on three key components: **a git-compatible database** that unifies code, intent, constraints, and reasoning in a single version-controlled system; a universal **semantic reasoning layer** that enables multi-agent coordination through the context graph; and an **AI-native software development lifecycle** to reinvent agent-to-human collaboration.

In pursuit of this [vision](https://entire.io/vision), we are proud to be **backed by a $60 million seed investment led by Felicis, with support from Madrona, M12, Basis Set, 20VC, Cherry Ventures, Picus Capital, and Global Founders Capital**. Entire is further backed by a slate of international investors including Gergely Orosz, Theo Browne, Jerry Yang, Olivier Pomel, Garry Tan, and othersâwho all understand that software development is ready for its next platform shift.

![Entire funding announcement](https://entire.io/blog/hello-entire-world/entire-funding-announcement-even-logos.png)

Our first release: The Entire CLI to track agent context
--------------------------------------------------------

Today, agent sessions are ephemeral. Prompts live in terminals and reasoning lives in context windows. The decisions, constraints, and iteration that produce code disappears the moment you close the session. Git preserves what changed, but nothing about why. With agents generating hundreds or thousands of lines per session, this context loss compounds fast. Without shared context, agents can't collaborate effectively. They retrace steps, duplicate reasoning, waste tokens, and lose the thread of decisions made hours or days earlier.

Our first ship makes that missing context durable:

**Checkpoints are a new primitive that automatically captures agent context as first-class, versioned data in Git.** When you commit code generated by an agent, Checkpoints capture the full session alongside the commit: the transcript, prompts, files touched, token usage, tool calls and more. This context becomes the foundational write-path of our semantic reasoning layer. You can browse checkpoints by branch, drill into individual sessions, and trace how your codebase evolved through human-and-agent collaboration commit by commit.

Our plan is to support Checkpoints for every agent. Today, Entire CLI ships with support for Anthropic's Claude Code and Google Gemini CLI. Codex, Cursor CLI, and other agents coming soon.

### How it works

Checkpoints run as a Git-aware CLI. On every commit generated by an agent, it writes a structured checkpoint object and associates it with the commit SHA. The code stays exactly the same, we just add context as first-class metadata. When you push your commit, Checkpoints also pushes this metadata to a separate branch (entire/checkpoints/v1), giving you a complete, append-only audit log inside your repository. As a result, every change can now be traced back not only to a diff, but to the reasoning that produced it.

Checkpoints are useful immediately:

* **Traceability** - inspect the reasoning behind any agent-generated change
* **Faster Reviews** - review intent and constraints, not just diffs
* **Better handoffs** - resume work without replaying prompts or sessions
* **Less token waste** - agents stop repeating mistakes that you corrected in past sessions
* **Multi-session and agent support** - support for concurrent agentic sessions

### Getting Started

The best part is that you can set up Entire in two easy steps.

curl`curl -fsSL https://entire.io/install.sh | bash`

Then navigate to your repository and run `entire enable` â follow the prompts to configure Entire for that project. That's it. Your agent sessions are captured automatically - in a structured and ready-to-use format.

No more stealth. We are building in the open!
---------------------------------------------

Checkpoints are our first step towards building a universal semantic reasoning layer for agents. Today, it gives you traceability and history. Tomorrow, it will become the shared memory that allows agents to coordinate, hand off context and build together without collision or loss of understanding.

Most importantly, we're releasing the [Entire CLI](https://github.com/entireio/cli) open source project because we believe that this layer should be portable, independent, and available for every single agent or model. And because we know, we are better with the contributions of the interconnected community of open-source developers.

Our roadmap will be directly paved by your feedback, in [Discord](https://discord.gg/jZJs3Tue4S) and in GitHub [Discussions](https://github.com/entireio/cli/discussions). We're ready for it. See you there.