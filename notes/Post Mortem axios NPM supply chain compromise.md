---
title: "Post Mortem: axios NPM supply chain compromise"
url: https://github.com/axios/axios/issues/10636
clipped: 2026-06-17 01:23:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Post Mortem: axios NPM supply chain compromise](https://github.com/axios/axios/issues/10636)

## Digest Summary
In March 2026 two malicious Axios releases (1.14.1 and 0.30.4) were published to npm from a compromised maintainer account. Both versions introduced the dependency **plain‑crypto‑[email protected]**, which installed a remote‑access trojan on macOS, Windows and Linux. The packages were live for roughly three hours before removal.

**Impact & remediation**
- Search lockfiles for `[email protected]|0.30.4` or `plain-crypto-js`; if found, treat the host as compromised.
- Downgrade to `[email protected]` (or `0.30.3` for 0.x), delete `node_modules/plain-crypto-js`, rotate all secrets, and audit network traffic for connections to `sfrclak.com` or `142.11.206.73:8000`.
- Apply the same steps on CI runners and rotate any injected credentials.

**Root cause**
- Targeted social‑engineering and RAT malware gave the attacker access to the lead maintainer’s PC and npm credentials, allowing unauthorized publishes.

**Response**
- Full wipe of the maintainer’s devices and reset of all related accounts.
- Deprecation of the compromised versions, removal of `plain-crypto-js` from npm, and coordination with npm security.
- Planned security upgrades: OIDC publishing flow, immutable releases, automated publish monitoring, and tighter maintainer access controls.

## Discussion Summary
The comments convey concern about a recent supply‑chain breach, noting that the malicious release lacked OIDC provenance attestations while legitimate versions included them, and highlighting that such discrepancies often go unchecked. Observers point to a broader rise in similar attacks and criticize npm’s current security measures for insufficient detection of malicious code in public packages. There is interest in detailed payload analysis to assess the breach’s scope, and questions about whether OIDC flows could mitigate this type of intrusion.

---

## Full Article

Post Mortem: axios npm supply chain compromise
==============================================

**Date:** March 31, 2026  
**Author:** Jason Saayman  
**Status:** Remediation in progress

On March 31, 2026, two malicious versions of axios (1.14.1 and 0.30.4) were published to the npm registry through my compromised account. Both versions injected a dependency called `plain-crypto-js@4.2.1` that installed a remote access trojan on macOS, Windows, and Linux.

The malicious versions were live for about 3 hours before being removed.

Are you affected?
-----------------

Check your lockfile:

```
grep -E "axios@(1\.14\.1|0\.30\.4)|plain-crypto-js" package-lock.json yarn.lock 2>/dev/null
```

If anything comes back, treat that machine as compromised:

1. Downgrade to `axios@1.14.0` (or `0.30.3` for 0.x users)
2. Delete `node_modules/plain-crypto-js/`
3. Rotate every secret, token, and credential on that machine
4. Check your network logs for connections to `sfrclak[.]com` or `142.11.206.73` on port 8000
5. If this happened on a CI runner, rotate any secrets that were injected during the affected build

If you were already pinned to a clean version and didn't run a fresh install between 00:21 and 03:15 UTC on March 31, you're fine.

For detailed remediation guidance, including CI/CD-specific steps, see:

What happened
-------------

The attacker gained access to the lead maintainer's PC through a targeted social engineering campaign and RAT malware. This gave them access to the npm account credentials, which they used to publish the malicious versions.

The attack followed patterns documented in similar campaigns targeting open source maintainers.

Resolution
----------

Complete wipe of all lead maintainer devices as well as resetting of all credentials. This includes all accounts irrespective of platform, both personal and all other capacities.

What's changing
---------------

To prevent this from happening again, these are the changes being made:

| Action | Type |
| --- | --- |
| Reset of all devices and credentials | Prevention |
| Immutable release setup | Prevention |
| Proper adoption of OIDC flow for publishing | Prevention |
| Improvement of overall security posture | Prevention |
| Updating of all GitHub actions to adopt best practices | Prevention |

This list is not the end. We will continue actively working on improving security beyond these items.

Attack Timeline
---------------

I don't have an exact timeline for when the initial compromise occurred, but this is the sequence of events for the package itself:

* About 2 weeks before March 31: social engineering campaign initiated against the lead maintainer
* March 30, 05:57 UTC: `plain-crypto-js@4.2.0` published to npm
* March 31, 00:21 UTC: `axios@1.14.1` published with `plain-crypto-js@4.2.1` injected
* March 31, around 01:00 UTC: `axios@0.30.4` published with the same payload
* March 31, around 01:00 UTC: first external detections
* March 31, around 01:00 UTC: community members file issues reporting the compromise. The attacker deletes them using the compromised account.
* March 31, 01:38 UTC: axios collaborator DigitalBrainJS opens PR [chore(ci): add deprecate action; #10591](https://github.com/axios/axios/pull/10591) to deprecate the compromised versions, flags the deleted issues to the community, and contacts npm directly
* March 31, 03:15 UTC: malicious versions removed from npm
* March 31, 03:29 UTC: `plain-crypto-js` removed from npm

For detailed technical timelines:

Lessons learned
---------------

We are actively investigating how unauthorized access was obtained and reviewing all aspects of our security posture and access controls. While we do not have confirmed details to share at this time, this incident reinforces the need for continuous monitoring, strong account protections, and vigilance across both project infrastructure and individual maintainer environments.

We will continue to strengthen our practices in alignment with industry best practices and in collaboration with groups such as the OpenJS Security Working Group.

Security posture should be continuously monitored and improved. Specifically from this incident:

* Publishing directly from a personal account was a risk that could have been avoided. The OIDC flow and immutable release setup we are now adopting should have been in place before this happened.
* There was no automated way to detect an unauthorized publish. Detection depended entirely on the community noticing.
* Open source maintainers with high-impact packages are active targets for sophisticated social engineering. Hyper vigilance is needed both on the registry and in a personal capacity.

Summary for broarder audience
-----------------------------

We can confirm that two compromised versions of Axios were briefly made available through a widely used software download system due to unauthorized access to the lead maintainer's account, not a change to the underlying code.

We are working with the companies that operate this system, along with security experts, to investigate and contain the issue. Organizations that installed these versions should remove them immediately and treat affected systems as potentially compromised, including rotating any sensitive credentials.

This was the result of a compromised lead maintainer's account, and we are actively investigating how access was obtained. We do not have confirmed details to share at this time.

Acknowledgments
---------------

Thanks to [@DigitalBrainJS](https://github.com/DigitalBrainJS) for acting fast when the compromised account had higher permissions than his own and for getting npm to take action. Thanks to Open Source Community and the npm security team for their fast response.

The malicious versions have been removed from npm and are no longer infecting users. The immediate incident is resolved. We are actively working on the security improvements listed above to prevent this from happening again.

I'll update this as the investigation progresses. Questions welcome in this thread.