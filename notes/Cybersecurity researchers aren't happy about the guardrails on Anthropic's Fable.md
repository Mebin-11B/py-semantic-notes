---
title: "Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable"
url: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/
clipped: 2026-06-17 00:49:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/)

## Digest Summary
Anthropic launched Fable, a public, limited version of its cybersecurity‑focused model Mythos, embedding guardrails that block any request deemed “cybersecurity or biology” related. When triggered, Fable pauses the conversation, flags the message, and falls back to Claude Opus 4.8. Researchers report that even benign tasks—reading a blog post, requesting a code review, or asking for secure‑coding advice—are rejected, indicating a keyword‑based filtering system. The restrictions aim to prevent misuse for malware or biological‑weapon development, mirroring earlier limits on Mythos, which was initially confined to select companies under “Project Glasswing” before expanding to hundreds of organizations across 15 countries. Critics describe the guardrails as haphazard, though some acknowledge they may evolve as Anthropic refines its approach. Anthropic’s Cyber Verification Program grants approved cybersecurity professionals fewer limitations, a model comparable to OpenAI’s Trusted Access for Cyber. Anthropic has not commented on the concerns.

## Discussion Summary
Comments express strong frustration with Anthropic’s Fable 5 guardrails, describing them as overly restrictive, opaque, and detrimental to legitimate research in cybersecurity, biology, and software development. Many users report frequent downgrades to weaker models, loss of functionality, and perceived token‑wasting, leading to calls for refunds or a boycott. A minority acknowledge the need for safety measures to prevent misuse, suggesting the trade‑off may be justified, while others compare the experience unfavorably to competing services that impose fewer restrictions. Overall, sentiment is largely negative toward the current implementation.

---

## Full Article

Anthropic [released its latest model Fable](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/) on Tuesday, billing it as a public and limited version of its powerful and much-hyped cybersecurity model Mythos.

But not everyone is happy with the restrictions, and [a number](https://x.com/Behi_Sec) of [cybersecurity](https://x.com/zeroxjf/status/2064400152178389307) [researchers](https://x.com/alexjplaskett/status/2064594731137409128) and [professionals](https://x.com/mehulmpt/status/2064449391969374238) [have aired](https://www.reddit.com/r/ClaudeCode/comments/1u1rvn3/fable_refusing_every_request_related_to/) [complaints](https://www.reddit.com/r/ClaudeAI/comments/1u1o50u/had_fable_5_run_an_indepth_cybersecurity_audit_of/) online.

“[Fable] rejects any request that could be tangentially cyber related. Even innocuous tasks like reading a blog post,” [said](https://x.com/chompie1337/status/2064431038554939507) Valentina “Chompie” Palmiotti, a well-known security researcher who works at IBM X-Force.

When a prompt triggers its guardrails, Fable pauses the chat and says that its “safety measures flagged this message for cybersecurity or biology topics.”

The guardrails were put in place to limit the risk that Fable could be used to develop malware or compromise software — [a long-standing concern](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack) within Anthropic. The restrictions on biology come from a similar concern around [developing biological weapons](https://red.anthropic.com/2025/biorisk/).

When [the AI giant released Mythos](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) in April, it restricted the model to a limited number of companies and organizations in what it called [Project Glasswing](https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/), an effort to deploy the model to secure critical software and infrastructure. Last week, [Anthropic expanded access to Mythos](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/?_thumbnail_id=3114152) to hundreds of organizations in 15 countries.

But despite the good intentions, many cybersecurity experts are still put off by the haphazard nature of the restrictions. Matt Suiche, a cybersecurity veteran, told TechCrunch that “if you ask it to write secure code, it assumes it is cybersecurity related work instead of software engineering best practices, and you get downgraded.” Fable is programmed to fall back to Claude Opus 4.8 if it hits a guardrail. “It seems to be keyword based, so anything in the lexical field of ‘cybersecurity’ triggers the guardrails.”

#### Contact Us

Do you have more information about how hackers are using AI? Or how cybersecuity companies are using AI? We’d love to hear from you. From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or

[email](mailto:lorenzo@techcrunch.com/)[.](mailto:lorenzo@techcrunch.com/)

“But it is understandable as we are still in the early days and they are still adapting their guardrails. I am sure they are going to evolve over time as Anthropic and other frontier model companies will collaborate more with the current new generation of cybersecurity companies,” said Suiche, who is a member of the technical staff at Tolmo, an AI cybersecurity startup. “It’s better to catch more people than not enough when you do such a release and to relax the guardrails over time.”

Another researcher [griped](https://x.com/evilsocket/status/2064694653765451925) on X that “even asking for a code review” triggers Fable’s guardrails.

Anthropic did not immediately respond to a request for comment.

Apart from guardrails inside its models, Anthropic requires cybersecurity professionals to apply to the [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude#:~:text=Program%20described%20below.-,Cyber%20Verification%20Program,-Many%20cybersecurity%20practitioners). If they get approved, the applicants have fewer limitations on using Claude for cybersecurity work. OpenAI has a similar program called [Trusted Access for Cyber](https://chatgpt.com/cyber).