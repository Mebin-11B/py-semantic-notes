---
title: "Run Android ARM64 VR APKs on Apple Vision Pro"
url: https://github.com/shinyquagsire23/Klepton
clipped: 2026-08-31 12:22:38
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Run Android ARM64 VR APKs on Apple Vision Pro](https://github.com/shinyquagsire23/Klepton)

## Digest Summary
GitHub project Klepton provides a JIT‑less relinker and compatibility layer that enables Android ARM64 VR/AR APKs (e.g., Quest/Android XR) to run on Apple Vision Pro, visionOS, and macOS. It translates Android .so libraries into loadable Apple .dylib/.framework binaries, which link against the Klepton runtime. Key components:

Graphics translation: OpenGL ES 3.2 → vendored ANGLE GLES 3.0 with Metal backend; Vulkan → MoltenVK (Vulkan‑to‑Metal).
Runtime libraries: libklepton_bionic maps libc, libm, libdl, pthread, liblog to libSystem; libklepton_ndk implements ALooper, ANativeWindow, ASensor, AAsset; libklepton_jni provides a synthetic JavaVM/JNI; libklepton_ovrp re‑implements Oculus runtime functions.
TLS handling: Patches usage of register x18 (used by older Android apps) because macOS zeroes x18 on context switches, substituting per‑library TLS slots.
Runtime loading: Supports mmap‑based loading/patching of .so files; JIT is only needed for apps that rely on scripting engines such as LuaJIT or V8, which macOS permits.
Build/Run: Uses Homebrew for dependencies; apktool to unpack APKs; make check for regression; scripts (build_run_viewer.sh, build_run_vpro.sh, build_run_slink.sh) compile and launch Beat Saber on macOS and Vision Pro. Beat Saber runs with minor graphics issues; Steam VR Link and broader tooling are under development.

---

## Full Article

[Skip to content](https://github.com/shinyquagsire23/Klepton#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [shinyquagsire23](https://github.com/shinyquagsire23)    
    /
    
      [Klepton](https://github.com/shinyquagsire23/Klepton)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fshinyquagsire23%2FKlepton)    You must be signed in to change notification settings

  

  
- 
          [Fork
    10](https://github.com/login?return_to=%2Fshinyquagsire23%2FKlepton)
  

  
- 
        
        [Star
          169](https://github.com/login?return_to=%2Fshinyquagsire23%2FKlepton)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/shinyquagsire23/Klepton/branches)[Tags](https://github.com/shinyquagsire23/Klepton/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[165 Commits](https://github.com/shinyquagsire23/Klepton/commits/main/)165 Commits

## Folders and files

NameNameLast commit messageLast commit date[angle-patches](https://github.com/shinyquagsire23/Klepton/tree/main/angle-patches)[angle-patches](https://github.com/shinyquagsire23/Klepton/tree/main/angle-patches)  [guest](https://github.com/shinyquagsire23/Klepton/tree/main/guest)[guest](https://github.com/shinyquagsire23/Klepton/tree/main/guest)  [mains](https://github.com/shinyquagsire23/Klepton/tree/main/mains)[mains](https://github.com/shinyquagsire23/Klepton/tree/main/mains)  [runtime](https://github.com/shinyquagsire23/Klepton/tree/main/runtime)[runtime](https://github.com/shinyquagsire23/Klepton/tree/main/runtime)  [spikes](https://github.com/shinyquagsire23/Klepton/tree/main/spikes)[spikes](https://github.com/shinyquagsire23/Klepton/tree/main/spikes)  [tests](https://github.com/shinyquagsire23/Klepton/tree/main/tests)[tests](https://github.com/shinyquagsire23/Klepton/tree/main/tests)  [tools](https://github.com/shinyquagsire23/Klepton/tree/main/tools)[tools](https://github.com/shinyquagsire23/Klepton/tree/main/tools)  [visionos](https://github.com/shinyquagsire23/Klepton/tree/main/visionos)[visionos](https://github.com/shinyquagsire23/Klepton/tree/main/visionos)  [.gitignore](https://github.com/shinyquagsire23/Klepton/blob/main/.gitignore)[.gitignore](https://github.com/shinyquagsire23/Klepton/blob/main/.gitignore)  [BUILDING.md](https://github.com/shinyquagsire23/Klepton/blob/main/BUILDING.md)[BUILDING.md](https://github.com/shinyquagsire23/Klepton/blob/main/BUILDING.md)  [DEBUG_ENV_VARS.md](https://github.com/shinyquagsire23/Klepton/blob/main/DEBUG_ENV_VARS.md)[DEBUG_ENV_VARS.md](https://github.com/shinyquagsire23/Klepton/blob/main/DEBUG_ENV_VARS.md)  [LICENSE](https://github.com/shinyquagsire23/Klepton/blob/main/LICENSE)[LICENSE](https://github.com/shinyquagsire23/Klepton/blob/main/LICENSE)  [Makefile](https://github.com/shinyquagsire23/Klepton/blob/main/Makefile)[Makefile](https://github.com/shinyquagsire23/Klepton/blob/main/Makefile)  [README.md](https://github.com/shinyquagsire23/Klepton/blob/main/README.md)[README.md](https://github.com/shinyquagsire23/Klepton/blob/main/README.md)  [build_run_host.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_host.sh)[build_run_host.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_host.sh)  [build_run_slink_vpro.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_slink_vpro.sh)[build_run_slink_vpro.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_slink_vpro.sh)  [build_run_viewer.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_viewer.sh)[build_run_viewer.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_viewer.sh)  [build_run_vpro.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_vpro.sh)[build_run_vpro.sh](https://github.com/shinyquagsire23/Klepton/blob/main/build_run_vpro.sh)  View all files

## Repository files navigation

# Klepton

Running Android ARM64 VR APKs on Apple Vision Pro, no JIT required!

## Architecture

 `klepton-ld`  translates Android  `.so`  libraries into loadable Apple  `.dylib`  and  `.framework`  libraries, which then link into the Klepton runtime. Klepton currently focuses on Java-thin applications only (no ART, no JVM).

For graphics, GLES 3.2 is translated to a vendored ANGLE GLES 3.0 (with its Metal backend), and Vulkan is translated to MoltenVK.
 ` `┌─────────────────────────────────────────────────────────────────┐
│  GUEST (translated Mach-O, instruction bytes mostly unmodified) │
│  libil2cpp · libunity · libunityopus · libmain · burst · ...    │
└─────────────────────────────────────────────────────────────────┘
    ↕ imports resolved to Klepton runtime in `klepton-ld`
┌─────────────────────────────────────────────────────────────────┐
│  libklepton_bionic   libc/libm/libdl/pthread/liblog → libSystem │
│  libklepton_ndk      ALooper · ANativeWindow · ASensor · AAsset │ 
│  libklepton_jni      synthetic JavaVM / JNIEnv                  │
│  libklepton_ovrp     ovrp_* reimplementation                    │
│  ...                                                            │
└─────────────────────────────────────────────────────────────────┘
    ↕ Frontend platform (`mains`) and OS-specifics
┌─────────────────────────────────────────────────────────────────┐
│  MoltenVK (Vulkan → Metal)     ANGLE (GLES 3.0)                 │
│  Compositor Services · ARKit · GameController · AVAudioEngine   │
└─────────────────────────────────────────────────────────────────┘
` ` 

While both Android and macOS reserve x18, some (a lot of) older Android applications still use x18, and macOS zeros x18 on context switches. All usage of x18 is patched by  `klepton-ld`  so that per-library TLS slots are used instead.

Klepton also has the ability to load and patch  `.so`  files at runtime with  `mmap` , but this is only really useful on macOS where JIT is actually allowed. It's likely that some applications will require JIT if they happen to utilize scripting runtimes that expect it (LuaJIT, V8, whatever else).

## Building

See  `` [BUILDING.md](https://github.com/shinyquagsire23/Klepton/blob/main/BUILDING.md) for the full guide. The short version:
 `brew install pkg-config sdl3 apktool          # host dependencies
apktool d -f -o beatsaber beatsaber.apk       # you supply the APK; see BUILDING.md
make check                                    # full regression sweep` 

Quick run scripts:
 `./build_run_viewer.sh [target] # build and run macOS frontend
./build_run_vpro.sh [target]  # build and run Vision Pro frontend
./build_run_host.sh [target]  # build and run a guest headless, with a summary
./build_run_host.sh steamlink-vr --shell --view  # Steam VR Link frontend (WIP)` 

Where  `[target]`  is the name of the target, defaulting to  `beatsaber` .

## Status

Currently working well on both macOS and visionOS with minor-to-no graphical issues:

- Beat Saber versions 1.6, 1.28, and 1.40

- BONELAB

- SUPERHOT VR

- Resident Evil 4 VR

- OpenBrush (OpenXR)

- OpenJK XR (Team Beef)

WIP or not in a great state:

- Steam VR Link (no AWDL mitigations due to entitlement restrictions, XR_EXT_hand_tracking not implemented yet)

Abandoned due to anticheat, JIT mmaping, or other problems:

- VRChat (Steam Frame APK)

## About

JIT-less relinker and compatibility layer for running Quest/Android XR APKs on visionOS and macOS

### Resources

[Readme](https://github.com/shinyquagsire23/Klepton#readme-ov-file)[MIT license](https://github.com/shinyquagsire23/Klepton#MIT-1-ov-file)[Activity](https://github.com/shinyquagsire23/Klepton/activity)

### Stars

169 stars

### Watchers

3 watching

### Forks

[10 forks](https://github.com/shinyquagsire23/Klepton/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fshinyquagsire23%2FKlepton&report=shinyquagsire23+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
