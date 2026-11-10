---
title: "The RCE that AMD won't fix"
url: https://mrbruh.com/amd/
clipped: 2026-06-17 01:48:20
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The RCE that AMD won't fix](https://mrbruh.com/amd/)

## Digest Summary
The author discovered a Remote Code Execution (RCE) issue in AMD’s AutoUpdate utility. The software’s `app.config` stores the update endpoint using a development URL but serves the actual executable download links over HTTP rather than HTTPS. Because the client fetches these binaries without any signature or certificate verification, a network attacker (e.g., via MITM or ISP-level access) can replace the downloaded files with malicious payloads, which the updater executes immediately. The vulnerability was identified on 27 January 2026, reported to AMD on 5 February 2026, and closed the same day as “out of scope”/won’t fix. The author published a blog post on 6 February 2026 documenting the findings. No remediation or patch from AMD is indicated.

## Discussion Summary
The comments express strong concern about the AMD AutoUpdate mechanism, emphasizing that its use of plain‑HTTP URLs creates a clear opportunity for man‑in‑the‑middle attacks and that widespread deployment could make many systems vulnerable if DNS or network settings are compromised. Participants contrast this with Linux distributions, which they view as more securely handling drivers without such update software. While some acknowledge that exploitation requires additional network compromise, the overall tone is critical of AMD’s security practices and the decision to deem the issue out‑of‑scope.

---

## Full Article

The RCE that AMD won’t fix
==========================

**NOTE: THIS ARTICLE IS OUT OF DATE, PLEASE READ THE UPDATED VERSION [HERE!](https://mrbruh.com/amd2)**

After being interrupted multiple times by an annoying console window that would pop up periodically on my new gaming PC, I managed to track the offending executable down to AMD’s AutoUpdate software.

In my anger, I decided to punish this software by decompiling it to figure out how it worked, and accidentally discovered a trivial Remote Code Execution (RCE) vulnerability in the process.

The first thing I found, is that they store their update URL in the program’s `app.config`, although its a little odd that they use their “Develpment” URL in production, it uses HTTPS so its perfectly safe.

![amd_appconfig.avif](https://mrbruh.com/amd/amd_appconfig.avif)

The real problem starts when you open up this URL in your web browser, and realise that all of the executable download URL’s are using HTTP.

![amd_updatexml.avif](https://mrbruh.com/amd/amd_updatexml.avif)

This means that a malicious attacker on your network, or a nation state that has access to your ISP can easily perform a MITM attack and replace the network response with any malicious executable of their choosing.

I was hoping that AMD perhaps had some form of certificate validation to ensure that it could not download & run any unsigned executables, however a quick look into the decompiled code revealed that the AutoUpdate software does no such validation and immediately executes the downloaded file.

![amd_installupdates.avif](https://mrbruh.com/amd/amd_installupdates.avif)

After finding this issue, I thought it was worth reporting to AMD since it seemed to be a pretty severe issue.

![amd_disclosure.avif](https://mrbruh.com/amd/amd_disclosure.avif)

However it turned out to be considered “out of scope”, resulting in AMD not considering this to be a vulnerability.

Timeline (DD/MM/YYYY)
---------------------

* 27/01/2026 - Vulnerability Discovered
* 05/02/2026 - Vulnerability Reported
* 05/02/2026 - Report Closed as `wont fix/out of scope`
* 06/02/2026 - Blog published

**If you liked this blog, you can read another of my write-ups here: [1.4 Billion exposed user records via insecure Firebase instances in top Android apps](https://mrbruh.com/firewreck2)**