---
title: "LÖVE: 2D Game Framework for Lua"
url: https://github.com/love2d/love
clipped: 2026-06-17 01:21:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Game Engines
  - Love2D
  - Lua Language
  - Cross-Platform Development
  - Open-Source Software
  - Generative AI Restrictions
related:
  - "[[Show HN Moongate – Ultima Online server emulator in .NET 10 with Lua scripting]]"
  - "[[Richard D. James aka Aphex Twin speaks to Tatsuya Takahashi (2017)]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** LÖVE is a popular open-source 2D game framework for Lua supporting major desktop and mobile platforms with a lightweight API.
>
> **Key points:**
> - LÖVE enables rapid game development in Lua across Windows, macOS, Linux, Android, and iOS.
> - Development is on the `main` branch, supported by separate stable release branches and nightly builds.
> - Rejects pull requests, bug reports, and contributions created with LLMs/generative AI.
> - Built using out-of-tree CMake configurations, with specific Xcode projects for macOS/iOS platforms.
>
> **Concept links:** [[Game Engines]], [[Love2D]], [[Lua Language]], [[Cross-Platform Development]], [[Open-Source Software]], [[Generative AI Restrictions]]
>
> **Suggested connections:**
> - [[Show HN Moongate – Ultima Online server emulator in .NET 10 with Lua scripting]] — related Lua-based game scripting.
> - [[Richard D. James aka Aphex Twin speaks to Tatsuya Takahashi (2017)]] — related microtuning/audio integrations.
<!-- ai-summary:end -->

# [LÖVE: 2D Game Framework for Lua](https://github.com/love2d/love)

## Digest Summary
LÖVE is an open‑source 2D game framework for Lua, supporting Windows, macOS, Linux, Android, and iOS. Development occurs on the **main** branch (unstable) with separate branches for released major versions; releases are tagged and binary downloads provided. Nightly builds are generated via GitHub CI, with Ubuntu packages in ppa:bartbes/love‑unstable and Arch packages in the AUR. A comprehensive test suite covers all LÖVE APIs and can be run with `love testing`. Contributions are accepted through the issue tracker, Discord/IRC, and pull requests, following the source‑code style guide; AI‑generated patches are rejected. Build instructions require out‑of‑tree CMake (≥ 3.15) or `-DCMAKE_INSTALL_PREFIX=` for older versions. macOS builds use the Xcode project `platform/xcode/love.xcodeproj`; iOS builds need the `love‑apple‑dependencies` zip and the same Xcode project. Android build steps are in a separate repository. Core dependencies include SDL3, OpenGL 3.3+/ES 3.0+/Vulkan/Metal, OpenAL, Lua/LuaJIT/LLVM‑lua, FreeType, harfbuzz, ModPlug, Vorbisfile, and Theora.

## Discussion Summary
Comments highlight strong enthusiasm for LÖVE (Love2D), praising its beginner‑friendly workflow, simple Lua API, and rapid prototyping via zip deployment. The community is described as welcoming and supportive, and the engine’s cross‑platform capabilities, SDL2 foundation, and performance are noted positively. Some express desire for an updated stable release and mention using the latest repository head for better performance. Comparisons to other frameworks note LÖVE’s lightweight nature versus larger engines, while a few note web‑based solutions as faster. Overall sentiment is largely favorable.

---

## Full Article

LÖVE is an *awesome* framework you can use to make 2D games in Lua. It's free, open-source, and works on Windows, macOS, Linux, Android, and iOS.

[![Build Status: Github CI](https://github.com/love2d/love/workflows/continuous-integration/badge.svg)](https://github.com/love2d/love/actions?query=workflow%3Acontinuous-integration)

We use our [wiki](https://love2d.org/wiki) for documentation.
If you need further help, feel free to ask on our [forums](https://love2d.org/forums), our [Discord server](https://discord.gg/rhUets9), or our [subreddit](https://www.reddit.com/r/love2d).

We use the 'main' branch for development of the next major release, and therefore it should not be considered stable.

There are also branches for currently released major versions, which may have fixes and changes meant for upcoming patch releases within that major version.

We tag all our releases (since we started using mercurial and git), and have binary downloads available for them.

Experimental changes are sometimes developed in a separate [love-experiments](https://github.com/slime73/love-experiments) repository.

Files for releases are in the [releases](https://github.com/love2d/love/releases) section on GitHub. [The site](https://love2d.org) has links to files and additional platform content for the latest release.

There are also unstable/nightly builds:

* Builds for some platforms are automatically created after each commit and are available through GitHub's CI interfaces.
* For ubuntu linux they are in [ppa:bartbes/love-unstable](https://launchpad.net/~bartbes/+archive/love-unstable)
* For arch linux there's [love-git](https://aur.archlinux.org/packages/love-git) in the AUR.

The test suite in `testing/` covers all the LÖVE APIs, and tests them the same way developers use them. You can view current test coverage from any [action](https://github.com/love2d/love/actions/workflows/main.yml?query=branch%3Amain).  
You can run the suite locally like you would run a normal LÖVE project, e.g.:  
`love testing`

See the [readme](https://github.com/love2d/love/tree/main/testing) in the testing folder for more info.

The best places to contribute are through the issue tracker and the official Discord server.

For code contributions, pull requests and patches are welcome. Be sure to read the [source code style guide](https://love2d.org/wiki/Code_Style).
Changes and new features typically get discussed in the issue tracker or on Discord or the forums before a pull request is made.

Note

Pull requests, bug reports, and other contributions made with LLM / generative AI technology will not be accepted.

Follow the instructions at the [megasource](https://github.com/love2d/megasource) repository page.

Because in-tree builds are not allowed, the Makefiles needs to be generated in a separate build directory. In this example, folder named `build` is used:

```
$ cmake -B build -S. --install-prefix $PWD/prefix # this will create the directory `build/`.
$ cmake --build build --target install -j$(nproc) # this will build with all cores and put the files in `prefix/`.
```

Note

CMake 3.15 and earlier doesn't support `--install-prefix`. In that case, use `-DCMAKE_INSTALL_PREFIX=` instead.

Download or clone [this repository](https://github.com/love2d/love-apple-dependencies) and copy, move, or symlink the `macOS/Frameworks` subfolder into love's `platform/xcode/macosx` folder and the `shared` subfolder into love's `platform/xcode` folder.

Then use the Xcode project found at `platform/xcode/love.xcodeproj` to build the `love-macosx` target.

Building for iOS requires macOS and Xcode.

Download the `love-apple-dependencies` zip file corresponding to the LÖVE version being used from the [Releases page](https://github.com/love2d/love/releases),
unzip it, and place the `iOS/libraries` subfolder into love's `platform/xcode/ios` folder and the `shared` subfolder into love's `platform/xcode` folder.

Or, download or clone [this repository](https://github.com/love2d/love-apple-dependencies) and copy, move, or symlink the `iOS/libraries` subfolder into love's `platform/xcode/ios` folder and the `shared` subfolder into love's `platform/xcode` folder.

Then use the Xcode project found at `platform/xcode/love.xcodeproj` to build the `love-ios` target.

See `readme-iOS.rtf` for more information.

Visit the [Android build repository](https://github.com/love2d/love-android) for build instructions.

* SDL3
* OpenGL 3.3+ / OpenGL ES 3.0+ / Vulkan / Metal
* OpenAL
* Lua / LuaJIT / LLVM-lua
* FreeType
* harfbuzz
* ModPlug
* Vorbisfile
* Theora