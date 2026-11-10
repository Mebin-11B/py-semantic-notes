---
title: "Micropayments as a reality check for news sites"
url: https://blog.zgp.org/micropayments-as-a-reality-check-for-news-sites/
clipped: 2026-06-17 01:42:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Micropayments as a reality check for news sites](https://blog.zgp.org/micropayments-as-a-reality-check-for-news-sites/)

## Digest Summary
The article argues that fragmented, low‑revenue readership created by modern search, aggregators, and social sharing can be monetized through micropayments without harming subscription models. Micropayments would act as a revenue multiplier for advertising and provide publishers with verifiable, human‑audience data to counter bot‑inflated metrics, strengthening ad pricing. The author cites mobile‑game in‑app‑purchase models—real‑money conversion to virtual coins then to assets—as a cognitive technique that reduces perceived transaction cost and could be adapted for “pay‑by‑article” systems. Suggested implementations include issuing publisher‑specific coins as subscriber bonuses that can be transferred to non‑subscribers, seeding free coins to develop user habit, and allowing advertisers to distribute coins to customers. The piece warns that big‑tech attribution proposals risk centralizing data control, making independent audience metrics crucial. It also notes that reducing UI friction (e.g., consolidating consent dialogs, sign‑ins) would improve user experience and revenue potential.

## Discussion Summary
Comments show mixed enthusiasm for collective unlocking of articles but a prevailing skepticism that micropayments can sustain journalism. Many cite past failures, high friction, charge‑back costs and a “race to the bottom” that would undervalue quality reporting, favoring subscription bundles, patronage, grants or ad‑supported models instead. Some propose friction‑less wallet or blockchain solutions, yet most argue that social‑psychological barriers, technical overhead and the need for stable revenue make per‑article payments impractical, while subscription‑style or community‑funded approaches receive broader support.

---

## Full Article

In [Digital Media Lost the
Newsstand. Micropayments Are the Obvious Way Back](https://substack.com/home/post/p-188545610), Rick Bruner makes
the case for giving micropayments another try.

> The internet has dramatically diversified reading patterns. In the
> print era, readers subscribed to a small, fixed set of publications
> constrained by geography, distribution, and cost. Today, thanks to
> search, aggregators, and social sharing, readers routinely consume
> journalism from dozens of sources in the course of a month, including
> international and niche publications that were previously inaccessible.
> This has expanded total news consumption while weakening the economic
> link between any individual reader and any individual publisher. As a
> result, large portions of valuable readership generate little or no
> direct revenue. Micropayments convert that fragmented, currently
> untapped demand into incremental revenue without undermining the
> subscription base.

And—like any other payments directly from readers—micropayments would
be a multiplier for advertising, not an alternative.

> In a marketplace increasingly distorted by bot activity and opaque
> platform reporting, micropayment histories give publishers a powerful,
> independent way to demonstrate the authenticity and engagement of their
> audience, strengthening their position with advertisers and supporting
> premium pricing.

The 404 Media team explains the value of a known human
audience in [We
Need Your Email Address](https://www.404media.co/why-404-media-needs-your-email-address/). Meanwhile, [Subscription
revenue is growing at big news publishers even as traffic shrinks](https://digiday.com/media/in-graphic-detail-subscriptions-are-rising-at-big-news-publishers-even-as-traffic-shrinks/),
and that’s good news for legit sites—stuck in a struggle for ad budgets
with Big Tech oligarchs who want to bury us in [deepfakes,
extreme right wing bullshit](https://www.france24.com/en/france/20260203-paris-prosecutor-s-cybercrime-unit-raids-x-s-french-office) and AI slop [until
nobody trusts anybody](https://rjionline.org/news/the-traffic-and-revenue-crisis-for-news-is-a-symptom-of-big-techs-economy-wide-trust-collapse/).

Clay Shirky’s old [argument
against micropayments from 2003](http://shirky.com/essays/fame-vs-fortune-micropayments-and-free-content/), based on mental transaction costs,
doesn’t work so well any more. We know that micropayments can work
because mobile games are a thing. Shirky was probably right for the
micropayments of his day, but mobile game developers have figured out
how to get people to spend money on in-app-purchases (IAP), by turning
it into a two-step process.

* exchange real money for in-game coins—which feels like you’re not
  spending, just exchanging one currency for another.
* exchange in-game coins for an in-game asset—which feels like
  you’re not spending real money.

A brilliant cognitive trick that works in all kinds of games. Of
course, it doesn’t work on everybody. Figure [about
half of adults play mobile games, and about 80 percent of those make an
in-app purchase](https://kotaku.com/free-to-play-mtx-adults-82-video-games-usa-comscore-1851599100). But if the numbers for a pay by the article system
were similar, that would result in enough payment records to enable an
advertiser to tell a legit site—where somebody spends a coin every so
often—apart from an AI slop site.

So it doesn’t seem like micropayments are necessarily unworkable—and
with a powerful industry devoted to pushing misinformation and slop,
legit content needs every human attention metric it can get—but the
tricky part is how to introduce micropayments. Publishers look at their
subscriber metrics and realize that a lot of subscribers read few enough
stories that they would save a lot of money by canceling and using
micropayments instead.

It might be better to introduce publisher coins as a bonus feature
for subscribers, then let them leak out to non-subscribers. Instead of
saying that you get 5 gift articles per month, say a gift article is 20
coins and you get 100 free coins a month. Then open them up to more
uses. Another good lesson from how mobile games handle IAP coins is that
they hand out a few to non-buyers to help develop the habit. As part of
a direct sold ad deal, legit sites could issue a stack of coins to legit
advertisers, to hand out to customers, event visitors, and others.

Measuring marketing is already hard enough without a determined set
of adversaries in the picture. And with Big Tech under pressure to
obfuscate and enshittify every data flow, marketers will need to look
harder for trustworthy information. [Rick
Bruner again](https://www.linkedin.com/pulse/only-thing-ai-cant-do-advertising-measure-true-roi-rick-bruner-mkrze/):

> ROI for most advertisers is falling in inverse proportion to Big Tech
> valuations going up. Advertisers are steadily paying more for less ROI,
> and Google, Meta, and Amazon are laughing all the way to the
> blockchain.
>
> If there is one thing marketers have even heard about causation —
> which, of course, is the ultimate point of advertising, causing
> consumers to buy your product who wouldn’t have otherwise — it is that
> correlation is not causation. But AI, you see, is nothing but
> correlation. Very fast and very sophisticated statistical inference. The
> fact remains that to truly know what is having an effect, you need to
> conduct a randomized experiment: subjects assigned at random to a test
> or control group, presented with an intervention where they are either
> treated or not with the stimulus of interest (the ad), and measured
> against the outcome of interest (incremental sales).

The fog of marketing
--------------------

Unfortunately, legit sites are on a clock here. Right now the Big
Tech companies are [quietly
pushing an in-browser advertising attribution tracking system](https://blog.zgp.org/terminator-ending-for-privacy-sandbox/)
through the World Wide Web Consortium (W3C). It’s a complicated
proposal, technically, but it aims to centralize attribution measurement
at one chokepoint per browser vendor, so we can safely predict what the
attribution reports are going to look like. `beep, boop, the
optimal place to spend your ad money is . . . whatever Performance Max
(or other Big Tech ML) says is the right place to spend your ad
money`. If any attribution tracking reports start to come out
looking favorable to legit sites—and potentially costing Big Tech’s
misinfo and slop operations billions—then management will just demand
changes to code, policies, and personnel until the numbers come out [the
way they want](https://blog.zgp.org/performance-max-preserving-attribution/). (More: [Attribution
cartel update](https://blog.zgp.org/attribution-cartel-update/))

The survival of legit sites depends on how quickly marketers can
level up to stuff like [rickcentralcontrolcom/geo-rct-methodology](https://github.com/rickcentralcontrolcom/geo-rct-methodology?utm_source=chatgpt.com)
and not just [dump
money and customer data in to Big Tech and get conversions out](https://blog.zgp.org/reinventing-gosplan/). The
problem with marketing today isn’t that marketers have gotten “too
technical” and ignored the creative mystique or whatever—it’s that
marketers are so afraid to look “non-technical” by asking the hard
questions.

Anyway, just going back and reading this, Rick Bruner has scored a
content marketing win here. Start people off thinking about
micropayments, and that ends up leading to the question of how to figure
out which sites are for real, in the presence of so many gatekeepers
with an interest in pushing the wrong answers? (and [destroying
the legit economy and crushing democracy, but that’s another
story](https://www.thebulwark.com/p/you-can-do-something-to-hurt-the)).

Where micropayments systems can go from here
--------------------------------------------

Right now a lot of sites have a lot of, let’s just say malarkey to
get through before seeing the actual page.

* “consent” dialogs (which don’t get real [consent](https://w3ctag.github.io/privacy-principles/#consent-principles)
  anyway, as [Prof. Daniel
  Solove explains](https://www.linkedin.com/pulse/why-consent-broken-privacy-ai-daniel-solove-1ogpc/))
* Email newsletter signups
* Prompts to allow notifications
* Sign in with (company name here)

A micropayment platform that can either eliminate those or act as a
front end for them, to consolidate on zero or one roadblock to get
through before reading, would be a user experience (and revenue) win.
Piling another thing to click onto already long-suffering users is not
the way to get people back to the web. **More:** [time to sharpen
your pencils, people](https://blog.zgp.org/sharpen-your-pencils-people/)

More on diversifying income streams
-----------------------------------

A copyright-like “oracle right” would give news publishers the
exclusive right to license their content for purposes of resolving a
prediction market. **More:** [Pay the oracle.](https://blog.zgp.org/pay-the-oracle/)

Bonus links
-----------

[What’s
next for Chinese open-source AI](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/) by Caiwei Chen. "The adoption of
Chinese models is picking up in Silicon Valley, too. Martin Casado, a
general partner at Andreessen Horowitz, has put a number on it: Among
startups pitching with open-source stacks, there’s about an 80% chance
they’re running on Chinese open models…." (related: [Please
Don’t Say Mean Things about the AI That I Just Invested a Billion
Dollars In](https://www.mcsweeneys.net/articles/please-dont-say-mean-things-about-the-ai-that-i-just-invested-a-billion-dollars-in), [generative ai
antimoats](https://blog.zgp.org/generative-ai-antimoats/))

[Why
the World Is Drawing a Line on Social Media for Kids](https://www.afterbabel.com/p/why-the-world-is-drawing-a-line-on) by Jon Haidt.
(As far as I know, teens in Australia can still make GitHub and
Wikipedia accounts. How did they manage to slice the definition of
“social media”?)

[EU
Parliament blocks AI features over cyber, privacy fears](https://www.politico.eu/article/eu-parliament-blocks-ai-features-over-cyber-privacy-fears/) by Ellen
O’Regan and Max Griera. "The latest move to switch off AI tools
concerns built-in features like writing and summarizing assistants,
enhanced virtual assistants and webpage summaries in both tablets and
phones, an EU official said, granted anonymity to disclose details of
the security policy."

[Journalism
Is Dead. Long Live Journalism](https://www.meditationsinanemergency.com/journalism-is-dead-long-live-journalism/) by Rebecca Solnit. "Silicon Valley
created and abets this chaos, both by undermining the financial basis
for traditional news by siphoning away its advertising revenue and
audiences, and by creating tools and platforms where, over and over,
from Facebook to Substack, the bosses insist they are defending free
speech by not filtering out dangerous disinformation and hate
speech."

[EPIC
Crafts 2026 Model Bill to Bolster Age-Appropriate Design Code Laws](https://pro.stateaffairs.com/us/disruption/model-bill-to-protect-kids-online-aims-to-withstand-big-tech-challenges)
by Austin Jenkins. "EPIC, which filed an amicus brief in the
California case, said its model bill was "carefully designed" to
avoid First Amendment issues and was built off of Vermont’s law, which
was passed last year after input from EPIC staff."

[People
who use chatbots for news consider them unbiased and “good enough,” new
study finds | Nieman Journalism Lab](https://www.niemanlab.org/2026/01/people-who-use-chatbots-for-news-consider-them-unbiased-and-good-enough-new-study-finds/) by Andrew Deck. "The study
found that right now even regular chatbot users aren’t relying on them
alone for news. Most interviewees continued to access traditional news
sources, while using chatbots to supplement these habits."