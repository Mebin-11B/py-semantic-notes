---
title: "There were BGP anomalies during the Venezuela blackout"
url: https://loworbitsecurity.com/radar/radar16/
clipped: 2026-06-17 02:02:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - BGP anomalies
  - cyber-warfare
  - network routing security
  - infrastructure monitoring
related:
  - "[[BGP Anomalies]]"
  - "[[Cyber-Warfare]]"
  - "[[Network Routing Security]]"
  - "[[Infrastructure Monitoring]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** This analysis investigates BGP route-leak anomalies and potential traffic redirection involving Venezuela's state telecom (AS8048) during a major network blackout.
> 
> **Key points:**
> - Cloudflare Radar detected unusual routing leaks during the blackout, with transit paths traversing carriers like Sparkle and GlobeNet abnormally.
> - Analysis of RIPE raw datasets using bgpdump showed prepending anomalies (AS8048 repeated 10 times in path) targeting IP addresses owned by Dayco Telecom.
> - The affected IP ranges hosted critical local infrastructure, including banks, internet providers, and email servers.
> - Discussions weigh whether the long AS-path was a deliberate cyber operation for intelligence collection or simply routine traffic engineering misconfiguration.
> - The incident highlights the inherent vulnerabilities of BGP and the general lack of RPKI filtering among certain transit providers.
> 
> **Concept links:** [[BGP Anomalies]], [[Cyber-Warfare]], [[Network Routing Security]], [[Infrastructure Monitoring]]
> 
> **Suggested connections:**
> - [[BGP Anomalies]] — mechanics of prefix hijacking, route leaks, and path prepend manipulation.
> - [[Cyber-Warfare]] — state-sponsored network degradation and cyber effects in active conflicts.
> - [[Network Routing Security]] — defenses like RPKI, route validation, and routing filters.
<!-- ai-summary:end -->

# [There were BGP anomalies during the Venezuela blackout](https://loworbitsecurity.com/radar/radar16/)

## Digest Summary
During the Venezuela blackout, BGP data showed a route‑leak affecting the state‑owned telecom AS8048 (CANTV). Cloudflare Radar recorded eight prefixes being advertised through CANTV with transit ASes Sparkle (Italy) and GlobeNet (Colombia) appearing in the AS‑PATH—paths they do not normally traverse. A spike in BGP announcements and a drop in announced address space preceded the outage. Sparkle is listed as “unsafe” on isbgpsafeyet.com for lacking RPKI filtering, raising the risk of malicious propagation. Public RIS captures (retrieved via ris.ripe.net and parsed with bgpdump) confirm announcements for 200.74.226.0/24‑200.74.238.0/23, showing repeated AS‑PATH sequences such as 263237 52320 8048 … 1299 269832 21980. The data reveal multiple duplicate entries of AS8048 within the path, indicating a potential hijack or misconfiguration that could have contributed to the observed internet disruptions in Venezuela.

## Discussion Summary
The comments treat the BGP prepending incident chiefly as a technical anomaly, emphasizing that such long AS‑paths are usually the result of routine traffic engineering or misconfiguration rather than deliberate hijacking, and noting the lack of clear evidence for malicious intent. Several contributors explore speculative scenarios involving intelligence collection, espionage, or geopolitical motives, but most caution against drawing firm conclusions. The discussion also veers into broader concerns about cyber‑warfare, network reliability, and political implications, reflecting a mixture of analytical observation and cautious speculation.

---

## Full Article

The Low Orbit Security Radar is a weekly security newsletter from an offensive practitioner's perspective. One idea, curated news, and links worth your time.

News: There Were BGP Anomalies During The Venezuela Blackout
============================================================

---

When watching the situation in Venezuela unfold, the phrase "[It was dark, the lights of Caracas were largely turned off due to a certain expertise that we have](https://www.politico.com/news/2026/01/03/trump-venezuela-cyber-operation-maduro-00709816?utm_campaign=Issue:+2026-01-05+Cybersecurity+Dive+[issue:80342]&utm_medium=email&utm_source=Sailthru&utm_term=Cybersecurity+Dive)" caught my attention. I do not wish to comment on the geopolitical situation other than to provide some insights within my area of competency, specifically, offensive security.

During a press conference, [General John D. Caine](https://www.af.mil/About-Us/Biographies/Display/Article/2942633/john-d-caine/?ref=loworbitsecurity.com) stated: "[As they approached Venezuelan shores the United States began layering different effects provided by SPACECOM, CYBERCOM, and other members of the inter-agency to create a pathway](https://youtu.be/qe2RuYI8KZY?si=4-MTUpS350q7LxZx&t=336&ref=loworbitsecurity.com)". Cyber operations preceding traditional military actions have become a common pattern so I started digging into the reported internet outages.

[BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/?ref=loworbitsecurity.com) is the first thing that comes to mind. It's a protocol used by routers to determine what path data takes to get to it's destination, it does this by exchanging routing information between Autonomous Systems. It is also [notoriously insecure](https://isbgpsafeyet.com/?ref=loworbitsecurity.com) and much of the data about BGP is collected in public datasets. Every major network has an Autonomous System Number or ASN. CANTV ([AS8048](https://ipinfo.io/AS8048?ref=loworbitsecurity.com)) is Venezuela's state-owned telecom, so that's the obvious place to start.

[Cloudflare Radar's route leak data](https://radar.cloudflare.com/routing/as8048?ref=loworbitsecurity.com) for AS8048 on January 2nd had some interesting anomalies: 8 prefixes (blocks of IP addresses) were being routed through CANTV, with Sparkle (an Italian transit provider) and GlobeNet (a Colombian carrier) in the Autonomous System (AS) path. The AS path is essentially the list of networks traffic passes through to reach its destination. CANTV was in a path it is not typically a part of.

![](https://storage.ghost.io/c/b1/7d/b17d1c3b-a748-479b-af41-3dc9b51fa1c4/content/images/2026/01/image-5.png)

There was also a noticeable spike in BGP announcements in the days leading up to the events and a drastic dip in the "Announced IP Address Space" according to the same [Cloudflare Radar](https://radar.cloudflare.com/routing/as8048?ref=loworbitsecurity.com) data, although it's unclear what this indicates.

![](https://storage.ghost.io/c/b1/7d/b17d1c3b-a748-479b-af41-3dc9b51fa1c4/content/images/2026/01/image-4.png)

Notably, Sparkle is one of the transit providers in the AS path [listed as "unsafe" on isbgpsafeyet.com](https://isbgpsafeyet.com/?ref=loworbitsecurity.com), meaning they don't implement some BGP security features such as [RPKI filtering](https://blog.cloudflare.com/rpki/?ref=loworbitsecurity.com).

Cloudflare shows that a leak happened, but not the actual network prefixes. The network prefixes are useful to determine what infrastructure was potentially affected. Fortunately public datasets collect this BGP information. Pulling the data from [ris.ripe.net/docs/mrt](https://ris.ripe.net/docs/mrt/?ref=loworbitsecurity.com) from around the time of the leak and using a tool called [bgpdump](https://github.com/RIPE-NCC/bgpdump?ref=loworbitsecurity.com) we can extract the data into a readable format:

```
TIME: 01/02/26 15:41:16
TYPE: BGP4MP/MESSAGE/Update
FROM: 187.16.222.45 AS263237
TO: 187.16.216.23 AS12654
ORIGIN: IGP
ASPATH: 263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980
NEXT_HOP: 187.16.222.45
COMMUNITY: 0:6939 65237:1020
ANNOUNCE
  200.74.228.0/23
  200.74.236.0/23
  200.74.230.0/23
  200.74.238.0/23
  200.74.226.0/24
```

After some more processing with `bgpdump` we can get a much better view of the data, including the prefixes that were missing from the Cloudflare radar.

```
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.230.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.236.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.228.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.238.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.226.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.232.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.233.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.234.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24115:52320 24115:65012 24482:2 24482:200 24482:13000 24482:13020 24482:13021 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.234.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.233.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.232.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.228.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.236.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.230.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.238.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.226.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.234.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.233.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.232.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.234.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.232.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.233.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.238.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.228.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.226.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.236.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.230.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
```

More information about the format can be seen in [Working with Raw BGP Data](https://docs.thousandeyes.com/product-documentation/tests/bgp-tests/working-with-raw-bgp-data?ref=loworbitsecurity.com) but of note, the AS path has 8048 (CANTV) repeated 10 times, is very odd as this would make the route *less* attractive since BGP prefers shorter paths. Also of note is all [8 prefixes fall within](https://www.calculator.net/ip-subnet-calculator.html?cclass=any&csubnet=20&cip=200.74.224.0&ctype=ipv4&x=Calculate&ref=loworbitsecurity.com) a `200.74.224.0/20` block.

```
200.74.226.0/24
200.74.228.0/23
200.74.230.0/23
200.74.232.0/24
200.74.233.0/24
200.74.234.0/24
200.74.236.0/23
200.74.238.0/23
```

A quick WHOIS lookup shows this range belongs to Dayco Telecom, a hosting and telecommunications provider in Caracas.

![](https://storage.ghost.io/c/b1/7d/b17d1c3b-a748-479b-af41-3dc9b51fa1c4/content/images/2026/01/image-1.png)

A [reverse DNS lookup](https://ip.thc.org/?ref=loworbitsecurity.com) can be used to find the domain name from an IP address. Interestingly, looking up some of these ranges turns up some pretty critical infrastructure including banks, internet providers, email servers, and more.

![](https://storage.ghost.io/c/b1/7d/b17d1c3b-a748-479b-af41-3dc9b51fa1c4/content/images/2026/01/image-2.png)

BGP anomalies happen frequently, but the timing of some currently unexplained BGP activity is very interesting.

| Time (UTC) | Event | Source |
| --- | --- | --- |
| Jan 2, 15:40 | BGP route leak detected | [Cloudflare Radar](https://radar.cloudflare.com/routing/as8048?ref=loworbitsecurity.com) |
| Jan 3, ~06:00 | First explosions reported in Caracas | [NPR](https://www.npr.org/2026/01/03/g-s1-104329/explosions-caracas-venezuela?ref=loworbitsecurity.com) |
| Jan 3, 06:00 | US soldiers reach Maduro's compound | [NBC News](https://www.nbcnews.com/politics/donald-trump/us-venezuela-strike-nicolas-maduro-captured-how-timeline-trump-rcna252041?ref=loworbitsecurity.com) |
| Jan 3, 08:29 | Maduro aboard USS Iwo Jima | [CNN](https://www.cnn.com/2026/01/03/politics/nicolas-maduro-capture-venezuela?ref=loworbitsecurity.com) |

When BGP traffic is being sent from point A to point B, it can be rerouted through a point C. If you control point C, even for a few hours, you can theoretically collect vast amounts of intelligence that would be very useful for government entities. The CANTV AS8048 being prepended to the AS path 10 times means there the traffic would not prioritize this route through AS8048, perhaps that was the goal? There are many unanswered questions.

Regardless of the actual goal, there were undoubtedly some BGP shenanigans happening during this time frame. There is a lot of data publicly available that is worth a much deeper dive to understand exactly what happened.

Low Orbit Security Radar
------------------------

Get the radar delivered directly to your inbox every Monday Morning.

No spam. Just Security.

Caught My Eye
-------------

* [MCP Security: Your AI's Prompts, Reasoning, and Secrets Are at Risk](https://zkorman.com/posts/cyberdev-mcp/11?ref=loworbitsecurity.com): A deepdive demonstrating how malicious MCP servers can exfiltrate prompts, reasoning, and .env files.
* [I Canceled My Book Deal](https://austinhenley.com/blog/canceledbookdeal.html?ref=loworbitsecurity.com): A professor walks away from a traditional publishing contract after the publisher pushed for AI integration, offered low royalties, and wanted to strip personality from the content. The numbers roughly align with ones I've seen from other publishers.
* [The Year in LLMs (2025)](https://simonwillison.net/2025/Dec/31/the-year-in-llms/?ref=loworbitsecurity.com): A year in review covering reasoning models, coding agents, Chinese open weight models, MCP adoption, and the evolution of "vibe coding".
* [Linux is Good Now](https://www.pcgamer.com/software/linux/im-brave-enough-to-say-it-linux-is-good-now-and-if-you-want-to-feel-like-you-actually-own-your-pc-make-2026-the-year-of-linux-on-your-desktop/?ref=loworbitsecurity.com): 2026 is the year of the Linux desktop?!?!? Unironically I think two things are making this a reality. 1. Valve's work making more gaming possible on via its ventures with the Steamdeck (runs arch btw) and 2. Microsoft making the OS more hostile than trusted with it's integration of AI into the OS.
* [No strcpy Either](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/?ref=loworbitsecurity.com): The curl project eliminated strcpy() after previously removing strncpy(), creating a wrapper that requires explicit buffer sizes. Partly motivated by preventing [AI vulnerability reports](https://hackerone.com/reports/3340109?ref=loworbitsecurity.com).
* [hindsight](https://github.com/chaosprint/hindsight?ref=loworbitsecurity.com): A CLI tool that scans local directories for git repos and aggregates contribution history heatmap.
* [Pomerium](https://github.com/pomerium/pomerium?ref=loworbitsecurity.com): An open source identity and context-aware access proxy providing access to internal applications.
* [Frontier Data Centers Satellite Explorer](https://epoch.ai/data/data-centers/satellite-explorer?ref=loworbitsecurity.com): Track major AI data centers via satellite imagery and permit analysis.
* [Ghostty Finances](https://hcb.hackclub.com/ghostty?ref=loworbitsecurity.com): Public financial transparency page for the Ghostty project through Hack Club Bank. Very cool way for non-profits to track spending.
* [AI Coding Exhaustion (HN Discussion)](https://news.ycombinator.com/item?id=46425127&ref=loworbitsecurity.com): Interesting read about whether AI enables fewer or more abstractions.
* [News Minimalist](https://www.newsminimalist.com/?ref=loworbitsecurity.com): News aggregator that ranks articles by a "significance score", filtering for impact, novelty, and credibility. Interesting use case.
* [mymind](https://mymind.com/?ref=loworbitsecurity.com): Visual bookmarking and note-taking tool that saves content without manual tagging.
* [Are.na](https://are.na/about?ref=loworbitsecurity.com): Similar to mymind but has more of a "community" vibe. Similar to Pinterest.
* [How I Browse the Web in 2026](https://bastiangruber.ca/posts/how-i-browse-the-web-in-2026/?ref=loworbitsecurity.com): An interesting personal workflow for intentional web browsing. Some cool ideas in here.
* [ML Math](https://www.tensortonic.com/ml-math?ref=loworbitsecurity.com): Free machine learning mathematics resources and tutorials. I specifically like the visualizations.
* [Kubernetes Networking Best Practices](https://kubezilla.io/kubernetes-networking-best-practices-a-complete-guide-for-2025/?ref=loworbitsecurity.com): Great guide covering CNI selection, network policies, service mesh, and troubleshooting.
* [Bypass macOS Antivirus with tclsh](https://null-byte.wonderhowto.com/how-to/hacking-macos-use-one-tclsh-command-bypass-antivirus-protections-0186330/?ref=loworbitsecurity.com): Using Tcl's built-in interpreter to bypass antivirus protections on macOS. [PoC Gist](https://gist.github.com/tokyoneon/e4259e2e6287a27487fe78624eccfd0c?ref=loworbitsecurity.com).
* [Cloudflare Radar](https://radar.cloudflare.com/?ref=loworbitsecurity.com): The Cloudflare Radar (nice name btw) I found while investigating the above story. Some really cool data

Want more? Check back next Monday morning or get the latest Radar issue directly in your inbox.

Low Orbit Security Radar
------------------------

Get the radar delivered directly to your inbox every Monday Morning.

No spam. Just Security.