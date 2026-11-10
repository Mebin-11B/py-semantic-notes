---
title: "Stop using icons in data tables"
url: https://medium.com/@codythistleward/stop-using-icons-in-data-tables-7537af18ea0d
clipped: 2026-06-17 01:47:26
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Stop using icons in data tables](https://medium.com/@codythistleward/stop-using-icons-in-data-tables-7537af18ea0d)

## Digest Summary
None

## Discussion Summary
The comments express confusion over the article’s unclear stance, criticizing its lack of explicit examples and contradictory arguments about icons versus text. There is consensus that unlabeled icons increase cognitive load and that visible text labels improve usability, while many acknowledge that simple, well‑known icons can aid quick interpretation in dense tables. Additional points include frustration with subscription prompts, concerns about inconsistent icon idioms across applications, and practical issues such as unwanted HTML when copying formatted tables. Overall, the feedback favors clear labeling and consistent design conventions.

---

## Full Article

Why your table icons suck
-------------------------

Press enter or click to view image in full size

Theres an implicit ***cognitive translation*** that must take place with any non-universal icon pairing. A star icon could mean “AI” or “Recommendation” or “Rating” or any number of concepts.

This type of **non-universality** is useful when drawing attention but within an already crowded interactive system you end up with more cognitive load not less.

This is due, in part, to the inherent visual intricacy of an icon. This is known as “[***high spatial frequency***](https://en.wikipedia.org/wiki/Spatial_frequency)”.

Press enter or click to view image in full size

### Icon spatial frequency

* Icons are high spacial frequency: within a tiny 16px field you have lines, curves, junctions, that don’t follow a universal rhythm. This makes us perceive them as incredibly high value for foveal vision.
* Icons are objects, its a self-contained concept. In gestalt terms icons have a stronger [***figure-ground***](https://en.wikipedia.org/wiki/Figure%E2%80%93ground_(perception)) relationship because the brain sees them as a discrete object

Press enter or click to view image in full size

### Word spatial Frequency

* Text is lower spatial frequency: predictable and rhythmic, the brain recognizes the gestalt (the [***Bouma***](https://en.wikipedia.org/wiki/Bouma) shape)
* Text is a texture, they’re a recognizable pattern with relative low visual cost despite each character having relatively high spacial frequency to the word lock up.

The Artsy Stuff
---------------

I also should mention [***visual entropy***,](https://arxiv.org/pdf/1907.12879) the degree of randomness or disorder in a visual plane.

Visual Entropy and the Visualization of Uncertainty Nicolas S. Holliman

An icon has minute details (a tiny pencil, a curved arrow). When you shrink those details down you increase the ***visual energy***.

This concept pairs with Anne Treisman’s ***“***[***Feature Integration Theory***](https://en.wikipedia.org/wiki/Feature_integration_theory)***”*** basically the text “binds” almost instantly but icons require milliseconds of “binding” (a user can’t avoid this pull to bind and parse meaning).

So within a data table you end up with an incredibly high level of cumulative cognitive load.

The “Objectness” of an icon is its greatest strength in a vacuum, but its greatest weakness in a system.

Conclusion: Designing for the Fovea, Not the Ego
------------------------------------------------

When we choose an icon over text, we are making a trade: we trade the predictable, rhythmic “texture” of typography for a high-energy, high-spatial-frequency object that demands ***foveal attention***.

In a data table, this trade is a losing one. We are essentially littering our users’ path with tiny visual speed bumps, forcing a cycle of “Feature Integration” and “Semantic Translation” that exhausts the brain long before the data is actually processed.

As designers, we must resist the urge to “illustrate” our way out of complexity. We need to respect the **Bouma shape** of a word and the efficiency of a low-entropy interface. If we want to build truly efficient tools, we must stop designing for how we want the interface to *look* and start designing for how the human brain is wired to *see*. Sometimes, the most sophisticated visual solution isn’t an icon at all, it’s just a word.

**Sources & Links**

There isn’t a ton of graphically oriented theory writing within Cognitive Translation & Interpretation Sciences but this [analysis on medical imagery](https://lans-tts.uantwerpen.be/index.php/LANS-TTS/article/view/464/422) is a good example

For spatial frequency selectivity I recommend this article “[Bridging Psychophysics And Interface Design](https://oscarpubhouse.com/index.php/sdlijmef/article/view/26/24)”. Its damn dense but only 6 pages. Upload it to gemini and talk about it with a robot

For a visual interface evaluation using visual entropy i’ll point to [this assessment](https://pdf.sciencedirectassets.com/776616/1-s2.0-S2451958821X00024/1-s2.0-S2451958821000750/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLWVhc3QtMSJGMEQCIBVnZI80mkLc7leYXdpyNXrJk3YMSXY4Mm3RUpYxtathAiBhkuIu851lCVRUbT4QSdOlsuAnHKvxovF%2B7VdMZJC02CqzBQgwEAUaDDA1OTAwMzU0Njg2NSIMZu5Iz1yCgAhbxa18KpAFGYW9oeD5VwHczBwovBni64FooWza1R9%2FqMLxO4WyGq1sDW80%2FEjQ6bjnIPmJjKAUCKDN8TORCf8LcD6gqWcBsgUIlrxKkoGWxQOxYT3G44hpglWlPECVxPBetRvNpx3zZfzWb2lLvYNWB%2FfD158lSmArxpm3ZApFCyyTxd7t8I4ImMhPhpXqRFQGfRFyckO4EvYj6%2Fc4vWCh7o%2B1q8UfZKy49T91y6Sl3vcLNNMRioD0ElBZKuqRA7FTnJ7mMUceXSjUr5fIZJkNinCw0rQnQHBxsu2CmiZPGX8yfKiawwVUhu57%2BcGGmNTT9vby524PdJ0C5s%2BmAvBpUZvzzokDsDElZIojaaLe3LrhTSnKIQTdJOoMpvy6xRSGGVWEeufC4yjE5MpAv9zAA5pUICd0PPwp0nCMZ6n6lD5EWa6oe8F%2BAUrnjBrhU%2BGfUA5IjDuhR83QDjhB0zavFDxIyflXEJqSt4qAUt7wP3jqqoHmcMalywSKLBEywaq3aO3mEJJXBdphbpJHzovicTJwQ9IXm1OvWZXCXjVmxu3WKdBvc2v2Y16eKqQ%2BgytN7f5mNF8cQE1rky7%2Fra%2FpN5G%2B0YAC5VJwjIGmBLUjfZwhNNgF4idXvl6eTYKRCDQBaacRVUEKtWTF%2FplIQ6%2FIZxnzB%2B394GbCNwVLseujqT8%2Btqykzyg%2FflmDqCf%2BDRSfkbYOOrD1Lh7noLn0Uvbz96Qf3HvlCncdHRWQIfJ51AIJ5zB8%2Bgg9MGjR%2FTUIYudWRbHJafQQ2gDb0E3TGywt0DmmuJSiq%2F%2BQPoMaSun3LudnlDFhvaREI3FZBsQIESNy8CiTRREAf7fJZlqs6j2yO0wNAOk3scvXQPRtYoZK4CsEkrmwEVUw9N%2BSzAY6sgF493EXJ%2F8IQPfnEa33UVqNhqNOOuTs7Nrq9KCeWhaasSM8zaSBqofMcl%2FGPzS3KF45XzY4mGXf%2FilPkPEpOq9qFLW%2FkDn32eLRbU9Z%2F2F1XrCaa%2Bac6HaDo%2Fj0kZeNh1T0hpxzwKckLPQXtUjDwjdt5OLLrs42LUNHR7V%2BKtNp48UTUwEWk5qOg1dCs7lj9te1hmUQ2hndHzG8Q9V%2BMF1jaQQ56BFeavIZU080F2AXXW0j&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260205T153044Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY3G6YBGKP%2F20260205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8afef7e014cbe2a6bc7da79427ea1286c3d90beda5955945f886d009c94d4b52&hash=7f87f53381ba9cc11a6a378eb0acdef4722accc2d643aa3fb0f3664a53a362eb&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2451958821000750&tid=spdf-d39d9cef-1052-4e82-9247-b60166b03d6a&sid=491efca652eb944da709107015f203fe745cgxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=13125e02565354515756&rr=9c937365ff298fb5&cc=us) of air traffic controllers attempting to parse data via a continuous animation vs a stepped animation timeline.