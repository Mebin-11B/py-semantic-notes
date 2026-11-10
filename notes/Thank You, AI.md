---
title: "Thank You, AI"
url: https://www.kraxel.org/blog/2026/01/thank-you-ai/
clipped: 2026-06-17 01:46:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Thank You, AI](https://www.kraxel.org/blog/2026/01/thank-you-ai/)

## Digest Summary
The author discontinued a self‑hosted Git service that had been running publicly since 2011 (previously a CVS server). Increased traffic from AI scrapers overwhelmed the cgit web frontend, generating large numbers of useless requests and filling disk space with log data despite Apache handling the 404 responses. After fixing dangling links to point to mirrors on major git‑hosting platforms (GitLab, GitHub), the author retained only a self‑hosted web server for the blog and a few static sites, which were migrated to Jekyll in 2018. This static setup resists scraper overload, though a recent scraper‑induced outage still occurred due to rapid log growth; the issue was mitigated by adjusting logrotate configuration. The post marks the end of the author’s self‑hosted repository hosting.

## Discussion Summary
The discussion questions the attribution of recent web‑scraping activity to AI, suggesting the observed bots appear poorly engineered and more likely the work of conventional actors rather than sophisticated LLM‑driven tools. It notes that typical scraper behavior—high error rates and aggressive request patterns—remains unchanged, and asks for concrete logs or analyses to verify the AI claim. The comment also points out that standard mitigation services such as Cloudflare could effectively block the activity, implying the issue may be overstated.

---

## Full Article

Ok, it is over. End of an era for me. No more self-hosted git. I
had a public git server running since 2011, and a public cvs server
before that. AI scrapers have hammered the poor, little server to
death by flooding the cgit frontend with tons of pointless²
requests. Actually a few months ago already.

Now I finally decided to not try rebuild the server, be it with or
without cgit web frontend. I don't feel like taking up the fight
with the scrapers in my spare time, I leave that to people who are
in a better position to do so. Most repositories had mirrors on one
or two of the large gitforges already. Those are the primary
repositories now. Go look
at [gitlab](https://gitlab.com/users/kraxel/projects)
and [github](https://github.com/kraxel?tab=repositories).

Last week I've fixed all (I hope) dangeling links to the cgit
repsitories to point to the forges instead.

Now I'm down to one self-hosted service, which is the webserver
hosting mainly this blog and a few more little things. In 2018 I've
migrated the blog from wordpress to jekyll, so it is all static
pages. Taking this out by AI scrapers overloading the machine should
be next to impossible, and so far this has hold up.

Nevertheless AI scrapers already managed to trigger one outage.
Apparently millions of 404 answers where not enough to convince the
bots that there is no cgit service (any more). Apache had no
problems to deliver those, but the logs have filled up the disk so
fast that logrotate didn't manage to keep things under control with
the default configuration. Fixed config. Knook wood.

---

¹ Title inspired by
the [2025
edition of Security Nightmares](https://media.ccc.de/v/39c3-security-nightmares). Fun watching if you speak
german.
  
² Most inefficient way to get the complete repo. Just clone it, ok?