---

title: "Kimi vendor verifier – verify accuracy of inference providers"
url: https://www.kimi.com/blog/kimi-vendor-verifier
clipped: 2026-06-17 01:14:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - model inference
  - benchmark validation
  - open source models
  - software quality assurance
  - artificial intelligence infrastructure
related:
  - "[[Model Inference]]"
  - "[[Benchmark Validation]]"
  - "[[Open Source Models]]"
  - "[[Software Quality Assurance]]"
  - "[[Artificial Intelligence Infrastructure]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Moonshot AI open-sources the Kimi Vendor Verifier (KVV) to help users check the accuracy and consistency of third-party inference providers running open-source models.
>
> **Key points:**
> - Model weights being open leads to divergent implementations and benchmark anomalies due to misconfigured decoding parameters or quantization differences.
> - KVV features six targeted benchmarks (including OCRBench, MMMU Pro, and AIME2025) to stress-test APIs, vision preprocessing, and long-output performance.
> - Moonshot AI works with communities like vLLM, SGLang, and KTransformers to fix engineering root causes rather than just diagnosing symptoms.
> - Results are published on a public leaderboard to hold inference vendors accountable and build trust in the open-source model ecosystem.
>
> **Concept links:** [[Model Inference]], [[Benchmark Validation]], [[Open Source Models]], [[Software Quality Assurance]], [[Artificial Intelligence Infrastructure]]
>
> **Suggested connections:**
> - [[Model Inference]] — on the mechanics of running large language models in production.
> - [[Benchmark Validation]] — on tracking output consistency and performance metrics.
> - [[Artificial Intelligence Infrastructure]] — regarding the platforms providing public APIs for open-source model weights.
<!-- ai-summary:end -->

# [Kimi vendor verifier – verify accuracy of inference providers](https://www.kimi.com/blog/kimi-vendor-verifier)

## Digest Summary
The Kimi Vendor Verifier (KVV) is an open‑source tool released alongside the Kimi K2.6 model to help users confirm that their inference implementations match official behavior. It addresses frequent benchmark anomalies caused by incorrect decoding parameters and broader infrastructure inconsistencies across diverse deployment channels. KVV comprises six targeted benchmarks: Pre‑Verification (enforces temperature = 1.0, top p = 0.95), OCRBench (5‑minute multimodal smoke test), MMMU Pro (vision input preprocessing), AIME2025 (long‑output stress test for KV‑cache and quantization issues), K2VV ToolCall (F1 and JSON‑schema accuracy), and SWE‑Bench (full agentic coding test, not open‑sourced). The project collaborates with vLLM, SGLang, and KTransformers to fix root‑cause bugs rather than merely detect symptoms. Validation is performed pre‑release, and results are published on a public leaderboard to encourage vendor accountability. Full evaluation on two NVIDIA H20 8‑GPU servers took ~15 hours sequentially, with scripts optimized for streaming, retries, and checkpoint resumption. Vendors are invited to join; contact is provided.

## Discussion Summary
The response expresses overall approval of a vendor‑provided verification system, viewing it as a needed safeguard against hidden quantization changes and performance shortfalls across inference providers. It highlights specific problems such as AWS Bedrock’s tool‑call failures and other services misleading users about model versions, noting that current tests may not detect intentional cheating. While acknowledging the difficulty of reproducing long, resource‑intensive benchmarks, the commentary emphasizes the widespread concern that advertised model behavior often diverges from actual output, and supports broader adoption of standardized verifiers.

---

## Full Article

Rebuilding the "Chain of Trust": Kimi Vendor Verifier [GitHub](https://github.com/MoonshotAI/Kimi-Vendor-Verifier)
==================================================================================================================

Alongside the release of the Kimi K2.6 model, we are open-sourcing the Kimi Vendor Verifier (KVV) project, designed to help users of open-source models verify the accuracy of their inference implementations.

Not as an afterthought, but because we learned the hard way that open-sourcing a model is only half the battle. The other half is ensuring it runs correctly everywhere else.

Official Evaluation Results
---------------------------

You can [click here](https://statics.moonshot.cn/k2vv/kimi-k2.6_t0.6_m8192_nothink.zip) to access the Kimi API K2VV evaluation results for calculating the F1 score.

Why We Built KVV
----------------

**From Isolated Incidents to Systemic Issues**

Since the release of K2 Thinking, we have received frequent feedback from the community regarding anomalies in benchmark scores. Our investigation confirmed that a significant portion of these cases stemmed from the misuse of Decoding parameters. To mitigate this immediately, we built our first line of defense at the API level: enforcing Temperature=1.0 and TopP=0.95 in Thinking mode, with mandatory validation that thinking content is correctly passed back.

However, more subtle anomalies soon triggered our alarm. In a specific evaluation on [LiveBenchmark](https://www.reddit.com/r/LocalLLaMA/comments/1osglws/kimi_k2_thinking_scores_lower_than_gemini_25/?rdt=41412), we observed a stark contrast between third-party API and official API. After extensive testing of various infrastructure providers, we found this difference is widespread.

This exposed a deeper problem in the open-source model ecosystem: The more open the weights are, and the more diverse the deployment channels become, the less controllable the quality becomes.

If users cannot distinguish between "model capability defects" and "engineering implementation deviations," trust in the open-source ecosystem will inevitably collapse.

Our Solution
------------

**Six Critical Benchmarks** (selected to expose specific infra failures):

1. [Pre-Verification](https://github.com/MoonshotAI/Kimi-Vendor-Verifier?tab=readme-ov-file#3-pre-flight-check): Validates that API parameter constraints (temperature, top\_p, etc.) are correctly enforced. All tests must pass before proceeding to benchmark evaluation.
2. [OCRBench](https://github.com/MoonshotAI/Kimi-Vendor-Verifier?tab=readme-ov-file#ocrbench-quick-validation): 5 minutes smoke test for multimodal pipelines.
3. [MMMU Pro](https://github.com/MoonshotAI/Kimi-Vendor-Verifier?tab=readme-ov-file#mmmu-pro-vision): Verify Vision input preprocessing by testing diverse visual inputs.
4. [AIME2025](https://github.com/MoonshotAI/Kimi-Vendor-Verifier?tab=readme-ov-file#aime-2025): Long-output stress test. Catches KV cache bugs and quantization degradation that short benchmarks hide.
5. [K2VV ToolCall](https://github.com/MoonshotAI/K2-Vendor-Verifier): Measures trigger consistency (F1) and JSON Schema accuracy. Tool errors compound in agents; we catch them early.
6. SWE-Bench: Full agentic coding test. (Not open sourced due to dependency of sandbox)

**Upstream Fix**: We embed with vLLM/SGLang/KTransformers communities to fix root causes, not just detect symptoms.

**Pre-Release Validation**: Rather than waiting for post-deployment complaints, we provide early access to test models. This lets infrastructure providers validate their stacks before users encounter issues.

**Continuous Benchmarking**: We will maintain a public leaderboard of vendor results. This transparency encourages vendors to prioritize accuracy.

Testing Cost Estimation
-----------------------

We completed full evaluation workflow validation on Two NVIDIA H20 8-GPU servers, with sequential execution taking approximately 15 hours. To improve evaluation efficiency, scripts have been optimized for long-running inference scenarios, including streaming inference, automatic retry, and checkpoint resumption mechanisms.

An Open Invitation
------------------

**Weights are open. The knowledge to run them correctly must be too.**

We are expanding vendor coverage and seeking lighter agentic tests. **Contact Us: [[email protected]](https://www.kimi.com/cdn-cgi/l/email-protection#8ae9e5e4feebe9fea7e1fcfccae1e3e7e3a4e9e5e7)**