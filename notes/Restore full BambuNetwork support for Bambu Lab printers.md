---
title: "Restore full BambuNetwork support for Bambu Lab printers"
url: https://github.com/FULU-Foundation/OrcaSlicer-bambulab
clipped: 2026-06-17 01:03:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - 3d printing slicers
  - printer networking
  - firmware customization
related:
  - "[[3D Printing Slicers]]"
  - "[[Printer Networking]]"
  - "[[Firmware Customization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** OrcaSlicer-bambulab is a custom fork that restores full BambuNetwork remote internet connectivity for Bambu Lab 3D printers without restricting users to LAN-only mode.
>
> **Key points:**
> - Bypasses LAN-only restrictions to allow users to control their Bambu Lab printers remotely over the internet.
> - Requires Windows users to enable Windows Subsystem for Linux (WSL 2) and Virtual Machine Platform via command line beforehand.
> - Linux users can run the utility out-of-the-box with a standard installation process.
> - Community discussions voice significant frustration over Bambu Lab's mandatory cloud authentication policies, citing security and user privacy concerns.
>
> **Concept links:** [[3D Printing Slicers]], [[Printer Networking]], [[Firmware Customization]], [[WSL2 Virtualization]], [[Cloud Authentication]], [[Open Source Slicers]]
>
> **Suggested connections:**
> - [[3D Printing Slicers]] — software programs that convert 3D digital models into printing instructions.
> - [[Printer Networking]] — methodologies for connecting and orchestrating hardware printing devices over local or cloud networks.
<!-- ai-summary:end -->

# [Restore full BambuNetwork support for Bambu Lab printers](https://github.com/FULU-Foundation/OrcaSlicer-bambulab)

## Digest Summary
The repository provides a version of OrcaSlicer that re-enables full BambuNetwork connectivity for Bambu Lab printers, allowing remote operation over the internet rather than LAN‑only. Windows users must install WSL 2: run the commands `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` and `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`, then restart before launching Orca Studio. Linux installations require only the standard setup. Development is ongoing, and the author recommends using the BMCU firmware, which is available in their other repositories. The page includes an OrcaSlicer logo image.

## Discussion Summary
The comments express widespread dissatisfaction with Bambu Lab’s shift to mandatory cloud authentication, emphasizing users’ desire for simultaneous local and cloud access that the current system does not provide. Many view the change as a reaction to backlash rather than a technical necessity, raising concerns about security, data privacy, and potential corporate espionage. Skepticism about the company’s motives—such as data collection or model training—is common, while a few remarks note the inconvenience and compare the situation to broader tech‑industry control tactics.

---

## Full Article

![OrcaSlicer logo](https://github.com/FULU-Foundation/OrcaSlicer-bambulab/raw/main/resources/images/OrcaSlicer.png)

This version of OrcaSlicer restores full BambuNetwork support for Bambu Lab printers.
-------------------------------------------------------------------------------------

You are not limited to LAN only.  
It works over the internet just like before, through BambuNetwork, with full functionality for normal use and printing.

Windows requires WSL 2.

Before first launch, open Command Prompt or PowerShell as Administrator and run:

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Restart Windows, then launch Orca Studio.

On Linux, a normal installation is enough.

Work in progress.

I also encourage you to use BMCU.

You can find BMCU firmware in my repositories.