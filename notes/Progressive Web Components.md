---
title: "Progressive Web Components"
url: https://arielsalminen.com/2026/progressive-web-components/
clipped: 2026-08-31 12:18:08
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Progressive Web Components](https://arielsalminen.com/2026/progressive-web-components/)

## Digest Summary
Progressive Web Components are native Custom Elements built in two layers: an immediate HTML + CSS rendering layer and a JavaScript enhancement layer for reactivity and templating. Three categories are defined: Composite components (light‑DOM markup wrapped and enhanced), Primitive components (self‑contained markup with light‑DOM CSS), and Declarative components (hybrid using Declarative Shadow DOM).  
Elena is a 2.6 kB library that facilitates this design philosophy. It loads HTML and CSS first, then hydrates with JavaScript, preserving cross‑framework portability, accessibility, and server‑side rendering (SSR) compatibility. Components lacking a render() method are fully SSR‑compatible; those with render() provide initial HTML output with client‑side hydration, and an optional @elenajs/ssrtool offers full hydration. Elena supports standard custom‑element features (open/closed Shadow DOM,

---

## Full Article

[Skip to main content](https://arielsalminen.com/2026/progressive-web-components/#content)

# Progressive Web Components

I’ve worked with [web components](https://elenajs.com) for nearly a decade and built various enterprise-scale design systems with them. While I love what they offer on paper, the same pain points keep coming back:

Layout shifts, flash of unstyled content, poor server-side rendering support, too much reliance on client side JavaScript, doesn't play well with frame­works like React Server Components, accessibility issues, and so on…

Despite all of this, I still think web components are a great foundation for a [design system](https://arielsalminen.com/services/). No other approach gives you true cross-framework portability built on what the web platform already provides. The problem isn’t necessarily the model itself, it’s how we’ve been building them.

This is how I ended up creating [Elena](https://elenajs.com), a library that I’m [open sourcing](https://github.com/arielsalminen/elena) today. Elena starts from HTML and CSS, and stays grounded in web standards and what the web platform natively provides.

## What is a Progressive Web Component? [#](https://arielsalminen.com/2026/progressive-web-components/#what-is-a-progressive-web-component)

A [Progressive Web Component](https://elenajs.com/components/overview) is a native Custom Element designed in two layers: a base layer of HTML and CSS that renders immediately, without JavaScript, and an enhancement layer of JavaScript that adds reactivity, event handling, and more advanced templating. There are three types of Progressive Web Components:
- 

Composite Components that wrap and enhance the HTML composed inside them. All of their HTML and CSS lives in the Light DOM. You could also call these [HTML Web Components](https://adactio.com/journal/20618).
- 

Primitive Components that are self-contained and render their own HTML. All of their CSS lives in the Light DOM together with the base HTML required for rendering the initial state.
- 

Declarative Components that are a hybrid of these and utilize [Declarative Shadow DOM](https://elenajs.com/components/templates#declarative-shadow-dom).

Note: Elena doesn’t force this taxonomy. They’re [all just web components](https://elenajs.com/advanced/faq#can-i-build-normal-web-components-with-elena), and you choose how to build yours. But since “Progressive Web Components” is a design philosophy rather than a library feature, understand­ing the distinction between these approaches helps when deciding what fits your use case.

## So what is Elena, anyway? [#](https://arielsalminen.com/2026/progressive-web-components/#so-what-is-elena%2C-anyway)

[Elena](https://elenajs.com) is a simple, tiny library ( `2.6kB` ) for helping you to build [Progressive Web Components](https://elenajs.com/components/overview). Unlike most web component libraries, Elena doesn’t force JavaScript for everything. You can load HTML and CSS first, then use JavaScript to progressively add interactivity.

I built Elena for teams creating [component libraries](https://elenajs.com/advanced/libraries) and [design systems](https://elenajs.com/advanced/libraries). If you need web components that work across [multiple frameworks](https://elenajs.com/advanced/frameworks), render HTML and CSS before JavaScript loads, and sidestep common issues like accessibility problems, server-side rendering limitations, and layout shifts, Elena is built for exactly that.

It handles the cross-framework complexity (prop/attribute syncing, event delegation, framework compatibility) so you can focus on building web components rather than plumbing.A screenshot of Elena’s lifecycle documentation.

Since [Progressive Web Components](https://elenajs.com/components/overview) is a design philosophy rather than a library feature, Elena also allows you to build regular web components. The full standard custom element lifecycle and features such as open or closed [Shadow DOM](https://elenajs.com/components/styles#shadow-dom),  `<template>` ,  `<slot>`  and even [Declarative Shadow DOM](https://elenajs.com/advanced/ssr#declarative-shadow-dom) are all supported out of the box.

## What is Elena’s approach to SSR? [#](https://arielsalminen.com/2026/progressive-web-components/#what-is-elena%E2%80%99s-approach-to-ssr)

Elena’s approach to [server-side rendering](https://elenajs.com/advanced/ssr) is simple and straightforward. Since Progressive Web Components are primarily HTML and CSS, you don’t need any special logic on the server to render them.

Components without a  `render()`  method are fully SSR-compatible by default, while components with  `render()`  provide partial support and complete hydration on the client side.

The “partial support” bit for the latter means that you can render the initial state without JavaScript, but JS is needed for the interactivity (unless you also use the provided [@elenajs/ssr](https://elenajs.com/advanced/ssr) tool).

Elena also supports [Declarative Shadow DOM](https://elenajs.com/components/templates#declarative-shadow-dom) for cases where you may need stronger isolation, but still want the component to render server-side.A screenshot of Elena’s command line interface.

## Release candidate is out today! [#](https://arielsalminen.com/2026/progressive-web-components/#release-candidate-is-out-today)

I’m super happy to announce the first seventh release candidate of [Elena](https://elenajs.com),  `v1.0.0-rc.7`  today. This release comes with a bunch of useful features aimed at product teams creating component libraries. 🎉

## Feature highlights include: [#](https://arielsalminen.com/2026/progressive-web-components/#feature-highlights-include%3A)

### 🔋 Extremely lightweight [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%94%8B-extremely-lightweight)

 `2.6kB`  minified and compressed, simple and tiny by design.

### 📈 Progressively enhanced [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%93%88-progressively-enhanced)

Renders HTML and CSS first, then hydrates with JavaScript.

### 🫶 Accessible by default [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%AB%B6-accessible-by-default)

Semantic HTML foundation with no Shadow DOM barriers.

### 🌍 Standards based [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%8C%8D-standards-based)

Built entirely on native custom elements and web standards.

### ⚡ Reactive updates [#](https://arielsalminen.com/2026/progressive-web-components/#%E2%9A%A1-reactive-updates)

Prop and state changes trigger efficient, batched re-renders.

### 🎨 Scoped styles [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%8E%A8-scoped-styles)

Simple and clean CSS encapsulation without complex workarounds.

### 🖥️ SSR friendly [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%96%A5%EF%B8%8F-ssr-friendly)

Works out of the box, with optional server-side utilities if needed.

### 🧩 Zero dependencies [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%A7%A9-zero-dependencies)

No runtime dependencies, runs entirely on the web platform.

### 🔓 Zero lock-in [#](https://arielsalminen.com/2026/progressive-web-components/#%F0%9F%94%93-zero-lock-in)

Works with every major framework, or no framework at all.

## Included packages [#](https://arielsalminen.com/2026/progressive-web-components/#included-packages)

Elena is divided into [13 npm packages](https://github.com/arielsalminen/elena) published under the  `@elenajs`  scope. These are the main packages intended for development:
-  `` [@elenajs/core](https://elenajs.com): Elena core runtime. The thing you’d use 99% of the time, other packages are just supporting tooling.
-  `` [@elenajs/bundler](https://elenajs.com/advanced/libraries): Bundler for Elena web component libraries.
-  `` [@elenajs/cli](https://elenajs.com/advanced/cli): CLI for scaffolding Elena web components.
-  `` [@elenajs/ssr](https://elenajs.com/advanced/ssr): Server-side rendering tools for Elena.
-  `` [@elenajs/mcp](https://elenajs.com/advanced/mcp): MCP server to support working with Elena.
-  `` [@elenajs/components](https://elenajs.com/examples/): Example Progressive Web Components.

## Next steps [#](https://arielsalminen.com/2026/progressive-web-components/#next-steps)

- To learn more, visit Elena’s website: [https://elenajs.com](https://elenajs.com)
- Browse the [FAQ](https://elenajs.com/advanced/faq) for frequently asked questions
- View the [live examples](https://elenajs.com/examples/) for demos
- Try Elena in the [playground](https://elenajs.com/playground/)

[Learn more](https://elenajs.com)[Elena on GitHub](https://github.com/arielsalminen/elena)

## 

[Get in TouchDoes your team need help? I’m Ariel Salminen, a Design Systems Architect specialized in helping organizations build and maintain design systems. I’m available for both local and remote projects around the world.](https://arielsalminen.com/)

### Keyboard Shortcuts

- Press Ctrl+K to open the search.
- Press ⏎ to select a search result.
- Press ↓ to navigate to the next search result.
- Press ↑ to navigate to the previous search result.
- Press Esc to dismiss the search or a modal.
- Press ⇥ to navigate forward on the page.
- Press ⇧+⇥ to navigate backward on the page.
- Press Alt+A to toggle the layout grid.
- Press Alt+R to toggle the color blind mode.
- Press Alt+I to toggle the invert mode.
- Press Alt+E to toggle the low vision mode.
- Press Alt+L to open this modal.Close
