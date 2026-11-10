---
title: "Fake building: Claude wrote 3k lines instead of import pywikibot"
url: https://fireflysentinel.github.io/posts/fake-building-claude-3000-lines/
clipped: 2026-06-17 01:04:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Fake building: Claude wrote 3k lines instead of import pywikibot](https://fireflysentinel.github.io/posts/fake-building-claude-3000-lines/)

## Digest Summary
The author used Claude Opus 4.7 to create a typo‑fixing script for Fandom wikis. Instead of installing existing libraries, Claude generated ~3,000 lines of custom Python that reimplemented the functionality of pywikibot, mwparserfromhell, and Wikipedia’s RETF ruleset. The hand‑rolled code required extensive debugging of regex‑based stripping, handling of ASCII art, and tokenization errors, yet Claude never suggested using the available libraries. After the author provided links, the codebase was reduced to 1,259 lines by making the stripper a thin wrapper over mwparserfromhell and consolidating edit runners into a shim over pywikibot; RETF rules were fetched at runtime. Claude then argued to retain a custom typo dictionary despite all entries already existing in RETF, indicating a tendency to preserve generated code. The author attributes this behavior to benchmark constraints that penalize external dependencies, leading models to treat self‑written code as load‑bearing and to exhibit sunk‑cost defenses. Similar patterns have been observed with Claude generating custom SVG instead of using charting libraries.

## Discussion Summary
The comments convey a mixed but pragmatic view of using Claude for code generation. Contributors note that the model often defaults to building from first principles, overlooking existing libraries, which leads to excessive custom code. They stress that explicit prompts, project‑level rules, or a “constitution” guiding dependency usage markedly improve outcomes, and that human oversight in architectural decisions remains essential. Skepticism about LLMs persists, yet many see the issue as stemming from insufficient prompting rather than inherent model flaws. Overall, clear guidance and deliberate constraints are regarded as key to better results.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: 404 Client Error: Not Found for url: https://fireflysentinel.github.io/posts/fake-building-claude-3000-lines/
> You can view the original article page directly [here](https://fireflysentinel.github.io/posts/fake-building-claude-3000-lines/).