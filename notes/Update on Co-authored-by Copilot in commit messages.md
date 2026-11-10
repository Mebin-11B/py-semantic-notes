---
title: "Update on \"Co-authored-by: Copilot\" in commit messages"
url: https://github.com/microsoft/vscode/issues/314311
clipped: 2026-06-17 01:07:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Update on "Co-authored-by: Copilot" in commit messages](https://github.com/microsoft/vscode/issues/314311)

## Digest Summary
In VS Code 1.110 a setting `git.addAICoAuthor` was introduced to append “Co‑authored‑by: Copilot ” to commit messages. The setting offered three modes: `off` (no attribution), `chatAndAgent` (attribution when code is generated via chat), and `all` (attribution for any AI‑generated code). The default was `off`. In version 1.117 the default was changed to `all`, but a bug caused the attribution to be added even when the `disableAIFeatures` option was enabled, mistakenly marking non‑Copilot completions as Copilot‑authored. The default was reverted to `chatAndAgent` in 1.118, and users could still disable it by setting the value to `off`.  

For the upcoming 1.119 release (rollout beginning 5 May), the default is restored to `off` and the feature is forced disabled when `disableAIFeatures` is true. Future changes will ensure attribution is added only for AI‑related changes, require explicit user consent before inserting a commit trailer, and consider switching to an “Assisted‑by” format that can include model details. The team is also reviewing testing and release processes to prevent similar issues.

## Discussion Summary
The comments express strong dissatisfaction with the lack of explanations for recent changes, emphasizing a need for transparency. Users describe alternative methods for tracking content authorship, rejecting imposed attribution labels as intrusive. There is pronounced criticism of a major technology corporation, accusing it of overreach, non‑compliance with legal agreements, and advocating for its division or even nationalization of its products. Overall sentiment is negative, focusing on demands for clearer communication, resistance to forced metadata, and broader concerns about corporate control of technology.

---

## Full Article

What happened?
--------------

In 1.110, we added a setting to add Copilot as coauthor in commit messages by appending `Co-authored-by: Copilot copilot@github.com`. The setting `git.addAICoAuthor` has three different values:

* `off` - no attribution no matter whether Copilot assisted or not with the code in this commit
* `chatAndAgent` - add attribution if the commit contains code that was generated using the chat feature
* `all` - add attribution if the commit contains any kind of AI-generated code (chat, inline completions, NES)

The default value of the setting was `off`.

In 1.117 (public rollout started 4/22), we changed the setting default to `all`. There was a bug in the code that was not found in testing that attributed non-Copilot code completions to Copilot. This resulted in commit messages containing `Co-authored-by: Copilot copilot@github.com` even when the `disableAIfeatures` setting was turned on. This issue is tracked in [#313064](https://github.com/microsoft/vscode/issues/313064).

Because of the bug, we changed the setting value to `chatAndAgent` in 1.118 (public rollout started 4/29).

You can disable the functionality by explicitly turning the feature off in user settings:  
`"git.addAICoAuthor": "off"`.

What is happening now?
----------------------

1. We reverted the default for the AI attribution feature back to `off`. We also ensure that the feature is disabled when `disableAIFeatures` is set to true no matter the value of `git.addAICoAuthor`. This was done in [Change default for git.addAICoAuthor to off #313931](https://github.com/microsoft/vscode/pull/313931). These fixes will be tested and released in 1.119 (public rollout starting 5/6).
2. We are reviewing our test and release processes for gaps to ensure we prevent similar issues in the future.

What will happen to the feature?
--------------------------------

Thank you for all your feedback. We'll make/retain the following changes:

1. The attribution is never applied for changes that are not AI-related.
2. Before adding a commit trailer, the user will have to give consent, no matter the default value of the setting.
3. We'll review the attribution message. A better approach might be using the approach of "assisted-by" attribution as described in [Add `Assisted-by` instead of `Co-authored-by` for AI agents #313962](https://github.com/microsoft/vscode/issues/313962).
4. The same approach would allow us to add model information as tracked in [Agent co author | add specific model information to commit #297353](https://github.com/microsoft/vscode/issues/297353).

We will work on these improvements and iterate with the community via issues and discussions on GitHub to make sure the bugs are fixed and concerns are addressed.