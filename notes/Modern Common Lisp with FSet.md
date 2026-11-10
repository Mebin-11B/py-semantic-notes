---
title: "Modern Common Lisp with FSet"
url: https://fset.common-lisp.dev/Modern-CL/Top_html/index.html
clipped: 2026-06-17 01:15:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Modern Common Lisp with FSet](https://fset.common-lisp.dev/Modern-CL/Top_html/index.html)

## Digest Summary
Modern Common Lisp with FSet – Version 1.0 for FSet v2.4.2, © 2026 Scott L. Burson. The document is released under the Creative Commons CC BY‑NC‑SA 4.0 license, which permits non‑commercial redistribution, remixing, adaptation, and distribution in any medium or format provided that (1) proper attribution to the author is given, (2) the work is not used for commercial purposes, and (3) any derivative material is licensed under identical terms. The author explicitly states that the text contains no LLM‑generated content and that all punctuation, including em‑dashes and semicolons, was manually written. Readers are invited to report errors or suggestions by filing issues on the Common‑Lisp.Net GitLab instance or on GitHub.

## Discussion Summary
The comments express overall support for the library and its role in the cloture project, with users showing enthusiasm for both initiatives. Requests include a single‑page HTML view and clearer, front‑loaded documentation that explains the project’s purpose. A technical correction points out that R6RS Scheme strings are mutable, challenging a misstatement in the text. The discussion acknowledges a past presentation of the material and offers constructive suggestions for improving accuracy and usability without detracting from the positive reception.

---

## Full Article

---

Modern Common Lisp with FSet [¶](https://fset.common-lisp.dev/Modern-CL/Top_html/index.html#Modern-Common-Lisp-with-FSet)
=========================================================================================================================

Version 1.0 (for FSet v2.4.2)

Â© 2026 Scott L. Burson

This document is published under the Creative Commons
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. This license
enables reusers to distribute, remix, adapt, and build upon the material in any medium or format for
noncommercial purposes only, and only so long as attribution is given to the creator. If you remix,
adapt, or build upon the material, you must license the modified material under identical terms.

This document contains no LLM-generated text — zero, zip, nada. (Yes, I do use em-dashes and
semicolons; yes, I have written every one myself.)

The FSet source code can be found at [Common-Lisp.Net’s GitLab instance](https://gitlab.common-lisp.net/fset/fset) or [GitHub](https://github.com/slburson/fset). If you
notice any errors in this book or have any other suggestions, please file issues at one of those two
sites.

---