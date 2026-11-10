---
title: "Xfwl4 – The Roadmap for a Xfce Wayland Compositor"
url: https://alexxcons.github.io/blogpost_15.html
clipped: 2026-06-17 01:52:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Xfwl4 – The Roadmap for a Xfce Wayland Compositor](https://alexxcons.github.io/blogpost_15.html)

## Digest Summary
The Xfce team announced a new Wayland compositor, xfwl4, funded by community donations and led by core developer Brian Tarrice. xfwl4 will be written from scratch in Rust using the smithay library, not a fork of the existing xfwm4 C code. The rewrite avoids X11‑specific architecture, eliminates risk to xfwm4, and leverages Rust’s safety to reduce memory bugs. smithay was chosen over wlroots because it implements most Wayland protocol extensions, offers low‑level customization, has strong documentation, and avoids the difficulty of creating Rust bindings for wlroots. Project goals include achieving feature parity with xfwm4, reusing xfwm4 configuration dialogs and xfconf settings, adding session‑startup changes (the compositor becomes the session root), supporting the xdg‑session‑management protocol, and providing XWayland compatibility. The Xfce CI container build system will be updated to compile Rust via Meson. Development has begun, with a first release expected around mid‑year; further details are available in the issue tracker and source repository, and discussions continue on the #xfce‑dev Matrix channel.

## Discussion Summary
Comments show mixed but generally hopeful sentiment toward an XFCE Wayland implementation in Rust. Many express optimism that modern libraries can deliver feature‑parity, good performance on low‑end hardware, and attract new contributors, while also emphasizing the need for speed, low memory use, customizability, theme support, and stability comparable to the X11 version. A notable portion remains skeptical, fearing loss of simplicity, potential bugs, and reduced X11 maintenance, and some request specific functionalities such as xscreensaver integration and reliable window shading. Overall, users desire a lightweight, reliable desktop that retains XFCE’s core qualities while embracing Wayland.

---

## Full Article

#### Jan 27,2026

Xfwl4 - The roadmap for a Xfce Wayland Compositor
-------------------------------------------------

We, the Xfce team are excited to share some great news!

After careful consideration, we’ve decided on a meaningful way to use the generous donations from our community: funding longtime Xfce core developer [Brian Tarricone](https://gitlab.xfce.org/kelnos) to create xfwl4, a brand-new Wayland compositor for Xfce.

This initiative will utilize a significant portion of the project’s donated funds, but we believe it’s an important investment in Xfce’s future.

The goal is, that xfwl4 will offer the same functionality and behavior as xfwm4 does, or as much as possible considering the differences between X11 and Wayland. Using xfwl4 should feel just like using xfwm4 on X11. We even plan to reuse the existing xfwm4 configuration dialogs and xfconf settings to ensure a seamless transition.

Xfwl4 will not be based on the existing xfwm4 code. Instead, it will be written from scratch in rust, using [smithay](https://github.com/Smithay/smithay/) building blocks.

### Why doing a rewrite?

The first attempt at creating an Xfce Wayland compositor involved modifying the existing xfwm4 code to support both X11 and Wayland in parallel. However, this approach turned out to be the wrong path forward for several reasons:

* Xfwm4 is architected in a way that makes it very difficult to put the window management behavior behind generic interfaces that don't include X11 specifics.
* Refactoring Xfwm4 is risky, since it might introduce new bugs to X11. Having two parallel code bases will allow for rapid development and experimentation with the Wayland compositor, with zero risk to break xfwm4.
* Some X11 window management concepts just aren't available or supported by Wayland protocols at this time, and dealing with those differences can be difficult in an X11-first code base.
* Using the existing codebase would require us to use C and wlroots, even if a better alternative is available.

### Why to base xfwl4 on smithay?

Once the decision to write a compositor from scratch was done, the next major question was: Which Wayland support library to use as a base? In order to find an answer on that question Brian evaluated wlroots and smithay. The decision to use smithay as a base was done for the following reasons:

* smithay supports most/all official Wayland protocol extensions, as well as the wlroots protocols and some KDE protocols.
* smithay has no high level abstraction, as wlroots has. However, it allows for very deep customization of the graphics and input pipeline, as well as all aspects of Wayland protocol and desktop/shell handling.
* smithay has great documentation.
* Using rust makes it easier to avoid memory related bugs and decreases the chances of crashes, something that should never happen for a Wayland compositor.
* Rather subjective: Brian has a strong preference to write code in rust over writing code in C.
* wlroots is written in C, in a way which makes it very difficult to write [wlroots rust bindings](https://way-cooler.org/blog/2019/04/29/rewriting-way-cooler-in-c.html).

### Scope of the project

Besides getting feature parity with xfwm4, the xfwl4 project scope includes as well some other related tasks:

* Major changes to session-startup will be required, since on Wayland the compositor has to be the root of the session instead of xfce4-session.
* Support for the xdg-session-management protocol is another goal.
* As well support for XWayland is part of the roadmap.
* The build system of the Xfce CI container will need to be upgraded in order to support building rust code via meson.

Brian has already started work on the project, so stay tuned for the first development release of xfwl4, which we hope to share around mid-year.

If you’re interested in the detailed reasoning behind the project or want to explore all the technical details, check out the [issues](https://gitlab.xfce.org/kelnos/xfwl4/-/issues) and the [work in progress source code](https://gitlab.xfce.org/kelnos/xfwl4).

For any questions related to xfwl4, please visit our Matrix channel [#xfce-dev](https://matrix.to/#/#xfce-dev:matrix.org).

We’d like to extend our heartfelt thanks to our generous supporters on [Open Collective US](https://opencollective.com/xfce) and [Open Collective EU](https://opencollective.com/xfce-eu) for making this project possible!

Best regards,

The Xfce development team