---
title: "A few interesting modern pixel fonts"
url: https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/
clipped: 2026-06-17 00:56:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A few interesting modern pixel fonts](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/)

## Digest Summary
Andrew Gleeson’s Analog Mono addresses the low‑baseline issue of the classic 1990s VCR‑style pixel font, raising descenders for better legibility. Kumiko Yoshida’s Coral Pixels, available on Google Fonts, is a color font that embeds the nostalgic sub‑pixel fringing once produced by chromatic aberration, using it as a stylistic element. Joseph Fatula’s Two Slice is a functional 2‑pixel‑tall font that remains marginally readable despite its extreme height constraint. All these are vector‑based fonts designed for modern operating systems while emulating pixel aesthetics. Geist Pixel, released by Vercel, is presented as a system‑level extension rather than a decorative novelty; it includes carefully tuned kerning, metadata, extra glyphs, and consistent vertical metrics to ensure proper scaling across viewports and seamless integration with existing typographic systems, overcoming typical production issues of traditional pixel fonts.

## Discussion Summary
The comments revolve around pixel‑style typefaces, noting historic differences in display aspect ratios and the impact on rendering older fonts on modern screens. Contributors share several recommended bitmap fonts, praise the readability of Analog Mono, Two Slice, Departure Mono, and classic options like 04b‑03 and Spleen, while critiquing others such as Geist and Coral Pixels for poor legibility or aesthetic choices. Advice on creating custom fonts with tools like FontForge appears frequently, and there is a recurring appreciation for nostalgic, low‑resolution design balanced with practical readability concerns.

---

## Full Article

Andrew Gleeson designed [Analog Mono](https://gleeson.itch.io/analog-mono), âfixing the crimes of VCR OSD Mono.â There used to be this classic pixel font that youâd see everywhere in the 1990s on hi-fi equipment: VCRs, TVs, camcorders, etc. One of its challenges was a low baseline which resulted in all the letters with descenders pulled up, for example:

![](https://unsung.aresluna.org/_media/a-few-interesting-modern-pixel-fonts/1.1088w.avif)

Analog Mono fixes that problem:

![](https://unsung.aresluna.org/_media/a-few-interesting-modern-pixel-fonts/2.1088w.avif)

Elsewhere, Kumiko Yoshida made [Coral Pixels](https://github.com/tanukifont/Coral-Pixels) (also on [Google Fonts](https://fonts.google.com/specimen/Coral+Pixels?preview.script=Latn)), a color font that comes with the 1990s and 2000s colorful fringing baked in. The fringing was once an artifact of subpixel rendering, but now it is meant to evoke nostalgia or just as an interesting visual element in and of itself. (Perhaps adjacent to chromatic aberration?)

![](https://unsung.aresluna.org/_media/a-few-interesting-modern-pixel-fonts/3.1088w.avif)

Lastly, [hereâs Two Slice](https://joefatula.com/twoslice.html) by Joseph Fatula â a font thatâs only 2 pixels tall, âand somewhat readable.â

![](https://unsung.aresluna.org/_media/a-few-interesting-modern-pixel-fonts/4.1088w.avif)

Of course, these are all vector fonts â e.g. ready to be installed on a modern operating system â pretending to be pixel fonts. Thatâs maybe a separate post altogether, but it leads us to the last font, [Geist Pixel from Vercel](https://vercel.com/blog/introducing-geist-pixel):

![](https://unsung.aresluna.org/_media/a-few-interesting-modern-pixel-fonts/5.1088w.avif)

The copy introducing the font is a little pretentious/​spicy, but it touches upon something important:

> Geist Pixel isnât a novelty font. Itâs a system extension. [â¦ It] was designed with real usage in mind, not as a visual gimmick, but as a functional tool within a broader typographic system. [â¦] This matters because pixel fonts often break in production. They donât scale properly across viewports, their metrics conflict with existing typography, or theyâre purely decorative. Geist Pixel was built to solve these problems, maintaining the visual texture teams want while preserving the typographic rigor products require.

There *are* definitely fonts whose Achillesâ heel is not the letterforms, but the invisible hard work put into everything that surrounds them: the kerning, the metadata, the extra glyphs, the vertical metrics. It seems that the team being Geist Pixel is proud of especially that last part.