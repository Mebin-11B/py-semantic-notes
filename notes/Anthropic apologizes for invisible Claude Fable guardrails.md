---
title: "Anthropic apologizes for invisible Claude Fable guardrails"
url: https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail
clipped: 2026-06-17 00:49:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Anthropic apologizes for invisible Claude Fable guardrails](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail)

## Digest Summary
Anthropic announced that the hidden “invisible” guardrails applied to its new Claude Fable 5 model will be replaced with transparent safeguards. Fable, the first publicly released model in Anthropic’s Mythos series, was originally configured to silently degrade responses to “high‑risk” queries—especially those suspected of attempting model distillation—without notifying users. The company now routes such queries to its prior flagship model, Claude Opus 4.8, and will display a clear notice each time this fallback occurs. Similar fallbacks apply to other high‑risk domains (biology, chemistry, cybersecurity) unless the request is outright blocked under broader safety policies (e.g., drugs, weapons). Anthropic cited criticism from the research community that invisible safeguards hindered evaluation and third‑party work, and acknowledged that overly broad safeguards in biology made Fable nearly unusable. The shift aims to provide visibility into safety mechanisms while maintaining protection against prohibited content.

## Discussion Summary
Comments overwhelmingly express distrust toward Anthropic’s recent implementation of invisible guardrails in Claude Code, citing concerns that the system silently degrades or redirects outputs, undermines reliability, and erodes user trust. Many users view the practice as paternalistic, potentially competitive, and insufficiently transparent, calling for clearer policies, refunds, or regulation. A minority defend the safeguards as necessary for dual‑use risk mitigation, but even supporters acknowledge the need for better communication and accountability. Overall, the sentiment is largely critical, emphasizing the negative impact on confidence and perceived product value.

---

## Full Article

Anthropic has apologized for stealthily throttling its [new AI model, Claude Fable 5](https://www.theverge.com/news/946725/anthropic-releases-claude-fable-5-mythos), with hidden guardrails that undermine both researchers and rivals using it to develop competing systems. The company says it is reversing course and will be more transparent about when the restrictions kick in, even if that means Fable refuses more queries.

Fable is the first widely available model in Anthropic’s Mythos class of AI systems, a group the company has spent months warning are [too dangerous for public release](https://www.theverge.com/ai-artificial-intelligence/917644/anthropic-claude-mythos-breach-humiliation). Anthropic says it has addressed some of those risks by launching Fable with safeguards that prevent it from responding to certain “high-risk” queries. One of the areas Anthropic [said](https://www.anthropic.com/news/claude-fable-5-mythos-5) it would restrict Fable’s responses is distillation, a technique for training smaller AI models using the outputs of larger ones.

In [Fable’s system card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf) — a public document AI developers release to explain how a system works — Anthropic said it would handle queries it believed were distillation attempts by altering and degrading the model’s answers directly. Users would not be notified that they had triggered the safety measure or informed that the responses had been changed.

Anthropic [said](https://x.com/ClaudeDevs/status/2064949876463645026?s=20) it is now changing its approach to distillation: Queries will now fall back to Claude Opus 4.8, Anthropic’s [previous flagship model](https://www.theverge.com/ai-artificial-intelligence/939094/anthropic-claude-4-8-opus-honesty-effort), the company said in a post on X. Anthropic will prominently tell users too: “You will see this every time it happens.”

This is similar to how Fable handles queries in other high-risk areas. When safety features are triggered in areas like biology, chemistry, and cybersecurity, queries are routed through Opus 4.8 unless they are blocked outright under the company’s broader safety rules, such as those covering drugs, weapons, or other prohibited content. In some cases, notably biology, the safeguards have been calibrated so broadly that Fable is [practically unusable for even basic queries](https://www.theverge.com/ai-artificial-intelligence/947973/fable-wont-answer-basic-biology-questions), something Anthropic spokesperson Paruul Maheshwary acknowledged in a comment to *The Verge*.

“Visible safeguards can be probed, so they have to be robust, which takes time to get right,” Anthropic [wrote on X](https://x.com/ClaudeDevs/status/2064949876463645026?s=20). “Invisible safeguards can be targeted more narrowly, allowing us to ship quickly with very few false positives. We went with invisible safeguards for this reason—and that was the wrong tradeoff. You should have visibility into the safeguards we have in place, and why. We’re sorry for not getting the balance right.”

The change follows [intense backlash from the AI research community](https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/) over Anthropic’s decision to silently limit users suspected of trying to distill Fable into competing models — a safeguard critics warned could also affect third parties trying to evaluate the frontier model. In the system card, Anthropic said newer models’ ability to accelerate AI development justified targeting those requests, noting that “using Claude to develop competing models already violates our Terms of Service.” Anthropic has previously [accused](https://www.theverge.com/ai-artificial-intelligence/883243/anthropic-claude-deepseek-china-ai-distillation) Chinese rivals like DeepSeek of unfairly distilling its models on an “industrial” scale.