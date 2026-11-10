---
title: "GitHub experience various partial-outages/degradations"
url: https://www.githubstatus.com?todayis=2026-02-02
clipped: 2026-06-17 01:49:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GitHub experience various partial-outages/degradations](https://www.githubstatus.com?todayis=2026-02-02)

## Digest Summary
GitHub reported a service incident affecting GitHub Actions hosted runners. From 19:03 UTC on Feb 2, degraded performance and high wait times were observed, with jobs queuing and failing across all labels; self‑hosted runners remained unaffected. The issue also impacted dependent features such as Copilot Coding Agent, Dependabot, and Pages, which showed degraded performance. An upstream provider was engaged; mitigation steps were applied by 22:53 UTC, leading to gradual recovery. By 00:56 UTC on Feb 3, Actions and related services were operating normally, and telemetry indicated full recovery for most customers. The incident was declared resolved at 00:56 UTC on Feb 3, with a root‑cause analysis to follow.

## Discussion Summary
The comments express frustration over a widespread Azure outage that disrupted VM‑scale operations and consequently halted GitHub Actions, causing jobs to fail and consume minutes. Users identify a recent storage‑account ACL change as the root cause and note the broader impact on services such as Azure Arc, Batch, DevOps, and Load Testing. There is disappointment with the reliability of the platform, criticism of Azure’s configuration handling, and concern about GitHub’s dependence on Azure, alongside requests for compensation for lost action minutes.

---

## Full Article

> [!WARNING]
> Could not retrieve full article content: HTTPSConnectionPool(host='www.githubstatus.com', port=443): Read timed out. (read timeout=10)
> You can view the original article page directly [here](https://www.githubstatus.com?todayis=2026-02-02).