---
title: "Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory"
url: https://github.com/localgpt-app/localgpt
clipped: 2026-06-17 01:47:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Rust
  - Game Engines
  - Bevy
  - Local AI
  - Semantic Search
  - Sandbox Security
  - Model Context Protocol
related:
  - "[[Tinybox – Offline AI device 120B parameters]]"
  - "[[CLI agents make self-hosting on a home server easier and fun]]"
  - "[[Ask HN Has anyone replaced ClaudeGPT with a local model for daily coding]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** LocalGPT is an open-source, local-first AI assistant written in Rust that supports natural-language 3D world building using Bevy, and features persistent markdown-based memory with SQLite-vec search and kernel-enforced sandboxing.
>
> **Key points:**
> - The project includes `localgpt-gen`, a Bevy-powered tool to build interactive 3D worlds (shapes, materials, lighting, audio) from natural language prompts, with support for MCP and headless modes.
> - The `localgpt` assistant runs entirely offline, leveraging XDG directories and a markdown-based workspace layout (`MEMORY.md`, `HEARTBEAT.md`, `SOUL.md`) for persistent state and task queueing.
> - Memory indexing is handled via SQLite FTS5 for full-text search and `sqlite-vec` for local embeddings-based semantic search.
> - Security features include a kernel-enforced sandbox (Seatbelt on macOS, Landlock/seccomp on Linux), HMAC-SHA256 signed policy files, and prompt injection defenses.
> - It supports both local backends (Ollama, LM Studio) and cloud APIs (Anthropic, OpenAI) without dependencies on Node.js or Python.
>
> **Concept links:** [[Rust]], [[Game Engines]], [[Bevy]], [[Local AI]], [[Semantic Search]], [[Sandbox Security]], [[Model Context Protocol]]
>
> **Suggested connections:**
> - [[Tinybox – Offline AI device 120B parameters]] — Related to hardware/devices for running large AI models locally.
> - [[CLI agents make self-hosting on a home server easier and fun]] — Discussions on running AI assistants and agents on local machines.
> - [[Ask HN Has anyone replaced ClaudeGPT with a local model for daily coding]] — Contextual discussion on replacing cloud services with local models.
<!-- ai-summary:end -->

# [Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory](https://github.com/localgpt-app/localgpt)

## Digest Summary
The page is identified as the GitHub repository “localgpt-app/localgpt.” No descriptive information about the project, its purpose, codebase, or documentation is provided. Instead, the only visible message states, “You can’t perform that action at this time,” indicating that the viewer lacks the required permissions or that the request was blocked. Consequently, the content offers no technical details, usage instructions, or source files for the repository; it merely conveys the repository name and an access‑restriction notice. No further data or context can be extracted from the provided snippet.

## Discussion Summary
The comments express enthusiasm for the project’s innovative, cyber‑punk feel and its potential to reshape device interaction, while also noting admiration for the integration of local‑first concepts. However, reviewers question the reliance on external LLM providers, seeking truly offline inference and clearer documentation. Several users discuss practical integration challenges, such as iMessage access without extensive permissions, and compare the tool to alternatives they find cumbersome or buggy. Overall, there is a mix of excitement, desire for greater locality, and calls for improved usability and transparency.

---

## Full Article

[LocalGPT](https://camo.githubusercontent.com/f5481f3526a022789b3fd6a224ac8b63e849356ae640004cd069b06c1a185f84/68747470733a2f2f6c6f63616c6770742e6170702f6c6f676f2f6c6f63616c6770742d69636f6e2d6170702e737667) LocalGPT
=======================================================================================================================================================================================================================

[![License](https://camo.githubusercontent.com/b29de0acdfd19013f1f02689b15c933e4a6c145be9efa718288f88ba3280b1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c75652e737667)](https://github.com/localgpt-app/localgpt#license)
[![Crates.io](https://camo.githubusercontent.com/df07e42246ad4701b97cee82b4efd0c46bb60ca1de2db28cf252bc64e6761e26/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f6c6f63616c6770742e737667)](https://crates.io/crates/localgpt)
[![Downloads](https://camo.githubusercontent.com/e364c969624bdcc9893ff27db888f6034257bfea7fdbeaf03159d0d76a837197/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f642f6c6f63616c6770742e737667)](https://crates.io/crates/localgpt)
[![Docs](https://camo.githubusercontent.com/48801d485e006f9ea339fdeeb0cac273fa916b3845faa309469271e4137635e5/68747470733a2f2f646f63732e72732f6c6f63616c6770742f62616467652e737667)](https://docs.rs/localgpt/latest/localgpt)
[![CI](https://github.com/localgpt-app/localgpt/workflows/CI/badge.svg)](https://github.com/localgpt-app/localgpt/actions)
[![Discord](https://camo.githubusercontent.com/56d8eb8d55c546643d22aba42ce4371c4460c17d370ed0fbeae99d2c282ae1f2/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3639313035323433313532353637353034382e7376673f6c6162656c3d266c6f676f3d646973636f7264266c6f676f436f6c6f723d66666666666626636f6c6f723d373338394438266c6162656c436f6c6f723d364137454332)](https://discord.gg/spKRr6mRyp)

Build explorable 3D worlds with natural language — geometry, materials, lighting, audio, and behaviors. Open source, runs locally.

[![LocalGPT Gen Demo](https://camo.githubusercontent.com/a7bd1bf993074570e5a6896272ff550fda77efdbf6943680466ff07cf708bdac/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f525f5f74673759593054382f6d617872657364656661756c742e6a7067)](https://www.youtube.com/watch?v=R__tg7YY0T8)

### From crates.io (for users)

If you just want to run LocalGPT — no source checkout needed:

```
# World Building
cargo install localgpt-gen

# AI Assistant (chat, memory, daemon)
cargo install localgpt
```

### From source (for developers)

If you've cloned the repository and want to hack on the code, use `cargo run` to iterate without installing:

```
git clone https://github.com/localgpt-app/localgpt.git
cd localgpt

# World Building
cargo run -p localgpt-gen -- "Create a desert scene with pyramids"

# AI Assistant
cargo run -- chat
cargo run -- daemon start
```

Full options (feature flags, headless builds, Docker): see [Installation](https://localgpt.app/docs/installation).

[LocalGPT](https://camo.githubusercontent.com/67873b0bc1132b38406f77a632c7594ed8fe760c50618a33bc2a8c4244216796/68747470733a2f2f6c6f63616c6770742e6170702f6c6f676f2f6c6f63616c6770742d69636f6e2e737667) Gen Mode (World Building)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`localgpt-gen` is a standalone binary for AI-driven 3D world creation with the Bevy game engine.

```
# Start interactive mode
localgpt-gen

# Start with an initial prompt
localgpt-gen "Create a desert scene with pyramids and a UFO hovering above"

# Load an existing scene
localgpt-gen --scene ./world.glb

# Verbose logging
localgpt-gen --verbose
```

* **Parametric shapes** — box, sphere, cylinder, capsule, plane, torus, pyramid, tetrahedron, icosahedron, wedge
* **PBR materials** — color, metalness, roughness, emissive, alpha, double-sided
* **Lighting** — point, spot, directional lights with color and intensity
* **Behaviors** — orbit, spin, bob, look\_at, pulse, path\_follow, bounce
* **Audio** — ambient sounds (wind, rain, forest, ocean, cave) and spatial emitters
* **Export** — glTF/GLB, HTML (browser-viewable), screenshots
* **World skills** — save/load complete worlds as reusable skills

### Headless Mode & Experiment Queue

Queue world experiments and generate without a window — overnight batch runs, CI pipelines, or scripted variations:

```
# Generate a single world (no window)
localgpt-gen headless --prompt "Build a cozy cabin in a snowy forest"

# With style hint
localgpt-gen headless --prompt "Village marketplace" --style "Studio Ghibli"
```

The memory system learns your creative style across sessions — palettes, lighting preferences, entity templates — and applies them automatically in future generations.

Full docs: [Headless Mode & Experiment Queue](https://localgpt.app/docs/gen/headless)

Use Gen from Claude Desktop, Codex Desktop, or any MCP-compatible editor (VS Code, Zed, Cursor):

Add to Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```
{
  "mcpServers": {
    "localgpt-gen": {
      "command": "localgpt-gen",
      "args": ["mcp-server"]
    }
  }
}
```

For CLI tools (Claude CLI, Gemini CLI, Codex CLI), use `--connect` to route tool calls to your existing window. See [CLI Mode (MCP Relay)](https://localgpt.app/docs/gen/cli-mode).

Full docs: [LocalGPT Gen](https://localgpt.app/docs/gen) | [MCP Server](https://localgpt.app/docs/gen/mcp-server)

Built something cool? Share on [Discord](https://discord.gg/spKRr6mRyp) or [YouTube](https://www.youtube.com/@localgpt-gen)!

---

`localgpt` is a local-first AI assistant with persistent memory, autonomous tasks, and multiple interfaces.

```
# Interactive chat
localgpt chat

# Single question
localgpt ask "What is the meaning of life?"

# Run as daemon with HTTP API and web UI
localgpt daemon start
```

* **Single binary** — no Node.js, Docker, or Python required
* **Local device focused** — runs entirely on your machine, your data stays yours
* **Persistent memory** — markdown-based knowledge store with full-text and semantic search
* **Hybrid web search** — native provider search passthrough plus client-side fallback
* **Autonomous heartbeat** — delegate tasks and let it work in the background
* **Multiple interfaces** — CLI, web UI, desktop GUI, Telegram bot
* **Defense-in-depth security** — signed policy files, kernel-enforced sandbox, prompt injection defenses
* **Multiple LLM providers** — LM Studio, Ollama, Anthropic, OpenAI, xAI, GLM, Vertex AI, CLI providers

LocalGPT uses XDG-compliant directories for config/data/state/cache. Run `localgpt paths` to see resolved paths.

Workspace memory layout:

```
<workspace>/
├── MEMORY.md     # Long-term knowledge (auto-loaded each session)
├── HEARTBEAT.md  # Autonomous task queue
├── SOUL.md       # Personality and behavioral guidance
└── knowledge/    # Structured knowledge bank
```

Files are indexed with SQLite FTS5 for keyword search and sqlite-vec for semantic search with local embeddings.

Stored at `<config_dir>/config.toml`:

**Local models via LM Studio** (no API key, fully offline):

```
[agent]
default_model = "openai/qwen/qwen3.5-35b-a3b"

[providers.openai]
api_key = "lm-studio"
base_url = "http://127.0.0.1:1234/v1"
```

**Cloud providers** (Anthropic, OpenAI, etc.):

```
[agent]
default_model = "claude-cli/opus"

[providers.anthropic]
api_key = "${ANTHROPIC_API_KEY}"
```

Full config reference: [`website/docs/configuration.md`](https://github.com/localgpt-app/localgpt/blob/main/website/docs/configuration.md)

* **Kernel-enforced sandbox** — Landlock/seccomp on Linux, Seatbelt on macOS
* **Signed policy files** — HMAC-SHA256 signed `LocalGPT.md` with tamper detection
* **Prompt injection defenses** — marker stripping, pattern detection, content boundaries
* **Audit chain** — hash-chained security event log

Security docs: [`website/docs/sandbox.md`](https://github.com/localgpt-app/localgpt/blob/main/website/docs/sandbox.md) | [`website/docs/localgpt.md`](https://github.com/localgpt-app/localgpt/blob/main/website/docs/localgpt.md)

| Endpoint | Description |
| --- | --- |
| `GET /` | Embedded web UI |
| `POST /api/chat` | Chat with assistant |
| `POST /api/chat/stream` | SSE streaming chat |
| `GET /api/memory/search?q=<query>` | Search memory |

Full API reference: [`website/docs/http-api.md`](https://github.com/localgpt-app/localgpt/blob/main/website/docs/http-api.md)

```
localgpt chat                   # Interactive chat
localgpt ask "question"         # Single question
localgpt daemon start           # Start daemon
localgpt memory search "query"  # Search memory
localgpt config show            # Show config
localgpt paths                  # Show resolved paths
```

Full CLI reference: [`website/docs/cli-commands.md`](https://github.com/localgpt-app/localgpt/blob/main/website/docs/cli-commands.md)

Rust, Tokio, Axum, Bevy, SQLite (FTS5 + sqlite-vec), fastembed, eframe

[![](https://camo.githubusercontent.com/53322a9af1540810eb1bfce4c1593005ef0312874e15f2e69f9921e9aef48a20/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6c6f63616c6770742d6170702f6c6f63616c677074)](https://github.com/localgpt-app/localgpt/graphs/contributors)

[Apache-2.0](https://github.com/localgpt-app/localgpt/blob/main/LICENSE)