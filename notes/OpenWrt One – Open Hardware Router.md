---
title: "OpenWrt One – Open Hardware Router"
url: https://openwrt.org/toh/openwrt/one
clipped: 2026-08-31 12:22:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [OpenWrt One – Open Hardware Router](https://openwrt.org/toh/openwrt/one)

## Digest Summary
Anubis is a server‑side protection mechanism that presents a Proof‑of‑Work (PoW) challenge, similar to Hashcash, to deter large‑scale AI‑driven web scrapers. The PoW adds negligible overhead for individual users but becomes costly when many requests are generated, thereby raising the expense of automated scraping. The system serves as a temporary measure while developers focus on more refined fingerprinting techniques—such as detecting headless browsers through font‑rendering anomalies—to reduce reliance on PoW challenges for legitimate visitors. Anubis requires modern JavaScript; extensions that block or modify JavaScript (e.g., JShelter) must be disabled for the site to function correctly. The overall goal is to protect website resources from excessive automated access without significantly impacting normal user experience.

---

## Full Article

# Testing to determine if you are a bot!

 

Loading...

You are seeing this because the administrator of this website has set up Anubis to protect the server against the scourge of AI companies aggressively scraping websites. This can and does cause downtime for the websites, which makes their resources inaccessible for everyone.

Anubis is a compromise. Anubis uses a Proof-of-Work scheme in the vein of Hashcash, a proposed proof-of-work scheme for reducing email spam. The idea is that at individual scales the additional load is ignorable, but at mass scraper levels it adds up and makes scraping much more expensive.

Ultimately, this is a placeholder solution so that more time can be spent on fingerprinting and identifying headless browsers (EG: via how they do font rendering) so that the challenge proof of work page doesn't need to be presented to users that are much more likely to be legitimate.

Please note that Anubis requires the use of modern JavaScript features that plugins like JShelter will disable. Please disable JShelter or other such plugins for this domain.
