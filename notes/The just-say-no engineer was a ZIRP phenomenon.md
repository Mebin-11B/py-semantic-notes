---
title: "The just-say-no engineer was a ZIRP phenomenon"
url: https://www.seangoedecke.com/the-just-say-no-engineer-was-a-zirp-phenomenon/
clipped: 2026-06-17 00:56:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - zirp era
  - developer archetypes
  - software quality
  - ai generated code
  - engineering leadership
  - pure vs impure engineering
related:
  - "[[ZIRP Era]]"
  - "[[Developer Archetypes]]"
  - "[[Pure vs Impure Engineering]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An essay on how the senior "just-say-no engineer" archetype, which prioritized code quality and gatekeeping, was supported by ZIRP economics and is now struggling in the AI and efficiency era.
>
> **Key points:**
> - The "just-say-no engineer" focuses on limiting complexity and blocking unnecessary code, contrasting with the fast-moving "just-say-yes" engineer.
> - During the zero interest rate policy (ZIRP) era (2008-2022), companies had the budget to tolerate project bloat and relied on gatekeepers to keep codebases manageable.
> - Post-ZIRP, corporate strategy has shifted toward rapid monetization, forcing gatekeepers to accept massive amounts of AI-generated code and face management pressure to say "yes."
> - While marginalized in user-facing feature development ("impure engineering"), this archetype remains critical in core infrastructure and compiler teams ("pure engineering").
>
> **Concept links:** [[ZIRP Era]], [[Developer Archetypes]], [[Software Quality]], [[AI Generated Code]], [[Engineering Leadership]], [[Pure vs Impure Engineering]]
>
> **Suggested connections:**
> - [[ZIRP Era]] — Explores the macroeconomic environment that shaped software team scales and corporate priorities.
> - [[Developer Archetypes]] — Classifies the roles and dynamics senior software engineers assume within organizations.
> - [[Pure vs Impure Engineering]] — Distinguishes between well-scoped technical system engineering and user-driven rapid iterations.
<!-- ai-summary:end -->


# [The just-say-no engineer was a ZIRP phenomenon](https://www.seangoedecke.com/the-just-say-no-engineer-was-a-zirp-phenomenon/)

## Digest Summary
The essay defines the “just‑say‑no engineer” as a senior technical archetype whose primary function is to block changes, prioritize code quality, and limit complexity, contrasting with a “just‑say‑yes” engineer who pushes rapid delivery. During the ZIRP era (2008‑2022), low‑interest financing fueled massive hiring, allowing companies to tolerate bloated engineering staff and rely on such gatekeepers to prevent runaway projects, maintain high technical standards, and enhance hiring reputation. When interest rates rose, tech firms cut 5‑20 % of staff, shifted focus to revenue‑generating AI‑driven features, and withdrew managerial support for the gatekeeping role. Consequently, just‑say‑no engineers now face pressure to approve AI‑generated code, experience reduced influence, and must adapt or relocate to “pure” engineering domains (e.g., core infrastructure, compilers) where slower, higher‑quality development remains valuable. The author argues the archetype’s relevance contracts post‑ZIRP but does not disappear, as niche pure‑engineering teams still require stringent quality oversight.

## Discussion Summary
Comments display mixed reactions to the claim that ending ZIRP should increase “just‑say‑no” engineering. Some argue that higher capital costs justify stricter project selection and stronger technical standards, while others view the premise as overly cynical or untestable, noting that many AI firms remain unprofitable regardless of interest rates. Opinions diverge on engineering practices such as skipping code reviews, with experiences cited on both sides. Additional remarks broaden the discussion to the broader economic impact of prolonged low‑rate policies, AI hype, and differing industry contexts.

---

## Full Article

The engineer who [says no all the time](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise#a-senior-developer-is-a-problem-avoider) is a real archetype among senior and staff engineers. Their role is to slow things down, to block the development of features that add complexity, and to ensure that as little code gets written as possible (since code is a liability).

We can think of this as the just-say-no engineer, as opposed to the just-say-yes engineer. The just-say-yes engineer is obsessed with moving fast, approves code changes by default, values [MTTR](https://en.wikipedia.org/wiki/Mean_time_to_repair) over [MTBF](https://en.wikipedia.org/wiki/Mean_time_between_failures), and tends to ship a lot of code. The just-say-no engineer is obsessed with quality, is happy to move slowly, and blocks code changes by default. Most engineers are somewhere in the middle of the spectrum. By “just-say-no engineer”, I’m talking about the group of engineers who most strongly identify with that archetype.

The just-say-no engineer is having a hard time in the era of AI. It used to be that they only had to say no to more junior engineers’ handwritten PRs, but now they have to say no to a barrage of AI-generated code, some of it generated by managers and VPs who are politically difficult to say no to. For the first time in their careers, they’re under a lot of pressure to lower their standards and start saying yes. However, **this isn’t because of AI.** It’s because of the end of ZIRP.

### ZIRP and the just-say-no engineer

ZIRP, or the “zero interest rate policy”, is a shorthand for the era of software development between 2008 and 2022 when banks were allowing companies to borrow money at near-zero interest rates. During this period, investors were throwing borrowed money at *anything*, which meant that tech companies were incentivized to constantly hire engineers for low-risk high-reward projects. Successful companies would routinely grow from tens of engineers to thousands, who would go and work on all kinds of things: tangential open-source projects, endless technology migrations, rewrites into other languages, and so on.

It was a great time to be a software engineer. We had a lot of bargaining power, and could get paid top dollar to do almost anything. The bosses largely didn’t care, because (a) teams were growing so fast they couldn’t pay attention, and (b) just having more engineers around was beneficial to the stock price, which was the main thing they cared about. But tech companies did have one problem: with so many engineers running wild, how would they keep their systems from becoming completely unmanageable? **Enter the just-say-no engineer.**

In this environment, having a very senior engineer whose only job is to say no to things was actually quite valuable to the company. There are a few reasons for this:

* Having half of the company’s engineers enmeshed in an endless loop of proposing changes and being told no was totally fine - they didn’t need to be productive anyway, and this way they weren’t impacting business-critical systems.
* It also solved the problem of the 5% of engineers who would get drunk on their technical freedom and make wild proposals like migrating to a hand-rolled database.
* Having a reputation for a very high technical bar is a positive for hiring (and remember, during ZIRP every tech company was always hiring)

### The end of ZIRP

When banks hiked interest rates, almost every tech company immediately laid off 5-20% of their engineers. It was just no longer profitable to keep a bloated engineering staff around to boost the stock price. Instead, companies had to actually make money. However, that wasn’t a good public explanation for the layoffs, since it sounds weak to admit that you were paying hundreds of engineers to do unprofitable work. Fortunately, the end of ZIRP coincided roughly with the rise of ChatGPT, so tech companies were able to to blame their layoffs on the power of AI. Saying “with this transformative new technology, we’re able to deliver 10x the value with half the engineers” is a much stronger message, even though it doesn’t make much sense (if this is true, why not keep your engineers and deliver 20x the value?)

Something like this dynamic has been happening to the just-say-no engineer. Tech companies are now more focused than at any time in the past two decades. They are not doing a bunch of random crap anymore; instead they’re desperately chasing new capabilities and features that can make money (mostly built on AI, for obvious reasons). This new environment is *actively inimical* to the just-say-no engineer. It’s as if a shark got pulled out of the deep ocean and dropped into a fast-flowing river: what was once a powerful apex predator is now disoriented and flailing.

This kind of engineer used to enjoy implicit (albeit distant) support from their management. If someone complained, they’d often get told “that engineer knows what they’re doing, if they said no, then I trust them”. Now that support is gone. The just-say-no engineer is now being criticized and actively overruled by their management. They’re being told to be more of a team player, to find a way to say yes, or are simply no longer being consulted (with the company’s blessing) on key decisions. They’re getting bad reviews for the exact same behavior that’s been rewarded pre-2022.

**None of this depends upon AI.** If LLMs had not taken off this decade, we would still be seeing the same cultural shifts in the industry. Companies would still be laying off engineers, and the engineers whose job has been to say no to things would still be upset and confused about why they’re now being punished for saying no.

### AI

Ironically, if ZIRP had not ended, this would be a glorious moment for the just-say-no engineers. LLMs would have thrown fuel on the “engineers running wild” problem that the just-say-no engineers were empowered to solve. Tech companies, unable to publicly or privately cast doubt on AI-assisted coding, would have relied *heavily* on these engineers to prevent the tsunami of AI code from swamping the entire company. They would have been paid even better and celebrated like kings.

Instead, LLMs are adding insult to injury for the just-say-no engineer. They’re forced to watch while other engineers merge AI-generated PRs that would previously have been blocked, and are told to use the tools themselves: to become the kind of engineer they’ve spent their entire careers battling against.

Worse still, the AI tooling mostly *works*. It’s not (yet) causing any kind of catastrophe. The code isn’t quite as clean, and it’s a bit less well-understood, but it’s good enough (particularly in a world where companies are trying lots of new things and abandoning the ones that fail). So the just-say-no engineer faces not just a threat to their livelihood, but to their entire self-identity: they have to either insist that the apocalypse is right around the corner, or accept that their technical role was contingent on a *really weird* economic environment in the tech industry.

### Pure and impure engineering

Will the just-say-no engineer go extinct? No. They don’t fit well into every single tech company anymore, but there are domains where they’re needed. In [*Pure and impure software engineering*](https://www.seangoedecke.com/pure-and-impure-engineering/) I drew a distinction between “pure” engineering, which has a well-scoped, largely technical goal (like building a compiler or a language runtime) and “impure engineering”, which has a poorly-scoped, largely customer-driven goal (like trying out a new feature you’re not sure will work). During the ZIRP era, tech companies did a lot more pure work (for instance, building [React](https://en.wikipedia.org/wiki/React_(software))), and tended to treat even impure work like pure work. The just-say-no engineer is *great* for pure work, because pure codebases have to have a much higher bar for quality and can tolerate slower development cycles.

Most tech companies are still doing some kind of pure work, typically in their core infrastructure pieces. This is essential work, but it doesn’t require a huge engineering team, and it’s rarely in [the spotlight](https://www.seangoedecke.com/the-spotlight/). If you’re a just-say-no engineer and you want to stay that way, I would recommend trying to move into one of these roles (and accepting that you’ll have a more limited scope than you did in the 2010s).

### Summary

edit: this post got some comments on [lobste.rs](https://lobste.rs/s/i2szle/just_say_no_engineer_was_zirp_phenomenon) and [Reddit](https://www.reddit.com/r/programming/comments/1thf964/the_justsayno_engineer_was_a_zirp_phenomenon/), including one of the [cruelest](https://lobste.rs/c/f3g1tn) comments I’ve ever read about my blog. A more concrete criticism was [about](https://lobste.rs/c/yoouec) [my](https://www.reddit.com/r/programming/comments/1thf964/comment/omnw6an/) off-hand remark that the models work: commenters felt it was too early to say, because the impact of bad code takes a while to manifest. Fair enough. “It’s too early to say” is never really *wrong*, though I think it’s clear that AI code is not immediately fatal. [Other](https://www.reddit.com/r/programming/comments/1thf964/comment/omn4990/) [commenters](https://lobste.rs/c/eluuto) argued that the just-say-no archetype existed for decades prior to ZIRP (e.g. Linus Torvalds). I agree with that, but I think the niche for this kind of engineer was artificially expanded by ZIRP, and now has contracted again. Finally, an [interesting comment](https://lobste.rs/c/bromgo) claiming that the just-say-no engineer had a niche because (a) people were using dynamic languages, and (b) observability/feature-flag-etc tooling was not yet mature.

I also want to share this quote from a reader, via email:

> …in a strange way your posts give me comfort that I’m not alone in some strange bubble where all of a sudden I’m the only one that’s somehow always wrong. I’m at somewhat of a crossroads as I either need to lower my standards and become the always say yes engineer to gain favour with managers again (which is in conflict with who I am) or move on and potentially risk landing at another company with the exact same setup.

edit: Another round of comments from [Hacker News](https://news.ycombinator.com/item?id=48289439), [with](https://news.ycombinator.com/item?id=48289749) [several](https://news.ycombinator.com/item?id=48289785) [commenters](https://news.ycombinator.com/item?id=48290371) [wishing](https://news.ycombinator.com/item?id=48289668) [I’d](https://news.ycombinator.com/item?id=48289953) provided more hard evidence for my theory. Unfortunately it doesn’t work like that - I’m writing from my own experience, which is just my tiny window into what the industry was like pre-and-post-ZIRP. Your mileage may (and often [does](https://news.ycombinator.com/item?id=48290017)) vary. It’s an interesting question how you might go about testing something like this. Maybe survey a few hundred senior+ engineers in 2010 and 2026, asking how many times a week they said “no” to something, and whether that “no” was overruled?

I do want to address comments like [this](https://news.ycombinator.com/item?id=48290126) and [this](https://news.ycombinator.com/item?id=48290499), which argue that saying no was essential both before and after ZIRP. Yes, but the difference (in my view) is: pre-ZIRP, *management* did not like saying no to engineers, but post-ZIRP they rapidly built that muscle, and so now no longer need a group of engineers saying no for them.

Here's a preview of a related post that shares tags with this one.