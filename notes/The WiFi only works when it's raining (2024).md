---
title: "The WiFi only works when it's raining (2024)"
url: https://predr.ag/blog/wifi-only-works-when-its-raining/
clipped: 2026-06-17 01:51:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The WiFi only works when it's raining (2024)](https://predr.ag/blog/wifi-only-works-when-its-raining/)

## Digest Summary
A line‑of‑sight Wi‑Fi bridge was installed between a home apartment and a nearby office, using high‑gain directional antennas and 802.11g equipment. For about a decade the link provided stable, high‑speed internet. Over time a neighbor’s tree grew tall enough that its upper branches partially obstructed the Fresnel zone between the antennas. When rain fell, water weight bent the branches away, temporarily clearing the line‑of‑sight and restoring the link; after the rain stopped the branches returned, causing 90 %+ packet loss and loss of connectivity. Debugging confirmed the local router was fine and that the loss occurred only on the bridge’s remote side. The solution was to replace the aging 802.11g devices with newer 802.11n hardware that supports beamforming and is more tolerant of partial obstructions. After installing the new antennas, the bridge maintained a reliable connection regardless of weather, eliminating the rain‑dependent behavior.

## Discussion Summary
The collection emphasizes that many technical problems stem from unexpected physical or environmental factors rather than software bugs, with anecdotes ranging from Wi‑Fi links degraded by foliage to monitors crashing near antennae and rain improving long‑range links. Contributors repeatedly note that simple, concrete adjustments—such as repositioning equipment, pruning trees, adding cooling fans, or using isolating cables—often resolve these issues. The overall tone is pragmatic and mildly amused, acknowledging that unconventional causes are common and that straightforward fixes are frequently sufficient.

---

## Full Article

*Happy April 1st! This post is part of [April Cools Club](https://aprilcools.club/): an April 1st effort to publish genuine essays on unexpected topics. Please enjoy this true story, and rest assured that the tech content will be back soon!*

That's what my dad said when I asked what was wrong with our home internet connection. "The Wi-Fi only works when it's raining."

![Illustration of a Wi-Fi antenna attached to the exterior of an upper floor of an apartment building. It's currently raining, and the Wi-Fi is working flawlessly.](https://predr.ag/processed_images/wifi-router-on-balcony-cropped.e51ec22e71a4e3ef.jpg)

Let's back up a few steps, so we're all on the same page about the *utter ridiculousness* of this situation.

At the time, I was still a college student — this was over 10 years ago. I had come back home to spend a couple of weeks with my parents before the fall semester kicked off. I hadn't been back home in almost a full year, because home and school were on different continents.

My dad is an engineer who had already been tinkering with networking gear longer than I'd been alive. Through the company he started, he had designed and deployed all sorts of complex network systems at institutions across the country — everything from gigabit Ethernet for an office building, to inter-city connections over [line-of-sight](https://en.wikipedia.org/wiki/Line-of-sight_propagation) microwave links.

He is *the last person on Earth* who would say a ["magical thinking"](https://en.wikipedia.org/wiki/Magical_thinking) phrase like that.

"What?" I uttered, stunned. "The Wi-Fi only works while it's raining," he repeated patiently. "It started a couple of weeks ago, and I haven't had a chance to look into it yet."

"No way," I said. If anything, [rain makes wireless signal quality *worse*](https://www.microwave-link.com/microwave/rain-fade-on-microwave-links/), not *better*. Never *better*!

Two weeks without reliable internet? I started a speed-run through the stages of grief...

Denial
------

I pulled open my laptop and started poking at the network.

Pinging any website had a 98% packet loss rate. The internet connection was still up, but only in the most annoying "technically accurate" sense. Nothing loads when you have a 98% packet loss rate! The network may as well have been dead.

I was upset. I had just started dating someone a few months prior, and she was currently on the other side of the planet! How was I to explain that I couldn't stay in touch because it wasn't raining? [Sidenote: Mobile data at the time was *exorbitantly* expensive, so much so that I didn't have a data plan at all for my cell service at home. I couldn't just use my phone's data plan to work around the problem, like one might do today in a similar situation.]

I was pacing around the house, fuming. Grief, stage two!

That's when the rain started.

Bargaining
----------

Like a miracle, within 5 minutes of the rain starting, the packet loss rate was down to 0%!

I couldn't believe my eyes! I was ready for the connection to die at any second, so I opened a million tabs at once — as if I don't normally do that anyway...

The rain held up for about an hour, and so did the internet connection.

Then, 15 minutes or so after the rain stopped, the packet loss rate shot back up to 90%+. The internet connection went back to being unusable.

I was ready to do just about anything to get more rain.

Thankfully, the weather stayed grey and murky for the next few days. Each time, the pattern stayed the same:

* The rain starts, and not even a few minutes later the internet connection is crisp and fast.
* The rain stops, and within 15 minutes the internet connection is unusable again.

As much as I hated to admit it, the evidence was solid. The Wi-Fi only works when it's raining!

At this point, I had a choice to make.

I could keep going through the stages of grief: I could sulk and plan my calls with my girlfriend around the weather forecast.

Or, I could break out of that downward spiral and get to the bottom of what was going on.

"[Magical thinking](https://en.wikipedia.org/wiki/Magical_thinking) be damned! Am I an engineer or what?" I told myself.

That settled it. I wasn't going to take this lying down.

Determination
-------------

Some context on our home networking setup is in order.

Remember how my dad's company had extensive experience with networking solutions? Well, we had a fancy networking setup at home too — and it had worked flawlessly for the best part of 10 years!

My dad's office had a very expensive, very fast [Sidenote: For the time, of course.]
commercial internet connection. The home internet options, meanwhile, weren't great! In my family, we are often stubbornly against settling for less unless there's absolutely no other choice.

The office and our apartment were a few blocks away from each other along a small hill, with our second-floor apartment holding the higher ground. With a bit of work, my dad set up a line-of-sight Wi-Fi bridge — [a couple of high-gain directional Wi-Fi antennas pointed at each other](https://en.wikipedia.org/wiki/Long-range_Wi-Fi) — between the office and our apartment. This let us enjoy the faster commercial internet connection at home!

I started poking around the network to figure out where the connection was breaking down.

The local Wi-Fi router at home was working well — no packets lost. The local end of the Wi-Fi bridge was fine too.

But pinging the remote end of the Wi-Fi bridge was showing a 90%+ packet loss rate — and so did pinging any other network device behind it. Aha, there's something wrong with the Wi-Fi bridge!

But *what*? And why *now*, when the system had been working fine for almost 10 years, rain or shine? [Sidenote: Maybe [years of work experience isn't a good metric](https://predr.ag/blog/mediocrity-can-be-a-sign-of-excellence/#years-of-experience-vs-experience-in-those-years) here either 😄]

*How* can a rain storm *fix* a Wi-Fi bridge, anyway?

So many confusing questions. Time to get some answers!

Debugging
---------

Like any experienced engineer, the first thing I tried was turning everything off and then on again. It didn't work.

Then I checked all the devices on the network individually:

Unlike debugging software, a lot of this hardware debugging was annoyingly *physical*. I had to climb up ladders, trace cables that hadn't been touched in 10 years, and do a lot of walking back and forth between our home and my dad's office.

On my umpteenth back-and-forth walk, as I was bored and exasperated, I started noticing how much our neighborhood had changed in the many years I hadn't been living at home full-time. [Sidenote: Before college, I spent four years at a boarding high school. I was on our national math and programming teams for the [IMO](https://www.imo-official.org/) and [IOI](https://ioinformatics.org/)), so I even spent most of each summer away from home at prep camps and at the competitions themselves.]
Many of the little neighborhood shops were new. Many houses had gotten a fresh coat of paint. Trees that used to be barely more than saplings had grown tall and strong.

Then it hit me.

Realization
-----------

I ran home and climbed up onto the scaffolding holding up the Wi-Fi bridge's antenna. I was hanging precariously off the side of our apartment building, two stories up in the air. [Sidenote: In retrospect, a safety harness would have been a good idea... Things people do for internet! Don't forget, a girl was involved too — I wasn't doing this merely for Netflix or Twitter.]

Then I looked downhill, at the antenna that formed the second half of the Wi-Fi bridge.

Or at least, *toward* the antenna, because I couldn't see it — a tree in a neighbor's yard was in the way! Its topmost branches were swaying back and forth in the line-of-sight between the antenna pair.

*Bingo!*

The Problem and the Fix
-----------------------

Here's what was going on.

Many years ago, we installed the Wi-Fi bridge. For a long time, everything was great!

But every year, our neighbor's tree grew taller and taller. Shortly before when I came back home that summer, its topmost branches had managed to reach high enough to interfere with our Wi-Fi signal.

It was *only barely* tall enough to interfere with the signal, though!

Every time it rained, the rain collected on its leaves and branches and *weighed them down*. The extra weight bent them out of the way of the Wi-Fi line-of-sight! [Sidenote: Interestingly, [objects *outside* the straight line between antennas can still cause interference](https://en.wikipedia.org/wiki/Line-of-sight_propagation#Impairments_to_line-of-sight_propagation)! For best signal quality, the [Fresnel zone](https://en.wikipedia.org/wiki/Fresnel_zone) between the antennas should be clear of obstructions. But perfection isn't achievable in practice, so RF equipment like Wi-Fi uses techniques like error-correcting codes so that it can still work without a perfectly clear Fresnel zone.]

Each time the rain stopped, the rainwater would continue to drip off the tree. Slowly, over the course of 15ish minutes, that would unburden the tree — letting it rise back up into the path of our bits and bytes. That's when the Wi-Fi would stop working.

The fix was easy: upgrade our hardware. We replaced [our old 802.11g devices](https://en.wikipedia.org/wiki/IEEE_802.11g-2003) with [new 802.11n ones](https://en.wikipedia.org/wiki/IEEE_802.11n-2009), which took advantage of new ~~magic~~ math and physics to make signals more resistant to interference. [Sidenote: One such piece of magic new to 802.11n Wi-Fi is called "[beamforming](https://www.oreilly.com/library/view/80211ac-a-survival/9781449357702/ch04.html)" — it's when a transmitter can use multiple antennas transmitting on the same frequency to shape and steer the signal in a way that improves the effective range and signal quality. Modern Wi-Fi does beamforming with only a few antenna elements, but if we scale that number way up we get [a phased array antenna](https://en.wikipedia.org/wiki/Phased_array). Ever wondered how come [Starlink antennas are flat](https://www.pcmag.com/news/spacex-reveals-next-gen-starlink-dish-for-residential-users) and not a ["dish" like old satellite TV antennas](https://en.wikipedia.org/wiki/Satellite_dish#Gallery)? They use phased arrays to aim their signal at [the Starlink satellites streaking across the sky](https://www.space.com/starlink-satellite-train-how-to-see-and-track-it) — without any moving parts. ~~Magic!~~ Physics!]

A few days later, the new gear arrived and I eagerly climbed back up the scaffolding to install the new antennas.

A few screws, zip ties, and cable connections later, the Wi-Fi's "link established" lights flashed green once again.

This time, *it wasn't raining.*

All was well once again.

*Hope you enjoyed this true story! [April Cools](https://aprilcools.club/) is about surprising our readers with fun posts on topics outside our usual beat. Check out the other April Cools posts on [our website](https://aprilcools.club/), and consider making your own blog part of April Cools Club next year!*

*If you liked this post, consider [subscribing or following me on social media](https://predr.ag/subscribe/).*

*Thanks to [Hillel Wayne](https://hillelwayne.com/) and [Jeremy Kun](https://jeremykun.com/) for reading drafts of this post. All mistakes are my own.*