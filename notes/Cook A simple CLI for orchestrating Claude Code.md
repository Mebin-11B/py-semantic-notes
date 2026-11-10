---
title: "Cook: A simple CLI for orchestrating Claude Code"
url: https://rjcorwin.github.io/cook/
clipped: 2026-06-17 01:30:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cook: A simple CLI for orchestrating Claude Code](https://rjcorwin.github.io/cook/)

## Digest Summary
Cook defines a lightweight DSL for orchestrating AI‑agent tasks. Its primitives are **work** (a single prompt), **loop operators** (repeat xN, review, ralph) and **composition operators** (versions vN/race, vs, pick/merge). Loop operators wrap preceding work left‑to‑right: `xN` repeats a task N times passing prior output forward; `review` adds a gated review step that iterates until a “DONE” condition is met; `ralph` provides an outer gate that advances through a task list, resetting iterations after each successful step. Composition runs parallel isolated git worktrees: `vN` spawns N identical cooks with a default “pick” resolver; `vs` runs distinct cooks side‑by‑side, each may contain its own loops, and results are merged via `pick` or `merge` criteria. Configuration is scaffolded with `cook init`, producing `COOK.md`, `.cook/config.json` (agent/model defaults, per‑step overrides, env vars), a Dockerfile, and a log directory. Execution can use an agent sandbox (`--sandbox agent`) or Docker sandbox (`--sandbox docker`), the latter required for OpenCode.

## Discussion Summary
The comments express curiosity about how the tool extends Claude‑CLI and seek clarification of its added functionality. The orchestration design is praised for its clean, declarative recipe pattern that automates execution. Several users raise cost concerns, noting that chaining multiple Claude Code calls can quickly consume API credits, and they suggest mitigating expenses by assigning cheaper model tiers to simpler steps while reserving higher‑tier models for complex reasoning. Overall, the discussion balances appreciation of the approach with practical considerations about efficiency and expense.

---

## Full Article

~\*~ ~\*~ ~\*~

cook.
=====

A simple CLI for orchestrating   
Claude Code, Codex, and OpenCode.

```
cook "Implement dark mode" review


cook "Implement dark mode" x3


cook "Implement dark mode" v3 "least code"


cook "Auth with JWT" vs "Auth with sessions" pick "best security"


cook "Work on next task in plan.md" review \
     ralph 5 "DONE if all tasks complete, else NEXT"


cook "Implement dark mode" review v3 "cleanest result"
```

Two ways to get it:

npm install -g @let-it-cook/cli

Add the `/cook` skill to Claude Code:

mkdir -p .claude/skills && \  
    cp -r $(npm root -g)/@let-it-cook/cli/skill .claude/skills/cook

[GitHub](https://github.com/rjcorwin/cook) ·
[npm](https://www.npmjs.com/package/@let-it-cook/cli)

\* Primitives
-------------

Cook parses three categories of tokens:

#### \* Work

A prompt. One agent call. The core unit.

#### \* Loop operators

Wrap work with iteration: `xN`, `review`, `ralph`.

#### \* Composition

Run parallel branches and resolve: `vN`, `vs`, `pick`.

Operators compose left to right. Each wraps everything to its left.

```
cook "work" x3 review          
cook "work" review x3          
cook "work" review v3 pick
```

\* Loop Operators
-----------------

### repeat (xN)

`xN` runs work N times sequentially, each pass seeing the previous output.

```
cook "Add dark mode" x3           
cook "Add dark mode" repeat 3     
cook "Add dark mode" x3 review    
cook "Add dark mode" review x3
```

### review

`review` adds a review→gate loop. After work, a reviewer checks quality and a gate decides DONE or ITERATE. On ITERATE, the iterate step runs, then review→gate repeats.

work
->
review
->
gate
->
iterate
<<

```
cook "Add dark mode" review           
cook "Add dark mode" review 5
```

Provide custom prompts after `review`, or use positional shorthand:

```
cook "Add dark mode" review \
     "Review for accessibility" \
     "DONE if WCAG AA, else ITERATE"


cook "Add dark mode" \
     "Review for accessibility" \
     "DONE if WCAG AA, else ITERATE"


cook "Add dark mode" \
     "Review for accessibility" \
     "DONE if WCAG AA, else ITERATE" \
     "Fix the issues" 5
```

Use different agents or models per step:

```
cook "Add dark mode" review \
  --work-agent codex --work-model gpt-5-codex \
  --review-agent claude --review-model opus
```

### ralph

Ralph wraps a cook with an outer gate for task-list progression. The work prompt is self-directing — it reads project state to find the current task each time.

```
cook "Work on next task in plan.md" \
     ralph 5 "DONE if all tasks complete, else NEXT"


cook "Work on next task in plan.md" \
     review "Code review" "DONE if no High issues, else ITERATE" \
     ralph 5 "DONE if all tasks complete, else NEXT"
```

The review gate decides **DONE** (pass to ralph) or **ITERATE** (fix and retry). The ralph gate decides **DONE** (exit) or **NEXT** (advance to next task, reset iterations).

\* Composition Operators
------------------------

Composition operators run multiple cooks in parallel isolated git worktrees, then combine the results with a resolver.

### versions (vN / race N)

`vN` runs N identical cooks in parallel worktrees. `pick` is the default resolver.

```
cook "Add dark mode" v3                       
cook "Add dark mode" v3 "least code wins"     
cook "Add dark mode" race 3 "least code wins" 

cook "Add dark mode" review v3 "cleanest"      
cook "Add dark mode" x3 v3 "most complete"
```

### vs

`vs` runs two different cooks in parallel worktrees. Each branch is a full cook — it can have its own loop operators.

```
cook "Implement auth with JWT" \
  vs \
  "Implement auth with sessions" \
  pick "best security"

cook "Build with React" review "Check accessibility" "DONE if WCAG AA" 3 \
  vs \
  "Build with Vue" review "Check bundle size" "DONE if under 50kb" 5 \
  merge "best developer experience"
```

### Resolvers

| Resolver | Behavior |
| --- | --- |
| `pick ["criteria"]` | Pick one winner. Merge that branch. Default. |
| `merge ["criteria"]` | Synthesize all results into a fresh implementation. |
| `compare` | Write a comparison doc to `.cook/compare-<session>.md`. No merge. |

\* Configuration
----------------

Run `cook init` in your project root to scaffold configuration files:

```
cook init
```

This creates:

* `COOK.md` — project instructions and agent prompt template
* `.cook/config.json` — agent/model/sandbox defaults and per-step overrides
* `.cook/Dockerfile` — project dependencies for Docker sandbox mode
* `.cook/logs/` — session logs (gitignored)

Example `.cook/config.json`:

```
{
  "agent": "claude",
  "sandbox": "agent",
  "steps": {
    "work":    { "agent": "codex",  "model": "gpt-5-codex" },
    "review":  { "agent": "claude", "model": "opus" }
  },
  "env": ["CLAUDE_CODE_OAUTH_TOKEN"]
}
```

### Sandbox Modes

| Mode | Flag | Description |
| --- | --- | --- |
| **Agent** (default) | `--sandbox agent` | Agents use their own OS-level sandboxes. No Docker required. |
| **Docker** | `--sandbox docker` | Agents run in a Docker container with restricted network access. |

> **Note:** OpenCode is only supported in Docker mode.

### Docker Network

By default, Docker sandbox restricts outbound traffic to only what each agent requires. Configure in `.cook/config.json`:

```
{
  "docker": {
    "network": {
      "mode": "restricted",
      "allowedHosts": ["api.mycompany.com"]
    }
  }
}
```

| mode | Behavior |
| --- | --- |
| `"restricted"` (default) | Blocks all outbound traffic except DNS and HTTPS to a whitelist of required agent hosts. |
| `"unrestricted"` | No network restrictions. |

`allowedHosts` adds extra hosts to the whitelist when mode is `"restricted"`.

### Commands

| Command | Description |
| --- | --- |
| `cook init` | Scaffold COOK.md, .cook/config.json, and Dockerfile |
| `cook rebuild` | Rebuild the sandbox Docker image |
| `cook doctor` | Check Docker daemon, CLI tools, and auth credentials |
| `cook shell` / `cook sandbox` | Interactive shell in the Docker sandbox |
| `cook shell <cmd>` | Run a command in the sandbox |
| `cook shell --unrestricted` | Shell with unrestricted networking |

### Rate-limit recovery

When an agent hits a token quota or rate limit, cook automatically waits and retries instead of bailing. A countdown is shown in the TUI. Enabled by default.

```
cook "Build the feature" review --no-wait
```

Configure wait behavior in `.cook/config.json`:

```
{
  "retry": {
    "enabled": true,
    "pollIntervalMinutes": 5,
    "maxWaitMinutes": 360
  }
}
```