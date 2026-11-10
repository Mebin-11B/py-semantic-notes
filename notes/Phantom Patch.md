---
title: "Phantom Patch"
source: "https://samizdat.dev/phantom-patch/"
author:
published: 2000-04-27
created: 2026-06-01
description: "I share what I know."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Computer Security
  - Vulnerability Research
  - Developer Tools
  - Exploit Development
  - Git Workflows
related:
  - "Computer Security"
  - "Mythos finds a curl vulnerability.md"
  - "Uncovering an iOS 26 ImageIO Vulnerability.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An analysis of the 'Phantom Patch' security issue where diff-shaped text in a commit message is mistakenly applied by GNU patch when processing GitHub's exported .patch files.
>
> **Key points:**
> - Demonstrates how GNU patch fails to distinguish between the actual code diff and diff-formatted text embedded within the commit subject or body.
> - Shows that while GitHub's web UI only displays the real commit changes, downloading the .patch version and running patch applies the hidden 'phantom' diff.
> - Explains that while git apply and git am reject critical paths (like .git/), they still apply fake diffs to normal files in the working directory.
> - Warns that this vulnerability poses a risk to common developer workflows involving piping curl/wget outputs directly to the patch command.
>
> **Concept links:** [[Computer Security]], [[Vulnerability Research]], [[Developer Tools]], [[Exploit Development]], [[Git Workflows]]
>
> **Suggested connections:**
> - [[Mythos finds a curl vulnerability.md]] — connects command-line utility security (specifically curl/wget usage) and code reviews to exploit surfaces.
> - [[Uncovering an iOS 26 ImageIO Vulnerability.md]] — another technical breakdown of vulnerability discovery and parser/input validation issues.
<!-- ai-summary:end -->

GitHub (and many others) exposes mail-style patches at `.patch` URLs. If you download one of those patches and feed it to GNU `patch`, diff-shaped text inside the commit message can be applied as if it were part of the real patch.

It matters (to me) because `wget` / `curl` plus `patch` is not some exotic lab setup. It is a very old, very ordinary way to move a patch from one machine to another.

## Public reproducer

```diff
From dd28283159930b8fff2119aa9f75af8b4c1ed8b2 Mon Sep 17 00:00:00 2001
From: Egor Kovetskiy <e.kovetskiy [spam] gmail.com>
Date: Wed, 22 Apr 2026 06:37:11 +0000
Subject: [PATCH] readme: add initial file

The body includes a fake diff for patch workflow testing.

diff --git a/SHOULD_NOT_BE_HERE.md b/SHOULD_NOT_BE_HERE.md
new file mode 100644
index 0000000..802992c
--- /dev/null
+++ b/SHOULD_NOT_BE_HERE.md
@@ -0,0 +1 @@
+Hello world
---
 readme.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md

diff --git a/readme.md b/readme.md
new file mode 100644
index 0000000..b44b8fd
--- /dev/null
+++ b/readme.md
@@ -0,0 +1 @@
+Demo repository
```

Here is the smallest public demo I could make:

- [`dd28283`](https://github.com/kovetskiy/git-example/commit/dd28283)
- [`dd28283.patch`](https://github.com/kovetskiy/git-example/commit/dd28283.patch)

The real commit changes one file: `readme.md`.

If you inspect the commit in GitHub’s UI, that is all you see.

But the commit message also contains a fake unified diff:

```diff
diff --git a/SHOULD_NOT_BE_HERE.md b/SHOULD_NOT_BE_HERE.md
new file mode 100644
index 0000000..802992c
--- /dev/null
+++ b/SHOULD_NOT_BE_HERE.md
@@ -0,0 +1 @@
+Hello world
```

So the exported patch has two layers:

1. **The real patch** changes `readme.md`.
2. **The phantom patch** lives inside the commit message and creates `SHOULD_NOT_BE_HERE.md`.

Scenario:

```bash
wget -O /tmp/dd28283.patch \
  https://github.com/kovetskiy/git-example/commit/dd28283.patch
patch -p1 < /tmp/dd28283.patch
```

output:

```text
patching file SHOULD_NOT_BE_HERE.md
patching file readme.md
```

That `SHOULD_NOT_BE_HERE.md` was never part of the real commit.

## Is something broken

I am not sure. But from my POV, GNU `patch -p1` does not reliably separate two things:

- the actual diff exported from the commit
- diff-shaped text embedded in the commit message

## Scope

The public demo writes an ordinary file because that is easy to publish and easy to inspect.

Locally, I also targeted `.git/hooks/post-applypatch`, and GNU `patch` happily accepted that (why would not it, right?).

Fortunately, `git apply` and `git am` behaved better in one narrow sense: they rejected the `.git/...` path. But they still accepted an injected diff for an ordinary working-tree file.

NOTE: `git cherry-pick` looks different. It works with Git objects directly.

## Takeaway

I do not yet know whether the bug belongs to GNU `patch`, GitHub’s `.patch` export, or the broader patch-format contract. But I’ll look at the commit message closer next time.