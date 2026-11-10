---
title: "Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation"
url: https://github.com/gavrielc/nanoclaw
clipped: 2026-06-17 01:49:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation](https://github.com/gavrielc/nanoclaw)

## Digest Summary
The GitHub repository gavrielc/nanoclaw offers a personal Claude‑based AI assistant designed to run inside Apple‑specific containers. It emphasizes lightweight operation, security, and ease of understanding and customization for individual needs. The page currently shows a “You can’t perform that action at this time” notice, indicating limited or restricted access to the content. An accompanying image (alt text “NanoClaw”) likely depicts the assistant’s branding or interface. No additional technical details, usage instructions, or code excerpts are provided in the scraped excerpt.

## Discussion Summary
The comments express strong caution about the project’s security implications, emphasizing fear that granting an AI extensive permissions could enable malicious actions and that current safeguards appear insufficient. Many criticize AI‑generated documentation as off‑putting and call for clearer, human‑written readmes and explicit disclaimers. Positive notes mention the novelty of using Apple containers for minimal footprint and appreciation for the concept’s potential, yet overall sentiment remains wary, urging tighter sandboxing, better transparency, and careful risk assessment before adoption.

---

## Full Article

[![NanoClaw](https://github.com/nanocoai/nanoclaw/raw/main/assets/nanoclaw-logo.png)](https://github.com/nanocoai/nanoclaw/blob/main/assets/nanoclaw-logo.png)

An AI assistant that runs agents securely in their own containers. Lightweight, built to be easily understood and completely customized for your needs.

[nanoclaw.dev](https://nanoclaw.dev)  •  
[docs](https://docs.nanoclaw.dev)  •  
[中文](https://github.com/nanocoai/nanoclaw/blob/main/README_zh.md)  •  
[日本語](https://github.com/nanocoai/nanoclaw/blob/main/README_ja.md)  •  
[![Discord](https://camo.githubusercontent.com/5d54ab97b11df53ffd11d91db846c9ef70b03d0120c6226b373dca61d5ee7417/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313437303138383231343731303034363839343f6c6162656c3d446973636f7264266c6f676f3d646973636f726426763d32)](https://discord.gg/VDdww8qS42)  •  
[![repo tokens](https://github.com/nanocoai/nanoclaw/raw/main/repo-tokens/badge.svg)](https://github.com/nanocoai/nanoclaw/blob/main/repo-tokens)

---

[OpenClaw](https://github.com/openclaw/openclaw) is an impressive project, but I wouldn't have been able to sleep if I had given complex software I didn't understand full access to my life. OpenClaw has nearly half a million lines of code, 53 config files, and 70+ dependencies. Its security is at the application level (allowlists, pairing codes) rather than true OS-level isolation. Everything runs in one Node process with shared memory.

NanoClaw provides that same core functionality, but in a codebase small enough to understand: one process and a handful of files. Claude agents run in their own Linux containers with filesystem isolation, not merely behind permission checks.

```
git clone https://github.com/nanocoai/nanoclaw.git nanoclaw-v2
cd nanoclaw-v2
bash nanoclaw.sh
```

`nanoclaw.sh` walks you from a fresh machine to a named agent you can message. It installs Node, pnpm, and Docker if missing, registers your Anthropic credential with OneCLI, builds the agent container, and pairs your first channel (Telegram, Discord, WhatsApp, or a local CLI). If a step fails, Claude Code is invoked automatically to diagnose and resume from where it broke.

**Migrating from NanoClaw v1?**

Run from a fresh v2 checkout next to your v1 install:

```
git clone https://github.com/nanocoai/nanoclaw.git nanoclaw-v2
cd nanoclaw-v2
bash migrate-v2.sh
```

`migrate-v2.sh` finds your v1 install (sibling directory, or `NANOCLAW_V1_PATH=/path/to/nanoclaw`), migrates state into the v2 checkout, then `exec`s into Claude Code to finish the parts that need judgment (owner seeding, CLAUDE.local.md cleanup, fork-customisation replay).

Run the script directly, not from inside a Claude session — the deterministic side needs interactive prompts and real shell I/O for Node/pnpm bootstrap, Docker, OneCLI, and the container build.

**What it does:** merges `.env`, seeds the v2 DB from `registered_groups`, copies group folders + session data + scheduled tasks, installs the channel adapters you select, copies channel auth state (including Baileys keystore + LID mappings for WhatsApp), builds the agent container.

**What it doesn't:** flip the system service. Pick *"switch to v2"* at the prompt, or do it manually after testing — your v1 install is left untouched.

See [docs/v1-to-v2-changes.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/v1-to-v2-changes.md) for what's different and [docs/migration-dev.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/migration-dev.md) for development notes.

**Small enough to understand.** One process, a few source files and no microservices. If you want to understand the full NanoClaw codebase, just ask Claude Code to walk you through it.

**Secure by isolation.** Agents run in Linux containers and they can only see what's explicitly mounted. Bash access is safe because commands run inside the container, not on your host.

**Built for the individual user.** NanoClaw isn't a monolithic framework; it's software that fits each user's exact needs. Instead of becoming bloatware, NanoClaw is designed to be bespoke. You make your own fork and have Claude Code modify it to match your needs.

**Customization = code changes.** No configuration sprawl. Want different behavior? Modify the code. The codebase is small enough that it's safe to make changes.

**AI-native, hybrid by design.** The install and onboarding flow is an optimized scripted path, fast and deterministic. When a step needs judgment, whether a failed install, a guided decision, or a customization, control hands off to Claude Code seamlessly. Beyond setup there's no monitoring dashboard or debugging UI either: describe the problem in chat and Claude Code handles it.

**Skills over features.** Trunk ships the registry and infrastructure, not specific channel adapters or alternative agent providers. Channels (Discord, Slack, Telegram, WhatsApp, …) live on a long-lived `channels` branch; alternative providers (OpenCode, Ollama) live on `providers`. You run `/add-telegram`, `/add-opencode`, etc. and the skill copies exactly the module(s) you need into your fork. No feature you didn't ask for.

**Best harness, best model.** NanoClaw natively uses Claude Code via Anthropic's official Claude Agent SDK, so you get the latest Claude models and Claude Code's full toolset, including the ability to modify and expand your own NanoClaw fork. Other providers are drop-in options: `/add-codex` for OpenAI's Codex (ChatGPT subscription or API key), `/add-opencode` for OpenRouter, Google, DeepSeek and more via OpenCode, and `/add-ollama-provider` for local open-weight models. Provider is configurable per agent group.

* **Multi-channel messaging** — WhatsApp, Telegram, Discord, Slack, Microsoft Teams, iMessage, Matrix, Google Chat, Webex, Linear, GitHub, WeChat, and email via Resend. Installed on demand with `/add-<channel>` skills. Run one or many at the same time.
* **Flexible isolation** — connect each channel to its own agent for full privacy, share one agent across many channels for unified memory with separate conversations, or fold multiple channels into a single shared session so one conversation spans many surfaces. Pick per channel via `/manage-channels`. See [docs/isolation-model.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md).
* **Per-agent workspace** — each agent group has its own `CLAUDE.md`, its own memory, its own container, and only the mounts you allow. Nothing crosses the boundary unless you wire it to.
* **Scheduled tasks** — recurring jobs that run Claude and can message you back
* **Web access** — search and fetch content from the web
* **Container isolation** — agents are sandboxed in Docker (macOS/Linux/WSL2), with optional [Docker Sandboxes](https://github.com/nanocoai/nanoclaw/blob/main/docs/docker-sandboxes.md) micro-VM isolation or Apple Container as a macOS-native opt-in
* **Credential security** — agents never hold raw API keys. Outbound requests route through [OneCLI's Agent Vault](https://github.com/onecli/onecli), which injects credentials at request time and enforces per-agent policies and rate limits.

Talk to your assistant with the trigger word (default: `@Andy`):

```
@Andy send an overview of the sales pipeline every weekday morning at 9am (has access to my Obsidian vault folder)
@Andy review the git history for the past week each Friday and update the README if there's drift
@Andy every Monday at 8am, compile news on AI developments from Hacker News and TechCrunch and message me a briefing
```

From a channel you own or administer, you can manage groups and tasks:

```
@Andy list all scheduled tasks across groups
@Andy pause the Monday briefing task
@Andy join the Family Chat group
```

NanoClaw doesn't use configuration files. To make changes, just tell Claude Code what you want:

* "Change the trigger word to @Bob"
* "Remember in the future to make responses shorter and more direct"
* "Add a custom greeting when I say good morning"
* "Store conversation summaries weekly"

Or run `/customize` for guided changes.

The codebase is small enough that Claude can safely modify it.

**Don't add features. Add skills.**

If you want to add a new channel or agent provider, don't add it to trunk. New channel adapters land on the `channels` branch; new agent providers land on `providers`. Users install them in their own fork with `/add-<name>` skills, which copy the relevant module(s) into the standard paths, wire the registration, and pin dependencies.

This keeps trunk as pure registry and infra, and every fork stays lean — users get the channels and providers they asked for and nothing else.

Skills we'd like to see:

**Communication Channels**

* `/add-signal` — Add Signal as a channel

* macOS or Linux (Windows via WSL2)
* Node.js 20+ and pnpm 10+ (the installer will install both if missing)
* [Docker Desktop](https://docker.com/products/docker-desktop) (macOS/Windows) or Docker Engine (Linux)
* [Claude Code](https://claude.ai/download) for `/customize`, `/debug`, error recovery during setup, and all `/add-<channel>` skills

```
messaging apps → host process (router) → inbound.db → container (Bun, Claude Agent SDK) → outbound.db → host process (delivery) → messaging apps
```

A single Node host orchestrates per-session agent containers. When a message arrives, the host routes it via the entity model (user → messaging group → agent group → session), writes it to the session's `inbound.db`, and wakes the container. The agent-runner inside the container polls `inbound.db`, runs Claude, and writes responses to `outbound.db`. The host polls `outbound.db` and delivers back through the channel adapter.

Two SQLite files per session, each with exactly one writer — no cross-mount contention, no IPC, no stdin piping. Channels and alternative providers self-register at startup; trunk ships the registry and the Chat SDK bridge, while the adapters themselves are skill-installed per fork.

For the full architecture writeup see [docs/architecture.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/architecture.md); for the three-level isolation model see [docs/isolation-model.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md).

Key files:

* `src/index.ts` — entry point: DB init, channel adapters, delivery polls, sweep
* `src/router.ts` — inbound routing: messaging group → agent group → session → `inbound.db`
* `src/delivery.ts` — polls `outbound.db`, delivers via adapter, handles system actions
* `src/host-sweep.ts` — 60s sweep: stale detection, due-message wake, recurrence
* `src/session-manager.ts` — resolves sessions, opens `inbound.db` / `outbound.db`
* `src/container-runner.ts` — spawns per-agent-group containers, OneCLI credential injection
* `src/db/` — central DB (users, roles, agent groups, messaging groups, wiring, migrations)
* `src/channels/` — channel adapter infra (adapters installed via `/add-<channel>` skills)
* `src/providers/` — host-side provider config (`claude` baked in; others via skills)
* `container/agent-runner/` — Bun agent-runner: poll loop, MCP tools, provider abstraction
* `groups/<folder>/` — per-agent-group filesystem (`CLAUDE.md`, skills, container config)

**Why Docker?**

Docker provides cross-platform support (macOS, Linux and Windows via WSL2) and a mature ecosystem. On macOS, Apple Container is also supported as a lighter-weight native runtime. For additional isolation, [Docker Sandboxes](https://github.com/nanocoai/nanoclaw/blob/main/docs/docker-sandboxes.md) run each container inside a micro VM.

**Can I run this on Linux or Windows?**

Yes. Docker is the default runtime and works on macOS, Linux, and Windows (via WSL2). Just run `bash nanoclaw.sh`.

**Is this secure?**

Agents run in containers, not behind application-level permission checks. They can only access explicitly mounted directories. Credentials never enter the container — outbound API requests route through [OneCLI's Agent Vault](https://github.com/onecli/onecli), which injects authentication at the proxy level and supports rate limits and access policies. You should still review what you're running, but the codebase is small enough that you actually can. See the [security documentation](https://docs.nanoclaw.dev/concepts/security) for the full security model.

**Why no configuration files?**

We don't want configuration sprawl. Every user should customize NanoClaw so that the code does exactly what they want, rather than configuring a generic system. If you prefer having config files, you can tell Claude to add them.

**Can I use third-party or open-source models?**

Yes. The supported path is `/add-opencode` (OpenRouter, OpenAI, Google, DeepSeek, and more via OpenCode config) or `/add-ollama-provider` (local open-weight models via Ollama). Both are configurable per agent group, so different agents can run on different backends in the same install.

For one-off experiments, any Claude API-compatible endpoint also works via `.env`:

```
ANTHROPIC_BASE_URL=https://your-api-endpoint.com
ANTHROPIC_AUTH_TOKEN=your-token-here
```

**How do I debug issues?**

Ask Claude Code. "Why isn't the scheduler running?" "What's in the recent logs?" "Why did this message not get a response?" That's the AI-native approach that underlies NanoClaw.

**Why isn't the setup working for me?**

If a step fails, `nanoclaw.sh` hands off to Claude Code to diagnose and resume. If that doesn't resolve it, run `claude`, then `/debug`. If Claude identifies an issue likely to affect other users, open a PR against the relevant setup step or skill.

**How do I uninstall NanoClaw?**

```
bash nanoclaw.sh --uninstall
```

Every install is tagged with a per-checkout id, so the uninstaller removes only what belongs to that copy: the background service, containers and image, app data and logs, your agents' files, and this copy's OneCLI vault agents. Shared things — the OneCLI app and your credentials, other NanoClaw copies on the machine — are left alone. It shows exactly what it found and asks for confirmation per group; nothing is deleted until you say yes. Use `--dry-run` to preview without changing anything, or `--yes` to skip the prompts. Your `.env` is backed up before removal. To finish, delete the checkout folder itself.

**What changes will be accepted into the codebase?**

Only security fixes, bug fixes, and clear improvements will be accepted to the base configuration. That's all.

Everything else (new capabilities, OS compatibility, hardware support, enhancements) should be contributed as skills: channel and provider code on the `channels`/`providers` registry branches, everything else as a self-contained skill. See [docs/customizing.md](https://github.com/nanocoai/nanoclaw/blob/main/docs/customizing.md) and [CONTRIBUTING.md](https://github.com/nanocoai/nanoclaw/blob/main/CONTRIBUTING.md).

This keeps the base system minimal and lets every user customize their installation without inheriting features they don't want.

Community
---------

Questions? Ideas? [Join the Discord](https://discord.gg/VDdww8qS42).

See [CHANGELOG.md](https://github.com/nanocoai/nanoclaw/blob/main/CHANGELOG.md) for breaking changes, or the [full release history](https://docs.nanoclaw.dev/changelog) on the documentation site.

MIT

[![](https://camo.githubusercontent.com/44c0ed0941cad1f5b7bf1dbb12471debc9ad26b55c929cc666949b357b58fdb8/68747470733a2f2f7374617469632e73636172662e73682f612e706e673f782d707869643d34373839346264352d333533622d343266652d626239372d373431343465366466306266)](https://camo.githubusercontent.com/44c0ed0941cad1f5b7bf1dbb12471debc9ad26b55c929cc666949b357b58fdb8/68747470733a2f2f7374617469632e73636172662e73682f612e706e673f782d707869643d34373839346264352d333533622d343266652d626239372d373431343465366466306266)