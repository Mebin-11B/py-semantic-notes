---
title: "OpenScreen is an open-source alternative to Screen Studio"
url: https://github.com/siddharthvaddem/openscreen
clipped: 2026-06-17 01:22:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [OpenScreen is an open-source alternative to Screen Studio](https://github.com/siddharthvaddem/openscreen)

## Digest Summary
OpenScreen is a free, open‑source screen‑recording application positioned as a lightweight alternative to the commercial product Screen Studio. Licensed under the MIT License, it permits unrestricted personal and commercial use, modification, and distribution. Core capabilities include full‑screen or window‑specific capture, microphone and system‑audio recording, customizable automatic or manual zooms, cropping, background selection (wallpaper, solid, gradient, custom), motion‑blur smoothing, annotations (text, arrows, images), clip trimming, segment‑wise speed adjustment, and export in various aspect ratios and resolutions. The app is built with Electron, React, TypeScript, Vite, PixiJS, and dnd‑timeline. Platform support:

- macOS 13+ (system audio requires macOS 14.2+ permission; older versions lack system audio);
- Windows (audio works out‑of‑the‑box);
- Linux (requires PipeWire; older PulseAudio may lack system audio).

Installation uses GitHub releases: macOS app bundle (requires Gatekeeper bypass via `xattr -rd com.apple.quarantine` and screen‑recording/accessibility permissions), Windows installer, and Linux AppImage (may need `--no-sandbox`). Contributions are welcomed via GitHub issues and roadmap.

## Discussion Summary
The comments acknowledge ScreenStudio’s ease of use and ability to produce polished videos quickly, with several users expressing genuine appreciation and interest in trying it. However, many note the $29‑$30 monthly cost as excessive, especially given its proprietary model, and compare it unfavorably to free or open‑source options such as OBS, Cap, Recordly, or self‑hosted Loom alternatives. Requests for additional features like presets, UI controls, and better Linux integration appear alongside curiosity about performance advantages over existing tools.

---

## Full Article

Warning

This started as a side project that blew up; not production grade and you'll hit bugs, but hopefully it covers what you need. **This project will soon be archived.**

[![OpenScreen Logo](https://github.com/siddharthvaddem/openscreen/raw/main/public/openscreen.png)](https://github.com/siddharthvaddem/openscreen/blob/main/public/openscreen.png)
  
  
[![siddharthvaddem%2Fopenscreen | Trendshift](https://camo.githubusercontent.com/cd190f91a1ec02ffcba7cecbfe0caa70fa04eb31658ac41d04df1e5a016e86d7/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3137343237)](https://trendshift.io/repositories/17427)

**OpenScreen is your free, open-source alternative to Screen Studio.**

If you don't want to pay $29/month for Screen Studio but want a version that does what most people seem to need - quick, polished product demos and walkthroughs you'd post on X, Reddit or Youtube. OpenScreen does not offer every Screen Studio feature, but covers a lot of the core functionality.

Screen Studio is an awesome product and this is definitely not a 1:1 clone. If you just want something fully free and open source, this project should cover most of your needs.

**100% free** for both **personal** and **commercial** use. Use it, modify it, distribute it. Please respect the License.

Note

Software should be accessible. OpenScreen has no paid tiers, premium features, upsells, or functionality locked behind a paywall.

[![](https://github.com/siddharthvaddem/openscreen/raw/main/public/demo.png)](https://github.com/siddharthvaddem/openscreen/blob/main/public/demo.png)
[![](https://github.com/siddharthvaddem/openscreen/raw/main/public/sample.png)](https://github.com/siddharthvaddem/openscreen/blob/main/public/sample.png)

* Record a specific window, or your whole screen.
* Record microphone and system audio.
* Webcam overlay with picture-in-picture, drag-to-position, mirroring, and shape options.
* Auto or manual zooms with adjustable depth, duration, easing, and pixel-precise position; auto-zoom follows your cursor as you work.
* Custom cursor size, smoothing, and click effects, with cursor themes and post-recording path smoothing.
* Automatic captions for voiceovers, generated on-device with no upload (works offline).
* Wallpapers, solid colors, gradients, or your own background image.
* Motion blur.
* Crop, trim, and per-segment speed control on the timeline.
* Text, arrow, and image annotations, with text animation presets.
* Timeline snapping guides and an audio waveform to make trimming easier.
* Customizable keyboard shortcuts.
* Export to MP4 or GIF in multiple aspect ratios and resolutions.
* Languages supported: Arabic, English, Spanish, French, Italian, Japanese, Korean, Portuguese (Brazil), Russian, Turkish, Vietnamese, Simplified Chinese, and Traditional Chinese.

Download the latest installer for your platform from the [GitHub Releases](https://github.com/siddharthvaddem/openscreen/releases) page.

The easiest way to install on macOS is via [Homebrew](https://brew.sh):

```
brew install --cask siddharthvaddem/openscreen/openscreen
```

Brew automatically picks the right build for Apple Silicon or Intel, and verifies the download against a notarized signature so Gatekeeper won't block it.

To update later: `brew upgrade --cask openscreen`
To uninstall: `brew uninstall --cask openscreen` (add `--zap` to also remove app data)

#### Manual install (if you prefer)

If you'd rather grab the `.dmg` directly from the [Releases page](https://github.com/siddharthvaddem/openscreen/releases) and encounter Gatekeeper blocking the app, you can bypass it by running the following command in your terminal after installation:

```
xattr -rd com.apple.quarantine /Applications/Openscreen.app
```

Note: Give your terminal Full Disk Access in **System Settings > Privacy & Security** to grant you access and then run the above command.

After running this command, proceed to **System Preferences > Security & Privacy** to grant the necessary permissions for "screen recording" and "accessibility". Once permissions are granted, you can launch the app.

Note

**Upgrading from an older version and hitting permission issues?** If you already had OpenScreen installed and the new version won't record (Screen Recording or Accessibility keep failing even after you grant them), uninstall the old version, remove OpenScreen's existing entries under **System Settings > Privacy & Security** (both Screen Recording and Accessibility), then do a fresh install and grant the permissions again when prompted.

Install via [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/):

```
winget install SiddharthVaddem.OpenScreen
```

To update later: `winget upgrade SiddharthVaddem.OpenScreen`
To uninstall: `winget uninstall SiddharthVaddem.OpenScreen`

If you'd rather grab the `.exe` installer directly, download it from the [Releases page](https://github.com/siddharthvaddem/openscreen/releases).

Three packages are published to the [Releases page](https://github.com/siddharthvaddem/openscreen/releases) for each version. Pick the one that matches your distro:

**Debian / Ubuntu / Pop!\_OS (`.deb`)**

```
sudo apt install ./Openscreen-Linux-latest.deb
```

**Arch / Manjaro (`.pacman`)**

```
sudo pacman -U Openscreen-Linux-latest.pacman
```

**Any distro (`.AppImage`)**

```
chmod +x Openscreen-Linux-*.AppImage
./Openscreen-Linux-*.AppImage
```

**NixOS / Nix (flake)**

Try without installing:

```
nix run github:siddharthvaddem/openscreen
```

Install into your user profile:

```
nix profile install github:siddharthvaddem/openscreen
```

For a NixOS system config (flake):

```
{
  inputs.openscreen.url = "github:siddharthvaddem/openscreen";

  outputs = { nixpkgs, openscreen, ... }: {
    nixosConfigurations.<host> = nixpkgs.lib.nixosSystem {
      modules = [
        openscreen.nixosModules.default
        { programs.openscreen.enable = true; }
      ];
    };
  };
}
```

For Home Manager, use `openscreen.homeManagerModules.default` with the same `programs.openscreen.enable = true;`.

You may need to grant screen recording permissions depending on your desktop environment.

**Sandbox error:** If the AppImage fails to launch with a "sandbox" error, run it with `--no-sandbox`:

```
./Openscreen-Linux-*.AppImage --no-sandbox
```

Everything in the editor and export is the same on macOS, Windows, and Linux: zooms, backgrounds, motion blur, crop/trim/speed, blur regions, annotations, auto-captions, projects, export, and all languages. The differences are in **capture**, where macOS and Windows use a native pipeline that Linux doesn't have:

* **Native recording**: macOS (ScreenCaptureKit) and Windows (Windows Graphics Capture) record through a native pipeline for higher quality and clean window-level capture. Linux records through the browser pipeline instead.
* **Custom cursors**: on macOS and Windows the real cursor is captured (shape, type, and clicks), which powers the cursor themes, click effects, and editable cursor overlay. On Linux only the cursor position is captured (used for auto-zoom), so those cursor options aren't available.
* **Webcam**: captured natively on macOS and Windows; on Linux it's recorded through the browser, but still works as a picture-in-picture overlay.
* **System audio** support varies by OS:
  + **macOS**: requires macOS 13+. On macOS 14.2+ you'll be prompted to grant audio capture permission. macOS 12 and below can't capture system audio (mic still works).
  + **Windows**: works out of the box.
  + **Linux**: needs PipeWire (default on Ubuntu 22.04+, Fedora 34+). Older PulseAudio-only setups may not capture system audio (mic should still work).

---

This project is licensed under the [MIT License](https://github.com/siddharthvaddem/openscreen/blob/main/LICENSE). By using this software, you agree that the authors are not liable for any issues, damages, or claims arising from its use.