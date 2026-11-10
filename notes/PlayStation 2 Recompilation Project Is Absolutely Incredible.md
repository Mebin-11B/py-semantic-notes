---
title: "PlayStation 2 Recompilation Project Is Absolutely Incredible"
url: https://redgamingtech.com/playstation-2-recompilation-project-is-absolutely-incredible/
clipped: 2026-06-17 01:51:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [PlayStation 2 Recompilation Project Is Absolutely Incredible](https://redgamingtech.com/playstation-2-recompilation-project-is-absolutely-incredible/)

## Digest Summary
The article describes PS2Recomp, a static recompiler and runtime tool that translates PlayStation 2 games—originally built for the Emotion Engine (a MIPS R5900 CPU with two Vector Units, ~300 MHz, 32 MB RAM, and a 147 MHz Graphics Synthesizer with 4 MB eDRAM)—into native executables for Windows or Linux. Unlike emulators such as PCSX2, which run the original binary in a virtualized environment, recompilation produces platform‑specific code, potentially offering higher frame rates, lower hardware requirements, and easier integration of HD texture packs without breaking physics or collision detection. The author cites successful N64 recompilation projects (e.g., Mario 64 RTX, Zelda enhancements) as precedents. Anticipated outcomes include native PC versions of titles like Metal Gear Solid 2, Gran Turismo, God of War, and Tekken 4, with support for modern controllers and additional features. The project is still under development, but its progress is presented as a significant step toward game preservation.

## Discussion Summary
The response expresses strong enthusiasm for preserving and experiencing classic PlayStation 2 titles, viewing emulation and recompilation as significant advances for game preservation while acknowledging that native ports could offer a complementary, though potentially less faithful, option. It highlights technical challenges such as PS2 floating‑point behavior and self‑modifying code, and notes legal concerns about intellectual‑property enforcement. The tone is generally positive about modern hardware’s capability to run legacy games, yet critical of the article’s technical depth, formatting errors, and limited coverage of only a few titles.

---

## Full Article

The PlayStation 2’s library is easily among the best of any console ever released, and even if you were to narrow down the list of games to the very best, you’d be left with dozens (more like hundreds) of incredible titles.

But the PS2 hardware is getting a bit long in the tooth, and even though you can hook up the console using RGB component cables to a great upscaler (or use other means) to get the best visuals on a modern 4k TV, emulators have grown in popularity with PCSX2 offering gamers means to scale titles to render internally at higher resolutions, run with a more stable frame rate and, even make use of texture packs.

But do you know what’s better than an emulator? Taking the existing Playstation 2 game and recompiling it to run on a modern platform (such as your Windows or Linux desktop PC). That’s exactly what is being worked on now with [PS2Recomp, a static Recompiler & Runtime Tool.](https://github.com/ran-j/PS2Recomp)

![](https://redgamingtech.com/wp-content/uploads/ps2-console-1024x683.jpg)

To keep things simple here, this will basically take a Playstation 2 game (which would be designed around the PS2’s unique architecture such as the ‘Emotion Engine’ CPU that’s based around a MIP R5900) and convert it to natively run on whatever platform you’re targeting.

In plain English, this is a tool and obviously, would need to be used on different games. In other words, it’s not just a ‘download and every game automatically runs’ application. But, it will give folks a tool to be able to decompile the game and quite frankly, that’s absolutely incredible.

This is a great stepping stone for some incredible remasters and community remakes of games. There are already [HD Texture Pack](https://sites.google.com/view/pcsx2-hd-textures-project/home)s available for PS2 emulators, as well as other ways to improve visuals. But this would give even more freedom and flexibility to do modify and really enhance the games. That’s to say nothing of totally unlocking the frame rates (and likely not breaking physics or collision detection which is a big problem with emulated titles).

At a guess, too, the games would also run great even with much lower-end hardware than would be needed for emulators. Recompilation efforts in the community certainly aren’t new. Indeed, you can look to the N64 because there have been several high-profile examples of what these kind of projects can achieve.

A few infamous ones would include both [including Mario 64](https://github.com/sm64-port/sm64-port) and Zelda. Indeed, there’s a fork of the Mario 64 project supporting RTX (ray tracing) for Nvidia owners. You can see an example of Mario 64 below:

![](https://redgamingtech.com/wp-content/uploads/mario-raytracing-1024x576.jpg)

Another example [on the N64 is Zelda, w](https://github.com/Zelda64Recomp/Zelda64Recomp)here the project has a plethora of visual and gameplay enhancements, and in the longer term again, they’re planning to introduce Ray Tracing.

So, in the future we could be playing the likes of MGS2, Gran Turismo, God of War, Tekken 4, Shadow Hearts with ‘native’ PC versions. This would allow controllers to run (such as dual shock or Xbox controllers) and other features to be bundled in too (exactly as we see with the N64 ports).

So yes, currently playing PS2 games on PC via emulator is still absolutely fantastic, but native ports would be the holy grail of game preservation.

The Playstation 2 architecture is extremely unique, and as I mentioned earlier in this article focused around a MIPS R5900 based CPU known as the Emotion Engine (operating a shade under 300MHz). This CPU was super unique, because Sony implemented a number of customized features include two Vector Units designed to help manipulate geometry and perform a bunch of other co-processing duties.

This was bundled with 32MB of memory, and the GPU was known as the Graphics Synthesizer, runing at about 147MHz, and sporting 4MB of embedded DRAM. Sony’s design was fascinating for the time, and despite its processor clocked significantly lower than either Nintendo’s GameCube or Microsoft’s Xbox, punched well above its weight class.

As a small update – I want to remind people that (as of the time I’m writing this article) the project is \*NOT\* finished yet, and there is still work to do. But the fact that this is being worked on is awesome for those of us interested in game preservation.