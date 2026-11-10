---
title: "Your ePub Is fine"
url: https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/
clipped: 2026-06-17 00:47:20
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - E-books
  - CSS Standards
  - Adobe RMSDK
  - Software Compatibility
  - Validation Tools
related:
  - "[[E-books]]"
  - "[[CSS Standards]]"
  - "[[Adobe RMSDK]]"
  - "[[Software Compatibility]]"
  - "[[Validation Tools]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A Kobo e-reader bug reveals how outdated Adobe RMSDK rendering engines fail to parse modern CSS functions, crashing ePub files that otherwise pass validation.
>
> **Key points:**
> - Although an ePub ebook passed epubcheck 3.3, it crashed Kobo devices running the Adobe-derived RMSDK engine.
> - The failure was traced to a CSS Level 4 `min()` function in the stylesheet, which the outdated RMSDK CSS parser (frozen around 2013) could not parse.
> - RMSDK does not support modern CSS features like flexbox, grid, or custom properties, and fails silently when encountering unsupported syntax.
> - Developers cannot rely solely on standard ePub validation tools to ensure cross-device compatibility.
>
> **Concept links:** [[E-books]], [[CSS Standards]], [[Adobe RMSDK]], [[Software Compatibility]], [[Validation Tools]]
>
> **Suggested connections:**
> - [[E-books]] — challenges of developing ebooks for heterogeneous e-reader hardware.
> - [[CSS Standards]] — how legacy web view engines in devices lag behind modern web standards.
<!-- ai-summary:end -->

# [Your ePub Is fine](https://andreklein.net/your-epub-is-fine-kobo-disagrees-blame-adobe/)

## Digest Summary
The author’s new ebook passes epubcheck 3.3 and works on Kindle, Apple Books, and Thorium, but Kobo devices report it as “corrupted.” Investigation revealed that Kobo’s rendering engine (RMSDK), derived from Adobe Digital Editions, uses an outdated CSS parser frozen around 2013. A CSS rule in the book’s stylesheet—`.copyright img { max‑width: min(150px, 30vw); }`—employs the CSS Level 4 `min()` function, which RMSDK cannot parse. When the stylesheet is disabled the book loads; replacing the rule with `max-width: 150px;` resolves the issue. RMSDK lacks support for modern CSS features (flexbox, grid, custom properties) and silently drops the book without error messages. epubcheck validates only against the EPUB specification and performs limited CSS checks; it cannot predict renderer‑specific failures. Consequently, relying solely on epubcheck is insufficient for Kobo compatibility; testing on Adobe’s engine or avoiding newer CSS syntax is necessary.

## Discussion Summary
The comments convey widespread frustration with Adobe’s DRM ecosystem, citing inaccessible SDKs, unresponsive support, and anticompetitive practices that hinder indie development. Contributors describe RMSDK’s outdated CSS handling and unreliable validation tools, leading to frequent crashes and compatibility headaches across e‑readers. Many criticize the fragmented ePub standards and urge simpler, backward‑compatible formatting, while noting that alternative devices and open‑source readers like Kobo’s beta, KoReader, and BOOX offer more viable solutions. Some users prefer PDFs or minimalist text formats to avoid these systemic issues.

---

## Full Article

