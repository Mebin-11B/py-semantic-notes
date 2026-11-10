---
title: "Haskell for all: Beyond agentic coding"
url: https://haskellforall.com/2026/02/beyond-agentic-coding
clipped: 2026-06-17 01:47:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Haskell for all: Beyond agentic coding](https://haskellforall.com/2026/02/beyond-agentic-coding)

## Digest Summary
The author argues that current “agentic” coding tools—LLM‑driven chat assistants that generate code—do not improve productivity and often disrupt developers’ flow. Evidence includes personal experience, interview observations where candidates using such tools performed worse, and academic studies (e.g., Becker, Shen) showing no productivity gain and increased idle time. The author proposes applying **calm‑technology** principles—minimizing attention demands, being “pass‑through,” and fostering a calm state—to AI‑assisted development. Existing calm examples are IDE inlay hints and file‑tree previews, which unobtrusively augment information. In contrast, chat agents require active interaction, are indirect, and break flow. GitHub Copilot’s inline suggestions violate calm principles by demanding attention, whereas its “next edit” suggestions better preserve flow by being peripheral and bite‑sized. The author sketches future calm‑oriented tools: a facet‑based project navigator for semantic browsing, automated commit‑refactoring that splits changes into review‑friendly units, and a “file lens” offering focus‑on or edit‑as modes to filter or reinterpret code. The overall aim is to embed AI in developers’ workflows without relying on chat interfaces.

## Discussion Summary
The feedback acknowledges that the article’s title is misleading but finds the main content solid and sees potential for Agentic/AI coding to develop along the described trajectory. It characterizes current tools as early‑stage, likening them to the MS‑DOS era, and suggests they may later enable automatic translation from a developer’s preferred language to a target language. However, it doubts the practicality of agentic coding in interview settings, noting the need for precise, iteratively refined specifications and that outcomes depend heavily on prompt quality.

---

## Full Article

I'm generally pretty pro-AI with one major exception: agentic coding. My consistent impression is that agentic coding does not actually improve productivity and deteriorates the user's comfort and familiarity with the codebase. I formed that impression from:

* [my own personal experiences](https://haskellforall.com/2026/02/my-experience-with-vibe-coding)

  Every time I use agentic coding tools I'm consistently unimpressed with the quality of the results.
* my experiences interviewing candidates

  I allow interview candidates to use agentic coding tools and candidates who do so consistently performed *worse* than other candidates, failing to complete the challenge or producing incorrect results[1](https://haskellforall.com/2026/02/beyond-agentic-coding#user-content-fn-1). This was a huge surprise to me at first because I expected agentic coding to confer an unfair advantage but â¦ nope!
* research studies

  Studies like the [Becker study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [Shen study](https://arxiv.org/abs/2601.20245) show that users of agentic coding perform no better and sometimes worse when you measure productivity in terms of fixed outcomes rather than code velocity/volume.

I don't believe agentic coding is a lost cause, but I do believe agentic coding in its present incarnation is doing more harm than good to software development. I also believe it is still worthwhile to push on the inadequacies of agentic coding so that it empowers developers and improves code quality.

However, in this post I'm taking a different tack: I want to present other ways to leverage AI for software development. I believe that agentic coding has so captured the cultural imagination that people are sleeping on other good and underexplored solutions to AI-assisted software development.

The master cue
--------------

I like to design tools and interfaces from first principles rather than reacting to industry trends/hype and I've accrued quite a few general design principles from over a decade of working in DevProd and also an even longer history of open source projects and contributions.

One of those design principles is my personal "master cue", which is:

> A good tool or interface should keep the user in a flow state as long as possible

This principle isn't even specific to AI-assisted software development, and yet still highlights why agentic coding sometimes misses the mark. Both studies and developer testimonials show that agentic coding breaks flow and keeps developers in an idle/interruptible holding pattern more than ordinary coding.

For example, the [Becker study](https://arxiv.org/abs/2507.09089) took screen recordings and saw that idle time approximately doubled:

![](https://haskellforall.com/imgs/beyond-agentic-coding/idle-time.png)

I believe we can improve AI-assisted coding tools (agentic or not) if we set our north star to âpreserve flow stateâ.

Calm technology
---------------

[Calm technology](https://calmtech.com/) is a design discipline that promotes flow state in tools that we build. The design principles most relevant to coding are:

* tools should minimize demands on our attention

  Interruptions and intrusions on our attention break us out of flow state.
* tools should be built to be âpass-throughâ

  A tool is not meant to be the object of our attention; rather the tool should *reveal* the true object of our attention (the thing the tool acts upon), rather than obscuring it. The more we use the tool the more the tool fades into the background of our awareness while still supporting our work.
* tools should create and enhance calm (thus the name: calm technology)

  A state of calm helps users enter and maintain flow state.

Non-LLM examples of calm technology
-----------------------------------

Engineers already use âcalmâ tools and interfaces as part of our work and here are a couple of examples you're probably already familiar with:

### Inlay hints

IDEs (like VSCode) can support [inlay hints](https://code.visualstudio.com/docs/typescript/typescript-editing#_inlay-hints) that sprinkle the code with useful annotations for the reader, such as inferred type annotations:

![](https://haskellforall.com/imgs/beyond-agentic-coding/inlay-hints.png)

These types of inlay hints embody calm design principles because:

* they minimize demands on our attention

  They exist on the periphery of our attention, available for us if we're interested but unobtrusive if we're not interested.
* they are built to be âpass-throughâ

  They don't replace or substitute the code that we are editing. They enhance the code editing experience but the user is still in direct contact with the edited code. The more we use type hints the more they fade into the background of our awareness and the more the code remains the focus of our attention.
* they create and enhance calm

  They promote a sense of calm by informing our understanding of the code **passively**. As one of the [Calm Technology](https://calmtech.com/) principles puts it: *âTechnology can communicate, but doesn't need to speakâ.*

### File tree previews

Tools like VSCode or GitHub's pull request viewer let you preview at a glance changes to the file tree, like this:

![](https://haskellforall.com/imgs/beyond-agentic-coding/file-tree-1.png)

You might think to yourself âthis is a very uninteresting thing to use as an exampleâ but that's exactly the point. The best tools (designed with the principles of calm technology) are pervasive and **boring** things that we take for granted (like light switches) and that have faded so strongly into the background of our attention that we forget they even exist as a part of our daily workflow (also like light switches).

File tree previews:

* minimize demands on our attention

  They're there if we need the information, but easy to ignore (or even forget they exist) if we don't use them.
* are built to be âpass-throughâ

  When we interact with the file tree viewer we are interacting directly with the filesystem and the interaction between the representation (the viewer) and the reality (the filesystem) feels direct, snappy, and precise. The more we use the viewer the more the representation becomes indistinguishable from the reality in our minds.
* create and enhance calm

  We do not need to constantly interact with the file tree to gather up-to-date information about our project structure. It passively updates in the background as we make changes to the project and those updates are unobtrusive and not attention-grabbing.

Chat-based coding agents are not calm
-------------------------------------

We can think about the limitations of chat-based agentic coding tools through this same lens:

* they place high demands on our attention

  The user has to either sit and wait for the agent to report back or do something else and run the LLM in a semi-autonomous manner. However, even semi-autonomous sessions prevent the user from entering flow state because they have to remain interruptible.
* they are not built to be âpass-throughâ

  Chat agents are a highly mediated interface to the code which is **indirect** (we interact more with the agent than the code), **slow** (we spend a lot of time waiting), and **imprecise** (English is a [dull interface](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)).
* they undermine calm

  The user needs to constantly stimulate the chat to gather new information or update their understanding of the code (the chat agent doesn't inform the user's understanding passively or quietly). Chat agents are also fine-tuned to maximize engagement.

Prior art for calm design
-------------------------

### Inline suggestions from GitHub Copilot

One of the earliest examples of an AI coding assistant that begins to model calm design principles is the OG AI-assistant: [GitHub Copilot's support for inline suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions), with some caveats I'll go into.

![](https://haskellforall.com/imgs/beyond-agentic-coding/inline-suggestions.png)

This does one thing really well:

However, by default these inline suggestions violate other calm technology principles:

* they demand our attention

  By default Copilot presents the suggestions quite frequently and the user has to pause what they're doing to examine the output of the suggestion. After enough times the user begins to condition themselves into regularly pausing and waiting for a suggestion which breaks them out of a flow state. Now instead of being proactive the user's been conditioned by the tool to be reactive.
* they undermine calm

  GitHub Copilot's inline suggestion interface is visually busy and intrusive. Even if the user ignores every suggestion the effect is still disruptive: suggestions appear on the user's screen in the center of their visual focus and the user has to decide on the spot whether to accept or ignore them before proceeding further. The user also can't easily passively absorb information presented in this way: understanding each suggestion requires the user's focused attention.

â¦ *buuuuut* these issues are partially fixable by disabling the automatic suggestions and requiring them to be explicitly triggered by `Alt` + `\`. However, unfortunately that also disables the next feature, which I like even more:

### Next edit suggestions (also from GitHub Copilot)

[Next edit suggestions](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions#_next-edit-suggestions) are a related GitHub Copilot feature that display related follow-up edits throughout the file/project and let the user cycle between them and possibly accept each suggested change. They behave like a âsuper-charged find and replaceâ:

[

](https://code.visualstudio.com/assets/docs/copilot/inline-suggestions/nes-video.mp4)

These suggestions do an amazing job of keeping the user in a flow state:

* they minimize demand on the user's attention

  The cognitive load on the user is smaller than inline suggestions because the suggestions are more likely to be bite-sized (and therefore easier for a human to review and accept).
* they're built to be âpass-throughâ

  Just like inline suggestions, next edit suggestions still keep the user in close contact with the code they are modifying.
* they create and enhance calm

  Suggestions are presented in an unobtrusive way: they aren't dumped in the dead center of the user's attention and they don't demand immediate review. They exist on the periphery of the user's attention as code suggestions that the user can ignore or focus on at their leisure.

AI-assisted calm technology
---------------------------

I believe there is a lot of untapped potential in AI-assisted coding tools and in this section I'll sketch a few small examples of how we can embody calm technology design principles in building the next generation of coding tools.

### Facet-based project navigation

You could browse a project by a tree of semantic facets. For example, if you were editing [the Haskell implementation of Dhall](https://github.com/dhall-lang/dhall-haskell) the tree viewer might look like this prototype I hacked up[2](https://haskellforall.com/2026/02/beyond-agentic-coding#user-content-fn-2):

[

](/imgs/beyond-agentic-coding/semantic-facets.mp4)

The goal here is to not only provide a quick way to explore the project by intent, but to also improve the user's understanding of the project the more they use the feature. "String interpolation regression" is so much more informative than `dhall/tests/format/issue2078A.dhall`[3](https://haskellforall.com/2026/02/beyond-agentic-coding#user-content-fn-3).

Also, the above video is based on a real tool and not just a mock. You can find the code I used to generate that tree of semantics facets [here](https://github.com/Gabriella439/facet-navigator) and I'll write up another post soon walking through how that code works.

### Automated commit refactor

You could take an editor session, a diff, or a pull request and automatically split it into a series of more focused commits that are easier for people to review. This is one of the cases where the AI can *reduce* human review labor (most agentic coding tools *create* more human review labor).

There is [some prior art here](https://softwareengineering.stackexchange.com/questions/458416/how-to-decompose-a-large-git-commit-with-an-ai) but this is still a nascent area of development.

### File lens

You could add two new tools to the user's toolbar or context menu: *âFocus onâ¦â* and *âEdit asâ¦â.*

*âFocus onâ¦â* would allow the user to specify what they're interested in changing and present only files and lines of code related to their specified interest. For example, if they want to focus on âcommand line optionsâ then only related files and lines of code would be shown in the editor and other lines of code would be hidden/collapsed/folded. This would basically be like âZen modeâ but for editing a feature domain of interest.

*âEdit asâ¦â* would allow the user to edit the file or selected code as if it were a different programming language or file format. For example, someone who was new to Haskell could edit a Haskell file âas Pythonâ and then after finishing their edits the AI attempts to back-propagate their changes to Haskell. Or someone modifying a command-line parser could edit the file âas YAMLâ and be presented with a simplified YAML representation of the command line options which they could modify to add new options.

Conclusion
----------

This is obviously not a comprehensive list of ideas, but I wrote this to encourage people to think of more innovative ways to incorporate AI into people's workflows besides just building yet another chatbot. I strongly believe that [chat is the least interesting interface to LLMs](https://haskellforall.com/2026/01/chat-is-least-interesting-interface-to) and AI-assisted software development is no exception to this.