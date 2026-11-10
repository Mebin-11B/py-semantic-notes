---
title: "Audio is the one area small labs are winning"
url: https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai
clipped: 2026-06-17 01:45:00
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Audio is the one area small labs are winning](https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai)

## Digest Summary
Gradium, spun out of the open‑source audio lab Kyutai, has built Moshi, a 7‑billion‑parameter full‑duplex conversational audio model that operates with ~160 ms latency, can interrupt, back‑channel, and change voice style in real time, and runs on mobile devices. The model was trained from scratch in six months by a four‑researcher team, using 7 M hours of audio with transcripts, 2 000 h of phone‑conversation data (Fisher), and 20 k+ h of synthetic dialogue for instruction fine‑tuning. Key technical contributions include:

* Multi‑stream modeling: separate user and machine audio streams enable simultaneous speaking and turn‑taking.  
* Mimi neural codec (derived from Google’s SoundStream): a universal encoder‑decoder that compresses speech, music, and general audio, producing combined semantic and acoustic tokens (1 semantic + 6 acoustic per timestep) for causal generation.  
* Efficient training: audio models are far smaller than large language models (7 B vs. >400 B parameters), reducing compute and data requirements, allowing small, expert teams to outperform larger labs.  

Gradium leverages these innovations to deliver production‑ready, multilingual voice AI APIs, positioning audio as a core future AI modality.

## Discussion Summary
Comments highlight that audio machine‑learning remains hindered more by insufficient signal‑processing knowledge and preprocessing practices than by compute or data volume, creating a niche where expertise yields strong opportunities. Practitioners note persistent difficulties such as reliable end‑of‑utterance detection, speaker variability, and latency constraints, leading some to adopt push‑to‑talk solutions. There is criticism of large organizations for lacking focus on audio, mixed views on emerging tools, and acknowledgment of ethical and legal complexities in domains like porn and music. Overall sentiment is cautiously optimistic about future advances contingent on deeper domain understanding.

---

## Full Article

> Disclosure: Amplify is an investor in Gradium.

If AI research is Star Wars and OpenAI is the death star, then without a doubt the rebels are building audio models. The best models for voice – TTS, STS, STT, and the like – are *not* coming from the big labs. Instead, they’re built by their underfunded, understaffed, and underhyped siblings, a wave of incredible startups that is improbably crushing benchmarks with every model release. And if you believe that audio is the biggest future modality for AI – like many researchers do – this is one of the more interesting and underdiscussed topics in genAI today.

One of these improbably cutting edge startups is [Gradium](https://gradium.ai/), born out of the open lab [Kyutai](https://kyutai.org/).

In summer 2024 on a stage in Paris, a Kyutai researcher (his name is Neil) demoed [the first realtime audio conversation with AI](https://www.youtube.com/live/hm2IJSKcYvo?si=hROZHbpKekVV7e7N&t=460). This model (Moshi) could respond in real time, change its voice style and volume on request, and even recite an original poem in a French accent (research shows poems sound better this way).

You’ve probably seen audio AI demos before. You may not be particularly impressed. Didn’t OpenAI do this a few years ago? Well, not exactly:

1. This was the [first full-duplex conversational AI model](https://moshi.chat/). Moshi could interrupt, be interrupted, backchannel ("uh-huh", "I see") and respond in around 160ms (faster than most human conversations).
2. This demo happened *before* OpenAI released Advanced Voice Mode, and a full year before xAI released a similar demo (with more latency).

This would have been a groundbreaking release from a major lab, except it wasn’t from a major lab, it was from a core team of 4 (four) researchers who built it completely from scratch (without a pre-trained base) in 6 months. The model is open source, and can even run on mobile. Oh, and the team was part of a non-profit with extremely limited funding. [How did they do it?](https://www.youtube.com/watch?v=Z7Bm_faK5Ic)

Based on extensive interviews with the Gradium team, this post is going to go in technical depth on an incredibly interesting niche of the increasingly top heavy AI world:

* A brief history of audio ML, and why it’s consistently overlooked
* Dynamics of big labs and why small teams of researchers can outperform
* Anatomy of training a voice AI model, and how it differs from text
* Core Gradium / Kyutai research: full-duplex models, audio codecs, oh my!

Let’s get to it.

**A brief history of audio ML, and why it’s consistently overlooked**
---------------------------------------------------------------------

If you watch any science fiction movie — [2001: A Space Odyssey](https://youtu.be/Wy4EfdnMZ5g?si=spQD0VynHgNpT4lI&t=19), [Her](https://youtu.be/dJTU48_yghs?si=1gITIq1nW_vHjTTI&t=32) and [Iron Man](https://youtu.be/EfmVRQjoNcY?si=wGAUDGh13ovx-Zfs&t=7) or incessantly invoked — the colloquial AI speaks in a distinctly natural, human-sounding voice. One simply needs to ask Siri what time it is (it took 5 seconds for me this morning) to realize how far away from this ideal our devices can be.

There’s an obvious question here: *how did we let it get this bad?* Why are we only now starting to see meaningful advances in audio AI, while text has been rapidly improving every single year since 2020?

This problem is actually foundational. For *years* audio has occupied the bottom tier of AI/ML’s informal coolness hierarchy. If you were around this scene pre-GPT, there was a clear ranking of what it was cool to work on. At the top was image classification via CNNs, which was for a while the most promising real world application of AI. Then came ML on tabular data, then text, and audio was somewhere all the way towards the bottom. For several reasons *audio just wasn’t sexy*1.

There are practical reasons for this gap: training data for audio is genuinely scarce compared to text. You can scrape trillions of tokens from Wikipedia, Stack Overflow, books, and papers. High-quality conversational audio is harder to come by, and much of it isn’t particularly informative. A Stack Overflow answer (usually) teaches you something, but a typical phone conversation is mostly filler. And generating audio is much more complex than predicting text tokens, requiring real domain expertise to execute effectively.

But there’s also a cultural problem here. In the mid-2010s, when deep learning was taking off for images and starting to work for text, audio felt impossibly hard. Neural networks were doing cool things with photos. Maybe they’d eventually be okay at writing. Very, very few people conceived that one day, audio could have realtime conversations with proper turn-taking and expressiveness. Siri put a laughably bad voice assistant in everyone’s pocket…is it possible we slowly internalized defeat?

This was undoubtedly true at larger labs. When Neil (Kyutai co-founder and Gradium CEO) was hired at Google Brain in 2019, he was one of a very small group working on voice. Management considered voice to be a “solved problem.” Meanwhile, projects like Meta’s [Seamless](https://github.com/facebookresearch/seamless_communication) and Google’s various speech initiatives shipped models, published papers, then languished. These repos haven’t been updated in years!

All of this created an opportunity. When you have a hard technical problem that’s been underfunded and underexplored, and yet has promise to be *the* core modality if things go right2, a few researchers who actually understand the domain can move incredibly fast. And they did.

**Dynamics of big labs and why small teams of researchers can outperform**
--------------------------------------------------------------------------

When Neil joined Facebook AI Research for his PhD in 2015 there was a clear social hierarchy among AI research:

* Research **scientists** were the “idea guys” — with prestigious academic backgrounds, working on theoretical problems, and rarely touching code3.
* Research **engineers** implemented those ideas in code and with machines. They knew how to get theory into software and hardware.

In quite a turn from SF culture today, the scientists almost universally had higher prestige and better compensation4.

Then deep learning happened, and the hierarchy completely inverted. Ideas became very cheap because Neural nets are universal approximators, and are essentially very dumb. A lot of research became “what can we throw Deep Learning at” and the hard problems were moving down the stack: training efficiently, managing distributed systems, etc. Now the engineers were in charge!

The researchers who thrived in this new climate — people like Noam Shazeer at Google — were actually both of these people. They could have the architectural insight *and* implement it themselves5.

> *“The biggest scam in big companies is thinking that you can lead a research organization without doing research yourself, just by being an ‘idea guy’. The only way to understand what is possible, what is challenging, how we should allocate resources, is to understand every single detail to the deepest level.”*

The priority now was less how creative your idea is, and more what you can realize as a tangible outcome of an idea. And critically, this did not necessarily require massive compute budgets and teams. In a sense (perhaps a very weak sense) this was the AWS moment for startups…but for AI research. Not to mention that getting GPUs in the cloud was now a few clicks (if your clicks were fast enough).

This is the crux of why big labs *still* don’t dominate in audio like they do in text. Small groups of research engineers are able to completely outclass their larger, better staffed and funded competitors because they move fast, build their own ideas, and don’t have to deal with the incessant big lab politics that you are reading about every day on X.

Not only that, but as we’ll see, audio is a completely different beast than text. It is *not* just about scaling compute and data. There are a million little edges to creating elite audio models, from correct turn taking to backchanneling and managing latency, that require deep domain expertise. Great audio models are trained by great audio researchers, and throwing money at the problem will only get you mediocrity.

All the Gradium cofounders (Neil + [Alex Défossez](https://www.linkedin.com/in/alexandre-d%C3%A9fossez-b099ba7b/), [Olivier Teboul](https://www.linkedin.com/in/olivier-teboul-800364103/), and [Laurent Mazaré](https://www.linkedin.com/in/laurent-mazare-ab01a53/)) worked around some combination of these labs, absolutely cooking in relative obscurity in their underfunded audio divisions. It was a fun time in Paris. Alex was working on mathematical optimization but DJing on the side. They started building an AI-based synthesizer for fun.

*NOT Neil and Alex.*

The first thing Neil did at Google Brain was work on audio compression, building the very first neural audio codec – [SoundStream](https://arxiv.org/abs/2107.03312). Better compression led Neil and Olivier to train the first model that could generate audio by predicting compressed tokens. After one week, they ran an experiment: “I passed three seconds of my voice to the model, and it kept talking in my voice.” (They had accidentally invented voice cloning). Every audio project at Google Brain started using this framework, which became the foundation for [Gemini Live](https://gemini.google/overview/gemini-live/).

Essentially, here was a small group of some of the best audio researchers on the planet all connected and working at big labs. It was only a matter of time…

Thus [Kyutai](https://kyutai.org/) in 2023 was born and all of our characters united. It was the first and is the only open audio lab, named for the Japanese word for “sphere.” In fact their two major model releases also carry Japanese names:

Kyutai is open because Neil and his cofounders believe in open research, and as competitive pressure between labs was intensifying, fewer and fewer papers were being published. With funding from Eric Schmidt and two French billionaires, they started cooking.

In addition to the above, Kyutai has released open source text-to-speech and speech-to-text models — the foundation for [NVIDIA’s PersonaPlex](https://research.nvidia.com/labs/adlr/personaplex/) and [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS). Their real-time speech-to-speech translation (you can check out the demo below) was running on-device many months before Apple’s.

All of this is nice, but mostly research as research. Kyutai models are fundamentally prototypes, and real apps need much more polished models. So part of the Kyutai team started Gradium to bridge that last mile between research and product, and [raised $70M to do it](http://google.com/search?q=gradium+funding&rlz=1C5GCCM_en&oq=gradium+fun&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIKCAIQABiABBiiBDIHCAMQABjvBTIHCAQQABjvBTIKCAUQABiABBiiBDIKCAYQABiABBiiBNIBCDIwODlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8). You can think of this as a sort of pipeline from fundamental Kyutai research into production-grade products via Gradium. And in a few short months, they built and shipped multi-lingual models that compete with the best in class.

**Anatomy of training an audio model**
--------------------------------------

When it comes to training audio is both like text and not like text.

To start with the similarities, most SOTA audio models use architectures that are pretty similar to text, e.g. they’re Transformer-based among other things. The nice thing about borrowing LLM architectures is you benefit from all of the advances in text over the past few years, RLHF techniques, distillation, and the hardware out there optimized for LLMs.

But unlike text that has the internet corpus, there is not a huge treasure trove of available high quality audio data. And what “audio data” even *means* is a moving target, because what exactly do you want to train on: labeled transcribed conversations? Translations of a single speaker’s voice? Conversations with multiple participants?  Peruse through the typical open datasets and test sets for audio AI ([Voxpopuli](https://github.com/facebookresearch/voxpopuli), [MADLAD-400](https://arxiv.org/abs/2309.04662), [NTREX](https://github.com/MicrosoftTranslator/NTREX)) and you can get a sense of how much more disjointed this is than text.

Audio models are also very small compared to LLMs. Moshi, Kyutai’s foundation audio model, has 7B parameters and was trained on only 2.1T tokens. As a result they tend to *know* a lot less ground information than a typical LLM.

All-in-all Moshi was:

* Pretrained on 7M hours of audio with transcripts.
* Post-trained on the Fisher dataset (2000 hours of phone conversations with separated channels).
* Instruction finetuned on 20k+ hours of synthetic dialogue.

One of the hardest parts of training these models, especially when it comes to reward functions in post-training, is the subjective nature of evaluations. This problem is [well documented](https://www.amplifypartners.com/barrchives/how-suno-builds-ai-models-for-musicians) in the music generation space. Good conversations are completely subjective! Neil and co. completely gave up on quantitative measures and only trusted humans, doing tons of blind tests and just listening (they also supplement their efforts with freelancers).

**Audio model architectures: speech-to-speech vs. full duplex**
---------------------------------------------------------------

One of the hardest problems to solve in audio AI has been the **turn taking problem**. How do you effectively trade conversation with an unpredictable user?When is the user done talking, and when are they just thinking? How do you handle interruptions? Should the model ever interrupt the user, and if so when? (The model should just [read Dale Carnegie](https://www.goodreads.com/book/show/4865.How_to_Win_Friends_Influence_People), duh.) It turns out it’s really hard to nail this dynamic, and among audio researchers it’s thought of as one of the most challenging problems in the space.

Accordingly, you will see “speech-to-speech” thrown around a lot, but not all S2S models are created equal.

Today’s OpenAI models are *technically* speech-to-speech, but they are **turn-based**. They are trained to understand (predict) when the user is finished talking or asking their question, which sounds reasonable enough, but ends up creating weird dynamics. For example, if you (the user) are silent for a few seconds because you’re thinking about the right formulation, the model is going to talk even though you didn’t want it to. It also cannot interrupt you (even though sometimes it should), and until recent editions, it was impossible to interrupt the model itself. This is like talking to someone on a walkie talkie, fun but ultimately not quite the real thing.

**Full duplex** models, on the other hand, are like being on the phone. It’s more like a real conversation, where the model interacts with you dynamically, you can both interrupt each other, and it’s more intelligent when it comes to interpreting your intent. These models are proficient at backchanneling (“aha, yes, I see, mhm”) which tends to make the conversation more lively and natural feeling.

You can see (hear?) this idea in action by talking to [Moshi](http://moshi.chat/), Kyutai’s realtime audio foundation model they released last year. It was the first realtime audio model on the planet, almost miraculously built by a non-profit team of four with a budget that was orders of magnitude smaller than the big labs. It’s a little rough around the edges, but the experience is pretty incredible.

Kyutai [pioneered this full duplex architecture](https://arxiv.org/abs/2410.00037), and to build it required a few clever research ideas.

### **Multi-stream modeling**

First, instead of modeling the conversation as one audio stream – the user’s – they model it with **two**, one for the user and one for the machine. When the machine isn’t *speaking*, it’s producing silence (or backchanneling) in the stream. This means that both can be active at the same time (or one active and one inactive), unlike turn based architectures. It’s an extremely simple architectural idea but it mostly solves turn taking, which is arguably the most challenging problems in dialogue / audio AI.

The full duplex architecture ended up being useful for more than just basic realtime audio generation. Kyutai’s second model family [Hibiki](https://kyutai.org/blog/2025-02-10-hibiki) uses the same idea to realtime translate audio into another language…using the speaker’s exact voice. It's [one of my favorite demos](https://kyutai.org/blog/2025-02-10-hibiki) I’ve seen in a while.

Bidirectional audio, especially when you introduce multilinguality, is incredibly difficult. For example…where are you going to find data of the same person in the same voice saying the same thing in multiple different languages? Gradium’s approach here is called DSM (Delayed Streams Modeling) and though it’s beyond the scope of this post, you can [read about it here](https://arxiv.org/abs/2509.08753).

### **Audio codecs and Mimi**

Second, which I mentioned earlier, is their SOTA codec called Mimi, based on earlier research from Neil at Google ([SoundStream](https://arxiv.org/abs/2107.03312)). This one requires a bit of background, so bear with me.

Codec is short for encoder-decoder and it’s how you compress audio data into something a model can use; you can think of it like embeddings but for audio6. Codecs are in a sense modular, and there are specific ones developed for different types of audio like [music](https://en.wikipedia.org/wiki/Comparison_of_audio_coding_formats) or [speech](https://en.wikipedia.org/wiki/Category:Speech_codecs). There are *tons* of these, and they implement very manual, bespoke rules that we know about the specific medium. Accordingly you can’t use a speech codec for music and vice versa. They also output completely different bitrates based on the target application. These are very bad qualities if you’re trying to train a model.

Neil’s idea while he was at Google Brain was instead to just train a model to do this. This work culminated in [SoundStream](https://arxiv.org/abs/2107.03312), a neural codec that can compress speech, music, *and* general audio at bitrates normally targeted by speech-only codecs. It worked pretty much just as well as domain-specific codecs with all of these ergonomic benefits, and was a big deal in the field at the time.

Another vein of research that Olivier and Neil worked on at Google, [AudioLM](https://research.google/blog/audiolm-a-language-modeling-approach-to-audio-generation/), introduced an even more novel idea for the model’s compression system. When it comes to audio there are two types of tokens researchers deal with:

1. **Semantic tokens** – these represent *the content* of what’s being said, the words and what they mean.
2. **Acoustic tokens** – these represent *the acoustic style* of what’s being said, how the voice sounds, emotion, etc.

Previous work in the space modeled these two tokens separately using a hierarchical approach, starting with the semantic (content) and then moving onto the acoustic (style). But prevailing open models for generating these semantic tokens are **non-causal** (like [WavLM](https://arxiv.org/abs/2110.13900)) and so they absolutely do not work in real time. It needs future audio to compute the current embedding.

Kyutai’s approach – and how they solved the real time problem – is by *combining* these two types of tokens into a *single generation process*, thanks to some fancy footwork on summing vector quantizations. When Moshi generates speech it produces 8 tokens per timestep: token 1 is a semantic token, and 2-7 are acoustic tokens. The whole causal system processes audio as it arrives and is thus able to generate all tokens (semantic + acoustic) in real-time.

Reading Kyutai papers, you can’t help but get this frenetic sense of depth. Most of the AI stuff I read on Arxiv has 1-3 fundamental ideas that enable whatever new architecture the paper is about. But **Kyutai papers have like 13**. For the Moshi paper I’m skipping over innovations in generation (Temporal+Depth transformers), differing weights on token loss, their Inner Monologue method…it’s hard to keep up.

All of this fancy work results in latency (at least theoretically) of 160ms, which is lower than the typical 200-250ms you’d expect in a human conversation. Talking to Moshi you can see that in some senses it’s even *too* fast.

**Why small teams win at audio**
--------------------------------

If you want to distill the story of Gradium (and other audio labs) and why startups continue to beat big labs at audio, it's this:

### **1) Audio models are much smaller and cheaper to train than text models**

Moshi has 7B parameters and was trained on 2.1T tokens. Llama 3.1 has 405B parameters trained on 15T tokens—that’s orders of magnitude of difference in cost. You don’t need a thousand people or a massive compute cluster. You need a few exceptional people who understand the domain deeply.

### **2) Audio requires genuine domain expertise in a way text doesn’t**

A text tokenizer is essentially a dictionary – you break words into subword tokens and you’re done. An audio codec like Mimi relies on deep understanding of how human hearing works, acoustic psychophysics, how to balance compression against perceptual quality. The bitter lesson is like…not so bitter here.

Similarly, if you’re training a multimodal model, you’re constantly compromising—more coding data means less audio data. Voice is always negotiating with text, video, and image teams for model capacity and training budget. At a focused lab, there's no compromise. Everything optimizes for audio.

### **3) Audio innovation is still about clever ideas efficiently executed, not just scale**

The full duplex architecture that Kyutai pioneered is a simple idea (model both streams simultaneously) but it solved the turn-taking problem that had stumped researchers for years. The Mimi codec’s technique for combining semantic and acoustic tokens uses novel compression rather than brute force. The opportunity in audio AI is that “very few people just need to focus on the right questions”.

Gradium is taking all of this and bringing it to the people in real, production-ready models that you can actually use to build things. You can chat with their models [on their site](https://gradium.ai/), and look through [their API docs here](https://gradium.ai/api_docs.html). But most importantly...**may the voice be with you**.