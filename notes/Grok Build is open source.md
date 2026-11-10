---
title: "Grok Build is open source"
url: https://github.com/xai-org/grok-build
clipped: 2026-08-31 12:22:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Grok Build is open source](https://github.com/xai-org/grok-build)

## Digest Summary
Grok Build is SpaceXAI’s terminal‑based AI coding agent, delivered as a full‑screen TUI that can analyze codebases, edit files, run shell commands, perform web searches, and manage long‑running tasks. It operates interactively, headlessly for CI/scripts, or via the Agent Client Protocol (ACP) for editor integration. The repository contains Rust source for the CLI/TUI and its runtime, synchronized from the SpaceXAI monorepo. Prebuilt binaries for macOS, Linux, and Windows are installed via curl or PowerShell scripts; the binary is named `xai-grok-pager` and distributed as `grok`. Build requirements include the pinned Rust toolchain (managed by `rust-toolchain.toml`), `protoc` for protobuf generation, and supported host OSes (macOS/Linux; Windows builds are best‑effort). The workspace uses a generated root `Cargo.toml`; individual crate `Cargo.toml` files should be edited. Documentation, user guide, keyboard shortcuts, slash commands, theming, plugins, hooks, headless mode, and sandboxing are available under `crates/codegen/xai-grok-pager/docs/user-guide/`. The code is licensed under Apache 2.0, with third‑party components retaining original licenses.

---

## Full Article

[Skip to content](https://github.com/xai-org/grok-build#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [xai-org](https://github.com/xai-org)    
    /
    
      [grok-build](https://github.com/xai-org/grok-build)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fxai-org%2Fgrok-build)    You must be signed in to change notification settings

  

  
- 
          [Fork
    4.9k](https://github.com/login?return_to=%2Fxai-org%2Fgrok-build)
  

  
- 
        
        [Star
          26.3k](https://github.com/login?return_to=%2Fxai-org%2Fgrok-build)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/xai-org/grok-build/branches)[Tags](https://github.com/xai-org/grok-build/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[40 Commits](https://github.com/xai-org/grok-build/commits/main/)40 Commits

## Folders and files

NameNameLast commit messageLast commit date[.cargo](https://github.com/xai-org/grok-build/tree/main/.cargo)[.cargo](https://github.com/xai-org/grok-build/tree/main/.cargo)  [bin](https://github.com/xai-org/grok-build/tree/main/bin)[bin](https://github.com/xai-org/grok-build/tree/main/bin)  [crates](https://github.com/xai-org/grok-build/tree/main/crates)[crates](https://github.com/xai-org/grok-build/tree/main/crates)  [prod/mc/cli-chat-proxy-types](https://github.com/xai-org/grok-build/tree/main/prod/mc/cli-chat-proxy-types)[prod/mc/cli-chat-proxy-types](https://github.com/xai-org/grok-build/tree/main/prod/mc/cli-chat-proxy-types)  [third_party](https://github.com/xai-org/grok-build/tree/main/third_party)[third_party](https://github.com/xai-org/grok-build/tree/main/third_party)  [.gitignore](https://github.com/xai-org/grok-build/blob/main/.gitignore)[.gitignore](https://github.com/xai-org/grok-build/blob/main/.gitignore)  [CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md)[CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md)  [Cargo.lock](https://github.com/xai-org/grok-build/blob/main/Cargo.lock)[Cargo.lock](https://github.com/xai-org/grok-build/blob/main/Cargo.lock)  [Cargo.toml](https://github.com/xai-org/grok-build/blob/main/Cargo.toml)[Cargo.toml](https://github.com/xai-org/grok-build/blob/main/Cargo.toml)  [LICENSE](https://github.com/xai-org/grok-build/blob/main/LICENSE)[LICENSE](https://github.com/xai-org/grok-build/blob/main/LICENSE)  [README.md](https://github.com/xai-org/grok-build/blob/main/README.md)[README.md](https://github.com/xai-org/grok-build/blob/main/README.md)  [SECURITY.md](https://github.com/xai-org/grok-build/blob/main/SECURITY.md)[SECURITY.md](https://github.com/xai-org/grok-build/blob/main/SECURITY.md)  [SOURCE_REV](https://github.com/xai-org/grok-build/blob/main/SOURCE_REV)[SOURCE_REV](https://github.com/xai-org/grok-build/blob/main/SOURCE_REV)  [THIRD-PARTY-NOTICES](https://github.com/xai-org/grok-build/blob/main/THIRD-PARTY-NOTICES)[THIRD-PARTY-NOTICES](https://github.com/xai-org/grok-build/blob/main/THIRD-PARTY-NOTICES)  [clippy.toml](https://github.com/xai-org/grok-build/blob/main/clippy.toml)[clippy.toml](https://github.com/xai-org/grok-build/blob/main/clippy.toml)  [rust-toolchain.toml](https://github.com/xai-org/grok-build/blob/main/rust-toolchain.toml)[rust-toolchain.toml](https://github.com/xai-org/grok-build/blob/main/rust-toolchain.toml)  [rustfmt.toml](https://github.com/xai-org/grok-build/blob/main/rustfmt.toml)[rustfmt.toml](https://github.com/xai-org/grok-build/blob/main/rustfmt.toml)  View all files

## Repository files navigation

# 
  
    
    
    
  
  
  Grok Build ( `grok` )

Grok Build is SpaceXAI's terminal-based AI coding agent. It runs as a
full-screen TUI that understands your codebase, edits files, executes shell
commands, searches the web, and manages long-running tasks — interactively,
headlessly for scripting/CI, or embedded in editors via the Agent Client
Protocol (ACP).

[Installing the released binary](https://github.com/xai-org/grok-build#installing-the-released-binary) ·
[Building from source](https://github.com/xai-org/grok-build#building-from-source) ·
[Documentation](https://github.com/xai-org/grok-build#documentation) ·
[Repository layout](https://github.com/xai-org/grok-build#repository-layout) ·
[Development](https://github.com/xai-org/grok-build#development) ·
[Contributing](https://github.com/xai-org/grok-build#contributing) ·
[License](https://github.com/xai-org/grok-build#license)

Learn more about Grok Build at [x.ai/cli](https://x.ai/cli)

This repository contains the Rust source for the  `grok`  CLI/TUI and its agent
runtime. It is synced periodically from the SpaceXAI monorepo.

A small  `SOURCE_REV`  file at the root records the full monorepo commit SHA
for the version of the code present in this tree.

## Installing the released binary

Prebuilt binaries are published for macOS, Linux, and Windows:
 `curl -fsSL https://x.ai/cli/install.sh | bash   # macOS / Linux / Git Bash
irm https://x.ai/cli/install.ps1 | iex          # Windows PowerShell
grok --version` 

See the [changelog](https://x.ai/build/changelog) for the latest fixes,
features, and improvements in each release.

## Building from source

Requirements:

- 

Rust — the toolchain is pinned by  `` [rust-toolchain.toml](https://github.com/xai-org/grok-build/blob/main/rust-toolchain.toml);
 `rustup`  installs it automatically on first build.

- 

[DotSlash](https://dotslash-cli.com) — required so hermetic tools under
 `` [bin/](https://github.com/xai-org/grok-build/blob/main/bin) (notably  `` [bin/protoc](https://github.com/xai-org/grok-build/blob/main/bin/protoc)) can download and run.
Install it and ensure  `dotslash`  is on your  `PATH`  before building:
 `cargo install dotslash
# or: prebuilt packages — https://dotslash-cli.com/docs/installation/
/usr/bin/env dotslash --help   # sanity check` 

- 

protoc — proto codegen resolves  `` [bin/protoc](https://github.com/xai-org/grok-build/blob/main/bin/protoc) via DotSlash,
or falls back to a  `protoc`  on  `PATH`  /  `$PROTOC` .

- 

macOS and Linux are supported build hosts; Windows builds are best-effort
and not currently tested from this tree.

 `cargo run -p xai-grok-pager-bin              # build + launch the TUI
cargo build -p xai-grok-pager-bin --release  # release binary: target/release/xai-grok-pager
cargo check -p xai-grok-pager-bin            # fast validation` 

The binary artifact is named  `xai-grok-pager` ; official installs ship it as
 `grok` . On first launch it opens your browser to authenticate — see the
[authentication guide](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/02-authentication.md).

## Documentation

Full online documentation is available at
[docs.x.ai/build/overview](https://docs.x.ai/build/overview).

The user guide ships with the pager crate:
 `` [crates/codegen/xai-grok-pager/docs/user-guide/](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide)
— getting started, keyboard shortcuts, slash commands, configuration, theming,
MCP servers, skills, plugins, hooks, headless mode, sandboxing, and more.

## Repository layout

Path
Contents

 `crates/codegen/xai-grok-pager-bin` 
Composition-root package; builds the  `xai-grok-pager`  binary

 `crates/codegen/xai-grok-pager` 
The TUI: scrollback, prompt, modals, rendering

 `crates/codegen/xai-grok-shell` 
Agent runtime + leader/stdio/headless entry points

 `crates/codegen/xai-grok-tools` 
Tool implementations (terminal, file edit, search, ...)

 `crates/codegen/xai-grok-workspace` 
Host filesystem, VCS, execution, checkpoints

 `crates/codegen/...` 
The rest of the CLI crate closure (config, MCP, markdown, sandbox, ...)

 `crates/common/` ,  `crates/build/` ,  `prod/mc/` 
Small shared leaf crates pulled in by the closure

 `third_party/` 
Vendored upstream source (Mermaid diagram stack) — see below

Important

The root  `Cargo.toml`  (workspace members, dependency versions, lints,
profiles) is generated — treat it as read-only. Prefer editing per-crate
 `Cargo.toml`  files.

## Development

 `cargo check -p <crate>        # always target specific crates; full-workspace builds are slow
cargo test -p xai-grok-config # per-crate tests
cargo clippy -p <crate>       # lint config: clippy.toml at the repo root
cargo fmt --all               # rustfmt.toml at the repo root` 

## Contributing

Note

External contributions are not accepted. See  `` [CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md).

## License

First-party code in this repository is licensed under the Apache License,
Version 2.0 — see  `` [LICENSE](https://github.com/xai-org/grok-build/blob/main/LICENSE).

Third-party and vendored code remains under its original licenses. See:

-  `` [THIRD-PARTY-NOTICES](https://github.com/xai-org/grok-build/blob/main/THIRD-PARTY-NOTICES) — crates.io / git dependencies,
bundled UI themes, and in-tree source ports (including openai/codex and
sst/opencode tool implementations)

-  `` [crates/codegen/xai-grok-tools/THIRD_PARTY_NOTICES.md](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-tools/THIRD_PARTY_NOTICES.md)
— crate-local notice for the codex and opencode ports (license texts +
Apache §4(b) change notice)

-  `` [third_party/NOTICE](https://github.com/xai-org/grok-build/blob/main/third_party/NOTICE) — vendored Mermaid-stack index

## About

SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.

### Resources

[Readme](https://github.com/xai-org/grok-build#readme-ov-file)[Apache-2.0 license](https://github.com/xai-org/grok-build#Apache-2.0-1-ov-file)

### Contributing

[Contributing](https://github.com/xai-org/grok-build#contributing-ov-file)

### Security policy

[Security policy](https://github.com/xai-org/grok-build#security-ov-file)[Activity](https://github.com/xai-org/grok-build/activity)[Custom properties](https://github.com/xai-org/grok-build/custom-properties)

### Stars

26.3k stars

### Watchers

222 watching

### Forks

[4.9k forks](https://github.com/xai-org/grok-build/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fxai-org%2Fgrok-build&report=xai-org+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
