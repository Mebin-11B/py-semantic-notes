---
title: "Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'"
url: https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level
clipped: 2026-06-17 01:31:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)

## Digest Summary
None

## Discussion Summary
Comments acknowledge that the original 2013 Xbox’s security was unusually robust, keeping it largely unhacked for years, but view the recent successful exploit as a significant technical achievement that could enable emulation and homebrew development. Many consider the “unhackable” label misleading, emphasizing that physical access always presents vulnerabilities and that no system is flawless. There is both admiration for Microsoft’s layered defenses and criticism of the notion that such measures guarantee absolute protection, alongside curiosity about how future consoles or other hardware might be affected.

---

## Full Article

A groundbreaking hack for [Microsoft](https://www.tomshardware.com/tag/microsoft)’s ‘unhackable’ [Xbox One](https://www.tomshardware.com/reviews/microsoft-xbox-one-console-review,3681.html) was revealed at the recent RE//verse 2026 conference. This console has remained a fortress since its launch in 2013, but now Markus ‘Doom’ Gaasedelen has showcased the ‘Bliss’ double glitch. Just as the [Xbox 360](https://www.tomshardware.com/tech-industry/artificial-intelligence/user-runs-an-ai-model-on-an-xbox-360-3-core-powerpc-with-512-mb-memory-handles-an-ai-model-based-on-llama2-c) famously fell to the Reset Glitch Hack (RGH), the Xbox One has now fallen to Voltage Glitch Hacking (VGH).

RE//verse 2026: Hacking the Xbox One - YouTube
![RE//verse 2026: Hacking the Xbox One - YouTube](https://img.youtube.com/vi/FTFn4UZsA5U/maxresdefault.jpg)

[Watch On](https://www.youtube.com/watch?v=FTFn4UZsA5U)

— [RE//verse 2026: Hacking the Xbox One](https://www.youtube.com/watch?v=FTFn4UZsA5U)

Go deeper with TH Premium: CPU

(Image credit: Tom's Hardware)

“In 2013 some kind of iron curtain came down on [security](https://www.tomshardware.com/tag/security), of the Xbox ecosystem, and the Xbox One never got hacked,” noted Gaasedelen in his introduction. The same is true of the Xbox One’s successors, and Microsoft was rightly proud. Seven years after its launch, Microsoft engineers would still assert that the Xbox One was “the most secure product Microsoft has ever produced.”

(Image credit: Markus ‘Doom’ Gaasedelen [video presentation](https://www.youtube.com/watch?v=FTFn4UZsA5U))

What made the Xbox One so secure, so special? Gaasedelen referenced prior work and presentations to convey this information. I’ve shared a summary slide about this, too, but let’s fast forward to the demo of the new Bliss hack, which takes place from about 46 minutes into the presentation.

Latest Videos From![](https://www.tomshardware.com/media/img/brand_logo.svg)

Since reset glitching wasn’t possible, Gaasedelen thought some [voltage glitching](https://www.tomshardware.com/news/yet-another-amd-zen-secure-encrypted-virtualization-vulnerability-demonstrated-by-researchers) could do the trick. So, instead of tinkering with the system rest pin(s) the hacker targeted the momentary collapse of the CPU voltage rail. This was quite a feat, as Gaasedelen couldn’t ‘see’ into the Xbox One, so had to develop new hardware introspection tools.

Eventually, the Bliss exploit was formulated, where two precise voltage glitches were made to land in succession. One skipped the loop where the [ARM Cortex](https://www.tomshardware.com/news/cortex-76-high-laptop-performance,37158.html) memory protection was setup. Then the Memcpy operation was targeted during the header read, allowing him to jump to the attacker-controlled data.

As a hardware attack against the boot ROM in silicon, Gaasedelen says the attack in unpatchable. Thus it is a complete compromise of the console allowing for loading unsigned code at every level, including the Hypervisor and OS. Moreover, Bliss allows access to the [security processor](https://www.tomshardware.com/features/intel-amd-most-secure-processors) so games, firmware, and so on can be decrypted.

What happens next with this technique remains to be seen. [Digital archivists](https://www.tomshardware.com/tech-industry/big-tech/data-hoarders-race-to-preserve-data-from-rapidly-disappearing-u-s-federal-websites) should enjoy new levels of access to Xbox One firmware, OS, games. There could be subsequent emulation breakthroughs thanks to this effort. We also now have a route to making a Bliss-a-like mod chip to automate the precise electrical glitching required.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Whether PC users, our core readership, will be interested in actually emulating Xbox One, looks unlikely. The 2013 system’s game library is largely overlapped in better quality on the PC platform.

*Follow* [*Tom's Hardware on Google News*](https://news.google.com/publications/CAAqLAgKIiZDQklTRmdnTWFoSUtFSFJ2YlhOb1lYSmtkMkZ5WlM1amIyMG9BQVAB)*, or* [*add us as a preferred source*](https://google.com/preferences/source?q=)*, to get our latest news, analysis, & reviews in your feeds.*