---
title: "Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering"
url: https://github.com/OlaProeis/Ferrite
clipped: 2026-06-17 02:00:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering](https://github.com/OlaProeis/Ferrite)

## Digest Summary
Ferrite is a lightweight, high‑performance text editor targeting Markdown, JSON, YAML, and TOML files. Implemented in Rust using the egui framework, it delivers a native, responsive UI with multiple viewing options: a raw code pane, a rendered preview, a split view combining both, and a distraction‑free Zen mode. The project is released under the MIT license. The repository’s front‑end displays typical GitHub UI elements, but access to certain actions is currently restricted (“You can’t perform that action at this time”). Image assets reference the MIT license badge, the Rust language logo, and screenshots of the editor’s raw, rendered, split, and Zen modes, illustrating its core functionality and interface design.

## Discussion Summary
The comment notes that existing Markdown editors like Typora already provide similar functionality, but lack built‑in support for JSON and YAML, highlighting a perceived gap as LLMs generate increasingly complex, parseable text with embedded diagrams. It questions whether mermaid rendering is implemented natively in Rust or relies on a JavaScript interpreter, and mentions difficulties encountered when rendering Markdown documents containing numerous mermaid diagrams, expressing a desire for a more reliable and robust rendering solution.

---

## Full Article

**English** | [简体中文](https://github.com/OlaProeis/Ferrite/blob/master/README.zh-CN.md)

A fast, lightweight text editor for Markdown, JSON, YAML, and TOML files. Built with Rust and egui for a native, responsive experience.

> ⚠️ **Platform Note:** Ferrite is developed and tested on **Windows** and **Linux**. macOS support is experimental. If you encounter issues, please [report them](https://github.com/OlaProeis/Ferrite/issues).

**🛡️ Code Signing & Antivirus**

Starting with v0.2.6.1, **all Windows releases are digitally signed** with a certificate from [SignPath Foundation](https://signpath.org). This means:

* **Windows SmartScreen** recognizes the publisher — no more "Unknown publisher" warnings
* **Antivirus false positives** are significantly reduced thanks to the trusted code signature
* **Integrity verification** — you can verify that the binary hasn't been tampered with

Older unsigned builds may still trigger antivirus detections. This was caused by:

* **Live Pipeline feature**: Uses `cmd.exe /C` on Windows for shell commands, which ML-based detection can misidentify
* **Rust compilation patterns**: Rust binaries can trigger heuristic detections due to unique characteristics

We've addressed this through code signing, build profile adjustments (disabled symbol stripping, speed optimization), and reporting to Microsoft's Security Intelligence portal.

If Windows Defender quarantines Ferrite:

1. **Upgrade**: Download the latest signed release from [GitHub Releases](https://github.com/OlaProeis/Ferrite/releases)
2. **Verify the signature**: Right-click `ferrite.exe` → Properties → Digital Signatures → should show "SignPath Foundation"
3. **Check VirusTotal**: Upload the file to [VirusTotal](https://www.virustotal.com) — signed builds should show clean results

Ferrite does **NOT** access passwords, browser data, or make unsolicited network connections. The only network access is the manual "Check for Updates" button (Settings → About), which contacts the GitHub Releases API when you click it. The application only accesses files you explicitly open.


**🍎 macOS Installation & Gatekeeper**

**GitHub Release** `.dmg` / `.tar.gz` builds are packaged as `Ferrite.app` but are **not** signed with an Apple Developer ID and are **not** notarized (CI limitation). **Gatekeeper**, especially on **macOS 15.x (Sequoia / 15.6+)**, may block or warn on first launch—see [GitHub #130](https://github.com/OlaProeis/Ferrite/issues/130) and the workarounds below.

📖 **Full troubleshooting:** [docs/install/macos.md](https://github.com/OlaProeis/Ferrite/blob/master/docs/install/macos.md)

### Option 1: Homebrew (often smoothest)

```
brew tap olaproeis/ferrite
brew install --cask ferrite
```

Homebrew typically avoids quarantine friction compared to raw GitHub downloads.

### Option 2: DMG / tar.gz from GitHub Releases + workaround

1. Download from [Releases](https://github.com/OlaProeis/Ferrite/releases):
   * **Apple Silicon:** `ferrite-macos-arm64.dmg` or `.tar.gz`
   * **Intel:** `ferrite-macos-x64.dmg` or `.tar.gz`
2. Copy `Ferrite.app` to **Applications** (or another folder you prefer).
3. **First launch — pick one:**
   * **Terminal (most reliable):** `xattr -dr com.apple.quarantine /Applications/Ferrite.app` — use the real path if the app is not under `/Applications`.
   * **Finder:** Control-click `Ferrite.app` → **Open** → **Open** (may **not** work on every macOS 15.x configuration).
   * **System Settings → Privacy & Security:** after a blocked launch, use **Open Anyway** if shown.

Apple expects apps distributed outside the Mac App Store to be signed with a **Developer ID** certificate and **notarized**. Ferrite is open source—you can [audit the code](https://github.com/OlaProeis/Ferrite) and [build from source](https://github.com/OlaProeis/Ferrite/blob/master/docs/building.md)—but paid enrollment and CI wiring are still pending for GitHub-hosted macOS builds.

🤖 AI-Assisted Development
-------------------------

This project is 100% AI-generated code. All Rust code, documentation, and configuration was written by Claude (Anthropic) via [Cursor](https://cursor.com) with MCP tools.

**About the AI workflow**

* **Product direction** — Deciding what to build and why
* **Testing** — Running the app, finding bugs, verifying features
* **Review** — Reading generated code, understanding what it does
* **Orchestration** — Managing the AI workflow effectively

1. **Idea refinement** — Discuss concepts with multiple AIs (Claude, Perplexity, Gemini Pro)
2. **PRD creation** — Generate requirements using [Task Master](https://github.com/task-master-ai/task-master)
3. **Task execution** — Claude Opus handles implementation (preferring larger tasks over many subtasks)
4. **Session handover** — Structured prompts maintain context between sessions
5. **Human review** — Every handover is reviewed; direction adjustments made as needed

📖 **Full details:** [AI Development Workflow](https://github.com/OlaProeis/Ferrite/blob/master/docs/ai-workflow/ai-development-workflow.md)

The actual prompts and documents used to build Ferrite are public:

This transparency is intentional — I want others to learn from (and improve upon) this approach.

[![Ferrite Demo](https://github.com/OlaProeis/Ferrite/raw/master/assets/screenshots/demo.gif)](https://github.com/OlaProeis/Ferrite/blob/master/assets/screenshots/demo.gif)

| Raw Editor | Split View | Zen Mode |
| --- | --- | --- |
| [Raw Editor](https://github.com/OlaProeis/Ferrite/blob/master/assets/screenshots/raw-dark.png) | [Split View](https://github.com/OlaProeis/Ferrite/blob/master/assets/screenshots/split-dark.png) | [Zen Mode](https://github.com/OlaProeis/Ferrite/blob/master/assets/screenshots/zen-dark.png) |

> ✨ **v0.3.0 (Latest):** **eframe / egui 0.34.2** platform refresh. **PDF + themed HTML export**. **Executable code blocks** (`▶ Run`). **Rendered edit session** (one-click WYSIWYG block switching). **Split-view scroll sync**. **User accent color**. **Mermaid** insert toolbar + validation + flowchart polish. **Phosphor icons**. **Session recovery** hardening. **Quick note workflow**. See [CHANGELOG.md](https://github.com/OlaProeis/Ferrite/blob/master/CHANGELOG.md) for full details.

> 🛠️ **Coming in v0.3.1:** LSP (diagnostics panel + hover/complete), YouTube embeds, Mermaid second wave, multi-window, CSV editing, and GitHub HTML parity. See [ROADMAP.md](https://github.com/OlaProeis/Ferrite/blob/master/ROADMAP.md) and [prd-v0.3.1.md](https://github.com/OlaProeis/Ferrite/blob/master/docs/ai-workflow/prds/prd-v0.3.1.md).

> 📦 **v0.2.6 Highlights:** Custom Editor Engine with virtual scrolling (80MB file uses ~80MB RAM), Multi-Cursor Editing, Code Folding, IME/CJK input improvements.

* **WYSIWYG Markdown Editing** - Edit markdown with live preview, **one-click block switching** between headings, paragraphs, lists, and table cells in rendered mode, click-to-edit formatting, and syntax highlighting
* **Executable Code Blocks** - Run shell or Python fenced blocks from rendered/split preview (`▶ Run`); inline ANSI output, timeout, and Stop (opt-in via Settings; first-run consent)
* **Multi-Format Support** - Native support for Markdown, JSON, CSV, YAML, and TOML files
* **Multi-Encoding Support** - Auto-detect and preserve file encodings (UTF-8, Latin-1, Shift-JIS, Windows-1252, GBK, and more)
* **Tree Viewer** - Hierarchical view for JSON/YAML/TOML with inline editing, expand/collapse, and path copying
* **Find & Replace** - Search with regex support and match highlighting
* **Go to Line (Ctrl+G)** - Quick navigation to specific line number
* **Undo/Redo** - Full undo/redo support per tab

* **Split View** - Side-by-side raw editor and rendered preview with resizable divider; both panes are fully editable; optional **live scroll sync** (minimap **Sync** / **2-way** controls)
* **Zen Mode** - Distraction-free writing with centered text column

* **Syntax Highlighting** - Full-file syntax highlighting for 100+ languages (Rust, Python, JavaScript, Go, TypeScript, PowerShell, and more)
* **Code Folding** - Fold/unfold regions with gutter indicators (▶/▼) for headings, code blocks, and lists; collapsed content is hidden
* **Semantic Minimap** - Navigation panel with clickable header labels, content type indicators, and text density bars (switchable to VS Code-style pixel view)
* **Multi-Cursor Editing** - Ctrl+Click to add multiple cursors; type, delete, and navigate at all positions simultaneously
* **Bracket Matching** - Highlight matching brackets `()[]{}<>` and emphasis pairs `**` `__`
* **Auto-close Brackets & Quotes** - Type `(`, `[`, `{`, `"`, or `'` to get matching pair; selection wrapping supported
* **Duplicate Line (Ctrl+Shift+D)** - Duplicate current line or selection
* **Move Line Up/Down (Alt+↑/↓)** - Rearrange lines without cut/paste
* **Smart Paste for Links** - Select text then paste URL to create `[text](url)` markdown link
* **Drag & Drop Images** - Drop images into editor to auto-save to `./assets/` and insert markdown link
* **Table of Contents** - Generate/update TOC from headings with `<!-- TOC -->` block (Ctrl+Shift+U)
* **Snippets** - Text expansions like `;date` → current date, `;time` → current time, plus custom snippets
* **Auto-Save** - Configurable auto-save with temp-file safety
* **Line Numbers** - Optional line number gutter
* **Configurable Line Width** - Limit text width for readability (80/100/120 or custom)
* **Custom Font Selection** - Choose preferred fonts for editor and UI; important for CJK regional glyph preferences
* **Keyboard Shortcut Customization** - Rebind shortcuts via settings panel

Native rendering of 11 diagram types directly in the preview:

* Flowchart, Sequence, Pie, State, Mindmap
* Class, ER, Git Graph, Gantt, Timeline, User Journey
* **Insert templates** - Format toolbar → **Insert → Mermaid…** for starter snippets per diagram type
* **Inline validation** - Parse errors in preview with squiggles on broken `mermaid` blocks in the raw editor
* **Flowchart polish** - Improved edge routing, extra shapes, `style` / classDef support; state diagrams support fork/join and history nodes

> **v0.3.0 Mermaid update:** Insert toolbar, syntax help (F1), inline validation, flowchart edge-routing and layout fixes, and state-diagram pseudostates. Complex diagrams may still differ from mermaid.js. See [ROADMAP.md](https://github.com/OlaProeis/Ferrite/blob/master/ROADMAP.md) for planned parity work.

* **Native Table View** - View CSV and TSV files in a formatted table with fixed-width column alignment
* **Rainbow Column Coloring** - Alternating column colors for improved readability
* **Delimiter Detection** - Auto-detect comma, tab, semicolon, and pipe separators
* **Header Row Detection** - Intelligent detection and highlighting of header rows

* **Workspace Mode** - Open folders with file tree, quick switcher (Ctrl+P), and search-in-files (Ctrl+Shift+F)
* **Workspace File Index** - Ctrl+P and Search in Files scan the **entire workspace** in the background (not only expanded folders in the tree)
* **Quick Note Workflow** - Pathless scratch tabs: quit without a save dialog by default; closing a tab still prompts; unsaved notes persist via session recovery (Settings → Files)
* **Git Integration** - Visual status indicators (modified, added, untracked, ignored) with auto-refresh on save, focus, and file changes
* **Session Persistence** - Restore open tabs, cursor positions, and scroll offsets on restart; hardened crash recovery with identity checks and disk-conflict banner

* **Integrated Terminal** - Multiple instances with shell selection (PowerShell, CMD, WSL, bash)
* **Tiling & Splitting** - Create complex 2D grids with horizontal and vertical splits
* **Smart Maximize** - Temporarily maximize any pane to focus on work (Ctrl+Shift+M)
* **Layout Persistence** - Save and load your favorite terminal arrangements to JSON files
* **Theming & Transparency** - Custom color schemes (Dracula, etc.) and background opacity
* **Drag-and-Drop Tabs** - Reorder terminals with visual feedback
* **AI-Ready** - Visual "breathing" indicator when terminal is waiting for input (perfect for AI agents)

* **Light & Dark Themes** - Beautiful themes with runtime switching; **custom Ferrite accent color** (Settings / Welcome) for headings, selection, tabs, and chrome
* **Document Outline & Statistics** - Navigate with outline panel; tabbed statistics showing word count, reading time, heading/link/image counts
* **Export & Print** - Export to **PDF** or **themed HTML** (options dialog, Mermaid as SVG); **print preview** opens a temp PDF in the in-app viewer; copy as HTML
* **Formatting Toolbar** - Quick access to bold, italic, headings, lists, links, Mermaid insert, and more
* **Phosphor Icons** - Consistent icon font across ribbon, toolbar, panels, and preview controls
* **Live Pipeline** - Pipe JSON/YAML content through shell commands (for developers)
* **Custom Window** - Borderless window with custom title bar and resize handles
* **Recent Files & Folders** - Click filename in status bar to access recently opened files and workspace folders
* **CJK Paragraph Indentation** - First-line indentation options for Chinese (2 chars) and Japanese (1 char) writing conventions

Download the latest release for your platform from [GitHub Releases](https://github.com/OlaProeis/Ferrite/releases).

| Platform | Download | Notes |
| --- | --- | --- |
| **Windows** | `ferrite-windows-x64.msi` | Recommended - full installer with Start Menu |
| Windows | `ferrite-portable-windows-x64.zip` | Portable - extract anywhere, run from USB |
| **Linux (Debian/Ubuntu)** | `ferrite-editor_amd64.deb` | For Debian, Ubuntu, Mint, Pop!\_OS |
| **Linux (Fedora/RHEL)** | `ferrite-editor.x86_64.rpm` | For Fedora, RHEL, CentOS, Rocky |
| Linux | `ferrite-linux-x64.tar.gz` | Universal - works on any distro |
| **macOS (Apple Silicon)** | `ferrite-macos-arm64.dmg` | Recommended - drag to Applications (M1/M2/M3) |
| macOS (Apple Silicon) | `ferrite-macos-arm64.tar.gz` | Alternative - contains Ferrite.app bundle |
| **macOS (Intel)** | `ferrite-macos-x64.dmg` | Recommended - drag to Applications |
| macOS (Intel) | `ferrite-macos-x64.tar.gz` | Alternative - contains Ferrite.app bundle |


**Windows Installation**

#### MSI Installer (Recommended)

Download `ferrite-windows-x64.msi` and run it. This will:

* Install Ferrite to `C:\Program Files\Ferrite`
* Add Start Menu shortcut with icon
* Enable easy uninstall via Windows Settings
* Store settings in `%APPDATA%\ferrite\`

Download `ferrite-portable-windows-x64.zip` and extract anywhere. The zip includes:

* `ferrite.exe` - the application
* `portable/` - folder for all your settings
* `README.txt` - quick start guide

**True portable mode:** All configuration, sessions, and data are stored in the `portable` folder next to the executable. Nothing is written to `%APPDATA%` or the Windows registry. Perfect for USB drives or trying Ferrite without installation.


**Linux Installation**

#### Debian/Ubuntu/Mint (.deb)

```
# Download the .deb file, then install with:
sudo apt install ./ferrite-editor_amd64.deb

# Or using dpkg:
sudo dpkg -i ferrite-editor_amd64.deb
```

#### Fedora/RHEL/CentOS (.rpm)

```
# Download the .rpm file, then install with:
sudo dnf install ./ferrite-editor.x86_64.rpm

# Or using rpm:
sudo rpm -i ferrite-editor.x86_64.rpm
```

Both .deb and .rpm packages will:

* Install Ferrite to `/usr/bin/ferrite`
* Add desktop entry (appears in your app menu)
* Register file associations for `.md`, `.json`, `.yaml`, `.toml` files
* Install icons for the system

[![Ferrite on AUR](https://camo.githubusercontent.com/c46e2dcead20a141247060d3ff1917b331360b74bf454cfa91f7f86f9fd330c1/68747470733a2f2f696d672e736869656c64732e696f2f6175722f76657273696f6e2f666572726974653f6c6162656c3d66657272697465)](https://aur.archlinux.org/packages/ferrite/)
[![Ferrite-bin on AUR](https://camo.githubusercontent.com/4d4a3a196ac510373be24f61d55b03c3d7705d0b750e1fc1a29f2c21b80fd695/68747470733a2f2f696d672e736869656c64732e696f2f6175722f76657273696f6e2f666572726974652d62696e3f6c6162656c3d666572726974652d62696e)](https://aur.archlinux.org/packages/ferrite-bin/)

Ferrite is available on the [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository):

```
# Release package
yay -Sy ferrite

# Binary package
yay -Sy ferrite-bin
```

#### Nix / NixOS (official flake)

```
# Run Ferrite directly from GitHub (no install)
nix run github:OlaProeis/Ferrite

# Drop into a shell that exposes ferrite in PATH
nix shell github:OlaProeis/Ferrite
```

From a local clone:

```
# Build package output
nix build .#ferrite
./result/bin/ferrite

# Enter development shell (Rust toolchain + system deps)
nix develop
```

```
tar -xzf ferrite-linux-x64.tar.gz
./ferrite
```

**Keyboard not working on Ubuntu 24.04 LTS (GNOME/Wayland)**

Keyboard input does not work when Ferrite is launched under GNOME on Wayland (Ubuntu 24.04 LTS and similar).
As a workaround, launch Ferrite with `WAYLAND_DISPLAY` unset to force X11 mode:

```
env -u WAYLAND_DISPLAY ferrite
```

To make this permanent for your desktop launcher, create a user-level desktop entry override:

```
mkdir -p ~/.local/share/applications
cp /usr/share/applications/ferrite-editor.desktop ~/.local/share/applications/ferrite-editor.desktop
```

Then edit `~/.local/share/applications/ferrite-editor.desktop` and change the `Exec` line to:

```
Exec=env -u WAYLAND_DISPLAY ferrite %F
```


**macOS Installation**

#### DMG Installer (Recommended)

Download the `.dmg` for your Mac:

* **Apple Silicon** (M1/M2/M3/M4): `ferrite-macos-arm64.dmg`
* **Intel**: `ferrite-macos-x64.dmg`

Open the DMG and drag `Ferrite.app` to the **Applications** folder. Launch from Launchpad or Spotlight.

#### From tar.gz (Alternative)

```
# Apple Silicon
tar -xzf ferrite-macos-arm64.tar.gz
cp -R Ferrite.app /Applications/

# Intel
tar -xzf ferrite-macos-x64.tar.gz
cp -R Ferrite.app /Applications/
```

> **Gatekeeper (GitHub downloads):** Unsigned / non-notarized CI builds may be blocked on **macOS 15.x**. See **[docs/install/macos.md](https://github.com/OlaProeis/Ferrite/blob/master/docs/install/macos.md)** — quickest fix: `xattr -dr com.apple.quarantine /Applications/Ferrite.app` (adjust path). Tracked: [#130](https://github.com/OlaProeis/Ferrite/issues/130).


**Build from Source**

* **Rust 1.70+** - Install from [rustup.rs](https://rustup.rs/)
* **Platform-specific dependencies:**

**Nix users:** you can skip manual dependency installation and use `nix develop` from the repository root (see `flake.nix`).

**Windows:**

* Visual Studio Build Tools 2019+ with C++ workload

**Linux:**

```
# Ubuntu/Debian
sudo apt install build-essential pkg-config libgtk-3-dev libxcb-shape0-dev libxcb-xfixes0-dev

# Fedora
sudo dnf install gcc pkg-config gtk3-devel libxcb-devel

# Arch
sudo pacman -S base-devel pkg-config gtk3 libxcb
```

**macOS:**

```
# Clone the repository
git clone https://github.com/OlaProeis/Ferrite.git
cd Ferrite

# Build release version (optimized)
cargo build --release

# The binary will be at:
# Windows: target/release/ferrite.exe
# Linux/macOS: target/release/ferrite

# macOS: Create .app bundle (optional)
cargo install cargo-bundle
cargo bundle --release
# Bundle will be at: target/release/bundle/osx/Ferrite.app
```

> **macOS "Open With" Limitation:** The app bundle includes file type associations, so Ferrite appears in Finder's "Open With" menu. However, opening files this way (or by dragging files onto the app icon) is not yet supported due to [eframe/winit limitations](https://github.com/rust-windowing/winit/issues/1751). **Workaround:** Open files via Terminal: `open -a Ferrite path/to/file.md` or use File > Open within the app.

> **Development Builds:** Building from the `main` branch gives you the latest features before they're officially released. These builds are untested and may contain bugs. For stable versions, download from [GitHub Releases](https://github.com/OlaProeis/Ferrite/releases).

```
# Open a file
ferrite path/to/file.md

# Open a folder as workspace
ferrite path/to/folder/
```

**More CLI options**

```
# Run from source
cargo run --release

# Or run the binary directly
./target/release/ferrite

# Open multiple files as tabs
./target/release/ferrite file1.md file2.md

# Show version
./target/release/ferrite --version

# Show help
./target/release/ferrite --help
```

See [docs/cli.md](https://github.com/OlaProeis/Ferrite/blob/master/docs/cli.md) for full CLI documentation.

Ferrite supports three view modes for Markdown files:

* **Raw** - Plain text editing with syntax highlighting
* **Rendered** - WYSIWYG editing with rendered markdown
* **Split** - Side-by-side raw editor and live preview

Toggle between modes using the toolbar buttons or keyboard shortcuts.

| Shortcut | Action |
| --- | --- |
| `Ctrl+N` | New file |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+W` | Close tab |
| `Ctrl+P` | Quick file switcher |
| `Ctrl+F` | Find |
| `Ctrl+G` | Go to line |
| `Ctrl+,` | Open settings |


**All Keyboard Shortcuts**


| Shortcut | Action |
| --- | --- |
| `Ctrl+N` | New file |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+Shift+S` | Save as |
| `Ctrl+W` | Close tab |



| Shortcut | Action |
| --- | --- |
| `Ctrl+Tab` | Next tab |
| `Ctrl+Shift+Tab` | Previous tab |
| `Ctrl+P` | Quick file switcher (workspace) |
| `Ctrl+Shift+F` | Search in files (workspace) |



| Shortcut | Action |
| --- | --- |
| `Ctrl+Z` | Undo |
| `Ctrl+Y` / `Ctrl+Shift+Z` | Redo |
| `Ctrl+F` | Find |
| `Ctrl+H` | Find and replace |
| `Ctrl+G` | Go to line |
| `Ctrl+Shift+D` | Duplicate line |
| `Alt+↑` | Move line up |
| `Alt+↓` | Move line down |
| `Ctrl+B` | Bold |
| `Ctrl+I` | Italic |
| `Ctrl+K` | Insert link |



| Shortcut | Action |
| --- | --- |
| `F11` | Toggle fullscreen |
| `Ctrl+,` | Open settings |
| `Ctrl+Shift+[` | Fold all |
| `Ctrl+Shift+]` | Unfold all |

Terminal shortcuts are **context-aware**; they work when the terminal panel is focused.

| Shortcut | Action |
| --- | --- |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Cycle through terminal tabs |
| `Ctrl+1-9` | Switch to specific terminal tab |
| `Ctrl+Arrow Keys` | Move focus between split panes |
| `Ctrl+Shift+M` | Toggle **Maximize Pane** (Zoom) |
| `Ctrl+L` | Clear terminal screen |
| `Ctrl+Shift+C` | Copy selection / screen |
| `Ctrl+Shift+V` | Paste to terminal |
| `Ctrl+W` / `Ctrl+F4` | Close focused pane (auto-collapses splits) |
| `Double-click Tab` | Rename terminal |

Access settings via `Ctrl+,` or the gear icon. Configure appearance, editor behavior, and file handling.

**Configuration details**

Settings are stored in platform-specific locations:

* **Windows:** `%APPDATA%\ferrite\`
* **Windows Portable:** `portable\` folder next to `ferrite.exe`
* **Linux:** `~/.config/ferrite/`
* **macOS:** `~/Library/Application Support/ferrite/`

**Portable Mode (Windows):** If a `portable` folder exists next to the executable, Ferrite automatically uses it for all configuration instead of `%APPDATA%`. This makes Ferrite fully self-contained - perfect for USB drives.

Workspace settings are stored in `.ferrite/` within the workspace folder.

* **Appearance:** Theme, font family, font size, default view mode
* **Editor:** Word wrap, line numbers, minimap, bracket matching, code folding, syntax highlighting, auto-close brackets, line width
* **Files:** Auto-save, recent files history

See [ROADMAP.md](https://github.com/OlaProeis/Ferrite/blob/master/ROADMAP.md) for planned features and known issues.

Contributions are welcome! Please see [CONTRIBUTING.md](https://github.com/OlaProeis/Ferrite/blob/master/CONTRIBUTING.md) for guidelines.

Ferrite is being translated into multiple languages with help from the community.

[![Translation Status](https://camo.githubusercontent.com/03c603b523e8627431c2f4faebdf9071944281fa80b8d4bf7e5a71ce9ca49745/68747470733a2f2f686f737465642e7765626c6174652e6f72672f7769646765742f666572726974652f666572726974652d75692f6d756c74692d6175746f2e737667)](https://hosted.weblate.org/engage/ferrite/)

**[Help translate Ferrite on Weblate](https://hosted.weblate.org/engage/ferrite/)** - no coding required!

**Quick Start for Contributors**

```
# Fork and clone
git clone https://github.com/YOUR_USERNAME/Ferrite.git
cd Ferrite

# Create a feature branch
git checkout -b feature/your-feature

# Make changes, then verify
cargo fmt
cargo clippy
cargo test
cargo build

# Optional (Nix users): validate flake outputs
nix flake check

# Commit and push
git commit -m "feat: your feature description"
git push origin feature/your-feature
```

Built with Rust 1.70+, egui/eframe for GUI, comrak for Markdown parsing, ropey for rope-based text editing, and syntect for syntax highlighting.

**Full tech stack**


| Component | Technology |
| --- | --- |
| Language | Rust 1.70+ |
| GUI Framework | egui 0.28 + eframe 0.28 |
| Text Buffer | ropey 1.6 (rope data structure) |
| Markdown Parser | comrak 0.22 |
| Syntax Highlighting | syntect 5.1 + two-face 0.5 |
| Git Integration | git2 0.19 |
| Terminal PTY | portable-pty 0.8 |
| Terminal ANSI Parser | vte 0.13 |
| Encoding Detection | encoding\_rs 0.8 + chardetng 0.1 |
| Internationalization | rust-i18n 3 + sys-locale 0.3 |
| CLI Parsing | clap 4 |
| File Dialogs | rfd 0.14 |
| Clipboard | arboard 3 |
| File Watching | notify 6 |
| Fuzzy Matching | fuzzy-matcher 0.3 |
| HTTP Client | ureq 2 (update checker) |
| Hashing | blake3 1.5 (Mermaid caching) |
| Date/Time | chrono 0.4 |
| CSV Parsing | csv 1.3 |
| Color Palette | palette 0.7 |
| Font Enumeration | font-kit 0.14 |
| Allocator (Windows) | mimalloc 0.1 |
| Allocator (Unix) | tikv-jemallocator 0.6 |

This project is licensed under the MIT License - see the [LICENSE](https://github.com/OlaProeis/Ferrite/blob/master/LICENSE) file for details.

* [egui](https://github.com/emilk/egui) and eframe - Immediate mode GUI and native window integration
* [ropey](https://github.com/cessen/ropey) - Rope text buffer for large-file editing
* [comrak](https://github.com/kivikakk/comrak) - CommonMark + GFM compatible Markdown parser
* [syntect](https://github.com/trishume/syntect) and [two-face](https://github.com/CosmicHorrorDev/two-face) - Syntax highlighting and extra language definitions
* [harfrust](https://github.com/harfbuzz/harfrust) - OpenType text shaping for complex scripts
* [git2](https://github.com/rust-lang/git2-rs) - libgit2 bindings for Rust
* [portable-pty](https://github.com/wez/wezterm) and [vte](https://github.com/alacritty/vte) - Integrated terminal (PTY and ANSI parsing)
* [image](https://github.com/image-rs/image) - Raster image decoding (markdown preview and image viewer)
* [hayro](https://github.com/LaurenzV/hayro) - Pure Rust PDF rasterization (PDF viewer tabs)
* [rust-i18n](https://github.com/longbridge/rust-i18n) - Internationalization
* [Inter](https://rsms.me/inter/) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/) fonts

* [Claude](https://anthropic.com) (Anthropic) - AI assistant that wrote the code
* [Cursor](https://cursor.com) - AI-powered code editor
* [Task Master](https://github.com/eyaltoledano/claude-task-master) - AI task management for development workflows

Sponsors
--------



---

If you find Ferrite useful, consider [supporting its development](https://github.com/sponsors/OlaProeis).