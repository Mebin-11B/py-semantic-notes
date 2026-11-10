---
title: "The struggle of resizing windows on macOS Tahoe"
url: https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/
clipped: 2026-06-17 01:59:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The struggle of resizing windows on macOS Tahoe](https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/)

## Digest Summary
The post describes how macOS “Tahoe” (a codename for a macOS version) introduced a large corner radius that reduces the effective click target for window resizing. The system expects a 19 × 19 px region near each window corner; with traditional sharp corners about 62 % of that region lies inside the window, but the rounded corners push roughly 75 % of the area outside the visible window frame. Consequently, users’ instinctive clicks inside the visual corner often miss the active zone, causing resize attempts to fail—a problem the author has not encountered in four decades of computing. The only reliable method on Tahoe is to place the cursor just outside the corner, a non‑intuitive gesture that increases error rates. No other functional changes or workarounds are discussed.

## Discussion Summary
The comments are overwhelmingly critical of macOS Tahoe’s visual redesign and window‑management changes, describing the new rounded corners, altered resize zones, and “Liquid Glass” aesthetic as unintuitive, space‑wasting, and detrimental to usability. Many users compare the update unfavorably to previous macOS versions, Windows 11, and contemporary Linux desktops, suggesting the changes push them toward alternative operating systems or third‑party tools that restore familiar resizing behavior. Some acknowledge occasional positive tweaks or appreciate the visual style, but the dominant view is that the update reflects poor design decisions, a shift toward iOS‑centric priorities, and reduced overall software quality.

---

## Full Article

A lot has already been said about the absurdly large corner radius of windows on macOS Tahoe. People are calling the way it looks comical, like a child’s toy, or downright insane.

Setting all the aesthetic issues aside – which are to some extent a matter of taste – it also comes at a cost in terms of usability.

Since upgrading to macOS Tahoe, I’ve noticed that quite often my attempts to resize a window are failing.

[](https://noheger.at/blog/wp-content/uploads/2026/01/resize-window.mov)

This never happened to me before in almost 40 years of using computers. So why all of a sudden?

It turns out that my initial click in the window corner instinctively happens in an area where the window doesn’t respond to it. The window expects this click to happen in an area of 19 × 19 pixels, located near the window corner.

If the window had no rounded corners at all, 62% of that area would lie **inside** the window:

![](https://noheger.at/blog/wp-content/uploads/2026/01/clickable-area-1.webp)

But due to the huge corner radius in Tahoe, most of it – about 75% – now lies **outside** the window:

![](https://noheger.at/blog/wp-content/uploads/2026/01/clickable-area-2.webp)

Living on this planet for quite a few decades, I have learned that it rarely works to grab things if you don’t actually touch them:

[](https://noheger.at/blog/wp-content/uploads/2026/01/scrambled-eggs.mov)

So I instinctively try to grab the window corner inside the window, typically somewhere in that green area, near the blue dot:

![](https://noheger.at/blog/wp-content/uploads/2026/01/expected-area-1.webp)

And I assume that most people would also intuitively expect to be able to grab the corner there. But no, that’s already outside the accepted target area:

![](https://noheger.at/blog/wp-content/uploads/2026/01/expected-area-2.webp)

So, for example, grabbing it here does **not** work:

![](https://noheger.at/blog/wp-content/uploads/2026/01/expect-2.webp)

But guess what – grabbing it here **does**:

![](https://noheger.at/blog/wp-content/uploads/2026/01/outside.webp)

So in the end, the most reliable way to resize a window in Tahoe is to grab it **outside** the corner – a gesture that feels unnatural and unintuitive, and is therefore inevitably error-prone.