---
title: "Bitwarden CLI compromised in ongoing Checkmarx supply chain campaign"
url: https://socket.dev/blog/bitwarden-cli-compromised
clipped: 2026-06-17 01:12:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - supply chain security
  - npm package security
  - ci/cd security
  - credential harvesting
  - open source security
related:
  - "[[Supply Chain Security]]"
  - "[[CI/CD Security]]"
  - "[[npm Package Security]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Security researchers discovered that the npm package of Bitwarden's open-source CLI was compromised via a hijacked GitHub Actions workflow to harvest and exfiltrate developer and cloud credentials.
>
> **Key points:**
> - The `@bitwarden/cli@2026.4.0` npm package was compromised, injecting a malicious payload (`bw1.js`) targeting CI/CD pipelines and developer environments.
> - The malware extracts GitHub tokens, cloud provider credentials (AWS, Azure, GCP), npm tokens, and SSH keys, exfiltrating them via HTTP requests, Git commits, and npm republishing.
> - The compromise shares infrastructure with the broader Checkmarx supply chain campaign, incorporating a novel Russian locale kill switch and Dune-themed exfiltration naming conventions.
> - Recommended actions include removing the affected package, rotating exposed credentials, and auditing GitHub repositories and npm registries for unauthorized changes.
>
> **Concept links:** [[Supply Chain Security]], [[npm Package Security]], [[CI/CD Security]], [[Credential Harvesting]], [[Open Source Security]]
>
> **Suggested connections:**
> - [[Supply Chain Security]] — techniques and defenses relating to securing software dependencies and distribution pipelines.
> - [[CI/CD Security]] — best practices for hardening automated integration and deployment workflows against compromise.
> - [[npm Package Security]] — safety, auditing, and vulnerability management within the JavaScript npm ecosystem.
<!-- ai-summary:end -->


# [Bitwarden CLI compromised in ongoing Checkmarx supply chain campaign](https://socket.dev/blog/bitwarden-cli-compromised)

## Digest Summary
Bitwarden’s open‑source CLI (npm package @bitwarden/cli 2026.4.0) was compromised in the ongoing Checkmarx supply‑chain campaign. Attackers injected a malicious file bw1.js into the package via a hijacked GitHub Actions workflow, reusing the same C2 endpoint https://audit.checkmarx.cx/v1/telemetry (obfuscated with a decode routine seeded 0x3039). The payload contains a gzip‑base64‑encoded Python memory‑scraper for GitHub Actions runners, a setup.mjs loader for republished npm packages, a malicious workflow YAML, hard‑coded RSA keys, and an ideological manifesto. It harvests GitHub tokens, AWS/Azure/GCP credentials, npm tokens, SSH keys, and environment variables, exfiltrating data through the GitHub API, npm registry republishing, and the C2 server. Additional behaviors include a lock file /tmp/tmp.987654321.lock, persistence via ~/.bashrc and ~/.zshrc, a Russian‑locale kill switch, and execution with Bun v1.3.13. Recommendations: remove the compromised package, rotate all exposed credentials, audit GitHub for unauthorized repositories, workflows, and Dune‑themed naming patterns, and monitor for outbound connections to audit.checkmarx.cx and IP 94.154.172.43. Harden token scopes and CI/CD permissions to limit future supply‑chain impact.

## Discussion Summary
The discussion centers on recent supply‑chain compromises affecting npm packages, especially the malicious Bitwarden CLI release, and the broader risk of automatic dependency updates. Commenters emphasize using version‑pinning, minimum‑release‑age settings, and dedicated tooling to restrict fresh releases, while several advocate moving to languages or ecosystems with tighter dependency trees. Experiences of credential exposure and distrust of JavaScript‑based CLIs reinforce calls for stricter CI/CD controls, alternative password‑manager solutions, and more cautious update policies. Consensus is that current practices are insufficient and additional safeguards are needed.

---

## Full Article

Socket researchers discovered that the Bitwarden CLI was compromised as part of the ongoing [**Checkmarx supply chain campaign**](https://socket.dev/blog/checkmarx-supply-chain-compromise). The open source password manager serves more than 10 million users and over 50,000 businesses, and ranks among among the [top three password managers](https://ramp.com/vendors/bitwarden) by enterprise adoption.

The affected package version appears to be [**`@bitwarden/cli2026.4.0`**](https://socket.dev/npm/package/@bitwarden/cli/overview/2026.4.0), and the malicious code was published in [**`bw1.js`**](https://socket.dev/npm/package/@bitwarden/cli/files/2026.4.0/bw1.js), a file included in the package contents. The attack appears to have leveraged a compromised GitHub Action in Bitwarden’s CI/CD pipeline, consistent with the pattern seen across other affected repositories in this campaign.

**What we know so far:**

* Bitwarden CLI builds were affected
* The compromise follows the same GitHub Actions supply chain vector identified in the broader [**Checkmarx campaign**](https://socket.dev/blog/checkmarx-supply-chain-compromise)

This is an ongoing investigation. Socket's security research team is conducting a full technical analysis and will publish detailed findings, including affected versions, indicators of compromise, and remediation guidance.

If you use Bitwarden CLI, we recommend reviewing your CI logs and rotating any secrets that may have been exposed to the compromised workflow. At this time, the compromise only involves only the npm package for the CLI. Bitwarden’s Chrome extension, MCP server, and other legitimate distributions have not been affected yet.

Technical analysis[#](https://socket.dev/blog/bitwarden-cli-compromised#Technical-analysis)
-------------------------------------------------------------------------------------------

The malicious payload was in a file named `bw1.js` , which shares core infrastructure with the [Checkmarx](https://socket.dev/blog/checkmarx-supply-chain-compromise) `mcpAddon.js` we analyzed yesterday:

* **Same C2 endpoint**: Uses identical `audit.checkmarx[.]cx/v1/telemetry` endpoint, obfuscated via `__decodeScrambled` with seed `0x3039`. Exfiltration also occurs through GitHub API (commit-based) and npm registry (token theft/republishing)
* **Embedded payloads**: Same gzip+base64 structure containing a Python memory-scraping script targeting GitHub Actions Runner.Worker, a setup.mjs loader for republished npm packages, a GitHub Actions workflow YAML, hardcoded RSA public keys, and an ideological manifesto string
* **Credential harvesting**: GitHub tokens via Runner.Worker memory scraping and environment variables, AWS credentials via ~/.aws/ files and environment, Azure tokens via azd, GCP credentials via gcloud config config-helper, npm configuration files (.npmrc), SSH keys, environment variables, and Claude/MCP configuration files
* Github **Exfiltration**: Public repositories created under victim accounts using Dune-themed naming ({word}-{word}-{3digits}), with encrypted results committed and tokens embedded in commit messages using the marker `LongLiveTheResistanceAgainstMachines`
* **Supply chain propagation**: npm token theft to identify writable packages and republish with injected preinstall hooks, GitHub Actions workflow injection to capture repository secrets
* **Russian locale kill switch**: Exits silently if system locale begins with "ru", checking Intl.DateTimeFormat().resolvedOptions().locale and environment variables LC\_ALL, LC\_MESSAGES, LANGUAGE, and LANG
* **Runtime**: Bun v1.3.13 interpreter downloaded from GitHub releases

This payload (bw1.js)also includes several indicators not documented in the Checkmarx incident:

* **Lock file**: Hardcoded path `/tmp/tmp.987654321.lock` prevents multiple instances from running simultaneously
* **Shell profile persistence**: Injects payload into `~/.bashrc` and `~/.zshrc`
* **Explicit branding**: Repository description `Shai-Hulud: The Third Coming` replaces the deceptive "Checkmarx Configuration Storage", and debug strings include `"Would be executing butlerian jihad!"`

The shared tooling strongly suggests a connection to the same malware ecosystem, but the operational signatures differ in ways that complicate attribution. The Checkmarx attack was claimed by TeamPCP via the @pcpcats social media account after discovery, and the malware itself attempted to blend in with legitimate-looking descriptions. This payload takes a different approach: the ideological branding is embedded directly in the malware, from the Shai-Hulud repository names to the "Butlerian Jihad" manifesto payload to commit messages proclaiming resistance against machines. This suggests either a different operator using shared infrastructure, a splinter group with stronger ideological motivations, or an evolution in the campaign's public posture.

Recommendations[#](https://socket.dev/blog/bitwarden-cli-compromised#Recommendations)
-------------------------------------------------------------------------------------

Organizations that installed the malicious Bitwarden npm package should treat this incident as a credential exposure and CI/CD compromise event.

Immediately remove the affected package from developer systems and build environments. Rotate any credentials that may have been exposed to those environments, including GitHub tokens, npm tokens, cloud credentials, SSH keys, and CI/CD secrets. Review GitHub for unauthorized repository creation, unexpected workflow files under .github/workflows/, suspicious workflow runs, artifact downloads, and public repositories matching the observed Dune-themed staging pattern ({word}-{word}-{3digits}). Check for the following keywords in newly published repositories if you believe you may be impacted:

```
atreides
cogitor
fedaykin
fremen
futar
gesserit
ghola
harkonnen
heighliner
kanly
kralizec
lasgun
laza
melange
mentat
navigator
ornithopter
phibian
powindah
prana
prescient
sandworm
sardaukar
sayyadina
sietch
siridar
slig
stillsuit
thumper
tleilaxu
```

Audit npm for unauthorized publishes, version changes, or newly added install hooks. In cloud environments, review access logs for unusual secret access, token use, and newly issued credentials.

On endpoints and runners, hunt for outbound connections to the observed exfiltration infrastructure (`audit[.]checkmarx[.]cx`), execution of Bun where it is not normally used, access to files such as .npmrc, .git-credentials, .env, cloud credential stores, gcloud, az, or azd. Check for the lock file `/tmp/tmp.987654321.lock` and shell profile modifications in ~/.bashrc and ~/.zshrc. For GitHub Actions, review whether any unapproved workflows were created on transient branches and whether artifacts such as `format-results.txt` were generated or downloaded.

As a longer-term control, reduce the blast radius of future supply chain incidents by locking down token scopes, requiring short-lived credentials where possible, restricting who can create or publish packages, hardening GitHub Actions permissions, disabling unnecessary artifact access, and monitoring for new public repositories or workflow changes created outside normal release processes.

IOCs[#](https://socket.dev/blog/bitwarden-cli-compromised#IOCs)
---------------------------------------------------------------

### Malicious Package

### Network Indicators

* **`94[.]154[.]172[.]43`**
* **`https://audit.checkmarx[.]cx/v1/telemetry`**

### File System Indicators (Victim Package Compromise)

* `/tmp/tmp.987654321.lock`
* `/tmp/_tmp_<Unix Epoch Timestamp>/`
* `package-updated.tgz`