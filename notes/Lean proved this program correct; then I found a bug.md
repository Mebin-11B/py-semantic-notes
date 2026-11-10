---
title: "Lean proved this program correct; then I found a bug"
url: https://kirancodes.me/posts/log-who-watches-the-watchers.html
clipped: 2026-06-17 01:17:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Lean proved this program correct; then I found a bug](https://kirancodes.me/posts/log-who-watches-the-watchers.html)

## Digest Summary
A verified Lean implementation of zlib, called **lean‑zip**, was shown to correctly decompress data for any byte array under 1 GiB, as proven by the theorem `ZlibDecode.decompressSingle (ZlibEncode.compress data level) = .ok data`. Over 105 million fuzzing runs using AFL++, AddressSanitizer, Valgrind, and UBSan revealed no memory bugs in the verified Lean code itself, but uncovered two separate issues:  

- A heap‑buffer overflow in the Lean 4 runtime function `lean_alloc_sarray`, present in all released Lean versions and reported for fixing.  
- A denial‑of‑service vulnerability in lean‑zip’s archive parser, which was not covered by verification.  

The findings illustrate that while formal verification can eliminate implementation bugs in the target program, runtime libraries and unverified components may still contain exploitable flaws. This case underscores the need for comprehensive verification of both application code and its underlying runtime environment.

## Discussion Summary
Comments largely criticize the article’s click‑bait title and stress that the discovered bugs reside in the Lean runtime rather than the verified kernel, limiting their relevance to the proof’s guarantees. Recurrent themes emphasize that formal verification only ensures correctness within a specified envelope, and that flawed or incomplete specifications can render proofs misleading, especially when unverified components like parsers or memory allocators are involved. While some express optimism about AI‑assisted verification, most caution that proofs cannot guarantee absolute bug‑free software and that spec quality remains a fundamental challenge.

---

## Full Article

***I fuzzed a verified implementation of zlib and found a buffer overflow in the Lean runtime.***

AI agents are getting **very good** at finding vulnerabilities in
large-scale software systems.

Anthropic, was apparently so spooked by the vulnerability-discovery
capabilities of Mythos, they decided not to release it as it was "too
dangerous" (lol). Whether you believe the hype about these latest
models or not, it seems undeniable that the writing is on the wall:

> The cost of
> discovering security bugs is collapsing, and the vast majority of
> software running today was never built to withstand that kind of
> scrutiny. **We are facing a looming software crisis.**

In the face of this oncoming tsunami, recently there has been
increasing interest in *formal verification* as a solution. If we state
and prove properties about our code using a mechanical tool, can we
build robust, secure and stable software that can overcome this
oncoming barrage of attacks?

One recent development in the Lean ecosystem has taken steps towards
this question. 10 agents autonomously built and proved an
implementation of zlib, [lean-zip](https://github.com/kim-em/lean-zip), an impressive landmark result.
Quoting from [Leo De Moura](https://leodemoura.github.io/), the chief architect of the Lean FRO
([here](https://leodemoura.github.io/static/etaps2026/#/1)):

With apologies for the AI-slop (Leo has a penchant for it, it seems),
the key result is that `lean-zip` is not just another implementation of
zlib. It is an implementation that has been verified as correct end to
end, guaranteed by Lean to be entirely free of implementation bugs.

What does "verified as correct" actually look like? Here is one of the
main theorems ([github](https://github.com/kim-em/lean-zip/blob/78e5bd6950afdda3ab88dbd567e54bc6adedf3ae/Zip/Spec/ZlibCorrect.lean#L146-L148)):

```
theorem zlib_decompressSingle_compress (data : ByteArray) (level : UInt8)
   (hsize : data.size < 1024 * 1024 * 1024) :
    ZlibDecode.decompressSingle
      (ZlibEncode.compress data level) = .ok data
```

For *any* byte array less than 1 gigabyte, calling
`ZlibDecode.decompressSingle` on the output of `ZlibEncode.compress`
produces the original data. The decompress function is exactly the
inverse of compression. This pair of functions is *entirely* correct.

**Or is it?**

I pointed a Claude agent at `lean-zip` over a weekend, armed with AFL++,
AddressSanitizer, Valgrind, and UBSan. Over **105 million fuzzing
executions**, it found:

* **Zero memory vulnerabilities** in the verified Lean application code.
* **A heap buffer overflow** in the Lean 4 runtime (`lean_alloc_sarray`), affecting every version of Lean to date. ([bug report](https://github.com/leanprover/lean4/issues/13388), [pending fix](https://github.com/leanprover/lean4/pull/13392))
* **A denial-of-service** in `lean-zip`'s archive parser, which was never verified.