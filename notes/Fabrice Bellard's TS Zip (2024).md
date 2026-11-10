---
title: "Fabrice Bellard's TS Zip (2024)"
url: https://www.bellard.org/ts_zip/
clipped: 2026-06-17 01:59:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - Text Compression
  - Neural Network Compression
  - RWKV Architecture
  - Arithmetic Coding
  - Deterministic Execution
related:
  - '[[2025 The Year in LLMs]]'
  - '[[A 30B Qwen model walks into a Raspberry Pi and runs in real time]]'
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Fabrice Bellard's ts_zip is an experimental text compression tool that achieves high ratios using the RWKV-169M-v4 language model and an arithmetic coder.
>
> **Key points:**
> - Utilizes an 8-bit quantized RWKV-169M-v4 model evaluated in BF16 to predict next-token probabilities.
> - Requires a GPU with at least 4 GB RAM, achieving up to 1 MB/s throughput on an RTX 4090.
> - Highly effective on English text, code, and other natural languages, but ineffective for binary files.
> - Evaluation is deterministic and reproducible, ensuring files can be decompressed on different hardware configurations.
>
> **Concept links:** [[Text Compression]], [[Neural Network Compression]], [[RWKV Architecture]], [[Arithmetic Coding]], [[Deterministic Execution]]
>
> **Suggested connections:**
> - [[2025 The Year in LLMs]] — links model-based compression to general developments in LLMs.
> - [[A 30B Qwen model walks into a Raspberry Pi and runs in real time]] — connects model quantization and local execution efficiency.
<!-- ai-summary:end -->

# [Fabrice Bellard's TS Zip (2024)](https://www.bellard.org/ts_zip/)

## Digest Summary
ts_zip is a text‑only compression tool that leverages the RWKV‑169M‑v4 language model (8‑bit quantized, evaluated in BF16). It predicts next‑token probabilities, which an arithmetic coder uses to encode the text. Key characteristics:

- Requires a GPU (≥4 GB RAM) for acceptable speed; on an RTX 4090 it reaches up to 1 MiB/s for both compression and decompression, slower than traditional compressors.
- Compression ratio is reported in bits per byte (bpb); benchmark results on enwik8/enwik9 are referenced in the Large Text Compression Benchmark.
- Only effective on textual data; binary files gain little compression. The model, trained mainly on English, also handles other languages and source code.
- Deterministic and reproducible encoding ensures that compressed files can be decompressed on different hardware or software configurations.
- The project is experimental; backward compatibility across versions is not guaranteed. A related tool, ts_sms, targets small‑message compression.

## Discussion Summary
The comments highlight NNCP’s recent leadership in the Large Text Compression Benchmark, noting its small archive size and strong performance on enwik8 while trailing on enwik9. Users express surprise at PPMd’s effectiveness and discuss connections between compression, prediction, and intelligence, including potential LLM‑based approaches and steganographic uses. There is also concern that benchmark rules should count model and code size, preventing trivial “compressed” files. Overall sentiment is appreciative of the technical advances, curious about future methods, and mildly critical of evaluation criteria.

---

## Full Article

ts\_zip: Text Compression using Large Language Models
=====================================================

The `ts_zip` utility can
compress (and hopefully decompress) text files using a Large Language
Model. The compression ratio is much higher than with other
compression tools. There are some caveats of course:

* A GPU is necessary to get a reasonable speed. 4 GB of RAM is
  required.
* It is slower than conventional compressors (compression and
  decompression speed: up to 1 MB/s on a RTX 4090).
* Only text files are supported. Binary files won't be compressed
  much. The currently used language model (RWKV 169M v4) was trained
  mostly on English texts. Other languages are supported including
  source code.
* It is experimental so no backward compability should be expected
  between the various versions.
* See also [ts\_sms](https://www.bellard.org/ts_sms) which is optimized for the
  compression of small messages.

Compression Ratio
-----------------

The compression ratio is given in bits per byte (bpb).

| File | Original size (bytes) | [xz](https://en.wikipedia.org/wiki/XZ_Utils) (bytes) (bpb) | | ts\_zip (bytes) (bpb) | |
| --- | --- | --- | --- | --- | --- |
| [alice29.txt](https://en.wikipedia.org/wiki/Canterbury_corpus) | 152089 | 48492 | 2.551 | 21713 | 1.142 |
| [book1](https://en.wikipedia.org/wiki/Calgary_corpus) | 768771 | 261116 | 2.717 | 137477 | 1.431 |
| [enwik8](http://mattmahoney.net/dc/text.html) | 100000000 | 24865244 | 1.989 | 13825741 | 1.106 |
| [enwik9](http://mattmahoney.net/dc/text.html) | 1000000000 | 213370900 | 1.707 | 135443237 | 1.084 |
| [linux-1.2.13.tar](https://mirrors.edge.kernel.org/pub/linux/kernel/v1.2/linux-1.2.13.tar.xz) | 9379840 | 1689468 | 1.441 | 1196859 | 1.021 |

Results and speed for other programs on enwik8 and enwik9 are
available at the [Large
Text Compression Benchmark](http://www.mattmahoney.net/dc/text.html).

Download
--------

Technical information
---------------------

* `ts_zip` uses
  the [RWKV 169M v4](https://github.com/BlinkDL/RWKV-LM)
  language model which is a good compromise between speed and
  compression ratio. The model is quantized to 8 bits per parameter
  and evaluated using BF16 floating point numbers.
* The language model predicts the probabilities of the next token. An
  arithmetic coder then encodes the next token according to the
  probabilities.
* The model is evaluated in a deterministic and reproducible
  way. Hence the result does not depend on the exact GPU or CPU
  model nor on the number of configured threads. This key point
  ensures that a compressed file can be decompressed using a
  different hardware or software configuration.

---

Fabrice Bellard - [https://bellard.org/](https://bellard.org)