---
title: "xAI is looking more like a datacentre REIT than a frontier lab"
url: https://martinalderson.com/posts/xais-new-rental-business/
clipped: 2026-06-17 00:50:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - gpu leasing
  - xai
  - datacenter reit
  - ai compute infrastructure
related:
  - "[[GPU Leasing]]"
  - "[[xAI]]"
  - "[[AI Compute Infrastructure]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An analysis of xAI's shift towards compute leasing, renting its Colossus 1 datacenter capacity to rivals like Anthropic and Google.
>
> **Key points:**
> - xAI has signed compute-leasing agreements with Anthropic ($1.25B/month) and Google ($920M/month) for older Colossus 1 infrastructure.
> - The deal functions as a rental model to offset high capital costs, making xAI look like a Real Estate Investment Trust (REIT) for datacenters.
> - This business model allows xAI to recoup its $40B datacenter investment quickly while competing labs secure immediate GPU scaling.
>
> **Concept links:** [[GPU Leasing]], [[xAI]], [[Datacenter REIT]], [[AI Compute Infrastructure]]
>
> **Suggested connections:**
> - [[Compute Scarcity]] — the market dynamics of GPU supply and demand among top AI labs.
> - [[AI Lab Economics]] — financial models and capital expenditures of frontier AI organizations.
<!-- ai-summary:end -->

# [xAI is looking more like a datacentre REIT than a frontier lab](https://martinalderson.com/posts/xais-new-rental-business/)

## Digest Summary
- xAI, now a SpaceX subsidiary, has signed large‑scale compute‑leasing agreements with Anthropic and Google, using its older “Colossus 1” datacenter in Memphis.  
- Anthropic pays up to $1.25 billion / month for 300 MW (≈220 k GPUs) to lift peak‑hour usage caps; Google pays about $920 million / month for 110 k GPUs. Both contracts allow 90‑day cancellation after an initial lock‑in.  
- At the projected rates, xAI would recoup the estimated $40 billion construction cost of the facility in roughly 18 months, even before accounting for operating expenses and depreciation.  
- The deals address a persistent global GPU shortage, giving Anthropic immediate capacity relief and providing xAI with a high‑margin revenue stream.  
- Potential conflicts of interest are noted: Elon Musk’s legal dispute with OpenAI and Google’s stake in SpaceX may influence the arrangements.  
- Leasing capacity reduces the compute available for xAI’s own Grok model, suggesting a shift from frontier‑lab ambitions toward a datacenter‑REIT business model.  
- The rapid build time (Colossus 1 constructed in 122 days) highlights SpaceX/xAI’s execution advantage over traditional hyperscalers.

## Discussion Summary
The comments collectively view SpaceX’s AI and datacenter activities with skepticism, emphasizing concerns about a large Google stake creating potential conflicts, the legality and environmental impact of rapidly built facilities, and the profitability and durability of xAI’s compute‑rental model. While a minority note Elon Musk’s hardware expertise and possible strategic benefits from orbital infrastructure, the prevailing sentiment questions the speculative valuation, long‑term relevance of the technology, and managerial execution.

---

## Full Article

An unexpected development over the past few weeks is xAI's new partnerships with Anthropic and Google, providing them with a huge amount of capacity. It's worth remembering that xAI is now part of SpaceX, after the two merged back in February - so the revenue from these deals flows straight into the entity about to go public. While much has been made of the potential financial engineering given SpaceX's upcoming IPO, I think there's a bit more to this than just pure accounting tricks.

Anthropic was in a serious bind
-------------------------------

If you use Claude products much, you'll be (very, probably) aware that Anthropic has had serious capacity problems, especially early afternoon onwards in Europe and in the mornings in the US (this is when demand *seems* to be highest as both European users and the Americas are both at work, fighting for capacity). I've written about this compute crunch before a few times - [the coming crunch](https://martinalderson.com/posts/the-coming-ai-compute-crunch/), [whether it's here yet](https://martinalderson.com/posts/is-the-ai-compute-crunch-here/), and [what comes next](https://martinalderson.com/posts/what-next-for-the-compute-crunch/).

This resulted in Anthropic having to introduce new [peak hour restrictions](https://x.com/trq212/status/2037254607001559305) on their subscriptions, with usage between 5am–11am PT / 1pm–7pm GMT using more of your usage limit - with the aim of smoothing demand between peak hours and off peak hours where they had more capacity available.

However, there is only so much demand shifting you can do when demand is growing as fast as Anthropic's. At some point you end up having to ration users further, which definitely is far from ideal when you have both Google and OpenAI breathing down your neck for customers.

xAI to the rescue?
------------------

At the start of May, xAI announced a [partnership](https://x.ai/news/anthropic-compute-partnership) with Anthropic to provide access to their (older) Colossus 1 datacentre in Memphis. This allowed Anthropic to reverse the usage limit restrictions on their subscriptions, and in general while stability of Anthropic services still leaves a *lot* to be desired, the peak time crunch has abated (for now, at least).

The fees involved are enormous, ramping to $1.25bn/month for 300MW of capacity - approximately 220k GPUs.

Last week, Google announced a similar partnership - $920mn/month for 110k GPUs. It's important to note that both agreements have cancellation clauses - allowing either party to cancel with 90 days' notice after an initial lock-in period.

If you take this on face value, this is a ludicrously profitable deal for xAI:

![Chart showing xAI's cumulative lease revenue from Anthropic and Google crossing the ~$40bn build cost at around 18 months](https://martinalderson.com/img/xai-datacentre-rental-payback.png)

While this doesn't include opex and depreciation, *if* the deals continue for 18 months, xAI recoups all the capex they spent *and* still has many hundreds of MW of GPUs available. With the giant compute shortages likely to persist into the medium term, even older H100s are likely to be extremely useful even 18 months out.

The case against
----------------

It's important to note there are certainly some red flags with the deal. Firstly, Elon Musk and OpenAI were/are locked in a bitter legal battle, and the Anthropic deal could be motivated to add pressure to OpenAI more than commercial reality.

And Google is a major shareholder in SpaceX, so they certainly have incentive to juice the valuation of the IPO.

While I'm sure there is some degree (potentially a lot!) of truth in these viewpoints, it's important to note that huge volumes of GPUs are in *enormously* short supply.

One of the untold stories of this capex boom in datacentres is just how *behind* all of them are. Even OpenAI's flagship Stargate UAE datacentre - being built in a jurisdiction that is renowned for a laissez-faire attitude to building regulations - is now under direct threat from the current Iran conflict, with Iranian drones having [already hit other UAE datacentres](https://www.cnbc.com/2026/03/03/iran-war-uae-drone-strikes-aws-data-centers.html).

In comparison, SpaceX/xAI are *incredible* at building datacentres on time. The original Colossus 1 datacentre was built in 122 days. Musk's empire does have a huge advantage in really understanding how to plan, build and execute enormous infrastructure projects quickly. While the hyperscalers no doubt have the experience to do this, they were built with far less urgency - with typical project execution taking many years. Given the capex only really started to ramp up in the last couple of years, many of these projects are still years away.

This gives xAI a serious competitive advantage that shouldn't in my opinion just be hand waved away.

But what about Grok?
--------------------

There is no doubt this leaves Grok in an odd spot, with a lot of the datacentre capacity that was destined for Grok training and inference now being leased to a *direct* competitor.

While it's foolish to write off any model provider, it certainly looks like a serious retreat from Grok vying to be a frontier class lab. But, perhaps, they over-specified their datacentre capacity - there is no doubt that inference *demand* for Grok models is likely to be seriously behind projections, leaving a bunch of spare capacity which might as well be monetised while the training lottery continues? It's hard to say and the xAI & Cursor deal muddies the water even further.

As such, I think *all three* things are true to some degree. There's no doubt some level of financial engineering going on. There's also an enormous compute shortage. And it seems to me SpaceX/xAI *does* have a real competitive advantage in datacentre buildout.

It's just the magnitude of how true each of these are is going to define the success or failure of the biggest IPO in North American history.

Either way, the more I look at it, the more xAI is starting to resemble a datacentre REIT with a frontier lab attached, rather than the other way around.