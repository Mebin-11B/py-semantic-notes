---
title: "Isseven"
url: https://isseven.app/
clipped: 2026-06-17 01:22:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - api design
  - microservices
  - satirical software
  - web development
related:
  - "[[API Design]]"
  - "[[Microservices]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Isseven is a humorous, commercialized API service designed solely to validate whether a given integer is equal to seven.
>
> **Key points:**
> - Exposes a POST endpoint `/api/isseven` that returns a Boolean indicating if the input number is 7.
> - Features tiered pricing models, including free limits, paid plans for higher concurrency, and promotional ad payloads.
> - Serves as a satirical take on the microservice pattern and over-engineering simple programmatic logic.
>
> **Concept links:** [[Api Design]], [[Microservices]], [[Satirical Software]], [[Web Development]]
>
> **Suggested connections:**
> - [[Satirical Software]] — mocking SaaS pricing structures and developer-centric API integrations.
> - [[Microservices]] — demonstrating the absurdity of decoupling trivial logical tasks into remote services.
<!-- ai-summary:end -->


# [Isseven](https://isseven.app/)

## Digest Summary
The page describes “isseven,” a web API that validates whether a submitted numeric value equals seven. Users send a POST request to /api/isseven with a JSON payload containing a field named number. The API returns a JSON response with a Boolean isseven field indicating the result and an ad field containing promotional text. Successful validation (value 7) yields {"isseven": true, ...}; any other value yields {"isseven": false, ...}. Three pricing tiers are offered:

* **Free** – 1 check per month, responses include ads, community support only.  
* **Pro** – $77 per month, unlimited checks, ad‑free responses, email support with a 72‑hour SLA, and a 77.7 % uptime SLA.  
* **Enterprise** – $777 per month, dedicated infrastructure, ad‑free responses, a dedicated engineer, and a “seven‑figure” SLA guarantee.

The service emphasizes minimal compromise: a single number, a single truth, and optional upgrades for ad‑free usage.

## Discussion Summary
The comments combine humor with substantive concerns, highlighting broken checkout flow, incorrect calculation results, and a perceived vulnerability to attacks. Several users request clearer enterprise uptime guarantees and additional capabilities such as an agent skill, while others note the product’s niche positioning relative to alternatives like Prolog. A few remarks acknowledge modest investments, such as domain costs, and express tentative optimism about enterprise prospects, but overall the feedback points to functional issues and security doubts that need addressing.

---

## Full Article

v7.7.7

isseven
=======

The only number validation API you'll ever need.

One number. One truth. Zero compromises.

// live demo

POST

POST /api/isseven

// response will appear here

// api documentation

POST /api/isseven

Send a JSON body with a `number` field.
Returns whether it is seven.

Response — 200 OK for 7 values

```
{
  "isseven": true,
  "ad": "Upgrade to isseven Pro for an ad-free experience!"
}
```

Response — 200 OK for non seven values

```
{
  "isseven": false,
  "ad": "isseven Pro: because your sevens deserve better."
}
```

// pricing

Free

$0/mo

* ✓ 7 checks/month
* ✓ Includes ads in response
* ✓ Community support (Stack Overflow)
* ✗ Ad-free responses

POPULAR

Pro

$77/mo

* ✓ Unlimited seven checks
* ✓ Ad-free responses
* ✓ Email support (72hr SLA)
* ✓ 77.77777% (seven seven's) uptime SLA

Enterprise

$777/mo

* ✓ Dedicated seven infrastructure
* ✓ Ad-free responses
* ✓ Dedicated Seven Engineer
* ✓ Seven-figure SLA guarantee