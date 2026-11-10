---
title: "Software factories and the agentic moment"
url: https://factory.strongdm.ai/
clipped: 2026-06-17 01:47:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Software factories and the agentic moment](https://factory.strongdm.ai/)

## Digest Summary
StrongDM’s “Software Factory” implements non‑interactive development: specifications and high‑level scenarios drive autonomous agents that generate code, execute harnesses, and converge without human authoring or review. The initiative began in July 2025 after Claude 3.5’s October 2024 update demonstrated long‑horizon coding correctness, especially via Anthropic’s YOLO mode, which reduced accumulated errors (syntax, library mismatches, hallucinations). Early experiments showed agents could pass narrow unit tests but required broader validation; the team introduced “scenarios”—end‑to‑end user stories stored outside the codebase—and measured “satisfaction” as the probabilistic fraction of scenario trajectories that meet user intent. Traditional tests were deemed too rigid and susceptible to reward hacking, prompting the creation of a Digital Twin Universe (DTU) that faithfully emulates APIs and edge cases of services such as Okta, Jira, Slack, Google Docs, Drive, and Sheets. DTU enables high‑volume, safe scenario testing, including failure modes, without live‑service limits or costs. The approach reshapes software economics by making high‑fidelity SaaS clones economically viable, encouraging a “deliberate naivete” that discards legacy constraints.

## Discussion Summary
The comments convey a mixed but largely cautious view of AI‑driven software factories. Many participants question the practicality of fully autonomous code generation, emphasizing the high token costs, the persistence of messy or incomplete output, and the necessity of human validation, testing, and security review. Skepticism is expressed toward bold productivity claims and the lack of rigorous quantitative evidence, while a minority note promising use cases such as digital‑twin simulations and automated integration scaffolding. Overall, the discussion balances intrigue about agentic workflows with concerns about quality, cost, regulatory implications, and the enduring role of engineers.

---

## Full Article

We built a **Software Factory**: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review.

The narrative form is included below. If you'd prefer to work from first principles, I offer a few constraints & guidelines that, applied iteratively, will accelerate any team toward the same intuitions, convictions[1](https://factory.strongdm.ai/#fn1), and ultimately a factory[2](https://factory.strongdm.ai/#fn2) of your own. In kōan or mantra form:

* Why am I doing this? (implied: the model should be doing this instead)

In rule form:

* Code **must not be** written by humans
* Code **must not be** reviewed by humans

Finally, in practical form:

* If you haven't spent at least **$1,000 on tokens today** per human engineer, your software factory has room for improvement

The StrongDM AI Story
---------------------

On July 14th, 2025, Jay Taylor and Navan Chauhan joined me (Justin McCarthy, co-founder, CTO) in founding the StrongDM AI team.

The catalyst was a transition observed in late 2024: with the second revision of Claude 3.5 (October 2024), long-horizon agentic coding workflows began to compound correctness rather than error.

![Compounding correctness vs compounding error](https://factory.strongdm.ai/images/growth.jpeg)

Compounding correctness vs compounding error

By December of 2024, the model's long-horizon coding performance was unmistakable via Cursor's [YOLO mode](https://forum.cursor.com/t/yolo-mode-is-amazing/36262).

Prior to this model improvement, iterative application of LLMs to coding tasks would accumulate errors of all imaginable varieties (misunderstandings, hallucinations, syntax, DRY violations, library incompatibility, etc). The app or product would decay and ultimately "collapse": death by a thousand cuts, etc.

Together with YOLO mode, the updated model from Anthropic provided the first glimmer of what we now refer to internally as **non-interactive** development or **grown** software.

Find Knobs, Turn To Eleven
--------------------------

![These go to 11](https://factory.strongdm.ai/images/eleven.jpg)

"These go to 11"

In the first hour of the first day of our AI team, we established a charter which set us on a path toward a series of findings (which we refer to as our "unlocks"). In retrospect, the most important line in the charter document was the following:

![Hands off](https://factory.strongdm.ai/images/no-hand-coded.jpg)

Hands off!

Initially it was just a hunch. An experiment. How far could we get, without writing any code by hand?

Not very far! At least: not very far, until we added tests. However, the agent, obsessed with the immediate task, soon began to take shortcuts: **return true** is a great way to pass narrowly written tests, but probably won't generalize to the software you want.

Tests were not enough. How about integration tests? Regression tests? End-to-end tests? Behavior tests?

From Tests to Scenarios and Satisfaction
----------------------------------------

One recurring theme of the agentic moment: we need new language. For example, the word "test" has proven insufficient and ambiguous. A test, stored in the codebase, can be lazily rewritten to match the code. The code could be rewritten to trivially pass the test.

We repurposed the word **scenario** to represent an end-to-end "user story", often stored outside the codebase (similar to a "holdout" set in model training), which could be intuitively understood and flexibly validated by an LLM.

![Synthetic scenario curation and shaping interface](https://factory.strongdm.ai/images/synthchat.png)

Synthetic scenario curation and shaping interface

Because much of the software we grow itself has an agentic component, we transitioned from boolean definitions of success ("the test suite is green") to a probabilistic and empirical one. We use the term **satisfaction** to quantify this validation: of all the observed trajectories through all the scenarios, what fraction of them likely satisfy the user?

Validating Scenarios in the Digital Twin Universe
-------------------------------------------------

In previous regimes, a team might rely on integration tests, regression tests, UI automation to answer "is it working?"

We noticed two limitations of previously reliable techniques:

1. **Tests are too rigid** - we were coding with agents, but we're also building with LLMs and agent loops as design primitives; evaluating success often required LLM-as-judge
2. **Tests can be reward hacked** - we needed validation that was less vulnerable to the model cheating

The Digital Twin Universe is our answer: behavioral clones of the third-party services our software depends on. We built twins of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, replicating their APIs, edge cases, and observable behaviors.

With the DTU, we can validate at volumes and rates far exceeding production limits. We can test failure modes that would be dangerous or impossible against live services. We can run thousands of scenarios per hour without hitting rate limits, triggering abuse detection, or accumulating API costs.

Digital Twin Universe: behavioral clones of Okta, Jira, Google Docs, Slack, Drive, and Sheets  
(click to enlarge)

Unconventional Economics
------------------------

Our success with DTU illustrates one of the many ways in which the Agentic Moment has profoundly changed the economics of software. Creating a high fidelity clone of a significant SaaS application was always possible, but never economically feasible. Generations of engineers may have *wanted* a full in-memory replica of their CRM to test against, but self-censored the proposal to build it. They didn't even bring it to their manager, because they knew the answer would be no.

Those of us building software factories must practice a **deliberate naivete**: finding and removing the habits, conventions, and constraints of [Software 1.0](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=95s). The DTU is our proof that what was unthinkable six months ago is now routine.

Read Next
---------

* [Principles](https://factory.strongdm.ai/principles): what we believe is true about building software with agents
* [Techniques](https://factory.strongdm.ai/techniques): repeated patterns for applying those principles
* [Products](https://factory.strongdm.ai/products): tools we use daily and believe others will benefit from

Thank you for reading. We wish you the best of luck constructing your own Software Factory.

---

---