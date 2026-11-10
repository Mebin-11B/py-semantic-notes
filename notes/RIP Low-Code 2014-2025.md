---
title: "RIP Low-Code 2014-2025"
url: https://www.zackliscio.com/posts/rip-low-code-2014-2025/
clipped: 2026-06-17 01:53:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [RIP Low-Code 2014-2025](https://www.zackliscio.com/posts/rip-low-code-2014-2025/)

## Digest Summary
Low‑code platforms were created to let non‑technical users build production‑ready applications with minimal code, freeing developer capacity and accelerating delivery. Forrester projected the market to reach $50 billion by 2028, and adoption has been strong. The emergence of AI‑driven, “agentic” coding tools changes the ROI calculus: AI can generate functional code faster and cheaper than integrating and maintaining external low‑code solutions, while avoiding the extra total‑cost‑of‑ownership those platforms impose. Cloud Capital’s experience illustrates this shift—initially reliant on Retool for internal dashboards and workflows, the team prototyped a standalone tool using AI‑assisted coding, found it faster, more maintainable, and better aligned with their product UI, and subsequently migrated all admin tooling away from Retool within a few sprints, achieving cost and velocity gains. Low‑code vendors are responding by adding AI features, but it remains uncertain whether this will preserve market share. Build‑vs‑buy decisions now focus on speed, financial and maintenance costs, vendor lock‑in, and organizational complexity, with AI‑enabled in‑house development increasingly favored.

## Discussion Summary
Comments reflect a nuanced view of low‑code’s future. Many acknowledge its continued relevance for non‑technical users, citing visual guardrails, easier deployment, and reduced maintenance overhead. Others argue that AI‑driven agents will blur the line between low‑code and code generation, potentially diminishing the need for dedicated platforms while raising concerns about brittleness, token costs, and long‑term security. A common thread is that low‑code is expected to evolve rather than disappear, integrating with AI tools to improve productivity, yet its value will depend on how well it balances flexibility, stability, and operational simplicity.

---

## Full Article

The rise of AI and particularly agentic development presents an existential threat to an entire category of low-code platforms. While the adoption of new techniques and tooling will take years to propagate through the Byzantine ranks of larger, slower-moving enterprises, the fundamental ROI case for these tools looks different in a world where the cost of shipping code now approaches zero.

This may seem like a preposterous conclusion given the substantial size and growth of the sector. Forrester, who actually gave low-code its name back in 2014, [projects the category will reach $50b by 2028](https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/) and sees no current indication that things will slow down, let alone contract. However, it’s worth digging in to why these tools arose in the first place and the problems they solve to explore how much the landscape has shifted in just the past year.

![Forrester Low-Code Market Projection](https://www.zackliscio.com/_astro/forrester.opE9g3oO_6ECtA.webp)

Put simply, these software platforms exist to allow users to create software with fewer developer resources. By purchasing one of these platforms, a company can enable non-technical stakeholders to ship production-ready experiences, often with little to zero actual code being written. This frees up developer bandwidth, accelerates the company, and until recently was a no-brainer investment for building internal and even customer-facing software.

![The Low Code Value Prop](https://www.zackliscio.com/_astro/value-prop.Bs7qCFDc_iEAxj.webp)

To enable these platforms in the real world, developers spend considerable time on prerequisite and ongoing work: piping and transforming data, writing and maintaining custom components that go beyond out-of-the-box functionality, and meshing authentication systems, to name a few. This investment is in turn justified by the reduction in development scope and complexity downstream of the low-code platform—non-technical users can be left to their own devices to ship to their hearts’ content.

With the emergence of AI coding, this ROI case gets inverted. It is now often faster, cheaper, and easier to ship the kind of tools you might have built with low-code tools outside these platforms. Yes, this still requires developer time, but so did enabling these low-code-platforms in the first place. Even disregarding the financial and organizational costs of low-code tools, AI affords developers the conveniences of their regular workflows without the bolt-on complexity introduced by external platforms. When you add in the total cost of ownership of these low-code tools, a return to in-house tooling becomes even more attractive.

As an illustration of what’s possible, we’ve seen this play out in real-time at [Cloud Capital](https://www.cloudcapital.co). In the not-too-distant past, we relied heavily on a low-code platform called [Retool](https://retool.com) for almost all of our internal Admin tooling. We built management dashboards, reporting, and orchestrated complex workflows that were critical to the business. The acceleration was real—our developers spent significantly less time rolling boilerplate tables, transforming data, and wiring up workflows. We even celebrated at our All Hands how much *better* our dashboards felt than if we’d hand-rolled them or used a pre-canned admin interface.

Then came the agentic tools that completely transformed the way we develop software. For our low-code tooling, the shift began with a single choice to prototype some new, self-contained functionality as a standalone internal tool instead of via our low-code platform. It was faster, easier, and leveraged our actual codebase in ways an external solution could not. That meant we shipped something safer, more robust, and more maintainable. The cherry on top is that the end product was also better—the UI looked and felt more like our in-house products, without the clunkiness required to stay on the WYSIWYG rails.

It felt immediately clear that we had identified an unlock for our internal tooling velocity. All of a sudden, we found ourselves feeling constrained by the same low-code tools that until so recently were unblocking us. Changes that would have been one-liners in Cursor or automated triage tickets handled by an agent meant logging in to another platform, moving around clunky UX blocks, bashing against version management systems that weren’t quite as polished or integrated as our core development flows. All with the additional cost of maintaining this additional system.

What started as a single tool quickly became a wholesale migration of all of our Admin tooling, and the inevitable sunsetting of our Retool instance. They hadn’t changed, but our culture and way of working had, and low-code couldn’t keep up. What was most shocking was the timeline of this change—for us as a small, fast-moving startup, the transition including migration played out fully in just a couple of sprints.

It’s inevitable that incumbent low-code tools will adapt—they will need to in order to survive. In many cases, this shift is already visible in their marketing, such as Retool’s new AI-heavy positioning:

![Retool&#x27;s new AI-heavy positioning](https://www.zackliscio.com/_astro/retool-positioning.DetKXgRI_Z1PcLTl.webp)

At this point, it’s hard to say whether it’ll be enough. While it’s possible low-code platforms will survive by providing non-technical users with the kind of magical experience that’s already possible for developers with AI coding tools today, it also seems likely they will continue to cede market share to the core AI players themselves. We’re beginning to see this take shape as non-technical AI artifacts become more complex, powerful, and collaborative.

For us, abandoning low-code to reclaim ownership of our internal tooling was a simple build vs buy decision with meaningful cost savings and velocity gains. It also feels like a massive upgrade in developer experience and end-user quality of life. It’s been about 6 months since we made this switch, and so far we haven’t looked back.

Every build vs buy decision is unique, but many ultimately boil down to ROI in terms of speed, financial cost, maintenance cost, and organizational complexity. There are of course additional considerations like vendor lock-in, ownership of core competencies, ecosystem compatibility, etc., but in this case we can reduce the decision to this: will buying this platform let my team go faster, ship more, and create more value for our customers. At least for now, that answer feels clearer every day.