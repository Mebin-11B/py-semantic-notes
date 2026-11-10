---
title: "You're Looking at the Wrong Pretext Demo"
source: "https://denodell.com/blog/youre-looking-at-the-wrong-pretext-demo"
author:
  - "[[Den Odell]]"
published: 2026-03-30
created: 2026-06-01
description: "Pretext went viral for its beautiful canvas demos. But the community is showcasing the wrong feature."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Developer Tools
  - Accessibility
  - Browser Performance
  - Web Development
  - Digital Culture
related:
  - "Developer Tools"
  - "Markdown with superpowers.md"
  - "The best is over.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Den Odell argues that while Pretext went viral for its interactive canvas animations, its true innovation is its accessible mathematical DOM layout engine that predicts text dimensions without causing costly browser reflows.
>
> **Key points:**
> - Clarifies the core value of Pretext: using canvas-based arithmetic (prepare() and layout()) to predict text heights and line wraps without accessing the DOM or triggering forced layouts.
> - Critiques manual canvas text rendering (the viral demos like ASCII smoke and dragons), explaining that painting text pixels destroys essential browser accessibility (JAWS/VoiceOver, translation, find-in-page, text selection).
> - Shows how Pretext enables performance optimization (e.g., virtual scrolling chat interfaces, masonry layouts, and fit-content calculations) while maintaining semantic DOM nodes.
> - Applies Goodhart's Law to frontend development, pointing out how the community optimizes for viral visual appeal (the proxy) over invisible usability gains.
> - Compares Pretext's DOM-preservation philosophy to robust web editors like CodeMirror, Monaco, and ProseMirror.
>
> **Concept links:** [[Developer Tools]], [[Accessibility]], [[Browser Performance]], [[Web Development]], [[Digital Culture]]
>
> **Suggested connections:**
> - [[Markdown with superpowers.md]] — connects document layout, typography, and developer-facing markup systems to programmatic rendering.
> - [[The best is over.md]] — links the critique of optimizing for viral online engagement metrics to the decay of authentic digital design.
> - [[ajratnamimage-to-ascii A python program to convert an image into an ascii image.md]] — connects text-based artistic representation (like the ASCII-smoke demos mentioned) to developer utility implementations.
<!-- ai-summary:end -->

[Pretext](https://github.com/chenglou/pretext), a new JavaScript library from Cheng Lou, crossed 7,000 GitHub stars in its first three days. If you’ve been anywhere near the frontend engineering circles in that time, you’ve seen the demos: [a dragon that parts text like water](https://pretext-playground.builderz.dev/), [fluid smoke rendered as typographic ASCII](https://somnai-dreams.github.io/pretext-demos/fluid-smoke.html), [a wireframe torus drawn through a character grid](https://somnai-dreams.github.io/pretext-demos/wireframe-torus.html), [multi-column editorial layouts with animated orbs displacing text at 60fps](https://somnai-dreams.github.io/pretext-demos/the-editorial-engine.html). These are visually stunning and they’re why the library went viral.

But they aren’t the reason this library matters.

---

The important thing Pretext does is predict the height of a block of text without ever reading from the DOM. This means you can position text nodes without triggering a single layout recalculation. The text stays in the DOM, so screen readers can read it and users can select it, copy it, and translate it. The accessibility tree remains intact, the performance gain is real, and the user experience is preserved for everyone. This is the feature that will change how production web applications handle text, and it’s the feature almost nobody is demonstrating.

The community has spent three days building dragons. It should be building chat interfaces. And the fact that the dragons went viral while the measurement engine went unnoticed tells us something important about how the frontend community evaluates tools: we optimize for what we can see, not for what matters most to the people using what we build.

---

## The Problem Pretext Solves

The problem is forced layout recalculation, where the browser has to pause and re-measure the page layout before it can continue. When a UI component needs to know the height of a block of text, the standard approach is to measure it from the DOM. You call `getBoundingClientRect()` or read `offsetHeight`, and the browser synchronously calculates layout to give you an answer. Do this for 500 text blocks in a virtual list and you’ve forced 500 of these pauses. This pattern, called *layout thrashing*, remains a leading cause of visual stuttering in complex web applications.

Pretext’s insight is that `canvas.measureText()` uses the same font engine as DOM rendering but operates outside the browser’s layout process entirely. Measure a word via canvas, cache the width, and from that point forward layout becomes pure arithmetic: walk cached widths, track running line width, and insert breaks when you exceed the container’s maximum. No slow measurement reads, and no synchronous pauses.

The architecture separates this into two phases. `prepare()` does the expensive work once: normalize whitespace, segment the text using `Intl.Segmenter` for locale-aware word boundaries, handle bidirectional text (such as mixing English and Arabic), measure segments with canvas, and return a reusable reference. `layout()` is then pure calculation over cached widths, taking about 0.09ms for a 500-text batch against roughly 19ms for `prepare()`. Cheng Lou himself calls the 500x comparison “unfair” since it excludes the one-time `prepare()` cost, but that cost is only paid once and spread across every subsequent call. It runs once when the text appears, and every subsequent resize takes the fast path, where the performance boost is real and substantial.

The core idea traces back to Sebastian Markbåge’s research at Meta, where Cheng Lou implemented the [earlier `text-layout` prototype](https://github.com/chenglou/text-layout) that proved canvas font metrics could substitute for DOM measurement. Pretext builds on that foundation with production-grade internationalization, bidirectional text support, and the two-phase architecture that makes the fast path so fast. Lou has a track record here: [react-motion](https://github.com/chenglou/react-motion) and ReasonML both followed the same pattern of identifying a constraint everyone accepted as given and removing it with a better abstraction.

---

## The Measurement Breakthrough

The first use case Pretext serves, and the one I want to make the case for, is measuring text height so you can render DOM text nodes in exactly the right position without ever asking the browser how tall they are. This isn’t a compromise path, it’s the most capable thing the library does.

Consider a virtual scrolling list of 500 chat messages. To render only the visible ones, you need to know each message’s height before it enters the viewport. The traditional approach is to insert the text into the DOM, measure it, and then position it, paying the layout cost for every message. Pretext lets you predict the height mathematically and then render the text node at the right position. The text itself still lives in the DOM, so the accessibility model, selection behavior, and find-in-page all work exactly as they would with any other text node.

Here’s what that looks like in practice:

```javascript
const prepared = prepare(message.text, '16px Inter');
const { height } = layout(prepared, containerWidth, 24);
```

Two function calls: the first measures and caches, the second predicts height through calculation. No layout cost, yet the text you render afterward is a standard DOM node with full accessibility.

[The shrinkwrap demo](https://chenglou.me/pretext/bubbles/) is the clearest example of why this path matters. CSS `width: fit-content` sizes a container to the widest wrapped line, which wastes space when the last line is short. There’s no CSS property that says “find the narrowest width that still wraps to exactly N lines.” Pretext’s `walkLineRanges()` calculates the optimal width mathematically, and the result is a tighter chat bubble rendered as a standard DOM text node. The performance gain comes from smarter measurement, not from abandoning the DOM. Nothing about the text changes for the end user.

[Accordion sections](https://chenglou.me/pretext/accordion/) whose heights are calculated from Pretext, and [masonry layouts](https://chenglou.me/pretext/masonry/) with height prediction instead of DOM reads: these both follow the same model of fast measurement feeding into standard DOM rendering.

There are edge cases worth knowing about, starting with the fact that the prediction is only as accurate as the font metrics available at measurement time, so fonts need to be loaded before `prepare()` runs or results will drift. Ligatures (where two characters merge into one glyph, like “fi”), advanced font features, and certain [CJK](https://en.wikipedia.org/wiki/CJK_characters) composition rules can introduce tiny differences between canvas measurement and DOM rendering. These are solvable problems and the library handles many of them already, but acknowledging them is part of taking the approach seriously rather than treating it as magic.

---

## Canvas Paints Pixels, Not Accessible Text

Pretext also supports manual line layout for rendering to Canvas, SVG, or WebGL. These APIs give you exact line coordinates so you can paint text yourself rather than letting the DOM handle it. This is the path that went viral, and the one that dominates every community showcase.

The canvas demos are impressive and they’re doing things the DOM genuinely can’t do at 60fps. But they’re also painting pixels, and when you paint text as canvas pixels, the browser has no idea those pixels represent language. Screen readers like VoiceOver, NVDA, and JAWS derive their understanding of a page from the accessibility tree, which is itself built from the DOM, so canvas content is invisible to them. Browser find-in-page and translation tools both skip canvas pixels entirely. Native text selection is tied to DOM text nodes and canvas has no equivalent, so users can’t select, copy, or navigate the content by keyboard. A `<canvas>` element is also a single tab stop, meaning keyboard users can’t move between individual words or paragraphs within it, even if it contains thousands of words. In short, everything that makes text behave as text rather than an image of text disappears.

None of this means the canvas path is automatically wrong. There are legitimate contexts where canvas text rendering is the right choice: games, data visualizations, creative installations, and design tools that have invested years in building their own accessibility layer on top of canvas. For SVG rendering, the trade-offs are different again, since SVG text elements do participate in the accessibility tree, making it a middle ground between DOM and canvas.

But the canvas path is not the breakthrough, because canvas text rendering has existed for fifteen or more years across dozens of libraries. What none of them offered was a way to predict DOM text layout without paying the layout cost. Pretext’s `prepare()` and `layout()` do exactly that, and it’s genuinely new.

---

## The Wrong Demos Often Go Viral

This pattern often repeats across the frontend ecosystem, and I understand why.

A dragon parting text like water is something you can record as a GIF, post to your socials, and collect thousands of impressions. A virtual scrolling list that pre-calculates text heights looks identical to one that doesn’t. The performance difference is substantial but invisible to the eye. Nobody makes a showcase called “works flawlessly with VoiceOver” or “scrolls 10,000 messages without a single forced layout” because these things look like nothing. They look like a web page working the way web pages are supposed to work.

This is [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) applied to web performance: once a metric becomes a target, it ceases to be a good measure. Frame rate and layout cost are proxies for “does this work well for users.” GitHub stars are a proxy for “is this useful.” When the proxy gets optimized instead, in this case by visually impressive demos that happen to use the path with the steepest accessibility trade-offs, the actual signal about what makes the library important gets lost. The library’s identity gets set by its most visually impressive feature in the first 72 hours, and the framing becomes “I am drawing things” rather than “I am measuring things faster than anyone has before.” Once that framing is set, it’s hard to shift.

The best text-editing libraries on the web, [CodeMirror](https://codemirror.net/), [Monaco](https://microsoft.github.io/monaco-editor/), and [ProseMirror](https://prosemirror.net/), all made the deliberate choice to stay in the DOM even when leaving it would have been faster, because the accessibility model isn’t optional. Pretext’s DOM measurement path belongs in that tradition but goes further: those editors still read from the DOM when they need to know how tall something is. Pretext eliminates that step entirely, predicting height through arithmetic before the node is ever rendered. It’s the next logical step in the same philosophy: keep text where it belongs, but stop paying the measurement cost to do so.

---

## The Bigger Picture

I’ve been thinking about performance engineering as a discipline for most of my career, and what strikes me about Pretext is that the real innovation is the one that is hardest to see. Predicting how text will lay out before it reaches the page, while keeping the text in the DOM and preserving everything that makes it accessible, is a genuinely new capability on the web platform. It’s the kind of foundational improvement that every complex text-heavy application can adopt immediately.

If you’re reaching for Pretext this week, reach for `prepare()` and `layout()` first. Build something that keeps text in the DOM and predicts its height without asking the browser. Ship an interface that every user can read, select, search, and navigate. Nobody else has done this yet, and it deserves building.

Performance engineering is at its best when it serves everyone without asking anyone to give something up. Faster frame rates that don’t make someone nauseous. Fewer layout pauses that mean a page responds when someone with motor difficulties needs it to. Text that is fast and readable and selectable and translatable and navigable by keyboard and comprehensible to a screen reader.

The dragons are fun. The measurement engine is important. Let’s try not to confuse the two.

---

Share this post:

[Back to top](#)