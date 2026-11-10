---
title: "AI code and software craft"
url: https://alexwennerberg.com/blog/2026-01-25-slop.html
clipped: 2026-06-17 01:52:41
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AI code and software craft](https://alexwennerberg.com/blog/2026-01-25-slop.html)

## Digest Summary
The essay argues that AI has amplified the production of low‑quality, metric‑driven content by reducing the effort required to generate “good enough” output. Drawing on Jacques Ellul’s notion of “technique,” it describes how platforms prioritize engagement and revenue over craft, citing Spotify’s algorithmic playlists versus Bandcamp’s album‑focused model as an example. In software, large‑tech firms are portrayed as “plumbing” operations that produce bloated, poorly designed systems, with engineers confined to narrow, rote tasks. AI agents can automate such repetitive work, but they lack understanding, often generate verbose or buggy code, and cannot replace the broader skill set and critical thinking required for high‑quality software. The author calls for a revival of craftsmanship in computing, referencing the Arts and Crafts movement and suggesting exploration of historic programming paradigms (e.g., Forth, Unix). While AI may increase mass‑produced software, it could also free space for human‑centric, experimental projects that emphasize genuine engineering craft.

## Discussion Summary
Comments portray AI coding tools as practical for routine tasks like boilerplate and glue code, while noting persistent weaknesses in system‑level reasoning, security, and edge‑case handling. Opinions diverge between those who view the technology as a productivity enhancer that reshapes engineering roles and those who fear it erodes craftsmanship and deep judgment. Skepticism also extends to broader societal impacts, including job displacement and political ramifications. Overall, the consensus acknowledges AI’s utility but stresses the need for careful integration, quality oversight, and awareness of its limits.

---

## Full Article

AI code and software craft
==========================

Jan 25 2026

*Update (Feb 17, 2026) — I no longer agree with many statements made in this blog post. I am leaving it here unmodified. See my follow-up: [AI can sort of code, can't write](https://alexwennerberg.com/blog/2026-03-31-craft2.html).*

Much has been said about audio, video and text "slop": low-quality,
AI-generated content that has proliferated on the internet since the release of
publicly-accessible AI models. Garbage content has always existed online, but
the novelty of AI is that it has made its generation orders of magnitude less labor-intensive.
For anyone who lacks a discerning eye, or is doing some task where discernment simply
does not matter, AI has become a sufficient replacement for human hands.

Jacques Ellul describes his concept of "technique" as the reduction of
activity to a set of efficient means to a measured and defined end — a
way of thinking dominant in modernity. *Technique* is the regime under which
many things are produced online: an Instagram reel, YouTube
video, blog post, and so on is "good" if it elicits as much "engagement" as
possible with as little effort as possible. This is *technique* as
a totalizing force, destroying any sense of craft, dignity, or human
freedom. It doesn't really matter what is being made, the purpose of the
endeavor is how much its creation is viewed, how much revenue it generates.
Obsession with metrics and outcomes erodes anything intangible about a creative effort,
like craft, beauty, or delight.

Taking music as an example, through the lens of *technique*, music is
"good" if it gets a lot of "plays". One can compare, for example, the operating
models of Bandcamp and Spotify, both of which have platform dynamics and a set
of values that have led to the production of certain kinds of music. For
Bandcamp, its focus on full albums and personal curation contributed to the
indie music boom of the 2010s/2020s and uplifted artists like Car Seat Headrest,
Mitski, Alex G, Phoebe Bridgers,
and others. For Spotify, its playlist and algorithmic recommendation based
model has spawned a wave of [bland,
algorithmically-targeted muzak](https://www.theguardian.com/commentisfree/2025/mar/09/spotify-algorithm-artists-music-musicians-money-songs-playlists). This is because Spotify's model doesn't
care about music, it cares about metrics: music is simply a means to
optimizing certain outputs. It is in this environment where AI is most successful — a nihilistic space of pure optimization. When craft is not a consideration, AI can produce a large volume of "good enough" content that has a much higher "profit maximization" function than actually human-produced music. On the other hand, for a platform whose primary goal is, well, music, AI is actively hostile, to the point that Bandcamp has [banned
it](https://blog.bandcamp.com/2026/01/13/keeping-bandcamp-human/).

A similar dynamic is taking place in the world of software. Even before the advent of AI, a lot of software was extremely low-quality. People have said that software engineering at large
tech companies resembles "plumbing" — connecting various systems
together in order to get data to flow between them. Any sense of what Richard
Hamming would call "[great
work](https://worrydream.com/HammingForeword/)", where engineers produce "gifts to humanity" seems absurdly high-minded in the context of the
tech industry as constituted today. Most large software systems are bad: bloated, poorly-designed,
badly-documented, and so on. Users are at war with platforms, lest they be taken advantage in the process of [enshittification](https://en.wikipedia.org/wiki/Enshittification). I essentially agree with Jonathan Blow's
characterization in his talk [Preventing the Collapse of
[Software] Civilization](https://www.youtube.com/watch?v=ZSRHeXYDLko) — more than anything, professional engineers and large software companies
have *forgotten how to do things*. In an environment largely insulated from market pressures by
[non-competitive monopolies](https://scholarship.law.columbia.edu/books/63/), software practices have become shoddy, organizations have
become bloated, and quality has suffered greatly as a result.
Engineers in Big Tech tend to have an extremely narrow role within a large
organization, and broader engineering skills (much less a sense of craft, which largely is not rewarded) atrophy.

A business, or society's, capacity to do things with computers depends on its
human capital, i.e., cultivating broadly-skilled and talented engineers. The
extreme division of labor and narrowness of tasks in large tech companies leads
to a production of relatively narrowly skilled people, i.e., people who are only
really capable of operating within big tech companies as they are structured today.

This has led to two separate phenomena. First, the very real sense that AI
agents are threatening to professional software engineering. This may be true
to some degree: for engineers whose roles have become rote and narrow
production of low-quality software (ie, many employees at large tech companies),
AI is actually quite good at this. But the second phenomenon is the celebration
and generalization of the broader capabilities of AI agents, the idea that AI can do "[most,
maybe all](https://moguldom.com/464672/ai-could-do-most-maybe-all-coding-within-6-12-months-warns-anthropic-ceo/)" of software engineering, or that AI is "[like a compiler](https://www.infoworld.com/article/4096265/writing-code-is-so-over.html)" that translates human language into code.

This being true requires an extreme narrowness of vision as to what software
is, much like AI generated music requires a narrowness of vision of what music
is. It requires software merely to be a means to an end, an endeavor where the
only thing that matters is that something is "good enough" given the
institutional contexts in which it is being created, where there is no place
for higher-minded ideals. I've experimented a lot with AI agents lately[1](https://alexwennerberg.com/blog/2026-01-25-slop.html#fn1), and they are
undeniably useful, but there are serious limits. They will lie to you, they
don't really understand things, and they often generate bad code. There are
many things they've improved at, and I do expect them to get better in some
domains, but much like with music, text, or anything else, there are
fundamental limitations. AI agents do not have a mind of their own, and they
cannot read your mind. They work best when you give them some well-defined
prompt for an already often-solved problem like "write some unit tests" or
"write a db function like this". But attempts to generalize their capabilities have
[largely failed](https://lucumr.pocoo.org/2026/1/18/agent-psychosis/) and produced code that is novel and impressive [only in its monstrosity](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Furthermore, after being initially impressed by "vibe coding," I started to
get frustrated with its tics. It produces verbose code in a braindead style.
Its designs are flat and ugly, and I have begun to notice and find unpleasant
its tells[2](https://alexwennerberg.com/blog/2026-01-25-slop.html#fn2). When things go wrong, I'm generally
coding in such a mindless state, watching a YouTube video or scrolling Instagram, that
debugging is a frustrating loop of repeatedly telling agents "no, there's a
bug, please fix it."

It is true that most code simply is not very good, especially at large
companies. And we can continue to do not very good software much more quickly
and effectively with AI. But AI cannot solve the main systemic problem in the
software industry, which is that, in my view, we still haven't quite figured
out how to build software well at scale. But to do this requires a sense of craft and real human critical thought.

I've been interested lately in the [Arts and
Crafts](https://en.wikipedia.org/wiki/Arts_and_Crafts_movement) movement of the second industrial revolution. John Ruskin and
William Morris were responding to a time when the capabilities of machines and
industrial production were extremely impressive, and increasingly replacing the
individual craftsman. They did not celebrate this, rather, they viewed
industrial production as having a particular *style* in both its goods
and its impact on workers, who had become cogs in a
monstrous industrial machine. They correctly noted that there were things that
machines could not do (and still can't do), and looked backwards towards a
revival of medieval craftsmanship for inspiration.

In my view, we need a similar movement in software, studying and restoring
earlier forms of computing. There is a whole treasure trove of ideas that never
really went anywhere, and software projects that are impressive and beautiful
in a way that today's software is often not. We find ourselves on a very narrow
branch of a tree of technological development (from C/Unix to Javascript/The
Web) and there is a lot more out there to explore[3](https://alexwennerberg.com/blog/2026-01-25-slop.html#fn3). Once you're doing something even somewhat
non-conventional, you'll find yourself almost entirely discarding AI. I tried
to get Claude to help me write Forth, and it was worse than useless.

AI code may make garbage,
mass-produced software more ubiquitous, but it may also free up a space for
engineers seeking to restore a genuine sense of craft and creative expression
in their programming work. I am not pessimistic here; as craft becomes
more scarce, it also becomes more valuable. As mainstream
software continues to demonstrate its limits, software continues to degrade, and [political concerns](https://european-alternatives.eu/categories) lead people to question the value of centralization, it is a great moment for experimental, human-made and human-scale software on the margins to shine.

[Discuss on Hacker News](https://news.ycombinator.com/item?id=46769188)

---

1 If you think I am anti-AI, I consider myself much more of an "AI centrist", and speaking to some people, even the admission that I use and pay for these models is morally compromising. My critical position, is, in my view, more moderate. [â©](https://alexwennerberg.com/blog/2026-01-25-slop.html#fnref1)

2 Overly-padded buttons, inconsistent spacing and coloring, an aesthetic flatness, UI elements of questionable utility, and a tendency to unnecessarily [label and describe everything](https://x.com/reactjpg/status/1415542684744249344). [â©](https://alexwennerberg.com/blog/2026-01-25-slop.html#fnref2)

3 I recommend the [Permacomputing](https://permacomputing.net/) Wiki to get started. [â©](https://alexwennerberg.com/blog/2026-01-25-slop.html#fnref3)