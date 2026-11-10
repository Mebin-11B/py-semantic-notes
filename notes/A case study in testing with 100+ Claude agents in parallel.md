---
title: "A case study in testing with 100+ Claude agents in parallel"
url: https://imbue.com/product/mngr_part_2/
clipped: 2026-06-17 01:22:26
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A case study in testing with 100+ Claude agents in parallel](https://imbue.com/product/mngr_part_2/)

## Digest Summary
The post describes how Imbue’s **mngr** CLI is used to launch and coordinate hundreds of Claude agents for self‑testing. A tutorial script ( tutorial.sh ) is written with commented blocks; each block is turned into one or more pytest functions. Agents generate these tests, annotate each function with its source block, and a validator ensures the correspondence. Tests use a thin wrapper over Python’s subprocess to run CLI commands, capture stdout/stderr, and produce transcript files; a custom connect_command (`mngr‑e2e‑connect`) records tmux sessions via asciinema.

Orchestration proceeds by collecting test names (`pytest --collect-only`), spawning an agent per test (via `mngr create` primitives), and having agents fix failing tests, improve passing ones, and emit JSON result artifacts. Results are pulled, and an “integrator” agent merges non‑implementation fixes wholesale, ranks implementation fixes, and creates a linear branch for review. The workflow scales from a local machine (using Git worktrees) to remote Modal sandboxes (via `mngr create [email protected]`), with identical primitives for listing, pulling, and stopping agents.

The architecture is framed as a map‑reduce pipeline: map each test to an agent, then reduce the outputs into a single PR. mngr’s design emphasizes low upfront cost, easy scale‑down, and platform‑agnostic primitives, supporting both small‑team local development and large‑scale remote execution.

## Discussion Summary
The discussion reflects concern over recent court rulings that deem AI‑generated content uncopyrightable, prompting questions about the future of intellectual‑property practices. Commenters speculate that traditional licensing may lose relevance, potentially discouraging open‑source contributions and encouraging developers to keep code proprietary. The overall tone is uncertain and inquisitive, focusing on how the legal shift could reshape attitudes toward sharing, licensing, and protecting software and creative works.

---

## Full Article

In our [previous blog post](https://imbue.com/product/mngr/), we introduced `mngr` and how you can use it to usefully launch hundreds of parallel agents. Hereâs all the details of how we are actually using `mngr` to run and improve itself, by testing its own demo script.

High-level architecture
-----------------------

This is how the entire setup works:

* We start from a tutorial script, `tutorial.sh`, containing blocks of commands. A block is simply a sequence of consecutive non-empty lines.
* For each block, we derive one or more pytest function.
* For each pytest function, we launch an agent to run, debug, fix and improve it.
* Finally, we integrate the outcome of all the agents together.

Letâs dive into how each step works.

Writing the tutorial script
---------------------------

This script is seeded with a lot of content we wrote ourselves, but it is a bit tiring once we have written 50 or so examples. So we simply:

1. Write some comments in the file, like `# Managing snapshots`
2. Ask a coding agent to fill in the blank.
3. Review and keep the ones that we like.

Since we already have a lot of documentation elsewhere in the codebaseâin particular, we have auto-generated man pages committed into the git repo, like [this one](https://github.com/imbue-ai/mngr/blob/main/libs/mngr/docs/commands/primary/create.md)âthe agent does a good job of generating examples!

In fact, even when it doesnât, itâs still useful: that means our interface is too confusing or was not properly documented, and a human may have problems figuring out how to use it too. We then used that signal to refine `mngr`âs interface to be as simple as possible.

Asking agents to generate examples turned out to be a win-win situationâwe either get good examples, or get bad examples and use that to improve `mngr` itself!

Converting tutorial blocks to pytest functions
----------------------------------------------

Now that we have a healthy amount of tutorial commands, we can ask a coding agent to convert it into pytest functions. There are a few details worth mentioning.

* Tutorial blocks tend to be concise and sometimes a bit contrived, but we want tests to be more exhaustive, covering both happy and unhappy paths. So this is a 1:N correspondence: for the same tutorial block, we can expect slight variations of the command itself or the environment to result in different outcomes, and they often deserve separate test cases.
* In order to preserve the correspondence between tutorial blocks and test functions, we also ask the agent to âdeclareâ which tutorial block it corresponds to, by citing the tutorial block in the function it generates, using a specific API in the test fixture.
* In order to keep the agent honest, we also use a simple script to check that itâs indeed the case - for each tutorial block, thereâs at least one pytest function that cites the tutorial block.

All of these are packaged into a slash command [sync-tutorial-to-e2e-tests](https://github.com/imbue-ai/mngr/blob/main/.claude/skills/sync-tutorial-to-e2e-tests/SKILL.md).

The coding agent usually canât do a very good job of writing end-to-end tests in this step, and thatâs totally expected. End-to-end tests are difficult to write for humans because there are fundamental tensions in all three stages of tests, and the reasons equally hold for coding agents:

* **Arrange**: You want to set up as little as possible to reflect real-world usage scenarios, but you need an appropriate amount of setup to make tests appropriately isolated.
* **Act**: You want to be as faithful to real-world commands as possibleâin this case, the commands from the tutorialâbut you often need some variation for the commands to be suitable for testing.
* **Assert**: You want to test the effect of the commands as closely as possible, but testing e.g. file contents too literally can end up with fragile or flaky tests.

But itâs okay if the coding agent doesnât do a good job at this stage! Weâll solve this in the next step, but letâs mention a few things about our test framework.

### The test framework

The great thing about running CLI commands is that Python (and any other programming language, really) already has an API for it: the `subprocess` module. Give it a command, and you can get the stdout, stderr and exit code.

Still, we built some utilities (really just a thin layer on top of `subprocess`) so that the test functions can be a little bit more concise and carry a little bit more information. A test function looks like this:

```
python
```

Building this extra layer also allows us to generate transcripts for the commands, which looks like:

```
sh
```

Finally, remember that `mngr` runs your agent in a tmux session, and `tmux` canât be so easily captured as simple CLI transcripts. But fear not: `mngr` allows us to define a custom âconnect commandâ, and in our test setup, we redirect it to a script by writing the following config:

```
toml
```

The `mngr-e2e-connect` script, in turn, uses `asciinema` to attach to the agent, and saves the recording in the test output directory.

We also built a combined view of all the artifactsâyou can see the CLI transcript and TUI recordings on a web page:

Orchestrating the tests
-----------------------

Now that we have all those tests, letâs run them! Hereâs the plan:

1. Collect all the test names using `pytest --collect-only`
2. For each test, launch an agent to work on it. This means several things:a. If the test is failing, either fix the test code or the code itâs testingb. If the test is passing, think about how to improve the test itself: make it more faithful to the original tutorial block, make the assertions more realistic, create additional tests etc.c. In any case, we instruct the agent to write a result JSON file.
3. Wait for them to finish, pulling their result JSON files and test artifacts.
4. Collect all the code changes they made, and use an agent to merge them all together into one mega PR.

Aside from step 1, every other step is implemented using `mngr`âs primitives:

1. Use the `mngr create` primitive to launch testing agents, which also allows us to send an initial prompt.
2. Use the `mngr list` primitive to poll the state of the agents.
3. When an agent is done, use the `mngr pull` primitive to pull down the result files and test artifacts, and then the `mngr stop` primitive to stop it.
4. Finally, use the `mngr create` primitive again to create the âintegratorâ agent that merges all the changes together.

### Integrating changes from all the agents

Integrating changes from many agents is not a trivial task, even for an agent. We spent a lot of time thinking about and iterating on this, and this is eventually what we ended up with:

* Each of the testing agents would divide its commits into implementation fixes, and non-implementation (fixing the test or just making it better, fixing some doc, etc.)
* When the integrator sees the results from all the testing agents, it just merges all the non-implementation fixes together - since these are usually uncontroversial.
* For all the implementation fixes, we instruct the integrator to rank them by importance, and keep them as distinct commits, but merge them into a single linear branch, resolving conflicts along the way.

This results in a single PR that can be easily reviewed by a human: the non-implementation fixes usually can be merged as is, and the implementation fixes can be reviewed one by one, with undesirable ones reverted.

Another thing worth mentioning is that not all testing agents produce changes that can get integrated. Some testing agents just get confused, or canât make progress unless something in the environment is fixed. We instruct the testing agents to reproduce a âblockedâ outcome in that case, and simply put that in the report we generate.

### How I developed the orchestration workflow

When I started building this workflow, I built the entire lifecycle using only agents on my local machine. This allows me to iterate super quickly, because the agents start up immediately, and if I want to peek into an agent, itâs just an instant tmux attach command away.

Eventually Iâm happy with this workflow for running 10 agents, and I want to scale up to 100 agents. My local machine is not strong enough for that, and itâs time to deploy those agents remotely. To do that, I simply change one thing in how I use `mngr create`: from `mngr create foo` to `mngr create foo@.modal` and voila! All my agents now run on Modal instead. And the subsequent interactions with the agents remain the same: `mngr list`, `mngr pull` and `mngr stop` all work the same between local and remote Modal agents, because `mngr` abstracts away the differences between them.

I lied a bit actually. When I started, I was using the Git worktree mode to create working copies for my local agents; merging their changes together is very easy, since they are already available as branches in my original Git repo. But Git worktrees donât work on remote agentsâthey use the Git mirror mode.

But fear not: I can also simply request `mngr` to also use the Git mirror mode when creating the local agent. Git worktree is the default for local agents, but youâre in no way locked into it. Now weâre exercising roughly the same code path as with remote agents, and we should now use `mngr pull` to explicitly pull the changes into my original git repo before merging the changes there. Now the workflow is really the same between local and remote.

Software composability
----------------------

Letâs take a step back and think about what we built. What we have built is essentially a small map reduce pipeline:

1. Gather a list of tests
2. Map them over an agent per test
3. Reduce the results together into a single branch

What is remarkable is that `mngr` itself doesnât know anything about map reduce: we built the pipeline, but each step uses a primitive that `mngr` provides. Unlike other multi-agent workflow tools that try to give you the âmap reduce frameworkâ, `mngr` gives you the âmapsâ and âreducesâ, just like a library of functional programming primitives, so that you can build whatever simple or complex multi-agent pipeline you want.

Software scalability
--------------------

Letâs also think about how I built the pipeline. The âend productâ runs on hundreds of Modal sandboxes, but I started out by running everything on my local machine. In other words, I started small and `mngr` allowed me to scale up smoothlessly.

But what is also remarkableâand this is a property that is often overlookedâis that I can always easily scale down back into my local machine. Sure, I canât easily run hundreds of agents on my machine because we are in the middle of a global RAM shortage, but I can always run 10 of them in parallel, and by trading space for time, I can run hundreds of agents overnight.

When we talk about software scalability, we often focus on two things: the ability to scale **up**, and the **incremental** cost to do so. But we donât talk nearly enough about the ability to scale **down**, and the **upfront** cost you have to pay.

In the world of increasingly large tech conglomerates with highly specialized infrastructure teams and billions of users, being only able to scale up and paying a lot of cost upfront is not a bad tradeoff. But for small teams, being able to get started quickly and easily and locallyâwithout the big up-front investmentâis often much more valuable. When doing so with `mngr`, itâs still easy to scale up later if you want to.

`mngr` is engineered to be truly scalable: the incremental cost is low, as is the upfront cost. It is an ergonomic CLI for managing a few local âpet agents,â but you can also just ask it to run 100 agents on Modal.

The future of software development
----------------------------------

Weâre really happy that weâve been able to leverage `mngr` to make itself better, but this is just the beginning.

Imbueâs mission is to make tech serve humans, and the way we are building `mngr` is consistent with that mission. Multi-agent workflowsâwhether itâs running a few coding agents locally, or launching hundreds of them remotelyâare quickly becoming the key to fully harnessing the power of AI-assisted software engineering.

Instead of locking you to a specific platform, `mngr` gives you primitives that you can use locally or remotely, works at tiny scales and large scales alike, giving you all the freedom to build the workflows that suit your personal or business needs.

`mngr` is free, open source, and [available here](https://github.com/imbue-ai/mngr/). Try it out and let us know what you think on [X](https://x.com/joshalbrecht/status/2039727392915349902) or [Product Hunt](https://www.producthunt.com/products/imbue-7).