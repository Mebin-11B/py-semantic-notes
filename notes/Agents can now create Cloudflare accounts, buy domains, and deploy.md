---
title: "Agents can now create Cloudflare accounts, buy domains, and deploy"
url: https://blog.cloudflare.com/agents-stripe-projects/
clipped: 2026-06-17 01:06:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Agents can now create Cloudflare accounts, buy domains, and deploy](https://blog.cloudflare.com/agents-stripe-projects/)

## Digest Summary
Agents can now provision Cloudflare resources automatically through a new protocol co‑designed with Stripe and exposed via Stripe Projects. The workflow lets an AI agent:

* Discover available Cloudflare services through a REST‑based catalog API.  
* Create a Cloudflare account on‑demand (or link an existing one via OAuth) using Stripe as the identity provider, receiving an API token for authenticated calls.  
* Start paid subscriptions and register domains by sending a Stripe‑issued payment token to Cloudflare; raw credit‑card data never reaches the agent. A default $100 USD/month spend limit is applied, adjustable via budget alerts.  

Human users only need to log into Stripe, grant consent, and accept Cloudflare’s terms of service; no manual dashboard navigation, token copying, or credit‑card entry is required. The system also offers $100 k of Cloudflare credits to new startups using Stripe Atlas. Any platform with signed‑in users can act as the “Orchestrator,” replicating this integration pattern for other services. Stripe Projects is in open beta; installation requires the Stripe CLI and the Projects plugin.

## Discussion Summary
The discussion conveys frustration with Cloudflare’s previous account verification restrictions, describing them as a barrier that limited illicit activity. It highlights how large‑language‑model agents now automate domain purchases and deployments, accelerating fraudulent schemes. The integration of Stripe as a central hub for these agents is noted as a strategic move, though uncertainty remains about Cloudflare’s partnership status within Stripe’s Atlas program. Overall, the comments blend criticism of past enforcement with enthusiasm for newer automation tools that simplify domain acquisition.

---

## Full Article

Coding agents are great at building software. But to deploy to production they need three things from the cloud they want to host their app âÂ an account, a way to pay, and an API token. Until now these have been tasks that humans handle directly. Increasingly, agents handle them on the userâs behalf. The agent needs to perform all the tasks a human customer can. Theyâre given higher-order problems to solve and choose to use Cloudflare and call Cloudflare APIs.

Starting today, agents can provision Cloudflare on behalf of their users. They can create a Cloudflare account, start a paid subscription, register a domain, and get back an API token to deploy code right away. Humans can be in the loop to grant permission and must accept Cloudflare's terms of service, but no human steps are otherwise required from start to finish. Thereâs no need to go to the dashboard, copy and paste API tokens, or enter credit card details. Without any extra setup, agents have everything they need to deploy a new production application in one shot. And with Cloudflareâs [Code Mode MCP server](https://blog.cloudflare.com/code-mode/) and [Agent Skills](https://github.com/cloudflare/skills), theyâre even better at it.

This all works via a new protocol that weâve co-designed with Stripe as part of the launch of [Stripe Projects](https://projects.dev/).

Weâre excited to launch this new partnership with Stripe, and also to offer [$100,000 in Cloudflare credits](https://support.stripe.com/questions/stripe-atlas-perks-partners) to all new startups who incorporate using [Stripe Atlas](https://stripe.com/atlas). But this new protocol also makes it possible for any platform with signed-in users to integrate with Cloudflare in the same way Stripe does, with zero friction for the end user.

How it works:Â zero to production without any setup or manual steps
-------------------------------------------------------------------

Install the [Stripe CLI](https://docs.stripe.com/stripe-cli/install) with the [Stripe Projects plugin](https://docs.stripe.com/projects), login to Stripe, and then start a new project:

```
stripe projects init
```

Then prompt your agent to build something new and deploy it to a new domain. You can watch a condensed two-minute video of this entire flow below:

If the email youâre logged into Stripe with already has a Cloudflare account, youâll be prompted with a typical OAuth flow to grant the agent access. If there is no existing Cloudflare account for the email youâre logged in with, Cloudflare will provision an account automatically for you and your agent:

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5Y4grvxbS3wPfLYOGPV0PE/230d2f439ff9ea8cc75fe6cde9469792/image8.png)

You will see the agent build and deploy a site to a new Cloudflare account, and then use the Stripe Projects CLI to register the domain:

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/EKRFYCJLYdsFBVVAkrmnX/82a9781b1e5f8818093f1028decd310b/image6.png)

The agent will prompt for input and approval when necessary. For example, if your Stripe account doesnât yet have a linked payment method, the agent will prompt you to add one:

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2oTud5jPuMjldOEhLBbMrd/fb91e1065a84668f7bd606963006641b/image1.png)

At the end, the agent has deployed to production, and the app runs on the newly registered domain:

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/57boiRl1hScbG8n1ktcUzt/d97e1fc46610329e21accaa34ad92f13/image4.png)

The agent has gone from literal zero, no Cloudflare account at all, without any preconfigured [Agent Skills](https://github.com/cloudflare/skills) or [MCP server](https://blog.cloudflare.com/code-mode-mcp/), to having:

But wait âÂ how did the agent discover that it could do all of this? How did it know what services it could provision, and how to purchase a domain? How did it gain the context it needed to understand how to deploy to Cloudflare? Letâs dig in.

How the protocol and integration works
--------------------------------------

There are three components to the interaction between the agent, Stripe, and Cloudflare shown above:

* **Discovery** â the agent can call a command to query the catalog of available services.
* **Authorization** âÂ the platform attests to the identity of the user, allowing providers to provision accounts or link existing ones, and securely issue credentials back to the agent.
* **Payment** âÂ the platform provides a payment token that providers can use to bill the customer, allowing the agent to start subscriptions, make purchases and be billed on a usage basis.

These build on prior art and existing standards like OAuth, OIDC and payment tokenization âÂ but are used together to remove many steps that might otherwise require a human in the loop.

Discovery:Â how agents find services they can provision themselves
------------------------------------------------------------------

In the agent session above, before the agent ran the CLI command `stripe projects add cloudflare/registrar:domain`, it first had to discover the [Cloudflare Registrar](https://domains.cloudflare.com/) service. It did this by calling the `stripe projects catalog` command, which returns available services:

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/1fGiH332y2mAIfxiPT4Uof/cad52b61f6f7c89088ea3d54cb678a46/image2.png)

The full set of [Cloudflare products](https://developers.cloudflare.com/directory/) and services from other providers is [long and growing](https://docs.stripe.com/projects#available-providers) â arguably overwhelming to humans. But for agents, this catalog of services is exactly the context they need. The agent chooses services to use from this catalog based on what the user has asked them to do and the userâs preferences â but the user needs no prior knowledge of what services are offered by which providers, and does not need to provide any input. Providers like Cloudflare make this catalog available via a simple REST API that returns JSON, and that gives agents everything they need.

Authorization: instant account creation for new users
-----------------------------------------------------

When the agent chooses a service and provisions it (ex: `stripe projects add cloudflare/registrar:domain`), it provisions the resource within a Cloudflare account. But how is it able to create one on demand, without sending a human to a signup page?

Remember how at the start, the user signed in to their Stripe account? Stripe acts as the identity provider, attesting to the userâs identity. Cloudflare automatically provisions a new account for the user if no account already exists, and returns credentials back to the Stripe Projects CLI, which are securely stored, but available to the agent to use to make authenticated requests to Cloudflare. This means if someone is brand new to Cloudflare or other services, they can start building right away with their agent, without extra steps.

If the user already has a Cloudflare account, theyâre sent through a standard OAuth flow to grant access to the Stripe Projects CLI, allowing them to provision resources on their existing Cloudflare account.

Payment:Â give your agent a budget it can spend, without giving it your credit card info
----------------------------------------------------------------------------------------

You might rightly worry, âWhat if my agent goes a bit overboard and starts buying dozens of domains? Will I end up on the hook for a massive bill? Can I really trust my agent with my credit card?â

The protocol accounts for this in two ways. When an agent provisions a paid service, Stripe includes a payment token in the request to the Provider (Cloudflare). Raw payment details like credit card numbers arenât ever shared with the agent. Stripe then sets a default limit of $100.00 USD/month as the maximum the agent can spend on any one provider. When youâre ready to raise this limit, you can then set [Budget Alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) on your Cloudflare account.

Any platform with signed-in users can integrate with Cloudflare in the same way Stripe does
-------------------------------------------------------------------------------------------

Any platform with signed-in users can act as the âOrchestratorâ, playing the same role Stripe does with Stripe Projects, and integrate with Cloudflare.

Letâs say your product is a coding agent. Youâd love for people to be able to take what theyâve built and get it deployed to production, using Cloudflare and other services. But the last thing you want is to send people down a maze of authorization flows and decision trees of where and how to deploy it. You just want to let people ship.

Your platform acts as the Orchestrator, with the already signed-in user. When your user needs a [domain](https://domains.cloudflare.com/), a [storage bucket](https://developers.cloudflare.com/r2/), a [sandbox](https://blog.cloudflare.com/dynamic-workers/) to give their agent, or [anything else](https://workers.cloudflare.com/), you make one API call to Cloudflare to provision a new Cloudflare account to them, and get back a token to make authenticated requests on their behalf.

Or letâs say you want Cloudflare customers to be able to easily provision your service, similar to how Cloudflare is partnering with Planetscale to make it possible to [create Planetscale Postgres databases directly from Cloudflare](https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/). We started working with Planetscale on this well before this new protocol got off the ground, but the flow here is quite similar. Cloudflare acts as the Orchestrator, letting you connect to your PlanetScale account, create databases, and use the userâs existing payment method for billing.

This new protocol starts to standardize the types of cross-product integrations that many platforms have been doing for years, often in ways that were one off or bespoke to a particular platform. Without a standard, each integration required engineering work that often couldnât be leveraged for future integrations. Similar to how the [OAuth standard](https://oauth.net/2/) made it possible to delegate access to your account to other platforms, the protocol uses OAuth and extends further into payments and account creation, doing so in a way that treats agents as a first-class concern.

Weâre excited to continue evolving the standard, and to work with Stripe on sharing a more official specification soon. Weâre also excited to integrate with more platforms âÂ  email us at [[email protected]](https://blog.cloudflare.com/agents-stripe-projects/#), and tell us how you want your platform to integrate with Cloudflare.

Give your agent the power to provision and pay
----------------------------------------------

Stripe Projects is in open beta, and you can get started even if you donât yet have a Cloudflare account. Just install the [Stripe CLI](https://docs.stripe.com/stripe-cli/install), log in to Stripe, and then start a new project:

```
stripe projects init
```

Prompt your agent to build something new on Cloudflare, and show us what youâve built!