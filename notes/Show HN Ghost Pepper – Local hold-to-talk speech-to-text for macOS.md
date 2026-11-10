---
title: "Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS"
url: https://github.com/matthartman/ghost-pepper
clipped: 2026-06-17 01:21:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Local AI
  - Speech-to-Text
  - WhisperKit
  - Apple Silicon
  - macOS Applications
  - Privacy-first AI
related:
  - "[[Sopro TTS A 169M model with zero-shot voice cloning that runs on the CPU]]"
  - "[[Show HN A context-aware permission guard for Claude Code]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Ghost Pepper is a privacy-first macOS menu-bar app offering local push-to-talk speech-to-text and post-processing cleanups on Apple Silicon.
>
> **Key points:**
> - Employs WhisperKit for speech-to-text transcription and LLM.swift for local LLM post-processing.
> - Runs 100% locally on device with zero telemetry or cloud APIs, providing high privacy guarantees.
> - Utilizes models like Whisper tiny/small and Qwen 3.5 cached locally on macOS.
> - Promotes user privacy, with a comprehensive audit verified through automated AI code reviews.
>
> **Concept links:** [[Local AI]], [[Speech-to-Text]], [[WhisperKit]], [[Apple Silicon]], [[macOS Applications]], [[Privacy-first AI]]
>
> **Suggested connections:**
> - [[Sopro TTS A 169M model with zero-shot voice cloning that runs on the CPU]] — related local audio AI models.
> - [[Show HN A context-aware permission guard for Claude Code]] — related local security/privacy utilities.
<!-- ai-summary:end -->

# [Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS](https://github.com/matthartman/ghost-pepper)

## Digest Summary
Ghost Pepper is a macOS menu‑bar application that provides hold‑to‑talk speech‑to‑text entirely locally on Apple Silicon (M1+), requiring macOS 14.0 or later. Users press and hold the Control key to record; releasing triggers transcription and automatic pasting into the active text field. The app uses WhisperKit for speech recognition and LLM.swift for post‑processing, with models sourced from Hugging Face and cached on the device. Features include customizable cleanup prompts, microphone selection, feature toggles, and no persistent logging—debug data exists only in memory. Installation is via a DMG that places the app in Applications and requests microphone and Accessibility permissions; Accessibility rights can be pre‑approved on managed devices through an MDM PPPC payload. Source code is available for building in Xcode, and the project is MIT‑licensed. The app integrates Sparkle for updates and emphasizes that no audio or transcription data leaves the user’s computer.

## Discussion Summary
The comments show strong interest in open‑source, locally run speech‑to‑text tools, praising their privacy, speed and potential for integration with coding workflows. Users repeatedly note usability gaps such as push‑to‑talk activation, limited real‑time editing, and inconsistent accuracy across accents and vocabularies, especially for proper names. Comparisons frequently mention Google’s offline engine, Dragon, Whisper, Parakeet and other projects, with no clear consensus on a single superior model. Many request better customization, cross‑platform support, clearer documentation, and more seamless hands‑free operation, while acknowledging trade‑offs between local processing and feature richness.

---

## Full Article

* **Hold Control to talk** — release to transcribe and paste into any text field
* **Meeting transcription** — record calls with notes, transcript, and AI-generated summaries saved as markdown
* **Runs entirely on your Mac** — models run locally via Apple Silicon, nothing is sent anywhere
* **Smart cleanup** — local LLM removes filler words and handles self-corrections
* **Menu bar app** — lives in your menu bar, no dock icon, launches at login
* **Customizable** — edit the cleanup prompt, pick your mic, toggle features on/off

Ghost Pepper uses open-source models that run entirely on your Mac. Models download automatically and are cached locally.

| Model | Size | Best for |
| --- | --- | --- |
| Whisper tiny.en | ~75 MB | Fastest, English only |
| **Whisper small.en** (default) | ~466 MB | Best accuracy, English only |
| Whisper small (multilingual) | ~466 MB | Multi-language support |
| Parakeet v3 (25 languages) | ~1.4 GB | Multi-language via [FluidAudio](https://github.com/FluidInference/FluidAudio) |
| Qwen3-ASR 0.6B int8 (50+ languages) | ~900 MB | Highest multilingual quality, macOS 15+ required |



| Model | Size | Speed |
| --- | --- | --- |
| **Qwen 3.5 0.8B** (default) | ~535 MB | Very fast (~1-2s) |
| Qwen 3.5 2B | ~1.3 GB | Fast (~4-5s) |
| Qwen 3.5 4B | ~2.8 GB | Full quality (~5-7s) |

Speech models powered by [WhisperKit](https://github.com/argmaxinc/WhisperKit). Cleanup models powered by [LLM.swift](https://github.com/eastriverlee/LLM.swift). All models served by [Hugging Face](https://huggingface.co/).

**Download the app:**

1. Download [GhostPepper.dmg](https://github.com/matthartman/ghost-pepper/releases/latest/download/GhostPepper.dmg)
2. Open the DMG, drag Ghost Pepper to Applications
3. Grant Microphone and Accessibility permissions when prompted
4. Hold Control and speak

> **"Apple could not verify" warning?** On macOS Sequoia, you may see a Gatekeeper warning the first time you open the app. Go to **System Settings > Privacy & Security**, scroll down, and click **Open Anyway** next to the Ghost Pepper message. Click **Confirm** in the popup. You only need to do this once.

**Build from source:**

1. Clone the repo
2. Open `GhostPepper.xcodeproj` in Xcode
3. Build and run (Cmd+R)

| Permission | Why |
| --- | --- |
| Microphone | Record your voice |
| Accessibility | Global hotkey and paste via simulated keystrokes |

Every core feature runs 100% on your Mac — verified by AI code review. No trust required, just point Claude at the repo and ask.

| Feature | Status | What was checked |
| --- | --- | --- |
| Speech-to-text | ✅ Local | WhisperKit/FluidAudio inference, no audio sent anywhere |
| Text cleanup | ✅ Local | Qwen LLM runs on-device via LLM.swift |
| Audio recording | ✅ Local | AVAudioEngine + ScreenCaptureKit, no streaming |
| Meeting transcription & storage | ✅ Local | Chunked transcription, markdown files on disk |
| Summary generation | ✅ Local | Local LLM summarization, no cloud API |
| OCR & screen capture | ✅ Local | Apple Vision framework, on-device |
| File storage | ✅ Local | Markdown to local filesystem, no cloud sync |
| Analytics & telemetry | ✅ Local | Local-only usage counters (UserDefaults) power the in-app Usage report panel. No Firebase, Mixpanel, Sentry, or any tracking SDK. |

**Optional cloud features** (disabled by default, require your own API keys): Zo AI chat, Trello integration, Granola meeting import. Model downloads are one-time from Hugging Face.

> **Verify it yourself:** run `cat PRIVACY_AUDIT.md` in Claude Code and ask it to review the codebase against the audit prompt. The [full audit](https://github.com/matthartman/ghost-pepper/blob/main/PRIVACY_AUDIT.md) includes the exact prompt and detailed file-level results.

* **Launch at login** is enabled by default on first run. You can toggle it off in Settings.
* **Everything stays local** — transcription history and recordings are stored on your Mac only. Nothing is sent to the cloud. You can clear history anytime in Settings.

Built with [WhisperKit](https://github.com/argmaxinc/WhisperKit), [LLM.swift](https://github.com/eastriverlee/LLM.swift), [Hugging Face](https://huggingface.co/), and [Sparkle](https://sparkle-project.org/).

MIT

All models run locally, no private data leaves your computer. And it's spicy to offer something for free that other apps have raised $80M to build.

Enterprise / managed devices
----------------------------

Ghost Pepper requires Accessibility permission, which normally needs admin access to grant. On managed devices, IT admins can pre-approve this via an MDM profile (Jamf, Kandji, Mosaic, etc.) using a Privacy Preferences Policy Control (PPPC) payload:

| Field | Value |
| --- | --- |
| Bundle ID | `com.github.matthartman.ghostpepper` |
| Team ID | `BBVMGXR9AY` |
| Permission | Accessibility (`com.apple.security.accessibility`) |



---

Matt invests at [factorialcap.com](https://factorialcap.com) — reach out on [X/Twitter](https://x.com/matthartman) if you're a technical founder building something newly technically possible.