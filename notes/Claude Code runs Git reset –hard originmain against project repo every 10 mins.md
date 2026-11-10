---
title: "Claude Code runs Git reset –hard origin/main against project repo every 10 mins"
url: https://github.com/anthropics/claude-code/issues/40710
clipped: 2026-06-17 01:25:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - claude code
  - git
  - debugging
  - automation tools
  - ai safety
  - process monitoring
related:
  - "[[Issue Claude Code is unusable for complex engineering tasks with Feb updates]]"
  - "[[Git]]"
  - "[[Debugging]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A GitHub issue reporting that Claude Code silently runs a periodic hard git reset on project repositories is resolved when the author discovers their own local script was the root cause.
>
> **Key points:**
> - The initial issue reported that Claude Code was performing programmatic `git fetch` and `git reset --hard` every 10 minutes, destroying uncommitted changes.
> - The author provided detailed logs, including 95+ reflog entries, fswatch logs, and lsof output to support the hypothesis.
> - Subsequent updates revealed that this was a false report; the resets were caused by a separate, locally run tool using GitPython.
> - The discussion highlights user concern about AI safety, deterministic guardrails, and reflog recovery options.
>
> **Concept links:** [[Claude Code]], [[Git]], [[Debugging]], [[Automation Tools]], [[Ai Safety]], [[Process Monitoring]]
>
> **Suggested connections:**
> - [[Issue Claude Code is unusable for complex engineering tasks with Feb updates]] — related concept or discussion in this area.
> - [[Git]] — the version control system and repository management techniques.
> - [[Debugging]] — the systematic process of ruling out external causes and identifying root causes of software issues.
<!-- ai-summary:end -->
# [Claude Code runs Git reset –hard origin/main against project repo every 10 mins](https://github.com/anthropics/claude-code/issues/40710)

## Digest Summary
Claude Code (v2.1.87, Homebrew Bun binary on macOS 15.4) automatically runs `git fetch origin` followed by `git reset --hard origin/main` in the user’s project directory every 600 seconds. The reset occurs silently, discarding all uncommitted changes to tracked files while leaving untracked files untouched; Git worktrees are not affected. Evidence includes >95 reflog entries exactly at 10‑minute intervals across multiple sessions, live reproduction where a modified tracked file reverts at the next interval, fswatch logs showing lock file creation typical of a fetch‑reset sequence, and lsof confirming only the Claude Code CLI process (PID 70111) has the repository as its CWD. No external `git` binary is invoked, implying the operation is performed programmatically (likely via libgit2) within the Claude Code process. The timer appears tied to session start time, with offsets such as :08, :36, :41, :09. Workarounds are to use Git worktrees or commit changes frequently. The issue seeks clarification from the Claude Code team on the internal mechanism that triggers these periodic resets.

## Discussion Summary
The comments convey mixed reactions to reports of Claude‑generated git commands resetting repositories. Several contributors view the incident as likely isolated or user‑error, emphasizing insufficient monitoring and suggesting wrappers, remote‑reject policies, or reflog recovery as mitigations. Others stress the probabilistic nature of language models, arguing that deterministic guardrails are needed to prevent destructive actions, while a few treat the situation humorously or as an expected feature of AI‑assisted development. Overall, the discussion balances technical critiques, safety concerns, and skepticism about the issue’s prevalence.

---

## Full Article

> **Update (2026-03-30): Root cause identified — this was NOT a Claude Code bug.**  
> The resets were caused by a separate tool I built that was running locally, which used GitPython to hard-reset the working directory on a poll cycle. The evidence was misleading because the tool shared the same CWD and monitored projects CC was working on. See [my comment below](https://github.com/anthropics/claude-code/issues/40710#issuecomment-4153044661) for full details. Apologies for the false report.

Summary
-------

Claude Code performs `git fetch origin` + `git reset --hard origin/main` on the user's project repo every 10 minutes via programmatic git operations (no external `git` binary spawned). This silently destroys all uncommitted changes to tracked files. Untracked files survive. Git worktrees are immune.

Environment
-----------

* **Claude Code version:** 2.1.87 (Homebrew cask, compiled Bun binary)
* **OS:** macOS 15.4 (Darwin 25.3.0, arm64)
* **Shell:** zsh

Evidence
--------

### 1. Git reflog: 95+ entries at exact 10-minute intervals

```
e8ea2c9 HEAD@{2026-03-29 22:19:09 +0200}: reset: moving to origin/main
e8ea2c9 HEAD@{2026-03-29 22:09:09 +0200}: reset: moving to origin/main
e8ea2c9 HEAD@{2026-03-29 21:59:09 +0200}: reset: moving to origin/main
e8ea2c9 HEAD@{2026-03-29 21:49:09 +0200}: reset: moving to origin/main
...
8792b6c HEAD@{2026-03-29 16:55:41 +0200}: reset: moving to origin/main
8792b6c HEAD@{2026-03-29 16:45:41 +0200}: reset: moving to origin/main
...
32aa7c7 HEAD@{2026-03-28 15:47:36 +0100}: reset: moving to origin/main
32aa7c7 HEAD@{2026-03-28 15:37:36 +0100}: reset: moving to origin/main
```

The second offset is consistent within each session but varies between sessions (`:08`, `:36`, `:41`, `:09`), confirming a timer tied to session start time with a 600-second interval. 95+ entries observed across 4 sessions over ~36 hours.

### 2. Live reproduction

1. Modified `src/lib/api.ts` (tracked file) and created `.canary-test.txt` (untracked file)
2. Monitored every 15 seconds
3. At the next 10-minute mark, `api.ts` silently reverted — modification gone
4. `.canary-test.txt` (untracked) survived
5. Reproduced consistently across 4 consecutive cycles

### 3. fswatch caught the file operations

At the exact reset time, fswatch on `.git/` captured:

```
23:59:10.349 .git/refs/remotes/origin/HEAD.lock  Created IsFile Removed AttributeModified
23:59:10.352 .git/logs/HEAD                       IsFile Updated
23:59:10.354 .git/refs/heads/main.lock            Created IsFile Removed AttributeModified
```

This is the classic pattern for `git fetch origin` + `git reset --hard origin/main`.

### 4. Only the Claude Code process is a candidate

`lsof` confirms the Claude Code CLI process (PID 70111, `claude --dangerously-skip-permissions`) is the **only process** with CWD in the affected repo. Two other Claude CLI sessions are in different directories.

### 5. No external git binary spawned

Process monitoring at 0.1-second intervals found zero `git` processes around reset times. The operations are programmatic (libgit2 or similar) within the Claude Code process, confirmed by `.git/` lock file creation without any external process.

### 6. Worktrees are immune

The worktree reflog shows **zero** `reset: moving to origin` entries. The reset targets the main working tree only.

What was ruled out
------------------

A thorough investigation eliminated all external causes:

| Cause | Verdict | Detail |
| --- | --- | --- |
| Git hooks | Cleared | All `.sample` (inactive). No husky/lint-staged. |
| Claude Code user hooks | Cleared | Only peon-ping (audio). None reference git. |
| Plugin marketplace updater | **Disproven** | Deleted `~/.claude/plugins/marketplaces/` — resets continued unchanged. |
| macOS cloud sync | Cleared | No sync tool covers this directory (checked iCloud, Dropbox, Syncthing, Synology, Google Drive). |
| Cron/LaunchAgents | Cleared | No crontab. No LaunchAgent does git operations on this path. |
| Vite/SvelteKit dev server | Cleared | All file writes go to output dirs. Zero git awareness in source. |
| IDE/editors | Cleared | nvim in different repo. No format-on-save. |
| Time Machine | Cleared | Local snapshots are read-only APFS. |
| File watchers | Cleared | No fswatch/entr/watchman/guard running. |

Binary analysis (partial)
-------------------------

From the compiled binary at `/opt/homebrew/Caskroom/claude-code/2.1.87/claude`:

* **`hg1()` function** does `["fetch","origin"]` via `t_(C8(), _)` **without explicit CWD**, defaulting to `process.cwd()`
* **`io1()` function** is a git pull wrapper logging `git pull: cwd=${H} ref=${_??"default"}`
* **`fileHistory` state** tracks `{snapshots: [], trackedFiles: new Set, snapshotSequence: 0}`
* The exact timer/setInterval setup could not be identified in minified code

Impact
------

Any uncommitted changes to tracked files in the main working tree are silently destroyed every 10 minutes. During a 2-hour session, changes had to be re-applied 3+ times before the cause was identified. The bug is invisible when all changes are committed (the reset is a no-op), making it appear intermittent.

Question for the Claude Code team
---------------------------------

**What internal mechanism runs `git fetch origin` + `git reset --hard` against `process.cwd()` every 600 seconds?** This could not be determined from the outside due to the compiled binary and lack of sudo for process tracing.

Workarounds
-----------

1. **Use git worktrees** — confirmed immune (zero reset entries in worktree reflog)
2. **Commit frequently** — committed changes survive the reset

Related issues
--------------