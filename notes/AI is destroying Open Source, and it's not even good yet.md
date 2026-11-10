---
title: "AI is destroying Open Source, and it's not even good yet"
url: https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/
clipped: 2026-06-17 01:44:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AI is destroying Open Source, and it's not even good yet](https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/)

## Digest Summary
- An Ars Technica article was retracted after an AI writer fabricated quotes from open‑source maintainer Scott Shambaugh, who had previously been harassed by an AI agent over a pull request.  
- Jeff Geerling reports that AI‑generated code (“AI slop”) is overwhelming open‑source projects: curl maintainer Daniel Stenberg saw bug‑bounty submissions drop from 15 % to 5 % useful reports, and contributors exhibit entitlement without providing fixes.  
- Over 300 of Geerling’s projects experience a rise in low‑quality AI PRs, prompting GitHub to add a feature that can disable pull requests entirely, threatening a core collaboration mechanism.  
- He notes that code‑generation models have plateaued; human reviewers lack the capacity to filter the volume, and delegating review to AI is not a viable solution.  
- Geerling warns against deploying unreviewed AI code in production systems and predicts that OpenClaw’s release and OpenAI’s hiring to “democratize agentic AI” will exacerbate the problem.  
- He likens current AI hype to past crypto/NFT bubbles, cites upcoming hardware shortages (e.g., HDD inventory sold out through 2026), and questions how many sectors AI will disrupt before accountability is enforced.

## Discussion Summary
Comments present a mixed view of LLMs in open‑source development. Many acknowledge that AI assistants accelerate personal coding, enable rapid fixes, and lower entry barriers, while stressing that generated code must be reviewed and tested before submission. A recurring concern is an influx of low‑quality or “AI‑slop” pull requests that increase maintainers’ workload and raise questions about mentorship, code quality, and security. Additional points include licensing and copyright implications, proposals for taxation or tooling to filter contributions, and optimism that improved practices could keep open source thriving.

---

## Full Article

Over the weekend Ars Technica [retracted an article](https://arstechnica.com/ai/2026/02/after-a-routine-code-rejection-an-ai-agent-published-a-hit-piece-on-someone-by-name/) because the AI a writer used [hallucinated quotes](https://bsky.app/profile/benjedwards.com/post/3mewgow6ch22p) from an open source library maintainer.

The irony here is the maintainer in question, Scott Shambaugh, was [harassed by someone's AI agent](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/) over not merging its AI slop code.

It's likely the bot was running through someone's local 'agentic AI' instance (likely using OpenClaw). The guy who built OpenClaw was just hired by OpenAI to "work on bringing agents to everyone." You'll have to forgive me if I'm not enthusastic about that.

Video
-----

This blog post is a lightly-edited transcript of the video I published to YouTube today. Scroll past the video embed if you're like me, and you'd rather read the text :)

Impacts on Open Source
----------------------

Last month, even before OpenClaw's release, curl maintainer Daniel Stenberg [dropped bug bounties](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/) because AI slop resulted in actual *useful* vulnerability reports going from 15% of all submissions down to 5%.

And that's not the worst of itâthe authors of these bug reports seem to have a more entitled attitude:

> These "helpers" try too hard to twist whatever they find into something horribly bad and a critical vulnerability, but they rarely actively contribute to actually improve curl. They can go to extreme efforts to argue and insist on their specific current finding, but not to write a fix or work with the team on improving curl long-term etc. I don't think we need more of that.

These agentic AI users don't care about curl. They don't care about Daniel or other open source maintainers. They just want to grab quick cash bounties using their private AI army.

I manage [over 300 open source projects](https://github.com/geerlingguy), and while many are more niche than curl or matplotlib, I've seen my own increase in AI slop PRs.

It's gotten *so* bad, GitHub added a feature to [disable Pull Requests entirely](https://github.blog/changelog/2026-02-13-new-repository-settings-for-configuring-pull-request-access/). Pull Requests are the fundamental thing that made GitHub popular. And now we'll see that feature closed off in more and more repos.

AI slop generation is getting easier, but it's not getting smarter. From what I've seen, models have [hit a plateau](https://er.educause.edu/articles/2025/9/an-ai-plateau) where code generation is *pretty good*...

But it's not improving like it did the past few years. The problem is the humans who *review* the codeâwho are responsible for the useful software that keeps our systems goingâdon't have infinite resources (unlike AI companies).

Some people suggest AI could take over code review too, but that's not the answer.

If you're running a personal weather dashboard or building a toy server for your Homelab, fine. But I wouldn't run my production appsâthat actually make money or could cause harm if they breakâon unreviewed AI code.

If this was a problem already, OpenClaw's release, and this hiring by OpenAI to democratize agentic AI further, will only make it worse. Right now the AI craze feels the same as the [crypto and NFT boom](https://uk.finance.yahoo.com/news/what-happened-to-nfts-094039263.html), with the same signs of insane behavior and reckless optimism.

The difference is there's more useful purposes for LLMs and machine learning, so scammers can point to those uses as they bring down everything good in the name of their AI god.

Since my video [The RAM Shortage Comes for Us All](https://www.youtube.com/watch?v=9rbz0akyLyQ) in December, we have *hard drives* as the next looming AI-related shortage, as [Western Digital just announced](https://www.tomshardware.com/pc-components/hdds/western-digital-is-already-sold-out-of-hard-drives-for-all-of-2026-chief-says-some-long-term-agreements-for-2027-and-2028-already-in-place) they're already sold through their inventory for 2026.

Some believe the AI bubble isn't a bubble, but those people are misguided, just like the AI that hallucinated the quotes in that Ars Technica article.

And they say ["this time it's different"](https://www.bogleheads.org/forum/viewtopic.php?t=375826), but it's not. The same signs are there from other crashes. The big question I have is, how many other things will AI companies destroy before they have to pay their dues.