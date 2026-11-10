---
title: "What Is OAuth?"
url: https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b
clipped: 2026-06-17 01:42:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What Is OAuth?](https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b)

## Digest Summary
OAuth was created to provide a standard, secure way for third‑party applications to act on a user’s behalf without sharing passwords. The core mechanism consists of two parts: (1) with the user’s consent, the authorization server issues a multi‑use token (the “secret”) to the delegate (client); (2) the client presents that token to resource servers to make authorized requests. This simple model replaces numerous ad‑hoc, insecure delegation schemes used by early Web 2.0 services (e.g., Flickr, AWS, Delicious). OpenID Connect (OIDC) builds on OAuth to enable “magic‑link” style sign‑in, showing how OAuth underpins modern authentication flows. Historical drivers included Twitter’s need in 2006 to support OpenID sign‑in for desktop and mobile clients without passwords, prompting the design of a reusable delegation protocol. The OAuth specifications have grown into a framework rather than a rigid standard, allowing implementations to adopt needed features while preserving security and interoperability. Understanding the underlying goal—delegated access with user consent—clarifies why the protocol appears complex.

## Discussion Summary
The comments convey overall appreciation for the article, noting that it addresses a common but poorly understood feature and provides useful clarification. Readers contribute practical advice, such as how to scroll correctly, and acknowledge the piece’s value for newer audiences unfamiliar with earlier web‑2.0 practices. Some critique the title as misleading, suggesting it implies a generic OAuth explanation rather than the specific design rationale and use‑case examples the post actually covers. Despite this, the consensus remains positive, highlighting the article’s informative nature.

---

## Full Article

What is OAuth?
==============

Wherein I [try to] answer a seemingly straightforward question: "WTF is OAuth, anyhow?"

@geoffreylitt.com

 [recently asked a question about OAuth](https://x.com/geoffreylitt/status/2022036670946979875) on dead-Twitter:

> I desperately need a Matt Levine style explanation of how OAuth works. What is the historical cascade of requirements that got us to this place?

There are plenty of explanations of the inner mechanical workings of OAuth, and lots of explanations about how various flows etc work, but Geoffrey is asking a [different question](https://x.com/geoffreylitt/status/2022288861284446225?s=20):

> What I need is to understand why it is designed this way, and to see concrete examples of use cases that motivate the design

In the 19 years (!) since I wrote the first sketch of an OAuth specification, there has been a lot of minutiae and cruft added, but the core idea remains the same. Thankfully, it's a very simple core. Geoffrey's a very smart guy, and the fact that he's asking this question made me think it's time to write down an answer to this.

It's maybe easiest to start with the Sign-In use-case, which is a much more complicated specification ([OpenID Connect](https://openid.net/developers/how-connect-works/)) than core [OAuth](https://datatracker.ietf.org/doc/html/rfc6749). OIDC uses OAuth under the hood, but helps us get to the heart of what's actually happening.

---

OIDC is functionally equivalent to "magic link" authentication.

We send a secret to a place that only the person trying to identify themselves can access, and they prove that they can access that place by showing us the secret.

That's it.

The rest is just accumulated consensus, in part bikeshedding (agreeing on vocabulary, etc), part UX, and part making sure that all the specific mechanisms are secure.

---

There's also an historical reason to start with OIDC to explain how all this works: in late 2006, I was working on Twitter, and we wanted to support OpenID (then 1.0) so that ahem Twitter wouldn't become a centralized holder of online identities. After chatting with the OpenID folks, we quickly realized that as it was constructed, we wouldn't be able to support both desktop clients and web sign-in, since our users wouldn't have passwords anymore! (mobile apps didn't exist yet, but weren't far out). So, in order to allow OpenID sign-in, we needed a way for folks using Twitter via alternative clients to sign in without a password.

There were plenty of solutions for this; Flickr had an approach, AWS had one, delicious had one, lots of sites just let random other apps sign-in to your account with your password, etc, but virtually every site in the "Web 2.0" cohort needed a way to do this. They were all insecure and all fully custom.

Rather than building TwitterAuth, I figured it was time to have a standard. Insert XKCD 927:

[Standards

Fortunately, the charging one has been solved now that we&#39;ve all standardized on mini-USB. Or is it micro-USB? Shit.

https://xkcd.com/927/](https://xkcd.com/927/)

Thankfully, against all odds, we now have one standard for delegated auth. What it does is very simple:

---

At its core, OAuth for delegation is a standard way to do the following:

* The first half exists to send, with consent, a multi-use secret to a known delegate.
* The other half of OAuth details how the delegate can use that secret to make subsequent requests on behalf of the person that gave the consent in the first place.

That's it. The rest is (sadly, mostly necessary) noise.

---

Obviously, the above elides absolute volumes of detail about how this is done securely and in a consistent interoperable way. This is the unenviable work of standards bodies. I have plenty of opinions on the pros and cons of our current standards bodies, but that's for another time.

There are very credible arguments that the-set-of-IETF-standards-that-describe-OAuth are less a standard than a framework. I'm not sure that's a bad thing, though. HTML is a framework, too – not all browsers need to implement all features, by design.

OIDC itself is an interesting thing – immediately after creating OAuth, we realized that we could compose OpenID's behaviour out of OAuth, even though it was impossible to use OpenID to do what OAuth did. For various social, political, technical, and operational reasons it took the better part of a decade to write down the bits to make that insight a thing that was true in the world. I consider it one of my biggest successes with OAuth that I was in no way involved in that work. I don't have children, but know all the remarkable and complicated feelings of having created something that takes on a life of its own.

More generally, though, authentication and authorization are complicated, situated beasts, impossible to separate from the UX and architectural concerns of the systems that incorporate them.

The important thing when implementing a standard like OAuth is to understand first what you're trying to do and why. Once that's in place, the how is usually a "simple" question of mechanics with fairly constrained requirements. I think that's what makes Geoffrey's question so powerful – it digs into the core of the reason why OAuth is often so inscrutable to so many: the complicated machinery of the standard means that the actual goals it encodes are lost.

Hopefully, this post helps clear that up!