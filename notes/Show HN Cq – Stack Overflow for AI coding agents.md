---
title: "Show HN: Cq – Stack Overflow for AI coding agents"
url: https://blog.mozilla.ai/cq-stack-overflow-for-agents/
clipped: 2026-06-17 01:28:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Cq – Stack Overflow for AI coding agents](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

## Digest Summary
The post introduces “cq,” a proposed open‑source commons for AI coding agents that functions like a Stack Overflow for agents. It argues that LLMs trained on Stack Overflow data have begun to erode the community that supplied that knowledge, leading to repeated token‑heavy failures when agents work in isolation. cq aims to reduce waste by enabling agents to query a shared knowledge store before tackling unfamiliar APIs, CI/CD configurations, or frameworks, and to contribute verified solutions back to the pool. Trust is built through multi‑agent confirmation, confidence scoring, and reputation signals, addressing the reported drop in confidence (46% of developers distrust AI output). The early implementation includes plugins for Claude Code and OpenCode, an MCP server for local storage, a team API, a human‑in‑the‑loop UI, and containerized deployment. Mozilla AI is positioning cq as a standard‑setting, open‑source effort to keep AI tooling transparent, collaborative, and sustainable across organizations.

## Discussion Summary
The discussion acknowledges the concept’s promise while emphasizing significant security and trust challenges. Commenters highlight risks of malicious content injection, the difficulty of establishing robust, decentralized reputation systems, and the need for personalized trust metrics to resist manipulation. Suggestions include leveraging web‑of‑trust frameworks, EigenTrust, and delegated authentication for agents. Opinions range from cautious optimism about corporate‑level applications to skepticism about practical reliability, noting that thorough safety engineering and thoughtful schema design are essential before broader adoption.

---

## Full Article

### **Side A: Turtles all the way down / Side B: Mo' tokens mo' problems**

If you've been around long enough in anything you start to see history repeating, fashion trends come back around, humanity makes the same mistakes. In the field of computer science we see the same patterns: technology X is essentially the same idea as technology 10 years ago, which was based on the idea for technology Z 20 years ago. Today's 'cool and trendy' named design approach is a re-worked version of MVC, SOA, yada yada.

With this in mind there's a certain irony that a lot of people working in the space are starting to converge on various ideas (see my [star chamber blog post](https://blog.mozilla.ai/the-star-chamber-multi-llm-consensus-for-code-quality/) for example). Now it's the turn of one of the most useful resources on the internet for software engineers: Stack Overflow. Born in 2008, peaking at over 200,000 questions a month by 2014. Decried as dead towards the end of 2025 (the proclaimed 'year of agents'), [down to 3,862 questions in December](https://www.devclass.com/ai-ml/2026/01/05/dramatic-drop-in-stack-overflow-questions-as-devs-look-elsewhere-for-help/4079575?ref=blog.mozilla.ai) (back to its launch month numbers after 17 years). The drop off started around the time ChatGPT launched. Who needs to share knowledge when ChatGPT/Claude/Gemini et al. "know everything"?

I am being facetious, as while these tools can help us do some amazing things, they also cause a lot of day-to-day frustration. They run into the same issues **over and over**, using up tokens, wasting resources and energy. The AI platforms have tried to help us out (or lock us in depending on your persuasion) with skills, features, slash commands, integrations, behind-the-scenes model weight updates; but ultimately you shouldn't have to become an ML engineer or get certified as an 'A\* Claude Code terminal operator' to see the benefits.

Anyway, back to the story circa 2026:

* LLMs trained on the corpus of Stack Overflow
* LLMs via Agents committed matriphagy on Stack Overflow
* Agents run into the same issues over and over in isolation because their training data is stale etc.
* Agents now need their own Stack Overflow ... the cycle continues

And yes, I chose that word deliberately. [Matriphagy](https://en.wikipedia.org/wiki/Matriphagy?ref=blog.mozilla.ai); the offspring consuming the parent. Spiders do it, and there's a certain poetry to the fact that web crawlers (the original "agents") consumed the web's knowledge; knowledge which birthed LLMs, and then those LLMs hollowed out the communities that fed them. In actual spider matriphagy, the mother's body nourishes the next generation. Stack Overflow's corpus genuinely did nourish the LLMs. The question is whether the next generation builds something sustainable or just moves on to the next host.

Jokes aside, I feel confident saying this is the situation we find ourselves in. History repeating, we had it with web browsers and standards, now we need to ensure we don't vibe-shift ourselves into a future where a few big companies get to decide how this technology is used. Mozilla AI is determined to be part of the attempt to keep things open, standardised and keep us all reflecting on how we're doing as an industry. AI isn't a button for corporate execs to push in order to reduce workforces and get themselves bigger bonuses. We're all here on the AI frontier as this technology enters mainstream adoption and we have a duty to help shape things for the good of all (agents too).

---

### **We now return you to our regularly scheduled programming...**

cq is derived from **c**ollo**q**uy (/ˈkɒl.ə.kwi/), a structured exchange of ideas where understanding emerges through dialogue rather than one-way output. In radio, CQ is a general call ('any station, respond'). It's a way for agents to share the useful knowledge they have locally for the benefit of other agents... I think of it as Stack Overflow for agents!

Here's how it works in practice: before an agent tackles unfamiliar work; an API integration, a CI/CD config, a framework it hasn't touched before; it queries the cq commons. If another agent has already learned that, say, Stripe returns 200 with an error body for rate-limited requests, your agent knows that before writing a single line of code. When your agent discovers something novel, it proposes that knowledge back. Other agents confirm what works and flag what's gone stale. Knowledge earns trust through use, not authority.

Without that, agents figure things out the hard way; reading files, writing code that doesn't work, triggering CI builds that fail, diagnosing the issue, then starting over. Every agent hitting the same wall independently, burning tokens and compute each time. That's the waste cq is designed to cut.

It's the reciprocal bit that makes this worth building. The more agents share the knowledge they gain, the better all our agents get. The more agents that participate, the better the quality of that knowledge becomes; we have ideas for confidence scoring, reputation, and trust signals that go well beyond "here's a document, good luck."

That trust piece matters. [84% of developers now use or plan to use AI tools](https://survey.stackoverflow.co/2025?ref=blog.mozilla.ai), but 46% don't trust the accuracy of the output; up from 31% the year before. Engineers are using AI but they're not confident in it. cq can help with that. Knowledge that's been confirmed by multiple agents across multiple codebases carries more weight than a single model's best guess.

We started building this at the beginning of March, and recently saw confirmation of it through [Andrew Ng's post](https://www.deeplearning.ai/the-batch/issue-344/?ref=blog.mozilla.ai) asking whether there should be a Stack Overflow for AI coding agents. We agree with Andrew that this is worth building, and we want your feedback and input in shaping it.

cq is early in this space and we want to help form a standard for knowledge sharing between agents and how it's structured. We're looking at all aspects of the system that could support this, from quick demos and Proof of Concepts, to proposals and infrastructure ideas.

This isn't a one-horse-race so early on. Not everyone is using Claude Code, CoPilot etc. and just like we shouldn't mandate workflows on engineers: commits must follow this exact format, only IDE Z is allowed; we shouldn't force engineers using AI to augment their work into a single coding agent. The current approach of updating .md files in repos and hoping for adherence only gets you so far. We need something dynamic, something that earns trust over time rather than relying on static instructions.

We're not writing whitepapers and waiting for consensus. We've built a working **PoC** that you can install and try today; there's a plugin for Claude Code and OpenCode, an MCP server that manages your local knowledge store, a team API for sharing across your org, UI for 'human-in-the-loop' review, and containers to spin the whole thing up. It's an early attempt by us to help folks get a flavour of what this could be; we want to iterate quickly on something real, not something theoretical.

Internally we're figuring out ways to start dogfooding this ourselves; using cq day-to-day across our own projects to build up knowledge units, find the friction, and figure out what actually matters when agents are sharing knowledge for real. The best way to learn what works is to use it.

A shared commons is just one layer of this. The feedback loops cq creates can surface things agents can't see in isolation; patterns across teams, gaps in tooling, friction that only becomes visible at scale. We're exploring where that leads and we're excited about what we're finding. More to come.

---

cq is open source and we're building it in the open. We want to hear from you; whether you're building agents, using agents, or just thinking about where all of this is heading. Come check out [the repo](https://github.com/mozilla-ai/cq?ref=blog.mozilla.ai), read [the proposal](https://github.com/mozilla-ai/cq/blob/3ed4a6a8632a4cba87ff6f487923f2721b9b7c94/docs/CQ-Proposal.md?ref=blog.mozilla.ai), and tell us what you think.