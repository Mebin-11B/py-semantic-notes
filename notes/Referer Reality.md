---
title: "Referer Reality"
url: https://www.robinsloan.com/lab/referer/
clipped: 2026-06-17 01:03:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Referer Reality](https://www.robinsloan.com/lab/referer/)

## Digest Summary
Chris Morgan blocks URLs containing query strings, assuming the Referrer header suffices to identify traffic sources. In practice, most visitors arrive via links in email or mobile apps (e.g., Instagram, iOS Messages, Substack) that do not send Referrer headers, causing them to be classified as “Direct/Unknown.” To compensate, the author appends a custom query parameter (e.g., utm_source=Robin_Sloan_sent_me) to every outbound link, allowing destination sites to trace the origin of clicks—especially useful for e‑commerce platforms like Shopify. The author does not use analytics but views the parameter as a digital‑etiquette practice, enabling site operators to verify and follow up on traffic (illustrated by a planetarium confirming legitimate subscriptions). Some services, notably YouTube, reject unexpected query strings; the author maintains an exception list, now including chrismorgan.info.

## Discussion Summary
The commentary questions the rationale for voluntarily adding tracking parameters to external links, suggesting it primarily benefits other sites rather than the originator. It emphasizes that legitimate query parameters, such as those used for search, should be allowed while unexpected or malicious values be blocked early in the processing stack. The same caution extends to the Referer header, which is viewed as prone to spam and potentially unsafe content, indicating a general distrust of unfiltered inbound data.

---

## Full Article

May 10, 2026

Chris Morgan is [tired of people tacking query strings](https://chrismorgan.info/no-query-strings) onto his URLs — e.g. `www.robinsloan.com/lab/?like=this&and=this`—so he’s con­fig­ured his web­site to reject those requests outright, rather than suffer in silence.

Naturally, any­body is free to set up their server in any way they like … however, Chris writes this:

> If I wanted to know [where a vis­itor came from] I’d look at the Ref­erer header; and if it isn’t there, it’s prob­ably for a good reason.

which isn’t really true anymore. For most web­sites, the majority — not just the plurality, but the majority — of vis­itors arrive by fol­lowing a link inside an email or an app (e.g. Instagram, Mes­sages on iOS, the Sub­stack app), nei­ther of which set a `Ref­erer` header; so, all of those vis­itors are lumped into a vast slab called *Direct* or *Unknown*.

This broken mech­a­nism pro­vides the impetus for the custom query string I append to all out­going links, `utm_source=Robin_Sloan_sent_me`: under­standing that many/most clicks on links I share will come from my email newsletter, I want the source to be legible, par­tic­u­larly in con­texts such as, e.g., Shopify.

This isn’t an argu­ment that Chris Morgan should do any­thing different — opinionated oper­ator deci­sions make the internet go round — but rather an oppor­tu­nity for clar­i­fi­ca­tion about the cur­rent state of play.

I don’t col­lect or review ana­lytics of any kind on my web­sites, so I’m not a con­sumer of this kind of referral info. Even so, my custom query string is, in my calculation, an expres­sion of dig­ital etiquette: rather than dump a load of anony­mous traffic on your doorstep, I reveal who’s linking, so a web­site or online shop oper­ator can trace it back and get in touch, if wanted or needed. (Memorably, this was useful when the [Abrams Planetarium](https://abramsplanetarium.natsci.msu.edu/sky-calendar/index.aspx?utm_source=Robin_Sloan_sent_me) received a wave of new sub­scrip­tions and weren’t sure if they were legitimate; a brief email cor­re­spon­dence assured them that yes, these people were real … they were nerdy … they wanted the Sky Calendar!)

Note that a handful of sites do choke on unex­pected query strings, including YouTube (!), so I main­tain a list of exceptions, to which `chrismorgan.info` is now added.

[To the blog home page](https://www.robinsloan.com/lab/)