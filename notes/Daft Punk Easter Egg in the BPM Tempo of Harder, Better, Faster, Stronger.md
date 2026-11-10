---
title: "Daft Punk Easter Egg in the BPM Tempo of Harder, Better, Faster, Stronger?"
url: https://www.madebywindmill.com/tempi/blog/hbfs-bpm/
clipped: 2026-06-17 02:04:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Daft Punk Easter Egg in the BPM Tempo of Harder, Better, Faster, Stronger?](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/)

## Digest Summary
Daft Punk’s “Harder, Better, Faster, Stronger” is commonly listed at 123 BPM, but precise measurement shows it is 123.45 BPM. Using a manual beat‑count method (identifying the first and last clear waveform peaks, measuring the interval between them, and applying bpm = 60 × (beats − 1) ÷ duration) yields 123.4499 BPM on a Discovery CD rip (216.276 s for 445 intervals) and 123.4534 BPM on the official YouTube audio (216.282 s). The author’s tempo‑detection software, based on FFT and autocorrelation, reports values between 123 and 124, confirming the non‑integral tempo. Hardware used on the Discovery album—E‑mu SP‑1200, Akai MPC‑3000, and Emagic Logic—supports fractional BPMs to one decimal place (SP‑1200, MPC‑3000) and to four decimal places (Logic), making a 123.45 BPM setting feasible. The close match suggests the tempo may have been an intentional Easter egg, though definitive confirmation from the producers is unavailable.

## Discussion Summary
The discussion centers on the track’s unusually precise 123.45 BPM, with participants debating whether it is an intentional Daft Punk easter‑egg or a byproduct of analog sampling, rounding, or digital processing quirks. Technical analyses cite timing calculations, software detection limits, and possible varispeed or mastering adjustments, while others view the precision as deliberate thematic symbolism tied to the song’s robotic narrative. Overall, commenters express admiration for the band’s ingenuity, yet many remain unconvinced that the exact tempo was purposefully engineered.

---

## Full Article

Was Daft Punk Having a Laugh When They Chose the Tempo of Harder, Better, Faster, Stronger?
===========================================================================================

![Robots illustration](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/assets/robots.jpg)

[Google "harder better faster stronger bpm"](https://www.google.com/search?q=harder+better+faster+stronger+bpm) and Google’s “AI Overview” will tell you:

> Daft Punk’s “Harder, Better, Faster, Stronger” generally sits around 123 BPM (Beats Per Minute), though some analyses find it slightly higher (like 123.48 BPM) or list different BPMs in remixes/workouts, with exact figures varying slightly by source and version.

Spotify’s metadata database, [SongBPM](https://songbpm.com/@daft-punk/harder-better-faster-stronger), and most other online BPM databases list it at exactly 123.

But I think our helmet-clad robot friends might have been making a little joke that we’ve apparently all missed. The BPM of Harder, Better, Faster, Stronger is actually 123.45.

How do I know this? It so happens that for over 10 years I’ve written an app called [Tempi](https://www.madebywindmill.com/tempi/) that shows the BPM of music in real time, so I know a little bit about the science and algorithms behind music tempo detection.

Most tempo detection software works basically the same way:

* A specialized algorithm called the Fast Fourier Transform (FFT) collects overlapping energy levels at different frequency bands.
* Those levels are refined into well-defined peaks that represent rhythmic events in the track.
* Another algorithm (autocorrelation) looks for patterns, or more accurately *periodicity*, in those peaks.

But these patterns are tricky because there’s all kinds of noise, performance inaccuracies, and rhythmic harmonics throwing things off. All that is to say, a) it’s complicated and b) it’s not perfectly accurate.

When I make changes to my own system of course I need some way to know if it’s getting better or worse, so I have a test library of hundreds of song snippets that I score it against. One of these songs is Daft Punk’s HBFS, and early on I noticed something strange about that track.

Almost all electronic music is synced to a sequencer and so obviously is going to have a very steady tempo. But while the vast majority of electronic music tracks I test have an “integral” tempo – meaning their tempo is exactly some round number like 95, and not a fraction like 95.2 – my software always finds the BPM of HBFS to be somewhere between 123 and 124, but not exactly either. For years I’ve chalked this up to inconsistencies with my system and didn’t think much of it. But lately I’ve made improvements to the system so that it’s much more accurate and it now tells me the BPM of HBFS is 123.4.

And that got me thinking, “Hmm. Did these guys pick that tempo because they have a sense of humor? And if so, how far would they take it?”

To get to the bottom of this I needed to establish what the BPM of HBFS really is.

### And that’s actually pretty easy to do…

Here’s a Venn diagram showing the overlap between human and computer capabilities in the digital realm:

![Venn diagram showing overlap between human and computer capabilities](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/assets/venn.png)

Computers can do almost all “computer-y” things (i.e. things that can be entirely done on a computer) MUCH better, faster, (and stronger?) than humans. But for the time being there remain a few things that humans can do very easily which computers find difficult. Along with counting traffic lights and crosswalks, one of those things is finding the exact BPM of a song. Not an estimate like most software does, but the *exact* value with extreme precision across the entire song. Anyone with a basic sense of rhythm and an audio app can do this.

Here’s how:

* Open the song in an audio app like Logic, Audition, Ableton, Reaper, ProTools, etc.
* Zoom in on the waveform a little bit so you can see the shape of the beats.
* Find the first obvious beat – meaning it has a well-defined waveform peak – and the last obvious beat. Let’s call these “bookend” beats.
* Measure the exact duration in seconds between the bookend beats.
* Play the song and *count* all the beats starting at the first bookend beat and ending at the last bookend beat. (If you have an old school calculator, an easy way to do this is type “1+1=” and then just keep tapping “=” to add 1 on each beat.)

Then to get the *exact* tempo of the track, averaged throughout the entire thing, use this formula:

```
bpm = 60 * (number_of_beats - 1) / duration
```

Computers have a rough time of this because they don’t really know how to “keep a beat”, and the algorithms that *can* find the beat do a lot better when they already know the estimated BPM, which is obviously a chicken/egg problem.

For the first bookend beat in HBFS I used the first beat after the “whooshing” intro, at around 5.58s. The last bookend beat I used the last “work” at about the 3:41.85 mark. (“Never” and “Over” aren’t good candidates because you can’t see their waveform peaks.)

That gives exactly 446 beats or 445 intervals.

I tried this with two different copies of HBFS. The Discovery CD rip I have of the song has a duration between the bookend beats of 216.282, so:

```
bpm = 60 * 445 / 216.282 = 123.4499403556
```

The “YouTube official audio” track I tested has a duration of 216.276, so:

```
bpm = 60 * 445 / 216.276 = 123.4533651445
```

The original Discovery CD version has obviously undergone less processing over time than the YouTube version so I tend to think it’s more representative, and it’s *very* close to 123.45 – only a 0.00005964 difference! But even the more modern YouTube version closely rounds to 123.45.

So hopefully I’ve put this fact to rest:

**The BPM of Harder, Better, Faster, Stronger is 123.45.**

But…was this intentional, or just a happy accident?
---------------------------------------------------

The year is 1999 or 2000. Would the gear Daft Punk uses even *support* fractional BPMs? And if so out to how many decimal places?

From their 2001 interview with Remix Magazine ([archive.org](https://web.archive.org/web/20080503064751/http://remixmag.com/mag/remix_robopop/)) we know that Bangalter says:

> Our sequencing is done either on an E-mu SP-1200, an Akai MPC, or a PC with Logic Audio software. We do not work on things in just one way.

And from later interviews we know the Akai MPC was specifically an MPC-3000. (Oh, and that’s *Emagic*’s Logic, *not* Apple’s. Apple didn’t acquire Emagic until 2002.)

Did the E-mu support fractional BPMs? Yes, but only to 1 decimal place:

![E-mu SP-1200 display showing tempo](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/assets/e-mu-display.jpg)

The Akai MPC-3000? Yep, also to 1 decimal place:

![Akai MPC-3000 display showing tempo](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/assets/akai-display.jpg)

What about Emagic’s Logic?

![Emagic Logic tempo display showing 4 decimal places](https://www.madebywindmill.com/tempi/blog/hbfs-bpm/assets/logic-tempo.jpg)

Oooh, look at that. Logic supported BPMs to *\*4\** decimal places.

But while we know those three sequencers were used on the Discovery album, I’m not sure anyone else knows which one was specifically used on HBFS. I’ve searched and searched and it seems this detail has just never been revealed.

And to confuse matters more, in a [2013 interview with Time Magazine](https://entertainment.time.com/2013/05/21/robocall-a-conversation-with-daft-punk/), Bangalter says:

> So we’ve never actually made music with computers! [laughs] Neither Homework nor Discovery nor even Human After All were made with computers.

Was he contradicting himself from 12 years before? Or did he forget? Or maybe it’s a terminology thing?

That the CD version is *so* close to exactly 123.45 makes me think this was intentional. And if it was? Well played, robots. You managed to leave a little Easter egg hiding in plain sight for 25 years.

*Update: A [Hacker News reader](https://news.ycombinator.com/item?id=46470550) pointed out that I accidentally reversed the durations of the YouTube clip and the CD rip. Fixed!*