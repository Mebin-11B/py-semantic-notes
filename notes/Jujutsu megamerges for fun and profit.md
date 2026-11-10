---
title: "Jujutsu megamerges for fun and profit"
url: https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit
clipped: 2026-06-17 01:14:20
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Version Control Systems
  - Git Workflows
  - Jujutsu VCS
  - Software Branching
  - Software Integration
related:
  - "[[Version Control Systems]]"
  - "[[Git Workflows]]"
  - "[[Jujutsu VCS]]"
  - "[[Software Branching]]"
  - "[[Software Integration]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Jujutsu's "megamerge" workflow uses multi-parent octopus merges to locally combine all active development branches, resolving conflicts early and simplifying multitasking.
>
> **Key points:**
> - A megamerge is a local octopus merge commit combining feature branches, bugfixes, PRs, and config branches.
> - Since work is done on top of this merged state, compile errors and merge conflicts are caught and resolved immediately.
> - Jujutsu's `absorb` and rebasing commands allow changes to automatically propagate back to their correct constituent branches.
> - Convenient revset aliases help automate and manage the stack rebases and stage operations.
>
> **Concept links:** [[Version Control Systems]], [[Git Workflows]], [[Jujutsu VCS]], [[Software Branching]], [[Software Integration]]
>
> **Suggested connections:**
> - [[Jujutsu VCS]] — how this modern version control system enables features like multi-parent merge edits.
> - [[Software Branching]] — comparing trunk-based development with local multi-branch staging.
<!-- ai-summary:end -->

# [Jujutsu megamerges for fun and profit](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit)

## Digest Summary
Jujutsu’s “megamerge” workflow uses an octopus merge (a commit with three + parents) to combine every branch a developer cares about—feature branches, bug‑fixes, pending PRs, local setup branches, etc.—into a single, local “megamerge” commit. The megamerge itself is never pushed; only its constituent branches are published. Because all work is built on this combined state, the codebase compiles and runs only if all parts interoperate, dramatically reducing surprise merge conflicts and making task switching frictionless.  

Creating a megamerge is simple: `jj commit --message "megamerge"` with each target branch as a parent, yielding an empty commit atop the merged history. New work is done above this commit. Changes are integrated using Jujutsu’s `absorb` (auto‑squash into downstream commits), `squash` (interactive or full), or `rebase` to move WIP commits onto appropriate branches.  

Convenient revset aliases streamline the process:  

* `closest_merge(to)` finds the nearest merge ancestor.  
* `stack` rebases a revset after `trunk()` and before the megamerge.  
* `stage` stacks the entire descendant chain after the megamerge.  
* `restack` rebases only mutable commits onto `trunk()` (`roots(trunk()..) & mutable()`).  

The workflow keeps the megamerge up‑to‑date, isolates personal changes from others’ branches, and enables rapid, low‑conflict development across many parallel streams.

## Discussion Summary
The comments convey strong enthusiasm for Jujutsu, noting its low‑risk entry point, streamlined megamerge workflow, and supportive Discord community, with many users recommending exclusive adoption after a short trial. Frequent praise highlights features such as parallelize, stack aliases, and the absence of a staging area, while calls for improved documentation, beginner guides, and tighter IDE integration appear. Concerns focus on managing complex megamerge conflicts, coordination with non‑jj collaborators, and missing Git‑like capabilities such as tags and preserved commit dates. Overall sentiment is largely positive, tempered by requests for better tooling and resources.

---

## Full Article

*This article is written both for intermediate Jujutsu users and for Git users
who are curious about Jujutsu.*

Iâm a big [Jujutsu](https://jj-vcs.github.io/jj/latest) user, and Iâve found myself relying more and more on
what we in the JJ community colloquially call the âmegamergeâ workflow for my
daily development. Itâs surprisingly under-discussed outside of a handful of
power users, so I wanted to share what that looks like and why itâs so handy,
especially if youâre in a complex dev environment or tend to ship lots of small
PRs.

*In a hurry? [Skip to the end](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit#tldr) for some quick tips.*

Merge commits arenât what you think they are
----------------------------------------------

If youâre an average Git user (or even a Jujutsu user who hasnât dug too deep
into more advanced workflows), you may be surprised to learn that there is
absolutely nothing special about a merge commit. Itâs not some special case
that has its own rules. Itâs just a normal commit that has multiple parents. It
doesnât even have to be empty![1](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit#user-content-fn-1)

```
@  myzpxsys Isaac Corbrey 12 seconds ago 634e82e2
â  (empty) (no description set)
â    mllmtkmv Isaac Corbrey 12 seconds ago git_head() 947a52fd
âââ®  (empty) Merge the things
â â  vqsqmtlu Isaac Corbrey 12 seconds ago f41c796e
â â  deps: Pin quantum manifold resolver
â â  tqqymrkn Isaac Corbrey 19 seconds ago 0426baba
âââ¯  storage: Align transient cache manifolds
â  zzzzzzzz root() 00000000
```

Gotta put it all together!

You may be even more surprised to learn that merge commits are not limited
to having two parents. We unofficially call merge commits with three or more
parents âoctopus mergesâ, and while you may be thinking to yourself âin what
world would I want to merge more than two branches?â, this is actually a really
powerful idea. Octopus merges power the entire megamerge workflow!

So what the hell is a megamerge?
--------------------------------

Basically, in the megamerge workflow you are rarely working directly off the
tips of your branches. Instead, you create an octopus merge commit (hereafter
referred to as âthe megamergeâ) as the child of every working branch you care
about. This means bugfixes, feature branches, branches youâre waiting on PRs
for, other peoplesâ branches you need your code to work with, local environment
setup branches, even private commits that may not be or belong in any branch.
*Everything* you care about goes in the megamerge. Itâs important to remember
that **you donât push the megamerge**, only the branches it composes.

```
@  mnrxpywt Isaac Corbrey 25 seconds ago f1eb374e
â  (empty) (no description set)
â      wuxuwlox Isaac Corbrey 25 seconds ago git_head() c40c2d9c
âââ¬ââ®  (empty) megamerge
â â â  ttnyuntn Isaac Corbrey 57 seconds ago 7d656676
â â â  storage: Align transient cache manifolds
â â â  ptpvnsnx Isaac Corbrey 25 seconds ago 897d21c7
â â â  parser: Deobfuscate fleem tokens
â â â  zwpzvxmv Isaac Corbrey 37 seconds ago 14971267
â â â  infra: Refactor blob allocator
â â â  tqxoxrwq Isaac Corbrey 57 seconds ago 90bf43e4
â âââ¯  io: Unjam polarity valves
â â  moslkvzr Isaac Corbrey 50 seconds ago 753ef2e7
â â  deps: Pin quantum manifold resolver
â â  qupprxtz Isaac Corbrey 57 seconds ago 5332c1fd
âââ¯  ui: Defrobnicate layout heuristics
â  wwtmlyss Isaac Corbrey 57 seconds ago 5804d1fd
â  test: Add hyperfrobnication suite
â  zzzzzzzz root() 00000000
```

Scary! Too much merge!

Itâs okay if this sounds like a lot. After all, you know how much effort you
put into switching contexts if you have to revisit an old PR to get it reviewed,
among other things. However, this enables a few really valuable things for you:

1. **You are always working on the combined sum of all of your work.** This
   means that if your working copy compiles and runs without issue, you know
   that your work will all interact without issue.
2. **You rarely have to worry about merge conflicts.** You already donât need to
   worry about merge conflicts a ton since conflicts are a first-class concept
   in Jujutsu, but since youâre literally always merging your changes together
   youâll never be struck with surprise merge conflicts on the forge side.
   There might be the occasional issue with contributorsâ changes, but in my
   experience this hasnât been a major problem.
3. **Thereâs way less friction when switching between tasks.** Since youâre
   always working on top of the megamerge, you never need to go to your VCS to
   switch tasks. You can just go edit what you need to. This also means itâs way
   easier to make small PRs for drive-by refactors and bugfixes.
4. **Itâs easier to keep your branches up to date.** With a little magic, you
   can keep your entire megamerge up to date with your trunk branch with a
   single rebase command. Iâll show you how to do that later on.

How do I make one?
------------------

Starting a megamerge is super simple: just make a new commit with each branch
you want in the megamerge as a parent. I like to give that commit a name and
leave it empty, like so:

```
jj new x y z
jj commit --message "megamerge"
```

Making megamerges. It's not so hard after all!

Youâre then left with an empty commit on top of this whole thing. This is where
you do your work! Anything above the megamerge commit is considered WIP. Youâre
free to split things out as you need to, make multiple branches based on that
megamerge commit, whatever you want to do. Everything you write will be based on
the sum of everything within the megamerge, just like we wanted!

Of course, at some point youâll be happy with what you have, and youâll be left
wondering:

How do I actually submit my changes?
------------------------------------

How you get your WIP changes into your megamerge depends on where they need to
land. If youâre making changes that should land in existing changes, you can
use the `squash` command with the `--to` flag to shuffle them into the right
downstream commits. If your commit contains multiple commitsâ worth of changes,
you can either `split` it out into multiple commits before squashing them or
(what I prefer) interactively squash with `squash --interactive` to just pick
out the specific pieces to move.

```
# Squash an entire WIP commit (defaults to `--from @`)
jj squash --to x --from y

# Interactively squash part of a WIP commit (defaults to `--from @`)
jj squash --to x --from y --interactive
```

Hunk, I choose you!

Of course, Jujutsu is a beautiful piece of software and has some automation for
this! The `absorb` command will do a lot of this for you by identifying which
downstream mutable commit each line or hunk of your current commit belong in and
**automatically squashing them down for you**. This feels like magic every time
I use it (and not the evil black box black magic kind of magic where nothing can
be understood), and itâs one of the core pieces of Jujutsuâs functionality that
make the megamerge workflow so seamless.

```
# Automagically autosquash your changes (defaults to `--from @`)
jj absorb --from x
```

Ope, that was fast.

Absorbing wonât always catch everything in your commit, but itâll usually get at
least 90% of your changes. The rest are either easily squashable downstream or
unrelated to any previous commit.

Conveniently, things arenât much more complicated if I have changes that belong
in a new commit. If the commit belongs in one of the branches Iâm working on, I
can just rebase it myself and move the bookmark accordingly.

```
jj commit
jj rebase --revision x --after y --before megamerge
jj bookmark move --from y --to x
```

Letâs break that rebase down to better understand how it works:

```
# We're gonna move some commits around!
jj rebase
    # Let's move our WIP commit(s) x...
    --revision x
        # so that they come after y (e.g. trunk())...
        --after y
            # and become a parent of the megamerge.
            --before megamerge
```

A little bit of rocket surgery, as a treat.

If Iâve started work on an entirely new feature or found an unrelated bug to
fix, then itâs even simpler! Using a few aliases, I can super easily include new
changes in my megamerge:[2](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit#user-content-fn-3)

```
[revset-aliases]
# Returns the closest merge commit to `to`
"closest_merge(to)" = "heads(::to & merges())"

[aliases]
# Inserts the given revset as a new branch under the megamerge.
stack = ["rebase", "--after", "trunk()", "--before", "closest_merge(@)", "--revision"]
```

Hereâs a quick explanation of what `closest_merge(to)` is actually doing:

```
heads(                 # Return only the topologically tip-most commit within...
      ::to             # the set of all commits that are ancestors of `to`...
           & merges()) # ...that are also merge commits.
```

Using that revset alias, `stack` lets us target any revset we want and insert it
between `trunk()` (your main development branch) and our megamerge commit:

```
jj stack x::y
```

Whoa, that was neat!

This is more useful if I have *multiple* stacks of changes I want to include in
parallel; if itâs just one, I have another alias that just gets the entire stack
of changes after the megamerge:

```
[aliases]
stage = ["stack", "closest_merge(@)+:: ~ empty()"]
```

```
closest_merge(@)+::           # Return the descendants of the closest merge
                              # commit to the working copy...
                    ~ empty() # ...without any empty commits.
```

This one doesnât require any input! Just have your commits ready and stage âem:

```
jj stage
```

Wait, what? You can do that?

The last missing piece of this megamerge puzzle is (unfortunately) dealing with
the reality that is *other people*:

How do I keep all this crap up to date?
---------------------------------------

Thatâs a great question, and one I spent a couple months trying to answer in
a general sense. Jujutsu has a really easy way of rebasing your entire working
tree onto your main branch:

```
jj rebase --onto trunk()
```

Nice.

However, this only works if your entire worktree is *your* changes. When you try
to reference commits you donât own (like untracked bookmarks or other peopleâs
branches) Jujutsu will stop early to protect them from being rewritten.[3](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit#user-content-fn-4)

Wait, not so nice. How do I do this?

Letâs fix that by rebasing only the commits we actually control. I struggled
with this one for a while, but thankfully the Jujutsu community is awesome.
Kudos to [Stephen Jennings](https://jennings.io) for coming up with this awesome revset:

```
[aliases]
restack = ["rebase", "--onto", "trunk()", "--source", "roots(trunk()..) & mutable()", "--simplify-parents"]
```

```
roots(                       # Get the furthest upstream commits...
      trunk()..)             # ...in the set of all descendants of ::trunk()...
                 & mutable() # ...and only return ones we're allowed to modify.
```

Rather than trying to rebase our entire working tree (like `jj rebase --onto trunk()` tries to do), this alias only targets commits weâre actually allowed to
move. This leaves behind branches that we donât control as well as work thatâs
stacked on top of other peopleâs branches. With `--simplify-parents` we also can
clean up any gross edges left behind by this process. It has yet to fail me,
even with monster ninefold mixed-contributor megamerges! (Say that five times
fast.)

There we go, that's better!

TL;DR
-----

Jujutsu megamerges are super cool and let you work on many different streams of
work simultaneously. Read the whole article for an in-depth explanation of how
they work. For a super ergonomic setup, add these to your config with `jj config edit --user`:

```
[revset-aliases]
"closest_merge(to)" = "heads(::to & merges())"

[aliases]
# `jj stack <revset>` to include specific revs
stack = ["rebase", "--after", "trunk()", "--before", "closest_merge(@)", "--revision"]

# `jj stage` to include the whole stack after the megamerge
stage = ["stack", "closest_merge(@)+:: ~ empty()"]

# `jj restack` to rebase your changes onto `trunk()`
restack = ["rebase", "--onto", "trunk()", "--source", "roots(trunk()..) & mutable()", "--simplify-parents"]
```

Use `absorb` and/or `squash --interactive` to get new changes into existing
commits, `commit` and `rebase` to make new commits under your megamerge,
and `commit` with `stack` or `stage` to move entire branches into your
megamerge.[4](https://isaaccorbrey.com/notes/jujutsu-megamerges-for-fun-and-profit#user-content-fn-5)

```
# Changes that belong in existing commits
jj absorb
jj squash --to x --interactive

# Changes that belong in new commits
jj rebase --revision y --after x

# Stack anything on top of the megamerge into it
jj stage

# Stack specific revsets into the megamerge
jj stack w::z
```

Remember that megamerges arenât really meant to be pushed to your remote;
theyâre just a convenient way of showing yourself the whole picture. Youâll
still want to publish branches individually as usual.

I live in this constantly, and you can too.

Megamerges may not be everyoneâs cup of tea â Iâve certainly gotten a few
horrified looks after showing my working tree â but once you try them, youâll
likely find they let you bounce between tasks with almost no effort. Give them
a try!

Errata
------

* I completely forgot about `--simplify-parents` on `restack`! This makes it so
  you can get a clean log after restacking your commits by eliminating redundant
  edges (e.g. if A-B-C and A-C exist, `simplify-parents` will eliminate A-C).
* `stage` should be using `closest_merge(@)+::`, not `closest_merge(@)..` as you
  donât want to pull in everything from all time! `x..` does technically include
  `x+::`, but itâs equivalent to `~::x`, which includes **anything that isnât a
  direct ancestor of `x`!**