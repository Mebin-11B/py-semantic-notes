---
title: "Gyroflow: Video stabilization using gyroscope data"
url: https://github.com/gyroflow/gyroflow
clipped: 2026-06-17 01:02:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Gyroflow: Video stabilization using gyroscope data](https://github.com/gyroflow/gyroflow)

## Digest Summary
Gyroflow is an open‑source application for video stabilization using gyroscope (and optionally accelerometer) data recorded by modern cameras (GoPro, Sony, Insta360, DJI, etc.) or external sources (Betaflight blackbox, smartphones). It processes footage with real‑time preview, GPU‑accelerated multi‑threaded algorithms, rolling‑shutter correction, adaptive zoom, lens‑distortion correction, and supports 10‑bit to 32‑bit color depths. Output formats include H.264/H.265, ProRes, DNxHD, CineForm, PNG, OpenEXR, and RAW (Blackmagic, RED, Canon). Plugins are available for Adobe Premiere/After Effects, DaVinci Resolve (OpenFX), and Final Cut Pro (Toolbox). The core engine is a pure‑Rust library without external dependencies; the UI uses QML/Qt, with optional OpenCV for calibration and optical flow. GPU back‑ends use DirectX, OpenGL, Metal, Vulkan via Qt RHI and wgpu. Supported platforms: Windows 10 64‑bit, macOS 10.15+, Linux (Debian 10+, Ubuntu 18.10+), Android 6+, iOS 14+. Minimum drivers and libraries are listed per GPU vendor. Licensed under GPL‑v3 with an additional permission to link the closed‑source mdk‑sdk. The project accepts contributions, offers translations, and provides detailed build instructions for desktop, Android, and iOS.

## Discussion Summary
The comments express strong approval of the software, highlighting its quality and the impressive benefits it provides, such as effective rolling‑shutter correction. Users also note a limitation: certain camera models, specifically the A7 iii, do not capture the required gyro data, which prevents full utilization of those features. Overall, the feedback is positive, emphasizing the software’s capabilities while acknowledging hardware compatibility constraints.

---

## Full Article

Video stabilization using gyroscope data
  
  
[Homepage](https://gyroflow.xyz) •
[Download](https://github.com/gyroflow/gyroflow/releases) •
[Documentation](https://docs.gyroflow.xyz) •
[Discord](https://discord.gg/YaUtNpWTUh) •
[Report bug](https://github.com/gyroflow/gyroflow/issues) •
[Request feature](https://github.com/gyroflow/gyroflow/issues)

[![Downloads](https://camo.githubusercontent.com/d55f41a3dc8439a05f1728445be8c8b799b00f0ae77eaa09d4dbebcc463e7fa2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6779726f666c6f772f6779726f666c6f772f746f74616c)](https://github.com/gyroflow/gyroflow/releases)
[![Contributors](https://camo.githubusercontent.com/3d4323e60644bc5a6536cb8aa10d638cd3c34ca39b6ce5a14ed6bf7a5c10a1df/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6779726f666c6f772f6779726f666c6f773f636f6c6f723d6461726b2d677265656e)](https://github.com/gyroflow/gyroflow/graphs/contributors)
[![](https://camo.githubusercontent.com/d699578d901aaba5587096a1c6e1db9639b9c9ef818ceee394dd3aef5c13cee6/68747470733a2f2f6261646765732e63726f7764696e2e6e65742f6779726f666c6f772f6c6f63616c697a65642e737667)](https://crowdin.com/project/gyroflow "Crowdin")
[![Issues](https://camo.githubusercontent.com/5ba44efa6cb4d00408da52d4b523396a87d26dd9c73df1d4d48d7042938311ac/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6779726f666c6f772f6779726f666c6f77)](https://github.com/gyroflow/gyroflow/issues/)
[![License](https://camo.githubusercontent.com/13e860cd97d6c8604ee2fa6a8f118e65888840aa7d04f7b783887462aebb894d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6779726f666c6f772f6779726f666c6f77)](https://github.com/gyroflow/gyroflow/blob/master/LICENSE)

Gyroflow is an application that can stabilize your video by using motion data from a gyroscope and optionally an accelerometer. Modern cameras record that data internally (GoPro, Sony, Insta360 etc), and this application stabilizes the captured footage precisely by using them. It can also use gyro data from an external source (eg. from Betaflight blackbox).

[Trailer / results video](https://www.youtube.com/watch?v=QR-SINyvNyI)

[![Screenshot](https://github.com/gyroflow/gyroflow/raw/master/resources/screenshot.jpg)](https://github.com/gyroflow/gyroflow/blob/master/resources/screenshot.jpg)

[![](https://github.com/gyroflow/gyroflow/raw/master/resources/comparison1.gif)](https://github.com/gyroflow/gyroflow/blob/master/resources/comparison1.mp4)
[![](https://github.com/gyroflow/gyroflow/raw/master/resources/comparison2.gif)](https://github.com/gyroflow/gyroflow/blob/master/resources/comparison2.mp4)

* Real-time preview, parameter adjustments and all calculations
* GPU processing and rendering, all algorithms fully multi-threaded
* Rolling shutter correction
* [Video editor plugins](https://github.com/gyroflow/gyroflow-plugins) (Adobe Premiere/Ae, DaVinci Resolve, Final Cut Pro and more), allowing you to apply stabilization directly in a video editor without transcoding
* Supports full Sony metadata (recording params, automatic lens, support for IBIS, OIS, EIS - you can have IBIS enabled in camera and still apply Gyroflow on top)
* Supports already stabilized GoPro videos (captured with Hypersmooth enabled) (Hero 8 and up)
* Supports and renders 10-bit videos (up to 16-bit 4:4:4:4 for regular codecs and 32-bit float for OpenEXR - working directly on YUV data to maintain maximum quality)
* Customizable lens correction strength
* Render queue
* Keyframes
* Ability to create custom settings presets
* Visual chart with gyro data (displays gyro, accelerometer, magnetometer, and quaternions, including smoothed quaternions)
* Supports underwater footage (corrects underwater distortions)
* Modern responsive user interface with Dark and Light theme
* Adaptive zoom (dynamic cropping)
* Zoom limit
* Supports image sequences (PNG, OpenEXR, CinemaDNG)
* Based on [telemetry-parser](https://github.com/AdrianEddy/telemetry-parser) - supports all gyro sources out of the box
* Gyro low pass filter, arbitrary rotation (pitch, roll, yaw angles) and orientation
* Multiple gyro integration methods for orientation determination
* Multiple video orientation smoothing algorithms, including horizon levelling and per-axis smoothness adjustment.
* Cross-platform - works on Windows/Linux/Mac/Android/iOS
* Multiple UI languages
* Supports variable and high frame rate videos - all calculations are done on timestamps
* H.264/AVC, H.265/HEVC, ProRes, DNxHD, CineForm, PNG and OpenEXR outputs, with H.264 and H.265 fully GPU accelerated (ProRes also accelerated on Apple Silicon)
* Easy lens calibration process
* Fully zero-copy GPU preview rendering
* Core engine is a separate library without external dependencies (no Qt, no ffmpeg, no OpenCV), and can be used to create OpenFX and Adobe plugins (on the TODO list)
* Automatic updates of lens profile database
* Built-in official lens profiles for GoPro HERO 6-13; Sony; DJI; Insta360 action cameras; RunCam: Thumb series, 5 Orange
* Easy management of the video editor plugins from within the app
* Ability to add an additional 3D rotation (useful for framing vertical videos)

* GoPro (HERO 5 and later)
* Sony (a1, a7c, a7r V, a7 IV, a7s III, a9 II, a9 III, FX3, FX6, FX9, RX0 II, RX100 VII, ZV1, ZV-E10, ZV-E10 II, ZV-E1, a6700)
* Insta360 (OneR, OneRS, SMO 4k, Go, GO2, GO3, GO3S, GOUltra, Caddx Peanut, Ace, Ace Pro)
* DJI (Avata, Avata 2, O3/O4 Air Unit, Action 2/4/5/6/Nano, Neo, Neo2)
* XTRA (Edge, Edge Pro)
* Blackmagic RAW (\*.braw)
* RED RAW (V-Raptor, KOMODO) (\*.r3d)
* Canon (C50, C80, C400, R6 Mk3, R5 Mk2) (\*.mp4, \*.mov, \*.mxf)
* Freefly (Ember)
* Betaflight blackbox (\*.bfl, \*.bbl, \*.csv)
* ArduPilot logs (\*.bin, \*.log)
* Gyroflow [.gcsv log](https://docs.gyroflow.xyz/app/technical-details/gcsv-format)
* iOS apps: [`Sensor Logger`](https://apps.apple.com/us/app/sensor-logger/id1531582925), [`G-Field Recorder`](https://apps.apple.com/at/app/g-field-recorder/id1154585693), [`Gyro`](https://apps.apple.com/us/app/gyro-record-device-motion-data/id1161532981)
* Android apps: [`Sensor Logger`](https://play.google.com/store/apps/details?id=com.kelvin.sensorapp&hl=de_AT&gl=US), [`Sensor Record`](https://play.google.com/store/apps/details?id=de.martingolpashin.sensor_record), [`OpenCamera Sensors`](https://github.com/MobileRoboticsSkoltech/OpenCamera-Sensors), [`MotionCam Pro`](https://play.google.com/store/apps/details?id=com.motioncam.pro)
* Runcam CSV (Runcam 5 Orange, iFlight GOCam GR, Runcam Thumb, Mobius Maxi 4K)
* Hawkeye Firefly X Lite CSV
* XTU (S2Pro, S3Pro)
* WitMotion (WT901SDCL binary and \*.txt)
* Vuze (VuzeXR)
* KanDao (Obisidian Pro, Qoocam EGO)
* [CAMM format](https://developers.google.com/streetview/publish/camm-spec)

### Info for cameras not on the list

* For cameras which do have built-in gyro, please contact us and we will implement support for that camera. Refer to the [documentation](https://docs.gyroflow.xyz) for information about the gyro logging process.
* For cameras which don't have built-in gyro, you can use any other device which records gyro data. It may be a phone, an action camera, or an external device like a Betaflight FC, [flowshutter](https://github.com/gyroflow/flowshutter), [esp-gyrologger](https://github.com/VladimirP1/esp-gyrologger) (eg. on an [AtomS3](https://shop.m5stack.com/products/atoms3-dev-kit-w-0-85-inch-screen)). You just have to mount it on your main camera.

* Download `Gyroflow-windows64.zip` from the [Releases](https://github.com/gyroflow/gyroflow/releases) page, extract the files somewhere and run `Gyroflow.exe`
* If it shows an error about `VCRUNTIME140.dll` or `0xc0000142`, [install VC redist](https://aka.ms/vs/17/release/vc_redist.x64.exe)

* Download `Gyroflow-mac-universal.dmg` from the [Releases](https://github.com/gyroflow/gyroflow/releases) page, run the downloaded file, and drag & drop `Gyroflow` app to the Applications folder (or anywhere you want, like on Desktop)
* You can also install using brew: `brew install gyroflow`. To upgrade Gyroflow, run `brew update` then `brew upgrade gyroflow`

* Download `Gyroflow-linux64.tar.gz` from the [Releases](https://github.com/gyroflow/gyroflow/releases) page, extract the files somewhere and run `./Gyroflow` in the terminal.
* If that doesn't work, you can try the `Gyroflow-linux64.AppImage`, but the .tar.gz one is preferred.
* Make sure you have latest graphics drivers installed
* Possibly needed packages: `sudo apt install libva2 libvdpau1 libasound2 libxkbcommon0 libpulse0 libc++-dev libvulkan1`
* GPU specific packages:
  + NVIDIA: `nvidia-opencl-icd nvidia-vaapi-driver nvidia-vdpau-driver nvidia-egl-icd nvidia-vulkan-icd libnvcuvid1 libnvidia-encode1`
  + Intel: `intel-media-va-driver i965-va-driver beignet-opencl-icd intel-opencl-icd`
  + AMD: `mesa-vdpau-drivers mesa-va-drivers mesa-opencl-icd libegl-mesa0 mesa-vulkan-drivers`

Latest development version is always available here: <https://gyroflow.xyz/devbuild/>.

Minimum system requirements:
----------------------------

* Windows 10 64-bit (1809 or later)
  + If you have Windows "N" install, go to `Settings` -> `Apps` -> `Optional features` -> `Add a feature` -> enable `Media Feature Pack`
* macOS 10.15 or later (both Intel and Apple Silicon are supported natively)
* Linux:
  + `.tar.gz` package (recommended): Debian 10+, Ubuntu 18.10+, CentOS 8.2+, openSUSE 15.3+. Other distros require glibc 2.28+ (`ldd --version` to check)
  + `.AppImage` should work everywhere
* Android 6+
* iOS 14+

For general support and discussion, you can find the developers and other users on the [Gyroflow Discord server](https://discord.gg/YaUtNpWTUh).

For companies or people wishing to get in touch with the team privately for collaborative purposes: [devteam@gyroflow.xyz](mailto:devteam@gyroflow.xyz).

You can download some clips with gyro data from here: <https://drive.google.com/drive/folders/1sbZiLN5-sv_sGul1E_DUOluB5OMHfySh?usp=sharing>

See the [open issues](https://github.com/gyroflow/gyroflow/issues) for a list of proposed features and known issues.
There's also a ton of TODO comments throughout the code.

Gyroflow OpenFX plugin is available [here](https://github.com/gyroflow/gyroflow-plugins). OpenFX plugin was tested in DaVinci Resolve

Adobe Premiere and After Effects plugin is available [here](https://github.com/gyroflow/gyroflow-plugins)

Final Cut Pro plugin is available as [Gyroflow Toolbox](https://gyroflowtoolbox.io).

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributors are **greatly appreciated**.

* If you have suggestions for adding or removing features, feel free to [open an issue](https://github.com/gyroflow/gyroflow/issues/new) to discuss it.
* If you want to implement a feature, you can fork this project, implement your code and open a pull request.

Currently *Gyroflow* is available in:

* **English** (base language)
* **Chinese Simplified** (by [DusKing1](https://github.com/DusKing1))
* **Chinese Traditional** (by [DusKing1](https://github.com/DusKing1))
* **Czech** (by Jakub Ešpandr, VitroidFPV, davidazarian, Michael Kmoch)
* **Danish** (by [ElvinC](https://github.com/ElvinC))
* **Finnish** (by Jesse Julkunen)
* **French** (by KennyDorion)
* **Galician** (by Martín Costas)
* **German** (by [Grommi](https://github.com/Gro2mi) and [Nicecrash](https://github.com/B-nutze-RR))
* **Greek** (by [Stamatis Galiatsatos](https://github.com/Logicenios))
* **Indonesian** (by Aloysius Puspandono)
* **Italian** (by Rosario Casciello)
* **Japanese** (by 井上康)
* **Korean** (by EP45)
* **Norwegian** (by [MiniGod](https://github.com/MiniGod) and [alexagv](https://github.com/alexagv))
* **Polish** (by [AdrianEddy](https://github.com/AdrianEddy))
* **Portuguese Brazilian** (by KallelGaNewk)
* **Portuguese** (by Ricardo Pimentel)
* **Russian** (by Андрей Гурьянов, redstar01 and lukdut)
* **Slovak** (by Radovan Leitman and Eduard Petrovsky)
* **Spanish** (by Pelado-Mat)
* **Turkish** (by [Metin Oktay Yılmaz](https://github.com/mettinoktay))
* **Ukrainian** (by Artem Alexandrov)

Help us translate *Gyroflow* to your language! We use *crowdin* to manage translations and you can contribute there: <https://crowdin.com/project/gyroflow>

#### I want to contribute but I don't know Rust or QML

### Used languages and technologies

*Gyroflow* is written in [Rust](https://www.rust-lang.org/), with UI written in [QML](https://doc.qt.io/qt-6/qmlfirststeps.html). It uses *Qt*, *ffmpeg*, *OpenCV* and *mdk-sdk* external dependencies for the main program, but the core library is written in pure Rust without any external dependencies.

OpenCV usage is kept to a minimum, used only for lens calibration and optical flow (`src/core/calibration/mod.rs` and `src/core/synchronization/opencv.rs`). Core algorithms and undistortion don't use OpenCV.

GPU stuff supports *DirectX*, *OpenGL*, *Metal* and *Vulkan* thanks to *Qt RHI* and *wgpu*.
For GPU processing we use *OpenCL* or *wgpu*, with highly parallelized CPU implementation as a fallback.

The Gyroflow binary links against mdk-sdk, which is closed-source and not licensed under the GNU GPL.
Gyroflow is licensed under GPLv3 with an additional permission allowing linking with mdk-sdk. mdk-sdk is distributed under its own license.

1. Entire GUI is in the `src/ui` directory
2. `src/controller.rs` is a bridge between UI and core, it takes all commands from QML and calls functions in core
3. `src/core` contains the whole gyroflow engine and doesn't depend on *Qt* or *ffmpeg*. *OpenCV* is optional
4. `src/rendering` contains all FFmpeg related code for rendering final video and processing for synchronization
5. `src/core/gpu` contains GPU implementations of the undistortion
6. `src/qt_gpu` contains zero-copy GPU undistortion path, using Qt RHI and GLSL compute shader
7. `src/gyroflow.rs` is the main entry point
8. `mod.rs` or `lib.rs` in each directory act as a main entry of the module (directory name is the module name and `mod.rs` is kind of an entry point)

`Visual Studio Code` with `rust-analyzer` extension.

For working with QML I recommend to use Qt Creator and load all QML files there, as it has auto-complete and syntax highlighting.
The project also supports UI live reload, it's a super quick way of working with the UI. Just change `live_reload = true` in `gyroflow.rs` and it should work right away. Now every time you change any QML file, the app should reload it immediately.

0. Prerequisites: `git`, `7z` and working `powershell`. If you never ran powershell scripts before, run `set-executionpolicy remotesigned` in powershell as admin
1. Get latest stable Rust language from: <https://rustup.rs/>
   * Please make sure to check the English language pack option when installing the C++ build tools from Visual Studio Installer
2. Install `Just` by running `cargo install --force just`
3. Clone the repo: `git clone https://github.com/gyroflow/gyroflow.git`
4. Enter the project directory and:
   * Install dependencies: `just install-deps`
   * Compile and run: `just run`

0. Prerequisites: `git`, `brew`
1. Get latest stable Rust language from: <https://rustup.rs/>
2. Install `Just` by running `cargo install --force just`
3. Clone the repo: `git clone https://github.com/gyroflow/gyroflow.git`
4. Enter the project directory and:
   * Install dependencies: `just install-deps`
   * Compile and run: `just run`
   * The first time you run it won't work, run `just deploy` once and then `just run` will work

0. Prerequisites: `git`, `7z`, `python`, `apt` package manager (or adjust commands inside scripts if on different distro)
1. Get latest stable Rust language from: <https://rustup.rs/>
2. Install `Just` by running `cargo install --force just`
3. Clone the repo: `git clone https://github.com/gyroflow/gyroflow.git`
4. Enter the project directory and:
   * Install dependencies: `just install-deps`
   * Compile and run: `just run`

0. Prerequisites: `git`, `7z`, working `powershell`, Android SDK and NDK. Building is supported only on Windows
1. Get latest stable Rust language from: <https://rustup.rs/>
2. Install `Just` by running `cargo install --force just`
3. Clone the repo: `git clone https://github.com/gyroflow/gyroflow.git`
4. Install Android SDK and NDK r23c and update paths in `_scripts/android.just`
5. Enter the project directory and:
   * Install dependencies: `just android install-deps`
   * Compile the apk and install on device: `just android deploy`

0. Prerequisites: `git`, `brew`
1. Get latest stable Rust language from: <https://rustup.rs/>
2. Install `Just` by running `cargo install --force just`
3. Clone the repo: `git clone https://github.com/gyroflow/gyroflow.git`
4. Enter the project directory and:
   * Install dependencies: `just ios install-deps`
   * Update Team ID, signing keys and provisioning profiles in `_scripts/ios.just`
   * Compile and run on device: `just ios run`

1. Install and run `Visual Studio Community Edition`
2. Compile and run Gyroflow with the `profile` profile: `just profile`
3. In Visual Studio, go to `Debug -> Performance Profiler...`
   * Under `Target`, open `Change Target` and select `Running Process...`, select the running `gyroflow.exe` process

1. Uncomment `config.define("QT_QML_DEBUG", None);` in `build.rs`
2. Comment `cli::run()` in `gyroflow.rs`
3. Run in debug mode with QML debugger args: `cargo run -- "-qmljsdebugger=port:1234,block,services:CanvasFrameRate,EngineControl,DebugMessages"`
4. In Qt Creator go to `Analyze` -> `QML Profiler (Attach to Waiting Application)` and enter port 1234

Distributed under the GPLv3 License with App Store Exception. See [LICENSE](https://github.com/gyroflow/gyroflow/blob/main/LICENSE) for more information.

As additional permission under section 7, you are allowed to distribute [`gyroflow_core`](https://github.com/gyroflow/gyroflow/tree/master/src/core) through an app store, even if that store has restrictive terms and conditions that are incompatible with the GPL, provided that the source is also available under the GPL with or without this permission through a channel without those restrictive terms and conditions.

The Gyroflow binary links against mdk-sdk, which is closed-source and not licensed under the GNU GPL.
An additional permission is granted allowing linking with mdk-sdk. mdk-sdk is distributed under its own license.

* [AdrianEddy](https://github.com/AdrianEddy/) - *Author of the Rust implementation (code in this repository), author of the UI, GPU processing, rolling shutter correction, advanced rendering features and the Adobe plugin*
* [Elvin Chen](https://github.com/ElvinC/) - *Author of the first version in Python, laid the groundwork to make all this possible*