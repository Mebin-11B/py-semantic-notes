---
title: "Microsoft reports AI is more expensive than paying human employees"
url: https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/
clipped: 2026-06-17 00:58:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Microsoft reports AI is more expensive than paying human employees](https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

## Digest Summary
Microsoft has begun scaling back internal AI use after cost overruns. It is canceling most Claude Code licenses for engineers, directing them to GitHub Copilot CLI, while maintaining its larger Anthropic “Foundry” partnership and Azure compute commitments. Uber’s CTO reported that its 2026 AI‑coding‑tools budget was exhausted in four months, despite internal leaderboards incentivizing heavy tool usage. Similar pressures exist at Meta and Amazon, where employees are urged to maximize token consumption. Analyst forecasts predict a 24‑fold rise in token usage by 2030, reaching ~120 quadrillion tokens per month; although token prices are expected to drop 90 % by that time, overall enterprise AI costs may rise because agentic models consume many more tokens per task and savings are not fully passed on. Executives such as Nvidia’s Jensen Huang envision dozens of AI agents per employee, but the disparity between falling unit costs and accelerating consumption could make the AI “agentic” future substantially more expensive than anticipated.

## Discussion Summary
The comments express skepticism toward the article’s framing, calling the title misleading and arguing that token‑based metrics artificially inflate perceived costs. They contend that inference remains affordable and that human engineers will still be required, disputing claims that combining humans with large language models is cheaper than hiring additional staff. The critique notes a lack of Microsoft data supporting higher AI expenses, dismisses reports of license cancellations as hearsay, and suggests using open‑source models such as DeepSeek or developing a self‑hosted, efficient stack.

---

## Full Article

Firms today are pushing employees to use as much AI as possible to squeeze out the technology’s productivity gains. But that pressure is leading to cracks, and those cracks may be irreparable.

[Microsoft](https://fortune.com/company/microsoft/) has reportedly begun canceling most of its direct Claude Code licenses, according to [*The Verge*](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad), instead moving engineers toward using GitHub Copilot CLI. That comes just six months after the firm first opened up access to Claude Code, encouraging thousands of its developers, project managers, designers, and other employees to experiment with coding. The tech became popular fast. Perhaps too popular. The scale at which employees use it is now prompting the firm to reverse course on a tool its own engineers had come to rely on. Canceling Claude Code licenses won’t affect Microsoft’s Foundry deal, which includes investing up to $5 billion in Anthropic and giving Foundry customers access to Claude models, as well as Anthropic’s $30 billion commitment to purchase Azure compute capacity, according to *The Verge*.

Microsoft isn’t the only company scaling back its internal AI use. Uber’s CTO Praveen Neppalli Naga told [*The Information*](https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets) in April that the firm had already burnt through its entire 2026 AI coding tools budget in just four months. That comes after the company had actively incentivized adoption through internal leaderboards ranking teams by AI tool usage.

The reports may throw cold water on the bets tech’s biggest firms have placed on the technology. While some cling to the promise of an AI “renaissance” or “revolution,” the cost of adoption is proving a stubborn bottleneck. These developments also suggest that the economics of replacing or augmenting human labor with AI may be more complicated than some early forecasts originally implied. That echoes what [Bryan Catanzaro](https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/), vice president of applied deep learning at [Nvidia](https://fortune.com/company/nvidia/), recently said in an interview with Axios.

“For my team, the cost of compute is far beyond the costs of the employees,” he said.

Anthropic didn’t immediately respond to *Fortune*’s request for comment. Microsoft didn’t provide a comment.

**An emerging AI paradox: cheaper tokens, bigger bills**
--------------------------------------------------------

Uber and Microsoft aren’t the only firms pushing employees to use as much AI as possible. Like at Uber, a [Meta](https://fortune.com/company/facebook/) employee crafted a leaderboard, fittingly named “[Claudeonomics](https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/),” after Anthropic’s AI model, to track which workers are using the most AI. [Amazon](https://fortune.com/company/amazon-com/) is pushing its employees to “[toxenmaxx](https://fortune.com/2026/05/12/amazon-tokenmaxxing-claude-ai-capex-meta-gil-luria/),” or use as many AI tokens as possible (the basic building blocks of AI compute).

But with a token-based pricing system, the work gets more expensive with more use and better efficiency. Goldman Sachs recently forecasted that agentic AI could drive a 24-fold increase in token consumption by 2030 as consumers and enterprises adopt AI agents, reaching a staggering 120 quadrillion tokens per month. As businesses turn to AI agents to boost productivity, aggregate costs could rise sharply even if the price of each token falls.

But as consumption increases, the cost of individual AI tokens is expected to fall sharply. A recent report from research firm [Gartner](https://fortune.com/company/gartner/) found that by 2030, inference on a one-trillion-parameter LLM—in simple terms, a highly sophisticated AI model—will cost AI firms nearly 90% less than it did in 2025. Even so, Gartner predicted that cheaper tokens won’t translate to cheaper enterprise AI because agentic models require far more tokens per task than standard models, increased consumption can outpace falling unit costs, and AI providers won’t fully pass through lower costs to consumers. In turn, inference costs are likely to push higher.

“Chief Product Officers (CPOs) should not confuse the deflation of commodity tokens with the democratization of frontier reasoning,” Gartner senior director analyst Will Sommer warned in a statement.

That reality may complicate the grand plans some firms have for deploying AI agents. Nvidia CEO Jensen Huang recently said he thinks [100 AI agents will one day work](https://fortune.com/2026/03/19/jensen-huang-nvidia-ai-agents-future-of-work-autonomous/) alongside every employee at his company.

Huang is part of a broader wave of CEOs touting an agentic future in which digital workers operate across the enterprise. But if token consumption rises faster than unit costs fall, that future could come with a much heavier bill than executives expect.