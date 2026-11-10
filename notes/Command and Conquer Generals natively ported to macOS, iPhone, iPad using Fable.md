---
title: "Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable"
url: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main
clipped: 2026-08-31 12:22:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main)

## Digest Summary
The repository provides a native port of Command & Conquer Generals: Zero Hour for Apple Silicon Macs, iPhone, and iPad, using the original 2003 engine compiled for ARM64. It translates DirectX 8 calls through DXVK to Vulkan, then to MoltenVK and Metal, delivering RTS‑style touch controls (tap‑select, drag‑box, pinch‑zoom, two‑finger scroll). The code builds on EA’s GPL‑v3 source released via GeneralsX; this fork adds iOS/iPadOS support and various engine fixes. No game assets are distributed; users must supply their own copy (e.g., via Steam). One‑time prerequisites include Xcode command‑line tools, Homebrew packages (cmake, ninja, meson, pkgconf, steamcmd), Microsoft vcpkg, and the LunarG Vulkan SDK. Build scripts automate macOS compilation and deployment; iOS builds require full Xcode, an Apple Developer team, and additional scripts to fetch MoltenVK, fonts, and package the app. Known issues include occasional iOS memory‑limit termination and background‑pause crashes; frequent saves are advised. Credits list Westwood/EA, fbraz3/GeneralsX, DXVK, MoltenVK, SDL, OpenAL Soft, FFmpeg, and Liberation Fonts.

---

## Full Article

[Skip to content](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [ammaarreshi](https://github.com/ammaarreshi)    
    /
    
      [Generals-Mac-iOS-iPad](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fammaarreshi%2FGenerals-Mac-iOS-iPad)    You must be signed in to change notification settings

  

  
- 
          [Fork
    153](https://github.com/login?return_to=%2Fammaarreshi%2FGenerals-Mac-iOS-iPad)
  

  
- 
        
        [Star
          1.6k](https://github.com/login?return_to=%2Fammaarreshi%2FGenerals-Mac-iOS-iPad)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/branches)[Tags](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[2,003 Commits](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/commits/main/)2,003 Commits

## Folders and files

NameNameLast commit messageLast commit date[.devin](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.devin)[.devin](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.devin)  [.github](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.github)[.github](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.github)  [.vscode](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.vscode)[.vscode](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/.vscode)  [Core](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Core)[Core](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Core)  [Dependencies](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Dependencies)[Dependencies](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Dependencies)  [Generals](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Generals)[Generals](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Generals)  [GeneralsMD](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/GeneralsMD)[GeneralsMD](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/GeneralsMD)  [GeneralsReplays @ 113cabc](https://github.com/fbraz3/GeneralsXReplays/tree/113cabc289426459a5fa5da810131cac498c8e5a)[GeneralsReplays @ 113cabc](https://github.com/fbraz3/GeneralsXReplays/tree/113cabc289426459a5fa5da810131cac498c8e5a)  [GeneralsZH/Data/Window/Menus](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/GeneralsZH/Data/Window/Menus)[GeneralsZH/Data/Window/Menus](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/GeneralsZH/Data/Window/Menus)  [Patches](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Patches)[Patches](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/Patches)  [assets](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/assets)[assets](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/assets)  [cmake](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/cmake)[cmake](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/cmake)  [docs](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/docs)[docs](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/docs)  [flatpak](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/flatpak)[flatpak](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/flatpak)  [ios](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/ios)[ios](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/ios)  [references](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/references)[references](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/references)  [resources](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/resources)[resources](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/resources)  [scripts](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/scripts)[scripts](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/scripts)  [triplets](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/triplets)[triplets](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main/triplets)  [.clang-tidy](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.clang-tidy)[.clang-tidy](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.clang-tidy)  [.editorconfig](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.editorconfig)[.editorconfig](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.editorconfig)  [.gitignore](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.gitignore)[.gitignore](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.gitignore)  [.gitmodules](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.gitmodules)[.gitmodules](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/.gitmodules)  [AGENTS.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/AGENTS.md)[AGENTS.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/AGENTS.md)  [CMakeLists.txt](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CMakeLists.txt)[CMakeLists.txt](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CMakeLists.txt)  [CMakePresets.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CMakePresets.json)[CMakePresets.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CMakePresets.json)  [CONTRIBUTING.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/CONTRIBUTING.md)  [LICENSE.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/LICENSE.md)[LICENSE.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/LICENSE.md)  [README.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/README.md)[README.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/README.md)  [SECURITY.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/SECURITY.md)[SECURITY.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/SECURITY.md)  [TESTING.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/TESTING.md)[TESTING.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/TESTING.md)  [stlport.diff](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/stlport.diff)[stlport.diff](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/stlport.diff)  [vcpkg-lock.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/vcpkg-lock.json)[vcpkg-lock.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/vcpkg-lock.json)  [vcpkg.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/vcpkg.json)[vcpkg.json](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/vcpkg.json)  View all files

## Repository files navigation

# Command & Conquer Generals: Zero Hour — macOS, iOS & iPadOS

Zero Hour running natively on Apple Silicon Macs, iPhone, and iPad — campaign,
skirmish, and Generals Challenge, with touch controls built for RTS (tap-select,
drag-box, long-press deselect, two-finger scroll, pinch zoom). No emulation: this
is the real 2003 engine compiled for ARM64, rendering DirectX 8 →
[DXVK](https://github.com/doitsujin/dxvk) → Vulkan →
[MoltenVK](https://github.com/KhronosGroup/MoltenVK) → Metal.

Built on EA's GPL v3 source release, standing on a chain of community work —
[TheSuperHackers](https://github.com/TheSuperHackers/GeneralsGameCode),
[Fighter19's original Unix port](https://github.com/Fighter19/CnC_Generals_Zero_Hour), and
[fbraz3/GeneralsX](https://github.com/fbraz3/GeneralsX) — this fork adds the iOS/iPadOS
port and a set of engine fixes. See [Lineage & credits](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#lineage--credits) for who built
what. The original GeneralsX README lives on the  `upstream-main`  branch.

No game assets are included or distributed. You need your own copy
([Steam](https://store.steampowered.com/app/2732960/), ~$5 on sale).

## What this port actually involved

"Porting" undersells how weird this journey was, so here's the honest shape of it.
The lineage below built the foundation: EA's source release, the community's
modernization, Fighter19's original Unix port, GeneralsX's macOS/Linux work.
What did not exist was any of this on iOS — and iOS is a hostile place for a
2003 Windows RTS:

- The engine assumes a writable filesystem wherever it lives. iOS apps live in a
read-only, code-signed bundle. Every config write, cache, and save path had to be
rerouted — and the working directory bootstrapped from the bundle itself.

- The renderer speaks DirectX 8. The iPad speaks Metal. In between: DXVK
translating D3D8→Vulkan, MoltenVK translating Vulkan→Metal — and DXVK had never
been built for iPhoneOS. That took a Meson cross-build and a patch to its Vulkan
loader, because iOS confines  `dlopen`  to the app bundle ( `` [Patches/dxvk-ios.patch](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/Patches/dxvk-ios.patch)).

- iOS owns your process. Open the app switcher and the OS seizes the Metal
drawable without backgrounding you — draw one more frame and you're dead on
resume. The whole render/sim loop learned to hold its breath.

- An RTS needs a mouse. SDL3 (from the lineage below) delivers raw touch events;
the RTS semantics on top are new. Taps defer until the 2003 GUI has processed
hover (or menu buttons never highlight), a drag has to decide "selection box or
camera pan," long-press became right-click, and a cancelled touch must never
ghost-click a rally point.

- And then the bug hunts — the best part. The minimap that rendered black
because a 2003 texture-format fallback silently dropped the alpha channel. The
EVA voice that went randomly mute because one zombie audio stream held a global
"don't talk over speech" flag while chirping forever. Every one chased to root
cause on a real device, fixed, and offered upstream.

→ The war stories: [Porting Playbook §8 — the bug archaeology](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/docs/port/PORTING_PLAYBOOK.md#8-post-ship-bug-hunts-junejuly-2026--the-archaeology-section)
→ The complete engineering log: [docs/port/PORTING_PLAYBOOK.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/docs/port/PORTING_PLAYBOOK.md)
→ How to do this to another game: [docs/port/PORTING_PATTERNS.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/docs/port/PORTING_PATTERNS.md)

Worth saying plainly: this was a human + AI collaboration. The engineering —
the C++, the cross-builds, the device debugging — was done by
[Claude Code](https://claude.com/claude-code) (Anthropic's Claude, Fable model),
directed and playtested by a human who described symptoms like "the minimap is
black" and "I hear chirping" and owned every decision. Neither half ships this
alone: one of us can't write C++, and the other can't hear the chirping.

## Quick start — macOS

Prerequisites (one time):
 `# Toolchain
xcode-select --install
brew install cmake ninja meson pkgconf
brew install --cask steamcmd

# vcpkg (full clone — a shallow clone breaks manifest baselines)
git clone https://github.com/microsoft/vcpkg ~/vcpkg && ~/vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=~/vcpkg          # add to your shell profile

# LunarG Vulkan SDK (NOT the Homebrew cask) — https://vulkan.lunarg.com/sdk/home
export VULKAN_SDK=$HOME/VulkanSDK/<version>/macOS   # add to your shell profile` 

Clone, build, get assets, play:
 `git clone https://github.com/ammaarreshi/Generals-Mac-iOS-iPad.git GeneralsX
cd GeneralsX
./scripts/build/macos/build-macos-zh.sh     # checks deps, configures, builds
./scripts/build/macos/deploy-macos-zh.sh    # creates ~/GeneralsX/GeneralsZH + run.sh
./scripts/get-assets.sh <your_steam_username>   # fetches game data you own
cd ~/GeneralsX/GeneralsZH && ./run.sh -win` 

## Quick start — iPhone / iPad

On top of the macOS prerequisites: full Xcode (signed into your Apple ID),
 `brew install xcodegen` , and a (free or paid) Apple Developer team.
 `cd GeneralsX
git submodule update --init references/fbraz3-dxvk   # iOS DXVK is built from this + Patches/dxvk-ios.patch
./scripts/build/ios/fetch-moltenvk.sh                # pinned MoltenVK.framework (checksummed)
./scripts/build/ios/stage-fonts.sh                   # Liberation fonts, renamed as the game expects
cmake --preset ios-vulkan
cmake --build build/ios-vulkan --target z_generals
GX_TEAM_ID=<your-team-id> GX_BUNDLE_ID=com.you.generalszh \
    ./scripts/build/ios/package-ios-zh.sh --install  # assembles, signs, installs` 

Find your team id in Xcode → Settings → Accounts. Assets ship inside the app
bundle (self-contained install);  `--dev`  skips the ~2.7 GB copy for fast code
iteration.

## Where things are

Path
What it is

 `` [docs/port/PORTING_PLAYBOOK.md](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/docs/port/PORTING_PLAYBOOK.md)
The complete engineering log of this port: every failure mode, root cause, fix — start with [§8, the bug archaeology](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/blob/main/docs/port/PORTING_PLAYBOOK.md#8-post-ship-bug-hunts-junejuly-2026--the-archaeology-section): the black minimap, the silent EVA lines, and the chirp

 `docs/port/PORTING_PATTERNS.md` 
Generalized methodology for porting classic Windows games to Apple platforms

 `docs/port/RELEASE_CHECKLIST.md` 
Gate for public release

 `scripts/get-assets.sh` 
Steam asset fetcher (your own copy; app 2732960)

 `scripts/build/macos/` ,  `scripts/build/ios/` 
Build, deploy, packaging pipelines

 `ios/` 
XcodeGen signing-stub project +  `ios/config/`  (staged Options.ini, dxvk.conf)

 `Patches/dxvk-ios.patch` 
DXVK changes the iOS d3d8/d3d9 dylibs are built from (applied via the local-fork build)

## Known issues

- Long sessions on iPad can be killed by iOS for memory (~3 GB+ resident); the app
exits to the home screen with no dialog. Session logs (current + previous) are in
the Files app under the game's folder. Under investigation.

- Backgrounding mid-game can occasionally crash on iOS — the lifecycle pause covers
the common paths; a rare race remains. Save often.

## What's next: Renegade 👀

Generals had a chain of giants to stand on. Command & Conquer: Renegade — EA's
2002 FPS from the same GPL source release — has far less: no native macOS or iOS
build of the W3D engine has ever shipped (Mac players today go through Wine-based
compatibility layers). The [OpenW3D](https://github.com/w3dhub/OpenW3D) community
project has real cross-platform groundwork — a DXVK wrapper scaffold and SDL3 build
plumbing — with Mac/Linux on its roadmap, and that groundwork is exactly what we
built on.

Same methodology as this repo, much deeper water: OpenW3D's Win32 compat scaffold
expanded by ~3,000 lines (the engine calls raw Windows APIs for file finding,
keyboard state, COM), a case-sensitivity strategy for twenty thousand asset paths,
the DXVK/MoltenVK renderer bring-up, the audio/video stack, and FPS touch controls.
It's playable today — campaign, cinematics, mission scripts — on a Mac and an
iPhone. For scale: this Generals port added ~2,200 lines on top of GeneralsX;
Renegade needed ~6,700 on top of the Windows-only source.

Repo drops soon, with the OpenW3D lineage credited the way this repo credits its
chain. Same rules: GPL v3, bring your own copy, full engineering log.

## Lineage & credits

This port is the newest link in a long chain, and the earlier links did foundational
work that this repo inherits everywhere:

- Westwood / EA Pacific — the game; EA — the GPL v3 source release

- [TheSuperHackers/GeneralsGameCode](https://github.com/TheSuperHackers/GeneralsGameCode) —
the community mainline: build modernization, VC6→modern toolchain, and much of the
cross-platform groundwork, including the FFmpeg video backend authored by
[feliwir](https://github.com/feliwir) (of [OpenSAGE](https://github.com/OpenSAGE/OpenSAGE)),
who also authored the OpenAL audio device work this port's audio stack builds on

- [Fighter19/CnC_Generals_Zero_Hour](https://github.com/Fighter19/CnC_Generals_Zero_Hour) —
the original Unix/64-bit port: SDL3 platform management, C++17
filesystem/threading, Freetype/Fontconfig text rendering, and the DXVK approach
this renderer path descends from

- [fbraz3/GeneralsX](https://github.com/fbraz3/GeneralsX) — the macOS/Linux port
this fork builds on directly, integrating and extending the above

- This fork — the iOS/iPadOS port (arm64-ios cross-build, DXVK-on-iOS, touch
controls, app lifecycle, packaging) and engine fixes, offered upstream

- DXVK, MoltenVK, SDL, OpenAL Soft, FFmpeg, Liberation Fonts — the load-bearing walls

Engine code GPL v3 (EA's source release → the chain above → this fork). Game
assets: not included, not licensed here.

## About

Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad — real engine (EA GPL v3 source, via GeneralsX), DXVK/MoltenVK renderer, RTS touch controls. No game assets included.

### Topics

[apple-silicon](https://github.com/topics/apple-silicon)[command-and-conquer](https://github.com/topics/command-and-conquer)[dxvk](https://github.com/topics/dxvk)[game-port](https://github.com/topics/game-port)[generals-zero-hour](https://github.com/topics/generals-zero-hour)[ios](https://github.com/topics/ios)[ipad](https://github.com/topics/ipad)[macos](https://github.com/topics/macos)[moltenvk](https://github.com/topics/moltenvk)[open-source-game](https://github.com/topics/open-source-game)[rts](https://github.com/topics/rts)[sdl3](https://github.com/topics/sdl3)

### Resources

[Readme](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#readme-ov-file)[License](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#License-1-ov-file)

### Contributing

[Contributing](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#contributing-ov-file)

### Security policy

[Security policy](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main#security-ov-file)[Activity](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/activity)

### Stars

1.6k stars

### Watchers

9 watching

### Forks

[153 forks](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fammaarreshi%2FGenerals-Mac-iOS-iPad&report=ammaarreshi+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
