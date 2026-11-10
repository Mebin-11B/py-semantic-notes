---
title: "Releasing rainbow tables to accelerate Net-NTLMv1 protocol deprecation"
url: https://cloud.google.com/blog/topics/threat-intelligence/net-ntlmv1-deprecation-rainbow-tables
clipped: 2026-06-17 01:57:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Releasing rainbow tables to accelerate Net-NTLMv1 protocol deprecation](https://cloud.google.com/blog/topics/threat-intelligence/net-ntlmv1-deprecation-rainbow-tables)

## Digest Summary
Mandiant is publishing a full set of Net‑NTLMv1 rainbow tables to demonstrate the protocol’s continued insecurity and to accelerate its deprecation. Net‑NTLMv1, known to be vulnerable since at least 1999 and publicly deprecated, still appears in active environments, allowing trivial credential theft and privilege escalation via authentication‑coercion attacks (e.g., recovering a domain‑controller machine‑account hash to obtain DCSync rights).  

The tables are stored in Google Cloud Storage (gs://net‑ntlmv1‑tables/tables) and can be downloaded with gsutil; SHA‑512 checksums are provided for verification. They are usable with traditional rainbow‑table tools such as rainbowcrack, RainbowCrack‑NG, or GPU‑accelerated forks after preprocessing Net‑NTLMv1 hashes to DES components via ntlmv1‑multi.  

Attackers typically capture Net‑NTLMv1 hashes using tools like Responder (‑‑lm ‑‑disable‑ess) with a static challenge (1122334455667788) and then coerce authentication from privileged hosts. The released dataset enables key recovery in under 12 hours on consumer hardware (~$600). The post emphasizes disabling Net‑NTLMv1 and Extended Session Security to prevent these attacks.

## Discussion Summary
The comments criticize NTLM as an outdated and insecure protocol, noting that its continued use in legacy systems, government environments, and old network equipment creates unnecessary risk. Contributors point out that the weaknesses have been known for years, requiring workarounds such as adding deprecated cryptographic algorithms, and that modern attackers can exploit them with modest resources. While some acknowledge the limited novelty of new exploits, the overall view is that reliance on NTLM reflects neglect of proper security updates and a failure to retire obsolete technology.

---

## Full Article

### Introduction

Mandiant is [publicly releasing](https://research.google/resources/datasets/?dataset_types=other&search=Net-NTLMv1&) a comprehensive dataset of Net-NTLMv1 rainbow tables to underscore the urgency of migrating away from this outdated protocol. Despite Net-NTLMv1 being deprecated and known to be insecure for over two decades—with cryptanalysis dating back to 1999—Mandiant consultants continue to identify its use in active environments. This legacy protocol leaves organizations vulnerable to trivial credential theft, yet it remains prevalent due to inertia and a lack of demonstrated immediate risk.

By releasing these tables, Mandiant aims to lower the barrier for security professionals to demonstrate the insecurity of Net-NTLMv1. While tools to exploit this protocol have existed for years, they often required uploading sensitive data to third-party services or expensive hardware to brute-force keys. The release of this dataset allows defenders and researchers to recover keys in under 12 hours using consumer hardware costing less than $600 USD. This initiative highlights the amplified impact of combining Mandiant's frontline expertise with Google Cloud's resources to eliminate entire classes of attacks.

This post details the generation of the tables, provides access to the dataset for community use, and outlines critical remediation steps to disable Net-NTLMv1 and prevent authentication coercion attacks.

### Background

Net-NTLMv1 has been widely known to be insecure since at least 2012, following presentations at DEFCON 20, with cryptanalysis of the underlying protocol [dating back to at least 1999](https://www.schneier.com/academic/archives/1999/09/cryptanalysis_of_mic_1.html). On Aug. 30, 2016, Hashcat [added support](https://github.com/hashcat/hashcat/commit/71a8459d851d246945343ea59effa1d46b965bf8) for cracking Data Encryption Standard (DES) keys using known plaintext, further democratizing the ability to attack this protocol. Rainbow tables are almost as old, with the initial paper on rainbow tables published in [2003 by Philippe Oechslin](https://infoscience.epfl.ch/record/99512/files/Oech03.pdf), citing an earlier iteration of a time-memory trade-off from [1980 by Martin Hellman](http://www-ee.stanford.edu/~hellman/publications/36.pdf).

Essentially, if an attacker can obtain a Net-NTLMv1 hash without Extended Session Security (ESS) for the known plaintext of `1122334455667788`, a cryptographic attack, referred to as a known plaintext attack (KPA), can be applied. This guarantees recovery of the key material used. Since the key material is the password hash of the authenticating Active Directory (AD) object—user or computer—the attack results can quickly be used to compromise the object, often leading to privilege escalation.

A common chain attackers use is authentication coercion from a highly privileged object, such as a domain controller (DC). Recovering the password hash of the DC machine account allows for DCSync privileges to compromise any other account in AD.

### Dataset Release

The unsorted dataset can be downloaded using `gsutil -m cp -r gs://net-ntlmv1-tables/tables .` or through the [Google Cloud Research Dataset portal](https://research.google/resources/datasets/?dataset_types=other&search=Net-NTLMv1&). 

The SHA512 hashes of the tables can be checked by first downloading the checksums `gsutil -m cp gs://net-ntlmv1-tables/tables.sha512 .` then checked by `sha512sum -c tables.sha512`. The password cracking community has already created derivative work and is also hosting the ready to use tables.

### Use of the Tables

Once a Net-NTLMv1 hash has been obtained, the tables can be used with historical or modern reinventions of rainbow table searching software such as [rainbowcrack (rcrack)](https://www.kali.org/tools/rainbowcrack/), or [RainbowCrack-NG](https://github.com/inAudible-NG/RainbowCrack-NG) on central processing units (CPUs) or a [fork](https://github.com/blurbdust/rainbowcrackalack) of [rainbowcrackalack](https://github.com/jtesta/rainbowcrackalack) on graphics processing units (GPUs). The Net-NTLMv1 hash needs to be preprocessed to the DES components using [ntlmv1-multi](https://github.com/evilmog/ntlmv1-multi) as shown in the next section.

### Obtaining a Net-NTLMv1 Hash

Most attackers will use [Responder](https://github.com/lgandx/Responder) with the `--lm` and `--disable-ess` flags and set the authentication to a static value of `1122334455667788` to only allow for connections with Net-NTLMv1 as a possibility. Attackers can then wait for incoming connections or coerce authentication using a tool such as [PetitPotam](https://github.com/topotam/PetitPotam) or [DFSCoerce](https://github.com/Wh04m1001/DFSCoerce) to generate incoming connections from DCs or lower privilege hosts that are useful for objective completion. Responses can be cracked to retrieve password hashes of either users or computer machine accounts. A sample workflow for an attacker is shown below in Figure 1, Figure 2, and Figure 3.