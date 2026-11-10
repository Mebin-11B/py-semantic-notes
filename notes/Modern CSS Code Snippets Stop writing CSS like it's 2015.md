---
title: "Modern CSS Code Snippets: Stop writing CSS like it's 2015"
url: https://modern-css.com
clipped: 2026-06-17 01:44:45
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Modern CSS Code Snippets: Stop writing CSS like it's 2015](https://modern-css.com)

## Digest Summary
The page presents a modern CSS code snippet that consolidates multiple heading selectors within a `.card` component. The legacy rule lists each heading element separately:

```css
.card h1, .card h2, .card h3, .card h4 { margin-bottom: 0.5em; }
```

The updated version employs the `:is()` pseudo‑class to group the selectors:

```css
.card:is(h1, h2, h3, h4) { margin-bottom: 0.5em; }
```

Using `:is()` reduces repetition, improves readability, and simplifies maintenance by applying the same style to all specified heading levels in a single declaration. The snippet demonstrates how modern CSS syntax can replace verbose selector chains with concise, function‑based selectors.

## Discussion Summary
The comments recognize recent CSS advances such as nested rules, :has, :is, :where and custom properties as useful, while questioning their limited browser support and noting that many demos rely on Chrome/Edge. Opinions diverge between advocates of utility frameworks, inline‑in‑JS, and preprocessors versus supporters of classic flexbox/grid techniques and older, broadly compatible code. Concerns are raised about vendor‑specific prefixes, excessive static layout elements, and the relevance of modern features for users on outdated browsers or low‑end devices. Overall, the discussion balances enthusiasm for new capabilities with caution about practical compatibility.

---

## Full Article

Old way

```
/* JS: manage hover, focus, and position */btn.addEventListener('mouseenter', () =>   {  tip.hidden = false;  positionTooltip(btn, tip);});btn.addEventListener('mouseleave', () =>   {  tip.hidden = true;});btn.addEventListener('focus', /* … */);btn.addEventListener('blur', /* … */);
```