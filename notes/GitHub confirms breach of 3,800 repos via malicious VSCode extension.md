---
title: "GitHub confirms breach of 3,800 repos via malicious VSCode extension"
url: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/
clipped: 2026-06-17 00:59:38
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GitHub confirms breach of 3,800 repos via malicious VSCode extension](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/)

## Digest Summary
GitHub confirmed that an employee’s installation of a malicious VS Code extension compromised roughly 3,800 internal repositories. The trojanized extension was removed from the VS Code Marketplace, the affected endpoint was isolated, and an incident response was initiated. GitHub’s investigation indicates exfiltration was limited to GitHub‑internal code; no evidence shows customer data outside the affected repos was accessed. The TeamPCP hacker group, previously linked to large supply‑chain attacks on platforms such as GitHub, PyPI, NPM, Docker, and the “Mini Shai‑Hulud” campaign, claimed responsibility and posted the stolen code on the Breached forum, demanding at least $50 000. This is not the first VS Code supply‑chain compromise—earlier incidents involved extensions with millions of installs that delivered cryptominers, ransomware, and data‑exfiltration tools (including AI‑assistant extensions that sent data to servers in China). GitHub’s platform hosts over 4 million organizations and 180 million developers across 420 million repositories.

## Discussion Summary
Comments express strong concern over the security of VS Code extensions, citing frequent prompts to install unknown add‑ons and recent supply‑chain compromises as evidence of inadequate sandboxing and permission controls. Users criticize Microsoft and GitHub for slow progress on extension isolation, request explicit permission systems, and highlight the difficulty of securing Electron‑based tools. Many suggest stricter policies such as disabling auto‑updates, enforcing fine‑grained tokens, and considering alternative IDEs or WebAssembly‑based plugins. Overall sentiment is wary, frustrated, and calls for more transparent, robust safeguards.

---

## Full Article

![GitHub](https://www.bleepstatic.com/content/hl-images/2026/05/20/GitHub.jpg)

***Update May 21**: GitHub has now [linked this breach to the TanStack npm supply-chain attack](https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/) and says the employee installed a malicious version of the Nx Console extension.*

GitHub has confirmed that roughly 3,800 internal repositories were breached after one of its employees installed a malicious VS Code extension.

The company has since removed the unnamed trojanized extension from the VS Code marketplace and has secured the compromised device.

"Yesterday we detected and contained a compromise of an employee device involving a poisoned VS Code extension. We removed the malicious extension version, isolated the endpoint, and began incident response immediately," [the company said](https://x.com/github/status/2056949169701720157).

"Our current assessment is that the activity involved exfiltration of GitHub-internal repositories only. The attacker's current claims of ~3,800 repositories are directionally consistent with our investigation so far."

This comes after GitHub told BleepingComputer on Tuesday evening that it was [investigating claims of unauthorized access](https://www.bleepingcomputer.com/news/security/github-investigates-internal-repositories-breach-claimed-by-teampcp/) to its internal repositories and added that it has no evidence that customer data stored outside the affected repos has been affected.

While GitHub has yet to attribute the breach, the TeamPCP hacker group claimed access to GitHub source code and "~4,000 repos of private code" on the Breached cybercrime forum on Tuesday, asking for at least $50,000 for the stolen data.

"As always this is not a ransom, We do not care about extorting Github, 1 buyer and we shred the data on our end, it looks like our retirement is soon so if no buyer is found we will leak it free," the cybercriminals said. "If you are interested. Send your offers to the communications below, we are not interested in under 50k, the best offer will get it."

​TeamPCP was previously linked to massive supply chain attacks targeting developer code platforms, including [GitHub](https://www.bleepingcomputer.com/news/security/trivy-vulnerability-scanner-breach-pushed-infostealer-via-github-actions/), [PyPI](https://www.bleepingcomputer.com/news/security/backdoored-telnyx-pypi-package-pushes-malware-hidden-in-wav-audio/), [NPM](https://www.bleepingcomputer.com/news/security/teampcp-deploys-iran-targeted-wiper-in-kubernetes-attacks/), and [Docker](https://www.bleepingcomputer.com/news/security/trivy-supply-chain-attack-spreads-to-docker-github-repos/), and, more recently, to [the "Mini Shai-Hulud" supply chain campaign](https://www.bleepingcomputer.com/news/security/openai-confirms-security-breach-in-tanstack-supply-chain-attack/)(which also impacted two OpenAI employees).

​VS Code extensions are plugins that can be installed from the VS Code Marketplace (the official store for add-ons for Microsoft's code editor) to add features or integrate tools into the editor.

This isn't the first time a trojanized VS Code extension has been spotted on the marketplace, as multiple other malicious extensions with millions of installs have been used to steal developer credentials and other sensitive data over the last several years.

For instance, last year, VSCode extensions with 9 million installs [were pulled over security risks](https://www.bleepingcomputer.com/news/security/vscode-extensions-with-9-million-installs-pulled-over-security-risks/), and 10 more, posing as legitimate development tools, [infected users with the XMRig cryptominer](https://www.bleepingcomputer.com/news/security/malicious-vscode-extensions-infect-windows-with-cryptominers/).

Later in the year, a [malicious extension with basic ransomware capabilities](https://www.bleepingcomputer.com/news/security/ai-slop-ransomware-test-sneaks-on-to-vs-code-marketplace/) snuck onto the VS Code marketplace after a threat actor named WhiteCobra [flooded it with 24 crypto-stealing extensions](https://www.bleepingcomputer.com/news/security/whitecobra-floods-vscode-market-with-crypto-stealing-extensions/).

More recently, in January, two malicious extensions advertised as AI-based coding assistants with 1.5 million installs [exfiltrated data from compromised developer systems to servers in China](https://www.bleepingcomputer.com/news/security/malicious-ai-extensions-on-vscode-marketplace-steal-developer-data/).

GitHub's cloud-based platform is now used by over 4 million organizations (including 90% of the Fortune 100) and more than 180 million developers who contribute to over 420 million code repositories.

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

[Get the whitepaper](https://hubs.li/Q04jQ9z40)