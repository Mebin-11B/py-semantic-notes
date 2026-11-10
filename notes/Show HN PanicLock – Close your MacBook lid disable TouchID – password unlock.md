---
title: "Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock"
url: https://github.com/paniclock/paniclock/
clipped: 2026-06-17 01:16:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock](https://github.com/paniclock/paniclock/)

## Digest Summary
PanicLock is a macOS menu‑bar utility for Macs with Touch ID (macOS 14.0 Sonoma or later) that instantly disables biometric authentication and locks the screen via a single click, customizable hotkey, or automatic lid‑close trigger. It temporarily sets the Touch ID timeout to one second using the privileged helper tool (installed via SMJobBless), then locks the display with `pmset displaysleepnow`; after unlocking with a password, the original timeout is restored. The helper runs only three hard‑coded commands (`bioutil` read/write, `pmset`) with minimal privileges, employs code‑signed XPC verification, and performs no network activity or data collection. Installation can be done via Homebrew (`brew install paniclock/tap/paniclock`) or by building from source (Xcode project requires setting a development team and updating plist entries). Uninstallation removes the helper and app files via launchctl and file deletion commands. The project includes a release script that automates building, signing with a Developer ID, notarization, and DMG packaging. It is released under the MIT License and hosted on GitHub.

## Discussion Summary
The comments express strong approval for the tool, highlighting its usefulness for quickly disabling biometric authentication in sensitive situations. Users note its value as a privacy measure against casual snooping and praise its simplicity, while also pointing out limitations against determined adversaries and emphasizing the importance of full‑disk encryption and panic‑shutdown options. Legal considerations about compelled biometric unlocking are mentioned, and several suggestions appear for additional features such as accelerometer‑based triggers, dummy accounts, and native OS integration.

---

## Full Article

[![PanicLock](https://github.com/paniclock/paniclock/raw/main/assets/paniclock-logo-and-name-v1.png)](https://github.com/paniclock/paniclock/blob/main/assets/paniclock-logo-and-name-v1.png)

PanicLock is a macOS menu bar utility that instantly disables Touch ID and locks the screen with a single click or closing your laptop lid.

PanicLock fills a gap macOS leaves open: there is no built-in way to instantly disable Touch ID when it matters. Biometrics are convenient day-to-day, and sometimes preferable when you need speed or want to avoid your password being observed. But in sensitive situations, law enforcement and border agents in many countries can compel a biometric unlock in ways they cannot with a password. PanicLock gives you a one-click menu bar button, a customizable hotkey, or an automatic lock-on-lid-close option that immediately disables Touch ID and locks your screen, restoring password-only protection without killing your session or shutting down.

[![Download PanicLock](https://camo.githubusercontent.com/fd6a551de086a52ecb9c8a2e8012d74597ec6ede194cd2048f0a21b837abeb8c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f776e6c6f61642d50616e69634c6f636b2d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d6170706c65)](https://github.com/paniclock/paniclock/releases/latest/download/PanicLock.dmg)

* **One-click panic lock** — Click the menu bar icon or press a hotkey to instantly lock
* **Lock on Close** — Optionally lock and disable Touch ID when you close the lid
* **Temporarily disables Touch ID** — Forces password-only unlock
* **Auto-restore** — Original Touch ID settings restored after unlock
* **Keyboard shortcut** — Configure a global hotkey (e.g., ⌃⌥⌘L)
* **Launch at login** — Start automatically when you log in

```
brew install paniclock/tap/paniclock
```

Download the latest DMG from the [releases page](https://github.com/paniclock/paniclock/releases/latest).

* macOS 14.0 (Sonoma) or later
* Mac with Touch ID

| Action | Result |
| --- | --- |
| **Left-click** icon | Trigger panic lock immediately |
| **Right-click** icon | Open menu (Preferences, Uninstall, Quit) |

When enabled in Preferences, closing your Mac's lid will automatically disable Touch ID and lock your screen. Touch ID stays disabled until you re-login with your password. If your screen locks for other reasons (screensaver, display sleep, etc.), Touch ID will still work as normal.

On first use, you'll be prompted for your admin password to install the privileged helper. This is a one-time setup.

1. Clone this repository
2. Open `PanicLock.xcodeproj` in Xcode
3. Set your Development Team in both targets (PanicLock and PanicLockHelper)
4. Update Team ID in `Info.plist` (`SMPrivilegedExecutables`) and `Info-Helper.plist` (`SMAuthorizedClients`)
5. Build and run

**Homebrew:**

**From the app:** Right-click → "Uninstall PanicLock..." → Enter admin password

**Manual:**

```
sudo launchctl bootout system/com.paniclock.helper
sudo rm -f /Library/PrivilegedHelperTools/com.paniclock.helper
sudo rm -f /Library/LaunchDaemons/com.paniclock.helper.plist
rm -rf /Applications/PanicLock.app
```

PanicLock uses a privileged helper (installed via SMJobBless) to modify Touch ID timeout settings:

1. Reads current timeout via `bioutil -r -s`
2. Sets timeout to 1 second via `bioutil -w -s -o 1`
3. Locks screen via `pmset displaysleepnow`
4. Restores original timeout after ~2 seconds

PanicLock only disables Touch ID. If you have other unlock methods enabled — Apple Watch unlock, security keys, etc. — your Mac can still be unlocked using those.

* **Minimal privileges** — Helper only runs 3 hardcoded commands (`bioutil`, `pmset`)
* **Code-signed XPC** — Helper verifies connecting app's bundle ID + team ID + certificate
* **No network activity** — App is 100% offline, no telemetry or analytics
* **No data collection** — Only stores preferences (icon style, keyboard shortcut)
* **Open source** — Full code available for audit

Note: PanicLock only disables Touch ID. If you have other unlock methods enabled, Apple Watch unlock, security keys, etc., your Mac can still be unlocked using those.

The release script handles building, signing, notarizing, and packaging:

**Features:**

* Extracts version from Xcode project automatically
* Signs with Developer ID for distribution outside the App Store
* Submits to Apple for notarization (can take minutes to hours)
* Creates a notarized DMG for distribution
* Supports parallel notarizations — each version gets its own `build/release/<version>/` directory

**Workflow:**

1. Bump `MARKETING_VERSION` in Xcode
2. Run `./scripts/release.sh` — builds and submits for notarization
3. Run again later to check status and continue when approved
4. Final output: `build/release/<version>/PanicLock-<version>.dmg`

MIT License — See [LICENSE](https://github.com/paniclock/paniclock/blob/main/LICENSE) for details.

Contributions welcome! Please open an issue or pull request.