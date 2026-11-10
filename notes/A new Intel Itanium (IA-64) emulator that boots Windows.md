---
title: "A new Intel Itanium (IA-64) emulator that boots Windows"
url: https://raymii.org/s/blog/Intel_Itanium_IA-64-Emulator_that_boots_Windows.html
clipped: 2026-08-31 12:23:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A new Intel Itanium (IA-64) emulator that boots Windows](https://raymii.org/s/blog/Intel_Itanium_IA-64-Emulator_that_boots_Windows.html)

## Digest Summary
A version 0.1 of an Intel Itanium (IA‑64) emulator has been released by Yufeng Gao with assistance from gdwnldsKSC. The emulator can boot the Itanium editions of Windows Server 2003 and Windows XP 64‑bit, though performance is very low (approximately 486‑class speed on a Ryzen 5000 series). At present it does not start OpenVMS, HP‑UX, Linux, or BSD guests. The code is currently closed‑source, but the developer indicated it will be published on GitHub under TheBrokenPipe/ski after cleanup. An update notes a QEMU fork that reportedly runs Windows Server 2008 on IA‑64 and is claimed to be generated with LLM assistance. No commercial IA‑64 emulators are known. The release is primarily of interest to preservation and hobbyist communities seeking to explore legacy Itanium software, especially Windows, while broader OS support remains unavailable.

---

## Full Article

[Skip to main content](https://raymii.org/s/blog/Intel_Itanium_IA-64-Emulator_that_boots_Windows.html#main)
            
          
    

## More emulation goodness, an Intel Itanium (IA-64) emulator that boots Windows!

Published: 18-07-2026 23:33 | Last update: 20-07-2026 05:31 | Author: Remy van Elst | [Text only version of this article](https://raymii.org/s/blog/Intel_Itanium_IA-64-Emulator_that_boots_Windows.txt)

The emulation space is going crazy, after my previous [post on Windows booting on DEC Alpha es40 emulator](https://raymii.org/s/blog/Run_Windows_2000_for_Dec_Alpha_on_a_new_es40_fork.html), there is now another huge breakthrough in the emulation of other non-x86 CPU emulation. [Yufeng Gao](https://github.com/TheBrokenPipe) with help from [gdwnldsKSC](https://github.com/gdwnldsKSC) (the man behind the updated es40-fork) has released version 0.1 of his [Intel Itanium (IA-64) emulator](https://thebrokenpipe.com/ia64/zx2000/) that boots the Itanium version of Windows Server 2003 and Windows XP 64-bit. No OpenVMS or HP-UX yet and Linux / BSD also don't boot. But Windows is amazing already.

Here is a screenshot of Windows Server 2003 with the Luna theme running 
in the emulator:

  

It runs quite slowly, (486-levels of performance on a Ryzen 5000 series
according to [this discord channel](https://discord.com/channels/712491206986170440/1520321862213566474)) but
hey, it runs at all. How cool is that! Let's hope development continues and
we might even get to run OpenVMS on Itanium, emulated. HP-UX would be nice as
well, but I care more for OpenVMS. As far as I know there are no commercial
Itanium emulators yet.

You can read more about the [Intel Itanium (IA-64) CPU on Wikipedia](https://en.wikipedia.org/wiki/Itanium) and here is a [great video](https://youtu.be/3oxrybkd7Mo) from RetroBytes with some more history.
Basically it was a promising architecture, but didn't make it and effectively
it was only used for HP-UX and OpenVMS in the later years. But [OpenVMS is now 
available on x86](https://raymii.org/s/blog/OpenVMS_9.2_for_x86_will_be_released_tomorrow.html) and
HP-UX is dead in the water, no migration path available there. I don't think
Windows on Itanium was ever used intensively. If you do know of more usage in
the real world, please let me know.

Here are two more screenshots, also showing Windows XP 64-bit for the Itaium:

The screenshots come from [discord](https://discord.com/channels/712491206986170440/1520321862213566474). 

The emulator was announced on [Twitter](https://nitter.net/x86corez/status/2078431660299743303):

The code is not open source, but the twitter thread stated:

Once cleaned up, it will be available here: [https://github.com/TheBrokenPipe/ski](https://github.com/TheBrokenPipe/ski).

Update: 2026-07-20: There seems to be a QEMU fork that can also run Server 2008.

See [this repo](https://github.com/syunnPC/qemu-system-ia64). I haven't checked that
one out but it does state that it's written using LLM's. Was mentioned on the Discord
server.

Screenshots:

Tags: [blog](https://raymii.org/s/tags/blog.html)
, [dec](https://raymii.org/s/tags/dec.html)
, [hp-ux](https://raymii.org/s/tags/hp-ux.html)
, [ia-64](https://raymii.org/s/tags/ia-64.html)
, [intel](https://raymii.org/s/tags/intel.html)
, [itanium](https://raymii.org/s/tags/itanium.html)
, [openvms](https://raymii.org/s/tags/openvms.html)
, [rx2200](https://raymii.org/s/tags/rx2200.html)
, [ski](https://raymii.org/s/tags/ski.html)
, [vms](https://raymii.org/s/tags/vms.html)
, [windows](https://raymii.org/s/tags/windows.html)
