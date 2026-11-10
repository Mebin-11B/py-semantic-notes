---
title: "Three constraints before I build anything"
url: https://jordanlord.co.uk/blog/3-constraints/
clipped: 2026-06-17 01:11:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Three constraints before I build anything](https://jordanlord.co.uk/blog/3-constraints/)

## Digest Summary
The author outlines three pre‑building constraints to keep projects focused and viable.  
1. **One‑page definition** – All ideas must be captured in a single, precise page that serves as the north‑star for investors, team members, and personal planning. If the concept cannot be expressed within one page, it is deemed overly complex and is not pursued.  
2. **Separable core technology** – The product must rely on a distinct, reusable core tech (method, tool, library, or methodology) that can exist independently of the product itself. This core tech provides long‑term leverage and aligns with the creator’s broader vision; without it, the idea lacks sufficient impact.  
3. **Defining constraint** – Each product needs a central, user‑visible constraint that gives it identity and limits feature creep (e.g., Minecraft’s blocks, IKEA’s flat‑pack design). This constraint should be evident in the one‑pager and guide all design decisions.  

If an idea fails any of these rules, the author does not build it.

## Discussion Summary
The comments largely endorse the idea that limiting a product to a few powerful, composable primitives improves design, usability, and learning speed, with many readers citing personal experience or analogous examples from software, games, and design. Several contributors note that articulating constraints on a concise “one‑page” level helps align teams and prevents misguided development, while a few request clearer practical illustrations and express cautious optimism about applying the principles beyond software. Overall sentiment is positive, emphasizing the value of constraints and clear abstraction.

---

## Full Article

These are the 3 constraints that I use before I start building anything. I'm a
believer in constraints as an enabler for creativity. Constraints help us
collapse the search space, and figure out innovative solutions to problems.

I've been a builder for 10 years, and I've built products that went nowhere
because they were either too complex or had no identity. These are the
constraints that I landed on after making those mistakes.

One page or it doesn't get built
--------------------------------

*This constraint limits complexity and ambiguity.*

Write a one pager for all of your ideas. Your one pager captures your north
star. It's non-negotiable, precise, ambitious, and lean. Once your one pager is
written, it is applied to all different types of communication. Share it as a
memo for investors, contributors, team members, friends, or family. Working
collaboratively on a product, there will always be contention points and
conflict, it can sometimes be difficult to know what battles to pick. If it's
not in the one pager, then it's either not worth fighting over, or the one pager
ought to be amended to include the thing. Not only is a one pager useful for
communication, it's useful for organising your own thoughts. If you can't fill
one page, don't fill the gaps with fluff, it means you're not ready to build.
First research, plan, prototype, then write the one pager again. Iterate. If it
requires more than one page, it's too complex, don't build it.

The core tech must be separable from the product
------------------------------------------------

*This constraint limits you to ideas that have real leverage and originality.*

Develop a core piece of technology that supports your product and is not the
product itself. The core tech is a method, skill, tool, or even product that
supports what you're doing today but must survive without it. It's a type of
reusable IP. Why? Separating the core tech forces you to think beyond the
product that you're building. Products pivot in direction all the time, while
your core tech is constant and compounding. Compounding efforts have non-linear
gains over longer time horizons. Linus Torvalds developed git to improve the
Linux kernel development workflow. HashiCorp has HCL (HashiCorp Configuration
Language). Google has Kubernetes. But you don't need big tech resources to build
core tech, it could be a library that you extract from your codebase, or even a
methodology that you refine and commit to. Your core tech is your long term
commitment. It is independent of your product's direction. However, it must be
aligned with you or your company's long term vision. If your idea doesn't enable
core tech, then it isn't high enough leverage.

One defining constraint must shape the product
----------------------------------------------

*This constraint limits feature creep and forces identity.*

Define your own constraint that is front and centre to your product. That means
the user sees and interacts with it all the time. It is obvious and it is what
gives your product identity. A good constraint gives your product a *feel*, it
permeates through all parts of the user experience. Minecraft is built entirely
from blocks. IKEA is flat-pack, self-assembly furniture. The constraint that you
choose limits scope by reducing your decision space, enabling you to concentrate
on the problems that really make the difference. If you don't choose a
constraint, or choose a bad constraint, you will build a bloated product that
will try to do everything. The design of your product will "fall out" of a
well-designed constraint. Like in your product, your constraint must be front
and centre in your one pager.

Closing Rule
------------

When it comes to deciding what to build, if it fails any of these constraints,
then I don't build it.