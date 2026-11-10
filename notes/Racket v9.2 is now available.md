---
title: "Racket v9.2 is now available"
url: https://blog.racket-lang.org/2026/05/racket-v9-2.html
clipped: 2026-06-17 00:55:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - programming languages
  - racket scheme
  - pattern matching
  - type systems
  - unicode standard
related:
  - "[[Programming Languages]]"
  - "[[Pattern Matching]]"
  - "[[Type Systems]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Racket version 9.2 introduces breaking pattern matching improvements, Unicode 17.0 support, and enhanced Typed Racket definitions.
>
> **Key points:**
> - The `match` form now strictly validates equality for non-linear patterns, potentially breaking backward compatibility.
> - Core library rewrites base functions directly on `racket/kernel` and introduce `#%foreign-inline` for low-level linklets.
> - Unicode handling is updated to Unicode 17.0, and Typed Racket provides better struct formatting and complex number results for trigonometric functions.
>
> **Concept links:** [[Programming Languages]], [[Racket Scheme]], [[Pattern Matching]], [[Type Systems]], [[Unicode Standard]]
>
> **Suggested connections:**
> - [[Programming Languages]] — functional programming paradigms and Scheme-derived languages.
> - [[Pattern Matching]] — structural search and decomposition mechanisms in compilers.
> - [[Type Systems]] — static and typed extensions in dynamic languages.
<!-- ai-summary:end -->

# [Racket v9.2 is now available](https://blog.racket-lang.org/2026/05/racket-v9-2.html)

## Digest Summary
Racket v9.2 is now available (https://download.racket-lang.org). Key updates include: the match form now validates equality for non‑linear patterns and rejects mismatched uses, which may break existing code; Typed Racket’s asin and acos type signatures correctly handle complex results, potentially causing compile‑time failures. The new #%foreign-inline core form exposes linklet‑level facilities, requiring updates to code that enumerates core forms. Unicode 17.0 is adopted for all character and string operations, and internal support for a more static “ffi2” foreign interface is added. The terminal-file-position function now counts bytes written to terminal ports (stdin, stderr). Cross‑phase persistent modules broaden quoted‑data support. Implementations of member, memw, when, unless, let/ec, and cond are rewritten to rely solely on racket/kernel. A new impersonator-property-predicate-procedure? identifies procedures created via make-impersonator-property. Typed Racket prints polymorphic struct types with explicit type arguments (e.g., (Array Byte)). The stepper’s numeric display aligns with language settings, Scribble documents default to an initial‑scale of 1.0, margin notes appear inline on narrow displays, and big‑bang .dmg bundles correctly honor the close‑on‑stop feature. Numerous other bug fixes and documentation improvements are included. Contributors are listed, and community discussion is encouraged on Discourse or Discord.

## Discussion Summary
The discussion highlights the release of Racket 9.2, noting its upgrade process and package migration steps, while emphasizing the language’s strength for rapid prototyping and deep‑learning model experimentation due to its highly flexible, language‑oriented design. Users appreciate its ability to redefine stack components and find the “little learner” useful for exploring new primitives such as sparse tensors. However, despite strong personal preference for Racket, there is a common acknowledgment that Python remains the primary tool because of its broader ecosystem and library support.

---

## Full Article

*posted by Stephen De Gabrielle and John Clements*

---

We are pleased to announce Racket v9.2 is now available from [https://download.racket-lang.org/](https://download.racket-lang.org).

As of this release:
-------------------

* The [`match`](https://docs.racket-lang.org/reference/match.html#%28form._%28%28lib._racket%2Fmatch..rkt%29._match%29%29) form checks that when non-linear patterns (patterns where the same variable is used multiple times) are used with `...`, the two parts of the matched value actually are equal. Additionally, match rejects non-linear patterns where one use of the variable is used with `...` and another is not. [This repair could cause existing code to fail](https://github.com/racket/racket/pull/5467).
* Typed Racket’s types for the `asin` and `acos` procedures correctly handle situations where the function produces a complex number, avoiding unsound results that were previously possible. [This repair could cause existing code to fail at compile time](https://github.com/racket/typed-racket/pull/1428).
* The [`#%foreign-inline`](https://docs.racket-lang.org/reference/foreign-inline.html#%28form._%28%28quote._~23~25kernel%29._~23~25foreign-inline%29%29) core syntactic form provides unsafe access to facilities provided at the linklet layer by a Racket implementation. This means that any code that handles all core forms by enumeration will need to be updated.
* Unicode 17.0 is used for character and string operations.
* This release includes internal support for a more static “ffi2” foreign interface (to be used in a future package).
* The [`terminal-file-position`](https://docs.racket-lang.org/reference/port-buffers.html#%28def._%28%28quote._~23~25kernel%29._terminal-file-position%29%29) function counts bytes written to ports connected to a terminal, such as `stdin` and `stderr`.
* Cross-phase persistent modules allow more types of `quote`d data.
* The implementations of `member`, `memw`, `when`, `unless`, `let/ec`, and `cond` are rewritten to use only [`racket/kernel`](https://docs.racket-lang.org/reference/Kernel_Forms_and_Functions.html) syntax
* The [`impersonator-property-predicate-procedure?`](https://docs.racket-lang.org/reference/chaperones.html#%28def._%28%28quote._~23~25kernel%29._impersonator-property-predicate-procedure~3f%29%29) function identifies procedures created by `make-impersonator-property`.
* In Typed Racket, polymorphic struct types are printed using type arguments (e.g., `(Array Byte)`) rather than exposing an internal representation.
* The stepper’s display of numbers better matches the language settings.
* Scribble documents that do not use the Racket-manual style get an [`initial-scale`](https://docs.racket-lang.org/scribble/core.html#%28def._%28%28lib._scribble%2Fhtml-properties..rkt%29._initial-scale%29%29) of 1.0, instead of the manual style’s 0.8, but this can be configured using the `initial-scale` property.
* By default, margin notes appear inline for narrow displays in all styles, not just in the Racket-manual style.
* Big-bang programs distributed as .dmg files correctly handle the `close-on-stop` feature.
* There are many other repairs and documentation improvements!

Thank you
---------

The following people contributed to this release:

Alexander Shopov, Alexis King, Asilo, Bert De Ketelaere, Bob Burger, Bogdan Popa, Chung-chieh Shan, François-René Rideau, Gustavo Massaccesi, Ilya Klyuchnikov, Jade Sailor, Jamie Taylor, John Clements, Jonathan Simpson, LS\_Hower, Matthew Flatt, Matthias Felleisen, Mike Sperber, Pavel Panchekha, Philippe Meunier, RMOlive, Robby Findler, Roman Klochkov, Sam Tobin-Hochstadt, Shu-Hung You, Stephen de Gabrielle, Tejas Sanap, Vincent Lee, and Wing Hei Chan.

**Racket** is a community developed open source project and we welcome new contributors. See [racket/README.md](https://github.com/racket/racket/blob/master/README.md#contributing) to learn how you can be a part of this amazing project.

Feedback Welcome
----------------

Questions and discussion welcome at the Racket community on [Discourse](https://racket.discourse.group/invites/VxkBcXY7yL) or [Discord](https://discord.gg/6Zq8sH5).

Please share
------------

If you can - please help get the word out to users and platform specific repo packagers

```
Racket - the Language-Oriented Programming Language - version 9.2 is now available from https://download.racket-lang.org

See https://blog.racket-lang.org/2026/05/racket-v9-2.html for the release announcement and highlights.
```