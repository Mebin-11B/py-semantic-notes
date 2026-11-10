---
title: "Cord: Coordinating Trees of AI Agents"
url: https://www.june.kim/cord
clipped: 2026-06-17 01:42:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - ai agents
  - agent coordination
  - workflow automation
  - orchestration frameworks
  - human-in-the-loop
  - context isolation
related:
  - "[[AI Agents]]"
  - "[[Workflow Automation]]"
  - "[[Apple reveals new AI architecture built around Google Gemini models]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Cord is an agent runtime protocol that allows LLM agents to dynamically construct, parallelize, and execute a task coordination tree instead of relying on static developer-defined workflows.
>
> **Key points:**
> - Existing frameworks like LangGraph and CrewAI rely on static, developer-defined agent roles and handoffs, which restricts flexibility.
> - Cord introduces a dynamic approach where agents decompose goals at runtime into a tree of tasks using five primitive operations.
> - Primitives include `spawn` (isolated subtask with fresh context), `fork` (subtask inheriting sibling results), and `ask` (human-in-the-loop escalation).
> - Cord handles parallelization and dependency tracking (using `blocked-by`), running on an SQLite database backed by Claude Code CLI and MCP.
>
> **Concept links:** [[Ai Agents]], [[Agent Coordination]], [[Workflow Automation]], [[Orchestration Frameworks]], [[Human-In-The-Loop]], [[Context Isolation]]
>
> **Suggested connections:**
> - [[AI Agents]] — the evolution of AI from answering questions to acting on tools.
> - [[Workflow Automation]] — methods for automating complex multi-step processes.
> - [[Apple reveals new AI architecture built around Google Gemini models]] — the model family powering Apple's cloud-based and collaborative AI features.
<!-- ai-summary:end -->
# [Cord: Coordinating Trees of AI Agents](https://www.june.kim/cord)

## Digest Summary
Cord is a runtime that lets LLM agents dynamically construct and execute a coordination tree rather than following a developer‑defined static workflow. Agents start with a single goal, then use five primitives—**spawn** (create a child with a clean context), **fork** (create a child inheriting all completed sibling results), **ask** (prompt a human), **complete**, and **read_tree**—to generate sub‑tasks, express dependencies (via blocked_by), and parallelize work. The distinction between spawn and fork controls what context the child receives, enabling independent research tasks (spawn) and synthesis steps that need all prior knowledge (fork).  

Implemented with Claude Code CLI processes, an MCP tool server, and a shared SQLite database, Cord enforces dependency resolution, authority scoping, and result injection. In fifteen tests Claude correctly decomposed projects, chose appropriate primitives, and escalated via ask when authority was lacking, confirming the model’s understanding of the protocol.  

The protocol is backend‑agnostic; it could run on PostgreSQL, multiple LLM providers, or incorporate human workers. Cord is released as a proof‑of‑concept repository and requires a Claude Code CLI subscription.

## Discussion Summary
The discussion questions whether using a “spawn” API can ever be advantageous compared to a “fork,” emphasizing concerns about unnecessary context removal. It suggests that while some scenarios may require context elimination, the preferred approach would involve efficient sub‑agent compaction rather than a complete “clean‑slate” reset, which is viewed as generally suboptimal. The overall sentiment leans toward favoring strategies that preserve existing context whenever possible.

---

## Full Article

Cord: Coordinating Trees of AI Agents
=====================================

AI agents are good at doing one thing at a time. Give Claude a focused task and it performs. But real work isnât one task. Itâs a tree of tasks with dependencies, parallelism, and context that needs to flow between them.

The multi-agent frameworks are multiplying. Theyâre all solving the wrong problem.

Whatâs out there
------------------

**LangGraph** models coordination as a state machine. You define nodes and edges in Python. The developer decides upfront how agents hand off work. Itâs powerful for fixed workflows, but the graph is static. If an agent realizes mid-task that the work should be split differently, tough luck. The developer has to anticipate every decomposition pattern in advance.

**CrewAI** is role-based. You define agents with personas â âresearcher,â âanalyst,â âwriterâ â and assign them tasks. Intuitive, but the roles are decided by the developer, not discovered by the agents. A crew of three canât decide it actually needs five people, or that âresearcherâ should be split into two parallel tracks.

**AutoGen** puts agents in a group chat. They coordinate by talking to each other. Flexible, but thereâs no structure. No dependency tracking, no authority scoping, no typed results. Coordination emerges from conversation, which means itâs unpredictable and hard to inspect.

**OpenAI Swarm** is the most minimal â lightweight handoffs between agents. Agent A decides itâs time for Agent B and transfers control. Simple, but linear. No parallelism, no tree structure, no way for an agent to spawn three subtasks and wait for all of them.

**Claudeâs tool-use loops** â Anthropicâs own pattern â put a single agent in a loop with tools. Handles sequential complexity well but runs into context window limits on large tasks and canât parallelize. One agent, one thread, one context.

The common thread: every framework requires the developer to predefine the coordination structure. *You* decide the workflow graph, the agent roles, the handoff pattern. The agents execute within your boundaries.

This made sense when agents were unreliable. Youâd never let GPT-3 decide how to decompose a project. But current models are good at planning. They break problems into subproblems naturally. They understand dependencies. They know when a task is too big for one pass.

So why are we still hardcoding the decomposition?

Let the agent build the tree
----------------------------

I built [Cord](https://github.com/kimjune01/cord). You give it a goal:

```
cord run "Should we migrate our API from REST to GraphQL? Evaluate and recommend."
```

One agent launches. It reads the goal, decides it needs research before it can answer, and creates subtasks:

```
â #1 [active] GOAL Should we migrate our API from REST to GraphQL?
  â #2 [active] SPAWN Audit current REST API surface
  â #3 [active] SPAWN Research GraphQL trade-offs for our stack
  â #4 [pending] ASK How many concurrent users do you serve?
    blocked-by: #2
  â #5 [pending] FORK Comparative analysis
    blocked-by: #3, #4
  â #6 [pending] SPAWN Write migration recommendation
    blocked-by: #5
```

No workflow was hardcoded. The agent decided this structure at runtime.

It parallelized the API audit (#2) and the GraphQL research (#3). It created an `ask` node (#4) â a question for the human â because it realized the recommendation depends on scale, something it canât research on its own. It blocked #4 on #2 because the question makes more sense with the audit results as context. It made #5 a `fork` so the analysis inherits everything learned so far. And it sequenced the final recommendation after the analysis.

Then you watch it run:

```
â #2 [complete] SPAWN Audit current REST API surface
  result: 47 endpoints. 12 heavily nested resources...
â #3 [complete] SPAWN Research GraphQL trade-offs
  result: Key advantages: reduced over-fetching...

? How many concurrent users do you serve?
  Options: <1K, 1K-10K, 10K-100K, >100K
> 10K-100K

â #5 [active] FORK Comparative analysis
  blocked-by: #3, #4
```

The research runs in parallel. When both finish and you answer the question, the analysis launches with all three results in its context. It produces a recommendation tailored to your actual scale and API surface â not a generic blog post about GraphQL.

Spawn vs fork
-------------

This is the one idea I think is genuinely new: the distinction between `spawn` and `fork` as a context-flow primitive.

A **spawned** agent gets a clean slate. Just its prompt and the results of nodes it explicitly depends on. Like hiring a contractor â hereâs the spec, go. Cheap to restart, easy to reason about.

A **forked** agent gets all completed sibling results injected into its context. Like briefing a team member â they know everything the team has learned so far. More expensive, but necessary for analysis that builds on prior work.

This isnât about concurrency. Both can run in parallel or sequentially. Itâs about *what the child knows*. In the example above, the agent chose `spawn` for the independent research tasks and `fork` for the analysis that needs everything. It made this choice correctly â because the tool descriptions explain the distinction clearly. Thatâs the point: the protocol is learnable from its interface alone.

The natural next step is making context flow a first-class primitive â a `context_query` parameter on spawn/fork that takes a natural language instruction like `"summary"`, `"relevant details from a web designer's perspective"`, or `"bullet points about error handling"`. A compaction subagent would read the parentâs full context, distill it according to the query, and pass only the result to the child. This has to be built into the client itself â an isolated MCP tool canât access the parentâs context without serializing the whole thing as a tool input, which defeats the purpose.

Under the hood
--------------

Each agent is a Claude Code CLI process with MCP tools backed by a shared SQLite database:

* `spawn(goal, prompt, blocked_by)` â create a child task
* `fork(goal, prompt, blocked_by)` â create a context-inheriting child
* `ask(question, options)` â ask the human a question
* `complete(result)` â mark yourself done
* `read_tree()` â see the full coordination tree

Agents know theyâre a node in a coordination tree â the system prompt tells them â but they donât manage it. They see tools and use them as needed. The protocol â dependency resolution, authority scoping, result injection â is enforced by the MCP server.

When an `ask` node becomes ready, the engine pauses to prompt the human in the terminal. The answer is stored as a result, and downstream nodes unblock. The human is a participant in the tree, not an observer.

~500 lines of Python. SQLite + MCP.

Behavioral testing as design validation
---------------------------------------

Before writing the runtime, I needed to know if the protocol was learnable from its interface alone. So I built a throwaway MCP server with the five tools, pointed Claude Code at it, and ran 15 tests. No runtime, no engine â just Claude, the tools, and a task.

The interesting results werenât the correct tool calls. They were the emergent behaviors. An agent asked to decompose a project called `read_tree()` before acting and again after to verify â read, act, verify, unprompted. An agent that got rejected for trying to stop a sibling escalated through `ask parent` â the correct pattern, but one Iâd never described. An agent that hit an error stopped the failing child and respawned a new one with an adjusted prompt.

15/15 passed. The passing rate wasnât the insight â it was that clear tool descriptions plus dependency semantics were sufficient for correct use. That told me the runtime was worth building.

What this is not
----------------

This implementation uses Claude Code CLI and SQLite. But the protocol â five primitives, dependency resolution, authority scoping, two-phase lifecycle â is independent of all that.

You could implement Cord over Postgres for multi-machine coordination. Over the Claude API directly, without the CLI overhead. With multiple LLM providers â GPT for cheap tasks, Claude for complex ones. With human workers for some nodes.

The protocol is the contribution. This repo is a proof of concept.

Try it
------

```
git clone https://github.com/kimjune01/cord.git
cd cord
uv sync
cord run "your goal here" --budget 2.0
```

You can also point it at a planning doc:

```
cord run plan.md --budget 5.0
```

The root agent reads the markdown and decomposes it into a coordination tree. Write your plan however you want â bullet points, sections, prose â and the agent figures out the task structure, dependencies, and parallelism.

Requires [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) and a subscription that includes it.

[GitHub](https://github.com/kimjune01/cord) | [RFC](https://github.com/kimjune01/cord/blob/master/RFC.md) | [HN Discussion](https://news.ycombinator.com/item?id=47096466)