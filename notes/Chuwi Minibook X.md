---
title: "Chuwi Minibook X"
url: https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/
clipped: 2026-06-17 00:54:20
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Chuwi Minibook X](https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/)

## Digest Summary
The Chuwi Minibook X is a 10.5‑inch x86_64 sub‑ultrabook priced at $350. It ships with an Intel N150 4‑core/4‑thread 3.6 GHz CPU, 16 GB LPDDR5‑6400 RAM (soldered), a 512 GB NVMe SSD (upgradable), a 2K IPS 16:10 display, 28.88 Wh Li‑ion battery, and two USB‑C ports (one PD‑capable). It includes a 12 V/2 A charger but works with standard PD chargers.

Linux runs with most hardware functional (camera, microphone, touchscreen, sleep/hibernate, keyboard backlight, USB‑C HDMI, Bluetooth, Wi‑Fi 6). The built‑in tablet panel is mounted sideways, requiring rotation fixes at multiple layers: GRUB/systemd‑boot bootloader patches, kernel parameters (`video=DSI-1:panel_orientation=right_side_up`, `fbcon=rotate:1`), loading the i915 driver in the initramfs, and X11 `xrandr` or Wayland DRM rotation.

Performance: Geekbench 6 scores 1295 (single) / 3332 (multi); idle power ~3.8 W, benchmark ~15 W; battery lasts ~6 h of video playback. Stress‑ng tests keep chassis temperature below 32 °C (90 °F). Drawbacks include low‑refresh 2K panel, imprecise keyboard, sub‑par touchpad, and tinny speakers. The device is positioned as a low‑cost platform for Linux experimentation.

## Discussion Summary
Comments describe the Chuwi Minibook X as a compact, low‑price device that runs Linux well and offers a high‑density display, making it appealing for travel and lightweight tasks. Positive notes highlight its small size, decent keyboard for some users, and acceptable performance for basic use, while criticisms focus on limited USB ports, modest battery life, a subpar trackpad, screen‑rotation quirks, and inconsistent keyboard reliability. Several remarks mention poor after‑sales support and warranty concerns, and many compare it unfavorably to higher‑spec alternatives such as GPD models. Overall sentiment is mixed, balancing affordability and portability against quality and support drawbacks.

---

## Full Article

Netbooks are dead, but the Chuwi Minibook X scratches the same
itch.

The Minibook X is a 10.5â³ x86\_64 sub-ultrabook with 16GB RAM, a 512GB
NVMe drive, and only one majorly annyoing Linux quirk.

I needed a knock-around laptop, so I bought myself a Minibook for my
birthday last year. The more I tote it around, the more fun Iâm having
with this ridiculous little computer.

[![Chuwi Minibook X, KDE lock screen](https://photos.tylercipriani.com/thumbs/58/ec9d31f64e7d203a6d40603d8ec352/medium.jpg)


Chuwi Minibook X](https://photos.tylercipriani.com/thumbs/58/ec9d31f64e7d203a6d40603d8ec352/xlarge.jpg)

Quick specs
-----------

Much like the netbooks of yore, the Minibook is a budget machine. But
itâs 2026, so even budget machines pack more oomph than I need from a
utility laptop.

* CPU 4-core/4-thread 3.6GHz Intel N150 Twin Lake
* 16 GB RAM â LPDDR5-6400 â soldered ð¿
* 512GB NVMe â upgradable
* 10.51â IPS 2K 16:10 screen
* 28.88Wh Li-Ion battery
* Weight: 911g
* Ports: 2ÃUSB-C (1ÃPD charging)
* Cost: $350

[![Chuwi Minibook with back cover removed, exposing battery and NVMe drive](https://photos.tylercipriani.com/thumbs/a1/cbe8bd56a1085ab2e3c7a6388bed5f/medium.jpg)


Chuwi Minibook Guts](https://photos.tylercipriani.com/thumbs/a1/cbe8bd56a1085ab2e3c7a6388bed5f/xlarge.jpg)

One oddity is that the Minibook comes bundled with a 12V/2A USB-C
charger. I chucked the charger; I worried Iâd fry some 5V SoC someday.
The Minibook works fine with a PD charger.

[![Minibook X using a PD Charger at 20V](https://photos.tylercipriani.com/thumbs/18/7a50ffe3248627bddf4ca435c047a5/medium.jpg)


Minibook X using a PD Charger at 20V](https://photos.tylercipriani.com/thumbs/18/7a50ffe3248627bddf4ca435c047a5/xlarge.jpg)

Iâd assume the 12V charger was a cost-saving choice, but it also
creates some weird possibilities for DC/off-grid setups.

Linux and weirdness: sideways panels and kernel parameters
----------------------------------------------------------

![Charlie Stross, one of my favorite SciFi authors, recommended the Chuwi Minibook X on Mastodon](https://photos.tylercipriani.com/2026-05-17_cstross-chuwi-minibook.png)


[Charlie Stross](https://wandering.shop/@cstross), a favorite SciFi author, talks up the Chuwi Minibook X on [Mastodon](https://wandering.shop/@cstross/113279670998603629)

The fediverse told me that Minibook runs Linux âboringly well,â which
was *almost* true.

I tried Debian, then jumped to NixOS for kicks.

What works:

* Camera/Microphone/Speakers
* Touchscreen
* Sleep/Suspend
* Hibernate
* Keyboard backlight
* USB-C HDMI
* Bluetooth (non-free blobs â Intel)
* Wi-Fi 6 (non-free blobs â Intel)

But on first boot, the screen orientation is 270Â° clockwise:

[![Tails setup screen rotated](https://photos.tylercipriani.com/thumbs/fd/618ab5184903c7a8a69428d4df70e0/medium.jpg)](https://photos.tylercipriani.com/thumbs/fd/618ab5184903c7a8a69428d4df70e0/xlarge.jpg)


Linux setup screen rotated 270Â°.

The Chuwiâs screen is a panel from a cheap tablet; the screen
rotation issue is a hardware problem (the screen is mounted sideways).
To fix the screenâs rotation, I had to tweak screen orientation at every
software layer. Fixing this problem was a journey:

1. Bootloader â Switched from `systemd-boot` to
   `grub`, carrying some [unmerged
   GRUB rotation patches](https://github.com/iggyZiggy/chuwi-grub-rotation-nix-patch) on top.
2. Initrd â Tell the Intel display driver about the panel orientation
   via a kernel parameter, and force the Intel driver to load in the
   initramfs. On NixOS:
   `boot.kernelParams = ["video=DSI-1:panel_orientation=right_side_up"];`
   and `boot.initrd.kernelModules = ["i915"];` (see Kernel docs
   for [modedb default
   video mode support](https://docs.kernel.org/fb/modedb.html))
3. Desktop environment â For X11, good ole
   `xrandr --output DSI-1 --rotate right`. Wayland picked this
   up from the DRM connector. This one was easy.
4. Framebuffer â Ensure all TTYs have the proper orientation by adding
   `fbcon=rotate:1` to kernel parameters
   `boot.kernelParams = ["fbcon=rotate:1"];` (see Kernel docs
   for [framebuffer
   console boot options](https://docs.kernel.org/fb/fbcon.html#c-boot-options))

Behold, the final result in all its glory:

[](https://photos.tylercipriani.com/2026-05-31_chuwi-boot-smol.mp4)


Non-rotated system boot. Zero Cool's bootscreen courtesy of [`mainframed/Hackers-Plymouth`](https://github.com/mainframed/Hackers-Plymouth)

Perf, thermals, and power
-------------------------

tl;dr: you get what you pay for. But battery life and cooling are
better than Iâd have guessed.

The Minibook X was never going to compile the Linux kernel in record
time. But the performance matches the specs, it stays cool, and it has
enough battery life to run a movie marathon.

Numbers:

* Geekbench6 (a fun side-quest to get running on NixOS), better than I
  [expected](https://browser.geekbench.com/search?q=n150).
  + Single-core: 1295
  + Multi-core: 3332
* Wi-Fi 6 speed: 424 Mbps, more than enough to stream a 4K movie.
* Power
  + Idle: 3.8W
  + During benchmark: ~15W

Battery: When I left the 1995 classic film âHackersâ looping in VLC,
the battery lasted about 6 hours.

Heat: Running `stress-ng` for 10 minutes, the hottest part
of the laptop chassis remained below 90Â°F (32Â°C):

[![Chuwi Minibook X running stress-ng on thermal camera. Thermal camera reads 88.4Â°F](https://photos.tylercipriani.com/thumbs/e1/ece6929d3378c0b9bff4e42c4f687d/medium.jpg)


Thermal camera view of Chuwi Minibook X running `stress-ng`](https://photos.tylercipriani.com/thumbs/e1/ece6929d3378c0b9bff4e42c4f687d/xlarge.jpg)

What I dislike
--------------

Thereâs so much to dislike about this laptop:

* Screen is terrible â 2K? 50Hz refresh rate? Why!?
* Keyboard is terrible â it only registers keystrokes when you hit the
  exact center of each key.
* Touchpad is terrible â Itâs a diving board-style, without physical
  buttons.
* Sound is meh â I can hear the tinny laptop speaker fine, but itâs
  underwhelming. Iâve never tried tweaking it in Pipewire, though; itâs
  possible it could be better.

But âterribleâ is in comparison to the nicest modern laptops in
existence. Everything I listed here works fine. Iâm honestly blown away
when I tune my expectations to the sub-$400 laptop range.

Verdict
-------

In [*The
Death and Life of Great American Cities*](https://en.wikipedia.org/wiki/The_Death_and_Life_of_Great_American_Cities), Jane Jacobs wrote,
ânew ideas require old buildingsâ: cheap spaces let people try risky
ideas.

The Chuwi Minibook X is an old building.

I can brick the Minibook and have a normal Monday on my serious work
laptop. Nothing has to work, which makes it perfect to try out new Linux
desktop stuff:

* NixOS â Iâve been using Debian for 15 years+, figured Iâd try
  joining the NixOS cult for a while.
* RiverWM â Iâm on a quest to find the Wayland version of XMonad; [River](https://github.com/riverwm/river) is pretty close.
* KDE Plasma â Iâve used a tiling window manager for over a decade.
  Whatâs it like to use a desktop that Just Worksâ¢?
* Steam â Never been much into games, but I decided to give Steam a
  try since, well, why not?

Cheap, weird computers like the Chuwi make it safe to play. And
playing with computers is still fun.

[](https://photos.tylercipriani.com/2026-05-19_chuwi-melatonin-smol.mp4)


Playing [Melatonin](https://store.steampowered.com/app/1585220/Melatonin/) on Steam on the Chuwi