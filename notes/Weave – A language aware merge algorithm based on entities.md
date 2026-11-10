---
title: "Weave – A language aware merge algorithm based on entities"
url: https://github.com/Ataraxy-Labs/weave
clipped: 2026-06-17 01:36:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Weave – A language aware merge algorithm based on entities](https://github.com/Ataraxy-Labs/weave)

## Digest Summary
Weave is a Git merge driver that replaces line‑based merging with entity‑level semantic merging using Tree‑Sitter parsers. It parses the base, ours, and theirs versions of a file into semantic entities (functions, classes, JSON keys, etc.), matches entities by name‑type‑scope, and merges each entity independently: unchanged entities are kept, single‑side changes are applied automatically, and concurrent changes to the same entity trigger an intra‑entity 3‑way merge, producing a conflict only when the modifications are truly incompatible. This eliminates false conflicts when unrelated code is added to the same file, a common issue for multiple AI agents or developers. Benchmarks on merge commits from major open‑source repositories show 31/31 clean merges versus Git’s 15/31, with zero regressions and high human‑match rates. Weave supports TypeScript, JavaScript, Python, Go, Rust, JSON, YAML, TOML, Markdown, and falls back to line‑level merging for unsupported or large files. It consists of three components: **weave‑core** (entity extraction and merge algorithm), **weave‑driver** (Git driver binary), and **weave‑cli** (setup and preview commands). Installation involves adding a custom merge driver in `.gitattributes` and configuring Git to invoke Weave for the supported file extensions.

## Discussion Summary
The feedback expresses enthusiasm for the tool, highlighting interest in adding Ruby language support and noting perceived value even without direct experience. The commenter also inquires about the effectiveness of agents within the platform, indicating curiosity about their performance. Overall sentiment is positive and forward‑looking, focusing on desired feature expansion and functional expectations.

---

## Full Article

> **Part of the [Ataraxy Labs](https://ataraxy-labs.com) stack** — agent-native infrastructure for software development. See also: [sem](https://ataraxy-labs.com/sem) (semantic version control) · [inspect](https://github.com/Ataraxy-Labs/inspect) (semantic code review) · [opensessions](https://github.com/Ataraxy-Labs/opensessions) (tmux sidebar for coding agents).
>
> Read the manifesto: <https://ataraxy-labs.com/#thesis> · Essays: <https://ataraxy-labs.com/blogs> · LLMs: <https://ataraxy-labs.com/llms.txt>

[![weave](https://github.com/Ataraxy-Labs/weave/raw/main/assets/banner.svg)](https://github.com/Ataraxy-Labs/weave/blob/main/assets/banner.svg)

**Entity-level semantic merge driver for Git.**  
Resolves merge conflicts that Git can't by understanding code structure via tree-sitter.

[Install](https://github.com/Ataraxy-Labs/weave#install) ·
[How It Works](https://github.com/Ataraxy-Labs/weave#how-weave-fixes-this) ·
[MCP Server](https://github.com/Ataraxy-Labs/weave#mcp-server) ·
[Releases](https://github.com/Ataraxy-Labs/weave/releases/latest)

[![Release](https://camo.githubusercontent.com/15c8f4da90200772e9faba0d53b39df5df381535452f216e55f35ce16edcaecd/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f417461726178792d4c6162732f77656176653f636f6c6f723d626c7565266c6162656c3d72656c65617365)](https://github.com/Ataraxy-Labs/weave/releases/latest)
[![Homebrew](https://camo.githubusercontent.com/95c6c1b103972cbe03045d529db521fbf7607695c8909815936c3fb97db51268/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f686f6d65627265772d77656176652d6f72616e6765)](https://formulae.brew.sh/formula/weave)
[![Rust](https://camo.githubusercontent.com/b626e173c5edefe432ae8fa0c1ebd27a25ab743455f72cfb65b8c9f1220959ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d737461626c652d6f72616e6765)](https://camo.githubusercontent.com/b626e173c5edefe432ae8fa0c1ebd27a25ab743455f72cfb65b8c9f1220959ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d737461626c652d6f72616e6765)
[![Tests](https://camo.githubusercontent.com/0d0331a01c91a2bf674eb0c7b762d698303535f24a36895a744ee2ddbbb314c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74657374732d3132345f70617373696e672d627269676874677265656e)](https://camo.githubusercontent.com/0d0331a01c91a2bf674eb0c7b762d698303535f24a36895a744ee2ddbbb314c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74657374732d3132345f70617373696e672d627269676874677265656e)
[![Version](https://camo.githubusercontent.com/81bd7b28e56634b09a424e1b0dfcca6aa59ee6eba19f7548e7e9accefbf88449/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e332e302d626c7565)](https://camo.githubusercontent.com/81bd7b28e56634b09a424e1b0dfcca6aa59ee6eba19f7548e7e9accefbf88449/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d302e332e302d626c7565)
[![License](https://camo.githubusercontent.com/3921b6a636b7d3fc4db90f929b9047fb47fa4fdd6233a2b5fa60b827480fc2c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d79656c6c6f77)](https://github.com/Ataraxy-Labs/weave/blob/main/LICENSE)
[![Languages](https://camo.githubusercontent.com/dc6e6eedfa54fa604e2e29c1acc992e1e485ad4e8c3fa09601491649c441dbb1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e6775616765732d32382d626c7565)](https://camo.githubusercontent.com/dc6e6eedfa54fa604e2e29c1acc992e1e485ad4e8c3fa09601491649c441dbb1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e6775616765732d32382d626c7565)

[![Weave merge animation: two branches add different functions, git conflicts, weave merges cleanly](https://github.com/Ataraxy-Labs/weave/raw/main/assets/merge-animation.gif)](https://github.com/Ataraxy-Labs/weave/blob/main/assets/merge-animation.gif)

Git merges by comparing **lines**. When two branches both add code to the same file — even to completely different functions — Git sees overlapping line ranges and declares a conflict:

```
<<<<<<< HEAD
export function validateToken(token: string): boolean {
    return token.length > 0 && token.startsWith("sk-");
}
=======
export function formatDate(date: Date): string {
    return date.toISOString().split('T')[0];
}
>>>>>>> feature-branch
```

These are **completely independent changes**. There's no real conflict. But someone has to manually resolve it anyway.

This happens constantly when multiple AI agents work on the same codebase. Agent A adds a function, Agent B adds a different function to the same file, and Git halts everything for a human to intervene.

Weave replaces Git's line-based merge with **entity-level merge**. Instead of diffing lines, it:

1. Parses all three versions (base, ours, theirs) into semantic entities — functions, classes, JSON keys, etc. — using [tree-sitter](https://tree-sitter.github.io/)
2. Matches entities across versions by identity (name + type + scope)
3. Merges at the entity level:
   * **Different entities changed** → auto-resolved, no conflict
   * **Same entity changed by both** → attempts intra-entity merge, conflicts only if truly incompatible
   * **One side modifies, other deletes** → flags a meaningful conflict

The same scenario above? Weave merges it cleanly with zero conflicts — both functions end up in the output.

| Scenario | Git (line-based) | Weave (entity-level) |
| --- | --- | --- |
| Two agents add different functions to same file | **CONFLICT** | Auto-resolved |
| Agent A modifies `foo()`, Agent B adds `bar()` | **CONFLICT** (adjacent lines) | Auto-resolved |
| Both agents modify the same function differently | CONFLICT | CONFLICT (with entity-level context) |
| One agent modifies, other deletes same function | CONFLICT (cryptic diff) | CONFLICT: `function 'validateToken' (modified in ours, deleted in theirs)` |
| Both agents add identical function | **CONFLICT** | Auto-resolved (identical content detected) |
| Both agents add different properties to same object | **CONFLICT** | Auto-resolved |
| Different JSON keys modified | **CONFLICT** | Auto-resolved |

The key difference: Git produces false conflicts on **independent changes** because they happen to be in the same file. Weave only conflicts on **actual semantic collisions** when two branches change the same entity incompatibly.

Tested on 31 real-world merge scenarios across Python, TypeScript, Rust, Go, Java, and C:

| Tool | Clean Merges | Score |
| --- | --- | --- |
| **Weave** | **31/31** | 100% |
| Mergiraf (v0.16.3) | 26/31 | 83% |
| Git | 15/31 | 48% |

Mergiraf fails on both-add-at-end-of-file, insert-between-existing, and decorator conflict scenarios. Weave resolves all of these because it operates at entity granularity (functions, classes, methods) rather than AST node level. Full breakdown at [ataraxy-labs.github.io/weave](https://ataraxy-labs.github.io/weave/).

Tested on real merge commits from major open-source repositories. For each merge commit, we replay the merge with both Git and Weave, then compare against the human-authored result.

* **Wins**: Merge commits where Git conflicted but Weave resolved cleanly
* **Regressions**: Cases where Weave introduced errors (0 across all repos)
* **Human Match**: How often Weave's output exactly matches what the human wrote
* **Resolution Rate**: Percentage of all merge commits Weave resolved vs total attempted

| Repository | Language | Merge Commits | Wins | Regressions | Human Match | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| [git/git](https://github.com/git/git) | C | 1319 | 39 | 0 | 64% | 13% |
| [Flask](https://github.com/pallets/flask) | Python | 56 | 14 | 0 | 57% | 54% |
| [CPython](https://github.com/python/cpython) | C/Python | 256 | 7 | 0 | 29% | 13% |
| [Go](https://github.com/golang/go) | Go | 1247 | 19 | 0 | 58% | 28% |
| [TypeScript](https://github.com/microsoft/TypeScript) | TypeScript | 2000 | 65 | 0 | 6% | 23% |

Zero regressions across all repositories. Every "win" is a place where a developer had to manually resolve a false conflict that Weave handles automatically.

When a real conflict occurs, weave gives you context that Git doesn't:

```
<<<<<<< ours — function `process` (both modified)
export function process(data: any) {
    return JSON.stringify(data);
}
=======
export function process(data: any) {
    return data.toUpperCase();
}
>>>>>>> theirs — function `process` (both modified)
```

You immediately know: what entity conflicted, what type it is, and why it conflicted.

TypeScript, TSX, JavaScript, Python, Go, Rust, Java, C, C++, Ruby, C#, PHP, Swift, Kotlin, Elixir, Bash, HCL/Terraform, Fortran, Dart, Perl, OCaml, Scala, Zig, Vue, Svelte, XML, ERB, JSON, YAML, TOML, CSV, Markdown. Falls back to standard line-level merge for unsupported file types.

Or build from source (requires Rust):

```
git clone https://github.com/Ataraxy-Labs/weave
cd weave
cargo install --path crates/weave-cli
cargo install --path crates/weave-driver
```

In any Git repo:

This configures Git to use weave for all supported file types. Then use `git merge` as normal.

To revert back to normal git merging:

To set up for just yourself (without modifying `.gitattributes`), write the same supported file type rules to `.git/info/attributes` instead:

Add to your jj config (`jj config edit --user`):

```
[merge-tools.weave]
program = "weave-driver"
merge-args = ["$base", "$left", "$right", "-o", "$output", "-l", "$marker_length", "-p", "$path"]
merge-conflict-exit-codes = [1]
merge-tool-edits-conflict-markers = true
conflict-marker-style = "git"
```

Resolve conflicts with `jj resolve --tool weave`, or set as default:

```
jj config set --user ui.merge-editor "weave"
```

Dry-run a merge to see what weave would do:

```
weave-cli preview feature-branch
```

```
  src/utils.ts — auto-resolved
    unchanged: 2, added-ours: 1, added-theirs: 1
  src/api.ts — 1 conflict(s)
    ✗ function `process`: both modified

✓ Merge would be clean (1 file(s) auto-resolved by weave)
```

```
weave-core       # Library: entity extraction, 3-way merge algorithm, reconstruction
weave-driver     # Git merge driver binary (called by git via %O %A %B %L %P)
weave-cli        # CLI: `weave setup` and `weave preview`
```

Uses [sem-core](https://github.com/Ataraxy-Labs/sem) for entity extraction via tree-sitter grammars.

```
         base
        /    \
     ours    theirs
        \    /
       weave merge
```

1. **Parse** all three versions into semantic entities via tree-sitter
2. **Extract regions** — alternating entity and interstitial (imports, whitespace) segments
3. **Match entities** across versions by ID (file:type:name:parent)
4. **Resolve** each entity: one-side-only changes win, both-changed attempts intra-entity 3-way merge
5. **Reconstruct** file from merged regions, preserving ours-side ordering
6. **Fallback** to line-level merge for files >1MB, binary files, or unsupported types

[![Star History Chart](https://camo.githubusercontent.com/89adc35b38736f5ed3c6a845134fd09d46d47e2edab5076a9e7113c168f29e97/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d417461726178792d4c6162732f776561766526747970653d44617465)](https://star-history.com/#Ataraxy-Labs/weave&Date)