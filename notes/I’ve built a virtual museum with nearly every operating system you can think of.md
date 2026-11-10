---
title: "I’ve built a virtual museum with nearly every operating system you can think of"
url: https://virtualosmuseum.org/
clipped: 2026-06-17 01:00:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Operating Systems
  - Digital Preservation
  - Emulation
  - Virtualization
  - Computing History
  - QEMU
related:
  - "[[Ahoy, DECmate II the little PDP-8 that could]]"
  - "[[Jef Raskin, the Visionary Behind the Mac (2013)]]"
  - "[[Xous Operating System]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The Virtual OS Museum is a pre-configured Linux virtual machine that emulates and runs historic and obscure operating systems from the 1948 Manchester Baby to modern OSes using a custom launcher.
>
> **Key points:**
> - The Virtual OS Museum packages pre-configured emulators and OS images into a unified Linux VM compatible with QEMU, VirtualBox, and UTM.
> - The collection features historical mainframes, minicomputers, workstations, classic home computers, and early mobile platforms like Symbian and Newton OS.
> - A custom launcher provides hypervisor-independent execution, snapshots to easily revert system changes, and automated background updates.
> - Offered in two versions, a Full offline edition (all images pre-loaded) and a Lite version that downloads guests on-demand to save initial storage space.
> - The project consolidates 20 years of archiving effort to bypass the friction of manually configuring obsolete hardware emulators.
>
> **Concept links:** [[Operating Systems]], [[Digital Preservation]], [[Emulation]], [[Virtualization]], [[Computing History]], [[QEMU]]
>
> **Suggested connections:**
> - [[Ahoy, DECmate II the little PDP-8 that could]] — Related to historical computing platforms and retro hardware emulation.
> - [[Jef Raskin, the Visionary Behind the Mac (2013)]] — Focuses on historical Macintosh interface design, which is represented in the OS museum.
> - [[Xous Operating System]] — Another unique, contemporary operating system project in the clippings.
<!-- ai-summary:end -->

# [I’ve built a virtual museum with nearly every operating system you can think of](https://virtualosmuseum.org/)

## Digest Summary
The Virtual OS Museum provides a pre‑configured Linux virtual machine that runs a wide range of historical operating systems and standalone applications under emulation. A hypervisor‑independent launcher (compatible with QEMU, VirtualBox, UTM) includes snapshot support, automatic/manual updates, and installers for Windows, macOS, and Linux hosts. The collection spans from the Manchester Baby (1948) through early mainframe monitors, CTSS, MVS, VM/370, TOPS‑10/20, ITS, Multics, RSX, RSTS, to workstation OSes (PERQ, SunOS, IRIX, OSF/1, A/UX, NeXTSTEP, Plan 9, BSDs, Linux distributions). It also covers home computers (CP/M, Apple II, Commodore, Atari, MSX, TRS‑80, BBC Micro, ZX Spectrum), personal computers (DOS variants, OS/2, BeOS, Windows 1.0‑early Longhorn, Classic Mac OS through OS X 10.5 PPC), mobile/embedded platforms (PalmOS, Symbian/EPOC, Windows CE, Newton, early Android/iOS, QNX), and obscure research systems (ZetaLisp, Smalltalk, Oberon). Two VM editions are offered: a full offline package and a lite version that downloads guest images on first run. The project consolidates over 20 years of collected images, patched emulators, and configuration scripts to make historically significant software instantly bootable.

## Discussion Summary
The comments express strong appreciation for the extensive OS‑preservation project, emphasizing its value for historical archiving, nostalgia, and education. Contributors praise the effort, note the significance of safeguarding rarely documented systems, and suggest enhancements such as searchable listings, inclusion of additional obscure operating systems, better documentation, and more streamlined access (e.g., individual downloads, browser‑based emulation, torrents). Minor criticisms point to missing entries, unclear labeling, and UI issues, while technical curiosity about emulation methods and performance is also mentioned. Overall, the response is overwhelmingly positive and supportive.

---

## Full Article

This is a virtual museum of operating systems (and standalone applications)
running under emulation, implemented as a Linux VM for QEMU, VirtualBox, or UTM.

A custom emulator-independent launcher is provided, and all OSes and emulators
are pre-installed and pre-configured. The launcher includes a snapshot feature to quickly revert broken installations back to a working state. Hypervisor installers and shortcuts to run the VM on Windows, macOS, and Linux are also included.

Want to see the earliest resident monitors? The ancestor of all modern OSes (CTSS)? The earliest versions of Unix? The first OS with a desktop metaphor GUI (Xerox Star Pilot/ViewPoint)? Early versions of mainstream OSes? If you want to explore historical OSes and platforms without having to worry about configuring/installing emulators and OSes or corrupting emulated installations, you’ve come to the right place.

Just about every well-known OS and platform (and also a lot of obscure ones) is included in some form, spanning the entire history of stored-program computing from the Manchester Baby of 1948 (the first stored-program computer) to the present day.

The catalogue covers, among many other things:

* **The earliest mainframes**: Manchester Baby test/demo programs, Mark 1 Scheme A/B/C/T (the earliest examples of system software that could be considered as an OS), various EDSAC software, etc.
* **Later mainframes and minicomputers**: CTSS, MVS, VM/370, TOPS-10/20, ITS, Multics, RSX, RSTS, and more
* **Workstations and Unix variants**: PERQ OSes, SunOS, IRIX, OSF/1, A/UX, NeXTSTEP, Plan 9, various BSDs, plus Linux distributions across the decades, and more
* **Home computers**: various CP/M variants, Apple II, Commodore 8-bit machines, Atari 8-bit, MSX, Tandy TRS-80, BBC Micro, ZX Spectrum, Sharp MZ, and more
* **Personal computer operating systems**: various DOS variants, OS/2, BeOS, Windows from 1.0 to early Longhorn betas, classic Mac OS through Mac OS X 10.5 PPC, and more
* **Mobile and embedded**: PalmOS, EPOC/Symbian, Windows CE, Newton OS, early Android and iOS where emulation permits, QNX, etc.
* **Research and obscure systems**: ZetaLisp, Smalltalk environments, Oberon, Plan 9, and many more that few people now have ever booted

If a working version of an operating system exists somewhere, the goal is to have it here, in a form anyone can run on a reasonably modern laptop/desktop.

Downloads
---------

Both a *full* and a *lite* version are available. The full version ships with everything pre-downloaded and runs offline. The lite version downloads disk/tape/etc. images for guest VMs the first time they are run. Automatic and manual updates are supported on both editions so new installations land without re-downloading the whole VM.

[Download the Virtual OS Museum](https://virtualosmuseum.org/downloads)

Screenshots
-----------

[More screenshots](https://virtualosmuseum.org/more-screenshots)  
[Full list of installations](https://virtualosmuseum.org/installation-list)

Why this exists
---------------

While the state of software preservation has improved significantly over the past two decades, many of the existing software preservation projects are still not particularly accessible.

When I started collecting emulator images (2003), there were only a few small archives of software images and the corresponding documentation, and relatively few emulators for anything other than well-known consumer-oriented platforms. Nowadays there are many large archives of historical software and documentation, and a lot of emulators for even a lot of very obscure platforms.

However, while such efforts are valuable when it comes to keeping historical software available and runnable (and without them this project would have never been possible; see the [credits page](https://virtualosmuseum.org/credits) for a list of emulators, pre-installed images, and media archives I have used), it often still takes time and effort to get runnable VM installations from them. OSes may have complicated install procedures. Some may depend on particular device configurations within an emulator. Some will only run in certain emulator versions, breaking in later ones due to regressions. Some emulators might have complex configuration files, or may require a specific environment on the host system.

This project is an attempt to keep reachable as much of the history that’s been preserved in various places as possible. Not theoretically reachable. Not “bootable in principle if you assemble the right toolchain on a Tuesday.” Reachable. You click an entry, it runs, and where possible it runs with software of the era already loaded the way someone might actually have used the machine at the time.

The work behind it
------------------

This is the result of over 20 years of collecting. OS installations have been sourced from various places. Some have been downloaded as pre-installed images, whereas others were installed from images of original install media. Some were installed in less than an hour, whereas others took almost a week.

A decent number only run in particular emulator versions due to regressions in later versions, and some emulators needed minor patches to run on modern Linux or to play nice with the launcher. A few emulators have been patched to run OSes that were previously broken.

Many installations also include various add-on software - applications, development tools, games, utilities, etc. - set up the way it actually might have been used.

This is still far from finished; I have many more images sitting around that I have yet to install and emulators I want to fix; check out my [YouTube channel](https://www.youtube.com/@AndrewsOSLab), [blog](https://andreww591.blogspot.com/), or [BlueSky](https://bsky.app/profile/andreww591.bsky.social) to see what I’m currently working on.

Support the project
-------------------

This is a personal project, run and curated by one person, sustained by patience and time. If you find it interesting, the easiest ways to support it are:

* [Patreon](https://www.patreon.com/andreww591) for ongoing support
* [Ko-fi](https://ko-fi.com/andreww591) for one-off contributions
* [Discord](https://virtualosmuseum.org/discord)/[Fluxer](https://virtualosmuseum.org/fluxer) to talk about it, ask questions, or suggest new platforms/OSes to add (new entries may not be added immediately since I’ve got a lot of stuff to add)
* [GitLab](https://gitlab.com/virtualosmuseum/) to submit bug reports or patches related to the launcher and scripts
* [GitHub](https://github.com/andreww591/) to submit bug reports or patches related to emulators forked from other GitHub repositories (e.g. MAME)
* Telling someone who works on, writes about, or studies the history of computing that this exists