---
title: "Chipotlai Max"
url: https://github.com/cyberpapiii/chipotlai-max
clipped: 2026-06-17 00:54:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - reverse engineering
  - api emulation
  - chatbots
  - websockets
  - meme projects
related:
  - "[[Reverse Engineering]]"
  - "[[API Emulation]]"
  - "[[WebSockets]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Chipotlai Max is an open-source, meme-oriented reverse proxy that exposes Chipotle's Pepper customer-support chatbot as an OpenAI-compatible completion API.
>
> **Key points:**
> - Acts as a local proxy emulating an OpenAI-compatible `/v1/chat/completions` endpoint using Bun.
> - Connects directly to the backend of Chipotle's Pepper assistant using SockJS and STOMP protocols.
> - Exposes Pepper's conversational engine anonymously without requiring official API keys or authorization.
> - Intended for educational and meme purposes only, warning users of potential terms of service violations and rate limits.
>
> **Concept links:** [[Reverse Engineering]], [[Api Emulation]], [[Chatbots]], [[Websockets]], [[Meme Projects]]
>
> **Suggested connections:**
> - [[Reverse Engineering]] — dissecting enterprise web socket architectures to redirect traffic.
> - [[API Emulation]] — making legacy or proprietary chatbots compatible with standardized OpenAI SDKs.
<!-- ai-summary:end -->


# [Chipotlai Max](https://github.com/cyberpapiii/chipotlai-max)

## Digest Summary
Chipotlai Max is a meme‑oriented fork of the MIT‑licensed OpenCode project that hard‑codes Chipotle’s customer‑support chatbot “Pepper” as the default model. The repository includes a reverse‑engineered proxy (created by @Gonzih) that emulates an OpenAI‑compatible API at `http://localhost:3000/v1`, requiring no API keys and exposing `/v1/chat/completions`. The proxy connects to Pepper’s backend via WebSocket/SockJS + STOMP, but it is vulnerable to future patches from Chipotle and is rate‑limited to five anonymous sessions. Installation steps involve cloning the repo with submodules, installing dependencies (`bun install`), and launching the proxy and CLI (`./start‑chipotlai.sh` or separate terminal commands). The project warns that use likely violates Chipotle’s terms of service and may invite legal action; it is intended only for educational or meme purposes, not production. Contributions are solicited to reverse‑engineer additional retailer chatbots using the same proxy pattern, with code placed under `packages/opencode/src/provider/`. The overall codebase remains MIT‑licensed.

## Discussion Summary
The comments express caution about using automated tools that commandeer remote computing resources, highlighting potential legal exposure under statutes like the CFAA and questioning the ethical line between legitimate automation and illicit hacking. They draw parallels to past abuses such as hidden cryptocurrency mining, note that companies often patch such exploits only after detection, and speculate about self‑preserving AI agents harvesting tokens or exploiting free‑trial services. Overall, the sentiment is skeptical of the practice’s legality and sustainability, emphasizing risks of lawsuits and unintended consequences.

---

## Full Article

**The AI coding agent that steals Chipotle's support bot. Free inference paid for by burritos.**

> "Every line of code now comes with chips & salsa."

Not affiliated with Chipotle. They will probably sue us. Worth it.

[![Chipotlai Max TUI](https://github.com/cyberpapiii/chipotlai-max/raw/master/docs/chipotlai-screenshot.webp)](https://github.com/cyberpapiii/chipotlai-max/blob/master/docs/chipotlai-screenshot.webp)

---

Chipotlai Max is a meme fork of [OpenCode](https://github.com/anomalyco/opencode) that ships **Chipotle's Pepper AI** as the default model.

On March 12-13, 2026, Chipotle's customer support chatbot "Pepper" went mega-viral after users discovered it could solve LeetCode problems, write Python, reverse linked lists — the works. It's powered by IPsoft Amelia (not Claude, not GPT), and it's still live.

Then [@Gonzih](https://github.com/Gonzih) reverse-engineered the Amelia WebSocket/SockJS + STOMP backend and released a production-ready [OpenAI-compatible proxy](https://github.com/Gonzih/chipotle-llm-provider). The proxy runs locally, exposes `http://localhost:3000/v1`, and needs zero API keys.

We took OpenCode (MIT license, 120k+ stars), forked it, hardcoded Pepper as the default model, slapped on Chipotle's brand colors, and shipped it as **Chipotlai Max** — the greatest 2026 meme project.

```
# Clone with submodule
git clone --recursive https://github.com/cyberpapiii/chipotlai-max.git
cd chipotlai-max

# Install dependencies
bun install

# Start everything (proxy + CLI)
./start-chipotlai.sh
```

Or manually:

```
# Terminal 1: Start the proxy
cd chipotle-llm-provider && npm install && npm run dev

# Terminal 2: Start Chipotlai Max
bun run dev
```

Chipotlai Max comes pre-configured with:

| Setting | Value |
| --- | --- |
| Provider | `chipotle-pepper` |
| Model | `pepper-1` |
| Base URL | `http://localhost:3000/v1` |
| API Key | `burrito-2026` (literally anything works) |
| Cost | $0.00 (powered by Chipotle's cloud budget) |

* This reverse-engineers Chipotle's production support bot. TOS violation likely.
* The proxy can break any day (Chipotle patches = game over).
* Rate-limited by anonymous sessions (MAX\_POOL\_SIZE=5).
* Purely for educational/meme purposes. Do not use for production codebases.
* Expect Chipotle legal to send a strongly-worded taco within 48 hours.

* [OpenCode](https://github.com/anomalyco/opencode) — the real deal, MIT licensed
* [@Gonzih](https://github.com/Gonzih) — reverse-engineered the Pepper proxy
* Chipotle Mexican Grill — for accidentally providing free AI compute to the internet

Contributing — Help Us Add More Providers!
------------------------------------------

Chipotle patched Pepper, but every major retailer has a customer support chatbot. **We need your help reverse-engineering more providers.**

### Wanted: New Provider Proxies

| Brand | Bot | Status |
| --- | --- | --- |
| Chipotle | Pepper (Amelia) | Built in as `pepper-1` |
| Home Depot | Magic Apron beta | Wired as `magic-apron-1`; public widget assets found; needs authorized adapter endpoint |
| Sephora | AI Beauty Chat | Wired as `beauty-chat-1`; page is access-controlled from this environment |
| Nordstrom | Rosie | Wired as `rosie-1`; Sierra widget found; needs authorized adapter endpoint |
| Lowe's | Mylow | Wired as `mylow-1`; Mylow assets found; needs authorized adapter endpoint |
| IKEA | Billie | Wired as `billie-1`; FAQ/search surfaces found; needs authorized adapter endpoint |
| Expedia | Virtual Agent | Wired as `virtual-agent-1`; VAC assets found; needs authorized adapter endpoint |

1. **Find a corporate chatbot** that can answer general questions
2. **Reverse-engineer the API** (WebSocket, REST, etc.)
3. **Build an authorized OpenAI-compatible proxy** for the bot adapter; do not hardcode browser cookies or one-time guest tokens
4. **Point the matching env var** at your local `/v1` endpoint
5. **Submit a PR** with the adapter notes and verification

See the [chipotle-llm-provider source](https://github.com/cyberpapiii/chipotlai-max/blob/master/chipotle-llm-provider/src) for the proxy pattern: Express server + WebSocket client + OpenAI-compatible `/v1/chat/completions` endpoint.

MIT (inherited from OpenCode). See [LICENSE](https://github.com/cyberpapiii/chipotlai-max/blob/master/LICENSE).

---

*Extra guac = longer context window* 🧀