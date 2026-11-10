---
title: "Rust implementation of Mistral's Voxtral Mini 4B Realtime runs in your browser"
url: https://github.com/TrevorS/voxtral-mini-realtime-rs
clipped: 2026-06-17 01:47:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Rust implementation of Mistral's Voxtral Mini 4B Realtime runs in your browser](https://github.com/TrevorS/voxtral-mini-realtime-rs)

## Digest Summary
The page refers to a GitHub repository named **TrevorS/voxtral-mini-realtime-rs**. No repository description, code details, or readme content are provided; the site displays the message “You can’t perform that action at this time,” indicating that the requested operation (likely viewing repository contents) was blocked or unavailable. The page includes two visual elements identified only by their alt text: one labeled **HuggingFace**, suggesting an association with the Hugging Face platform or model hub, and another labeled **Live Demo**, implying a demonstration interface or example. No further technical information, usage instructions, licensing, or contribution guidelines are present in the scraped content.

## Discussion Summary
The feedback indicates that the application fails to operate correctly on the user's system, producing garbled output and a runtime error after speaking into the microphone. The user reports the issue occurring on Firefox with Asahi Linux on an M1 Pro device, notes a prolonged processing period before failure, and asks for possible fixes or whether testing on an alternative browser such as Brave might resolve the problem.

---

## Full Article

Voxtral Mini 4B Realtime (Rust)
===============================

[![HuggingFace ASR](https://camo.githubusercontent.com/49e6e0bdf1baecb5e0fece61896fdadd90d7e94e189586acafd2d670cad1b948/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372d4153525f4d6f64656c2d79656c6c6f77)](https://huggingface.co/TrevorJS/voxtral-mini-realtime-gguf)
[![HuggingFace TTS](https://camo.githubusercontent.com/0881294cfd4aa1046a2e9dbac6ebf7908fef38fc34a4e4c0bb476b08b3095316/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462541342539372d5454535f4d6f64656c2d79656c6c6f77)](https://huggingface.co/TrevorJS/voxtral-tts-q4-gguf)
[![ASR Demo](https://camo.githubusercontent.com/4543dac0efcadbafeb18d3976fa698d40bc7f15c94a65795f5cfb952b38c288e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462538452539392545462542382538462d4153525f44656d6f2d626c7565)](https://huggingface.co/spaces/TrevorJS/voxtral-mini-realtime)
[![TTS Demo](https://camo.githubusercontent.com/84d5a69040add1d91750e79db07c03005944c145b5b2c1fa36ea5e9561b7c362/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2546302539462539342538412d5454535f44656d6f2d707572706c65)](https://huggingface.co/spaces/TrevorJS/voxtral-4b-tts)

Streaming speech recognition and text-to-speech running natively and in the browser. A pure Rust implementation of Mistral's [Voxtral Mini 4B Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) (ASR) and [Voxtral 4B TTS](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) models using the [Burn](https://burn.dev) ML framework.

NVIDIA DGX Spark (GB10, LPDDR5x).

16s test audio, 3-run average:

| Path | Encode | Decode | Total | RTF | Tok/s | Memory |
| --- | --- | --- | --- | --- | --- | --- |
| **Q4 GGUF native** | 1021 ms | 5578 ms | 6629 ms | **0.416** | **19.4** | 703 MB |
| BF16 native | 887 ms | 23689 ms | 24607 ms | 1.543 | 4.6 | 9.2 GB |
| Q4 GGUF WASM | — | — | ~225 s | ~14.1 | ~0.5 | (browser) |

* **8.49% WER** on FLEURS English (647 utterances), vs. Mistral's reported 4.90% at f32

"The quick brown fox jumps over the lazy dog" (9 tokens), casual\_female voice:

| Path | Euler Steps | Gen Time | Audio | RTF | Model Size |
| --- | --- | --- | --- | --- | --- |
| **Q4 GGUF native** | 3 | 3.7s | 3.84s | **0.97** | 2.67 GB |
| Q4 GGUF native | 4 | 5.0s | 4.96s | 1.01 | 2.67 GB |
| BF16 native | 3 | 10.4s | 2.72s | 3.82 | ~8 GB |
| BF16 native | 8 | 20.6s | 2.96s | 6.97 | ~8 GB |
| Q4 GGUF WASM | 8 | 367s | 3.52s | 104 | 2.67 GB |

* **RTF** < 1.0 means faster-than-real-time synthesis
* Q4 at 3 Euler steps achieves **real-time** with perfect Whisper large-v3 transcription
* Optimizations: batched CFG (2× → batch=2), fused QKV+gate/up projections, pre-allocated KV cache
* Q4 model load: 3.9s native, 9.2s WASM (including shard download over localhost)
* 20 preset voices across 9 languages. Use `--euler-steps` to tune speed/quality tradeoff

* Custom WGSL compute shaders with vectorized u32 reads and vec4 dot products
* Dual-path kernel dispatch: shared-memory tiled kernel for single-token decode, naive kernel for multi-row encode/prefill
* Q4 GGUF (2.5 GB ASR, 2.67 GB TTS) runs entirely client-side in a browser tab via WASM + WebGPU

Try the demos: [ASR (speech-to-text)](https://huggingface.co/spaces/TrevorJS/voxtral-mini-realtime) | [TTS (text-to-speech)](https://huggingface.co/spaces/TrevorJS/voxtral-4b-tts)

```
# Download ASR model weights (~9 GB BF16 or ~2.5 GB Q4)
uv run --with huggingface_hub \
  hf download mistralai/Voxtral-Mini-4B-Realtime-2602 --local-dir models/voxtral
uv run --with huggingface_hub \
  hf download TrevorJS/voxtral-mini-realtime-gguf --local-dir models/

# Transcribe audio (BF16 or Q4)
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- \
  transcribe --audio audio.wav --model models/voxtral
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- \
  transcribe --audio audio.wav --gguf models/voxtral-q4.gguf
```

```
# Build WASM package
wasm-pack build --target web --no-default-features --features wasm

# Generate self-signed cert (WebGPU requires secure context)
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 \
  -keyout /tmp/voxtral-key.pem -out /tmp/voxtral-cert.pem \
  -days 7 -nodes -subj "/CN=localhost"

# Start dev server
bun serve.mjs
```

Open `https://localhost:8443`, accept the certificate, and click **Load from Server** to download the model shards. Record from your microphone or upload a WAV file to transcribe.

Hosted demos: [ASR on HuggingFace Spaces](https://huggingface.co/spaces/TrevorJS/voxtral-mini-realtime) | [TTS on HuggingFace Spaces](https://huggingface.co/spaces/TrevorJS/voxtral-4b-tts)

```
# Download TTS model weights (~8 GB BF16 or ~2.67 GB Q4)
uv run --with huggingface_hub \
  hf download mistralai/Voxtral-4B-TTS-2603 --local-dir models/voxtral-tts
uv run --with huggingface_hub \
  hf download TrevorJS/voxtral-tts-q4-gguf voxtral-tts-q4.gguf --local-dir models

# Synthesize speech (BF16 or Q4)
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- \
  speak --text "Hello world" --voice casual_female
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- \
  speak --text "Hello world" --voice casual_female --gguf models/voxtral-tts-q4.gguf

# Real-time with 3 Euler steps
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- \
  speak --text "Hello world" --gguf models/voxtral-tts-q4.gguf --euler-steps 3

# List available voices
cargo run --release --features "wgpu,cli,hub" --bin voxtral -- speak --list-voices
```

20 preset voices across 9 languages. The TTS pipeline runs backbone (Ministral 3B) autoregressive decoding, flow-matching acoustic prediction, and codec synthesis to produce 24 kHz audio.

```
Audio (16kHz mono)
  -> Mel spectrogram [B, 128, T]
    -> Causal encoder (32 layers, 1280 dim, sliding window 750)
      -> Conv 4x downsample -> Reshape [B, T/16, 5120]
        -> Adapter [B, T/16, 3072]
          -> Autoregressive decoder (26 layers, 3072 dim, GQA 32Q/8KV)
            -> Token IDs -> Text
```

|  | BF16 (native) | Q4 GGUF (native + browser) |
| --- | --- | --- |
| Weights | SafeTensors (~9 GB) | GGUF Q4\_0 (~2.5 GB) |
| Linear ops | Burn tensor matmul | Custom WGSL shader (fused dequant + matmul) |
| Embeddings | f32 tensor (1.5 GiB) | Q4 on GPU (216 MB) + CPU bytes for lookups |
| Browser | No | Yes (WASM + WebGPU) |

The upstream mistral-common library left-pads audio with 32 silence tokens (at 12.5 Hz). After the mel/conv/reshape pipeline, this covers only 16 of the 38 decoder prefix positions with silence — the remaining 22 contain actual audio. The f32 model handles this fine, but Q4\_0 quantization makes the decoder sensitive to speech content in the prefix: audio that starts immediately with speech (mic recordings, clips with no leading silence) produces all-pad tokens instead of text.

The left padding is increased to 76 tokens, which maps to exactly 38 decoder tokens of silence and covers the full streaming prefix. See [`src/audio/pad.rs`](https://github.com/TrevorS/voxtral-mini-realtime-rs/blob/main/src/audio/pad.rs) for details.

Running a 4B model in a browser tab required solving five hard constraints:

1. **2 GB allocation limit** — `ShardedCursor` reads across multiple `Vec<u8>` buffers
2. **4 GB address space** — Two-phase loading: parse weights, drop reader, then finalize
3. **1.5 GiB embedding table** — Q4 embeddings on GPU + CPU-side row lookups
4. **No sync GPU readback** — All tensor reads use `into_data_async().await`
5. **256 workgroup invocation limit** — Patched cubecl-wgpu to cap reduce kernel workgroups

```
# Native (default features: wgpu + native-tokenizer)
cargo build --release

# With all features
cargo build --release --features "wgpu,cli,hub"

# WASM
wasm-pack build --target web --no-default-features --features wasm
```

| Feature | Description |
| --- | --- |
| `wgpu` (default) | GPU backend via Burn/CubeCL (WebGPU, Vulkan, Metal) |
| `native-tokenizer` (default) | Tekken BPE encoding via tiktoken (WASM-compatible) |
| `wasm` | Browser support: wasm-bindgen, WebGPU device init, JS bindings |
| `cli` | CLI binary with clap + indicatif |
| `hub` | HuggingFace Hub model downloads |

```
# Unit + integration tests (requires GPU for full suite)
cargo test --features "wgpu,cli,hub"

# Lint
cargo clippy --features "wgpu,cli,hub" -- -D warnings
cargo clippy --no-default-features --features wasm --target wasm32-unknown-unknown -- -D warnings

# E2E browser test (requires Playwright + model shards)
bunx playwright test tests/e2e_browser.spec.ts
```

GPU-dependent tests (model layer shapes, Q4 matmul, WGSL shader correctness) are skipped in CI since GitHub Actions runners lack a GPU adapter. These tests run locally on any machine with Vulkan, Metal, or WebGPU support.

### Q4 GGUF Sharding (for browser)

GGUF files must be split into shards of 512 MB or less to stay under the browser's `ArrayBuffer` limit:

```
# ASR shards
split -b 512m models/voxtral-q4.gguf models/voxtral-q4-shards/shard-

# TTS shards (quantize first, then shard)
uv run --with safetensors --with torch --with numpy --with packaging \
  scripts/quantize_tts_gguf.py models/voxtral-tts/ -o models/voxtral-tts-q4.gguf
split -b 512m models/voxtral-tts-q4.gguf models/voxtral-tts-q4-shards/shard-
```

The dev server discovers shards from `models/voxtral-q4-shards/` (ASR) and `models/voxtral-tts-q4-shards/` (TTS).

```
src/
  audio/          # Mel spectrogram, chunking, resampling, padding
  models/         # BF16 model: encoder, decoder, adapter, attention, RoPE, KV cache
  gguf/           # Q4 GGUF: reader, loader, model, tensor, WGSL shader, tests
  web/            # WASM bindings: VoxtralQ4, initWgpuDevice, async decode loop
  tts/            # TTS pipeline: backbone, flow matching, codec, voice presets
  tokenizer/      # Tekken tokenizer: decode (ASR) + encode (TTS via tiktoken)
  bin/transcribe  # ASR CLI binary
  bin/speak       # TTS CLI binary

web/              # Browser demo: index.html, worker.js, voxtral-client.js
tests/            # Integration tests + Playwright E2E spec
scripts/          # Dev scripts: reference implementations, weight inspection, E2E helpers
patches/          # cubecl-wgpu workgroup size fix for WebGPU
```

Apache-2.0