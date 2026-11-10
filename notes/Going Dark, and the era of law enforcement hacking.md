---
title: "Going Dark, and the era of law enforcement hacking"
url: https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/
clipped: 2026-08-31 12:22:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Going Dark, and the era of law enforcement hacking](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/)

## Digest Summary
The post reviews how advances in AI‑driven vulnerability discovery are changing the balance between security and law‑enforcement access. After smartphones adopted passcode‑derived encryption (Apple 2010) and default end‑to‑end encrypted messaging (WhatsApp 2016), U.S. agencies launched the “Going Dark” initiative, seeking mandatory “exceptional access” or backdoors. Instead of court‑mandated access, agencies began purchasing commercial exploits such as GrayKey and Pegasus, while vendors patched vulnerabilities. Recent AI models (e.g., Anthropic’s Mythos, OpenAI, Z.ai, Moonshot) can autonomously locate software bugs at scale, prompting rapid integration of AI‑based scanning into development pipelines. The author predicts that within two years most mature software will have few exploitable bugs left, effectively “going dark” for intelligence and law‑enforcement agencies. This scarcity may revive pressure for mandated backdoors, potentially weakening U.S. software and encouraging foreign adversaries to shift away from U.S. products. The author admits no clear solution, emphasizing the need for careful policy choices as AI reshapes cryptographic engineering.

---

## Full Article

[Skip to content](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/#content)

	

			[Home](https://blog.cryptographyengineering.com/)
	
			[Menu](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/#slide-menu)
	
	
					
				

# Everything is about to “go dark”

						
			[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/)			
				in [Uncategorized](https://blog.cryptographyengineering.com/category/uncategorized/)			

			August 14, 2026August 15, 2026

							1,377 Words
			
					
				
			

	
		

		

	
		

		
			

	
	
		

I’m coming down from spending a few days at [Usenix Security](https://www.usenix.org/conference/usenixsecurity26), right here in my hometown of Baltimore. This means that my days have been taken up with two kinds of conversation: first, explaining to colleagues why Baltimore isn’t actually like [The Wire](https://en.wikipedia.org/wiki/The_Wire). And second, trying not to talk about AI.

Here I’m going to break that second rule. 

I have many worries about what AI means for our field, for various definitions of “field”. But in this post I want to focus on just one thing I’ve started worrying about, and it’s a perverse thing: specifically, I’m concerned that AI is going to make software much too secure.

While that doesn’t sound so bad on the surface, there’s a consequence to this. I mean something very specific: I’m concerned that U.S. intelligence and law enforcement agencies are about to go dark, meaning: that they’re going to suddenly lose a huge portion of their capability. And that this isn’t going to be simply a problem for those agencies, but also for those of us who value computer security and privacy in general.

### Going Dark, and the era of law enforcement hacking

To explain how we got here, we need to talk about recent history. This actually gives me a real excuse to reference The Wire, just because it’s a perfect snapshot of what electronic surveillance looked like way back in 2002. If you’ve seen the first season, you’ll recall that it’s about cops wiretapping drug dealers who use payphones and burners. The mobile phones in the show are relatively new technology for the time, but from a technological perspective nothing in this scenario would have shocked a cop who jumped forward from, say, 1989.

In less than a decade from the premier, everything in those episodes became totally quaint.

The change began in the late 2000s, thanks to the rise of smartphones and texting. Because smartphones can actually store data as well as conveying it, the contents of those phones quickly became a useful new source of law-enforcement capability. Or they were until 2010, when Apple began encrypting iPhone storage using a key derived from the user’s passcode (Android phones followed shortly thereafter.) The next year, Apple deployed end-to-end encryption in iPhone text messages. By 2014, a tiny texting startup named WhatsApp had gathered 600 million users worldwide. By 2016 those users, now nearly a billion strong, were all using default end-to-end encrypted messaging and calls. These two trends — the move from calls to texts, and texts to encrypted data — happened very rapidly. The chart below gives one view of the transition:

The FBI and law enforcement agencies were not insensitive to what was happening. In 2014, Director Comey announced an initiative called [Going Dark](https://www.fbi.gov/news/speeches-and-testimony/going-dark-encryption-technology-and-the-balances-between-public-safety-and-privacy), which would launch a “national conversation” about what providers could do — or be compelled to do — to make these new communications media legible to law enforcement and counterintelligence.

In 2016, the agency quit talking and took their theory to court. When a terrorist attack left the FBI holding a shooter’s locked iPhone, the agency ordered Apple to [give them access](https://en.wikipedia.org/wiki/Apple%E2%80%93FBI_encryption_dispute). The company [refused](https://www.apple.com/customer-letter/). What broke the stalemate — and, to some extent, ended “Going Dark” itself — was something that neither the FBI nor Apple expected. An outside company announced that there was no need for Apple’s assistance: [they could simply hack the phone](https://www.abramslaw.com/media/thought-leadership/new-court-decision-the-fbi-apple-the-company-that-broke-iphone-encryption/).

The Apple v. FBI case has turned out to be a microcosm of the whole Going Dark debate. For the next decade, law enforcement and intelligence agencies continued to ask for “exceptional access” backdoors, but the urgency was gone. Agencies and manufacturers both knew that law enforcement could and would [purchase targeted hacking tools](https://www.reddit.com/r/apple/comments/1gvk6ff/leaked_documents_show_what_phones_secretive_tech/) like GrayKey (for phone unlocking), or even remote exploitation tools like NSO Group’s Pegasus, if they needed them badly enough. Vendors like Apple and Google continued to play a vigorous defense, closing vulnerabilities as soon as they learned about them. But offensive vulnerability hunters consistently managed to keep the edge.

And now there’s a very good chance that all this is about to be history.

### The era of AI bug hunting is here

This April (just four months ago!) Anthropic announced a [new model called Mythos](https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands/) that happened to be unusually skilled at software vulnerability finding. The U.S. government [temporarily blocked](https://www.anthropic.com/news/fable-mythos-access) its export, restricting access to U.S. agencies and trusted vendors. While the ban was dramatic and made for good PR, it turned out to be mostly pointless. [OpenAI](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/), along with Chinese open-weight model labs like [Z.ai](https://www.reuters.com/technology/chinas-zai-says-new-model-nears-anthropics-mythos-5-cyber-defence-tests-2026-08-14/) and [Moonshot](https://www.wired.com/story/moonshot-kimi-k3-ai-model-escape-sandbox/), have since demonstrated that vulnerability finding isn’t something that a single lab is likely to hold a monopoly on. The list of [serious vulnerabilities](https://chatgpt.com/share/6a7f3359-2108-83ea-bd72-3132566ac989) [that these models](https://cvd.z.ai/) have found is getting scarier (or more impressive) by the day.

At first glance, this might seems like good news for the offensive team, and for hackers in general. But I doubt that’s how this will play out in the long term. Defenders are now in the process of patching every bug they can find — often decades worth of bugs — and the backlog feels huge. But they’re making progress. Entire CI toolchains are being rebuilt to incorporate AI-based vulnerability scanning before software ever reaches the point where a human will touch it. While I doubt this means that every bug will be found (even calculating the number of bugs in a piece of code is probably uncomputable), in the real world, it does feel likely that we’re going to hit some sort of a ceiling on the number of useful bugs, and probably we’ll hit it soon.

Thus: over the next two years, major pieces of software are likely to run out of remotely-exploitable bugs.

Obviously I think this is great. But for law enforcement and offensive intelligence agencies, it’s going to be a nightmare. For the first time since 2010, law enforcement might experience what it looks like to really “go dark”, across a huge category of advanced (well-maintained) devices and pieces of software.

### So how is this a problem?

The debate over “exceptional access” mechanisms never really went away. In some places, like the UK, it even [metastasized into something worse](https://support.apple.com/en-us/122234). Here in the US it mostly went into hibernation. Some of the slowdown can legitimately be attributed to expert pushback — academics and industry engineers pointing out the risk that [backdoors might be abused by the very adversaries that Agencies are supposed to be protecting us against](https://en.wikipedia.org/wiki/Salt_Typhoon). But I fear that this was less of a principled pause, and more of a market that was just pricing supply.

The destruction of the low-hanging vulnerability fruit will make law enforcement (and intelligence) agencies’ need much more acute. The demand for constructed, intentional backdoors will re-start in earnest. The result will be enormous pressure on industry to re-architect their systems to make their systems amenable to exceptional access. In some cases, governments will ask for these capabilities in the expectation that they’ll be useful for spying on other governments — a strategy that might have been undetectable in the pre-AI era, but that probably will be less productive now. The results are unpredictable. One result might be that non-US governments entirely remove their dependence on US software. 

The worst part about this dynamic is that these potential new backdoors will probably only affect the countries that demand them, meaning that they will be primarily useful for allowing the US to weaken its own systems. This will in turn allow foreign adversaries to find new ways to attack our communications. This deliberate self-sabotage will happen just at a moment when we’re finally getting a handle on securing our own infrastructure.

### So what do we do about it?

I honestly have no idea. This is not a call to action for experts to rally behind a sophisticated plan. Like so many things about the AI revolution, it’s just occurring to me that we’re on a long greasy slide to a place that will look different than where we are today. Just realizing this doesn’t mean that I have any strategy in mind to avoid it. In this case, we’re just going to have to hope that this time we make the right choices, for no other reason than that they’re right.

	

### Related

	

			
			
							
					

					
						[Matthew Green](https://blog.cryptographyengineering.com/author/matthewdgreen/)
						
							I'm a cryptographer and professor at Johns Hopkins University. I've designed and analyzed cryptographic systems used in wireless networks, payment systems and digital content protection platforms. In my research I look at the various ways cryptography can be used to promote user privacy.						
					

					
				
					
	
			
	
			

	
			

## 
			9 thoughts on “Everything is about to “go dark””		

		
		
					
- 
			
				

				
					

Interesting argument!

I can see a well disciplined and resourced company like Apple using AI to lower the number of security vulnerabilities over time (if they remain focused on quality over profit). However I expect most companies (looking at you Microsoft!) are going to introduce AI slop bugs as they rush to fix other bugs.
				

							
		
		
- 
			
				

				
					

I doubt that if this happens it happens in under a decade, or if it does will be due to manufactured demand. LLMs, at least currently, don’t generate secure code better than a human team, and as Alex Gaynor writes ([https://alexgaynor.net/2026/jul/15/you-cant-bugfix-your-way-out-of-the-vulnpocalypse/](https://alexgaynor.net/2026/jul/15/you-cant-bugfix-your-way-out-of-the-vulnpocalypse/) ) that the bugs that are being found by LLMs right now are specific classes of bugs systemic in the system architectures, and “the most important thing you can do is channel it into systemic fixes”. This can be fixed, through large overhauls of current systems and tooling such as static analyzers, or better testing/fuzzing, but all these take a large amount of effort, by LLMs and humans. This is possible, as seen by Trail of Bits/OpenAI’s Patch the Planet campaign and the recent zlib fuzzing harness, but this is much harder to fit into the codebases of large companies built up over decades, with orders of magnitude more code (and dependencies), while continuing to keep up with their pace of new development and by proxy new vulnerabilities.

This is, of course, just my opinion, but I expect if this doesn’t play out then this entire discussion will be pointless and the jobs of every software engineer and security researcher will be replaced by AnthropenAI’s 7.9 model.
				

							
		
		
- 
			
				

				
					

Maybe there are still enough untapped data sources so that intelligence agencies can pivot and hence aren’t yet completely in the dark.

For example new cars typically are online and collect a ton of telemetry data that isn’t well secured. Same with IoT devices and their lacking security as intelligence agencies are surely happy if “bugs” are planted en masse for them.

There are also plenty of services, particularly financial services, that will always be fully transparent to intelligence agencies. Even Bitcoin turned out fully traceable and only pseudonymous. And following the money trail is still one of the most successful ways to catch criminals.

In the end the security world is as always growing more complex and the intelligence agencies need to adapt. In the foreseeable future the intelligence agencies might be on the back foot but in the never ending security cat and mouse game that will inevitable switch again. I’m sure the intelligence agencies will find creative uses for AI to catch up…

Not sure what role legislation will play but IMHO legislation is typically too slow for the security game as often new legislation becomes obsolete rather fast… The really savvy criminals will only use a tech stack they fully trust anyway and legislation is always pointless in that case.
				

							
		
		
- 
			
				

				
					

Boo-hoo-hoo, poor spies/cops/whatever, they will have to WORK (gasp!) to do their job, instead of just gulp up all of our communications and metadata and location data, everyone of us, all of the time, whether we are suspects in an investigation or not, all the way on the other side of the world or not…

Puhlease…
				

							
		
		
- 
			
				

				
					

Right? The single most effective way to reduce crime is to reduce income inequality and make sure everyone has stable access to food, housing, work, and medical care—something we easily have the capacity to do in a mechanical sense, stymied only by politics (specifically the tendency of the ultra-wealthy to work against these things, to keep people most people on the razor’s edge, so that they can control everything).

Any discussion of downstream issues like encryption and data security is completely pointless without addressing the massive underlying causes of crime.
				

							
		

		
- 
			
				

				
					

The dynamic of “non-US governments entirely remove their dependence on US software” is already in full execution due to cloud/software support pulled due to the wars in EE and ME. With other superpower fully aware of these and NVDA chips ban. So the backdoors, as usual, will primarily impact the countries that push for these.
				

							
		
		
- 
			
				

				
					

Exactly. The digital autonomy movement is stronger than ever, also due to political choices in the US. Having a world less dependent on the US weakens the US for sure but it may make it harder for all nations to all at once keep up with security issues as well. But yeah, the world is heading in an interesting direction.

Maybe the point to make here that the services may need to move back on the infiltration – surveillance axis in the direction of infiltration. 
				

							
		

		
- 
			
				

				
					

Security is an arms race.  There is no perfect defense and there is no perfect infiltration. The same AI tools that make defense better are available to make offense better. The real “casualty” in this is most likely going to be that we will stop producing people who are amazingly good at hacking (and defending). If enough civilization survives the upcoming catastrophe, maybe cyborg/BCI-equipped hackers will become the best operators. 
				

							
		
		
- 
			
				

				
					

An attacker may not need to insert an explicit backdoor at all; instead, they can intentionally introduce an exploitable vulnerability that appears accidental and is optimized to evade the same AI-based vulnerability detector used by the defender. If both sides have access to the detector, the attacker can treat it as an oracle, iteratively modifying candidate vulnerabilities until one remains exploitable while escaping detection. However, this advantage depends on the detector’s capabilities remaining sufficiently stable. In a more realistic setting, defenders may continuously update, retrain, or diversify their detection models, potentially eliminating previously discovered blind spots. The relevant security question is therefore not simply whether an attacker can evade a fixed AI vulnerability detector, but whether detector-aware vulnerabilities can remain evasive under an adaptive defense in which detection capabilities evolve over time.
				

							
		
		

		
	
			

Comments are closed.
	
	

		
		
	

		

		
	

			
			Menu

			

## Menu

			

					
	

	

		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
								
- 
						Reblog
					
									
- 
								Subscribe
		Subscribed
							
							
							
															
											
- 
			[A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com)
		
										
									
																						Join 1,077 other subscribers
																					
										
										
										
										
										
										
																				
											
												Sign me up											
										
									
									
- 
										
											Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fblog.cryptographyengineering.com%252F2026%252F08%252F14%252Feverything-is-about-to-go-dark%252F)										
									
								
															
						
					
							
- 
								
					
					
						
								
- 
			[A Few Thoughts on Cryptographic Engineering](https://blog.cryptographyengineering.com)
		
								
- 
										Subscribe
		Subscribed
								
														
- [Sign up](https://wordpress.com/start/)
							
- [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fblog.cryptographyengineering.com%252F2026%252F08%252F14%252Feverything-is-about-to-go-dark%252F)
																
- 
										[Copy shortlink](https://wp.me/pE4dk-2rw)
									
																
- 
									[Report this content](https://wordpress.com/abuse/?report_url=https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark/)
								
															
- 
									[View post in Reader](https://wordpress.com/reader/blogs/9549322/posts/9394)
								
															
- 
									[Manage subscriptions](https://subscribe.wordpress.com/)
								
																
- Collapse this bar
														
					
				
			
		
	
	

			
			
				
			
		
		

		
			
			
				
				
					
				
				
					
				
			
			
			
				
			
			
			
				
					
						
						
					
					
						
					
					
						
												
											
				
				
					
						
							
						
						
															
									Loading Comments...
								
								
								
									
									
																														
												Write a Comment...
												
												
													
																													
																Email (Required)
																
															
															
																Name (Required)
																
															
															
																Website
