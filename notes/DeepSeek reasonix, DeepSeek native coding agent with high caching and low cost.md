---
title: "DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost"
url: https://esengine.github.io/DeepSeek-Reasonix/
clipped: 2026-06-17 00:57:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost](https://esengine.github.io/DeepSeek-Reasonix/)

## Digest Summary
Reasonix is a DeepSeek-native AI coding agent designed for use directly within a terminal environment, enabling developers to leverage AI-powered code assistance and generation without leaving the command line.

## Discussion Summary
Comments show mixed reactions to the DeepSeek coding agent. Users acknowledge the strong cache‑hit efficiency and potential cost savings, but many question the necessity of a dedicated harness given existing tools like OpenCode, Claude Code, and Pi. Recurrent criticisms target the site’s UI—animated typing, layout issues, dark‑theme defaults—and the API documentation’s clarity. Several participants call for benchmark data, better handling of context invalidation, and clearer differentiation from other agents, while others remain cautiously interested in trying the tool.

---

## Full Article

Features特性

Built for long, cheap sessions.为长会话、低成本而生。
------------------------------------------

Most agents pay full price for the same growing prompt every turn. Reasonix keeps the prefix byte-identical so DeepSeek's cache does the heavy lifting — and everything else follows.多数 agent 每回合都为同一段不断增长的 prompt 付全价。Reasonix 让前缀逐字节稳定,让 DeepSeek 的缓存替你扛下来——其余一切由此而来。

01 / cache-first

### Cache-first loop缓存优先循环

Append-only history aligned to DeepSeek's prefix cache. 90%+ hit on long sessions; input tokens bill at ~1/5.append-only 历史对齐 DeepSeek prefix-cache。长会话 90%+ 命中,输入 token 约 1/5 计费。

02 / single binary

### Single Go binary单个 Go 二进制

CGO-free, cross-compiled for darwin/linux/windows × amd64/arm64. No Node runtime to install or babysit.无 CGO,交叉编译覆盖 darwin/linux/windows × amd64/arm64。运行不需要 Node。

03 / mcp

### MCP first-class

stdio, SSE, streamable HTTP. External servers merge their tools into one registry under a prefix.stdio、SSE、streamable HTTP。外部服务器的工具以前缀合并进同一 registry。

04 / plan + sandbox

### Plan mode & sandbox计划模式 + 沙箱

Writers are jailed to the workspace; `/plan` gates the session read-only until you approve.写工具被关进工作区;`/plan` 进只读门,批准前不写盘。

`$ /plan → read-only until approved`

05 / subagents

### Subagents & skills子智能体与技能

explore / research / review / security-review agents, plus Markdown skill scripts with isolated tools.explore / research / review / security-review 子智能体,加 Markdown 技能脚本与隔离工具。

06 / terminal

### Terminal-native终端原生

Not another IDE plugin. `git diff` handles diffs, `ls` handles trees — the terminal is the workspace.不是又一个 IDE 插件。diff 交给 `git diff`,树交给 `ls` —— 终端就是工作面板。

`$ ssh build-box → reasonix`