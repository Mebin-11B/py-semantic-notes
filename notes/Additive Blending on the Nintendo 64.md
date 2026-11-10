---
title: "Additive Blending on the Nintendo 64"
url: https://phoboslab.org/log/2026/05/n64-additive-blending
clipped: 2026-06-17 01:01:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - nintendo 64
  - computer graphics
  - game console hardware
  - render buffers
  - color blending
  - vector processor
related:
  - "[[WiiFin – Jellyfin Client for Nintendo Wii]]"
  - "[[Computer Graphics]]"
  - "[[Vector Processor]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An engineering analysis of why the Nintendo 64 lacked the bright additive blending of the PlayStation, and a technical workaround utilizing the console's vector co-processor.
>
> **Key points:**
> - The N64's RDP (Reality Display Processor) lacked native clamping for its additive blending mode, resulting in color overflow and wrap-around.
> - PlayStation games achieved bright explosions because the PSX GPU automatically clamped color additions to the maximum value of 255.
> - The author implements a solution by rendering sprites into a 32-bit RGBA buffer at reduced color scale, giving enough headroom to avoid overflow.
> - To make the method playable, the N64's vector co-processor (RSP) is used to accelerate the conversion of the 32-bit buffer back to 16-bit.
>
> **Concept links:** [[Nintendo 64]], [[Computer Graphics]], [[Game Console Hardware]], [[Render Buffers]], [[Color Blending]], [[Vector Processor]]
>
> **Suggested connections:**
> - [[WiiFin – Jellyfin Client for Nintendo Wii]] — another community-driven homebrew/open-source effort targeting constrained hardware.
> - [[Computer Graphics]] — the broader mathematics and algorithms of pixel rasterization and blending.
> - [[Vector Processor]] — low-level optimization using vector co-processors like the N64's RSP.
<!-- ai-summary:end -->
# [Additive Blending on the Nintendo 64](https://phoboslab.org/log/2026/05/n64-additive-blending)

## Digest Summary
The article explains why Nintendo 64 (N64) games lacked the bright additive blending seen on PlayStation titles. While the N64’s Reality Display Processor (RDP) supports configurable blending via a color combiner (similar to OpenGL’s glBlendFunc), its default additive mode does not clamp results, causing overflow and color wrap‑around. The author solves this by rendering to a 32‑bit RGBA 8888 buffer while keeping sprites in 16‑bit RGBA 5551 format, effectively scaling sprite colors down (right‑shifting 3 bits) to provide headroom for additive accumulation. A fog‑color trick inserts the required scaling in the combiner, and after rendering the scene the 32‑bit buffer is converted back to 16‑bit for display. Conversion is accelerated using the N64’s vector co‑processor (RSP) with 128‑bit instructions, reducing processing from ~70 ms to ~3 ms per 320×240 frame. The method yields correctly clamped additive effects without wrap‑around, at the cost of higher memory bandwidth; further optimizations could limit 32‑bit rendering to only additive sprites or lower resolutions. A demo implementation is available on GitHub.

## Discussion Summary
The comments express strong curiosity about the visual disparity between PlayStation and Nintendo 64 explosions, coupled with appreciation for explanations linking the difference to each console’s color‑blending and saturation handling. Readers note that PlayStation’s default processing often yields more striking effects, while the N64 can achieve comparable results when developers manually manage blending and clamping. The linked article and technical references are received positively, with participants acknowledging the insight and confirming the relevance of saturation arithmetic to the observed visual characteristics.

---

## Full Article

Additive Blending on the Nintendo 64
====================================

Did you ever wonder why explosions and other effects looked so much cooler on
the original PlayStation than they did on the Nintendo 64?

[](/content/assets/n64-blend/silent-bomber.mp4)

*“Silent Bomber“ for the PSX*

[](/content/assets/n64-blend/starfox.mp4)

*“Star Fox 64“ for the N64*

The reason is additive blending! Or rather, in the N64 case, the lack thereof. While
the N64 actually did support additive blending, it was practically unusable.

### PSX

The PSX supports 4 different blend modes (in addition to just overwriting
pixels) to control how sprites and geometry are mixed into the existing
frame buffer:

```
0: (src + dst) / 2
1: src + dst
2: dst - src
3: dst + src/4
```

The one you see here in Silent Bomber is conceptually the simplest one: `src + dst`.
That is, colors are just added to the existing ones in the frame buffer.

```
                      |   R |   G |   B |
|   src (sprite)      | 171 |  42 | 226 | 
| + dst (framebuffer) |  63 | 141 | 170 | 
| = result            | 234 | 183 | 255 |
```

Drawing a sprite over a scene can only ever make it **brighter**, never darker.
Perfect for explosions, plasma beams and magic spells. Importantly, note how
the `B` value in this example adds up to `396`, but the PSX GPU helpfully clamps
it to the maximum range of `255`.

(Aside: the PSX GPU actually only works in 16bit precision with 5bit color
components, so values range from `0 .. 31`; the math is the same.)

### N64

The N64's “Reality Display Processor” (the fixed-function rasterizer, short RDP)
has a much more flexible way to control blending: a configurable “Color Combiner”.
This is somewhat similar to OpenGL's `glBlendFunc()`.

[Libdragon](https://libdragon.dev/) exposes this functionality with the
`RDPQ_BLENDER((P, A, Q, B))` macro that instructs the RDP to execute
`(P * A) + (Q * B)`, where each *slot* can be one of several inputs.

Setting up additive blending with this is trivial:

```
RDPQ_BLENDER(( IN_RGB, IN_ALPHA, MEMORY_RGB, ONE ))
```

The problem is, the RDP doesn't clamp the result.

```
                      |   R |   G |   B |
|   src (sprite)      | 171 |  42 | 226 | 
| + dst (framebuffer) |  63 | 141 | 170 | 
| = result            | 234 | 183 | 140 | 
                                     ^
                                     wraps around!
```

The resulting output is less than desirable:

[](/content/assets/n64-blend/add-blend-16bit.mp4)

Now, you could of course fall back to draw such effects on the “Reality Signal
Processor” (RSP), the vector co-processor of the N64. But that gets complicated
quickly if you want to do rotation, scaling or any actual 3D stuff. The RDP
is much better suited for this. Displaying is its job!

While the RDP *can* draw into a 32bit buffer, it was very uncommon for games
to do so. Almost all N64 games used a 16bit framebuffer for the final output.
But with this in mind, I came up with a different plan:

Let the RDP draw onto a 32bit `RGBA 8888` (8 bits per component) buffer, but have
all our sprites in the 16bit `RGBA 5551` (5 bits per color component, 1 bit alpha)
range. I could just pre-process assets by dividing RGB by `8` (or right shifting
by `3` bits). This will essentially draw everything way too dark, but in turn
gives us lots of headroom for additive blending.

[](/content/assets/n64-blend/add-blend-32bit.mp4)

*No wrap around when all additive blended sprites result in less than 255*

Better yet, we don't have to do this image pre-processing offline. We can just
instruct the color combiner to do it for us when drawing. For free!

```
rdpq_set_fog_color(RGBA32(0, 0, 0, 256/8));
rdpq_mode_blender(RDPQ_BLENDER(( IN_RGB, FOG_ALPHA, MEMORY_RGB, ONE )));
```

So how do we get this back to normal brightness? Simple: use a 16bit frame buffer
for displaying and “copy” all the 32bit colors into it. We just have to be careful
to clamp all 8bit color components into the 5bit range.

```
void cpu_rgba_8888_to_5551(uint32_t *rgba32_in, uint16_t *rgba16_out) {
    for (int i = 0; i < 320 * 240; i++) {
        color_t c = color_from_packed32(rgba32_in[i]);
        if (c.r > 31) { c.r = 31; }
        if (c.g > 31) { c.g = 31; }
        if (c.b > 31) { c.b = 31; }
        rgba16_out[i] = (c.r << 11) | (c.g << 6) | (c.b << 1) | 0x1;
    }
}
```

Doing this on the CPU is of course prohibitively expensive. It takes about 70ms
for a 320×240 frame. But this is where the RSP co-processor shines. The problem
now became simple enough.

The RSP's 128bit vector instructions can process 8 pixels at a time. With
some help from HailToDodongo on the #N64Brew discord optimizing the GPU microcode,
this now runs in about 3.1ms for the whole frame!

(*Trivia*: I'd like to interject for a moment. What is commonly referred to as
“GPU microcode” in the context of the N64 is in fact, MIPS/assembly that runs
on the RSP, or as I've recently taken to calling it, MIPS plus assembly.)

Modern tooling for N64 development is phenomenal. While it helps to have
some understanding of assembly, you don't have to write MIPS assembly by hand
anymore. HailToDodongo invented a C-like language called [RSPL](https://github.com/HailToDodongo/rspl)
that directly compiles to it.

So the whole setup looks like this:

```
display_init(RESOLUTION_320x240, DEPTH_16_BPP, 3, GAMMA_NONE, FILTERS_DISABLED);

surface_t render32 = surface_alloc(FMT_RGBA32, 320, 240);
rdpq_set_color_image(render32);

rdpq_set_fog_color(RGBA32(0, 0, 0, 256/8));
rdpq_mode_blender(RDPQ_BLENDER((IN_RGB, FOG_ALPHA, MEMORY_RGB, ONE)));

render_scene();

rsp_rgba_8888_to_5551(render32->buffer, screen->buffer);

display_show(screen);
```

Resulting in lots of gloriously additive blended sprites without any wrap around
artifacts.

[](/content/assets/n64-blend/add-blend-rsp.mp4)

There was of course a reason that most games used a 16bit frame buffer to
begin with: the atrocious memory throughput of the N64. Drawing onto a 32bit
buffer takes almost twice the time compared to a 16bit buffer, because the RDP
has to shuffle twice the amount of bytes from and back to the frame buffer
stored in RDRAM.

Still, this technique worked out better than I expected. It's certainly good
enough for some applications.

I can also see further optimization potential by only drawing those sprites
that need additive blending to the 32bit buffer – maybe even at a lower
resolution — and then combine it with the rest of scene's 16bit buffer on the RSP…

A simple demo project for the above video can be found on github:  
[github.com/phoboslab/n64\_addblend](https://github.com/phoboslab/n64_addblend)