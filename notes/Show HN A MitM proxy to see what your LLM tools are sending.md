---
title: "Show HN: A MitM proxy to see what your LLM tools are sending"
url: https://github.com/jmuncor/sherlock
clipped: 2026-06-17 01:51:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: A MitM proxy to see what your LLM tools are sending](https://github.com/jmuncor/sherlock)

## Digest Summary
The GitHub repository **jmuncor/sherlock** provides a tool for intercepting Large Language Model (LLM) API traffic and visualizing token usage in a real‑time terminal dashboard. It enables developers to track API costs, debug prompts, and monitor context‑window consumption during AI development sessions. The project is implemented in Python, licensed under an open‑source license, and built on the **mitmproxy** platform to capture HTTP traffic. It includes integrations for Anthropic’s Claude service and references related contributors (e.g., @jmuncor, @claude, @kolarski). Access to the repository page returned the message “You can’t perform that action at this time,” indicating restricted access or a temporary error.

## Discussion Summary
The comments show strong interest in the tool’s ability to observe and control Claude Code traffic, with many users praising its usefulness for debugging, token‑budget management, and post‑mortem analysis. There is a recurring desire for easier integration, such as OpenTelemetry export, plugin‑style extensions, and support for other LLM providers and Bedrock. Security and privacy concerns are noted, especially regarding MITM‑proxy usage and certificate handling. Users also ask about configuration steps, SSL requirements, and whether the solution could evolve into broader enterprise‑grade observability offerings.

---

## Full Article

Tokentap (formerly Sherlock)
============================

**Token Tracker for LLM CLI Tools**

[![Python](https://camo.githubusercontent.com/f12b46fe26968f97149ee10725a248ec02c28ce205f9f5d3c40ef06a38de8ea0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31302b2d3337373641423f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/f12b46fe26968f97149ee10725a248ec02c28ce205f9f5d3c40ef06a38de8ea0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31302b2d3337373641423f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)
[![License](https://camo.githubusercontent.com/8bb50fd2278f18fc326bf71f6e88ca8f884f72f179d3e555e20ed30157190d0d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e2e737667)](https://camo.githubusercontent.com/8bb50fd2278f18fc326bf71f6e88ca8f884f72f179d3e555e20ed30157190d0d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e2e737667)
[![Platform](https://camo.githubusercontent.com/09bd1562a600554ab1374f91b4008b5ab76f2b940faeb41a15b6946cffc63a62/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d6d61634f532532302537432532304c696e75782d6c69676874677265792e737667)](https://camo.githubusercontent.com/09bd1562a600554ab1374f91b4008b5ab76f2b940faeb41a15b6946cffc63a62/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d6d61634f532532302537432532304c696e75782d6c69676874677265792e737667)
[![Claude Code](https://camo.githubusercontent.com/c218c58e48b7f31182f3664134ce3747a222f0b408afa99f62edf37b0493860a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c617564655f436f64652d737570706f727465642d626c756576696f6c65742e737667)](https://camo.githubusercontent.com/c218c58e48b7f31182f3664134ce3747a222f0b408afa99f62edf37b0493860a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c617564655f436f64652d737570706f727465642d626c756576696f6c65742e737667)
[![Gemini](https://camo.githubusercontent.com/b8bb6c31bf306ffc19082cfae80ff75e76ca5b56043ea7807481a107ecf2bc54/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f47656d696e695f434c492d737570706f727465642d626c75652e737667)](https://camo.githubusercontent.com/b8bb6c31bf306ffc19082cfae80ff75e76ca5b56043ea7807481a107ecf2bc54/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f47656d696e695f434c492d737570706f727465642d626c75652e737667)
[![Codex](https://camo.githubusercontent.com/e6f5e69ee333710b88d48195c2e538385987c01b80dae51cdcabb072746a2526/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d737570706f727465642d677265656e2e737667)](https://camo.githubusercontent.com/e6f5e69ee333710b88d48195c2e538385987c01b80dae51cdcabb072746a2526/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d737570706f727465642d677265656e2e737667)
[![MiniMax](https://camo.githubusercontent.com/8e5b1b4df03bfd6035020c544066590a091f32527958d3e1b05d449a6187c6dc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d696e694d61782d737570706f727465642d6f72616e67652e737667)](https://camo.githubusercontent.com/8e5b1b4df03bfd6035020c544066590a091f32527958d3e1b05d449a6187c6dc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d696e694d61782d737570706f727465642d6f72616e67652e737667)

[Installation](https://github.com/jmuncor/sherlock#installation) •
[Quick Start](https://github.com/jmuncor/sherlock#quick-start) •
[Features](https://github.com/jmuncor/sherlock#features) •
[Commands](https://github.com/jmuncor/sherlock#commands) •
[Contributing](https://github.com/jmuncor/sherlock#contributing)

---

tokentap tracks token usage for LLM CLI tools with a live terminal dashboard. See exactly how many tokens you're using in real-time.

* **Track Token Usage**: See exactly how many tokens each request consumes
* **Monitor Context Windows**: Visual fuel gauge shows cumulative usage against your limit
* **Debug Prompts**: Automatically saves every prompt as markdown and JSON for review
* **Zero Configuration**: No certificates, no setup - just install and go

Or install from source:

```
git clone https://github.com/jmuncor/tokentap.git
cd tokentap
pip install -e .
```

### Terminal 1: Start the Dashboard

You'll be prompted to choose where to save captured prompts, then the dashboard appears:

```
┌─────────────────────────────────────────────────────────────┐
│  TOKENTAP - LLM Traffic Inspector                           │
├─────────────────────────────────────────────────────────────┤
│  Context Usage  ████████████░░░░░░░░░░░░░░░░  42%           │
│                 (84,231 / 200,000 tokens)                   │
├─────────────────────────────────────────────────────────────┤
│  Time     Provider    Model                      Tokens     │
│  14:23:01 Anthropic   claude-sonnet-4-20250514   12,847     │
│  14:23:45 Anthropic   claude-sonnet-4-20250514   8,234      │
│  14:24:12 Anthropic   claude-sonnet-4-20250514   15,102     │
├─────────────────────────────────────────────────────────────┤
│  Last Prompt: "Can you help me refactor this function..."   │
└─────────────────────────────────────────────────────────────┘
```

### Terminal 2: Run Your LLM Tool

```
# For Claude Code
tokentap claude

# For Gemini CLI (see known issues)
tokentap gemini

# For OpenAI Codex
tokentap codex

# For MiniMax-powered tools
tokentap run --provider minimax python my_app.py
```

That's it! Watch the dashboard update in real-time as you work.

Real-time token tracking with color-coded fuel gauge:

* Green: < 50% of limit
* Yellow: 50-80% of limit
* Red: > 80% of limit

Every intercepted request is saved to your chosen directory:

* **Markdown** - Human-readable format with metadata
* **JSON** - Raw API request body for debugging

When you exit, see your total usage:

```
Session complete. Total: 84,231 tokens across 12 requests.
```

| Command | Description |
| --- | --- |
| `tokentap start` | Start the proxy and dashboard |
| `tokentap claude` | Run Claude Code with proxy configured |
| `tokentap gemini` | Run Gemini CLI with proxy configured |
| `tokentap codex` | Run OpenAI Codex CLI with proxy configured |
| `tokentap run --provider <name> <cmd>` | Run any command with proxy configured |

Supported providers for `--provider`: `anthropic`, `openai`, `gemini`, `minimax`

```
tokentap start [OPTIONS]

Options:
  -p, --port NUM    Proxy port (default: 8080)
  -l, --limit NUM   Token limit for fuel gauge (default: 200000)
```

```
tokentap claude [OPTIONS] [ARGS]...

Options:
  -p, --port NUM    Proxy port (default: 8080)
```

```
┌─────────────────────────────────────────────────────────────────┐
│  Terminal 1: tokentap start                                     │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  HTTP Proxy (localhost:8080)                                ││
│  │  + Dashboard                                                ││
│  │  + Prompt Archive                                           ││
│  └─────────────────────────────────────────────────────────────┘│
└───────────────────────────────┬─────────────────────────────────┘
                                │ HTTP
                                │
┌───────────────────────────────┴─────────────────────────────────┐
│  Terminal 2: tokentap claude                                    │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  Sets ANTHROPIC_BASE_URL=http://localhost:8080              ││
│  │  Runs: claude                                               ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                                │
                                │ HTTPS
                                ▼
                      ┌───────────────────┐
                      │ api.anthropic.com │
                      └───────────────────┘
```

For OpenAI-compatible providers like [MiniMax](https://www.minimaxi.com), tokentap uses
path-prefix routing so requests are forwarded to the correct upstream API:

```
tokentap run --provider minimax python my_app.py
  → sets OPENAI_BASE_URL=http://localhost:8080/minimax/v1
  → requests arrive at /minimax/v1/chat/completions
  → proxy strips prefix, forwards to https://api.minimax.io/v1/chat/completions
```

| Provider | Command | Status |
| --- | --- | --- |
| Anthropic (Claude Code) | `tokentap claude` | Supported |
| Google (Gemini CLI) | `tokentap gemini` | Blocked by upstream issue |
| OpenAI (Codex) | `tokentap codex` | Supported |
| MiniMax | `tokentap run --provider minimax <cmd>` | Supported |

Gemini CLI currently has a [known issue](https://github.com/google-gemini/gemini-cli/issues/15430) where it ignores custom base URLs when using OAuth authentication. tokentap's Gemini support will work automatically once the Gemini CLI team fixes this issue.

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

```
git clone https://github.com/jmuncor/tokentap.git
cd tokentap
python -m venv venv
source venv/bin/activate
pip install -e .
```

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jmuncor/tokentap/blob/main/LICENSE) file for details.

---

*See what's really being sent to the LLM. Track. Learn. Optimize.*

[tokentap.ai](https://tokentap.ai)