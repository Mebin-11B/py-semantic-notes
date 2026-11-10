---
title: "Professional video editing, right in the browser with WebGPU and WASM"
url: https://tooscut.app/
clipped: 2026-06-17 01:29:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - webgpu
  - webassembly
  - browser applications
  - video editing
  - animation engines
related:
  - "[[WebGPU]]"
  - "[[WebAssembly]]"
  - "[[Video Editing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Tooscut is a browser-based video editor utilizing WebGPU and WASM to provide professional-grade keyframe animations and transitions.
>
> **Key points:**
> - Offers a comprehensive keyframe animation system for opacity, transforms, and effects.
> - Employs Bézier-based easing curves to allow precise, non-linear property interpolation.
> - Accelerates visual processing inside browser contexts using WebGPU rendering and WebAssembly compilation.
>
> **Concept links:** [[Webgpu]], [[Webassembly]], [[Browser Applications]], [[Video Editing]], [[Animation Engines]]
>
> **Suggested connections:**
> - [[WebGPU]] — leveraging GPU-bound parallel pipelines directly in web applications.
> - [[Video Editing]] — porting heavy video manipulation workloads from desktop tools to sandboxed web environments.
<!-- ai-summary:end -->


# [Professional video editing, right in the browser with WebGPU and WASM](https://tooscut.app/)

## Digest Summary
Tooscut’s video editor incorporates a comprehensive keyframe animation system. Users can animate any editable property by placing keyframes and applying Bézier‑based easing curves, enabling fine‑grained control over motion and transition timing. The system supports the full range of visual parameters—including geometric transforms (position, scale, rotation), opacity levels, and effect settings—each of which is fully keyframeable. By leveraging Bézier curves, the editor allows non‑linear interpolation, giving creators the ability to craft smooth or sharply timed changes across the timeline. This functionality provides a unified approach to animating both basic and advanced video attributes within the Tooscut environment.

## Discussion Summary
Overall the comments express enthusiasm for a browser‑native NLE built on WebGPU, praising its UI and innovative architecture while noting its current limitations. Reviewers highlight performance glitches on certain browsers, missing professional features such as text, transitions, and comprehensive filter sets, and a non‑commercial license that deters commercial use. Many request API access, shared‑project support, server‑GPU rendering, and mobile usability. The consensus is that the project shows promise but requires further development and stability before it can replace established editors.

---

## Full Article

### Keyframe Animation

Animate any property with bezier easing curves. Transform, opacity, effects — everything is keyframeable.