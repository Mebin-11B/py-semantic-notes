---
title: "15 Years of Forking"
url: https://www.waterfox.com/blog/15-years-of-forking/
clipped: 2026-06-17 01:25:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - Web Browser Development
  - Open Source Monetization
  - Ad Blocking
  - Independent Software
  - Data Privacy
  - Search Engine Partnerships
related:
  - '[[2026 will be my year of the Linux desktop]]'
  - '[[A website to destroy all websites]]'
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Waterfox celebrates 15 years as an independent, privacy-focused browser, introducing a native adblocker in 2026 to ensure financial sustainability while remaining free of AI bloat.
>
> **Key points:**
> - Waterfox has reached over 25 million downloads and maintains ~1 million monthly active users since its start as a 64-bit Firefox compile by a 16-year-old in 2009.
> - Relies on search-partner revenue (currently Startpage) and search text ads for financial sustainability after the termination of Bing's third-party contracts.
> - Incorporates a native adblocker using Brave's adblock-rust library (MPL2 licensed) running directly in the main browser process for improved speed.
> - Reaffirms its commitment to open-source independence, ARM64 architecture support, and a policy of no built-in AI tools.
>
> **Concept links:** [[Web Browser Development]], [[Open Source Monetization]], [[Ad Blocking]], [[Independent Software]], [[Data Privacy]], [[Search Engine Partnerships]]
>
> **Suggested connections:**
> - [[2026 will be my year of the Linux desktop]] — relates the demand for privacy-focused browsers to the broader trend of users switching to user-owned desktop systems like Linux.
> - [[A website to destroy all websites]] — connects browser engine behavior, ad-blocking, and extension standards to the user experience of the modern web.
<!-- ai-summary:end -->

# [15 Years of Forking](https://www.waterfox.com/blog/15-years-of-forking/)

## Digest Summary
Waterfox began in 2009 when a 16‑year‑old compiled a 64‑bit build of Firefox and released it on SourceForge, quickly reaching 50 k downloads. Over fifteen years it has accumulated roughly 1 million monthly active users and over 25 million lifetime downloads. The founder studied electronics engineering at York, earned a software‑engineering master’s at Oxford, and later served as VP of Engineering at System1, helping scale the browser team through an IPO before returning Waterfox to independent ownership under BrowserWorks.

Financially, the privacy‑focused browser relies on search‑partner revenue (currently Startpage); loss of third‑party search contracts has caused recent deficits. In 2026 Waterfox introduced a native content blocker built on Brave’s MPL‑2‑licensed ad‑block library (adblock‑rs), running in the main process for speed and integration, while allowing text ads on the default search page to support sustainability. The browser remains free of AI features, focuses on privacy, and expands support for varied architectures, notably ARM64 Linux. Membership in the Browser Choice Alliance underscores its commitment to market competition.

## Discussion Summary
The comments blend lighthearted appreciation for the juxtaposition of “15 Years of Forking” with “There is no Spoon” and curiosity about Waterfox, noting many have not encountered it before but find it intriguing. There is also a recurring theme of skepticism toward Waterfox’s decision to include text ads for sustainability, suggesting that while the rationale is acknowledged, some view it as a profit‑driven shift from original ideals. Overall, the tone mixes humor, interest, and cautious criticism of monetization choices.

---

## Full Article

Logo 2011-2014  Logo 2014-2015  Logo 2015-2019  Logo 2019  Logo 2019-2023  Logo Today

Fifteen years ago today, I posted [a thread on the Overclock.net forums](https://web.archive.org/web/20110402234032/http://www.overclock.net/other-software/975626-waterfox-firefox-4-64-bit-build.html). I was sixteen, I had an HP Compaq TC4400 that Iâd convinced my parents would âimprove my school workâ, and I was frustrated that Firefox didnât have an official 64-bit build. So I compiled one myself, called it Waterfox, stuck it on SourceForge and went back to my A levels.

Within a week it had 50,000 downloads, completely unexpected. Frustratingly, being on an island in the Mediterranean meant there was no support network or anyone to turn to with regards to âwhatâs nextâ. Had I been stateside, with the infrastructure and institutional knowledge of âtechâ, who knows - I mightâve had a guiding hand on how to manage something like this and work with the momentum. But alas, I would have to learn a lot of painful lessons myself.

Fast forward to today, 15 years later, and Waterfox is still here. So am I, albeit a bit older and significantly more tired. At best estimates, Waterfox probably has around 1M monthly active users.

Where it started
----------------

If you go and look at that [original OCN thread](https://web.archive.org/web/20110402234032/http://www.overclock.net/other-software/975626-waterfox-firefox-4-64-bit-build.html), itâs a very different world. People are talking about Silverlight support, MSVCR100.dll errors, and Peacekeeper benchmark scores. Someone asks for a 64-bit Chromium build and the thread title gets updated with every new Firefox version, all the way up to 56.0.2.

Originally, and under the username MrAlex, I was only trying to earn enough forum reputation so I could trade and buy second hand PC parts. I didnât have a plan and I certainly didnât have a business model. I just thought it was cool that you could take someone elseâs source code, compile it with some changes, and end up with something different. Open source is a wonderful thing when youâre sixteen and donât know anything about the software development lifecycle, yearning for ~~the mines~~ knowledge.

What happened in between
------------------------

You can scour the internet, read this blog or view the media carousel at the bottom for then until now, but the short version: Waterfox grew - a lot - over 25 million lifetime downloads, and that figure is from calculations about seven years ago so the real number is certainly higher. I went to university, studying Electronics Engineering at York before a masters in Software Engineering at Oxford. I tried to start a charitable search engine, which failed as badly run startups tend to do. Ecosia reached out and something nice happened - Waterfox users helped plant over 350,000 trees in a single year.

Then System1 came along. I joined them, served as VP of Engineering, and helped scale the browser engineering team through a NYSE IPO - a genuine education, though companies change and focus shifts.

So I took Waterfox back under BrowserWorks, independent once again. The three years since have been simultaneously the most difficult and the most rewarding of Waterfoxâs existence.

The hard bit
------------

Iâm not going to pretend the economics of running a privacy focused independent browser are great, because theyâre really not. When Bing terminated all third party search contracts it hit hard - search partnerships are basically how independent browsers survive, and revenue has been poor since. There have been a few months in the red recently.

Other ways browsers make money just feel icky, and itâs not something that Waterfox stands for either.

But, pain and all, I keep coming back. Every time I think about stepping away, someone sends a kind message through the donation page, or I see a thread somewhere of someone discovering Waterfox for the first time and being pleasantly surprised. Thereâs a community here that cares, and I care about it.

I want users to know that whatever future steps Iâll take, theyâll always be with Waterfox and its sustainability in mind.

What Waterfox is in 2026
------------------------

This year will see Waterfox shipping a native content blocker built on [Braveâs adblock](https://github.com/brave/adblock-rust) library - and itâs worth explaining what that means and why.

The blocker runs in the main browser process rather than as a web extension, which means it isnât subject to the limitations that extension based blockers like uBlock Origin face. Itâs faster, more tightly integrated, and doesnât depend on a separate extension process or require us to constantly pull in upstream updates. Braveâs adblock library is also mature - it has paid engineers working on it, a wide filterset, and crucially itâs licensed under MPL2, the same licence as Waterfox, which makes it a natural fit. uBlock Origin, as good as it is, carries a GPLv3 licence that wouldâve created real compatibility headaches.

For how it works in practice: by default, text ads will remain visible on our default search partnerâs page - currently Startpage. The idea is that this is what will keep the lights on. ~~This mirrors the approach Brave takes with their search partner.~~

**Update (28 March 2026):** Corrected a statement about Braveâs ad blocking behaviour. The original text implied Brave special cases ads on their search partnerâs page - they donât. Brave blocks *third party* ads on all websites by default, regardless of any partnership, and offers an additional aggressive mode that blocks *first party* ads as well. Waterfoxâs approach of allowing text ads on the default search partner page is our own decision for sustainability, not something inherited from `adblock-rs`. Thanks to Shivan at Brave for the correction.

Users who want to disable that entirely can do so with a single toggle in settings, and it has nothing to do with any of Braveâs crypto or rewards ecosystem - weâre just using the adblocking library. Everyone else gets a fast, native adblocker out of the box, no extension required.

If you already use an adblocker, donât worry, you can carry on using it. This will be enabled for new users or users who arenât already using an adblocker.

In the meanwhile, Waterfoxâs membership of the Browser Choice Alliance alongside Google and Opera, is pushing for fair competition and actual user choice in the browser market.

And we still donât have AI in the browser. [That hasnât changed](https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/). The browserâs job is to load web pages, keep your data private, and get out of the way. It seems other browsers have forgotten that.

Oh and one last thing - distribution is important too, so thereâs a bigger focus on different packages and architecture support (Linux, you are such a pain to target) - more specifically for ARM64.

Fifteen more?
-------------

Iâd like to think so. The browser market is more diverse than itâs ever been in terms of soft forks - everyone and their mum seems to be launching a variation of Firefox. Running an independent browser is getting harder, not easier. But there are more people who care about privacy now than there were when I was compiling a blue Firefox on a tablet PC in my bedroom. More people who want software that respects them.

Waterfox started because a sixteen year old wanted a faster browser. Fifteen years later, itâs still here because enough people want a browser that works for them - not for AI companies, and not for anyone else.

Thanks to everyone whoâs been part of this - from the OCN community who gave those early builds a chance, to the people who send donations with messages that make my day, to the contributors who submit patches and file bugs. This project has always been bigger than me, even when Iâm the only one working on it.

Hereâs to the next 15! ð»

A Special Shout Out
-------------------

I also wouldnât be where I am with the constant moral support of my parents, Angela & Lakis, who since day dot have been proud of everything Iâve done, even if itâs felt like I was failing and flailing. My friends, numerous to count, but especially Lee who Iâm surprised hasnât once told me to shut up about my trials and tribulations. And finally, my wonderful girlfriend and partner [Lucy](https://www.lucyafountain.com/) who has been giving helpful design tips because while I have wonderful taste (only half joking) my creative talent is unfortunately lacking.

Read the media coverage Waterfox has received over the last 15 years.