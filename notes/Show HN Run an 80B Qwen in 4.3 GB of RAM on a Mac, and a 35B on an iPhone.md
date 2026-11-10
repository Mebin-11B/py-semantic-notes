---
title: "Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone"
url: https://github.com/leonickson1/Swiftlet
clipped: 2026-08-31 12:22:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone](https://github.com/leonickson1/Swiftlet)

## Digest Summary
Swiftlet is a Swift + Metal runtime that enables Qwen3‑Next and Qwen3.5/3.6 Mixture‑of‑Experts (MoE) models (35 B and 80 B) to run on Apple Silicon devices, including iPhones. It retains only the dense core (attention, DeltaNet projections, routers, shared experts, embeddings) in RAM—≈1.3 GB (35 B) or 2.5 GB (80 B) at 4‑bit quantization—while streaming routed expert weights from SSD on demand via a fixed‑stride .qpack container. Each token activates ≈3 B parameters: the 35 B model routes to 8 of 256 experts, the 80 B to 10 of 512. A bounded LFU + recency cache mitigates miss penalties; Apple SSDs absorb the remaining latency. The forward pass runs entirely on Metal with runtime‑compiled shaders, using Gated DeltaNet linear attention (no growing KV cache). Swiftlet provides:

Swift package (SwiftletCore) for macOS/iOS integration  
CLI tools (swiftlet chat, swiftlet generate, swiftlet-repack)  
Loopback OpenAI‑compatible server (swiftlet-server)  
Open‑source iOS app (Priv AI) for on‑device chat  

Models validate against mlx‑lm reference implementations; the project builds on ~10 k lines of Swift/Metal and is Apache 2.0 licensed. Requirements: Apple Silicon, macOS 14+/iOS 17+, 18 GB (35 B) or 42 GB (80 B) SSD space.

---

## Full Article

[Skip to content](https://github.com/leonickson1/Swiftlet#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [leonickson1](https://github.com/leonickson1)    
    /
    
      [Swiftlet](https://github.com/leonickson1/Swiftlet)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fleonickson1%2FSwiftlet)    You must be signed in to change notification settings

  

  
- 
          [Fork
    29](https://github.com/login?return_to=%2Fleonickson1%2FSwiftlet)
  

  
- 
        
        [Star
          576](https://github.com/login?return_to=%2Fleonickson1%2FSwiftlet)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/leonickson1/Swiftlet/branches)[Tags](https://github.com/leonickson1/Swiftlet/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[29 Commits](https://github.com/leonickson1/Swiftlet/commits/main/)29 Commits

## Folders and files

NameNameLast commit messageLast commit date[Sources](https://github.com/leonickson1/Swiftlet/tree/main/Sources)[Sources](https://github.com/leonickson1/Swiftlet/tree/main/Sources)  [Tests](https://github.com/leonickson1/Swiftlet/tree/main/Tests)[Tests](https://github.com/leonickson1/Swiftlet/tree/main/Tests)  [assets/model-configs](https://github.com/leonickson1/Swiftlet/tree/main/assets/model-configs)[assets/model-configs](https://github.com/leonickson1/Swiftlet/tree/main/assets/model-configs)  [fixtures](https://github.com/leonickson1/Swiftlet/tree/main/fixtures)[fixtures](https://github.com/leonickson1/Swiftlet/tree/main/fixtures)  [references](https://github.com/leonickson1/Swiftlet/tree/main/references)[references](https://github.com/leonickson1/Swiftlet/tree/main/references)  [scripts](https://github.com/leonickson1/Swiftlet/tree/main/scripts)[scripts](https://github.com/leonickson1/Swiftlet/tree/main/scripts)  [.gitignore](https://github.com/leonickson1/Swiftlet/blob/main/.gitignore)[.gitignore](https://github.com/leonickson1/Swiftlet/blob/main/.gitignore)  [IPHONE.md](https://github.com/leonickson1/Swiftlet/blob/main/IPHONE.md)[IPHONE.md](https://github.com/leonickson1/Swiftlet/blob/main/IPHONE.md)  [LICENSE](https://github.com/leonickson1/Swiftlet/blob/main/LICENSE)[LICENSE](https://github.com/leonickson1/Swiftlet/blob/main/LICENSE)  [PLAN.md](https://github.com/leonickson1/Swiftlet/blob/main/PLAN.md)[PLAN.md](https://github.com/leonickson1/Swiftlet/blob/main/PLAN.md)  [Package.resolved](https://github.com/leonickson1/Swiftlet/blob/main/Package.resolved)[Package.resolved](https://github.com/leonickson1/Swiftlet/blob/main/Package.resolved)  [Package.swift](https://github.com/leonickson1/Swiftlet/blob/main/Package.swift)[Package.swift](https://github.com/leonickson1/Swiftlet/blob/main/Package.swift)  [README.md](https://github.com/leonickson1/Swiftlet/blob/main/README.md)[README.md](https://github.com/leonickson1/Swiftlet/blob/main/README.md)  [THIRD_PARTY_NOTICES.md](https://github.com/leonickson1/Swiftlet/blob/main/THIRD_PARTY_NOTICES.md)[THIRD_PARTY_NOTICES.md](https://github.com/leonickson1/Swiftlet/blob/main/THIRD_PARTY_NOTICES.md)  View all files

## Repository files navigation

# Swiftlet

Run 35B and 80B Qwen models on ordinary Apple devices, including iPhones.

Swiftlet is a Swift + Metal runtime for the Qwen3-Next and Qwen3.5/3.6 MoE
hybrid model family. It keeps only the small dense core of a model resident in
memory and streams the routed Mixture-of-Experts weights from storage on
demand. The result:

Model
Disk
Peak RAM
Decode speed (M5 Mac)

[Qwen3.6-35B-A3B, 4-bit](https://huggingface.co/Leonickson/Qwen3.6-35B-A3B-qpack)
18 GB
2.6 GB
7 to 11 tok/s

[Qwen3.6-35B-A3B, 8-bit](https://huggingface.co/Leonickson/Qwen3.6-35B-A3B-8bit-qpack)
34 GB
7.6 GB
3.5 to 4 tok/s

[Qwen3-Next-80B-A3B, 4-bit](https://huggingface.co/Leonickson/Qwen3-Next-80B-A3B-qpack)
42 GB
4.3 GB
4.5 to 5 tok/s

Those figures are on an M5. For a low end reference, on a base M1 (8-core GPU,
16 GB) the 4-bit 35B decodes at about 2.5 tok/s and the 8-bit at about 1.7
tok/s, with prefill running at that same speed. On so few GPU cores the decode
loop is fully compute bound, so the expert cache is a memory knob rather than a
speed one there:  `--cache-gb 2`  matches  `--cache-gb 8`  while saving several GB
of RAM, which is the better setting on a 16 GB machine. Thanks to @Avicennasis
for the measurements (#18).

The 8-bit 35B is the quality tier for Macs: tested head to head on identical
prompts, it removes the repetition artifacts the 4-bit build can show on
longer writing tasks, at the cost of disk, RAM, and speed.

The 35B also runs on an iPhone 17 in about 2.5 GB of RAM, at about 1 tok/s
today. Credit where due: [ANEMLL](https://www.anemll.com/) showed a 397B
MoE streaming on an iPhone 17 Pro as a proof of concept in early 2026.
Swiftlet's aim is the next step, making this class of model an installable
app on a base iPhone, with an open runtime anyone can build on.

Status: working end to end. Both models generate correct, validated output.
The current focus is kernel speed (the decode loop is dispatch bound, not
IO bound, so there is clear headroom). One expectation to set honestly: only
about 3B parameters are active per token, so these models chat and write
like large models but recall facts like small ones.

## Quick start: try it on a Mac

 `git clone https://github.com/leonickson1/Swiftlet.git && cd Swiftlet
swift build -c release

# Download the 35B container from the R2 mirror (fast and consistent;
# Hugging Face throttles anonymous downloads harder the longer they run):
.build/release/swiftlet-repack \
  --from-url https://pub-c0cfece2dbc340dbb2cd9d94310a7d68.r2.dev/qwen3.6-35b-qpack \
  --output ~/models/qwen3.6-35b.qpack

# Or the 80B (42 GB on disk, still only ~4.3 GB of RAM):
.build/release/swiftlet-repack \
  --from-url https://pub-c0cfece2dbc340dbb2cd9d94310a7d68.r2.dev/qwen3-next-80b-qpack \
  --output ~/models/qwen3-next-80b.qpack

# Or the 8-bit 35B (best writing quality, 34 GB disk, ~7.6 GB RAM):
.build/release/swiftlet-repack \
  --from-url https://pub-c0cfece2dbc340dbb2cd9d94310a7d68.r2.dev/qwen3.6-35b-8bit-qpack \
  --output ~/models/qwen3.6-35b-8bit.qpack

# The same containers are on Hugging Face (anonymous downloads are
# rate-limited there, so the mirror is usually much faster):
#   --from-hf Leonickson/Qwen3.6-35B-A3B-qpack
#   --from-hf Leonickson/Qwen3.6-35B-A3B-8bit-qpack
#   --from-hf Leonickson/Qwen3-Next-80B-A3B-qpack

# Verify a finished download against the source hashes (optional):
#   python3 scripts/verify_container.py <base-url or org/repo> <container-dir>

# Chat (applies the model chat template, disables the reasoning block,
# keeps conversation state so follow-ups prefill only the new turn):
.build/release/swiftlet chat ~/models/qwen3.6-35b.qpack \
  "What is the capital of Spain?" "And what about France?"

# One-shot generation with stats:
.build/release/swiftlet generate ~/models/qwen3.6-35b.qpack \
  --gpu --chat --prompt "Explain expert streaming in one paragraph."

# OpenAI-compatible server (loopback only):
.build/release/swiftlet-server --model ~/models/qwen3.6-35b.qpack --port 8080` 

The same command also repacks raw MLX checkpoints
( `--from-hf mlx-community/...`  or  `--source /path/to/checkpoint` ).

Requirements: Apple Silicon, macOS 14+ or iOS 17+, free SSD space for the
container (18 GB for the 35B, 34 GB for the 8-bit 35B, 42 GB for the 80B).

## Try it on your phone

The 35B runs on iPhone inside
[Priv AI on the App Store](https://apps.apple.com/us/app/priv-ai/id6765706001):
open Settings, then Experimental Models, and download the model. It streams
from storage and chats on-device with no server involved.

The Experimental Models feature ships in the newest app version, which is
still in App Store review, so it may not appear for a couple of days. If you
want the phone experience today, build the app from source: the app is open
source at [leonickson1/localLLM](https://github.com/leonickson1/localLLM).
Clone this repo next to it as  `swiftlet` , open the Xcode project, and run it
on your iPhone.

## How it works

These models activate only about 3B of their parameters per token. Each layer
routes every token to 10 of 512 experts (80B) or 8 of 256 (35B). Swiftlet:

- keeps the dense weights resident: attention, DeltaNet projections, routers,
shared experts, embeddings. About 1.3 GB (35B) or 2.5 GB (80B) at 4-bit;

- repacks the tens of thousands of routed experts into fixed-stride blobs in
a  `.qpack`  container, so fetching one expert is exactly one  `pread`  from
SSD, no mmap and no page-cache thrash;

- caches hot experts in a bounded pool with LFU plus recency eviction. Cache
size barely affects speed (measured 43 to 70 percent hit rates at the same
throughput), because Apple SSDs absorb the misses;

- runs the whole forward pass on Metal with runtime-compiled shaders, so no
Metal toolchain is needed at build time and the same code ships on iOS.

75 percent of the layers use Gated DeltaNet linear attention with a
fixed-size recurrent state, so there is no growing KV cache for those layers
at any context length.

## Four ways to use it

Swiftlet is a library first:

- The Swift package. Add SwiftletCore to any macOS or iOS app and use
 `SwiftletSession`  for chat with streaming deltas, conversation caching,
sampling with repetition control, and memory-pressure handling built in.

- The CLI.  `swiftlet chat`  and  `swiftlet generate`  for local use and
benchmarking,  `swiftlet-repack`  to build containers from MLX checkpoints
(including streaming straight from Hugging Face with resume).

- The server.  `swiftlet-server`  speaks the OpenAI chat-completions API
on loopback, so any chat UI that talks to OpenAI-compatible endpoints can
use a streamed local model.

- An app. [Priv AI](https://apps.apple.com/us/app/priv-ai/id6765706001)
on iOS embeds SwiftletCore as its streamed-model engine. End users tap
Download and chat. Nothing here is terminal-only. The app itself is open
source at [leonickson1/localLLM](https://github.com/leonickson1/localLLM)
if you want to build it yourself (clone this repo next to it as
 `swiftlet` ).

## Correctness

Every layer of the forward pass (Gated DeltaNet recurrence, gated GQA
attention, sparse MoE routing) is validated against mlx-lm reference
implementations with per-layer fixtures, in f32 and int4 quantized form.
Incremental decoding is verified against whole-sequence processing. Metal
kernels are tested against the exact CPU reference, and the fast and scalar
GPU kernels are verified to produce identical outputs. Containers are
byte-verifiable against their source checkpoints. Streaming placement never
changes model semantics: an expert answers identically from cache or disk.
 `swift test` 

The test suite uses [Swift Testing](https://developer.apple.com/documentation/testing),
which ships with the full Xcode toolchain (Xcode 16+) and with Swift.org
toolchains. If  `swift build`  succeeds but  `swift test`  fails with
 `no such module 'Testing'` , the bare Command Line Tools are selected rather than
a full toolchain; point at Xcode with  `sudo xcode-select -s /Applications/Xcode.app` 
(or run through  `xcrun` ).

## Roadmap

- Batched prefill: long prompts currently process at decode speed, so agent
clients with big system prompts are slow. Top of the list.

- Phone speed pass: fp16 activations and fewer GPU dispatches per token.

- A 6-bit container tier between the 4-bit and 8-bit ones.

## Relationship to TurboFieldfare

[TurboFieldfare](https://github.com/drumih/turbo-fieldfare) proved the
expert-streaming thesis for Gemma on Macs, and Swiftlet adopts several of its
published design lessons with gratitude: stream experts with  `pread`  into a
bounded slot pool instead of mmap, evict with LFU plus recency, pack experts
at fixed stride so one fetch is one read, install by routing downloaded bytes
straight into their final container positions, and compile shaders at
runtime.

Everything else is built here, from scratch, in about 10k lines of Swift and
Metal written against mlx-lm references rather than TurboFieldfare code:

- support for a different model family with a fundamentally different
architecture: the Qwen hybrid stack with Gated DeltaNet linear attention,
gated GQA, and high-sparsity MoE with a shared expert (TurboFieldfare runs
Gemma, a classical dense transformer);

- MLX affine int4/int8 group quantization compute in Metal, byte-addressed
kernels with 64-bit offsets for multi-gigabyte shards, a cooperative
simdgroup GEMV fast path, and explicit hazard management;

- a validated CPU reference implementation and the fixture infrastructure
that gates every kernel change;

- the  `.qpack`  container and repacker, the resumable Hugging Face streaming
installer with stall recovery, and download cancellation;

- the chat session layer: template handling for thinking and non-thinking
Qwen variants, sampling with presence and frequency penalties and
minimum-length and sentence-completion stopping, conversation caching with
delta prefill, and iOS memory-pressure coordination;

- iPhone support end to end, including the app engine integration.

[colibrì](https://github.com/JustVugg/colibri) informed the caching and
placement policy thinking. mlx-lm is the correctness reference throughout.

Swiftlet was built with
[Claude Code](https://claude.com/claude-code).

## License

Apache 2.0. Model weights are downloaded separately and remain governed by
their own terms (Qwen models: Apache 2.0). See THIRD_PARTY_NOTICES.md.

## About

Swiftlet is a Swift and Metal runtime that runs large Qwen Mixture-of-Experts models locally on Apple devices by streaming expert weights from storage, enabling 35B and 80B models to run with low RAM, including on iPhone.

### Topics

[local-llm](https://github.com/topics/local-llm)[mixture-of-experts](https://github.com/topics/mixture-of-experts)[on-device-ai](https://github.com/topics/on-device-ai)[qwen](https://github.com/topics/qwen)[swift](https://github.com/topics/swift)

### Resources

[Readme](https://github.com/leonickson1/Swiftlet#readme-ov-file)[Apache-2.0 license](https://github.com/leonickson1/Swiftlet#Apache-2.0-1-ov-file)[Activity](https://github.com/leonickson1/Swiftlet/activity)

### Stars

576 stars

### Watchers

2 watching

### Forks

[29 forks](https://github.com/leonickson1/Swiftlet/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fleonickson1%2FSwiftlet&report=leonickson1+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
