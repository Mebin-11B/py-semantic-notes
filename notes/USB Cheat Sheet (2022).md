---
title: "USB Cheat Sheet (2022)"
url: https://fabiensanglard.net/usbcheat/index.html
clipped: 2026-06-17 01:11:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - usb standards
  - hardware specifications
  - usb-c architecture
  - power delivery (pd)
  - data encoding
related:
  - "[[USB Standards]]"
  - "[[USB-C Architecture]]"
  - "[[Power Delivery (PD)]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A reference cheat sheet detailing USB generations, wire counts, connector capabilities, real-world speeds, and power delivery capacities.
>
> **Key points:**
> - Summarizes USB specifications from USB 1.1 to USB4 40Gbps, comparing marketing names, nominal rates, and actual sequential read rates.
> - Explains the "Gen A x B" naming convention, where "A" denotes speed generation and "B" represents the number of lanes bonded.
> - Breaks down wire configurations: 4 wires (half-duplex), 8 wires (one TX, one RX full-duplex), and 12 wires (two TX, two RX lanes, exclusive to USB-C).
> - Maps out USB-C features, including Configuration Channel (CC) pins for negotiation and Sideband Use (SBU) pins for alternate modes, alongside Power Delivery (PD) limits up to 240W.
>
> **Concept links:** [[USB Standards]], [[Hardware Specifications]], [[USB-C Architecture]], [[Power Delivery (PD)]], [[Data Encoding]]
>
> **Suggested connections:**
> - [[USB Standards]] — The historical progress and naming conventions of the USB specification.
> - [[USB-C Architecture]] — The interface pin mapping enabling alternate modes and multi-lane routing.
<!-- ai-summary:end -->


# [USB Cheat Sheet (2022)](https://fabiensanglard.net/usbcheat/index.html)

## Digest Summary
USB generations use the notation “Gen Ax BA” where A is the generation and B is the number of lanes. Multi‑lane systems employ lane‑striping on transmit (TX) and lane‑bonding on receive (RX). Rates quoted on packaging include encoding overhead (e.g., 8b/10b adds ~20 %); actual sequential read throughput is lower.  

Cable wiring:  
- 4‑wire cable (V BUS, GND, D+, D‑) = one half‑duplex lane.  
- 8‑wire cable adds RX⁺/RX⁻ and TX⁺/TX⁻ = two full‑duplex lanes (one up, one down).  
- 12‑wire cable provides four lanes (two up, two down).  

Connectors: USB‑A/B support 4 or 8 wires; only USB‑C has enough pins for the 12‑wire, two‑lane configuration.  

Specification timeline: USB 1.0 (1996), 1.1 (1998), 2.0 (2000), 3.0 (2008), 3.1 (2013), 3.2 (2017), 4.0 (2019).

## Discussion Summary
The comments express overall approval of the article while noting several inaccuracies and omissions, such as the definition of SBU and the absence of low‑speed specifications. Contributors repeatedly criticize USB’s confusing naming conventions and inconsistent marketing, proposing clearer labeling schemes and emphasizing the need for product listings that faithfully reflect specifications. Additional points raise interest in related standards like Thunderbolt, request more detail on connector pinouts, voltage, signaling, and power‑delivery profiles, and suggest expanding the cheat sheet to cover these areas.

---

## Full Article

May 05, 2022

USB Cheat Sheet

---

I spend time investigating a non-existing bug today because I misunderstood a USB term. So I made myself a cheat sheet. Maybe it will save time to someone.

| Marketing Name | Also Known As | Signal Mbps | Signal MiB/s | Wires | Cable |
| --- | --- | --- | --- | --- | --- |
| USB 1.1 | Full Speed | 12 Mbps | 1.5 MiB/s | 4 | 4m |
| USB 2.0 | Hi-Speed | 480 Mbps | 60 MiB/s | 4 | 4m |
| SuperSpeed USB  5Gbps | USB 3.0  USB 3.1  USB 3.2  USB 3.1 Gen 1  USB 3.2 Gen 1 | 5000 Mbps | 625 MiB/s | 8 | 3m |
| SuperSpeedPlus USB 10Gbps | USB 3.1  USB 3.2  USB 3.1 Gen 2  USB 3.2 Gen 2 | 10000 Mbps | 1250 MiB/s | 8 | 2m |
| SuperSpeedPlus USB 20Gbps | USB 3.2  USB 3.2 Gen 2x2 | 20000 Mbps | 2500 MiB/s | 12 | 1m |
| USB4 20Gbps | USB4 Gen 2×2  USB4 | 20000 Mbps | 2500 MiB/s | 12 | 0.8m |
| USB4 40Gbps | USB4 Gen 3×2  USB4 | 40000 Mbps | 5000 MiB/s | 12 | 0.8m |

Gen naming Convention, lanes, and Speed

---

USB Gen A x B  
A = Generation  
B = Num lanes used

| Name | Signal | Sig Totala | Encoding | Effective bb | Effective Bb | Real Lifec |
| --- | --- | --- | --- | --- | --- | --- |
| USB 3.2 Gen 1x1 | 5,000 Mbps | 5,000 Mbps | 8b/10b | 4,000 Mbps | 500 MiB/s | 400 MiB/s[[1]](https://fabiensanglard.net/usbcheat/index.html#footnote_1) |
| USB 3.2 Gen 1x2 | 5,000 Mbps | 10,000 Mbps | 8b/10b | 8,000 Mbps | 1,000 MiB/s | 800 MiB/s |
| USB 3.2 Gen 2x1 | 10,000 Mbps | 10,000 Mbps | 128b/132b | 9,696 Mbps | 1,212 MiB/s | 780 MiB/s[[2]](https://fabiensanglard.net/usbcheat/index.html#footnote_2) |
| USB 3.2 Gen 2x2 | 10,000 Mbps | 20,000 Mbps | 128b/132b | 19,392 Mbps | 2,424 MiB/s | 1,600 MiB/s[[4]](https://fabiensanglard.net/usbcheat/index.html#footnote_4) |
| USB 4 Gen 2x2 | 10,000 Mbps | 20,000 Mbps | 128b/132b | 19,392 Mbps | 2,424 MiB/s | 1,600 MiB/s |
| USB 4 Gen 3x2 | 20,000 Mbps | 40,000 Mbps | 128b/132b | 38,787 Mbps | 4,848 MiB/s | 2,700 MiB/s[[5]](https://fabiensanglard.net/usbcheat/index.html#footnote_5) |

**Note:** Multi-lanes systems, uses lane striping (on TX) and lane bonding (on RX).  
a - What they put on the box.  
b - Rate with encoding overhead. e.g, 8b/10b = 20%.   
c - Real life sequencial read rate.

Cables

---

 4 wires: PWR, GND, D+, D-.  
 8 wires: PWR, GND, D+, D-. RX+ , RX- , TX- , TX+.  
12 wires: PWR, GND, D+, D-, RX1+, RX1-, RX2-, RX2+, TX1+, TX1-, TX2-, TX2+.

**Note:** 1 USB lane = 1 twisted wire pair +/-.  
**Note:** 4 wires = 1 half-duplex lane, 8 wires = 2 lanes (one up, one down), and 12 wires = 4 lanes (two up, two down).

USB-A/B: Connectors 4/8 wires

---

| Type-A 4-wires | Type-A 8-wires | Type-B 4-wires | Type-B 8-wires |
| --- | --- | --- | --- |
|  |  |  |  |

USB-C: Connectors 12 wires

---

Only the USB Type-C connector has enough pins to support two lanes.

![](https://fabiensanglard.net/usbcheat/typec.svg)- CC1 and CC2 are downstream facing port (DFP) and upstream facing port (UFP) detection. Also used for power negotiation and alt mode switch.  
- SBU1 and SBU2 are **S**ideband **U**se wires, for the DisplayPort AUX channel, hot plug detection (HPD), and occasionally UART), audio.  

Charge rates / Cable types

---

| Specifications | Max. Voltage | Max. Current | Max. Power |
| --- | --- | --- | --- |
| USB 2.0 | 5V | 500mA | 2.5W |
| USB 3.0 / USB3.1 | 5V | 900mA | 4.5W |
| USB Battery Charging (BC) 1.2 | 5V | 1.5A | 7.5W |
| USB-C Current Mode (non-PD) | 5V | 3A | 15W |
| USB-C / Power Delivery (PD 1/2) | 20V | 5A | 100W |
| USB-C PD 3.1 (EPR) | 48V | 5A | 240W |

Specifications

---

[USB 1.0](https://fabiensanglard.net/usbcheat/usb1.pdf) (Jan, 1996).  
[USB 1.1](https://fabiensanglard.net/usbcheat/usb1.1.pdf) (Sep, 1998).  
[USB 2.0](https://fabiensanglard.net/usbcheat/usb2.pdf) (Apr, 2000).  
[USB 3.0](https://fabiensanglard.net/usbcheat/usb3.pdf) (Nov, 2008).  
[USB 3.1](https://fabiensanglard.net/usbcheat/usb3.1.pdf) (Jul, 2013).  
[USB 3.2](https://fabiensanglard.net/usbcheat/usb3.2.pdf) (Sep, 2017).  
[USB 4.0](https://fabiensanglard.net/usbcheat/usb4.pdf) (Aug, 2019).

References

---

---

\*