---
title: "Pi – a minimal terminal coding harness"
url: https://pi.dev
clipped: 2026-06-17 01:40:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Pi – a minimal terminal coding harness](https://pi.dev)

## Digest Summary
pi.dev is a minimal, terminal‑based coding harness that can be customized through TypeScript extensions, skills, prompt templates, and themes, distributed as npm or git packages. It supports over 15 AI providers (Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi, MiniMax, OpenRouter, Ollama, etc.) with API‑key or OAuth authentication, and allows model switching mid‑session via `/model`, Ctrl+L, or Ctrl+P. Sessions are stored as a single tree‑structured file, navigable with `/tree`, exportable to HTML (`/export`) or GitHub Gist (`/share`). Context engineering is handled via customizable system prompts (`SYSTEM.md`), auto‑summarization (compaction), and dynamic extensions that can inject messages, implement RAG, or maintain long‑term memory. Messaging supports steering (`Enter`) and follow‑up (`Alt+Enter`) while the agent runs. Four interaction modes are provided: interactive TUI, print/JSON, RPC (JSON over stdin/stdout), and SDK embedding. Core functionality is intentionally minimal; features such as sub‑agents, plan mode, permission dialogs, to‑dos, or background bash are expected to be added via extensions or third‑party packages.

## Discussion Summary
Comments show strong overall enthusiasm for Pi, highlighting its speed, extensibility, modular architecture and suitability as a daily driver, especially when integrated with tools like Emacs or custom GUIs. Users appreciate the transparency and ability to tailor commands, extensions and plans, and many cite successful community forks and lightweight deployments. Critiques focus on missing features such as sub‑agents or plan mode, concerns about cost, sandboxing and security, and mixed impressions of alternative harnesses. The consensus leans toward Pi being a favored, flexible option while noting areas for improvement.

---

## Full Article

Why Pi?
-------

Pi - manipulate the website

Pi is a minimal agent harness. Adapt Pi to your workflows, not the other way around. Customize Pi with [extensions](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#extensions), [skills](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#skills), [prompt templates](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#prompt-templates), and [themes](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#themes). Bundle them as [Pi packages](https://pi.dev/packages) and share via npm or git.

Pi ships with powerful defaults but skips features like sub-agents and plan mode. Ask Pi to build what you want, or install a package that does it your way.

Four modes: interactive, print/JSON, [RPC, and SDK](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#programmatic-usage). See [OpenClaw](https://github.com/OpenClaw/OpenClaw) for a real-world integration.

[Read the docs](https://pi.dev/docs/latest)

Change the harness, not your workflow
-------------------------------------

Pi - Build a custom workflow extension

Pi isn't a sealed product. If you need a command, tool, provider, workflow, or UI tweak, just ask Pi to build it. It will customize itself on the fly.

Have Pi manipulate itself in place, hit `/reload`, and keep going. If you think others will find what you built useful, share it!

15+ providers, hundreds of models
---------------------------------

Pi - Switch models mid-session

Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi For Coding, MiniMax, OpenRouter, Ollama, and more. Authenticate via API keys or OAuth.

Switch models mid-session with `/model` or `Ctrl+L`. Cycle through your favorites with `Ctrl+P`.

Add custom providers and models via [models.json](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs/models.md) or [extensions](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs/custom-provider.md).

Tree-structured, shareable history
----------------------------------

Pi - Branch and share a session tree

Sessions are stored as trees. Use `/tree` to navigate to any previous point and continue from there. All branches live in a single file. Filter by message type, label entries as bookmarks.

Export to HTML with `/export`, or upload to a GitHub gist with `/share` and get a shareable URL that renders it. [Example session](https://pi.dev/session/#0ea51497613daf7e1de28ee99950b074).

Context engineering
-------------------

Pi - Load project skills and instructions

Pi's [minimal system prompt](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/system-prompt.ts) and extensibility let you do actual context engineering. Control what goes into the context window and how it's managed.

**AGENTS.md:** Project instructions loaded at startup from `~/.pi/agent/`, parent directories, and the current directory.

**SYSTEM.md:** Replace or append to the default system prompt per-project.

**Compaction:** Auto-summarizes older messages when approaching the context limit. Fully customizable via [extensions](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/custom-compaction.ts): implement topic-based compaction, code-aware summaries, or use different summarization models.

**Skills:** Capability packages with instructions and tools, loaded on-demand. Progressive disclosure without busting the prompt cache. See [skills](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#skills).

**Prompt templates:** Reusable prompts as Markdown files. Type `/name` to expand. See [prompt templates](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#prompt-templates).

**Dynamic context:** [Extensions](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#extensions) can inject messages before each turn, filter the message history, implement RAG, or build long-term memory.

Steer or follow up
------------------

Pi - Steer a running agent

Submit messages while the agent works. `Enter` sends a steering message (delivered after current tool, interrupts remaining tools). `Alt+Enter`sends a follow-up (waits until the agent finishes).

Four modes
----------

Pi - Generate a shell script in print mode

**Interactive:** The full TUI experience.

**Print/JSON:** `pi -p "query"` for scripts, `--mode json` for event streams.

**RPC:** JSON protocol over stdin/stdout for non-Node integrations. See [docs/rpc.md](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs/rpc.md).

**SDK:** Embed Pi in your apps. See [OpenClaw](https://github.com/OpenClaw/OpenClaw) for a real-world example.

Primitives, not features
------------------------

Pi - Install a third-party extension

Features that other agents bake in, you can build yourself. Extensions are TypeScript modules with access to tools, commands, keyboard shortcuts, events, and the full TUI.

[Sub-agents](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/subagent/), [plan mode](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/plan-mode/), [permission gates](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/permission-gate.ts), [path protection](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/protected-paths.ts), [SSH execution](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/ssh.ts), [sandboxing](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/sandbox/), MCP integration, custom editors, status bars, overlays.

Don't want to build it? Ask Pi to build it for you. Or install a [package](https://pi.dev/packages) that does it your way. See the [50+ examples](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/).

Bundle extensions, skills, prompts, and themes as packages. Install from npm or git:

`$ pi install npm:@foo/pi-tools  
$ pi install git:github.com/badlogic/pi-doom`

![Doom running in Pi](https://pi.dev/doom-extension.png)

Fig. 01 | DOOM EXTENSION