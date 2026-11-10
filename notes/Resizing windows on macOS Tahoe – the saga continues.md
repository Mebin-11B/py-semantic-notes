---
title: "Resizing windows on macOS Tahoe – the saga continues"
url: https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/
clipped: 2026-06-17 01:46:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - macos window management
  - fitts's law
  - hit-testing
  - ui design regression
  - user experience (ux)
  - software qa
related:
  - "[[macOS window management]]"
  - "[[Fitts's Law]]"
  - "[[Hit-Testing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An empirical analysis of window-resizing regions in the macOS 26.3 (Tahoe) release cycle, tracking how Apple introduced and then reverted a corner-radius hit-testing fix.
>
> **Key points:**
> - The author created a test application to map macOS window corner hit-test target areas pixel-by-pixel using simulated clicks.
> - The macOS 26.3 Release Candidate updated the hit-boxes to follow the rounded corner radius, but simultaneously narrowed the vertical/horizontal edge resize strip by 14% (from 7px to 6px).
> - In the final public release of macOS 26.3, Apple reverted the changes entirely back to the old square corner hit-boxes, re-classifying the problem as a "Known Issue."
> - User feedback highlights ongoing frustration with modern macOS window sizing accuracy, rounded screens, and the reliance on third-party tools to navigate narrow target borders.
>
> **Concept links:** [[macOS window management]], [[Fitts's Law]], [[Hit-Testing]], [[UI Design Regression]], [[User Experience (UX)]], [[Software QA]]
>
> **Suggested connections:**
> - [[macOS window management]] — The core operating system window server and workspace management engine.
> - [[Fitts's Law]] — Human-computer interaction principles governing target acquisition ease based on click-target dimensions.
> - [[Hit-Testing]] — The coordinate mapping technique used to determine which graphical element is targeted by cursor events.
<!-- ai-summary:end -->


# [Resizing windows on macOS Tahoe – the saga continues](https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/)

## Digest Summary
The post documents testing of macOS 26.3’s window‑resizing behavior using a custom app that scans the bottom‑right corner for mouse‑event zones. In the Release Candidate, Apple changed the resize regions to follow the window’s corner radius instead of remaining square. However, the vertical/horizontal resize band (yellow) narrowed: the inner portion reduced from 3 px to 2 px, and the overall band thickness dropped from 7 px to 6 px—a 14 % reduction that increases missed resize attempts. In the final macOS 26.3 release, this adjustment was removed, restoring the original square regions. Correspondingly, the release notes were updated, reclassifying the issue from “Resolved” to a “Known Issue.” The findings are illustrated with three comparative images.

## Discussion Summary
The comments express broad dissatisfaction with macOS window‑management, particularly the difficulty of resizing and moving windows due to thin borders, rounded corners, and inconsistent hit‑testing, which many view as a regression or design flaw. Users compare the experience unfavorably to Linux and Windows, cite workarounds such as third‑party tools, and request features like predefined zones and edge‑linked resizing. Technical critiques of the recent pixel‑size change appear, while some note similar bugs on multi‑monitor setups and lament perceived misallocation of engineering resources at Apple.

---

## Full Article

macOS 26.3, Release Candidate
-----------------------------

In the release notes for macOS 26.3 RC, Apple stated that the window-resizing issue I demonstrated in [my recent blog post](https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/) had been resolved.

![](https://noheger.at/blog/wp-content/uploads/2026/02/resolved-issues.webp)

I was happy to read that, but also curious about what had actually changed.

So I wrote a little test app.

[](https://noheger.at/blog/wp-content/uploads/2026/02/corner-scan.mp4)

It performs a pixel-by-pixel scan in the area around the bottom-right corner of the window, hammering it with simulated mouse clicks to detect exactly where it responds to those clicks (red), where it’s about to resize (green), where it’s about to resize vertically or horizontally only (yellow), and where it doesn’t receive any mouse events at all (blue).

And indeed, the window resize areas now follow the corner radius instead of using square regions:

[](https://noheger.at/blog/wp-content/uploads/2026/02/before-after.mp4)

So that’s definitely better!

But unfortunately, as you can see, the thickness of the yellow area – used for resizing the window only vertically or horizontally – also became thinner. The portion that lies inside the window frame is now only 2 pixels instead of 3.

In total the thickness went down from 7 to 6 pixels, which is a 14% decrease, making it 14% more likely to miss it.

macOS 26.3, Final Release
-------------------------

When the final version of macOS 26 was released I was curious if Apple might have further refined the implementation. So I performed the scan once again. But to my big surprise, the fix was not only unrefined – it was completely removed! So we are now back to the previous square regions:

![](https://noheger.at/blog/wp-content/uploads/2026/02/26.3.webp)

And in fact, the release notes have also been updated: the problem went from a “Resolved Issue” to a “Known Issue”.

![](https://noheger.at/blog/wp-content/uploads/2026/02/known-issues.webp)