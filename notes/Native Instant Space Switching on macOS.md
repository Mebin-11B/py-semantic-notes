---
title: "Native Instant Space Switching on macOS"
url: https://arhan.sh/blog/native-instant-space-switching-on-macos/
clipped: 2026-06-17 01:19:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Native Instant Space Switching on macOS](https://arhan.sh/blog/native-instant-space-switching-on-macos/)

## Digest Summary
The article critiques existing macOS space‑switching methods and presents a native solution. It notes that the “Reduce motion” setting only replaces the default animation with a fade, and that Yabai achieves instant switching via binary patches requiring System Integrity Protection (SIP) disablement and forces use of its tiling window manager, which conflicts with alternatives like PaperWM.spoon. Third‑party virtual workspace tools (e.g., FlashSpace, AeroSpace) are deemed unnecessary because they emulate spaces rather than disabling animation. BetterTouchTool can provide “Move Right/Left Space (Without Animation)” but requires a paid license. The author recommends InstantSpaceSwitcher (GitHub: jurplel/InstantSpaceSwitcher), a menu‑bar app that simulates a high‑velocity trackpad swipe to switch spaces instantly without disabling SIP. It supports left/right moves, direct jumps to a specific space index, and offers a CLI. Installation steps: clone the repo, run `./build.sh`; the CLI becomes available at `.build/release/ISSCli`. The project has minimal GitHub stars, and the author encourages users to star it if useful.

## Discussion Summary
Comments express widespread frustration with macOS’s space‑switching animation, especially on newer 120 Hz displays where it feels slower and disrupts muscle memory. Users frequently cite accessibility concerns, productivity loss, and a perception that Apple has deprioritized power‑user needs, prompting many to adopt third‑party tools, reduce‑motion settings, or switch to alternative window managers and operating systems such as Linux. While a minority enjoy the visual effect, the dominant view calls for faster, customizable transitions and criticizes Apple’s limited options for disabling or adjusting the animation.

---

## Full Article

The worst part about the MacOS window management situation is the inability to instantly switch spaces, and that Apple has [continuously ignored requests](https://discussions.apple.com/thread/253938203?sortBy=rank) to disable the nauseating switching animation. Sure, it’s not *that* long, but I switch spaces often enough to the point where it becomes very noticeable and drives me insane.

I believe to have found the best solution to instant space switching!

But before I show you, of course, other people share the same sentiment. I claim that none of the surveyed contemporary solutions, except for what I bring up at the end of this article, suffice for what I want:

1. Enable the “Reduce motion” setting in System Settings.

   This is always the default answer to this question online, and I’m sick of it! It doesn’t even solve the problem, but rather replaces it with an equally useless fade-in animation. It also has the side effect of activating the [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) media query on web browsers.
2. Install the [yabai](https://github.com/asmvik/yabai) tiling window manager and use its instant space switcher.

   And to be fair, it works pretty well. There are only two problems: for one, yabai does this by binary patching a part of the operating system. This is only possible by disabling [System Integrity Protection](https://en.wikipedia.org/wiki/System_Integrity_Protection) at your own discretion. For the second, installing yabai forces you to learn and use it as your tiling window manager[1](https://arhan.sh/blog/native-instant-space-switching-on-macos/#fn-instantspaces). I personally use [PaperWM.spoon](https://github.com/mogenson/PaperWM.spoon) as my window manager. Both of which are incompatible when installed together.
3. Use a third-party virtual space manager facade, hiding and showing windows as needed when switching spaces.

   Some popular options are [FlashSpace](https://github.com/wojciech-kulik/FlashSpace) and [AeroSpace virtual workspaces](https://nikitabobko.github.io/AeroSpace/guide#emulation-of-virtual-workspaces). I actually offer no criticism other than that they are not native to MacOS, and feel unnecessary given that all we want to do is disable an animation.
4. Pay for a license for [BetterTouchTool](https://folivora.ai). Enable “Move Right Space (Without Animation)” and “Move Left Space (Without Animation)”.

Without further ado, I managed to find [InstantSpaceSwitcher](https://github.com/jurplel/InstantSpaceSwitcher) by [jurplel](https://github.com/jurplel) on GitHub. It is a simple menu bar application that achieves instant space switching while offering *none* of the aforementioned drawbacks. You can bind a keybind or use swipe gestures to instantly switch spaces.

![A commit with 2,000 contributors](https://arhan.sh/_astro/settings._dQOT8aK_Z37rj.png) 

Here I have InstantSpaceSwitcher paired up with

[SpaceName](https://github.com/ekalinin/SpaceName)

.

InstantSpaceSwitcher does not require disabling Security Integration Protection; it works by simulating a trackpad swipe with a large amount of velocity. It additionally allows you to instantly jump to a space number. The last thing it provides is a command line interface.

The installation instructions are [listed on the README](https://github.com/jurplel/InstantSpaceSwitcher#installation), and I will briefly repeat them. You can either install InstantSpaceSwiter via Homebrew:

```
brew install --cask jurplel/tap/instant-space-switcher
```

Building from source:

```
git clone https://github.com/jurplel/InstantSpaceSwitcher
cd InstantSpaceSwitcher
./dist/build.sh
open ./build/InstantSpaceSwitcher.app
```

Or using a [pre-built binary](https://github.com/jurplel/InstantSpaceSwitcher/tags).

It is recommended to move `InstantSpaceSwitcher.app` to `/Applications` to install it as a native application.

The command line interface is provided at:

```
$ InstantSpaceSwitcher.app/Contents/MacOS/ISSCli --help
Usage: InstantSpaceSwitcher.app/Contents/MacOS/ISSCli [left|right|index <n>]
```

Did I mention that the repository literally has one star on GitHub (me)? I want more people to discover InstantSpaceSwitcher and consider it trustworthy; hence, please consider giving it a [star](https://github.com/jurplel/InstantSpaceSwitcher) if you find it helpful.

Until next time!

[↑ Scroll to top ↑](https://arhan.sh/blog/native-instant-space-switching-on-macos/#page-top)