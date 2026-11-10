---
title: "Measuring Claude 4.7's tokenizer costs"
url: https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you
clipped: 2026-06-17 01:15:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Measuring Claude 4.7's tokenizer costs](https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you)

## Digest Summary
Anthropic’s Claude Opus 4.7 tokenizes text 1.3–1.45× more than 4.6. Real‑world Claude Code samples (CLAUDE.md, prompts, logs, diffs) show a weighted increase of 1.325× (8 254 → 10 937 tokens); technical documents reach 1.47×, synthetic English/code samples 1.345×, while CJK, emoji, and symbols change minimally (≈1.0×). The rise stems from finer sub‑word splits: English chars‑per‑token drop 4.33 → 3.60, TypeScript 3.66 → 2.69, and code tokens grow 1.29–1.39× versus prose 1.20×. Because per‑token pricing is unchanged, sessions consume ~20–30 % more dollars (e.g., an 80‑turn Claude Code session rises from ~$6.65 to $7.86–$8.76) and hit rate limits sooner; cache reads also expand (average cached prefix ≈115 K tokens vs 86 K).  

A benchmark (IFEval) on 20 sampled prompts shows a modest ≈5 pp improvement in strict instruction following (exact formatting constraints) for 4.7 versus 4.6, with no clear advantage on looser tasks. The tokenizer change thus trades higher token usage for a small, measurable gain in literal compliance; its value depends on how heavily a workflow relies on precise instruction adherence.

## Discussion Summary
The discussion centers on Anthropic’s Opus 4.7 pricing and performance, with many users reporting a 20‑30 % token cost increase that they feel is not matched by a clear quality gain. Several commentors note regressions, higher token consumption, and slower response times, prompting a shift toward older or faster models such as Sonnet, Codex, or Haiku. A recurring theme is the desire for better cost‑efficiency metrics, sustainable model development, and transparent token‑per‑task benchmarks. While some accept the trade‑off for marginal improvements, overall sentiment is skeptical of the price hike and concerned about diminishing returns.

---

## Full Article

Anthropic's Claude Opus 4.7 migration guide says the new tokenizer uses "roughly 1.0 to 1.35x as many tokens" as 4.6. I measured 1.47x on technical docs. 1.45x on a real CLAUDE.md file. The top of Anthropic's range is where most Claude Code content actually sits, not the middle.

Same sticker price. Same quota. More tokens per prompt. Your Max window burns through faster. Your cached prefix costs more per turn. Your rate limit hits sooner.

So Anthropic must be trading this for something. What? And is it worth it?

I ran two experiments. The first measured the cost. The second measured what Anthropic claimed you'd get back. Here's where it nets out.

**What does it cost?**
----------------------

To measure the cost, I used `POST /v1/messages/count_tokens` — Anthropic's free, no-inference token counter. Same content, both models, one number each per model. The difference is purely the tokenizer.

**First**: seven samples of real content a Claude Code user actually sends — a CLAUDE.md file, a user prompt, a blog post, a git log, terminal output, a stack trace, a code diff.

**Second**: twelve synthetic samples spanning content types — English prose, code, structured data, CJK, emoji, math symbols — to see how the ratio varies by kind.

The core loop is three lines of Python:

copy

```
from anthropic import Anthropic
client = Anthropic()

for model in ["claude-opus-4-6", "claude-opus-4-7"]:
    r = client.messages.count_tokens(
        model=model,
        messages=[{"role": "user", "content": sample_text}],
    )
    print(f"{model}: {r.input_tokens} tokens")
```

### Real-world Claude Code content

Seven samples pulled from real files a Claude Code user actually sends:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| User prompt (typical Claude Code task) |  |  |  |  |
| Blog post excerpt (Markdown) |  |  |  |  |
|  |  |  |  |  |
| Terminal output (pytest run) |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Weighted ratio across all seven: **1.325x** (8,254 → 10,937 tokens).

### Content-type baseline (12 synthetic samples)

For comparison across well-defined content types:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Markdown with code blocks |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Tool definitions (JSON Schema) |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

English-and-code subset, weighted: 1.345x. CJK subset: 1.01x on both.

What changed in the tokenizer
-----------------------------

Three patterns in the data:

1. **CJK, emoji, and symbol content moved 1.005–1.07x.** A wholesale new vocabulary would shift these more uniformly. That didn't happen. Consistent with the non-Latin portions of the vocabulary changing less than the Latin. Token counts don't prove which specific slots were preserved.
2. **English and code moved 1.20–1.47x on natural content.** Consistent with 4.7 using shorter or fewer sub-word merges for common English and code patterns than 4.6 did.
3. **Code is hit harder than unique prose** (1.29–1.39x vs 1.20x). Code has more repeated high-frequency strings — keywords, imports, identifiers — exactly the patterns a Byte-Pair Encoding trained on code would collapse into long merges.

Chars-per-token on English dropped from 4.33 to 3.60. TypeScript dropped from 3.66 to 2.69. The vocabulary is representing the same text in smaller pieces.

That's a hypothesis, not a proof. Counting tokens doesn't tell you which specific entries in Anthropic's proprietary vocabulary changed.

#### **Free Claude Code crash course**

60-min video lesson + CLAUDE.md starter kit. Yours when you subscribe.

### Why ship a tokenizer that uses more tokens

Anthropic's migration guide: *"more literal instruction following, particularly at lower effort levels. The model will not silently generalize an instruction from one item to another."*

Smaller tokens force attention over individual words. That's a documented mechanism for tighter instruction following, character-level tasks, and tool-call precision. Partner reports (Notion, Warp, Factory) describe fewer tool errors on long runs.

The tokenizer is one plausible contributor. Weights and post-training also changed. Token counts can't separate them.

Does 4.7 actually follow instructions better?
---------------------------------------------

That's the cost, measured. Now the question: what did Anthropic trade for it?

Their pitch is "more literal instruction following." Plausible, but the token-count data doesn't prove it. I ran a direct test.

[IFEval](https://arxiv.org/abs/2311.07911) (Zhou et al., Google, 2023) is a benchmark of prompts with verifiable constraints. "Respond in exactly N words." "Include the word X twice." "No commas." "All uppercase." Each constraint has a Python grader. Binary pass/fail.

IFEval ships 541 prompts. I sampled 20 with a fixed seed, ran each through both models, and graded with IFEval's published checker.

|  |  |  |  |
| --- | --- | --- | --- |
| Strict, prompt-level (all passed) |  |  |  |
| Strict, instruction-level |  |  |  |
|  |  |  |  |
|  |  |  |  |

A small but directionally consistent improvement on strict instruction following. Loose evaluation is flat. Both models already follow the high-level instructions — the strict-mode gap comes down to 4.6 occasionally mishandling exact formatting where 4.7 doesn't.

Only one instruction type moved materially: `change_case:english_capital` (0/1 → 1/1). Everything else tied. The one prompt that actually separated the models was a four-constraint chain where 4.6 fumbled one and 4.7 got all four.

A few caveats worth naming:

* **N=20.** IFEval has 541 prompts. A 20-prompt sample is enough to see direction, not enough to be confident about size. A +5pp delta at N=20 is consistent with anything from "no real difference" to "real +10pp improvement."
* **This measures the net effect of 4.6 → 4.7.** Tokenizer, weights, and post-training all changed. I can't isolate which one drove the +5pp. The causal link between "smaller tokens" and "better instruction following" remains a hypothesis.
* **Single generation per prompt.** Multiple runs per prompt would tighten the estimate.

So: 4.7 follows strict instructions a few points better than 4.6 on this subset. Small effect, small sample. Not the "dramatic improvement" framing Anthropic's partners used in launch quotes — at least not on this benchmark.

The extra tokens bought something measurable. +5pp on strict instruction-following. Small. Real. So: is that worth 1.3–1.45x more tokens per prompt? Here's the cost, session by session.

Dollar math for one Claude Code session
---------------------------------------

Imagine a long Claude Code session — 80 turns of back-and-forth on a bug fix or refactor.

The setup (what's in your context each turn):

* **Static prefix**: 2K CLAUDE.md + 4K tool definitions = **6K tokens**, same every turn
* **Conversation history**: grows ~2K per turn (500-token user message + 1,500-token reply), reaches ~160K by turn 80
* **User input**: ~500 fresh tokens per turn
* **Output**: ~1,500 tokens per turn
* **Cache hit rate**: ~95% (typical within the 5-minute TTL)

One thing to explain upfront: the **average cached prefix across the 80 turns is ~86K tokens**, not 6K. The static 6K is tiny; the average history across all turns (0 at turn 1, 160K at turn 80, average ~80K) dominates. Since most of the cache-read cost happens in late turns where the history is huge, that ~86K average is what actually gets billed per turn.

### 4.6 session cost

Cache reads dominate input cost. Output dominates overall.

### 4.7 session cost

Every token in the prefix scales by its content ratio:

* CLAUDE.md: 1.445x → 2K becomes 2.9K
* Tool defs: 1.12x → 4K becomes 4.5K
* Conversation history (mostly English and code): 1.325x → 160K becomes 212K by turn 80, averaging ~106K across the session
* User input: 1.325x → 500 becomes ~660

Average cached prefix on 4.7: **~115K tokens** (up from 86K). Output tokens are a wildcard — roughly the same as 4.6, up to ~30% higher if Claude Code's new `xhigh` default produces more thinking tokens.

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  | 80 × 1,500–1,950 × $25/MTok |  |
|  |  |  |

### The delta

**~$6.65 → ~$7.86–$8.76. Roughly 20–30% more per session.**

The per-token price didn't change. The per-session cost did, because the same session packs more tokens.

For Max-plan users hitting rate limits instead of dollars: your 5-hour window ends sooner by roughly the same ratio on English-heavy work. A session that ran the full window on 4.6 probably doesn't on 4.7.

How this hits the prompt cache
------------------------------

Prompt caching is the architecture Claude Code runs on.

The 4.7 tokenizer change interacts with caching in three ways:

1. **First 4.7 session starts cold.** Anthropic's prompt cache is partitioned per model — switching from 4.6 to 4.7 invalidates every cached prefix, the same way switching between Opus and Sonnet does. The tokenizer change doesn't cause this, but it makes the cold-start more expensive: the prefix you're writing to the new cache is 1.3–1.45x larger than the 4.6 equivalent.
2. **Cache volume grows by the token ratio.** 1.445x more tokens in the CLAUDE.md portion means 1.445x more tokens paying cache-write once, and 1.445x more paying cache-read every turn after. The mechanism still works. There's just more of it to pay for.
3. **Same transcript, different count.** Re-run a 4.6 session on 4.7 and your logs show a different number. If you baseline billing or observability off historical token counts, expect a step-change the day you flip the model ID.

Objections
----------

### "Input is mostly cache reads. The per-token cost barely changed."

Legitimate. In a session that stays within the 5-minute TTL, 96% of input is cache reads at $0.50/MTok — already 90% off nominal. A 1.325x ratio on the cached portion is a smaller dollar impact than on fresh input.

But Max plans count all tokens toward rate limits, not dollars. And several patterns hit uncached territory: first session after a TTL expiry, every cache-bust event (CLAUDE.md edits, tool-list changes, model switches), and every compaction event that rewrites the prefix. On those turns you pay the full ratio on the cache-write. The steady-state is a bright spot. The edges got noisier.

### "Anthropic documented 1.0–1.35x as a range, not a hard ceiling."

Agreed. The real-world weighted ratio (1.325x) lands near the top of their range. Individual file types exceed it — CLAUDE.md at 1.445x, technical docs at 1.473x. That's the useful finding: the top of the documented range is where most Claude Code content sits, not the middle. Plan around the upper range, not the average.

So: tokens are 1.3–1.45x more expensive on English and code. Anthropic bought you +5pp on strict instruction following. The sticker price didn't change. The effective per-session cost did.

**Is it worth it?** That depends on what you send. You're paying ~20–30% more per session for a small but real improvement in how literally the model follows your prompt.