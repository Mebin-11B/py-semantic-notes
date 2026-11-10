---
title: "Turning a MacBook into a touchscreen with $1 of hardware (2018)"
url: https://anishathalye.com/macbook-touchscreen/
clipped: 2026-06-17 01:25:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Computer Vision
  - Human-Computer Interaction
  - Hardware Hacking
  - Homography
  - Open Source Hardware
related:
  - "[[Running Tesla Model 3's computer on my desk using parts from crashed cars]]"
  - "[[Jef Raskin, the Visionary Behind the Mac (2013)]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Project Sistine demonstrates a low-cost, open-source method to turn a MacBook into a touchscreen using a $1 mirror assembly and classical computer vision to detect fingers and their screen reflections.
>
> **Key points:**
> - Project Sistine uses a simple $1 mirror assembly placed over a MacBook webcam to view the screen at a sharp angle.
> - It detects fingers and their reflections on the screen surface using a classical computer vision pipeline (skin-color filtering, contours, and vertical distance analysis to distinguish touch vs. hover).
> - Coordinate mapping from the webcam video feed to the screen is performed via a homography matrix calibrated using RANSAC.
> - The prototype translates detected touches/hovers into standard mouse events, making existing macOS apps instantly touch-enabled.
> - The project is open-source under the MIT license and could be improved with higher webcam resolutions and curved mirrors.
>
> **Concept links:** [[Computer Vision]], [[Human-Computer Interaction]], [[Hardware Hacking]], [[Homography]], [[Open Source Hardware]]
>
> **Suggested connections:**
> - [[Running Tesla Model 3's computer on my desk using parts from crashed cars]] — Another project involving custom hardware setup and interface hacking.
> - [[Jef Raskin, the Visionary Behind the Mac (2013)]] — Historical context on alternative Macintosh interface concepts and human-computer interaction.
<!-- ai-summary:end -->

# [Turning a MacBook into a touchscreen with $1 of hardware (2018)](https://anishathalye.com/macbook-touchscreen/)

## Digest Summary
Project Sistine demonstrates a low‑cost method to convert a MacBook into a touchscreen using a $1 mirror assembly placed before the built‑in webcam. The setup consists of a small mirror, rigid paper plate, door hinge, and hot glue, angled so the webcam captures the screen and its reflection. Finger detection relies on classical computer‑vision steps: skin‑color filtering, binary thresholding, contour extraction, selecting the two largest overlapping contours, and defining the touch/hover point as the midpoint between contour extremes. Touch versus hover is distinguished by the vertical gap between contours. A homography matrix maps webcam coordinates to screen coordinates; it is calibrated by prompting the user to touch known points and estimating the transformation with RANSAC. The system translates detected contacts into mouse events, enabling existing applications to respond to touch. The prototype uses a 480p webcam; higher‑resolution cameras and a curved mirror could improve coverage, making the approach a viable, open‑source, MIT‑licensed low‑cost touchscreen solution.

## Discussion Summary
Comments show strong skepticism toward touchscreen MacBooks, emphasizing ergonomic discomfort, fatigue, and fingerprint issues, with many preferring the existing non‑touch design. Practical concerns dominate, including lighting variability, accuracy limits, and the difficulty of adapting software for reliable use across diverse conditions. Nevertheless, the prototype is praised for its inventive use of existing hardware, open‑source code, and potential niche applications such as outdoor displays, though most view it as a fun proof‑of‑concept rather than a viable consumer product.

---

## Full Article

We turned a MacBook into a touchscreen using only $1 of hardware and a little
bit of computer vision. The proof-of-concept, dubbed âProject Sistineâ after
our [recreation](https://anishathalye.com/_next/static/images/thumbnail-75236687051a403d7d7168f93dd4498a.jpg) of the famous [painting](https://en.wikipedia.org/wiki/The_Creation_of_Adam) in the Sistine Chapel, was prototyped
by me, [Kevin](https://twitter.com/antimatter15), [Guillermo](https://twitter.com/biject), and [Logan](https://github.com/lengstrom) in about 16 hours.

The basic principle behind Sistine is simple. Surfaces viewed from an angle
tend to look shiny, and you can tell if a finger is touching the surface by
checking if itâs touching its own reflection.

Kevin, back in middle school, noticed this phenomenon and built [ShinyTouch](https://antimatter15.com/project/shinytouch/),
utilizing an external webcam to build a touch input system requiring virtually
no setup. We wanted to see if we could miniaturize the idea and make it work
without an external webcam. Our idea was to retrofit a small mirror in front of
a MacBookâs built-in webcam, so that the webcam would be looking down at the
computer screen at a sharp angle. The camera would be able to see fingers
hovering over or touching the screen, and weâd be able to translate the video
feed into touch events using computer vision.

Our hardware setup was simple. All we needed was to position a mirror at the
appropriate angle in front of the webcam. Here is our bill of materials:

* Small mirror
* Rigid paper plate
* Door hinge
* Hot glue

After some iteration, we settled on a design that could be assembled in minutes
using a knife and a hot glue gun.

Hereâs the finished product:

The first step in processing video frames is detecting the finger. Hereâs a
typical example of what the webcam sees:

The finger detection algorithm needs to find the touch/hover point for further
processing. Our current approach uses classical computer vision techniques. The
processing pipeline consists of the following steps:

1. Filter for skin colors and binary threshold
2. Find contours
3. Find the two largest contours and ensure that the contours overlap in the
   horizontal direction and the smaller one is above the larger one
4. Identify the touch/hover point as the midpoint of the line connecting the
   top of the bottom contour and the bottom of the top contour
5. Distinguish between touch and hover based on the vertical distance between
   the two contours

Shown above is the result of applying this process to a frame from the webcam.
The finger and reflection (contours) are outlined in green, the bounding box is
shown in red, and the touch point is shown in magenta.

The final step in processing the input is mapping the touch/hover point from
webcam coordinates to on-screen coordinates. The two are related by a
[homography](https://en.wikipedia.org/wiki/Homography_(computer_vision)). We compute the homography matrix through a calibration process
where the user is prompted to touch specific points on the screen. After we
collect data matching webcam coordinates with on-screen coordinates, we can
estimate the homography robustly using [RANSAC](https://en.wikipedia.org/wiki/Random_sample_consensus). This gives us a projection
matrix that maps webcam coordinates to on-screen coordinates.

The video above demonstrates the calibration process, where the user has to
follow a green dot around the screen. The video includes some debug
information, overlaid on live video from the webcam. The touch point in webcam
coordinates is shown in magenta. After the calibration process is complete, the
projection matrix is visualized with red lines, and the software switches to a
mode where the estimated touch point is shown as a blue dot.

In the current prototype, we translate hover and touch into mouse events,
making existing applications instantly touch-enabled.

If we were writing our own touch-enabled apps, we could directly make use of
touch data, including information such as hover height.

Project Sistine is a proof-of-concept that turns a laptop into a touchscreen
using only $1 of hardware, and for a prototype, it works pretty well! With some
simple modifications such as a higher resolution webcam (ours was 480p) and a
curved mirror that allows the webcam to capture the entire screen, Sistine
could become a practical low-cost touchscreen system.

Our Sistine prototype is [open source](https://github.com/bijection/sistine), released under the MIT License.