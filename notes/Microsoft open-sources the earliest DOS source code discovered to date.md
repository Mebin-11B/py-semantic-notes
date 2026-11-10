---
title: "Microsoft open-sources \"the earliest DOS source code discovered to date\""
url: https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/
clipped: 2026-06-17 00:58:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - operating system history
  - MS-DOS
  - open source software
  - digital preservation
  - retrocomputing
related:
  - "[[Operating System History]]"
  - "[[Before GitHub]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Microsoft has open-sourced the 86-DOS 1.00 kernel (originally QDOS) and early PC-DOS 1.00 snapshots, offering a historic look at the precursor to MS-DOS.
>
> **Key points:**
> - The release includes the source code for the 86-DOS 1.00 kernel, Seattle Computer Products' development snapshots of PC-DOS 1.00, and early utilities like CHKDSK.
> - Written by Tim Paterson, 86-DOS (originally QDOS) was licensed and eventually acquired by Microsoft to meet IBM's OS requirements for the IBM PC 5150.
> - This software laid the foundation for MS-DOS, which dominated the personal computing market throughout the 1980s and 1990s via IBM PC clones.
> - Hacker News discussion highlights the value of transcribing paper-based source archives, nostalgia for low-level assembly optimization, and interest in future digital preservation releases from Microsoft's catalog.
>
> **Concept links:** [[Operating System History]], [[MS-DOS]], [[Open Source Software]], [[Digital Preservation]], [[Seattle Computer Products]], [[Retrocomputing]], [[Assembly Language]]
>
> **Suggested connections:**
> - [[Operating System History]] — tracing the development of foundational operating systems and the early software industry.
> - [[Before GitHub]] — examining how software was distributed, collaborated on, and archived before modern version control networks.
<!-- ai-summary:end -->

# [Microsoft open-sources "the earliest DOS source code discovered to date"](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/)

## Digest Summary
Microsoft has open‑sourced the earliest DOS source code discovered, predating the MS‑DOS brand. The release contains the complete source for the 86‑DOS 1.00 kernel (originally QDOS, written by Tim Paterson for Seattle Computer Products), several development snapshots of the PC‑DOS 1.00 kernel, and source for utilities such as CHKDSK. Historically, Microsoft licensed 86‑DOS to supply an operating system for the IBM PC 5150, hired Paterson to continue its development, and later acquired full rights. Microsoft then licensed the OS to IBM as PC‑DOS while marketing the same code as MS‑DOS, which became dominant through the 1980s‑1990s on IBM PC clones. The newly released code provides a rare view into the initial implementation of the operating system that underpinned early personal computers.

## Discussion Summary
The comments express appreciation for Microsoft’s release of historic BASIC and DOS source code, noting its significance for preserving early computing history and acknowledging the effort required to transcribe the material from paper. There is optimism that similar releases could eventually include early Windows versions, alongside curiosity about potential security research. Several remarks convey nostalgia for the era of hand‑written, highly optimized software and critique contemporary reliance on layers of libraries and virtualization, while some view the release as valuable yet belated.

---

## Full Article

Several times in the last couple of decades, Microsoft has released source code for the original MS-DOS operating system that kicked off its decades-long dominance of consumer PCs. This week, the company has [reached further back than ever](https://opensource.microsoft.com/blog/2026/04/28/continuing-the-story-of-early-dos-development/), releasing “the earliest DOS source code discovered to date” along with other documentation and notes from its developer.

Today’s source release is so old that it predates the MS-DOS branding, and it includes “sources to the 86-DOS 1.00 kernel, several development snapshots of the PC-DOS 1.00 kernel, and some well-known utilities such as `CHKDSK`,” write Microsoft’s Stacey Haffner and Scott Hanselman in their co-authored post about the release.

To understand the context, here’s a very brief history of what would become MS-DOS: Programmer Tim Paterson originally created 86-DOS (previously known as QDOS, for “quick and dirty operating system”) for an Intel 8086-based computer kit sold by Seattle Computer Products. Microsoft, on the hook to provide an operating system for [the still-in-development IBM PC 5150](https://arstechnica.com/gadgets/2017/06/ibm-pc-history-part-1/), licensed 86-DOS and hired Paterson to continue developing it, later buying the rights to 86-DOS outright. Microsoft then licensed this operating system to IBM as PC-DOS while retaining the ability to sell the operating system to other companies. The version sold by Microsoft was called MS-DOS, and the proliferation of third-party IBM PC clones over the ’80s and ’90s made it the version of the operating system that most people ended up using.