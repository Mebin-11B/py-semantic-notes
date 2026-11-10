---
title: "Jimi Hendrix was a systems engineer"
url: https://spectrum.ieee.org/jimi-hendrix-systems-engineer
clipped: 2026-06-17 01:39:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Jimi Hendrix was a systems engineer](https://spectrum.ieee.org/jimi-hendrix-systems-engineer)

## Digest Summary
Jimi Hendrix’s 3 Feb 1967 “Purple Haze” session used a custom Octavia pedal (Roger Mayer) alongside a Fuzz Face, wah‑wah, Marshall 100‑W amp and studio acoustics. The author reproduced the full analog signal chain in ngspice, modeling guitar pickups (6 kΩ, 2.5 H) and cable capacitance, and simulated both germanium and silicon Fuzz Face variants. Key findings: • Fuzz Face is a low‑impedance (≈20 kΩ) two‑transistor feedback amp that turns sinusoidal input into near‑square‑wave fuzz; reducing guitar volume restores a sinusoid (“cleanup effect”). • Octavia’s rectifier flips waveform troughs, effectively doubling frequency content and adding a bright octave‑up harmonic. • Wah‑wah functions as a sweepable band‑pass filter (≈300 Hz → 2 kHz), producing vowel‑like articulations. • Uni‑Vibe cascades four phase‑shift sections modulated by photoresistors, adding low‑frequency motion. • Driving the Marshall near saturation and exploiting room‑coupled acoustic feedback extends sustain and creates controllable oscillation modes. All circuit schematics, ngspice files, and Python scripts are publicly available on GitHub (nahorov/Hendrix-Systems-Lab). The work reframes Hendrix’s tone as an engineered, reproducible system.

## Discussion Summary
The comments show generally positive appreciation for the article’s exploration of Hendrix’s use of feedback and the interplay between engineering and musical expression, with several readers highlighting historical examples, modern effects, and the instrument’s expressive potential. At the same time, a notable minority point out factual inconsistencies, such as mismatched diagrams, mislabeled images, and unclear explanations of technical symbols, and some extend the discussion to broader topics like curriculum relevance and other artists’ experimental gear. Overall, the feedback balances admiration for the content with calls for greater technical precision.

---

## Full Article

3 February 1967 is a day that belongs in the annals of music history. [It’s the day that Jimi Hendrix](https://www.jimihendrix.com/) entered London’s [Olympic Studios](https://en.wikipedia.org/wiki/Olympic_Studios) to record a song using a new component. The song was “[Purple Haze](https://www.youtube.com/watch?v=WGoDaYjdfSg),” and the component was the Octavia guitar pedal, created for Hendrix by sound engineer [Roger Mayer](https://www.roger-mayer.co.uk/). The pedal was a key element of a complex chain of analog elements responsible for the final sound, including the [acoustics](https://spectrum.ieee.org/tag/acoustics) of the studio room itself. When they sent the tapes for remastering in the [United States](https://spectrum.ieee.org/tag/united-states), the sounds on it were so novel that they included an accompanying note explaining that the distortion at the end was not malfunction but intention. A few months later, Hendrix would deliver his [legendary electric guitar](https://www.youtube.com/watch?v=P-IRA5UrZ7g) performance at the Monterey International Pop Festival.

“Purple Haze” firmly established that an electric guitar can be used not just as a stringed instrument with built-in pickups for convenient sound amplification, but also as a full-blown wave synthesizer whose output can be manipulated at will. Modern guitarists can reproduce Hendrix’s chain using separate plug-ins in [digital audio](https://spectrum.ieee.org/tag/digital-audio) workstation software, but the magic often disappears when everything is buffered and quantized. I wanted to find out if a more systematic approach could do a better job and provide insights into how Hendrix created his groundbreaking sound.

My fascination with Hendrix’s Olympic Studios’ performance arose because there is a “Hendrix was an alien” narrative surrounding his musical innovation—that his music appeared more or less out of nowhere. I wanted to replace that narrative with an engineering-driven account that’s inspectable and reproducible—plots, models, and a signal chain from the guitar through the pedals that you can probe stage by stage.

![Four plots showing magnitudes plotted against time and frequency.](https://spectrum.ieee.org/jimi-hendrix-systems-engineer) Each effects pedal in Hendrix’s chain contributed to enhancing the electric guitar beyond its intrinsic limits. A selection of plots from the full-circuit analysis shows how the Fuzz Face turns a sinusoid signal from a string into an almost square wave; how the Octavia pedal inverts half the input waveform to double its frequency; how the wah-wah pedal acts as band-pass filter; and how the Uni-Vibe pedal introduces selective phase shifts to color the sound.James Provost/ Rohan S. Puranik

Although I work mostly in the digital domain as an edge-computing architect in my day job, I knew that analog circuit simulations would be the key to going deeper.

My first step was to look at the challenges Hendrix was trying to address. Before the 1930s, guitars were too quiet for large ensembles. Electromagnetic pickups—coils of wire wrapped around magnets that detect the vibrations of metal strings—fixed the loudness problem. But they left a new one: the **envelope**, which specifies how the amplitude of a note varies as it’s played on an instrument, starting with a rising initial **attack**, followed by a falling **decay**, and then any **sustain** of the note after that. Electric guitars attack hard, decay fast, and don’t sustain like bowed strings or organs. Early manufacturers tried to modify the electric guitar’s characteristics by using hollow bodies fitted with magnetic pickups, but the instrument still barked more than it sang.

Hendrix’s mission was to reshape both the electric guitar’s envelope and its tone until it could feel like a human voice. He tackled the guitar’s constraints by augmenting it. His solution was essentially a modular analog signal chain driven not by knobs but by hands, feet, gain staging, and physical movement in a feedback field.

Hendrix’s setups are well documented: Set lists, studio logs, and interviews with Mayer and Eddie Kramer, then the lead engineer at Olympic Studios, fill in the details. The signal chain for “Purple Haze” consisted of a set of pedals—a [Fuzz Face](https://en.wikipedia.org/wiki/Fuzz_Face), the Octavia, and a[wah-wah](https://en.wikipedia.org/wiki/Wah-wah_pedal)—plus a [Marshall 100-watt amplifier](https://mopop.emuseum.com/objects/100504/marshall-super-lead-amplifier-formerly-owned-by-jimi-hendrix) stack, with the guitar and room acoustics closing a feedback loop that Hendrix tuned with his own body. Later, Hendrix would also incorporate a [Uni-Vibe](https://en.wikipedia.org/wiki/Uni-Vibe) pedal for many of his tracks. All the pedals were commercial models except for the [Octavia](https://www.roger-mayer.co.uk/octavia.htm), which Mayer built to produce a distorted signal an octave higher than its input.

Hendrix didn’t speak in decibels and ohm values, but he collaborated with engineers who did.

I obtained the schematics for each of these elements and their accepted parameter ranges, and converted them into [netlists](https://en.wikipedia.org/wiki/Netlist) that [ngspice](https://ngspice.sourceforge.io/) can process (ngpsice is an [open source](https://spectrum.ieee.org/tag/open-source) implementation of the Spice circuit analyzer). The Fuzz Face pedal came in two variants, using [germanium](https://spectrum.ieee.org/germanium-can-take-transistors-where-silicon-cant) or silicon [transistors](https://spectrum.ieee.org/tag/transistors), so I created models for both. In my models, Hendrix’s guitar pickups had a resistance of 6 kiloohms and an inductance of 2.5 henrys with a realistic cable capacitance.

I chained the circuit simulations together using a script, and I produced data-plot and sample sound outputs with [Python](https://spectrum.ieee.org/tag/python) scripts. All of the ngspice files and other scripts are available in my [GitHub](https://spectrum.ieee.org/tag/github) repository at[github.com/nahorov/Hendrix-Systems-Lab](https://github.com/nahorov/Hendrix-Systems-Lab), with instructions on how to reproduce my simulations.

What Does The Analysis of Hendrix’s Signal Chain Tell Us?
---------------------------------------------------------

Plotting the signal at different points in the chain with different parameters reveals how Hendrix configured and manipulated the nonlinear complexities of the system as a whole to reach his expressive goals.

A few highlights: First, the Fuzz Face is a two-transistor feedback amplifier that turns a gentle sinusoid signal into an almost binary “fuzzy” output. The interesting behavior emerges when the guitar’s volume is reduced. Because the pedal’s input impedance is very low (about 20 kΩ), the pickups interact directly with the pedal circuit. Reducing amplitude restores a sinusoidal shape—producing the famous “[cleanup effect](https://www.youtube.com/shorts/XJdw_KrUN2w)” that was a hallmark of Hendrix’s sound, where the fuzz drops in and out as desired while he played.

![A photograph of three young men beside a recording studio mixing desk.](https://spectrum.ieee.org/jimi-hendrix-systems-engineer) Engineer Eddie Kramer, Jimi Hendrix, and studio manager Jim Marron at the Electric Lady Studios in [New York City](https://spectrum.ieee.org/tag/new-york-city).Fred W. McDarrah/Getty Images

Second, the Octavio pedal used a rectifier, which normally converts alternating to [direct current](https://spectrum.ieee.org/tag/direct-current). Mayer realized that a rectifier effectively flips each trough of a waveform into a peak, doubling the number of peaks per second. The result is an apparent doubling of frequency—a bloom of second-harmonic content that the ear hears a bright octave above the fundamental.

Third, the wah-wah pedal is a band-pass filter: Frequency plots show the center frequency sweeping from roughly 300 hertz to 2 kilohertz. Hendrix used it to make the guitar “talk” with vowel sounds, most iconically on “[Voodoo Child](https://www.youtube.com/watch?v=C0XwPUFfFwE) (Slight Return).”

Fourth, the Uni-Vibe cascades four phase-shift sections controlled by photoresistors. In circuit terms, it’s a low-frequency oscillator modulating a variable-phase network; in musical terms it’s motion and air.

Finally, the whole chain became a closed loop by driving the [Marshall amplifier near saturation](https://spectrum.ieee.org/the-cool-sound-of-tubes), which among other things extends the sustain. In a reflective room, the guitar strings couple acoustically to the speakers—move a few centimeters and you shift from one stable feedback mode to another. To an engineer, this is a gain-controlled acoustic feedback system. To Hendrix, it was part of the instrument. He learned to tune oscillation with distance and angle, shaping sirens, bombs, and harmonics by walking the edge of instability.

Hendrix didn’t speak in decibels and ohm values, but he collaborated with engineers who did—Mayer and Kramer—and iterated fast as a systems engineer. Reframing Hendrix as an engineer doesn’t diminish the art. It explains how one person, in under four years as a bandleader, could pull the electric guitar toward its full potential by systematically augmenting the instrument’s shortcomings for maximum expression.

*This article appears in the March 2026 print issue as “Jimi Hendrix, Systems Engineer.”*

*A correction to this article was made on 27 Feb 2026 to correctly identify the men posing with Jimi Hendrix in the recording studio.*

From Your Site Articles

Related Articles Around the Web