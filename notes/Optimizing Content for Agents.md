---
title: "Optimizing Content for Agents"
url: https://cra.mr/optimizing-content-for-agents/
clipped: 2026-06-17 01:33:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - ai agents
  - web optimization
  - markdown endpoints
  - information retrieval
related:
  - "[[AI Agents]]"
  - "[[Web Optimization]]"
  - "[[Markdown Endpoints]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Strategies for web content creators to optimize sites for AI agents, including markdown content negotiation and layout simplification.
>
> **Key points:**
> - Web optimization for AI agents targets token budget limits and agentic parsing constraints.
> - Key techniques include markdown endpoints (via `Accept: text/markdown`), removing interactive JS, and prioritizing logical headers.
> - Structuring pages for easy indexing improves agent navigation speed and prevents extraction errors.
>
> **Concept links:** [[AI Agents]], [[Web Optimization]], [[Markdown Endpoints]], [[Information Retrieval]]
>
> **Suggested connections:**
> - [[LLM Friendly Design]] — techniques for structuring databases and document systems for automated agents.
> - [[Search Engine Optimization]] — how agent-optimization differs from traditional human-centric SEO.
<!-- ai-summary:end -->

# [Optimizing Content for Agents](https://cra.mr/optimizing-content-for-agents/)

## Digest Summary
Optimizing content for AI agents involves tailoring responses to the constraints of frontier models, which often limit context size and favor concise, structured data. Key practices include:

- Providing a content‑negotiation hook (e.g., `Accept: text/markdown`) so agents receive raw markdown instead of HTML, reducing tokenization overhead and improving parsing accuracy.  
- Stripping browser‑only elements such as navigation scripts and JavaScript, and emphasizing link hierarchy to aid navigation.  
- Supplying programmatic entry points (MCP servers, CLI, API) when a human‑oriented page would otherwise require authentication, enabling agents to access structured data without HTML parsing.  
- Designing “skill” files in markdown that define prompts for code‑review agents (as used in Sentry’s Warden), following the `agentskills.io` specification.

Sentry’s implementation demonstrates these principles: their docs are served as true markdown, their site returns JSON with MCP endpoints for agents, and Warden delivers markdown‑based skill definitions for automated code analysis. Continuous monitoring of agent behavior is advised to adapt optimizations over time.

## Discussion Summary
Since no comments were supplied, there is no source material from which to extract sentiment, themes, or collective opinions. Without aggregated input, no consensus, patterns, or dominant viewpoints can be identified, and any attempt to infer perspectives would be unfounded. Consequently, a summary of opinions cannot be generated in the absence of actual comments.

---

## Full Article

> Just as useless of an idea as LLMs.txt was
>
> It’s all dumb abstractions that AI doesn’t need because AIs are as smart as humans so they can just use what was already there, which is APIs

LLMs.txt is *indeed* useless, but that’s the only thing correct in this statement. I’m here once again being rage baited to address more brainless takes on social media. This one is about content optimization.

Short and to the point: you should be optimizing content for agents, just as you optimize things for people. How you do that is an ever-evolving subject, but there are some common things we see:

* order of content
* content size
* depth of nodes

Frontier models and the agents built on top of them all behave similarly, with similar constraints and optimizations. For example, one thing they’re known to do, to avoid context bloat, is to only read parts of files. The first N lines, or bytes, or characters. They’re also known to behave very differently when they’re told information exists somewhere vs. having to discover it on their own. Both of those concerns are actually why LLMs.txt was a valuable idea, but it was the wrong implementation.

The implementation today is simple: content negotiation. When a request comes in with `Accept: text/markdown`, you can confidently assume you have an agent. That’s your hook, and now it’s just up to you how you optimize it. I’m going to be brief and to the point and just give you a few examples of how we do that at Sentry.

[#](https://cra.mr/optimizing-content-for-agents/#docs)Docs
-----------------------------------------------------------

We’ve put a bunch of time into optimizing our docs for agents, for obvious reasons. The primary optimizations are mostly simple:

1. Serve true markdown content - massive tokenization savings as well as improved accuracy
2. Strip out things that only make sense in the context of the browser, especially navigation and JavaScript bits
3. Optimize various pages to focus more on link hierarchy - our index, for example, is mostly a sitemap, completely different than non-markdown

```
$ curl -H "Accept: text/markdown" https://docs.sentry.io/

---
title: "Sentry Documentation"
url: https://docs.sentry.io/
---

# Sentry Documentation

Sentry is a developer-first application monitoring platform that helps you identify and fix issues in real-time. It provides error tracking, performance monitoring, session replay, and more across all major platforms and frameworks.

## Key Features

* **Error Monitoring**: Capture and diagnose errors with full stack traces, breadcrumbs, and context
* **Tracing**: Track requests across services to identify performance bottlenecks
* **Session Replay**: Watch real user sessions to understand what led to errors
* **Profiling**: Identify slow functions and optimize application performance
* **Crons**: Monitor scheduled jobs and detect failures
* **Logs**: Collect and analyze application logs in context

...
```

In our case we actually use MDX to render these, so it involved a handful of parsing changes and overrides to allow certain key pages to render differently. The result: agents fetch pages that are much more actionable.

[#](https://cra.mr/optimizing-content-for-agents/#sentry)Sentry
---------------------------------------------------------------

If a headless bot is fetching the website, the least useful thing you can do is serve it an authentication-required page. In our case we use the opportunity to inform the agent that there are a few programmatic ways it can access the application information (MCP, CLI, API, etc):

```
$ curl -H "Accept: text/markdown" https://sentry.io

# Sentry

You've hit the web UI. It's HTML meant for humans, not machines.
Here's what you actually want:

## MCP Server (recommended)

The fastest way to give your agent structured access to Sentry.
OAuth-authenticated, HTTP streaming, no HTML parsing required.

```json
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/mcp"
    }
  }
}
```

Docs: https://mcp.sentry.dev

## CLI

Query issues and analyze errors from the terminal.

https://cli.sentry.dev

...
```

[#](https://cra.mr/optimizing-content-for-agents/#warden)Warden
---------------------------------------------------------------

For projects like [Warden](https://warden.sentry.dev), we actually set it up so the agent can hit the entire content to bootstrap itself:

> Help me set up warden.sentry.dev

```
curl -H "Accept: text/markdown" https://warden.sentry.dev

# Warden

> Agents that review your code. Locally or on every PR.

Warden watches over your code by running **skills** against your changes. Skills are prompts that define what to look for: security vulnerabilities, API design issues, performance problems, or anything else you want consistent coverage on.

Skills follow the [agentskills.io](https://agentskills.io) specification. They're markdown files with a prompt that tells the AI what to look for. You can use community skills, write your own, or combine both.

- Docs: https://warden.sentry.dev
- GitHub: https://github.com/getsentry/warden
- npm: https://www.npmjs.com/package/@sentry/warden

## How It Works

Every time you run Warden, it:

1. Identifies what changed (files, hunks, or entire directories)
2. Matches changes against configured triggers
3. Runs the appropriate skills against matching code
4. Reports findings with severity, location, and optional fixes

Warden works in two contexts:

- **Locally** - Review changes before you push, get instant feedback
- **In CI** - Automatically review pull requests, post findings as comments

## Quick Start

...
```

If you’re varying the response based on the `Accept` header, you need to tell caches about it. Otherwise your CDN stores whichever version it sees first and serves that to everyone — markdown to browsers, HTML to agents, chaos all around.

```
Vary: Accept
```

Add `Vary: Accept` to your response headers so caches key on the request’s `Accept` value. Without it, content negotiation is just a race condition with your cache layer.

[#](https://cra.mr/optimizing-content-for-agents/#thats-it)That’s It
--------------------------------------------------------------------

It’s simple and it works. You should do it. You should also pay attention to how patterns are changing with agents and update your optimizations as behavior changes.