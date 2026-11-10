---
title: "Gentoo on Codeberg"
url: https://www.gentoo.org/news/2026/02/16/codeberg.html
clipped: 2026-06-17 01:43:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Gentoo on Codeberg](https://www.gentoo.org/news/2026/02/16/codeberg.html)

## Digest Summary
Gentoo has added a mirror repository on Codeberg (https://codeberg.org/gentoo/gentoo) as an alternative to GitHub, part of a planned migration away from GitHub noted in the 2025 end‑of‑year review. Codeberg runs on Forgejo, is operated by a non‑profit in Berlin, and will later host additional Gentoo git repositories. The mirrors are intended solely for convenient contribution; Gentoo continues to host its primary repositories as before. Contributors are advised to use an “AGit” workflow to avoid maintaining personal forks. The workflow involves cloning the upstream Gentoo repository via [email protected], adding a remote for Codeberg (ssh://[email protected]/gentoo/gentoo), creating a feature branch, and pushing with `git push codeberg HEAD:refs/for/master -o topic="$title"` (adding `-o force-push=true` for amended commits). Further details are on the Gentoo wiki.

## Discussion Summary
Comments show a growing interest in moving code hosting away from GitHub toward alternatives such as Codeberg, Gitea, Forgejo, and self‑hosted solutions. Users cite GitHub’s deteriorating UI performance, pricing changes, AI integration, and perceived US‑centric lock‑in as reasons for migration, while acknowledging its useful features like organization‑wide code search. Alternatives are praised for speed, simplicity, open‑source ethos, and independence, though some note slower git operations or occasional availability issues. The overall sentiment reflects a collective shift toward diversified, less centralized hosting options.

---

## Full Article

[![Codeberg logo](https://www.gentoo.org/assets/img/news/2026/logo-codeberg.png)](https://codeberg.org/)

Gentoo now has a presence on [Codeberg](https://codeberg.org/), and contributions can be submitted for the Gentoo
repository mirror at <https://codeberg.org/gentoo/gentoo> as an alternative to GitHub.
Eventually also other git repositories will become available under the Codeberg Gentoo organization.
This is part of the gradual mirror migration away from GitHub, as already mentioned in the [2025 end-of-year review](https://www.gentoo.org/news/2026/01/05/new-year.html).
Codeberg is a site based on [Forgejo](https://forgejo.org/), maintained by a dedicated
[non-profit organization](https://docs.codeberg.org/getting-started/what-is-codeberg/),
and located in Berlin, Germany. Thanks to everyone who has helped make this move possible!

These mirrors are for convenience for contribution and we continue to host our own
repositories, just like we did while using GitHub mirrors for ease of
contribution too.

Submitting pull requests
------------------------

If you wish to submit pull requests on Codeberg, it is recommended to
use the [AGit approach](https://forgejo.org/docs/latest/user/agit-support/) as it is more space efficient and does not
require you to maintain a fork of gentoo.git on your own Codeberg
profile. To set it up, clone the upstream URL and check out a branch
locally:

```
git clone https://anongit.gentoo.org/git/repo/gentoo.git
cd gentoo
git remote add codeberg ssh://git@codeberg.org/gentoo/gentoo
git checkout -b my-new-fixes
```

Once youâre ready to create your PR:

```
git push codeberg HEAD:refs/for/master -o topic="$title"
```

and the PR should be created automatically. To push additional
commits, repeat the above command - be sure that the same topic is
used. If you wish to force-push updates (because youâre amending
commits), add â-o force-push=trueâ to the above command.

More documentation can be found [on our wiki](https://wiki.gentoo.org/wiki/Project:Codeberg/Pull_requests).