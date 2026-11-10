---
title: "Some things just take time"
url: https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/
clipped: 2026-06-17 01:29:20
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - longevity
  - open source sustainability
  - AI acceleration
  - software quality
  - developer productivity
  - trust and community
related:
  - "[[Using AI to write better code more slowly]]"
  - "[[Software Quality]]"
  - "[[Open Source Sustainability]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The essay reflects on how valuable, enduring outcomes—such as mature trees, Swiss watches, trust, and software quality—inherently require time and tenacity, warning against the harms of the modern obsession with instant gratification and AI-accelerated speed.
>
> **Key points:**
> - Valuable achievements require embedded time, and attempting to automate away all friction (e.g., in compliance or software design) can degrade quality, trust, and maturity.
> - AI-assisted rapid development risks commoditizing software and shortening product shelf lives, resulting in transient startups and open-source projects that are abandoned after a few commits.
> - "Time-saving" tools rarely grant developers more leisure; instead, saved time is captured by competition, leading to higher output pressure and less capacity for deep, quality work.
> - The true hallmark of successful companies and open-source projects remains longevity and the tenacity of maintainers who commit to problems across years and decades.
>
> **Concept links:** [[Longevity]], [[Open Source Sustainability]], [[AI Acceleration]], [[Software Quality]], [[Developer Productivity]], [[Trust and Community]]
>
> **Suggested connections:**
> - [[Using AI to write better code more slowly]] — contrasting the push for AI speed with the need for deliberate, high-quality development practices.
> - [[Software Quality]] — discussing how rapid iteration and lack of friction can degrade the long-term viability of software products.
> - [[Open Source Sustainability]] — analyzing how tenacity and long-term commitment define successful open-source projects compared to short-lived hype.
<!-- ai-summary:end -->

# [Some things just take time](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/)

## Digest Summary
The essay reflects on how many valuable outcomes—trees, historic goods, legal rights—require long periods to develop, and argues that this principle also applies to software, startups, and open‑source projects. It critiques the current emphasis on rapid iteration, instant gratification, and frictionless automation, especially in AI‑driven code generation and compliance processes, noting that speed can undermine durability, trust, and community continuity. The author observes that accelerated development often yields short‑lived products whose shelf life is measured in months, and that premature shutdowns erode customer relationships. In open‑source, fleeting commit activity and lack of succession planning threaten project longevity. The piece also questions the promise of “time‑saving” tools, suggesting that any saved time is quickly re‑absorbed by competitive pressures, leaving developers with less genuine capacity for quality work. Ultimately, the author emphasizes that sustained commitment and gradual growth—akin to planting and nurturing a tree—are essential for lasting impact.

## Discussion Summary
Comments emphasize that AI accelerates prototyping and debugging but stress that speed without clear direction can waste effort. Many note that iterative refinement and domain knowledge remain essential, and that AI tools serve as aids rather than replacements for expertise. Concerns are raised about productivity pressures, burnout, and the persistence of tasks that inherently require time. Overall sentiment balances optimism about AI‑enabled efficiency with caution that quality, alignment, and human judgment must guide rapid development.

---

## Full Article

Some Things Just Take Time
==========================

written on March 20, 2026

Trees take quite a while to grow. If someone 50 years ago planted a row of oaks
or a chestnut tree on your plot of land, you have something that no amount of
money or effort can replicate. The only way is to wait. Tree-lined roads, old
gardens, houses sheltered by decades of canopy: if you want to start fresh on an
empty plot, you will not be able to get that.

Because some things just take time.

We know this intuitively. We pay premiums for Swiss watches, Hermès bags and
old properties precisely because of the time embedded in them. Either because
of the time it took to build them or because of their age. We require age
minimums for driving, voting, and drinking because we believe maturity only
comes through lived experience.

Yet right now we also live in a time of instant gratification, and it’s entering
how we build software and companies. As much as we can speed up code
generation, the real defining element of a successful company or an Open Source
project will continue to be tenacity. The ability of leadership or the
maintainers to stick to a problem for years, to build relationships, to work
through challenges fundamentally defined by human lifetimes.

Friction Is Good
----------------

The current generation of startup founders and programmers is obsessed
with speed. Fast iteration, rapid deployment, doing everything as quickly as
possible. For many things, that’s fine. You can go fast, leave some quality on
the table, and learn something along the way.

But there are things where speed is actively harmful, where the friction exists
for a reason. Compliance is one of those cases. There’s a strong desire to
eliminate everything that processes like SOC2 require, and an entire industry of
turnkey solutions has sprung up to help —
[Delve](https://substack.com/home/post/p-191342187) just being one example,
there are more.

There’s a feeling that all the things that create friction in your life should
be automated away. That human involvement should be replaced by AI-based
decision-making. Because it is the friction of the process that is the problem.
When in fact many times the friction, or that things just take time, is
precisely the point.

There’s a reason we have cooling-off periods for some important decisions in
one’s life. We recognize that people need time to think about what they’re
doing, and that doing something right once doesn’t mean much because you need to
be able to do it over a longer period of time.

Vibe Slop At Inference Speeds
-----------------------------

AI writes code fast which isn’t news anymore. What’s interesting is that we’re
pushing this force downstream: we seemingly have this desire to ship faster than
ever, to run more experiments and that creates a new desire, one to remove all
the remaining friction of reviews, designing and configuring infrastructure,
anything that slows the pipeline. If the machines are so great, why do we even
need checklists or permission systems? Express desire, enjoy result.

Because we now believe it is important for us to just do everything faster. But
increasingly, I also feel like this means that the shelf life of much of the
software being created today — software that people and businesses should depend
on — can be measured only in months rather than decades, and the relationships
alongside.

In one of last year’s earlier YC batches, there was already a handful that just
disappeared without even saying what they learned or saying goodbye to their
customers. They just shut down their public presence and moved on to other
things. And to me, that is not a sign of healthy iteration. That is a sign of
breaking the basic trust you need to build a relationship with customers. A
proper shutdown takes time and effort, and our current environment treats that
as time not wisely spent. Better to just move on to the next thing.

This is extending to Open Source projects as well. All of a sudden, everything
is an Open Source project, but many of them only have commits for a week or so,
and then they go away because the motivation of the creator already waned. And
in the name of experimentation, that is all good and well, but what makes a good
Open Source project is that you think and truly believe that the person that
created it is either going to stick with it for a very long period of time, or
they are able to set up a strategy for succession, or they have created enough
of a community that these projects will stand the test of time in one form or
another.

My Time
-------

Relatedly, I’m also increasingly skeptical of anyone who sells me something that
supposedly saves my time. When all that I see is that everybody who is like me,
fully onboarded into AI and agentic tools, seemingly has less and less time
available because we fall into a trap where we’re immediately filling it with
more things.

We all sell each other the idea that we’re going to save time, but that is not
what’s happening. Any time saved gets immediately captured by competition.
Someone who actually takes a breath is outmaneuvered by someone who fills every
freed-up hour with new output. There is no easy way to bank the time and it
just disappears.

I feel this acutely. I’m very close to the red-hot center of where economic
activity around AI is taking place, and more than anything, I have less and less
time, even when I try to purposefully scale back and create the space. For me
this is a problem. It’s a problem because even with the best intentions, I
actually find it very hard to create quality when we are quickly commoditizing
software, and the machines make it so appealing.

I keep coming back to the trees. I’ve been maintaining Open Source projects for
close to two decades now. The last startup I worked on, I spent 10 years at.
That’s not because I’m particularly disciplined or virtuous. It’s because I or
someone else, planted something, and then I kept showing up, and eventually the
thing had roots that went deeper than my enthusiasm on any given day. That’s
what time does! It turns some idea or plan into a commitment and a commitment
into something that can shelter and grow other people.

Nobody is going to mass-produce a 50-year-old oak. And nobody is going to
conjure trust, or quality, or community out of a weekend sprint. The things
I value most — the projects, the relationships, the communities — are all
things that took years to become what they are. No tool, no matter how fast,
was going to get them there sooner.

We recently [planted a new tree](https://earendil.com/) with Colin. I want it
to grow into a large one. I know that’s going to take time, and I’m not in a
rush.

This entry was tagged
[ai](https://lucumr.pocoo.org/tags/ai/)

[copy as](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time.md) / [view](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time.md) markdown