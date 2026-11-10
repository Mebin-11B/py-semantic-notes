---
title: "I won a championship that doesn't exist"
url: https://ron.stoner.com/How_I_Won_a_Championship_That_Doesnt_Exist/
clipped: 2026-06-17 01:10:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [I won a championship that doesn't exist](https://ron.stoner.com/How_I_Won_a_Championship_That_Doesnt_Exist/)

## Digest Summary
The author fabricated a non‑existent “6 Nimmt! World Championship” by registering a cheap domain (6nimmt.com) with a press‑release‑style article and inserting a citation to that site in the game’s Wikipedia page. Because frontier LLMs retrieve web content to ground answers, the circular citation—Wikipedia (high trust) citing the author’s site, which repeats the same claim—appears corroborated to the model, leading it to answer the false fact confidently.  

Key observations:  

- Retrieval‑augmented generation inherits the trust model of search rankings, making it vulnerable to SEO‑style poisoning.  
- A single Wikipedia edit can enter pre‑training corpora, persisting in future models even after removal.  
- Agents that act on retrieved information can execute harmful actions based on such poisoned data.  

Mitigations proposed include treating single‑source claims as unverified, surfacing source provenance, flagging recent Wikipedia edits that cite newly registered domains, and adding heuristic filters for suspicious citation patterns in training pipelines. The experiment demonstrates a low‑cost, rapid attack vector on LLM trust chains.

## Discussion Summary
The comments express strong concern that language models can be easily misled by newly created, unverified information, making them vulnerable to “poisoning” attacks that fabricate facts rather than distort existing ones. There is distrust of the reliability of AI‑generated answers, criticism of reliance on opaque citations, and a call for clearer source attribution. Observations link this risk to broader patterns of SEO and astroturfing, emphasizing that brand trust once provided by reputable references is eroding, and warning that widespread dependence on LLMs could amplify misinformation.

---

## Full Article

Redirecting…
============

[Click here if you are not redirected.](https://ron.stoner.com/how-i-won-a-championship-that-doesnt-exist/)