---
title: "Bug 1950764: Work Around Crash on Intel Raptor Lake CPU"
url: https://phabricator.services.mozilla.com/D301917
clipped: 2026-06-17 00:57:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Bug 1950764: Work Around Crash on Intel Raptor Lake CPU](https://phabricator.services.mozilla.com/D301917)

## Digest Summary
Bug 1950764 reports a crash occurring on Intel Raptor Lake CPUs and proposes a workaround. The issue is linked to the Rust implementation of zlib (path: third_party/rust/zlib‑rs/src/deflate/). The revision was authored on 21 May 2026 and underwent multiple updates, with timestamps ranging from 21 May 23:39 UTC to 23 May 12:41 UTC. Each update appears duplicated in the event log. No additional technical details, code changes, or mitigation steps are provided in the excerpt.

## Discussion Summary
The discussion conveys strong criticism of Intel’s handling of a Raptor Lake errata, noting the absence of official documentation or microcode fixes and questioning whether the problem stems from design flaws or post‑manufacturing damage. Commenters emphasize that the defect appears tied to clock‑propagation edge cases rather than a universal architectural bug, and they criticize media coverage for spreading inaccurate information. There is a consensus that comprehensive regression testing and upstream compiler or microcode changes are needed, while blanket software work‑arounds are deemed impractical.

---

## Full Article

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Authored by **[glandium](https://phabricator.services.mozilla.com/p/glandium/)** on Thu, May 21, 9:16 PM.  |  |  | | --- | --- | |  | Unknown Object (File) | | Mon, Jun 15, 2:10 PM2026-06-15 14:10:18 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Thu, Jun 11, 1:20 PM2026-06-11 13:20:55 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Mon, Jun 8, 4:43 PM2026-06-08 16:43:28 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Fri, Jun 5, 9:02 PM2026-06-05 21:02:55 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Thu, Jun 4, 11:11 AM2026-06-04 11:11:41 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Thu, Jun 4, 1:08 AM2026-06-04 01:08:15 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Wed, Jun 3, 6:11 PM2026-06-03 18:11:10 (UTC+0) |  |  |  | | --- | --- | |  | Unknown Object (File) | | Wed, Jun 3, 10:27 AM2026-06-03 10:27:52 (UTC+0) |  Event Timeline       [phab-bot](https://phabricator.services.mozilla.com/p/phab-bot/) published this revision for review.          This revision is now accepted and ready to land.      This revision was automatically updated to reflect the committed changes.      This revision is now accepted and ready to land.          This revision was automatically updated to reflect the committed changes.  | Path | Size | | --- | --- | |  |  | |  | 3 lines | | |  |  |  |  |  | | --- | --- | --- | --- | --- | |  | third\_party/ | rust/ | zlib-rs/ | src/ | |  | |  |  | |  | 13 lines | |  | 4 lines |  | Commit | Tree | Parents | Author | Summary | Date | | --- | --- | --- | --- | --- | --- | | 83c242319d07 | 4c80ad45ede1 |  | Mike Hommey | Bug 1950764 - Work around crash on Intel Raptor Lake CPU. r=gsvelto [(Show More…)](https://phabricator.services.mozilla.com/D301917#) |  |  * + Tue, Jun 16, 5:19 PM2026-06-16 17:19:56 (UTC+0) * + Tue, Jun 16, 3:24 PM2026-06-16 15:24:32 (UTC+0) * + Tue, Jun 16, 11:50 AM2026-06-16 11:50:32 (UTC+0) * + Tue, Jun 16, 1:02 AM2026-06-16 01:02:59 (UTC+0) * + ·Reviewers: Restricted Project, [emilio](https://phabricator.services.mozilla.com/p/emilio/)  + Mon, Jun 15, 1:15 PM2026-06-15 13:15:08 (UTC+0) * + Sun, Jun 14, 3:04 PM2026-06-14 15:04:19 (UTC+0) * + Sat, Jun 13, 10:31 PM2026-06-13 22:31:10 (UTC+0) * + Sat, Jun 13, 10:09 PM2026-06-13 22:09:10 (UTC+0) * + Thu, Jun 11, 1:21 PM2026-06-11 13:21:37 (UTC+0) * + Thu, Jun 11, 11:06 AM2026-06-11 11:06:15 (UTC+0) |