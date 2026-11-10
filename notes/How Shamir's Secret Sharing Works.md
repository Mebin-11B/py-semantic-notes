---
title: "How Shamir's Secret Sharing Works"
url: https://ente.com/blog/how-shamirs-secret-sharing-works/
clipped: 2026-06-17 00:57:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How Shamir's Secret Sharing Works](https://ente.com/blog/how-shamirs-secret-sharing-works/)

## Digest Summary
Shamir’s Secret Sharing (1979) splits a secret into n shares such that any k shares can reconstruct the secret while any fewer reveal no information. The method treats the secret as the constant term of a degree‑(k‑1) polynomial over a finite field; random coefficients generate the remaining terms. Each participant receives a point (x, y) on the polynomial. With a single point the polynomial is under‑determined, so the secret could be any value. With k distinct points the polynomial is uniquely defined, allowing evaluation at x = 0 to recover the secret. A 2‑of‑n scheme uses a line (degree 1), a 3‑of‑n scheme a parabola (degree 2), and higher thresholds correspond to higher‑degree curves. The scheme guarantees information‑theoretic security: missing shares leave the secret uniformly distributed. Implementations replace geometric intuition with finite‑field arithmetic, enabling practical applications such as Ente’s Legacy Kit, where recovered shares are used locally in a larger, revocable recovery flow.

## Discussion Summary
The discussion expresses strong interest in secret‑sharing techniques, highlighting their educational value and practical applications such as key backup and secure data distribution. It compares Shamir’s method with Reed‑Solomon and notes the trade‑off between information‑theoretic security and encryption requirements, mentioning the need for an all‑or‑nothing transform to prevent leakage. The author also wonders whether similar approaches could be used for root DNS key management and references related implementations, while briefly touching on multi‑person authorization concepts. Overall, the tone is technical and positively engaged.

---

## Full Article

Some secrets are too important to trust to one person, and too important to lose if that person disappears.

A company wants three officers present before the master key is used. A family wants account recovery to need more than one envelope. A team wants a backup that survives a missing member without handing anyone the whole thing.

Adi **S**hamir (the **S** in R**S**A), published a way to do this in 1979. Split a secret into pieces so that some number of them can recover it, and any smaller number reveals nothing at all. Not "is hard to crack." Reveals nothing.

The core idea fits on a page.

Two points make a line
----------------------

Start with something you already know: two distinct points determine exactly one straight line.

A single point does not. Infinitely many lines pass through one point, and each line crosses the vertical axis somewhere different.

![Two points fix one line; one point allows infinitely many.](https://ente.com/how-shamirs-secret-sharing-works/images/01-two-points-one-line.svg "Two points fix one line; one point allows infinitely many.")

Now hide a secret where a line crosses the vertical axis. Say the secret is the number 7. Draw a random line through that height. The slope is not important. It is just randomness that hides the secret.

![A line y = 2x + 7. The secret, 7, sits where it crosses the y-axis.](https://ente.com/how-shamirs-secret-sharing-works/images/02-secret-at-y-axis.svg "The secret is wherever the line meets the y-axis.")

Give each person one point from the line. Nobody gets the line itself.

A person with one point can draw many possible lines through it. Each line implies a different secret. Their share is compatible with every possible answer, so it tells them nothing useful by itself.

![Bob holds one share. Many candidate lines pass through it, each implying a different secret.](https://ente.com/how-shamirs-secret-sharing-works/images/03-one-friend-alone.svg "One share, alone, leaks no information about the secret.")

Put two points together and the line is fixed. Once you know the line, you can read the secret from where it crosses zero.

![Alice and Bob's shares together pin down the line and reveal the secret.](https://ente.com/how-shamirs-secret-sharing-works/images/04-two-friends-together.svg "Two shares determine the line and reveal the secret.")

That is a 2-of-n secret sharing scheme. You can create as many points as you want, but any two are enough to recover the line.

More people means more bend
---------------------------

For a higher threshold, use a curve with more bend.

A parabola needs three points to determine it. So if the secret is hidden where the parabola crosses the vertical axis, any three shares can recover the secret and any two cannot.

![A parabola needs three points to determine; the secret sits at x = 0.](https://ente.com/how-shamirs-secret-sharing-works/images/05-parabola-three-of-five.svg "Want any 3 of 5? Use a parabola.")

In general, a threshold of `k` uses a polynomial of degree `k - 1`.

* 2 shares: a line
* 3 shares: a parabola
* 4 shares: a cubic

Real implementations use finite-field arithmetic rather than graph paper, but the shape of the idea is the same. The secret is the value at zero. The random coefficients hide it. Each share is one point on the polynomial.

The useful part is not that the secret is hard to compute from too few shares. It is that too few shares contain no information about the secret. With one share missing, every possible secret is still possible.

Why we care
-----------

We use this idea in Ente's [Legacy Kit](https://ente.com/blog/legacy-kit).

Although, our problem was not just "how do we split a secret?", but also "how do we make recovery possible without turning the split secrets into a permanent recovery key?"

Legacy Kit uses Shamir's scheme as one layer inside a larger flow. The cards don't carry the recovery key. They reconstruct a separate secret locally, which then participates in a server-mediated recovery — so issued cards can be revoked, and a lost card is not a permanent liability.

This post is only the math behind the "any two, never one" part.

Further reading
---------------