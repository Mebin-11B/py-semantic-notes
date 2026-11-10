---
title: "LLMs can be exhausting"
url: https://tomjohnell.com/llms-can-be-absolutely-exhausting/
clipped: 2026-06-17 01:32:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [LLMs can be exhausting](https://tomjohnell.com/llms-can-be-absolutely-exhausting/)

## Digest Summary
The author reflects on exhaustion when using LLMs such as Claude and Codex and identifies two main technical pain points: degraded prompt quality due to mental fatigue and slow, context‑heavy feedback loops. Fatigue leads to incomplete prompts, interruptions, and poorer model outputs, while iterative tasks (e.g., parsing large files) require repeated re‑parsing, inflating the context window and slowing the cycle. To mitigate these issues, the author recommends:

- Recognize when prompting feels uncertain or impatient and pause to avoid “doom‑loop” degradation.  
- Write highly descriptive prompts with clear end‑state expectations; confidence in the prompt correlates with better results.  
- Treat slow feedback loops as the target problem: start a fresh session, define explicit success criteria (e.g., reproduce a failure case within five minutes), and let the LLM propose optimizations.  
- Apply a test‑driven approach, asking the model to generate minimal reproducible examples and leverage levers for faster iteration, which reduces context consumption and debugging time.

Overall, the piece frames exhaustion as a skill‑management issue, emphasizing disciplined prompting and engineered feedback cycles to improve LLM productivity.

## Discussion Summary
Comments converge on the view that using LLMs for code generation shifts work from writing to intensive verification, creating higher cognitive load and fatigue. Review of AI‑produced code is described as more draining than manual coding, especially under corporate mandates for large pull requests. Several participants suggest mitigating strategies such as test‑driven prompts, limiting concurrent agent sessions, asynchronous workflows, and prompt libraries. Opinions differ on whether the difficulty stems from skill gaps or inherent tool design, but most agree the current workflow can lead to burnout without careful process adjustments.

---

## Full Article

LLMs can be absolutely exhausting
=================================

*15 Mar, 2026*

Some days I get in bed after a tortuous 4-5 hour session working with Claude or Codex wondering what the heck happened. It's easy to blame the model - there's so many options to choose from:

1. They're dumbing down the model to save money.
2. Context rot!
3. Codex/Claude Code/[insert harness] is getting bloated.

It's not uncommon for me to come back to the problem the next day, my own context window cleared from rest, and find a fast and fulfilling path forward with the help of the LLM. What's going on?

I'm tired & experiments are too slow
------------------------------------

### As I get more tired, the quality of my prompts degrade

This one seems pretty obvious. If I am becoming mentally fatigued, I will write worse prompts, and because of that, the AI will do a worse job. Here's an example of what happens when I'm really tired: Kick off a somewhat meaty prompt (after 30% of context was used to align with the AI on the problem), realize right after submitting that I missed some key context, interrupt the LLM, provide the context, and then have it proceed. Without a doubt, interrupting Claude Code or "steering" in Codex leads to worse outcomes.

### Feedback loop is too slow and context is bloated

Some of the work I'm doing right now requires parsing some large files. There's bugs in that parsing logic that I'm trying to work through with the LLM. The problem is, every tweak requires re-parsing and it's a slow process. I liken it to a slot machine that takes 10 minutes to spin. To add insult to injury, some of these tasks take quite a bit of context to get rolling on a new experiment, and by the end of the parsing job, the LLM is 2% away from compaction. That then leads to either a very dumb AI or an AI that is pretending to know what's going on with the recent experiment once it's complete.

The happy path with AI
----------------------

### Avoiding the doom-loop psychosis caused by bad prompting

If I reach the point where I am not getting joy out of writing a great prompt, then it's time to throw in the towel. That has to be the first signal. If I'm half-assing it, being short, interrupting, and getting frustrated, then time to take a break.

There's some metacognition that needs to take place here. Am I being less descriptive because I haven't actually thought through this problem and I'm hoping the AI will just fill the gaps? That can be a very seductive trap to fall into. AIs are getting quite good at filling in undefined requirements, something that I remember having to do as a software engineer myself, but they're not good enough yet.

There's times I write a prompt with so much clarity in my desired end-state that I'm already celebrating the end-result when I submit the prompt because I know the AI is going to CRUSH IT. That's the feeling I need to look for in every prompt. If it's more the feeling of unsureness or impatience, it's just not going to pan out.

### Recognizing slow feedback loops and making those the problem

In the case of my parsing problem I mentioned above, it was too slow and the feedback loop was painful. I want my slot machine to take seconds/minutes to spin, not 15/20/30 minutes. In these cases, I've started to spin up a new session with the LLM, lay out my problem with feedback loop speed, express my desire to get to a sub 5-minute loop, give it an example of a failure case, and ask it to reproduce that failure case as quickly as possible. This is starting to sound familiar ... TDD anyone?

I was always the scrappy engineer. Sure I wrote tests, but I was never one to stop and create elaborate test cases or integration tests for bespoke problems. That was too time consuming, and also, I was getting paid even if my feedback loop wasn't perfect.

It's been quite the journey to fight that feeling that writing elaborate tests is time-consuming when working with AI. If you give an LLM clear success criteria: "Reproduce this specific failure case and make sure the clock time is less than 5 minutes to do it. Feel free to experiment with ways to optimize the code path or omit certain pieces that are unnecessary to reproduce" - the AI will not only reproduce the problem (maybe slowly the first time), but it will create levers for a faster feedback cycle. With that fast feedback cycle, it will consume less context and be SMARTER. This can seriously save hours of debugging time.

Conclusion
----------

When I am exhausted from working with an LLM - it might actually be a "skill issue". I need to recognize when I'm tired and entering the doom-loop psychosis. Cognitive outsourcing of requirements is seductive, but it's a trap. If I'm not enjoying the act of writing the perfect prompt and absolutely confident I will return to a result I'm 95% happy with, I need to either take a break or ponder if I've really thought through the problem. If things are moving slow and it feels as though context is filling up too quickly - I need to make that the problem to solve. Find a path, with the help of the LLM, to iterate faster and use up less context.

### Subscribe

You can subscribe to my blog [here](https://buttondown.com/tjohnell) or via [RSS feed](https://tomjohnell.com/feed/).