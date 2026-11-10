---
title: "5x5 Pixel font for tiny screens"
url: https://maurycyz.com/projects/mcufont/
clipped: 2026-06-17 01:13:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - typography
  - embedded systems
  - microcontrollers
related:
  - "[[Show HN Audiomass – a free, open-source multitrack audio editor for the web]]"
  - "[[RTX 5090 and M4 MacBook Air Can It Game]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The project introduces a custom-designed, monospaced 5x5 pixel font optimized for readability on ultra-low-resolution displays.
>
> **Key points:**
> - Details a hand-crafted 5x5 pixel monospaced font tailored for microcontrollers and very small screen hardware.
> - Explains the layout, design constraints, and technical decisions to maximize legibility at minimal pixel sizes.
> - Discusses symbol representation, character set limitations, and rendering optimization.
>
> **Concept links:** [[Typography]], [[Embedded Systems]], [[Hardware Design]], [[Microcontrollers]], [[User Interface Design]]
>
> **Suggested connections:**
> - [[Show HN Audiomass – a free, open-source multitrack audio editor for the web]] — connects to open-source, utility-focused web tools.
> - [[RTX 5090 and M4 MacBook Air Can It Game]] — contrasts low-resource display requirements with high-end gaming hardware.
<!-- ai-summary:end -->

# [5x5 Pixel font for tiny screens](https://maurycyz.com/projects/mcufont/)

## Digest Summary
The post describes a hand‑crafted 5×5 pixel monospaced font designed for ultra‑low‑resolution displays. Built on lcamtuf’s 5×6 font (itself derived from the ZX Spectrum 8×8 set) and intended for a 6×6 grid, it is the smallest size that retains legibility—2×2 is impossible, 3×3 unreadable, 4×4 cannot render “E”, “M”, or “W”. Fixed‑width characters make layout calculations trivial (string width = 6 × character count) and prevent overflow when mixing numbers and letters. The entire font occupies 350 bytes, fitting comfortably in 8‑bit microcontrollers such as the AVR128DA28 (16 KB RAM). The author compares the 5×5 set with narrower variants (4×5, 3×5, 3×4, 3×3, 2×3, 3×2, 2×2), noting progressive loss of distinct glyphs, especially for “M”, “W”, “Q”, and numeric clarity. Real‑screen tests show sub‑pixel rendering adds a pseudo‑dropshadow effect, improving perceived smoothness on color displays, while monochrome screens still render acceptably. The font targets small OLED panels (e.g., 128×64) where hand‑drawn, memory‑efficient glyphs are essential.

## Discussion Summary
The discussion centers on the practicality of extremely small bitmap fonts, with participants comparing 3 × 5, 4 × 5, 5 × 5, and slightly larger grids. Consensus holds that 3 × 5 is generally illegible, while 5 × 5 can be readable if extra spacing is added, and 4 × 5 or 5 × 6 often provide a better balance of clarity and compactness. Historical retro examples and modern embedded uses are cited, and several contributors express admiration for the design skill required, while noting that modern high‑resolution displays reduce the need for such ultra‑tiny fonts.

---

## Full Article

*5x5 Pixel font for tiny screens*
=================================

**2026-04-18** — **2026-04-20** ([Programming](https://maurycyz.com/tags/programming/))![Some example text in this font.](https://maurycyz.com/projects/mcufont/demo.png)
[Font data (C header)](https://maurycyz.com/projects/mcufont/mcufont.h)

All characters fit within a 5 pixel square, and are safe to draw on a 6x6 grid.
The design is based off of lcamtuf's 5x6 font-inline.h, which is itself inspired by the ZX Spectrum's 8x8 font.

*5x5 is the smallest size* that doesn't compromise legibility:

* **2x2**: Impossible.
* **3x3**: Technically possible, but unreadable.
* **4x4**: Not enough to draw "E", "M" or "W" properly.
* **5x5**: This font.

Five by five is actually big enough to draw most lowercase letters one pixel smaller, making them visually distinct from uppercase.

*Narrower 4x5 and 3x5 dimensions are possible*, but would require sacrificing the M,
dotted zero, and reduce U/V/Y distinctiveness.

There's no artistic reason to make all characters five wide just because a few must be...
but a using a constant width makes programming a lot easier:
The length of a string on screen is always 6 times the number of characters.

It also makes compact layouts much safer:
There's no need to worry that a number will overflow because "8978" is longer than "1111".

*The whole font takes up just 350 bytes* of memory,
which makes it ideally suited to 8-bit microcontrollers like the AVR128DA28 (16 kB of RAM)
These are cheap, low power and robust...
but they fall short on graphics:

Even a low-resolution 384x288 display has 110 thousand pixels:
way too big to fit in the AVRs memory.

... except most projects don't need anywhere near that many pixels.
A 160x128 or 128x64 OLED is more practical and cheaper —
but these need hand-drawn, pixel-efficient fonts to make good use of them.

*For reference, here's a vector font* rendered at a similar scale:

![A screenshot of my computer displaying text at a tiny font size. It's a blurry mess.](https://maurycyz.com/projects/mcufont/vector.png)
Actually 6 tall, but the letters are narrower, so I'll allow it.

Antialiasing, several megabytes of code, a megabyte of font data, and it's still terrible compared 350 hand-crafted bytes.

Real *pixels*:
==============

Pixels aren't perfect squares, so the font won't actually look like the rendering at the top of this post:
This is it on an actual screen:

![A photograph of the font displayed on real hardware](https://maurycyz.com/projects/mcufont/real.jpg)

I actually really like the pseudo-dropshadow effect created by the subpixels.
This won't happen on monochrome displays, but the font will still look smoother than you might expect.

The gaps between pixels really help sell the "e" and "g", but this same effect should allow...

Even *smaller* fonts:
=====================

While 5x5 is the smallest no-compromise resolution, a 3x5 isn't too bad:

![](https://maurycyz.com/projects/mcufont/3x5.png)
There are 32,768 glyphs at this size. (27,904 are distinct)

The "M", "W" and "Q" suffer, but it's still got a distinct O and zero.
Something like this might actually be a good option if you need to cram (50%) more columns into a display.

That's still readable, so what about *3x4*?

![](https://maurycyz.com/projects/mcufont/3x4.png)
There are 4,096 glyphs at this size. (3,392 are distinct)

At this size, there's no way to have a distinct upper and lowercase, so I've picked whatever style works the best in the limited space.
The numbers have also taken a hit, but still work ok.

How about *3x3*?

![](https://maurycyz.com/projects/mcufont/3x3.png)
There are 512 glyphs at this size. (400 are distinct)

The main loss was the numbers, but the letters don't include any duplicates and are somewhat recognizable.

This font is hugely improved by being displayed on real hardware:

![](https://maurycyz.com/projects/mcufont/tiny.jpg)

That means it's still too big. How about *2x3*?

![](https://maurycyz.com/projects/mcufont/2x3.png)
There are 64 glyphs at this size. (44 are distinct)

Ok, this is getting ridiculous.
Most letters are unrecognizable, and there are quite a few duplicates.
In case you couldn't tell, the bottom line reads "Hello World".

Flipping the aspect ratio to a *3x2* makes it a lot better:

![](https://maurycyz.com/projects/mcufont/3x2.png)
There are 64 glyphs at this size. (44 are distinct)![](https://maurycyz.com/projects/mcufont/3x2_pixelsim.png)
Simulated pixel grid

More letters have horizontal detail (M, W, N, Q, G, P, etc) then have vertical detail (E, F).
The bottom line reads "you can probably read this", although you might have to squint or zoom out.

... and for the sake of completeness, a *2x2*:

![](https://maurycyz.com/projects/mcufont/2x2.png)
There are 16 glyphs at this size. (10 are distinct)

On paper, there are 16 possible 2x2 images, but one of them is blank and 5 of them are shifted copies of another one.
That leaves 10, just enough to do all the digits...
but because they have no resemblance to the originals, it's more of a secret code than a font.

*Related*:
==========