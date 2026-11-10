---
title: "Obsidian plugin was abused to deploy a remote access trojan"
url: https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/
clipped: 2026-06-17 01:04:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - obsidian security
  - social engineering
  - remote access trojan
  - blockchain c2
  - malware analysis
  - endpoint detection
related:
  - "[[Obsidian Security]]"
  - "[[Social Engineering]]"
  - "[[Remote Access Trojan]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A highly targeted social engineering campaign (REF6598) weaponizes shared Obsidian vaults and malicious community plugins to deploy the PHANTOMPULSE remote access Trojan.
>
> **Key points:**
> - The REF6598 campaign targets financial and cryptocurrency sectors on both Windows and macOS via LinkedIn and Telegram.
> - Attackers manipulate victims into opening a shared Obsidian vault and enabling malicious community plugins (Shell Commands, Hider) which execute loader scripts.
> - The loaders drop the PHANTOMPULSE RAT into memory to evade file-based detection, which then uses the Ethereum blockchain to resolve its C2 server IP address.
> - Mitigation strategies include restricting community plugins, disabling auto-sync on untrusted vaults, and monitoring for Obsidian spawning CLI child processes.
>
> **Concept links:** [[Obsidian Security]], [[Social Engineering]], [[Remote Access Trojan]], [[Blockchain C2]], [[Malware Analysis]], [[Endpoint Detection]]
>
> **Suggested connections:**
> - [[Obsidian Security]] — security risks, sandboxing concerns, and best practices within the Obsidian community plugin ecosystem.
> - [[Social Engineering]] — techniques used by threat actors to manipulate users into compromising their own systems.
> - [[Remote Access Trojan]] — malware designed to give attackers administrative control over a target system.
<!-- ai-summary:end -->


# [Obsidian plugin was abused to deploy a remote access trojan](https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/)

## Digest Summary
Security researchers identified campaign REF6598 that exploits the Obsidian note‑taking app to deliver the undocumented PHANTOMPULSE remote‑access Trojan (RAT) against financial and cryptocurrency targets on Windows and macOS. Attackers pose as venture capitalists on LinkedIn/Telegram, lure victims into a shared cloud‑hosted Obsidian vault, and persuade them to enable “Installed community plugins” synchronization. Malicious versions of legitimate plugins (Shell Commands, Hider) run a PowerShell script (Windows) or AppleScript (macOS) that drops a loader (PHANTOMPULL) which decrypts and memory‑loads the PHANTOMPULSE RAT, evading file‑based detection. The RAT uses a novel C2 method: it queries the Ethereum blockchain for a transaction from a hard‑coded wallet, extracting the C2 server IP from the transaction data. Capabilities include keylogging, screenshot capture, file exfiltration, and arbitrary command execution. Detection guidance: monitor Obsidian spawning powershell.exe, cmd.exe, osascript, or bash; watch for outbound connections to Ethereum nodes from non‑standard processes; and track creation/modification of files in the .obsidian/plugins directory. Mitigations include restricting community plugins, disabling auto‑sync for untrusted vaults, applying least‑privilege execution, and employing EDR/network monitoring.

## Discussion Summary
The discussion centers on concerns about Obsidian’s plugin security, emphasizing that the recent incident was a social‑engineering attack rather than a software vulnerability. Commenters express a desire for clearer permission prompts and sandboxing, while others trust the upcoming security updates and remain confident in the platform. Skepticism persists regarding the maturity of the plugin framework, with opinions ranging from preferring a plugin‑free experience to fearing enterprise‑level risks, and calls for better review processes and safeguards.

---

## Full Article

Executive Summary
-----------------

Security researchers have identified a highly targeted social engineering campaign (REF6598) that weaponizes the **[Obsidian](https://obsidian.md/)** note-taking application to deliver a previously undocumented Remote Access Trojan (RAT) named **PHANTOMPULSE**. The campaign targets individuals in the financial and cryptocurrency sectors on both Windows and macOS. Attackers use platforms like LinkedIn and Telegram to build trust before luring victims into a malicious shared Obsidian vault. The attack chain relies on tricking the user into enabling a community plugin, which then executes code to deploy the RAT. **PHANTOMPULSE** demonstrates advanced capabilities, including using the Ethereum blockchain to dynamically resolve its command-and-control (C2) server address, making it highly resilient to takedowns.

---

Threat Overview
---------------

The attack, designated REF6598, is a multi-stage social engineering effort. Threat actors pose as venture capitalists and engage with targets on professional networking sites before moving the conversation to a private Telegram group. The primary lure is an invitation to collaborate via a shared, cloud-hosted **[Obsidian](https://obsidian.md/)** vault.

Once the victim opens the shared vault, the infection is triggered by social engineering. The victim is prompted to enable the "Installed community plugins" synchronization feature. This seemingly innocuous action, which requires manual user approval, is the key to the compromise. It enables malicious versions of legitimate **[Obsidian](https://obsidian.md/)** plugins ('Shell Commands' and 'Hider') that are present in the shared vault.

Technical Analysis
------------------

The attack chain differs slightly between Windows and macOS but follows the same general principle:

1. **Initial Access ([`T1566.002`](https://attack.mitre.org/techniques/T1566/002/)):** The attacker uses social engineering on LinkedIn/Telegram to convince the target to open a malicious shared **[Obsidian](https://obsidian.md/)** vault.
2. **Execution ([`T1204.002`](https://attack.mitre.org/techniques/T1204/002/)):** The user is manipulated into enabling community plugins within Obsidian. This action executes a malicious script via the compromised 'Shell Commands' plugin.
3. **Staging:** On Windows, a PowerShell script is executed. This script drops a loader known as **PHANTOMPULL**. On macOS, a similar process occurs using AppleScript.
4. **Payload Delivery:** The **PHANTOMPULL** loader decrypts and launches the final payload, the **PHANTOMPULSE** RAT, directly into memory to evade file-based detection ([`T1055`](https://attack.mitre.org/techniques/T1055/)).
5. **Command and Control ([`T1102.002`](https://attack.mitre.org/techniques/T1102/002/)):** **PHANTOMPULSE** uses a novel C2 mechanism. It queries the Ethereum blockchain for the latest transaction from a hard-coded wallet address. The C2 server's IP address is embedded within this transaction data, providing a decentralized and censorship-resistant way for the malware to receive instructions.

Once active, **PHANTOMPULSE** can capture keystrokes, take screenshots, exfiltrate files, and execute arbitrary commands.

Impact Assessment
-----------------

A successful compromise gives the attacker full access to the victim's machine. For professionals in finance and crypto, this could lead to the theft of sensitive corporate data, intellectual property, trading strategies, and, most critically, cryptocurrency wallet keys and exchange credentials. The cross-platform nature of the attack broadens its potential victim pool. The use of a blockchain-based C2 demonstrates a high level of sophistication, making the threat infrastructure difficult to disrupt.

Cyber Observables for Detection
-------------------------------

Description

Monitor for Obsidian spawning child processes like `powershell.exe`, `cmd.exe`, or `osascript`.

Value

`powershell -ExecutionPolicy Bypass`

Description

Suspicious PowerShell execution, especially when initiated by a non-standard application like Obsidian.

Type

network\_traffic\_pattern

Value

Outbound connections to Ethereum blockchain nodes or gateways from unexpected processes.

Description

Could indicate PHANTOMPULSE attempting to resolve its C2 address.

Value

`[Vault]/.obsidian/plugins/`

Description

Monitor for the creation or modification of files within the Obsidian plugins directory, especially outside of the official plugin marketplace.

Detection & Response
--------------------

1. **Process Monitoring (D3-PA: Process Analysis):** Implement EDR rules to detect and alert when the **[Obsidian](https://obsidian.md/)** process spawns command-line interpreters (`powershell.exe`, `cmd.exe`, `bash`, `osascript`). This is highly anomalous behavior.
2. **User Training:** Educate users, especially those in high-risk industries, about the dangers of social engineering and the specific tactic of abusing collaboration tool features like shared vaults and plugins.
3. **Application Control (D3-EAL: Executable Allowlisting):** Where possible, use application control policies to restrict the installation and execution of unapproved community plugins in applications like Obsidian.
4. **Network Monitoring (D3-NTA: Network Traffic Analysis):** Monitor for unusual DNS queries or direct IP connections related to blockchain services from endpoints where such activity is not expected.

Mitigation
----------

1. **Vet Community Plugins:** Be extremely cautious when enabling third-party or community-developed plugins in any application. Only install plugins from the official, trusted marketplace and review their permissions.
2. **Disable Auto-Sync for Untrusted Vaults:** Do not enable plugin synchronization when connecting to an **[Obsidian](https://obsidian.md/)** vault from an unknown or untrusted source.
3. **Principle of Least Privilege:** Run applications like **[Obsidian](https://obsidian.md/)** as a standard user, not with administrative privileges, to limit the potential impact of a compromise.
4. **Endpoint Security:** Ensure up-to-date EDR and antivirus solutions are deployed to detect and block suspicious script execution and process injection techniques.