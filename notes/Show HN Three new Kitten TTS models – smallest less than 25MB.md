---
title: "Show HN: Three new Kitten TTS models – smallest less than 25MB"
url: https://github.com/KittenML/KittenTTS
clipped: 2026-06-17 01:30:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Text-To-Speech
  - Machine Learning
  - ONNX Runtimes
  - Edge Computing
  - CPU Optimization
related:
  - "[[Text-To-Speech]]"
  - "[[Machine Learning]]"
  - "[[ONNX Runtimes]]"
  - "[[Edge Computing]]"
  - "[[CPU Optimization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** KittenTTS is an open-source, ONNX-based text-to-speech library optimized for CPU, offering extremely small model sizes (under 25MB) suitable for edge deployment.
>
> **Key points:**
> - The library provides three model sizes (15M, 40M, and 80M parameters) ranging from 25MB to 80MB on disk.
> - It enables high-quality 24 kHz speech synthesis on CPU without requiring a GPU.
> - KittenTTS includes eight built-in voices and text preprocessing for numbers, currencies, and units.
> - Users appreciate its offline speed and small size, but note issues with installation dependencies and number pronunciation.
>
> **Concept links:** [[Text-To-Speech]], [[Machine Learning]], [[ONNX Runtimes]], [[Edge Computing]], [[CPU Optimization]]
>
> **Suggested connections:**
> - [[Audio Synthesis]] — how small-footprint models compare to cloud-based alternatives.
> - [[ONNX Runtimes]] — using ONNX for cross-platform model execution without GPUs.
<!-- ai-summary:end -->

# [Show HN: Three new Kitten TTS models – smallest less than 25MB](https://github.com/KittenML/KittenTTS)

## Digest Summary
KittenTTS is an open‑source, CPU‑optimized text‑to‑speech library built on ONNX. It offers three model sizes (15 M, 40 M, 80 M parameters) ranging from 25 MB to 80 MB on disk, enabling high‑quality 24 kHz speech synthesis without a GPU. The package includes eight built‑in voices (Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, Leo) and supports adjustable playback speed and comprehensive text preprocessing (numbers, currencies, units, etc.). Primary API functions are `KittenTTS(model_name, cache_dir=None)`, `generate(text, voice, speed, clean_text)` returning a NumPy audio array, and `generate_to_file(...)` for direct file output. Installation is via a pip wheel from the GitHub release; usage examples show model loading, speech generation, and file saving. Supported on Linux, macOS, and Windows with Python 3.8+. The project is in developer preview (APIs may change) and licensed under Apache 2.0; commercial support and custom‑voice services are offered (contact [email protected]). Some users report issues with the `kitten-tts-nano-0.8-int8` model.

## Discussion Summary
The comments express strong appreciation for the tiny TTS models’ impressive audio quality, fast inference and offline operation, especially given their small footprint. Users note practical benefits for accessibility and personal projects, while also highlighting recurring issues such as inaccurate number pronunciation, limited expressive controls, and voices that feel more cartoon‑like than professional. Installation complexity and large dependency chains are criticized, and many request clearer GPU support, language extensions (e.g., Japanese), custom‑voice options, comparative benchmarks, and guidance for mobile or embedded deployment. Overall sentiment is positive but calls for usability improvements.

---

## Full Article

[![Kitten TTS](https://private-user-images.githubusercontent.com/224667291/551914046-f4646722-ba78-4b25-8a65-81bacee0d4f6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDAzMjgsIm5iZiI6MTc4MTY0MDAyOCwicGF0aCI6Ii8yMjQ2NjcyOTEvNTUxOTE0MDQ2LWY0NjQ2NzIyLWJhNzgtNGIyNS04YTY1LTgxYmFjZWUwZDRmNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDAwMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NjRmOGE1ODMyOWExZDYxNzAzOTE2NGUyZjA5MzEwYzg5YjU1MjkwZWNjY2U1OTZlNDU4MGRjODllYTJmNzA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.oJBZ_EI-EP0opS5u8PLKKnkettgVl245CobhnvpXh54)](https://private-user-images.githubusercontent.com/224667291/551914046-f4646722-ba78-4b25-8a65-81bacee0d4f6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDAzMjgsIm5iZiI6MTc4MTY0MDAyOCwicGF0aCI6Ii8yMjQ2NjcyOTEvNTUxOTE0MDQ2LWY0NjQ2NzIyLWJhNzgtNGIyNS04YTY1LTgxYmFjZWUwZDRmNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDAwMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NjRmOGE1ODMyOWExZDYxNzAzOTE2NGUyZjA5MzEwYzg5YjU1MjkwZWNjY2U1OTZlNDU4MGRjODllYTJmNzA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.oJBZ_EI-EP0opS5u8PLKKnkettgVl245CobhnvpXh54)

[![Hugging Face Demo](https://camo.githubusercontent.com/0cf7fe7a19b73ab669d5b817ff290761947e52184dff13945efe7631c76b3335/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f44656d6f2d48756767696e67253230466163652532305370616365732d6f72616e6765)](https://huggingface.co/spaces/KittenML/KittenTTS-Demo)
[![Discord](https://camo.githubusercontent.com/21bcf2f16cd91eb55d87e708baecb6623dbff8c363498d411af045234e74b63e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d4a6f696e253230436f6d6d756e6974792d3538363546323f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.com/invite/VJ86W4SURW)
[![Website](https://camo.githubusercontent.com/0b5ebd5ba357c3d2880d1e5b522cde90e5286ad0b7194570a6e3b11a2d73338c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f576562736974652d6b697474656e6d6c2e636f6d2d626c7565)](https://kittenml.com)
[![License](https://camo.githubusercontent.com/65bd7c9aa78c2b90294d6b118247e7306a1cb0035ddafc42a8947e8f3c83562e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368655f322e302d677265656e2e737667)](https://github.com/KittenML/KittenTTS/blob/main/LICENSE)

> **New:** Kitten TTS v0.8 is out -- 15M, 40M, and 80M parameter models now available.

Kitten TTS is an open-source, lightweight text-to-speech library built on ONNX. With models ranging from 15M to 80M parameters (25-80 MB on disk), it delivers high-quality voice synthesis on CPU without requiring a GPU.

> **Status:** Developer preview -- APIs may change between releases.

**Commercial support is available.** For integration assistance, custom voices, or enterprise licensing, [contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview).

* **Ultra-lightweight** -- Model sizes from 25 MB (int8) to 80 MB, suitable for edge deployment
* **CPU-optimized** -- ONNX-based inference runs efficiently without a GPU
* **8 built-in voices** -- Bella, Jasper, Luna, Bruno, Rosie, Hugo, Kiki, and Leo
* **Adjustable speech speed** -- Control playback rate via the `speed` parameter
* **Text preprocessing** -- Built-in pipeline handles numbers, currencies, units, and more
* **24 kHz output** -- High-quality audio at a standard sample rate

> **Note:** Some users have reported issues with the `kitten-tts-nano-0.8-int8` model. If you encounter problems, please [open an issue](https://github.com/KittenML/KittenTTS/issues).

final\_vid.mp4

[
](https://private-user-images.githubusercontent.com/224667291/551915065-d80120f2-c751-407e-a166-068dd1dd9e8d.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDAzMjgsIm5iZiI6MTc4MTY0MDAyOCwicGF0aCI6Ii8yMjQ2NjcyOTEvNTUxOTE1MDY1LWQ4MDEyMGYyLWM3NTEtNDA3ZS1hMTY2LTA2OGRkMWRkOWU4ZC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDAwMjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNmQxYTM0ZGZjNDAzMjY0YzM3ZDU2YjcyN2E1MDk1ZjdiYmFjYzJmNmMwYTFlZDVjNzk5MWU5NjU4ZTFiNDNhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9dmlkZW8lMkZtcDQifQ.dnKqCNpmzDjVLoZEv-OEhhQViXSxKomNLKOi4JFN1v8)

Try Kitten TTS directly in your browser on [Hugging Face Spaces](https://huggingface.co/spaces/KittenML/KittenTTS-Demo).

```
pip install https://github.com/KittenML/KittenTTS/releases/download/0.8.1/kittentts-0.8.1-py3-none-any.whl
```

```
from kittentts import KittenTTS

model = KittenTTS("KittenML/kitten-tts-mini-0.8")
audio = model.generate("This high-quality TTS model runs without a GPU.", voice="Jasper")

import soundfile as sf
sf.write("output.wav", audio, 24000)
```

```
# Adjust speech speed (default: 1.0)
audio = model.generate("Hello, world.", voice="Luna", speed=1.2)

# Save directly to a file
model.generate_to_file("Hello, world.", "output.wav", voice="Bruno", speed=0.9)

# List available voices
print(model.available_voices)
# ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
```

```
pip install -r requirements_gpu.txt
```

```
m = KittenTTS("KittenML/kitten-tts-mini-0.8", backend="cuda")
```

Check out `example_cuda.py`

### `KittenTTS(model_name, cache_dir=None)`

Load a model from Hugging Face Hub.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model_name` | `str` | `"KittenML/kitten-tts-nano-0.8"` | Hugging Face repository ID |
| `cache_dir` | `str` | `None` | Local directory for caching downloaded model files |

### `model.generate(text, voice, speed, clean_text)`

Synthesize speech from text, returning a NumPy array of audio samples at 24 kHz.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | -- | Input text to synthesize |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name (see available voices) |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `clean_text` | `bool` | `False` | Preprocess text (expand numbers, currencies, etc.) |

### `model.generate_to_file(text, output_path, voice, speed, sample_rate, clean_text)`

Synthesize speech and write directly to an audio file.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | -- | Input text to synthesize |
| `output_path` | `str` | -- | Path to save the audio file |
| `voice` | `str` | `"expr-voice-5-m"` | Voice name |
| `speed` | `float` | `1.0` | Speech speed multiplier |
| `sample_rate` | `int` | `24000` | Audio sample rate in Hz |
| `clean_text` | `bool` | `True` | Preprocess text (expand numbers, currencies, etc.) |

### `normalize_text(text, locale="en-US", return_spans=False)`

Normalize text for TTS without generating audio.

```
from kittentts import normalize_text

normalized = normalize_text("Dr. Rivera paid $12.50 at 3:05 p.m.")
# "Doctor Rivera paid twelve dollars and fifty cents at three oh five p m."

result = normalize_text("Fig. 2", return_spans=True)
print(result.text)
print(result.spans)
```

When `return_spans=True`, the result includes original-to-normalized character spans for changed segments such as abbreviations, dates, times, numbers, currency, URLs, and punctuation.

Returns a list of available voice names: `['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']`

* **Operating system:** Linux, macOS, or Windows
* **Python:** 3.8 or later
* **Hardware:** Runs on CPU; no GPU required
* **Disk space:** 25-80 MB depending on model variant

A virtual environment (conda, venv, or similar) is recommended to avoid dependency conflicts.

We offer commercial support for teams integrating Kitten TTS into their products. This includes integration assistance, custom voice development, and enterprise licensing.

[Contact us](https://docs.google.com/forms/d/e/1FAIpQLSc49erSr7jmh3H2yeqH4oZyRRuXm0ROuQdOgWguTzx6SMdUnQ/viewform?usp=preview) or email [info@stellonlabs.com](mailto:info@stellonlabs.com) to discuss your requirements.

This project is licensed under the [Apache License 2.0](https://github.com/KittenML/KittenTTS/blob/main/LICENSE).