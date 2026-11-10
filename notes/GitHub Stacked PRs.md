---
title: "GitHub Stacked PRs"
url: https://github.github.com/gh-stack/
clipped: 2026-06-17 01:17:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [GitHub Stacked PRs](https://github.github.com/gh-stack/)

## Digest Summary
GitHub Stacked PRs enable developers to organize related changes as an ordered series of pull requests, each building on the previous one and ultimately merging into the main branch in a single action. The UI displays a stack map, allowing reviewers to navigate layers, see individual diffs, and enforce branch‑protection rules against the final target branch. CI runs for each PR as if targeting the final branch. The `gh stack` CLI extension (installable via `ghextension install github/gh-stack`) automates local workflow: creating stacked branches, performing cascading rebases, pushing branches, and opening PRs with correct base references. Stacks can be merged wholly or partially; after a merge, remaining PRs are automatically rebased to target the base branch. An AI agent integration (`npx skills add github/gh-stack`) lets coding agents manipulate stacks. The tool aims to improve reviewability, reduce merge conflicts, and maintain context for large changes.

## Discussion Summary
The comments show strong enthusiasm for native stacked PR support, citing benefits for breaking large changes into smaller, reviewable units, especially in monorepos and long‑running feature work. Users appreciate the UI navigation widget and expect smoother rebasing, conflict handling, and AI‑assisted workflows, while many also rely on external tools like the gh‑stack CLI. Skepticism remains about added complexity, redundancy with existing commit‑level review, limitations for cross‑repo stacks, and the need for clearer merge semantics. Concerns about documentation, domain authenticity, and the learning curve also appear throughout.

---

## Full Article

Stacked PRs, Native in GitHub

Arrange pull requests in an ordered stack and merge them all in one click. Each PR represents one focused layer of your change, reviewed independently and landed together.

Simplified Stack Management

Navigate between PRs in your stack from the GitHub UI, check the status of every layer at a glance, and trigger a cascading rebase across the entire stack with one click.

Powerful CLI

The `gh stack` CLI makes it easy to create stacks, perform cascading rebases, push branches and create PRs, and navigate between layers — all from your terminal.

AI Agent Integration

Run `gh skill install github/gh-stack` to teach your AI coding agents how to work with stacks. Break up a large diff into a stack or develop with stacks from the start.

Large pull requests are hard to review, slow to merge, and prone to conflicts. Reviewers lose context, feedback quality drops, and the whole team slows down. Stacked PRs solve this by breaking big changes into a chain of small, focused pull requests that build on each other — each one independently reviewable.

A **stack** is a series of pull requests in the same repository where each PR targets the branch of the PR below it, forming an ordered chain that ultimately lands on your main branch.

main    PR #1 · auth-layer    PR #2 · api-endpoints    PR #3 · frontend     ← bottom ← top

GitHub understands stacks end-to-end: the pull request UI shows a **stack map** so reviewers can navigate between layers, branch protection rules are enforced against the **final target branch** (not just the direct base), and CI runs for every PR in the stack as if they were targeting the final branch.

**While the `gh stack` CLI makes the local workflow seamless, it is entirely optional.** You can create and manage Stacked PRs directly via the GitHub UI, the API, or your standard Git workflow. If you choose to use the CLI, it handles creating branches, managing rebases, pushing to GitHub, and creating PRs with the correct base branches. On GitHub, the PR UI gives reviewers the context they need — a stack map for navigation, focused diffs for each layer, and proper rules enforcement.

When you’re ready to merge, you can merge all or a part of the stack. Each PR can be merged directly or through the merge queue. **If you want to merge multiple PRs at once (e.g., the bottom two PRs in a stack), simply wait for CI to pass on those specific layers, and you can merge them in a single step.** After a merge, the remaining PRs in the stack are automatically rebased so the lowest unmerged PR targets the updated base branch.

```
# Install the CLI extension



gh extension install github/gh-stack



# Alias `gh stack` as `gs` for easier use (optional)



# Start a stack (creates and checks out the first branch)



# Create new layers in the stack (creates and checks out each new branch)
```

Ready to dive in? Start with the [Quick Start guide](https://github.github.com/gh-stack/getting-started/quick-start/) or read the [full overview](https://github.github.com/gh-stack/introduction/overview/).