---
title: "The Unreasonable Effectiveness of the Fourier Transform"
url: https://joshuawise.com/resources/ofdm/
clipped: 2026-06-17 02:01:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Unreasonable Effectiveness of the Fourier Transform](https://joshuawise.com/resources/ofdm/)

## Digest Summary
The document summarizes Joshua Wise’s “The Unreasonable Effectiveness of the Fourier Transform” talk (Teardown 2025). It lists supporting materials: a YouTube recording, slide PDF, and a Jupyter notebook used for generating plots (not optimized code). It references the original OFDM patent (US 3488445 A, filed 1966, expired 1987) and cites Eugene Wigner’s essay “The Unreasonable Effectiveness of Mathematics in the Natural Sciences.” Additional resources include a paper describing simultaneous carrier‑offset and time‑offset estimation, a custom DVB‑T decoder implementation, and a recommended video explaining the Fast Fourier Transform algorithm. The page invites feedback from attendees.

## Discussion Summary
The discussion emphasizes the broad impact and utility of the Fourier Transform, highlighting its historical roots, connections to the uncertainty principle, and practical applications such as signal analysis, video‑based heart‑rate detection, and analogies to principal component analysis. Educational resources, including a recommended video, are noted for making the concept accessible. While most remarks convey appreciation for the transform’s explanatory power and teaching value, a few express criticism of its infinite nature and concerns about patent implications. Overall, the sentiment is largely positive with minor reservations.

---

## Full Article

The Unreasonable Effectiveness of the Fourier Transform
=======================================================

***Notes from [Joshua Wise](https://joshuawise.com/)'s talk at [Teardown 2025](https://www.crowdsupply.com/teardown/portland-2025).***

![](https://joshuawise.com/resources/ofdm/title.png)

**New**: You can now watch a recording of my talk [on my YouTube channel](https://youtu.be/9k1Wu69Gw4w)! Or you can
just click "play" below, I suppose.

VIDEO

Here are a few resources from my talk.

* Here is [a PDF of my slides](https://joshuawise.com/resources/ofdm/jwise-ofdm-teardown.pdf), if you
  wanted to refer to anything in specific.
* Here is [the Jupyter notebook](https://joshuawise.com/resources/ofdm/teardown_2025_talk.ipynb) that I
  used to produce all of the zillions of plots. I do not claim that it is
  good code, but it is code.
* The OFDM patent is [US3488445A](https://patents.google.com/patent/US3488445A/en), filed
  in 1966, expired in 1987.
* Here is [Eugene Wigner's
  original discussion, "The Unreasonable Effectiveness of Mathematics in the
  Natural Sciences"](https://doi.org/10.1002/cpa.3160130102). There are many good follow-ons to this, too.
* Here is [the paper
  on how to estimate both carrier offset *and* time offset *at the same
  time*](https://ieeexplore.ieee.org/document/599949). I implemented it by typing in the algorithm, and it worked, but if you
  understand it and can explain it to me please let me know.
* Here is [the DVB-T decoder that I
  wrote](https://github.com/jwise/dvbt). I do not claim that it is the right way to do any of these
  things, but it is a way to do these things.
* Finally, here is [an absolutely fantastic
  video that breaks down the implementation of the *Fast* Fourier
  Transform algorithm](https://www.youtube.com/watch?v=h7apO7q16V0). I watch it every year or two.

Thanks so much for coming! Please let me know if you have feedback on
this. I'd love to hear what you thought.