---
title: "Has_not_been_viewed_much"
url: https://iamwillwang.com/notes/has-not-been-viewed-much/
clipped: 2026-08-31 12:22:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Has_not_been_viewed_much](https://iamwillwang.com/notes/has-not-been-viewed-much/)

## Digest Summary
The Art Institute of Chicago’s public API defines a boolean field named **has_not_been_viewed_much** for each artwork record. According to the source code, the field is set to true when the artwork has been viewed fewer than 200 times on the museum’s website since January 1 2010; otherwise it is false. This metric provides a simple indicator of low online engagement for individual pieces, allowing developers or analysts to filter or flag artworks that receive minimal visitor attention. No additional criteria or context for the low view count is supplied beyond the numeric threshold.

---

## Full Article

[â Home](https://iamwillwang.com/)   

The
[Art Institute of Chicago's API](https://api.artic.edu/docs/) includes a
 `has_not_been_viewed_much`  [field](https://api.artic.edu/docs/#artworks-2) on artwork. It's a boolean that describes whether an art piece hasn't
        been visited on their website very much.
 

More specifically, per the
[source code](https://github.com/art-institute-of-chicago/data-aggregator/blob/1eeb87ce21f51f27034eafabbd1eeae7a70aa2c2/app/Transformers/Outbound/Collections/Artwork.php#L112-L133),  `has_not_been_viewed_much`  means the art piece has been viewed
        fewer than 200 times on the website since January 1, 2010.
 

Of course, that still begs the question: what are these artworks? Why
        aren't they being viewed? I can't answer the latter, but, if you have a
        moment for the former, please take some time to browse.
