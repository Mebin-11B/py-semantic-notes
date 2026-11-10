---
title: "MeshCore development team splits over trademark dispute and AI-generated code"
url: https://blog.meshcore.io/2026/04/23/the-split
clipped: 2026-06-17 01:13:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [MeshCore development team splits over trademark dispute and AI-generated code](https://blog.meshcore.io/2026/04/23/the-split)

## Digest Summary
The MeshCore team has released over 85 firmware versions for more than 75 hardware variants since its launch in January 2025. A dispute arose when a team member, Andy Kirby, extensively used AI‑generated code (Claude) to rewrite core components and secretly applied for the MeshCore trademark, claiming ownership of the brand and creating a separate “MeshOS” line. The team disputes his claim, stating the official source is the GitHub repository, which Kirby has never contributed to, and noting his control of meshcore.co.uk and the original Discord server. In response, the core developers launched a new site (meshhcore.io) and Discord, publishing change logs, documentation, and firmware updates there. The project reports 38 000+ nodes worldwide and over 100 000 active app users. Key contributors include Scott (founder, firmware lead), Recro (map developer), Liam (app developer), FDLamotte (Python tools, STM32 firmware), and Oltaco (OTA bootloader). The team emphasizes human‑written software and invites community engagement through the new platform.

## Discussion Summary
The discussion conveys a generally critical stance toward current mesh networking projects, highlighting concerns about trademark enforcement, undisclosed AI-generated code, and perceived low code quality and inadequate testing. It points to governance issues such as hidden trademark filings and closed‑source business layers that limit openness, while also noting practical problems like illegal broadcast settings. Positive remarks are limited to personal satisfaction with specific implementations (e.g., Reticulum and related tools). The overall sentiment favors more transparent, well‑maintained alternatives, suggesting Wi‑Fi HaLow as a potentially better technological direction.

---

## Full Article

Since inception, the MeshCore development team have been working hard to build MeshCore.

We’ve released more than 85 versions of the MeshCore Companion, Repeater and Room Server firmwares with support for more than 75 hardware variants.
All of this has been hand crafted, by humans.

We have always been wary of AI generated code, but felt everyone is free to do what
they want and experiment, etc. But, one of our own, Andy Kirby, decided to branch out
and extensively use Claude Code, and has decided to aggressively take over
all of the components of the MeshCore ecosystem: standalone devices, mobile app,
web flasher and web config tools.

And, he’s kept that *small* detail a secret - that it’s all majority *vibe coded*.

We ran a poll recently, and asked in the MeshCore Discord about AI and trust, and these are the results:

![](https://blog.meshcore.io/assets/images/2026/04/23/trust-ai-gen-firmware.png)

![](https://blog.meshcore.io/assets/images/2026/04/23/have-right-to-know.png)

The team didn’t feel it was our place to protest, until we recently discovered that Andy
applied for the MeshCore Trademark (on the 29th March, according to filings) and didn’t tell
any of us. We have tried discussing this, and what his intentions are, but those broke down
and we now have no communication with Andy.

It’s been a stressful few months trying to sort this out, and is now a sad day
to bring this out to the public. It’s been a slap in the face to the team that
have worked so hard on this project, to have an insider team up with a robot
and a lawyer.

“Official” MeshCore
-------------------

The use of the ‘official’ status is what is currently being contested. Andy is adamant
that he *owns* the brand, and is using the word very heavily with his MeshOS line.

Meanwhile, in reality, the only ‘official’ MeshCore is the github repo. It’s the
*source of truth* in terms of what is MeshCore, and Andy has *never* contributed
to that.

Since the internal split, we launched the [meshcore.io](https://meshcore.io) site, as Andy controls
the meshcore.co.uk site and original discord server. We’ve been left with little other recourse. And, since
launching the site, Andy copied the look and feel (again, using Claude) even though
we asked him not to.

Project Growth
--------------

The MeshCore project has been on an incredible journey.

Having only started in January 2025, we have grown extremely fast!

As of this post, the official [MeshCore Map](https://map.meshcore.io) shows 38,000+ nodes around the world, and the official [MeshCore App](https://meshcore.io) has more than 100,000+ active users across Android and iOS.

It’s pretty epic how we’ve all built such an incredible community in such as a short time!

As the project grows, so does our need for a dedicated space that provides you with official information from the *core team*.

In recent times, we’ve seen an explosion of growth in MeshCore web sites dedicated to specific countries and mesh communities.

To name a few, we’ve seen:

Andy Kirby did do an amazing job helping to promote the MeshCore project on his personal YouTube, but only promotes his own products now.

Where To From Here?
-------------------

So, the core team are pushing ahead with the [meshcore.io](https://meshcore.io) website, the ongoing work of firmware feature development,
bug fixes, managing PR’s and developer discussions, etc.

We now release change logs, blog posts and technical documentation for all of our new firmware and app releases here.

You’ll also find some familiar faces on our blog posts, such as:

* **Scott** our project founder, lead firmware engineer and developer of the Ripple firmware!
* **Recrof** our official MeshCore Map developer and Firmware Flasher guru. He has shared some insights into the early development of the MeshCore Map.
* **Liam Cottle** the official MeshCore App developer who will be posting useful guides for getting started with the MeshCore App.
* **FDLamotte** who has done epic work on the Python tooling for MeshCore, as well as the STM32 firmware variants.
* **Oltaco** (Che Aporeps) who has done amazing work on the new OTA Fix bootloader that makes firmware updates much more reliable.

The Core Team
-------------

The MeshCore team, now consisting of **Scott**, **Liam**, **Recrof**, **FDLamotte** and now **Oltaco** remain committed to designing and developing high quality, *human-written* software.

Our New Home
------------

Please update your bookmarks!

This is where we will be hosting all official releases, technical documentation, and community discussions moving forward.

With the new website, we are also starting fresh with a new Discord server!

This is where you can interact directly with the MeshCore developers, get help with your projects, and contribute to the future of MeshCore.

Thanks for being a part of this journey!

*The MeshCore Team*