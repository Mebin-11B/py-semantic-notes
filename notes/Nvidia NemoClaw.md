---
title: "Nvidia NemoClaw"
url: https://github.com/NVIDIA/NemoClaw
clipped: 2026-06-17 01:31:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Nvidia NemoClaw](https://github.com/NVIDIA/NemoClaw)

## Digest Summary
NVIDIA NemoClaw is an open‑source plugin that installs the NVIDIA OpenShell runtime to run OpenClaw agents inside a sandboxed environment. The sandbox enforces security policies (Landlock, seccomp, network namespaces) and routes inference calls through NVIDIA cloud APIs, e.g., the nemotron‑3‑super‑120b‑a12b model. Installation is performed via a single script (`curl … | bash`) which also installs Node.js if needed, then runs an onboarding wizard to configure the sandbox, inference provider, and security policies. The compressed sandbox image (~2.4 GB) requires ≥8 GB RAM or sufficient swap to avoid OOM termination. Primary CLI commands include `nemoclaw  connect`, `status`, `logs`, and OpenShell subcommands for sandbox management. Interaction with the agent can be done through the OpenClaw TUI (`openclaw tui`) or CLI (`openclaw agent …`). Local inference options (Ollama, vLLM) are experimental and may need additional host routing support. Known limitations note ongoing development of the OpenClaw‑NemoClaw plugin and potential platform‑specific workarounds. The project is released under the Apache License 2.0.

## Discussion Summary
The discussion centers on strong skepticism toward OpenClaw’s security model, emphasizing risks such as prompt‑injection, credential leakage, and inadequate sandboxing despite Nvidia‑provided inference. Commenters repeatedly call for more granular, kernel‑level isolation methods (e.g., Docker, gVisor, custom bwrap) and tighter policy controls rather than relying on the current bespoke sandbox. Opinions also question the practical usefulness of fully integrated agents and view the hype as commercially driven. A minority note the impressive early‑career implementation and suggest alternative frameworks like NanoClaw or proxy‑based solutions.

---

## Full Article

NVIDIA NemoClaw: Reference Stack for Sandboxed AI Agents in OpenShell
=====================================================================

[![License](https://camo.githubusercontent.com/d8e3b9d3b1213595b06824a404d41ad7743f1e880a3f9e47bae54533a9b60c99/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368655f322e302d626c7565)](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE)
[![Security Policy](https://camo.githubusercontent.com/d7b3ea7a80c2502d6f91036a7b8d1b56bf3f0c7fda63638c5735c06d64af5644/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53656375726974792d5265706f72742532306125323056756c6e65726162696c6974792d726564)](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md)
[![Discord](https://camo.githubusercontent.com/32172cbf5d9e1bad5a24c341e72d774dfdeb83e7099e33bfbb21756a3e669e42/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d4a6f696e2d373238396461)](https://discord.gg/XFpfPv9Uvx)

NVIDIA NemoClaw is an open source reference stack for running always-on AI agents more safely inside [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) sandboxes.
It provides guided onboarding, a hardened blueprint, routed inference, network policy, and lifecycle management through a single CLI.

**Supported agents:**

For capabilities, architecture, security controls, and the full feature list, see the [NemoClaw documentation](https://docs.nvidia.com/nemoclaw/latest/).

Review [Prerequisites](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html) before installing.
For Hermes, set `NEMOCLAW_AGENT=hermes` before running the installer, or use the `nemohermes` alias after install.

Refer to the following pages on the official documentation website for more information on NemoClaw.

| Page | Description |
| --- | --- |
| [Overview](https://docs.nvidia.com/nemoclaw/latest/about/overview.html) | What NemoClaw does and how it fits together. |
| [Architecture Overview](https://docs.nvidia.com/nemoclaw/latest/about/how-it-works.html) | High-level overview of Plugin, blueprint, sandbox lifecycle, and protection layers. |
| [Ecosystem](https://docs.nvidia.com/nemoclaw/latest/about/ecosystem.html) | How OpenClaw, OpenShell, and NemoClaw form a stack and when to use NemoClaw versus OpenShell alone. |
| [Architecture Details](https://docs.nvidia.com/nemoclaw/latest/reference/architecture.html) | Detailed description of Plugin structure, blueprint lifecycle, sandbox environment, and host-side state. |
| [Prerequisites](https://docs.nvidia.com/nemoclaw/latest/get-started/prerequisites.html) | Hardware, software, and supported platforms, with any platform-specific pre-setup. |
| [Inference Options](https://docs.nvidia.com/nemoclaw/latest/inference/inference-options.html) | Supported providers, validation, and routed inference configuration. |
| [Network Policies](https://docs.nvidia.com/nemoclaw/latest/reference/network-policies.html) | Baseline rules, operator approval flow, and egress control. |
| [Customize Network Policy](https://docs.nvidia.com/nemoclaw/latest/network-policy/customize-network-policy.html) | Static and dynamic policy changes, presets. |
| [Security Best Practices](https://docs.nvidia.com/nemoclaw/latest/security/best-practices.html) | Controls reference, risk framework, and posture profiles for sandbox security. |
| [Sandbox Hardening](https://docs.nvidia.com/nemoclaw/latest/manage-sandboxes/sandbox-hardening.html) | Container security measures, capability drops, process limits. |
| [CLI Commands](https://docs.nvidia.com/nemoclaw/latest/reference/commands.html) | Full NemoClaw CLI command reference. |
| [Troubleshooting](https://docs.nvidia.com/nemoclaw/latest/reference/troubleshooting.html) | Common issues and resolution steps. |

Community
---------

Join the NemoClaw community to ask questions, share feedback, and report issues.
NemoClaw is an alpha project, so maintainers review issues, discussions, and pull requests on a best effort basis without guaranteed response timelines.

We welcome contributions. See [CONTRIBUTING.md](https://github.com/NVIDIA/NemoClaw/blob/main/CONTRIBUTING.md) for development setup, coding standards, and the PR process.

NVIDIA takes security seriously.
If you discover a vulnerability in NemoClaw, **DO NOT open a public issue.**
Use one of the private reporting channels described in [SECURITY.md](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md):

For security bulletins and PSIRT policies, visit the [NVIDIA Product Security](https://www.nvidia.com/en-us/security/) portal.

NemoClaw's current priorities are maintained here as a public orientation point for contributors and community members.
This list is not a delivery commitment, support promise, or fixed roadmap; priorities can change as maintainers respond to security, quality, platform readiness, and community feedback.

* Improve install and onboarding reliability across tested platforms.
* Strengthen sandbox hardening, credential handling, and network-policy defaults.
* Validate local and routed inference behavior for supported provider paths.
* Keep documentation, troubleshooting guidance, and agent skills aligned with supported workflows.

For specific scoped work, use [GitHub Issues](https://github.com/NVIDIA/NemoClaw/issues) and start broader proposals in [GitHub Discussions](https://github.com/NVIDIA/NemoClaw/discussions).
Security vulnerabilities must use the private reporting channels in [SECURITY.md](https://github.com/NVIDIA/NemoClaw/blob/main/SECURITY.md), not public issues.

This software automatically retrieves, accesses or interacts with external materials. Those retrieved materials are not distributed with this software and are governed solely by separate terms, conditions and licenses. You are solely responsible for finding, reviewing and complying with all applicable terms, conditions, and licenses, and for verifying the security, integrity and suitability of any retrieved materials for your specific use case. This software is provided "AS IS", without warranty of any kind. The author makes no representations or warranties regarding any retrieved materials, and assumes no liability for any losses, damages, liabilities or legal consequences from your use or inability to use this software or any retrieved materials. Use this software and the retrieved materials at your own risk.

Apache 2.0. See [LICENSE](https://github.com/NVIDIA/NemoClaw/blob/main/LICENSE).