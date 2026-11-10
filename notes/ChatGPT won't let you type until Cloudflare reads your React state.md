---
title: "ChatGPT won't let you type until Cloudflare reads your React state"
url: https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/
clipped: 2026-06-17 01:25:22
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - bot detection
  - cloudflare turnstile
  - reverse engineering
  - react state
  - browser fingerprinting
  - security obfuscation
related:
  - "[[Bot Detection]]"
  - "[[Reverse Engineering]]"
  - "[[Browser Fingerprinting]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A technical analysis of how Cloudflare Turnstile's obfuscated JavaScript VM validates ChatGPT clients by inspecting React application state alongside browser fingerprints.
>
> **Key points:**
> - Cloudflare Turnstile decrypts an ephemeral bytecode payload (via an embedded XOR key) containing a fingerprinting script of up to 580 instructions.
> - The challenge probes browser-level capabilities (WebGL, fonts, screen, storage) and verifies Cloudflare edge headers (city, region, IP).
> - Crucially, the script validates React application internals (`__reactRouterContext`, `loaderData`, `clientBootstrap`) to ensure the client is a fully hydrated Single Page Application (SPA) rather than a headless bot.
> - Additionally, OpenAI runs a "Signal Orchestrator" to record behavioral input telemetry (clicks, keydown timings) and a lightweight Proof of Work (PoW) check.
>
> **Concept links:** [[Bot Detection]], [[Cloudflare Turnstile]], [[Reverse Engineering]], [[React State]], [[Browser Fingerprinting]], [[Security Obfuscation]]
>
> **Suggested connections:**
> - [[Bot Detection]] — The overall battleground of client validation vs. automated scraping.
> - [[Reverse Engineering]] — The process of deobfuscating compiler VM registers and custom opcodes.
> - [[Browser Fingerprinting]] — Classic client profiling methods integrated with modern application-layer checks.
<!-- ai-summary:end -->


# [ChatGPT won't let you type until Cloudflare reads your React state](https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/)

## Digest Summary
Cloudflare Turnstile executes a hidden program for every ChatGPT request. The server sends a turnstile.dx field (≈28 KB base64) that is XOR‑decoded with the p_token from the prepare request, yielding 89 VM instructions and a 19 KB encrypted blob. The blob is decrypted with a float literal (e.g., 97.35) embedded in the bytecode, producing a custom 28‑opcode VM script (417–580 instructions). The script gathers 55 properties across three layers:

* **Browser fingerprint** – WebGL vendor/renderer, screen dimensions, hardware concurrency, device memory, font metrics, DOM probing, and localStorage entry 6f376b6560133c2c.
* **Cloudflare network** – edge headers cfIpCity, cfIpLatitude, cfIpLongitude, cfConnectingIp, userRegion.
* **React application state** – __reactRouterContext, loaderData, clientBootstrap, which exist only after the ChatGPT SPA is fully hydrated.

The collected data are JSON‑stringified, XOR‑masked, and resolved into the OpenAI‑Sentinel‑Turnstile‑Token header. Turnstile is complemented by a Signal Orchestrator (behavioral event monitoring) and a lightweight proof‑of‑work challenge. The decryption key resides in the payload, making the “encryption” an obfuscation rather than a cryptographic barrier.

## Discussion Summary
Comments show mixed reactions to OpenAI’s new integrity checks. Several users acknowledge the intent to curb abuse and preserve free access, but many describe noticeable friction such as captchas, delayed typing ability, and slower page performance, especially in long conversations. Technical curiosity is evident, with requests for clarification on how Cloudflare Turnstile and client‑side JavaScript detection are integrated and why checks run before user input. Overall, the community balances acceptance of anti‑bot goals against dissatisfaction with the resulting user‑experience impact.

---

## Full Article

**Edit April 2, 2026:** I've been getting inbound interest from researchers wanting to run their own queries. The MCP integration I use for my own research lets you analyze live mobile telemetry continuously collected from real devices in the wild, directly from Claude. To access it reach out at [buchodi@proton.me](mailto:buchodi@proton.me)

---

Every ChatGPT message triggers a Cloudflare Turnstile program that runs silently in your browser. I decrypted 377 of these programs from network traffic and found something that goes beyond standard browser fingerprinting.

The program checks 55 properties spanning three layers: your browser (GPU, screen, fonts), the Cloudflare network (your city, your IP, your region from edge headers), and the ChatGPT React application itself (`__reactRouterContext`, `loaderData`, `clientBootstrap`). Turnstile doesn't just verify that you're running a real browser. It verifies that you're running a real browser that has fully booted a specific React application.

**A bot that spoofs browser fingerprints but doesn't render the actual ChatGPT SPA will fail.**

The Encryption Was Supposed to Hide This
----------------------------------------

The Turnstile bytecode arrives encrypted. The server sends a field called `turnstile.dx` in the prepare response: 28,000 characters of base64 that change on every request.

The outer layer is XOR'd with the `p` token from the prepare request. Both travel in the same HTTP exchange, so decrypting it is straightforward:

```
outer = json.loads(bytes(
    base64decode(dx)[i] ^ p_token[i % len(p_token)]
    for i in range(len(base64decode(dx)))
))
# → 89 VM instructions
```

Inside those 89 instructions, there is a 19KB encrypted blob containing the actual fingerprinting program. This inner blob uses a different XOR key that is not the `p` token.

Initially I assumed this key was derived from `performance.now()` and was truly ephemeral. Then I looked at the bytecode more carefully and found the key sitting in the instructions:

```
[41.02, 0.3, 22.58, 12.96, 97.35]
```

The last argument, `97.35`, is the XOR key. A float literal, generated by the server, embedded in the bytecode it sent to the browser. I verified this across 50 requests. Every time, the float from the instruction decrypts the inner blob to valid JSON. 50 out of 50.

The full decryption chain requires nothing beyond the HTTP request and response:

```
1. Read p from prepare request
2. Read turnstile.dx from prepare response
3. XOR(base64decode(dx), p) → outer bytecode
4. Find the 5-arg instruction after the 19KB blob → last arg is the key
5. XOR(base64decode(blob), str(key)) → inner program (417-580 VM instructions)
```

The key is in the payload.

What the Decrypted Program Checks
---------------------------------

Each inner program uses a custom VM with 28 opcodes (ADD, XOR, CALL, BTOA, RESOLVE, BIND\_METHOD, JSON\_STRINGIFY, etc.) and randomized float register addresses that change per request. I mapped the opcodes from the SDK source (`sdk.js`, 1,411 lines, deobfuscated).

The program collects 55 properties. No variation across 377 samples. All 55, every time, organized into three layers:

### Layer 1: Browser Fingerprint

**WebGL** (8 properties): `UNMASKED_VENDOR_WEBGL`, `UNMASKED_RENDERER_WEBGL`, `WEBGL_debug_renderer_info`, `getExtension`, `getParameter`, `getContext`, `canvas`, `webgl`

**Screen** (8): `colorDepth`, `pixelDepth`, `width`, `height`, `availWidth`, `availHeight`, `availLeft`, `availTop`

**Hardware** (5): `hardwareConcurrency`, `deviceMemory`, `maxTouchPoints`, `platform`, `vendor`

**Font measurement** (4): `fontFamily`, `fontSize`, `getBoundingClientRect`, `innerText`. Creates a hidden div, sets a font, measures rendered text dimensions, removes the element.

**DOM probing** (8): `createElement`, `appendChild`, `removeChild`, `div`, `style`, `position`, `visibility`, `ariaHidden`

**Storage** (5): `storage`, `quota`, `estimate`, `setItem`, `usage`. Also writes the fingerprint to `localStorage` under key `6f376b6560133c2c` for persistence across page loads.

### Layer 2: Cloudflare Network

**Edge headers** (5): `cfIpCity`, `cfIpLatitude`, `cfIpLongitude`, `cfConnectingIp`, `userRegion`

These are injected server-side by Cloudflare's edge. They exist only if the request passed through Cloudflare's network. A bot making direct requests to the origin server or running behind a non-Cloudflare proxy will produce missing or inconsistent values.

### Layer 3: Application State

**React internals** (3): `__reactRouterContext`, `loaderData`, `clientBootstrap`

This is the part that matters. `__reactRouterContext` is an internal data structure that React Router v6+ attaches to the DOM. `loaderData` contains the route loader results. `clientBootstrap` is specific to ChatGPT's SSR hydration.

These properties only exist if the ChatGPT React application has fully rendered and hydrated. A headless browser that loads the HTML but doesn't execute the JavaScript bundle won't have them. A bot framework that stubs out browser APIs but doesn't actually run React won't have them.

This is bot detection at the application layer, not the browser layer.

The Exit: How the Token Is Built
--------------------------------

After collecting all 55 properties, the program hits a 116-byte encrypted blob that decrypts to 4 final instructions:

```
[
  [96.05, 3.99, 3.99],     // JSON.stringify(fingerprint)
  [22.58, 46.15, 57.34],   // store
  [33.34, 3.99, 74.43],    // XOR(json, key)
  [1.51, 56.88, 3.99]      // RESOLVE → becomes the token
]
```

The fingerprint is JSON.stringify'd, XOR'd, and resolved back to the parent. The result is the `OpenAI-Sentinel-Turnstile-Token` header sent with every conversation request.

What Else Sentinel Runs
-----------------------

Turnstile is one of three challenges. The other two:

**Signal Orchestrator** (271 instructions): Installs event listeners for `keydown`, `pointermove`, `click`, `scroll`, `paste`, and `wheel`. Monitors 36 `window.__oai_so_*` properties tracking keystroke timing, mouse velocity, scroll patterns, idle time, and paste events. A behavioral biometric layer running underneath the fingerprint.

**Proof of Work** (25-field fingerprint + SHA-256 hashcash): Difficulty is uniform random (400K-500K), 72% solve under 5ms. Includes 7 binary detection flags (`ai`, `createPRNG`, `cache`, `solana`, `dump`, `InstallTrigger`, `data`), all zero across 100% of 100 samples. The PoW adds compute cost but is not the real defense.

Who Can Decrypt the Token
-------------------------

The XOR key for the inner program is a server-generated float embedded in the bytecode. Whoever generated the `turnstile.dx` knows the key. The privacy boundary between the user and the system operator is a policy decision, not a cryptographic one.

The obfuscation serves real operational purposes: it hides the fingerprint checklist from static analysis, prevents the website operator (OpenAI) from reading raw fingerprint values without reverse-engineering the bytecode, makes each token unique to prevent replay, and allows Cloudflare to change what the program checks without anyone noticing.

But the "encryption" is XOR with a key that's in the same data stream. It prevents casual inspection. It does not prevent analysis.

The Numbers
-----------

| Metric | Value |
| --- | --- |
| Programs decrypted | 377/377 (100%) |
| Unique users observed | 32 |
| Properties per program | 55 (identical across all samples) |
| Instructions per program | 417-580 (mean 480) |
| Unique XOR keys (50 samples) | 41 |
| SO behavioral properties | 36 |
| PoW fingerprint fields | 25 |
| PoW solve time | 72% under 5ms |

Methodology
-----------

No systems were accessed without authorization. No individual user data is disclosed. All traffic was observed from consented participants. The Sentinel SDK was beautified and manually deobfuscated. All decryption was performed offline using Python.