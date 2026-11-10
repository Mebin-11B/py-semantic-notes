---
title: "OpenLogi"
url: https://openlogi.org/en
clipped: 2026-08-31 12:22:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [OpenLogi](https://openlogi.org/en)

## Digest Summary
OpenLogi is an independent, open‑source tool for configuring Logitech peripherals; it is not affiliated with or endorsed by Logitech, whose trademarks (e.g., “Logitech,” “MX Master,” “Options+”) remain theirs. The program and Logitech’s Options+ both communicate via HID++ and cannot share a receiver simultaneously—Options+ must be closed before OpenLogi can claim the device. Supported hardware includes MX Master 4, 3S, 3, MX Anywhere 3, Signature M650, Ergo M575, as well as Logitech keyboards (F‑row remapping, Fn‑lock, RGB/backlight), Litra lighting, and webcams, usable through Logi Bolt, Unifying, Lightspeed receivers, Bluetooth, or USB. OpenLogi runs on Linux (deb, rpm, Arch packages with udev rules and a systemd user unit) and Windows (validated on Windows 11, signed MSI installers). It performs no network communication aside from optional image downloads and an opt‑in update check. All settings are saved in a single plain‑text TOML file, editable by hand or via the GUI.

---

## Full Article

HID++BoltUnifyingBluetoothUSB

# Your Logitech mousekeyboardcamera,finally local.

A local-first alternative to Logitech Options+, written in Rust.Remap buttons, drive DPI and SmartShift over HID++.No account, no telemetry.[Download](https://openlogi.org/en#install)$brew install --cask openlogi

.dmg.deb / .rpm / .pkg.tar.zst.msiMIT / Apache-2.0Not affiliated with LogitechHID++ 0x2111smartShiftEnhancedHID++ 0x2150thumbwheel

## Click a button, bind an action.

The center of the app, working right here: a mouse diagram with clickable hotspots and a per-button action picker. Choose a hotspot, then bind any of the built-in actions.config.tomlschema_version = 4MX Master 4~/.config/openlogi/config.tomllive ` `schema_version = 4`  `selected_device = "receiver:aabbccdd:slot:1"`  ` `  `[devices."receiver:aabbccdd:slot:1".bindings]`  `MiddleClick   = "MissionControl"`  `DpiToggle     = "CycleDpiPresets"`  `Thumbwheel    = "VolumeUp"`  `Forward       = "BrowserForward"`  `Back          = "BrowserBack"`  `GestureButton = "AppExpose"` ` MX Master 4Writes straight to  `config.toml` , the file you own.

## Everything Options+ does, without the account.

OpenLogi drives your mouse over HID++ directly: buttons, DPI and SmartShift, from a native app that never phones home.HID++ 2.044 actions

### Remap any button

Bind any of 44 built-in actions to each physical button, per device. Custom shortcuts, app launchers and scripted actions too.

### DPI control & presets

Set pointer resolution and cycle your own presets, written straight to the sensor over HID++.HID++ 0x2201

### SmartShift

Flip the wheel between ratchet and free-spin, or let it switch automatically by scroll speed.HID++ 0x2111

### Per-app profilesComing soon

Per-application overlays that switch the moment your focused app does. Ships in a later release.

### Bolt, Unifying, Lightspeed, Bluetooth or wired

Reach devices over a Logi Bolt, Unifying or Lightspeed receiver, a direct Bluetooth pairing, or a USB cable. No receiver required.

### Live device view

A carousel of paired devices with battery percentage and charge state for everything online.HID++ 0x1004

## Nothing between your mouse and your machine.

No account, no telemetry, no cloud. Bindings live in a plain TOML file you own, and every change goes straight to the device over HID++.NetworkDevice renders only

## Up and running in a minute.

Signed builds for macOS, Linux and Windows. Pick your platform below. Step-by-step setup lives in the docs..dmg.deb.rpm.msi

### macOS

$brew install --cask openlogi[Download .dmg](https://openlogi.org/download/macos)

Homebrew is recommended, or grab the signed .dmg for Apple silicon or Intel.

### Linux

[Download .deb](https://openlogi.org/download/linux)

Packages for amd64 and arm64, with .rpm and Arch .pkg.tar.zst builds also available.

### Windows

New[Download .msi](https://openlogi.org/download/windows)

The newest port: signed x86_64 and arm64 installers, validated on Windows 11.

Quit Logi Options+ before launching: the two fight over HID++ access, and only one app can own a receiver at a time. On Linux, the same applies to Solaar.

## Things you might ask.

Something else? Ask in [Telegram](https://t.me/openlogi_org) or open a [GitHub issue](https://github.com/AprilNEA/OpenLogi/issues).Will OpenLogi support Logitech Flow?It's on the roadmap, at the far end: a cross-computer pointer and clipboard bridge is a very large feature. The half that lives in the protocol already ships. OpenLogi drives Easy-Switch host switching over HID++ (0x1814/0x1815), and paired mice follow the keyboard when it switches hosts. If the rest lands, it will be opt-in and local-network only.Can I pair a new device from OpenLogi?Bolt pairing ships in the GUI, and Unifying and Lightspeed pairing is in progress. Until it lands, pair once with Logitech's tool or Solaar; OpenLogi drives the device from then on.Can I import my Options+ settings?Not yet, though an importer is in progress. In the meantime, bindings are a short TOML file you can rebuild in minutes, and unlike Options+ they stay in one portable, hand-editable file.Why does macOS ask for Accessibility permission?OpenLogi remaps the side buttons (Back, Forward, middle click) through a CGEventTap, and macOS puts event taps behind the Accessibility permission. The HID++ paths (gesture button, thumb wheel, DPI, SmartShift) don't need it.How do updates work?Only when you ask. The in-app update check is opt-in and off by default; new builds come from Homebrew (brew upgrade --cask openlogi) or the signed installers on the releases page.Do my bindings move to another machine?Copy the TOML file. Devices are keyed by physical identity (receiver serial and slot, or the device's own serial), so the same mouse keeps its bindings wherever the file goes. Built-in sync may come one day, but it's hard to square with the no-account principle.
