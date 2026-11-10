---
title: "Unknowable Math Can Help Hide Secrets"
url: https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/
clipped: 2026-06-17 01:01:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Unknowable Math Can Help Hide Secrets](https://www.quantamagazine.org/how-unknowable-math-can-help-hide-secrets-20260511/)

## Digest Summary
The article explains how recent work by researcher Ilango circumvents the 1994 impossibility theorem of Goldreich and Oren, which proved that non‑interactive zero‑knowledge (ZK) proofs cannot have simulators under the original Goldwasser‑Micali‑Rackoff definition. Ilango introduces “effective” zero knowledge, a notion that relaxes the simulator requirement: a proof need not have a simulator as long as it is infeasible to demonstrate that it lacks one. By embedding an unprovable‑in‑practice assumption—namely, that no efficient proof can refute the consistency of standard mathematics—into the statement being proved, the resulting non‑interactive proof becomes effectively ZK. The approach leverages proof‑complexity hardness (extremely long proofs for certain statements) rather than computational hardness of specific problems. This loophole creates a scenario where a verifier cannot be certain whether a simulator exists, granting the practical benefits of ZK without interaction. The result suggests that proof‑complexity techniques may enable other cryptographic constructions previously considered impossible.

## Discussion Summary
The comments express skepticism toward the presented concept, questioning its similarity to one‑way hashing, its unpredictability, and whether it amounts to security through obscurity. They request clarification on the claimed “new powerful tool” in cryptography and note confusion about the distinction between interactive and non‑interactive zero‑knowledge proofs, suggesting that the article appears disconnected from practical applications. Overall, the tone is inquisitive yet critical, seeking concrete explanation and relevance.

---

## Full Article

The interactive character of zero-knowledge proofs makes them strikingly different from ordinary mathematical proofs, which can be written down in a textbook without any input from a verifier. Intuitively, interactivity seems like an essential element of a zero-knowledge proof. A prover who simply hands over a written document can’t stop the verifier from examining the whole thing and learning everything the prover knows. The prover could encrypt that document to prevent the verifier from learning too much, but in that case the verifier won’t be able to confirm that the proof is valid, since they can’t interrogate the prover.

In 1994, the cryptographers [Oded Goldreich](https://www.wisdom.weizmann.ac.il/~oded/) and Yair Oren proved a theorem that [confirmed this intuition](https://link.springer.com/article/10.1007/BF00195207). Their result established that it’s impossible to construct a completely noninteractive proof that meets Goldwasser, Micali, and Rackoff’s definition of zero knowledge. It was bad news for cryptographers who’d held out hope for zero-knowledge proofs that were otherwise identical to ordinary ones.

“People just said, ‘Forget it, it’s not going to happen,’” said [Abhishek Jain](https://www.cs.jhu.edu/~abhishek/), a cryptographer at Johns Hopkins University and NTT Research. “How can you overcome an impossibility?”

Ilango’s new result shows how — by harnessing a different kind of impossibility.

**Mission Impossible**
----------------------

In the summer of 2023, at the end of his third year of graduate school at the Massachusetts Institute of Technology, Ilango was growing increasingly interested in an arcane subfield of complexity theory called proof complexity. Most complexity theorists study how hard problems like three-coloring are (in this case, how many steps are needed to find a valid coloring). In proof complexity, by contrast, researchers analyze [the difficulty of proving statements about these problems](https://www.quantamagazine.org/reverse-mathematics-illuminates-why-hard-problems-are-hard-20251202/) — statements like “There’s no way to properly color this specific map.” They gauge this difficulty by measuring the length of the simplest possible proof of a given statement.

In math, some statements cannot be proved either true or false. (This is Gödel’s other incompleteness theorem.) Other statements, however, might be provable in principle, but only with proofs that are too long to ever write down. For all practical purposes, these intrinsically hard-to-prove statements are just as unknowable as the unprovable statements that Gödel identified.

Kurt Gödel showed that certain mathematical statements are true but unprovable.

Alfred Eisenstaedt/Public Domain

Researchers usually study such hard-to-prove statements for their own sake, to better understand the limits of mathematical proof. But Ilango suspected that these statements might also have applications in cryptography. Nearly all techniques in modern cryptography are based on the difficulty of solving specific problems, like ones about coloring maps. What if, Ilango wondered, he could exploit the difficulty of proving specific statements instead? Doing so might allow him to concoct new cryptographic techniques.

“We find ourselves constantly slamming into these walls of ‘Why can’t we prove this? Why can’t we prove that?’” said [Marco Carmosino](https://marco.ntime.org/), a complexity theorist at IBM. “Can we benefit from that kind of hardness?”

In 2024, after a few false starts, Ilango identified a specific task in cryptography that could serve as a test bed for his approach. He wanted to build zero-knowledge proofs that weren’t interactive. Thirty years earlier, Goldreich and Oren had established that such proofs are impossible. But Ilango realized that there might be more than one way to define “zero knowledge” — and that the impossibility result only applied to the original definition.

It is pretty mind-bending. The first time you see it, you’re like, ‘Wait, what?’

Amit Sahai, University of California, Los Angeles

To understand that definition, put yourself in the position of the verifier in the map-coloring example. Even before you interact with the prover, you can predict, or simulate, exactly what a valid proof will look like: Each round, the prover will always reveal two differently colored regions, no matter which border you choose. In cryptographers’ lingo, this proof has a “simulator,” and that’s what it means for the proof to be zero knowledge.

“If you and I were going to have a conversation, but I could predict in advance everything that you were going to say, then you’d probably agree that I’m not going to learn anything by talking to you,” Ilango said.

What Goldreich and Oren’s impossibility result actually said was that noninteractive proofs can’t have simulators, and therefore, by definition, they can’t be zero knowledge. Ilango hoped to use proof complexity to define a new notion of zero knowledge — what he called “effective” zero knowledge — that would not be subject to the old impossibility result but would still be just as useful as ordinary zero knowledge.

At the heart of his new definition was a simple insight: It’s OK if a proof doesn’t have a simulator, as long as nobody can tell.

**Burden of Proof**
-------------------

Imagine you’re about to buy a lock that’s famously unbreakable. You read the fine print on the package, expecting to find a guarantee that the lock is secure. Instead you find a frank admission that the lock is not secure, followed by a promise: Even though it’s not secure, no one can prove that it’s not secure.

At first, this may sound like a willfully perverse way to market a useless product. But if the lock lives up to that unusual promise, it’s actually exactly as safe as one that’s provably unbreakable. To see why, imagine that you found a way to break the lock. Then the broken lock itself would count as a proof that it wasn’t secure — but if the promise on the packaging is correct, such a proof is impossible. In other words, if a vulnerability exists, but it’s impossible to prove that it exists, then there’s no way to take advantage of it.

As a graduate student, Rahul Ilango invented a new type of zero-knowledge proof by exploiting the limits of mathematics.

This is the basic idea behind Ilango’s new result. Traditionally, to demonstrate that a proof is zero knowledge, you would want to show that it has a simulator. (In our metaphor, this would be equivalent to proving that the lock is unbreakable.) But that would also mean that the proof has to be interactive. To get effective zero knowledge, Ilango instead wanted to show that it’s extremely difficult to guarantee that his proof *doesn’t* have a simulator. (That is, there’s no way to prove that the lock is breakable.)

If he could show this, he would get all the benefits of zero knowledge while cleverly getting around the requirement of interactivity. “It is actually really hard to think of any real-life situation where this effective zero knowledge wouldn’t be good enough,” Sahai said.

To understand how Ilango pulled this off, let’s return to the three-coloring example. If you know how to color the map, you can write down a noninteractive proof of the statement “This map can be three-colored.” But because of the 1994 impossibility result, that proof can’t have a simulator, and so it can’t be zero knowledge.

Using Ilango’s new approach, you’d instead start by rewriting the statement you want to prove, now adding an extra assumption: “This map can be three-colored — assuming that there’s no efficient way to find a contradiction in the standard axioms of mathematics.” This additional assumption is usually taken for granted. If it’s false, then math is rife with contradictions, and no proof is trustworthy. If it’s true, as researchers universally believe, then Ilango’s new statement is essentially equivalent to the original one.

But the assumption is also thought to be [effectively impossible to prove](https://www.cambridge.org/core/product/identifier/S0022481200041748/type/journal_article): It’s likely provable in principle, but any proof would be way too long to ever write down. That makes it the sort of Gödel-type assertion that researchers in proof complexity love to study.

It also means that a reader of the proof can’t entirely rule out the possibility that the assumption is false — which has important implications. In particular, it means that there are two possible worlds in which we might live. In the first, the assumption is indeed true, and we’re right back where we started: You’ve written a noninteractive proof that your map can be three-colored, but this proof can’t have a simulator and therefore can’t be zero knowledge. But in the second world, the assumption is false, and we can no longer trust that mathematics is consistent. It’s impossible to distinguish between correct and incorrect proofs; crucially, in this bizarro realm, Goldreich and Oren’s impossibility result no longer applies. Any proof — valid or invalid, interactive or noninteractive — can have a simulator.

This unlikely second world acts as a loophole of sorts. A reader can’t know for certain which world they live in — even though it’s almost certainly the first one, where mathematics remains safe. That, in turn, means that they can’t actually be sure that the proof has no simulator. The proof can still be effectively zero knowledge, even though there’s no interactivity. Ilango had successfully evaded the decades-old impossibility result.

The mathematical sleight of hand involved can make even a seasoned researcher do a double take, but the logic checks out. “It is pretty mind-bending,” Sahai admitted. “The first time you see it, you’re like, ‘Wait, what?’”

To many computer scientists, the broader implications of Ilango’s result are as exciting as the result itself. For decades, proof complexity researchers have studied esoteric questions that seem more closely linked to mathematical logic than to any other area of computer science. The new work suggests that this famously difficult field isn’t as remote as it seems. Ilango, now a postdoctoral researcher at the Institute for Advanced Study in Princeton, New Jersey, and others are already beginning to explore how ideas from proof complexity might help them realize other cryptographic constructions long thought impossible.

“I don’t think it will be an isolated result,” Jain said. “Sometimes, you just need to show people a slight crack in the door.”