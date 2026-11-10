---
title: "Show HN: Homebrew 6.0.0"
url: https://brew.sh/2026/06/11/homebrew-6.0.0/
clipped: 2026-06-17 00:48:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - package management
  - supply chain security
  - sandboxing
  - homebrew
  - ruby dsl
  - open source development
related:
  - "[[Package Management]]"
  - "[[Supply Chain Security]]"
  - "[[Sandboxing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Homebrew 6.0.0 is released with a new tap-trust security framework, Linux Bubblewrap sandboxing, a default internal JSON API, and parallelized bundle installs.
>
> **Key points:**
> - A new "tap trust" security model prevents untrusted third-party taps from running arbitrary Ruby code on the client machine without explicit approval.
> - The internal JSON API becomes the default metadata delivery mechanism, speeding up startup times and deprecating the old repo tap syncing patterns.
> - Linux installations gain Bubblewrap sandboxing for build, test, and post-installation phases, matching macOS's existing sandbox design.
> - The experimental Rust frontend project (`brew-rs`) was archived after benchmarks showed it only improved simple cached bottle queries, redirecting focus to optimizing Ruby and I/O routines.
>
> **Concept links:** [[Package Management]], [[Supply Chain Security]], [[Sandboxing]], [[Homebrew]], [[Ruby DSL]], [[Open Source Development]]
>
> **Suggested connections:**
> - [[Package Management]] — The primary software vertical of Homebrew across macOS, Linux, and Windows WSL.
> - [[Supply Chain Security]] — Highlighted by tap-trust and sandbox controls to prevent remote exploit delivery.
> - [[Sandboxing]] — Confinement mechanism isolating formula execution steps from the host OS.
<!-- ai-summary:end -->


# [Show HN: Homebrew 6.0.0](https://brew.sh/2026/06/11/homebrew-6.0.0/)

## Digest Summary
Homebrew 6.0.0 introduces several core changes: a **tap‑trust** model that requires explicit trust for third‑party taps before evaluating their Ruby code, with new `brew tap` and `brew trust` commands and JSON‑v1 support; the **internal JSON API** becomes the default, consolidating metadata into a single download and deprecating `HOMEBREW_USE_INTERNAL_API`. Linux now uses a **Bubblewrap sandbox** for build, test, and post‑install phases, mirroring macOS sandbox behavior. `brew bundle` gains parallel formula installation, npm/krew/cargo/uv cleanup, Windows winget integration, and new flags for describing and disabling bundle types. Performance is improved by faster startup, ~30 % quicker `brew leaves`, and parallel bottle‑tab fetching. Initial support for **macOS 27 (Golden Gate)** is added. An **install‑steps DSL** expresses common pre‑/post‑install actions as literal data, reducing Ruby evaluation at install time. Documentation, security advisories, and supply‑chain security measures are updated, and the project notes ongoing volunteer‑driven development and donation options.

## Discussion Summary
Comments express widespread appreciation for Homebrew’s longevity, ease of use, and cross‑platform utility, with many users citing it as their primary tool for installing software on macOS and Linux. Several contributors acknowledge alternative managers such as Mise, Nix, and MacPorts, but most remain loyal while highlighting desired improvements: better pinning, rollback, bandwidth limits, cooldown periods, and clearer trust mechanisms. Concerns are raised about forced upgrades, loss of Intel‑Mac support, and dependency handling. Donation willingness is noted, and users request clearer documentation and stability without sacrificing flexibility.

---

## Full Article

Today, I’m proud to announce Homebrew 6.0.0.
The most significant changes since 5.1.0 are a new tap trust security mechanism, the new faster, smaller, default internal Homebrew JSON API, sandboxing on Linux, better defaults informed by our user survey, many `brew bundle` improvements, improved performance and initial support for macOS 27 (Golden Gate).

### ✨ Highlights since 5.1.0

#### 🔐 Tap trust

Homebrew 6.0.0 introduces tap trust. A third-party tap can contain arbitrary, unsandboxed Ruby that runs on your machine, so Homebrew now requires taps (and tap-qualified formulae and casks) to be explicitly trusted before their code is evaluated or run. This reduces the risk from malicious or compromised taps while leaving the official Homebrew taps trusted by default. See the new [Tap-Trust documentation](https://docs.brew.sh/Tap-Trust) for details.

* Homebrew [enforces initial tap trust so untrusted taps are flagged before their code runs](https://github.com/Homebrew/brew/pull/22470), [trusts qualified tap items before install](https://github.com/Homebrew/brew/pull/22621), [stops auto-tapping untrusted taps](https://github.com/Homebrew/brew/pull/22599), [pins tap allow, forbid and trust lists to remotes](https://github.com/Homebrew/brew/pull/22590) and [uses tap trust when evaluating all formulae and casks](https://github.com/Homebrew/brew/pull/22476).
* [`brew tap` gains commands for managing tap trust](https://github.com/Homebrew/brew/pull/22472), can [trust a tap by its remote URL](https://github.com/Homebrew/brew/pull/22611), [`brew trust` adds a `--json=v1` flag](https://github.com/Homebrew/brew/pull/22624) and [`brew tap-info` adds a `trusted` field](https://github.com/Homebrew/brew/pull/22613).
* [`brew bundle` honours the `trusted:` option](https://github.com/Homebrew/brew/pull/22594) and [`brew bundle dump` records trusted bundle entries](https://github.com/Homebrew/brew/pull/22528), [marking custom-remote taps as trusted](https://github.com/Homebrew/brew/pull/22625).
* [docs.brew.sh has new pages, including Tap-Trust](https://docs.brew.sh/Tap-Trust), explaining Homebrew’s new tap trust model, and [Homebrew trusts taps in test-bot](https://github.com/Homebrew/brew/pull/22497).

#### ⚡ Default internal JSON API

The **internal JSON API** is [now the default](https://github.com/Homebrew/brew/pull/22546), [advancing](https://github.com/Homebrew/brew/pull/22367) the smaller API that Homebrew [re-enabled](https://github.com/Homebrew/brew/pull/22042) and [turned on for developers](https://github.com/Homebrew/brew/pull/22226) recently. It combines all Homebrew’s metadata into a single download, so `brew` updates faster and talks to the network less. It was opt-in via `HOMEBREW_USE_INTERNAL_API` since 5.0.0; that variable is now deprecated (see below).

#### 🐧 Linux sandbox

The **[Linux Bubblewrap sandbox](https://github.com/Homebrew/brew/pull/22240)** aligns Linux with macOS, where build, test and postinstall phases already run sandboxed. It is [on by default for developers](https://github.com/Homebrew/brew/pull/22370), Homebrew [moved its macOS sandbox logic](https://github.com/Homebrew/brew/pull/22238) to share code, [improved Linux sandbox behaviour](https://github.com/Homebrew/brew/pull/22315) (with [Homebrew/homebrew-core setting the sandbox env in CI](https://github.com/Homebrew/homebrew-core/pull/283172)), [hardened sandboxed install phases](https://github.com/Homebrew/brew/pull/22413), [sandboxed cask executable hooks](https://github.com/Homebrew/brew/pull/22406), [allowed logs in the build sandbox](https://github.com/Homebrew/brew/pull/22539), [installed Bubblewrap on hosted Ubuntu](https://github.com/Homebrew/brew/pull/22458) and [skips sandbox setup for syntax-only jobs](https://github.com/Homebrew/brew/pull/22507).

#### ⚙️ Better defaults

#### 📦 `brew bundle`

* `brew bundle` gains many improvements, most notably [parallel formula installation](https://github.com/Homebrew/brew/pull/21891) that now [runs jobs automatically by default](https://github.com/Homebrew/brew/pull/22545), plus [npm](https://github.com/Homebrew/brew/pull/21820) and [krew](https://github.com/Homebrew/brew/pull/21802) extensions, [wider cleanup support](https://github.com/Homebrew/brew/pull/22395) and, on Windows, [`winget` support](https://github.com/Homebrew/brew/pull/22397).
* Homebrew [adds cleanup support to npm, cargo, go and uv extensions](https://github.com/Homebrew/brew/pull/21883) and [asks before removing during cleanup](https://github.com/Homebrew/brew/pull/22453).
* Homebrew runs [`brew bundle krew` via `kubectl-krew` directly](https://github.com/Homebrew/brew/pull/22328), [respects `CARGO_HOME` and friends for `cargo`](https://github.com/Homebrew/brew/pull/21795), [adds a `--describe` flag to `brew bundle add`](https://github.com/Homebrew/brew/pull/21797) and [tries `mas install` before falling back to `mas get`](https://github.com/Homebrew/brew/pull/22361).
* Homebrew [adds bundle type disable flags](https://github.com/Homebrew/brew/pull/22452), [improves check guidance](https://github.com/Homebrew/brew/pull/22265) and [checks formula link status](https://github.com/Homebrew/brew/pull/22412).
* Homebrew [serialises formula locks](https://github.com/Homebrew/brew/pull/22297), [makes non-core DSLs a single file](https://github.com/Homebrew/brew/pull/21721), [removes description comments from `brew bundle/remover`](https://github.com/Homebrew/brew/pull/21735) and [avoids parsing the output of `brew services list`](https://github.com/Homebrew/brew/pull/21830).
* [`brew bundle` performs npm installs more securely.](https://github.com/Homebrew/brew/pull/22405)

#### 🏎️ Performance

Homebrew is faster across the board, with [startup performance tweaks](https://github.com/Homebrew/brew/pull/21734), [a ~30% faster `brew leaves`](https://github.com/Homebrew/brew/pull/21911), [parallelised bottle tab fetching on upgrade](https://github.com/Homebrew/brew/pull/22118) and [less work loading Ruby libraries at startup](https://github.com/Homebrew/brew/pull/22133).

#### 🍎 macOS 27 (Golden Gate)

[Homebrew adds initial support for macOS 27 (Golden Gate)](https://github.com/Homebrew/brew/pull/22592).

### 🔮 Upcoming changes

### 🔒 Security

#### 🚨 Security advisories

Homebrew published three security advisories:

#### 🛡️ Other security improvements

### 🗑️ Deprecations

### 🎁 Features

#### 🖥️ Casks

#### 💻 Operating system support

#### 🚰 Taps

#### ℹ️ `brew info` and `brew tap-info`

#### 🆕 New commands, flags and output

#### 🧊 Cooldowns, livecheck and bumping

#### ⬇️ Downloads and fetching

#### 🛎️ Services

#### 🧪 Formulae and packaging

#### 🪜 Install steps framework

* The **[install steps framework](https://github.com/Homebrew/brew/pull/22371)** expresses common postinstall, preflight and postflight behaviour as ordered, literal-only DSL data that is exposed through the JSON APIs. Where a formula or cask only does simple file preparation, it no longer needs to download and evaluate a Ruby file at install time. Homebrew adds [formula install steps](https://github.com/Homebrew/brew/pull/22372), [cask install steps](https://github.com/Homebrew/brew/pull/22373), [an audit for formula install steps](https://github.com/Homebrew/brew/pull/22474), [install step rebuild actions](https://github.com/Homebrew/brew/pull/22513), [rebuild step methods](https://github.com/Homebrew/brew/pull/22554), [rebuild step RuboCop checks](https://github.com/Homebrew/brew/pull/22515) and [an audit of cask flight step conversions](https://github.com/Homebrew/brew/pull/22411); `homebrew/core` and `homebrew/cask` adopt the new DSLs ([`post_install_steps`](https://github.com/Homebrew/homebrew-core/pull/285885), [`postinstall`](https://github.com/Homebrew/homebrew-core/pull/285474) and [flight steps](https://github.com/Homebrew/homebrew-cask/pull/267046)). In `homebrew/core` and `homebrew/cask` this covers a large share of `post_install` and `*flight` blocks (creating directories, touching markers, moving and symlinking files), with more operation types planned.

#### 🔀 Other changes

#### 🧹 Internals, typing and refactors

#### 📚 Documentation

Finally:

* Homebrew is a non-profit project run entirely by volunteers, not employees. We need your funds to pay for software, hardware and hosting around continuous integration and future improvements to the project. Every donation will be spent on making Homebrew better for our users. Please consider a regular donation through [GitHub Sponsors](https://github.com/sponsors/Homebrew), [OpenCollective](https://opencollective.com/homebrew#category-CONTRIBUTE) and [Patreon](https://www.patreon.com/homebrew).
* [Homebrew/brew has no open issues](https://github.com/Homebrew/brew/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen+) at the time of writing 🎉.
* Homebrew has a brand new [brew.sh](https://brew.sh) homepage style.
* [BrewUI is Homebrew’s upcoming official graphical interface](https://github.com/Homebrew/brewui). It’s not ready for general use yet.
* The `brew-rs` experiment in moving parts of Homebrew’s Ruby frontend to Rust [has concluded](https://github.com/Homebrew/brew-rs): benchmarks showed Homebrew’s Rust frontend only ahead on narrow, already-cached bottle fetches, not on representative full installs (pouring bottles, linking, writing metadata and health checks), so the performance focus has moved back to Ruby and to starting useful network and disk I/O sooner. We’ve [added an FAQ entry](https://github.com/Homebrew/brew/pull/22658) explaining all of this. Our numbers come from honest, fully-compatible comparisons. Not all unofficial Homebrew frontends seem to apply the same rigor to their benchmarks, compatability or security: your mileage with those may vary.
* Homebrew is increasingly a **“package manager for everywhere”**: Homebrew is recommended in [Microsoft’s Windows Developer Config for WSL comfort](https://github.com/microsoft/WindowsDeveloperConfig#-wsl-comfort), works well on [Bazzite](https://bazzite.gg) and now [supports `winget` in `brew bundle`](https://github.com/Homebrew/brew/pull/22397) as a Windows-only feature.
* The Homebrew team is aware of the supply-side security issues with other package managers. We’ve taken various steps to mitigate these risks for our users, some existing (e.g. macOS sandboxing, human review on all changes, environment filtering, all package maintainers are Homebrew maintainers), some new (e.g. Linux sandboxing, sandboxing reads of sensitive locations, cooldown from riskier ecosystems). We will continue to monitor the supply-side security landscape and take further steps as needed. See the new [Supply Chain Security documentation](https://docs.brew.sh/Supply-Chain-Security) we’ve [added](https://github.com/Homebrew/brew/pull/22657) for details.
* Homebrew has [documented the principles behind our AI and LLM usage rules](https://github.com/Homebrew/brew/pull/22656) in a new [Responsible AI Usage](https://docs.brew.sh/Responsible-AI-Usage) page.
* [Homebrew has joined the Open Source Resistance and you should too.](https://ossresistance.com)

Thanks to all our hard-working volunteer maintainers, contributors, sponsors and supporters for getting us this far.

### Latest Posts

* [5.1.0](https://brew.sh/2026/03/10/homebrew-5.1.0/)
  10 Mar 2026

  Homebrew 5.1.0 has been released. Homebrew’s most significant changes since 5.0.0 are expanded brew bundle support, brew version-install, new -full formula handling an...
* [5.0.0](https://brew.sh/2025/11/12/homebrew-5.0.0/)
  12 Nov 2025

  Today, I’d like to announce Homebrew 5.0.0. The most significant changes since 4.6.0 are download concurrency by default, official support for Linux ARM64/AArch64, tim...
* [4.6.0](https://brew.sh/2025/08/05/homebrew-4.6.0/)
  05 Aug 2025

  Today, I’d like to announce Homebrew 4.6.0. The most significant changes since 4.5.0 are opt-in concurrent downloads with HOMEBREW\_DOWNLOAD\_CONCURRENCY, preliminary ma...
* [4.5.0](https://brew.sh/2025/04/29/homebrew-4.5.0/)
  29 Apr 2025

  Today, I’d like to announce Homebrew 4.5.0. The most significant changes since 4.4.0 are major improvements to brew bundle/services, preliminary Linux support for cask...