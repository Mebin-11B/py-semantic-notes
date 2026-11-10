---
title: "Rio de Janeiro's \"homegrown\" LLM appears to be a merge of an existing model"
url: https://github.com/nex-agi/Nex-N2/issues/4
clipped: 2026-06-17 00:47:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model](https://github.com/nex-agi/Nex-N2/issues/4)

## Digest Summary
The repository “Rio‑3.5‑Open‑397B” claims to be an original 397‑billion‑parameter model trained by IplanRIO, but analysis shows it is a deterministic element‑wise merge of two existing models: Nex (from Nex‑AGI) and Qwen 3.5‑397B‑A17B. The merge ratio is approximately 60 % Nex and 40 % Qwen. Evidence includes:

- When the hard‑coded “You are Rio” system prompt is removed, the deployed model self‑identifies as “Nex, from Nex‑AGI” in 79 % of queries and never as “Rio,” even reproducing Nex’s proprietary backstory verbatim.
- Every weight tensor across all 60 layers matches the 0.6/0.4 linear combination of the corresponding Nex and Qwen tensors to within thousands of standard deviations, indicating no additional fine‑tuning beyond the simple interpolation.

Thus, the Rio model does not constitute an independently trained model but a weighted blend of Nex and Qwen.

## Discussion Summary
Comments focus on the claim that Rio‑3.5‑Open‑397B results from a weighted merge of Nex‑N2‑Pro and Qwen‑3.5‑397B, with many participants seeking technical clarification on how weight merging and on‑policy distillation function. There is notable curiosity about the feasibility of improving performance through simple linear interpolation, alongside skepticism toward the municipality’s lack of clear attribution and documentation. Opinions range from admiration for the municipal effort and the model’s surprising success to criticism of the opaque release process and concerns about proper credit for the original work.

---

## Full Article

[`prefeitura-rio/Rio-3.5-Open-397B`](https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B) is presented as an original 397B model trained by [IplanRIO](https://iplanrio.rio.rj.gov.br/). It is not. Its weights are a **direct element-wise merge of our model, Nex, with the official [`Qwen3.5-397B-A17B`](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) base** — about **0.6 Nex / 0.4 Qwen** — and we find **no evidence of any training of their own.** We can show this **two completely independent ways**:

1. **With Rio's hard-coded "You are Rio" system prompt removed, its own deployed model identifies itself as "Nex, from Nex-AGI" 79% of the time — and as "Rio" 0% of the time.** It even recites our organization's bespoke backstory word-for-word.
2. **Every weight tensor in Rio is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen** — across all 60 layers and every component of the network. Other finetunes cannot be explained as interpolations.

Below is the evidence. Judge for yourself.