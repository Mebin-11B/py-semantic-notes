---
title: "My graduation cap runs Rust"
url: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/
clipped: 2026-06-17 01:03:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [My graduation cap runs Rust](https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/)

## Digest Summary
A blog post dated May 12 2026 describes a DIY graduation‑cap project that lights up when the tassel is moved. The author built the system using a Digispark ATtiny85 microcontroller, 48 WS2812B addressable LEDs, a reed switch with magnet for tassel detection, a USB‑C Power Delivery trigger board, and a power bank. The firmware was written in Rust, requiring forks and patches to the avr‑hal and ws2812‑avr crates to support the ATtiny85 at 16 MHz; this coding phase took roughly two hours, while hardware assembly took three-plus hours. The author notes that using Arduino libraries or a different board would have been simpler, but chose Rust for thematic consistency. The cap is not intended for actual graduation use, as it appears tacky. Source code is available on GitHub (ericswpark/gradcap-rs). Additional anecdotal notes include the cost of renting cap and gown ($94) and a warning about strobing video content.

## Discussion Summary
The comments blend humor, mild self‑deprecation, and occasional praise. Many readers joke about the expense and logistics of renting graduation robes, noting personal shortcuts like buying instead of renting, and express empathy for being broke. Several remarks reference the author’s choice to use Rust, mixing sarcasm about the language’s hype with light‑hearted admiration for the project’s execution. Overall sentiment is friendly and supportive, with a recurring theme of nostalgic reflection on past freedom and a subtle critique of broader software‑industry culture.

---

## Full Article

My graduation cap runs Rust
===========================

### May 12, 2026

I’ve never graduated before. I mean, from college. So all the cap and gown stuff
is new to me.

Fun fact #1: you rent your cap and gown in the US. You have to return them. And
they’re expensive, too! I paid $94 just for the privilege of renting mine, which
is insane because they probably cost way less than that to manufacture. What if,
say, you say you’re fine without a cap and gown? Well, then you can’t walk in
the ceremony. So you do need to shell out to rent them. And they don’t give you
the option to buy the cap and gown outright.

OK, that’s not such a fun fact. How about:

Fun fact #2: when you graduate, they move your tassel from right to left to
signify… something? Why not left to right? What about left-handed people?!
Why are graduation ceremonies discriminating against left-handed people?!

Anyway. I was thinking about fun fact #2, and then I thought it might be cool if
my cap lit on fire as whoever it is moves my tassel. But the rental agreements
clause 98.c.2 probably forbids it, and I don’t think Purdue would like it very
much if I set the stage on fire.

Hmm. What if I made a contraption that detects when the tassel is moved away and
light up the bottom-side of the cap?

And with that, I got to building this crazy idea. And the end result is
beautiful if I do say so myself:

VIDEO

FAQ
---

### What parts did you use?

* One Digispark ATtiny85
* 48 WS2812B LEDs
* Wires stripped from a dead Apple USB-C-to-C cable
* Reed switch and magnet to detect tassel movement (not shown in demo)
* A USB-C Power Delivery trigger board
* Power bank (and USB-C cable)

### How long did you spend on this thing?!

Writing the code took about 2 hours, mostly because `avr-hal` and `ws2812-avr`
do not support the ATtiny85 out of the box, at least not without a couple of
tweaks. I had to fork them and dirty-patch a couple of things, including setting
the default clock speed to 16 MHz.

It probably would’ve been easier if I didn’t use Rust and just used the Arduino
libraries, or if I used a different board. But I was really married to this blog
post title idea, and I was pretty sure a ESP32 board would’ve been overkill and
wouldn’t have stayed on the cap properly.

The hardware side took the longest, at 3+ hours. If anybody tells you hardware
is easy they’re wrong or they’re lying and have never worked on a custom
hardware project!

### Are you actually going to wear this to your graduation?

Heck no.

I thought about it but decided it looks pretty tacky. It looks like what kids
would think of as a gaming PC and what boomers would think of as a seizure.

### Speaking of seizure, there really was a missed opportunity…

…missed?

**Warning: the following video contains rapid strobing of light. I’ve written
this out so people who are reading this with a screen reader know not to watch
the video!**

VIDEO

[~~WKUK eat your heart out~~](https://www.youtube.com/watch?v=uQRIvXymJZI)

### Can I see the code?

<https://github.com/ericswpark/gradcap-rs>

---