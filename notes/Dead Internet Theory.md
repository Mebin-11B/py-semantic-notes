---
title: "Dead Internet Theory"
url: https://kudmitry.com/articles/dead-internet-theory/
clipped: 2026-06-17 01:56:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Dead Internet Theory](https://kudmitry.com/articles/dead-internet-theory/)

## Digest Summary
The author reflects on encounters on Hacker News where an open‑source project's code and its author’s comments appear AI‑generated—evidenced by unusual em‑dash usage, formulaic phrases (“you are absolutely right”), and templated offers. This prompted suspicion that the author, despite denying AI assistance, might be a bot. Extending this observation, the piece cites the “Dead Internet Theory,” which argues that since ~2016 most online interactions and content are produced by automated agents to drive sales or manipulate SEO. The writer contrasts this with early‑2000s experiences on IRC and phpBB forums, where human discourse was commonplace and learning was peer‑driven. Additional examples include AI‑altered corporate photos on LinkedIn and fabricated multimedia on platforms such as Facebook, X, and TikTok. The overall concern is that widespread, inexpensive AI tools enable mass generation of code, comments, and media, eroding authentic human contribution and threatening the internet’s role as a collaborative knowledge hub.

## Discussion Summary
The comments express widespread unease about the growing prevalence of AI‑generated and bot‑driven content, viewing it as a source of division, misinformation, and erosion of genuine discourse across platforms such as YouTube, Reddit, and Hacker News. Many anticipate a “dead‑internet” or “dark‑forest” scenario in which human interaction becomes isolated pockets amid overwhelming automated noise, while some suggest technical countermeasures and community curation as possible mitigations. There is also debate over terminology for social media and occasional lighter remarks about typographic conventions, but overall the tone is cautious and skeptical of AI’s impact on online ecosystems.

---

## Full Article

The other day I was browsing my one-and-only social network — which is not a social network, but I’m tired of arguing with people online about it — [HackerNews](https://news.ycombinator.com/).
It’s like this dark corner of the internet, where anonymous tech-enthusiasts, scientists, entrepreneurs, and internet-trolls, like to lurk.
I like HackerNews.
It helps me stay up-to-date about recent tech news (like [Cloudflare acquiring Astro](https://news.ycombinator.com/item?id=46646645) which makes me happy for the Astro team, but also sad and worried since I really like Astro, and big-tech has a tendency to ruin things); it *mostly* avoids politics; and it’s not a social network.

And, in the fashion of HackerNews, I stumbled upon someone sharing their open-source project.
It’s great to see people work on their projects and decide to show them to the world.
I think people underestimate the fear of actually shipping stuff, which involves sharing it with the world.

Upon glancing at the comment section, I started to see other anonymous participants questioning the validity of said open-source project in terms of how much of it was AI-generated.
I grabbed my popcorn, and started to follow this thread.
More accusations started to appear: the commit timeline does not make sense; the code has AI-generated comments; etc.
And at the same time, the author tried to reply to every comment claiming that they wrote this 100% without using AI.

I don’t mind people using AI to write code, even though I tried to resist it myself, until eventually succumbing to it.
But I think it’s fair to disclose the use of AI, especially in open-source software.
People on the internet are, mostly, anonymous, and it’s not always possible to verify the claims or expertise of particular individuals.

But as the amount of code is growing, considering that everyone is using AI to generate whatever-app they want, it’s impossible to verify every piece of code we are going to use.
So it’s fair to know, I think, if some project is AI generated and to what extent.
In the end, LLMs are just probabilistic next-token generators.
And while they are getting extremely good at most simple tasks, they have the potential to wreak havoc with harder problems or edge-cases (especially if there are no experienced engineers, with domain knowledge, to review the generated code).

As I was following this thread, I started to see a pattern: the comments of the author looked AI generated too:

* The use of em-dashes, which on most keyboard require a special key-combination that most people don’t know, and while in markdown two dashes will render as em-dash, this is not true of HackerNews (hence, you often see `--` in HackerNews comments, where the author is probably used to Markdown renderer turning it into em-dash)
* The notorious “you are absolutely right”, which no living human ever used before, at least not that I know of
* The other notorious “let me know if you want to [do that thing] or [explore this other thing]” at the end of the sentence

I was sitting there, refreshing the page, seeing the author being confronted with use of AI in both their code and their comments, while the author claiming to have not used AI at all.
Honestly, I was thinking I was going insane.
Am I wrong to suspect them?
What if people DO USE em-dashes in real life?
What if English is not their native language and in their native language it’s fine to use phrases like “you are absolutely right”?
Is this even a real person?
Are the people who are commenting real?

And then it hit me.
We have reached the [Dead Internet](https://en.wikipedia.org/wiki/Dead_Internet_theory).
The Dead Internet Theory claims that since around 2016 (a whooping 10 years already), the internet is mainly dead, i.e. most interactions are between bots, and most content is machine generated to either sell you stuff, or game the SEO game (in order to sell you stuff).

I’m ~~ashamed~~ proud to say that I spent a good portion of my teenage years on the internet, chatting and learning from real people who knew more than me.
Back in the early 2000s, there were barely bots on the internet.
The average non-tech human didn’t know anything about phpBB forums, and the weird people with pseudonyms who hanged-out in there.
I spent countless hours inside IRC channels, and on phpBB forums, learning things like network programming, OS-development, game-development, and of course web-development (which became my profession for almost two decades now).
I’m basically a graduate of the Internet University.
Back then, nobody had doubts that they were talking to a human-being.
Sure, you could think that you spoke to a hot girl, who in reality was a fat guy, but hey, at least they were real!

But today, I no longer know what is real.
I saw a picture on LinkedIn, from a real tech company, posting about their “office vibes” and their happy employees.
And then I went to the comment section, and sure enough this picture is AI generated (mangled text that does not make sense, weird hand artifacts).
It was posted by an employee of the company, it showed other employees of said company, and it was altered with AI to showcase a different reality.
Hell, maybe the people on the picture do not even exist!

And these are mild examples.
I don’t use social networks (and no, HackerNews is **not** a social network), but I hear horror stories about AI generated content on Facebook, Xitter, TikTok, ranging from photos of giants that built the pyramids in Egypt, all the way to short videos of pretty girls saying that the EU is bad for Poland.

I honestly got sad that day.
Hopeless, if I could say.
AI is easily available to the masses, which allow them to generate shitload of AI-slop.
People no longer need to write comments or code, they can just feed this to AI agents who will generate the next “you are absolutely right” masterpiece.

I like technology.
I like software engineering, and the concept of the internet where people could share knowledge and create communities.
Were there malicious actors back then on the internet?
For sure.
But what I am seeing today, makes me question whether the future we are headed to is a future where technology is useful anymore.
Or, rather, it’s a future where bots talk with bots, and human knowledge just gets recycled and repackaged into “10 step to fix your [daily problem] you are having” for the sake of selling you more stuff.