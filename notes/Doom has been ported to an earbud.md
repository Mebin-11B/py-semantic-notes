---
title: "Doom has been ported to an earbud"
url: https://doombuds.com
clipped: 2026-06-17 01:53:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Doom has been ported to an earbud](https://doombuds.com)

## Digest Summary
The DOOMBUDS project implements Doom on earbud hardware using four components: a Doom port running on the earbuds, a serial server that bridges earbuds to a web server and transcodes the MJPEG stream for Twitch, a web server handling assets, queue management, keypress forwarding and MJPEG delivery, and a static webpage that drives the browser interface. Because earbuds lack displays, communication must use either Bluetooth (≈1 Mbps, unreliable) or UART pads (≈2.4 Mbps). The 320 × 200 8‑bit framebuffer (96 KB) requires compression; MJPEG is used with an embedded JPEG encoder, yielding ~11–13.5 KB per high‑quality frame, allowing a theoretical 22–27 FPS but actual performance caps at ~18 FPS due to JPEG encoding load on a Cortex‑M4F CPU (up‑clocked from 100 MHz to 300 MHz). RAM is limited to 992 KB after disabling the co‑processor, while Doom nominally needs 4 MB; extensive optimisations (lookup tables, const data in flash, disabling caches) reduce usage. Flash storage holds a trimmed Doom 1 WAD (“Squashware”, 1.7 MB) fitting within the 4 MB limit.

## Discussion Summary
The comments blend enthusiasm for the novelty of running Doom on increasingly unconventional hardware with a nostalgic fondness for classic, simpler games, while expressing disappointment that contemporary titles have become larger, more complex, and often feel like passive experiences rather than interactive play. Technical curiosity about the feasibility of distributed processing on earbuds and other tiny devices appears alongside humor and speculation about future Doom ports, reflecting a mixed sentiment of admiration for creative engineering, criticism of modern game design trends, and playful conjecture.

---

## Full Article

I'll put out an article / video diving deeper into this later, but here are a few bits of info:  
This project is made up of four parts:

1. The DOOM port that runs on the earbuds
2. The 'serial server' that acts as a bridge between the earbuds and the web server and also transcodes the MJPEG stream to twitch
3. The web server that serves assets, manages the queue, forwards keypresses and displays the MJPEG stream
4. The static webpage that tells your browser what to display on the screen and how to communicate with the web server

The firmware pushes up against a few hardware limitations:

1. Serial Connection

   Earbuds don't have displays, so the only way to transfer data to/from them is either via bluetooth, or the UART contact pads.  
   Bluetooth is pretty slow, you'd be lucky to get a consistent 1mbps connection, UART is easily the better option.  
   DOOM's framebuffer is (width \* height) bytes, 320 \* 200 = 96kB. (doom's internal framebuffer is 8-bit not 24-bit)  
   The UART connection provides us with 2.4mbps of usable bandwidth. 2,400,000 / 8 / 96,000 gives us... 3 frames per second.  
   Clearly we need to compress the video stream. Modern video codecs like h264 consume way too much CPU and RAM.  
   The only feasible approach is sending the video as an MJPEG stream. MJPEG is a stream of JPEG images shown one after the other.  
   I found an excellent JPEG encoder for embedded devices [here](https://github.com/bitbank2/JPEGENC), thanks Larry!  
   A conservative estimate for the average HIGH quality JPEG frame is around 13.5KB, but most scenes (without enemies) are around 11kb.  
   Theoretical maximum FPS:  
   - Optimistic: `2,400,000 / (11,000 \* 8)` = 27.3 FPS  
   - Conservative: `2,400,000 / (13,500 \* 8)` = 22.2 FPS
2. CPU

   The stock open source firmware has the CPU set to 100mhz, so I cranked that up to 300mhz and disabled low power mode.  
   The Cortex-M4F running at 300mhz is actually more than enough for DOOM, however it struggles with JPEG encoding.  
   This is why it maxes out at ~18fps, I don't think there's much else I can do to speed it up.
3. RAM

   By default, we only have access to 768KB of RAM, after disabling the co-processor it gets bumped up to the advertised 992KB.  
   DOOM requires 4MB of RAM, though there are plenty of optimisations that can reduce this amount.  
   Pre-generating lookup tables, making variables const, reading const variables from flash, disabling DOOM's caching system, removing unneeded variables. It all adds up!
4. FLASH

   The shareware DOOM 1 wad (assets file) is 4.2MB and the earbuds can only store 4MB of data.  
   Thankfully, [fragglet](https://github.com/fragglet), a well-known doom modder, has already solved this issue for me.  
   [Squashware](https://github.com/fragglet/squashware) is his trimmed-down DOOM 1 wad that is only 1.7MB in size.  
   With this wad file, everything comfortably fits in flash.