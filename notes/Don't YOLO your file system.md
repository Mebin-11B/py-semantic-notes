---
title: "Don't YOLO your file system"
url: https://jai.scs.stanford.edu/
clipped: 2026-06-17 01:26:09
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Don't YOLO your file system](https://jai.scs.stanford.edu/)

## Digest Summary
Jai is a lightweight sandbox for running AI‑generated commands on a local machine without granting full account access. It gives the current working directory read/write permissions while overlaying the rest of the home directory with a copy‑on‑write layer, leaving original files untouched. Temporary directories (/tmp, /var/tmp) are private; all other paths are read‑only. Jai operates via a single prefix command (e.g., “jai codex”) and requires no Docker images, Dockerfiles, or complex bubblewrap flags.

Three isolation levels let users balance convenience and security, though even the strict mode is not equivalent to a hardened container or VM. Jai is positioned between containers, bubblewrap, and chroot: lighter than Docker, simpler than bubblewrap’s manual namespace setup, and more isolated than chroot (which lacks namespace and credential separation). It is intended for ad‑hoc tasks such as quick coding assistance or running untrusted installer scripts, reducing blast radius but not guaranteeing full confidentiality or protection against determined attackers.

## Discussion Summary
The comments show cautious optimism toward sandboxed AI agents, praising the ability to confine file‑system access while allowing work in the current directory and noting that such defaults would improve safety. Users express frustration with building C++ tools and request ready‑to‑run binaries. Security concerns focus on agents writing unexpected files, potential privilege escalation, and the need for mechanisms like git‑filtered transfers, overlay directories, or snapshotting to mitigate damage. Alternative sandbox solutions (firejail, seatbelt, safety‑net projects) are mentioned, and calls for clearer UI, documentation, and broader discussion of risks are common.

---

## Full Article

This is not hypothetical.
-------------------------

People are already reporting lost files, emptied working trees, and wiped home directories after giving AI tools ordinary machine access.

There's a gap between giving an agent your real account and stopping everything to build a container or VM. **jai fills that gap.** One command, no images, no Dockerfiles — just a light-weight boundary for the workflows you're already running: quick coding help, one-off local tasks, running installer scripts you didn't write.

### Your files, your rules

Use AI agents without handing over your whole account. jai gives your working directory full access and keeps the rest of your home behind a copy-on-write overlay — or hidden entirely.

### Stop trusting blindly

One-line installer scripts, AI-generated shell commands, unfamiliar CLIs — stop running them against your real home directory. Drop `jai` in front and the worst case gets a lot smaller.

### Containment shouldn't be hard

No images to build, no Dockerfiles to maintain, no 40-flag bwrap invocations. Just `jai your-agent`. If containment isn't easier than YOLO mode, nobody will bother.

How it works
------------

One command. No setup required.

1

**Prefix your command**  
`jai codex`, `jai claude`, or just `jai` for a shell.

2

**CWD stays writable**  
Your working directory keeps full read/write access inside the jail.

3

**Home is an overlay**  
Changes to your home directory are captured copy-on-write. Originals are untouched.

4

**Rest is locked down**  
`/tmp` and `/var/tmp` are private. All other files are read-only.

Three modes
-----------

Pick the level of isolation that fits your workflow.

|  | Casual | Strict | Bare |
| --- | --- | --- | --- |
| Home directory | Copy-on-write overlay | Empty private home | Empty private home |
| Process runs as | Your user | Unprivileged `jai` user | Your user |
| Confidentiality | Weak — most files readable | Strong — separate UID | Medium — your UID, but home hidden |
| Integrity | Overlay protects originals | Full isolation | Full isolation |
| NFS home support | Yes | No | Yes |

Versus the alternatives
-----------------------

jai is not trying to replace containers. It fills a different niche.

### Docker

Great for reproducible, image-based environments. Heavier to set up for ad-hoc sandboxing of host tools. No overlay-on-home workflow.

### bubblewrap

Powerful namespace sandbox. Requires explicitly assembling the filesystem view — often turns into a long wrapper script, which is the friction jai removes.

### chroot

Not a security mechanism. No mount isolation, no PID namespace, no credential separation. Linux documents it as not intended for sandboxing.

### jai is not a promise of perfect safety.

jai is a casual sandbox — it reduces the blast radius, but does not eliminate all the ways AI agents can harm you or your system. Casual mode does not protect confidentiality. Even strict mode is not equivalent to a hardened container runtime or VM. When you need strong multi-tenant isolation or defense against a determined adversary, use a proper container or virtual machine. [Read the full security model →](https://jai.scs.stanford.edu/security.html)