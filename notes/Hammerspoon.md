---
title: "Hammerspoon"
url: https://github.com/Hammerspoon/hammerspoon
clipped: 2026-06-17 01:33:17
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - macos automation
  - lua scripting
  - developer productivity
related:
  - "[[Nitpicking the shell history scene in 'Tron Legacy']]"
  - "[[Anatomy of the .claude folder]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Hammerspoon is a powerful, open-source macOS automation framework that links the operating system to a Lua scripting engine via custom system extensions.
>
> **Key points:**
> - Connects macOS system APIs to a Lua scripting engine for powerful, personalized OS automation.
> - Originates as a fork of the Mjolnir project, opting for a more integrated, feature-rich developer experience.
> - Enables window management, keyboard shortcut mapping, and deep control over system events using custom 'Spoons'.
> - Enjoys strong community support and is widely adopted as an alternative or complement to proprietary automation tools.
>
> **Concept links:** [[macOS Automation]], [[Lua Scripting]], [[Window Management]], [[Open Source Tooling]], [[Developer Productivity]]
>
> **Suggested connections:**
> - [[Nitpicking the shell history scene in 'Tron Legacy']] — connects to custom scripting and command line environments on macOS/Linux.
> - [[Anatomy of the .claude folder]] — highlights developer environments and local file automation.
<!-- ai-summary:end -->

# [Hammerspoon](https://github.com/Hammerspoon/hammerspoon)

## Digest Summary
Hammerspoon is a macOS automation framework that connects the operating system to a Lua scripting engine. Its functionality derives from a suite of extensions that expose specific system APIs, allowing users to write Lua scripts to control various aspects of macOS. Installation can be performed by dragging the downloaded Hammerspoon.app into /Applications or via Homebrew (`brew install hammerspoon --cask`). After installation, users create ~/.hammerspoon/init.lua to load custom scripts. The project originated as a fork of Mjolnir, which emphasized minimalism and external extension management; Hammerspoon seeks a more integrated experience. Development goals include expanding coverage of system APIs across extensions, improving integration between extensions, and delivering a smoother overall user experience. Continuous integration and code coverage metrics are displayed on the project page.

## Discussion Summary
The comments convey a strongly positive consensus: users rely on Hammerspoon as an essential, versatile automation layer for macOS, praising its Lua‑based scripting, extensive hotkey and window‑management capabilities, and the rich ecosystem of spoons. Many share detailed personal workflows and express enthusiasm for community contributions and tutorials. Minor concerns appear around the planned shift to JavaScript and occasional limitations such as space switching without disabling SIP, but overall the tool is viewed as superior or complementary to alternatives like Yabai, Keyboard Maestro, or AppleScript.

---

## Full Article

[![CI](https://github.com/Hammerspoon/hammerspoon/workflows/CI/badge.svg)](https://github.com/Hammerspoon/hammerspoon/actions?query=workflow%3ACI)
[![codecov.io](https://camo.githubusercontent.com/2d089bb159213bf737ae6f182dbe7ac39f0e1396ed49c5ee9a453d5a3e91c6e6/68747470733a2f2f636f6465636f762e696f2f6769746875622f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f636f7665726167652e7376673f6272616e63683d6d6173746572)](https://codecov.io/github/Hammerspoon/hammerspoon?branch=master)
[![Downloads current release](https://camo.githubusercontent.com/6ddd625999826b9436ba8dfda7872697cbe33a93b42668563d8fec75630e0469/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f6c61746573742f746f74616c2e737667)](https://github.com/Hammerspoon/hammerspoon/releases)
[![Downloads all releases](https://camo.githubusercontent.com/d96d206320ee016a13854acb8f606b0276f7886ff24e9336f7e1bbbead6a80e2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2f746f74616c2e7376673f6d61784167653d32353932303030)](https://github.com/Hammerspoon/hammerspoon/releases)
[![Latest tag](https://camo.githubusercontent.com/4db7cd41adf93b9876fc868bdb13be57054bffc7a3b7f66fd324569e4022fac7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7461672f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2e737667)](https://github.com/Hammerspoon/hammerspoon/tags)
[![Latest release](https://camo.githubusercontent.com/92956660a29d5f072a573d93e9087ca517c1711e02baf6b5db8cd920f5d9d666/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f48616d6d657273706f6f6e2f68616d6d657273706f6f6e2e737667)](https://github.com/Hammerspoon/hammerspoon/releases/latest)

Discord: [Click to join](https://discord.gg/vxchqkRbkR)

This is a tool for powerful automation of OS X. At its core, Hammerspoon is just a bridge between the operating system and a Lua scripting engine.

What gives Hammerspoon its power is a set of extensions that expose specific pieces of system functionality, to the user. With these, you can write Lua scripts to control many aspects of your OS X environment.

* Download the [latest release](https://github.com/Hammerspoon/hammerspoon/releases/latest)
* Drag `Hammerspoon.app` from your `Downloads` folder to `Applications`

* `brew install hammerspoon --cask`

Out of the box, Hammerspoon does nothing - you will need to create `~/.hammerspoon/init.lua` and fill it with useful code. There are several resources which can help you:

What is the history of the project?
-----------------------------------

Hammerspoon is a fork of [Mjolnir](https://github.com/mjolnirapp/mjolnir). Mjolnir aims to be a very minimal application, with its extensions hosted externally and managed using a Lua package manager. We wanted to provide a more integrated experience.

What is the future of the project?
----------------------------------

Our intentions for Hammerspoon broadly fall into these categories:

* Ever wider coverage of system APIs in Extensions
* Tighter integration between extensions
* Smoother user experience