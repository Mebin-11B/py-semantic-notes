---
title: "Upcoming breaking changes for npm v12"
url: https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/
clipped: 2026-06-17 00:49:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Upcoming breaking changes for npm v12](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

## Digest Summary
npm v12 (scheduled for July 2026) changes default install behavior to improve security. Scripts (preinstall, install, postinstall, node‑gyp rebuild, prepare) are disabled by default; only packages explicitly allowed via `npm approve-scripts` remain executable, with the allowlist stored in `package.json`. Git dependencies are blocked unless `--allow-git` is used, closing a code‑execution vector where a dependency’s `.npmrc` could override the Git executable. Remote URL dependencies (e.g., HTTPS tarballs) are also blocked by default and require `--allow-remote`; the defaults for `--allow-file` and `--allow-directory` stay unchanged. These defaults are already available as warnings in npm 11.16.0+ (or later) so developers can test, review blocked items with `npm approve-scripts --allow-scripts-pending`, approve trusted packages, and commit the updated allowlist before upgrading. Documentation and community discussion links are provided for further guidance.

## Discussion Summary
The comments focus on npm’s new allow‑scripts feature, noting that it defaults to off and mirrors pnpm’s recent changes. Users raise practical questions about its behavior for global installs, version‑specific allowlists, and whether it truly improves security versus merely shifting the risk window. Many express skepticism, arguing the change is superficial, could repeat past defaults, and lack robust safeguards such as sandboxing or age limits. A few view it as a needed step, but overall sentiment leans toward criticism and calls for stronger, more practical security measures.

---

## Full Article

Our next npm major version, v12, introduces security-related default changes to `npm install`. All these changes are available behind warnings in npm today on 11.16.0 or newer, so you can prepare before the upgrade. v12 is estimated to release in July 2026.

Each change turns an `npm install` behavior that runs automatically today into one you explicitly opt into:

* **`allowScripts` defaults to off:** `npm install` will no longer execute `preinstall`, `install`, or `postinstall` scripts from dependencies unless they are explicitly allowed in your project. This includes native `node-gyp` builds (i.e., a package with a `binding.gyp` and no explicit install script still gets blocked, because npm runs an implicit `node-gyp rebuild` for it). `prepare` scripts from git, file, and link dependencies are blocked the same way. To see what would be blocked, run `npm approve-scripts --allow-scripts-pending`. Then allow the packages you trust with `npm approve-scripts` and block the rest with `npm deny-scripts`. The resulting allowlist is written to `package.json` and should be committed. If your install routine runs scripts, you can observe warnings in npm 11.16.0+.
* **`--allow-git` defaults to `none`:** `npm install` will no longer resolve Git dependencies (direct or transitive) unless explicitly allowed via `--allow-git`. This closes a code-execution path where a Git dependency’s `.npmrc` could override the Git executable, even with `--ignore-scripts`. This change was [previously announced on 2026-02-18](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/) and is available in npm 11.10.0+.
* **`--allow-remote` defaults to `none`:** `npm install` will no longer resolve dependencies from remote URLs, such as https tarballs (direct or transitive), unless explicitly allowed via `--allow-remote`. This flag is available in npm 11.15.0+. The related `--allow-file` and `--allow-directory` flags are not changing their defaults in v12.

Upgrade to npm 11.16.0 or later, run your normal install, and review the warnings. Use `npm approve-scripts --allow-scripts-pending` to see which packages have scripts, approve the ones you trust, and commit the updated `package.json`. After that, only the scripts you approved keep running once you upgrade. Anything you leave unapproved will stop. More details are available in our docs at [`npm approve-scripts`](https://docs.npmjs.com/cli/v11/commands/npm-approve-scripts), [`npm deny-scripts`](https://docs.npmjs.com/cli/v11/commands/npm-deny-scripts), and [`allow-scripts` config](https://docs.npmjs.com/cli/v11/using-npm/config#allow-scripts) (for `npx` and global installs). Please share your comments and questions in our [community discussion](https://github.com/orgs/community/discussions/198547).