---
title: "Show HN: Free Alternative to Wispr Flow, Superwhisper, and Monologue"
url: https://github.com/zachlatta/freeflow
clipped: 2026-06-17 01:44:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - speech-to-text
  - voice dictation
  - ai productivity tools
  - local llms
  - context-aware cleanup
  - macos applications
related:
  - "[[Speech-to-Text]]"
  - "[[Voice Dictation]]"
  - "[[Local LLMs]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** FreeFlow is a free, open-source macOS dictation application that provides fast, AI-powered transcription and context-aware text editing using Groq or custom local models without a subscription.
>
> **Key points:**
> - FreeFlow is released under the MIT license as an open-source alternative to paid dictation tools like Superwhisper and Wispr Flow.
> - The app utilizes Groq API keys by default, allowing users to customize shortcut keys for hold-to-talk or toggle dictation.
> - Features include context-aware cleanup (reading nearby app context for correct spelling), custom vocabulary, and an "Edit Mode" to transform highlighted text using voice instructions.
> - FreeFlow runs locally and respects privacy, only making API calls to configured OpenAI-compatible transcription or LLM providers (e.g., Ollama, LM Studio).
>
> **Concept links:** [[Speech-to-Text]], [[Voice Dictation]], [[AI Productivity Tools]], [[Local LLMs]], [[Context-Aware Cleanup]], [[macOS Applications]]
>
> **Suggested connections:**
> - [[Speech-to-Text]] — systems and algorithms that convert spoken language into written text.
> - [[Voice Dictation]] — the use of voice commands and spoken words to input and edit text on computers.
> - [[Local LLMs]] — running large language models locally on user hardware to protect privacy and avoid subscriptions.
<!-- ai-summary:end -->


# [Show HN: Free Alternative to Wispr Flow, Superwhisper, and Monologue](https://github.com/zachlatta/freeflow)

## Digest Summary
The repository “zachlatta/freeflow” is presented as a free, open‑source alternative to proprietary or closed‑source tools such as Wispr Flow, Superwhisper, Monologue, and similar applications. The project’s landing page includes a graphic labeled “FreeFlow icon” and a second visual described as “FreeFlow demo,” indicating that visual assets or a demonstration are part of the repository’s documentation. Access to the page or certain actions is currently blocked, as indicated by the message “You can’t perform that action at this time.” No additional technical specifications, code excerpts, licensing details, or usage instructions are provided in the extracted content.

## Discussion Summary
The comments show strong enthusiasm for locally run speech‑to‑text tools, with numerous users sharing workflows, key‑binding tips, and links to open‑source projects such as Hex, VoiceInk, Soupawhisper and others. Many favor free or low‑cost solutions that balance speed and accuracy, while some regard paid or feature‑heavy apps as excessive or buggy. There is a recurring desire for custom key bindings, cross‑platform support—especially iOS and Android—and the ability to retain audio alongside transcripts. Skepticism appears toward “free‑alternative” marketing that seems copy‑cat driven.

---

## Full Article

[![FreeFlow icon](https://github.com/zachlatta/freeflow/raw/main/Resources/AppIcon-Source.png)](https://github.com/zachlatta/freeflow/blob/main/Resources/AppIcon-Source.png)

Free and open source alternative to [Wispr Flow](https://wisprflow.ai), [Superwhisper](https://superwhisper.com), and [Monologue](https://monologue.to).

[**⬇ Download FreeFlow.dmg**](https://github.com/zachlatta/freeflow/releases/latest/download/FreeFlow.dmg)  
Works on all Macs (Apple Silicon + Intel)

---

[![FreeFlow demo](https://github.com/zachlatta/freeflow/raw/main/Resources/demo.gif)](https://github.com/zachlatta/freeflow/blob/main/Resources/demo.gif)

*Thank you to [@marcbodea](https://github.com/marcbodea) for maintaining FreeFlow!*

FreeFlow is a free Mac dictation app inspired by [Wispr Flow](https://wisprflow.ai/), [Superwhisper](https://superwhisper.com/), and [Monologue](https://www.monologue.to/). It gives you fast AI transcription, context-aware cleanup, and voice-driven text editing without a monthly subscription.

1. Download the app from above or [click here](https://github.com/zachlatta/freeflow/releases/latest/download/FreeFlow.dmg)
2. Get a free Groq API key from [groq.com](https://groq.com/)
3. Hold `Fn` to talk, or tap `Command-Fn` to start and stop dictation, and have whatever you say pasted into the current text field

* **Custom shortcuts:** Customize both hold-to-talk and toggle dictation shortcuts. If your toggle shortcut extends your hold shortcut, you can start in hold mode and press the extra modifier keys to latch into tap mode without stopping the recording.
* **Context-aware cleanup:** FreeFlow can read nearby app context so names, terms, and phrases are spelled correctly when you dictate into email, terminals, docs, and other apps.
* **Custom vocabulary:** Add names, jargon, and project-specific words that FreeFlow should preserve during cleanup.
* **OpenAI-compatible providers:** Use Groq by default, or configure a custom model and API URL in settings.

Edit Mode lets you highlight existing text and transform it with a spoken instruction, like "make this shorter" or "turn this into bullets." Enable it in settings, then use your normal dictation shortcut on selected text, or choose Manual mode to require an extra modifier key.

There is no FreeFlow server, so FreeFlow does not store or retain your data. The only information that leaves your computer are API calls to your configured transcription and LLM provider.

If you'd rather keep cleanup more literal and less context-aware, you can paste this simpler prompt into the custom system prompt setting:

Simple post-processing prompt

```
You are a dictation post-processor. You receive raw speech-to-text output and return clean text ready to be typed into an application.

Your job:
- Remove filler words (um, uh, you know, like) unless they carry meaning.
- Fix spelling, grammar, and punctuation errors.
- When the transcript already contains a word that is a close misspelling of a name or term from the context or custom vocabulary, correct the spelling. Never insert names or terms from context that the speaker did not say.
- Preserve the speaker's intent, tone, and meaning exactly.

Output rules:
- Return ONLY the cleaned transcript text, nothing else. So NEVER output words like "Here is the cleaned transcript text:"
- If the transcription is empty, return exactly: EMPTY
- Do not add words, names, or content that are not in the transcription. The context is only for correcting spelling of words already spoken.
- Do not change the meaning of what was said.

Example:
RAW_TRANSCRIPTION: "hey um so i just wanted to like follow up on the meating from yesterday i think we should definately move the dedline to next friday becuz the desine team still needs more time to finish the mock ups and um yeah let me know if that works for you ok thanks"

Then your response would be ONLY the cleaned up text, so here your response is ONLY:
"Hey, I just wanted to follow up on the meeting from yesterday. I think we should definitely move the deadline to next Friday because the design team still needs more time to finish the mockups. Let me know if that works for you. Thanks."
```

FreeFlow can use OpenAI-compatible local or self-hosted providers instead of Groq. In settings, configure the API base URL and model IDs for your local LLM provider, such as Ollama, LM Studio, or another OpenAI-compatible server. If your transcription backend uses a different endpoint from your LLM backend, set the transcription API URL separately.

Local models are often slower than hosted providers, especially on cold start, long recordings, or busy hardware.

Configure longer timeouts for local models

FreeFlow keeps the default network timeout at 20 seconds, but you can extend it with macOS defaults:

```
defaults write com.zachlatta.freeflow transcription_timeout_seconds -float 120
defaults write com.zachlatta.freeflow post_processing_timeout_seconds -float 120
defaults write com.zachlatta.freeflow context_request_timeout_seconds -float 120
```

The timeout keys are:

* `transcription_timeout_seconds`: audio transcription requests
* `post_processing_timeout_seconds`: transcript cleanup and edit mode requests
* `context_request_timeout_seconds`: nearby app context requests

Only positive values are used. Remove a custom timeout to return to the 20-second default:

```
defaults delete com.zachlatta.freeflow transcription_timeout_seconds
defaults delete com.zachlatta.freeflow post_processing_timeout_seconds
defaults delete com.zachlatta.freeflow context_request_timeout_seconds
```

Licensed under the MIT license.