---
title: "AI assistance when contributing to the Linux kernel"
url: https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst
clipped: 2026-06-17 01:19:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AI assistance when contributing to the Linux kernel](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

## Digest Summary
The document outlines how AI tools may assist in Linux kernel development while adhering to existing processes and licensing rules. Contributions must follow the standard kernel development workflow, including the development‑process, coding‑style, and patch‑submission guidelines. All code must be GPL‑2.0‑only compatible and use proper SPDX identifiers, as detailed in the license‑rules documentation. AI agents are prohibited from adding “Signed‑off‑by” tags; only human submitters can certify the Developer Certificate of Origin (DCO) and must review any AI‑generated code, ensure licensing compliance, add their own Signed‑off‑by, and assume full responsibility. When AI assistance is used, an “Assisted‑by” tag should be added, formatted as Assisted‑by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2], where optional tools may include analysis utilities such as coccinelle, sparse, smatch, or clang‑tidy. Basic development tools are excluded from this tag.

## Discussion Summary
The comments acknowledge the policy’s intent to keep human contributors legally responsible for AI‑generated code, viewing it as a sensible, common‑sense approach. However, many express doubts about practical enforceability, especially regarding GPL compliance and detecting license violations in model‑produced output. Several contributors worry that the rule may shift liability without effectively preventing infringement, and some view the reliance on AI as a threat to open‑source integrity. Overall, the discussion balances acceptance of responsibility with significant skepticism about feasibility and potential risks.

---

## Full Article

This document provides guidance for AI tools and developers using AI
assistance when contributing to the Linux kernel.

AI tools helping with Linux kernel development should follow the standard
kernel development process:

* Documentation/process/development-process.rst
* Documentation/process/coding-style.rst
* Documentation/process/submitting-patches.rst

Licensing and Legal Requirements
--------------------------------

All contributions must comply with the kernel's licensing requirements:

* All code must be compatible with GPL-2.0-only
* Use appropriate SPDX license identifiers
* See Documentation/process/license-rules.rst for details

Signed-off-by and Developer Certificate of Origin
-------------------------------------------------

AI agents MUST NOT add Signed-off-by tags. Only humans can legally
certify the Developer Certificate of Origin (DCO). The human submitter
is responsible for:

* Reviewing all AI-generated code
* Ensuring compliance with licensing requirements
* Adding their own Signed-off-by tag to certify the DCO
* Taking full responsibility for the contribution

When AI tools contribute to kernel development, proper attribution
helps track the evolving role of AI in the development process.
Contributions should include an Assisted-by tag in the following format:

```
Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]
```

Where:

* `AGENT_NAME` is the name of the AI tool or framework
* `MODEL_VERSION` is the specific model version used
* `[TOOL1] [TOOL2]` are optional specialized analysis tools used
  (e.g., coccinelle, sparse, smatch, clang-tidy)

Basic development tools (git, gcc, make, editors) should not be listed.

Example:

```
Assisted-by: Claude:claude-3-opus coccinelle sparse
```