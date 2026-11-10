---
title: "Towards Trust in Emacs"
url: https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html
clipped: 2026-06-17 01:15:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Emacs
  - Software Trust Models
  - CVE-2024-53920
  - Developer Tooling
  - Sandboxing
related:
  - "[[Emacs]]"
  - "[[Software Trust Models]]"
  - "[[CVE-2024-53920]]"
  - "[[Developer Tooling]]"
  - "[[Sandboxing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The `trust-manager` package for Emacs mitigates the friction of Emacs 30's new file trust security model by automating project-level trust prompts.
>
> **Key points:**
> - Emacs 30 introduced a strict trust model to address CVE-2024-53920, defaulting files to untrusted and disabling features like Flymake diagnostics.
> - To prevent users from entirely disabling this safety check, the `trust-manager` package automates project-level trust authorizations.
> - It automatically trusts user configurations (init files) and items on the load path, while using a mode-line indicator to easily grant trust to new files.
> - Commenters critique broad permissions granted to developer tooling for simple tasks like autocomplete and call for better sandboxing.
>
> **Concept links:** [[Emacs]], [[Software Trust Models]], [[CVE-2024-53920]], [[Developer Tooling]], [[Sandboxing]]
>
> **Suggested connections:**
> - [[Software Trust Models]] — balancing user experience friction with security boundaries in extensible environments.
> - [[CVE-2024-53920]] — the specific vulnerability history of arbitrary code execution through Emacs file loading.
<!-- ai-summary:end -->

# [Towards Trust in Emacs](https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html)

## Digest Summary
Emacs versions ≤ 30 treated all files as trusted, leading to vulnerabilities such as CVE‑2024‑53920. Version 30 added an explicit trust model that defaults files to untrusted and disables risky features (e.g., the Emacs‑Lisp Flymake backend) unless a buffer is marked trusted, but this creates friction for users.  

**trust‑manager** (available on MELPA) addresses this by:
- Providing `trust-manager-mode` which prompts once per project to trust or distrust it, storing the choice in `trust-manager-trust-alist`.
- Automatically trusting the init file, early init file, custom file, and all directories on `load-path`.
- Adding a red “?” indicator in the mode line of untrusted buffers; clicking it marks the buffer trusted and re‑enables disabled features.
- Supplying commands `trust-manager-set-project-trust` and `trust-manager-set-file-trust` for manual adjustments, and integrating with `project-forget-project` to clear stale entries.
- Allowing inspection and editing via `M-x trust-manager-customize`.

Installation is via `M-x package-install trust-manager`, with source at  and GitHub mirror. The package aims to preserve Emacs 30’s security improvements while minimizing workflow interruption.

## Discussion Summary
The comments express dissatisfaction with the current permission model, criticizing the requirement to grant broad read/write and network access for a feature that primarily provides code autocomplete. Users call for improved sandboxing, isolation, and more granular permissions to protect privacy and security. The overall sentiment is negative toward the existing approach, emphasizing a desire for tighter controls while retaining the functionality they need.

---

## Full Article

Created on [2026-04-15], last updated [2026-04-15]

Emacs has some serious trust issues. Up to version 30, it didn’t
differentiate between trusted and untrusted files, and in effect treated
all files as trusted. This implicit trust manifested in various
security issues, such as the arbitrary code execution vulnerability
CVE-2024-53920 which [I reported](https://eshelyaron.com/posts/2024-11-27-emacs-aritrary-code-execution-and-how-to-avoid-it.html) a couple of years ago.

To fix this vulnerability, Emacs 30 introduced an explicit notion of
trust, where some potentially risky features are only enabled for
trusted files. It also set all files to untrusted by default.

In theory, this is a safe default, but it is not very convenient,
and the problem with security measures that cause too much friction is
that users tend to disable them in order to get on with their work.
To fulfill its security purposes, a good trust system needs to stay
out of your way. Enter [`trust-manager`](https://github.com/eshelyaron/trust-manager), my new trust management
package for Emacs.

But first, let’s take a closer look at a common pitfall of the current
Emacs trust situation. Then we’ll see how `trust-manager` solves it.
The most prominent Emacs feature that has been limited to trusted
files for security reasons is the Emacs Lisp Flymake backend, which is
responsible for on-the-fly diagnostics in Emacs Lisp code. The way it
works is that when Emacs invokes the Flymake backend to retrieve
diagnostics in a given buffer (file), a check is performed to see
whether the buffer is trusted according to the current trust settings.
If it was not marked as trusted, then the backend is disabled, and you
get a message saying:

```
Disabling elisp-flymake-byte-compile in foo.el (untrusted content)
```

Now, seeing this, you know that your on-the-fly diagnostics are gone,
and you also know why; but even if you actually do trust this buffer,
you don’t have any immediate way of telling that to Emacs, and getting
your diagnostics back and your job done.

This annoyance pushes many users to configure overly broad trust
settings, and indeed a quick search among Emacs configurations
published on GitHub reveals users going as far as disabling the
trust mechanism altogether. This is exactly the kind of friction
`trust-manager` is designed to eliminate.

Granting trust just-in-time with `trust-manager`
------------------------------------------------

My new `trust-manager` package, which is available from MELPA, helps
you grant trust just-in-time, with minimal friction. You enable
`trust-manager-mode` in your init file and forget about trust
configuration. The first time you visit a file in a given project,
`trust-manager-mode` asks you whether you trust that project. If you
say yes, it marks the project directory as trusted and remembers your
choice. If you say no, that’s remembered too. The next time you
visit a file in that same project, no questions are asked. If you
change your mind, you can edit your trust settings at any time with
`trust-manager-customize`.

The commentary section of `trust-manager.el` details useful tips and
customization options that you may want to check out, but usually all
you need in terms of configuration is:

Beyond just-in-time prompting, `trust-manager-mode` also takes care of
some files that you most certainly trust already: your init file, your
early init file, your custom file, and all directories on your
`load-path`. These are marked as trusted as soon as the mode is
enabled, so Emacs Lisp features work without interruption in your own
configuration files and in the ELisp source files that come with Emacs
and packages you install.

An additional improvement that `trust-manager` brings is a mode line
indicator for untrusted buffers. In untrusted Emacs Lisp buffers,
you’ll see a small red `?` in the mode line. This indicator serves
two purposes: it reminds you that some features may be disabled in
this buffer, and it lets you act on that information right away:
clicking on it marks the buffer as trusted and immediately re-enables
any features that were waiting for trust. Here’s a quick demo:

![trust-manager.gif](https://eshelyaron.com/assets/trust-manager.gif)

Your trust choices are stored in the user option
`trust-manager-trust-alist`. You can inspect and edit it directly
with `M-x trust-manager-customize`, or use the dedicated commands
`trust-manager-set-project-trust` and `trust-manager-set-file-trust`
to mark specific directories or files as trusted or untrusted without
going through the Customize interface.

`trust-manager-mode` also hooks into `project-forget-project`: when you
ask Emacs to forget a project, its trust entry is cleared automatically,
so stale trust settings don’t linger.

Conclusion
----------

Emacs 30’s trust system is a meaningful step forward for security, but
its out-of-the-box experience leaves some room for improvement.
`trust-manager` helps you grant trust just-in-time, so you can keep your
settings secure without compromising on functionality.

You can install `trust-manager` from MELPA with `M-x package-install`,
or find the source at <https://git.sr.ht/~eshel/trust-manager> or at
<https://github.com/eshelyaron/trust-manager>.