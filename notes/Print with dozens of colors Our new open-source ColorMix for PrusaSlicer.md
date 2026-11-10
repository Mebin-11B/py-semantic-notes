---
title: "Print with dozens of colors: Our new open-source ColorMix for PrusaSlicer"
url: https://blog.prusa3d.com/our-new-open-source-colormix-model-in-prusaslicer-and-easyprint_136079/
clipped: 2026-06-17 00:55:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Print with dozens of colors: Our new open-source ColorMix for PrusaSlicer](https://blog.prusa3d.com/our-new-open-source-colormix-model-in-prusaslicer-and-easyprint_136079/)

## Digest Summary
Prusa has released an open‑source “Prusa ColorMix” model that enables multi‑material FDM printers to reproduce dozens of colors using only five filaments (Cyan, Magenta, Yellow, Black, White). The approach adapts traditional CMYK halftoning: colors are mixed by alternating thin layers rather than dots, relying on the eye’s limited resolution to blend adjacent layers. A calibrated Yule‑Nielsen‑based algorithm predicts resulting colors; systematic errors (darkening of light‑dark mixes, saturation loss, cyan hue drift) are corrected with lightness‑scaled adjustments derived from measured test cards. Calibration is performed per batch using a consumer colorimeter on five base filaments and 20+ mixes, ensuring consistency without expensive spectrophotometers. The model, licensed under MIT, is integrated into PrusaSlicer 2.9.6 and EasyPrint, with a dedicated CMYKW filament set (Prusament) and tools for creating and testing mixes. Source code and a TypeScript/C++ port are on GitHub, and the community is invited to contribute additional measurements for broader material support.

## Discussion Summary
The comments express overall enthusiasm for the new color‑mixing capabilities, viewing them as a strong competitive step for Prusa and anticipating broader adoption across slicers. Several contributors request expanded color support, including six‑color systems, and a mechanism to preview arbitrary filament blends. Criticism centers on the Prusa cone model’s design, which is seen as less effective than dome‑shaped testers, and on the perception that Prusa repackages community innovations without sufficient attribution. Nonetheless, the community’s existing tools and databases are acknowledged as valuable resources.

---

## Full Article

Estimated reading time: 12 minutes

For the past few months, the 3D printing community has been poking at a very interesting question: what if a multi-material printer were not limited to the colors physically loaded on it?

And we must say it right now: This is a really awesome way to expand your 3D printing capabilities! In this article and video, we’ll show you **how to print with dozens of color tones on any multi-material printer** and how we made that possible. It’s a proper deep dive, so get comfy – you’re in for a ride!

Let’s talk about the community – because that’s where it started. Solutions started appearing in slicer forks, test palettes, and increasingly convincing prints. **Ratdoux’s OrcaSlicer-FullSpectrum** showed how virtual mixed-color filaments could be created by **alternating** thin **layers** of differently colored materials. Justin H. Rahb’s **filament-mixer** helped predict what those colors might look like, and community projects like **PeggyPalette** made it easier to compare and share results. It was one of those moments where you could feel an idea catching fire in real time. These projects are all amazing and truly demonstrate the benefits of an open-source approach.

VIDEO

And honestly, we got excited too. Inside Prusa, the idea spread fast: let’s create an easy way to take a couple of filament spools and let people **print in dozens of beautiful colors.** The teams working on [Prusament](https://prusament.com/), [PrusaSlicer](https://www.prusa3d.com/p/prusaslicer/), [EasyPrint](https://www.printables.com/slice), and [OpenPrintTag](https://openprinttag.org/) are always pulling in the same direction, and this was the perfect project for them. We calibrated a new, more accurate color mixing model against measured FDM prints, connected it to real material data through the **OpenPrintTag Material Database**, brought the workflow directly into **PrusaSlicer** and **EasyPrint**, and started preparing a dedicated **Prusament CMYKW** set to make the whole process more reliable from the first print. Why CMYKW? We’ll explain in a second.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/7945ae91-easyprint-colormix-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/7945ae91-easyprint-colormix-scaled.jpg)

The result is a much easier workflow that makes printing in color feel more like painting rather than programming, with more accurate color previews than any existing solution.

Our color mixing model is **published under the MIT license,** so the community can inspect it, use it, test it, improve it, and build on it just like we built on the work that came before us. We call the model **Prusa** **ColorMix** to distinguish it from similar projects and products.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/9ee1a42b-colored_prints-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/9ee1a42b-colored_prints.jpg)

How does it work?
=================

So, how is it possible to print a model that looks almost painted – using just five filaments?

The principle is well-known from traditional 2D printing. It uses **Cyan, Magenta, and Yellow** (CMY) inks in a method called **Halftoning**, which allows a printer to produce continuous tones by varying the size and spacing of small ink dots. Printing CMY dots in equal size ratios creates black. Inkjet printers have an additional black (K) ink to save on ink and use the **CMYK color model**. They usually print on white paper, so white is just the absence of any printed color.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/61783e3c-halftoning_theory-1024x341.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/61783e3c-halftoning_theory.jpg)

*A color perceived as cerulean is a blend of cyan, magenta, yellow, and black inks, as observed under magnification. (Wikipedia)*

In 3D printing, there is no paper, so the existing models work with CMY colors and white (W). Because of the nature of FDM printing, we don’t use a combination of dots, but we **alternate the colors by layer**. A model with a 0.1 mm layer height that has all odd layers white and all even layers black appears grey from a normal viewing distance. This neat trick is possible because of the limited resolution of the human eye, which can’t see details below a certain size. Mixing the CMY colors is predictable because it is known from 2D printing.

### Behind the scenes

Let’s hear about the Prusa ColorMix from the people who worked on bringing it to you.

**Meet Barbora Marsikova**, from the team of Prusa Academy, who fell for the full spectrum on the way to bringing multi-material printing to 3D printing beginners.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/608b48cf-barbora-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/608b48cf-barbora-scaled.jpg)

### Why I started this

I first heard about Full Spectrum from our multi-material expert from Prusa Development. When he said this is the future, I believed him. I kept an eye on the community trying out the existing fork and used every opportunity to internally promote it. But it really took off once we started printing test samples with the Easy PLA CMYK Filament Set and the [Prusament Galaxy Black](https://www.prusa3d.com/product/prusament-pla-prusa-galaxy-black-1kg-nfc/) on the [Original Prusa XL](https://www.prusa3d.com/en/product/original-prusa-xl-5-toolhead-3d-printer/). Because everyone who saw it wanted it.

Most available multi-filament systems use four spools in parallel and therefore work in the CMYW mode. But the color mixing never produces a truly black color, more like blueish grey. On the 5T **Prusa XL**, we were able to directly add black and work with the **CMYKW color combinations**. By trying out all of them, we identified about 40 color combinations that make sense.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/6753474a-chameleon-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/6753474a-chameleon-scaled.jpg)

We also easily agreed that we would love to have our own Full Spectrum for the [Prusa CORE One INDX](https://www.prusa3d.com/product/indx-conversion-kit-8-toolhead/). To have a Prusa solution, there were three key teams to get on board: Prusa Polymers, EasyPrint, and PrusaSlicer.

### Everybody Loves Color

Prusa Polymers, where the in-house manufactured Prusament comes into existence, didn’t need much persuading. Before we finished testing the CMYKW filaments available on the market, they were already working on the **new Prusament colors**. Right now, they are tuning the final shades and transparency of the Prusa CMYKW bundle and even preparing **PLA Natural Glitter**, which can add a glittery look to any existing PLA.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/f72d74c3-spools-1024x683.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/f72d74c3-spools.jpg)

The PrusaSlicer team is working hard on the upcoming PrusaSlicer 3.0 and, at the same time, finalizing CORE One INDX profiles to deliver the best possible performance. They borrowed the test prints cautiously but soon realized how much fun this is. So they happily became part of the movement and were eager to prepare a build for **version 2.9.6** already.

The biggest leap forward came when we paid a visit to the EasyPrint & Printables team. They literally dropped (almost) everything and immediately started discussing how to implement the **CMYKW slicing in EasyPrint** and get it out there as fast as possible.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/b54e336d-easyprint_colors-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/b54e336d-easyprint_colors.jpg)

So, we had both the EasyPrint and PrusaSlicer teams fully on the case, and new features started popping up in the test environment every other day. When the first test batch of Prusament CMYKW arrived, we were able to leave behind all other software implementations of the Full Spectrum and work purely in the Prusaverse.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/ff672eaf-prusaslicer-1024x554.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/ff672eaf-prusaslicer.jpg)

### Developer’s diary

**Meet Ondrej Bartas**, software engineer from the Printables & EasyPrint team and the main developer behind the ColorMix model.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/1bc4458a-ondrej-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/1bc4458a-ondrej.jpg)

What we learned trying to mix colors on a 3D printer
====================================================

These are my notes on building a color mixing model for layer-interleaved FDM. We’re sharing this because we want to **help the community** adopt full-spectrum printing, not because we’ve solved color mixing.

### Why I started this

I want multicolor FDM printing to **feel like painting**. You squeeze tubes onto a palette, you grab a brush, you mix. The colors are right there in front of you.  
It doesn’t feel like that in any slicer today. In Orca and Bambu, if you want a non-base color, you click “add mixed color combination,” pick which two extruders to mix, set a ratio, and repeat for every color. There are preset 3MFs floating around the community that skip this, but they’re workarounds. The underlying experience is still “configure machinery first, see colors second.”

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/943abb25-slicer_painting.gif)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/943abb25-slicer_painting.gif)

So we’re building two things into PrusaSlicer and Prusa EasyPrint: a color-mixing model that **predicts what color** you’ll actually get when you interleave layers and a **UI** that gets out of the way. Load filaments, the palette appears, paint.

This post is about the color model.

### How we got here

We didn’t invent multicolor FDM via layer stacking. Ratdoux did, with OrcaSlicer-FullSpectrum. They also vendored Justin H. Rahb’s filament-mixer, a polynomial pigment-mix model trained on Mixbox (oil paint) to predict the resulting colors. Bambu Studio iterated through linear sRGB, then gamma-corrected RGB, and in April 2026, vendored a filament-mixer directly.

We’re showing up with PrusaSlicer and EasyPrint integration now. We got to look at what was available, print our own test cards, and notice something nobody had done yet: the **actual calibration of a model against measured FDM prints**. Filament-mixer predicts oil paint behavior.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/e52bc3fa-printed-samples-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/e52bc3fa-printed-samples-scaled.jpg)

It’s good at what it was trained on; it just wasn’t trained on filament.  
So that’s the gap we’re filling: we ran necessary measurements, and we applied corrections to those measurements.

### What didn’t work

* **Kubelka-Munk.** The canonical pigment-mixing model from paint science. It assumes pigments stirred together in one medium, but no consumer FDM printer does that. Bambu AMS, Prusa MMU, Prusa XL and INDX – they all swap filaments per layer. K-M solves a different problem.
* **Beer-Lambert / HueForge stacking.** This is the one I almost shipped. HueForge stacks translucent layers and looks down through them. Light passes through the top, hits the bottom, and comes back. Then I caught it: HueForge looks at flat prints from above. We’re looking at 3D objects from the side. Layers are adjacent, not stacked in the light path. Different geometry.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/3ac3df7d-easypyrint_filaments-1024x782.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/3ac3df7d-easypyrint_filaments.jpg)

### What worked

This is halftone printing, not paint mixing. Once I got that, the physics got simpler. Side-view multicolor FDM is spatial optical mixing – adjacent thin layers blending in your eye at viewing distance. Same family as printing CMYK ink dots. The right starting formula is **Yule-Nielsen**, the standard halftone equation. Yule-Nielsen alone is already roughly twice as good as plain linear-RGB averaging.  
The ratios (in %) are 75:25, 50:50, 25:75, and 33:33:33. Not arbitrary. Layer-interleaved mixing isn’t continuous, it’s discrete layers. A 50:50 mix alternates one of each. To get 30:70, you’d need a 3:7 repeating block, ten layers per “pixel” of color, which eats vertical resolution and visibly stripes. So the **printable ratios are 1:1, 1:3, and 3:1 layers**, and for **three colors,** there is a **balanced ratio, 1:1:1**. That’s what we measured, because that’s what the printer can actually produce.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/9e35b5aa-colormixing-painting_and_gcode-1024x512.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/9e35b5aa-colormixing-painting_and_gcode.jpg)

Both toolchangers and MMU/AMS work. Toolchangers (Prusa XL, CORE One+ INDX) are fast but need an **accurate XY offset** between nozzles. With an inaccurate offset, the color of the printed object is inconsistent. MMU/AMS (Bambu X1C, Prusa MK4S+MMU) has one nozzle, so no offset to worry about, but every color change is a purge cycle. The model doesn’t care which architecture you have. It predicts what color you get from a ratio of layers.[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/d61a5fff-mmu.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/d61a5fff-mmu.jpg)

### The correction stack

Once we had measured prints, the residuals from Yule-Nielsen showed structured errors. Predictable patterns, not noise. So we picked them off:

* **Real prints come out darker** than the math says, especially when mixing a very light filament with a very dark one. The bigger the lightness gap between inputs, the darker the actual print is than predicted. We pull the prediction’s lightness down accordingly.
* **Bright mixes lose color faster** than dark mixes. A 50:50 mix of pastel pink and pastel blue comes out greyer than expected. Two dark colors hold their color better. We scale saturation down based on prediction lightness.
* **Cyan mixes drift slightly warm.** Surprise finding. Predictions in the cyan-blue range (180-240 hue) lean toward teal when they should be cyan. We rotate them back, strongest at the middle of the band.
* **Don’t over-correct** mixes that are mostly one filament. A 99/1 mix barely needs correction. So all the corrections above get scaled by a bell-curve weight that peaks at uniform mixing and drops to zero at pure components. Pure colors round-trip exactly. Gradients stay smooth. As a bonus, this also fixes three-color mixes for free – every other model collapses on three colors; ours degrades gracefully.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/7c31b677-indx_samples-1024x684.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/7c31b677-indx_samples.jpg)

Each batch reprints its own bases. Methodology choice that mattered more than expected. Every batch of test cards includes the five base filaments printed solo plus 20+ mixes, all measured on the same colorimeter in the same session. Why: colorimeters drift, lighting varies, operators differ. If the device is reading off with a certain shift on cyan today, it’s also off on every cyan-containing mix in the same batch. The systematic error cancels when the model fits the relationship between the base and the mix, not the absolute values. So you don’t need a $5,000 spectrophotometer. A consumer colorimeter is fine as long as bases and mixes get measured together.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/68477c4f-colorimeter-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/68477c4f-colorimeter.jpg)

We also tested adding TD (transmission distance) values from the HueForge filament library as a model input. It didn’t help. So we kept the model simple: hex colors and ratios.

### What we know vs. what we don’t

We measured Prusament PLA on a Prusa XL. That’s it.

The structure of the corrections should hold across PLA brands, because pigment chemistry is similar across the industry. The Yule-Nielsen base should hold for any “swap filaments per layer” architecture. What we don’t know: whether the exact coefficients are right for PETG, ABS, or non-Prusa PLA (probably not exactly, probably close), and how special-effect filaments (bronze, glitter, galaxy) behave. Their orientation-dependent reflectance breaks any scalar model. They sit in our worst-error tail.

If the model predicts wrong on your filaments, that’s a data problem, not a model problem. We **need more measurements**.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/401002b3-models-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/401002b3-models.jpg)

### What’s next, and how to help

The **ColorMix model** we shipped is a first step. With a few hundred more measurements across brands and materials, there’s a real path to a proper perceptual colorspace model in the spirit of Mixbox or Spectral.js – predictions that are correct by construction across the full ratio space, not patches on residuals. None of this is hard. The math exists. It’s a data problem.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/d5bb6836-color_model-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/d5bb6836-color_model.jpg)

The repo is [prusa3d/prusa-fdm-mixer](https://github.com/prusa3d/prusa-fdm-mixer)., it runs as an [app](https://prusa3d.github.io/prusa-fdm-mixer/). **MIT licensed**. TypeScript (npm install prusa-fdm-mixer) and a C++17 single-header port designed to vendor straight into PrusaSlicer or OrcaSlicer. Three browser apps: a Playground, a Harness for scoring the model, and a Gatherer for entering your own LAB measurements.  
If you have a colorimeter and some test cards, **send us data**. If you predict a mix and it doesn’t match, tell us. Wrong predictions are how the model gets better.

The model is connected to the

[OpenPrintTag Material Database](https://database.openprinttag.org/)

. From there, it gets information about the filaments. As the database grows and

**OpenPrintTag**

gets adopted and widely used, there will be more data for the model as well. The model is not dependent on the CMYKW filaments, it predicts a mix of any materials that you assign while painting.

Both OpenPrintTag and the color-mixing model are open-source under the MIT license and published on GitHub.

### One more thing

Let’s Go back to the painting thing for a second. My 4-year-old paints with everything. Hands, clothes, the toys, sometimes the wall. There’s no menu, no setup wizard, no “configure your extruder mapping.” There’s blue, there’s yellow, there’s a brush somewhere that’s been abandoned for fingers, and green just happens.

Multicolor FDM should feel like that. Not in some distant future. Now. The hardware exists. The slicers exist. The filaments exist. The only thing in the way is a UX that treats color as an afterthought and a model that lies about what the print will look like. We can fix both.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/8f862222-ezgif.com-resize.gif)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/8f862222-ezgif.com-resize.gif)

This isn’t going to take over functional printing. Single-color PETG, ABS, ASA, and PA will keep doing their job because the job is mechanical, not visual. That’s correct. But for the fidgets, the toys, the cosplay props, the figurines, gifts, desk decorations, the things people print because they want to make something cool – that whole world has been stuck on single-color PLA for too long. A printed dragon in actual dragon colors. A puzzle box with a real gradient. A nameplate that doesn’t look like a nameplate.

Help us get there.

Let’s go paint something.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/2ca343f6-dragons.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/2ca343f6-dragons.jpg)

Back to your printer
====================

That was a deep dive into the development of the **Prusa ColorMix**. As a summary, you can now use both **EasyPrint** ([guidelines](https://help.prusa3d.com/article/easyprint_898029) are available on the help page) and **PrusaSlicer 2.9.6** ([released](https://github.com/prusa3d/PrusaSlicer) on GitHub) to slice ColorMix models for any printer with multi-filament capabilities. The colors you see on the screen when you assign them to parts of your model are as close as possible to the real printed colors. The use of the painting tools is about as difficult as in Windows Paint (ideal for the 90s kids).

If you’d like to try the ColorMix right now, we have a few models prepared for you: the [ColorMix Calibration Cones](https://www.printables.com/model/1726525-colormix-calibration-cones), for testing the possible combinations of your available filaments; the [colorful chameleon](https://www.printables.com/model/1734124-colormix-chameleon) that uses five filaments; and the [shaded fish](https://www.printables.com/model/1734108-colormix-shady-fish) that uses two colors.

You can also try creating your own shaded models directly in your browser using this [ColorMix Shading app](https://gzeus.github.io/Color-Mix-Shading/) we’re working on.

New **Prusament CMYKW colors are coming soon**, but you can also mix any filaments you have at home. To experiment with CMY mixing already, you can use Prusament [Azure Blue](https://www.prusa3d.com/product/prusament-pla-azure-blue-1kg-nfc/), [Ms. Pink](https://www.prusa3d.com/product/prusament-pla-blend-ms-pink-1kg-nfc/), and [Pineapple Yellow](https://www.prusa3d.com/product/prusament-pla-pineapple-yellow-1kg-nfc/). Feel free to **test any filaments you have at home** and let us know how it turned out.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/8a4e5ca0-shady-fish-1024x576.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/8a4e5ca0-shady-fish-scaled.jpg)

Final brushstroke
=================

Many of us here at Prusa are a little bit like Ondrej’s 4-year-old kid. We enjoy 3D printing ourselves, we like new features and innovations, and we want solutions for our own projects. Thanks to that, we were able to prepare the ColorMix, our own Full Spectrum implementation, in what felt like no time. Behind it is the work of many people across the company, so many thanks to them for joining the movement the moment they saw the first Full Spectrum print. Of course, we don’t abandon it here, but we’ll look into the unsolved questions, like efficient **gradients** and **top layer mixing**. We also keep working on ways to use these features to create more lifelike models, not just rainbows.

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/94439eb8-mushrooms_shading-1024x1024.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/94439eb8-mushrooms_shading.jpg)

Last but not least, **huge thanks to the community** team that brought so much attention to the feature: @ratdoux, @justinh-rabh under https://github.com/justinh-rahb, as well as @wombley for their filament-mixer library and @huntercook for his work on the peggypalette.

Happy painting!

[![](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/95c00df6-indx_cmykwrgb-1024x684.jpg)](https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-blog-prod/2026/05/95c00df6-indx_cmykwrgb.jpg)