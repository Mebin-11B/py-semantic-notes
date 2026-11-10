---
title: "Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon"
url: https://github.com/RunanywhereAI/rcli
clipped: 2026-06-17 01:34:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon](https://github.com/RunanywhereAI/rcli)

## Digest Summary
RCLI is an on‑device voice‑AI suite for macOS (Apple Silicon, macOS 13+). It integrates speech‑to‑text (VAD + Zipformer/Whisper/Parakeet), a local large language model (Qwen3, LLM 3 B, LFM2 series) with KV‑cache, Flash Attention, and text‑to‑speech (Piper, Kokoro, etc.) into a single Metal‑GPU pipeline (MetalRT) that runs natively on M3/M3 Pro/M3 Max/M4 chips; M1/M2 fallback to llama.cpp. End‑to‑end latency is sub‑200 ms, with STT up to 714 × real‑time and LLM throughput ≈550 tokens / s. The tool exposes 38 macOS actions (AppleScript or shell) such as app control, media playback, reminders, and screen capture, reachable via voice or typed commands in an interactive TUI. RCLI also provides on‑device RAG: documents (PDF/DOCX/TXT) are indexed with hybrid vector + BM25 (≈4 ms over 5 k+ chunks) and queried via voice. Installation is via Homebrew or curl script; models (~1 GB total) are downloaded once. MetalRT is proprietary (license via [email protected]); RCLI code is MIT‑licensed.

## Discussion Summary
The comments present a mixed view: many express enthusiasm for the on‑device AI demo and its potential, while others highlight practical problems such as instability, high latency, missing features, and limited macOS support. Concerns recur about a leaked API key, unclear licensing of the proprietary engine, and the company’s alleged spam practices. Users are confused about whether the tool is a voice assistant, a general‑purpose LLM, or a RAG system, and request broader model selection, diarization, and better integration. Overall interest is tempered by skepticism over security, legality, and usability.

---

## Full Article

[![RCLI Waveform](https://github.com/RunanywhereAI/RCLI/raw/main/assets/rcli_waveform.gif)](https://github.com/RunanywhereAI/RCLI/blob/main/assets/rcli_waveform.gif)
  
**Talk to your Mac, query your docs, no cloud required.**
  
  
[![macOS](https://camo.githubusercontent.com/c9411b4859cd08394ca4e74a3613f6262cc87e7d86d920be0f988be76e66cad1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d6d61634f532d626c7565)](https://github.com/RunanywhereAI/RCLI)
[![Apple Silicon](https://camo.githubusercontent.com/23ff775bfb5ea47f1b54ad2ed824037e402f19c2318f625bdbb8664a5defcd41/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636869702d4170706c655f53696c69636f6e2d626c61636b)](https://github.com/RunanywhereAI/RCLI)
[![Local](https://camo.githubusercontent.com/336d5e961adf1728bfb263a65e5be9fa3e791325b44d1e46e9b5b0dd628bf28a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f696e666572656e63652d3130302532355f6c6f63616c2d677265656e)](https://github.com/RunanywhereAI/RCLI)
[![MIT](https://camo.githubusercontent.com/b8cadaa967891081f8f165695470689986c028821dd8a040132f6e661795dc0d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c7565)](https://github.com/RunanywhereAI/RCLI/blob/main/LICENSE)

**RCLI** is an on-device voice AI for macOS. A complete STT + LLM + TTS + VLM pipeline running natively on Apple Silicon — 40 macOS actions via voice, local RAG over your documents, on-device vision (camera & screen analysis), sub-200ms end-to-end latency. No cloud, no API keys.

Powered by [MetalRT](https://github.com/RunanywhereAI/rcli#metalrt-gpu-engine), a proprietary GPU inference engine built by [RunAnywhere, Inc.](https://runanywhere.ai) specifically for Apple Silicon.

> Real-time screen recordings on Apple Silicon — no cloud, no edits, no tricks.

|  |  |
| --- | --- |
| **Voice Conversation**  *Talk naturally — RCLI listens, understands, and responds on-device.*   [Voice Conversation Demo](https://youtu.be/qeardCENcV0)  Click for full video with audio | **App Control**  *Control Spotify, adjust volume — 38 macOS actions by voice.*   [App Control Demo](https://youtu.be/eTYwkgNoaKg)  Click for full video with audio |
| **Models**  *Browse models, hot-swap LLMs — all from the TUI.*   [Models & Benchmarks Demo](https://youtu.be/HD1aS37zIGE)  Click for full video with audio | **Document Intelligence (RAG)**  *Ingest docs, ask questions by voice — ~4ms hybrid retrieval.*   [RAG Demo](https://youtu.be/8FEfbwS7cQ8)  Click for full video with audio |

> [IMPORTANT]
> **Requires macOS 13+ on Apple Silicon. MetalRT engine requires M3 or later.** M1/M2 Macs fall back to llama.cpp automatically.

**One command:**

```
curl -fsSL https://raw.githubusercontent.com/RunanywhereAI/RCLI/main/install.sh | bash
```

**Or via Homebrew:**

```
brew tap RunanywhereAI/rcli https://github.com/RunanywhereAI/RCLI.git
brew install rcli
rcli setup          # required — downloads AI models (~1GB, one-time)
```

**Upgrade to latest:**

```
brew update
brew upgrade rcli
```

**Troubleshooting: SHA256 mismatch or stale version**

If `brew install` or `brew upgrade` fails with a checksum error:

```
# Force-refresh the tap to pick up the latest formula
cd $(brew --repo RunanywhereAI/rcli) && git fetch origin && git reset --hard origin/main
brew reinstall rcli
```

If that doesn't work, clean re-tap and clear the download cache:

```
brew untap RunanywhereAI/rcli
rm -rf "$(brew --cache)/downloads/"*rcli*
brew tap RunanywhereAI/rcli https://github.com/RunanywhereAI/RCLI.git
brew install rcli
rcli setup
```

```
rcli                             # interactive TUI (push-to-talk + text)
rcli listen                      # continuous voice mode
rcli ask "open Safari"           # one-shot command
rcli ask "play some jazz on Spotify"
rcli vlm photo.jpg "what's in this image?"  # vision analysis
rcli camera                      # live camera VLM
rcli screen                      # screen capture VLM
rcli metalrt                     # MetalRT GPU engine management
rcli llamacpp                    # llama.cpp engine management
```

[![MetalRT vs llama.cpp decode speed](https://github.com/RunanywhereAI/RCLI/raw/main/assets/decode-vs-llamacpp.webp)](https://github.com/RunanywhereAI/RCLI/blob/main/assets/decode-vs-llamacpp.webp)
  
*MetalRT decode throughput vs llama.cpp and Apple MLX on Apple M3 Max*

[![STT and TTS real-time factor comparison](https://github.com/RunanywhereAI/RCLI/raw/main/assets/rtf_comparison.webp)](https://github.com/RunanywhereAI/RCLI/blob/main/assets/rtf_comparison.webp)
  
*STT and TTS real-time factor — lower is better. MetalRT STT is 714x faster than real-time.*

For More info :

A full STT + LLM + TTS pipeline running on Metal GPU with three concurrent threads:

* **VAD** — Silero voice activity detection
* **STT** — Zipformer streaming + Whisper / Parakeet offline
* **LLM** — Qwen3 / LFM2 / Qwen3.5 with KV cache continuation and Flash Attention
* **TTS** — Double-buffered sentence-level synthesis (next sentence renders while current plays)
* **Tool Calling** — LLM-native tool call formats (Qwen3, LFM2, etc.)
* **Multi-turn Memory** — Sliding window conversation history with token-budget trimming

Analyze images, camera captures, and screen regions using on-device vision-language models. VLM runs on the llama.cpp engine via Metal GPU — no cloud.

* **Image Analysis** — `rcli vlm photo.jpg "describe this"` for single-image queries
* **Camera** — Press **V** in the TUI or run `rcli camera` for live camera analysis
* **Screen Capture** — Press **S** in the TUI or run `rcli screen` to analyze screen regions
* **Models** — Qwen3 VL 2B, Liquid LFM2 VL 1.6B, SmolVLM 500M — download on demand via `rcli models vlm`

> **Note:** VLM is currently available on the llama.cpp engine. MetalRT VLM support is coming soon.

Control your Mac by voice or text. The LLM routes intent to actions executed locally via AppleScript and shell commands.

| Category | Examples |
| --- | --- |
| **Productivity** | `create_note`, `create_reminder`, `run_shortcut` |
| **Communication** | `send_message`, `facetime_call` |
| **Media** | `play_on_spotify`, `play_apple_music`, `play_pause`, `next_track`, `set_music_volume` |
| **System** | `open_app`, `quit_app`, `set_volume`, `toggle_dark_mode`, `screenshot`, `lock_screen` |
| **Web** | `search_web`, `search_youtube`, `open_url`, `open_maps` |

Run `rcli actions` to see all 40, or toggle them on/off in the TUI Actions panel.

> **Tip:** If tool calling feels unreliable, press **X** in the TUI to clear the conversation and reset context. With small LLMs, accumulated context can degrade tool-calling accuracy — a fresh context often fixes it.

Index local documents, query them by voice. Hybrid vector + BM25 retrieval with ~4ms latency over 5K+ chunks. Supports PDF, DOCX, and plain text.

```
rcli rag ingest ~/Documents/notes
rcli ask --rag ~/Library/RCLI/index "summarize the project plan"
```

A terminal dashboard with push-to-talk, live hardware monitoring, model management, and an actions browser.

| Key | Action |
| --- | --- |
| **SPACE** | Push-to-talk |
| **V** | Camera — capture and analyze with VLM |
| **S** | Screen — capture and analyze a screen region with VLM |
| **M** | Models — browse, download, hot-swap LLM/STT/TTS/VLM |
| **A** | Actions — browse, enable/disable macOS actions |
| **R** | RAG — ingest documents |
| **X** | Clear conversation and reset context |
| **T** | Toggle tool call trace |
| **ESC** | Stop / close / quit |

MetalRT is a high-performance GPU inference engine built by [RunAnywhere, Inc.](https://runanywhere.ai) specifically for Apple Silicon. It delivers the fastest on-device inference for LLM, STT, and TTS — up to **550 tok/s** LLM throughput and sub-200ms end-to-end voice latency.

> **Apple M3 or later required.** MetalRT uses Metal 3.1 GPU features available on M3, M3 Pro, M3 Max, M4, and later chips. M1/M2 support is coming soon. On M1/M2, RCLI automatically falls back to the open-source llama.cpp engine.

MetalRT is automatically installed during `rcli setup` (choose "MetalRT" or "Both"). Or install separately:

```
rcli metalrt install
rcli metalrt status
```

**Supported models:** Qwen3 0.6B, Qwen3 4B, Llama 3.2 3B, LFM2.5 1.2B (LLM) · Whisper Tiny/Small/Medium (STT) · Kokoro 82M with 28 voices (TTS)

MetalRT is distributed under a [proprietary license](https://github.com/RunanywhereAI/metalrt-binaries/blob/main/LICENSE). For licensing inquiries: [founder@runanywhere.ai](mailto:founder@runanywhere.ai)

RCLI supports 20+ models across LLM, STT, TTS, VLM, VAD, and embeddings. All run locally on Apple Silicon. Use `rcli models` to browse, download, or switch.

**LLM:** LFM2 1.2B (default), LFM2 350M, LFM2.5 1.2B, LFM2 2.6B, Qwen3 0.6B, Qwen3.5 0.8B/2B/4B, Qwen3 4B

**STT:** Zipformer (streaming), Whisper base.en (offline, default), Parakeet TDT 0.6B (~1.9% WER)

**TTS:** Piper Lessac/Amy, KittenTTS Nano, Matcha LJSpeech, Kokoro English/Multi-lang

**VLM:** Qwen3 VL 2B, Liquid LFM2 VL 1.6B, SmolVLM 500M — on-demand download via `rcli models vlm` (llama.cpp engine only)

**Default install** (`rcli setup`): ~1GB — LFM2 1.2B + Whisper + Piper + Silero VAD + Snowflake embeddings. VLM models are downloaded on demand.

```
rcli models                  # interactive model management
rcli models vlm              # download/manage VLM models
rcli upgrade-llm             # guided LLM upgrade
rcli voices                  # browse and switch TTS voices
rcli cleanup                 # remove unused models
```

CPU-only build using llama.cpp + sherpa-onnx (no MetalRT):

```
git clone https://github.com/RunanywhereAI/RCLI.git && cd RCLI
bash scripts/setup.sh
bash scripts/download_models.sh
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -j$(sysctl -n hw.ncpu)
./rcli
```

All dependencies are vendored or CMake-fetched. Requires CMake 3.15+ and Apple Clang (C++17).

**CLI Reference**

```
rcli                          Interactive TUI (push-to-talk + text + trace)
rcli listen                   Continuous voice mode
rcli ask <text>               One-shot text command
rcli vlm <image> [prompt]     Analyze an image with VLM
rcli camera [prompt]          Live camera capture + VLM analysis
rcli screen [prompt]          Screen capture + VLM analysis
rcli actions [name]           List actions or show detail
rcli rag ingest <dir>         Index documents for RAG
rcli rag query <text>         Query indexed documents
rcli models [llm|stt|tts|vlm] Manage AI models
rcli voices                   Manage TTS voices
rcli metalrt                  MetalRT GPU engine management
rcli llamacpp                 llama.cpp engine management
rcli setup                    Download default models
rcli info                     Show engine and model info

Options:
  --models <dir>      Models directory (default: ~/Library/RCLI/models)
  --rag <index>       Load RAG index for document-grounded answers
  --gpu-layers <n>    GPU layers for LLM (default: 99 = all)
  --ctx-size <n>      LLM context size (default: 4096)
  --no-speak          Text output only (no TTS)
  --verbose, -v       Debug logs
```

Contributions welcome. See [CONTRIBUTING.md](https://github.com/RunanywhereAI/RCLI/blob/main/CONTRIBUTING.md) for build instructions and how to add new actions, models, or voices.

RCLI is open source under the [MIT License](https://github.com/RunanywhereAI/RCLI/blob/main/LICENSE).

MetalRT is proprietary software by [RunAnywhere, Inc.](https://runanywhere.ai), distributed under a separate [license](https://github.com/RunanywhereAI/metalrt-binaries/blob/main/LICENSE).

Built by [RunAnywhere, Inc.](https://www.runanywhere.ai)