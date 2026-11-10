---

title: "288,493 Requests – How I Spotted an XML-RPC Brute Force from a Weird Cache Ratio"
url: https://marcindudek.dev/blog/xmlrpc-brute-force-cache-rate/
clipped: 2026-06-17 01:16:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - web security
  - cache hit ratio
  - brute force attack
  - web application firewall
  - wordpress optimization
related:
  - "[[Web Security]]"
  - "[[Cache Hit Ratio]]"
  - "[[Brute Force Attack]]"
  - "[[Web Application Firewall]]"
  - "[[WordPress Optimization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The author explains how a drop in Cloudflare cache hit ratio led to detecting and mitigating a massive XML-RPC brute force attack targeting a WordPress site.
>
> **Key points:**
> - A sudden drop in Cloudflare cache hit ratio (down to 0.8%) served as a primary signal of uncacheable malicious traffic.
> - The attack used WordPress's `xmlrpc.php` and the `system.multicall` method to pack hundreds of credential login attempts into a single POST request.
> - XML-RPC brute force attacks are highly stealthy because they bypass naive rate limits and do not trigger traditional uptime monitors.
> - Defense-in-depth mitigation involves blocking `/xmlrpc.php` at the CDN edge (Cloudflare WAF) and disabling XML-RPC within WordPress plugins or themes.
>
> **Concept links:** [[Web Security]], [[Cache Hit Ratio]], [[Brute Force Attack]], [[Web Application Firewall]], [[WordPress Optimization]]
>
> **Suggested connections:**
> - [[Web Security]] — on credentials validation and rate limiting.
> - [[Web Application Firewall]] — how blocking requests at the edge saves server resources.
> - [[WordPress Optimization]] — regarding the removal of legacy endpoints like XML-RPC.
<!-- ai-summary:end -->

# [288,493 Requests – How I Spotted an XML-RPC Brute Force from a Weird Cache Ratio](https://marcindudek.dev/blog/xmlrpc-brute-force-cache-rate/)

## Digest Summary
Cloudflare analytics showed a cache‑hit ratio of 0.8 % on a mostly static WordPress site, revealing a flood of uncacheable traffic. One Singapore‑based DigitalOcean IP sent 288 493 POST requests to /xmlrpc.php within 24 hours, using the system.multicall method to embed hundreds of credential pairs per request and brute‑force WordPress logins. Because /xmlrpc.php is always dynamic, each request drove the cache‑rate down, serving as a clear indicator of abuse.  

Detection: query Cloudflare’s GraphQL analytics (or use the dashboard) for top paths; a high‑count, dynamic /xmlrpc.php entry signals an attack.  

Mitigation:  
- Deploy a Cloudflare WAF rule `http.request.uri.path eq "/xmlrpc.php"` to block at the edge, eliminating origin CPU load.  
- Disable XML‑RPC in WordPress (e.g., `add_filter('xmlrpc_enabled', '__return_false');` or via WP Multitool’s Frontend Optimizer, enabled by default in v1.1.19).  

Recommendations: monitor cache‑hit ratios, review top paths weekly, pre‑emptively block /xmlrpc.php, and rely on the REST API instead of XML‑RPC unless required (e.g., Jetpack mobile). This layered approach restores normal cache performance and prevents similar brute‑force floods.

## Discussion Summary
The comments express strong dissatisfaction with the article’s AI‑generated style, describing it as excessively verbose, repetitive, and difficult to read. Readers find the phrasing irritating and the repeated points unnecessary, leading to a sense of nausea. The content is viewed as lacking value beyond niche WordPress advice, and the criticism extends to questioning the effectiveness of Cloudflare in mitigating basic brute‑force attacks. Overall sentiment is markedly negative toward both the writing quality and practical usefulness.

---

## Full Article

TL;DR

* Cloudflare cache hit ratio on a WordPress site dropped to 0.8% — the real alarm, not CPU or uptime.
* Root cause: a single Singapore DigitalOcean IP flooding `/xmlrpc.php` with 288,493 POSTs in 24 hours, using `system.multicall` to brute-force hundreds of credentials per request.
* Fix: Cloudflare WAF rule blocking `/xmlrpc.php` at the edge, plus WP Multitool's Frontend Optimizer disabling xmlrpc inside WordPress — defense in depth, both layers on by default in 1.1.19.
* Action for you: check your Cloudflare Top Paths weekly. If `xmlrpc.php` shows up in the top 3, you're already being hit.

Today I was glancing at Cloudflare analytics for one of my sites and something looked off. Cache hit ratio: **0.8%**. That's not a typo. Zero point eight percent.

For a mostly-static WordPress site that should be sitting at 70–90%, 0.8% means something is very wrong. Either the cache rules are broken, or something is flooding the site with uncacheable traffic. Turned out to be the second one.

I pulled up the traffic breakdown and the answer was sitting right there. One IP from Singapore, **288,493 requests in 24 hours**, all POSTs to `/xmlrpc.php`, all returning 200. That's about 12,000 requests per hour from a single DigitalOcean droplet. The site was still up because Cloudflare was absorbing most of it, but my origin was burning CPU on every single one of those requests.

Why 0.8% Cache Rate Was the Real Signal
---------------------------------------

Here's the thing about WordPress attacks on `xmlrpc.php` — they're almost invisible if you only watch uptime. The site loads fine for real visitors. The CPU graph might look a bit elevated. But the attack itself doesn't trigger any obvious alarm.

Cache rate is a great canary because `xmlrpc.php` is POST-only and marked dynamic. Every attack request counts against your cache rate denominator. When you see 288k uncacheable dynamic requests vs a few thousand normal cached ones, the ratio collapses.

So if your cache rate suddenly drops on an otherwise quiet WordPress site, don't immediately blame your plugins. Check what's being requested.

What system.multicall Actually Does
-----------------------------------

The vector is old but still works because so many sites leave xmlrpc enabled by default. Attackers POST XML payloads like this:

```
<?xml version='1.0'?>
<methodCall>
  <methodName>system.multicall</methodName>
  <params>
    <param><value><array><data>
      <value><struct>
        <member><name>methodName</name><value>wp.getUsersBlogs</value></member>
        <member><name>params</name><value><array><data>
          <value><string>admin</string></value>
          <value><string>password1</string></value>
        </data></array></value></member>
      </struct></value>
      ... [hundreds more credential pairs]
    </data></array></value></param>
  </params>
</methodCall>
```

One HTTP request, hundreds of login attempts. **That's the amplification.** A regular `wp-login.php` brute force triggers rate limiting and WAF rules after a few attempts. `system.multicall` lets you test 500 credentials in a single POST that looks like normal API traffic. That's why it's still the preferred vector in 2026 — efficient, quiet, and slips past naive rate limits that count requests instead of auth attempts.

How to Check If You're Being Hit
--------------------------------

If you're on Cloudflare, the fastest way is the GraphQL analytics API. Query the top paths for the last 24 hours, grouped by path and cache status:

```
query($zone:String!, $since:Time!, $until:Time!) {
  viewer {
    zones(filter:{zoneTag:$zone}) {
      httpRequestsAdaptiveGroups(
        limit:20,
        filter:{datetime_geq:$since, datetime_leq:$until},
        orderBy:[count_DESC]
      ) {
        count
        dimensions { clientIP clientCountryName clientRequestPath cacheStatus }
      }
    }
  }
}
```

If `/xmlrpc.php` shows up in the top 3 paths with `cacheStatus` "dynamic" and a request count in the tens of thousands, you're being hit. Also check `wp-login.php` while you're there — where there's xmlrpc abuse there's usually a coordinated login flood from other IPs.

If you don't use the API, the Cloudflare dashboard has the same data under Analytics → Traffic. The Top Paths widget will give it away.

Fix #1 — Block It at the Edge
-----------------------------

The fastest mitigation is a Cloudflare WAF custom rule. One line expression, block action:

```
(http.request.uri.path eq "/xmlrpc.php")
```

This stops the requests at Cloudflare's edge before they reach your origin. No CPU cost, no PHP execution, no bandwidth. After I deployed this rule the 288k/day flood stopped hitting my server entirely and the cache rate started recovering within the hour.

If you have dozens of zones to protect, the Cloudflare API makes this a one-liner per zone. I ran it on all my own zones in about 10 seconds.

Fix #2 — Disable It at the WordPress Level Too
----------------------------------------------

Edge blocks are great but I'm a defense-in-depth person. If someone misconfigures the WAF or bypasses Cloudflare, I want WordPress itself to refuse xmlrpc requests.

You can do it with a few lines in `functions.php`:

```
add_filter('xmlrpc_enabled', '__return_false');
add_filter('xmlrpc_methods', function($methods) { return []; });
```

Or if you'd rather not touch code, any decent WordPress optimizer plugin has this option. My own plugin [WP Multitool](https://wpmultitool.com/) has it in the Frontend Optimizer module and it's on by default in the latest version — which is why I updated all my sites to 1.1.19 after spotting this attack. Install, activate, done — xmlrpc is disabled both ways.

The key insight: don't rely on a single layer. Edge WAF rules can be misconfigured, origin can be exposed directly, and plugins can be deactivated. Stack them so no single failure leaves you open.

Do You Actually Need xmlrpc in 2026?
------------------------------------

Probably not. `xmlrpc.php` was the WordPress API before REST existed. These days:

* The WordPress REST API handles everything xmlrpc used to do, better and with proper auth
* Remote publishing apps have mostly moved to REST
* Even WooCommerce and major page builders don't touch xmlrpc

The one remaining legit use case is the Jetpack mobile app, which still uses xmlrpc under the hood for some features. If you don't use Jetpack mobile, you can kill xmlrpc without losing anything. If you do, there are better ways — restrict xmlrpc to Jetpack's IP ranges via WAF rule instead of blocking outright.

In my case none of my sites need it, so I blocked it everywhere.

What I'd Do Going Forward
-------------------------

A few habits I'm adding after this:

**Watch cache rate, not just uptime.** A 5% drop in hit ratio on a static-ish site deserves a look. A 50% drop means something is happening right now.

**Check top paths weekly.** Five seconds in the Cloudflare dashboard, tells you immediately if an attack is warming up. Most brute force attempts start small and ramp up over days.

**Block `xmlrpc.php` preemptively on new sites.** It's one WAF rule. There's no reason to wait until you see 288k requests before adding it.

And if you're running WordPress anywhere without a CDN or WAF in front of it, fix that first. Cloudflare's free tier would have absorbed this entire attack without breaking a sweat.

The cache rate on my site is back to normal now. But I'm genuinely curious how many WordPress owners are getting hit right now and have no idea because they only check if the homepage loads.

If you run WordPress sites and want xmlrpc hardening (plus a bunch of other defense-in-depth optimizations) on by default, [WP Multitool 1.1.19+](https://wpmultitool.com/) handles it automatically.