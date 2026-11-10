---
title: "I believe there are entire companies right now under AI psychosis"
url: https://twitter.com/mitchellh/status/2055380239711457578
clipped: 2026-06-17 01:02:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [I believe there are entire companies right now under AI psychosis](https://twitter.com/mitchellh/status/2055380239711457578)

## Digest Summary
The scraped page provides no substantive title or content. It begins with a generic error notice—“Something went wrong, but don’t fret — let’s give it another shot”—indicating a failed load or processing issue and suggesting a retry. Following the message, a section labeled “Images and Visual Content” appears, containing a single entry: “Image 1” whose alt text consists solely of a warning emoji (⚠️). No additional descriptive text, data, links, or contextual information accompanies the image placeholder. The overall structure consists only of the error prompt and an empty visual‑content placeholder, offering no further technical details, narrative, or actionable content. Consequently, the page’s scraped material is limited to the error message and the minimal alt‑text indicator.

## Discussion Summary
Comments express a mixed but cautious view of AI‑assisted development. Many acknowledge AI’s usefulness for pattern‑matching tasks such as code generation, scripting, and defect detection, yet warn that over‑reliance can erode critical thinking, introduce generic or low‑quality solutions, and create opaque, hard‑to‑maintain systems. Concerns include security risks, potential for “AI psychosis” where users accept AI output uncritically, and the impact on engineering standards and responsibility. Opinions converge on the need for human oversight, balanced adoption, and new design principles to mitigate long‑term instability.

---

## Full Article

I strongly believe there are entire companies right now under heavy AI psychosis and its impossible to have rational conversations about it with them. I can't name any specific people because they include personal friends I deeply respect, but I worry about how this plays out.
I lived through the great MTBF vs MTTR (mean-time-between-failure vs. mean-time-to-recovery) reckoning of infrastructure during the transition to cloud and cloud automation. All those arguments are rearing their ugly heads again but now its... the whole software development industry (maybe the whole world, really).
It's frightening, because the psychosis folks operate under an almost absolute "MTTR is all you need" mentality: "its fine to ship bugs because the agents will fix them so quickly and at a scale humans can't do!" We learned in infrastructure that MTTR is great but you can't yeet resilient systems entirely.
The main issue is I don't even know how to bring this up to people I know personally, because bringing this topic up leads to immediately dismissals like "no no, it has full test coverage" or "bug reports are going down" or something, which just don't paint the whole picture.
We already learned this lesson once in infrastructure: you can automate yourself into a very resilient catastrophe machine. Systems can appear healthy by local metrics while globally becoming incomprehensible. Bug reports can go down while latent risk explodes. Test coverage can rise while semantic understanding falls. Changes happens so fast that nobody notices the underlying architecture decaying.
I worry.