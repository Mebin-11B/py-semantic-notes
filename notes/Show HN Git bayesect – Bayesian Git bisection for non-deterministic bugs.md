---
title: "Show HN: Git bayesect – Bayesian Git bisection for non-deterministic bugs"
url: https://github.com/hauntsaninja/git_bayesect
clipped: 2026-06-17 01:24:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Git bayesect – Bayesian Git bisection for non-deterministic bugs](https://github.com/hauntsaninja/git_bayesect)

## Digest Summary
Git _Bayesect_ is a Python tool that applies Bayesian inference to git bisect, identifying the commit where a change in event likelihood (e.g., increased test flakiness) occurs. It selects commits by greedily minimizing expected entropy and uses a Beta‑Bernoulli conjugacy to handle unknown failure rates. Users start a bisection with `git bayesect start --old ` (optionally specifying `--new`), record observations via `git bayesect pass`/`fail` (or on a specific commit), and check status with `git bayesect status`. Priors can be set per commit (`git bayesect prior --commit  --weight `), derived from filenames (`priors_from_filenames`) or commit text (`priors_from_text`) using user‑provided callbacks. The tool logs commands for reproducibility, supports undoing observations, and can run automatically with `git bayesect run `. A demo repository (`scripts/generate_fake_repo.py`) creates a fake history with a flaky script, allowing users to practice locating the commit that altered the failure probability. Installation is via `uv tool install git_bayesect`.

## Discussion Summary
The discussion is overwhelmingly positive about the Bayesian bisect approach, noting its mathematical elegance, superior accuracy to traditional bisect under flaky conditions, and the practical benefit of incorporating structural priors to further improve results. Users highlight successful benchmarks, express interest in extending the method to handle repeated test runs, noisy performance metrics, and exposing posterior confidence. Questions arise about handling varying test costs and broader applications, but overall the tool is regarded as useful, innovative, and promising for deterministic and nondeterministic bug investigation.

---

## Full Article

Bayesian git bisection!

Use this to detect changes in likelihoods of events, for instance, to isolate a commit where
a slightly flaky test became very flaky.

You don't need to know the likelihoods (although you can provide priors), just that something
has changed at some point in some direction

Or:

```
uv tool install git_bayesect
```

`git_bayesect` uses Bayesian inference to identify the commit introducing a change, with
commit selection performed via greedy minimisation of expected entropy, and using a Beta-Bernoulli
conjugacy trick while calculating posterior probabilities to make handling unknown failure rates
tractable.

See <https://hauntsaninja.github.io/git_bayesect.html> for a write up.

Start a Bayesian bisection:

```
git bayesect start --old $COMMIT
```

Record an observation on the current commit:

Or on a specific commit:

```
git bayesect pass --commit $COMMIT
```

Check the overall status of the bisection:

Reset:

Set the prior for a given commit:

```
git bayesect prior --commit $COMMIT --weight 10
```

Set prior for all commits based on filenames:

```
git bayesect priors_from_filenames --filenames-callback "return 10 if any('suspicious' in f for f in filenames) else 1"
```

Set prior for all commits based on the text in the commit message + diff:

```
git bayesect priors_from_text --text-callback "return 10 if 'timeout' in text.lower() else 1"
```

Get a log of commands to let you reconstruct the state:

Undo the last observation:

Run the bisection automatically using a command to make observations:

Checkout the best commit to test:

This repository contains a little demo, in case you'd like to play around:

```
# Create a fake repository with a history to bayesect over
python scripts/generate_fake_repo.py
cd fake_repo

# The fake repo contains a script called flaky.py
# This is a simple script that fails some fraction of the time
# At some point in the history of the repo, that fraction was changed
python flaky.py
git log --oneline

# Start the bayesection
OLD_COMMIT=$(git rev-list HEAD --reverse | head -n 2 | tail -n 1)
git bayesect start --new main --old $OLD_COMMIT

# Run a bayesection to find the commit that introduced the change
git bayesect run python flaky.py
```