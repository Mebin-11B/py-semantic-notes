---
title: "Cal.com is going closed source"
url: https://cal.com/blog/cal-com-goes-closed-source-why
clipped: 2026-06-17 01:16:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Open Source vs Closed Source
  - AI Security Risks
  - Vulnerability Scanning
  - Cal.com
  - Cal.diy
  - Product Monetization
related:
  - "[[Show HN A context-aware permission guard for Claude Code]]"
  - "[[I found a Vulnerability. They found a Lawyer]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Cal.com transitions its main scheduling codebase to closed source, citing security vulnerabilities exposed by AI-driven scanning tools.
>
> **Key points:**
> - Cal.com closed its production repository to mitigate the risk of automated AI tools scanning code to generate exploits.
> - AI security scanners make codebases "blueprints" for attackers, as demonstrated by the AI discovery of a 27-year-old BSD kernel flaw.
> - To support the community, Cal.com released Cal.diy, a separate MIT-licensed version lacking production authentication and data handling.
> - Criticisms suggest the move is "security-by-obscurity" or a business strategy to prevent AI cloning rather than a safety measure.
>
> **Concept links:** [[Open Source vs Closed Source]], [[AI Security Risks]], [[Vulnerability Scanning]], [[Cal.com]], [[Cal.diy]], [[Product Monetization]]
>
> **Suggested connections:**
> - [[Show HN A context-aware permission guard for Claude Code]] — related to security guards for automated agents.
> - [[I found a Vulnerability. They found a Lawyer]] — related security reporting and company behaviors.
<!-- ai-summary:end -->

# [Cal.com is going closed source](https://cal.com/blog/cal-com-goes-closed-source-why)

## Digest Summary
Cal.com is transitioning its production codebase from open source to closed source, citing heightened security risks posed by AI. The company argues that modern AI tools can rapidly scan publicly available code, identify vulnerabilities, and generate exploits, effectively giving attackers “blueprints” to the software. Recent AI‑driven security startups have produced multiple, sometimes conflicting vulnerability reports, making it hard to determine a reliable security baseline. To protect user data, Cal.com chose to close its main code while still supporting the open‑source community by releasing a separate MIT‑licensed version, Cal.diy, which diverges significantly from the production system (including rewrites of authentication and data handling). The decision references an AI discovery of a 27‑year‑old BSD kernel flaw as evidence of the accelerated threat landscape. Cal.com hopes to revert to open source when security conditions improve.

## Discussion Summary
Comments largely criticize the shift to closed‑source, describing it as security‑by‑obscurity and a marketing pretext rather than a genuine technical solution. Contributors argue that AI tools actually enhance open‑source auditing, making transparency more valuable and that obscuring code does not prevent exploitation of binaries. Several remarks emphasize business motivations—revenue, protecting against AI‑driven cloning, and competitive advantage—over security concerns. While a minority accept the move as a pragmatic business decision, the dominant view questions its effectiveness and sees it as detrimental to trust and the open‑source ecosystem.

---

## Full Article

![](https://i.ytimg.com/vi_webp/JYEPLpgCRck/sddefault.webp)VIDEO

This is not an easy post to write.

When we started Cal.com, we believed deeply in [open source](https://cal.com/blog/the-ultimate-guide-to-open-source-calendar-software-and-scheduler-tools). Itâs a core principle we built this company around, and something weâve been incredibly proud of.

Today, we are making the very difficult decision to move to closed source, and thereâs one simple reason: security.

AI is changing everything. Itâs transforming how we write content, build software, and operate day to day. But whatâs talked about far less is how dramatically AI is changing the world of security.

In the past, exploiting an application required a highly skilled hacker with years of experience and a significant investment of time to find and exploit vulnerabilities. The reality is that humans donât have the time, attention, or patience to find everything.

Today, AI can be pointed at an open source codebase and [systematically scan it for vulnerabilities](https://cal.com/blog/continuous-ai-pentesting-vulnerability-discovery).

Being open source is increasingly like giving attackers the blueprints to the vault. When the structure is fully visible, it becomes much easier to identify weaknesses and exploit them.

In recent months, weâve seen a wave of AI security startups productizing this capability. Each platform surfaces different vulnerabilities, making it difficult to establish a single, reliable source of truth for what is actually secure.

This uncertainty forced us to make a choice: remain open source and accept increasing risk to customer data, or move to closed source to reduce that risk. Itâs not a perfect solution, but we have to do everything we can to protect our users.

At the same time, we still care deeply about open source. Thatâs why we are releasing a version of our codebase to the community under the MIT license as [Cal.diy](https://cal.com/blog/cal-diy-open-source-to-closed-source). While our production codebase has significantly diverged, including major rewrites of core systems like [authentication and data handling](https://cal.com/blog/ensuring-data-privacy-in-open-source-scheduling), we want to ensure there is still a [truly open version](https://cal.com/blog/self-hosted-scheduling-platforms-benefits-and-challenges) available for developers, hobbyists, and anyone who wants to explore and experiment.

The risk landscape is accelerating quickly. Advanced AI models are now capable of identifying and exploiting vulnerabilities at unprecedented speed. In one recent example, AI uncovered a 27-year-old vulnerability in the BSD kernel, one of the most widely used and security-focused open source projects, and generated working exploits in a matter of hours.

Continuing as open source would put our application, our customers, and the [sensitive data](https://cal.com/security) we handle at significant risk. We are taking every step we can to reduce that risk and protect our users, and for now, that means moving to closed source despite how difficult that decision is.

We hope that one day we can return to open source as the security landscape evolves. But for now, we have to put our customers first.