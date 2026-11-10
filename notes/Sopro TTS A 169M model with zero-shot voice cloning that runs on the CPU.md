---
title: "Sopro TTS: A 169M model with zero-shot voice cloning that runs on the CPU"
url: https://github.com/samuel-vitorino/sopro
clipped: 2026-06-17 02:01:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Text-to-Speech
  - Voice Cloning
  - Lightweight AI Models
  - On-device Inference
  - Audio Processing
  - CPU Optimization
related:
  - "[[Show HN Ghost Pepper – Local hold-to-talk speech-to-text for macOS]]"
  - "[[My thousand dollar iPhone can't do math]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Sopro is a 135M parameter lightweight text-to-speech model featuring streaming and zero-shot voice cloning capabilities optimized for CPU execution.
>
> **Key points:**
> - Sopro uses dilated convolutions and lightweight cross-attention layers rather than standard Transformer architectures.
> - Achieves a 0.05 real-time factor (RTF) on CPU, generating 32 seconds of audio in 1.77 seconds on base Apple Silicon.
> - Supports zero-shot voice cloning using only 3 to 12 seconds of reference audio.
> - Discussion notes that the audio can be artifact-prone and low-quality compared to larger models, but represents a high-efficiency alternative for local alerts.
>
> **Concept links:** [[Text-to-Speech]], [[Voice Cloning]], [[Lightweight AI Models]], [[On-device Inference]], [[Audio Processing]], [[CPU Optimization]]
>
> **Suggested connections:**
> - [[Show HN Ghost Pepper – Local hold-to-talk speech-to-text for macOS]] — related local audio-processing application.
> - [[My thousand dollar iPhone can't do math]] — related to performance profiling on local devices.
<!-- ai-summary:end -->

# [Sopro TTS: A 169M model with zero-shot voice cloning that runs on the CPU](https://github.com/samuel-vitorino/sopro)

## Digest Summary
The GitHub repository “samuel‑vitorino/sopro” is presented as a lightweight text‑to‑speech (TTS) model that includes zero‑shot voice cloning capabilities. The page currently displays the message “You can’t perform that action at this time,” indicating restricted access or a temporary limitation preventing further interaction with the content. The entry references two visual elements: an image labeled only with the generic alt text “Alt Text,” and a second image described as a “Screenshot.” No additional technical details, code snippets, or documentation are provided in the scraped excerpt beyond the repository title and the access restriction notice.

## Discussion Summary
The comments show mixed reactions: many note the audio sounds noticeably low‑quality and artifact‑prone, comparing it unfavorably to older TTS systems, while others appreciate the technical achievement and see potential for practical uses such as alerts or VTuber voice modulation. Several users suggest alternative open‑source models or request larger, higher‑fidelity versions. Technical interest appears in questions about zero‑shot capability and model parameters. A recurring concern highlights possible misuse for fraud, prompting calls for consideration of ethical implications.

---

## Full Article

SoproTTSv1.5demo.mp4

[
](https://private-user-images.githubusercontent.com/44442720/545766896-8b70f36e-2623-452d-b65a-be473ec36f26.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIxOTksIm5iZiI6MTc4MTY0MTg5OSwicGF0aCI6Ii80NDQ0MjcyMC81NDU3NjY4OTYtOGI3MGYzNmUtMjYyMy00NTJkLWI2NWEtYmU0NzNlYzM2ZjI2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjE2VDIwMzEzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgyY2RlM2M3ZjQ1OTVkYjhjZmYyNWYwNDZiYTYzYThlNjA5MDBhZDU0OGUwMWU1YTRkNzZlYjVmMzcwYjc4NDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.eL1JZFv5OSwmrCiuDIIIWOT2oGRBHdo7vu1i1w5d6PA)

[![Alt Text](https://camo.githubusercontent.com/a05e88b73ccd0b19d358a98085401f5db500c52c9bdaba999119ccd6577f65ee/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48756767696e67466163652d4d6f64656c2d6f72616e67653f6c6f676f3d68756767696e6766616365)](https://huggingface.co/samuel-vitorino/sopro)

**2026.02.04 - SoproTTS v1.5 is out: more stable, faster, and smaller (135M parameters). Trained for just $100 on a single GPU, it reaches 250 ms TTFA streaming and 0.05 RTF (~20× realtime) on CPU.**

Sopro (from the Portuguese word for “breath/blow”) is a lightweight English text-to-speech model I trained as a side project. Sopro is composed of dilated convs (à la WaveNet) and lightweight cross-attention layers, instead of the common Transformer architecture. Even though Sopro is not SOTA across most voices and situations, I still think it’s a cool project made with a very low budget (trained on a single L40S GPU), and it can be improved with better data.

Some of the main features are:

* **135M parameters**
* **Streaming**
* **Zero-shot voice cloning**
* **0.05 RTF on CPU** (measured on an M3 base model), meaning it generates 32 seconds of audio in 1.77 seconds
* **3-12 seconds of reference audio** for voice cloning

---

I only pinned the minimum dependency versions so you can install the package without having to create a separate env. However, some versions of Torch work best. For example, on my M3 CPU, `torch==2.10.0` (without `torchvision`) achieves ~600 it/s on the AR generation.

(Optional)

```
conda create -n soprotts python=3.10
conda activate soprotts
```

```
git clone https://github.com/samuel-vitorino/sopro
cd sopro
pip install -e .
```

---

```
soprotts \
  --text "Sopro is a lightweight 135 million parameter text-to-speech model. Some of the main features are streaming, zero-shot voice cloning, and 0.05 real-time factor on the CPU." \
  --ref_audio ref.wav \
  --out out.wav
```

You have the expected `temperature` and `top_p` parameters, alongside:

* `--style_strength` (controls the FiLM strength; increasing it can improve or reduce voice similarity; default `1.2`)

```
from sopro import SoproTTS

tts = SoproTTS.from_pretrained("samuel-vitorino/sopro", device="cpu")

wav = tts.synthesize(
    "Hello! This is a non-streaming Sopro TTS example.",
    ref_audio_path="ref.wav",
)

tts.save_wav("out.wav", wav)
```

```
import torch
from sopro import SoproTTS

tts = SoproTTS.from_pretrained("samuel-vitorino/sopro", device="cpu")

chunks = []
for chunk in tts.stream(
    "Hello! This is a streaming Sopro TTS example.",
    ref_audio_path="ref.mp3",
):
    chunks.append(chunk.cpu())

wav = torch.cat(chunks, dim=-1)
tts.save_wav("out_stream.wav", wav)
```

You can also precalculate the reference to reduce TTFA:

```
import torch
from sopro import SoproTTS

tts = SoproTTS.from_pretrained("samuel-vitorino/sopro", device="cpu")

ref = tts.prepare_reference(ref_audio_path="ref.mp3")

chunks = []
for chunk in tts.stream(
    "Hello! This is a streaming Sopro TTS example.",
    ref=ref,
):
    chunks.append(chunk.cpu())

wav = torch.cat(chunks, dim=-1)
tts.save_wav("out_stream.wav", wav)
```

---

Interactive streaming demo
--------------------------

[![Screenshot](https://private-user-images.githubusercontent.com/44442720/532988339-a1902bb9-734c-4da8-ad0d-f842fb7da370.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIxOTksIm5iZiI6MTc4MTY0MTg5OSwicGF0aCI6Ii80NDQ0MjcyMC81MzI5ODgzMzktYTE5MDJiYjktNzM0Yy00ZGE4LWFkMGQtZjg0MmZiN2RhMzcwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjE2VDIwMzEzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY2OGMxYTY4M2VmZTM3MjU0OTkxMjExOWU1ZDRjMzAxZmUxNTcyNzUzZWM3M2EwOTA3M2E0ZDBlZDQ3NDFiZDQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9._ECV8JpSTwmCdDR_MUqYF2qzXUpEtx2Y6WFduqMqyDc)](https://private-user-images.githubusercontent.com/44442720/532988339-a1902bb9-734c-4da8-ad0d-f842fb7da370.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDIxOTksIm5iZiI6MTc4MTY0MTg5OSwicGF0aCI6Ii80NDQ0MjcyMC81MzI5ODgzMzktYTE5MDJiYjktNzM0Yy00ZGE4LWFkMGQtZjg0MmZiN2RhMzcwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjE2VDIwMzEzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY2OGMxYTY4M2VmZTM3MjU0OTkxMjExOWU1ZDRjMzAxZmUxNTcyNzUzZWM3M2EwOTA3M2E0ZDBlZDQ3NDFiZDQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9._ECV8JpSTwmCdDR_MUqYF2qzXUpEtx2Y6WFduqMqyDc)

After you install the `sopro` package:

```
pip install -r demo/requirements.txt
uvicorn demo.server:app --host 0.0.0.0 --port 8000
```

Or with docker:

```
docker build -t sopro-demo .
docker run --rm -p 8000:8000 sopro-demo
```

Navigate to <http://localhost:8000> on your browser.

---

* Sopro can be inconsistent, so mess around with the parameters until you get a decent sample.
* Voice cloning is **highly dependent** on mic quality, ambient noise, etc. On more OOD voices it might fail to match the voice well.
* Prefer words instead of abbreviations and symbols. For example, `“1 + 2”` → `“1 plus 2”`. That said, Sopro can generally read abbreviations like “CPU”, “TTS”, etc.
* The streaming version is not bit-exact compared to the non-streaming version. For best quality, prioritize the non-streaming version.
* If you use torchaudio to read or write audio, ffmpeg may be required. I recommend just using soundfile.
* I will publish the training code once I have time to organize it.

Currently, generation is limited to **~32 seconds (400 frames)**. You can increase it, but the model generally hallucinates beyond that.

AI was used mainly for creating the web demo, organizing my messy code into this repo, ablations and brainstorming.

I would love to support more languages and continue improving the model. If you like this project, consider buying me a coffee so I can buy more compute: <https://buymeacoffee.com/samuelvitorino>

---



---