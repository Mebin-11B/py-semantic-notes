---
title: "Data is the only moat"
url: https://frontierai.substack.com/p/data-is-your-only-moat
clipped: 2026-06-17 01:58:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Business Moat
  - AI Startups
  - Product Adoption
  - Data Flywheel
  - Systems Integration
  - Startup Strategy
related:
  - "[[Domain expertise has always been the real moat]]"
  - "[[Learn Claude Code by doing, not reading]]"
  - "[[CLI agents make self-hosting on a home server easier and fun]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article outlines a 2x2 matrix analyzing AI startup defensibility, arguing that user adoption feedback loops and custom enterprise data integrations form the only true moats.
>
> **Key points:**
> - AI application space is divided into a 2x2 matrix of technical complexity (Easy vs. Hard to Solve) and friction (Easy vs. Hard to Adopt).
> - "Easy to Solve, Easy to Adopt" is a value trap where model providers (Google, OpenAI) will crush startups by leveraging massive consumer data.
> - "Hard to Solve, Easy to Adopt" (like coding agents) succeeds by creating a rapid feedback loop ("data flywheel") to train specialized models.
> - "Easy to Solve, Hard to Adopt" (like enterprise customer support) is defensible due to the high integration friction of legacy enterprise systems.
> - The next growth phase lies in "Hard to Solve, Hard to Adopt" tasks (like SRE and security ops), which will become viable as reasoning models improve.
>
> **Concept links:** [[Business Moat]], [[AI Startups]], [[Product Adoption]], [[Data Flywheel]], [[Systems Integration]], [[Startup Strategy]]
>
> **Suggested connections:**
> - [[Domain expertise has always been the real moat]] — Directly related contrast piece arguing that domain knowledge, not data, is the true business moat in the AI era.
> - [[Learn Claude Code by doing, not reading]] — Practical application of developer/coding agents mentioned in the article.
> - [[CLI agents make self-hosting on a home server easier and fun]] — AI adoption and self-hosted tools.
<!-- ai-summary:end -->

# [Data is the only moat](https://frontierai.substack.com/p/data-is-your-only-moat)

## Digest Summary
None

## Discussion Summary
Comments emphasize that competitive advantage stems from a mix of factors—vertical and horizontal integration, brand reputation, visible storytelling, design simplicity, network effects, regulatory positioning, and execution speed—rather than data alone. Attention is highlighted as the primary moat, with data serving mainly to capture that attention. Opinions are split between optimism about LLM progress and calls for critical evaluation of their limitations. Concerns about aggressive tactics, data ownership, and the need for regulation appear alongside recognition that algorithmic breakthroughs and user‑centric design can foster strong loyalty.

---

## Full Article

Theoretically, we should have a stellar AI agent for every problem in our lives by now. The talent is there, the capital is certainly there, and the models are increasingly capable. And yet, the results are lopsided. Why is it that we have agents that can prospect for sales leads and answer support tickets accurately, but we don’t seem to be able to consistently generate high quality slides?

The simplest explanation might be complexity. Easier problems (e.g., answer a support question) naturally get solved first, and more open-ended problems like slide generation require more effort. That doesn’t quite hold up: Coding is obviously not a simple application area, and yet coding agents are some of the best that we have today – in fact, they are improving faster than any other single agent use case.

How did this happen? Ease of adoption enabled data collection at scale that in turn helped coding agents improve rapidly.Every developer could switch to Cursor in 5 minutes without any approval. That created a data flywheel (more on this below) that allowed the Cursor team to build a better application experience over time – to the point where our whole team now swears by Cursor’s [Composer model](https://cursor.com/blog/composer) for code generation.

The combination of technical complexity and adoption difficulty creates an interesting 2x2:

You might be tempted to think that being in one of the “easy to adopt” quadrants is the holy grail – after all, who doesn’t want more data to build better models? That is certainly a valid way to build a business, but the trap is that easy to adopt *also* means easy to displace. Hard to adopt products have their own data moat: Once you’re embedded in an enterprise, you learn about how *that company* works in a way that makes your product incredibly hard to replace.

Whichever quadrant you fall into, data is your only moat.

Easy to adopt and easy to solve is the most obvious quadrant to work in. It didn’t take an incredible amount of foresight to see back in 2023 that consumer search on Google would be replaced by custom answers to every question that a user has – whether it was finding a nice fact or providing healthcare advice. This has been the bread-and-butter use case for the foundation model providers and plenty of new entrants (e.g., Perplexity, [You.com](http://you.com)) flocked to these use cases as well.

The “easy to solve, easy to adopt” quadrant is a **value trap**. If the barrier to entry is low for you, it’s non-existent for frontier labs (or more likely, they’ve already built it). Given that these are the “obvious” use cases, they’re the ones for which the existing chat applications will see the highest volume of usage. That means that – whatever the use case is – OpenAI, Google, and Anthropic are gathering millions of data points to improve their models in these areas. Last week’s release of [ChatGPT Health](https://openai.com/index/introducing-chatgpt-health/) feels like an obvious step in this direction. Beyond data access, the model providers can also subsidize costs and leverage their massive user bases to learn any new application area quite quickly. In short, you very likely will get crushed by the model providers.

An interesting side note is that loyalty is quite low in this quadrant – we all [use multiple chat agents](https://www.interconnects.ai/p/use-multiple-models) depending on the use case, and unlike with the web search market, everyone seems to be on relatively equal footing. If dominant brand leaders do emerge, we’d place our bets on the model providers.

Why did coding – ostensibly one of the hardest problems to solve! – see such rapid progress? Most importantly, it is because adoption was easy – you could see a ton of value by pasting a snippet of code into ChatGPT back in 2023, and Cursor quickly made that much easier even though quality was limited early on. Since every engineer typically has the freedom to choose their own IDE, switching from IntellIJ or VSCode to Cursor wasn’t a crazy lift. Once it was in place, it also had a very fast feedback loop – a software engineer might generate code with Cursor tens or hundreds of times a day. That created a data flywheel: Every accepted or rejected suggestion adds to training data for future model improvements. With this data in hand, it was inevitable that model quality would improve dramatically over time. Notably, other markets in this quadrant (e.g., slide generation) that don’t have the same fine-grained feedback loop have seen much slower improvements.

Anything in the “hard to solve” category is going to require significant investment – across token usage, technical talent, and likely eventually model training and RL. The ease of adoption is a powerful data acquisition flywheel that enables that deeper investment. The frontier model labs seem to view these kinds of widely used productivity agents as being in their domain. They’re already competing heavily on coding agents, and we would not be surprised to see them launch more office-suite productivity tools beyond the document editors they already have. In other words, our prediction is that these markets are going to have heavyweight fights – smaller players will struggle to compete without huge capital outlays.

Stickiness, however, continues to be low here. Many of us run multiple coding agents, and as office productivity tools improve, there’s no reason that you wouldn’t jump to whichever app makes you the prettiest slides. The argument for stickiness is company-specific customization (e.g., Cursor rules, brand templates), but it’s possible we will see interoperability or a single standard emerge to enable migration.

This is the area where enterprise adoption of AI has really taken off in the last two years. When we say easy to solve, we’re not implying that there’s no product depth, but it’s easy to imagine how an LLM can execute a playbook for an e-commerce return or a password reset. Given that most enterprises are looking for wins from AI, the “obvious” problems are where they’ve turned for immediate adoption. That’s enabled an incredible pace of revenue growth for the leaders in these markets.

Two key things differentiate this quadrant. First, these products are not individually adoptable – buying an agent to handle support tickets or IT helpdesk requests is an organization-level decision that likely has a buying committee. Second, the comparative simplicity of the use case is offset by the difficult and tedious reality of enterprise integrations. The teams that can navigate legacy enterprise systems have a huge leg up.

That integration story is where there’s a data moat. While the data you get from these agents is less broadly applicable – and enterprises will likely restrict your ability to train models with it – you’re gathering data about how *each customer* works. Over time, that will help you make your product at large better, but most importantly, your product will become stickier for each customer. The next agent that comes along will have a hard time recreating that learned expertise.

In this area, investors are treating the larger startups as *de facto* incumbents. That’s not to say that there isn’t product innovation left to be done – there very likely is! – but it’s not immediately obvious why a smaller startup would be able to compete with the likes of Sierra and Decagon, for example. What’s less clear is whether the capital these companies are raising is primarily being used to drive GTM or whether there is a clear technical moat that’s emerging, à la coding-specific models. If it’s only the former, then startups might have to resort to competing on cost.

*Example apps: SRE, security ops*

Hard to adopt, hard to solve problems have received (comparatively) the least attention out of all four quadrants. The potential value of solving complex engineering or operations workflows can be incredibly high, as these are tasks that typically take humans hours or days. Unfortunately, these are workflows that are also fairly custom on a company-by-company basis, which means evaluation and implementation are much more cumbersome than “easy to solve, hard to adopt” products.

We’ve placed [our bet](https://www.runllm.com/product) in the hard-hard quadrant, and this is where we expect to see the next phase of growth. The hard-hard markets will grow very quickly in the next couple years for a handful of reasons. First, reasoning models are now capable of planning to handle more complex tasks, which will help grapple with multi-step solutions. Second, a lot of the complexity in solving these problems comes from the steps outside of AI – building and configuring workflows; that will get easier and faster as coding agents get better. Finally, enterprises are already actively plucking the low-hanging fruit and will look to harder problems once those run out.

The data moat here is the most complex and potentially the most valuable. If you build expertise in one company’s workflows, that becomes very difficult to replicate – switching products would be akin to firing an experienced engineer and replacing them with a new person. There’s potentially an opportunity to build expertise in core capabilities (e.g., an SRE agent that’s an expert in AWS). However, this improvement cycle will be significantly slower than it was with coding agents because the quantity of data is lower and verifiability is less obvious.

While every one of these markets has a company that has raised astronomical amounts of money (often well ahead of revenue growth), we have a hard time imagining that these companies are as entrenched as their equivalents in the “easy to solve, hard to adopt” category. There’s a very long game left to be played in this market.

This map isn’t set in stone; both boundaries will change. On the complexity front, we’ve seen dramatic improvements in model capabilities every few months. However, model improvements [seem to be plateauing](https://frontierai.substack.com/p/model-inference-model-products-and?utm_source=publication-search), so there’s less interest on this axis.

The real excitement is around UX. We’ve long believed that the UX aspects of AI applications are underexplored. We would not be surprised to see new UX paradigms developed that change the way users adopt products. [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) is probably the best recent example of this – by making a coding agent available in a web browser available to everyone, it’s allowed users who might be scared away by an IDE or terminal to access these tools.

Regardless of what path they take, our bet is that the next 12-24 months will see the rise of winners in the hard-hard quadrant. It won’t look as seamless as the growth of Sierra and Decagon has been – there will be longer evaluation cycles, more complex implementations, and likely an overall lower success rate. But as companies improve their process and data enables improved models, this is where incredible amounts of revenue can be generated.