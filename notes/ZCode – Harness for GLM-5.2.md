---
title: "ZCode – Harness for GLM-5.2"
url: https://zcode.z.ai/en
clipped: 2026-08-31 12:22:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [ZCode – Harness for GLM-5.2](https://zcode.z.ai/en)

## Digest Summary
ZCode is an official harness for the GLM‑5.2 model designed to integrate AI agents directly with existing development tools. It emphasizes a streamlined workflow for planning, coding, reviewing, and deploying software, promoting simplicity and speed. The platform’s interface includes components such as “Ryan Bot” for interaction, a “Finder” tool for locating resources, support for long‑running tasks, and a bot‑control panel. Deep integration with GLM‑5.2 enables advanced language model capabilities throughout the development cycle.

---

## Full Article

[🎉Official Harness for GLM-5.3, taking multi-agent development further](https://zcode.z.ai/en/changelog)

# Simple, Fast, Vibe‑Ready !

ZCode is next-gen vibe coding for complex goals—with multiple agents and control from anywhere.

[Download ZCodeDownload .dmg(Apple Silicon)](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/macos-arm64/ZCode-3.10.1-mac-arm64.dmg)[View all downloads](https://zcode.z.ai/en#all-downloads)New Task⌘NOpen WorkspaceSkills

### Tasks

- gomoku-ai
- 

Create an intelligent Gomoku (Five-in-a-Row) game where the player competes against a smart algorithm that can make strategic moves and accurately detect winning conditions.2m
- 

Refine start prompts, turn-state messaging, and win copy9m
- 

Wire in heuristic AI turns and the player-first game flow14m
- 

Adapt board scaling and portrait/landscape layout for mobile27m
- 

Add rules copy, restart entry points, and empty-state guidance51m
- zcode-website
- 

Fix bottom pinning when the conversation view is resized8m
- 

Refresh hero visual workspace and task mock data3m
- 

Tighten homepage English copy and unify positioning with CTAs42m
- 

Tune hero breakpoints for 13-inch screens and mobile1h
- 

Add pricing FAQ content and enterprise capability notes2h
- 

Improve docs search highlighting and empty-state feedback5h
- zcode-desktop
- 

Debug the sidebar state mismatch after session recovery1h
- 

Reduce repaint cost after terminal panel resize2h
- 

Fix sidebar collapsed state not restoring after restart3h
- 

Audit settings IA to reduce advanced-option sprawl6h
- 

Add recent items and keyboard hints to the command palette9h
- 

Add remote-dev guidance and permission hints to onboarding1d
- release-bot
- 

Hook up changelog generation and draft GitHub Releases4h
- 

Draft a failed-CI summary template with retry guidance1d
- 

Connect tag validation, version sync, and release-note preview1d
- 

Write release announcement templates for patch and feature drops2d
- 

Add idempotent retries and alert dedupe for failed releases3dRyan BotCreate an intelligent Gomoku (Five-in-a-Row) game where the player competes against a smart algorithm that can make strategic moves and accurately detect winning conditions.05:10 PMEditCopyForkWorked for 3m 1s

I’m going to inspect the current Gomoku project structure first, then I’ll identify what already exists for board state, rendering, and game flow before wiring in AI and win detection.Explored1 search, 1 fileFailedRan `pwd` SearchedList in ~/ryan/gomoku-aiFailed

The repository looks either empty or nearly empty. I’m checking the actual directory contents now and confirming whether there’s an existing app to extend or whether I should build the game from scratch.Ran `git status --short` Failed$ `git status --short`  `2026-04-19 17:10:16.280 xcodebuild[60663:50240053] DVTFilePathFSEvents: Failed to start fs event stream.
git: warning: confstr() failed with code 5: couldn't get path of DARWIN_USER_TEMP_DIR; using /tmp instead
fatal: not a git repository (or any of the parent directories): .git` 

There isn’t an existing app here, so I’m building a self-contained implementation from scratch. I’m checking whether there are any local project conventions to respect, then I’ll add a browser-based Gomoku with a heuristic AI, turn handling, and explicit five-in-a-row detection.Wroteindex.html,app.js,styles.css+733Wroteindex.html+62Wroteapp.js+471Wrotestyles.css+200

The full UI and core logic are in place. I’m verifying the JavaScript parses cleanly and reviewing the move-scoring logic for edge cases like first-move response, draw handling, and long-line wins.Ran `node --check app.js` $ `node --check app.js` 

No output.

I found one avoidable dependency: the page was pulling a web font. I’m removing that so the game stays fully local and works by opening  `index.html`   with no network requirement.Updatedstyles.css,index.html+1 -7Updatedstyles.css+1-1Updatedindex.html-6

Built a standalone browser Gomoku game in index.html, styles.css, and app.js. It renders a 15x15 board, lets the player place black stones, detects wins in all four directions, highlights the winning line, tracks turns and move count, and supports restarting the match.

The AI is heuristic rather than random. It searches nearby candidate moves, scores offensive patterns for itself, scores defensive blocks against the player, adds center preference, and chooses the strongest move. There's also an optional “AI focus area” overlay so you can see the strongest candidate points it considered.

Verification:  `node --check app.js`   passed. I did not run an interactive browser session here, so the remaining step is to open index.html  in a browser and play.3 files changed+734 -7Undoapp.js+471-0index.html+62-6styles.css+201-1

Ask for follow-up changesAdd contextAsk before changesGLM-5.3MaxSendTerminalzshryan@mac zcode-website % 

Z.AI

## Code with GLM Coding Plan

GLM is tuned for ZCode, making agentic coding faster and steadier.[View plans](https://z.ai/subscribe#code-plans-container)

GLM Coding

### Lite

Built for lightweight iteration on small repo$12.6/ month$18

10,000 Credits / week
- Rolling access to the latest flagship models and features
- Supports 20+ agent tools, including ZCode, Claude Code, and more
- Default data privacy

GLM Coding

### Pro

Popular

Built for day-to-day development on mid-sized repo$56/ month$80

6× Lite usage
- All Lite benefits
- Priority access to the latest flagship models and features
- Includes a curated selection of MCP tools
- Faster generation speeds

GLM Coding

### Max

Max Usage

Built for advanced users working on mid-to-large repo$117.6/ month$168

14× Lite usage
- All Pro benefits
- First access to the latest flagship models and features
- Dedicated resources during peak times

Prices and plan benefits may change. Final details are shown on z.ai.

Capabilities

## Stay on the Frontier

From understanding legacy monoliths to shipping real-time features, ZCode keeps every engineer on the frontier of software development.

### Long-running tasks

Use Goals to manage complex work with continuous planning, execution, and verification.

### Bot control

Start and steer ZCode from WeChat, Feishu, or Telegram so work can keep moving anywhere.

### Deep GLM-5.3 integration

Optimized for GLM-5.3 across reasoning, coding, and multi-agent collaboration, with GLM-5.3-Flash built in for multimodal tasks such as screenshot understanding and image analysis.

## All Downloads

All ZCode installers for every platform

### MacOS

[macOS (Apple Silicon).dmgv3.10.1](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/macos-arm64/ZCode-3.10.1-mac-arm64.dmg)[macOS (Intel).dmgv3.10.1](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/macos-x64/ZCode-3.10.1-mac-x64.dmg)

### Windows

[Windows (64-bit).exev3.10.1](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/windows-x64/ZCode-3.10.1-win-x64.exe)[Windows (ARM64).exev3.10.1](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/windows-arm64/ZCode-3.10.1-win-arm64.exe)

### Linux

BetaLinux x64v3.10.1[.deb](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-x64/ZCode-3.10.1-linux-x64.deb)[.rpm](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-x64/ZCode-3.10.1-linux-x64.rpm)[.AppImage](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-x64/ZCode-3.10.1-linux-x64.AppImage)Linux ARM64v3.10.1[.deb](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-arm64/ZCode-3.10.1-linux-arm64.deb)[.rpm](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-arm64/ZCode-3.10.1-linux-arm64.rpm)[.AppImage](https://cdn-zcode.z.ai/zcode/electron/releases/3.10.1/linux-arm64/ZCode-3.10.1-linux-arm64.AppImage)
