---
title: "Show HN: Mastra 1.0, open-source JavaScript agent framework from the Gatsby devs"
url: https://github.com/mastra-ai/mastra
clipped: 2026-06-17 01:55:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Mastra 1.0, open-source JavaScript agent framework from the Gatsby devs](https://github.com/mastra-ai/mastra)

## Digest Summary
Mastra is an open‑source framework for building AI‑powered applications and agents, authored by the team behind Gatsby and written in a modern TypeScript stack. The GitHub repository displays typical project badges: npm package version, CodeQL analysis status, star count, Discord and Twitter community links, npm download statistics, and a static build badge. A long list of contributor usernames (e.g., @envoy1084, @sizzlebop, @cmullins70, @Balbader, @SLAI‑HUB, @CLOUDPIXEL‑LAB, etc.) is shown, indicating active community involvement. The page also includes a generic “You can’t perform that action at this time” notice, likely related to a restricted GitHub operation.

## Discussion Summary
Overall sentiment is positive, praising the launch, developer experience, UI, and TypeScript integration. Common themes include appreciation for the framework’s quality, a desire for clearer guidance on practical use cases, and concerns about workflow complexity when using non‑LLM agents, leading some to prefer rule‑based logic. There are worries about platform lock‑in, comparisons with other agent frameworks, and curiosity about future alignment with the Vercel AI SDK and Claude Agent SDK, as well as questions about real‑world applications beyond simple chat bubbles.

---

## Full Article

[![npm version](https://camo.githubusercontent.com/0f0dd95c064904c8c2c18b69582eb97f163ddbb1221a2e23d6fb4cab37bcddcf/68747470733a2f2f62616467652e667572792e696f2f6a732f406d6173747261253246636f72652e737667)](https://www.npmjs.com/package/@mastra/core)
[![CodeQl](https://github.com/mastra-ai/mastra/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/mastra-ai/mastra/actions/workflows/github-code-scanning/codeql)
[![GitHub Repo stars](https://camo.githubusercontent.com/2ec077b4adc1761e785781b4631581b2cb9e69519158684c94ee55e119c560a0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6d61737472612d61692f6d6173747261)](https://github.com/mastra-ai/mastra/stargazers)
[![Discord](https://camo.githubusercontent.com/7349353f755b34b2ddf5991cdf263daaa7ab0cb20c0e3699dfa5d8e59ff413d8/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313330393535383634363232383737393133393f6c6f676f3d646973636f7264266c6162656c3d446973636f7264266c6162656c436f6c6f723d776869746526636f6c6f723d373238394441)](https://discord.gg/BTYqqHKUrf)
[![Twitter Follow](https://camo.githubusercontent.com/81df0a9aaaeea0c0bc42d649ac6e8ff3920705d0f21ff52de19dd7047de51baf/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6d61737472613f7374796c653d736f6369616c)](https://x.com/mastra)
[![NPM Downloads](https://camo.githubusercontent.com/c91935107e53fb03125664f93f25e84f9ed947c9b892dd8374952464af106351/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f2534306d61737472612532353246636f7265)](https://www.npmjs.com/package/@mastra/core)
[![Static Badge](https://camo.githubusercontent.com/128f10e53ff366ebb8985128d3a5ec40fa1c9d68f842ef1f9410ae17ea1f4352/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f59253230436f6d62696e61746f722d5732352d6f72616e6765)](https://www.ycombinator.com/companies?batch=W25)

Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.

It includes everything you need to go from early prototypes to production-ready applications. Mastra integrates with frontend and backend frameworks like React, Next.js, and Node, or you can deploy it anywhere as a standalone server. It's the easiest way to build, tune, and scale reliable AI products.

Purpose-built for TypeScript and designed around established AI patterns, Mastra gives you everything you need to build great AI applications out-of-the-box.

Some highlights include:

* [**Model routing**](https://mastra.ai/models) - Connect to 40+ providers through one standard interface. Use models from OpenAI, Anthropic, Gemini, and more.
* [**Agents**](https://mastra.ai/docs/agents/overview) - Build autonomous agents that use LLMs and tools to solve open-ended tasks. Agents reason about goals, decide which tools to use, and iterate internally until the model emits a final answer or an optional stopping condition is met.
* [**Workflows**](https://mastra.ai/docs/workflows/overview) - When you need explicit control over execution, use Mastra's graph-based workflow engine to orchestrate complex multi-step processes. Mastra workflows use an intuitive syntax for control flow (`.then()`, `.branch()`, `.parallel()`).
* [**Human-in-the-loop**](https://mastra.ai/docs/workflows/suspend-and-resume) - Suspend an agent or workflow and await user input or approval before resuming. Mastra uses [storage](https://mastra.ai/docs/server-db/storage) to remember execution state, so you can pause indefinitely and resume where you left off.
* **Context management** - Give your agents the right context at the right time. Provide [conversation history](https://mastra.ai/docs/memory/conversation-history), [retrieve](https://mastra.ai/docs/rag/overview) data from your sources (APIs, databases, files), and add human-like memory with [Observational Memory](https://mastra.ai/docs/memory/observational-memory) so your agents behave coherently.
* **Integrations** - Bundle agents and workflows into existing React, Next.js, or Node.js apps, or ship them as standalone endpoints. When building UIs, integrate with agentic libraries like Vercel's AI SDK UI and CopilotKit to bring your AI assistant to life on the web.
* [**MCP servers**](https://mastra.ai/docs/tools-mcp/mcp-overview) - Author Model Context Protocol servers, exposing agents, tools, and other structured resources via the MCP interface. These can then be accessed by any system or agent that supports the protocol.
* **Production essentials** - Shipping reliable agents takes ongoing insight, evaluation, and iteration. With built-in [evals](https://mastra.ai/docs/evals/overview) and [observability](https://mastra.ai/docs/observability/overview), Mastra gives you the tools to observe, measure, and refine continuously.

The **recommended** way to get started with Mastra is by running the command below:

Follow the [Installation guide](https://mastra.ai/docs/getting-started/installation) for step-by-step setup with the CLI or a manual install.

If you're new to AI agents, check out our [templates](https://mastra.ai/docs/getting-started/templates), [course](https://mastra.ai/course), and [YouTube videos](https://youtube.com/@mastra-ai) to start building with Mastra today.

**Alternative:** Use this pre-built prompt to get started

```
Make new Mastra project. Mastra = framework for AI apps + agents on modern TypeScript stack. Before run command, ask these questions one by one. Wait for answers unless already given:

Project name? (default: "my-mastra-app")
Provider? (default: "openai", options: "openai", "anthropic", "groq", "google", "cerebras", "mistral")
Provider rules:

Allowed provider -> use it.
Any other value -> use "openai".
Run with answers: npm create mastra@latest <project-name> --default --llm <provider>

After project created, go to project dir. Start dev server: npx bgproc start -n <project-name> -w -- npm run dev

Start Mastra Studio at http://localhost:4111. Studio = UI for build, test, manage agents, workflows, tools.

Also tell: Mastra model router give 3000+ models from many providers: https://mastra.ai/models
```

Visit our [official documentation](https://mastra.ai/docs).

Learn how to make your agent a Mastra expert by following the [Build with AI guide](https://mastra.ai/docs/getting-started/build-with-ai).

Looking to contribute? All types of help are appreciated, from coding to testing and feature specification. Read [CONTRIBUTING.md](https://github.com/mastra-ai/mastra/blob/main/CONTRIBUTING.md) for more details on how to get involved.

If you are a developer and would like to contribute with code, please open an issue to discuss before opening a Pull Request.

Information about the project setup can be found in the [development documentation](https://github.com/mastra-ai/mastra/blob/main/DEVELOPMENT.md)

We have an [open community Discord](https://discord.gg/BTYqqHKUrf). Come and say hello and let us know if you have any questions or need any help getting things running.

It's also super helpful if you leave the project a star here, at the [top of the page](https://github.com/mastra-ai/mastra)

This repository uses a dual-license model:

* **Apache License 2.0** — The core framework and the vast majority of this codebase is open source under Apache-2.0.
* **Mastra Enterprise License** — Code in any directory named `ee/` (e.g., `packages/core/src/auth/ee/`) is source-available under the Mastra Enterprise License. These features require a valid enterprise license for production use but can be freely used for development and testing.

See [LICENSE.md](https://github.com/mastra-ai/mastra/blob/main/LICENSE.md) for the full license mapping and [ee/LICENSE](https://github.com/mastra-ai/mastra/blob/main/ee/LICENSE) for the enterprise license terms.

We are committed to maintaining the security of this repo and of Mastra as a whole. If you discover a security finding we ask you to please responsibly disclose this to us at [security@mastra.ai](mailto:security@mastra.ai) and we will get back to you.