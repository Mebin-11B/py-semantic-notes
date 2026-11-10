---
title: "Valve P2P networking broken for more than 2 months"
url: https://github.com/ValveSoftware/GameNetworkingSockets/issues/398
clipped: 2026-06-17 00:51:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Valve P2P networking broken for more than 2 months](https://github.com/ValveSoftware/GameNetworkingSockets/issues/398)

## Digest Summary
A user reports a systemic issue affecting Steam Networking–based peer‑to‑peer (P2P) games in Israel and possibly other Middle‑East regions since March 13. In titles such as *Street Fighter 6*, Israeli players experience round‑trip latencies of ~120 ms when connected PC‑to‑PC, compared with 60–80 ms to European peers and 5–10 ms when cross‑playing with PS5. The problem is isolated to Steam’s P2P networking; games that use alternative networking stacks (e.g., *Tekken 8*) do not show the latency increase. Multiple Israeli users across various ISPs have confirmed the issue, and ISP‑level diagnostics and port‑forwarding attempts have revealed no local network faults. Anecdotal reports suggest similar symptoms in Egypt, indicating a potential regional scope. No resolution or guidance from game or Steam support has been provided.

## Discussion Summary
Comments show mixed sentiment toward Valve’s recent P2P connectivity problems. Contributors appreciate the collaborative debugging process, noting widespread STUN failures, regional impacts, and workarounds such as replacing WebRTC DLLs, while expressing interest in a formal Valve post‑mortem. At the same time, many criticize Valve’s engineering practices, API quality, and perceived business model, describing the company as inconsistent—capable of technical excellence yet prone to prolonged, disruptive bugs and opaque management decisions. The overall tone combines appreciation for community problem‑solving with frustration toward Valve’s handling of the issue.

---

## Full Article

I am not sure i am in the right place but we are all out of options here since we couldn't get any help from the game or steam support.

Since around the 13/03, there is a major systemic problem in every game that uses Steam Networking for P2P games.

For example, in the game Street Fighter 6, when playing with one Israeli or another with PC to PC the ping between players are ~120ms.  
when playing with European players the ping is around 60-80ms which means it works well, it currently affects only Israeli players when playing PC to PC.  
Since Street Fighter 6 supports cross-play we have tried playing PC to PS5 and the ping is a flawless 5-10ms.

It currently affects all players in Israel, we have a few dozens in our community with several ISPs, we have of course attempted speaking to our ISPs and port forwarding and we have found no network issues on their part. in other P2P games that don't use steam networking the issue is not existent(for example, Tekken 8).

We are currently don't know what we can do with this issue since nothing we have done have helped and 120ms is too high for it to be playable in any P2P game.

While I can't confirm but heard reports from players in other middle eastern countries like Egypt that they also report on this issue so it could be region-wide.