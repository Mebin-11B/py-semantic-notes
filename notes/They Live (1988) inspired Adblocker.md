---
title: "They Live (1988) inspired Adblocker"
url: https://github.com/davmlaw/they_live_adblocker
clipped: 2026-06-17 01:03:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [They Live (1988) inspired Adblocker](https://github.com/davmlaw/they_live_adblocker)

## Digest Summary
A fork of uBlock Origin Lite replaces cosmetically‑blocked ads with white tiles displaying random slogans from John Carpenter’s *They Live* (e.g., “OBEY”, “CONSUME”, “DO NOT QUESTION AUTHORITY”). The extension injects a ::after overlay sourced from a data‑ubol‑they‑live attribute, using a MutationObserver to tag newly loaded ads. Network‑blocked ads remain empty, as only cosmetic‑filtered elements are altered.  

**Installation & build**  
- Download the pre‑built uBOLite_theylive.chromium.zip or build from source (requires Node ≥ 22).  
- Clone the repo recursively, run tools/make‑mv3.sh for the target browser (Chromium, Firefox, Edge, Safari).  
- Load the generated uBlock/dist/build/uBOLite.chromium folder as an unpacked extension.  

**Usage**  
- Set uBO Lite filtering mode to Optimal or Complete via the dashboard to enable the “OBEY” tiles.  

**Limitations**  
- Only cosmetic filters are affected; custom cosmetic rules hide ads normally.  
- Re‑exposing previously hidden elements may shift page layout.  

The project is a personal hobby fork, GPL‑3.0 licensed, and not an official uBlock Origin release.

## Discussion Summary
The comments convey strong positive nostalgia for the film, describing it as a formative influence that encouraged skepticism toward fads, peer pressure, and authority while prompting later interest in philosophical ideas. Viewers recommend it for younger audiences despite potential scariness, noting it could foster mental resilience. There is enthusiasm for adapting the work to modern platforms such as Apple Vision Pro, with suggestions on visual style and willingness to invest financially, reflecting overall appreciation and interest in broader accessibility.

---

## Full Article

[![They Live billboards](https://github.com/davmlaw/they_live_adblocker/raw/main/docs/they-live-billboards.jpg)](https://github.com/davmlaw/they_live_adblocker/blob/main/docs/they-live-billboards.jpg)

A fork of [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home) that, instead of *hiding* cosmetically-blocked ads, **replaces** them with white tiles bearing slogans from John Carpenter's 1988 film *They Live*: **OBEY**, **CONSUME**, **WATCH TV**, **SLEEP**, **SUBMIT**, **CONFORM**, **STAY ASLEEP**, **BUY**, **WORK**, **NO INDEPENDENT THOUGHT**, **DO NOT QUESTION AUTHORITY**.

Each blocked ad gets a single phrase, picked at random from the list.

The idea is from a blog post I wrote in 2015 (and never got around to building): [*They Live adblock mode*](https://proceduralgraphics.blogspot.com/2015/04/they-live-adblock-mode.html).

Now on [YouTube - Fireship 10 weird OSS projects you need right now...](https://www.youtube.com/watch?v=qPuzWFvRajk&t=137s) -

[![reddit_screenshot](https://private-user-images.githubusercontent.com/763201/590772819-908b6602-078a-4d78-abc0-9ca13e22d62e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2Mzg3MzgsIm5iZiI6MTc4MTYzODQzOCwicGF0aCI6Ii83NjMyMDEvNTkwNzcyODE5LTkwOGI2NjAyLTA3OGEtNGQ3OC1hYmMwLTljYTEzZTIyZDYyZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQxOTMzNThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjhhYmU4Mzc3YzcwODIzYjMxNGI4MmYyNTY5YjNjMTk2NWE0ZjgzNmI1MGRlZGY3NzdhOWFiOTRlYTRmMjljJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.7ZLfPrQy4u0lH75KkXhDP5bP_NZxnjjRmWmujL7Ccmc)](https://private-user-images.githubusercontent.com/763201/590772819-908b6602-078a-4d78-abc0-9ca13e22d62e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2Mzg3MzgsIm5iZiI6MTc4MTYzODQzOCwicGF0aCI6Ii83NjMyMDEvNTkwNzcyODE5LTkwOGI2NjAyLTA3OGEtNGQ3OC1hYmMwLTljYTEzZTIyZDYyZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQxOTMzNThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjhhYmU4Mzc3YzcwODIzYjMxNGI4MmYyNTY5YjNjMTk2NWE0ZjgzNmI1MGRlZGY3NzdhOWFiOTRlYTRmMjljJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.7ZLfPrQy4u0lH75KkXhDP5bP_NZxnjjRmWmujL7Ccmc)

Download the latest **`uBOLite_theylive.chromium.zip`** from the [Releases page](https://github.com/davmlaw/they_live_adblocker/releases), extract it, then in Chromium / Chrome / Brave / Edge:

1. Open `chrome://extensions`
2. Toggle **Developer mode** on (top-right)
3. Click **Load unpacked** and select the extracted folder

Keep the folder around — the extension is loaded from that path.

### Make it actually replace ads

By default uBO Lite uses **Basic** filtering mode, which blocks ads at the network layer. Network-blocked ads never produce a DOM element, so there's nothing to "they-live-ify" — you just get empty space, as with normal uBO Lite. To see the OBEY tiles:

1. Click the uBO Lite toolbar icon → cog (⚙) → Dashboard.
2. Set the filtering mode for the sites you care about to **Optimal** or **Complete**.
3. Reload.

Requires Node 22.

```
git clone --recursive https://github.com/davmlaw/they_live_adblocker
cd they_live_adblocker/uBlock
nvm use 22                       # or otherwise ensure Node >= 22
tools/make-mv3.sh chromium       # or: firefox | edge | safari
```

The packaged extension lands in `uBlock/dist/build/uBOLite.chromium/` — load it as an unpacked extension.

uBO Lite's cosmetic filtering normally injects CSS like `selector { display: none !important }` to hide matched ad elements. This fork patches those injection sites to instead apply a white-box mask with a `::after` overlay whose `content` is read from a `data-ubol-they-live` attribute, then walks the DOM (with a MutationObserver for late-loaded ads) to tag each matched element with a random phrase from the list.

Touched files in the [`davmlaw/uBlock`](https://github.com/davmlaw/uBlock/tree/they-live) submodule:

* `platform/mv3/extension/js/scripting/they-live.js` *(new)* — phrase list, CSS generator, DOM tagging
* `platform/mv3/extension/js/scripting/css-{specific,generic,procedural-api}.js` — call sites
* `platform/mv3/extension/js/scripting-manager.js` — registers `they-live.js` ahead of consumers

* Personal hobby fork; **not** an official uBlock Origin product. Don't file uBO issues against this.
* Forcing previously-hidden elements visible can occasionally shift page layout where the site's CSS assumed the ad slot collapsed.
* Custom user-defined cosmetic filters still hide normally (no OBEY treatment).
* Network-blocked ads (most of uBO Lite's blocking) don't get replaced — only cosmetic-filtered ones do.

GPL-3.0, same as upstream uBlock Origin / uBO Lite.