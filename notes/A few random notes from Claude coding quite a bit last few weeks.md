---
title: "A few random notes from Claude coding quite a bit last few weeks"
url: https://twitter.com/karpathy/status/2015883857489522876
clipped: 2026-06-17 01:52:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Agentic Coding
  - AI Productivity
  - Developer Workflows
  - Cognitive Atrophy
  - Technical Hype
  - Software Engineering Shifts
related:
  - "[[Using AI to write better code more slowly]]"
  - "[[Learn Claude Code by doing, not reading]]"
  - "[[Reports of code's death are greatly exaggerated]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Andrej Karpathy shares reflections on his rapid shift to 80% agentic coding with Claude, highlighting AI's relentless stamina, the necessity of IDE-based monitoring, and the cognitive atrophy of manual programming.
>
> **Key points:**
> - Karpathy describes a rapid workflow phase-shift, moving from 80% manual coding to 80% AI agent generation, primarily programming via high-level English instructions.
> - Coding models still make conceptual mistakes, overcomplicate abstractions, and bloat code, making vigilant monitoring in a dedicated IDE essential.
> - AI agents possess superhuman stamina and tenacity, executing loops and attempting creative solutions for extended periods without fatigue.
> - LLM coding expands a developer's capabilities, allowing them to build projects that previously wouldn't have been worth the time or required unavailable skillsets.
> - Continuous reliance on coding agents leads to the cognitive atrophy of manual code generation, as writing and reading code utilize different brain pathways.
>
> **Concept links:** [[Agentic Coding]], [[AI Productivity]], [[Developer Workflows]], [[Cognitive Atrophy]], [[Technical Hype]], [[Software Engineering Shifts]]
>
> **Suggested connections:**
> - [[Using AI to write better code more slowly]] — Explores the balance of speed versus quality when coding with AI.
> - [[Learn Claude Code by doing, not reading]] — Practical context for using agentic terminal tools like Claude Code.
> - [[Reports of code's death are greatly exaggerated]] — A counter-perspective on why code and precise formalisms remain vital in the age of "vibe coding."
<!-- ai-summary:end -->

# [A few random notes from Claude coding quite a bit last few weeks](https://twitter.com/karpathy/status/2015883857489522876)

## Digest Summary
The page consists of a generic header (“Title: [no‑title]”) followed by a separator line and an error notice stating that something went wrong and advising a retry. Another separator introduces an “Images and Visual Content” section, which contains a single entry: “Image 1” with an alt‑text label of a warning symbol (⚠️). No additional text, data, or functional elements are present. The structure is limited to the title, error message, section heading, and the placeholder for one image with a warning icon as its descriptive text.

## Discussion Summary
Comments express a mixed view of LLM‑assisted coding. Many note the agents’ tireless, high‑stamina work and the productivity gains they can deliver, especially for front‑end or incremental tasks, while also highlighting the need for new workflows, education, and continued IDE‑based review. A recurring concern is skill atrophy and complacency, with users fearing dependence on opaque models, loss of manual coding ability, and potential societal effects from gatekeeper control. Opinions diverge on whether the technology will amplify top engineers’ output or create a split between “builders” and traditional coders, and adoption is seen as uneven pending cultural and tooling changes.

---

## Full Article

A few random notes from claude coding quite a bit last few weeks.
Coding workflow. Given the latest lift in LLM coding capability, like many others I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December. i.e. I really am mostly programming in English now, a bit sheepishly telling the LLM what code to write... in words. It hurts the ego a bit but the power to operate over software in large "code actions" is just too net useful, especially once you adapt to it, configure it, learn to use it, and wrap your head around what it can and cannot do. This is easily the biggest change to my basic coding workflow in ~2 decades of programming and it happened over the course of a few weeks. I'd expect something similar to be happening to well into double digit percent of engineers out there, while the awareness of it in the general population feels well into low single digit percent.
IDEs/agent swarms/fallability. Both the "no need for IDE anymore" hype and the "agent swarm" hype is imo too much for right now. The models definitely still make mistakes and if you have any code you actually care about I would watch them like a hawk, in a nice large IDE on the side. The mistakes have changed a lot - they are not simple syntax errors anymore, they are subtle conceptual errors that a slightly sloppy, hasty junior dev might do. The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking. They also don't manage their confusion, they don't seek clarifications, they don't surface inconsistencies, they don't present tradeoffs, they don't push back when they should, and they are still a little too sycophantic. Things get better in plan mode, but there is some need for a lightweight inline plan mode. They also really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves, etc. They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like "umm couldn't you just do this instead?" and they will be like "of course!" and immediately cut it down to 100 lines. They still sometimes change/remove comments and code they don't like or don't sufficiently understand as side effects, even if it is orthogonal to the task at hand. All of this happens despite a few simple attempts to fix it via instructions in CLAUDE . md. Despite all these issues, it is still a net huge improvement and it's very difficult to imagine going back to manual coding. TLDR everyone has their developing flow, my current is a small few CC sessions on the left in ghostty windows/tabs and an IDE on the right for viewing the code + manual edits.
Tenacity. It's so interesting to watch an agent relentlessly work at something. They never get tired, they never get demoralized, they just keep going and trying things where a person would have given up long ago to fight another day. It's a "feel the AGI" moment to watch it struggle with something for a long time just to come out victorious 30 minutes later. You realize that stamina is a core bottleneck to work and that with LLMs in hand it has been dramatically increased.
Speedups. It's not clear how to measure the "speedup" of LLM assistance. Certainly I feel net way faster at what I was going to do, but the main effect is that I do a lot more than I was going to do because 1) I can code up all kinds of things that just wouldn't have been worth coding before and 2) I can approach code that I couldn't work on before because of knowledge/skill issue. So certainly it's speedup, but it's possibly a lot more an expansion.
Leverage. LLMs are exceptionally good at looping until they meet specific goals and this is where most of the "feel the AGI" magic is to be found. Don't tell it what to do, give it success criteria and watch it go. Get it to write tests first and then pass them. Put it in the loop with a browser MCP. Write the naive algorithm that is very likely correct first, then ask it to optimize it while preserving correctness. Change your approach from imperative to declarative to get the agents looping longer and gain leverage.
Fun. I didn't anticipate that with agents programming feels \*more\* fun because a lot of the fill in the blanks drudgery is removed and what remains is the creative part. I also feel less blocked/stuck (which is not fun) and I experience a lot more courage because there's almost always a way to work hand in hand with it to make some positive progress. I have seen the opposite sentiment from other people too; LLM coding will split up engineers based on those who primarily liked coding and those who primarily liked building.
Atrophy. I've already noticed that I am slowly starting to atrophy my ability to write code manually. Generation (writing code) and discrimination (reading code) are different capabilities in the brain. Largely due to all the little mostly syntactic details involved in programming, you can review code just fine even if you struggle to write it.
Slopacolypse. I am bracing for 2026 as the year of the slopacolypse across all of github, substack, arxiv, X/instagram, and generally all digital media. We're also going to see a lot more AI hype productivity theater (is that even possible?), on the side of actual, real improvements.
Questions. A few of the questions on my mind:
- What happens to the "10X engineer" - the ratio of productivity between the mean and the max engineer? It's quite possible that this grows \*a lot\*.
- Armed with LLMs, do generalists increasingly outperform specialists? LLMs are a lot better at fill in the blanks (the micro) than grand strategy (the macro).
- What does LLM coding feel like in the future? Is it like playing StarCraft? Playing Factorio? Playing music?
- How much of society is bottlenecked by digital knowledge work?
TLDR Where does this leave us? LLM agent capabilities (Claude & Codex especially) have crossed some kind of threshold of coherence around December 2025 and caused a phase shift in software engineering and closely related. The intelligence part suddenly feels quite a bit ahead of all the rest of it - integrations (tools, knowledge), the necessity for new organizational workflows, processes, diffusion more generally. 2026 is going to be a high energy year as the industry metabolizes the new capability.