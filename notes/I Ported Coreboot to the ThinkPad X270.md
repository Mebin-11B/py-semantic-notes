---
title: "I Ported Coreboot to the ThinkPad X270"
url: https://dork.dev/posts/2026-02-20-ported-coreboot/
clipped: 2026-06-17 01:40:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [I Ported Coreboot to the ThinkPad X270](https://dork.dev/posts/2026-02-20-ported-coreboot/)

## Digest Summary
Ported Coreboot/Libreboot to a ThinkPad X270 (20HM, Kaby Lake). The BIOS was dumped using an RP2040‑zero running pico‑serprog (flashprog) to back up the image and extract the Intel Management Engine (IME) and GbE sections needed for deguard processing. A capacitor was accidentally removed; schematic reference (PJ304) identified the part and it was replaced with a 10 µF 0603 component. The flash was examined with ifdtool, deguard patches applied, and a patched IME produced. Differences from the X280 required disabling Thunderbolt pins, handling the MEC1653 vs. MEC1663 controller, and adjusting GPIO definitions. Initial builds booted payloads but NVMe and Wi‑Fi were absent due to incorrect PCIe allocations; community assistance identified wrong CLKREQ assignments (CLKREQ1 instead of CLKREQ2) and an overridetree.cb issue. After correcting the CLKREQ mapping and rebuilding, GRUB and Guix booted successfully, with functional NVMe and wireless (ath9k). The changes are being prepared for upstreaming, and further integration of the wireless dongle is planned.

## Discussion Summary
The comment expresses frustration with a persistent throttling issue on the X270 when using third‑party 9‑cell batteries, noting that the system repeatedly triggers CPU_PROCHOT and drops below 1 GHz. It recounts a personal workaround involving a boot‑time script that disables thermal throttling, acknowledging its imperfection but deeming it necessary due to limited official battery availability. The author also inquires whether AI contributed to the discussion.

---

## Full Article

Loading...

You are seeing this because the administrator of this website has set up Anubis to protect the server against the scourge of AI companies aggressively scraping websites. This can and does cause downtime for the websites, which makes their resources inaccessible for everyone.

Anubis is a compromise. Anubis uses a Proof-of-Work scheme in the vein of Hashcash, a proposed proof-of-work scheme for reducing email spam. The idea is that at individual scales the additional load is ignorable, but at mass scraper levels it adds up and makes scraping much more expensive.

Ultimately, this is a placeholder solution so that more time can be spent on fingerprinting and identifying headless browsers (EG: via how they do font rendering) so that the challenge proof of work page doesn't need to be presented to users that are much more likely to be legitimate.

Please note that Anubis requires the use of modern JavaScript features that plugins like JShelter will disable. Please disable JShelter or other such plugins for this domain.