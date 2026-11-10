---
title: "Incident March 30th, 2026 – Accidental CDN Caching"
url: https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching
clipped: 2026-06-17 01:25:00
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Incident March 30th, 2026 – Accidental CDN Caching](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching)

## Digest Summary
Railway experienced a CDN‑caching incident on 30 March 2026. Between 10:42 UTC and 11:34 UTC a configuration change unintentionally enabled caching for ~0.05 % of domains that had CDN disabled. During this 52‑minute window GET responses, including those containing authenticated data, were stored in edge caches and could be served to users other than the original requester. The issue was first detected at 11:14 UTC via internal monitoring and user reports; the change was reverted and all cached assets were purged globally at 11:34 UTC. Affected users will receive email notification. Railway has added automated tests for caching behavior, implemented staged CDN rollouts over hours, and committed to prioritizing safety over new feature development to prevent recurrence. The incident details are posted on Railway’s status page.

## Discussion Summary
Comments focus on the incident’s explanation, criticizing the blog post for omitting the root cause, using vague metrics, and containing contradictory statements about which data were exposed. Reviewers note that the status page provides clearer details, especially regarding cached content without cache‑control. While some express respect for Railway’s transparency and execution, others request insight into the QA or testing process that missed the issue and suggest unique session‑specific URLs as a mitigation. Overall, the discussion balances critique of communication with acknowledgement of the company’s openness.

---

## Full Article

🚄

Edits have been added to provide additional clarity as of 00:00 UTC, in addition to an update to the title for accuracy

Railway experienced an incident where CDN features were accidentally enabled for some domains without users enabling them.

For those affected, this may have resulted in potentially authenticated data being served to unauthenticated users.

[Impact
------](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching#impact)

On March 30, 2026 between 10:42 UTC and 11:34 UTC (52 minutes), a Railway engineer rolled out a change causing HTTP GET responses to be incorrectly cached across ~0.05% of domains on Railway with CDN disabled.

During this window, cached responses may have been served to users other than the original requester, which meant potentially authenticated data is served to unauthenticated users.

This meant that, your application may have served requests for one user to a different user.

As a result, for those applications serving on Railway, your users may have seen pages intended for *other* users.

We take this very seriously, and detail below what happened, how we’ve addressed it, and how we’re preventing it from happening in the future.

[Incident Timeline
-----------------](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching#incident-timeline)

**On March 30, 2026:**

* **10:42 UTC** - A Railway engineer deployed a configuration update to our CDN provider. This accidentally enabled caching for domains that had CDN turned off.
* **11:14 UTC -** First identification of a possible issue, based on internal information + user reports
* **11:34 UTC** - The change was fully reverted and all cached assets were purged globally.

The full incident is available on our Status Page [here](https://status.railway.com/incident/X0Q39H56).

[What Happened?
--------------](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching#what-happened)

A CDN (Content Delivery Network) caches your application's content at edge servers around the world so it can be served faster to users. On Railway, CDN caching is opt-in. Domains without CDN enabled will always route requests directly to your application.

During this incident, a configuration update to enable Surrogate Keys, allowing us to cache assets on a per domain basis, accidentally enabled caching on domains that had it disabled. As a result, responses — including authenticated ones — were stored and served from our edge cache instead of reaching your application directly.

Origin `Cache-Control` directives were respected where provided, and `Set-Cookie` response headers were not cached. However, most GET responses without explicit cache headers were cached by default during this window.

Users with domains affected by this incident will be notified via e-mail shortly.

[**Preventative Measures**
-------------------------](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching#preventative-measures)

We have already rolled out the following:

* Additional tests for correct/incorrect caching behaviors before changes are in production
* Aggressive shard-ing of CDN rollouts over hours as opposed to minutes

We are deeply sorry for this grave error on our part. We have already put mitigations in place to prevent it from happening again (see below), but we realize that incidents like this damage your trust in Railway, which is of paramount importance to us.

We have been working nonstop to keep up with the surge in growth we are experiencing, but will be prioritizing safety and security over new feature development to make sure we avoid similar issues in the future