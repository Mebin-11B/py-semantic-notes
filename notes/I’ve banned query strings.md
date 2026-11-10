---
title: "I’ve banned query strings"
url: https://chrismorgan.info/no-query-strings
clipped: 2026-06-17 01:04:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - url parameters
  - web tracking
  - user privacy
  - server configuration
  - protocol constraints
related:
  - "[[User Privacy]]"
  - "[[Server Configuration]]"
  - "[[Web Tracking]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The author configured their Caddyfile to block all unauthorized query parameters to protect user privacy and mitigate tracking via URLs.
>
> **Key points:**
> - Query parameters like `ref` and `utm_source` are criticized as invasive tracking mechanisms that compromise user privacy.
> - The author relies on HTTP headers (e.g., Referer) for referral data, asserting that missing headers should be respected.
> - Enforcement is done via server-level routing (Caddyfile), blocking non-whitelisted queries and letting those requests fail or return error codes.
>
> **Concept links:** [[Url Parameters]], [[Web Tracking]], [[User Privacy]], [[Server Configuration]], [[Protocol Constraints]]
>
> **Suggested connections:**
> - [[User Privacy]] — technical measures to prevent user profiling and tracking.
> - [[Server Configuration]] — using tools like Caddy to enforce traffic rules.
> - [[Web Tracking]] — how marketers and analytics tools gather data via URLs.
<!-- ai-summary:end -->

# [I’ve banned query strings](https://chrismorgan.info/no-query-strings)

## Digest Summary
The author bans all unauthorised query strings on their site, citing concerns that query parameters are often used for tracking (e.g., ref, utm_source) and can abuse users. They argue that referral information should be obtained from the Referer header, and if absent it is likely intentional. Historically they used query strings for cache‑busting CSS files (e.g., ?t=…, &h=…) but now consider any such usage unnecessary and are willing to let those requests fail. If future functionality requires query parameters, only explicitly approved ones will be allowed. The restriction is enforced via a rule in the server’s Caddyfile configuration, which blocks any request containing a query string unless it matches a predefined whitelist. The post invites readers to test the behaviour by appending query strings to URLs.

## Discussion Summary
Comments reflect a split view on unsolicited query strings. Many acknowledge that query strings are a standard, percent‑encoded part of URLs useful for tracking, state sharing, and internal routing, and that servers can safely ignore unknown parameters. Others criticize adding tracking parameters without consent, citing privacy concerns, broken links, excessively long URLs, and unnecessary server errors such as 404 or 414 responses. While some advocate strict rejection of unexpected queries, a significant portion argues for tolerant handling or graceful redirects, emphasizing that robust sites should not fail when extra parameters appear. Overall sentiment balances practical utility against perceived misuse and user inconvenience.

---

## Full Article

I’ve banned query strings
=========================

🗓️ 2026-05-08 • Tagged [/url](https://chrismorgan.info/url "URL"), [/web](https://chrismorgan.info/web "Web"), [/opinions](https://chrismorgan.info/opinions "Opinions (that I hold)"), [/meta=only](https://chrismorgan.info/meta%3Donly "Meta only (things about this site that are unlikely to be generally applicable)")

I don’t like people adding tracking stuff to URLs.   
Still less do I like people adding tracking stuff to *my* URLs.

https://chrismorgan.info/no-query-strings?ref=example.com? Did I ask?   
If I wanted to know I’d look at the `Referer` header; and if it isn’t there, it’s probably for a good reason.   
You abuse your users by adding that to the link.

https://chrismorgan.info/no-query-strings?utm\_source=example&utm\_*&c.*?   
Hey! That one’s even worse, [UTM parameters](https://en.wikipedia.org/wiki/UTM_parameters) are for *me* to use, not *you*.   
Leave my URLs alone.

So I’ve decided to try a blanket ban for this site: **no unauthorised query strings**.

At present I don’t use any query strings.   
If I ever start using any query strings, I’ll allow only known parameters.   
(In past times I used ?t=… and ?h=… cache-busting URLs for stylesheet URLs;   
and I decided I’m okay breaking such requests; there shouldn’t be any legitimate ones.)

Want to see what happens if you add a query string[?](https://chrismorgan.info/no-query-strings?) Go ahead, try it.

It’s my website: I can do what I want with it.

And you can do what you want with yours!

*This is currently implemented [in my Caddyfile](https://chrismorgan.info/Caddyfile#?).* 

Aside: this page’s URL
----------------------

It was *very* tempting to publish this at https://chrismorgan.info/? (path «», query ).

This would have broken a lot of common but incorrect assumptions, and made some tools cry:   
`curl`, for example, seems to illegitimately strip a trailing question mark   
(could be only for the command line, didn’t test library usage).

In the end, I decided to respect the notion of path and have mercy on people.   
Myself most of all; I’m already pushing Caddy in enough directions it’s not happy with.

My next plan was to publish it at /%3F (path «?», query null),   
but I guess no one has ever tried doing such stupid things with Caddy before;   
[if `try_files` rewriting is involved it can’t cope](https://github.com/caddyserver/caddy/issues/7678 "Caddy issue #7678: try_files mangles paths containing characters like ? and % (whereas file_server without the rewrite works properly)").

So /no-query-strings will do.   
I’ll probably use /? or /%3F later for something *else* about query strings.