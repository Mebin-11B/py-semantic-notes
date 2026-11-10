---
title: "Mo RAM, Mo Problems (2025)"
url: https://fabiensanglard.net/curse/
clipped: 2026-06-17 01:11:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Mo RAM, Mo Problems (2025)](https://fabiensanglard.net/curse/)

## Digest Summary
- In a 1998 XA100 retro‑PC the author installed 384 MiB of 1997 SDRAM at a very low cost.  
- Initial Quake benchmark (Pentium MM 233 MHz) showed 44 fps, matching period benchmarks.  
- After re‑running the same test later, the framerate fell to 33 fps (~25 % slower).  
- Extensive troubleshooting (GPU swaps, driver changes, OS reinstall, CPU verification) did not alter the drop.  
- Removing RAM modules restored performance: with a single module the game ran at 44 fps, but with two or more modules it reverted to 33 fps.  
- The cause is the chipset’s limited cacheable memory: similar to the 430FX’s 64 MiB limit, the XA100’s cache effectively handles only about 128 MiB, leaving any excess RAM uncached and degrading performance.  
- The author solved the issue by reducing installed RAM to stay within the cacheable range.

## Discussion Summary
The comment reflects on legacy hardware memory management, noting a kernel patch that treated RAM above 64 MB as a swap‑based RAM disk to prioritize faster memory, and recalling similar L2 cache disabling on dual‑CPU BeBOX systems due to memory controller limits. It suggests that such trade‑offs were considered worthwhile when additional compute or memory was needed. The author observes that contemporary applications, exemplified by Chrome, often cache based on total RAM and may not scale efficiently on larger systems, and speculates that an extensible tag‑RAM feature on a 1997 board could be related.

---

## Full Article

Feb 16, 2026

Mo RAM, mo problems

---

As a retro-computer enthusiast, it seems that parts are either insanely expensive or dirt cheap. If the first case has obvious problems, the second can also lead to issues.

When I built the [Quake PC](https://fabiensanglard.net/quake_pc), the motherboard and HDD were worth their weight in gold. But the price of RAM modules was ridiculously low. So I maxed out by buying $40,000 worth of 1997 SDRAM, namely 384 MiB, for the price of $60.

From 44 fps to 33 fps

---

After I got the machine working, I ran benchmarks for weeks. I was constantly swapping video-cards, changing RAM types (SDRAM, EDO), adding RAM, removing RAM, and testing different CPUs. The CPU in my collection that ran Quake the best was the Pentium MM 233MHz clocking demo1 at **44.6 fps**. That figure was consistent with benchmarks of the era.

I wrote an [article about winquake](https://fabiensanglard.net/winquake) then took a break from 1997. A month later I had the idea to measure Michael Abrash assembly optimizations. I ran the same benchmark again. But this time I measured **33 fps**. That was nearly 25% slower. What happened?

Troubleshooting

---

I tried pretty much everything I could think of. I swapped the graphic card, removed all the 3D accelerators, updated the drivers, downgraded the drivers, wiped the whole system, re-installed everything, double checked that I was still using the MMX 233Mhz, and verified the frequency multiplier. Still **33 fps**.

Did a RAM module go bad? I tried to remove one of them. **33 fps**. Remove a second one (leaving only one). Now the game ran at **44 fps**. Two modules going bad? Hm, that seems weird. I tried to swap modules, leaving only one in the machine. All of them ran the game a **44 fps**. Only when two of more are in the machine, the framerate drops back to **33 fps**.

Epiphany

---

I vaguely remembered something about having too much RAM from the excellent *Upgrading and Repairing PCs 10th edition*.

> That last issue is one that many people are not aware of. The 430FX chipset can only cache up to 64M of main memory. This means that if you install more than 64M of RAM in your system, performance will suffer greatly.
> Now, many think this won’t be that much of a problem—after all, they don't normally run enough software to load past the first 64M anyway. That is another misunderstanding, because Windows 95 and NT load from the top down.  
>   
> This means, for example, that if you install 96M of RAM (one 64M and one 32M bank), then virtually all of your software, including the main operating system, will be loading into the non-cached region above 64M. Only if you use more than 32M would you begin to see an improvement in performance.
> tem.
>   
>   
>
> - Upgrading and Repairing PCs 10th edition

My motherboard, an XA100, is from 1998 and advertised[[1]](https://fabiensanglard.net/curse/#footnote_1) as supporting caching of 512MiB, but there is clearly something amiss there. It seems it actually can only cache in the neighborhood of 128 MiB. Which means any amount over that, made everything run without a L2 cache!

And that is the story of how I made that PC faster, by removing RAM.

References

---

---

\*