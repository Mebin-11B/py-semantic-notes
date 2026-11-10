---

title: "There is an AI code review bubble"
url: https://www.greptile.com/blog/ai-code-review-bubble
clipped: 2026-06-17 01:52:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AI code review
  - developer tools
  - automation pipelines
  - software testing
  - AI agent workflow
related:
  - "[[AI Code Review]]"
  - "[[Developer Tools]]"
  - "[[Automation Pipelines]]"
  - "[[Software Testing]]"
  - "[[AI Agent Workflow]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Greptile outlines its strategy to differentiate in a crowded AI code review market by focusing on independent validation, background automation, and Claude Code integrations.
>
> **Key points:**
> - Greptile argues that code review agents should be independent of code generation agents to avoid conflict of interest in validation.
> - The company focuses on a zero-UI, background pipeline automation approach, predicting that human engineers will eventually oversee code merge decisions autonomously handled by agents.
> - A feedback loop integrated with Claude Code allows LLMs to pull and resolve Greptile's comments iteratively until no issues remain.
> - The AI code review market is experiencing rapid expansion and a "bubble" of competition from both IDEs/coding agents and pure-play review agents.
>
> **Concept links:** [[AI Code Review]], [[Developer Tools]], [[Automation Pipelines]], [[Software Testing]], [[AI Agent Workflow]]
>
> **Suggested connections:**
> - [[AI Agent Workflow]] — on how independent coding and review agents interact to automate PR merges.
> - [[Developer Tools]] — regarding the transition toward autonomous software validation pipelines.
> - [[AI Code Review]] — comparing pure-play review agents with integrated IDE models.
<!-- ai-summary:end -->

# [There is an AI code review bubble](https://www.greptile.com/blog/ai-code-review-bubble)

## Digest Summary
Greptile notes a rapid expansion of AI‑driven code review tools, listing major players (OpenAI, Anthropic, Cursor, Augment, Cognition, Linear) and pure‑review agents (Greptile, CodeRabbit, Macroscope, YC startups). Its differentiation rests on three pillars:

- **Independence:** Greptile separates the reviewer from any code‑generation function, refusing to ship a coding agent and arguing that an auditor should not author the code it validates.  
- **Autonomy:** The service is built as a background automation (“pipes”) without a dedicated UI, aiming for near‑full automation of code validation—review, test, and QA—so human engineers focus on design and intent.  
- **Feedback loops:** Integration with Claude Code lets an LLM fetch and resolve Greptile comments iteratively, looping until no new issues appear; ambiguous cases trigger Slack alerts to the human.

Greptile envisions a workflow where a human issues a ticket, a coding agent creates a PR, and an independent review agent approves and merges it. It cites adoption by enterprise customers, including two of the “Mag7,” and positions its approach as a long‑term, low‑switch‑cost solution in a market where code‑validation automation is expected to dominate.

## Discussion Summary
The comments express mixed views on AI‑driven code review. Many users report low signal‑to‑noise ratios, limited contextual understanding, and redundancy with existing linters or human reviewers, seeing the tools as premature or marketing‑driven. Some note occasional bug detection that humans miss, but overall trust remains low, with concerns about over‑reliance, integration hurdles, and loss of nuanced judgment. A few highlight successful integrations or specific use cases, while the dominant sentiment questions the current value, feasibility, and strategic focus of such products.

---

## Full Article

Today, we're in the [hard seltzer](https://www.youtube.com/watch?v=iBpgqRbEFVg) era of AI code review: everybody's doing them. OpenAI, Anthropic, Cursor, Augment, now Cognition, and even Linear. Of course, there's also the "White Claws" of code review: pure-play code review agents like Greptile (that's us!), CodeRabbit, Macroscope, and a litter of fledgling YC startups. Then there are the adjacent Budweisers of this world:

Amazingly, these two were announced practically within 24 hours of each other.

As the proprietors of an, er, AI code review tool suddenly beset by an avalanche of competition, we're asking ourselves: what makes us different?

**How does one differentiate?**

Based on our benchmarks, we are uniquely good at catching bugs. However, if all company blogs are to be trusted, this is something we have in common with every other AI code review product. One just has to try a few, and pick the one that feels the best.

Unfortunately, code review performance is ephemeral and subjective, and is ultimately not an interesting way to discern the agents before trying them. It's useless for me to try to convince you that we're the best. You should just try us and make up your own mind.

Instead of telling you how our *product* is differentiated, I am going to tell you how our *viewpoint* is differentiated - how we think code review will look in the long-term, and what we're doing today to prepare our customers for that future.

Our thesis can be distilled into three pillars: independence, autonomy, and feedback loops.

We *strongly* believe that the review agent should be different from the coding agent. We are opinionated on the importance of *independent* code validation agents. In spite of multiple requests, we have never shipped codegen features. We don't write code; an auditor doesn't prepare the books, a fox doesn't guard the henhouse, and a student doesn't grade their own essays.

Today's agents are better than the median human code reviewer at catching issues and enforcing standards, and they're only getting better. It's clear that in the future a large percentage of code at companies will be auto-approved by the code review agent. In other words, there will be some instances where a human writes a ticket, an agent writes the PR, and another agent validates, approves, and merges it.

This might seem far-fetched but the counterfactual is Kafkaesque. A human rubber-stamping code being validated by a super intelligent machine is the equivalent of a human sitting silently in the driver's seat of a self-driving car, "supervising".

If agents are approving code, it would be quite absurd and perhaps non-compliant to have the agent that *wrote* the code also *approve* the code. Only once would you have X write a PR, then have X approve and merge it to realize the absurdity of what you just did.

Something that Greptiles generally agree on is that everything that *can* be automated, *will* be automated.

Code validation - which to us is the combination of review, test, and QA, is an excellent candidate for full automation. It's work that humans don't want to do, and aren't particularly good at. It also requires little in the way of creative expression, unlike programming. In addition, success is generally pretty well-defined. Everyone wants correct, performant, bug-free, secure code.

While some other products have built out great UIs for humans to review code in an AI-assisted paradigm, we have chosen to build for what we consider to be an inevitable future - one where code validation requires vanishingly little human participation. We have no code review UI, and view ourselves as more of a background automation or "pipes" product. Human engineers should be focused only on two things - coming up with brilliant ideas for what should exist, and expressing their vision and taste to agents that do the cruft of turning it all into clean, performant code.

Not long ago, we released our Claude Code plugin. It can do many things - but most notably, you can ask Claude Code to pull down and address Greptile's comments from the PR. You can ask it to keep going until there are no new comments, waiting a few minutes for a review after each push.

This is a step towards the future we're excited about: Human expresses intent, coding agent executes, validation/review agent finds issues and hands them back - kicking off a loop until it approves and merges. If there is ambiguity at any point, the agents Slack the human to clarify.

The question of how these things are different is important. Unlike picking IDEs and coding agents that ostensibly have low switching costs, code review products are harder to rip out, so your decision will very likely turn out to be a long-term one, especially if you're a large company.

We've been around for about as long as AI code review has been around. It has gone from a fringe interest of the world's most adventurous vibecoders to a mainstream product that our enterprise users (including two of the Mag7) often describe as a "no-brainer" purchase.

Yet, our guess on where this goes is about as good as anyone else's. Meanwhile, we'll keep doing what we've always done - trying to make things our users love.