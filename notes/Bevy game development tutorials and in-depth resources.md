---
title: "Bevy game development tutorials and in-depth resources"
url: https://taintedcoders.com/
clipped: 2026-06-17 01:19:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Bevy engine
  - Rust programming
  - Entity Component System
  - game development
  - technical tutorials
related:
  - "[[Adventure Game Studio OSS software for creating adventure games]]"
  - "[[Rust Programming]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The taintedcoders.com website provides comprehensive, free, open-source game development guides and tutorials for the Rust-based Bevy game engine.
>
> **Key points:**
> - Guides target Bevy version 0.18, structuring learning paths from a basic "Pong Tutorial" to advanced "TLDR" architectural overviews.
> - Explores Bevy's Entity Component System (ECS) architecture, which decouples data (components) from logic (systems) for high performance.
> - Developed by Nolan Tait, a veteran Ruby developer who built the static site using a custom Ruby generator called Staticky.
> - Hacker News discussion highlights the scarcity of high-quality free Bevy resources and discusses the steep learning curve when transitioning from dynamic languages (like Ruby) to systems languages (like Rust).
>
> **Concept links:** [[Bevy Engine]], [[Rust Programming]], [[Entity Component System]], [[Game Development]], [[Technical Tutorials]], [[Open Source Engine]]
>
> **Suggested connections:**
> - [[Adventure Game Studio OSS software for creating adventure games]] — comparing specialized 2D narrative/adventure game IDEs with modern systems-level ECS game engines like Bevy.
> - [[Rust Programming]] — analyzing developer experiences, language transitions (e.g., from Ruby to Rust), and the benefits of memory safety in game engines.
<!-- ai-summary:end -->

# [Bevy game development tutorials and in-depth resources](https://taintedcoders.com/)

## Digest Summary
The site offers a series of Bevy game‑development guides originally created for a private learning group and now expanded for public use. Authored by a programmer with a decade of Ruby web experience, the site itself is generated with a custom Ruby‑based static site generator called Staticky. It includes links to additional resources such as a Bevy starter project, a curated collection of notable Bevy repositories, and a Rust‑on‑Solana blog (Soldev). All tutorials target Bevy version 0.18. New users are directed to the “Pong Tutorial” for introductory learning, while more experienced developers are encouraged to start with the concise “TLDR” guide.

## Discussion Summary
Comments note a scarcity of free, comprehensive resources for the Bevy engine, observing that most available material is paid. There is also surprise at the transition from Ruby to Rust, emphasizing the perceived difficulty of moving between the two languages and suggesting that Rust presents a distinctly different development experience. Overall, the feedback highlights limited accessible learning options and curiosity about the challenges associated with adopting Rust for game development.

---

## Full Article

Bevy game development
=====================

[Bevy](https://bevy.org) is an open source game engine built in Rust that uses an
Entity Component System (ECS) architecture.

These guides were originally created for a group of friends
to learn from. Over the years they have evolved into the [Rails guides](https://guides.rubyonrails.org) for Bevy.

[I am](https://github.com/nolantait) a programmer who has worked mostly with Ruby on the web over
the last decade. This site was built with [Staticky](https://github.com/nolantait/staticky) a static site generator I built with Ruby.

If you like these guides, you might also like my [Bevy Starter](https://github.com/nolantait/bevy-starter) and [Awesome Bevy](https://github.com/nolantait/awesome-bevy) repos where I am collecting resources for Bevy developers. You can also check out [Soldev](https://soldev.ca) where I am writing about Rust development on Solana.

These guides are up to date with Bevy version 0.18

If you're new here and looking for a good place to start I
recommend checking out the [Pong Tutorial](https://taintedcoders.com/bevy/tutorials/pong-tutorial) if you are a beginner, or the [TLDR](https://taintedcoders.com/bevy/tldr) if you are more advanced.