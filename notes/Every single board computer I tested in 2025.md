---
title: "Every single board computer I tested in 2025"
url: https://bret.dk/every-single-board-computer-i-tested-in-2025/
clipped: 2026-06-17 01:34:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Every single board computer I tested in 2025](https://bret.dk/every-single-board-computer-i-tested-in-2025/)

## Digest Summary
The 2025 SBC roundup covered 15 boards from eight manufacturers, spanning SoCs from Rockchip, Broadcom, Qualcomm, MediaTek, Allwinner, StarFive, CIX and Texas Instruments, with prices from $42 to $590.

* **Budget (< $50)** – Six boards: BeagleBone Green Eco (TI Sitara AM3358, 512 MB DDR3L, $42); VisionFive 2 Lite (StarFive JH7110S, 4 GB LPDDR4, $43); Arduino UNO Q (Qualcomm QRB2210, 2 GB LPDDR4X, $44); Orange Pi RV/RV2 (JH7110 and Ky X1, 4 GB LPDDR4/4X, $46‑$50); Radxa Cubie A7A (Allwinner A733, 6 GB LPDDR5, $45) – the Cubie A7A delivered the highest Geekbench scores in this tier (641 SC/1,545 MC).

* **Mid‑range ($50‑$100)** – Notable boards: Radxa ROCK 4D (Rockchip RK3576, 8 GB LPDDR5, $60, 319 SC/1,332 MC); Radxa Dragon Q6A (Qualcomm QCS6490, 6 GB LPDDR5, $70, 1,180 SC/3,215 MC); ArmSoM CM5 (RK3576 compute module, $95); Banana Pi R4 (MediaTek MT7988A network‑oriented SoC, 8 GB LPDDR4, $99).

* **High‑end (>$100)** – Highlights: Raspberry Pi 500+ ($200, 16 GB LPDDR4X, NVMe); ArmSoM AIM7 (RK3588, $239, Jetson‑Nano form factor); CIX P1 boards – Radxa Orion O6N ($199) and Orange Pi 6 Plus ($260) with 32 GB LPDDR5, achieving > 1,300 SC and > 7,000 MC; Radxa Fogwise Airbox Q900 ($590, Qualcomm IQ‑9075, 36 GB LPDDR5, AI‑edge focus).  

Key trends: CIX P1 emerged as the top‑performing SoC; Qualcomm entered the SBC market with competitive performance; RISC‑V boards improved but lag behind ARM; Rockchip RK3576 solidified its mid‑range role; RAM pricing volatility impacted board costs.

## Discussion Summary
Comments focus on the need for clearer information about software support, especially main‑line Linux compatibility, security updates, and distro readiness for SBC and SoC platforms. There is a recurring request for more detailed benchmarking data, consistent model reporting, and summarized tables. Hardware concerns include the scarcity of USB‑C DisplayPort Alt‑mode on lower‑priced boards and the importance of hardware‑accelerated PPPoE performance versus CPU‑only solutions. Users also note preferences for router firmware options and emphasize the relevance of driver upstreaming and reliable boot device ordering.

---

## Full Article

*364*

2025 was a pretty busy year for single board computers. I had 15 boards released in 2025 come through the bench from 8 different manufacturers, spanning SoCs from Rockchip, Broadcom, Qualcomm, MediaTek, Allwinner, StarFive, CIX, and Texas Instruments. Prices have ranged from $42 all the way up to $590, and the variety on offer has been genuinely impressive. We’ve had RISC-V boards, Qualcomm entering the SBC space (in a big way), a new-ish SoC vendor in CIX turning heads, an Arduino SBC of all things, and Raspberry Pi iterating on their keyboard form factor.

![Raspberry Pi 500+/Plus NVMe SSD](https://bret.dk/every-single-board-computer-i-tested-in-2025/ "Every Single Board Computer I Tested in 2025 17")

Also, my friend Meco of sbcwiki has a great series called “State of Embedded” that shares some insight into the scene, too, and you can read his [Q4 roundup](https://sbcwiki.com/news/articles/state-of-embedded-q4-25/) on the matter if you want bit of a dive into things in general, rather than specific SBCs.

All of the boards in this article have been benchmarked and are available to compare on [sbc.compare](https://sbc.compare/browse?release_year=2025), so if you want to dig into the raw numbers yourself, head over there. I’ll be linking to each board’s page throughout this article so you can see the full data for anything that catches your eye.

Before we get into it though, a quick note on pricing. The prices listed throughout this article are what the boards were retailing at when I tested them. As many of you will be aware, LPDDR4 and LPDDR5 memory didn’t escape RAMageddon and costs have been climbing since late 2025, with manufacturers pivoting production towards more profitable (and AI-hungry) memory types. This has already [hit Raspberry Pi pricing](https://bret.dk/1gb-raspberry-pi-5-launched-alongside-price-increases/) and it’s affecting other boards too. Some of the prices you see here may have gone up, or the boards may not be available at all right now. I’ll try to note where I’m aware of changes, but do check current pricing before purchasing and comparing.

The Budget Boards (Under $50)
-----------------------------

Six boards came in under $50 this year, and they’re a surprisingly varied bunch. You’ve got RISC-V, ARM, even a decades-old Texas Instruments SoC making an appearance. If you’re looking to tinker without a significant outlay, 2025 has given you plenty to choose from.

![StarFive VisionFive 2 Lite - JH7110S SoC Close Up](https://bret.dk/every-single-board-computer-i-tested-in-2025/ "Every Single Board Computer I Tested in 2025 18")

We get some more JH7110(S) RISC-V variants in 2025!

### BeagleBoard BeagleBone Green Eco ($42)

So to kick things off, I’ll be honest, the [BeagleBone Green Eco](https://sbc.compare/86-beagleboard-beaglebone-green-eco-512mb) is a bit of an oddity on this list. It’s running a TI Sitara AM3358, a single-core Cortex-A8, with 512MB of DDR3L. In 2025. BeagleBoard have always had a strong following in the industrial and education spaces though, and this is clearly where the Green Eco is aimed. It’s not here to compete on raw performance and it knows it. If you need something reliable, well-documented, and with a long history of community support for embedded applications, BeagleBoard have that covered. For general-purpose SBC tinkering though, you’re better off looking elsewhere in this tier.

### StarFive VisionFive 2 Lite ($43)

StarFive’s [VisionFive 2 Lite](https://sbc.compare/100-starfive-visionfive-2-lite-4gb) is a trimmed-down version of the VisionFive 2 that I [reviewed a while back](https://bret.dk/risc-v-starfive-visionfive-2-review-jh7110/), running the JH7110S variant of the SoC. With Geekbench 6 scores of 59 single-core and 180 multi-core, the numbers aren’t going to set the world alight, but sadly, that’s the state of RISC-V in 2025 (at least at these price points). If you’re interested in the architecture and want a cheap way in, $43 for 4GB of RAM isn’t bad. Just don’t go in expecting 2025 ARM-level performance.

### Arduino UNO Q ($44)

This one caught me off guard. Arduino, the company most of us associate with microcontrollers and blinking LEDs, have released an SBC. The [UNO Q](https://sbc.compare/96-arduino-uno-q-2gb) runs a Qualcomm QRB2210 with 2GB of LPDDR4X, and whilst the Geekbench scores of 190 SC / 527 MC are modest, I think the story here is less about the performance and more about what Arduino are trying to do. It feels like they’re testing the waters in the SBC market, and having Qualcomm silicon in an Arduino product is something that we should have seen coming given Qualcomm’s acquisition of them. Whether there’s a meaningful audience for it beyond curiosity remains to be seen, however, as it was a rather confusing product. My X thread below details it fairly well (feel free to follow whilst you’re there, too!)

> Sooo 1st impressions of the [@arduino](https://twitter.com/arduino?ref_src=twsrc%5Etfw) UNO Q are that the app lab software isn't my cup of tea. It shouted that I needed to update the image on the UNO Q, but the flasher is a separate CLI-only utility, and you need to short headers to flash. OK, fine.  
>   
> After booting again, App Lab…
>
> — bret.dk (@bretweber) [November 26, 2025](https://twitter.com/bretweber/status/1993763803498955263?ref_src=twsrc%5Etfw)

### Orange Pi RV and RV2 ($50 / $46)

Orange Pi have thrown two RISC-V boards into the ring this year. The [Orange Pi RV](https://sbc.compare/92-orange-pi-rv-4gb) ($50) runs the StarFive JH7110, the same chip as the VisionFive 2, pulling in Geekbench scores of 74 SC / 220 MC. The [Orange Pi RV2](https://sbc.compare/28-orange-pi-rv2-4gb) ($46) is the more interesting of the pair, using the less common Ky X1 SoC (which seems to just be a clone of the Spacemit K1?) and managing 118 SC / 528 MC in Geekbench. Both come with 4GB of LPDDR4/4X.

It’s good to see Orange Pi investing in RISC-V alongside their ARM lineup to keep things fresh and fun. The RV2’s Ky X1 results are a step in the right direction, though we’re still a long way from RISC-V boards being competitive with similarly priced ARM options on raw compute. The software ecosystems for both chips are still maturing too, so if you’re picking one of these up, you’ll want to be comfortable with a bit of tinkering to get things working the way you want, but the software wasn’t completely terrible, which is nice.

### Radxa Cubie A7A ($45)

The [Radxa Cubie A7A](https://sbc.compare/46-radxa-cubie-a7a-6gb) is the standout of the budget tier. An Allwinner A733 with 6GB of LPDDR5 for $45 is a strong proposition, and the Geekbench scores of 641 SC / 1,545 MC put it comfortably ahead of everything else under $50. For context, that multi-core score isn’t far off some of the Rockchip RK3576 boards in the next tier up that cost $60+. If you’re after the best bang for your buck in 2025, the Cubie A7A makes a compelling case for itself.

The Mid-Range ($50 to $100)
---------------------------

The $50 to $100 bracket is where most people tend to shop, and this year it’s been dominated by a few interesting trends. Rockchip’s RK3576 has turned up on multiple boards, Qualcomm has made a very strong entrance, and there’s a networking-focused option that doesn’t care about your Geekbench score.

### Radxa ROCK 4D ($60)

The [Radxa ROCK 4D](https://sbc.compare/48-radxa-rock-4d-8gb) is one of three RK3576-based boards I’ve tested this year (the others being the ArmSoM CM5 and the [DShanPi A1](https://bret.dk/dshanpi-a1-rockchip-rk3576-sbc-with-hdmi-input-dual-gbe-and-6-tops-npu/)). With 8GB of LPDDR5 at $60, it’s the cheapest way into RK3576 territory. Geekbench results of 319 SC / 1,332 MC are right in line with what we’ve seen from this SoC across all three boards. You can [compare all three RK3576 boards on sbc.compare](https://sbc.compare/48-radxa-rock-4d-8gb/83-armsom-cm5-8gb/95-dshan-pi-a1-4gb) if you’re curious how they stack up against each other.

At this price for 8GB of RAM, it’s solid value. The usual Rockchip software story applies though, so do factor that in. [Armbian](https://www.armbian.com/radxa-rock-4d/) have a great alternative to the Radxa OS builds, and that’s what I’ve used in testing, so maybe it’s less of an issue on that front.

### Radxa Dragon Q6A ($70)

If I had to pick the most interesting board of the year, the [Radxa Dragon Q6A](https://sbc.compare/47-radxa-dragon-q6a-6gb) would be right up there. A Qualcomm QCS6490 with 6GB of LPDDR5 for $70, and Geekbench scores of 1,180 SC / 3,215 MC. Read those numbers again. That single-core score is in Raspberry Pi 5 territory, at $70, from a Qualcomm SoC, on a Radxa board. If someone had told me that a year ago, I’d have been extremely sceptical. It even dips its toes into Windows on ARM and can offer respectable gaming performance!

Qualcomm entering the SBC market is one of the bigger stories of 2025 in my view. The performance-per-dollar here is genuinely impressive. The big question mark is the software ecosystem. Qualcomm’s Linux support has historically been a little hit and miss, though they seem to be really trying with these SoCs, and mainline support is there or there abouts. It also has [great Armbian support](https://www.armbian.com/radxa-dragon-q6a/). Regardless, the hardware is there though, and I’m here for it.

### ArmSoM CM5 ($95)

The [ArmSoM CM5](https://sbc.compare/83-armsom-cm5-8gb) is another RK3576 board, this time in a compute module form factor with 8GB of LPDDR5 at $95. Geekbench scores of 326 SC / 1,366 MC are essentially identical to the ROCK 4D, which makes sense given they share the same SoC. The price premium over the ROCK 4D comes down to the compute module form factor, which serves a different purpose. If you need something that slots into a carrier board for a specific deployment, the CM5 fills that role. If you’re after a general-purpose dev board and don’t need the modularity, the ROCK 4D at $60 is likely the better buy. I’ve [reviewed ArmSoM’s AIM7 previously](https://bret.dk/armsom-aim7-review-rk3588-meets-jetson-nano/) and came away impressed with their documentation and approach, so they’re a brand worth keeping an eye on.

### Banana Pi R4 ($99)

The [Banana Pi R4](https://sbc.compare/94-banana-pi-r4-8gb) is a different beast entirely. Running a MediaTek MT7988A with 8GB of LPDDR4 at $99, its Geekbench scores of 305 SC / 889 MC look underwhelming on paper. But judging this board on CPU benchmarks alone would be missing the point (and to be honest, that stands true for most of the boards in this piece.) The MT7988A is a networking SoC, and the R4 exists for OpenWrt, router, and network appliance use cases. If you’re looking for something to replace ageing network hardware or build a custom router, this is the board to look at. If you want a general-purpose SBC, it’s not.

![Banana Pi R4](https://bret.dk/every-single-board-computer-i-tested-in-2025/ "Every Single Board Computer I Tested in 2025 20")

I’m using the R4 in the office for benchmarking, with its 10Gbit SFP+ ports, it’s connected to my big ol’ [UniFi Pro 48 PoE switch](https://eu.store.ui.com/eu/en/category/switching-professional/products/usw-pro-48-poe) and acts as a perfect iPerf3 endpoint for testing!

The High End ($100 and Up)
--------------------------

Five boards landed above the $100 mark this year, ranging from $199 to $590. This is where we see some serious silicon, a newer SoC vendor making waves, and one board that’s in a category of its own.

### Raspberry Pi 500+ ($200)

I’ve already [reviewed the Pi 500+ in full](https://bret.dk/raspberry-pi-500-plus-review/), so I won’t rehash everything here. The short version: 16GB of LPDDR4X, NVMe storage, mechanical keyboard switches, and it’s what the [original Pi 500](https://bret.dk/raspberry-pi-500-review-a-pi-5-in-a-keyboard/) should have been from the start. [Geekbench scores](https://sbc.compare/56-raspberry-pi-500-plus-16gb) of 892 SC / 2,121 MC are in line with the BCM2712’s known performance. At $200 it’s not cheap, but when you break down what you’re getting (the NVMe, the doubled RAM, the mechanical keyboard upgrade), the value is there. It’s the most refined Raspberry Pi product to date in my opinion, though 2025 wasn’t a revolutionary year for Pi. More of an iterative one.

### ArmSoM AIM7 ($239)

The [ArmSoM AIM7](https://sbc.compare/5-armsom-aim7-8gb) packs an RK3588 with 8GB of LPDDR4X into a Jetson Nano-compatible form factor. Geekbench scores of 828 SC / 3,186 MC. I covered this one in depth in my [full AIM7 review](https://bret.dk/armsom-aim7-review-rk3588-meets-jetson-nano/) and the summary hasn’t changed: if you specifically need a Jetson Nano replacement with modern performance, the AIM7 does exactly what it says on the tin. If you don’t need that form factor compatibility, there are more flexible RK3588 options out there for less money. As mentioned earlier, ArmSoM continue to impress on the documentation and overall quality front though.

### Radxa Orion O6N and Orange Pi 6 Plus ($199 / $260)

I’m covering these two together because they share the same story: the CIX P1. This is a brand new SoC from a vendor that wasn’t on anyone’s radar a year ago, and both the [Radxa Orion O6N](https://sbc.compare/101-radxa-orion-o6n-32gb) ($199) and the [Orange Pi 6 Plus](https://sbc.compare/91-orange-pi-6-plus-32gb) ($260) pair it with 32GB of LPDDR5.

The numbers speak for themselves. The O6N pulls in 1,327 SC / 6,954 MC on Geekbench, whilst the 6 Plus hits 1,328 SC / 7,130 MC. Those multi-core scores are in a completely different league to anything else on this list. You can [compare the two CIX P1 boards directly on sbc.compare](https://sbc.compare/101-radxa-orion-o6n-32gb/91-orange-pi-6-plus-32gb) and the results are near-identical, as you’d expect from the same SoC.

So is the CIX P1 the most exciting new SoC to arrive in the SBC space this year? Based on raw performance, I’d say yes. Having two manufacturers already shipping boards with it suggests there’s confidence in the platform. The $61 price gap between the O6N and the 6 Plus is worth investigating if you’re considering one, as the silicon is the same and the performance is effectively identical.

Software maturity is the usual question mark with a new SoC vendor, but the early signs are encouraging. There’s the power consumption quirks, along with a few other annoyances but in terms of raw performance, they take the top spots. Other SBCs (if I can call them that, I guess?) with the CIX P1 include the [Radxa Orion O6](https://radxa.com/products/orion/o6/) (the mITX brother of the O6N), and the Minisforum MS-R1, though the former is a bit harder to get right now, and the latter came at a pretty unfortunate time. It’s a polished unit, it’s just sadly quite expensive compared to the alternatives.

### Radxa Fogwise Airbox Q900 ($590)

Finally, the [Fogwise Airbox Q900](https://sbc.compare/97-radxa-fogwise-airbox-q900-36gb) is the outlier on this list. A Qualcomm IQ-9075 with 36GB of LPDDR5 at $590 isn’t really a traditional SBC purchase. Geekbench scores of 1,111 SC / 5,638 MC are strong but actually fall behind the CIX P1 boards that cost a third of the price. The Airbox’s value proposition is in its Qualcomm AI stack and the specific edge deployment use cases it’s designed for, not general-purpose compute. If you know you need it, you know you need it. For the rest of us, it’s interesting to see where the high end of the SBC market is heading, but $590 is a lot of money for a single board computer.

![Radxa fogwise Airbox Q900 Edge AI Box](https://bret.dk/every-single-board-computer-i-tested-in-2025/ "Every Single Board Computer I Tested in 2025 21")

AI AI AI AI AI AI AI AI AI AI AI

The Elephant in the Room: RAM Prices
------------------------------------

I can’t write a 2025 SBC roundup without addressing the memory situation. LPDDR4 and LPDDR5 prices have been climbing since the second half of the year, driven by manufacturers shifting production towards higher-margin memory types (the AI boom has a lot to answer for here). We’ve already seen [Raspberry Pi raise prices across their lineup](https://bret.dk/1gb-raspberry-pi-5-launched-alongside-price-increases/), and they’re unlikely to be the last.

For the boards in this article, the prices I’ve listed are from when I tested them. Some may have gone up since, others may be temporarily out of stock. If you’re looking to pick something up, do check current pricing on the relevant retailer or AliExpress listing before ordering. The situation is supposedly temporary (come on bubbble.. pop..), but whether that means months or years is anyone’s guess at this point.

The silver lining, if there is one, is that it makes performance-per-dollar comparisons all the more relevant. If you’re going to pay more for a board, you want to make sure you’re getting the most out of that money. That’s exactly the kind of comparison you can run on sbc.compare, so do make use of it!

What Did 2025 Tell Us?
----------------------

Looking back at 15 boards across a year, a few themes stand out.

### CIX P1 is the breakout SoC of the year

Two boards, monster multi-core numbers, and a new vendor that brute forced their way to the top. If the software ecosystem matures alongside the hardware, CIX could become a serious player. The fact that both Radxa, Minisforum, and Orange Pi are already shipping boards with it says something about the confidence in the platform.

### Qualcomm is here, and they mean business

The Dragon Q6A’s single-core performance at $70 is a shot across the bow for anyone who thought ARM SBCs were a two-horse race between Broadcom and Rockchip. The Arduino UNO Q and Fogwise Airbox Q900 round out a spread from budget to premium. Software support will be the deciding factor, as it always is, but the silicon is competitive.

We even have Indian manufacturer, Vicharak teasing a modular SBC that utilises the same Qualcomm SoC as the Dragon Q6A from Radxa. I’ve been speaking with one of their hardware team about it, and it seems like it’s getting close to reality, and I’m pretty excited about that!

VIDEO

### RISC-V is still finding its feet

Four boards this year (VisionFive 2 Lite, Orange Pi RV, Orange Pi RV2, plus the Ky X1 showing up in the RV2) and the performance gap to ARM remains significant. It’s getting closer, and the fact that we’re seeing this many RISC-V boards in a single year is progress in itself, but we’re not at the point where I’d recommend one over an ARM board for anything other than architecture-specific interest. I’m not a hater, though, don’t get me wrong. I love the fast progress and the competition it’s slowly starting to offer. 2026 has already shown some promising new releases (with the Spacemit K3-based boards like the Milk-V Jupiter) so keep your eyes peeled.

### Rockchip RK3576 is the new mid-range workhorse

Three boards this year (ROCK 4D, ArmSoM CM5, DShanPi A1), all performing within a few percent of each other. The software story is the same as it’s been for Rockchip, and that’s promising hardware that needs the kernel and driver support to catch up. That said, Collabora’s recent progress on upstream video decoder support for the RK3576 and RK3588 is encouraging, and it only builds on the great work they’ve already done in the area.

### The price spectrum has widened

From $42 to $590, the definition of “single board computer” is stretching. That’s not a bad thing. Having options at every price point means there’s something for every use case, whether you’re building a network appliance for $99 or deploying edge AI at $590.

### Raspberry Pi is iterating, not revolutionising

The 500+ is a great product and my pick if you want something that just works, but 2025 wasn’t a Pi-defined year the way 2023 and 2024 were. The competition has stepped up, and Raspberry Pi are likely biding their time to hit a sweet spot for interest (and likely costs!) before releasing the Raspberry Pi 6. Will that be 2026? Unless RAM pricing comes crashing down, I’d be surprised, but maybe it’ll launch with 1/2GB RAM options first and spread out over time. I’d hope not, it would hamstring the SoC I imagine, but let’s see.

If you want to explore all of the boards in this article (and the 80+ others I’ve benchmarked), head over to sbc.compare and have a dig around. If there’s a specific comparison you’d like to see, or a board you think I should get on the bench for 2026, let me know in the comments, or shout at your favourite SBC vendor to reach out ;-)

I hope 2026 is everything you want it to be!