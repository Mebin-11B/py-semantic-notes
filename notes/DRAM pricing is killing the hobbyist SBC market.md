---
title: "DRAM pricing is killing the hobbyist SBC market"
url: https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/
clipped: 2026-06-17 01:24:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [DRAM pricing is killing the hobbyist SBC market](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/)

## Digest Summary
Raspberry Pi announced further price hikes for all models with LPDDR4 RAM, including a 3 GB Pi 4 at US $83.75 and a 16 GB Pi 5 at US $299.99. The increases reflect a surge in DRAM costs, which now represent the majority of component expenses for most hobbyist single‑board computers (SBCs). Consequently, boards with more than 4 GB RAM have become unaffordable for many hobbyists, and new SBC releases have sharply declined, with Radxa being the only vendor maintaining a recent product cadence. Comparable mini‑PCs now exceed US $250 for 8 GB configurations, and used PCs with similar memory are also pricier. Hobbyist developers are reverting to older SBCs or microcontrollers to keep project costs below US $100. While Raspberry Pi’s leadership expects DRAM prices to eventually fall, the timing is uncertain, and smaller SBC manufacturers may struggle to survive if current pricing trends persist.

## Discussion Summary
Comments converge on the view that soaring DRAM costs, driven by AI data‑center demand, supply‑chain constraints, and geopolitical factors, are sharply reducing low‑ and mid‑range smartphone volumes and pushing hobbyist single‑board computers, especially higher‑memory Raspberry Pi models, into an unaffordable range. Users report price spikes for memory, SSDs and SBCs, express frustration, and suggest postponing purchases, repurposing older hardware, or shifting to used x86 mini‑PCs. While most consider the surge temporary and anticipate eventual price easing, the prevailing sentiment remains concern over reduced accessibility for hobbyists and budget consumers.

---

## Full Article

Today Raspberry Pi announced [more price increases for all Pis with LPDDR4 RAM](https://www.raspberrypi.com/news/a-new-3gb-raspberry-pi-4-for-83-75-and-more-memory-driven-price-increases/), alongside a 'right-sized' 3GB RAM Pi 4 for $83.75.

The price increases bring the 16GB Pi 5 up to *$299.99*.

Despite today's date, this is not a joke.

I published a video going over the state of the hobbyist 'high end SBC' market (4/8/16 GB models in the current generation), which I'll embed below:

But if you'd like the **tl;dr**:

Unless the DRAM pricing situation changes *radically*, I think the hobbyist SBC market is dyingâor at least on life support. And I don't just mean Raspberry Pis, but all SBC vendors. LPDDR chips now account for the majority of board cost from the vendors I've checked with.

![Raspberry Pi 5 Price Increases since launch 2 4 and 16 GB models](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/raspberry-pi-price-increase-since-launch.jpg)

Besides causing a radical reduction in new boards launched (Radxa seems to be the only vendor that had some cadence last year), the price increases for boards with greater than 4 GB of RAM have put those boards out of the reach of most hobbyists.

Even mini PCs, which for a time were a *great* deal, have risen to $250+ for 8 GB models. *Used* PC are also more expensive, especially with more than 4 GB of RAM.

I design most of my projects so they can be replicated for less than $100. Learning is easier on cheaper parts you won't fret over too much when you break them. With prices going up, this limits the types of projects I take on.

I'm working more with older SBCs and microcontrollers now, and I think that's the direction many in the hobbyist space are going.

Maybe, as Eben Upton says in Raspberry Pi's post,

> memory prices wonât remain at their current very high level indefinitely; the circumstances in which we find ourselves are challenging, but in the future they will abate.

But I'm not sure how long we'll have to wait, or if a hobbyist SBC market will exist by the time the bubble bursts.

Lucky for Raspberry Pi, they have a thriving microcontroller ecosystem and industrial base to keep them going. I fear smaller vendors won't be able to go on like this forever.