---
title: "Cursor 3"
url: https://cursor.com/blog/cursor-3
clipped: 2026-06-17 01:23:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cursor 3](https://cursor.com/blog/cursor-3)

## Digest Summary
Cursor 3 is a redesigned, agent‑centric IDE that unifies local and cloud development workflows. The interface supports multi‑workspace projects, letting humans and AI agents operate across multiple repositories simultaneously. All agents—local, cloud, and those triggered from mobile, web, Slack, GitHub, or Linear—appear in a shared sidebar; cloud agents generate visual demos for verification. Users can transfer an agent session between cloud and desktop instantly, enabling on‑device edits with Composer 2 (a high‑limit coding model) or background execution when offline. A new diffs view streamlines staging, committing, and PR management. Additional features include full LSP navigation, an integrated browser for local site interaction, and a marketplace offering hundreds of plugins (MCPs, skills, subagents) with private team options. Cursor 3 aims to provide the core model, product, and runtime needed for more autonomous agents and collaborative AI‑enhanced coding, while retaining a conventional IDE fallback.

## Discussion Summary
Comments show mixed reactions to Cursor’s recent direction. Many users criticize the shift toward a chat‑first, agent‑centric UI, feeling it diminishes code‑centric workflows, adds unnecessary complexity, and replicates designs of competing tools, while also raising cost and performance concerns. Some appreciate the ability to switch models, integrated cloud agents, and occasional productivity gains, especially for large codebases, but a sizable portion plans to revert to traditional IDEs or alternative platforms, citing better value, familiarity, and more effective developer control. Overall sentiment leans toward disappointment with the new approach.

---

## Full Article

Software development is changing, and so is Cursor.

In the last year, we moved from manually editing files to working with agents that write most of our code. How we create software will continue to evolve as we enter the [third era of software development](https://cursor.com/blog/third-era), where fleets of agents work autonomously to ship improvements.

We're building toward this future, but there is a lot of work left to make it happen. Engineers are still micromanaging individual agents, trying to keep track of different conversations, and jumping between multiple terminals, tools, and windows.

**We're introducing Cursor 3, a unified workspace for building software with agents.** The new Cursor interface brings clarity to the work agents produce, pulling you up to a higher level of abstraction, with the ability to dig deeper when you want. It's faster, cleaner, and more powerful, with a multi-repo layout, seamless handoff between local and cloud agents, and the option to switch back to the Cursor IDE at any time.

[#](https://cursor.com/blog/cursor-3#whats-new-in-cursor-3)What's new in Cursor 3
---------------------------------------------------------------------------------

When we started building Cursor, we forked VS Code instead of building an extension so we could shape our own surface. With Cursor 3, we took that a step further by building this new interface from scratch, centered around agents.

### [#](https://cursor.com/blog/cursor-3#all-your-agents-in-one-place)All your agents in one place

The new interface is inherently multi-workspace, allowing humans and agents to work across different repos.

### [#](https://cursor.com/blog/cursor-3#run-many-agents-in-parallel)Run many agents in parallel

Working with agents is now much easier. All local and cloud agents appear in the sidebar, including the ones you kick off from mobile, web, desktop, Slack, GitHub, and Linear.

Cloud agents produce demos and screenshots of their work for you to verify. This is the same experience you get at [cursor.com/agents](https://cursor.com/agents), now integrated into the desktop app.

### [#](https://cursor.com/blog/cursor-3#new-ux-for-handoff-between-local-and-cloud)New UX for handoff between local and cloud

We made moving agents between environments really fast.

Move an agent session from cloud to local when you want to make edits and test it on your own desktop. [Composer 2](https://cursor.com/blog/composer-2), our own frontier coding model with high usage limits, is great for iterating quickly.

In the reverse direction, you can move an agent session from local to cloud to keep it running while you're offline, or so that you can move on to the next task. This is especially useful for longer-running tasks that would otherwise get interrupted when you close your laptop.

### [#](https://cursor.com/blog/cursor-3#go-from-commit-to-merged-pr)Go from commit to merged PR

The new diffs view allows you to edit and review changes faster with a simpler UI. When you're ready, you can stage, commit, and manage PRs.

[#](https://cursor.com/blog/cursor-3#building-on-the-best-features-of-cursor)Building on the best features of Cursor
--------------------------------------------------------------------------------------------------------------------

Alpha users told us that a lot of what they like about Cursor 3 is the way it combines the best parts of the IDE with more recent capabilities we've shipped in an agent-first interface.

### [#](https://cursor.com/blog/cursor-3#files-for-understanding-code)Files for understanding code

Dive deeper anytime by viewing files, and go to definition in the editor with full LSPs.

### [#](https://cursor.com/blog/cursor-3#integrated-browser)Integrated browser

Cursor can use the built-in [browser](https://cursor.com/docs/agent/tools/browser) to open, navigate, and prompt against local websites.

### [#](https://cursor.com/blog/cursor-3#plugins-on-the-cursor-marketplace)Plugins on the Cursor Marketplace

Browse hundreds of [plugins](https://cursor.com/docs/plugins) that extend agents with MCPs, skills, subagents, and more. Install with one click, or set up your own [team marketplace](https://cursor.com/docs/plugins#team-marketplaces) of private plugins.

[#](https://cursor.com/blog/cursor-3#the-best-way-to-code-with-ai)The best way to code with AI
----------------------------------------------------------------------------------------------

With Cursor 3, we have the foundational pieces in place—model, product, and runtime—to build more autonomous agents and better collaboration across teams. We will also continue to invest in the IDE until codebases are self-driving.

This won't be the last time the interface for building software changes. More powerful coding models will unlock new interaction patterns. We are excited to continue to build, simplify, and transform Cursor to be the best way to code with AI.

Upgrade Cursor, and type `Cmd+Shift+P -> Agents Window` to try the new interface. Or learn more in our [docs](https://cursor.com/docs/agent/agents-window).