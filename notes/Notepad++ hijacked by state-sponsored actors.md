---
title: "Notepad++ hijacked by state-sponsored actors"
url: https://notepad-plus-plus.org/news/hijacked-incident-info-update/
clipped: 2026-06-17 01:49:36
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Notepad++ hijacked by state-sponsored actors](https://notepad-plus-plus.org/news/hijacked-incident-info-update/)

## Digest Summary
None

## Discussion Summary
The comments express strong concern about the Notepad++ supply‑chain incident, focusing on unclear targeting criteria, the extent of compromise, and how users can verify whether their installations were affected. Many request concrete mitigation steps, signature verification, and details about the hosting provider, while drawing parallels to similar past attacks on other open‑source tools. Skepticism appears toward the limited information provided and toward political framing of the threat, with overall sentiment centered on caution and a desire for clearer technical guidance.

---

## Full Article

Notepad++ Hijacked by State-Sponsored Hackers
=============================================

2026-02-02

Following the security disclosure published in the v8.8.9 announcement  
<https://notepad-plus-plus.org/news/v889-released/>  
the investigation has continued in collaboration with external experts and with the full involvement of my (now former) shared hosting provider.

According to the analysis provided by the security experts, the attack involved infrastructure-level compromise that allowed malicious actors to intercept and redirect update traffic destined for notepad-plus-plus.org. The exact technical mechanism remains under investigation, though the compromise occurred at the hosting provider level rather than through vulnerabilities in Notepad++ code itself. Traffic from certain targeted users was selectively redirected to attacker-controlled malicious update manifests.

The incident began in June 2025. Multiple independent security researchers have assessed that the threat actor is likely a Chinese state-sponsored group, which would explain the highly selective targeting observed during the campaign.

An incident-response (IR) plan was proposed by the security expert, and I facilitated direct communication between the hosting provider and the IR team. After the IR team engaged with the provider and reviewed the situation, I received the following detailed statement from the provider:

```
Dear Customer,
We want to further update you following the previous communication with us about your server compromise and further investigation with your incident response team.
We discovered the suspicious events in our logs, which indicate that the server (where your application https://notepad-plus-plus.org/update/getDownloadUrl.php was hosted until the 1st of December, 2025) could have been compromised.
As a precautionary measure, we immediately transferred all clientsâ web hosting subscriptions from this server to a new server and continued our further investigation.
Here are the key finding points:
1. The shared hosting server in question was compromised until the 2nd of September, 2025. On this particular date, the server had scheduled maintenance where the kernel and firmware were updated. After this date, we could not identify any similar patterns in logs, and this indicates that bad actors have lost access to the server. We also find no evidence of similar patterns on any other shared hosting servers.
2. Even though the bad actors have lost access to the server from the 2nd of September, 2025, they maintained the credentials of our internal services existing on that server until the 2nd of December, which could have allowed the malicious actors to redirect some of the traffic going to https://notepad-plus-plus.org/getDownloadUrl.php to their own servers and return the updates download URL with compromised updates.
3. Based on our logs, we see no other clients hosted on this particular server being targeted. The bad actors specifically searched for https://notepad-plus-plus.org/ domain with the goal to intercept the traffic to your website, as they might know the then-existing Notepad++ vulnerabilities related to insufficient update verification controls.
4. After concluding our research, the investigated security findings were no longer observed in the web hosting systems from the 2nd of December, 2025, and onwards, as:
* We have fixed vulnerabilities, which could have been used to target Notepad++. In particular, we do have logs indicating that the bad actor tried to re-exploit one of the fixed vulnerabilities; however, the attempt did not succeed after the fix was implemented.
* We have rotated all the credentials that bad actors could have obtained until the 2nd of September, 2025.
* We have checked the logs for similar patterns in all web hosting servers and couldnât find any evidence of systems being compromised, exploited in a similar way, or data breached.
While we have rotated all the secrets on our end, below you will find the preventive actions you should take to maximize your security. However, if below actions have been done after the 2nd of December, 2025, no actions are needed from your side.
* Change credentials for SSH, FTP/SFTP, and MySQL database.
* Review administrator accounts for your WordPress sites (if you have any), change their passwords, and remove unnecessary users.
* Update your WordPress sites (if you have any) plugins, themes, and core version, and turn on automatic updates, if applicable.
We appreciate your cooperation and understanding. Please let us know in case you have any questions.
```

**TL;DR**  
According to the former hosting provider, the shared hosting server was compromised until September 2, 2025. Even after losing server access, attackers maintained credentials to internal services until December 2, 2025, which allowed them to continue redirecting Notepad++ update traffic to malicious servers. The attackers specifically targeted the Notepad++ domain with the goal of exploiting insufficient update verification controls that existed in older versions of Notepad++.
All remediation and security hardening was completed by the provider by December 2, 2025, successfully blocking further attacker activity.

**Note on timelines:** The security expert’s analysis indicates the attack ceased on November 10, 2025, while the hosting provider’s statement shows potential attacker access until December 2, 2025. Based on both assessments, I estimate the overall compromise period spanned from June through December 2, 2025, when all attacker access was definitively terminated.

To address this severe security issue, the Notepad++ website has been migrated to a new hosting provider with significantly stronger security practices.  
Within Notepad++ itself, WinGup (the updater) was enhanced in v8.8.9 to verify both the certificate and the signature of the downloaded installer. Additionally, the XML returned by the update server is now signed (XMLDSig), and the certificate & signature verification will be enforced starting with upcoming v8.9.2, expected in about one month.

I deeply apologize to all users affected by this hijacking. **I recommend [downloading v8.9.1](https://notepad-plus-plus.org/downloads/v8.9.1/) (which includes the relevant security enhancement) and running the installer to update your Notepad++ manually.**

With these changes and reinforcements, I believe the situation has been fully resolved.
Fingers crossed.

---

***Edit (February 2, 2026):*** *I’ve got a lot of emails requesting the IoC (Indicator of Compromise). I unfortunately do not have any IoCs to share. Our IR team spent a week analyzing roughly 400â¯GB of server logs provided by the former hosting provider. While signs of an intrusion were identified, no concrete indicators of compromise - such as binary hashes, domains, or IP addresses - were found. We also requested IoCs directly from the former hosting provider, but we were not able to obtain any.*

---

***Edit 2 (February 3, 2026 minight):*** *Last evening I received an email from Ivan Feigl (Rapid7) to share their excellent [investigation story](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/) - it seems to be the same story, and obviously, they have more tangible information (including IoCs) than I do.*

---

***Edit 3 (February 3, 2026 7:55 PM):*** *More technical information & IoCs from Kaspersky: <https://securelist.com/notepad-supply-chain-attack/118708/>*

---

***Edit 4 (February 5, 2026 4:12 AM):*** *IoCs provided by our former hosting provider: please check: [Important Clarification: Notepad++ Security Incident](https://notepad-plus-plus.org/news/clarification-security-incident)*