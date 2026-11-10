---
title: "Do_not_track"
url: https://donottrack.sh/
clipped: 2026-06-17 01:08:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Do_not_track](https://donottrack.sh/)

## Digest Summary
The text highlights that many command‑line tools, SDKs, and frameworks enable telemetry or usage reporting by default, each requiring a distinct environment variable to opt out (e.g., DOTNET_CLI_TELEMETRY_OPTOUT, GATSBY_TELEMETRY_DISABLED, HOME‑BREW_NO_ANALYTICS). It proposes a unified environment variable—**DO_NOT_TRACK=1**—to express a user’s intent to disable all forms of tracking, including ad tracking, usage reporting, telemetry, crash reporting, and any non‑essential network requests. Users are instructed to add `export DO_NOT_TRACK=1` (or the equivalent syntax for their shell) to their configuration files (e.g., ~/.bashrc, ~/.zshrc, fish config, PowerShell). For developers, the recommendation is to check for this variable and, when set to 1, disable any telemetry, respecting it alongside existing opt‑out mechanisms and ideally shifting to an opt‑in model.

## Discussion Summary
The comments express strong disapproval of default‑opt‑in telemetry, characterizing it as a dark‑pattern that burdens users with opting out via numerous environment variables or DNS blocklists. Contributors suggest technical workarounds such as setting DO_NOT_TRACK‑style flags, using network namespaces, or maintaining comprehensive opt‑out lists, while also arguing for legal safeguards that would require explicit consent. Opinions diverge on effectiveness: some view automated blocking as practical, others deem it insufficient without enforceable standards, but the consensus favors protecting privacy through mandatory opt‑in rather than permissive opt‑out.

---

## Full Article

DO\_NOT\_TRACK
A standard for respecting user privacy in software
=================================================================

The Problem
-----------

Many CLI tools, SDKs, and frameworks collect telemetry data by default.
Each one has its own way to opt out:

| Tool | Opt-out method |
| --- | --- |
| .NET | `DOTNET_CLI_TELEMETRY_OPTOUT=1` Copy |
| AWS SAM CLI | `SAM_CLI_TELEMETRY=0` Copy |
| Azure CLI | `AZURE_CORE_COLLECT_TELEMETRY=0` Copy |
| Gatsby | `GATSBY_TELEMETRY_DISABLED=1` Copy |
| Go | `go telemetry off` Copy |
| Google Cloud SDK | `gcloud config set disable_usage_reporting true` Copy |
| Homebrew | `HOMEBREW_NO_ANALYTICS=1` Copy |
| Netlify CLI | `netlify --telemetry-disable` Copy |
| Syncthing | `STNOUPGRADE=1` Copy |

You get the idea. There are too many, and they are all different.

The Proposal
------------

A single, standard environment variable that clearly and unambiguously
expresses a user's wish to opt out of **any** of the following:

* Ad tracking
* Usage reporting, anonymous or not
* Telemetry
* Crash reporting
* *Non-essential-to-functionality* requests to the creator of the software or third-party

We just want local software.

`export DO_NOT_TRACK=1`
  

Copy to clipboard

Add the line above to your shell configuration file so it applies
to all your terminal sessions:

| Shell | File | Syntax |
| --- | --- | --- |
| Bash | `~/.bashrc` Copy | `export DO_NOT_TRACK=1` Copy |
| Zsh | `~/.zshrc` Copy | `export DO_NOT_TRACK=1` Copy |
| Fish | `~/.config/fish/config.fish` Copy | `set -x DO_NOT_TRACK 1` Copy |
| PowerShell | `$PROFILE` Copy | `$env:DO_NOT_TRACK = "1"` Copy |
| Windows (CMD) | System Environment Variables | `setx DO_NOT_TRACK 1` Copy |

For Software Authors
--------------------

If you develop tools that collect telemetry, analytics, or make
non-essential network requests, please check for this variable:

* If `DO_NOT_TRACK` is set to `1`, disable all tracking
* Respect the variable alongside your existing opt-out mechanisms
* Consider making telemetry opt-in rather than opt-out

---

See Also
--------