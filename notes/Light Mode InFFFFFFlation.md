---
title: "Light Mode InFFFFFFlation"
url: https://willhbr.net/2025/10/20/light-mode-infffffflation/
clipped: 2026-06-17 01:57:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Light Mode InFFFFFFlation](https://willhbr.net/2025/10/20/light-mode-infffffflation/)

## Digest Summary
- The author measured macOS UI brightness by extracting representative window sections from the macOS Screenshot Library (512 px), converting each crop to greyscale with Pillow, and recording the mean pixel value (0‑255).  
- Plotting these average lightness values against OS release years shows a steady rise in light‑mode brightness: from ~71 % in Snow Leopard (2012) to 100 % in macOS Tahoe, with dark mode following a lower but similarly increasing trend.  
- Dark mode first appeared in macOS Mojave (2018); the author switched permanently after Big Sur raised light‑mode brightness to ~97 %, prompting the change in 2020.  
- The analysis excludes perceptual adjustments such as wallpaper‑based tinting and focuses solely on raw greyscale averages of window chrome, noting that overall screen brightness would require broader app‑level sampling.  
- A future concern is iOS 26’s use of HDR to render UI elements brighter than 100 % white, potentially encouraging further “brightness inflation.”  
- The author recommends considering medium‑grey UI tones to mitigate visual strain from ever‑brighter default themes.

## Discussion Summary
The comments show a divided view of light versus dark interfaces, with many users linking eye comfort to ambient lighting, auto‑brightness, and personal habit rather than a universal rule. Some argue dark mode reduces glare and is preferable on bright screens, while others find light mode easier to read, especially for long documents, and criticize dark themes for low contrast or excessive darkness on OLED displays. Several participants note a broader design trend toward higher brightness and reduced color richness, expressing a desire for more nuanced or customizable greyscale schemes rather than a strict binary choice.

---

## Full Article

Back in the day, light mode wasn’t called “light mode”. It was just the way that computers were, we didn’t really think about turning everything light or dark. Sure, some applications were often dark (photo editors, IDEs, terminals) but everything else was light, and that was fine.

What we didn’t notice is that light mode has been slowly getting lighter, and I’ve got a graph to prove it. I did what any normal person would do, I downloaded the same (or similar) screenshots from the [MacOS Screenshot Library](https://512pixels.net/projects/aqua-screenshot-library/) on [*512 Pixels*](https://512pixels.net/). This project would have been much more difficult without a single place to get well-organised screenshots from. I cropped each image so just a representative section of the window was present, here shown with a pinkish rectangle:

![screenshot of OS X Snow Leopard Finder window with toolbar section highlighted](https://willhbr.net/images/2025/macos-light-mode.webp)

Then used [Pillow](https://pypi.org/project/pillow/) to get the average lightness of each cropped image:

```
for file in sorted(os.listdir('.')):
  image = Image.open(file)
  greyscale = image.convert('L')
  stat = ImageStat.Stat(greyscale)
  avg_lightness = int(stat.mean[0])
  print(f"{file}\t{avg_lightness}")
```

This ignores any kind of perceived brightness or the tinting that MacOS has been doing for a while based on your wallpaper colour. I could go down a massive tangent trying to work out exactly what the best way to measure this is, but given that the screenshots aren’t perfectly comparable between versions, comparing the average brightness of a greyscale image seems reasonable.

I graphed that on the release year of each OS version, doing the same for dark mode:

2009
2025
100%
0%

This graph is an SVG, which may not render correctly in feed readers. [View this post on the web](https://willhbr.net/2025/10/20/light-mode-infffffflation/).

You can clearly see that the brightness of the UI has been steadily increasing for the last 16 years. The upper line is the default mode/light mode, the lower line is dark mode. When I started using MacOS in 2012, I was running Snow Leopard, the windows had an average brightness of 71%. Since then they’ve steadily increased so that in MacOS Tahoe, they’re at a full 100%.

What I’ve graphed here is just the brightness of the window chrome, which isn’t really representative of the actual total screen brightness. A better study would be looking at the overall brightness of a typical set of apps. The default background colour for windows, as well as the colours for inactive windows, would probably give a more complete picture.

For example, [in Tahoe](https://512pixels.net/projects/aqua-screenshot-library/macos-26-tahoe/) the darkest colour in a typical light-mode window is the colour of a section in an inactive settings window, at 97% brightness. In Snow Leopard the equivalent colour was 90%, and that was one of the *brightest* parts of the window, since the window chrome was typically darker than the window content.

I tried to remember exactly when I started using dark mode all the time on MacOS. I’ve always used a dark background for my editor and terminal, but I wasn’t sure when I swapped the system theme across. When it first came out I seem to remember thinking that it looked gross.

It obviously couldn’t be earlier than 2018, as that’s when dark mode was introduced in [MacOS Mojave](https://en.wikipedia.org/wiki/MacOS_Mojave). I’m pretty sure that when I updated my personal laptop to an M1 MacBook Air at the end of 2020 that I set it to use dark mode. This would make sense, because the [Big Sur](https://en.wikipedia.org/wiki/MacOS_Big_Sur) update bumped the brightness from 85% to 97%, which probably pushed me over the edge.

I think the reason this happens is that if you look at two designs, photos, or whatever, it’s really easy to be drawn in to liking the brighter one more. Or if they’re predominantly dark, then the darker one. I’ve done it myself with this very site. If I’m tweaking the colours it’s easy to bump up the brightness on the background and go “ooh wow yeah that’s definitely cleaner”, then swap it back and go “ewww it looks like it needs a good scrub”. If it’s the dark mode colours, then a darker background will just look *cooler*.

I’m not a designer, but I assume that resisting this urge is something you learn in design school. Just like making a website look good with a non-greyscale background.

This year in iOS 26, some UI elements use the HDR screen to make some elements and highlights brighter than 100% white. This year it’s reasonably subtle, but the inflation potential is there. If you’ve ever looked at an HDR photo on an iPhone (or any other HDR screen) then looked at the UI that’s still being shown in SDR, you’ll know just how grey and sad it looks. If you’re designing a new UI, how tempting will it be to make just a little bit more of it just a little bit brighter?

As someone whose job involves looking at MacOS for a lot of the day, I find that I basically *have* to use dark mode to avoid looking at a display where all the system UI is 100% white blasting in my eyes. But the alternative doesn’t have to be near-black for that, I would happily have a UI that’s a medium grey. In fact what I’ve missed since swapping to using dark mode is that I don’t have contrast between windows. Everything looks the same, whether it’s a text editor, IDE, terminal, web browser, or Finder window. All black, all the time.

Somewhat in the spirit of [Mavericks Forever](https://mavericksforever.com), if I were to pick an old MacOS design to go back to it would probably be [Yosemite](https://512pixels.net/projects/aqua-screenshot-library/os-x-10-10-yosemite/). I don’t have any nostalgia for skeuomorphic brushed metal or stitched leather, but I do quite like the flattened design and blur effects that Yosemite brought. Ironically Yosemite was a substantial jump in brightness from previous versions.

So if you’re making an interface or website, be bold and choose a 50% grey. My eyes will thank you.