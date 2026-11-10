---
title: "Agents that run while I sleep"
url: https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep
clipped: 2026-06-17 01:34:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Agents that run while I sleep](https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep)

## Digest Summary
The author describes a workflow for verifying AI‑generated code using explicit acceptance criteria rather than relying on AI‑written tests or manual reviews. After writing plain‑English specifications (e.g., login flow, error messages, rate limiting), a Claude‑based agent generates code that is automatically exercised by Playwright (frontend) or curl (backend) against those criteria. Each acceptance criterion yields a pass/fail verdict with screenshots and reasoning, allowing reviewers to focus only on failures. The process consists of four stages: a Bash pre‑flight check, a planner call (Opus) that parses the spec and determines needed checks, parallel browser agents (Sonnet) that execute each criterion, and a final judge call (Opus) that aggregates evidence into JSON verdicts. The system is implemented as a Claude Skill (github.com/opslane/verify) that runs in Claude Code’s headless mode without extra backend services. The approach mirrors Test‑Driven Development by defining “done” before code generation, exposing integration issues that code review alone often misses, though it cannot detect incorrect specifications.

## Discussion Summary
The comments convey a mixed view of autonomous coding agents: many acknowledge noticeable productivity gains but stress that the tools remain costly, complex, and prone to errors that demand thorough human oversight and robust testing. Participants highlight the difficulty of maintaining reliable specifications, preventing “placeholder” code, and managing review fatigue, while warning against over‑engineered frameworks and unchecked long‑running agents. Overall, the consensus is that AI can accelerate development if paired with disciplined TDD, clear specs, and vigilant validation rather than being relied upon as a standalone solution.

---

## Full Article

I've been building agents that write code while I sleep. Tools like Gastown run for hours without me watching. Changes land in branches I haven't read. A few weeks ago I realized I had no reliable way to know if any of it was correct: whether it actually does what I said it should do.

I care about this. I don't want to push slop, and I had no real answer.

I've run Claude Code workshops for over 100 engineers in the last six months. Same problem everywhere, just at different scales. Teams using Claude for everyday PRs are merging 40-50 a week instead of 10. Teams are spending a lot more time in code reviews.

As systems get more autonomous, the problem compounds. At some point you're not reviewing diffs at all, just watching deploys and hoping something doesn't break.

So the question I kept coming back to: what do you actually trust when you can't review everything?

### The obvious answers don't work

You could hire more reviewers. But you can't hire fast enough. And making senior engineers read AI-generated code all day isn't worth it.

When Claude writes tests for code Claude just wrote, it's checking its own work. The tests prove the code does what Claude thought you wanted. Not what you actually wanted. They catch regressions but not the original misunderstanding.

When you use the same AI for both, you've built a self-congratulation machine.

This is exactly the problem code review was supposed to solve: a second set of eyes that wasn't the original author. But one AI writing and another AI checking isn't a fresh set of eyes. They come from the same place. They'll miss the same things.

### The thing TDD got right

Write the test first, write the code second, stop when the test passes. Most teams don't do this because thinking through what the code should do before writing it takes time they don't have.

AI removes that excuse, because Claude handles the speed. The slow part is now figuring out if the code is right. That's what TDD was built for: write down what correct looks like, then check it.

TDD asks you to write unit tests, which means thinking about how the code will work before you write it. This is easier. Write down what the feature should do in plain English. The machine figures out how to check it.

"Users can authenticate with email and password. On wrong credentials they see 'Invalid email or password.' On success they land on /dashboard. The session token expires after 24 hours." You can write that before you open a code editor. The agent builds it. Something else checks it.

#### **Free Claude Code crash course**

60-min video lesson + CLAUDE.md starter kit. Yours when you subscribe.

### What this looks like in practice

For frontend changes, we generated acceptance criterias based on the spec file:

# Task  
Add email/password login.  
  
## Acceptance Criteria  
  
### AC-1: Successful login  
- User at /login with valid credentials gets redirected to /dashboard  
- Session cookie is set  
  
### AC-2: Wrong password error  
- User sees exactly "Invalid email or password"  
- User stays on /login  
  
### AC-3: Empty field validation  
- Submit disabled when either field is empty, or inline error on empty submit  
  
### AC-4: Rate limiting  
- After 5 failed attempts, login blocked for 60 seconds  
- User sees a message with the wait time

Each criterion is specific enough that it either passes or fails. Once the agent builds the feature, verification runs Playwright browser agents against each AC, takes screenshots, and produces a report with per-criterion verdicts. If something fails you see exactly which criterion and what the browser saw.

For backend changes the same pattern works without a browser. You specify observable API behavior (status codes, response headers, error messages) that curl commands can check.

One thing worth being honest about: this doesn't catch spec misunderstandings. If your spec was wrong to begin with, the checks will pass even when the feature is wrong. What Playwright does catch is integration failures, rendering bugs, and behavior that works in theory but breaks in a real browser. That's a narrower claim than "verified correct," but it's more than a code review was reliably catching anyway.

The workflow: write acceptance criteria before you prompt, let the agent build against them, run verification, review only the failures. You review failures instead of diffs.

### How to build it

I started building a Claude Skill ([github.com/opslane/verify](https://github.com/opslane/verify)) that runs using **claude -p** (Claude Code's headless mode) plus Playwright MCP. No custom backend, no extra API keys beyond your existing Claude OAuth token. Four stages:

**Pre-flight** is pure bash, no LLM. Is the dev server running? Is the auth session valid? Does a spec file exist? Fail fast before spending any tokens.

**The planner** is one Opus call. It reads your spec and the files you changed. It figures out what each check needs and how to run it. It also reads your code to find the right selectors, so it's not guessing at class names.

**Browser agents** are one Sonnet call per AC, all running in parallel. Five ACs, five agents, each navigating and screenshotting independently. Sonnet costs 3-4x less than Opus here and works just as well for clicking around.

**The judge** is one final Opus call that reads all the evidence and returns a verdict per criterion: pass, fail, or needs-human-review.

claude -p --model claude-opus-4-6 \  
 "Review this evidence and return a verdict for each AC.  
 Evidence: $(cat .verify/evidence/\*/result.json)  
 Return JSON: {verdicts: [{id, passed, reasoning}]}"

Install it as a Claude Code plugin:

/plugin marketplace add opslane/verify  
/plugin install opslane-verify@opslane/verify

Or clone the repo and adapt it. Each stage is a single **claude -p** call with a clear input and structured output. You can swap models, add stages, or wire it into CI with **--dangerously-skip-permissions**.

The thing I keep coming back to: you can't trust what an agent produces unless you told it what "done" looks like before it started. Writing acceptance criteria is harder than writing a prompt, because it forces you to think through edge cases before you've seen them. Engineers resist it for the same reason they resisted TDD, because it feels slower at the start.

Without them, all you can do is read the output and hope it's right.