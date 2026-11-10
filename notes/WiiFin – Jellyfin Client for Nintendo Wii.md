---
title: "WiiFin – Jellyfin Client for Nintendo Wii"
url: https://github.com/fabienmillet/WiiFin
clipped: 2026-06-17 01:17:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - homebrew development
  - media streaming
  - nintendo wii
  - jellyfin
  - c++
  - mplayer
related:
  - "[[Homebrew Development]]"
  - "[[Media Streaming]]"
  - "[[Additive Blending on the Nintendo 64]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** WiiFin is an experimental, open-source homebrew Jellyfin client written in C++ for the Nintendo Wii.
>
> **Key points:**
> - WiiFin is developed in C++ using devkitPro tools, GRRLIB for graphics, and MPlayer CE for video playback.
> - It supports library browsing (movies, TV, music) and authentication (username/password or QuickConnect).
> - Video is transcoded server-side and streamed, supporting stereo audio and embedded subtitles.
> - Users can run WiiFin on a physical Wii (via DOL or WAD) or inside the Dolphin emulator.
>
> **Concept links:** [[Homebrew Development]], [[Media Streaming]], [[Nintendo Wii]], [[Jellyfin]], [[C++]], [[Mplayer]]
>
> **Suggested connections:**
> - [[Homebrew Development]] — creating unofficial applications for legacy console hardware.
> - [[Media Streaming]] — how open-source clients parse and play server-transcoded video.
> - [[Additive Blending on the Nintendo 64]] — another technical exploration of legacy game console hardware capabilities.
<!-- ai-summary:end -->
# [WiiFin – Jellyfin Client for Nintendo Wii](https://github.com/fabienmillet/WiiFin)

## Digest Summary
WiiFin is an experimental homebrew client for Jellyfin designed for the Nintendo Wii, written in C++ and built with devkitPro (devkitPPC, libogc, wii‑dev). It uses GRRLIB for graphics, libpngu, freetype, libjpeg, and integrates MPlayer CE (libmplayer.a) for video playback. Authentication supports username/password and QuickConnect; multiple profiles store only access tokens. The UI provides library browsing (movies, TV shows, music) with cover art, detail view (synopsis, rating, cast, audio/subtitle selection), Continue Watching/Next Up rows, and season/episode navigation. Playback is server‑side transcoded, streamed via the integrated MPlayer engine; only stereo audio is available and subtitles are embedded by the server. Progress is reported back to the Jellyfin server for resume. HTTPS connections use mbedTLS with self‑signed certificate support. Input is handled via Wiimote IR pointer and a virtual on‑screen keyboard. The project ships as a .dol and .wad installable via the Homebrew Channel or WAD manager, and can run in Dolphin emulator. It is GPL‑v3 licensed and actively developed.

## Discussion Summary
Comments highlight Jellyfin’s increasing popularity, noting it now surpasses Plex in TrueNAS catalog installs and is praised for reliable performance across devices such as Samsung TVs and custom Wii setups. Users appreciate its open‑source nature and potential for broader developer contributions, while also expressing interest in features like OpenSubsonic API support and better native transcoding options. Several remarks inquire about scaling the server for multi‑household use or clustering, and a few suggest creative hardware integrations, indicating overall positive sentiment tempered by technical improvement requests.

---

## Full Article

[![WiiFin logo](https://raw.githubusercontent.com/fabienmillet/WiiFin/refs/heads/main/assets/logo_wiifin_banner.png)](https://raw.githubusercontent.com/fabienmillet/WiiFin/refs/heads/main/assets/logo_wiifin_banner.png)  
*Jellyfin client for the Nintendo Wii*

[![English](https://camo.githubusercontent.com/3456d7e63f264e8b51c1d1b84d888934afe032b5d433d3df90d733cb2d2ceff8/68747470733a2f2f666c616763646e2e636f6d2f7734302f67622e706e67)](https://github.com/fabienmillet/WiiFin/blob/README.md)
 
[![Français](https://camo.githubusercontent.com/697d0536b9eeab940446fb0dcc5d20cd4170a3d5e0de3027b4e7333a070dc033/68747470733a2f2f666c616763646e2e636f6d2f7734302f66722e706e67)](https://github.com/fabienmillet/WiiFin/blob/main/README/README.fr.md)
 
[![Deutsch](https://camo.githubusercontent.com/67873da57b9448ca10f1344ee5ba546a4da8db7a52835ab95d617a347f2f52e9/68747470733a2f2f666c616763646e2e636f6d2f7734302f64652e706e67)](https://github.com/fabienmillet/WiiFin/blob/main/README/README.de.md)
 
[![Español](https://camo.githubusercontent.com/53f34c3a9d30afc4492cdd38f8bc1d1dee7abaeaba2e6eeecdbdfc50e8ca66d2/68747470733a2f2f666c616763646e2e636f6d2f7734302f65732e706e67)](https://github.com/fabienmillet/WiiFin/blob/main/README/README.es.md)
 
[![Italiano](https://camo.githubusercontent.com/6481eeb4ff48308f56e57de726ceea4ddbdce0f60739940406a88ab737f27777/68747470733a2f2f666c616763646e2e636f6d2f7734302f69742e706e67)](https://github.com/fabienmillet/WiiFin/blob/main/README/README.it.md)

---

**WiiFin** is an experimental homebrew client for [Jellyfin](https://jellyfin.org), built specifically for the Nintendo Wii.
It provides a lightweight, console-friendly media browsing and playback experience, written in C++ using [GRRLIB](https://github.com/GRRLIB/GRRLIB) and [MPlayer CE](https://github.com/dborth/mplayer-ce).

---

> 🚧 **Experimental** – functional but still under active development. Expect rough edges on real hardware.

* **Authentication**: login with username/password or via **QuickConnect** (approve on another device)
* **Saved profiles**: multiple accounts stored securely (access token only, no password stored)
* **Library browsing**: movies, TV shows, music libraries with cover art loaded from the server
* **Detail view**: synopsis, rating, genres, cast, director, audio/subtitle track selection
* **Continue Watching** and **Next Up** rows
* **TV shows**: season and episode navigation
* **Video playback**: server-side transcoding streamed through the integrated MPlayer CE engine
* **Music playback**: audio libraries, album/track navigation
* **Player overlay**: seek bar, volume control, next/prev episode, audio & subtitle track switching, intro skip
* **Playback reporting**: progress sent back to the Jellyfin server (resume where you left off)
* **HTTPS**: TLS connections via mbedTLS (self-signed certificates supported)
* **Wiimote IR pointer** and **virtual on-screen keyboard**
* **Background music** on menus
* Ships as a ready-to-use `.dol` and installable `.wad` (Wii / vWii)

* Direct-play is not supported; all video is transcoded by the server
* No 5.1 multi-channel audio (stereo only via transcoding)
* Subtitle rendering relies on the server embedding them into the video stream

---

* [devkitPro](https://devkitpro.org) with `devkitPPC`, `libogc`, and `wii-dev` portlibs
* Graphics: `GRRLIB`, `libpngu`, `freetype`, `libjpeg`
* mbedTLS (bundled under `libs/`, cross-compiled automatically by the CI)
* **Optional**: MPlayer CE compiled as `libmplayer.a` — required for video playback. See [MPLAYER\_CE\_BUILD.md](https://github.com/fabienmillet/WiiFin/blob/main/MPLAYER_CE_BUILD.md) for instructions. Without it, WiiFin still compiles but video playback is unavailable.

On **Dolphin Emulator**:

```
dolphin-emu -e WiiFin.dol
```

On **real Wii hardware**: copy `WiiFin.dol` to `SD:/apps/WiiFin/boot.dol`, or install `WiiFin.wad` using a WAD manager (works on vWii too).

---

```
WiiFin/
├── source/
│   ├── core/        # App lifecycle, background music, utilities
│   ├── input/       # Wiimote + USB keyboard input
│   ├── jellyfin/    # Jellyfin HTTP API client (HTTPS via mbedTLS)
│   ├── player/      # MPlayer CE integration, player overlay HUD
│   └── ui/          # All views: Connect, Library, Profile, Settings
├── data/            # PNG/TTF graphical assets
├── libs/            # Bundled mbedTLS
├── tools/           # WAD packager, banner generator
├── Makefile         # devkitPro-compatible build script
└── apps/WiiFin/     # Homebrew Channel metadata
```

---



---

[![WiiFin Menu Screenshot](https://github.com/fabienmillet/WiiFin/raw/main/assets/preview.png?raw=true)](https://github.com/fabienmillet/WiiFin/blob/main/assets/preview.png?raw=true)  
 *WiiFin running in Dolphin Emulator*

---

WiiFin is open to pull requests, bug reports, and suggestions.

[![Discord Badge](https://camo.githubusercontent.com/7f4794b6adb6eecea2c6b7b16c20e9b721472f0ff45ab34051a69745ddbc9fb3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e25323075732532306f6e253230446973636f72642d3538363546323f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/p9DXfEmUYu)


---

This project is licensed under the **GPLv3**.
See the [LICENSE](https://github.com/fabienmillet/WiiFin/blob/main/LICENSE) file for more details.