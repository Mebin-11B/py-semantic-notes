---
title: "Open Code Review – An AI-powered code review CLI tool"
url: https://github.com/alibaba/open-code-review
clipped: 2026-06-17 00:52:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - code review
  - artificial intelligence (ai)
  - cli tools
  - devops & ci/cd
  - ai coding agents
related:
  - "[[Code Review]]"
  - "[[Artificial Intelligence (AI)]]"
  - "[[CLI Tools]]"
  - "[[DevOps & CI/CD]]"
  - "[[AI Coding Agents]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Alibaba open-sources Open Code Review (OCR), an AI-powered code review CLI tool combining deterministic engineering constraints with dynamic LLM agent decision-making.
>
> **Key points:**
> - Originated from Alibaba's internal code review system and released under the Apache-2.0 license.
> - Combines deterministic logic (precise file selection, smart bundling, templates, positioning) with an LLM agent (scenario-tuned prompts, tools, code retrieval) to improve review accuracy.
> - Exposes multiple installation paths (npm, binaries, source) and flexible configuration via interactive CLI commands or environment variables.
> - Supports workspace reviews, branch comparisons, single commit reviews, and rule configuration using a four-layer priority model.
> - Integrates directly with agents as a skill, a Claude Code command plugin, or a local Codex plugin, and includes a secure local web viewer for review logs.
>
> **Concept links:** [[Code Review]], [[Artificial Intelligence (AI)]], [[CLI Tools]], [[DevOps & CI/CD]], [[AI Coding Agents]]
>
> **Suggested connections:**
> - [[Code Review]] — the automation of code defect detection and architectural feedback in development pipelines.
> - [[AI Coding Agents]] — how CLI-based reviewers act as plugins or skills for tools like Claude Code and Codex.
> - [[DevOps & CI/CD]] — integrating automated JSON-formatted reviews into Merge/Pull Request flows.
<!-- ai-summary:end -->

# [Open Code Review – An AI-powered code review CLI tool](https://github.com/alibaba/open-code-review)

## Digest Summary
Open Code Review (OCR) is an AI‑powered CLI tool for automated code review, originated from Alibaba’s internal system and now open‑sourced under Apache‑2.0. It processes Git diffs, sends changed files to a configurable LLM (OpenAI, Anthropic, etc.) via an agent with tool‑use capabilities, and returns structured, line‑level comments.  

**Hybrid architecture**:  
- *Deterministic engineering* enforces hard constraints—precise file selection, smart bundling of related files, rule‑based matching, and independent positioning/reflection modules to guarantee coverage and comment accuracy.  
- *Agent* handles dynamic decisions—scenario‑tuned prompts, a curated toolset, and contextual code retrieval.  

**Installation**: available via npm (`npm i -g @alibaba-group/open-code-review`), pre‑built binaries for macOS/ Linux/ Windows, or source build (`make build`).  

**Configuration**: set LLM endpoint, token, model via `ocr config set` or environment variables (`OCR_LLM_URL`, `OCR_LLM_TOKEN`, etc.). Config stored in `~/.opencodereview/config.json`.  

**Usage**: `ocr review` for workspace, `ocr review --from main --to feature-branch`, `ocr review --commit `, with `--format json` for CI integration. Supports rule files (four‑layer priority, first‑match‑wins) and concurrency control.  

**Integrations**: can be added as a skill (`npx skills add alibaba/open-code-review`), Claude Code plugin, or direct command file; also provides a web viewer for session logs with host‑allowlist security. Telemetry via OpenTelemetry is optional.

## Discussion Summary
The discussion emphasizes strong interest in AI‑driven code review, noting that integrating such tools directly into Git can quickly add value and alleviate review bottlenecks. Users report positive outcomes with existing services like Coderabbit and custom multi‑model approaches, while also expressing concerns about pricing, feature overreach, and corporate attitudes that diminish appeal. There is curiosity about comparative performance on benchmarks and a desire for affordable, effective alternatives to replace internal or legacy review pipelines. Overall sentiment is cautiously optimistic but price‑sensitive.

---

## Full Article

[![OpenCodeReview logo](https://github.com/alibaba/open-code-review/raw/main/imgs/logo.svg)](https://alibaba.github.io/open-code-review/)

The open source AI code review agent.

[![npm](https://camo.githubusercontent.com/e4b8794715fd95b551a5f9151bb4cafdc660ff143c3375aadbae3698a50ed82e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f40616c69626162612d67726f75702f6f70656e2d636f64652d7265766965773f7374796c653d666c61742d737175617265)](https://www.npmjs.com/package/@alibaba-group/open-code-review)
[![Build status](https://camo.githubusercontent.com/aaac266761424237a7f8ac6c51a51a453169fc8881d26a2ca027259d3bed5bea/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f616c69626162612f6f70656e2d636f64652d7265766965772f72656c656173652e796d6c3f7374796c653d666c61742d737175617265)](https://github.com/alibaba/open-code-review/actions/workflows/release.yml)
[![Go Report Card](https://camo.githubusercontent.com/6fca799dde1e7e5c3d710bbee2cb7ca77f6347a51e0758b933db21a8c7eebd38/68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f616c69626162612f6f70656e2d636f64652d7265766965773f7374796c653d666c61742d737175617265)](https://goreportcard.com/report/github.com/alibaba/open-code-review)
[![License](https://camo.githubusercontent.com/81a302e376f278236fe580b923ee7e69db270e5ed4b65b78c325efbb9158be05/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f616c69626162612f6f70656e2d636f64652d7265766965773f7374796c653d666c61742d737175617265)](https://github.com/alibaba/open-code-review/blob/main/LICENSE)

English | [简体中文](https://github.com/alibaba/open-code-review/blob/main/README.zh-CN.md) | [日本語](https://github.com/alibaba/open-code-review/blob/main/README.ja-JP.md) | [한국어](https://github.com/alibaba/open-code-review/blob/main/README.ko-KR.md) | [Русский](https://github.com/alibaba/open-code-review/blob/main/README.ru-RU.md)

---

What is Open Code Review?
-------------------------

Open Code Review is an AI-powered code review CLI tool. It originated as Alibaba Group's internal official AI code review assistant — over the past two years, it has served tens of thousands of developers and identified millions of code defects. After thorough validation at massive scale, we incubated it into an open source project for the community. Simply configure a model endpoint to get started.

It reads Git diffs, sends changed files to a configurable LLM via an agent with tool-use capabilities, and generates structured review comments with line-level precision. The agent can read full file contents, search the codebase, inspect other changed files for context, and produce deep reviews — not just surface-level diff feedback.

[![Highlights](https://github.com/alibaba/open-code-review/raw/main/imgs/highlights-en.png)](https://github.com/alibaba/open-code-review/blob/main/imgs/highlights-en.png)

### The Problem with General-Purpose Agents

If you've used general-purpose agents like Claude Code with Skills for code review, you've likely encountered these pain points:

* **Incomplete coverage** — On larger changesets, agents tend to "cut corners," selectively reviewing only some files and missing others.
* **Position drift** — Reported issues frequently don't match the actual code location, with line numbers or file references drifting off target.
* **Unstable quality** — Natural-language-driven Skills are hard to debug, and review quality fluctuates significantly with minor prompt variations.

The root cause: a purely language-driven architecture lacks hard constraints on the review process.

### Core Design: Deterministic Engineering × Agent Hybrid

Open Code Review's core philosophy is to combine deterministic engineering with an agent, each handling what it does best.

**Deterministic Engineering — Hard Constraints**

For review steps that *must not go wrong*, engineering logic — not the language model — guarantees correctness:

* **Precise file selection** — Determines exactly which files need review and which should be filtered, ensuring no important change is missed.
* **Smart file bundling** — Groups related files into a single review unit (e.g., `message_en.properties` and `message_zh.properties` are bundled together). Each bundle runs as a sub-agent with isolated context — a divide-and-conquer strategy that stays stable on very large changesets and naturally supports concurrent review.
* **Fine-grained rule matching** — Matches review rules to each file's characteristics, keeping the model's attention sharply focused and eliminating information noise at the source. Compared to purely language-driven rule guidance, template-engine-based rule matching is more stable and predictable.
* **External positioning and reflection modules** — Independent comment-positioning and comment-reflection modules systematically improve both the location accuracy and content accuracy of AI feedback.

**Agent — Dynamic Decision-Making**

The agent's strengths are concentrated where they matter most — dynamic decisions and dynamic context retrieval:

* **Scenario-tuned prompts** — Prompt templates deeply optimized for code review, improving effectiveness while reducing token consumption.
* **Scenario-tuned toolset** — Distilled from deep analysis of tool-call traces in large-scale production data — including call frequency distributions, per-tool repetition rates, and the impact of new tools on the overall call chain — resulting in a purpose-built toolset that is more stable and predictable for code review than a generic agent toolkit.

**Via NPM (Recommended)**

```
npm install -g @alibaba-group/open-code-review
```

After installation, the `ocr` command is available globally.

**From GitHub Release**

Download the latest binary from [GitHub Releases](https://github.com/alibaba/open-code-review/releases):

```
# macOS (Apple Silicon)
curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-darwin-arm64
chmod +x ocr && sudo mv ocr /usr/local/bin/ocr

# macOS (Intel)
curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-darwin-amd64
chmod +x ocr && sudo mv ocr /usr/local/bin/ocr

# Linux (x86_64)
curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-linux-amd64
chmod +x ocr && sudo mv ocr /usr/local/bin/ocr

# Linux (ARM64)
curl -Lo ocr https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-linux-arm64
chmod +x ocr && sudo mv ocr /usr/local/bin/ocr

# Windows (x86_64) — move ocr.exe to a directory in your PATH
curl -Lo ocr.exe https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-windows-amd64.exe

# Windows (ARM64) — move ocr.exe to a directory in your PATH
curl -Lo ocr.exe https://github.com/alibaba/open-code-review/releases/latest/download/opencodereview-windows-arm64.exe
```

**From Source**

```
git clone https://github.com/alibaba/open-code-review.git
cd open-code-review
make build
sudo cp dist/opencodereview /usr/local/bin/ocr
```

**1. Configure LLM**

**You must configure an LLM before reviewing code.**

**Option A: Interactive setup (Recommended)**

```
ocr config provider          # Select a built-in provider or add a custom one
ocr config model             # Pick a model for the active provider
```

[![Provider setup](https://github.com/alibaba/open-code-review/raw/main/imgs/providers.jpg)](https://github.com/alibaba/open-code-review/blob/main/imgs/providers.jpg)

**Option B: Manual config**

```
ocr config set llm.url https://api.anthropic.com/v1/messages
ocr config set llm.auth_token your-api-key-here
ocr config set llm.model claude-opus-4-6
ocr config set llm.use_anthropic true
```

Config is stored in `~/.opencodereview/config.json`.

**`auth_header` (optional):** Controls which HTTP header carries the API key when using Anthropic. Defaults to `authorization` (Bearer token) if omitted. If you use a standard `sk-ant-*` API key, you must set it to `x-api-key`:

```
ocr config set llm.auth_header x-api-key
```

Supported values: `x-api-key`, `authorization` (alias: `bearer`). Other values are rejected with an error.

**Option C: Environment variables (highest priority)**

```
export OCR_LLM_URL=https://api.anthropic.com/v1/messages
export OCR_LLM_TOKEN=your-api-key-here
export OCR_LLM_MODEL=claude-opus-4-6
export OCR_USE_ANTHROPIC=true
```

It is also compatible with Claude Code environment variables (`ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_MODEL`) and parses `~/.zshrc` / `~/.bashrc` for those exports.

> **Note for CC-Switch Users**: If you are using [CC-Switch](https://github.com/farion1231/cc-switch) with [routing service](https://www.ccswitch.io/en/docs?section=proxy&item=service) enabled, you can point `llm.url` to the CC-Switch proxy address without additional configuration:
>
> * For **Claude** provider: set `llm.url` to `http://127.0.0.1:15721`
> * For **Codex** provider: set `llm.url` to `http://127.0.0.1:15721/v1`
> * Set `llm.model` according to your provider settings
> * `llm.auth_token` can be any value
> * `extra_body` settings still apply

**2. Test Connectivity**

**3. Review**

```
cd your-project

# Workspace mode — review all staged, unstaged, and untracked changes
ocr review

# Branch range — compare two refs
ocr review --from main --to feature-branch

# Single commit
ocr review --commit abc123
```

### Integrate with Coding Agents

OCR can be seamlessly integrated into AI coding agents as a slash command, enabling code review directly within your agent workflow.

#### Option 1: Install as a Skill

Use `npx` to install the OCR skill into your project:

```
npx skills add alibaba/open-code-review --skill open-code-review
```

This installs the `open-code-review` skill from the [skills registry](https://github.com/alibaba/open-code-review/blob/main/skills/open-code-review/SKILL.md), which teaches your coding agent how to invoke `ocr` for code review, classify issues by priority, and optionally apply fixes.

#### Option 2: Install as a Claude Code Plugin

For [Claude Code](https://docs.anthropic.com/en/docs/claude-code), install the command plugin through the following command in Claude Code:

```
/plugin marketplace add alibaba/open-code-review
/plugin install open-code-review@open-code-review
```

This registers the `/open-code-review:review` slash command, which runs OCR and automatically filters and fixes issues.

#### Option 3: Install as a Codex Plugin

For local Codex, install the Open Code Review plugin from this repository:

```
codex plugin marketplace add alibaba/open-code-review
codex
/plugins
```

For a local checkout or fork:

```
codex plugin marketplace add .
codex
/plugins
```

Install and enable `Open Code Review`, then start a new Codex thread and invoke it explicitly:

```
@Open Code Review review my current changes
@Open Code Review review this branch against main
@Open Code Review review and fix high-confidence issues
```

This registers a Codex skill that runs the local OCR CLI:

```
ocr review --audience agent
```

This integration does not change OCR's internal LLM backend and does not require configuring an OpenAI Responses API endpoint for Codex. OCR itself still requires the `ocr` CLI to be installed and configured as described in the CLI setup section.

Korean guide: [`plugins/open-code-review/CODEX.ko-KR.md`](https://github.com/alibaba/open-code-review/blob/main/plugins/open-code-review/CODEX.ko-KR.md)

#### Option 4: Copy the Command File Directly

For a quick setup without any package manager, simply copy the command file to use the `/open-code-review` slash command in Claude Code.

**Project-level** (shared with team via git):

```
mkdir -p .claude/commands
curl -o .claude/commands/open-code-review.md \
  https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/commands/review.md
```

**User-level** (personal global use across all projects):

```
mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/open-code-review.md \
  https://raw.githubusercontent.com/alibaba/open-code-review/main/plugins/open-code-review/commands/review.md
```

> **Prerequisite**: All integration methods require the `ocr` CLI to be installed and an LLM configured. See [Install](https://github.com/alibaba/open-code-review#install) and [Configure LLM](https://github.com/alibaba/open-code-review#1-configure-llm) above.

OCR can be integrated into CI/CD pipelines to automate code review on Merge Requests / Pull Requests.

The core command for CI integration:

```
ocr review \
  --from "origin/main" \
  --to "<commit_sha>" \
  --format json
```

The `--from` flag accepts a branch ref (e.g., `origin/main`) or commit SHA as the base, while `--to` accepts a commit SHA or branch ref as the head. In CI environments, using commit SHA for `--to` is recommended to correctly handle fork PRs/MRs where the source branch doesn't exist on the origin remote.

The `--format json` flag outputs machine-readable results suitable for parsing in CI scripts.

See the [`examples/`](https://github.com/alibaba/open-code-review/blob/main/examples) directory for integration examples:

| Command | Alias | Description |
| --- | --- | --- |
| `ocr review` | `ocr r` | Start a code review |
| `ocr rules check <file>` | — | Preview which review rule applies to a file path |
| `ocr config provider` | — | Interactive provider setup (built-in, custom, or manual) |
| `ocr config model` | — | Interactive model selection for the active provider |
| `ocr config set <key> <value>` | — | Set configuration values |
| `ocr llm test` | — | Test LLM connectivity |
| `ocr llm providers` | — | List built-in LLM providers |
| `ocr viewer` | `ocr v` | Launch WebUI session viewer on `localhost:5483` |
| `ocr version` | — | Show version info |



| Flag | Shorthand | Default | Description |
| --- | --- | --- | --- |
| `--repo` | — | current dir | Git repository root |
| `--from` | — | — | Source ref (e.g., `main`) |
| `--to` | — | — | Target ref (e.g., `feature-branch`) |
| `--commit` | `-c` | — | Single commit to review |
| `--preview` | `-p` | `false` | Preview which files will be reviewed without running the LLM |
| `--format` | `-f` | `text` | Output format: `text` or `json` |
| `--concurrency` | — | `8` | Max concurrent file reviews |
| `--timeout` | — | `10` | Concurrent task timeout in minutes |
| `--audience` | — | `human` | `human` (show progress) or `agent` (summary only) |
| `--background` | `-b` | — | Optional requirement/business context for the review; auto-filled from commit message when using `--commit` |
| `--model` | — | — | Select or override the LLM model for this review |
| `--rule` | — | — | Path to custom JSON review rules |
| `--max-tools` | — | built-in | Max tool call rounds per file; only takes effect when greater than template default |
| `--max-git-procs` | — | built-in | Max concurrent git subprocesses |
| `--tools` | — | — | Path to custom JSON tools config |

```
# Interactive provider and model setup
ocr config provider
ocr config model
ocr llm providers

# Preview which files will be reviewed (no LLM calls)
ocr review --preview
ocr review -c abc123 -p

# Review workspace changes with default settings
ocr review

# Review branch diff with higher concurrency
ocr review --from main --to my-feature --concurrency 4

# Review a specific commit with verbose JSON output
ocr review --commit abc123 --format json --audience agent

# Select or override model for this review
ocr review --model claude-opus-4-6
ocr review --commit abc123 --model claude-sonnet-4-6

# Provide requirement context for more targeted review
ocr review --background "Adding rate limiting to the login API"

# Use custom review rules
ocr review --rule /path/to/my-rules.json

# Preview which rule applies to a file
ocr rules check src/main/java/com/example/Foo.java
ocr rules check --rule custom.json src/main/resources/mapper/UserMapper.xml

# View review session history in browser
ocr viewer
ocr viewer --addr :3000
```

The viewer serves session JSONL contents (LLM request messages and responses) over HTTP. It enforces a Host-header allowlist on every request: loopback names (`localhost`, `127.0.0.0/8`, `::1`) and the concrete bind host are always allowed. Wildcard binds (`--addr :3000`, `--addr 0.0.0.0:3000`) and other non-loopback Hostnames must be added via the `OCR_VIEWER_ALLOWED_HOSTS` environment variable (comma-separated):

```
OCR_VIEWER_ALLOWED_HOSTS=review.internal,ocr.lan ocr viewer --addr :3000
```

This blocks DNS-rebinding attacks against the local viewer.

OCR resolves review rules using a four-layer priority chain. Each layer uses first-match-wins: if a file path matches a pattern, that rule is used; otherwise it falls through to the next layer.

| Priority | Source | Path | Description |
| --- | --- | --- | --- |
| 1 (highest) | `--rule` flag | User-specified path | CLI explicit override |
| 2 | Project config | `<repoDir>/.opencodereview/rule.json` | Per-project rules, can be committed to git |
| 3 | Global config | `~/.opencodereview/rule.json` | User-wide personal preferences |
| 4 (lowest) | System default | Embedded `system_rules.json` | Built-in rules covering common languages and file types |

Layers 1–3 share the same JSON format:

```
{
  "rules": [
    {
      "path": "force-api/**/*.java",
      "rule": "All new methods must validate required parameters for null values"
    },
    {
      "path": "**/*mapper*.xml",
      "rule": "Check SQL for injection risks, parameter errors, and missing closing tags"
    }
  ]
}
```

* `path` supports `**` recursive matching and `{java,kt}` brace expansion.
* Within each layer, rules are evaluated in declaration order — the first match wins.
* If a rule file does not exist, it is silently skipped.

Rule files also support `include` and `exclude` fields to control which files enter the review scope:

```
{
  "rules": [
    {"path": "**/*.java", "rule": "Check for null safety"}
  ],
  "include": ["src/main/**/*.java", "lib/**/*.kt"],
  "exclude": ["**/generated/**", "vendor/**"]
}
```

**Filter decision priority (highest to lowest):**

| Step | Condition | Result |
| --- | --- | --- |
| 1 | File is binary | Excluded |
| 2 | Path matches user `exclude` pattern | Excluded |
| 3 | File extension not in supported list | Excluded |
| 4 | `include` is configured and path matches | **Reviewed** (skips step 5) |
| 5 | Path matches built-in default exclude pattern (test files, etc.) | Excluded |
| 6 | None of the above | Reviewed |

**How it works:**

* `include` and `exclude` follow the same priority chain as review rules (`--rule` > project config > global config). The **highest-priority layer that has include/exclude configured** takes effect as a whole — patterns are not merged across layers.
* `exclude` always wins over `include` — a file matching both is excluded.
* `include` acts as a **bypass for built-in default exclude patterns** (e.g., test files), not as an exclusive allowlist — files not matching any `include` pattern still proceed through the default filter checks normally.
* Pattern syntax: supports `**` recursive matching, `*` single-segment matching, and `{a,b}` brace expansion. Matching is case-insensitive.

**Built-in default exclude patterns** (filters test files, etc. — can be overridden with `include`):

```
**/*_test.go, **/*Test.java, **/*Tests.java, **/*_test.rs,
**/*.test.{js,jsx,ts,tsx}, **/*.spec.{js,jsx,ts,tsx}, **/__tests__/**,
**/src/test/java/**/*.java, **/src/test/**/*.kt,
**/test/**/*_test.py, **/tests/**/*_test.py, **/*_test.py,
**/*_spec.rb, **/spec/**/*_spec.rb, **/oh_modules/**
```

Config file: `~/.opencodereview/config.json`

| Key | Type | Example |
| --- | --- | --- |
| `provider` | string | `anthropic` | `openai` | `dashscope` | `deepseek` | `z-ai` |
| `providers.<name>.api_key` | string | Provider-specific API key |
| `providers.<name>.url` | string | Provider base URL override |
| `providers.<name>.protocol` | string | `anthropic` | `openai` |
| `providers.<name>.model` | string | Model name for the provider |
| `providers.<name>.models` | array | Optional provider model list for interactive selection |
| `providers.<name>.auth_header` | string | `x-api-key` | `authorization` |
| `custom_providers.<name>.*` | — | Same fields as `providers.<name>.*`, including optional `models` |
| `llm.url` | string | `https://api.openai.com/v1/chat/completions` |
| `llm.auth_token` | string | `sk-xxxxxxx` |
| `llm.auth_header` | string | Anthropic only: `x-api-key` | `authorization` |
| `llm.model` | string | `claude-opus-4-6` |
| `llm.use_anthropic` | boolean | `true` | `false` |
| `language` | string | `English` | `Chinese` (default: Chinese) |
| `telemetry.enabled` | boolean | `true` | `false` |
| `telemetry.exporter` | string | `console` | `otlp` |
| `telemetry.otlp_endpoint` | string | OTLP collector address |
| `telemetry.content_logging` | boolean | Include prompts in telemetry |

Environment variables take precedence over the config file.

| Variable | Purpose |
| --- | --- |
| `OCR_LLM_URL` | LLM API endpoint URL |
| `OCR_LLM_TOKEN` | API key / auth token |
| `OCR_LLM_AUTH_HEADER` | Anthropic auth header (`x-api-key` or `authorization`) |
| `OCR_LLM_MODEL` | Model name |
| `OCR_USE_ANTHROPIC` | `true` = Anthropic, `false` = OpenAI |

OpenTelemetry integration for observability (spans, metrics). Disabled by default.

```
ocr config set telemetry.enabled true
ocr config set telemetry.exporter otlp
ocr config set telemetry.otlp_endpoint localhost:4317
```

Set `telemetry.content_logging` to include LLM prompts and responses in exported data.

See [CONTRIBUTING.md](https://github.com/alibaba/open-code-review/blob/main/CONTRIBUTING.md) for development setup, coding guidelines, and how to submit pull requests.

[![Star History Chart](https://camo.githubusercontent.com/43321b7a2f6a055e70a296276197f1c46fc2f3ab0a578258cf51f38645599371/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d616c69626162612f6f70656e2d636f64652d72657669657726747970653d44617465)](https://star-history.com/#alibaba/open-code-review&Date)

[Apache-2.0](https://github.com/alibaba/open-code-review/blob/main/LICENSE) — Copyright 2026 Alibaba