---
title: "Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS"
url: https://www.v68k.org/advanced-mac-substitute/
clipped: 2026-06-17 01:18:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS](https://www.v68k.org/advanced-mac-substitute/)

## Digest Summary
Advanced Mac Substitute is an API‑level reimplementation of the 1980s Macintosh operating system that runs classic 68 k‑processor Mac applications without requiring an Apple ROM or original system software. It replaces the OS rather than emulating full hardware, launching directly into the target application. The backend includes a 68 k CPU emulator and is designed to compile on any POSIX‑like system; the frontend uses SDL2 for a generic bit‑mapped terminal abstraction with platform‑specific implementations for macOS, X11, and Linux framebuffer (fbdev). Current capabilities support 1‑bit graphics, regions, circles, round‑rects, lines, cursors, GrafPorts, text, windows, controls, menus, dialogs, and related primitives. Demonstrated applications include four 1984 games—Amazing, Solitaire, Missile, and IAGO—along with Lode Runner and The Fool’s Errand cinematic. Source code is hosted on GitHub, and the program can be executed on macOS/OS X, X Window System, Linux framebuffer consoles, or via VNC clients.

## Discussion Summary
The reaction is overwhelmingly positive, with users praising the project’s speed, nostalgic appeal, and potential to run classic Mac applications on modern hardware. Several comments highlight interest in adding conveniences such as file sharing, windowed frames, and browser‑based deployment, while others note technical hurdles like missing OpenDF support and compatibility quirks. Comparisons to earlier solutions such as Executor acknowledge similar goals, and there is broad enthusiasm for further development and experimentation despite the noted challenges.

---

## Full Article

Advanced Mac Substitute
=======================

---

[![In MacPaint, the word 'hello' is written in cursive.](https://www.v68k.org/advanced-mac-substitute/pix/macpaint/hello.png "Hello, world!")](https://www.v68k.org/advanced-mac-substitute/demo/MacPaint-AMS-demo.mp4)

**MacPaint** running in **Advanced Mac Substitute** (click to see video)

![Advanced Mac Substitute icon: A grey desktop and arrow cursor, on a grayed-out Macintosh](https://www.v68k.org/advanced-mac-substitute/ams-icon.png)

Advanced Mac Substitute

**Advanced Mac Substitute** is an API-level reimplementation of 1980s-era Mac OS.
It runs 68K Mac applications in an emulator *without an Apple ROM or system software*.

!["But those times are now only legend."](https://www.v68k.org/advanced-mac-substitute/systems-twilight-legend.png)
!["But those times are now only legend."](https://www.v68k.org/advanced-mac-substitute/systems-twilight-legend-gray.png)

**System’s Twilight** running in **Advanced Mac Substitute**.

![The first level of Lode Runner that it autoplays in its Attract mode](https://www.v68k.org/advanced-mac-substitute/lode-runner-1.png)
![The player is burning a hole in the floor to trap an approaching guard.](https://www.v68k.org/advanced-mac-substitute/lode-runner-2.png)

**Lode Runner** running in **Advanced Mac Substitute**

![The white-on-black title screen of the prologue cinematic from The Fool’s Errand](https://www.v68k.org/advanced-mac-substitute/tfe-prologue-title.png)
![The same title, but with a rain-against-the-camera-lens effect.](https://www.v68k.org/advanced-mac-substitute/tfe-prologue-title-rain.png)

The opening of the **prologue** cinematic from **The Fool’s Errand** running in **Advanced Mac Substitute**

![Amazing, a maze-tracing game by Steve Capps](https://www.v68k.org/advanced-mac-substitute/amazing-close.png)
![When you solve the maze, a picture appears of a penguin blowing a triumphant note on a bugle.](https://www.v68k.org/advanced-mac-substitute/amazing-done.png)

**Amazing** running in **Advanced Mac Substitute** (point to see the solved maze)

Unlike traditional emulators, Advanced Mac Substitute doesn’t emulate the hardware on which an operating system runs (except for the 680x0 processor), but actually replaces the OS — so it launches directly into an application, without a startup phase.

![A parody of the Macintosh loading screen.](https://www.v68k.org/advanced-mac-substitute/welcome.png)

**Welcome** to **Advanced Mac Substitute**.

(This is an application, not a real loading screen.)

Advanced Mac Substitute is a **factored application**. The **backend** includes a 68K emulator and should build and run on any POSIX-like system. The **frontend** is a generic bitmapped terminal abstraction, provided by SDL2 (for various platforms) along with custom implementations for macOS, X11, and Linux framebuffer (fbdev).

Advanced Mac Substitute is capable of running several applications written for the original Macintosh computer. Examples include four games from 1984: **Amazing**, **Solitaire**, **Missile**, and **IAGO**.

![Missile, a Missile Command clone for Macintosh from 1984](https://www.v68k.org/advanced-mac-substitute/missile-791.png)
![Another incoming ICBM is destroyed, yet many more remain — including a MIRV warhead](https://www.v68k.org/advanced-mac-substitute/missile-792.png)

**Missile** running in **Advanced Mac Substitute** (point to see the next frame)

![IAGO, an Othello game for Macintosh from 1984](https://www.v68k.org/advanced-mac-substitute/iago.png)
![Game over: White has beaten Black, 48-16](https://www.v68k.org/advanced-mac-substitute/iago-win.png)

**IAGO** running in **Advanced Mac Substitute** (point to see who won)

Current [support](https://www.v68k.org/advanced-mac-substitute/status/) includes 1-bit-deep graphics, regions, circles and roundrects, lines, cursors, GrafPorts, text, windows, controls, menus, dialogs, and more.

Source
------

[Source code](https://github.com/jjuran/metamage_1/tree/master/68k) for Advanced Mac Substitute is on GitHub.

If you’re feeling adventurous, you can [try out Advanced Mac Substitute](https://www.v68k.org/advanced-mac-substitute/howto/) in macOS / OS X, the X Window System, a Linux framebuffer console, or a VNC client.

![Still image of monochrome nyancat using patterns instead of colors](https://www.v68k.org/advanced-mac-substitute/nyancat.png)
![Animation of monochrome nyancat using patterns instead of colors](https://www.v68k.org/advanced-mac-substitute/NyanCat.gif)

**Nyanochrome Cat** running in **Advanced Mac Substitute** (point to animate)

([Older documentation](https://www.v68k.org/advanced-mac-substitute/legacy/) has moved while revision is under way.)