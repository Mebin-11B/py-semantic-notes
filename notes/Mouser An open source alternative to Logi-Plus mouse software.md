---
title: "Mouser: An open source alternative to Logi-Plus mouse software"
url: https://github.com/TomBadash/MouseControl
clipped: 2026-06-17 01:33:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Mouser: An open source alternative to Logi-Plus mouse software](https://github.com/TomBadash/MouseControl)

## Digest Summary
Mouser is an open‑source, local alternative to Logitech Options+ for the Logitech MX Master 3S mouse. It runs on Windows 10/11 and macOS 12+, requires no Logitech software, and stores all configuration in a local JSON file. Key capabilities include:

- Remapping all six programmable buttons with 22 built‑in actions (navigation, editing, media, etc.).
- Per‑application profiles that auto‑switch when the foreground app changes (detected via periodic GetForegroundWindow polling).
- DPI control (200–8000) and independent vertical/horizontal scroll inversion, synchronized via HID++.
- Full HID++ 2.0 gesture‑button support over Bluetooth and a three‑tier fallback (raw input, middle‑click redirection).
- Low‑level Windows mouse hook (SetWindowsHookExW, WH_MOUSE_LL) and macOS CGEventTap for event interception; key simulation uses SendInput (Windows) or Quartz events (macOS).
- Qt Quick UI with interactive mouse diagram, system‑tray control, and real‑time connection status.
- Portable build via PyInstaller; source installation uses Python 3.10+, PySide6, hidapi, pystray, Pillow.

The repository includes core modules (engine, mouse_hook, hid_gesture, key_simulator, config, app_detector) and UI QML files. Contributions focus on extending support to other HID++ devices, improving scroll inversion, and porting to Linux.

## Discussion Summary
Comments express strong dissatisfaction with Logitech’s Options+ software, criticizing its bloat, telemetry, frequent updates, and poor macOS permissions, while noting occasional functional adequacy but high resource use. Users highlight a demand for open‑source or third‑party replacements, citing tools such as MacMouseFix, BetterTouchTool, Piper, LinearMouse, and similar utilities that offer remapping, smooth scrolling, and device‑switching features. Several remarks note missing capabilities compared with Options+, especially macro and chord support, and concern about long‑term maintenance of community‑driven alternatives. Overall sentiment favors alternatives and calls for more reliable, lightweight solutions.

---

## Full Article

Mouser — Logitech Mouse Remapper
================================

[![Mouser logo](https://github.com/TomBadash/Mouser/raw/master/images/logo_icon.png)](https://github.com/TomBadash/Mouser/blob/master/images/logo_icon.png)

English | [中文文档](https://github.com/TomBadash/Mouser/blob/master/README_CN.md)

A lightweight, open-source, fully local alternative to **Logitech Options+** for
remapping Logitech HID++ mice. The current best experience is on the **MX Master**
and **MX Anywhere** families, with detection and fallback UI support for additional
Logitech models.

**No telemetry. No cloud. No Logitech account required.**

---



---

> **No install required.** Just download, extract, and double-click.

[![Windows Downloads](https://camo.githubusercontent.com/b5c296e96d867d432eb77bd11ea622c7caabf6b0145294cc6792b78178139877/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f6c61746573742f4d6f757365722d57696e646f77732e7a69703f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6f676f3d77696e646f7773266c6162656c3d57696e646f777326646973706c617941737365744e616d653d66616c7365)](https://github.com/TomBadash/Mouser/releases/latest)
[![macOS Apple Silicon Downloads](https://camo.githubusercontent.com/c5b6e94dd05a8a69cd7e27e2d6df4b8f9a2f5f3b51737ea7d973bf4c871974cd/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f6c61746573742f4d6f757365722d6d61634f532e7a69703f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6f676f3d6170706c65266c6162656c3d6d61634f532532304170706c6525323053696c69636f6e26646973706c617941737365744e616d653d66616c7365)](https://github.com/TomBadash/Mouser/releases/latest)
[![macOS Intel Downloads](https://camo.githubusercontent.com/d0ea7d7608f978c73fee58b46a3367a8f5e4ac04322605aa7da107ba4147cdd3/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f6c61746573742f4d6f757365722d6d61634f532d696e74656c2e7a69703f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6f676f3d6170706c65266c6162656c3d6d61634f53253230496e74656c26646973706c617941737365744e616d653d66616c7365)](https://github.com/TomBadash/Mouser/releases/latest)
[![Linux Downloads](https://camo.githubusercontent.com/6259f7e590f8f517b60297539f3ee260650c3cb919fb4b73681ca7faa53c494e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f6c61746573742f4d6f757365722d4c696e75782e7a69703f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6f676f3d6c696e7578266c6162656c3d4c696e757826646973706c617941737365744e616d653d66616c7365)](https://github.com/TomBadash/Mouser/releases/latest)
  
[![Downloads](https://camo.githubusercontent.com/a710ab2e62cca6fe365f12e534061080aad8fc5d924e11869d8924383668f430/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f746f74616c3f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6162656c3d546f74616c253230446f776e6c6f61647325323028616c6c25323076657273696f6e7329)](https://camo.githubusercontent.com/a710ab2e62cca6fe365f12e534061080aad8fc5d924e11869d8924383668f430/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f546f6d4261646173682f4d6f757365722f746f74616c3f7374796c653d666f722d7468652d626164676526636f6c6f723d303064346161266c6162656c3d546f74616c253230446f776e6c6f61647325323028616c6c25323076657273696f6e7329)

1. Open the [**latest release page**](https://github.com/TomBadash/Mouser/releases/latest).
2. Download the zip for your platform:
   * **Windows** — `Mouser-Windows.zip`
   * **macOS (Apple Silicon)** — `Mouser-macOS.zip`
   * **macOS (Intel)** — `Mouser-macOS-intel.zip`
   * **Linux** — `Mouser-Linux.zip`
3. Extract it anywhere (Desktop, Documents, `/Applications`, wherever).
4. Run the executable: `Mouser.exe`, `Mouser.app`, or `./Mouser`.

That's it. The app opens, drops a tray / menu-bar icon, and starts remapping immediately.

### What to expect on first launch

* The settings window opens to the device-aware **Mouse & Profiles** page.
* A tray icon appears (next to the clock on Windows / Linux, in the menu bar on macOS).
* Closing the window keeps Mouser running in the tray. Right-click the tray icon → **Quit Mouser** to fully exit.
* Mouser remembers language and startup behavior between runs.

* **Windows SmartScreen** may warn the first time — click **More info** → **Run anyway**.
* **Logitech Options+ must not be running.** Both apps fight over HID++ access; quit Options+ before launching Mouser.
* **macOS** asks for **Accessibility** permission so the event tap can intercept mouse events. See [readme\_mac\_osx.md](https://github.com/TomBadash/Mouser/blob/master/readme_mac_osx.md) for the full setup walkthrough.
* **Linux** needs read access to `/dev/hidraw*`, `/dev/input/event*`, and write access to `/dev/uinput`. Run the bundled helper once after extracting:

  ```
  cd /path/to/extracted/Mouser
  ./install-linux-permissions.sh
  ```

  Reconnect the mouse, then relaunch.
* Config is saved automatically to:
  + `%APPDATA%\Mouser\config.json` (Windows)
  + `~/Library/Application Support/Mouser/config.json` (macOS)
  + `~/.config/Mouser/config.json` (Linux)
* Logs rotate automatically (5 × 5 MB) under `%APPDATA%\Mouser\logs`, `~/Library/Logs/Mouser`, or `$XDG_STATE_HOME/Mouser/logs`.

---



| Mouse & Profiles | Point & Scroll |
| --- | --- |
| [Mouser — Mouse & Profiles page](https://github.com/TomBadash/Mouser/blob/master/images/Screenshot_mouse.png) | [Mouser — Point & Scroll settings](https://github.com/TomBadash/Mouser/blob/master/images/Screenshot_settings.png) |



---

* **Remap any programmable button** — middle click, gesture button, back, forward, mode shift, DPI switch (MX Vertical), and horizontal scroll.
* **Mouse-to-mouse remap** — bind any button to act as left, right, middle, back, or forward click.
* **Per-application profiles** — Mouser auto-switches mappings when the foreground app changes (e.g. Chrome vs. VS Code).
* **Custom keyboard shortcuts** — record any key combination (e.g. `Ctrl+Shift+P`) directly in the UI.
* **40+ built-in actions** — navigation, browser, editing, media, scroll-mode, and DPI shortcuts that adapt per platform.

* **DPI / pointer speed** — slider from 200 to the device max (8000 on MX Master) with quick presets, plus a `Cycle DPI Presets` action you can map to a button.
* **Smart Shift** — toggle Logitech's ratchet ↔ free-spin scroll mode (HID++ `0x2111`), with a sensitivity threshold and a mappable `Toggle SmartShift` action.
* **Switch scroll mode** — bind a button to flip ratchet / free-spin without opening the UI; defaults to mode-shift.
* **Scroll direction inversion** — independent toggles for vertical and horizontal scroll.
* **Gesture button + swipe actions** — tap for one action, swipe up/down/left/right for four others.

* **Windows, macOS, and Linux** — native hooks per platform (`WH_MOUSE_LL`, `CGEventTap`, `evdev` + `uinput`).
* **Native Intel and Apple Silicon macOS builds** — separate `Mouser-macOS-intel.zip` and `Mouser-macOS.zip` artifacts; the menu-bar app runs as `LSUIElement` (no Dock icon).
* **Resizable UI** — main window starts at 1060 × 700 with a 920 × 620 minimum; the mouse diagram and controls reflow as you resize.
* **Start at login** — Windows registry key, macOS LaunchAgent, and Linux XDG autostart, with an independent **Start minimized** option that boots straight into the tray. Linux autostart intentionally waits about 15 seconds after login so Bluetooth / HID devices are usually ready before Mouser restores device settings.
* **Single-instance guard** — launching a second copy brings the existing window to the front instead of starting a duplicate.

* **Bluetooth and Logi Bolt** — both transports are supported on all three platforms; the UI labels the live connection (`Logi Bolt` only when the receiver PID is positively identified).
* **Auto-reconnection** — Mouser watches for power-off / on cycles and rebinds HID++ + the OS mouse hook without a restart; SmartShift settings are replayed on every reconnect (including wake-from-sleep).
* **Live connection status** — real-time Connected / Not Connected badge, model name, and active layout in the UI.
* **Device-aware UI** — interactive MX Master and MX Anywhere diagrams with clickable hotspots; generic fallback card for other models, with an experimental layout-override picker.

* **English / Simplified Chinese / Traditional Chinese** — switch instantly, no restart required.
* Language preference is saved to `config.json` and restored on next launch.
* Covers nav, mouse page, settings page, dialogs, system tray / menu bar, and permission prompts.

* **Fully local** — config is a plain JSON file, all processing happens on your machine.
* **System tray / menu bar** — runs quietly in the background.
* **Zero telemetry, zero cloud, zero account required.**

---



| Family / model | Detection + HID++ probing | UI support |
| --- | --- | --- |
| MX Master 4 / 3S / 3 / 2S / MX Master | Yes | Dedicated interactive per-model layouts |
| MX Anywhere 3S / 3 / 2S | Yes | Dedicated interactive per-model layouts |
| MX Vertical | Yes | Generic fallback card (with DPI switch button support) |
| Unknown Logitech HID++ mice | Best effort by PID/name | Generic fallback card |

> MX Master and MX Anywhere devices have dedicated visual overlays. Other devices are still detected, show their model name, and can opt into an experimental layout override — button positions just may not line up until a real overlay lands. See [CONTRIBUTING\_DEVICES.md](https://github.com/TomBadash/Mouser/blob/master/CONTRIBUTING_DEVICES.md) to add yours.

---



| Button | Default action |
| --- | --- |
| Back button (XButton1) | Alt + Tab (Switch Windows) |
| Forward button (XButton2) | Alt + Tab (Switch Windows) |
| Middle click | Pass-through |
| Gesture button | Pass-through |
| Gesture swipes (up / down / left / right) | Pass-through |
| Mode shift (scroll click) | Switch Scroll Mode (Ratchet / Free Spin) |
| Horizontal scroll left | Browser Back |
| Horizontal scroll right | Browser Forward |
| DPI switch (MX Vertical) | Pass-through |



---

Action labels adapt per platform. Windows exposes `Win+D` and `Task View`; macOS exposes `Mission Control`, `Show Desktop`, `App Exposé`, and `Launchpad`; Linux falls back to compositor-native equivalents.

| Category | Actions |
| --- | --- |
| **Navigation** | Alt+Tab, Alt+Shift+Tab, Show Desktop, Previous Desktop, Next Desktop, Task View (Windows), Mission Control / App Exposé / Launchpad (macOS), Page Up / Page Down / Home / End |
| **Browser** | Back, Forward, Close Tab (Ctrl+W), New Tab (Ctrl+T), Next Tab (Ctrl+Tab), Previous Tab (Ctrl+Shift+Tab) |
| **Editing** | Copy, Paste, Cut, Undo, Select All, Save, Find |
| **Media** | Volume Up, Volume Down, Volume Mute, Play / Pause, Next Track, Previous Track |
| **Scroll** | Switch Scroll Mode (Ratchet / Free Spin), Toggle SmartShift, Cycle DPI Presets |
| **Mouse** | Left Click, Right Click, Middle Click, Back (Mouse Button 4), Forward (Mouse Button 5) |
| **Custom** | User-defined keyboard shortcuts (any key combination, captured in the UI) |
| **Other** | Do Nothing (pass-through) |



---

You only need this if you want to hack on Mouser or run a development build. Most users should grab a release zip — see [Download & Run](https://github.com/TomBadash/MouseControl#download--run).

* **Windows 10/11**, **macOS 12+ (Monterey)**, or **Linux** (X11; KDE Wayland for app detection)
* **Python 3.10+** (tested up to 3.14)
* A supported Logitech HID++ mouse paired via Bluetooth or a USB receiver
* **Logitech Options+ must NOT be running** — it conflicts with HID++ access
* `git` and a working build toolchain

```
git clone https://github.com/TomBadash/Mouser.git
cd Mouser
python -m venv .venv
```

**Windows**

```
.\.venv\Scripts\activate
pip install -r requirements.txt

# Run from source
python main_qml.py

# Or start straight into the tray
python main_qml.py --start-hidden

# Build a portable zip
build.bat                # standard
build.bat --clean        # force clean rebuild
```

`build.bat` installs requirements, verifies that `hidapi` is importable, and packages with PyInstaller. The output lives in `dist\Mouser\` — zip the folder and ship it.

To launch a source checkout without a console window, create a shortcut that uses `pythonw.exe`; see [DEVELOPMENT.md](https://github.com/TomBadash/Mouser/blob/master/DEVELOPMENT.md#desktop-shortcut-windows).


**macOS**

```
source .venv/bin/activate
pip install -r requirements.txt

# Run from source
python main_qml.py
python main_qml.py --start-hidden     # launch directly to menu bar

# Build the native menu-bar bundle
pip install pyinstaller
./build_macos_app.sh
```

The output is `dist/Mouser.app`. The script reuses `images/AppIcon.icns` when present, otherwise generates one from `images/logo_icon.png`. Signing depends on whether `MOUSER_SIGN_IDENTITY` is set in the environment:

* **Unset (default)**: ad-hoc signs with `codesign --sign -`. Convenient for one-off builds, but the bundle's code identity can change on rebuild, so macOS may ask for Accessibility permission again.
* **Set to a codesigning identity** (`security find-identity -v -p codesigning` to list them — SHA-1 form preferred): signs every nested `.dylib` / `.so` / `.framework` with hardened runtime options, then signs the outer app with the hardened-runtime exceptions at `build_resources/Mouser.entitlements`. This is a local developer signing path for repeated builds; stable macOS permission behavior depends on keeping the same source, resolved Python interpreter, dependency versions, architecture, signing identity, entitlements, and timestamp policy. A failing `codesign --verify --deep --strict` check aborts the build.

```
MOUSER_SIGN_IDENTITY="ABCD1234..." ./build_macos_app.sh   # local signed build
```

* This is **not** a notarized release-signing flow. Public macOS release zips remain ad-hoc signed until a separate Developer ID signing, secure timestamp, notarization, stapling, and Gatekeeper validation workflow exists.
* Build on the architecture you want to ship: an `arm64` Python produces an Apple Silicon bundle, an `x86_64` Python produces an Intel bundle. Set `PYINSTALLER_TARGET_ARCH=arm64|x86_64|universal2` to override.
* Release CI publishes both `Mouser-macOS.zip` (Apple Silicon) and `Mouser-macOS-intel.zip` (Intel) automatically on tag pushes.
* Accessibility permission is required. See [readme\_mac\_osx.md](https://github.com/TomBadash/Mouser/blob/master/readme_mac_osx.md) for the full grant flow and platform-specific notes.

**Linux**

```
source .venv/bin/activate
pip install -r requirements.txt

# Run from source
python main_qml.py

# Install device permissions (only needed once, then reconnect the mouse)
./packaging/linux/install-linux-permissions.sh

# Build a portable bundle
sudo apt-get install libhidapi-dev
pip install pyinstaller
pyinstaller Mouser-linux.spec --noconfirm
```

The helper installs `69-mouser-logitech.rules`, reloads `udev`, and tries to `modprobe uinput`. After a successful run, reconnect the mouse, fully quit Mouser, and launch normally — no `sudo`. On systems without logind / `uaccess`, adding the user to the `input` group is the distro-specific fallback.

The first normal Linux launch creates or refreshes:

```
~/.local/share/applications/io.github.tombadash.mouser.desktop
```

The generated launcher uses absolute paths for the current portable app or source checkout. If you move the checkout, launch Mouser once from the new path to refresh the app-menu entry. Enabling **Start at login** also manages:

```
~/.config/autostart/io.github.tombadash.mouser.desktop
```

That Linux autostart entry includes a short GNOME startup delay so Mouser does not race Bluetooth / HID initialization immediately after login.

`xdotool` enables per-app profile switching on X11; `kdotool` adds KDE Wayland support. Other Wayland compositors fall back to the default profile.

> **Automated releases:** pushing a `v*` tag triggers [`.github/workflows/release.yml`](https://github.com/TomBadash/Mouser/blob/master/.github/workflows/release.yml), which builds Windows, macOS (Apple Silicon + Intel), and Linux artifacts in CI and uploads them to the GitHub Release.

For project layout, the architecture diagram, the HID++ gesture detector, the Engine + reconnection flow, debug CLI flags (`--hid-backend=iokit|hidapi|auto`), and how to run the test suite, see [DEVELOPMENT.md](https://github.com/TomBadash/Mouser/blob/master/DEVELOPMENT.md). To add a new device, see [CONTRIBUTING\_DEVICES.md](https://github.com/TomBadash/Mouser/blob/master/CONTRIBUTING_DEVICES.md).

---

* **Per-device mappings aren't fully separated yet** — layout overrides are stored per detected device, but profile mappings are still global.
* **Conflicts with Logitech Options+** — both apps fight over HID++ access. Quit Options+ before running Mouser.
* **Scroll inversion** uses coalesced post-injection on Windows to avoid LL-hook deadlocks; it's stable in mainstream apps but may misbehave in some games or low-level drivers.
* **Admin not required** — but injected keystrokes may not reach elevated windows or some games. Run Mouser elevated if you need that path.
* **Linux app detection is partial** — X11 works via `xdotool`, KDE Wayland works via `kdotool`, GNOME / other Wayland compositors still fall back to the default profile.
* **Linux device permissions** — Mouser needs access to `/dev/hidraw*`, `/dev/input/event*`, and `/dev/uinput`. Use [`install-linux-permissions.sh`](https://github.com/TomBadash/Mouser/blob/master/packaging/linux/install-linux-permissions.sh) once instead of running as root.

---



---

Contributions are welcome.

* **Code, fixes, and features:** fork → branch → PR. The dev setup, architecture overview, debug flags, and test instructions live in [DEVELOPMENT.md](https://github.com/TomBadash/Mouser/blob/master/DEVELOPMENT.md).
* **Adding a new Logitech mouse:** follow the discovery-dump walkthrough in [CONTRIBUTING\_DEVICES.md](https://github.com/TomBadash/Mouser/blob/master/CONTRIBUTING_DEVICES.md). Even a partial dump helps.
* **Help wanted:**
  + Testing with other Logitech HID++ devices
  + Scroll inversion improvements
  + Broader Linux / Wayland validation
  + UI/UX polish, accessibility, and translations

If Mouser saves you from installing Logitech Options+, consider supporting development:

[![Sponsor](https://camo.githubusercontent.com/c753ffb06d388f9c73284c020e1769a1e347513ddef38ea3e3791bd6a4f819d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706f6e736f722de29da4efb88f2d6561346161613f7374796c653d666f722d7468652d6261646765266c6f676f3d67697468756273706f6e736f7273)](https://github.com/sponsors/TomBadash)

Every bit helps keep the project going — thank you.

---

* **[@andrew-sz](https://github.com/andrew-sz)** — macOS port: CGEventTap mouse hooking, Quartz key simulation, NSWorkspace app detection, and NSEvent media key support.
* **[@thisislvca](https://github.com/thisislvca)** — significant expansion of the project including macOS compatibility improvements, multi-device support, new UI features, and active triage of open issues.
* **[@awkure](https://github.com/awkure)** — cross-platform login startup (Windows registry + macOS LaunchAgent), single-instance guard, start-minimized option, and MX Master 4 detection.
* **[@hieshima](https://github.com/hieshima)** — Linux support (evdev + HID++ + uinput), mode-shift mapping, Smart Shift toggle, custom keyboard shortcut support, Linux connection-state stabilization, and macOS CGEventTap reliability fixes (auto re-enable on timeout, trackpad scroll filtering).
* **[@pavelzaichyk](https://github.com/pavelzaichyk)** — Next Tab / Previous Tab browser actions, persistent rotating log file storage, Smart Shift enhanced support (HID++ `0x2111`) with sensitivity control and scroll-mode sync.
* **[@nellwhoami](https://github.com/nellwhoami)** — Multi-language UI system (English, Simplified Chinese, Traditional Chinese) and Page Up / Page Down / Home / End navigation actions.
* **[@guilamu](https://github.com/guilamu)** — Mouse-to-mouse button remapping (left, right, middle, back, forward click) and HID++ stability fixes (stuck-button auto-release, auto-reconnect after consecutive timeouts, async dispatch queue for the Windows hook).
* **[@vcanuel](https://github.com/vcanuel)** — Logi Bolt receiver support on macOS via the `hidapi` fallback path.
* **[@farfromrefug](https://github.com/farfromrefug)** — smaller macOS bundle (Qt Quick Controls trim, QtDBus, Qt asset filtering).
* **[@MysticalMike60t](https://github.com/MysticalMike60t)** — README structure ideas (collapsible per-OS build sections).

---

This project is licensed under the [MIT License](https://github.com/TomBadash/Mouser/blob/master/LICENSE).

**Mouser** is not affiliated with or endorsed by Logitech. "Logitech", "MX Master", and "Options+" are trademarks of Logitech International S.A.