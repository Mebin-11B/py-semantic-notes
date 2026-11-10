---
title: "Uber's $1,500/month AI limit is a useful signal for AI tool pricing"
url: https://simonwillison.net/2026/Jun/3/uber-caps-usage/
clipped: 2026-06-17 00:53:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)

## Digest Summary
Uber has instituted a $1,500 monthly cap on token spending for each AI coding tool used by employees, covering agentic software such as Cursor and Anthropic’s Claude Code. The limits are independent per tool, so usage of one does not affect the budget for another. According to Bloomberg, the policy was introduced to curb excessive spending after Uber’s 2026 AI budget was exhausted within four months. Assuming two tools per engineer, the cap translates to $36,000 annually per employee, roughly 11 % of the median $330,000 compensation for Uber software engineers in the United States. By contrast, the author’s personal usage averages $1,000 per month per provider, costing $100 due to subsidized individual plans unavailable to large firms like Uber. The caps represent Uber’s effort to align AI costs with employee compensation.

## Discussion Summary
Comments show mixed attitudes toward AI token pricing and usage limits. Many note that current subsidized rates mask higher future costs and question whether competition, especially from Chinese open‑weight models, will drive prices down. Users report wide variance in spend, with some burning thousands of dollars while others stay well below caps, leading to concerns about ROI and the practicality of large models versus cheaper “flash” alternatives. Lock‑in risk, unclear productivity gains, and the effectiveness of spending caps are repeatedly debated, reflecting overall skepticism tempered by occasional acceptance of limited budgeting as a pragmatic measure.

---

## Full Article

3rd June 2026 - Link Blog

**[Uber Caps Usage of AI Tools Like Claude Code to Manage Costs](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs)**. I wrote [the other day](https://simonwillison.net/2026/May/27/product-market-fit/#the-ai-failure-stories-around-this-are-pretty-thin) about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, before anyone could have predicted how popular token-burning coding agents were about to become.
Natalie Lung for Bloomberg:

> The rideshare giant is limiting all employees to $1,500 in monthly token spending per AI coding tool, an Uber spokesperson said in response to a Bloomberg News inquiry. That means spending on one tool doesn’t have a bearing on the budget for another. The limits, which have been instituted in recent months, only apply to agentic coding software such as Cursor or Anthropic PBC’s Claude Code.

A $1,500 monthly limit per tool strikes me as a rational policy response to over-spending, and *much* more sensible than those [tokenmaxxing](https://en.wikipedia.org/wiki/Token_maxxing) leaderboards encouraging employees to compete for as much AI usage as possible.

It's also interesting in that it hints at a real dollar value for what Uber is getting out of these tools. If we assume two actively used tools per engineer that's $3,000 \* 12 = $36,000 cap per engineer per year. Levels.fyi lists [the median yearly compensation package for Uber software engineers in the USA](https://www.levels.fyi/companies/uber/salaries/software-engineer?country=254) at $330,000.

That means each employee's AI spending cap is ~11% of that median compensation package.

I [noted](https://simonwillison.net/2026/May/27/product-market-fit/#enterprise-customers-are-now-paying-api-prices) that my own token usage comes to about $1,000/month against each of Anthropic and OpenAI - which currently costs me just $100 per provider thanks to their generous subsidized plans for individual subscribers. Those plans are no longer available to larger companies like Uber.

Their new policy means if I were working at Uber I'd still have ~$500/month of tokens to spare for each of those tools, given my current usage patterns.