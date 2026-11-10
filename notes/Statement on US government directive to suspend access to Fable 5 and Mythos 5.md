---
title: "Statement on US government directive to suspend access to Fable 5 and Mythos 5"
url: https://www.anthropic.com/news/fable-mythos-access
clipped: 2026-06-17 00:48:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Statement on US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

## Digest Summary
The U.S. government issued an export‑control directive requiring Anthropic to suspend all access to its Fable 5 and Mythos 5 models for any foreign national, including Anthropic employees abroad, effective immediately; other Anthropic models remain available. The order, received at 5:21 p.m. ET, cites a national‑security concern about a “jailbreak” method for Fable 5 but provides no specifics. Anthropic reviewed the reported technique, finding only minor, non‑universal vulnerabilities that also exist in publicly available models.  

Key points from Anthropic’s response:  
- Strong safeguards were built into Fable 5, tested for thousands of hours with U.S., U.K., and private red‑team partners, and deemed more effective than prior models.  
- No universal jailbreak has been discovered; only narrow, low‑impact bypasses are known.  
- A defense‑in‑depth strategy, including 30‑day data retention for monitoring, is in place.  
- The cited jailbreak involved asking the model to analyze and fix a codebase—capabilities common to other frontier models.  
- Anthropic argues that recalling the models over a narrow issue would set a precedent that could halt future model deployments and calls for a transparent, fact‑based statutory process.  

Anthropic apologizes for the disruption and is working to restore access.

## Discussion Summary
Comments converge on the view that the U.S. export‑control action against Anthropic’s Fable 5 and Mythos 5 signals a broader shift toward governmental restriction of advanced language models, driven by national‑security concerns. Many see the move as likely to limit public and foreign access, prompting speculation about future KYC requirements, on‑premise deployments, and increased reliance on non‑U.S. alternatives such as Chinese or European offerings. While some criticize Anthropic’s hype and handling of safeguards, others doubt the models’ superiority and worry the decision will hinder AI innovation and market dynamics. Overall sentiment is cautious and skeptical about both the policy and the technology’s impact.

---

## Full Article

The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for **all** our customers to ensure compliance. **Access to all other Anthropic models** **will not be affected.**

We received the directive from the government today at 5:21pm (ET). The letter did not provide specific details of its national security concern. Our understanding is that the government believes it has become aware of a method of bypassing, or “jailbreaking” Fable 5. We reviewed a demonstration of this specific technique being used to identify a small number of previously known, minor vulnerabilities. These vulnerabilities all appear relatively simple, and we have found that other publicly-available models are able to discover them as well without requiring a bypass.

Anthropic’s posture with respect to Fable’s safeguards, as laid out in our launch [blog post](https://www.anthropic.com/news/claude-fable-5-mythos-5), is the following:

* We have instituted strong safeguards that greatly reduce the likelihood that Fable is misused for tasks related to cybersecurity (among others). In fact, our safeguards are so strong that many users have complained that they are overly broad.
* In the weeks leading up to the launch of Fable, Anthropic worked with the US government, the UK AISI, multiple private third-party organizations and internal teams to red-team Fable’s safeguards for thousands of hours in total.
* These tests showed that Fable’s safeguards are substantially more effective than those of any previously deployed model.
* No testers have yet been able to find a *universal jailbreak*—a jailbreak method that can very broadly bypass the model’s safeguards, unblocking a wide range of cyber capabilities.
* We suspect that perfect jailbreak resistance is not currently possible for any model provider. Every safeguard used in the industry is vulnerable to *non-universal jailbreaks* (which can elicit *some* cyber information in specific circumstances), and it is likely that universal jailbreaks will eventually be found in the future. We stated this clearly when we [released](https://www.anthropic.com/news/claude-fable-5-mythos-5) Fable 5.
* Given that perfect jailbreak resistance does not appear to be possible today, Anthropic adopted a *defense in depth* strategy with Fable 5. We aimed to make jailbreaks either narrow (in the case of non-universal jailbreaks) or very expensive to produce (in the case of universal jailbreaks), and to combine this with thorough monitoring to quickly detect and shut down any successful attacks. This is also why Anthropic has required 30-day retention of customer data with Fable—a policy change that carries [real costs for us with customers](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models), but that allows us to research and mitigate jailbreaks.
* We stand by this defense in depth strategy. It reduces the risks posed by Fable, making them comparable to the risks of existing models already deployed across the industry.
* We have not even received a disclosure of a concerning non-universal potential jailbreak that led to a harmful result. The potential jailbreaks that have been disclosed to us are either entirely benign responses or are minor findings that provide no Mythos-specific uplift.

To date, the government has only given us verbal evidence of a potential narrow, non-universal jailbreak, which essentially consists of asking the model to read a specific codebase and fix any software flaws. Our understanding is that one potential jailbreak was shared with the government. We have reviewed a report that we believe is the basis of the government's directive and validated that the level of capability displayed there is widely available from other models (including OpenAI’s [GPT-5.5](https://deploymentsafety.openai.com/gpt-5-5/cybersecurity)), and is used every day by the defenders who keep systems safe. We will share more details over the next 24 hours.

We are complying with the government’s legal directive and are removing access to Fable 5 and Mythos 5 for all users. However, we disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people. If this standard was applied across the industry, we believe it would essentially halt all new model deployments for all frontier model providers.

As we have [stated](https://www.anthropic.com/policy-on-the-ai-exponential) [publicly](https://darioamodei.com/post/policy-on-the-ai-exponential), we believe the government should have the ability to block unsafe deployments, as part of a statutory process that is transparent, fair, clear, and grounded in technical facts. This action does not adhere to those principles.

We apologize for this disruption to our customers. We believe this is a misunderstanding and are working to restore access as soon as possible.