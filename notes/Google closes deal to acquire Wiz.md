---
title: Google closes deal to acquire Wiz
url: https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz
clipped: 2026-06-17 01:34:11
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - cloud security
  - google cloud
  - tech mergers
  - ai security
related:
  - "[[Cloud Security]]"
  - "[[Google Cloud]]"
  - "[[Tech Mergers]]"
  - "[[AI Security]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Wiz officially joins Google Cloud, planning to accelerate AI-era security integrations while continuing its cloud-agnostic security posture.
>
> **Key points:**
> - The acquisition marks Wiz's transition into a Google company, focusing on securing rapid GenAI deployment.
> - Wiz emphasizes security as a business accelerator, offering visibility across code, cloud, and runtime.
> - The firm hit major development milestones during the acquisition process, maintaining rapid platform velocity.
> - Commenters voice concerns about Google's growing market concentration and potential loss of Wiz's cloud-agnostic edge.
>
> **Concept links:** [[Cloud Security]], [[Google Cloud]], [[Tech Mergers]], [[Ai Security]]
>
> **Suggested connections:**
> - [[Cloud Security]] — Integrates Wiz's agentless scanning architecture with Google's global scale.
> - [[Tech Mergers]] — Analyzes the competitive impact of large hyperscalers acquiring independent security platforms.
<!-- ai-summary:end -->

# [Google closes deal to acquire Wiz](https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz)

## Digest Summary
Wiz has officially become a Google company, maintaining its mission to protect all assets organizations build and run while adapting to the rapid pace of AI‑driven development. The blog notes that AI now accelerates application delivery, requiring security that scales with speed. Over the past year Wiz Research disclosed several high‑impact vulnerabilities—including an exposed Moltbook database, the CodeBreach supply‑chain flaw, the CVSS 10.0 Redis RCE “RediShell,” the NVIDIAScape container escape, and supply‑chain attacks such as Shai‑Hulud and NX—while hosting the ZeroDay.cloud hacking competition. Product advances introduced the Wiz AI Security Platform (visibility and protection for AI workloads), Wiz Exposure Management (unified risk view from code to cloud), AI Security Agents (automated investigation and remediation), and WizOS (hardened container base images). Wiz remains a multi‑cloud solution serving most Fortune 100 firms, AI labs, and cloud‑native companies across AWS, Azure, GCP, and OCI. Integration with Google’s infrastructure, Mandiant intelligence, and the Unified Security Platform is positioned to enhance its security capabilities.

## Discussion Summary
The comments combine factual observations with critical reactions. Reported accusations that a Wiz board member paid bribes to CISOs and the unprecedented arrangement for Israeli taxes to be paid in dollars are highlighted as concerning. Many express unease about Google’s acquisition reducing competition and potentially compromising Wiz’s cloud‑agnostic advantage, while others note strategic benefits such as deeper integration with Google’s security offerings. The tone is largely skeptical, citing monopoly risks, tax‑policy implications, and corporate‑culture jokes, though a few remarks acknowledge the company’s quality and congratulate the team.

---

## Full Article

Nearly a year ago, we shared that Wiz would be joining Google. At the time, we spoke about a belief that by bringing together Wiz’s innovation and Google’s scale, we could meaningfully change what security looks like in the cloud.

Today, as we officially begin our journey as a Google company, that belief feels real in a much deeper way. Not because of what has changed, but because of what has stayed true.

Our mission remains bold and unwavering: **to help every organization protect everything they build and run.** What has changed is the world around us. Now, we must do this at the speed of AI.

A Year of Redefining Velocity
-----------------------------

Cloud once transformed how fast teams could build. AI is doing it again, unlocking a new era of innovation where applications move from idea to production in minutes. Generative AI is no longer experimental; it’s becoming a core part of how modern organizations build, ship, and scale.

Customers are leaning into this moment, using AI to move faster, create more, and reimagine what’s possible. But building at this pace requires a new approach to security – one that keeps up with change and supports innovation rather than slows it down.

At Wiz, we believe security should accelerate progress. By combining deep understanding of cloud environments with rich context across code, cloud, and runtime, we enable teams to build AI-powered applications securely from the start and strengthen them continuously as they evolve.

Today’s security leaders are focused on enabling the business, supporting rapid innovation while staying ahead of increasingly sophisticated threats. With Wiz, they don’t have to choose between speed and security.

In this environment, velocity is everything. At Wiz, it’s our mantra; we’re committed to helping customers turn that speed into a lasting edge – building boldly, securely, and with confidence.

The Path That Brought Us Here
-----------------------------

During the acquisition process, our wizards never stopped building. In the past year, we hit many major milestones thanks to their grit and determination.

**Wiz** **Research** continues to be at the forefront of security, uncovering critical vulnerabilities that protect not just Wiz customers, but the industry at large. This work highlights the systemic risks inherent in the digital age, with discoveries like:

* An exposed database in [Moltbook](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys), a viral social network for AI agents, that leaked millions of API keys and underscored the security implications of vibe coded applications.
* [CodeBreach](https://www.wiz.io/blog/wiz-research-codebreach-vulnerability-aws-codebuild), a critical supply chain vulnerability that could have compromised the AWS Console.
* [RediShell](https://www.wiz.io/blog/wiz-research-redis-rce-cve-2025-49844), a 13-year-old critical RCE flaw in Redis (CVSS 10.0) that impacted over 75% of cloud environments.
* [NVIDIAScape](https://www.wiz.io/blog/nvidia-ai-vulnerability-cve-2025-23266-nvidiascape), a container escape vulnerability that threatened shared AI infrastructure.
* A collaboration with vibe coding leader [Lovable](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps) to harden their platform and protect the next generation of AI-generated applications (where Wiz found that 1 in 5 organizations are exposed to systemic risks).
* The discovery and remediation of a sophisticated wave of supply chain attacks, including [Shai-Hulud](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack) and [NX](https://www.wiz.io/blog/s1ngularitys-aftermath), where our research protected hundreds of organizations from highly targeted, evolving threats.

To push the boundaries of innovation even further, we also hosted [ZeroDay.cloud](https://www.wiz.io/blog/wiz-zeroday-cloud-hacking-competition-behind-the-scenes), a first-of-its-kind hacking competition where the world's top researchers uncovered a record number of CVEs in foundational cloud and AI tools.

These milestones represent our unwavering commitment to securing the open-source and multicloud infrastructure underpinning the modern world.

Building an AI Security Platform for the Future
-----------------------------------------------

Product innovation has always been at the heart of Wiz, and over the past year, our momentum has only accelerated.

As customers build and ship faster in the AI era, we expanded the [**Wiz AI Security Platform**](https://www.wiz.io/blog/complete-ai-application-visibility-wiz) to secure AI applications themselves, providing visibility into AI usage, preventing AI-native risks, and protecting AI workloads in runtime.

We introduced [Wiz Exposure Management](https://www.wiz.io/blog/wiz-exposure-management-now-generally-available) to give teams a single, proactive view of risk -- unifying vulnerability and attack surface management from code to cloud to on-prem, so they can focus on what truly matters and proactively remove exploitable risk.

We pushed the boundaries of automation with [AI Security Agents](https://www.wiz.io/blog/wiz-ai-agents), purpose-built to help teams investigate, prioritize, and remediate risk at machine speed, powered by deep context across code, cloud, and runtime.

And to help developers start secure by default, we launched [WizOS](https://www.wiz.io/blog/wizos-secured-image-adoption-with-ai): hardened, near-zero-CVE container base images that give teams a trusted foundation from the very first commit.

These are just a few highlights from a year of relentless building, and we’re only getting started.

### **The Power of AI and the Strength of Multi-Cloud**

Now, as one team with Google Cloud, we have the opportunity to accelerate our roadmap in ways that simply weren’t possible before. By integrating the most cutting edge AI capabilities into the Wiz platform, we’ll continue to give security teams new superpowers. In the coming days, we’ll share more about how we’re already working with Gemini, and what the next phase of this partnership will unlock.

But one thing is not changing: **Wiz remains a multi-cloud platform.** Today, we work with most of the Fortune 100, and most of the Frontier AI labs, as well as many of the world’s fastest-growing, cloud-native companies. Our customers run on AWS, Azure, GCP, and OCI. Our goal is to protect their entire environment – every workload, every application, every major cloud.

Joining Google doesn’t narrow our focus. It strengthens it. With Google’s infrastructure, Mandiant’s threat intelligence, and the broader Google Unified Security Platform and ecosystem, we can protect customers better – wherever they build.

Trust is something we earn every day. And we intend to prove it through our actions, our product, and our pace of innovation.

### **The Next Chapter**

To our customers: thank you for your trust. You challenge us to solve the hardest problems in security, and you are the reason we build.

To the Wiz team: I may be CEO in title, but you are the ones who lead. Thank you for your dedication, your care, and your belief in what we’re making together.

Our mission remains as bold as ever: to protect everything organizations build and run.  
And we are *still* just getting started.

###### Get a 1-on-1 demo

From code to cloud to AI, get a firsthand look at how Wiz helps you build, ship, and run securely, regardless of where your workloads live.
