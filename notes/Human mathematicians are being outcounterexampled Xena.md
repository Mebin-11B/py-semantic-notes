---
title: "Human mathematicians are being outcounterexampled | Xena"
url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
clipped: 2026-08-31 12:26:30
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Human mathematicians are being outcounterexampled | Xena](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/)

## Full Article

[Xena](https://xenaproject.wordpress.com/)
					
				
				Mathematicians learning Lean by doing.

									
								

			
								[Skip to content](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#content)
				
- [Home](https://xenaproject.wordpress.com)

- [About Xena](https://xenaproject.wordpress.com/what-is-the-xena-project/)

- [Student projects](https://xenaproject.wordpress.com/student-projects/)

- [Installing Lean and mathlib](https://leanprover-community.github.io/get_started.html)

- [Bluesky](https://bsky.app/profile/xenaproject.bsky.social)

- [Useful links.](https://xenaproject.wordpress.com/useful-links/)
			
		
	

	

		
			

			

				
					[← Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
					[The Annals Challenge →](https://xenaproject.wordpress.com/2026/08/13/the-annals-challenge/)
				

				
											

## [Human mathematicians are being outcounterexampled](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/)

					
					
						Posted on [July 20, 2026](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) by [xenaproject](https://xenaproject.wordpress.com/author/xenaproject/)					

					
						

It’s been an interesting few weeks for counterexamples. This post is basically my perspective of what has been going on in the world of formalization, AI tools and, in particular, counterexamples.

## Unit distance

Two months ago today (20th May 2026), ChatGPT disproved Erdős’ Unit Distance conjecture in discrete geometry. This is now old news but I had to start somewhere. The [announcement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) was accompanied with testimonies by human mathematicians, many of whom I knew and a few of whom I trusted, saying that they believed the argument (they had been given early access to it and had checked it). The basic structure of the proof is that a profound theorem in number theory due to Golod and Shafarevich from the 1960s could be used to construct a counterexample to the conjecture.

It is now 9 years since I had a mid-life crisis, realised I no longer trusted many human mathematicians when it comes to technical details, discovered Lean, and started to argue that interactive theorem provers should play an important role in the future of mathematics. So of course my first question was “is the counterexample formalized in Lean”. The answer was “no”.

But under a week later (26th May 2026), I got an email from Fields Medallist Mike Freedman. Mike is now the Chief Science Officer for [Logical Intelligence](https://logicalintelligence.com/), a company cofounded by Turing Award winner and “godfather of AI” Yan LeCun. Mike informed me that their system had autoformalized the entire ChatGPT-generated paper in Lean and could I take a look. I looked, and my post-doc Thomas Browning looked too. And indeed this was what Logical Intelligence had done: they had formalized precisely the statement that the profound theorem of number theory implied the Erdős counterexample. Breakthrough LLM-generated mathematics being formalized in real time. Interesting data point.

Of course there is an elephant in the room here though, the profound theorem of number theory which takes 100+ pages to prove (it needs huge chunks of global class field theory, a theory developed at the beginning of the 20th century and for which there are still no short proofs; it is proving difficult to compress). In 2025 I had run a [Clay Summer School](https://www.claymath.org/events/formalizing-class-field-theory/) with Richard Hill on the formalization of class field theory, and one year later we have nearly done the local case (it is the current PhD project of my student Edison Xie); the global case remained open, and indeed in 2025 formalizing global class field theory seemed like a fantasy.

One month later, on June 26th 2026, my perception of what was possible again changed. Boris Alexeev [announced on the Lean Zulip](https://leanprover.zulipchat.com/#narrow/channel/583339-AI-authored-projects/topic/Erd.C5.91s.20unit-distance.20counterexample.2C.20exponent.20above.201/near/606778508) that he had steered ChatGPT to a complete formalization of the Erdős counterexample, assuming nothing beyond the axioms of mathematics. Boris works at OpenAI and had used their new model Sol to do the autoformalization. Boris made the code public and it did not take long for me to realise that somewhere within all this AI-generated (and sometimes horrible, although sometimes decent) code was indeed a proof of some really hard theorems in global class field theory. Also of interest to me was that Sol had generated 1.2 million lines of Lean code in the three weeks that it had worked on the project. Lean’s fantastic (declaration of conflict of interest: I am a maintainer) mathematics library [mathlib](https://github.com/leanprover-community/mathlib4) is only 2.3 million lines of code, and took nine years to write. Perhaps it was at this point that the penny really dropped for me — large AI-generated developments of mathematics are inevitable. One cannot trust AI-generated code so I ran it in a sandbox on my machine (malicious Lean code can run arbitrary commands on your computer — Lean is a programming language, after all). Indeed, it was proving nontrivial theorems about the cohomology of number fields. Wow.

## Group schemes of order n

A week after Boris’ revelation, in early July, I was thinking hard about how to run my [Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/). This workshop was sponsored by [Logos Research](https://www.logosresearch.ai/), who, like Logical Intelligence (and Harmonic and Axiom AI and Moonshot AI and…) have a tool which can autoformalize mathematics — translating it from human language into Lean — building on mathlib. Logos told me that they were only going to allow 5 people at a time to use their system during the workshop, and there were 25 attendees, so I told all attendees that I would buy them a Claude Max subscription for a month, so they had something to experiment with when it wasn’t their turn for Logos’ tool. The workshop was 6th to 10th July, and the Claude Max subscription would give attendees access to Claude Fable, at least until Tuesday 7th, when it was being switched off. When OpenAI got wind of what I was doing, they also offered all attendees free ChatGPT Pro access for a month; this was a big deal because ChatGPT Sol was coming out on the 9th. So basically all attendees would have access to Sol and Fable for 4 out of the 5 days of the workshop, and Logos’ tool for the entire week. In fact Fable access was not removed on the 7th so we were in even better shape.

I was not sure how good Logos’ tool was going to be, but I wanted a development of the theory of finite flat group schemes in Lean for my ongoing proof of Fermat’s Last Theorem, so I put uploaded some classic papers in the area to Fable and ChatGPT, and got them together to write down an exposition of the theory in natural language. I passed this pdf document over to Logos the day before the workshop, and on the first day of the workshop they said that one of the claims in the pdf was false and they had found an explicit counterexample. Another counterexample! I took a look and indeed the LLM-generated pdf was simply wrong at some point when describing a standard construction; false alarm. I had missed this myself though when reading through the pdf. Interesting how AI had again found a counterexample. I fixed the pdf. I thought it was interesting that the AI didn’t just say “I don’t quite follow this argument”, it instead said “here is a proof that this argument is simply wrong”, a much more powerful statement.

With the development of the theory of finite flat group schemes back on track, I could relax back into the FLT workshop. On Tuesday 7th July I sat opposite [Akhil Mathew](https://math.uchicago.edu/~amathew/) at lunch; Akhil is a professor of mathematics at UChicago and he was an attendee who had been experimenting with the tools available. We talked about potential questions which AI could work on, and Akhil raised the old question of Grothendieck about whether every finite free group scheme of order n was killed by n. Deligne had proved the result in the commutative case, and Grothendieck had proved it when the base was reduced; Rene Schoof had proved it in more cases, and there had even been [a paper](https://ems.press/content/serial-article-files/51994) by Emiliano Torti published last year, proving it in even more generality. I said that I thought that this was a fabulous thing to get AI thinking about.

The day after the workshop finished, on Saturday 11th July, I got a DM from Akhil telling me that Sol had found a counterexample. He sent me a 12 page pdf. I immediately replied saying that I was not reading AI-generated informal mathematics and could he please formalize the entire thing in Lean. Four hours later he replied again, saying that Fable had autoformalized the entire thing. I scanned over the 1076-line Lean file, checking that the code did not delete all the files on my hard drive (Lean is a programming language, so it can do this). Convinced that it was only theorems, I then compiled it on my laptop and it took me under 5 minutes in total to check that (a) the statement of the claimed theorem used only concepts in mathlib (and thus things like  `[HopfAlgebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/HopfAlgebra/Basic.html#HopfAlgebra)`  can be trusted to mean what mathematicians think of as Hopf algebras) (b) the statement of the claimed theorem was that there was a counterexample and (c) the proof compiled. At this point I knew that we had a counterexample — a group scheme of order 4 which was not killed by 4. I suggested to Akhil that he make a PR to mathlib with the counterexample — which [he did](https://github.com/leanprover-community/mathlib4/pull/41748). I would have also suggested to him that he draft a press release saying that a machine had solved a 60-year-old question of Grothendieck in algebraic geometry, but somehow by this point I was almost becoming immune to all of this. It wasn’t clear to me that the media would even be able to distinguish between “machine resolves question due to Erdős” and “machine resolves question due to Grothendieck” even though I personally found the latter far more interesting. Of course the Grothendieck counterexample was far far easier than the Erdős one (a thousand lines, not a million), all I’m saying is that it’s an area of mathematics that I personally find more interesting. I pointed out to Akhil that machines seemed to be getting very good at finding counterexamples and suggested that he try the Hodge conjecture next.

## Modularity lifting theorems

I think it’s worth stepping back at this point and surveying what the attitudes of human experts to these sorts of things are. On Tuesday (14th July) I went to work at Imperial and the Grothendieck counterexample was the talk of lunch. A member of the faculty (who I won’t name) said to me that the fact that the counterexample was so easy to find just indicated that humans had not spent enough time thinking about the problem, implying that a 60-year-old question of Grothendieck was not actually that interesting to work on. I didn’t tell him that at some point earlier in my career I had spent a week working hard on the problem. In my mind my colleague is just going through the five stages of grief; right now they seem to be in the denial phase. 

After lunch I met with my PhD student Andrew Yang, who had been working on formalizing a modularity lifting theorem in Lean, something which is crucial to my FLT work. Andrew had come to the Logos FLT workshop and now had access to both Sol and Fable. He told me that using these tools he had written 250K lines of Lean code which basically completely finished the project in what was I guess a 2 week period.

A few days earlier I had got an email from a professor in the maths department here at Imperial, expressing surprise that some of our graduate students were paying $200 per month to access models such as Sol and Fable. He said that he thought that these people were crazy. I did not immediately respond. But after meeting with Andrew I emailed the professor back and told him that in my opinion, any PhD student who was not paying $200 per month to access these tools was crazy. In fact during the workshop I learnt from Harvard PhD student Bryan Wang that Harvard were already giving free Fable access to all PhD students, post-docs and faculty at Harvard.

## The Jacobian Conjecture

But back to Akhil. I am not sure if he took my idea to disprove the Hodge conjecture seriously. But it looks like he had deeply understood that, with these extraordinary new AI tools, counterexamples might be low-hanging fruit right now. He had discussed with Levent Alpöge the idea of finding more counterexamples in algebraic geometry, and 12 hours ago Levent [posted on X](https://x.com/__alpoge__/status/2079028340955197566?s=20) that Fable had found a counterexample to the [Jacobian Conjecture](https://en.wikipedia.org/wiki/Jacobian_conjecture). This is a big deal — this is a famous question in algebraic geometry which had been open for 100 years and which many people had thought about. It was apparently solved during the 2026 World Cup Final.

I woke up today to a DM from Akhil saying “shall I make another PR?” but this time he was too late — Paul Lezeau had already formalized the counterexample manually and had [made a PR](https://github.com/google-deepmind/formal-conjectures/pull/4474) to DeepMind’s [Formal Conjectures repo](https://github.com/google-deepmind/formal-conjectures). Mathlib does not contain a large list of conjectures in mathematics, but DeepMind’s repo does. The importance of formalization of conjectures by humans is that if humans are agreed that a Lean statement does faithfully capture the idea behind a conjecture, then checking that (possibly AI-generated) Lean code does comprise a proof or disproof of the conjecture is a triviality. Congratulations to Levent, thanks to Akhil for suggesting the problem to him, and thanks to DeepMind for already having formalized the statement and thus making formal verification of the counterexample a triviality. 

The Jacobian conjecture is resolved! Wow! The next step in that work is for humans to understand exactly what is going on with the example. For the true value of work like this is to give humans better understanding of mathematics. Indeed Akhil has been working on trying to understand the Grothendieck counterexample in a way which is far deeper than “here is a random presentation of a random ring and a random calculation which shows that something doesn’t work”. What we need next is the insight which can be drawn from these extraordinary examples.

What a time to be alive.

		
	

### Share this:

- [Share on X (Opens in new window)
				X](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?share=twitter)
- [Share on Facebook (Opens in new window)
				Facebook](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?share=facebook)
- Like Loading...

	

### Related

											

							
						
													
						
							

## 
							About xenaproject							

							The Xena Project aims to get mathematics undergraduates (at Imperial College and beyond) trained in the art of formalising mathematics on a computer. Why? Because I have this feeling that digitising mathematics will be really important one day.							
								[View all posts by xenaproject →](https://xenaproject.wordpress.com/author/xenaproject/)
							
						
					

						
							This entry was posted in [Algebraic Geometry](https://xenaproject.wordpress.com/category/algebraic-geometry/), [Fermat's Last Theorem](https://xenaproject.wordpress.com/category/fermats-last-theorem/), [Machine Learning](https://xenaproject.wordpress.com/category/machine-learning/), [Research formalisation](https://xenaproject.wordpress.com/category/research-formalisation/) and tagged [AI](https://xenaproject.wordpress.com/tag/ai/), [Artificial Intelligence](https://xenaproject.wordpress.com/tag/artificial-intelligence/), [counterexample](https://xenaproject.wordpress.com/tag/counterexample/), [counterexamples](https://xenaproject.wordpress.com/tag/counterexamples/), [Grothendieck](https://xenaproject.wordpress.com/tag/grothendieck/), [group scheme](https://xenaproject.wordpress.com/tag/group-scheme/), [Jacobian Conjecture](https://xenaproject.wordpress.com/tag/jacobian-conjecture/), [lean](https://xenaproject.wordpress.com/tag/lean/), [math](https://xenaproject.wordpress.com/tag/math/), [mathematics](https://xenaproject.wordpress.com/tag/mathematics/), [philosophy](https://xenaproject.wordpress.com/tag/philosophy/), [science](https://xenaproject.wordpress.com/tag/science/), [technology](https://xenaproject.wordpress.com/tag/technology/). Bookmark the [permalink](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/).													
					

				
					[← Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
					[The Annals Challenge →](https://xenaproject.wordpress.com/2026/08/13/the-annals-challenge/)
				

				
			

			

### 
			53 Responses to Human mathematicians are being outcounterexampled			

			
						
- 
		
			
								ys says:			

				
				
			[July 20, 2026 at 3:55 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4839)			

			

Dear Kevin, 

Thanks for this article. You write that you are “not reading AI-generated informal mathematics” but also that “the next step in that work is for humans to understand exactly what is going on with the example.” How do we do this without reading the informal AI output? We are surely not going through a thousand-line Lean file? 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4839&_wpnonce=ff760f2b5f)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4839#respond)			
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 20, 2026 at 8:05 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4848)			

			

I actually find it easier to go through the formal output than the informal output. With the formal output, there is no danger of imagining things or misinterpreting the argument. Most reasonable Lean developments are organized into logical progressions of lemmas, and most of the lemmas might even be obvious to someone well versed in the field (who can also read Lean, of course), leaving only a small amount of actual argumentation to read.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4848&_wpnonce=277cf6e582)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4848#respond)			
		

				
		
- 
		
			
								dasc says:			

				
				
			[July 21, 2026 at 9:16 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4866)			

			

Well, that’s because you are versed in Lean. IMO, Lean proofs are very hard to read as a begginner, compared to, say Isabelle/HOL. If human understanding is the main objective “informal output”, which I believe is a Latex document, for example shouldn’t be relegated at all.

It will be very sad if, in the future all proofs are machine-generated in lean/rocq/whatever proof assistant only, and relegating knowledge to the handful of people that know the proof assistant AND are experts in the specific field.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4866&_wpnonce=706849be34)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
							
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 21, 2026 at 9:06 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4879)			

			

I only started using Lean three months ago; I would hardly call myself an expert. Nobody really “reads” Lean in the traditional sense of reading a static artifact. You step through the proof interactively and observe the state transformations at each step.

It takes a fair bit of training to read mathematics in the first place. Reading Lean is only a small difficulty increment on top of that, provided that one is motivated to learn.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4879&_wpnonce=3c391f5fcc)Like

			
							
		

				

		
- 
		
			
								Tanay Wakhare says:			

				
				
			[July 21, 2026 at 3:13 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4858)			

			

Parsing through so much LLM and Lean output is exactly the bottleneck I think is coming this year. We’re going to be dealing with two huge issues going forwards 

- An overload of LLM generated proofs (which are error prone, as noted in the post)

- A need to check Lean code (much of which will be written by LLMs)

For newcomers to Lean especially, the bigger risk imo is formalizing something different that what they thought they were formalizing.

Both of these are fundamentally a UI/UX problem about how human mathematicians will deal with information overload and it’s exactly what we’re addressing at [https://mathvision.ai/](https://mathvision.ai/) 🙂 Check it out for free if you’re interested.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4858&_wpnonce=6a2d899b05)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4858#respond)			
		

				

		
- 
		
			
								jeanabousamra says:			

				
				
			[July 20, 2026 at 5:24 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4840)			

			

“A few days earlier I had got an email from a professor in the maths department here at Imperial, expressing surprise that some of our graduate students were paying $200 per month to access models such as Sol and Fable. He said that he thought that these people were crazy. I did not immediately respond. But after meeting with Andrew I emailed the professor back and told him that in my opinion, any PhD student who was not paying $200 per month to access these tools was crazy.”

With due respect, I find this comment disgusting. Among other problems, this money will be used for the gigantic V-sign to future generations that is building lots of extra gas power plants to supply new data centers. I won’t judge people for doing it any more than for eating red meat, and especially not in such a toughly competitive academic system, but if you think it’s crazy not to give 10% of your salary to unethical companies if it might hurt your career, then we are fundamentally not operating on the same set of values.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4840&_wpnonce=fe464f5cf7)Liked by [5 people](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4840#respond)			
		

				
		
- 
		
			
								[Yemon Choi](http://ifwisdomwereteachable.wordpress.com) says:			

				
				
			[July 20, 2026 at 7:50 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4842)			

			

With the caveat that the internet and years of social media encourage us to make kneejerk responses, my instinct is to concur with JAS’s comment/reply. Aside from views one may (or may not) have about the companies building and selling these tools, the sentiment that Kevin candidly admits to  is not a mentality that I want to see encouraged among those doing a PhD.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4842&_wpnonce=bfcb778398)Liked by [2 people](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4842#respond)			
		

				
		
- 
		
			
								alpacadeliciously52e6be6b27 says:			

				
				
			[July 20, 2026 at 8:02 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4847)			

			

There are possibly political or social welfare reasons why one should resist the AI takeover of mathematics. But, from a strict utilitarian standpoint, these tools make you much more than 10% more productive, and are well worth the cost.

I worry about the social implications of handing over a large portion of our resources to AI companies, and the equity and access concerns for people from countries where $200 is a lot of money. Also, there is evidence that AI companies are subsidizing the present cost of subscription access and that the true cost is much higher than what we pay.

But, for now, if you’re a graduate student at Harvard or Imperial, the economic argument is persuasively in favor of spending the money to subscribe to AI.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4847&_wpnonce=4a7da7cc73)Like

			
							
		

				

		
- 
		
			
								kenhchan says:			

				
				
			[July 20, 2026 at 7:57 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4844)			

			

you should inform your opinion on actual numbers, data centers use a small fraction of electricity and water compared to, say agriculture. so if you’re the kind of person who judges people for eating red meat, you need to dish out that judgement proportionally for AI users. 

i’ve given the exact same advice to graduate students months ago, pay for the best models, especially now that they are still affordable. contribute to proving the use case (at this point, is there even any doubt?), and get your department / advisor to pay for the models going forward. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4844&_wpnonce=fd8cacaa0e)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4844#respond)			
		

				
		
- 
		
			
								PaulKu says:			

				
				
			[July 24, 2026 at 9:05 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4895)			

			

A Bloomberg article that was published in the past week made the claims that 5.9% of US electricity production is currently consumed by datacentres.  By 2035 that’s projected to be 20% – IIRC that represents 193GWh of power demand.

There should be no assumption that the US grid can grow to handle that in time, or that every planned US data centre actually gets built.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4895&_wpnonce=853f1bc622)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
							
		

				
		
- 
		
			
								JFB says:			

				
				
			[July 25, 2026 at 1:29 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4901)			

			

This comparison with agriculture makes little sense. Food (even red meat) is fundamental for human survival. Data centres?

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4901&_wpnonce=abd8e71d39)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
							
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 25, 2026 at 12:41 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4907)			

			

As much as I enjoy red meat, I have to admit that red meat is not actually necessary for human survival. Humans can live and even thrive on a diet containing no red meat.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4907&_wpnonce=3e00690f2d)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
							
		

				

		
- 
		
			
								adolfont says:			

				
				
			[July 24, 2026 at 12:46 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4896)			

			

Great! At least one person mentioned ethical issues.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4896&_wpnonce=353ee6f886)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4896#respond)			
		

				
		
- 
		
			
								Mark says:			

				
				
			[July 24, 2026 at 10:29 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4900)			

			

If people care about ethical issues in mathematics, then why do so many mathematicians in academia accept grants from governments around the world that are engaged in terrible things like wars? 

None other than Alexandre Grothendieck himself quit academia because he didn’t want his mathematics research to be funded by the French government and associated with the French and American military fighting in Vietnam.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4900&_wpnonce=dd5ef768cd)Like

			
							
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 25, 2026 at 12:35 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4906)			

			

Gah, this is such an absurd take. Do you pay taxes to governments? Are you suggesting that we should stop paying taxes because tax money is used for wars?

The logic actually escapes me. Shouldn’t paying to fund a war be significantly more morally objectionable than taking money from someone who would otherwise use that money for war?

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4906&_wpnonce=17126a4afd)Like

			
							
		

				
		
- 
		
			
								Mark says:			

				
				
			[July 25, 2026 at 1:46 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4908)			

			

David Jao,

It’s the same kind of logic as to whether researchers should be accepting grant money from corporations like OpenAI or Raytheon, or whether employees should work for such corporations who will be paying them a salary on the backs of their gross ethical violations around the world. The concept of having your sources of income and research money come from ethical sources rather than coming from some sort of corporate and government misbehavior. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4908&_wpnonce=f272f263ed)Like

			
							
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 25, 2026 at 1:49 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4909)			

			

OK, so now wait a minute, your reply presumes that 1) recipients of the money are contributing to the ethical violations directly through their work, and 2) providers of the money are earning the money through their ethical violations. While both 1 and 2 are true in the case of a corporate employee, they are NOT true for grant recipients such as NDSEG fellows. An NDSEG recipient is under no obligation to work for the Defense Department (or War Department or whatever they’re calling it these days), and the Defense Department derives their income from tax revenues, not from profiting off of ethical violations.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4909&_wpnonce=a97c70f950)Like

			
							
		

				

		
- 
		
			
								Anon says:			

				
				
			[July 20, 2026 at 5:55 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4841)			

			

idk if this is satisfactory but here’s how GPT interpreted the Jacobian example. Take P1xP2->P3 (Union of divisors on P1 say), remove ramification locus and remove a hyperplane of P3 which is tangent to a point of the map P1->P3 (tripling the divisor) but not osculating (multiplicity exactly two). Then the preimage is A3 by direct computation.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4841&_wpnonce=c3810130d0)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4841#respond)			
		

				
		
- 
		
			
								[Yemon Choi](http://ifwisdomwereteachable.wordpress.com) says:			

				
				
			[July 20, 2026 at 7:55 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4843)			

			

On a more constructive note than my previous comment/post: in the hope that some people who follow this blog as part of their interest in/commitment to formalization are also interested in understanding algebraic geometry, I want to give a signal boost to [https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/) so that some maths discussion takes place there.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4843&_wpnonce=dc0303bf84)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4843#respond)			
		

				
		
- 
		
			
								Madeleine Birchfield says:			

				
				
			[July 21, 2026 at 12:09 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4851)			

			

A pretty important set of philosophical questions: what is the point of mathematics and the role of mathematicians when the task of formally proving conjectures has been outsourced to a team consisting of a large language model and a proof assistant? What’s the point of mathematical rigour when mathematicians no longer have to develop and write proofs out by hand? 

I feel like whatever remains of the formalist viewpoint of mathematics has been largely disproven by developments in the past few years in artificial intelligence and proof assistants: clearly there are still activities for mathematicians in an era where large language models are the ones writing formal proofs in a proof assistant. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4851&_wpnonce=d3f3e8c05f)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4851#respond)			
		

				
		
- 
		
			
								vmarko says:			

				
				
			[July 21, 2026 at 12:30 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4873)			

			

“what is the point of mathematics and the role of mathematicians when the task of formally proving conjectures has been outsourced to a team consisting of a large language model and a proof assistant?”

The role of mathematicians is not just to prove conjectures, but also to formulate them. Formulating an interesting/important/useful statement that is a candidate for a theorem often requires as much creative insight (if not more) as does proving it.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4873&_wpnonce=27a82c2b4b)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4873#respond)			
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 21, 2026 at 9:14 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4881)			

			

For now, I agree, it is still true that humans have an edge in formulating conjectures and judging the importance of the results. But I can reasonably imagine a world where machines get better at formulating conjectures.

The next moat behind inquiry and judging is liability and responsibility. I believe there have been a number of court cases where customers interacting with AI customer service chatbots received incorrect information from those chatbots (for example, an airline’s chatbot claiming that a ticket purchase was refundable when it wasn’t). In all of these cases, the companies that those chatbots were supposedly representing were held liable for the statements that the chatbots made (e.g. the company was forced to honor the promised refund). For now, many companies are skittish about allowing their machines to assume liability on their behalf. The human is still the final backstop for liability purposes.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4881&_wpnonce=322de522a9)Like

			
							
		

				
		
- 
		
			
								Jason Starr says:			

				
				
			[July 22, 2026 at 3:30 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4884)			

			

I have one article (with Graber, Harris and Mazur) that disproves a conjecture about rational points that Serre posed in correspondence with Grothendieck.  Our theorem proves that a counterexample to the conjecture exists (as a corollary of a more general theorem), but our method gives no explicit counterexample.  Almost immediately afterward, somebody sat down and found an explicit counterexample.  Honestly, that explicit counterexample could probably have been found (by a dedicated human) anytime in the four decades the conjecture was open, but the community expected the conjecture to be true.  If the conjecture is true, it is a waste of resources to search for counterexamples.  Now AI means that sort of “checking for counterexamples” can probably be done automatically.  That is a fantastic development!  As others have said, we could try to *disprove* positive characteristic resolution of singularities (by disproving some of the corollaries about specific congruences of rational points of specific varieties over specific finite fields).

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4884&_wpnonce=6458bcf227)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
							
		

				

		
- 
		
			
								Mark says:			

				
				
			[July 25, 2026 at 8:08 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4903)			

			

I don’t know if you’ve read any Oswald Spengler but he makes a distinction over the course of a civilization’s lifetime between the “Age of Faith”, “Age of Reason”, and “Age of Memory”. Mathematics has been in an age of reason for the past 400-500 years and AI generated proofs are going to force mathematics to exit the age of reason and enter the age of memory, where the most valued skill is no longer the ability to come up with proofs through reason (that characterises the Age of Reason more broadly), but the ability to sift through everything that has been proven and determine what is actually important for human beings to remember (that characterises the Age of Memory more broadly). 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4903&_wpnonce=2bae634f82)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4903#respond)			
		

				

		
- 
		
			
								Shreyas says:			

				
				
			[July 21, 2026 at 11:25 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4867)			

			

But after meeting with Andrew I emailed the professor back and told him that in my opinion, any PhD student who was not paying $200 per month to access these tools was crazy.

Maybe you intended to express enthusiasm for how good AI has gotten at mathematics. But from the perspective of a PhD student, this comes across as very tone deaf. In many parts of the world (including Europe and many places in the US), PhD students are paid a pittance and are barely making ends meet. Expecting them to fork out 200 USD/month is extremely unreasonable and unrealistic. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4867&_wpnonce=2dd973c9c6)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4867#respond)			
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 21, 2026 at 9:08 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4880)			

			

I think we’re all hoping for the Harvard approach where the institution pays for access without docking grad student pay to offset the cost.

I don’t think it’s realistic to go back to the good old days. Even if you yourself forswear AI, you can’t stop other people from using it, and those other people are your competition.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4880&_wpnonce=e094ea8941)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4880#respond)			
		

				

		
- 
		
			
								Jeremy says:			

				
				
			[July 21, 2026 at 11:29 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4868)			

			

What we need next is the insight which can be drawn from these extraordinary examples.

Just ask Fable!

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4868&_wpnonce=d10f69e8d4)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4868#respond)			
		

				
		
- 
		
			
								AG says:			

				
				
			[July 21, 2026 at 12:17 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4872)			

			

Next do resolution of singularities in positive characteristic.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4872&_wpnonce=1d0866219c)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4872#respond)			
		

				
		
- 
		
			
								Elderly postdoc says:			

				
				
			[July 21, 2026 at 5:05 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4878)			

			

It is really, really gutting for senior people to be so in favour of this de-skilling. I learned a lot your old stream-of-counciousness notes on various examples for $\SL_2$, etc., and apparently now your opinion seems to amount to saying that I shouldn’t have bothered, although for psychological purposes this never seems to be said directly.

Said aloud or not, though, we all know what our students mean when they say they “understand perfectly all the lectures” but “just can’t solve the exercises.” The same will be true, after enough time, of anyone who claims that “understanding” the machines constitutes legitimate research activity. 

Just because this is inevitable doesn’t mean it’s not the end of the world.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4878&_wpnonce=b7d67d3917)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4878#respond)			
		

				
		
- 
		
			
								Anon says:			

				
				
			[July 21, 2026 at 10:18 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4882)			

			

For finding these counterexamples, like the Jacobian conjecture one, did the model shell out to python, mathematica, Z3, Lean, etc, or was it all just reasoning in natural language? I understand that the final result was checked with wolfram and Lean, but I’m curious about the actual process of finding the counterexample in the first place.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4882&_wpnonce=5140f650bf)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4882#respond)			
		

				
		
- 
		
			
								Will Sawin says:			

				
				
			[July 27, 2026 at 6:55 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4914)			

			

When asked a question AI models will often write and run code, I think most commonly Python, to gather information that may help in answering the question. No details have been released about how the Jacobian conjecture counterexample was found, but it would be surprising if code wasn’t run at some point in the reasoning process. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4914&_wpnonce=996bd7907c)Liked by [1 person](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#)

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4914#respond)			
		

				

		
- 
		
			
								dcef says:			

				
				
			[July 22, 2026 at 10:59 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4883)			

			

Is the use of calculators and sympy deskilling as well? No, it means factoring a Mersenne number isn’t conference worthy like a century ago. The community got more ambitious. It’s not like we’ll run out of math to explore, even with fable.

People are freaking out about this because it’s happening so quickly, but there is also an ostrich-in-the-sand aspect to it as well. For many abstract-minded academics, AI is intellectually distasteful because it runs counter to many of our intuitions about intelligence, reasoning and elegance, and to add insult to injury it is run by some of the least savory people on the planet. So people willfully tried not to learn or hear about it until they couldn’t, then they tried to sneer at it (“it’s not working”) until they couldn’t, then they tried to move the goalposts (“it’s just a stochastic parrot, it can’t come up with new insights”) until they couldn’t. So you end up having to change your worldview, methods, and ways of doing research all overnight, which understandably is upsetting.

But if you’ve been following it for a while and use it for what it is (a powerful tool, like symbolic libraries before it and calculators before that), there’s no reason to feel anything but enthusiasm.

I should also note that Sol/Fable transcripts show that it didn’t come up with exotic new structures to come up with the Jacobian counterexample, it built onto a 1998 paper and reasoned from there. So it’s not a case of “helplessly watching from the sidelines as the machine god Andrew Wiles its way into Fermat with unfathomable alien concepts”, but more a case of “I could devote a research project to it but wouldn’t before because the risk of an impasse/wasted PhD/postdoc was too high, but now I can just point the computer at it, neat”. Again, a tool.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4883&_wpnonce=f55c6e7c53)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4883#respond)			
		

				
		
- 
		
			
								Elderly Postdoc says:			

				
				
			[July 27, 2026 at 4:58 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4913)			

			

My first run-in with long-termists/CFAR/AI-safety people was…some time ago. I am so concerned precisely because of this reason, and because they, and the amount of money invested (more in a single year year than then highway construction in US history, plus the Apollo programme!) says that “helplessly watching from the sidelines as the machine god Andrew Wiles its way into Fermat with unfathomable alien concepts” is probably one or two years away. It seems basically unthinkable that those of us without jobs yet will ever have a chance at them, now. Will anyone hired last year get tenure? 

When Fields medalists are quitting math because it is seemingly pointless now, maybe it’s time to drop the “just a tool” line, because no one can articulate any non-sham vision of research, given access to this tool, or rather, where this tool will be in one year. I wish I could have feelings towards this other than absolute doom, but it seems like the only people who will survive this even a few years are those protected by professional licensure cartels. Theirs is also a doomed fight, but they will survive at least a little longer. The only long-term outcomes seem to be AI owner or serf.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4913&_wpnonce=b941257b12)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4913#respond)			
		

				

		
- 
		

Pingback: [Xena on Counterexamples | Persiflage](https://galoisrepresentations.org/2026/07/22/xena-on-counterexamples/)
				
		
- 
		
			
								[Kevin Ventullo](https://kevinventullo.com/) says:			

				
				
			[July 23, 2026 at 1:05 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4886)			

			

Why stop at $200/month? The subscription plan rate limits per-session token usage and the labs show no signs of decreasing prices anytime soon. 

Perhaps the 2020’s will be remembered as the final decade in which one could in principle do cutting-edge research mathematics on a shoestring budget. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4886&_wpnonce=bdd2713683)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4886#respond)			
		

				
		
- 
		
			
								David Jao says:			

				
				
			[July 23, 2026 at 1:11 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4887)			

			

If we take inspiration from computing itself, the existence of top-500 supercomputers does not prevent ordinary researchers from doing interesting research with personal computers.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4887&_wpnonce=0fd13d2ba1)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4887#respond)			
		

				
		
- 
		
			
								[xenaproject](https://xenaproject.wordpress.com) says:			

				
				
			[July 23, 2026 at 8:33 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4888)			

			

$200/month is the current cost for research-math-capable models but I am cautiously optimistic that as the open source models get better (and they are lagging around a year behind the frontier models) we might find that mathematicians can just switch to them and end up paying less, not more.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4888&_wpnonce=8a8b500bb2)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4888#respond)			
		

				
		
- 
		
			
								adolfont says:			

				
				
			[July 25, 2026 at 8:21 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4910)			

			

Maybe. Who knows. But there’s also the possibility that open-weight models (they are *not* open source) will become comparatively much worse than the paid models if the latter are no longer subsidized (it’s no secret that open-source models use closed-source models in their training).

And none of this minimizes the ethical issues, which are not the subject of this thread.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4910&_wpnonce=b04c2cc18d)Like

			
							
		

				

		
- 
		
			
								Steven Heston says:			

				
				
			[July 23, 2026 at 11:29 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4889)			

			

Kevin is right, $200/month is cheap, only 2% of an average professor salary.  It is ludicrous to economize on these revolutionary AI tools.  We could fire 2% of professors (or double their teaching loads) and give these tools to everyone.

Fortunately, these tools will become better and cheaper.  Meanwhile, business schools spend money relabeling basic statistics courses as “machine learning”.  Rich universities resemble hedge funds with sports teams.  Some student-athletes now make millions!

Remember, every month that an Erdos problems goes unsolved, an angel dies.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4889&_wpnonce=b0ed32c264)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4889#respond)			
		

				
		
- 
		
			
								Madeleine Birchfield says:			

				
				
			[July 23, 2026 at 1:42 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4890)			

			

I’m a lot less impressed with the disproof of the Jacobian conjecture for more than two variables after Terence Tao showed that the disproof is a result of the basic fact that multiplication of a linear homogeneous polynomial and a quadratic homogeneous polynomial is not injective: 

[A digestion of the Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

At this point, to me the counterexample just shows how blind human beings can be at times, rather than how good large language models are at proving mathematics. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4890&_wpnonce=faa2e289c5)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4890#respond)			
		

				
		
- 
		
			
								[xenaproject](https://xenaproject.wordpress.com) says:			

				
				
			[July 24, 2026 at 8:14 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4894)			

			

Re human beings being “blind” — hindsight is a wonderful thing 🙂 Although I think it’s more accurate to say that the disproof is a highly nontrivial consequence of the basic fact that multiplication of a linear homogeneous polynomial and a quadratic homogeneous polynomial is not injective. There’s much more going on than that.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4894&_wpnonce=93f38ce027)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4894#respond)			
		

				

		
- 
		
			
								Madeleine Birchfield says:			

				
				
			[July 24, 2026 at 3:35 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4897)			

			

I think there is a big distinction to be made in mathematics between conjectures that are existential in form “there exists a X such that Y Z etc” and conjectures that are about all such objects “for all X, Y Z etc”. 

I think that conjecture of the first kind are much easier for large language models to prove than conjectures of the second kind, since for the first kind, all the large language model needs to do is to find an example X satisfying the conditions Y Z etc. This is also why refutations of conjectures of the second kind are also easy, because the negation of “for all X, Y Z etc” is “there exists X such that not Y Z etc”, so one just has to find a counterexample. 

But proving statements about all such X where Y Z etc holds requires a lot more deep mathematics than just finding an example. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4897&_wpnonce=5f64c43607)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4897#respond)			
		

				
		
- 
		
			
								HHarad says:			

				
				
			[July 25, 2026 at 11:40 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4904)			

			

Can’t you just turn one kind of conjecture into the other by attempting to disprove its negation? This seems like a case of moving yet again the goalposts. “The Jacobian conjecture wasn’t that hard to disprove, it ‘just’ had to find a polynomial.” Okay, and I guess the Riemann hypothesis won’t have been that hard to disprove, one just needs to find a nontrivial zero with real part different from .5?

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4904&_wpnonce=e125df3927)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4904#respond)			
		

				
		
- 
		
			
								[xenaproject](https://xenaproject.wordpress.com) says:			

				
				
			[July 25, 2026 at 12:31 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4905)			

			

No — there’s a genuine difference between a proof of the Jacobian conjecture and a proof of its converse. For example, it is extremely unlikely that a proof of the conjecture would have fitted into a tweet. The conjecture is a “for all” statement, its converse is a “there exists” statement.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4905&_wpnonce=0d0ec42310)Like

			
							
		

				

		
- 
		
			
								Madeleine Birchfield says:			

				
				
			[August 12, 2026 at 5:43 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4926)			

			

Timothy Gowers has a new blog post where he argues against LLMs having an inherent edge for solving existential statements over universal statements:

[What sort of maths are LLMs good at?](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/)

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4926&_wpnonce=148adc8c4a)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4926#respond)			
		

				

		
- 
		
			
								Mark says:			

				
				
			[July 24, 2026 at 10:19 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4899)			

			

Having humans try to understand why a LLM’s proof is valid is probably a lot easier than having humans try to understand why a computer generated proof brute forcing through all the possible hundreds of thousands of options is valid. 

Does anybody for instance truly understand why the Boolean Pythagorean triples problem only holds for numbers up to 7824? 

Compare with the LLM generated counterexample of the Jacobian conjecture and the reasons why that function is a counterexample, which was digested pretty rapidly by the mathematics community. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4899&_wpnonce=e2c9c3e51a)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4899#respond)			
		

				
		
- 
		
			
								trevoruptain says:			

				
				
			[July 27, 2026 at 10:15 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4915)			

			

Buzzard’s list is the tip of it – there’ve been close to a dozen of these just this month once you count the smaller-renown ones (Dinitz-Garg-Goemans on July 22, a quantum information problem on July 24). I’ve been keeping a running scored registry of open conjectures plus a kill feed with verification tiers at openconjectures.org, partly because “was this actually resolved” is turning into a full-time question.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4915&_wpnonce=b2eb95a5e6)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4915#respond)			
		

				
		
- 
		
			
								[David Speyer](http://www.math.lsa.umich.edu/~speyer) says:			

				
				
			[July 30, 2026 at 6:16 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4916)			

			

I’m sure this is due to my failure to know how to read Lean, but what is the co-product in Matthew’s example? 

Thanks!

David Speyer

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4916&_wpnonce=8005caf29c)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4916#respond)			
		

				
		
- 
		
			
								[xenaproject](https://xenaproject.wordpress.com) says:			

				
				
			[July 30, 2026 at 8:55 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4917)			

			

The base ring is R := ℤ[a, b] / (a³, b³, a²b + 2), the R-Hopf algebra is A := R[U, V] / (U² – abU + b²V, V² – a²V), and the comultiplication on A is defined [here]([https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L581](https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L581)) using `mkAlgHom`. The definition of `mkAlgHom` is [here]([https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L365](https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L365)) — it says “to give an R-algebra map from A to an arbitrary R-algebra S it suffices to supply elements u,v in S satisfying u^2=abu-b^2v and v^2=a^2v”, and so now you can probably guess that the comultiplication is defined by sending U to deltaU defined [here]([https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L553](https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L553)) and V to deltaV defined [here]([https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L550](https://github.com/j2d9w5xtjn-png/mathlib4/blob/3c7eba91d99fb5ef0668e497e1fdad5fb2c81be1/Counterexamples/GrothendieckPower.lean#L550)). Explicitly (modulo typos), U maps to U tensor 1 + (1+aU)(1+bV) tensor U, and V maps to (V tensor 1)*(1+a tensor U)*(1+bV tensor 1) + 1 tensor V. The variables u_1,u_2,v_1_v,2 are U tensor 1, 1 tensor U, V tensor 1 and 1 tensor V. 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4917&_wpnonce=b48e2a6652)Like

			
				[Reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?replytocom=4917#respond)			
		

				
		
- 
		
			
								[David Speyer](http://www.math.lsa.umich.edu/~speyer) says:			

				
				
			[July 30, 2026 at 8:56 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4918)			

			

Thanks!

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4918&_wpnonce=3e72ef6442)Like

			
							
		

				
		
- 
		
			
								[xenaproject](https://xenaproject.wordpress.com) says:			

				
				
			[July 30, 2026 at 10:26 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4919)			

			

I’ve added some more comments to the file in order to make this clearer. Note also the module docstring at the top of the file.

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4919&_wpnonce=8840ae4463)Like

			
							
		

				
		
- 
		
			
								[David Speyer](http://www.math.lsa.umich.edu/~speyer) says:			

				
				
			[July 31, 2026 at 1:36 am](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4920)			

			

Thanks! This is perfectly clear now.

Lots of us talked about this problem in grad school, although I don’t think any of us had any serious idea of how to approach it, so I feel like I should spend a little time trying to understand the counterexample now.

One thing to think about is how mathematical publishing should adapt to the rise of AI. I wonder whether it would make sense for each field of math to run some sort of survey article, every few months, on what new AI results have been proven recently? If I hadn’t happened to read your blog, I never would have learned about this example!

David

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4920&_wpnonce=3f00eb4ffb)Like

			
							
		

				
		
- 
		
			
								[David Speyer](http://www.math.lsa.umich.edu/~speyer) says:			

				
				
			[July 31, 2026 at 3:05 pm](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comment-4921)			

			

I decided that this result was noteworthy enough to add to the big list at MathOverflow [https://mathoverflow.net/a/513790/297](https://mathoverflow.net/a/513790/297) . Please feel free to make corrections or improvements, and thanks for telling me about this! 

[Like](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/?like_comment=4921&_wpnonce=8036a7ceeb)Like

			
							
		

				

			

	

	
		

### Leave a comment [Cancel reply](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#respond)

			
			

Δ
	
	

	
			
		

		
						

- 
				
					Search for:
					
					
				
			
- 

### Categories

			
					
- [Algebraic Geometry](https://xenaproject.wordpress.com/category/algebraic-geometry/)

	
- [computability](https://xenaproject.wordpress.com/category/computability/)

	
- [Fermat's Last Theorem](https://xenaproject.wordpress.com/category/fermats-last-theorem/)

	
- [formalising mathematics course](https://xenaproject.wordpress.com/category/imperial/formalising-mathematics-course/)

	
- [General](https://xenaproject.wordpress.com/category/general/)

	
- [Imperial](https://xenaproject.wordpress.com/category/imperial/)

	
- [Learning Lean](https://xenaproject.wordpress.com/category/learning-lean/)

	
- [liquid tensor experiment](https://xenaproject.wordpress.com/category/liquid-tensor-experiment/)

	
- [M1F](https://xenaproject.wordpress.com/category/m1f/)

	
- [M1P1](https://xenaproject.wordpress.com/category/m1p1/)

	
- [M40001](https://xenaproject.wordpress.com/category/m40001/)

	
- [M4P33](https://xenaproject.wordpress.com/category/imperial/m4p33/)

	
- [Machine Learning](https://xenaproject.wordpress.com/category/machine-learning/)

	
- [mathlib](https://xenaproject.wordpress.com/category/mathlib/)

	
- [number theory](https://xenaproject.wordpress.com/category/number-theory/)

	
- [Olympiad stuff](https://xenaproject.wordpress.com/category/olympiad-stuff/)

	
- [Research formalisation](https://xenaproject.wordpress.com/category/research-formalisation/)

	
- [rigour](https://xenaproject.wordpress.com/category/rigour/)

	
- [tactics](https://xenaproject.wordpress.com/category/tactics/)

	
- [Technical assistance](https://xenaproject.wordpress.com/category/technical-assistance/)

	
- [Type theory](https://xenaproject.wordpress.com/category/type-theory/)

	
- [Uncategorized](https://xenaproject.wordpress.com/category/uncategorized/)

	
- [undergrad maths](https://xenaproject.wordpress.com/category/undergrad-maths/)

			

						
		

		
			
				
		
- 
		

### Recent Posts

		
											
- 
					[The Annals Challenge](https://xenaproject.wordpress.com/2026/08/13/the-annals-challenge/)
											August 13, 2026
									
											
- 
					[Human mathematicians are being outcounterexampled](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/)
											July 20, 2026
									
											
- 
					[Formalizing Fermat workshop](https://xenaproject.wordpress.com/2026/05/15/formalizing-fermat-workshop/)
											May 15, 2026
									
											
- 
					[Accelerating mathematics](https://xenaproject.wordpress.com/2026/02/09/accelerating-mathematics/)
											February 9, 2026
									
											
- 
					[Formalization of Erdős problems](https://xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/)
											December 5, 2025
									
					

					
		

	

	
		

			
				[Xena](https://xenaproject.wordpress.com/)
							

			
								[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)
			

		
	

	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		

		
		

	
		

		Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use. 
To find out more, including how to control cookies, see here:
				[Cookie Policy](https://automattic.com/cookies/)
 

		
		
								
- 
						[Comment](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/#comments)
					
									
- 
						Reblog
					
									
- 
								Subscribe
		Subscribed
							
							
							
															
											
- 
			[Xena](https://xenaproject.wordpress.com)
		
										
									
																						Join 209 other subscribers
																					
										
										
										
										
										
										
																				
											
												Sign me up											
										
									
									
- 
										
											Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fxenaproject.wordpress.com%2F2026%2F07%2F20%2Fhuman-mathematicians-are-being-outcounterexampled%2F&signup_flow=account)										
									
								
															
						
					
							
- 
								
					
					
						
								
- 
			[Xena](https://xenaproject.wordpress.com)
		
								
- 
										Subscribe
		Subscribed
								
														
- [Sign up](https://wordpress.com/start/)
							
- [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fxenaproject.wordpress.com%2F2026%2F07%2F20%2Fhuman-mathematicians-are-being-outcounterexampled%2F&signup_flow=account)
																
- 
										[Copy shortlink](https://wp.me/p9bxpM-ZL)
									
																
- 
									[Report this content](https://wordpress.com/abuse/?report_url=https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/)
								
															
- 
									[View post in Reader](https://wordpress.com/reader/blogs/135737082/posts/3829)
								
															
- 
									[Manage subscriptions](https://subscribe.wordpress.com/)
								
																
- Collapse this bar
														
					
				
			
		
	
	

	
	
				
	

	
	%d
	 

		 	Design a site like this with WordPress.com[Get started](https://wordpress.com/start/?ref=marketing_bar)
