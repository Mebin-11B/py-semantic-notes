---
title: "AWS Adds support for nested virtualization"
url: https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e
clipped: 2026-06-17 01:46:17
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AWS
  - Nested Virtualization
  - Intel Xeon 6
  - R8i Instances
  - Micro-VMs
  - Firecracker
related:
  - "[[Claude Platform on AWS]]"
  - "[[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** AWS introduces R8i instances powered by custom Intel Xeon 6 processors with sustained 3.9 GHz turbo frequency, enabling nested virtualization support.
>
> **Key points:**
> - Release 2026-02-12 of `aws/aws-sdk-go-v2` introduces R8i instances with custom Intel Xeon 6 processors.
> - The processors run at a sustained all-core turbo frequency of 3.9 GHz and are exclusive to AWS.
> - Nested virtualization support allows running micro-VMs (like Firecracker) without requiring bare-metal instances, aligning AWS with GCP.
> - Enabling this feature disables Virtual Secure Mode (VSM) on the instances.
>
> **Concept links:** [[AWS]], [[Nested Virtualization]], [[Intel Xeon 6]], [[R8i Instances]], [[Micro-VMs]], [[Firecracker]]
>
> **Suggested connections:**
> - [[Claude Platform on AWS]] — related AWS cloud infrastructure.
> - [[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]] — related performance environments.
<!-- ai-summary:end -->

# [AWS Adds support for nested virtualization](https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e)

## Digest Summary
Release 2026‑02‑12 of the aws/aws‑sdk‑go‑v2 repository (commit 3dca5e4) announces a new hardware offering: R8i instances that use custom Intel Xeon 6 processors. These instances are exclusive to AWS and are specified to sustain an all‑core turbo frequency of 3.9 GHz. The release notes repeat this feature description, indicating its primary focus on the processor’s performance characteristics and AWS‑only availability. No additional technical details, code changes, or usage instructions are provided in the excerpt. An accompanying image is listed with the alt text “author,” but no further visual information is described.

## Discussion Summary
The comments express overall enthusiasm for AWS’s addition of nested virtualization, noting its significance for running micro‑VMs such as Firecracker without costly bare‑metal instances and aligning AWS with capabilities already available on GCP and other providers. Participants also discuss technical complexity, questioning kernel stability, performance overhead, and the impact on I/O‑bound workloads, while acknowledging that enabling the feature disables Virtual Secure Mode. There is interest in broader adoption across cloud services and curiosity about future extensions to security technologies like SEV‑SNP and TDX.

---

## Full Article

`* **Feature**: R8i instances powered by custom Intel Xeon 6 processors available only on AWS with sustained all-core 3.9 GHz turbo frequency` |