---
title: "$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol"
url: https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6
clipped: 2026-08-31 12:22:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [$100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol](https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6)

## Digest Summary
The experiment compared two frontier‑level language models—Claude Fable 5 and GPT‑5.6 Sol—in an autonomous music‑video generation task. Each model received the same inputs (the song “Uptown Funk,” a brief description, and a timestamped lyric transcript) and accessed six tools: a planning tool, web search, budget check, image/video generation (via FAL or Replicate), and a local ffmpeg shell for analysis and editing. Four runs were performed (each model at $25 and $100 budgets). Generation spend was $36.57 (Sol $100) and $48.60 (Fable $100); token costs added $3‑4 for Sol and $17‑25 for Fable. All runs produced full‑length videos; three used pure text‑to‑video, while Sol $25 employed an image‑to‑video pipeline and Sol $100 mixed three video models. Common shortcomings included inconsistent characters, literal lyric interpretation, weak tempo matching, and lack of iterative editing. Sol $25 showed the most inventive overlay effects; Fable $100 yielded slightly higher visual coherence but at higher total cost (~$73.65). Both models relied exclusively on FAL for generation. The open‑source arena (github.com/hershalb/music-video-arena) allows replication with custom songs and budgets.

---

## Full Article

[All posts](https://www.tryai.dev/blog)

We built a small agentic harness with one job: hand a model a song, a hard dollar budget, and a set of tools, then get out of the way and let it produce a full music video on its own. The model researches which video models exist, generates clips, watches its own footage, edits with ffmpeg, and assembles a final cut.

A few readers of our [last build-off](https://www.tryai.dev/blog/gpt-5.6-build-off-12-models) said they wanted to see how tool use actually varies between models, so we gave frontier-level models an open-ended, long-horizon task where each model decides on its own what to research, what to generate, and how to edit. We log every tool call, so you can see exactly how each one worked (full transcripts below).

We ran two models, [Claude Fable 5](https://www.tryai.dev/models/claude-fable-5) and [GPT-5.6 Sol](https://www.tryai.dev/models/gpt-5.6-sol), each at two budgets ($25 and $100), for four runs total. Every run got the same song (Bruno Mars and Mark Ronson's "Uptown Funk"), a short text description, and a time-stamped lyric transcript.

## The setup

Each model ran an autonomous tool-calling loop with six tools:

- plan: a tool for thinking (no cost, no action).

- web_search: to research generation models and their APIs and fetch information about music videos (if needed).

- get_budget: to check the remaining budget.

- generate_image and generate_video: the only tools that spend budget. The model can pick any FAL or Replicate model and pass its own parameters.

- run_command: a local shell with ffmpeg/ffprobe available, used to analyze audio, cut and concatenate clips, and mux the final video.

Once the budget hits zero, paid generation is refused, but the model can keep editing. Every model message, tool call, charge, and error was logged. The whole harness is open source at [github.com/hershalb/music-video-arena](https://github.com/hershalb/music-video-arena), so you can run it yourself.

## The four videos

Each clip below is the model's final, self-assembled output.mp4, full length with the original song muxed in.
Claude Fable 5 · $25GPT-5.6 Sol · $25
Claude Fable 5 · $100GPT-5.6 Sol · $100

## The numbers

All four runs finished on their own (none hit a step or time limit) and all four produced a valid, full-length video with the original song muxed in.
ModelBudget↕Wall-clock↕Steps↕Images↕Videos↕Failed calls↕Generation spend↕Output↕Claude Fable 5$2539m10s250541$24.301280x720GPT-5.6 Sol$2542m52s38614610$23.181280x720GPT-5.6 Sol$10049m39s340702$36.571280x720Claude Fable 5$10038m56s280800$48.601920x1080

"Generation spend" is the metered FAL cost, which is what the budget caps. At $25 both models nearly exhausted it. At $100 they spent $36.57 (Sol) and $48.60 (Fable), so more budget did translate into more footage. It does not include the cost of running the model itself, which we add below.

## Time to finished video

## What each model built with

Left to choose their own tools, the models diverged. Three of the four runs went pure text-to-video. Only GPT-5.6 Sol at $25 used an image-to-video pipeline (generating stills first, then animating them). GPT-5.6 Sol at $100 mixed three different video models in a single run.
RunImage modelVideo model(s)ApproachFable 5 · $25noneWan 2.5 t2v ($0.05/s)Text-to-video onlySol · $25FLUX schnell ($0.003/img)Wan 2.2-5b i2v ($0.10/s)Keyframe, then image-to-videoSol · $100noneWan 2.5 ($0.05/s), Veo 3.1 Lite ($0.10/s), Hailuo 2.3 Standard ($0.28/video)Text-to-video, mixed modelsFable 5 · $100noneSeedance 1.0 Pro t2v (~$0.12/s at 1080p)Text-to-video only

Prices are FAL's listed rates, shown per second of output video unless noted. Hailuo 2.3 Standard is priced per video (about $0.28 per 6s clip), and Seedance 1.0 Pro is token-priced (~$0.62 per 5s 1080p clip, shown above as its effective per-second rate). Distinct clips generated per run ranged from 46 to 80.

## Tool usage

How each run spent its tool calls (this counts attempts, including failed generation calls).
Claude Fable 5 · $25GPT-5.6 Sol · $25
Claude Fable 5 · $100GPT-5.6 Sol · $100

Each run's full transcript, every plan, tool call, and command, is here: [Fable 5 · $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/fable-25.txt), [Sol · $25](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/sol-25.txt), [Sol · $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/sol-100.txt), [Fable 5 · $100](https://d1md4c6gq9re9p.cloudfront.net/blog/music-video-arena/transcripts/fable-100.txt).

## Errors along the way

"Failed calls" are generation requests that returned an error (mostly transient network failures to the provider). They were not charged, but the model spent steps retrying them.

## Token usage

RunInput tokensOutput tokensReasoningCached inputFable 5 · $251,476,90044,341n/a0Sol · $252,956,27033,2209,6562,558,029Sol · $1002,097,57231,71512,3301,819,050Fable 5 · $1002,264,61048,029n/a0

## Total cost per run

The budget only meters generation (FAL) spend. Adding the LLM token cost for [Claude Fable 5](https://www.tryai.dev/models/claude-fable-5) ($10 / $50 per 1M input/output) and [GPT-5.6 Sol](https://www.tryai.dev/models/gpt-5.6-sol) ($5 / $30), gives the total cost of each run.
RunGeneration spendLLM token costTotal costFable 5 · $25$24.30$16.99$41.29Sol · $25$23.18$4.27$27.45Sol · $100$36.57$3.25$39.82Fable 5 · $100$48.60$25.05$73.65

For Claude Fable 5, the tokens alone ran $16.99 to $25.05, about 30-40% of each run's total. GPT-5.6 Sol's token cost stayed near $3-4 despite similar token volume.

## Method notes

- Same inputs for all four runs: song, a short text description, and a time-stamped lyric transcript. Each model chose its own generation models on FAL and did its own ffmpeg editing.

- Wall-clock time includes the model's own retries and any waiting on provider queues.

- Generation spend is a best-effort estimate from a per-model price table.

## Try it yourself

The arena is open source: [github.com/hershalb/music-video-arena](https://github.com/hershalb/music-video-arena). Point it at your own song and budget, swap in whichever models you want to pit against each other, and see what they build. Issues and PRs welcome, we would love feedback on the setup.

## Our take

None of the music videos were great, but watching how the models got there was pretty interesting and does show where gaps still clearly exist for frontier-level models. A few things notes:

- Character and story consistency was a struggle for all four. Recurring characters drift between shots, and none of the videos hold a coherent storyline from start to finish.

- The models take lyrics very literally. "Make a dragon wanna retire, man" gets you an actual dragon on screen. It's interesting for a few shots, but got a little weird after a while.

- Tempo matching is weak. The cuts land on the beat (they all ran the ffmpeg beat detection), but the motion inside the clips, dancing, camera moves, rarely matches the song's tempo, so it often feels a little off. An example line "gotta kiss myself I'm so pretty", shows the main character making a kissing motion way too slowly.

- GPT-5.6 Sol at $25 was the most inventive editor. It overlaid text and animated still images with video effects, techniques none of the other runs tried. The rest mostly just stitched generated clips together. GPT 5.6 Sol $100 also tried multiple video models instead of just sticking with one like Fable did.

- Nobody really iterated on the edit. Once clips existed, the models concatenated and muxed, but rarely went back to re-cut or add effects, and none seriously probed their own clips to confirm they were any good. GPT-5.6 Sol's $100 run shipped some genuinely low-quality AI clips, while Claude Fable 5 happened to pick a model with more coherent output. Some of this is probably a model limitation, but the lack of self-review is notable.

- Neither model touched Replicate. Both FAL and Replicate keys were available, but all four runs used FAL exclusively.

- Claude Fable 5 was the pricier pick. It cost more per run (and the most overall, at $73.65) despite finishing faster than GPT-5.6 Sol. Subjectively, we slightly preferred the Fable $100 video, though none blew us away.

- $100 was probably too much budget. Neither model wanted to spend near the cap, and both kept their step counts modest. With that headroom they could have, for example, generated consistent character images up front and animated from those, but neither chose to.

We'll see if models can improve on more subjective/stylistic tasks as they continue to get smarter, but for now there's still a lot of room for improvement.

## Try it yourself

Every model mentioned here is available on TryAI with one account, pay-as-you-go, no subscription.[Start free](https://www.tryai.dev/chat)
