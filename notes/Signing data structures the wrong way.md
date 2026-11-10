---
title: "Signing data structures the wrong way"
url: https://blog.foks.pub/posts/domain-separation-in-idl/
clipped: 2026-06-17 01:24:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Signing data structures the wrong way](https://blog.foks.pub/posts/domain-separation-in-idl/)

## Digest Summary
The post explains that cryptographic operations (signing, encryption, MAC, hashing) require data encodings that are both canonical and domain‑separated to prevent type‑confusion attacks, where distinct message types serialize to identical byte streams (e.g., TreeRoot vs. KeyRevoke). Existing ad‑hoc mitigations (context strings, method‑name hashes) are error‑prone. Snowpack, the serialization format used by FOKS, embeds a random, immutable 64‑bit domain separator directly in the IDL definition of each struct. Compilers generate a `GetUniqueTypeID()` method; signing and verification concatenate this identifier with the serialized object, while the identifier itself is omitted from the transmitted bytes. The type system enforces that only objects with a domain separator can be processed, eliminating mismatched‑type signatures. Snowpack also provides canonical encodings via positional JSON‑like arrays and Msgpack, enforcing minimal integer sizes and avoiding dictionary key ordering issues. It supports forward/backward compatibility through nullable fields and variant handling, and tooling ensures uniqueness of separators within a project. The approach is open‑sourced for Go and TypeScript, with plans for additional languages.

## Discussion Summary
The discussion emphasizes the importance of explicit domain separation and context inclusion in signatures, favoring straightforward, readable implementations over complex binary formats and heavyweight libraries. Participants argue that JSON‑based approaches and in‑band type fields can simplify canonicalisation, while binary‑oriented designs are seen as unnecessary and potentially obscure. Concerns are raised about supply‑chain risks from precompiled cryptographic binaries, advocating minimal, auditable code. Established cryptographic principles such as the Horton principle are reinforced, and suggestions for protobuf extensions and DSSE are noted as practical, non‑novel solutions.

---

## Full Article

How do you package data before feeding it into a cryptographic algorithm, like
Sign, Encrypt, MAC or Hash? This question has lingered for decades
without a sufficient solution.
There are at least two important problems to solve. First,
the encoding ought to produce *canonical* outputs,
as systems like [Bitcoin have struggled](https://en.wikipedia.org/wiki/Transaction_malleability_problem) when
two different encodings decode to the same in-memory data. But more important,
the encoding system ought to weigh in on the important problem of *domain
separation*.

To get a sense for this issue, let’s look at a simple example, using
a well-known IDL like protobufs. Imagine a distributed system that has two
types of messages (among others): `TreeRoot`s that encapsulate the root
of a transparency tree, and `KeyRevoke`s that signify a key being revoked:

```
message TreeRoot {
  int64 timestamp = 1;
  bytes hash = 2;
}
message KeyRevoke {
  int64 timestamp = 1;
  publicKeyFingerprint hash = 2;
}
```

By a stroke of bad luck, these two data structures line up field-for-field,
even though as far as the program and programmer are concerned, they mean
totally different things. If a node in this system signs a `TreeRoot` and
injects the signature into the network, an attacker might try to forge a
`KeyRevoke` message that serializes byte-for-byte into the same message as the
signed tree root, then staple the `TreeRoot` signature onto the `KeyRevoke` data
structure. Now it looks like the signer signed a `KeyRevoke` when it
never did, it only signed a `TreeRoot`. A verifier might be fooled into
“verifying” a statement that the signer never intended.

This is not a theoretical attack. It has a long historical record
of success, in the contexts of [Bitcoin](https://bitcointalk.org/?topic=102395),
[DEXs in Ethereum](https://hacken.io/insights/order-book-security-vulnerabilities/),
[TLS](https://doi.org/10.1109/comst.2025.3526605),
[JWTs](https://pentesterlab.com/blog/jwt-vulnerabilities-attacks-guide),
and [AWS](https://github.com/SummitRoute/csp_security_mistakes/blob/main/README.md),
among others.

And though our small example concerns signing, the same idea is in play
for MAC’ing (via HMAC or SHA-3), hashing, or even encryption, as most encryption
these days is authenticated. In general, the cryptography should
guarantee that the sender and receiver agree not only on the contents
of the payload, but also the “type” of the data.

The systems that have taken stabs at domain separation
use ad-hoc techniques, such as hashing the local name of
[surrounding program methods in Solana](https://www.anchor-lang.com/docs/basics/idl#discriminators),
[best practices in Ethereum](https://eips.ethereum.org/EIPS/eip-712) or
[“context strings” in TLS v1.3](https://datatracker.ietf.org/doc/html/rfc8446).
Given the rich variety of serious bugs possible here,
a more systematic approach is warranted. When building
[FOKS](https://blog.foks.pub/posts/introducing/), we invented one.

The Idea: Domain Separators in the IDL
--------------------------------------

The main idea behind FOKS’s plan for serializing cryptographic
data (called [Snowpack](https://github.com/foks-proj/go-snowpack-compiler))
is to put random, immutable domain separators directly into the IDL:

```
struct TreeRoot @0x92880d38b74de9fb {
   timestamp @0 : Uint;
   hash @1 : Blob;
}
```

A simple compiler transpiles the IDL to a target language. In the target
language, a runtime library provides a method to sign such an object: it makes a concatenation of the domain separator
(`@0x92880d38b74de9fb`) and the serialization of the object, and then feeds the
byte stream into the signing primitive. Similarly, verification of an object
verifies this same reconstructed concatenation against the supplied signature.
Note that the domain separator does not appear in the eventual serialization
(which would waste bytes), since both signer and receiver agree on it via this
shared protocol specification. Encrypt, HMAC, and hash work the same way.

In Go (as well as TypeScript and other languages), the type system
enforces the security guarantees. The compiler outputs a method:

```
func (t TreeRoot) GetUniqueTypeID() uint64 { return 0x92880d38b74de9fb }
```

And the `Sign` and `Verify` methods look like:

```
func Sign(key Key, obj VerifiableObjecter) ([]byte, error) 
func Verify(key Key, sig []byte, obj VerifiableObjecter) error
```

`VerifiableObjecter` is an interface that requires the `GetUniqueTypeID()` method,
in addition to other methods like `EncodeToBytes`.

These 64-bit domain separators are not required for all structs, and many
don’t need them. However, these untagged structs do not get `GetUniqueTypeID()` methods, and therefore cannot be
fed into `Sign` or `Verify` without type errors. Same
goes for encryption, MAC’ing, prefixed hashing, etc.

As long as the random domain separators are unique (which they will be,
globally, with high probability), there is no chance of the signer and verifier
misaligning on what data types they are dealing with. Any substitution like the
one we discussed earlier will fail verification. Developers should use simple
tooling, either in the IDE or CLI, to generate these random domain separators
and insert them into their protocol specifications.

The logic behind random generation of domain separators is reminiscent of
generating *p(x)* randomly in [Rabin
Fingerprinting](https://en.wikipedia.org/wiki/Rabin_fingerprint). In the base
case, if Bob sits down to write a new project today, and generates all domain
separators randomly, with very good probability, he knows the *verifiers* in his
project will never verify signatures generated by another existing project. Random
generation saves him the effort of thinking about mistaken collisions. As
an inductive step, imagine Mallory builds a new project after Bob publishes his
protocol specification. She might deliberately reuse his domain separators. If Bob
gives her project access to his private keys, she might confuse verifiers in his
project into verifying signatures generated by hers. We claim there is nothing
to be done here. Mallory’s attack against domain separators is possible in any
system, and since her project is malicious, it was a mistake to trust it with his
private keys in the first place. If on the other hand, Mallory generates domain
separators randomly, she and Bob get the same desirable guarantees as in the base case.

Another risk is that AI coding or auto-completion agents might copy-paste
existing domain separators, or generate them sequentially. The snowpack compiler
and runtime ensure that all domain separators are unique within the same
project, and error or panic (respectively) otherwise.

Though developers are free to change the struct name `TreeRoot` however they please, they
should keep the domain separator fixed over the lifetime of the protocol,
even if they add or remove fields. As in protobufs
and Cap’n Proto, the system supports removal and addition of fields, so long
as the positions of remaining fields (as given by `@0` and `@1` above) never change,
and as long as retired fields are never repurposed.

The Snowpack IDL: Domain Separation + Canonical Encodings + More!
-----------------------------------------------------------------

Built-in domain separation is the novel idea in Snowpack. But overall, it’s proven
to be a simple and effective forwards- and backwards-compatible system for both RPCs and serialization of inputs to
cryptographic functions. We insist that the same system should serve both
purposes well.
Protobufs, for example, make no guarantees regarding [canonical
encodings](https://protobuf.dev/programming-guides/serialization-not-canonical/).
JSON encodings, though often used in cryptographic settings, are deficient
in that they lack binary buffers (as output by most cryptographic
primitives!), and therefore invite confusion between strings and base64-encoded
binary data.

Snowpack, however, checks all the boxes for us. The simple idea is to encode
structures of the form `TreeRoot` above as JSON-like positional arrays:

```
[ 1234567890, \xdeadbeef ]
```

The `@1` in the protocol specification above instructs encoders and decoders
to look for the `hash : Blob` field in the 1st position
of the array. Skipped and retired fields
get encoded as `nil`s. If the `TreeRoot`
message upgrades to something that looks more like:

```
struct TreeRoot @0x92880d38b74de9fb {
   hash @1 : Blob;
   timestampMsec @2 : Uint;
}
```

the intermediate encoding becomes:

```
[ nil, \xdeadbeef, 1234567890123 ]
```

Old decoders can still decode the new encoding, but see 0-values for the
`timestamp` they were expecting. New decoders can decode old encodings, but
see 0-values for the `timestampMsec` field they were expecting. It’s of
course up to the application developer to decide if these conditions will break
the program or not and consequently whether or not this protocol evolution makes sense,
but they can rest assured that decoding will not fail at the protocol level.

From this intermediate encoding, Snowpack arrives at a flat byte-stream via
[Msgpack](https://msgpack.org) encoding, but with important limitations. First,
all integer encodings must use the minimum-size encoding possible. And second,
dictionaries with more than one key-value pair are never sent into the encoder,
so we can sidestep the whole thorny issue of canonical key ordering. As a
result, we wind up with canonical encodings every time.

Thus the overall flow is:

Go Structs
Snowpack


Intermediate
JSON-like Objects
self-describing


bytes

self-describing

Intermediate
JSON-like Objects
Snowpack


Go Structs

Unlike the outer conversions, the inner conversions (to and from bytes) are
self-describing and do not need a Snowpack protocol definition to complete.
This design choice enables forwards compatibility: old decoders can decode
messages from the future. It also allows for convenient debugging and inspection
of the byte stream.

We have seen how structs encode and decode. In addition, Snowpack offers just enough
complexity to cover every situation we have seen in [FOKS](https://foks.pub).
Other important features are: `List`s, `Options` and `variant`s. The first two
find straightforward expression as array-based encodings. Variants, or tagged
unions, encode as single key-value-pair dictionaries, allowing existing
Msgpack libraries to decode them with type safety.

Summary
-------

Domain separation bugs have bitten real systems repeatedly. Existing
mitigations are ad-hoc: context strings, method-name hashes, and hand-rolled
prefixes that are easy to forget and hard to audit.

Snowpack takes a different approach: random, immutable 64-bit domain
separators live in the IDL itself, and the type system ensures you cannot
sign, encrypt, or MAC an object that lacks one.
We think this core idea is bigger than any one system, and we’d love to see
other serialization schemes adopt it. In the meantime,
get it in Snowpack, [open-sourced on GitHub](https://github.com/foks-proj/go-snowpack-compiler),
currently targeting Go and TypeScript with more languages to come.

✌️️ [Max](https://maxk.org) 🔑

PS: Comments and discussion are welcome, please post to this discussion
on [Hacker News](https://news.ycombinator.com/item?id=47605677)

### Credits

Thanks to [Jack O’Connor](https://jacko.io/) for his feedback
on a draft of this post, and for building related systems that influenced Snowpack.