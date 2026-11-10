---
title: "Quality non-fiction books are the antithesis of AI slop"
url: https://resobscura.substack.com/p/quality-non-fiction-books-are-the
clipped: 2026-08-31 12:26:33
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Quality non-fiction books are the antithesis of AI slop](https://resobscura.substack.com/p/quality-non-fiction-books-are-the)

## Full Article

# 

SubscribeSign in

# Quality non-fiction books are the antithesis of AI slop

### ...so I vibe-coded a tool for finding more of them

[Benjamin Breen](https://substack.com/@benjaminbreen)Jul 22, 20261052421Share

My first year of college, I had a work-study job which ended up being one of the most sneakily important intellectual experiences of my life. I was a lowly library shelver, assigned to the shelves labelled A through F section in the Library of Congress filing system: mostly works on religion, philosophy, sociology, and history. I say sneakily important because at first glance, shelving books in a library is super boring. What it amounts to, physically, is reading the label on a book, then placing it on the shelf where it belongs, repeated around a thousand times per shift. 

To avoid the tedium, I decided that I would also flip to a random page of every book I shelved and read a random sentence from it. Usually, I would stop there — running aground on some passage by a Hungarian classical music critic or a long-dead statistician of Bolivia’s agricultural development or any number of other things that failed to catch my interest.  But other times — like when I came across a book about [Hellenistic mystery cults](https://en.wikipedia.org/wiki/Mithraism), or The Education of Henry Adams, or [Are Clothes Modern?](https://medium.com/items/bernard-rudofskys-1944-exhibition-are-clothes-modern-1ba461789d24)— I would become so absorbed that I’d make my way through several pages before reluctantly depositing the book back where it belonged. 

And then, very often, I’d do the same with the books on either side of the one I’d liked.GR 830, v through w: the vampire/werewolf section of Columbia’s Butler Library. 

In retrospect, I learned more at this job than in any formal class I’ve ever taken, because it was a filtered form of auto-didacticism. The Library of Congress classification system — and the expert staff of an academic research library — had already sorted and filtered these texts. Not to mention the selection mechanism of the fact that that they had been checked out: had, in other words, found a lasting readership. Thus I was not seeing a truly haphazard sampling of books, but a targeted, organized, yet still interestingly randomized sampling of good books. 

Today, undergraduate students will invariably search on Google when asked to find a source, and the results are so much worse than the old method of going to, say, the GR 830 shelf of a research library (basically, “books that the Ghostbusters would read”) and just looking around. 

But honestly, even research libraries are not what they used to be. I am 41, and I feel like I’ve lived through the peak, and now the decline, of what libraries can be (I still love them, of course — in fact I’m currently writing this in the genealogy section of the Santa Cruz Public Library). The browsable open stacks of old are being replaced by Learning Labs and Digital Innovation Hubs and seating areas devoted mostly to socializing and snacking, and increasingly, the delightful, weird old books that I had the opportunity to browse as an undergrad are heading to dumpsters, replaced by e-editions.

But one thing that has remained consistently good throughout my life is the books themselves — non-fiction books, I mean. Even now, as readership of non-fiction declines amid competition from AI chatbots and podcasts, I feel like we are living through a golden age of the form that rarely gets recognized as such. 

### The Book Prize Index

Which is why I set aside some time this summer to create — or, rather, induce Claude Code to create — a free platform for searching in the long tail of high-quality non-fiction books. Quality is difficult to define, but it’s been my experience that books that win or achieve the short-list of the major non-fiction prizes are almost always noticeably good, so that was the litmus test I used. To get started, I counted up all the major non-fiction prizes in the English language. Then I had Claude and GPT-5.6 gather the lists of finalists and winners from various online sources (mostly Wikipedia) and arrange it into a searchable, sortable list. 

You can visit it [here](https://book-prize-index.vercel.app). 

(And before you wonder, yes this is actually free. I am paying for the hosting and the API costs entirely because I just want people to find and read more good non-fiction books.)

Though you could consider a paid subscription if you want to support this kind of thing:Subscribe

 There is really nothing “AI” about this aside from the tool that collected the data and coded it,[1](https://resobscura.substack.com/p/quality-non-fiction-books-are-the#footnote-1) and, crucially, semantic search, which for me is the most appealing of all current AI tools precisely because it offers a straightforward improvement for a workflow and habit that researchers already have: it makes text search work better. 

So for instance, you can search simple phrases like “modern France” or “social history” or the like, but you can also search things like “classic biographies that are surprisingly weird,” and an embedding model pulls from the 6,500 or so titles to surface some:I am planning on reading Edith Wharton, which doesn’t sound all that weird, but having read Lewis’s eclectic and brilliant biography of the James family, I think it’s a fair guess that it is. 

Sometimes the “choices” that the search makes are a bit baffling, but that is precisely why I like it: the idea is to recapture some of that feeling of a random walk through a well-tended garden that made my library shelving job so rewarding. [“Books for dads who like Pavement”](https://book-prize-index.vercel.app/books?q=books%20for%20dads%20who%20like%20Pavement&queryModel=gpt-5.4-nano)[“David Attenborough, but in book form”](https://book-prize-index.vercel.app/books?q=Joni%20Mitchell%2C%20but%20in%20book%20form&queryModel=gpt-5.4-nano)

I find it tends to be best for finding “books like.” For instance I found Stefan Zweig’s memoir of pre-war Vienna, [The World of Yesterday](https://en.wikipedia.org/wiki/The_World_of_Yesterday), to be deeply moving (even before I learned that he committed suicide, in Brazil in 1942, immediately after completing it). A search for a books like it using semantic search in the corpus immediately yields some titles that seem promising but which I’d never heard of before: 

Once I had gathered all this book-related data, it became a fun experiment to make some [data visualizations](https://book-prize-index.vercel.app/experiments) with it, including fun oddities like this display of roughly 5,000 books from the corpus arranged by color (it would be interesting to plot this by decade, to see whether the same [graying effect we see in cars](https://www.reddit.com/r/Infographics/comments/1p2p5x6/the_evolution_of_car_colours_from_colourful_to/) over the past few decades is active in book covers, too).[Link](https://book-prize-index.vercel.app/fun/chromatic-index).

More useful, perhaps (since I’ve never seen this plotted anywhere else), is [this chart](https://book-prize-index.vercel.app/experiments) and accompanying [ranking](https://book-prize-index.vercel.app/publishers?sort=all_activity) which allows you to explore which imprints and publishers have fared best when it comes to non-fiction book awards over the past century.

### Against the algorithmic filter

And this, in turn, got me thinking about the past and future of nonfiction as a cultural force. For instance, here is a chart of all the non-fiction book prizes which I sampled for this project. I was surprised to learn that even the august, renowned Pulitzer Prize for nonfiction was actually relatively recently instituted, beginning in 1962. 

Throughout the 70s, 80s and 90s, the number of prizes increases, until we reach a peak in 2014, and then, in 2020, the beginning of what may be a slow decline:

And yet, maybe not. What most struck me as I began using my own tool to find new books to read was how consistently good the long tail of non-fiction from the past few decades is. You can pick a book more or less at random from this list and end up with something extraordinary and original — not because it’s a hidden gem or forgotten, since obviously these books are on the list by virtue of having been celebrated and praised. But a book that won enormous praise in newspapers and among literary intelligentsia or scholars in the early 1990s, say — like, for instance, David Levering Lewis’s [acute biography of W.E.B. Du Bois](https://www.amazon.com/W-B-Bois-Biography-1868-1919/dp/0805026215/ref=pd_lpo_d_sccl_1/143-2013381-1211736?pd_rd_w=f3zgb&content-id=amzn1.sym.4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_p=4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_r=XRXCM2M2E1N5RR9H2ADM&pd_rd_wg=bwf2S&pd_rd_r=1d5a7928-e80b-4240-b31b-1de9a9de5d12&pd_rd_i=0805026215&psc=1), which I’m currently reading — is not exactly the sort of thing that Amazon is likely to recommend, as it’s out of print and currently at 1 million+ in the sales rankings. 

Yet there it is on the list, ranked near the top ten of all books because it won no less than four major prizes when it was published back in 1993. And I can personally attest that you can buy it used for ~$4 and it’s really good. [Link](https://book-prize-index.vercel.app/books/w-e-b-du-bois-biography-of-a-race-1868-1919-david-levering-lewis)

While writing this post, I got interested in the bigger question of when the golden age of non-fiction began and why. I suspect it has much to do with the rise of those old-school open stack research libraries, whose origins I wrote about here:

## 

[The open-stack library: a futuristic technology from the 18th century](https://resobscura.substack.com/p/the-open-stack-library-a-futuristic)[Benjamin Breen](https://substack.com/profile/408222-benjamin-breen)·November 8, 2023

“Where are all the books?” I asked the campus bookstore clerk earlier this year, as I was gearing up to teach in person for the first time since the COVID-19 shutdowns and my paternity leave.[Read full story](https://resobscura.substack.com/p/the-open-stack-library-a-futuristic)

It’s true that the basic blueprint of these institutions is an 18th and 19th century development — but the post-war era radically transformed the ways that libraries and archives produced new knowledge, for a range of reasons that I will dig into more in a future post. It seems to me that a surprising number of them are related to technological and social change: 

• The jet plane allowed writers and researchers to travel to multiple continents to research books — the sort of opportunity previously available only to the ultra-wealthy. 

• The erosion of restrictions around class, race, and gender made formerly elite spaces like rare book libraries more widely accessible, and the same process also opened up new questions and research leads (for instance, it is striking how rarely biographers before ~1965 or so dug into the sexuality of their subjects). 

• Proto-digital and early digital technologies like the Library of Congress classification system and the related MARC (machine-readable cataloguing) standard, developed in the late 1960s, made it much easier to sort and classify books. Crucially, they also made it easier to fact check sources and create high quality endnotes. 

• The advent of broadcast news, oddball TV interview shows ([Dick Cavett!](https://www.youtube.com/watch?v=gl0Yh0aXNdQ)), and the book-to-Hollywood pipeline created new incentives for authors and new platforms for making their work visible.

• Word processors and early computers? I’m still unsure whether these appreciably altered the quality of non-fiction writing, but I think it’s possible. Certainly (moving into the 2000s) Wikipedia and Google Books/Hathi Trust have been enormously helpful for me and others in my generation. 

My own entirely subjective opinion, based on a whole lot of skimming in a whole lot of library books, is that non-fiction writing quality noticeably improved across the whole twentieth century and probably reached a peak around the 1980s to early 2000s. Whether it is now declining is, again, a topic for another post — though I’d be curious to hear what you think, dear reader, both about this question and about the Book Prize Index. Subscribe

[Share](https://resobscura.substack.com/p/quality-non-fiction-books-are-the?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## Weekly links

• [The making of the Jurassic Park computers](https://fabiensanglard.net/jurrasic_park_computers/index.html).

• “Mill’s life has as much to teach here as his arguments. When he suffered that early breakdown, in 1826, it was because he lost faith in the pursuit of utilitarianism, his family creed. But he had no one he felt he could talk to about his crisis. His recovery, he said, came in part from reading Wordsworth. It came, too, from rejecting the psychological picture in which his father had raised him, a form of associationism that treated the mind as a mechanism for managing pleasure and pain, just as his father’s utilitarian ethics treated morality as a matter of maximizing the surplus of pleasure over pain. As he wrote in On Liberty, human nature is ‘not a machine to be built after a model,’ but a living thing that must ‘grow and develop itself on all sides.’” — [Kwame Anthony Appiah on AI and John Stuart Mill](https://humanistreview.ai/issue-1/appiah-ai-moral-character/), whose Autobiography is one of the books that caught my attention in the open stacks. 

• Mercifully, Pangram rates the Appiah essay as 100% human written… one can never tell these days. But apparently you can tell, sort of, on Substack — as I was preparing this post, I noticed this [newly-added feature](https://support.substack.com/hc/en-us/articles/50891130623508-How-can-I-detect-AI-on-Substack): 

I have been skeptical in the past about software that claims to be able to detect AI writing, but I have to say, Pangram feels different. I’ve tested it and it’s dismayingly effective — dismaying because, as I wrote about [here](https://resobscura.substack.com/p/what-is-happening-to-writing), a lot of the writing people seem to like online these days is coming up as 100% AI. I’m glad Substack added this feature and I hope it pops up elsewhere, e.g., it would be interesting to see it automatically applied to the output of major news websites and magazines. 

[Leave a comment](https://resobscura.substack.com/p/quality-non-fiction-books-are-the/comments)

[Share](https://resobscura.substack.com/p/quality-non-fiction-books-are-the?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[1](https://resobscura.substack.com/p/quality-non-fiction-books-are-the#footnote-anchor-1)

I had fun making the [early modern style colophon](https://book-prize-index.vercel.app/colophon). 1052421SharePreviousNext

#### Discussion about this post

CommentsRestacks[maigraines](https://substack.com/profile/3917382-maigraines?utm_source=substack-feed-item)[Jul 22](https://resobscura.substack.com/p/quality-non-fiction-books-are-the/comment/299555155)Liked by Benjamin Breen

Very cool! You should see if you're able to replicate your bookshelving experience by maybe having an option on the platform where someone can 'roll the dice' as it were and get returned 1-5 sentences from one of these books at random (or maybe be allowed to filter the dice roll sentence they get by topic or time period), and if it intrigues them maybe a link to the book page proper?ReplyShare[2 replies by Benjamin Breen and others](https://resobscura.substack.com/p/quality-non-fiction-books-are-the/comment/299555155)[Benjamin Breen](https://substack.com/profile/408222-benjamin-breen?utm_source=substack-feed-item)[Jul 23](https://resobscura.substack.com/p/quality-non-fiction-books-are-the/comment/300495311)Author

For those who asked for a "shelf" feature where you can simulate browsing around on the open stacks, here you go! It was surprisingly easy to make since I had already collected Library of Congress cataloguing info for about a third of the corpus - it currently only shows that portion of the books but it's still fun I think: [https://book-prize-index.vercel.app/fun/library-of-congress-shelf](https://book-prize-index.vercel.app/fun/library-of-congress-shelf)ReplyShare[22 more comments...](https://resobscura.substack.com/p/quality-non-fiction-books-are-the/comments)TopLatestDiscussions

No posts

### Ready for more?

Subscribe© 2026 Benjamin Breen · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)[Substack](https://substack.com) is the home for great culture
