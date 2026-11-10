---
title: "Woxi: Wolfram Mathematica Reimplementation in Rust"
url: https://github.com/ad-si/Woxi
clipped: 2026-06-17 01:38:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Woxi: Wolfram Mathematica Reimplementation in Rust](https://github.com/ad-si/Woxi)

## Digest Summary
The repository ad‑si/Woxi on GitHub implements a re‑creation of the Wolfram Language/Mathematica environment using the Rust programming language, referred to as “Wolfram oxidized.” The page displays a wordmark for Woxi, a collage of applications that integrate the library, and a screenshot of a Jupyter Notebook session demonstrating its usage. User handles @claude, @ad‑si, @rgbkrk, and @adamnemecek are shown, likely indicating contributors or community members. No additional technical documentation, code examples, or usage instructions are present in the scraped content.

## Discussion Summary
The discussion highlights mixed reactions to the project’s design and progress. Critics point to an architectural issue where core mathematical features are hard‑coded in Rust instead of the language itself, fearing long‑term maintainability problems. The lead developer emphasizes steady advancement toward a release covering most Mathematica 1.0 functionality and notes existing Jupyter‑Lite and studio front‑ends. Participants express enthusiasm for a polished CLI kernel and the open‑source, AGPL model, while also raising concerns about licensing, proprietary algorithms, and potential code reuse. Overall sentiment combines cautious optimism with technical skepticism.

---

## Full Article

[![Wordmark of Woxi](https://github.com/ad-si/Woxi/raw/main/images/logo.png)](https://github.com/ad-si/Woxi/blob/main/images/logo.png)

An interpreter for the Wolfram Language powered by Rust.

[![Collage of apps using Woxi](https://github.com/ad-si/Woxi/raw/main/images/2026-02-28T1201_collage.png)](https://github.com/ad-si/Woxi/blob/main/images/2026-02-28T1201_collage.png)

The initial focus is to implement a subset of the Wolfram Language
so that it can be used for CLI scripting and notebooks.
For example:

```
#!/usr/bin/env woxi

(* Print the square of 5 random integers between 1 and 9 *)
RandomInteger[{1, 9}, 5] // Map[#^2&] // Map[Print]
```

It has full support for Jupyter Notebooks including graphical output:

[![Screenshot of Jupyter Notebook](https://github.com/ad-si/Woxi/raw/main/images/2026-02-12t1501_jupyter.png)](https://github.com/ad-si/Woxi/blob/main/images/2026-02-12t1501_jupyter.png)

Check out the [CLI tests](https://github.com/ad-si/Woxi/blob/main/tests/cli) directory
to see all currently supported commands and their expected output.
All tests must pass with Woxi and WolframScript.

Also check out the [functions.csv](https://github.com/ad-si/Woxi/blob/main/functions.csv) file
for a list of all Wolfram Language functions and their implementation status.

Woxi runs faster than WolframScript as there is no overhead of starting a kernel
and verifying its license.

You can easily install it with [Rust's cargo](https://doc.rust-lang.org/cargo/):

If you want to build Woxi from source, you need to have Rust installed.
You can get it from [rust-lang.org](https://www.rust-lang.org/tools/install).

Clone the repository, build the project, and install it:

```
git clone https://github.com/ad-si/Woxi
cd Woxi
make install
```

On macOS, `make install` additionally builds the Woxi Studio notebook editor
and installs it as a `.app` bundle at `/Applications/Woxi Studio.app`,
registered with Launch Services so that `.nb`, `.wl`, and `.wls` files appear
under Finder's "Open With…" menu.

You can use the interpreter directly from the command line:

```
woxi eval 'StringJoin["Hello", " ", "World!"]'
# Hello World!
```

Or you can run a script:

```
woxi run tests/scripts/hello_world.wls
```

You can also use Woxi in Jupyter notebooks.
Install the kernel with:

Then start the Jupyter server:

```
cd examples && jupyter lab
```

Or simply use our
[JupyterLite instance](https://woxi.ad-si.com/jupyterlite/lab/index.html?path=showcase.ipynb).
It runs fully self-contained in your browser and no data is send to the cloud.

| Woxi | WolframScript |
| --- | --- |
| `woxi eval "1 + 2"` | `wolframscript -code "1 + 2"` |
| `woxi run script.wls` | `wolframscript script.wls` |

Contributions are very welcome!
Please feel free to submit a Pull Request.

To run the test suite: