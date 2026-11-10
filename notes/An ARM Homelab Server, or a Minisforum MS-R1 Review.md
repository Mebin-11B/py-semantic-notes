---
title: "An ARM Homelab Server, or a Minisforum MS-R1 Review"
url: https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/
clipped: 2026-06-17 01:42:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [An ARM Homelab Server, or a Minisforum MS-R1 Review](https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/)

## Digest Summary
The Minisforum MS‑R1 is a bare‑bones ARM mini‑PC positioned as a low‑cost homelab server (MSRP $599, purchased for $559). After installing a 1 TB SSD, the author attempted Rocky Linux but the onboard Realtek RTL8127 NIC was not detected, requiring manual driver insertion and causing maintenance concerns. Fedora provided native driver support and was adopted for the system. Key hardware observations:

- Quiet operation and adequate performance for ARM workloads, though far below high‑end x86 CPUs (≈285 kIPS vs a 9950X).
- Two M.2 slots, one occupied by Wi‑Fi; the second accepts only U.2, limiting SSD expansion and RAID options.
- Marvell AQC107 NICs are invisible to UEFI, rendering them unusable.
- “Power‑on after outage” feature fails to restart the unit.

The device runs headless, hosts a FreeBSD 15.0 VM as a secondary Samba domain controller, and functions well as an ARM hypervisor despite the NIC and expandability limitations. The reviewer finds it a practical, affordable addition to an existing x86‑heavy homelab, while noting the ARM ecosystem remains smaller than x86.

## Discussion Summary
The comments show strong interest in ARM‑based homelab servers, with several users expressing enthusiasm after trying a Minisforum unit and noting its preinstalled Debian and price volatility. Many seek clarification on the unusual CPU core arrangement and its high idle power draw, questioning why it exceeds typical Intel or AMD levels and why the power supply appears oversized. Additional inquiries address the suitability of macOS versus Linux for server workloads, the perception of Fedora as less appropriate for servers, and the potential role of newer power‑efficiency technologies.

---

## Full Article

I’ve always wanted an ARM server in my homelab. But earlier, I either had to use an underpowered ARM system, or use Asahi which not only requires expensive Mac hardware but also slowed down in the past few years.

Then Minisforum introduced the MS-R1 Mini PC. Two MS-01s were already incumbent in my homelab when they replaced power-hungry HPE towers, but the MS-R1 gave me what I wanted: a reasonably powerful ARM machine which doesn’t have bank-breaking Mac pricing.

Assembly
--------

I got the MS-R1 barebones and had a 1TB SSD sitting around.

First, we have the box:

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_201531792-1024x771.jpg)

I opened the box and got this:

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_201755134-1024x771.jpg)

I installed my SSD, and attempted to install Rocky Linux.

Rocky Linux Installation
------------------------

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_203326687-1024x771.jpg)

So here it is, Rocky Linux booted.

There’s one issue: the onboard NICs weren’t detected:

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_203453944-771x1024.jpg)

I installed it anyways, and tried to sideload the Realtek r8127 drivers. While they did install and load, keeping the driver upon kernel updates wasn’t elegant and very hacky.

I could keep trying, but decided to just use Fedora instead:

Fedora Installation
-------------------

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_222139362-1024x771.jpg)

Yes, while I use Fedora on my laptop, I also know Fedora is generally not a good option for a server. But it had the NIC drivers as the RTL8127 is newer than RHEL 10’s freeze but not Fedora 43’s.

So that’s what I used.

Homelab Picture
---------------

Here’s my obligatory homelab picture:

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_223554374-771x1024.jpg)

MS-R1 on the top, then two MS-01s, MikroTik CCR2004-16G-2S+PC, CRS309-1G-8S+IN and CSS610-8P-2S+IN.

The Upsides
-----------

First, it’s a powerful-enough ARM system which doesn’t break the bank. I wanted this for so long. I’d say it’s quieter than the MS-01s but then Intel doesn’t exactly have the most efficient silicon. Yet even as an efficiency for performance freak I have a 285K instead of a 9950X.

While Minisforum recommends their Debian image, Rocky Linux worked for everything but the NICs, and Fedora works for everything I need. I haven’t tested the integrated GPU since I plan to use this headless. I also own a Mac as my ARM (but not main) laptop.

Say what you want about UEFI and ACPI, but it does make hardware support easier. Heck, not just Macs with UTM, but *Huawei* ARM laptops in China can run Windows VMs, despite crippling US sanctions.

I do hope a future CentOS/RHEL/Rocky 10 adds the Realtek 8127 so I won’t have to wait until 2028 for Rocky 11. And no I won’t use Debian.

The Downsides
-------------

By no means is the MS-R1 perfect.

For instance, there are two M.2 slots but one is used by the Wi-Fi and even if I remove it, cannot use it for a M.2 SSD, only U.2. I’d still prefer to have RAID if not for the shortage. The MS-01 and A2 have multiple M.2 SSD slots.

Also, Marvell AQC107 NICs wasn’t detected by the UEFI, so they couldn’t be used as far as I tried:

![](https://sour.coffee/wp-content/uploads/2026/02/PXL_20260219_220233492-771x1024.jpg)

Unless the NIC died or my UEFI configuration is wrong, it’s simply not usable.

One nit: if I select “power on after outage,” it didn’t do it when I unplugged and replugged the server. Darn.

**EDIT:** Apparently if I want auto power on, it’s a physical switch. Minisforum support told me this, so I flipped it and now it works great.

Why not Debian or Ubuntu?
-------------------------

While I’m aware there’s a “recommended” Debian variant for the MS-R1, I’m simply not a fan of Debian-based distros. Sure, I run my UniFi controller on Debian (inside Incus). But that’s because I *have* to, not because I want to.

I don’t hate Debian, I respect Debian for what they do. They do many things right, like being truly community-owned and having a reliable upgrade path (which RHEL and co notoriously lacks). But it’s not for me, despite having used it for 2.5 months before nearly a decade of FreeBSD.

Conclusion
----------

The ARM ecosystem while growing is still small when compared to x86. Heck, I daily drive an HP OmniBook Ultra instead of a faster M3 Pro MacBook Pro *because* of Linux. And Asahi’s delays.

The MS-R1 isn’t perfect, but works quite well as a homelab ARM hypervisor. Do I regret it? Not at all, despite its problems. It’s early adopter problems, but I have pretty thick skin as long as my privacy isn’t invaded for profit and “AI”.

The Mac Studio is way too expensive, even used, while expected for Apple is more expensive than even already expensive current-gen HPE ProLiants. *HPE* is cheaper than Apple, and is already expensive as-is. ARM64 SBCs are great, but I still wanted something like a PC.

There is also one other perk: while the MSRP is $599, I got it for $559 *despite* a RAM shortage.

While it won’t replace my two MS-01s (too much x86 software! vPro!), it’s a nice addition and is already running my secondary Samba domain controller in a FreeBSD 15.0 virtual machine.