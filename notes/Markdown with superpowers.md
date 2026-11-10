---
title: "Markdown with superpowers"
source: "https://quarkdown.com/"
author:
  - "[[Giorgio Garofalo]]"
published:
created: 2026-06-01
description: "Quarkdown is a modern, open-source, Markdown-based typesetting system for creating papers, presentations, knowledge bases and static websites."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Developer Tools
  - Markdown
  - Typesetting
  - Knowledge Management
  - Model Context Protocol
related:
  - "Developer Tools"
  - "Knowledge Management"
  - "tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An introduction to Quarkdown, an open-source Markdown-based typesetting system designed to create papers, presentations, wikis, and static websites using a single tool.
>
> **Key points:**
> - Synthesizes multiple formatting requirements into a single Markdown-based markup language with a focus on ease of authoring.
> - Supports multiple output formats (docs, slides, paged reports, plain web pages) controlled by a simple .doctype configuration.
> - Built to be 'agent-friendly,' offering structured patterns and skills that make it easy for AI coding agents to write and refactor.
> - Includes advanced templating, layout rows/columns, and macro functions to avoid repetition in document layouts.
>
> **Concept links:** [[Developer Tools]], [[Markdown]], [[Typesetting]], [[Knowledge Management]], [[Model Context Protocol]]
>
> **Suggested connections:**
> - [[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]] — links to tools designed for processing and managing local knowledge bases.
> - [[Going Full Time on Open Source.md]] — connects to open-source developer tool creation and community ecosystem efforts.
<!-- ai-summary:end -->

## Spend your time writing

and don't worry about the rest.

```
.docauthor {Jennifer Chu}

.pagemargin {topright}
    .docauthor | MIT News

# X-ray flashes from a supermassive black hole

!(70%)[Black hole](img/blackhole.jpg)

.abstract
    One supermassive black hole has kept astronomers glued to their scopes
    for the last several years.
    The black hole in question is \`1ES 1927+654\`, which is about as
    massive as a million suns and sits in a galaxy that is 270 million
    light-years away.
    In 2018, astronomers at MIT and elsewhere observed that the black
    hole’s corona — a cloud of whirling, white-hot plasma — suddenly
    **disappeared**, before reassembling months later.
    The brief though dramatic shut-off was a first in black hole astronomy.

> This would be the closest thing we know of around any black hole.
> - Megan Masterson, a graduate student in physics at MIT
```
![Rendered article about X-ray flashes from a supermassive black hole](https://quarkdown.com/_astro/no-boilerplate.SaDlAnd3_Z10UnlF.webp)

Batteries included

## Complete authoring experience

Write Markdown to reach flow state faster.  
Use Quarkdown's extensions to achieve more.

Ready for autopilot

## Agent-friendly

Let your AI agent speak fluent Quarkdown with built-in skills.  
[Read the eval](https://quarkdown.com/blog/agent-skill)

\> Add a warning for candy thieves

Versatile

## One tool to rule them all

Whether you are writing a research paper, a quick report, a company-wide wiki, class notes, or preparing interactive slides for your next talk, there's only one line you need.

```
.doctype {paged}
```
![Paged document output showing a formatted article](https://quarkdown.com/_astro/doctype-paged.D0Cs-mnS_Z17X8C6.webp)

For articles, books and reports.

```
.doctype {plain}
```
![Plain document output showing a coffee brewing guide](https://quarkdown.com/_astro/doctype-plain.DAkJSSiY_Z2swD77.webp)

For notes, knowledge bases and simple static websites.

```
.doctype {docs}
```
![Documentation website output](https://quarkdown.com/_astro/doctype-docs.Bk9wAFWq_1v0TuY.webp)

For wikis, technical documentation and large knowledge bases.

```
.doctype {slides}
```
![Slide presentation output](https://quarkdown.com/_astro/doctype-slides.CezSCHgD_ZiSEey.webp)

For lectures, talks and interactive presentations.

Reactive preview

## Typesetting for the impatient

With blazing fast compilation and live preview, see results instantly as you type.

## Don't repeat yourself

Reuse your workflow thanks to powerful scripting capabilities.

```
.function {animal}
    name ecosystem picture:
    .row
        .clip {circle}
            .picture

        - **Name**: .name
        - **Ecosystem**: .ecosystem

.animal {Red panda} ecosystem:{Temperate forests}
    ![Red panda](img/red-panda.jpg)

.animal {Sea otter} ecosystem:{Kelp forests}
    ![Sea otter](img/sea-otter.jpg)

.animal {Clownfish} ecosystem:{Coral reefs}
    ![Clownfish](img/clownfish.jpg)
```
![Animal cards rendered from a custom function](https://quarkdown.com/_astro/scripting.B2wI0zk3_Z133iOD.webp)