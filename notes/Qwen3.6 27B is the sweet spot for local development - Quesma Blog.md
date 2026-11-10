---
title: "Qwen3.6 27B is the sweet spot for local development - Quesma Blog"
url: https://quesma.com/blog/qwen-36-is-awesome/
clipped: 2026-08-31 12:26:38
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Qwen3.6 27B is the sweet spot for local development - Quesma Blog](https://quesma.com/blog/qwen-36-is-awesome/)

## Full Article

[Skip to main content](https://quesma.com/blog/qwen-36-is-awesome/#main-content)

I’ve been disappointed by local models in the past. But then I checked Qwen3.6, and I was in awe.
For me it’s the first local model that actually makes sense as a general intelligence.

It comes in two variants, a mixture-of-experts model [Qwen3.6 35B A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), and a dense [Qwen3.6 27B](https://huggingface.co/Qwen/Qwen3.6-27B) - slower, but more powerful. The one I recommend!

Let me share my impressions, and show that you can run it too.

Update 27 July 2026 see also our follow-up on its quantizations: [Do Qwen3.6 27B quantizations break the pelican?](https://quesma.com/blog/qwen-quantization-quality/)

It’s hot, literally. When my knees started to melt, I grabbed a phone-attached [thermal
camera](https://github.com/stared/thermal-upscale) and took a photo.

Qwen3.6, rightfully, [got a lot of coverage on Hacker News](https://hn.algolia.com/?dateEnd=1782305498&dateRange=custom&dateStart=1775001600&page=0&prefix=true&query=qwen&sort=byPopularity&type=story). The most common statement about Qwen3.6 27B is that it punches above its weight - see [Will it Mythos?](https://swelljoe.com/post/will-it-mythos/). And I think it is a well-deserved sentiment.
It will make your computer hot, but it’s worth it!

## Testing the waters

Simon Willison uses “a pelican riding a bicycle” as a smoke test (see for [Qwen3.6 35B A3B](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/) and then [Qwen3.6 27B](https://simonwillison.net/2026/Apr/22/qwen36-27b/)). I usually go with constrained writing.

A year ago these kinds of things were state of the art, needing a unique, and insanely expensive GPT-4.5, see [vibe
translating Quantum Flytrap](https://p.migdal.pl/blog/2025/04/vibe-translating-quantum-flytrap/).

I also asked it to write an 8-line poem about Zouk dance and quantum physics, see [the transcript](https://gist.github.com/stared/bac79cd053ea5443abcf58e622c083b7).
The thought process made sense, both in terms of deliberation on quantum terms, and rhymes.

Then I asked in OpenCode to create a hexagonal minesweeper using  `pnpm` . It worked:

It worked on the first go, from a single prompt, with a proper Node package.
The mixture-of-experts Qwen3.6 35B A3B was faster… but ignored my instruction to create a package, and did it in a single  `index.html` .

## Real work

Sure, creative writing about quantum mechanics, or yet another clone of a minesweeper, is rarely a day job.
But Qwen3.6 27B is decent at regular tasks as well.

Prompt by a friend, [Maciej Cielecki](https://cielecki.com/), at [AI Tinkerers
Warsaw](https://poland.aitinkerers.org/).

It worked for a few minutes and created this:

A landing page by Qwen3.6 27B — [view the live page](https://quesma.com/blog/qwen-36-is-awesome/qwen-landing-demo/).

By standards of current frontier models, it’s unremarkable.
But it is already a practical job. It worked, was responsive, defaults were nice - all from a single, short prompt.

## Running Qwen3.6 locally with llama.cpp

Running local models is easier than ever. A few CLI lines and you’re off.

I recommend [llama.cpp](https://github.com/ggml-org/llama.cpp) - a direct, open-source tool that allows running models on various devices. You don’t need Ollama, and frankly - [I would recommend against using that on ethical grounds](https://sleepingrobots.com/dreams/stop-using-ollama/).

First, we go to Hugging Face, to get proper quantization, i.e., a model with reduced size - popular ones are by [unsloth](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF) or [bartowski](https://huggingface.co/bartowski/Qwen_Qwen3.6-27B-GGUF), among others.
Default models usually come with  `BF16`  precision. A common 8-bit quantization saves half the space at almost no cost to quality. Going further down the road, models are smaller (and potentially - faster), but at the cost of quality, see [this comparison for 27B](https://www.reddit.com/r/LocalLLaMA/comments/1tr9vzn/qwen3627b_quantization_benchmark/) and another one for [35B A3B](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/discussions/10).

We grab [unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0](https://huggingface.co/unsloth/Qwen3.6-27B-MTP-GGUF), an 8-bit quantization with support for multi-token prediction (MTP).
 ` `llama-server -hf unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0 \
    --spec-type draft-mtp -ngl 999 -fa on -c 65536 --port 8080` ` 

What it does:

-  `-hf unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0`  grabs from Hugging Face, on the next runs will reuse that

-  `-m ~/models/Qwen3.6-27B-Q8_0.gguf`  use instead if you already have it

-  `draft-mtp`  we use a fast model to predict subsequent tokens, speeds up things

-  `-ngl 999`  for putting all layers to GPU

-  `-fa on`  flash attention is on

-  `-c 65536`  context size set to 64k tokens (this we can tweak, as Qwen3.6 27B native context is 256k)

-  `--port 8080`  better to pin port, as it will be used by other configs

If you open  `http://127.0.0.1:8080` , you can directly chat with it.

Precisely the same server can be used for vibe coding. Choice of agent depends both on one’s goal and subjective taste - for an all-around OpenCode, minimalistic Pi, and self-improving Hermes.

For OpenCode, it is as simple as adding to  `~/.config/opencode/opencode.jsonc` :
 ` `{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "llama": {
      "name": "llama.cpp (local)",
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1",
        "apiKey": "local"
      },
      "models": {
        "qwen3.6-27b": { "name": "Qwen3.6-27B Q8 +MTP" }
      }
    }
  },
  "model": "llama/qwen3.6-27b"
}` ` 

If you just want to chat and are a big fan of Terminal, instead of  `llama-server`  use  `llama-cli` :
 ` `llama-cli -hf unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0 \
    -ngl 999 -fa on -c 65536` ` 

## Measuring performance

Is it fast enough?

I ran a few tests ([source on GitHub](https://github.com/stared/benching-local-llms-on-apple-silicon)) on my MacBook M5 Max 128 GB, running it with and without multi-token prediction, and comparing both with the 35B A3B model, and also a quantized DeepSeek V4 Flash version [DwarfStar4](https://github.com/antirez/ds4).
tokens / sRAMQwen3.6-35B-A3B · 8-bitMLX85 tok/s8537 GB RAM37 GBllama.cpp93 tok/s9344 GB RAM44 GBllama.cpp + MTP105 tok/s10545 GB RAM45 GBQwen3.6-27B · 8-bitMLX17 tok/s1728 GB RAM28 GBllama.cpp18 tok/s1841 GB RAM41 GBllama.cpp + MTP32 tok/s3242 GB RAM42 GBDeepSeek-V4-Flash · Q2–Q4llama.cpp33 tok/s33103 GB RAM103 GB

30 tokens per second is not bad, [well within typical frontier model API range](https://openrouter.ai/openai/gpt-5.5#performance).
While [mlx-lm](https://github.com/ml-explore/mlx-lm) is precisely targeted at Apple silicon devices, and AI agents heavily recommend it, llama.cpp turned out to be faster.
It was using 95% of GPU, which means it is efficiently using available resources.

MacBook M5 Max is a beast (at least for a laptop), but on other devices it should also work decently.
As you can see, both Qwen3.6 variants run within 48 GB of Apple silicon’s shared RAM. A 4-bit quantization is less than 18 GB and should run on a 32 GB device.
On consumer NVIDIA RTX cards, you need to quantize aggressively, but inference runs even faster.

I set this up today on my 5090 at Q6_K quantization and Q4_0 KV, got 50 tokens/s consistently at 123k context, using ~28/32gb vram through LM Studio. - [gfosco on Hacker News](https://news.ycombinator.com/item?id=47871338)

While 35B A3B is 3x faster, I prefer 27B. I’d rather generate a third as much code, but of higher quality.

## How do they relate to previous state-of-the-art models?

Manual inspection is great, but benchmarks help with grounding intuitions. Here is the score from [Artificial Analysis](https://artificialanalysis.ai/), comparing it with frontier models:
Gemma 4 31B29≈ late 2024o1 / Claude 3.5 SonnetQwen3.6-35B-A3B32≈ early 2025o3 / Claude 4 SonnetQwen3.6-27B37≈ mid 2025GPT-5 / Claude Sonnet 4.5DeepSeek-V4-Flash40≈ late 2025GPT-5.2 / Claude Opus 4.5

A few more benchmarks are in [these notes](https://github.com/stared/benching-local-llms-on-apple-silicon), but the spirit is similar.
Added here [Gemma 4 31B](https://deepmind.google/models/gemma/gemma-4/), as a lot of people use this as the default for local coding. But both benchmarks and general sentiment online favor Qwen3.6 27B by a large margin.

Here there is a caveat - 8-bit quantization of Qwen3.6 likely does not affect results much, but DwarfStar4 uses much more aggressive ones for DeepSeek V4 Flash, 2-4 bit. For sure it is worse than the full model.
My personal impression is that within these quantizations Qwen3.6 27B is as good as (or maybe slightly better than) DwarfStar4. Though, I won’t be surprised if for longer-context projects DS4 has an edge.

## What’s next

I think we are entering a fascinating era, when it becomes feasible to run one’s own models.

The change will be propelled further by the state of proprietary frontier models. Claude Fable 5 was taken down. Other frontier models run at a massive subsidy, where paying $100 a month gives us thousands of dollars’ worth of tokens. Let’s use the discount while it lasts!

A locally run model can be fine-tuned to our needs, and cannot be taken away. Businesses can use them for proprietary and sensitive data. We can use them personally for offline projects, or when we don’t feel comfortable sharing our deepest secrets, or medical data, with the US or China.

With the release of [frontier-level open-weight GLM 5.2](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index), there is a new era.
While Qwen3.6 was the stepping stone, even frontier [GLM 5.2 can be run locally](https://unsloth.ai/docs/models/glm-5.2). It won’t run on your MacBook or a single RTX 5090. But still, it is manageable with a company budget.

Moreover, I strongly believe that we will have models smarter than current state of the art, while runnable on local devices, maybe even smartphones. Current models combine both raw intelligence and factual knowledge in the same weights.
Future models will likely separate that, offloading a lot of knowledge to tool calling.

Discuss on [Hacker News](https://news.ycombinator.com/item?id=48721903), [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7477477713050685440/), or [X](https://x.com/pmigdal/status/2071641659289330168).

Previous

### 

[Compare harnesses, not models: Blitzy vs. GPT-5.4 on SWE-Bench ProAn independent audit of agentic scaffolding and harnesses. We analyze how agent workflows, codebase documentation, and test verification impact performance compared to raw base models like GPT-5.4, Gemini 3.1 Pro, and Claude Code.](https://quesma.com/blog/verifying-blitzy-swe-bench-pro/)

Next

### 

[Featured Tokenflation: When “Hi” triggers 33 tool callsTokenflation: simple tasks consuming ever more context, reasoning, and tool calls without more useful output. We benchmarked 14 models; one answered “Hi” with 33 tool calls and an unsolicited commit.](https://quesma.com/blog/tokenflation-when-hi-triggers-33-tool-calls/)

Related

### 

[Do Qwen3.6 27B quantizations break the pelican?We tested Qwen3.6 27B quantizations by Unsloth on Hugging Face, with pelicans on bikes, gears, Terminal-Bench 2.1, and AIME-120.](https://quesma.com/blog/qwen-quantization-quality/)
