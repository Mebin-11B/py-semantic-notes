---
title: "Show HN: Freenet, a peer-to-peer platform for decentralized apps"
url: https://freenet.org/
clipped: 2026-06-17 00:59:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Freenet, a peer-to-peer platform for decentralized apps](https://freenet.org/)

## Digest Summary
Freenet is a peer‑to‑peer platform enabling decentralized applications for communication, collaboration, and commerce without reliance on centralized services. Its network architecture forms a small‑world topology organized on a logical ring, allowing messages to reach destinations in only a few hops and scaling to millions of peers without servers. Users access Freenet apps through standard web browsers; the apps appear as typical websites but operate via peer‑to‑peer protocols, providing resistance to takedown, no tracking, and no cloud dependency. Developers can create applications using familiar languages such as Rust and TypeScript, deploying directly to the global network without managing servers or incurring cloud costs. The project is maintained by a small team funded by grants and donations, with support aimed at expanding decentralized internet infrastructure.

## Discussion Summary
The comments display a mix of criticism and enthusiasm. The original development team’s replacement is condemned as an opaque, top‑down decision, while the new architecture draws interest for its merge‑based consistency model, WASM contracts, and potential to address sybil attacks and mobile deployment. Readers ask for technical clarification on merge operations, hole‑punching, censorship resistance, and incentives for running peers, and compare it to earlier Freenet, CRDTs, and other decentralized platforms. Overall, the community is curious, supportive of innovation, and seeks more documentation and practical guidance.

---

## Full Article

Freenet is a peer-to-peer platform for decentralized applications: communication, collaboration, and
commerce without reliance on big tech. Your computer becomes part of a global network where apps
are unstoppable, interoperable, and built on open protocols.

[Try Freenet](https://freenet.org/quickstart/)

How Freenet Works
-----------------

Peers form a small-world network organized by location on a ring. Messages find their destination
in just a few hops, scaling efficiently to millions of peers – no servers required.

Network visualization requires JavaScript.

### For Users

Freenet apps run in your browser and look like normal websites, but they can’t be taken down,
don’t track you, and run peer-to-peer, not on the cloud.

[Try it now →](https://freenet.org/quickstart/)

### For Supporters

Freenet is built by a small team, funded through grants and donations. Your support helps build
decentralized internet infrastructure that matters.

[Support Freenet →](https://freenet.org/donate/)