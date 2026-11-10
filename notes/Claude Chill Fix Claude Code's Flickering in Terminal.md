---
title: "Claude Chill: Fix Claude Code's Flickering in Terminal"
url: https://github.com/davidbeesley/claude-chill
clipped: 2026-06-17 01:55:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Claude Chill: Fix Claude Code's Flickering in Terminal](https://github.com/davidbeesley/claude-chill)

## Digest Summary
The GitHub repository davidbeesley/claude‑chill displays an access‑restriction notice (“You can’t perform that action at this time.”). The page includes a series of badge images whose alt texts reveal key metadata: a continuous‑integration (CI) badge, an MIT‑license badge, and platform badges for Linux, macOS, and Windows, indicating the project targets those operating systems. A Rust badge denotes the implementation language. Additional badges reference three social‑media handles: @davidbeesley, @claude, and @mulfyx, likely the author and related accounts. No further code, documentation, or functional description is present in the scraped content.

## Discussion Summary
Comments express widespread frustration with an ongoing flickering problem in Claude Code that remains unresolved, noting its negative impact on terminal scrolling and formatting. Users criticize Anthropic’s decision not to open‑source the project, suspecting poor code quality, while also acknowledging recent community fixes that reduce the issue and expressing gratitude for those improvements. Opinions are divided between disappointment over the prolonged bug and optimism about contributions that enhance usability, with a general desire for a permanent resolution.

---

## Full Article

[![CI](https://github.com/davidbeesley/claude-chill/actions/workflows/ci.yml/badge.svg)](https://github.com/davidbeesley/claude-chill/actions/workflows/ci.yml)
[![License: MIT](https://camo.githubusercontent.com/08cef40a9105b6526ca22088bc514fbfdbc9aac1ddbf8d4e6c750e3a88a44dca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667)](https://github.com/davidbeesley/claude-chill/blob/master/LICENSE)
[![Version](https://camo.githubusercontent.com/0f828c67fd44b6160081563af04b40977ec0e8a0ee7c4c557f63f69ce5c06a81/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e312e342d626c7565)](https://camo.githubusercontent.com/0f828c67fd44b6160081563af04b40977ec0e8a0ee7c4c557f63f69ce5c06a81/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e312e342d626c7565)
[![Linux](https://camo.githubusercontent.com/cc5b5a35a7692922bcc26c9bf4618440bab7d08028902d13774772ce260ab41f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d737570706f727465642d677265656e)](https://camo.githubusercontent.com/cc5b5a35a7692922bcc26c9bf4618440bab7d08028902d13774772ce260ab41f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e75782d737570706f727465642d677265656e)
[![macOS](https://camo.githubusercontent.com/be5e68576ae4e3209fa508531c7dffae1095514c75275619ce079b7ad227b5e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d737570706f727465642d677265656e)](https://camo.githubusercontent.com/be5e68576ae4e3209fa508531c7dffae1095514c75275619ce079b7ad227b5e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d61634f532d737570706f727465642d677265656e)
[![Windows](https://camo.githubusercontent.com/64bcda52ad249d962625ff80a991de71b7589bc759de13ea2b64c77e04569f60/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57696e646f77732d756e737570706f727465642d726564)](https://camo.githubusercontent.com/64bcda52ad249d962625ff80a991de71b7589bc759de13ea2b64c77e04569f60/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f57696e646f77732d756e737570706f727465642d726564)
[![Rust](https://camo.githubusercontent.com/2e68e93283f79a11a0af69c57016856a55712032f997102c496052a6764d8074/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d323032342d6f72616e6765)](https://camo.githubusercontent.com/2e68e93283f79a11a0af69c57016856a55712032f997102c496052a6764d8074/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d323032342d6f72616e6765)

A PTY proxy that tames Claude Code's massive terminal updates using VT-based rendering.

Claude Code uses synchronized output to update the terminal atomically. It wraps output in sync markers (`\x1b[?2026h` ... `\x1b[?2026l`) so the terminal renders everything at once without flicker.

The problem: Claude Code sends *entire* screen redraws in these sync blocks - often thousands of lines. Your terminal receives a 5000-line atomic update when only 20 lines are visible. This causes lag, flicker, or jitters in the terminal, making for a poor user experience.

claude-chill sits between your terminal and Claude Code:

1. **Intercepts sync blocks** - Catches those massive atomic updates
2. **VT-based rendering** - Uses a VT100 emulator to track screen state and renders only the differences
3. **Preserves history** - Accumulates content in a buffer for lookback
4. **Enables lookback** - Press a key to pause Claude and view the full history buffer

```
cargo install --git https://github.com/davidbeesley/claude-chill
```

Or, if you've cloned the repository locally:

```
cargo install --path crates/claude-chill
```

```
claude-chill claude
claude-chill -- claude --verbose   # Use -- for command flags
```

```
$ claude-chill --help
A PTY proxy that tames Claude Code's massive terminal updates

Usage: claude-chill [OPTIONS] <COMMAND> [ARGS]...

Arguments:
  <COMMAND>  Command to run (e.g., "claude")
  [ARGS]...  Arguments to pass to the command

Options:
  -H, --history <HISTORY_LINES>
          Max lines stored for lookback (default: 100000)
  -k, --lookback-key <LOOKBACK_KEY>
          Key to toggle lookback mode, quote to prevent glob expansion (default: "[ctrl][6]")
  -a, --auto-lookback-timeout <AUTO_LOOKBACK_TIMEOUT>
          Auto-lookback timeout in ms, 0 to disable (default: 15000)
  -h, --help
          Print help
  -V, --version
          Print version
```

```
# Basic usage
claude-chill claude

# Pass arguments to claude
claude-chill -- claude --verbose

# Custom history size
claude-chill -H 50000 claude

# Custom lookback key
claude-chill -k "[f12]" claude

# Disable auto-lookback (see below)
claude-chill -a 0 claude

# Combine options with claude arguments
claude-chill -H 50000 -a 0 -- claude --verbose
```

Press `Ctrl+6` (or your configured key) to enter lookback mode:

> **macOS Note:** Some Mac terminals don't send control characters for `Ctrl+number` keys.`Ctrl+Shift+6` (i.e., `Ctrl+^`) will work by default, or the lookback key can be customized.

1. **Claude pauses** - Output from Claude is cached, input is blocked
2. **History dumps** - The full history buffer is written to your terminal
3. **Scroll freely** - Use your terminal's scrollback to review everything
4. **Exit** - Press the lookback key again or `Ctrl+C` to resume

When you exit lookback mode, any cached output is processed and the current state is displayed.

After `auto_lookback_timeout_ms` (default 15 seconds) of idle (no user input), the full history is automatically dumped to your terminal so you can scroll back without pressing any keys. This continues to re-dump every `auto_lookback_timeout_ms` while idle. This is useful for reviewing Claude's output after it finishes working.

**Note:** The auto-lookback causes a brief screen flicker during the transition as it clears the screen and writes the history buffer. Disable with `-a 0` or adjust the timeout with `-a 30000` (30 seconds).

Config file location:

* **Linux**: `~/.config/claude-chill.toml`
* **macOS**: `~/Library/Application Support/claude-chill.toml`

```
history_lines = 100000           # Max lines stored for lookback
lookback_key = "[ctrl][6]"       # Key to toggle lookback mode
refresh_rate = 20                # Rendering FPS
auto_lookback_timeout_ms = 15000 # Auto-lookback after 15s idle (0 to disable)
```

Note: History is cleared on full screen redraws, so lookback shows output since Claude's last full render.

Modern terminals like Kitty, Ghostty, and WezTerm support the [Kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) which encodes keys differently than legacy terminals.

claude-chill automatically tracks Kitty protocol state by monitoring the escape sequences passing through the proxy. When Claude Code enables Kitty mode, claude-chill switches to expecting Kitty-encoded key sequences for the lookback key. When Claude Code disables it, claude-chill switches back to legacy mode. This happens transparently with no configuration needed.

`[modifier][key]` - Examples: `[f12]`, `[ctrl][g]`, `[ctrl][shift][j]`

Modifiers: `[ctrl]`, `[shift]`, `[alt]`

Keys: `[a]`-`[z]`, `[f1]`-`[f12]`, `[pageup]`, `[pagedown]`, `[home]`, `[end]`, `[enter]`, `[tab]`, `[space]`, `[esc]`

**Note:** Quote the key value on the command line to prevent shell glob expansion: `-k "[ctrl][7]"`

`Ctrl+6` sends 0x1E (ASCII RS), a control character not frequently used by terminals, signals, or shells. Avoid `Ctrl+letter` hotkeys - terminals can't distinguish `Ctrl+J` from `Ctrl+Shift+J`.

**macOS caveat:** Mac terminals don't send control characters for `Ctrl+number` combinations. On macOS, press `Ctrl+Shift+6` (equivalent to `Ctrl+^`) which produces the same 0x1E byte. A more portable default key may be chosen in a future release.

claude-chill creates a pseudo-terminal (PTY) and spawns Claude Code as a child process. It then acts as a transparent proxy between your terminal and Claude:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Terminal   │◄───►│ claude-chill │◄───►│  Claude Code │
│   (stdin/    │     │   (proxy)    │     │   (child)    │
│    stdout)   │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

1. **Input handling**: Keystrokes pass through to Claude, except for the lookback key which toggles lookback mode
2. **Output processing**: Scans output for sync block markers. Non-sync output passes through directly
3. **VT emulation**: Feeds output through a VT100 emulator to track the virtual screen state
4. **Differential rendering**: Compares current screen to previous and emits only the changes
5. **History tracking**: Maintains a buffer of output for lookback mode since the last full redraw
6. **Signal forwarding**: Window resize (SIGWINCH), interrupt (SIGINT), and terminate (SIGTERM) signals are forwarded to Claude

### Any System (Linux / MacOS)

```
# Install directly from GitHub
nix profile install github:davidbeesley/claude-chill

# Or run without installing
nix run github:davidbeesley/claude-chill -- --help
```

Add the following to your `flake.nix`:

```
inputs.claude-chill.url = "github:davidbeesley/claude-chill";
```

And then the following package to your environment.systemPackages or home.packages:

```
inputs.claude-chill.packages.${system}.default
```

This tool was developed for personal convenience. It works for me on Linux and macOS, but it hasn't been extensively tested across different terminals or edge cases. Don't use it to send anyone to space, perform surgery, or run critical infrastructure. If it breaks, you get to keep both pieces.

See [CONTRIBUTING.md](https://github.com/davidbeesley/claude-chill/blob/master/CONTRIBUTING.md).

MIT