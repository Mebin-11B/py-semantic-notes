---
title: "What Is Agentic Engineering?"
url: https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/
clipped: 2026-06-17 01:32:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What Is Agentic Engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)

## Digest Summary
Agentic engineering refers to developing software with the assistance of coding agents—LLM‑based systems that can both generate and execute code (e.g., Claude Code, OpenAI Codex, Gemini CLI). An agent is prompted with a goal, then iteratively produces and runs code until the goal is satisfied; code execution distinguishes these agents from pure text generators. Human engineers focus on problem definition, solution selection, and trade‑off analysis rather than manual coding. Effective use of coding agents requires supplying appropriate tools, specifying problems at the correct level of detail, and continuously verifying and refining outputs. Although LLMs do not self‑learn from errors, agents can be improved by updating prompts and tool harnesses based on observed failures. The approach aims to increase the quantity, quality, and impact of software produced. This guide outlines evolving patterns for working with coding agents, emphasizing reproducible techniques that remain relevant as the technology advances.

## Discussion Summary
Comments converge on the view that agent‑assisted coding is useful for well‑defined, narrowly scoped problems where tests and output formats are clear, but it struggles with evolving requirements and architectural decisions that demand deep domain insight. Participants stress the necessity of separate verification steps, loud failure signals, and human accountability to mitigate alignment and safety risks. The naming debate—whether to call it “agentic coding” or “agentic engineering”—is seen as secondary to recognizing these boundaries. Skepticism about industry hype and the novelty of agents is also expressed, emphasizing that the core concept predates recent LLM advances.

---

## Full Article

I use the term **agentic engineering** to describe the practice of developing software with the assistance of coding agents.

What are **coding agents**? They're agents that can both write and execute code. Popular examples include [Claude Code](https://code.claude.com/), [OpenAI Codex](https://openai.com/codex/), and [Gemini CLI](https://geminicli.com/).

What's an **agent**? Clearly defining that term is a challenge that has frustrated AI researchers since [at least the 1990s](https://simonwillison.net/2024/Oct/12/michael-wooldridge/) but the definition I've come to accept, at least in the field of Large Language Models (LLMs) like GPT-5 and Gemini and Claude, is this one:

**Agents run tools in a loop to achieve a goal**

The "agent" is software that calls an LLM with your prompt and passes it a set of tool definitions, then calls any tools that the LLM requests and feeds the results back into the LLM.

For coding agents, those tools include one that can execute code.

You prompt the coding agent to define a goal. The agent then generates and executes code in a loop until that goal has been met.

Code execution is the defining capability that makes agentic engineering possible. Without the ability to directly run the code, anything output by an LLM is of limited value. With code execution, these agents can start iterating towards software that demonstrably works.

Agentic engineering
-------------------

Now that we have software that can write working code, what is there left for us humans to do?

The answer is *so much stuff*.

Writing code has never been the sole activity of a software engineer. The craft has always been figuring out *what* code to write. Any given software problem has dozens of potential solutions, each with their own tradeoffs. Our job is to navigate those options and find the ones that are the best fit for our unique set of circumstances and requirements.

Getting great results out of coding agents is a deep subject in its own right, especially now as the field continues to evolve at a bewildering rate.

We need to provide our coding agents with the tools they need to solve our problems, specify those problems in the right level of detail, and verify and iterate on the results until we are confident they address our problems in a robust and credible way.

LLMs don't learn from their past mistakes, but coding agents can, provided we deliberately update our instructions and tool harnesses to account for what we learn along the way.

Used effectively, coding agents can help us be much more ambitious with the projects we take on. Agentic engineering should help us produce more, better quality code that solves more impactful problems.

Isn't this just vibe coding?
----------------------------

The term "vibe coding" was [coined by Andrej Karpathy](https://twitter.com/karpathy/status/1886192184808149383) in February 2025 - coincidentally just three weeks prior to the original release of Claude Code - to describe prompting LLMs to write code while you "forget that the code even exists".

Some people extend that definition to cover any time an LLM is used to produce code at all, but I think that's a mistake. Vibe coding is more useful in its original definition - we need a term to describe unreviewed, prototype-quality LLM-generated code that distinguishes it from code that the author has brought up to a production ready standard.

About this guide
----------------

Just like the field it attempts to cover, *Agentic Engineering Patterns* is very much a work in progress. My goal is to identify and describe patterns for working with these tools that demonstrably get results, and that are unlikely to become outdated as the tools advance.

I'll continue adding more chapters as new techniques emerge. No chapter should be considered finished. I'll be updating existing chapters as our understanding of these patterns evolves.