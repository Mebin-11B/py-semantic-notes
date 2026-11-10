---
title: "Draig, a Welsh Programming Language"
url: https://raku.land/zef:l10n/L10N::CY
clipped: 2026-06-17 01:53:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Draig, a Welsh Programming Language](https://raku.land/zef:l10n/L10N::CY)

## Digest Summary
L10N::CY is the Welsh localization module for the Raku programming language. The distribution installs a `draig` executable that automatically activates the Welsh locale, and it can also be enabled in specific scripts with a `use L10N::CY` statement. Example usage shown in the synopsis:  

```
draig -e 'dywedyd "Helo Byd"'
```  

outputs “Helo Byd”. The module requires the environment variable `RAKUDO_RAKUAST=1` to be set. It contains the logic needed to provide Welsh language support throughout Raku. The documentation references “Creating a new programming language – Draig”. Author is Richard Hainsworth ([email protected]). Copyright © 2024‑2025 Raku Localization Team; the library is released under the Artistic License 2.0. Images listed are generic “Actions Status” placeholders.

## Discussion Summary
The comments express enthusiasm for the project’s educational focus and multilingual potential, noting its appeal to those interested in similar tools such as Hedy. Several contributors show interest in further development, including a desire for a Raku implementation and curiosity about specific syntax choices. One comment references a detailed “how‑to” guide from the developer, while another raises the broader pedagogical question of teaching children programming in their native language. Overall, the tone is supportive and inquisitive about future expansions.

---

## Full Article

[![Actions Status](https://github.com/Raku-L10N/CY/actions/workflows/linux.yml/badge.svg)](https://github.com/Raku-L10N/CY/actions) [![Actions Status](https://github.com/Raku-L10N/CY/actions/workflows/macos.yml/badge.svg)](https://github.com/Raku-L10N/CY/actions) [![Actions Status](https://github.com/Raku-L10N/CY/actions/workflows/windows.yml/badge.svg)](https://github.com/Raku-L10N/CY/actions)

NAME
====

L10N::CY - Welsh localization of Raku

SYNOPSIS
========

```
$ draig -e 'dywedyd "Helo Byd"'
Helo Byd
```

```
# Must have RAKUDO_RAKUAST=1 environment variable set
use L10N::NL;
dywedyd "Helo Byd"
```

DESCRIPTION
===========

The `L10N::CY` distribution contains the logic to provide a Welsh localization of the Raku Programming Language. It installs a `draig` executable that will automatically activate the Welsh localization. And it allows one to use the Welsh localization in selected programs with a `use L10N::CY` statement.

REFERENCES
==========

[Creating a new programming language - Draig](https://dev.to/finanalyst/creating-a-new-programming-language-draig-503p)

AUTHORS
=======

Richard Hainsworth [rnhainsworth@gmail.com](mailto:rnhainsworth@gmail.com)

COPYRIGHT AND LICENSE
=====================

Copyright 2024, 2025 Raku Localization Team

This library is free software; you can redistribute it and/or modify it under the Artistic License 2.0.