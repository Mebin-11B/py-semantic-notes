---
title: "Azure Linux 4.0 is Microsoft's first general-purpose Linux"
url: https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/
clipped: 2026-06-17 00:52:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - linux distributions
  - fedora os
  - cloud computing
  - azure linux
  - supply chain security
  - cbl-mariner
related:
  - "[[Linux Distributions]]"
  - "[[Azure Linux]]"
  - "[[Supply Chain Security]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An analysis of Microsoft's release of Azure Linux 4.0, which transitions its container-focused CBL-Mariner distro into a Fedora-derived general-purpose Linux operating system.
>
> **Key points:**
> - Azure Linux 4.0, announced at Build 2026, is now available for general virtual machine deployments, moving past its previous role as an internal AKS-appliance.
> - The OS is now derived from a Fedora 43 snapshot with tracked overlay files detailing all modifications, changing the package manager to dnf5.
> - Core specifications include an Azure-hardened Linux 6.18 LTS kernel, glibc 2.42, systemd 258, OpenSSL 3.5, and RPM 6.0 with FIPS 140-3 in progress.
> - Major corporate infrastructures (e.g., Databricks, LinkedIn) have completed migrations to the OS, which emphasizes minimal container bases and SBOM auditable supply chains.
>
> **Concept links:** [[Linux Distributions]], [[Fedora OS]], [[Cloud Computing]], [[Azure Linux]], [[Supply Chain Security]], [[CBL-Mariner]]
>
> **Suggested connections:**
> - [[Linux Distributions]] — The open-source ecosystem that Microsoft has officially joined as a developer.
> - [[Azure Linux]] — The specific OS engineered for Azure hardware and AKS host runtimes.
> - [[Supply Chain Security]] — The mechanisms (SBOMs, signed packages, transparent spec overlays) used to guarantee package integrity.
<!-- ai-summary:end -->


# [Azure Linux 4.0 is Microsoft's first general-purpose Linux](https://www.boxofcables.dev/azure-linux-4-0-is-microsofts-first-general-purpose-linux/)

## Digest Summary
Azure Linux 4.0, announced at Build 2026, is Microsoft’s first general‑purpose Linux distribution, now available for any Azure VM via the Marketplace. Built from a Fedora 43 snapshot, it replaces the hand‑crafted package set of earlier releases with declarative overlays that document every deviation from upstream. Key components include an Azure‑tuned Linux 6.18 LTS kernel with Hyper‑V, GPU and AI‑accelerator support, dnf5 (replacing the custom tdnf), glibc 2.42, systemd 258, OpenSSL 3.5 (with post‑quantum extensions), Python 3.14, and RPM 6.0 with enhanced signature verification; FIPS 140‑3 certification is pending. Security defaults enable SELinux, ASLR, stack protection, seccomp, and systemd sandboxing, and all packages are cryptographically signed with published SBOMs. Azure Linux ships minimal server‑only images and distroless container bases, and is deployable as VMs, scale‑sets, AKS hosts, and via WSL. Major customers (Databricks, LinkedIn) have migrated large workloads. Its upstream‑first, auditable supply‑chain distinguishes it from other cloud‑focused distros.

## Discussion Summary
The comments convey mixed reactions to Microsoft’s Azure‑focused Linux distribution. Many note that it is specifically tuned for Azure hardware and question its relevance beyond that environment, viewing it as a niche rather than a broadly useful OS. Some appreciate its RPM base and see it as a logical continuation of Microsoft’s Linux efforts, while others criticize the marketing emphasis on AI and express concern that Microsoft may not support broader open‑source projects. Overall, the consensus is cautious acknowledgment of the release’s limited scope.

---

## Full Article

Microsoft shipped Azure Linux 4.0 into [public preview](https://techcommunity.microsoft.com/blog/linuxandopensourceblog/announcing-azure-linux-4-0-purpose-built-for-azure-now-in-public-preview/4524267) at Build 2026, and for the first time you can run it on any Azure virtual machine, not just as the host underneath Azure Kubernetes Service. That sounds like a small distinction. But, this is the moment Microsoft's in-house Linux stops being a special-purpose appliance distro and becomes a general-purpose Linux distro.

I have been following this distribution since before it had a marketing name. So let me put 4.0 in context...

Photos from the Azure Linux 4 session at Microsoft Build 2026

What I keep on about
--------------------

Microsoft has built more than one Linux distribution. Back in February 2022 I went looking through Microsoft's package mirrors and found [CBL-Delridge](https://www.boxofcables.dev/building-cbl-d-microsofts-other-linux-distro/), a Debian-based distro that powered Azure Cloud Shell. It was never announced. [Mary Jo Foley wrote it up at ZDNet](https://www.zdnet.com/article/surprise-theres-yet-another-microsoft-linux-distro-cbl-delridge/) after reading that post. By November 2022, Delridge was [404](https://www.boxofcables.dev/cbl-delridge-is-dead-long-live-cbl-mariner/): its apt repository went dark and Cloud Shell moved to Microsoft's other Linux: CBL-Mariner.

CBL stands for Common Base Linux, a whole family of internal distros named after Seattle geography. Delridge was the Debian one. Mariner was an RPM one, built from scratch with spec files borrowed from [Photon OS](https://vmware.github.io/photon/), Fedora, and [Linux From Scratch](https://www.linuxfromscratch.org/). Mariner is the one that survived. In [March 2024 Microsoft renamed it Azure Linux](https://www.phoronix.com/news/Microsoft-Azure-Linux) and renamed the [GitHub repository](https://github.com/microsoft/azurelinux) to match.

So when I say Azure Linux, I mean the distribution that started internal development in September 2019, went public on GitHub in November 2020, hit 2.0 in April 2022, and has been the container host for AKS since 2023. None of that history was aimed at you running it on your own VM.

That is what changes now.

What is actually new in 4.0
---------------------------

Azure Linux 4.0 is [derived from Fedora](https://en.wikipedia.org/wiki/Azure_Linux), right now a Fedora 43 snapshot, rather than assembled package by package the way 1.0 through 3.0 were. Microsoft no longer maintains every spec file by hand. Instead it tracks Fedora upstream and applies declarative overlays, where every deviation from Fedora carries a written description of why it exists. The rendered spec files are checked into the [repository](https://github.com/microsoft/azurelinux) so you can read exactly what Microsoft changed and why.

The component stack moved up accordingly:

* **Kernel 6.18 LTS**, Azure-tuned, with the Hyper-V integration and GPU and AI accelerator support you would expect from an Azure cloud kernel. Microsoft maintains its own [kernel fork](https://github.com/microsoft/azurelinux/tree/3.0/SPECS/kernel) and embeds its signing keys directly in the build.
* **dnf5** replaces `tdnf`, Microsoft's lean C reimplementation of dnf inherited from Photon OS. This is the single most user-visible change. You now get standard [dnf5](https://dnf5.readthedocs.io/) tooling and the full plugin ecosystem instead of a Microsoft-specific package manager.
* **glibc 2.42**, **systemd 258**, **OpenSSL 3.5** (with post-quantum cryptography support), **Python 3.14**, and **RPM 6.0** with a modernized database backend and stronger signature verification.
* **FIPS 140-3** certification is in progress and slated for general availability.

Security is solid. SELinux is supported on every image, the kernel ships with hardening turned on (ASLR, stack protection, seccomp, and systemd service sandboxing), packages and repositories are cryptographically signed, and Microsoft [publishes SBOMs](https://github.com/microsoft/azurelinux) for the supply chain.

Why this is the next step
-------------------------

Here is the part that matters. For most of its life, Azure Linux was infrastructure you ran on without knowing it. It was the host OS for AKS nodes, the base image for Microsoft's own first-party services, the system distro that hosts [WSLg](https://github.com/microsoft/wslg). You did not pick it. It was underneath the thing you picked.

Azure Linux 4.0 is built to be picked. It runs across every Azure compute surface:

* **Virtual machines and scale sets**, deployable straight from the [Azure Marketplace](https://aka.ms/AzureLinuxProduct) with no additional OS licensing cost.
* **Containers**, with base, distroless, and language-runtime images on the [Microsoft Container Registry](https://mcr.microsoft.com/), built from the same supply chain as the VM images.
* **AKS**, where it has been the container host since 2023, now joined by Azure Container Linux, a Flatcar-based immutable variant that shares the same kernel for stricter compliance environments.
* **WSL**, so you can develop locally on the same Linux you deploy to production with `wsl --install -d AzureLinux` **(soon, go try it on Azure first)**.

Databricks migrated more than 100,000 VMs and over a million CPU cores to Azure Linux. LinkedIn moved its infrastructure to Azure Linux. Azure Linux already runs behind AKS, Azure SQL, and Cosmos DB. The 4.0 preview takes that and gives it to everyone else.

What makes Azure Linux different
--------------------------------

There are a lot of cloud Linux distributions. Amazon has Amazon Linux. The Flatcar and CoreOS lineage offers immutable container hosts. Ubuntu and RHEL run nearly everywhere. So what is distinct here?

A few things stand out:

* **The supply chain is auditable by design.** Building on Fedora with declarative overlays means every change from upstream is documented in the repository. That is a stronger story than most distributions can tell about what is in their packages and why.
* **It is minimal on purpose.** Azure Linux ships only what cloud and server workloads need. There is no desktop, no GUI, no general-purpose sprawl. The [distroless container images](https://mcr.microsoft.com/) take this to its logical end: no shell, no package manager, almost nothing to exploit.
* **Microsoft made a Linux distro.**

What it means for Linux
-----------------------

I have [tracked Microsoft's open source arc for years](https://www.boxofcables.dev/microsoft-and-open-source-an-unofficial-timeline/). The short version: Azure started hosting Linux VMs in 2012, Satya Nadella said "Microsoft loves Linux" in 2014, Microsoft joined the Linux Foundation in 2016, shipped WSL the same year, cross-licensed 60,000 patents through the Open Invention Network in 2018, and by 2019 Linux was the majority operating system on Azure. Today more than two-thirds of customer cores on Azure run Linux.

Against that backdrop, a general-purpose Azure Linux is the logical next step. Microsoft went from consuming Linux, to shipping Linux internally, to shipping a Linux distribution anyone can run.

Another major vendor maintaining a distribution upstream-first against Fedora, contributing patches, and putting real money into supply-chain security work through OpenSSF and Alpha-Omega. More maintained distributions, built in the open, is good for everyone downstream.

From an undocumented Debian remix I had to reverse-engineer from a package mirror, to a Fedora-derived, FIPS-targeted, distroless-capable distribution you can deploy from a marketplace in two clicks. That is a long way in four years.

Microsoft ships Linux.