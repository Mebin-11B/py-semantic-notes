---
title: "Claude Platform on AWS"
url: https://claude.com/blog/claude-platform-on-aws
clipped: 2026-06-17 01:03:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Claude Platform
  - AWS
  - Amazon Bedrock
  - Anthropic
  - AI APIs
  - Data Residency
related:
  - "[[Show HN A context-aware permission guard for Claude Code]]"
  - "[[What it feels like to work with Mythos]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Anthropic launches Claude Platform on AWS, providing native Claude Console features and model APIs directly through AWS billing and console channels.
>
> **Key points:**
> - Grants access to the Claude Console (prompt generators, evaluation tools, agent management) and the latest Opus, Sonnet, and Haiku models.
> - Differentiates from Claude on Amazon Bedrock by running directly under Anthropic control with processing outside the AWS boundary.
> - Bedrock processes data strictly inside the AWS boundary for users with rigorous regional data residency requirements.
> - Billing is integrated into AWS, though Bedrock private-offer discounts do not automatically apply.
>
> **Concept links:** [[Claude Platform]], [[AWS]], [[Amazon Bedrock]], [[Anthropic]], [[AI APIs]], [[Data Residency]]
>
> **Suggested connections:**
> - [[Show HN A context-aware permission guard for Claude Code]] — related Claude security tools.
> - [[What it feels like to work with Mythos]] — related to Claude model capabilities.
<!-- ai-summary:end -->

# [Claude Platform on AWS](https://claude.com/blog/claude-platform-on-aws)

## Digest Summary
The Claude Platform on AWS offers native Claude API features and includes the Claude Console for development, featuring a prompt improver, generator, and evaluation tools. Available models are Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5, with future releases added automatically. Two deployment options exist:

- **Claude Platform on AWS** – Anthropic runs the service; data is processed outside AWS. Suitable for organizations seeking the full Claude Platform experience.
- **Claude on Amazon Bedrock** – AWS processes data within its infrastructure, meeting strict regional residency or exclusive‑AWS processing requirements.

The platform is currently live; users can begin via the Claude Platform on AWS site or documentation. Existing Bedrock private‑offer customers must coordinate with their Anthropic or AWS account executive to apply discounts, which cannot be retroactively applied.

## Discussion Summary
The comments show widespread confusion over the distinction between the new Claude‑on‑AWS offering and the existing Bedrock integration, with many users uncertain about where data is processed and what benefits it provides. Several participants note possible convenience for billing and infrastructure automation, while others question any real technical advantage and express skepticism about the product’s purpose and clarity. Concerns about data residency, latency, and operational risk appear alongside cautious interest in tighter AWS‑centric management, resulting in a mixed but predominantly uncertain overall sentiment.

---

## Full Article

What's included
---------------

The Claude Platform on AWS includes native platform features, like:

Claude Platform on AWS customers also get access to the Claude Console, Anthropic's development environment for building and testing with Claude. The Console includes management for agents, skills, environments, vaults, observability tools, and more.

Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5 are available, with new models shipping on the Claude Platform on AWS as they launch.

Choosing the right path for developers
--------------------------------------

Both the Claude Platform on AWS and Claude on Amazon Bedrock enable AWS customers to build on Claude models. The difference is in who operates the service and which features are available.

The **Claude Platform on AWS** is a first of its kind offering for Anthropic, giving you all native Claude API features from day one. Anthropic operates the service and data is processed outside the AWS boundary. This is a good option for companies that want the full Claude Platform experience.

**Claude on Amazon Bedrock** keeps AWS as the data processor and operates within the AWS boundary. This is a good fit for companies that have strict regional data residency requirements or need their data processed exclusively within AWS's infrastructure.

Getting started
---------------

The Claude Platform on AWS is available today. To get started, visit the [Claude Platform on AWS](https://aws.amazon.com/claude-platform/) or explore the [documentation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

If you have an existing Bedrock private offer, please contact your Anthropic or AWS account executive before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before a Claude Platform private offer is accepted.