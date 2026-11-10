---
title: "The UK paid £4.1M for a bookmarks site"
url: https://mahadk.com/posts/ai-skills-hub
clipped: 2026-06-17 01:51:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The UK paid £4.1M for a bookmarks site](https://mahadk.com/posts/ai-skills-hub)

## Digest Summary
The UK government’s AI Skills Hub, contracted to PwC for £4.1 million, serves as a portal that primarily links to external training resources such as Salesforce Trailhead rather than hosting original content. The site has been noted for several technical shortcomings: a non‑intuitive user interface, a small “Enroll Now” button that can be missed, and broken or inaccessible navigation elements (e.g., a “Skills & Training Gap Analysis” link that is unavailable to the public). Accessibility testing indicates the platform does not fully comply with required standards, leading to usability issues for all users. Content inaccuracies include a course on “AI and intellectual property” that references “fair use,” a concept applicable only in US law, whereas UK law uses the more restrictive “fair dealing.” Overall, the platform’s design and content delivery have been criticized for inefficiency and for providing limited value relative to the contract cost.

## Discussion Summary
The comments describe the contract as unusually expensive and attribute the cost to rigid government procurement rules, risk‑averse officials, and reliance on large consulting firms that command high fees. Many express frustration that the work could likely be produced far cheaper by in‑house teams or smaller providers, and they suspect political favoritism or kickbacks influencing the selection. Comparisons to other public‑sector projects highlight perceived waste, though a minority note that the expenditure might be justified if it delivers wide‑scale upskilling. Overall sentiment is critical of the price and procurement process.

---

## Full Article

The UK Government recently unveiled its [‘AI Skills Hub’](https://www.gov.uk/government/news/free-ai-training-for-all-as-government-and-industry-programme-expands-to-provide-10-million-workers-with-key-ai-skills-by-2030), which wants to provide 10 million workers with AI skills by 2030. The main site was delivered by PwC for the low, low price of.. [£4.1 million (~$5,657,000).](https://www.find-tender.service.gov.uk/Notice/001337-2025)

![Image of the procurement contract](https://cdn.mahadk.com/s/v3/fa4d19cdf4b054d4_image.png)

It is *not* good. Like, at all - the UI is insanely bad and it’s clear that this was just a vibecoded site (to be fair, this is the *AI* Skills Hub, but c’mon, where is the pride in your work? I would be ashamed to even release this as a prototype!)

![Image of the AI Skills Hub](https://cdn.mahadk.com/s/v3/fa0761d06de95286_image.png)

PwC didn’t even write any of the course content! The only thing the Skills Hub does is link out to external pages, like Salesforce’s free Trailhead learning platform:

![Screenshot of Salesforce's Trailhead learning platform](https://cdn.mahadk.com/s/v3/9aed674092d49d24_image.png)

Note that I’m fairly certain this course already existed before the contract was even awarded, so all the site does is.. link out to other sites?

PwC itself also admits that the site does not properly meet accessibility standards:

![Accessibility policy](https://cdn.mahadk.com/s/v3/f346a09eb011342a_image.png)

Even for those without a disability, the lack of here in this regard means that the site can be very confusing and buggy as a result.

Incorrect laws
--------------

The site has a course on “AI and intellectual property”. One thing it mentions is [fair use](https://en.wikipedia.org/wiki/Fair_use):

![Fair use](https://cdn.mahadk.com/s/v3/1e8f7dc501128b15_image.png)

[(credits for the photo)](https://x.com/ednewtonrex/status/2016443895505203379)

Except that *fair use is not a thing in the UK* - that’s a US concept! The UK uses what’s known as “fair dealing”, which is more restrictive than fair use, so the details here are plain wrong.

Lack of care, lack of craft
---------------------------

The interface for this website has also not been clearly thought out - one glaring example is the process of actually enrolling in a course.

On the course page, the “Enroll Now” button is *tiny*, and if you don’t see it and try scrolling down to the bottom, you will find yourself nothing but a comment section!

![Image of the course page](https://cdn.mahadk.com/s/v3/61dc1d957dc892f8_image.png)

Then you have other bugs too, like the “Skills & Training Gap Analysis” - which is linked at the top of the site! - apparently being closed off to the public for no reason:

![Image of the S&T Gap Analysis page](https://cdn.mahadk.com/s/v3/f03c15b9365950ff_image.png)

---

To be honest, seeing this made me angry.

I’m angry at the sheer *wastefulness* of the UK Government here. Our public services are collapsing - while £4 million is admittedly chump change for the UK government, there are real people behind these numbers - families waiting months for NHS appointments, children in crumbling schools, vulnerable people not getting the care they need. The waste feels particularly galling when you realise that almost no one will actually use this site!

I’m also angry that the small webdev businesses we have here in the UK were left out of this - for less than 5% of the cost, we’d have a *better* website and help out small businesses who actually care about their work, instead of handing the project to a multinational company that made nearly $60 billion in revenue in a year and has zero qualms about ripping off the British taxpayer.

Do better.

---

A reader sent me another [“AI Delivery”](https://delivery.ai.gov.uk/) site from the government, that was also AI generated. This one is admittedly a fair bit better — for one thing, we didn’t pay £4.1 million for it! — but have some pride in your work, for goodness sake!