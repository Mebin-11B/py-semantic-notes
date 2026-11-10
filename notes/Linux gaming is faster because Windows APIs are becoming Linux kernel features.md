---
title: "Linux gaming is faster because Windows APIs are becoming Linux kernel features"
url: https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/
clipped: 2026-06-17 01:03:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Linux gaming is faster because Windows APIs are becoming Linux kernel features](https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/)

## Digest Summary
Linux gaming reached a new milestone in March 2026 when Steam users on Linux surpassed 5 % of the platform’s total base, driven by Windows 10’s end‑of‑support and the widespread use of the Steam Deck, which runs a Linux‑based OS. Historically, performance gains came from Wine/Proton, the compatibility layers that translate Windows system calls. The recent addition of NTSYNC—a kernel‑level driver implementing Windows synchronization primitives directly in the Linux kernel—marks a shift to deeper integration. By providing native handling of coordination mechanisms formerly emulated via esync/fsync, NTSYNC reduces overhead and eliminates subtle bugs such as hitches and deadlocks, though raw FPS improvements over Proton’s fsync are modest for already smooth titles. Development is led by Valve, CodeWeavers, and community contributors; Valve has shipped NTSYNC in stable SteamOS despite existing workarounds, indicating confidence in its stability. The move exemplifies a broader trend of incorporating Windows‑specific features into the Linux kernel to support gaming, and further kernel‑level adaptations are expected as the Linux user base continues to grow.

## Discussion Summary
The comments collectively highlight strong enthusiasm for recent advances in Linux gaming, especially the impact of Proton, Vulkan, and NTSYNC in improving compatibility and performance for many titles, with users reporting smooth experiences on systems like Steam Deck and Bazzite. Frequent points of agreement note remaining challenges such as anti‑cheat restrictions, occasional performance gaps versus Windows, and a lack of comprehensive benchmark data. Several contributors express optimism that continued kernel improvements and broader developer support could further reduce the “Windows tax,” while a minority remain skeptical about full parity for high‑profile competitive games.

---

## Full Article

In March 2026, Linux crossed five percent of Steam's user base for the first time, an all-time high for an operating system that spent two decades as a novelty when it came to any kind of gaming. Microsoft's end-of-support deadline for Windows 10 last October pushed many users to look at alternatives, and the Steam Deck has quietly turned millions of people into Linux gamers without them really thinking about it, leading to more widespread adoption on desktop machines.

Most of that progress used to happen inside a piece of software called Wine, the translation layer that convinces Windows games they're running on Windows. Valve's tuned version of [Wine, called Proton](https://www.xda-developers.com/wine-11-6-just-made-modding-windows-games-linux-easier/), is what makes Steam Play and the Steam Deck work. For years, every meaningful improvement to Linux gaming came from changes to Wine and Proton themselves. That's still true, but increasingly the most important changes are happening one layer deeper, inside the Linux kernel. The latest example of that is something called [NTSYNC](https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/), a kernel-level driver that has offered great performance gains over previous versions of Wine, and is loaded by default on every Steam Deck that's up-to-date.

[![A computer screen showing Windows apps running on Ubuntu through Wine](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2025/09/windows-apps-through-wine.jpg?q=49&fit=crop&w=220&h=124&dpr=2)](https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/)
Related

Wine 11 is the biggest jump for Linux gaming in years.

What NTSYNC actually is
-----------------------

### An additional piece of the performance puzzle

NTSYNC is a small piece of driver added directly to the Linux kernel that gives it a native implementation of a set of Windows-specific tools that games depend on to coordinate themselves.

Modern games juggle dozens of things at once. While you're playing, your CPU manages the rendering pipeline, loading assets, running physics, processing audio, handling AI NPC routines, and tracking inputs, all in parallel across multiple cores. All those jobs constantly have to coordinate so they don't trip over each other.

![XDA](https://static0.xdaimages.com/assets/images/xda-logo-full-colored-light.svg?v=3.6)Quiz

8 Questions · Test Your Knowledge

The history of Linux Trivia challenge
-------------------------------------

From a Finnish student's side project to powering the world — how well do you know the story of Linux?

OriginsKernelDistrosPioneersMilestones

Begin

In what year did Linus Torvalds first announce the Linux kernel to the world?

A1989B1991C1993D1995

Correct! Linus Torvalds posted his now-famous message to the comp.os.minix newsgroup on August 25, 1991, describing Linux as 'just a hobby' project. Few could have predicted it would one day run the majority of the world's servers and smartphones.

Not quite — Torvalds made his announcement in 1991. He was a 21-year-old computer science student at the University of Helsinki at the time, and his modest post described the project as something that 'won't be big and professional' like GNU.

Continue

Which university was Linus Torvalds attending when he created the first version of the Linux kernel?

AStockholm UniversityBAalto UniversityCUniversity of HelsinkiDMIT

Correct! Torvalds was studying at the University of Helsinki in Finland when he began working on Linux as a personal project, initially inspired by MINIX, a small Unix-like system used for educational purposes.

Not quite — Torvalds was a student at the University of Helsinki in Finland. He started Linux partly out of frustration with the limitations of MINIX, which his professor Andrew Tanenbaum had designed deliberately to be simple for teaching.

Continue

What operating system primarily inspired Linus Torvalds to create the Linux kernel?

AMS-DOSBMINIXCBSD UnixDSolaris

Correct! MINIX, created by professor Andrew Tanenbaum, was the direct inspiration for Linux. Torvalds used MINIX on his new Intel 386 PC but found it too restricted for his needs, which pushed him to write his own kernel.

Not quite — the answer is MINIX. Torvalds was using MINIX when he started Linux, and even held a famous online debate with its creator Andrew Tanenbaum about kernel design philosophy, specifically monolithic versus microkernel architectures.

Continue

What was the version number of the first publicly released Linux kernel in 1991?

A0.01B0.1C1.0D0.99

Correct! Linux version 0.01 was the first kernel Torvalds released publicly in September 1991. It was a rough, early build that could only run on Intel 386 hardware and had very limited functionality, but it marked the true beginning of the Linux project.

Not quite — the first public release was version 0.01 in September 1991. The kernel didn't reach version 1.0 until March 1994, by which point it had grown significantly in capability and had attracted contributions from developers around the world.

Continue

Which Linux distribution, first released in 1993, is one of the oldest still actively maintained today?

AUbuntuBFedoraCSlackwareDDebian

Correct! Slackware, created by Patrick Volkerding, was first released in July 1993, making it one of the oldest surviving Linux distributions. It is known for its simplicity and Unix-like philosophy, and it continues to be maintained to this day.

Not quite — the answer is Slackware, released in 1993 by Patrick Volkerding. While Debian was also founded in 1993, Slackware narrowly edges it out as the older release. Ubuntu didn't arrive until 2004, and Fedora launched in 2003.

Continue

The GNU Project, which provided many tools that paired with the Linux kernel, was founded by which developer?

AEric RaymondBRichard StallmanCBruce PerensDIan Murdock

Correct! Richard Stallman founded the GNU Project in 1983 with the goal of creating a completely free Unix-like operating system. When the Linux kernel appeared in 1991, it filled the missing piece GNU needed, and the combination became what many call GNU/Linux.

Not quite — it was Richard Stallman who founded the GNU Project in 1983. Stallman is also known for creating the GPL (GNU General Public License) and founding the Free Software Foundation, two pillars that shaped the legal and philosophical foundation of free software.

Continue

Which company released a landmark commercial Linux distribution in 1994, helping bring Linux into the enterprise world?

ACanonicalBSUSECRed HatDMandriva

Correct! Red Hat released its first Linux distribution in 1994 and became one of the most influential commercial Linux companies in history. It pioneered the enterprise Linux market and was eventually acquired by IBM in 2019 for approximately $34 billion.

Not quite — Red Hat is the answer. Founded by Marc Ewing and Bob Young, Red Hat helped prove that companies could build sustainable businesses around open-source software. SUSE Linux also launched in 1994, making it a close rival, but Red Hat became the more globally dominant enterprise force.

Continue

Ubuntu Linux, one of the most popular desktop distributions, is based on which other Linux distribution?

AArch LinuxBFedoraCDebianDGentoo

Correct! Ubuntu is based on Debian and was first released in October 2004 by Mark Shuttleworth's company Canonical. It was designed to make Linux more accessible to everyday users, and its six-month release cycle and long-term support versions made it a favorite for both desktops and servers.

Not quite — Ubuntu is built on top of Debian. Debian itself was founded in 1993 by Ian Murdock and is known for its strict commitment to free software and stability. Ubuntu inherits Debian's package management system (APT and .deb packages) but adds its own user-friendly layer on top.

See My Score

Challenge Complete

Your Score
----------

/ 8

Thanks for playing!

Try Again

Windows handles this coordination by using a specific set of mechanisms, and before NTSYNC, Wine had to mimic these mechanisms using things like esync and fsync, which both worked, but didn't always match Windows exactly. NTSYNC builds these mechanisms straight into the Linux kernel for the first time, and it means Wine doesn't have to emulate anything anymore. The developer-facing API calls don't actually change, Linux just knows how to answer them natively.

[![A laptop shwoing the KDE Plasma desktop with apps including Affinity and Vivaldi open](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/linux-laptop-with-kde-plasma.jpg?q=49&fit=crop&w=220&h=124&dpr=2)](https://www.xda-developers.com/wine-translating-windows-games-linux-proton-effortless/)
Related

Wine is the foundation that makes gaming on Linux possible.

NTSYNC is part of a growing pattern
-----------------------------------

### Not the first time Linux has inherited features because of Windows

NTSYNC isn't the first time Linux has gained a new feature specifically because Windows games needed it. A few years back, Linux added a way for software to wait on several events at once, which is something Windows had built in for decades, but Linux didn't. Wine had been working around the gap with awkward tricks until the kernel finally got native support.

This work is driven by Valve, by CodeWeavers (the company that employs many of the core Wine developers, including NTSYNC's author Elizabeth Figura), and by a steady stream of contributors who want Linux to be a real gaming platform without depending on out-of-ecosystem patches forever.

[![Steam Deck OLED header](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/steam-deck-oled.jpg?q=49&fit=crop&w=220&h=124&dpr=2)](https://www.xda-developers.com/valve-isnt-ditching-windows-x86-quietly-making-optional/)
Related

Valve wants to make it possible for gamers to play anywhere.

These aren't magical performance gains
--------------------------------------

### fsync was already pretty good

The headline performance gains look great, but they need some context. The eye-catching 40 to 200 percent FPS gains cited in [NTSYNC's original benchmarks](https://lwn.net/Articles/960275/) were measured against unmodified upstream Wine, which almost nobody uses to play games on Linux anymore. Most Linux gamers, including every Steam Deck owner, use Proton, which already has fsync. Compared to fsync, NTSYNC's performance gains are far more modest. The games that benefit most from the change to NTSYNC are games that were really struggling before. Anything that was running at decent framerates beforehand is still going to run fine.

[![A Steam Deck on a colorful background held in one hand.](https://static0.xdaimages.com/wordpress/wp-content/uploads/2024/09/reasons-to-pick-a-gaming-handheld-over-a-pc.jpg?q=49&fit=crop&w=220&h=124&dpr=2)](https://www.xda-developers.com/these-linux-myths-you-still-believe-simply-arent-true/)
Related

Linux is a completely different beast than it was a decade ago.

Valve adopted it anyway
-----------------------

### It's a great sign

Pierre-Loup Griffais, an engineer at Valve, has [gone on the record to say that fsync was already fast enough](https://bsky.app/profile/plagman.bsky.social/post/3lkp26xmco22k), and despite that, Valve still shipped NTSYNC in stable SteamOS in March anyway, which speaks to the fact that fsync is still a workaround at its core, and can be the cause of issues outside of poor raw FPS.

These old workarounds got subtle edge cases wrong in ways that produced occasional hitches, deadlocks, or weird behavior in specific games, which are bugs that don't show up on benchmark charts but can absolutely ruin individual experiences. NTSYNC fixes those at the source by matching Windows behavior exactly, and that means as soon as your favorite distro moves to the new kernel version, whether it be Bazzite, CachyOS, Fedora, or a flavor of Ubuntu, they all get this much-needed fix.

[![Jsaux Steam Deck Dock SSD Enclosure 4](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2024/08/jsaux-steam-deck-dock-ssd-enclosure-4.jpg?q=49&fit=crop&w=220&h=124&dpr=2)](https://www.xda-developers.com/reasons-valve-full-steamos-release-change-pc-gaming/)
Related

Valve's full SteamOS release will change PC gaming again, and here are some of the most important ways.

### Gaming on Linux continues to improve by the month

Linux has grown so much in the gaming department. Where there once was nothing but clever [Wine patches and community workarounds](https://www.xda-developers.com/wine-translating-windows-games-linux-proton-effortless/) now lies support from gaming behemoths like Valve, driving changes to the Linux kernel itself. NTSYNC won't be the last time a piece of [Windows](https://www.xda-developers.com/theres-a-cure-to-linux-distro-hopping-but-everyone-keeps-forgetting-about-it/) gets rebuilt inside Linux because gamers needed it, and with more than five percent of Steam's user base now running Linux, the incentive to keep doing it has never been stronger.