---
title: "News publishers limit Internet Archive access due to AI scraping concerns"
url: https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/
clipped: 2026-06-17 01:45:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [News publishers limit Internet Archive access due to AI scraping concerns](https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/)

## Digest Summary
News publishers are restricting the Internet Archive (IA) to prevent AI companies from scraping their content. The Guardian has excluded its article pages from IA’s APIs and Wayback Machine URL listings, while still allowing regional homepages. The Financial Times blocks all bots, including those from OpenAI, Anthropic, Perplexity and IA; only unpaywalled stories appear in the Wayback Machine. The New York Times “hard‑blocks” the IA crawler via robots.txt, and Reddit has limited IA’s access to Reddit data. IA’s robots.txt currently welcomes crawlers, though it uses internal rate‑limiting and Cloudflare protection. Analyses show the Wayback Machine was used in Google’s C4 dataset and Meta’s Llama training. A survey of 1,167 news sites found 241 explicitly disallow at least one IA bot—87 % of these are USA Today (Gannett) outlets, with additional blocks by Le Monde sites. Most of the same sites also block Common Crawl, OpenAI, and Google AI bots, reflecting publishers’ concern that IA’s bulk access can serve as a backdoor for unauthorized AI training.

## Discussion Summary
Comments express strong concern that news publishers are blocking archival services to protect revenue and prevent AI training use, which many see as threatening the public historical record. There is broad agreement that independent, reliable preservation mechanisms are needed, with suggestions ranging from open‑source self‑hosted tools to government‑backed search archives and crowd‑sourced browser extensions. Some participants argue that archival restrictions mainly serve commercial interests and risk knowledge erosion, while a minority view the loss of content as acceptable or even beneficial. Overall, the discussion emphasizes the tension between monetization, AI scraping, and long‑term access to information.

---

## Full Article

As part of its mission to preserve the web, the Internet Archive operates crawlers that capture webpage snapshots. Many of these snapshots are accessible through its public-facing tool, the [Wayback Machine](https://web.archive.org/). But as AI bots scavenge the web for training data to feed their models, the Internet Archive’s commitment to free information access has turned its digital library into a potential liability for some news publishers.

When The Guardian took a look at who was trying to extract its content, access logs revealed that the Internet Archive was a frequent crawler, said [Robert Hahn](https://www.linkedin.com/in/robert-hahn-08b45719/), head of business affairs and licensing. The publisher decided to limit the Internet Archive’s access to published articles, minimizing the chance that AI companies might scrape its content via the nonprofit’s repository of over one trillion webpage snapshots.

Specifically, Hahn said The Guardian has taken steps to exclude itself from the Internet Archive’s APIs and filter out its article pages from the Wayback Machine’s URLs interface. The Guardian’s regional homepages, topic pages, and other landing pages will continue to appear in the Wayback Machine.

In particular, Hahn expressed concern about the [Internet Archive’s APIs](https://archive.org/help/wayback_api.php).

“A lot of these AI businesses are looking for readily available, structured databases of content,” he said. “The Internet Archive’s API would have been an obvious place to plug their own machines into and suck out the IP.” (He admits the Wayback Machine itself is “less risky,” since the data is not as well-structured.)

As news publishers try to safeguard their contents from AI companies, the Internet Archive is also getting caught in the crosshairs. The Financial Times, for example, blocks any bot that tries to scrape its paywalled content, including bots from OpenAI, Anthropic, Perplexity, and the Internet Archive. The majority of FT stories are paywalled, according to director of global public policy and platform strategy [Matt Rogerson](https://www.linkedin.com/in/mattrogerson/). As a result, usually only unpaywalled FT stories appear in the Wayback Machine because those are meant to be available to the wider public anyway.

“Common Crawl and Internet Archive are widely considered to be the ‘good guys’ and are used by ‘the bad guys’ like OpenAI,” [said Michael Nelson](https://www.linkedin.com/in/michaellloydnelson/), a computer scientist and professor at Old Dominion University. “In everyone’s aversion to not be controlled by LLMs, I think the good guys are collateral damage.”

The Guardian hasn’t documented specific instances of its webpages being scraped by AI companies via the Wayback Machine. Instead, it’s taking these measures proactively and is working directly with the Internet Archive to implement the changes. Hahn says the organization has been receptive to The Guardian’s concerns.

The outlet stopped short of an all-out block on the Internet Archive’s crawlers, Hahn said, because it supports the nonprofit’s mission to democratize information, though that position remains under review as part of its routine bot management.

“[The decision] was much more about compliance and a backdoor threat to our content,” he said.

When asked about The Guardian’s decision, Internet Archive founder Brewster Kahle said that “if publishers limit libraries, like the Internet Archive, then the public will have less access to the historical record.” It’s a prospect, he implied, that could undercut the organization’s work countering “[information disorder](https://firstdraftnews.org/training/information-disorder/).”

The Guardian isn’t alone in reevaluating its relationship to the Internet Archive. The New York Times confirmed to Nieman Lab that it’s actively “hard blocking” the Internet Archive’s crawlers. At the [end of 2025](https://web.archive.org/web/20251223163226/http://nytimes.com/robots.txt), the Times also added one of those crawlers — archive.org\_bot — to its [robots.txt file](https://www.nytimes.com/robots.txt), disallowing access to its content.

“We believe in the value of The New York Times’s human-led journalism and always want to ensure that our IP is being accessed and used lawfully,” said a Times spokesperson. “We are blocking the Internet Archive’s bot from accessing the Times because the Wayback Machine provides unfettered access to Times content — including by AI companies — without authorization.”

Last August, [Reddit announced](https://www.theverge.com/news/757538/reddit-internet-archive-wayback-machine-block-limit) that it would block the Internet Archive, whose digital libraries include countless archived Reddit forums, comments sections, and profiles. This content is not unlike what Reddit now licenses to [Google as AI training data for tens of millions of dollars](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php).

“[The] Internet Archive provides a service to the open web, but we’ve been made aware of instances where AI companies violate platform policies, including ours, and scrape data from the Wayback Machine,” a Reddit spokesperson [told The Verge](https://www.theverge.com/news/757538/reddit-internet-archive-wayback-machine-block-limit) at the time. “Until they’re able to defend their site and comply with platform policies…we’re limiting some of their access to Reddit data to protect redditors.”

Kahle has also alluded to steps the Internet Archive is taking to restrict bulk access to its libraries. In a [Mastodon post](https://mastodon.archive.org/@brewsterkahle/115368911896794707) last fall, he wrote that “there are many collections that are available to users but not for bulk downloading. We use internal rate-limiting systems, filtering mechanisms, and network security services such as Cloudflare.”

Currently, however, the Internet Archive does not disallow any specific crawlers through its robots.txt file, including those of major AI companies. As of January 12, the robots.txt file for [archive.org](http://archive.org) read: “​​Welcome to the Archive! Please crawl our files. We appreciate it if you can crawl responsibly. Stay open!” Shortly after we inquired about this language, it was changed. The file now reads, simply, “Welcome to the Internet Archive!”

There is evidence that the Wayback Machine, generally speaking, has been used to train LLMs in the past. An [analysis of Google’s C4 dataset](https://www.washingtonpost.com/technology/interactive/2023/ai-chatbot-learning/) by the Washington Post in 2023 showed that the Internet Archive was among millions of websites in the training data used to build Google’s T5 model and Meta’s Llama models. Out of the 15 million domains in the C4 dataset, the domain for the Wayback Machine ([web.archive.org](http://web.archive.org)) was ranked as the 187th most present.

In May 2023, the Internet Archive went

[offline](https://blog.archive.org/2023/05/29/let-us-serve-you-but-dont-bring-us-down/)

temporarily after an AI company caused a server overload, Wayback Machine director

[Mark Graham](https://www.linkedin.com/in/markjohngraham/)

told Nieman Lab this past fall. The company sent tens of thousands of requests per second from virtual hosts on Amazon Web Services to extract text data from the nonprofit’s public domain archives. The Internet Archive blocked the hosts twice before putting out a public call to “respectfully” scrape its site.

“We got in contact with them. They ended up giving us a donation,” Graham said. “They ended up saying that they were sorry and they stopped doing it.”

“Those wanting to use our materials in bulk should start slowly, and ramp up,” [wrote Kahle in a blog post](https://blog.archive.org/2023/05/29/let-us-serve-you-but-dont-bring-us-down/) shortly after the incident. “Also, if you are starting a large project please contact us …we are here to help.”

The Guardian’s moves to limit the Internet Archive’s access made us wonder whether other news publishers were taking similar actions. We looked at publishers’ robots.txt pages as a way to measure potential concern over the Internet Archive’s crawling.

A website’s robots.txt page tells bots which parts of the site they can crawl, acting like a “[doorman](https://www.youtube.com/watch?v=qRlQ965pGCA&t=0),” telling visitors who is and isn’t allowed in the house and which parts are off limits. Robots.txt pages aren’t legally binding, so the companies running crawling bots aren’t obligated to comply with them, but they indicate where the Internet Archive is unwelcome.

For example, in addition to “hard blocking,” The New York Times and The Athletic include the archive.org\_bot in their robots.txt file, though they do not currently disallow other bots operated by the Internet Archive.

To explore this issue, Nieman Lab used journalist [Ben Welsh](https://www.linkedin.com/in/palewire/)‘s [database of 1,167 news websites](https://palewi.re/docs/news-homepages/openai-gptbot-robotstxt.html) as a starting point. As part of a larger side project to archive news sites’ homepages, Welsh runs crawlers that regularly scrape the robots.txt files of the outlets in his database. In late December, we downloaded a spreadsheet from Welsh’s site that displayed all the bots disallowed in the robots.txt files of those sites. We identified four bots that the AI user agent watchdog service [Dark Visitors](https://darkvisitors.com/) has associated with the Internet Archive. (The Internet Archive did not respond to requests to confirm its ownership of these bots.)

This data is not comprehensive, but exploratory. It does not represent global, industry-wide trends — 76% of sites in the Welsh’s publisher list are based in the U.S., for example — but instead begins to shed light on which publishers are less eager to have their content crawled by the Internet Archive.

In total, 241 news sites from nine countries explicitly disallow at least one out of the four Internet Archive crawling bots.

Most of those sites (87%) are owned by USA Today Co., the largest newspaper conglomerate in the United States formerly known as Gannett. (Gannett sites only make up 18% of Welsh’s original publishers list.) Each Gannett-owned outlet in our dataset disallows the same two bots: “archive.org\_bot” and “ia\_archiver-web.archive.org”. These bots were added to the robots.txt files of Gannett-owned publications in 2025.

Some Gannett sites have also taken stronger measures to guard their contents from Internet Archive crawlers. [URL searches for the Des Moines Register in the Wayback Machine](https://web.archive.org/web/20260000000000*/desmoinesregister.com) return a message that says, “Sorry. This URL has been excluded from the Wayback Machine.”

“USA Today Co. has consistently emphasized the importance of safeguarding our content and intellectual property,” a company spokesperson said via email. “Last year, we introduced new protocols to deter unauthorized data collection and scraping, redirecting such activity to a designated [page](https://www.usatoday.com/bot-detection) outlining our licensing requirements.”

Gannett declined to comment further on its relationship with the Internet Archive. In an October 2025 [earnings call](https://www.investing.com/news/transcripts/earnings-call-transcript-gannett-cos-q3-2025-digital-focus-amid-revenue-dip-93CH-4320263), CEO Mike Reed spoke to the company’s anti-scraping measures.

“In September alone, we blocked 75 million AI bots across our local and USA Today platforms, the vast majority of which were seeking to scrape our local content,” Reed said on that call. “About 70 million of those came from OpenAI.” ([Gannett signed a content licensing agreement with Perplexity in July 2025](https://www.usatodayco.com/pr/gannett-i-usa-today-network-and-perplexity-announce-strategic-ai-content-licensing-ageement/#:~:text=Gannett%20I%20USA%20TODAY%20Network,available%20for%20a%20broader%20audience.).)

About 93% (226 sites) of publishers in our dataset disallow two out of the four Internet Archive bots we identified. Three news sites in the sample disallow three Internet Archive crawlers: Le Huffington Post, Le Monde, and Le Monde in English, all of which are owned by Group Le Monde.

The news sites in our sample aren’t only targeting the Internet Archive. Out of the 241 sites that disallow at least one of the four Internet Archive bots in our sample, 240 sites disallow Common Crawl — another nonprofit internet preservation project that has been [more closely linked to commercial LLM development](https://www.wired.com/story/the-fight-against-ai-comes-to-a-foundational-data-set/). Of our sample, 231 sites all disallow bots operated by OpenAI, Google AI, and Common Crawl.

As we’ve [previously reported](https://www.niemanlab.org/2025/10/the-wayback-machines-snapshots-of-news-homepages-plummet-after-a-breakdown-in-archiving-projects/), the Internet Archive has taken on the Herculean task of preserving the internet, and many news organizations aren’t equipped to save their own work. In December, Poynter [announced](https://www.poynter.org/business-work/2025/poynter-ire-and-internet-archive-launch-todays-news-for-tomorrow-a-project-to-help-newsrooms-preserve-their-digital-footprint/) a joint initiative with the Internet Archive to train local news outlets on how to preserve their content. Archiving initiatives like this, while urgently needed, are few and far between. Since there is no federal mandate that requires internet content to be preserved, the Internet Archive is the most robust archiving initiative in the United States.

“The Internet Archive tends to be good citizens,” Hahn said. “It’s the law of unintended consequences: You do something for really good purposes, and it gets abused.”

Photo of Internet Archive homepage by

[SDF\_QWE](https://stock.adobe.com/images/houston-usa-july-7-2025-internet-archive-digital-library-and-web-preservation-website-with-logo-visible-on-computer-screen-in-web-browser/1571353025)

used under an Adobe Stock license.