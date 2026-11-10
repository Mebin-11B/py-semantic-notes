---
title: "Claude Code uses Bun written in Rust now"
url: https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/
clipped: 2026-08-31 12:23:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Claude Code uses Bun written in Rust now](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)

## Digest Summary
Claude Code v2.1.181 (released June 17) and later versions use a Rust‑ported version of Bun, yielding roughly a 10 % startup speed improvement on Linux. Inspection of the installed binary with `strings` shows “Bun v1.4.0 (macOS arm64)”, a version newer than the latest public GitHub release (v1.3.14). The Rust canary build can be installed via `bun upgrade --canary`. Further analysis with `strings` extracts 563 Rust source file paths (e.g., `src/runtime/bake/dev_server/mod.rs`, `src/bundler/bundle_v2.rs`), confirming Rust code inclusion. A workaround using `BUN_OPTIONS="--preload=/tmp/bun-version.ts"` displays the embedded Bun version (`1.4.0`). The version bump to 1.4.0 appears in a May 17 commit to `package.json`, but it remains untagged outside the canary channel. This indicates Claude Code’s production deployment runs the Rust‑based Bun across many devices.

---

## Full Article

# [Simon Willison’s Weblog](https://simonwillison.net/)

    [Subscribe](https://simonwillison.net/about/#subscribe)
  

  
    Sponsored by: Greptile — The Al code reviewer that runs your code. Catch bugs that only show up at runtime. [Try it for free](https://10xn.link/sw-greptile)
  

19th July 2026

In [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) Jarred Sumner made the following claim:

Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.

I decided to have a poke at my own Claude Code installation to see if I could find evidence that it was using Bun written in Rust.

I found these two commands convincing:
 ` `strings ~/.local/bin/claude | grep -m1 'Bun v1'
` ` 

For me this outputs  `Bun v1.4.0 (macOS arm64)` . The most recent release of [Bun on GitHub](https://github.com/oven-sh/bun/releases) is currently [v1.3.14](https://github.com/oven-sh/bun/releases/tag/bun-v1.3.14) from May 12th, so that v1.4.0 version number in Claude supports them shipping a preview of a not-yet-released Bun version.

(Update: The Rust version has been released as [Bun canary](https://bun.com/docs/installation#canary-builds) - running  `bun upgrade --canary`  will install [this release](https://github.com/oven-sh/bun/releases/tag/canary).)
 ` `strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'
` ` 

This outputs a list of [563 filenames](https://gist.github.com/simonw/c92fb0f67b114ac26e3b95a09ddccfdc), starting with these:
 ` `src/runtime/bake/dev_server/mod.rs
src/runtime/bake/production.rs
src/bundler/bundle_v2.rs
` ` 

It looks like Bun in Rust is indeed being run in production across millions of different devices. Like Jarred said, "Boring is good".

Update: Here's a neat trick [from Ajan Raj](https://twitter.com/ajanraj25/status/2078825794701242697):
 ` `cat > /tmp/bun-version.ts <<'EOF'
console.log("embedded bun:", Bun.version);
process.exit(0);
EOF
BUN_OPTIONS="--preload=/tmp/bun-version.ts" claude --version
` ` 

This outputs  `1.4.0`  for me.

Here's [the commit from May 17th](https://github.com/oven-sh/bun/commit/b18bf6d1d0a92238f240bfd125f0e3b3461b9243#diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519) that updated the version in  `package.json`  to 1.4.0. That version hasn't been changed since then, but also hasn't yet made it into a tagged release outside of  `canary` .

Posted [19th July 2026](https://simonwillison.net/2026/Jul/19/) at 3:54 am

## Recent articles

  
    
- [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) - 30th August 2026
  
    
- [Conceptual integrity and counting lines of code](https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/) - 19th August 2026
  
    
- [Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) - 16th August 2026
  

 

This is a note by Simon Willison, posted on [19th July 2026](https://simonwillison.net/2026/Jul/19/).

    
        [rust
            113](https://simonwillison.net/tags/rust/)
    
        [anthropic
            332](https://simonwillison.net/tags/anthropic/)
    
        [claude-code
            125](https://simonwillison.net/tags/claude-code/)
    
        [bun
            9](https://simonwillison.net/tags/bun/)
    
        [jarred-sumner
            3](https://simonwillison.net/tags/jarred-sumner/)
    

  

### 
    Monthly briefing
  

  

    Sponsor me for $10/month and get a curated email digest of the month's most important LLM developments.
  
  

    Pay me to send you less!
  
  [Sponsor & subscribe](https://github.com/sponsors/simonw/)

 

 
 

    
      
- [Disclosures](https://simonwillison.net/about/#disclosures)
      
- [Colophon](https://simonwillison.net/about/#about-site)
      
- ©
      
- [2002](https://simonwillison.net/2002/)
      
- [2003](https://simonwillison.net/2003/)
      
- [2004](https://simonwillison.net/2004/)
      
- [2005](https://simonwillison.net/2005/)
      
- [2006](https://simonwillison.net/2006/)
      
- [2007](https://simonwillison.net/2007/)
      
- [2008](https://simonwillison.net/2008/)
      
- [2009](https://simonwillison.net/2009/)
      
- [2010](https://simonwillison.net/2010/)
      
- [2011](https://simonwillison.net/2011/)
      
- [2012](https://simonwillison.net/2012/)
      
- [2013](https://simonwillison.net/2013/)
      
- [2014](https://simonwillison.net/2014/)
      
- [2015](https://simonwillison.net/2015/)
      
- [2016](https://simonwillison.net/2016/)
      
- [2017](https://simonwillison.net/2017/)
      
- [2018](https://simonwillison.net/2018/)
      
- [2019](https://simonwillison.net/2019/)
      
- [2020](https://simonwillison.net/2020/)
      
- [2021](https://simonwillison.net/2021/)
      
- [2022](https://simonwillison.net/2022/)
      
- [2023](https://simonwillison.net/2023/)
      
- [2024](https://simonwillison.net/2024/)
      
- [2025](https://simonwillison.net/2025/)
      
- [2026](https://simonwillison.net/2026/)
      
-
