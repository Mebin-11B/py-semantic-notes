---
title: "Tailscale state file encryption no longer enabled by default"
url: https://tailscale.com/changelog
clipped: 2026-06-17 02:02:09
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tailscale state file encryption no longer enabled by default](https://tailscale.com/changelog)

## Digest Summary
Tailscale 1.42.0 is the final release supporting Windows 7, Windows 8, Windows Server 2008, and Windows Server 2012; later versions will not install on these systems, though security updates for 1.42.0 are promised through at least 31 May 2024. macOS 10.13 users are advised to upgrade directly to version 1.44.0.

Key changes across platforms:
- **All platforms:** Added `tailscale serve reset` command to clear current serve configuration; internal DNS handling revised for mixed global and private DNS servers.
- **Linux:** Added SSH login support on systems lacking the `getent` utility.
- **Windows:** Switched to a new application‑signing certificate valid through 2025; notification icons refreshed.
- **macOS:** Updated Sparkle updater frequency; Taildrop now delivers incomplete files.
- **iOS:** “Delete Account” button now redirects to the admin panel; improved memory handling to stay below the 50 MiB limit.
- **Unraid:** Added support for Unraid as a NAS platform, comparable to Synology and QNAP.
- **Kubernetes:** Introduced support for `priorityClassName`.

## Discussion Summary
The discussion centers on Tailscale’s decision to disable node‑state encryption and TPM attestation by default. Engineers explain the change was driven by frequent TPM failures on diverse hardware, which created heavy support load and unexpected breakages. Users express disappointment, citing the feature’s security value and describing the default off‑switch as a foot‑gun that caused crashes, while also seeking assurance that the issue will be resolved and the option re‑enabled. Overall sentiment combines technical justification with frustration over lost protection and implementation inconvenience.

---

## Full Article

Note: This is the last release to support the following operating systems:

• Microsoft Windows 7  
• Microsoft Windows 8  
• Microsoft Windows Server 2008  
• Microsoft Windows Server 2012

Tailscale releases after 1.42.0 will no longer install on these operating systems, though we expect to maintain forward compatibility and critical security updates for 1.42.0 with future releases until at least May 31, 2024.

Note: Do not install this version of the Tailscale client on macOS 10.13. Upgrade to version 1.44.0 instead.

###### All platforms

* [`tailscale serve reset`](https://tailscale.com/kb/1242/tailscale-serve/) command to clear out the current
  serve configuration
* Changed: Update internal DNS handling to better support mixtures of global and private DNS
  servers

###### Linux

* SSH login on platforms which lack `getent`

###### Windows

*Note: This release switches to a new application signing certificate, which is valid through 2025.*

* Notification icons are updated

###### macOS

* Update Sparkle to check more regularly
* Taildrop delivery of incomplete files

###### iOS

* **Delete Account** button to redirect to the admin panel
* Better handle memory management to avoid hitting 50 MByte memory limit

###### Unraid

* Support Unraid as a NAS platform similar to how Synology and QNAP are handled

###### Kubernetes

* Support for `priorityClassName`