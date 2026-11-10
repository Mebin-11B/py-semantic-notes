---
title: "Neutrino-1 8B · Fermion Research"
url: https://www.fermionresearch.com/models/neutrino-8b/
clipped: 2026-08-31 12:26:36
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Neutrino-1 8B · Fermion Research](https://www.fermionresearch.com/models/neutrino-8b/)

## Full Article

Overview

Neutrino-1 8B is a local 8.19B-parameter model for chat, tool calling, and OpenAI-compatible applications. The fermion runtime serves it on CUDA, Apple silicon, and x86 from the same 3.88 GB artifact, with streaming and a persistent KV session enabled by default.

Its measured behavior is not limited to multiple-choice recall. On BFCL it composes simple, multiple, parallel, and parallel-multiple function calls, and declines an irrelevant function nearly as reliably as it selects the right one. On GSM8K, flexible and strict stated-format grading differ by 1.67 points.

Its 252 transformer projection matrices are stored in a packed ternary-family format. The weights stay bit-packed at rest and are decoded inside the matrix kernels. The same container serves each supported platform without a conversion pass.

The base is Qwen3-8B. Fermion Research continued it with ternary quantization-aware training, so the projection weights adapted to the representation used by the shipping runtime instead of being rounded once after training. The base is credited; the training method is ours.

Architecture

A dense decoder-only transformer. Grouped-query attention holds the KV cache at a quarter of the query width. fermion 0.1.10 stores it in fp16 by default at 144 KiB per token, so an 8K-token session occupies 1.13 GiB beside the 3.88 GB of weights.Base modelApache-2.0, Alibaba CloudQwen3-8BParameters6.95B coded projection weights, 1.24B int8 embedding, 0.3M norm8,190,735,360Decoder layers36Hidden width4,096Feed-forward widthgated (SwiGLU), three linears per layer12,288Attentiongrouped-query 4:1, head width 12832 query heads, 8 key-value headsKV cachefp16 default; 1.13 GiB at 8K context, 5.6 GiB at 40,960144 KiB per tokenPosition encodingapplied across the full 128-wide headrotary, base 1,000,000Normalizationplus per-head query/key RMSNorm inside attentionRMSNorm, eps 1e-6Context length40,960 tokensVocabulary151,936Embeddingsinput embedding and output head are separate tensorsuntiedGeometry as read from the shipped container's header.

### Artifact byte composition

Only the transformer linears carry the coded format. The two embedding tensors stay int8 because their rows are read one token at a time, not multiplied against the full activation stream, and the normalization weights are too small to be worth coding. A third of the file is vocabulary.252 transformer linearsthe coded ternary-family lane, 67.2% of the file: query, key, value, and output projections plus the gate, up, and down feed-forward linears, 7 per layer, 72,351,744 bytes per layer2,605 MBToken embeddings32.1% of the file: two untied int8 tensors of 151,936 × 4,096, input embedding and output head, one scale per row1,245 MBPer-row metadata0.6%: row dimensions, scales, and row sums25 MBNormalization weights145 tensors, kept float32: four per layer plus the final norm1.2 MBContainer header60 bytesByte budget of the 3,875,404,812-byte container, by tensor class.

### Zero-state occupancy

Across the 6.95B coded weights, 62.63% are zero. Occupancy varies with depth: the gate and down feed-forward projections reach 70 to 72% zeros in layers 1 through 3, while all four attention projections stay within about one point of 62% from layer 0 to layer 35.gateupdownquery, key, value, outputShare of coded weights at zero, per projection, across all 36 layers.

Format

The 2.56 GB download is a losslessly coded transport of the 3.88 GB serving artifact. Expansion is bit-exact, and each supported runtime loads the same stored model weights.

The weights, manifest, GGUF pack, MLX implementation, and llama.cpp fork are public under their stated open-source licenses. The optimized fermion kernels are closed. The manifest binds tensor layout, sizes, and hashes so the loader can verify the artifact before execution.Downloadcoded transport, 2,559,822,594 bytes; expansion is bit-exact2.56 GBOn diskreleased artifact, 3,875,404,812 bytes3.88 GB

### Distribution surfaces

#### pip engine

24.9 tok/s on the native CPU path, 9 threads

Installing fermion-research provides the loader and the platform-matching native binary. CPU runtimes are available for macOS arm64 and Linux x86-64, with a bit-exact torch reference implementation.

#### GGUF pack + llama.cpp fork

30.7 tok/s on an NVIDIA L4, 4.68 GiB at 4k context

The container converted to GGUF with the FV5 tensor type. It requires the public Fermion Research llama.cpp fork: stock llama.cpp, Ollama, and LM Studio do not load this tensor type. The fermion-fv5 branch runs on CPU/CUDA; fermion-fv5-metal carries the Apple-GPU kernels.

#### MLX pack

33.7 tok/s on the optimized MLX path

A Python-native Apple-silicon implementation with custom Metal kernels. The artifact is memory-mapped and the packed planes are decoded inside the GEMV kernels.

Evaluation

The release battery runs on the published artifact with thinking disabled. Each row states the shot count, grading mode, and item count.MMLU5-shot, all 57 subjects, 14,042 items72.1MMLU-Reduxgenerative, re-annotated subset, thinking off67.8IFEval, prompt-strictgenerative, thinking off77.2IFEval, instruction-strictsame run, per-instruction grading80.2IFEval, prompt-loosesame run, loose extraction76.3BFCL v3macro over 13 subsets, thinking off68.9GSM8K, flexible extraction0-shot generative, greedy, 256-token cap53.4GSM8K, stated formatsame run, answer accepted only in the requested form51.73Measured on standard public harnesses, July 2026. Methodology on the model card.

The BFCL result covers thirteen suites rather than a single function-call template. The model handles simple, multiple, parallel, and parallel-multiple calls against public API schemas with varied argument names and nested fields. Its relevance suites also test the opposite behavior: declining an offered function when none applies.

GSM8K is reported twice to expose output discipline. Flexible extraction accepts the last number and scores 53.4; stated-format extraction accepts only the requested answer position and scores 51.73. The 1.67-point gap separates formatting failures from arithmetic failures instead of folding both into one number.

Throughput

These measurements use single-stream decode with one active generation. Every row uses identical model weights through a different runtime backend.H100 80 GB, drafted0.6B draft + 8B verify, output identical to plain decode; fastest prompt class763 tok/sH100 80 GBplain single-stream greedy396 tok/sNVIDIA L4, CUDA forkGGUF pack, full offload, 4.68 GiB VRAM at 4k context; fits 8 GB cards30.7 tok/sMLX draft-and-verify pathfactual prompts, 0.6B drafting in the same process under a 6 GiB cap25.7 tok/sOptimized MLX pathsingle-stream decode on the shipped container33.7 tok/sNative CPU pathshipped native binary, 9 threads24.9 tok/sSingle-stream decode rates by platform and surface, July 2026.

The optimized MLX path reaches 33.7 tokens per second and the native CPU path reaches 24.9. The same weights reach 396 tokens per second on one H100 before drafting. These are different kernels over the same 3.88 GB model, not separately converted checkpoints.

Speculative decoding

Neutrino-1 0.6B drafts a run of tokens, the 8B scores the whole run in one forward pass, and the agreeing prefix is kept. A draft token is accepted only when it equals the 8B's own argmax, so the output stream is the plain greedy stream: on the shipping configuration, 27,648 consecutive tokens matched with zero divergences.

Speculative-decoding speed depends on how many proposed tokens the 8B accepts, so results are reported per prompt class against the 396 tok/s plain rate. On counting prompts the 8B accepts the full six-token draft on every pass, about seven tokens emitted per 8B forward; on factual prompts acceptance holds at 96.5%. A dynamic controller sizes each draft from recent acceptance. Every measured class exceeds the plain decode rate.Counting and lists763 tok/s×1.93Factual short answers613 tok/s×1.55Prose continuation532 tok/s×1.34Conversational explanation447 tok/s×1.13Code426 tok/s×1.07H100, three-round median per prompt class, over 396 tok/s plain decode.

### Memory requirements

Both models use the same format and runtime binaries. The draft loads in the verifier process without a conversion step. The draft artifact uses 328 MB beside the 8B's 3.88 GB, and 4k tokens of shared context allocate exactly one gibibyte of cache across the pair.Weights resident3.88 GB verifier plus 328 MB draft, one process4.20 GBDraft surchargethe extra weight bytes the pairing costs8.46%Shared cache288 KiB on the 8B, 224 KiB on the draft; 2 GiB at 4k context512 KiB per tokenCertified rundraft plus verify against plain greedy, zero divergences27,648 tokensThe drafted pair drawn to byte scale, with the residency each side costs.

### Drafting through MLX

Both models load into one MLX process and peak at 4.3 GiB together, with the draft accounting for 0.53 GiB. The exactness gate returns 6 of 6 prompts token-identical with drafting on and off, and on factual prompts the drafted rate is 25.71 tok/s against 22.00 plain at an acceptance of 0.744.

Run it

### Install and run Neutrino-1 8B.

 `$ pip install fermion-research$ fermion chat --model fermionresearch/Neutrino-8B` 

On the first 8B run, fermion downloads a 2.56 GB coded transport with a progress bar, verifies its SHA-256, and unpacks it locally. Later runs load from cache.
- Long context with bounded KV memory `$ fermion chat --model fermionresearch/Neutrino-8B --kv-dtype int8 --yarn-factor 4` 

The native window is 40,960 tokens. --yarn-factor 4 extends the loaded window toward 160K without changing the artifact; --kv-dtype int8 holds 131,072 tokens in about 9.3 GiB. fp16 is the default, fp32 preserves byte-identical 0.1.9 output, and --yarn-factor 1.0 is exact identity.
- A local OpenAI-compatible server `$ fermion serve --model fermionresearch/Neutrino-8B` 

Serves at http://127.0.0.1:8000/v1. Point any OpenAI client at that base URL; the key can be any string. Tool calling, streaming, and a persistent KV session are on by default.
- Plain Transformers `$ hf download fermionresearch/Neutrino-8B --local-dir Neutrino-8B \    --exclude "gguf/*" --exclude "*.tv4z"`  `import fermionfrom transformers import AutoModelForCausalLM, AutoTokenizermodel = AutoModelForCausalLM.from_pretrained("Neutrino-8B")tokenizer = AutoTokenizer.from_pretrained("Neutrino-8B")` 

Import fermion first to register the trtc_v4 model type. Load from the downloaded local directory; passing the Hub repository id directly to from_pretrained does not work.
- GGUF, through our llama.cpp fork only `$ git clone https://github.com/fermionresearch/llama.cpp && cd llama.cpp$ git checkout fermion-fv5$ cmake -B build -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=OFF -DGGML_METAL=OFF$ cmake --build build -j --target llama-completion` 

The pack uses the FV5 tensor type: stock llama.cpp, Ollama, and LM Studio cannot load it. The fermion-fv5 branch is the CPU/CUDA build and requires -DGGML_METAL=OFF. For Apple-GPU kernels, use the live fermion-fv5-metal branch and omit that flag.
- MLX, on Apple silicon `$ cd Neutrino-8B/mlx$ pip install -r requirements.txt$ python -m fermion_mlx --model ../neutrino-8b_v4.bin --mode chat --tokenizer .` 

Run this exact sequence after downloading the repository. The working directory and relative model path are required.

#### The full CLI

CommandWhat it does `fermion chat` Start an interactive streaming chat. Session caching is enabled by default. `fermion serve` Run a local OpenAI-compatible API with streaming and tool calling. `fermion generate` Generate a one-shot completion. Scripted output is deterministic by default. `fermion info` Verify the container header and SHA-256 against the model manifest. `fermion bench` Measure decode performance on the current machine. `fermion inspect` Inspect weight occupancy and per-layer byte counts inside a container. `fermion verify` Check that a speculative draft and target model produce identical tokens.

Every command takes --model with a Hub id or local path.

[Fermion documentation](https://www.fermionresearch.com/docs/)

Get the models

[Neutrino-1 8BWeights, native binaries, GGUF pack, MLX pack.Hugging Face](https://huggingface.co/FermionResearch/Neutrino-8B) `$ fermion chat --model fermionresearch/Neutrino-8B` Run Neutrino-1 8B `$ pip install fermion-research$ fermion chat --model fermionresearch/Neutrino-8B` 

First run downloads a 2.56 GB coded transport, shows progress, verifies its SHA-256, and unpacks locally. Later runs load from cache.

[Neutrino-1 0.6BThe draft model, and a fast model on its own.Hugging Face](https://huggingface.co/FermionResearch/Neutrino-0.6B) `$ fermion chat --model fermionresearch/Neutrino-0.6B` Run Neutrino-1 0.6B `$ pip install fermion-research$ fermion chat --model fermionresearch/Neutrino-0.6B` 

First run downloads the 0.24 GB coded transport, shows progress, verifies its SHA-256, and unpacks locally. Later runs load from cache.

[Neutrino-1 0.6B-ChatThe conversational small model.Hugging Face](https://huggingface.co/FermionResearch/Neutrino-0.6B-Chat) `$ fermion chat --model fermionresearch/Neutrino-0.6B-Chat` Run Neutrino-1 0.6B-Chat `$ pip install fermion-research$ fermion chat --model fermionresearch/Neutrino-0.6B-Chat` 

First run downloads about 0.33 GB of raw model files with progress and verifies them. This model does not use the coded transport. Later runs load from cache.

[fermion-researchThe engine, the loader, and the chat front end.PyPI](https://pypi.org/project/fermion-research) `$ pip install fermion-research` 

[llama.cpp forkAdds the format to the llama.cpp toolchain.GitHub](https://github.com/fermionresearch/llama.cpp) `$ git clone https://github.com/fermionresearch/llama.cpp && git checkout fermion-fv5` 

Availability

Neutrino-1 8B ships in a public repository with the model artifact, manifest, GGUF pack, MLX implementation, and installation instructions. The optimized fermion kernels distributed by the pip package are closed.Available nowPublic model repositoryOpen weights, Apache 2.0

### License

Open weights under the Apache License 2.0. Commercial use, modification, fine-tuning, and redistribution are permitted, with no access request and no acceptance form. The model is a derivative of Qwen3-8B, itself Apache-2.0. The pip package is Apache-2.0 too; the llama.cpp fork is MIT, following upstream llama.cpp.

### Citation

 `@misc{fermionresearch2026neutrino,
  title  = {Neutrino-1 8B},
  author = {{Fermion Research}},
  year   = {2026},
  url    = {https://www.fermionresearch.com/models/neutrino-8b/}
}` 

## Related research

[All research](https://www.fermionresearch.com/research/)

### 

[Introducing the Neutrino-1 modelsAnnouncement·July 27, 2026Introducing the Neutrino-1 modelsThree open-weight models trained for a compact ternary format and released with CUDA, Apple-silicon, and x86 runtimes.](https://www.fermionresearch.com/research/neutrino-8b/)

### 

[The Neutrino EngineResearch·July 27, 2026The Neutrino EngineAn A100 can move the weights for one measured decoder step in 104 microseconds. The step takes 694. The Neutrino Engine is built around the gap.](https://www.fermionresearch.com/research/the-neutrino-engine/)
