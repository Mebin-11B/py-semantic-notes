---
title: "Zed 1.0"
url: https://zed.dev/blog/zed-1-0
clipped: 2026-06-17 01:10:08
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Zed 1.0](https://zed.dev/blog/zed-1-0)

## Digest Summary
Zed 1.0 is a native desktop code editor built from the ground up in Rust, using a custom GPU‑accelerated UI framework (GPUI) rather than web‑based technologies like Electron. By owning the entire stack, the team eliminated platform constraints and achieved higher performance and extensibility. The editor now supports a full language ecosystem (Git, SSH, debugging, etc.) across macOS, Windows, and Linux, with over a million lines of code. Zed is “AI‑native”: multiple AI agents (Claude, Codex, OpenCode, Cursor) can run in parallel via the Agent Client Protocol, providing keystroke‑level edit predictions. A forthcoming Business edition will add centralized billing, role‑based access, and team management. Development continues on DeltaDB, a CRDT‑based synchronization engine that records character‑level edits, enabling real‑time collaboration among humans and AI agents. Zed’s release cadence remains weekly, and the project is open to contributors and hiring.

## Discussion Summary
The discussion shows strong enthusiasm for Zed’s speed, lightweight design, remote‑SSH integration, and the novel agent workflow, with many users citing it as a compelling alternative to heavier IDEs. Praise also extends to its modern UI, fast startup, and open‑source foundation. Recurrent criticisms focus on incomplete language support, intrusive warnings, limited extensibility, and UI quirks such as the search tab, diff view, terminal handling, theme accessibility, and licensing language. Platform‑specific performance or stability issues on Linux and macOS are noted, and several users request richer feature sets and configurability. Overall sentiment is mixed‑positive, acknowledging both impressive strengths and notable gaps.

---

## Full Article

To create a fundamentally better editor, we had to invent a new approach to building desktop software. Our previous editor, [Atom](https://zed.dev/blog/we-have-to-start-over), was built as a fork of Chromium, spawning the Electron framework in the process. Electron eventually became the foundation of VS Code (which today seems to be forked into a new AI code editor every other week). Web technology offered an easy path to shipping flexible software, but it also imposed a ceiling. No matter how hard we worked, we couldn't make Atom better than the platform it was built on.

So we started over. Instead of building Zed like a web page, we built it [like a video game](https://zed.dev/blog/videogame), organizing the entire application around feeding data to shaders running on the GPU. That meant writing our own UI framework, [GPUI](https://zed.dev/blog/gpui-ownership), from scratch in Rust.

Owning every layer of our stack lets us take Zed places that no one building on borrowed foundations can go, but we knew from the beginning that it wasn't going to be an easy path. Thanks to years of hard work by our team and community, Zed is closer than ever to that ideal tool we set out to create. We've added a ton of capabilities while remaining true to our core ethos of craft and performance, and hundreds of thousands of developers now rely on Zed to ship software each day. That's part of what gives us the confidence to declare version 1.0.

Zed is 1.0

Developers expect a modern editor to support dozens of languages and their ecosystems, endless variations and edge cases across every stack: [Git integration](https://zed.dev/git), [SSH remoting](https://zed.dev/blog/remote-development), a [Debugger](https://zed.dev/debugger), and, yes, [rainbow brackets](https://zed.dev/blog/rainbow-brackets). We've spent five years building that surface area across Mac, [Windows](https://zed.dev/windows), and [Linux](https://zed.dev/linux), exceeding a million lines of code.

Zed is also an AI-native editor. You can run [multiple agents in parallel](https://zed.dev/blog/parallel-agents), and [edit predictions](https://zed.dev/blog/edit-prediction) suggest your next change at keystroke granularity and with the speed you've come to expect from Zed. The [Agent Client Protocol](https://zed.dev/blog/bring-your-own-agent-to-zed) opens Zed up to a growing number of the best agents out there, including Claude Agent, Codex, OpenCode, and more recently Cursor. We built AI into our editor's foundation instead of bolting it on top.

We're also launching Zed for Business. Companies have been asking us for a way to roll out Zed to their engineering teams, and very soon they can, with centralized billing, role-based access controls, and team management.

1.0 doesn't mean "done". It also doesn't mean "perfect". It means we've reached a tipping point where most developers can quickly feel at home in Zed. If you tried Zed a year or two ago and bounced because something was missing, 1.0 is our invitation to try again. Zed is more capable than it's ever been, and still more performant.

Our vision hasn't changed since we started: we're building the most performant and collaborative coding environment. What's changed is what collaboration means while creating software. It used to mean humans working together in real time. Now it means humans and AI agents, working in the same space, on the same code.

Building our own foundations is what got us to 1.0, and it's also what makes the next chapter possible. We're actively developing [DeltaDB](https://zed.dev/blog/sequoia-backs-zed), a synchronization engine built on [CRDTs](https://zed.dev/blog/crdts) that tracks every change with character-level granularity. DeltaDB lets multiple humans and agents share a single, consistent view of the codebase as it evolves. DeltaDB will allow you to invite teammates into conversations with agents to review and evolve agentic code directly in the context from which it's generated.

This vision depends on deep ownership of our fundamental primitives. It's not an experience we'd be able to ship inside of someone else's browser engine.

We've shipped over a thousand versions of Zed, but all of them began with zero. Today, that changes.

We'll keep shipping every week, the way we always have. The list of things to build will never end, and that's exactly how we like it. Each release moves the craft forward.

If you want to try Zed, [download now](https://zed.dev/download). If you want to help us build it, [join us](https://zed.dev/jobs)!

![Zed is now 1.0](https://zed.dev/img/post/one-point-zero/sticker.webp)

### Related Posts

Check out similar blogs from the Zed team.

---

### Looking for a better editor?

You can try Zed today on macOS, Windows, or Linux. [Download now](https://zed.dev/download)!

---

### We are hiring!

If you're passionate about the topics we cover on our blog, please consider [joining our team](https://zed.dev/jobs) to help us ship the future of software development.