---
title: "Richard D. James aka Aphex Twin speaks to Tatsuya Takahashi (2017)"
url: https://web.archive.org/web/20180719052026/http://item.warp.net/interview/aphex-twin-speaks-to-tatsuya-takahashi/
clipped: 2026-06-17 02:01:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Synthesizer Design
  - Audio Engineering
  - Aphex Twin
  - Korg
  - Microtuning
  - Ergonomics
related:
  - "[[LÖVE 2D Game Framework for Lua]]"
  - "[[When the cheap one is the cool one]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Aphex Twin (Richard D. James) and Korg synth designer Tatsuya Takahashi discuss audio design, tuning systems, hardware ergonomics, and creative standardization.
>
> **Key points:**
> - Discussion covers the 440 Hz standard vs. historical tuning, highlighting water resonance and cymatics.
> - Takahashi explains the engineering behind non-standard sampling rates (like the Volca Sample's 31.25 kHz) and how limits shape sound.
> - Notes the history of reversed faders (e.g. Yamaha SK-10, Calrec desks) designed as safeguards in broadcast mixing.
> - Compares synthesizer interface design, noting the impact of cultural conventions like vertical Japanese text.
>
> **Concept links:** [[Synthesizer Design]], [[Audio Engineering]], [[Aphex Twin]], [[Korg]], [[Microtuning]], [[Ergonomics]]
>
> **Suggested connections:**
> - [[LÖVE 2D Game Framework for Lua]] — related to sound engine programming.
> - [[When the cheap one is the cool one]] — related design limits and artistic constraints.
<!-- ai-summary:end -->

# [Richard D. James aka Aphex Twin speaks to Tatsuya Takahashi (2017)](https://web.archive.org/web/20180719052026/http://item.warp.net/interview/aphex-twin-speaks-to-tatsuya-takahashi/)

## Digest Summary
The interview covers several technical aspects of audio standards and design. Takahashi notes that concert orchestras typically tune slightly below the 440 Hz reference, a standard originally adopted to align instruments, while acknowledging the ongoing 432 Hz vs 440 Hz debate and the acoustic relevance of cymatics. He explains the 48 kHz sample rate’s basis in the Nyquist theorem and contrasts it with the Volca Sample’s 31.25 kHz rate, which imparts a distinctive sound due to hardware constraints. James adds that human hearing tops out near 20 kHz, though higher frequencies may still affect the body, and comments on his preference for lo‑fi “70s” timbres despite interest in ultra‑clear spectra. Both discuss unconventional control layouts—Yamaha SK‑10 and Calrec mixers invert faders to prevent accidental broadcast distortion—and how such ergonomics influence workflow. The conversation also touches on cultural design differences, such as Japanese vertical text and synth aesthetics diverging from Moog‑style designs, and references custom hardware like micro‑tuning converters, hand‑made sequencers, KORG35 filter chips, and Taguchi omnidirectional speakers.

## Discussion Summary
The comments express strong admiration for Richard James’s extensive knowledge and pioneering approach, noting his music’s distinctiveness and his willingness to experiment with unconventional performances such as a swinging piano. They highlight his continued involvement in hardware development, particularly leading Korg’s research and development in Berlin, and mention interest in programming synths with Scala. The overall tone is enthusiastic and appreciative, emphasizing both his artistic impact and technical contributions while providing links to interviews and archival material for further exploration.

---

## Full Article

But I’ve also read studies from the old Philips laboratories in the Netherlands that show orchestras average deviation from 440 Hz was measured over many concerts and was seen to differ by a few Hz, usually slightly below. Pretty anal. Some people obviously really cared that 440 Hz was being adhered to in practice.

Why 440 Hz was chosen in the first place is another interesting story, but looking at the resonances of water and sound is a great place to start, or read up on [cymatics](https://web.archive.org/web/20180719052026/https://en.wikipedia.org/wiki/Cymatics). If you aren’t already familiar with it, that is.

TT: So many things are standardised that you don't really think about because they were there before you started using it. 440 Hz was brought about to standardise the way people play together and, yeah, someone can bring a guitar to a piano and it would work together because of that standard.

It's like how a green light means you can cross the road or if you shake your head sideways it means no. Those two standards will help you through life in many places around the world. But it's dangerous to enforce standards in creativity. I have a son who's started school in Japan, where every kid will paint the sun red. Now that is some fucked up standardisation! Just really messed up on so many levels.

Anyway, I'm not going into that whole 432 Hz vs 440 Hz debate. (BTW: I absolutely love cymatics and I've done some nice workshops for kids with it.) But I will say different frequencies sound different, so why not use that in your music? You got to use whatever feels right and the monologue let's you do exactly that with pitch.

RDJ: Yep.

TT: Talking of standards, the sample rate of 48 kHz is another one for sampling and signal processing, but the volca sample uses a weird one at 31.25 kHz. Purely because of technical constraints, but I was thinking that might be part of the reason you liked it so much, because the different sample rate gives it a unique sound.

RDJ: Haha, yes, it was pretty much the first thing I noticed. Yeah, I thought the 48 kHz, was based on the [Nyquist Theorem](https://web.archive.org/web/20180719052026/https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem). I think it’s double what humans can apparently hear or something, which is another weird one. I don’t know how anybody worked out humans only hear to 20 kHz. I mean even if you can’t hear above 20 kHz, it doesn't mean that your body doesn't feel it. You don’t just experience sound through your eardrums. A good example of this is listening to a recording of your own voice. To almost everyone apart from maybe the most narcissistic, it always sounds weird/thinner/smaller, as you don’t feel the vibration of your chest and body. There are other reasons of course but that’s one for sure. Anyway, I’m into the extremes of the audio spectrum, ultra clarity ’n’ all but I probably prefer fucked-muffled/lo-bit/’70s sound more, ha!

TT: Oh, and when something defies the standard – I just remembered the first time I played a Yamaha SK-10, the faders were all upside down, like max was downwards, even on the volume. I didn't know what was going on and it threw me off at first, but it's actually a bit fun like that and you soon realise it all comes from organ drawbars.

RDJ: I never played the SK-10, but these Calrec mixers I use are like that also, the faders are backwards. There is a little dip switch inside to change it, but I think they have them like that for TV/broadcasting, coz if someone falls asleep at the desk they don’t want them to push all the faders up and distort two million TVs at once… Not surprising they have this safeguard considering how skull numbingly boring most TV is.

TT: Right!! Yeah, but there is a certain feeling to pulling rather than pushing. It's like how an orgasm is "coming" in English, but it's “going” [iku] in Japanese.

RDJ: Never thought of it like that.

TT: I mean, written text in Japanese was traditionally vertical. Although now a lot is westernised and horizontal.

RDJ: Ah, that’s kinda sad… So traditional Japanese text is like trackers and now it’s going like Cubase! :)

TT: I sometimes wonder what Japanese synths would have looked like if they didn't copy Moog in the ’70s. You've got to think about what is convention and what is really a good design.