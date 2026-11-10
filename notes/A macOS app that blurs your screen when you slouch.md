---
title: "A macOS app that blurs your screen when you slouch"
url: https://github.com/tldev/posturr
clipped: 2026-06-17 01:53:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A macOS app that blurs your screen when you slouch](https://github.com/tldev/posturr)

## Digest Summary
GitHub repository “tldev/posturr” hosts a macOS application designed to improve user posture by automatically blurring the screen when the user slouches. The app leverages Apple’s Vision framework to perform real‑time posture detection using the device’s camera, analyzing body position to determine slouching events. Upon detecting a slouch, the software triggers a visual blur overlay, prompting the user to correct their posture. The repository presumably includes source code, build instructions, and dependencies required for integrating Vision‑based pose estimation into a macOS environment. Access to the full repository content was blocked, displaying a “You can’t perform that action at this time” message, so detailed implementation specifics, licensing, and contribution guidelines are not available in the scraped excerpt.

## Discussion Summary
The comments show overall enthusiasm for the posture‑monitoring concept and for AI‑driven development that made the app feasible, with many expressing interest in using it, paying for it, or extending it to other platforms and sensors. At the same time, users raise practical concerns about camera privacy, security warnings, high CPU usage, and lack of a Windows version, and note that “good posture” is debated and that comfort or breaks may be more important than strict uprightness. The consensus balances optimism for the tool with caution over privacy, performance, and ergonomic assumptions.

---

## Full Article

**A macOS app that blurs your screen when you slouch.**

Dorso monitors your posture in real-time using either your Mac's camera or AirPods motion sensors. When it detects that you're slouching, it progressively blurs your screen to remind you to sit up straight. Maintain good posture, and the blur clears instantly.

[![Download on the App Store](https://camo.githubusercontent.com/1e090632c1f3784e23e0489a1588058ed948f94afcd9be428ddb4bb184101c21/68747470733a2f2f746f6f6c626f782e6d61726b6574696e67746f6f6c732e6170706c652e636f6d2f6170692f76322f6261646765732f646f776e6c6f61642d6f6e2d7468652d6170702d73746f72652f626c61636b2f656e2d75733f72656c65617365446174653d31373639393930343030)](https://apps.apple.com/us/app/posturr-posture-monitor/id6758276540?mt=12)

[![Download Latest Release](https://camo.githubusercontent.com/3be0a39f46e0c00a432bc9ad2490229951ab4408973766860a0d7d8571d3d87e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f746c6465762f646f72736f3f7374796c653d666f722d7468652d6261646765266c6f676f3d6170706c65266c6162656c3d446f776e6c6f616426636f6c6f723d303037414646)](https://github.com/tldev/dorso/releases/latest)
[![Discord](https://camo.githubusercontent.com/dd8e6f852c996ee0b4d52a9f2a0117c58ac9f78fb60942bdf33939e3fbd05800/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d4a6f696e253230436f6d6d756e6974792d3538363546323f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/6Ufy2SnXDW)

**Join our Discord** to share feedback, get help, suggest features, and connect with other Dorso users!

dorso-preview.mp4

[
](https://github.com/user-attachments/assets/de02c78b-c6c4-4ddc-9650-320e7267921a)

[![Onboarding - Choose Tracking Method](https://github.com/tldev/dorso/raw/main/assets/dorso_onboarding.png)](https://github.com/tldev/dorso/blob/main/assets/dorso_onboarding.png)
[![Settings](https://github.com/tldev/dorso/raw/main/assets/dorso_settings.png)](https://github.com/tldev/dorso/blob/main/assets/dorso_settings.png)

[![Menu Bar](https://github.com/tldev/dorso/raw/main/assets/dorso_menubar.png)](https://github.com/tldev/dorso/blob/main/assets/dorso_menubar.png)
[![Analytics Dashboard](https://github.com/tldev/dorso/raw/main/assets/dorso_analytics.png)](https://github.com/tldev/dorso/blob/main/assets/dorso_analytics.png)

* **Two tracking methods** - Use your camera (Vision framework) or AirPods motion sensors
* **AirPods motion tracking** - Track posture without camera using AirPods Pro, Max, or 3rd gen+ (macOS 14+)
* **Progressive screen blur** - Gentle visual reminder that intensifies with worse posture
* **Menu bar controls** - Easy access to settings, calibration, and status from the menu bar
* **Multi-display support** - Works across all connected monitors
* **Privacy-focused** - All processing happens locally on your Mac
* **Lightweight** - Runs as a background app with minimal resource usage
* **Optional Dock visibility** - Show in Dock and Cmd+Tab app switcher when preferred
* **No account required** - No signup, no cloud, no tracking

1. Download the latest `Dorso-vX.X.X.dmg` or `.zip` from the [Releases](https://github.com/tldev/dorso/releases) page
2. Open the DMG and drag `Dorso.app` to your Applications folder
3. Launch normally - no Gatekeeper warnings (app is signed and notarized)

**Camera Mode:** Requires camera access. When you first launch the app, macOS will ask for permission.

**AirPods Mode:** Requires Motion & Fitness Activity permission (macOS 14+). This allows the app to read head motion data from your AirPods.

If you accidentally denied permission, you can grant it later in **System Settings** > **Privacy & Security** > **Camera** or **Motion & Fitness Activity**.

Once launched, Dorso appears in your menu bar with a person icon. The app continuously monitors your posture and applies screen blur when slouching is detected.

### Menu Bar Controls

Click the menu bar icon to access:

* **Status** - Shows current state (Monitoring, Slouching, Good Posture, etc.)
* **Enabled** - Toggle posture monitoring on/off
* **Recalibrate** - Reset your baseline posture (sit up straight, then click)
* **Settings** - Open the settings window to configure all options
* **Quit** - Exit the application

The Settings window (accessible from the menu bar) provides:

* **Sensitivity** - Adjust how sensitive the slouch detection is (5 levels from Low to Very High)
* **Dead Zone** - Set the tolerance before blur kicks in (5 levels from None to Very Large)
* **Blur when away** - Blur screen when you step away from camera
* **Show in dock** - Show app in Dock and Cmd+Tab app switcher
* **Pause on the go** - Auto-pause when laptop display becomes the only screen
* **Compatibility mode** - Use public macOS APIs for blur (try this if blur doesn't appear)

* Position your camera at eye level when possible
* Ensure adequate lighting on your face
* Sit at a consistent distance from your screen
* The app works best when your shoulders are visible

Dorso offers two tracking methods:

Uses Apple's Vision framework to detect body pose landmarks:

* **Body Pose Detection**: Tracks nose and head position
* **Face Detection Fallback**: When full body isn't visible, tracks face position
* **Posture Analysis**: Measures vertical head position against your calibrated baseline

Uses motion sensors in compatible AirPods (Pro, Max, 3rd gen+):

* **Head Tilt Detection**: Tracks pitch angle of your head
* **No Camera Required**: Works without any camera access
* **Automatic Pause**: Pauses when AirPods are removed from ears

The screen blur uses macOS's private CoreGraphics API by default for efficient, system-level blur. If the blur doesn't appear on your system, enable **Compatibility Mode** from settings to use `NSVisualEffectView` instead.

* macOS 13.0 (Ventura) or later
* Xcode Command Line Tools (`xcode-select --install`)

```
git clone https://github.com/tldev/dorso.git
cd dorso
./build.sh
```

The built app will be in `build/Dorso.app`.

```
# Standard build
./build.sh

# Build with release archive (.zip)
./build.sh --release
```

```
swiftc -O \
    -framework AppKit \
    -framework AVFoundation \
    -framework Vision \
    -framework CoreImage \
    -o Dorso \
    Sources/*.swift
```

* **Camera mode**: Requires a working camera with adequate lighting and clear view of upper body/face
* **AirPods mode**: Requires macOS 14.0+ and compatible AirPods (Pro, Max, or 3rd generation+)

Dorso exposes a file-based command interface for external control:

| Command | Description |
| --- | --- |
| `capture` | Take a photo and analyze pose |
| `blur <0-64>` | Set blur level manually |
| `quit` | Exit the application |

Write commands to `/tmp/dorso-command`. Responses appear in `/tmp/dorso-response`.

* macOS 13.0 (Ventura) or later
* Camera (built-in or external)
* Approximately 10MB disk space

Dorso processes all video data locally on your Mac. No images or data are ever sent to external servers. The camera feed is used solely for posture detection and is never stored or transmitted.

MIT License - see [LICENSE](https://github.com/tldev/dorso/blob/main/LICENSE) for details.

```
dorso/
├── Sources/
│   ├── main.swift                  # App entry point
│   ├── AppDelegate.swift           # Main app coordinator and state machine
│   ├── PostureDetector.swift       # Protocol for posture detection methods
│   ├── CameraPostureDetector.swift # Camera-based detection (Vision framework)
│   ├── AirPodsPostureDetector.swift # AirPods motion-based detection
│   ├── Models.swift                # Shared types (settings keys, profile data, app state)
│   ├── Persistence.swift           # Settings and profile storage
│   ├── DisplayManager.swift        # Display detection and configuration
│   ├── MenuBar.swift               # Menu bar setup and management
│   ├── SettingsWindow.swift        # SwiftUI settings window
│   ├── OnboardingWindow.swift      # Tracking method selection UI
│   ├── CalibrationWindow.swift     # Calibration UI
│   └── BlurOverlay.swift           # Screen blur overlay management
├── build.sh                        # Build script
├── release.sh                      # Release automation
└── AppIcon.icns                    # App icon
```

Contributions are welcome! Please feel free to submit issues and pull requests.

* Built with Apple's Vision framework for body pose detection
* Uses private CoreGraphics API for blur, with NSVisualEffectView fallback
* Inspired by the need for better posture during long coding sessions

Want this on Linux? See [postured](https://github.com/vadi2/postured) or [dorso-linux](https://github.com/Gheop/dorso-linux).