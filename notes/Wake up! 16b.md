---
title: "Wake up! 16b"
url: https://hellmood.111mb.de/wake_up_16b_writeup.html
clipped: 2026-06-17 00:58:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Wake up! 16b](https://hellmood.111mb.de/wake_up_16b_writeup.html)

## Digest Summary
“wake up! 16b” is a 16‑byte real‑mode DOS demo presented at Outline Demoparty (May 2026). The program sets video mode 0 via INT 10h, points DS to the VGA text buffer (0xB800), and enters an infinite loop that loads a byte (LOD SB), subtracts 57 from SI (moving –56 bytes per iteration), XORs the loaded value with the memory cell at the new SI, outputs AL to port 61h (PC speaker), and jumps back. This loop simultaneously writes a Sierpinski‑triangle pattern into video memory and streams the same bitstream to the speaker, producing a self‑similar bytebeat. The algorithm relies on XOR as carry‑free addition, generating the binomial sequence 2·C(k+p, p‑1) mod 256; the least‑significant toggling bit follows elementary cellular automaton rule 60, yielding the fractal geometry. The –56‑byte step maps to a 10‑column visual shear on an 80‑column screen and creates an octave‑lower audio due to the 8 192‑step wrap in the 64 KB segment. The demo exploits the BIOS‑cleared video memory pattern (0x20 0x07) and hardware quirks for its sound and visual output without any explicit memory initialization.

## Discussion Summary
The comments express strong admiration for the remarkably compact binary, highlighting its technical elegance and artistic quality. Readers note the impressive reduction in size, referencing expectations of larger demos and even mistaking it for a 16‑byte implementation, and emphasize how the achievement reignites enthusiasm for programming and low‑level craftsmanship. The consensus celebrates the work as a standout example of minimalism, with many expressing a desire to replicate or explore it on additional architectures, and overall sentiment is overwhelmingly positive.

---

## Full Article

wake up! 16b
============

Released at the Outline Demoparty in May 2026, Ommen, NL  
An exploration of algorithmic density in 16 bytes of x86 assembly.

Hey everyone. I learned programming as a kid on an old IBM PC with a monochrome green monitor over 30 years ago and always wanted to create a program for this system. I created well over 100 tiny intros in the last 15 years. Recently I was not too active but the fantastic "Rainbow Surf" from Plex in just 16 bytes motivated me to dig up some old dusty sketches again and get to work.

The creation of this program happened with the usual tinkering around. I was messing with cellular automaton for graphics and sounds and discovering sizecoding tricks. Actually: a) polymorphic asm instructions, like `add [bx+si],al` which is `0x0000` b) jumping into the middle of instructions to save bytes and reuse opcodes. In hundreds of tiny experiments, this one stuck out, just by the sound of it.

When I unfolded what's left and removed "the rest", I had a hard time to grasp what's really going on. I was scratching my head looking at the simple formula that remained after golfing many bytes away. I myself didn't expect that the explanation would go this deep for just these few bytes xD.

My original "M8trix" from 2014 already did smear pseudorandom letters across the screen (in 8 bytes, then in 7) and I always wondered how I could make it "sound good". But chronologically in the development of "wakeup", the sound was first. Since you "see what you hear" it doesn't really matter, but "16 bytes that turn Sierpinski sound into Matrix rain" would be a good subtitle =)

**TLDR:** Each time step, another Sierpinski triangle line is a) played on the speaker b) drawn to the screen with a stepsize of 56. You can sense the motion, but not really see it, since it's 8192 "pixels wide" but one line of chars is just 80 bytes. On a much much much bigger screen, you could see the triangle. Or, if you don't "skip pixels" and draw it all at once, you would see it as well.

So, here are the **16 bytes** of x86 real-mode DOS assembly. When you run it, it uses the video memory as a calculation space to draw an infinite Sierpinski fractal, and at the same time bangs the speaker with that geometry.

```
int 10h          ; 2 bytes
mov bh, 0xb8     ; 2 bytes
mov ds, bx       ; 2 bytes
L:
lodsb            ; 1 byte
sub si, byte 57  ; 3 bytes
xor [si], al     ; 2 bytes
out 61h, al      ; 2 bytes
jmp short L      ; 2 bytes
```

1. The Canvas: A Primed Void
----------------------------

The code starts with a standard BIOS interrupt: `int 10h`. This sets up video mode 0, giving a 40x25 text mode grid. Then the data segment (`ds`) is pointed to `0xb800`, the memory address of the VGA/CGA text buffer.

When the BIOS clears the screen, it doesn't fill memory with absolute zeroes. Every character space is two bytes: the ASCII character and the color attribute. All 2,000 slots are set to **`0x20`** (space) and **`0x07`** (light gray on black). So the screen looks empty, but the memory is already filled with a uniform pattern.

I created a lot of "noise" or "CA" sound intros but this one stands out. It was and is still super unexpected! The specific spice here is how memory is initialized on "clear screen" and what's "before" and "after" the actual visible memory. The "pure" sound is also lovely (I can carefully set everything with a few more bytes to make it sound the same on all systems) but this spicy difference I still have to fully understand makes it sound even better imho =)

2. The Engine: Additive Prefix Sums
-----------------------------------

The intertwine, the synesthesia goes far beyond what I found so far in other tiny intros. I would even go so far as to say it's revealing more mathematical secrets and relations than using iterated function systems for the "chaos game" without an RNG. Anyway, this time I want you to fundamentally understand the mathematics of what you hear. Not just "you do some operation here and then it sounds interesting".

To strip it down to pure math: assume a zeroed state instead of `0x20`, use `add` instead of `xor`, and step forward **16 bytes** at a time. Assume the accumulator `al` starts at **2**.

A DOS segment is exactly 65,536 bytes. Moving 16 bytes per step means exactly **4,096 steps** to traverse the segment (\( 65536 / 16 = 4096 \)). Then `si` wraps cleanly back to `0x0000`.

Adding up values between cells creates partial sums. Because 4,096 is a multiple of 256 (the 8-bit register size), the carryover aligns perfectly when the segment wraps, cleanly resetting `al` to 2 at the start of each sweep.

The value follows a binomial sequence, scaled by 2:

$$A^{(p)}[k] \equiv 2 \binom{k+p}{p-1} \pmod{256}$$

Here is how the first 16 steps accumulate row by row:

3. Crystallization: XOR and the Sierpinski Shift
------------------------------------------------

Now, back to combinatorics. By special laws, when doing modulo two, the Sierpinski triangle emerges. This specific bit is what gets banged into the speaker, while the other bits are ignored.

To separate the bitplanes, the fact that carry-free addition of bits is **XOR** is why it is there instead of `add`.

Since the code starts with 2 (binary `00000010`), **only bit 1 is toggled** between `0x00` and `0x02`. This perfectly maps to **rule 60** in elementary cellular automata:

$$Cell^{(p)}[k] = Cell^{(p-1)}[k] \oplus Cell^{(p)}[k-1]$$

Lucas's theorem guarantees this matches bit 1 from the addition table. See for yourself ('2' means bit 1 is set):

4. The Voice of the Machine: Translating Data to Audio
------------------------------------------------------

Here is the trick: `out 61h, al`

Port `61h` interfaces with the PC speaker. **Bit 1** pushes the speaker cone out (1) and pulls it in (0). The code computes the fractal via XOR, writes it to memory, and shoves that byte straight into the speaker port.

The 1s and 0s from the fractal create square waves that shift naturally in pulse width and frequency:

When played linewise, this creates self-similar, almost tempo-invariant bytebeats.

But it gets better: not only the text is output to the speaker but also the remaining bytes of the 64 kilobyte segment, which in this case also contains shadowed video ROM BIOS code, which is the secret ingredient to the punky and gritty sound that differs quite a bit from the expected Sierpinski line based overlayed rectangle wave bytebeat.

5. The 56-Byte Step: Octave Shifts and Diagonal Shears
------------------------------------------------------

To recreate the M8trix effect, the cells themselves have to be splat across the screen in a way that the sound buffer is not too large and the screen is nicely sparsely filled with chars.

So the code doesn't step by 16. `sub si, byte 57` plus `lodsb` means it moves **-56 bytes** per iteration - going backwards.

### The Audio

56 doesn't divide 65,536 evenly. The code only hits offsets that are multiples of 8, taking **8,192 steps** and wrapping 7 times before resetting. This doubles the cycle length, halving the fundamental frequency. The sound drops one octave.

### The Visuals

Moving back 56 bytes on an 80-byte wide screen is like moving forward 24 bytes (12 columns). Only 10 distinct columns are visited. The fractal isn't drawn as a solid image; it shears diagonally into 10 pillars of characters moving up the screen.

6. Real Hardware and Final Thoughts
-----------------------------------

The scener *miragept* did a capture with this motivation:

> "This is so awesome that I had to try running it in real hardware. The green text is a natural fit for MDA/Hercules, so I patched the address from 0xB800 to 0xB000 which is what MDA uses.  
> I don't have the exact IBM computer, but used a 286 with EGA card capable of emulating MDA/Hercules, and a real MDA monitor, so it's close enough.  
>   
> Sorry for the low quality audio (the constant noise is from the machine itself). Please note that this monitor (IBM 5151) has a HUGE phosphor persistence, which I think hurts the presentation in this case because it's very fast."

My reply to him:

> "HellMood @miragept: Thank you so much for this ♥ I'm happy to see it works like intended, even with a slightly different sound due to the byte change. Maybe it would indeed be a bit better to have it run slower, but what I found remarkable is, that the Sierpinski structure becomes actually more visible (towards the end) than in my version =)"

Emulators and different BIOS versions leave slightly different artifacts in RAM. Since the code XORs against whatever is there, the output is highly sensitive to the environment. Clearing the memory first would give a perfectly uniform output, but that costs precious bytes. Embracing the hardware's natural state is just part of the charm of sizecoding. Thanks for reading.

This text is handwritten.