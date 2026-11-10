---
title: "Hoot: Scheme on WebAssembly"
url: https://www.spritely.institute/hoot/
clipped: 2026-06-17 01:47:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Hoot: Scheme on WebAssembly](https://www.spritely.institute/hoot/)

## Digest Summary
Hoot is a Spritely project enabling execution of Scheme code in WebAssembly‑capable browsers that support garbage collection. It provides a Scheme‑to‑Wasm compiler and a complete Wasm toolchain, all built atop Guile with no external dependencies. The toolchain includes a Wasm interpreter, allowing Hoot binaries to be tested directly from the Guile REPL. The current stable release is version 0.7.0, with source and development versions available via Git. Documentation, announcements, and related articles or videos are linked from the project page. An accompanying logo image is also provided.

## Discussion Summary
Comments show enthusiasm for recent Guile developments and the resurgence of WebAssembly language support, with interest in using the compiled output on platforms like Cloudflare Workers and avoiding JavaScript. At the same time, users express disappointment over community fragmentation, performance gaps compared to Racket, and the lack of extensive libraries. Some reflections consider broader implications for future programming languages, questioning their professional relevance and potential shift toward more explicit, error‑reducing designs. Overall sentiment blends optimism about new capabilities with criticism of existing limitations.

---

## Full Article

Hoot: Scheme on WebAssembly
===========================

![Hoot logo](https://files.spritely.institute/images/blog/hoot.png)

Hoot is a Spritely project for running Scheme programs on the web,
featuring a Scheme to Wasm compiler and a general-purpose Wasm
toolchain.

Hoot is built on [Guile](https://gnu.org/software/guile) and has no
additional required dependencies. The toolchain is self-contained and
even includes a Wasm interpreter for running Wasm programs on the
Guile virtual machine.

The latest release is [0.9.0](https://www.spritely.institute/news/hoot-0-9-0-released.html).

Try Hoot!
---------

Get Hoot!
---------

### Install on Guix

Guix is well-integrated into the Guile ecosystem and is the best way
to get the most up-to-date version of Hoot.

```
guix install guile guile-hoot
```

### Install on Debian

Hoot is currently available in Debian testing and unstable. In time
it will reach stable, too.

```
apt install guile-hoot
```

### Install on macOS

Hoot is [available in the Guile Homebrew
tap](https://github.com/aconchillo/homebrew-guile).

```
brew tap aconchillo/guile
brew install guile-hoot
```

### Build from source

Source release tarballs and their respective GPG signatures can be
found [on our artifact
server](https://files.spritely.institute/releases/guile-hoot).

See the `README` file for build instructions.

Documentation
-------------

[Read the online manual](https://files.spritely.institute/docs/guile-hoot/latest)

Compatibility
-------------

Hoot supports R7RS-small Scheme and a subset of Guile Scheme.

Hoot is compatible with the following Wasm runtimes:

* Firefox 121+
* Chrome 119+
* Safari 26+
* NodeJS 22+

Get involved
------------

Issues and pull requests for Hoot can be submitted over on our
[Codeberg repository](https://codeberg.org/spritely/hoot).

Articles and videos
-------------------