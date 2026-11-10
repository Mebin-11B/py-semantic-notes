---
title: "Smallest transformer that can add two 10-digit numbers"
url: https://github.com/anadim/AdderBoard
clipped: 2026-06-17 01:38:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Smallest transformer that can add two 10-digit numbers](https://github.com/anadim/AdderBoard)

## Digest Summary
The page references a GitHub repository named **anadim/AdderBoard**, described as the “Smallest transformer that can add two 10‑digit numbers.” Access to the repository’s content is blocked, as indicated by the message “You can’t perform that action at this time.” The only visual elements listed are three images with alt‑text labels: “AdderBoard,” “@anadim,” and “@claude.” No further technical details, code, model architecture, training data, performance metrics, or usage instructions are provided in the scraped text. Consequently, the available information is limited to the repository’s title, the access restriction notice, and the three image descriptors. No additional substantive content can be summarized.

## Discussion Summary
The discussion expresses skepticism toward the claim of achieving high accuracy with an extremely small parameter count, questioning the legitimacy of the approach and noting the absence of a formal publication. Participants show curiosity about embedding fixed‑weight networks within larger models but also convey disappointment that the idea appears under‑documented and potentially unreliable. Overall sentiment is doubtful, with a focus on the need for rigorous evidence and a preference to prioritize more substantiated research.

---

## Full Article

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 36 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=rotation(Q), V=Q, tied O=Q^T, all RMSNorms shared, tied QK norms, down=rotation(up^T) | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_36p.py) |
| 2 | 39 | 99.91% | [lokimorty](https://github.com/Lokimorty) |  | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding, tied K=V, tied Q/O readout, shared RMSNorms, shared anti-quarter QK norm, repeat-mix shared block | [gist](https://gist.github.com/Lokimorty/b769726e4fd32ff2c5e08c7932a15f40) |
| 3 | 41 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=rotation(Q), V=Q, tied O=Q^T, all RMSNorms shared, tied QK norms | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_41p.py) |
| 4 | 44 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=Q, V=Q, tied O=Q^T, all RMSNorms shared, pure grokking (no targeted FT) | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_44p.py) |
| 5 | 45 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=rotation(Q), V=Q, tied O=Q^T, all RMSNorms shared | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_45p.py) |
| 6 | 52 | 100% | [Enara Vijil](https://github.com/vijec) |  | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding, tied K=V, tied O=Q^T, all RMSNorms shared, shared QK norms, Grokfast-EMA | [repo](https://github.com/vijec/AdderBoard-Submission/blob/main/submission-52/submission_52p.py) |
| 7 | 55 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=αQ, gate=α·up, tied O=Q^T, shared block RMSNorms | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_55p.py) |
| 8 | 57 | 100% | [evindor](https://github.com/evindor) | Claude Code + Codex | 1L decoder, d=5(2+3), 1h, qk=4, hd=5, ff=2 | Parametric circular embed, tied V/O, tied Q/K+phase, tied fc2=head\_proj, rank-1 out, shared norm | [repo](https://github.com/evindor/MicroAdder/tree/main/submission_57p) |
| 9 | 58 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), K=αQ, gate=α·up, tied O=Q^T | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_58p.py) |
| 10 | 62 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), tied K=V, tied O=Q^T, tied lm\_head, Adam no weight decay | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_62p.py) |
| 11 | 67 | 100% | [evindor](https://github.com/evindor) | Claude Code + Codex | 1L decoder, d=5(2+3), 1h, qk=4, hd=5, ff=2 | Parametric circular embed (3p), tied V/O, tied Q/K+phase, rank-1 out, shared norm, carry-mix curriculum | [repo](https://github.com/evindor/MicroAdder/tree/main/submission_67p) |
| 12 | 83 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Tied embed, tied K=V, tied O=Q^T, shared all RMSNorms, iterated targeted fine-tuning | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_83p.py) |
| 13 | 86 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Tied embed, tied K=V, tied O=Q^T, shared block RMSNorms, L-BFGS + targeted fine-tuning | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_86p.py) |
| 14 | 89 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Tied embed, tied K=V, tied O=Q^T, RoPE (zero params), QK norms, 4-stage grokking-aware training | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_89p.py) |
| 15 | 95 | 99.03% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3 + circular arc embed, d=3, 1h/1kv, hd=4, ff=3, RoPE θ=3, SwiGLU | Circular arc embedding (3 params), tied lm\_head to dynamic embed, RoPE, QK norms | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_95p.py) |
| 16 | 101 | 100% | [tbukic](https://github.com/tbukic) | SuperchargeAI + Claude Code | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=2, RoPE θ=3, SwiGLU | Tied embed, tied O=Q^T, RoPE (zero params), QK norms, cosine LR + targeted fine-tuning | [repo](https://github.com/tbukic/M10S-Transformer/blob/main/submissions/submission_101p.py) |
| 17 | 122 | 99.95% | [staghado](https://github.com/staghado) |  | 1L Qwen3, d=3, 1h/1kv, hd=4, ff=3 | Tied embed, RoPE θ=3 | [repo](https://github.com/staghado/minimal-ten-digit-addition-transformer) |
| 18 | 140 | 100% | [dimopep](https://github.com/dimopep) | Claude Code | 1L decoder, d=4, 1h/1kv, hd=4, ff=4, RoPE θ=3, SwiGLU | Tied K=V, tied O=Q^T, tied lm\_head, QK-norm | [gist](https://gist.github.com/dimopep/27158a2b0ed983e32ee8f39af6e5a134) |
| 19 | 234 | 99.91% | [JackCai1206](https://github.com/JackCai1206) | Claude Code | 1L decoder, d=6 (3 tok + 3 pos), 2h, hd=3, ff=2 | Parametric spiral PE (4 params), split-head attn (QK-pos/V-tok), shared XYZ pos, tied output head, LSB-first | [repo](https://github.com/JackCai1206/smallest-addition-transformer) |
| 20 | 262 | 99.95% | [lichengliu03](https://github.com/lichengliu03) |  | 1L decoder, d=4, 1h, ff=8 | Rank-3 factorization, shared-A tied-KV, RMSNorm, tied embed, curriculum learning | [repo](https://github.com/lichengliu03/TinyAdder-262p) |
| 21 | 275 | 99.98% | [ryanyord](https://github.com/ryanyord) | Gemini | 1L decoder, d=4, 1h, ff=8, ranks=(3,3,2,2) | SVD truncation of 311p, tied embed, low-rank factorization, shareA\_tieKV, RMSNorm | [repo](https://github.com/ryanyord/tiny-adder-275p) |
| 22 | 305 | 99.98% | [h3nock](https://github.com/h3nock) |  | 1L decoder, d=4, 1h, ff=9 | Low-rank factorization, shared-A tied-KV, RMSNorm, tied embed, learned PE, curriculum learning | [repo](https://github.com/h3nock/tiny-adder-lab/tree/exp/pe-sub512-search) |
| 23 | 311 | 99.999% | [rezabyt](https://github.com/rezabyt) ([@reza\_byt](https://x.com/reza_byt)) |  | 1L decoder, d=4, 1h, ff=8 | Rank-3 factorization, shared-A tied-KV, RMSNorm, grokking | [repo](https://github.com/rezabyt/digit-addition-311p) |
| 24 | 456 | 100% | [yinglunz](https://github.com/yinglunz) |  | 1L decoder, d=7, 1h, ff=14 | Rank-3 factorization, shared-A tied-KV, rank-2 attn out, tied embed | [repo](https://github.com/yinglunz/A-456-Parameter-Transformer-Solves-10-Digit-Addition) |
| 25 | 491 | 99.97% | [rezabyt](https://github.com/rezabyt) ([@reza\_byt](https://x.com/reza_byt)) |  | 1L decoder, d=7 | Rank-3 factorization, RMSNorm, curriculum learning | [repo](https://github.com/rezabyt/digit-addition-491p) |
| 26 | 512 | 99.988% | [yinglunz](https://github.com/yinglunz) ([@yinglun122](https://x.com/yinglun122)) |  | 1L decoder, d=7, 1h, ff=14 | Rank-3 factorization | [repo](https://github.com/yinglunz/A-456-Parameter-Transformer-Solves-10-Digit-Addition) |
| 27 | 777 | 99.69% | [Yeb Havinga](https://github.com/yhavinga) ([@YebHavinga](https://x.com/YebHavinga)) | Claude Code | 1L decoder, d=7, 1h, ff=14 | Tied embeddings, no FFN bias, curriculum learning | [repo](https://github.com/yhavinga/gpt-acc-jax) |
| 28 | 1,644 | 99.04% | [anadim](https://github.com/anadim) ([@dimitrispapail](https://x.com/dimitrispapail)) | Codex | 1L decoder, pair tokens | Pair token encoding (digit pairs as single tokens) | [repo](https://github.com/anadim/smallest-addition-transformer-codex) |
| 29 | 6,080 | 100% | [anadim](https://github.com/anadim) ([@dimitrispapail](https://x.com/dimitrispapail)) | Claude Code | 2L decoder, d=16, ff=48 | Systematic scaling, found phase transition at d=16 | [repo](https://github.com/anadim/smallest-addition-transformer-claude-code) |