---
title: "We stopped AI bot spam in our GitHub repo using Git's –author flag"
url: https://archestra.ai/blog/only-responsible-ai
clipped: 2026-06-17 01:00:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - open source collaboration
  - git operations
  - spam mitigation
related:
  - "[[Open Source Collaboration]]"
  - "[[Git Operations]]"
  - "[[Spam Mitigation]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** To combat low-quality AI-generated bot spam in their repository, the Archestra team implemented a GitHub "prior contributors" whitelist bypass hack using Git's `--author` flag.
>
> **Key points:**
> - Archestra's project issues and PRs were flooded by automated AI bots posting hallucinated implementation plans, creating team overhead and security risks.
> - They enabled GitHub's "Limit to prior contributors" setting, which prevents users without a commit on `main` from commenting or opening PRs.
> - To allow new human contributors, they created an onboarding form that generates a commit on `main` using the user's GitHub noreply email via `git commit --author`.
> - The whitelist workaround successfully filters bot noise while preserving the entry path for legitimate developers who complete the captcha-guarded registration.
>
> **Concept links:** [[Open Source Collaboration]], [[Git Operations]], [[Spam Mitigation]], [[Bot Management]], [[GitHub Workflows]], [[Information Quality Control]]
>
> **Suggested connections:**
> - [[Open Source Collaboration]] — processes, community guidelines, and challenges in public repository management.
> - [[Spam Mitigation]] — techniques to protect public networks and forums from automated garbage submissions.
<!-- ai-summary:end -->

# [We stopped AI bot spam in our GitHub repo using Git's –author flag](https://archestra.ai/blog/only-responsible-ai)

## Digest Summary
The Archestra team reports that AI‑generated bots have flooded their GitHub repository with low‑quality comments, PRs, and issues, drowning legitimate contributions and creating security risks. To mitigate this “AI slop,” they disabled issue, PR, and comment creation for users who have not completed an onboarding process, effectively using GitHub’s “Limit to prior contributors” setting. Since GitHub only recognises accounts with a commit on the main branch, the team devised a workaround: during onboarding they generate a commit authored with the user’s GitHub noreply email ( `+@users.noreply.github.com` ) via `git commit --author`, push it to main, and record the handle in an EXTERNAL_CONTRIBUTORS.md file via a GitHub Action. This grants the user prior‑contributor status, allowing them to comment and submit PRs. The process includes an ethical‑AI agreement and CAPTCHA. The post stresses that while AI‑driven activity inflates GitHub metrics, it harms open‑source collaboration and requires active filtering and custom workflows to preserve repository quality.

## Discussion Summary
Overall sentiment is critical of GitHub’s handling of pull‑request spam and AI‑generated contributions, highlighting security gaps where contributors gain elevated rights without robust verification. Commenters propose stronger identity checks, reputation or ELO‑style scoring, financial deposits, or real‑name requirements, while noting that simple captchas or temporary limits provide only limited relief. Frustration is expressed over the large volume of low‑quality AI PRs and the difficulty of distinguishing genuine work, with occasional acknowledgement that incremental tool improvements can help but are seen as insufficient.

---

## Full Article

Discussion on **Hacker News**:

The End of Open Source as We Know It
------------------------------------

When a few months ago GitHub shared statistics about

[celebrating an enormous contribution of AI in their product metrics](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/?utm_source=web-k2k-octoverse-cta&utm_medium=web&utm_campaign=universe25)

, completely missing the point of degraded contribution quality, we already felt that things were going south.

The first worrying moment was the

[issue we posted with a $900 bounty](https://github.com/archestra-ai/archestra/issues/1301)

. We were hoping to motivate someone to contribute and bring shiny new "MCP Apps" support to our platform. We quickly got the attention of legitimate contributors proposing plans, asking questions, submitting attempts — but soon...

AI bots arrived and blew up the issue, taking it to **253 comments total**, poisoning the conversation with pointless "implementation plans" and even pure aggression toward the maintainers!

AI accounts started flooding not just this issue — but the entire repo. Every sloppy comment triggered a notification for every team member watching the repo. Our GitHub notifications became a wall of noise. Real conversations from contributors like @ethanwater, @developerfred, and @Geetk172 — people actively working on bounties — were getting buried.

Later, the problem took the form of an epidemic. For example, just for the issue to add x.ai provider support to Archestra, we received

**[27 pull requests](https://github.com/archestra-ai/archestra/pulls?page=1&q=is%3Apr+is%3Aclosed+is%3Aunmerged+x.ai)**

, most of which

**contributors didn't even try testing**

.

One of our team members had to spend **half a day every week cleaning AI garbage out of the repo**, removing untested PRs and closing hallucinated issues. When we forgot to do so, our repo quickly became a place completely unfriendly to legitimate contributors.

Fighting Back
-------------

At first, we tried to calculate the "reputation" of contributors and built

["London-Cat"](https://github.com/archestra-ai/reputation-bot)

, a tiny bot calculating a contributor's reputation based on merged PRs and a few other signals (

[example](https://github.com/archestra-ai/archestra/issues/1301#issuecomment-3725798117)

). It obviously didn't stop the spam, but it helped us figure out "who is who".

As a next step, we built an "AI sheriff" (

[example](https://github.com/archestra-ai/archestra/pull/2843#issuecomment-3916574929)

), which obviously closed a few legitimate PRs 🤦.

The constant flow of useless AI comments and proposals was only getting worse, turning legitimate contributors away and making us reconsider: should we stop

[motivating contributions with bounties](https://github.com/archestra-ai/archestra/issues?q=is%3Aissue%20state%3Aclosed%20label%3A%22%F0%9F%92%8E%20Bounty%22)

? Should we stop

[giving fun test tasks to our job candidates](https://archestra.ai/careers)

?

We've decided that we need to fight back and insist on making our repo a comfortable and safe space for legitimate contributors, responsible AI users, newbies, and seasoned engineers.

Today we're **blocking the ability to create issues, open PRs, and leave comments for those who didn't go through the onboarding**.

![Contributor onboarding, five steps to get whitelisted](https://archestra.ai/blog/2026-04-07-onboarding.webp)

Contributor onboarding, five steps to get whitelisted

It's a nuclear option, yes. It's especially sensitive for a VC-backed startup that is measured thoroughly by GitHub activity, but we have to pull the trigger: **we value quality over quantity. We don't value metrics pumped by AI slop.**

We want Archestra to be a great piece of software that everyone can contribute to, without it being swallowed by AI bots.

Doing It in GitHub
------------------

There is no straightforward way to whitelist those who can comment or create PRs on an open source repo, so we had to hack around.

There is a setting called "Limit to prior contributors." Simple rule: if you haven't previously committed to `main`, you can't comment on issues or PRs.

![Prior contributors setting](https://archestra.ai/blog/2026-04-07-prior-contributors-setting.webp)

Prior contributors setting

The setting can't tell the difference between an AI bot and a real developer who signed up to work on a bounty. Both are "not prior contributors." Both get locked out.

GitHub defines "prior contributor" as someone whose GitHub account is the **author** of a commit on `main`. Git commits have two identity fields — **author** and **committer** — and they can be different people.

You can create a commit attributed to someone else using Git's `--author` flag. If the email matches their GitHub account, GitHub links the commit to their profile and grants them contributor status.

Every GitHub account has a noreply email: `<id>+<username>@users.noreply.github.com`. Look up the ID via the API and commit:

```
gh api users/their-username --jq '.id'

git commit \
  --author="their-username <ID+their-username@users.noreply.github.com>" \
  -m "chore: add their-username to external contributors"
```

Push to `main`, and they can comment immediately.

![Commit attributed to external user](https://archestra.ai/blog/2026-04-07-prior-contributors-commit.webp)

Commit attributed to external user

The external user shows up as the **author**, our account as the **committer**. That's all GitHub needs to consider them a prior contributor.

The full flow:

1. Onboarding on our website with ethical AI rules and a CAPTCHA: <https://archestra.ai/contributor-onboard>
2. A GitHub Action that fires on submission, looks up the user's GitHub ID, adds their handle to an `EXTERNAL_CONTRIBUTORS.md` file, and pushes a commit to `main` authored under their account.
3. The user becomes whitelisted and gets access to the repo.

Final Words
-----------

While GitHub reports massive metric growth — a substantial part of which is AI-generated — we as an open source project team have to do the heavy lifting of cleaning up AI slop from our repository and come up with esoteric workarounds to keep the level of legitimacy of our open source audience.

Slop is not only demotivating contributors who want to spend their time doing good and have to break through the wall of noise instead, it's also bringing a substantial security risk, as it happened

[in the LiteLLM repo](https://github.com/BerriAI/litellm/issues/24512)

when attackers tried to steer the conversation using AI bots.

Dear community, it's time to have a serious talk about the effect AI has on open source.

[Archestra](https://archestra.ai) is an open-source control plane for running AI agents safely in production. It runs [self-hosted in your own Kubernetes cluster](https://archestra.ai/docs/platform-deployment), putting a [deterministic policy gateway](https://archestra.ai/docs/platform-ai-tool-guardrails) between your agents and your stack. Every [LLM call](https://archestra.ai/docs/platform-llm-proxy), [tool invocation](https://archestra.ai/docs/platform-ai-tool-guardrails), and [external request](https://archestra.ai/docs/platform-mcp-gateway) gets governed with [RBAC](https://archestra.ai/docs/platform-access-control), [credential isolation](https://archestra.ai/docs/platform-secrets-management), [audit trails](https://archestra.ai/docs/platform-observability), and [cost controls](https://archestra.ai/docs/platform-costs-and-limits). Built by the ex-Grafana team.