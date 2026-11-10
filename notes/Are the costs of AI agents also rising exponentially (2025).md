---
title: "Are the costs of AI agents also rising exponentially? (2025)"
url: https://www.tobyord.com/writing/hourly-costs-for-ai-agents
clipped: 2026-06-17 01:15:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Are the costs of AI agents also rising exponentially? (2025)](https://www.tobyord.com/writing/hourly-costs-for-ai-agents)

## Digest Summary
The post notes that AI models have expanded dramatically over seven years—parameter counts grew ~4,000× and token usage per task ~100,000×—suggesting that peak‑performance costs (measured by METR) may also be rising exponentially. If AI agents’ task‑completion speed improves by a factor of three each year while costs rise similarly, their cost per human‑hour would stay constant; a slower cost growth would make them cheaper relative to humans, but faster cost growth would erode competitiveness. The author defines “hourly cost” as the monetary expense of running an LLM to finish a task at its 50 % METR time horizon, divided by that horizon length. Few have examined this metric, and opinions vary: some expect total task cost to stay flat (implying declining hourly rates), others anticipate exponential cost growth. Attempts to infer costs from METR benchmark spend are problematic because benchmarks prioritize maximal performance, often over‑using compute. A recently released chart from METR offers limited insight into how LLM agents’ hourly costs have evolved.

## Discussion Summary
The comments highlight growing concern over the steep and rapidly increasing token and compute costs of frontier AI models, noting that hourly expenses can rise orders of magnitude for longer tasks and that failure rates remain significant. Participants reference personal experience and external measurements that suggest token consumption escalates as model capabilities expand, while smaller, cheaper models show performance gains. There is skepticism about the evidence but agreement that unsustainable pricing, hardware scarcity, and quadratic transformer scaling could drive future price hikes, with uncertainty about providers’ profitability.

---

## Full Article

As this trend shows no signs of stopping, people have naturally taken to extrapolating it out, to forecast when we might expect AI to be able to do tasks that take an engineer a full work-day; or week; or year.

But we are missing a key piece of information — the cost of performing this work.

Over those 7 years AI systems have grown exponentially. The size of the models (parameter count) has grown by 4,000x and the number of times they are run in each task (tokens generated) has grown by about 100,000x. AI researchers have also found massive efficiencies, but it is eminently plausible that the cost for the peak performance measured by METR has been growing — and growing exponentially.

This might not be so bad. For example, if the best AI agents are able to complete tasks that are 3x longer each year and the costs to do so are also increasing by 3x each year, then the cost to have an AI agent perform tasks would remain the same multiple of what it costs a human to do those tasks. Or if the costs have a longer doubling time than the time-horizons, then the AI-systems would be getting cheaper compared with humans.

But what if the costs are growing more quickly than the time horizons? In that case, these cutting-edge AI systems would be getting less cost-competitive with humans over time. If so, the METR time-horizon trend could be misleading. It would be showing how the state of the art is improving, but part of this progress would be due to more and more lavish expenditure on compute so it would be diverging from what is economical. It would be becoming more like the Formula 1 of AI performance — showing what is possible, but not what is practical.

So in my view, a key question we need to ask is:

***How is the ‘hourly’ cost of AI agents changing over time?***

By ‘hourly’ cost I mean the financial cost of using an LLM to complete a task right at the model’s 50% time horizon divided by the length of that time horizon. So as with the METR time horizons themselves, the durations are measured not by how long it takes the model, but how long it typically takes humans to do that task. For example, Claude 4.1 Opus’s 50% time horizon is 2 hours: it can succeed in 50% of tasks that take human software engineers 2 hours. So we can look at how much it costs for it to perform such a task and divide by 2, to find its hourly rate for this work.

I’ve found that very few people are asking this question. And when I ask people what they think is happening to these costs over time, their opinions vary wildly. Some assume the total cost of a task is staying the same, even as the task length increases exponentially. That would imply an exponentially declining hourly rate. Others assume the total cost is also growing exponentially — after all, we’ve seen dramatic increases in the costs to access cutting-edge models. And most people (myself included) had little idea of how much it currently costs for AI agents to do an hour’s software engineering work. Are we talking cents? Dollars? Hundreds of dollars? An AI agent can’t cost more per hour than a human to complete these tasks can it? Can it?

⁂

A couple of months ago I asked METR if they could share the cost data for their benchmarking. I figured it would be easy — just take the cost of running their benchmark for each model, plot it against release date and see how it is growing. Or plot the cost of each model vs its time horizon and see the relationship.

But they helpfully pointed out that it isn’t so easy at all. Their headline time-horizon numbers are meant to show the best possible performance that can be attained with a model (regardless of cost). So they run their models inside an agent scaffold until the performance has plateaued. Since they really want to make sure it has plateaued, they use a *lot* of compute on this and don’t worry too much about whether they’ve used too much. After all, if you are just trying to find the eventual *height* of a plateau, there is no problem in going far into the flat part of the graph.

But if you are trying to find out when the plateau *begins*, there is a problem with this strategy. Their total spend for each model is sometimes just enough to get onto the plateau and sometimes many times more than is needed. So total spend can’t be used as direct estimate of the costs of achieving that performance.

Fortunately, they released a chart that can be used to shed some light on the key question of how hourly costs of LLM agents are changing over time: