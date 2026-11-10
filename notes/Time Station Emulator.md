---
title: "Time Station Emulator"
url: https://github.com/kangtastic/timestation
clipped: 2026-06-17 01:52:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Time Station Emulator](https://github.com/kangtastic/timestation)

## Digest Summary
GitHub repository **kangtastic/timestation** provides software to synchronize radio‑controlled (“atomic”) clocks and watches using a smartphone or tablet. The project is open‑source under the MIT license. Build and test pipelines are shown via GitHub Actions workflow status and Codecov coverage badges. Implementation combines native code in **C** with web components built using **Lit**, typed with **TypeScript**, and compiled to **WebAssembly** for performance. The repository includes standard project assets such as a logo and licensing information. No additional documentation or usage instructions are present in the scraped content.

## Discussion Summary
The comments express interest in the concept of generating low‑power radio signals from audio hardware, noting past personal experiments and theoretical possibilities. Enthusiasm is balanced by doubts about practical effectiveness, especially given weak signals, limited demo evidence, and device restrictions such as iPhone browser constraints. Several remarks appreciate the novelty and soothing aspects of received time‑signal tones, while others voice concern over potential interference with clocks and question the claim of universal phone compatibility.

---

## Full Article

**Time Station Emulator** turns almost any phone or tablet into a low-frequency
radio transmitter broadcasting a time signal that can synchronize most
radio-controlled (“atomic”) clocks and watches.

Real time signal broadcasts are limited in geographic range and notoriously
prone to interference in urban areas, so many such clocks end up never actually
using their self-setting functionality. **Time Station Emulator** may allow
setting such clocks when/where a suitable signal is not otherwise available.

* **Compatible with most radio-controlled clocks**: Emulates the five
  operational radio time signal stations
  ([🇨🇳 BPC](https://en.wikipedia.org/wiki/BPC_(time_signal)),
  [🇩🇪 DCF77](https://en.wikipedia.org/wiki/DCF77),
  [🇯🇵 JJY](https://en.wikipedia.org/wiki/JJY),
  [🇬🇧 MSF](https://en.wikipedia.org/wiki/Time_from_NPL_(MSF)),
  and [🇺🇸 WWVB](https://en.wikipedia.org/wiki/WWVB)).
* **Network time**: Derives the current time from the network using an NTP-like
  algorithm.
* **Location-agnostic**: Supports applying an offset to the transmitted time of
  ±24 hours from the present.
* **BST/CEST/DST-aware**: Transmits daylight saving time information for DCF77,
  MSF, and WWVB.
* **Leap second-aware**: Transmits a DUT1 offset for MSF and WWVB.
* **Client-side, browser-based**: Runs entirely in the browser; no
  installation, no signup, no data collection.

The hard requirements of note are browser WebAssembly support and DAC support
for ≥44.1 KHz PCM. Almost any device running a browser from ≥2019 should
work.

In general, **Time Station Emulator** works best with a
**built-in speaker** of a **phone or tablet**. See
[Technical Details](https://github.com/kangtastic/timestation#technical-details) for an explanation.

As of early 2024, **Safari on iOS** and **Firefox on Android** had multiple
breaking issues that prevented them from working. As of early 2026, these
issues appear to have been resolved for at least some users. Good luck!

**Time Station Emulator** is hosted at <https://timestation.pages.dev/>.

click to expand/hide

1. **Choose emulator settings.**

   The most important setting is which time station to emulate. Certain settings
   are only available for certain stations.

   Clocks (or watches) that support more than one station may prefer one of them
   over the others.
2. **Choose any clock settings and place the clock into sync mode.**

   If your clock has them, try to choose station and/or time zone settings that
   make sense for your location.

   Most clocks provide a way to force a synchronization attempt. You will
   probably have to navigate menus and/or press physical buttons.
3. **Position the speaker as close as possible to the clock’s antenna.**

   The transmission range is quite short, so positioning is crucial. Some
   experimentation will probably be required, especially if you’re unsure where
   the antenna is.

   The volume should be set so that the clock picks up the cleanest signal.
   Usually, this occurs at or near the maximum possible volume.

   | WARNING |
   | --- |
   | **DO NOT PLACE YOUR EARS NEAR THE SPEAKER TO DETERMINE VOLUME.**  Use a visual volume indicator instead.  The generated waveform has full dynamic range, but is pitched high enough to be difficult to perceive.  **Even if you “can’t hear anything”,** many common devices are capable of playing it back loud enough to potentially cause **permanent hearing damage!** |
4. **Start transmitting and hold the speaker in position.**

   If all goes well, the clock will set itself within three minutes.

click to expand/hide

**Time Station Emulator** generates an audio waveform intentionally crafted to
create, when played back through consumer-grade audio hardware, the right kind
of RF noise to be mistaken for a time station broadcast.

Specifically, given a fundamental carrier frequency used by a real time station,
it generates and modulates the highest odd-numbered subharmonic that also falls
below the Nyquist frequencies of common playback sample rates.

One of the higher-frequency harmonics inevitably created by any real-world DAC
during playback will then be the original fundamental, which should leak to the
environment as a short-range radio transmission via the ad-hoc antenna formed by
the physical wires and circuit traces in the audio output path.

| NOTE |
| --- |
| Because it relies upon this leakage, **Time Station Emulator** works best with a **built-in speaker** of a **phone or tablet**.  In some cases, **wired headphones or earbuds** may also be suitable.  Higher-frequency harmonics are considered artifacts beyond the range of human hearing, so they are routinely suppressed by audio compression algorithms and better equipment.   Bluetooth devices and audiophile-grade equipment are therefore less likely to work. |

`src/shared/casefoldingmap.ts` derives from a
[data file](https://unicode.org/Public/UCD/latest/ucd/CaseFolding.txt)
published by the Unicode Consortium, and is
[Unicode licensed](https://unicode.org/license.txt).

`src/shared/icons.ts` derives from SVG icons originally part of
[ionicons v5.0.0](https://ionic.io/ionicons/) and
[Flagpack](https://flagpack.xyz/), and is MIT licensed by way of those projects.

All other files are also [MIT licensed](https://github.com/kangtastic/timestation/blob/main/LICENSE).