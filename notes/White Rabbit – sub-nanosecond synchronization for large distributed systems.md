---
title: "White Rabbit – sub-nanosecond synchronization for large distributed systems"
url: https://ohwr.org/projects/white-rabbit/
clipped: 2026-06-17 00:57:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - distributed systems
  - clock synchronization
  - open hardware
  - CERN
  - Ethernet protocols
related:
  - "[[Temporal A nine-year journey to fix time in JavaScript]]"
  - "[[Distributed Systems]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** White Rabbit is an open-hardware, Ethernet-based synchronization platform developed at CERN that achieves sub-nanosecond clock synchronization and deterministic data delivery for large distributed systems.
>
> **Key points:**
> - Delivers sub-nanosecond timing accuracy and picosecond precision across thousands of nodes separated by typical distances of up to 10 km.
> - Integrates timing synchronization and gigabit-rate reliable data transfer over the same Ethernet network interface.
> - Released as fully open-source hardware, firmware, and software, supported by commercial multi-vendor hardware manufacturers.
> - Discussion highlights the engineering behind Layer 1 physical synchronization and the utility of such precise coordination in large experimental physics and telecommunication systems.
>
> **Concept links:** [[Distributed Systems]], [[Clock Synchronization]], [[Open Hardware]], [[CERN]], [[Ethernet Protocols]], [[Precision Engineering]]
>
> **Suggested connections:**
> - [[Temporal A nine-year journey to fix time in JavaScript]] — comparing software-based representations of time and date APIs to hardware-level physical clock synchronization systems.
> - [[Distributed Systems]] — how precise physical time synchronization aids consistency models, transaction ordering, and telemetry collation in distributed networks.
<!-- ai-summary:end -->

# [White Rabbit – sub-nanosecond synchronization for large distributed systems](https://ohwr.org/projects/white-rabbit/)

## Digest Summary
White Rabbit is an open‑hardware, Ethernet‑based platform that provides sub‑nanosecond synchronization accuracy with picosecond‑level precision for large distributed systems. It enables deterministic, reliable data delivery and precise time‑tagging of measured data, while using the same network for data acquisition and transmission. Key capabilities include:

- Sub‑nanosecond timing synchronization across thousands of nodes.  
- Support for typical inter‑node distances of up to 10 km.  
- Gigabit‑rate Ethernet links offering reliable data transfer.  
- Fully open hardware, firmware, and software, allowing multi‑vendor commercial production.  

The system is intended for installations requiring precise trigger timing and coordinated data collection over extensive networks. Contact: Maciej Lipinski.

## Discussion Summary
The discussion highlights a CERN‑origin paper describing a novel Ethernet‑style link in which physical layers are synchronized at layer 1, achieving sub‑nanosecond timing over distances up to 10 km. Participants note the technical intrigue of continuous gigabit transmission and the precise clock coordination, while also observing that the implementation is not hosted on GitHub and that recruitment links on the page appear as a promotional element. The overall tone is curious and mildly appreciative of the engineering approach.

---

## Full Article

White Rabbit provides **sub-nanosecond accuracy** and picoseconds
precision of **synchronization** for large distributed systems. It also
allows for deterministic and reliable data delivery.  
White Rabbit allows you to **precision time-tag measured data** and lets
you trigger data taking in large installations while at the same time
using the same **network to transmit data**.

* sub-nanosecond synchronization
* connecting thousands of nodes
* typical distances of 10 km between nodes
* Ethernet-based gigabit rate reliable data transfer
* fully open hardware, firmware and software
* multi-vendor commercially produced
  hardware

### Contact

[Maciej Lipinski](mailto:maciej.lipinski@cern.ch)

### Tags

[Documentation](https://ohwr.org/?f=Documentation)
[White Rabbit](https://ohwr.org/?f=White+Rabbit)