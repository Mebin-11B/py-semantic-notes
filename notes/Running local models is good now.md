---
title: "Running local models is good now"
url: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/
clipped: 2026-08-31 12:22:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Running local models is good now](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/)

## Digest Summary
Local models have become practically usable on a 2022 M2 Mac with 64 GB RAM using tools such as llama.cpp, Ollama, LM Studio, and Pi. The author notes a marked improvement since the release of GPT‑OSS, with models now requiring minimal verification against API services. Recent Google Gemma‑4 releases (26B‑A4B and 12B‑QAT) achieve roughly 75 % of frontier model accuracy and speed, enabling tasks like refactoring Python code, linting with type hints, proofreading, generating unit tests, and bootstrapping recommendation systems. The workflow runs in Docker containers for security, using Pi as the agent harness and LM Studio as the inference server; a provided Docker‑Compose configuration connects Pi to the local model endpoint. Limitations remain: slower inference, constrained context windows, and occasional prompt‑template mismatches that are quickly patched. Benefits include full introspection of token processing, adjustable context windows, quantization tweaks, and the ability to compare models directly. The ecosystem is maturing, though the author cautions that it may not yet be production‑ready.

---

## Full Article

# Running local models is good now

Jun 15 2026

I’ve been working [with local models](https://vickiboykis.com/2024/02/28/gguf-the-long-way-around/) since they came out, and finally, they’re surprisingly good now.

I have a 2022 M2 Mac with 64 GB RAM and 1TB storage and I’ve used
- [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/)
- [Gemma 3](https://deepmind.google/models/gemma/gemma-3/)
- [OpenAI OSS-20B](https://huggingface.co/openai/gpt-oss-20b)
- [Qwen 3 MOE](https://huggingface.co/Qwen/Qwen3-30B-A3B), as well as a number of other Qwen variants like [Qwen 2.5 Coder](https://ollama.com/library/qwen2.5-coder)

across [a lot of different system setups](https://vickiboykis.com/2026/05/18/tagging-my-blog-posts-with-bertopic-and-llms/) like
- raw llama.cpp with [Open WebUI](https://github.com/open-webui/open-webui)
- llama-cpp-python
- Ollama
- llamafiles and
- LM Studio

## Where are local models now?

Early on, models were slow, hard to use, and just not that accurate for most programming tasks. The idea that local models were severely lagging behind was largely true until, for me, the release of GPT-OSS. I have no concrete scientific evidence of this - my own personal vibe metric of “is a model good enough” is, “do I have to double-check it against an API model”, and GPT-OSS was the first one where I started doing that a lot less often.

As a result, I’ve mostly been using local models as fast, personalized Google for development questions that don’t require recency.

But with the most recent releases from Google in the [Gemma 4](https://deepmind.google/models/gemma/gemma-4/), family, I’ve finally been able to do agentic coding locally and have loops work at about ~75% the accuracy/speed of frontier models, which is incredible.

I’ve so far been using  `gemma-4-26b-a4b`  [LM Studio implementation](https://lmstudio.ai/models/google/gemma-4-26b-a4b) as my default local model. I’ve used the local setup so far to: Refactor a Python script that was a notebook into a repo of 5-6 modules, [lint that module](https://peps.python.org/pep-0585/) to use correct type hints for generics (most frontier models now do this automatically, but not always).

I’ve also used it to proofread some blog posts, write unit tests, and to bootstrap a repo that stands up a two-tower model for recommendations just to see what the agent would do with a blank slate. Here’s what it generated, which was pretty basic but still beyond the scope of anything I would have thought possible last year:

Note that the environment is restricted because I run all my agentic workflows in a Docker container with limited access to execution.

I’m also building an app that surfaces trending topics from Arxiv papers. Out of curiosity, I had Pi go through my past LM Studio session logs and figure out what I was using LM Studio for:

Unsurprisingly, since I’ve [been working on Rijksearch,](https://vickiboykis.com/2026/04/20/build-yourself-flowers/)

None of these are groundbreaking tasks (again, a lot of personalized Google/docs lookups), and working on them does give my GPUs and RAM a workout and the K-V cache grows to 64 GB RAM.

But, the larger story for me is that these kinds of tasks, even as simple as they are, used to be impossible for local models as recently as 6 months ago.

 `` [Gemma-4-12b-qat](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) just came out but I’ve already also really been impressed with its performance relative to its size. The model architecture itself is [really interesting](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b) and proposes a bunch of interesting questions like, “if we are constrained by performance and price, what architectural tradeoffs do we need to make?” a question that so far has not really been asked in the mad token gold rush.

## Running agentic models locally today

But don’t take my word for any of this, try it out for yourself! You’ll need a local model inference engine, an agentic harness, and the local model artifact if you want to try to run local agentic flows. You’ll need to set up the harness to point at your local inference endpoint, the [downloaded model artifact](https://vickiboykis.com/2024/02/28/gguf-the-long-way-around/) served via the inference engine.

For my local setup, I’m currently using [Pi](https://pi.dev/) as the agent harness and [LM Studio](https://lmstudio.ai/) as the inference server, although it would likely be faster if I just used llama.cpp directly - a potential direction for a future experiment.

[This post was very easy to follow](https://patloeber.com/gemma-4-pi-agent/) to set up agentic coding with Pi and LM Studio, although I did make a few tweaks to the post’s setup.
- Model: The post recommends  `Gemma 26B A4B`  , but  `gemma-4-12b-qat`  is more recent and smaller and faster, without much sacrifice in accuracy.
- Security: I run every Pi session in a Docker container and give it permissions only to bash so that it can’t run Python code or do web browsing, although I do plan to allow curl in a different image for some research work I’m doing.
- Agent Harness Config: Since I run everything in Docker, I edited Pi’s  `models.json`  in order to get Pi to talk to the model. ` `"lmstudio": {
      "baseUrl": "http://host.docker.internal:1234/v1",
      "api": "openai-completions",
      "apiKey": "not-needed",
      "models": [
        {
          "id": "google/gemma-4-12b-qat",
          "input": [
            "text",
            "image"
          ]
        }
      ]
    }
` ` 

Here’s my Docker Compose config: ` `services:
  pi:
    build:
      context: .
      dockerfile: Dockerfile
    image: pi-agent:0.74.0
    init: true
    stdin_open: true
    tty: true
    extra_hosts:
      - "host.docker.internal:host-gateway"
    environment:
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
      OPENAI_API_KEY: ${OPENAI_API_KEY:-not-needed}
      GEMINI_API_KEY: ${GEMINI_API_KEY:-}
      OPENAI_API_BASE: ${OPENAI_API_BASE:-http://host.docker.internal:1234/v1} # note that you'll need to specify a base if you also use OpenAI to access OpenAI's actual completions endpoint
      WHATEVER_API_KEY: ${WHATEVER_API_KEY:-}
    volumes:
      - ${HOME}/.pi/agent/models.json:/config/models.json
      - ${WORKSPACE:-.}:/workspace
      - pi-config:/config
      - pi-sessions:/sessions
    working_dir: /workspace

volumes:
  pi-config:
  pi-sessions:
` ` 

and here’s the bash script that runs  `pi`  . ` `#!/usr/bin/env bash

# Pi — Start the containerized Pi agent.

# Directory containing this script and the compose files.
SCRIPT_DIR="$(cd -- "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Workspace to mount into the container. 
WORKSPACE_DIR="${WORKSPACE:-$(pwd)}"
case "$WORKSPACE_DIR" in
  /*) ;; 
  *)  WORKSPACE_DIR="$(cd -- "$WORKSPACE_DIR" && pwd)" ;; 
esac
export WORKSPACE="$WORKSPACE_DIR"

sandbox="${PI_SANDBOX:-0}"
pi_args=()

while (($#)); do
  case "$1" in

    --sandbox)    sandbox=1 ;;
    --no-sandbox) sandbox=0 ;;
    *)            pi_args+=("$1") ;;

  esac
  shift
done

compose_files=( -f "$SCRIPT_DIR/docker-compose.yml" )
if [[ "$sandbox" == "1" ]]; then
  # an even more secure sandbox
  compose_files+=( -f "$SCRIPT_DIR/docker-compose.sandbox.yml" )
fi

# Derive a container name from the workspace directory's basename.
# Sanitize to characters Docker accepts: [a-zA-Z0-9][a-zA-Z0-9_.-]*
repo_slug="$(basename -- "$WORKSPACE_DIR" | tr -c 'a-zA-Z0-9_.-' '-' | sed 's/^-*//')"
[[ -z "$repo_slug" ]] && repo_slug="workspace"
container_name="pi-${repo_slug}-$$"

api_key_args=(
  -e OPENAI_API_KEY
  -e DEEPSEEK_API_KEY
  -e ANTHROPIC_API_KEY
  -e GEMINI_API_KEY
)

cmd=(
  docker compose
  --project-directory "$SCRIPT_DIR"
  "${compose_files[@]}"
  run --rm
  --name "$container_name"
  "${api_key_args[@]}"
  pi
)

if ((${#pi_args[@]})); then
  cmd+=("${pi_args[@]}")
fi

exec "${cmd[@]}"
` ` 

I build the Docker container and make changes to the files in its own repo. Then, I run Pi in the repo I’m working in, which spins up Docker so that Pi can’t wipe files or directories by acting on my physical hard drive. This also enables Pi running in the container to see my custom model  `json`  config by shipping it into the container. All of this has been working fairly well for my experiments.

There are still issues with local models: inference can be slow, context windows are small and limited to your own hardware, and the ecosystem, although it’s made a ton easier by tooling like LM Studio and HuggingFace’s [Use This Model button](https://huggingface.co/blog/yagilb/lms-hf). Early releases suffer from [prompt template mismatches](https://docs.langchain.com/langsmith/prompt-template-format). But, these are usually patched extremely quickly. Needless to say, I’m not sure this is ready for production software development quite yet.

The benefits, though, are numerous and the ecosystem critical to invest in, particularly now. One of the very cool parts of local models is you can introspect almost everything, like watching the token inference process live,

and watching tokens in/out.

You can do things like change the local context window and watch performance improve or degrade, and really dig into how your tokens are processed on the GPU. You can change the system prompt, the quantizations. You can pit models against each other. You can also change and introspect the harness side.

The possibilities are endless, and the tools only keep getting better.

[#agentic](https://vickiboykis.com/tags/agentic/)
[#llms](https://vickiboykis.com/tags/llms/)
[#ml](https://vickiboykis.com/tags/ml/)
[#local llms](https://vickiboykis.com/tags/local-llms/)
[#open source](https://vickiboykis.com/tags/open-source/)
