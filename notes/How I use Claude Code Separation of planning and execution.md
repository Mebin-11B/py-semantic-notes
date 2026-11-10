---
title: "How I use Claude Code: Separation of planning and execution"
url: https://boristane.com/blog/how-i-use-claude-code/
clipped: 2026-06-17 01:41:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How I use Claude Code: Separation of planning and execution](https://boristane.com/blog/how-i-use-claude-code/)

## Digest Summary
The author’s workflow for Claude Code consists of four disciplined phases:

- **Research** – Prompt Claude to read relevant code deeply and generate a detailed `research.md` report saved as a persistent markdown file. The report is reviewed manually to verify understanding before any planning.

- **Planning** – Using the verified research, request a comprehensive `plan.md` that includes explanations, code snippets, file paths, and trade‑offs. The plan is edited locally with inline notes that correct assumptions, add constraints, or provide domain knowledge.

- **Annotation Cycle** – Send the annotated plan back to Claude repeatedly (1–6 times) with a “don’t implement yet” guard until the document satisfies the developer. Then request a granular todo list within the plan.

- **Implementation** – Issue a single “implement it all” prompt that directs Claude to execute every task, mark completed items in the plan, avoid unnecessary comments, enforce strict typing, and continuously run type‑checks. The developer provides terse corrections during execution and retains final control over scope and architectural decisions.

The process relies on persistent markdown artifacts to maintain context, isolates planning from coding, and keeps the developer in the decision‑making loop.

## Discussion Summary
Comments converge on the view that explicit, multi‑stage planning and annotation significantly improve LLM‑driven code generation, with many users citing success using detailed prompts, spec files, ticket‑style documents, and tools such as Superpowers, Speckit, OpenSpec, and custom PCL lists. Benefits are linked to newer models like Claude Opus that handle larger token budgets, while token limits, costs, and workflow overhead are repeatedly noted as constraints. Skepticism remains about the extra effort compared to manual coding, but overall the community favors structured, lean‑context workflows despite the need to balance productivity and expense.

---

## Full Article

Iâve been using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) as my primary development tool for approx 9 months, and the workflow Iâve settled into is radically different from what most people do with AI coding tools. Most developers type a prompt, sometimes use plan mode, fix the errors, repeat. The more terminally online are stitching together ralph loops, mcps, gas towns (remember those?), etc. The results in both cases are a mess that completely falls apart for anything non-trivial.

The workflow Iâm going to describe has one core principle: **never let Claude write code until youâve reviewed and approved a written plan**. This separation of planning and execution is the single most important thing I do. It prevents wasted effort, keeps me in control of architecture decisions, and produces significantly better results with minimal token usage than jumping straight to code.

```
flowchart LR
    R[Research] --> P[Plan]
    P --> A[Annotate]
    A -->|repeat 1-6x| A
    A --> T[Todo List]
    T --> I[Implement]
    I --> F[Feedback & Iterate]
```

Phase 1: Research
-----------------

Every meaningful task starts with a deep-read directive. I ask Claude to thoroughly understand the relevant part of the codebase before doing anything else. And I always require the findings to be written into a persistent markdown file, never just a verbal summary in the chat.

> read this folder in depth, understand how it works deeply, what it does and all its specificities. when thatâs done, write a detailed report of your learnings and findings in research.md

> study the notification system in great details, understand the intricacies of it and write a detailed research.md document with everything there is to know about how notifications work

> go through the task scheduling flow, understand it deeply and look for potential bugs. there definitely are bugs in the system as it sometimes runs tasks that should have been cancelled. keep researching the flow until you find all the bugs, donât stop until all the bugs are found. when youâre done, write a detailed report of your findings in research.md

Notice the language: **âdeeplyâ**, **âin great detailsâ**, **âintricaciesâ**, **âgo through everythingâ**. This isnât fluff. Without these words, Claude will skim. Itâll read a file, see what a function does at the signature level, and move on. You need to signal that surface-level reading is not acceptable.

The written artifact (`research.md`) is critical. Itâs not about making Claude do homework. Itâs my review surface. I can read it, verify Claude actually understood the system, and correct misunderstandings before any planning happens. If the research is wrong, the plan will be wrong, and the implementation will be wrong. Garbage in, garbage out.

This is the most expensive failure mode with AI-assisted coding, and itâs not wrong syntax or bad logic. Itâs implementations that work in isolation but break the surrounding system. A function that ignores an existing caching layer. A migration that doesnât account for the ORMâs conventions. An API endpoint that duplicates logic that already exists elsewhere. The research phase prevents all of this.

Phase 2: Planning
-----------------

Once Iâve reviewed the research, I ask for a detailed implementation plan in a separate markdown file.

> I want to build a new feature <name and description> that extends the system to perform <business outcome>. write a detailed plan.md document outlining how to implement this. include code snippets

> the list endpoint should support cursor-based pagination instead of offset. write a detailed plan.md for how to achieve this. read source files before suggesting changes, base the plan on the actual codebase

The generated plan always includes a detailed explanation of the approach, code snippets showing the actual changes, file paths that will be modified, and considerations and trade-offs.

I use my own `.md` plan files rather than Claude Codeâs built-in plan mode. The built-in plan mode sucks. My markdown file gives me full control. I can edit it in my editor, add inline notes, and it persists as a real artifact in the project.

**One trick I use constantly:** for well-contained features where Iâve seen a good implementation in an open source repo, Iâll share that code as a reference alongside the plan request. If I want to add sortable IDs, I paste the ID generation code from a project that does it well and say âthis is how they do sortable IDs, write a plan.md explaining how we can adopt a similar approach.â Claude works dramatically better when it has a concrete reference implementation to work from rather than designing from scratch.

But the plan document itself isnât the interesting part. The interesting part is what happens next.

The Annotation Cycle
--------------------

This is the most distinctive part of my workflow, and the part where I add the most value.

```
flowchart TD
    W[Claude writes plan.md] --> R[I review in my editor]
    R --> N[I add inline notes]
    N --> S[Send Claude back to the document]
    S --> U[Claude updates plan]
    U --> D{Satisfied?}
    D -->|No| R
    D -->|Yes| T[Request todo list]
```

After Claude writes the plan, I open it in my editor and **add inline notes directly into the document**. These notes correct assumptions, reject approaches, add constraints, or provide domain knowledge that Claude doesnât have.

The notes vary wildly in length. Sometimes a note is two words: ânot optionalâ next to a parameter Claude marked as optional. Other times itâs a paragraph explaining a business constraint or pasting a code snippet showing the data shape I expect.

Some real examples of notes Iâd add:

* *âuse drizzle:generate for migrations, not raw SQLâ* â domain knowledge Claude doesnât have
* *âno â this should be a PATCH, not a PUTâ* â correcting a wrong assumption
* *âremove this section entirely, we donât need caching hereâ* â rejecting a proposed approach
* *âthe queue consumer already handles retries, so this retry logic is redundant. remove it and just let it failâ* â explaining why something should change
* *âthis is wrong, the visibility field needs to be on the list itself, not on individual items. when a list is public, all items are public. restructure the schema section accordinglyâ* â redirecting an entire section of the plan

Then I send Claude back to the document:

> I added a few notes to the document, address all the notes and update the document accordingly. donât implement yet

**This cycle repeats 1 to 6 times.** The explicit **âdonât implement yetâ** guard is essential. Without it, Claude will jump to code the moment it thinks the plan is good enough. Itâs not good enough until I say it is.

### Why This Works So Well

The markdown file acts as **shared mutable state** between me and Claude. I can think at my own pace, annotate precisely where something is wrong, and re-engage without losing context. Iâm not trying to explain everything in a chat message. Iâm pointing at the exact spot in the document where the issue is and writing my correction right there.

This is fundamentally different from trying to steer implementation through chat messages. The plan is a structured, complete specification I can review holistically. A chat conversation is something Iâd have to scroll through to reconstruct decisions. The plan wins every time.

Three rounds of âI added notes, update the planâ can transform a generic implementation plan into one that fits perfectly into the existing system. Claude is excellent at understanding code, proposing solutions, and writing implementations. But it doesnât know my product priorities, my usersâ pain points, or the engineering trade-offs Iâm willing to make. The annotation cycle is how I inject that judgement.

### The Todo List

Before implementation starts, I always request a granular task breakdown:

> add a detailed todo list to the plan, with all the phases and individual tasks necessary to complete the plan - donât implement yet

This creates a checklist that serves as a progress tracker during implementation. Claude marks items as completed as it goes, so I can glance at the plan at any point and see exactly where things stand. Especially valuable in sessions that run for hours.

Phase 3: Implementation
-----------------------

When the plan is ready, I issue the implementation command. Iâve refined this into a standard prompt I reuse across sessions:

> implement it all. when youâre done with a task or phase, mark it as completed in the plan document. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure youâre not introducing new issues.

This single prompt encodes everything that matters:

* *âimplement it allâ*: do everything in the plan, donât cherry-pick
* *âmark it as completed in the plan documentâ*: the plan is the source of truth for progress
* *âdo not stop until all tasks and phases are completedâ*: donât pause for confirmation mid-flow
* *âdo not add unnecessary comments or jsdocsâ*: keep the code clean
* *âdo not use any or unknown typesâ*: maintain strict typing
* *âcontinuously run typecheckâ*: catch problems early, not at the end

I use this exact phrasing (with minor variations) in virtually every implementation session. By the time I say âimplement it all,â every decision has been made and validated. The implementation becomes mechanical, not creative. This is deliberate. **I want implementation to be boring**. The creative work happened in the annotation cycles. Once the plan is right, execution should be straightforward.

Without the planning phase, what typically happens is Claude makes a reasonable-but-wrong assumption early on, builds on top of it for 15 minutes, and then I have to unwind a chain of changes. The âdonât implement yetâ guard eliminates this entirely.

Feedback During Implementation
------------------------------

Once Claude is executing the plan, my role shifts from architect to supervisor. My prompts become dramatically shorter.

```
flowchart LR
    I[Claude implements] --> R[I review / test]
    R --> C{Correct?}
    C -->|No| F[Terse correction]
    F --> I
    C -->|Yes| N{More tasks?}
    N -->|Yes| I
    N -->|No| D[Done]
```

Where a planning note might be a paragraph, an implementation correction is often a single sentence:

* *âYou didnât implement the `deduplicateByTitle` function.â*
* *âYou built the settings page in the main app when it should be in the admin app, move it.â*

Claude has the full context of the plan and the ongoing session, so terse corrections are enough.

Frontend work is the most iterative part. I test in the browser and fire off rapid corrections:

* *âwiderâ*
* *âstill croppedâ*
* *âthereâs a 2px gapâ*

For visual issues, I sometimes attach screenshots. A screenshot of a misaligned table communicates the problem faster than describing it.

I also reference existing code constantly:

* *âthis table should look exactly like the users table, same header, same pagination, same row density.â*

This is far more precise than describing a design from scratch. Most features in a mature codebase are variations on existing patterns. A new settings page should look like the existing settings pages. Pointing to the reference communicates all the implicit requirements without spelling them out. Claude would typically read the reference file(s) before making the correction.

When something goes in a wrong direction, I donât try to patch it. I revert and re-scope by discarding the git changes:

* *âI reverted everything. Now all I want is to make the list view more minimal â nothing else.â*

Narrowing scope after a revert almost always produces better results than trying to incrementally fix a bad approach.

Staying in the Driverâs Seat
------------------------------

Even though I delegate execution to Claude, **I never give it total autonomy over what gets built**. I do the vast majority of the active steering in the `plan.md` documents.

This matters because Claude will sometimes propose solutions that are technically correct but wrong for the project. Maybe the approach is over-engineered, or it changes a public API signature that other parts of the system depend on, or it picks a more complex option when a simpler one would do. I have context about the broader system, the product direction, and the engineering culture that Claude doesnât.

```
flowchart TD
    P[Claude proposes changes] --> E[I evaluate each item]
    E --> A[Accept as-is]
    E --> M[Modify approach]
    E --> S[Skip / remove]
    E --> O[Override technical choice]
    A & M & S & O --> R[Refined implementation scope]
```

**Cherry-picking from proposals:** When Claude identifies multiple issues, I go through them one by one: *âfor the first one, just use Promise.all, donât make it overly complicated; for the third one, extract it into a separate function for readability; ignore the fourth and fifth ones, theyâre not worth the complexity.â* Iâm making item-level decisions based on my knowledge of what matters right now.

**Trimming scope:** When the plan includes nice-to-haves, I actively cut them. *âremove the download feature from the plan, I donât want to implement this now.â* This prevents scope creep.

**Protecting existing interfaces:** I set hard constraints when I know something shouldnât change: *âthe signatures of these three functions should not change, the caller should adapt, not the library.â*

**Overriding technical choices:** Sometimes I have a specific preference Claude wouldnât know about: *âuse this model instead of that oneâ* or *âuse this libraryâs built-in method instead of writing a custom one.â* Fast, direct overrides.

Claude handles the mechanical execution, while I make the judgement calls. The plan captures the big decisions upfront, and selective guidance handles the smaller ones that emerge during implementation.

Single Long Sessions
--------------------

I run research, planning, and implementation in a **single long session** rather than splitting them across separate sessions. A single session might start with deep-reading a folder, go through three rounds of plan annotation, then run the full implementation, all in one continuous conversation.

I am not seeing the performance degradation everyone talks about after 50% context window. Actually, by the time I say âimplement it all,â Claude has spent the entire session building understanding: reading files during research, refining its mental model during annotation cycles, absorbing my domain knowledge corrections.

When the context window fills up, Claudeâs auto-compaction maintains enough context to keep going. And the plan document, the persistent artifact, survives compaction in full fidelity. I can point Claude to it at any point in time.

The Workflow in One Sentence
----------------------------

Read deeply, write a plan, annotate the plan until itâs right, then let Claude execute the whole thing without stopping, checking types along the way.

Thatâs it. No magic prompts, no elaborate system instructions, no clever hacks. Just a disciplined pipeline that separates thinking from typing. The research prevents Claude from making ignorant changes. The plan prevents it from making wrong changes. The annotation cycle injects my judgement. And the implementation command lets it run without interruption once every decision has been made.

Try my workflow, youâll wonder how you ever shipped anything with coding agents without an annotated plan document sitting between you and the code.

I'm also building [polylane](https://polylane.com), because nobody should be on-call in 2026.