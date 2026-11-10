---
title: Snowboard Kids 2 is 100% Decompiled
url: https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/
clipped: 2026-06-17 00:55:31
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - game decompilation
  - reverse engineering
  - nintendo 64
  - ai coding agents
related:
  - "[[Game Decompilation]]"
  - "[[Reverse Engineering]]"
  - "[[Nintendo 64]]"
  - "[[AI Coding Agents]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The Nintendo 64 game Snowboard Kids 2 reaches 100% decompilation, matching all MIPS assembly functions to equivalent, recompilable C code.
>
> **Key points:**
> - Every original MIPS function has been matched to C code that compiles to the exact same machine code.
> - The decompilation took under two years, aided by N64 decompilation Discord members and LLM coding assistants.
> - Coding agents like Codex 5.5 xhigh and Claude were crucial in matching the final ten complex functions.
> - Enables native ports, asset extraction, and gameplay mods, with future plans for recompilation and widescreen support.
>
> **Concept links:** [[Game Decompilation]], [[Reverse Engineering]], [[Nintendo 64]], [[Ai Coding Agents]]
>
> **Suggested connections:**
> - [[Game Decompilation]] — Documents the process of converting legacy ROM binaries back into matching, human-readable source code.
> - [[AI Coding Agents]] — Explores the use of LLMs to assist in matching complex compiler-generated assembly structures.
<!-- ai-summary:end -->

# [Snowboard Kids 2 is 100% Decompiled](https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/)

## Digest Summary
Snowboard Kids 2 has reached 100 % decompilation: every original N64 MIPS function now has a matching C implementation that assembles to the same machine code. The effort spanned under two years, beginning with the first commit in September 2024, and concluded while the author was hospitalized with a newborn. Community support from the N64 decompilation Discord (notably Bl00D4NGEL, inspectredc, SlaveOfIDO, queueRAM) was essential, and coding agents—Claude, GLM, and Codex—accelerated the final ten functions, with Codex 5.5 xhigh proving most effective for the hardest cases. The next phase is a high‑quality recompilation, already functional but still containing bugs, widescreen adjustments, and extended draw distance artifacts. Remaining decompilation tasks include renaming functions, cleaning up structures, and extracting graphics/audio assets. The author also contemplates a Snowboard Kids 1 decompilation to enable a combined “Super Snowboard Kids” version on the newer engine. Further information and contribution tasks are listed in the project README.

## Discussion Summary
The comments convey strong nostalgia for the game and praise the recent decompilation as valuable for preservation, potential ports, and learning low‑level hardware constraints. Many commend the developers’ effort and note the educational benefits, while a minority question the scale of work, labeling it a meme. Interest in how AI and large language models may accelerate decompilation appears, and there is enthusiasm for applying similar projects to other titles, accompanied by modest debate over the game’s status among N64 classics.

---

## Full Article

I’m very pleased to announce that *Snowboard Kids 2* is 100% decompiled!

All of the game’s functions have now been implemented in C and compile to assembly that matches the original game. There’s still some occasional `__asm__` hackery, and plenty of code needs better names and documentation, but every function now has a matching C implementation.

That matters because a matching decompilation turns the game from a pile of MIPS assembly into a codebase we can read, build, study, and modify. It should help with recompilation, asset extraction, modding, and generally understanding the mechanics of the N64’s greatest game.

[![screenshot of the decomp.dev Snowboard Kids 2 decompilation report](https://blog.chrislewis.au/snowboardkids2-decomp-report.svg)

Snowboard Kids 2 decompilation report from decomp.dev. Boxes represent different files.](https://decomp.dev/cdlewis/snowboardkids2-decomp)

The journey
-----------

This project has been a little under two years in the making, with the [first commit](https://github.com/cdlewis/snowboardkids2-decomp/commit/f1025d16a8aa1d11ec937f8c721af59149feee7c) landing in September 2024.

The circumstances surrounding the final matches were not quite what I expected when I started. I’m currently sitting in hospital with my newborn daughter. She’s doing fine, but needs some help eating. Decompilation has been a useful distraction and an enjoyable way to fill the quiet hours.

![photo of me in the hospital with my daughter](https://blog.chrislewis.au/hospital.webp)

The path to decompiling any game, let alone a Nintendo 64 game, is not especially well documented. This project would not have been possible without the N64 decompilation Discord community, whose members have been incredibly generous with their time. I would particularly like to thank [Bl00D4NGEL](https://github.com/Bl00D4NGEL), [inspectredc](https://github.com/inspectredc), [SlaveOfIDO](https://github.com/SlaveOfIDO), and [queueRAM](https://github.com/queueRAM) for their significant contributions to the project, especially across the final ten functions.

![screenshot of the decomp.dev Snowboard Kids 2 leaderboard](https://blog.chrislewis.au/leaderboard.webp)

Leaderboard shared on discord for tracking work on the remaining Snowboard Kids 2 functions.

The community was more important than any model: people answered my dumb questions, explained tooling, and decompiled functions themselves. With that said, coding agents also greatly accelerated the decompilation effort, particularly Claude, GLM, and Codex. I don’t want to turn this into another AI blog post, but I do have a couple of observations:

1. Based on my experience with the final ten functions, which were among the most difficult, the most effective model appeared to be Codex 5.5 xhigh. Historically Claude was more effective, and I expect this to keep changing, perhaps even by the time you read this.
2. Frontier models are now very effective at decompilation, but this comes at a cost. GLM has probably been the best value for money for this specific kind of work. If you want to try coding agents on your own decompilation project but are put off by high subscription fees, that is where I would start.

What next?
----------

Reaching 100% decompilation was not technically blocking the recompilation effort, but it was more interesting to me personally. With the decompilation finished, my next goal is to release a high-quality recompilation of *Snowboard Kids 2*.

That’s already in a pretty good state thanks to help from [sonicdcer](https://github.com/sonicdcer) and [DarioSamo](https://github.com/DarioSamo), but there are still bugs to squash before I’m comfortable releasing it.

![screenshot of an alpha version of Snowboard Kids 2: Recompiled](https://blog.chrislewis.au/sbk2-recompiled-screenshot.webp)

Screenshot from Snowboard Kids 2: Recompiled. Note the use of widescreen and expanded draw distance. This can lead to some visual quirks.

There’s also plenty of work left to do in the decompilation project itself. A 100% match doesn’t mean the source is perfectly understood. Many functions still have generated names, many structures need to be cleaned up, and graphics/audio assets are still mostly treated as binary blobs. The project is now in a much better place for that work, but the work still needs doing.

Finally, I’m interested in starting a *Snowboard Kids* 1 decompilation. I think it would be very cool to have a ‘Super Snowboard Kids’ that combines both games and allows you to play all the original tracks on the second game’s more modern engine. I have no idea how feasible that ultimately is, but it’s a fun thing to think about.

If you’ve made it this far, you probably have an interest in decompilation and *Snowboard Kids 2*. Take a look at the [Snowboard Kids 2 decompilation project](https://github.com/cdlewis/snowboardkids2-decomp). The README includes a list of good first tasks.

**You can also [follow me on Bluesky](https://bsky.app/profile/chrislewis.au) for more Snowboard Kids 2 updates.**
