---
title: "Going Full Time on Open Source"
source: "https://jdx.dev/posts/2026-04-17-going-full-time-on-open-source/"
author:
published: 2026-04-23
created: 2026-06-01
description: "Jeff Dickey's personal website"
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Open Source
  - Developer Tools
  - CLI Tools
  - Software Engineering Career
  - Software Licensing
  - Sustainable Development
related:
  - "Developer Tools"
  - "Exceptional engineers.md"
  - "tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Jeff Dickey shares his transition from Figma to full-time open-source development on mise and other dev tools, exploring sustainability models like memberships, corporate sponsorships, and targeted consulting.
>
> **Key points:**
> - Describes the massive success of mise (a Rust-based rewrite of asdf), which has become the 10th most downloaded Homebrew formula and is used by OpenAI and NVIDIA.
> - Details the challenge of maintaining rapidly growing open-source projects alongside a full-time job, leading to notification overload and 'notification bankruptcy.'
> - Introduces en.dev as a vehicle for full-time work, aiming to fund development, improve project bus factor, and keep open-source maintainership sustainable.
> - Outlines a multi-pronged monetization strategy including tiered individual memberships, corporate sponsorships, high-rate monorepo consulting, and future developer-focused services.
> - Emphasizes that the ultimate goal is sustainable developer tool creation rather than venture-backed SaaS hyper-growth.
>
> **Concept links:** [[Open Source]], [[Developer Tools]], [[CLI Tools]], [[Software Engineering Career]], [[Software Licensing]], [[Sustainable Development]]
>
> **Suggested connections:**
> - [[Exceptional engineers.md]] — highlights the drive of independent creators building complex software systems as a form of personal craft.
> - [[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]] — connects to other Rust-based CLI developer utilities being built in the community.
> - [[Software Engineering Career]] — provides context on alternative paths in tech, moving away from corporate software engineering towards independent open-source maintainership.
<!-- ai-summary:end -->

For the last several years, I’ve been building and maintaining developer tools in my spare time, chiefly [mise](https://mise.jdx.dev/).

What started as a simple rewrite of [asdf](https://asdf-vm.com/) in Rust has become an incredibly successful local dev manager. mise now has [27k+ stars on GitHub](https://github.com/jdx/mise) and is the [10th most downloaded Homebrew formula](https://formulae.brew.sh/analytics/install-on-request/30d/). In fact, roughly 1% of users typing `brew install` are running `brew install mise`.

I’ve also watched mise show up in places I never expected, including [OpenAI Codex Universal](https://github.com/openai/codex-universal/blob/54b8f0434886aeff0817cc4d5a7d76bdb0d834d5/Dockerfile#L86-L100) and [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell/blob/e4d6f92d9b803719928eca5187b428a7ca55c1a5/mise.toml).

Alongside it I maintain [aube](https://github.com/endevco/aube) (the newest of the bunch, which I’m really excited about), [hk](https://hk.jdx.dev/) (git hook runner), [pitchfork](https://pitchfork.jdx.dev/) (process supervisor), [fnox](https://fnox.jdx.dev/) (secrets), [usage](https://github.com/jdx/usage), and a handful of smaller tools.

That has been incredibly rewarding. It’s also become a lot of work. For a while, I could do this alongside a full-time job. But as mise has grown, that has become less and less realistic. I have not been able to keep up with PR review the way I want to. I’ve had to declare notification bankruptcy every few weeks by deleting all of my GitHub notifications because I genuinely could not keep up.

I do not want mise to stall because I only have scraps of time left after work. I want it to keep getting better.

So I left Figma to work on these full time.

## en.dev

To keep this sustainable I’m doing it under a company: [en.dev](https://en.dev/). Right now that means one person — me — working full time on mise and the rest of the portfolio. If the funds grow enough, the plan is to bring on a second maintainer so mise keeps a bus factor above 1.

## Money

My OSS work does not currently make enough money for me to live on. Right now, I make roughly:

- **$100/month** from ads in the docs
- **$500/month** from GitHub Sponsors

I’m grateful for this, but it won’t be enough, so I am going to try a few different ways to make this work.

### Memberships

For individuals who want to support the work, I’ve set up tiered memberships at [en.dev](https://en.dev/):

- **Supporter** — $5/mo or $50/yr
- **Member** — $10/mo or $100/yr
- **Sustaining Member** — $20/mo or $200/yr
- **Patron** — $50+/mo or $500+/yr

Members get access to a members-only Discord and a mention in `mise patrons`. There will also be a bi-weekly Live Q&A and bi-weekly newsletter for members.

### Sponsorships

For companies that rely on mise, I’m offering two sponsor tiers:

- **Backer** — $200+/mo — logo on [en.dev](https://en.dev/), plus a GitHub Sponsors badge. For small teams that depend on mise.
- **Sustainer** — $1,000+/mo — logo on [en.dev](https://en.dev/) *and* on the docs site for every en.dev tool (mise, hk, pitchfork, fnox, etc.), in a more prominent position.

Sponsorship is not roadmap control, and it is not a private support contract. It is a way for companies to fund the open source infrastructure they depend on.

### Consulting

I’m also going to spend up to 2 days a week consulting for companies that want hands-on help adopting mise. Typical engagements look like:

- Migrating a monorepo’s tooling onto `mise.toml`
- Wiring mise into CI and standardising images / containers
- Authoring custom plugins for internal tools
- Reviewing how secrets and env vars flow through developer machines

Rates are high — I’m the only person in the world who can offer this, slots are scarce, and a portion of every engagement subsidises ongoing mise development.

### Paid Services

Longer term, I want to identify paid services I could host for teams that use mise.

I have not figured out exactly what those should be yet. I want these to be simple since my goal is sustainability so that I can build OSS tools, not building a SaaS and becoming a billionaire. If you use mise at work and have ideas for services your team would pay for, please let me know.

## The Goal

If you use mise and want to support that, you can become a member at [en.dev](https://en.dev/), sponsor me on [GitHub Sponsors](https://github.com/sponsors/jdx), or [reach out](https://jdx.dev/contact/) if your company is interested in sponsorship or consulting.

Thank you to everyone who has used mise, contributed to it, reported bugs, written docs, recommended it to a teammate, or sponsored the work already.