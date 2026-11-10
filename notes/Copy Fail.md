---
title: "Copy Fail"
url: https://copy.fail/
clipped: 2026-06-17 01:10:10
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Copy Fail](https://copy.fail/)

## Digest Summary
CVE‑2026‑31431 (“Copy Fail”) affects Linux kernels built from 2017 up to the patch release, encompassing virtually all mainstream distributions that enable the kernel crypto API (AF_ALG) by default. The vulnerability can be exploited locally by any unprivileged user without requiring network access, debugging features, or pre‑installed primitives. Tested kernels include 6.17.0‑1007‑aws, 6.18.8‑9.213.amzn2023, 6.12.0‑124.45.1.el10_1, and 6.12.0‑160000.9‑default; similar behavior is expected on Debian, Arch, Fedora, Rocky, Alma, Oracle, and embedded systems.

Impact categories and severity:
- Multi‑tenant Linux hosts (shared dev boxes, jump hosts, build servers): any user can obtain root – **High**.
- Kubernetes/containers: shared page cache allows a compromised pod to gain host‑level root – **High**.
- CI runners & build farms (GitHub Actions, GitLab, Jenkins): untrusted PR code can become root – **High**.
- Cloud SaaS running user code (notebooks, serverless functions): tenant can gain host root – **Medium**.
- Standard single‑tenant servers: local privilege escalation useful for chaining with other exploits – **Lower**.
- Single‑user workstations: provides a post‑exploitation privilege‑escalation step – **Low**.

## Discussion Summary
Comments emphasize that the AF_ALG vulnerability (CVE‑2026‑31431) is viewed as serious due to its large attack surface and ease of exploitation, especially on systems with default crypto user‑API options enabled. Contributors note inconsistent vendor handling, delayed patches across distributions, and variable reproducibility of the PoC. Common mitigation advice includes updating to patched kernels, disabling CONFIG_CRYPTO_USER_API_* or the algif_aead module, and applying seccomp restrictions. There is criticism of AI‑generated write‑ups and a call for broader security review.

---

## Full Article

Who is affected
---------------

If your kernel was built between 2017 and the patch — which covers essentially every mainstream Linux distribution — you're in scope.

Copy Fail requires only an unprivileged local user account — no network access, no kernel debugging features, no pre-installed primitives. The kernel crypto API (`AF_ALG`) ships enabled in essentially every mainstream distro's default config, so the entire 2017 → patch window is in play out of the box.

**Distributions we directly verified:**

| Distribution | Kernel |
| --- | --- |
| Ubuntu 24.04 LTS | `6.17.0-1007-aws` |
| Amazon Linux 2023 | `6.18.8-9.213.amzn2023` |
| RHEL 10.1 | `6.12.0-124.45.1.el10_1` |
| SUSE 16 | `6.12.0-160000.9-default` |

These are what we tested directly. Other distributions running affected kernels — Debian, Arch, Fedora, Rocky, Alma, Oracle, the embedded crowd — behave the same. Tested it elsewhere? [Open an issue](https://github.com/theori-io/copy-fail-CVE-2026-31431) to add to the list.

**Should you patch first?**

High

### Multi-tenant Linux hosts

Shared dev boxes, shell-as-a-service, jump hosts, build servers — anywhere multiple users share a kernel.

any user becomes root

High

### Kubernetes / container clusters

The page cache is shared across the host. A pod with the right primitives compromises the node and crosses tenant boundaries.

cross-container, cross-tenant

High

### CI runners & build farms

GitHub Actions self-hosted runners, GitLab runners, Jenkins agents — anything that executes untrusted PR code as a regular user, on a shared kernel.

a PR becomes root on the runner

High

### Cloud SaaS running user code

Notebook hosts, agent sandboxes, serverless functions, any tenant-supplied container or script.

tenant becomes host root

Medium

### Standard Linux servers

Single-tenant production where only your team has shell access.

internal LPE; chains with web RCE or stolen creds

Lower

### Single-user laptops & workstations

You're already the only user. The bug doesn't grant remote attackers access by itself, but any local code execution becomes root.

post-exploitation step-up