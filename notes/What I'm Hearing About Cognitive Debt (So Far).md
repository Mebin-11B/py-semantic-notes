---
title: "What I'm Hearing About Cognitive Debt (So Far)"
url: https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/
clipped: 2026-06-17 01:07:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What I'm Hearing About Cognitive Debt (So Far)](https://margaretstorey.com/blog/2026/02/18/cognitive-debt-revisited/)

## Digest Summary
The article defines “cognitive debt” as the gap between a system’s evolving architecture and a team’s shared mental model of its purpose and changeability, a gap amplified by generative and agentic AI. Practitioners report that rapid development speed erodes understanding, leading to loss of confidence, heavier review loads, debugging friction, slower onboarding, and developer fatigue. Unlike technical debt, which resides in code, cognitive debt lives in people, documentation, tests, conversations, tooling, and increasingly AI agents, requiring active repayment by restoring distributed knowledge of intent, rationale, constraints, and architectural intent. While disciplined engineering practices (specifications, reviews, tests) can mitigate the issue, AI lowers the cost of structural change, outpacing the ability to keep shared understanding current. Mitigation strategies emerging include stricter reviews, intent‑capturing tests, continuously updated design docs, disposable prototypes, and leveraging AI for cognitive tracking and explanation. The open challenge is how high‑performing teams will adapt socio‑technical practices and AI tools to externalize intent and sustain collective theory, preventing cognitive debt from becoming the primary performance bottleneck.

## Discussion Summary
Comments express mixed views on “cognitive debt” and AI‑assisted development. Many regard the term as overly broad or buzz‑wordy, arguing that lack of documentation, onboarding, and architectural clarity are standard workflow issues rather than a distinct concept. Opinions converge that AI can accelerate routine tasks, testing, and small scripts, but reliance on it for core code risks hidden complexity and longer‑term technical debt, especially in larger teams. Concerns also surface about managerial pressure, job security, and burnout, while some see AI as a useful, limited productivity boost when paired with solid standards and clear handoff protocols.

---

## Full Article

read

A week ago, I wrote about how Generative and Agentic AI may be amplifying what I’ve been calling [cognitive debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/): the accumulated gap between a system’s evolving structure and a team’s shared understanding of how and why that system works and can be changed over time.

The post sparked thoughtful discussion across different communities. Rather than respond thread by thread, I want to synthesize what I’m hearing and connect it to other reflections I’ve been reading. I will likely update this as the conversation evolves.

### A Growing Concern About Shared Understanding

Several practitioners, including [Simon Willison](https://simonwillison.net/2026/Feb/15/cognitive-debt/) and others on a [Hacker News discussion of a Martin Fowler article](https://news.ycombinator.com/item?id=47005856), describe experiencing cognitive debt directly. They talk about getting lost in their own projects and finding it harder to confidently add new features. They can move faster, but they lose the deeper sensemaking that connects decisions to intent, and intent to code.

This is not just about code quality. It is about whether individual developers and product teams can maintain a coherent mental model of what the system is doing and why.

Across these discussions, one theme is consistent: velocity can outpace understanding.

### Cognitive Debt Hurts Developers, Not Just the Software

Technical debt lives in the code.  
Cognitive debt lives in people.

When shared understanding erodes, the pain shows up in:

* Loss of confidence when making changes
* Heavier review burden
* Debugging friction
* Slower onboarding
* Stress and fatigue

The software may be “working”, but the theory of the system becomes harder to access and keep track of. The cost is not only structural. It is experiential.

Siddhant Khare has written about [AI fatigue](https://siddhantkhare.com/writing/ai-fatigue-is-real). Steve Yegge reflects on [burnout emerging from AI-accelerated development](https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163). Annie Vella eloquently writes about the [emotional and cognitive experience of uncertainty](https://annievella.com/posts/finding-comfort-in-the-uncertainty/) when systems become harder to reason about. These perspectives reinforce that this is not just an engineering discipline issue, but one that affects how developers feel and function.

### Cognitive Debt, Like Technical Debt, Must Be Repaid

Martin Fowler notes that, like technical debt, [cognitive debt must eventually be repaid](https://martinfowler.com/fragments/2026-02-13.html). I agree.

But rebuilding lost knowledge requires restoring the distributed theory of the system. That includes capturing intent, the rationale behind decisions, key constraints, and how the architecture supports change.

That theory is not stored in code alone. It is distributed across:

* People
* Documentation
* Tests
* Conversations
* Tooling
* And increasingly, AI agents

Repayment means maintaining all of these, not just refactoring code or updating architecture documents.

Under pressure to move quickly, whether in startups racing to learn or in large organizations pushing AI adoption, that repayment can feel expensive and easy to defer.

### “This Is Just Engineering”, But Incentives Are Changing

Several commenters, including Michael Würsch, argue that [cognitive debt reflects a failure of good engineering discipline](https://www.linkedin.com/pulse/ai-doesnt-replace-engineering-discipline-rewards-michael-w%C3%BCrsch-vxa6e/?trackingId=oeXISV30PWkxmfwhACjUug%3D%3D). Clear specifications, rigorous reviews, extensive testing, and explicit architecture documentation should prevent knowledge loss.

In principle, I agree. But in practice, the incentives are shifting. AI lowers the cost of producing structure. It becomes easier for structure to evolve faster than shared understanding can stabilize. Even disciplined teams must consciously throttle or shape their practices to keep understanding aligned with change.

Specifications and documents are not sufficient if they are not living artifacts that teams actively engage with.

### Emerging Mitigation Strategies

Encouragingly, many readers shared how they are mitigating cognitive debt.

They describe:

* More rigorous review practices
* Writing tests that capture intent
* Updating design documents continuously
* Treating prototypes as disposable

Some also describe using [AI to reduce the cost of these practices](https://www.linkedin.com/pulse/ai-doesnt-replace-engineering-discipline-rewards-michael-w%C3%BCrsch-vxa6e/?trackingId=oeXISV30PWkxmfwhACjUug%3D%3D), and even to support cognitive tracking, dependency management, and explanation.

Used deliberately, AI may help make cognitive work more visible rather than obscuring it.

### The Open Question: How Will High-Performing Teams Adapt?

High-performing teams have always managed technical debt intentionally. As AI is adopted by startups and large companies, the question becomes how teams will manage cognitive debt.

How will they shape socio-technical practices and tools to externalize intent and sustain shared understanding? How will they use Generative and Agentic AI not only to accelerate code production, but to maintain their collective theory?

As AI reduces technical friction, shared understanding may become the bottleneck on performance.

I am continuing to watch how this evolves. If you are seeing mitigation practices that work in real teams, I would love to learn from them.