---
title: "Adding insular script like it's 1626"
url: https://www.djmurphy.net/blog/clo-gaelach/
clipped: 2026-06-17 02:03:17
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Adding insular script like it's 1626](https://www.djmurphy.net/blog/clo-gaelach/)

## Digest Summary
The medieval Irish “Cló Gaelach” script evolved from Latin to encode Irish phonology, using a dot over consonants to indicate séimhiú (softening). Production was hampered by limited insular typefaces and cumbersome typewriter entry (letter + backspace + dot), making printing slow and costly. Modern Irish orthography replaced the dot with a following “h”, which preserves the text but reduces phonetic transparency.

To revive the visual style while keeping text data intact, the author created an OpenType font (Úr cló GC) with discretionary ligatures that replace consonant‑+‑h sequences with dotted equivalents and substitute the ampersand with the Tironian “et”. The ligatures are optional, activated via `font-variant-ligatures: discretionary-ligatures;`, so copy‑paste and screen‑reader output remain in standard Latin characters.

For web presentation, a custom Astro component wraps Irish text in a `` element, providing a visible Gaelic script (via the ligature‑enabled font) and an optional English translation displayed as ruby annotation. The component also includes hidden `` elements with `lang="ga"` and `lang="en"` for screen‑reader accessibility, preserving language metadata while delivering the historic visual aesthetic.

## Discussion Summary
The remarks convey a positive reception of the ruby HTML element, describing it as an effective expanded use case, and express agreement with the observation that older internet blogs are experiencing a resurgence, a trend the commenter finds enjoyable. The tone is enthusiastic, highlighting personal enjoyment and alignment with the broader shift toward nostalgic online content.

---

## Full Article

I’m a generation removed from when Irish children were taught to read and write in insular Irish script the Cló Gaelach.

[![artistic print of the Irish alphabet in old script](https://www.djmurphy.net/main-web-clo-gaelach.jpg)](https://www.ninearrow.com/shop/p/clo-gaelach)

Here’s a beautiful print of the full alphabet in old script, with a couple of extra symbols used for etcetera, from [Nine Arrow](https://www.ninearrow.com/), who has also [fallen down this rabbit hole](https://www.ninearrow.com/blog/clo-gaelach-project).

While my parents’ primary association with it are literally being rapped on the knuckles for getting it wrong, for me it’s the type of official signage on old buildings and at historical sites - it’s antiquity and heritage. (For more examples, check out the [CLÓSCAPE Project](https://nicolevolmering.ie/closcape/), dedicated to cataloging use around Dublin.)

![Engraving over a school in Ireland in old Irish script](https://www.djmurphy.net/cros-an-araldaig.jpg)

The “old script” was created when medieval monks evolved the latin script to encode the *sound* of Irish. It uses a dot over a consonant to indicate it should soften according to grammatical rules.

Few printers had insular typesets and typewriters were rare and difficult to use, with modifier dots rather than distinct characters. Applying them required typing the letter, then backspace, then typing the dot - not very ergonomic. This made producing print slow and expensive.

![A typewriter with Gaelic characters](https://www.djmurphy.net/gaelic_typewriter.jpg)

A Gaelic typewriter. (Image via [Galway City Museum](https://www.galwaycitymuseum.ie/))

The solution was to switch to using a pure latin character set, with the dot being replaced with a “h” after the letter. This is why you get Irish names like “Sadhbh” that improbably rhyme with “five”. It’s much less phonetic because you have to look at the preceeding letter to understand what the “h” modifier is going to do, and you have to process letters in groups to understand what sound they make.

I’m a bit wistful that something so distinctive and beautiful and endemic has been lost, and (not having to learn to write another character set) to my mind the old script’s approach of preserving the majority word shape while still capturing the phonetic content is a better writing system. I have been thinking about how use modern tools to add the old back into modern media gracefully. There have been typographers making Gaelic fonts for a long time - [gaelchlo.com](https://www.gaelchlo.com) is the central repository of these, but we also need to perform some letter substitutions to really achieve the old script.

From an accessibility and data portability perspective the ship has sailed. While Google Translate can (impressively and improbably) handle Cló Gaelach, other Irish language reference sites of record like [teanglann.ie](https://teanglann.ie) or [abair.ie](https://abair.ie) cannot. There is a “ga” language tag you can use to indicate to screen readers that text is in Irish, but I wouldn’t expect Irish text in Cló Gaelach to work with the Irish language NVDA screenreader plugin (I don’t have a copy of Windows to check though). So, while we might like to visually replace the “aitches” to achieve the look of the old script, we should preserve the original text.

Luckily there is a feature in OTF typefaces called [“discretionary ligatures”](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/opentype-font-features#ligatures) - these allow us to modify a script font to define optional ligatures that can be selected on or off, that won’t mess with the original text. It seemed like adding some ligatures to the relevant consonant-séimhiú pairs might work.

I gave it a try - I opened my favorite Cló Gaelach font [Úrchló GC](https://www.gaelchlo.com/urgc.html) using [Font Forge](https://fontforge.org) and:

1. Added a discretionary ligature table

![FontForge screenshot of adding a discretionary ligature table](https://www.djmurphy.net/ff_1.png)

2. Added a subtable for substitutions - replace all the relevant consonant + h with the dotted constant. (And for flair replace the latin etcetera (&) with the [Tironian et](https://en.wiktionary.org/wiki/%E2%81%8A) - a piece of shorthand credited to [Tiro](https://en.wikipedia.org/wiki/Marcus_Tullius_Tiro), scribe of [Cicero](https://en.wikipedia.org/wiki/Cicero), and still in use in Irish today.)

![FontForge screenshot of adding a subtable for substitutions](https://www.djmurphy.net/ff_2.png)

3. Because this is discretionary and so off by default, enable it by setting the font-variant-ligatures:

```
gaeilge {
  font-family: "urgc", sans-serif;
  font-variant-ligatures: discretionary-ligatures;
}
```

… and  feidhmíonn sé!   feidhmíonn sé!  - it works!
This approach means that while the user sees the ligatures, the underlying text is still preserved for copy-paste and presentation to screen readers.

Ok, but you might say whatever about sprinkling Irish on a website not really about the Irish language, including it in an ancient albeit beautiful script that’s niche even in Ireland might be a little self-indulgent. To which I say it might [resonate](https://resonantcomputing.org/) with a few people, and it’s fun and you’ve already agreed it’s beautiful but ok, I hear you. To preserve the flow for non-Irish readers, I’m playing with repurposing the HTML `<ruby>` element. These are ordinarily used to [give pronunciation hints for east-Asian scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby), but for right now this seems like an interesing way to preserve reading flow for the  cúpla focail  (meaning: couple of words)   cúpla focail (
couple of words
)  of Irish I’m ever liable to use.

Hmm, but what about screen readers? Well, trying to replicate the visual approach, which is to give priority to the gaelic script over the translation, I decided to have screenreaders speak “[the Irish text] meaning: [translation]”. It turns out the `<ruby>` element does not have defined screenreader behavior yet, and wanting to provide both `lang="ga"` for the gaelic text and `lang="en"` for the translation out of principle was a bit tricky, you can see (and judge) my approach below.
I’m using Astro as a blogging framework, it allows me to define components that I can use like HTML elements. My Gaeilge.astro component looks like

```
<!-- Gaeilge.astro -->
---
interface Props {
  translation?: string;
}

const { translation } = Astro.props;
const slotContent = (await Astro.slots.render("default")).trim();
const plainText = slotContent.replace(/<[^>]*>/g, "");
---

<span class="sr-only">
  <span lang="ga">{plainText}</span>
  {translation && <span lang="en"> (meaning: {translation})</span>}
</span>
<ruby aria-hidden="true">
  <span class="gaeilge-text" lang="ga" set:html={slotContent} />
  {
    translation && (
      <rp>(</rp>
      <rt>{translation}</rt>
      <rp>)</rp>
    )
  }
</ruby>

<style>
  ruby > rt {
    text-align: left;
    font-weight: lighter;
    font-size: 0.75em;
  }
  .gaeilge-text {
    font-family: "urgc", sans-serif;
    font-variant-ligatures: discretionary-ligatures;
    font-feature-settings: "ss01" 1;
  }
</style>
```

I include this in my `[..slug].astro` file:

```
<!-- [..slug].astro -->
---
import Gaeilge from '../../components/Gaeilge.astro';
... stuff ...
<BlogPost {...post.data}>
  <Content components={{ Gaeilge }} />
</BlogPost>
```

This allows me to write

```
<Gaeilge translation="welcome">Failté romhait</Gaeilge>
```

in my blog markdown on any .mdx blog post, and to produce somethine like:

```
<span class="sr-only">
  <span lang="ga">Fáilte romhait</span>
  <span lang="en"> (meaning: Welcome)</span>
</span>
<ruby>
  <span lang="ga">Fáilte romhait</span>
  <rp>(</rp><rt>Welcome</rt><rp>)</rp>
</ruby>
```

on the actual page, resulting in the english-over-script look that’s screenreader-friendly:  Failté romhait.  (meaning: welcome)   Failté romhait. (
welcome
)

As an aside I wanted to try blogging again to get back to the spirit of the “old internet” from pre-social media. I don’t know why this topic is where I started, but in digging into the Cló Gaelach I discovered and enjoyed a number of other blogs: [a talented graphic designer exploring the type](https://www.ninearrow.com/blog/clo-gaelach-project), interesting material about [Gaelic](https://johnjburnslibrary.wordpress.com/2022/09/19/flann-obrien-and-the-irish-typewriter/) [typewriters](https://www.evertype.com/celtscript/type-keys.html),  [scholarly material](https://www.libfocus.com/2020/04/cataloguing-older-irish-language.html) on the [origins of the typeface](https://www.dbnl.org/tekst/_gul005199001_01/_gul005199001_01_0004.php) as a [tool for religious persuasion](https://www.dib.ie/biography/kearney-john-o-cearnaigh-sean-a4413), and its [connection with Leuven](https://www.ustc.ac.uk/news/defining-the-early-modern-irish-language-micheal-o-cleirighs-focloir-no-sanasan). Almost none of this information is surfaced by searches for Google Books or Scholar, nor is it on Wikipedia. Most of it is hearteningly from the 2020s. *This* is the web I want!

As a bonus I got to play with some accessibility and UX problems and now have a reusable element that allows me to sprinkle the site with some idiosyncratic vernacular design elements that, for me, capture a little of wild-west spirit of the Geocities days, but with the more responsible accessibility and data portability considerations of the modern mature web.