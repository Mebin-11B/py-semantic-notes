---
title: "2,100 Swiss municipalities showing which provider handles their official email"
url: https://mxmap.ch/
clipped: 2026-06-17 01:15:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - digital sovereignty
  - CLOUD Act
  - email infrastructure
  - DNS analysis
  - open data
  - Swiss tech ecosystem
related:
  - "[[Swiss AI Initiative (2023)]]"
  - "[[Digital Sovereignty]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The mxmap.ch project maps the email providers for Switzerland's 2,100 municipalities by analyzing public DNS signals, highlighting issues of digital sovereignty and exposure to the US CLOUD Act.
>
> **Key points:**
> - Analyzes municipal domain DNS records, SMTP banners, and ASN mappings to determine which email services handle official Swiss municipal mail.
> - Highlights digital sovereignty concerns: US-based providers (like Microsoft and Google) are subject to the US CLOUD Act, allowing US law enforcement to demand access to data hosted abroad.
> - Releases both the collection script codebase and the raw municipal classification data as open-source on GitHub.
> - Hacker News discussion focuses on the diversity of non-hyperscaler hosting providers in Switzerland and debates the necessity or challenges of creating a unified national cloud hosting solution for municipal governments.
>
> **Concept links:** [[Digital Sovereignty]], [[CLOUD Act]], [[Email Infrastructure]], [[DNS Analysis]], [[Open Data]], [[Swiss Tech Ecosystem]], [[Cloud Geopolitics]]
>
> **Suggested connections:**
> - [[Swiss AI Initiative (2023)]] — exploring how Switzerland approaches digital sovereignty, infrastructure autonomy, and independent technology initiatives.
> - [[Digital Sovereignty]] — detailing the geopolitical tensions and legislative measures (like the US CLOUD Act) impacting municipal and government infrastructure choices.
<!-- ai-summary:end -->

# [2,100 Swiss municipalities showing which provider handles their official email](https://mxmap.ch/)

## Digest Summary
A map visualizes the email service provider for roughly 2,100 Swiss municipalities by analyzing each municipality’s official domain. The classification uses eleven public signals—including DNS records, SMTP banners, ASN lookups, and a Microsoft API endpoint—to identify the handling provider and assign a confidence score. The project highlights digital‑sovereignty concerns, noting that US‑based providers fall under the US CLOUD Act, which can compel data disclosure irrespective of physical storage location. Results are grouped by jurisdiction, showing the distribution of providers across municipalities. The underlying code and the compiled dataset are released as open‑source on GitHub, with a mechanism for users to report inaccuracies via issue submission. A disclaimer clarifies that DNS information reflects mail routing and authorized senders, not the actual data‑hosting location.

## Discussion Summary
The comments express a reflective and appreciative tone toward the breadth of the global internet, noting satisfaction that it isn’t dominated solely by major providers like Google and Microsoft. They highlight the existence of numerous regional domain maps and question how specific locales end up using particular hosting services. There is curiosity about the lack of a unified national hosting solution that could simplify municipal decisions, suggesting interest in more centralized options.

---

## Full Article

### What is this?

A map of all ~2,100 Swiss municipalities, grouped by jurisdiction. Each is colored by the provider handling its official email, based on public DNS records and other public network signals.

### Context

US-based providers are subject to the US CLOUD Act, allowing US authorities to request stored data regardless of where it is hosted. This map makes the current provider landscape visible.

### How does it work?

Each municipality's email domain is checked against multiple public DNS and network signals, then classified by provider type.

### Accuracy

Classifications may contain errors. DNS records indicate mail routing, not necessarily where data is stored.   
If you notice an error, please [submit an issue](https://github.com/davidhuser/mxmap/issues).

### Open source & open data

The code and data are on [GitHub](https://github.com/davidhuser/mxmap).