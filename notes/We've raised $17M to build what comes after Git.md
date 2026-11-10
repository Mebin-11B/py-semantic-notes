---
title: "We've raised $17M to build what comes after Git"
url: https://blog.gitbutler.com/series-a
clipped: 2026-06-17 01:19:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [We've raised $17M to build what comes after Git](https://blog.gitbutler.com/series-a)

## Digest Summary
GitButler announced a $17 million Series A round led by a16z, with continued participation from seed investors Fly Ventures and A Capital, and added a16z partner Peter Levine to its board. Co‑founder Scott Chacon, a former GitHub co‑founder, explained that the company aims to redesign version‑control workflows that were built for older, linear Git models. The technical preview of the GitButler CLI targets short‑lived, trunk‑based GitHub Flow, enabling stacked branches, multitasking, easy undo, and seamless integration into existing Git projects. Chacon emphasized that current development friction stems from fragmented context across tools, people, and AI agents, and that GitButler intends to make coding more “social” by surfacing merge‑conflict warnings early, allowing branches to be stacked on teammates’ work, and preserving conversation and change metadata within Git. The funding will accelerate development of this next‑generation collaboration layer, which the team describes as infrastructure for future software construction rather than merely a better Git implementation.

## Discussion Summary
The discussion reflects skepticism about the high development cost and the ability to achieve sufficient network effects for a commercial version‑control tool, questioning whether it can truly replace Git or merely abstracts it. Commenters note Git’s widespread adoption, reliability once mastered, and the difficulty of displacing it, while also acknowledging existing pain points that the new tool might address. References to alternative projects such as Pijul and jj illustrate interest in alternatives, but overall confidence in the new offering’s market viability remains low.

---

## Full Article

Today we’re announcing that **GitButler has raised a $17M Series A** led by [a16z](https://a16z.com/) with continuing support from our lead seed investors, [Fly Ventures](https://fly.vc/) and [A Capital](https://acapital.com/).

I know what you’re thinking. You’re hoping that we’ll use phrases such as “*we’re excited*,” “*this is just the beginning*,” and “*AI is changing everything*”. While all those things are true, I’ll try to avoid them and instead make this announcement a little more personal.

![Our new board member, a16z's Peter Levine, and myself at the GitButler Series A signing. We're excited to have Peter join us - he and I also worked together on GitHub's board.](https://blog.gitbutler.com/_next/image?url=https%3A%2F%2Fd2m1ukvwmu7gz4.cloudfront.net%2FCleanShot%25202026-02-17%2520at%252011.06.49%25402x.png&w=3840&q=75)

Our new board member, a16z's Peter Levine, and myself at the GitButler Series A signing. We're excited to have Peter join us - he and I also worked together on GitHub's board.

For me this is a long story.

I was one of the cofounders of [GitHub](https://github.com/) and over the last 15 years I’ve watched Git go from a rather niche developer tool written for a very esoteric collaboration style to the foundational infrastructure of all software development on the planet. I may have even had a small hand in some part of that.

What I learned from watching that story unfold is that developer platforms win when they remove friction from collaboration, and when they let the people producing code have less overhead to deal with.

GitButler was started three years ago because we felt like our development practices have been shoehorned into what Git could do for such a long time, it would be amazing to see what we could do with tooling that was actually designed for those practices.

That’s fundamentally what is behind this round.

We think software development is quickly moving into a new phase, and the problem that Git has solved for the [last 20 years](https://blog.gitbutler.com/20-years-of-git) is overdue for a redesign. Today, with Git, we're all teaching swarms of agents to use a tool built for sending patches over mailing lists. That's far from what is needed today.

At GitHub, one thing became painfully clear over and over: developers don’t struggle because they can’t write code. They struggle because context falls apart between tools, between people, and now between people and agents. The hard problem is not generating change, it’s organizing, reviewing, and integrating change without creating chaos.

The old model assumed one person, one branch, one terminal, one linear flow. Not only has the problem not been solved well for that old model, it’s now only been compounded with our new AI tools.

Last week we released our first answer to that, the technical preview of [the GitButler CLI](https://gitbutler.com/cli).

VIDEO

A quick tour through a typical workflow with the new GitButler CLI.

This is a tool designed for the [GitHub Flow](https://scottchacon.com/2011/08/31/github-flow/) style - the short lived branch, trunk based workflows that so many of us are using. This is a tool designed for humans, designed for agents, designed for scripting. Designed to [stack branches](https://docs.gitbutler.com/cli-guides/cli-tutorial/branching-and-commiting#stacked-and-parallel-branches), to [multitask](https://docs.gitbutler.com/cli-guides/cli-tutorial/branching-and-commiting#stacked-and-parallel-branches), to control and [organize](https://docs.gitbutler.com/cli-guides/cli-tutorial/rubbing) your changes, to easily [undo](https://docs.gitbutler.com/cli-guides/cli-tutorial/operations-log) - to be simple, powerful and intuitive, no matter who (or what) you are. Best of all, it just drops into any existing Git project.

But of course, that’s just the beginning. (*Damn*, I said I wasn’t going to say that…)

There was a tagline at GitHub that I always loved, but I never felt like we lived up to the promise of: “**Social Coding**”.

While GitHub certainly made it easier to collaborate on open source projects with forks and pull requests, it otherwise didn’t much improve the process of working together. There are still lists of issues and kanban boards, there are still patches (we just call them PRs now), we still chat in external chat rooms. We don’t look at commit messages and our PR descriptions aren’t stored in Git and usually lost in history. Heck, it could be argued that development in teams is *less* social than it was when version control was centralized.

But what if coding was actually *social*? What if it was easier to for a team to work together than it is to work alone?

Imagine your version control tool taking what you’ve worked on and helping you craft logical, beautiful changes with proper context. Imagine being able to access agent interactions, related conversations and other information we’re currently losing. Imagine your tools telling you as soon as there are possible merge conflicts between teammates, rather than at the end of the process. Imaging being able to work on a branch stacked on a coworkers branch while you’re both constantly modifying them. Imagine your agent being fully aware of not only what your other agents are working on, but what everyone on your team is working on, right now.

There is so much more that this fundamental layer of our software tooling could be doing for us. This is what we’re doing at GitButler, this is why we’ve raised the funding to help build all of this, faster.

We’re not building some “*better git*”.

We’re building the infrastructure for how software gets built next.

[![Scott Chacon](https://blog.gitbutler.com/_next/image?url=%2Fprofiles%2Fschacon.jpg&w=256&q=75)](https://blog.gitbutler.com/author/schacon)

Written by [Scott Chacon](https://blog.gitbutler.com/author/schacon)

Scott Chacon is a co-founder of GitHub and GitButler, where he builds innovative tools for modern version control. He has authored Pro Git and spoken globally on Git and software collaboration.