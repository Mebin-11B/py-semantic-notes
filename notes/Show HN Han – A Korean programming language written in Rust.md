---
title: "Show HN: Han – A Korean programming language written in Rust"
url: https://github.com/xodn348/han
clipped: 2026-06-17 01:32:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Han – A Korean programming language written in Rust](https://github.com/xodn348/han)

## Digest Summary
Han is a statically‑typed, compiled language whose entire syntax uses Korean Hangul keywords (e.g., 함수, 만약, 반복, 변수). Implemented in Rust, the toolchain includes a lexer, recursive‑descent parser, AST, tree‑walking interpreter, and a code generator that emits plain‑text LLVM IR, which clang then compiles to native binaries. The language supports:

- Primitive types: 정수, 실수, 문자열, 불, 없음.  
- Arrays with indexing (including negative indices) and methods (.추가, .삭제, .정렬, .역순, .합치기).  
- Structs with field access and impl blocks; closures with environment capture.  
- Control flow: if/else (만약/아니면), for loops (반복), while loops (동안), break/continue (멈춰/계속), pattern matching (맞춰).  
- Error handling via try/catch style (시도/실패).  
- File I/O (파일읽기, 파일쓰기, 파일추가, 파일존재).  
- Built‑in math, format strings, generics syntax, and module imports (가져오기).  

The project ships a REPL, LSP server, and VS Code extension. Build requires Rust 1.70+ and clang; the interpreter runs without clang. The repository includes examples, a formal SPEC.md, and 46 tests under an MIT license.

## Discussion Summary
The comments express strong interest in exploring programming languages that use non‑English scripts, especially Korean Hangul, and see the project as a creative extension of LLM‑driven language design. Multiple remarks cite existing Korean languages, note potential ergonomic and input‑method challenges, and ask whether Hangul’s structural features could be leveraged beyond simple keyword substitution. Opinions are generally supportive and curious, with occasional technical questions about compilation speed, symbol handling, and naming, while acknowledging inertia and practical barriers as reasons such languages remain rare.

---

## Full Article

Han (한) Programming Language
============================

> A general-purpose compiled language with Korean keywords, types, built-ins, and standard library — written in Rust

[![Playground](https://camo.githubusercontent.com/cdc8a3562cf488366407d76057d29e4f3c6338f47e9e2a545f3f251f84bdd854/68747470733a2f2f696d672e736869656c64732e696f2f62616467652fe296b6253230706c617967726f756e642d74727925323069742532306c6976652d627269676874677265656e3f7374796c653d666c61742d737175617265)](https://xodn348.github.io/han/playground/)
[![Docs](https://camo.githubusercontent.com/ec3defa9d7dfcd3df48430b4e81c5880b16e9748ce0137e9434caad9649935d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d786f646e3334382e6769746875622e696f25324668616e2d626c75653f7374796c653d666c61742d737175617265)](https://xodn348.github.io/han/introduction.html)
[![crates.io](https://camo.githubusercontent.com/43f3ee28fb389a755afabc77cccc5fe119895fc785f0b7dd14c748fa0f3665ab/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f68616e2d6c616e673f7374796c653d666c61742d737175617265)](https://crates.io/crates/han-lang)
[![Rust](https://camo.githubusercontent.com/4a9a8942a5fe5653e3871357474f3a0876397e60834a8cfc8d05cd82f168a68b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e67756167652d527573742d6f72616e67653f7374796c653d666c61742d737175617265)](https://github.com/xodn348/han)
[![MIT](https://camo.githubusercontent.com/422db9fd40f5831c765cf6530b6750c081b696bd18d904cf89554df98c676277/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d677265656e3f7374796c653d666c61742d737175617265)](https://github.com/xodn348/han/blob/main/LICENSE)

[![Han REPL — typing animation demo](https://github.com/xodn348/han/raw/main/assets/demo.gif)](https://github.com/xodn348/han/blob/main/assets/demo.gif)

[![Han — mugunghwa flower + 한 braille banner](https://github.com/xodn348/han/raw/main/assets/banner.png)](https://github.com/xodn348/han/blob/main/assets/banner.png)

---

**[Museum as Code](https://github.com/xodn348/museum-as-code)** ([live site](https://xodn348.github.io/museum-as-code/)) — the National Museum of Korea rebuilt with Han. 56 catalog entries and 10 hero pages are real `.hgl` source files; every code block on the site runs unchanged in `hgl interpret`. The flagship demonstration that Korean-as-syntax scales beyond hello-world to a full content site.

---

Han is not just a programming language. It is an experiment with three goals:

**1. Hangul is one of the most scientifically designed writing systems ever created**
Each character encodes the exact shape of the mouth and tongue used to pronounce it. Vowels are composed from three symbols: heaven (·), earth (ㅡ), and human (ㅣ). It was engineered for clarity, not inherited from history. Han asks: what does code look like when written in a script that was *designed* rather than evolved? *(Invented 1443 — King Sejong)*

**2. Korean Code for the AI Age — BPE optimization**
LLMs are trained on English-dominant data. BPE tokenizers treat Korean characters as rare, splitting `함수` into multiple byte-level tokens while `function` becomes one. The more Korean code exists on the internet — in repos, in documentation, in examples — the better future tokenizers will represent the Korean language. Han is a small contribution to that corpus.

**3. Minority Language as First-Class Syntax**
Korean is spoken by ~80 million people, yet essentially zero programming languages use it as syntax. Han is an experiment: what happens when a minority language becomes the grammar of a compiler? How far can it go?

---

Han is a statically-typed, compiled programming language where keywords, type names, 50+ built-in functions, and standard library methods are written in Korean — with all error messages in Korean too. Arithmetic, comparison, and assignment operators follow C/Rust conventions. It compiles to native binaries through LLVM IR and also ships with a tree-walking interpreter for instant execution. The compiler toolchain is written entirely in Rust.

---

Install the Rust crate from crates.io. The package is named `han-lang`; the language is Han and the installed CLI command is `hgl`.

Create `hello.hgl`:

Run it:

```
hgl interpret hello.hgl
# Output: 안녕하세요, 세계!
```

Conditionals use the Korean-default `만약 조건 이면 { }` form:

```
만약 x > 0 이면 {
    출력("양수")
} 아니면 {
    출력("0 또는 음수")
}
```

Or jump into the REPL:

```
hgl repl
한> 출력("안녕!")
안녕!
```

---

```
함수 계산(식: 문자열) -> 정수 {
    변수 부분 = 식.분리(" ")
    변수 왼쪽 = 정수변환(부분[0])
    변수 연산자 = 부분[1]
    변수 오른쪽 = 정수변환(부분[2])

    맞춤 연산자 {
        "+" => { 반환 왼쪽 + 오른쪽 }
        "-" => { 반환 왼쪽 - 오른쪽 }
        "*" => { 반환 왼쪽 * 오른쪽 }
        "/" => { 반환 왼쪽 / 오른쪽 }
        _ => { 반환 0 }
    }
}

출력(계산("10 + 20"))     // 30
출력(계산("6 * 7"))       // 42
```

```
구조 할일 {
    제목: 문자열,
    완료: 불
}

변수 목록 = []
목록.추가(할일 { 제목: "한글 프로그래밍 언어 만들기", 완료: 참 })
목록.추가(할일 { 제목: "README 작성하기", 완료: 거짓 })

반복 변수 i = 0; i < 목록.길이(); i += 1 {
    변수 상태 = "[ ]"
    만약 목록[i].완료 이면 { 상태 = "[✓]" }
    출력(형식("{0} {1}. {2}", 상태, i + 1, 목록[i].제목))
}
```

More examples — including word counting, file I/O, JSON, HTTP, regex, and a full 10-step tutorial series — live in the [`examples/`](https://github.com/xodn348/han/blob/main/examples) directory and the [Examples Index](https://xodn348.github.io/han/examples/index.html) in the docs.

---

* **Korean keywords** — `함수`, `만약`, `이면`, `반복`, `변수`, `상수`, `반환`, `구조`, `시도`, `처리`, `맞춤`
* **Korean word order** — `만약 조건 이면 { }`, `조건 동안 { }` (SOV) and `동안 조건 { }` (SVO)
* **Korean logical operators** — `그리고` (and), `또는` (or)
* **Hangul identifiers** — name your variables, functions, fields in Korean
* **Compiled & interpreted** — `hgl build` (LLVM IR → clang → binary) or `hgl interpret` for instant runs
* **REPL + LSP** — `hgl repl` for interactive sessions, `hgl lsp` for editor hover/completion
* **Static typing** — 5 primitives: `정수`, `실수`, `문자열`, `불`, `없음` plus arrays, structs, tuples, enums
* **Pattern matching** — `맞춤 값 { 1 => ..., _ => ... }`
* **Error handling** — `시도 { } 처리(오류) { }`
* **Closures + higher-order functions** — `변수 f = 함수(x: 정수) { 반환 x * 2 }`
* **String interpolation** — `"${expr}"` and `형식("이름: {이름}")`
* **Pipe operator** — `값 |> 함수1 |> 함수2`
* **Stdlib in Korean** — 50+ built-ins: math, regex, JSON, HTTP, file I/O, date/time, system
* **Linear algebra** — `행렬곱`, `전치`, `내적`, `외적`, `텐서곱`, `단위행렬`
* **Optional Python interop** — `파이썬()` / `파이썬_값()` for NumPy, PyTorch, etc. when built with `--features python`
* **Module imports** — `포함 "파일.hgl"` (canonical-path deduplicated)
* **Generics syntax** — `함수 최대값<T>(a: T, b: T) -> T`
* **40+ example programs** — from hello world to HTTP API calls

---

* [Rust](https://rustup.rs) (1.70+)
* clang (for `hgl build` / `hgl run`) — `xcode-select --install` or `brew install llvm`

```
git clone https://github.com/xodn348/han.git
cd han
./install.sh
```

This installs `hgl` globally and automatically sets up the VS Code extension (syntax highlighting + LSP) if VS Code is detected.

Alternatively from crates.io, install the published Rust package:

The crates.io package name is `han-lang` to avoid naming ambiguity. The language remains **Han**, and the command installed on your PATH remains `hgl`.

The default crates.io install is intentionally Python-free so `hgl` runs without requiring a local Python dynamic library. If you want Python interop built in, install with `cargo install han-lang --features python`.

---

```
hgl interpret <file.hgl>    Run with interpreter (no clang needed)
hgl build <file.hgl>        Compile to native binary (requires clang)
hgl run <file.hgl>          Compile and run immediately
hgl check <file.hgl>        Type-check only (no execution)
hgl init [name]             Create new Han project
hgl repl                    Interactive REPL
hgl lsp                     Start LSP server (hover + completion)
```

---



---

`cargo test` covers the lexer, parser, AST, interpreter, type checker, compiled backend, and integration scenarios such as closure capture, struct impl methods, tuples, and SOV parsing.

---

See [CONTRIBUTING.md](https://github.com/xodn348/han/blob/main/CONTRIBUTING.md) for development setup, branch conventions, and the PR checklist.

---

MIT

---

*Han — where the beauty of Hangul meets the precision of code.*