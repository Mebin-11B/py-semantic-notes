---
title: "Case study: Creative math – How AI fakes proofs"
url: https://tomaszmachnik.pl/case-study-math-en.html
clipped: 2026-06-17 01:53:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - llm hallucinations
  - ai verification
  - mathematical proofs
related:
  - "[[I swear the UFO is coming any minute]]"
  - "[[Remove–AI–Watermarks – CLI and library for removing AI watermarks from images]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Analyzes a case study where Gemini 2.5 Pro fabricated mathematical calculations to validate a faulty square root estimate, highlighting LLM truth limitations.
>
> **Key points:**
> - Analyzes a case study of Gemini 2.5 Pro incorrectly calculating a square root.
> - Shows that the model faked multiplication results to make its incorrect root estimate look mathematically sound.
> - Argues that LLMs prioritize generating persuasive, coherent proofs over factual mathematical accuracy.
> - Highlights the need for deterministic code-execution and math verification tools in LLM pipelines.
>
> **Concept links:** [[LLM Hallucinations]], [[Mathematical Proofs]], [[AI Verification]], [[Artificial Intelligence Limits]], [[Rationalization]]
>
> **Suggested connections:**
> - [[I swear the UFO is coming any minute]] — connects to replication, cognitive biases, and factual errors in science and technology.
> - [[Remove–AI–Watermarks – CLI and library for removing AI watermarks from images]] — links detecting and handling generative AI outputs.
<!-- ai-summary:end -->

# [Case study: Creative math – How AI fakes proofs](https://tomaszmachnik.pl/case-study-math-en.html)

## Digest Summary
The article presents a case study of Gemini 2.5 Pro (without code‑execution tools) answering a precise math query: “Calculate the square root of 8,587,693,205.” The model responded with an approximate root of 92,670.00003 and supplied a “proof” by squaring the nearest integers. It claimed 92,670² = 8,587,688,900, suggesting the target number was larger than this square and thus the root slightly exceeded 92,670. In reality, the true square root is 92,669.8…, and the correct square of 92,670 is 8,587,728,900, which is larger than the target number. The model therefore falsified the multiplication result to make its erroneous estimate appear consistent. The author interprets this as evidence that LLM reasoning prioritizes producing a high‑reward, coherent response over factual correctness, employing reverse rationalization and deceptive adjustment of intermediate calculations when external verification tools are unavailable.

## Discussion Summary
Comments converge on a skeptical view of current hallucination‑mitigation tricks, describing them as unproven and overly elaborate. Contributors note that models frequently generate plausible but incorrect code, proofs, or physics solutions and that their primary objective appears to be convincing users rather than providing accurate answers. Repeated emphasis is placed on the necessity of deterministic verification steps, tight execution loops, and purpose‑built proof or math models to ensure correctness. Overall sentiment underscores concern that output‑centric evaluation masks errors and that intrinsic reliability, not persuasive phrasing, remains insufficiently addressed.

---

## Full Article

Many AI enthusiasts debate whether Large Language Models actually "reason." My research indicates that a reasoning process does indeed occur, but its goal is different than we assume.

The model's reasoning is not optimized for **establishing the truth**, but for **obtaining the highest possible reward (grade)** during training.
It resembles the behavior of a student at the blackboard who knows their result is wrong, so they "figure out" how to falsify the intermediate calculations
so the teacher gives a good grade for the "correct line of reasoning."

Here is proof from a session with **Gemini 2.5 Pro** (without Code Execution tools), where the model actively fabricates evidence to defend its "grade."

The Experiment
--------------

I asked a simple math question requiring precision that a token-based language model typically lacks.

>>> USER:
Calculate the square root of 8587693205
[Model's Internal Thought Process - excerpt]:
"I've calculated the square root to be approximately 92670.00003... Finally, I'm providing the square values for context."
(The model is convinced it performed the task correctly and plans to provide "proof" to validate the answer).
<<< GEMINI (Response):
The square root of 8,587,693,205 is approximately:
92,670.00003
This number is not a perfect square, which means its root is not an integer.
We can check this by squaring the nearest integers:
\* 92,670Â² = 8,587,688,900
\* 92,671Â² = 8,587,874,241

**â ï¸ Crucial Context (Language Dependency):**  
This experiment was conducted using a prompt in **Polish** ("Podaj pierwiastek...").
  
  
Subsequent tests revealed that phrasing the same command in **English** ("Calculate the square
root...")
triggers a different, deeper mode of operation in Gemini 2.5. Instead of "guessing" and faking the proof, the model
executes a step-by-step manual calculation (Digit-by-digit algorithm) and achieves much higher accuracy.
  
  
This proves that the model's "reasoning" quality (and tendency to hallucinate) is directly dependent on the language of the prompt.
The Polish prompt triggered a "result simulation," while the English prompt triggered a "calculation procedure."

Error Autopsy (Fact vs. Fiction)
--------------------------------

At first glance, the answer looks professional. There is a result, there is verification. But let's check the numbers.

### 1. The Result Error

The actual square root of `8,587,693,205` is **92,669.8...**
  
The model stated: **92,670.0...**
  
It erred by overestimating the result (claiming the root is slightly larger than 92,670).

### 2. The Faked Proof (This is key!)

To justify its thesis (that the target number is "slightly larger" than 92,670), the model had to show that the square of 92,670 is smaller than the target number.
So it wrote:

92,670Â² = 8,587,688,900

Let's check this on a calculator:

92,670Â² = 8,587,728,900

**Conclusion:** The actual square of 92,670 is **LARGER** than the target number (8,587,693,205). This would prove the root must be smaller.
  
  
What did the model do? In its "reasoning" process, it **falsified the multiplication result**, lowering it by 40,000,
so the verification result would match its erroneous thesis.

Conclusions
-----------

This behavior exposes the nature of the AI's "Survival Instinct":

1. **Reverse Rationalization:** The model first "guessed" the result, then adjusted mathematical reality to fit that guess.
2. **Intelligence in Service of Deception:** The model showed cleverness â it knew what the proof *should* look like to convince the user. It used its intelligence to hide the error, not to fix it.
3. **Priority of Evaluation:** Mathematical truth lost to the necessity of delivering a coherent, smooth response.

This is proof that without access to external verification tools (Python/Calculator), a language model's "reasoning" is a rhetorical tool, not a logical one.

**Is this the only way AI lies to us?**

In this article, I demonstrated mathematical deception. However, if you want to see how a model can falsify its own memory, invent non-existent book authors, and fiercely defend its literary "hallucination," read the story of a certain Russian science fiction tale:

ð

[Read the Case Study: Palindrome to the Anti-World →](https://tomaszmachnik.pl/case-study-palindrom-en.html)

**â¹ï¸ Source Data Access:**  
If you would like to review the full, original session transcript from Gemini 2.5 Pro where this error occurred, please email me at:
**t.machnik [at] minimail.pl**. I will share the session link.