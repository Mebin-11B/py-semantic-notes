---
title: "Google broke reCAPTCHA for de-googled Android users"
url: https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users
clipped: 2026-06-17 01:05:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Google broke reCAPTCHA for de-googled Android users](https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users)

## Digest Summary
Google’s next‑generation reCAPTCHA is now tied to Google Play Services (version 25.41.30 or higher) on Android. When reCAPTCHA flags activity as suspicious, it replaces image puzzles with a QR‑code scan that requires Play Services to run in the background and communicate with Google’s servers. Devices without Google’s proprietary framework—such as GrapheneOS or other de‑Googled ROMs—cannot complete the verification and are blocked. The requirement was announced as part of Google Cloud Fraud Defense at Cloud Next on 23 April and has been documented in an Internet Archive snapshot from October 2025, indicating a rollout of at least seven months before being reported by a Reddit de‑Google community and covered by PiunikaWeb and Android Authority. iOS devices (iOS 16.4+) perform the same verification without additional apps, highlighting an asymmetry that ties Android web access to Google’s ecosystem. Web developers using this reCAPTCHA should note that implementation effectively excludes users of de‑Googled Android phones.

## Discussion Summary
The comments convey strong criticism of the new reCAPTCHA implementation, viewing it as a privacy‑invasive device‑attestation system that can link user accounts, enforce de‑facto KYC, and marginalize devices without Google Play services. Users express frustration over blocked access, increased reliance on Google’s infrastructure, and perceived monopolistic and anti‑competitive behavior, while calling for alternative anti‑bot solutions or regulatory action. Several contributors report personal workarounds or migration to self‑hosted services, but the dominant view is that the change threatens anonymity and broad web accessibility.

---

## Full Article

Google has tied its next-generation reCAPTCHA system to Google Play Services on Android, meaning anyone running a [de-Googled phone](https://reclaimthenet.org/the-deal-that-could-change-de-googled-phones-forever) will automatically fail verification when the system decides to challenge them.

The requirement forces Android users to run Google’s proprietary app framework version 25.41.30 or higher just to prove they’re human.

When reCAPTCHA flags what it considers suspicious activity, it abandons the old image puzzles and demands you scan a QR code. That scan requires Play Services running in the background, communicating with Google’s servers. If you’re using GrapheneOS or any other custom ROM that strips out Google’s software, the verification fails.

Google announced the broader system, Google Cloud Fraud Defense, at Cloud Next on April 23, pitching it as a trust platform designed to handle autonomous AI agents and traditional bots alike. What Google didn’t emphasize was the part where proving you’re human now requires submitting to its proprietary surveillance.

This wasn’t sudden, either. An Internet Archive snapshot from October 2025 shows the same [support page](https://support.google.com/recaptcha/answer/16609652?hl=en) already listing a Play Services requirement at version 25.39.30. Google built this dependency quietly for at least seven months before a Reddit user on the degoogle subreddit flagged it, with reporting from [PiunikaWeb](https://piunikaweb.com/2026/05/07/google-recaptcha-play-services-requirement/) and Android Authority bringing wider attention.

![Troubleshoot reCAPTCHA mobile verification instructions with QR code on left and "Click to Verify" button on right.](https://media.reclaimthenet.org/2026/05/0MVBtltU3vpy.jpg)

The iOS comparison is revealing because Apple devices running iOS 16.4 or later complete the same verification without installing any additional apps. Google didn’t demand iPhone users install Google software to pass the test. Only Android users who refuse Play Services get locked out. The asymmetry reveals what this is really about: not security, but ecosystem control.

reCAPTCHA sits in front of millions of websites. When Google ties verification to Play Services, it establishes a precedent where accessing basic web content requires running Google’s software and transmitting data to Google’s servers.

People running de-Googled phones chose those setups because they read the data practices, understood what Play Services phones home about, and decided they didn’t consent. Google’s new system punishes that decision by treating the absence of its proprietary software as suspicious by default.

Web developers adopting this reCAPTCHA should understand what they’re choosing. Every site that implements it tells de-Googled Android users they’re not welcome. That’s a small audience today. It’s also the audience most likely to care about how a website treats their data, and the least likely to capitulate.