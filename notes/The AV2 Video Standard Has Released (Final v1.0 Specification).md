---
title: "The AV2 Video Standard Has Released (Final v1.0 Specification)"
url: https://av2.aomedia.org
clipped: 2026-06-17 00:55:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AV2 Codec
  - Video Compression
  - Alliance for Open Media
  - AOMedia Video Model
  - Streaming Media
  - Hardware Acceleration
related:
  - "[[SANA-WM, a 2.6B open-source world model for 1-minute 720p video]]"
  - "[[Try text scaling support in Chrome Canary]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Alliance for Open Media releases the AV2 video coding specification v1.0.0, promising enhanced compression efficiency and optimized multi-stream delivery.
>
> **Key points:**
> - AV2 builds on AV1 to provide superior compression, reducing bitrates for streaming, broadcasting, and conferencing.
> - Features support for AR/VR applications, split-screen multi-program delivery, and improved screen content handling.
> - Accompanied by the official AOMedia Video Model (AVM) reference software tagged v1.0.0.
> - Comments note that widespread hardware acceleration is not expected until 2028–2030, making current implementation CPU-intensive.
>
> **Concept links:** [[AV2 Codec]], [[Video Compression]], [[Alliance for Open Media]], [[AOMedia Video Model]], [[Streaming Media]], [[Hardware Acceleration]]
>
> **Suggested connections:**
> - [[SANA-WM, a 2.6B open-source world model for 1-minute 720p video]] — related media encoding technologies.
> - [[Try text scaling support in Chrome Canary]] — related web standards and browser feature releases.
<!-- ai-summary:end -->

# [The AV2 Video Standard Has Released (Final v1.0 Specification)](https://av2.aomedia.org)

## Digest Summary
AV2 is the next‑generation video coding specification from the Alliance for Open Media, extending AV1 to achieve higher compression efficiency and lower bitrate delivery for streaming, broadcasting, and real‑time conferencing. The specification defines the full bitstream syntax, semantics, and decoding processes required for conformance and includes support for AR/VR, split‑screen multi‑program delivery, enhanced screen‑content handling, and a broader visual‑quality range. Version 1.0.0 is the current released specification, accompanied by the AOMedia Video Model (AVM) reference implementation tagged v1.0.0. Supporting assets include a downloadable PDF of the complete document, extracted lookup tables from section 9 provided as C header files, and an interactive syntax browser for sections 5 and 6 with navigation, search, and copy features. An earlier development draft labeled “v13” is retained for historical reference only.

## Discussion Summary
The comments convey a mixed view of AV2, noting that its current encoder performance makes it impractical and that widespread adoption is unlikely until hardware acceleration appears around 2028‑2030. Efficiency improvements of roughly 20‑30 % are acknowledged, but the primary advantage is seen as multi‑stream capability for VR, live sports, and separate alpha channels. Skepticism is expressed about AVIF’s lossless quality compared with JPEG XL and WebP, while there is anticipation for Apple TV support and concern about ongoing patent disputes.

---

## Full Article

About AV2
---------

**AV2** is the next-generation video coding specification from the Alliance for Open Media (AOMedia). Building on the foundation of AV1, AV2 is engineered to provide superior compression efficiency, enabling high-quality video delivery at significantly lower bitrates. It is optimized for the evolving demands of streaming, broadcasting, and real-time video conferencing.

This specification serves as the definitive technical reference for AV2 implementations. It outlines the bitstream syntax, semantics, and decoding processes required to ensure full conformance.

AV2 provides enhanced support for AR/VR applications, split-screen delivery of multiple programs, improved handling of screen content, and an ability to operate over a wider visual quality range.

To assist implementers, the **AOMedia Video Model (AVM)** serves as the official reference software.

Available Versions
------------------

The AV2 Bitstream & Decoding Process Specification, version 1.0.0, with corresponding AVM reference software.

An earlier development draft, superseded by v1.0.0. The "v13" label denotes a
working-draft milestone and does not indicate a version newer than 1.0.0.
Retained here for reference.

Using the Specification
-----------------------

### Full Specification

The complete AV2 coding specification document includes all sections from scope and definitions
through annexes. It provides comprehensive coverage of the format, syntax, semantics, and decoding process.

### PDF Version

A self-contained PDF of the complete v1.0.0 specification is available for download and offline reference.

### Additional Tables

The Additional Tables are extracted lookup tables from section 9 as C header files, useful for implementation reference.

### Syntax Browser

The syntax browser provides a specialized view of Sections 5 (Syntax Structures) and
6 (Semantics) in a split-pane interface. Features include:

* Side-by-side view of syntax definitions and their semantics
* Clickable syntax elements for easy navigation
* Search functionality across both sections
* Copy-to-clipboard for syntax structures

### Reference Software

The reference software, known as AVM, corresponding to this version of the specification is the [v1.0.0](https://github.com/AOMediaCodec/avm/tree/v1.0.0) tag.