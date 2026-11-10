---
title: "RIP software hackathons. Long live the hardware hackathon"
url: https://blog.oscars.dev/posts/rip-software-hackathons-long-live-the-hardware-hackathon/
clipped: 2026-06-17 00:49:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [RIP software hackathons. Long live the hardware hackathon](https://blog.oscars.dev/posts/rip-software-hackathons-long-live-the-hardware-hackathon/)

## Digest Summary
The author describes a recent 48‑hour hackathon in Vilnius where their two‑person team retrofitted an old rotary phone with a Raspberry Pi, exposing its I/O and linking it to a server via a single WebSocket. The server handled two‑way audio, custom bell tones, and hang‑up control, while an AI agent used the Spotify API to generate playlists from natural‑language prompts (e.g., “play music by artists alleged to be on the Epstein files,” “create a 1970s Zambian psychedelic rock playlist”). Voice output was provided by ElevenLabs, giving the phone a “warm Yorkshire gentleman” persona. The team relied on AI‑generated code, noting that modern hackathons prioritize system architecture and rapid integration over manual coding. The author argues that as software problems become “solved,” future hackathons will emphasize hardware and legacy tech, proposing projects such as Apple II applications, fax‑to‑social‑media converters, Game Boy Advance Bloomberg terminals, LLM‑driven cash registers, and AI‑controlled microwaves. The piece calls for “ridiculous”, overbuilt prototypes that blend APIs, wiring, and consumer electronics.

## Discussion Summary
The comments portray hackathons as increasingly divided between superficial UI‑focused showcases and deeper, hands‑on creation, with participants noting that strong design talent often outweighs technical substance. Many express personal challenges in pitching, storytelling, and audience engagement, seeing hackathons as practice grounds for those skills. A recurring theme is excitement about emerging tools—affordable hardware, 3D printing, and AI—that could revive substantive product development, while others criticize the trend toward gimmicky presentations and the exploitation of participants by organizers.

---

## Full Article

I took part in a hackathon in Vilnius the other weekend (courtesy of Basedcollective) during the [pink soup festival](https://www.govilnius.lt/pink-soup-fest). I brought along an old rotary phone and our two-man team spent the next 48 hours sticking our fingers in it. We wired a Raspberry Pi into the phone which interfaced with all of its IO and communicated with our server via a single websocket connection which controlled everything from two-way audio, the bell ringer (with custom frequency and audio patterns) and the hangup switch. For the demo, we set up an AI agent which could research music, create playlists and play collections of niche music all via the Spotify API on request. Interpreting requests such as:

> “play some music by artists who are alleged to be on the Epstein files”

or

> “create me a playlist of 70s Zambian psychedelic rock”,

*et cetera*

We put the personality of a warm Yorkshire gentleman on the other end of the line (courtesy of ElevenLabs) and had good fun getting all the parts working together ready for the final demo under 48 hours later.

As is the evolving trend with writing code nowadays, neither me nor my team-mate looked at a single line of code over the entire weekend. Something which would have been unheard of just 12 months ago has become today's reality. As it was a hackathon, all we cared about was that it worked and the inner lines of code didn't matter.

For this reason, the focus of hackathons has completely shifted away from typing code with aching fingers and zero sleep, to thinking of the system as a whole (not a very unique opinion now, I know) and iterating on intricacies of implementation with radical refactors has become a trivial task. This leaves free mental RAM to actually faff with hardware and how it interfaces with the physical world.

All of this really makes me think:

> What does a hackathon moonshot idea really look like nowadays?

As software subtends to becoming more and more "solved", a web-app which may have been a fantastic feat 24 months ago has now tumbled into mediocrity. How do we continue to push the hackathon bar further? This is where I think hardware comes in.

In the coming months, we are going to see more of an emphasis on hardware hackathons than we did before. Something I would like to see specifically is a renaissance of old tech which had previously required very niche and time consuming domain knowledge to mess with.

Some project ideas off the top of my head:

* Building a ridiculous Apple II application
* Turning a fax machine into a social media network
* Turning a Game Boy Advance into a Bloomberg terminal
* Making an LLM-driven cash register that can feel love and pain
* An AI voice-activated microwave

These are just some ideas...

Yes there’s probably no real *sane* business case in any of these projects but I am also of the opinion that hackathons **should** be a bit ridiculous. I don’t want to see your VC pitch and the problem you are solving, I want to see an unholy, overbuilt and morally confusing obelisk of wires and APIs, a [hubris manifest](https://www.youtube.com/watch?v=cYxIe7T8ZKA) in a breadboard paired with a frankenstein'd consumer electronics item that makes me question my very own reality.