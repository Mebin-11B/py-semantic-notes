---
title: "Show HN: Wikipedia as a doomscrollable social media feed"
url: https://xikipedia.org
clipped: 2026-06-17 01:49:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Progressive Web Apps
  - Client-side Algorithms
  - Recommender Systems
  - Wikipedia
  - Web Performance
  - Browser Limitations
related:
  - "[[Open Chaos A self-evolving open-source project]]"
  - "[[Show HN Twitch Roulette – Find live streamers who need views the most]]"
  - "[[CLI agents make self-hosting on a home server easier and fun]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Xikipedia is an offline-capable web application that presents Simple Wikipedia articles as a doomscrollable social media feed, using a basic client-side recommendation algorithm to learn user preferences locally.
>
> **Key points:**
> - Xikipedia mimics a social media feed interface to display articles sourced from Simple Wikipedia.
> - It employs a simple, local, non-machine-learning recommendation algorithm that infers user interests purely from device interactions without sending data to servers.
> - The app is designed to function fully offline as a Progressive Web App (PWA) once loaded.
> - The developer highlights platform limitations on iOS, criticizing Apple's memory constraints and browser engine restrictions.
> - User feedback focuses on initial load performance issues, suggesting lazy loading and incremental database fetching to optimize the web experience.
>
> **Concept links:** [[Progressive Web Apps]], [[Client-side Algorithms]], [[Recommender Systems]], [[Wikipedia]], [[Web Performance]], [[Browser Limitations]]
>
> **Suggested connections:**
> - [[Open Chaos A self-evolving open-source project]] — Another experimental web-based community project.
> - [[Show HN Twitch Roulette – Find live streamers who need views the most]] — Another Show HN web prototype focusing on random content discovery.
> - [[CLI agents make self-hosting on a home server easier and fun]] — Relates to offline-first and self-hosted tools.
<!-- ai-summary:end -->

# [Show HN: Wikipedia as a doomscrollable social media feed](https://xikipedia.org)

## Digest Summary
Xikipedia is a prototype social‑media feed that presents content sourced from Simple Wikipedia. It uses a basic, non‑machine‑learning algorithm that runs locally in the browser to infer a user’s interests from their interactions and then recommends similar articles. No user data is transmitted, stored, or shared; all processing occurs client‑side and data is cleared when the page is refreshed or closed. The project’s source code is publicly available on GitHub, with discussion channels on federated platforms such as fedi, Bluesky, and Twitter. Users may select predefined categories or add custom ones to seed the feed. Because the underlying articles are drawn randomly, the interface can display adult‑oriented (NSFW) material, and users are warned to proceed only if they are of legal age.

## Discussion Summary
Comments highlight slow loading times, large initial data transfer, and frequent page refreshes, leading to frustration. Suggestions include lazy loading and incremental fetching. The concept is recognized as interesting, with calls for ranking to surface higher‑quality articles. Several remarks criticize the relevance of doom‑scrolling framing and question the value of Wikipedia content, while a few note age‑appropriateness concerns. Overall reception blends appreciation for originality with strong performance and content concerns.

---

## Full Article

Loading...

[![](https://xikipedia.org/favicon.ico)](https://xikipedia.org)
Profiles
Stats
Settings
Install

**Xikipedia** is a pseudo social media feed that algorithmically shows you content from [Simple Wikipedia](https://simple.wikipedia.org/). It is made as a demonstration of how even a basic non-ML algorithm with no data from other users can quickly learn what you engage with to suggest you more similar content. The algorithm runs locally and no data leaves your device.

Once Xikipedia has loaded, it is available fully offline, and you can even install it as an app by clicking the install button.

Source code on [GitHub](https://github.com/rebane2001/xikipedia), discuss on [fedi](https://infosec.exchange/@rebane2001/115998023365214091), [bluesky](https://bsky.app/profile/rebane2001.bsky.social/post/3mdtj5cc7pk2b), or [twitter](https://twitter.com/rebane2001/status/2018107789512474738).

Note to iOS users: Apple arbitrarily limits the amount of memory a site can use, which means it's possible this site will crash before the loading finishes. I have no way to test for this myself as my iPhone does not do that. If this happens to you, try opening the site in desktop mode and see if that helps. If it still crashes, you'll just have to use this site from a different device. Blame Apple for creating undebuggable web platform issues while not letting you use an alternative browser engine on a device you supposedly own.

Pick some categories to get started (optional)

Or add your own

Since the content and images shown is from random Wikipedia articles, you will likely see NSFW content. Please only continue if you're an adult.

I'm an adult, continue

Profiles
--------

X

Warning! You have disabled the "Store data" setting in settings, no data will get saved to your profiles until you turn the setting back on.



Statistics
----------

X

Top categories
Bottom categories
Liked posts


Settings
--------

X

Store data

Whether to store your algorithm data locally (the data still never leaves your device). If this is turned off, your feed will start from scratch every time.

Open links in English Wikipedia

The articles are pulled from Simple English Wikipedia, but you can choose to still open them in (non-Simple) English Wikipedia.

Theme
Auto
Light
Dark
About Xikipedia
Reset the algorithm
Delete all data


About Xikipedia
---------------

X

**Xikipedia** is a pseudo social media feed that algorithmically shows you content from [Simple Wikipedia](https://simple.wikipedia.org/). It is made as a demonstration of how even a basic non-ML algorithm with no data from other users can quickly learn what you engage with to suggest you more similar content. The algorithm runs locally and no data leaves your device.

  

Once Xikipedia has loaded, it is available fully offline, and you can even install it as an app by clicking the install button.

  

Source code on [GitHub](https://github.com/rebane2001/xikipedia), discuss on [fedi](https://infosec.exchange/@rebane2001/115998023365214091), [bluesky](https://bsky.app/profile/rebane2001.bsky.social/post/3mdtj5cc7pk2b), or [twitter](https://twitter.com/rebane2001/status/2018107789512474738).