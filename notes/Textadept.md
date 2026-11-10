---
title: "Textadept"
url: https://orbitalquark.github.io/textadept/
clipped: 2026-06-17 01:36:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Textadept](https://orbitalquark.github.io/textadept/)

## Digest Summary
Textadept is a fast, minimalist, cross‑platform text editor aimed at programmers. It is implemented in C, C++ and Lua and runs on Windows 10+ (64‑bit/ARM), macOS 13+, Linux (Qt 5/GTK 3 GUI or ncurses terminal) and BSD, delivering self‑contained executables that require no installation. Core features include support for over 100 languages, multiple carets and selections, unlimited split views, highly configurable key bindings (including language‑specific keys, chains and modes), generic and language‑specific nested snippets, and shell‑command integration for building and testing. Nearly every editor component can be scripted or extended with Lua, and the application has no internet connectivity.

Pre‑built binaries bundle required runtimes (Qt on Windows/macOS). Optional extra modules can be installed in ~/.textadept/modules and loaded via Lua’s require() in the preferences file. Building from source needs CMake 3.22+, a C/C++ compiler, and at least one UI toolkit (Qt 5.15+, GTK 2.24+, or ncurses). The MIT‑licensed project provides a manual (F1) and Lua API reference (Shift + F1).

## Discussion Summary
The comments express overall approval of TextAdept’s lightweight, fast performance and Qt‑based UI, highlighting its Lua extensibility and open‑source code as strengths. Users note the appeal of its split‑view capability but point out the lack of an automatic temporary‑file save feature and limited documentation on its GUI widget implementation. Comparisons to similar editors such as Geany, Kate, NotepadNext and Lite XL appear, with suggestions to explore Lua APIs for additional functionality while acknowledging the broader value of open‑source text editors.

---

## Full Article

Textadept
=========

Textadept is a fast, minimalist, and remarkably extensible cross-platform text editor for programmers.

Quick links: [Download](https://orbitalquark.github.io/textadept/#download) | [Manual](https://orbitalquark.github.io/textadept/manual.html) | [Lua API Docs](https://orbitalquark.github.io/textadept/api.html) | [Project Page](https://github.com/orbitalquark/textadept)

[![windows](https://orbitalquark.github.io/textadept/assets/images/windows.png)](https://orbitalquark.github.io/textadept/assets/images/windows.png)
[![macos](https://orbitalquark.github.io/textadept/assets/images/macos.png)](https://orbitalquark.github.io/textadept/assets/images/macos.png)

[![linux](https://orbitalquark.github.io/textadept/assets/images/linux.png)](https://orbitalquark.github.io/textadept/assets/images/linux.png)
[![terminal](https://orbitalquark.github.io/textadept/assets/images/terminal.png)](https://orbitalquark.github.io/textadept/assets/images/terminal.png)

Features
--------

* Traditional desktop application written in a combination of C, C++, and [Lua](https://lua.org).
* Runs on Windows, macOS, Linux, and BSD.
* Self-contained executables – no installation necessary.
* User-friendly graphical and terminal interfaces with sensible defaults.
* Support for over 100 programming languages.
* Multiple carets and selections.
* Unlimited split views.
* Configurable key bindings, including language-specific keys, key chains, and key modes.
* Snippets, both generic and language-specific, and support for nested snippets.
* Invoke shell commands for running code, building projects, and executing tests.
* Almost every aspect of the editor can be scripted, extended, and customized with Lua.
* Does not connect to the internet – *it’s just a text editor!*

[![textadept](https://orbitalquark.github.io/textadept/assets/images/textadept.png)](https://orbitalquark.github.io/textadept/assets/images/textadept.png)

Requirements
------------

Textadept’s pre-built binaries require the following:

* Windows 10+ (64-bit or ARM)
* macOS 13+
* Linux: [Qt](https://www.qt.io) 5 or [GTK](https://gtk.org) 3 for the GUI version, and [ncurses](https://invisible-island.net/ncurses/ncurses.html) for the terminal version.

You can [compile](https://orbitalquark.github.io/textadept/#compile) Textadept from source for use with different UI library versions,
such as Qt 6 and GTK 2.24.

**Note:** Lua and other [third-party dependencies](https://orbitalquark.github.io/textadept/manual.html#technologies) are compiled into the application itself,
and a Qt runtime is distributed with Windows and macOS builds.

Download
--------

You can download pre-built binaries for various platforms, as well as source code from the
links below.

A list of all released versions is [here](https://github.com/orbitalquark/textadept/releases) along with their release notes.

**Note:** while Textadept contains plenty of built-in productivity tools, some extra features and
functionality are available as optional modules in the “Extra modules” links above. This includes:

[![lsp](https://orbitalquark.github.io/textadept/assets/images/lsp.png)](https://orbitalquark.github.io/textadept/assets/images/lsp.png)
[![diff](https://orbitalquark.github.io/textadept/assets/images/diff.png)](https://orbitalquark.github.io/textadept/assets/images/diff.png)

Install and Use
---------------

Simply unpack the pre-built binary archive anywhere you have permission to and run one of the following executables:

| Platform | GUI version | Terminal version |
| --- | --- | --- |
| Windows | *textadept.exe* | *textadept-curses.exe* |
| macOS | *Textadept.app*  *ta* (shell script) | *Textadept.app/Contents/MacOS/textadept-curses* |
| Linux | *textadept* (Qt version)  *textadept-gtk* (GTK version) | *textadept-curses* |

**macOS Note:** if you get a notice that Textadept “is damaged and can’t be opened,” you will
need to remove the quarantine attribute from the app by running the following command in your
terminal: `xattr -d com.apple.quarantine /path/to/Textadept.app`.

The “Help > Show Manual” menu item, or the `F1` keyboard shortcut opens Textadept’s comprehensive
user manual. There is also an [online version](https://orbitalquark.github.io/textadept/manual.html). The manual covers all of Textadept’s
main features, including installation, usage, configuration, theming, scripting, and compiling
from source.

The “Help > Show LuaDoc” menu item, or the `Shift+F1` keyboard shortcut opens Textadept’s extensive
API reference for users interested in scripting the editor. There is also an [online version](https://orbitalquark.github.io/textadept/api.html).

If you downloaded the optional set of modules, unpack it into the *.textadept/* directory in
your home folder (keeping the top-level *modules/* directory intact). You could instead unpack
it into Textadept’s directory (thus merging the two *modules/* directories), but this is not
recommended, as it may make upgrading more difficult.

**Note:** Textadept generally does not auto-load modules. To use any of modules from the optional
set, select the “Edit > Preferences”, use Lua’s `require()` function for each module to load,
save the file, and restart Textadept. For example:

```
require('lsp')
require('file_diff')
require('spellcheck')
```

[![preferences](https://orbitalquark.github.io/textadept/assets/images/settings.png)](https://orbitalquark.github.io/textadept/assets/images/settings.png)

Compile
-------

Compiling Textadept from source requires the following:

* [CMake](https://cmake.org) 3.22+
* A C and C++ compiler, such as:
* A UI toolkit (at least one of the following):
  + [Qt](https://www.qt.io) 5.15+ development libraries for the GUI version
  + [GTK](https://gtk.org) 2.24+ development libraries for the GUI version
  + [ncurses](https://invisible-island.net/ncurses/ncurses.html)(w) development libraries (wide character support) for the terminal version
* Unix `patch` command

Basic procedure:

1. Configure CMake by pointing it to Textadept’s source directory (where *CMakeLists.txt* is),
   specify a directory to build in, and optionally specify a directory to install to. CMake will
   determine what UI toolkits are available and fetch third-party build dependencies.
     
   [![cmake](https://orbitalquark.github.io/textadept/assets/images/compile.png)](https://orbitalquark.github.io/textadept/assets/images/compile.png)
2. Build Textadept.
3. Either copy the built binaries to Textadept’s source directory or use CMake to install it.

For example:

```
cmake -S . -B build_dir -D CMAKE_BUILD_TYPE=RelWithDebInfo \
	-D CMAKE_INSTALL_PREFIX=build_dir/install
cmake --build build_dir -j # compiled binaries are in build_dir/
cmake --install build_dir # self-contained installation is in build_dir/install/
```

**Note:** if you would like to build the nightly development version of Textadept, enable the
`NIGHTLY` option during the configuration phase (e.g. `-D NIGHTLY=1`).

The “[Compiling](https://orbitalquark.github.io/textadept/manual.html#compiling)” section of the manual contains more information about this process.

Support
-------

Textadept is an open-source project, released under the MIT License.

You can contact me personally at code att foicica.com.

[![lines of code](https://orbitalquark.github.io/textadept/assets/images/loc.png)](https://orbitalquark.github.io/textadept/assets/images/loc.png)