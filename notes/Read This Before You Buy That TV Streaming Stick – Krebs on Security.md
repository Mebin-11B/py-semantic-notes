---
title: "Read This Before You Buy That TV Streaming Stick – Krebs on Security"
url: https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/
clipped: 2026-08-31 12:26:39
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Read This Before You Buy That TV Streaming Stick – Krebs on Security](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/)

## Full Article

Advertisement
	Advertisement
	
	
	
	
	

	
		

			
					
				
		
		
							
												

Security experts have been sounding the alarm for years about the risks of using generic TV boxes that promise unlimited content streaming for a one-time fee, warning that they secretly rent the user’s Internet connection out to strangers. But a groundbreaking new analysis finds these devices also routinely spoof themselves as mobile phones clicking ads on AI-generated websites as part of a sprawling operation that seeks to defraud online merchants and advertising networks.

Pedro Falé is a threat researcher with the security firm Bitsight. Falé told KrebsOnSecurity he was able to peer inside a vast and complex ad fraud network by registering an expired domain name that was used to coordinate fake ad clicks across a particularly popular brand of these streaming devices known as H96.

An H96 TV streaming device currently advertised for sale on Amazon.

Falé said the domain he scooped up was previously used for telemetry, periodically collecting full hardware information and the entire list of installed apps from tens of thousands of H96 streaming sticks plugged into television sets around the globe. But upon inspecting the traffic being funneled to the domain, he discovered nearly all of the TV boxes transmitting data claimed to be mobile phone models from a variety of manufacturers, including Samsung, Vivo, Huawei, and Xiaomi.

“We noticed something was wildly wrong,” Falé said. “Multiple devices reporting to this factory Android TV Box backdoor were ‘phones.'”

Image: Bitsight.

The researcher found all of the devices reported having the same two apps installed, and that those apps were made by a company called Zhejiang Fengwo IoT Technology Ltd, an entity founded in 2019 in mainland China which operates an ad-publishing portfolio under the name Fengwo Group. Further investigation into the Fengwo Group revealed it has registered multiple patents that match the inner workings of these apps.

“Bitsight TRACE identified several Hong Kong, Singapore, and single person ‘legal’ shell identities used to collect the monetization and traced the operation back to a mainland China company known as Zhejiang Fengwo IoT Technology Co., Ltd, which operates under the Fengwo Group,” Falé [wrote](https://www.bitsight.com/blog/fuyao-enterprise-building-ad-fraud-empire-ai-and-kids-coding-blocks) in a report released today about their findings.

Falé said an analysis of the apps shows they help to coordinate an ad fraud network that uses these H96 devices as a captive traffic source to click on ads at AI-generated websites operated by the Fengwo Group.

Bitsight discovered the websites contain machine-generated news articles and graphics across a range of categories, including finance, health, education, gaming, music and food blogs. But they also found none of those sites displayed ads unless the device visiting the page matched the spoofed mobile profile of these H96 devices.

## AI DIGITAL HUMANS

The domain for the Fengwo Group — fwgcloud[.]com — claims the company is “redefining the boundaries of human-AI interaction,” and that it has created more than 120,000 “AI digital humans” available to rent for everything from emotional companionship to 24/7 customer service and creative design.

The homepage for fwgcloud dot com.

Falé said the Fengwo Group’s domain shared its SSL certificate data with other domains associated with the apps found on H96 devices, specifically the phone spoofing mechanism. He noted the domain also has an internal wiki platform that directly ties the Fengwo Group to a proprietary implementation of a Google-built visual programming language called Blockly, which was originally designed to help kids learn how to write software.

According to Bitsight, the Fengwo Group’s employees use Blockly to build the sham websites, allowing low-skilled operators to drag blocks of code together in their Blockly editor — without any need to understand what the underlying code blocks do or how they work.

The Blockly homepage.

“An operator can drag blocks together in their Blockly editor, to define each fraud routine, given a task type,” reads Bitsight’s report. “Once the routine is saved, it gets exported as JavaScript and uploaded to the S3 buckets. An operator doesn’t need as much understanding of the underlying technicalities, as it is all set in place for ease of use.”

Bitsight even found one of the Fengwo Group app developers mentioning exactly these advantages, noting the developer remarked that “only a small number of highly-skilled developers are needed to build the template execution-unit images,” and that “developers who create execution units from those templates have significantly lower technical requirements, greatly reducing the company’s operating costs.”

Falé said if a user’s H96 streaming stick is selected for a specific fraud task, it will be pushed the appropriate Blockly module according to the task desired, which can include silently launching a web browser, visiting websites, browsing pages, managing tabs, and clicking on ads.

To ensure the TV boxes masquerading as mobile phones can reliably click on ads displayed via the AI-generated websites, the Fengwo group “fuses three vision and reasoning systems into a single interface,” allowing the bots to correctly identify an ad on the webpage and navigate the site much like a human would, the Bitsight report observed.

Examples of ad landing pages linked to the Fengwo Group. Image: Bitsight.

## TV ON? PROXY. TV OFF? AD FRAUD

Bitsight found the H96 devices were either relaying residential proxy traffic or participating in ad fraud, but never both at the same time. In fact, they concluded that when these TV boxes detect an HDMI signal from an attached television — indicating the user intends to stream video content — the box is usually functioning as a residential proxy. When the TV is off, it switches back to waiting for ad fraud jobs.

Falé said he believes the TV boxes are set up this way because its ad fraud activities are far more resource intensive and could interfere with the device’s stated purpose — streaming video content over the Internet.

Despite repeated [warnings from the FBI](https://www.fbi.gov/investigate/cyber/alerts/2025/home-internet-connected-devices-facilitate-criminal-activity) and security industry leaders about the security and privacy risks of using these streaming devices, major e-commerce providers like Amazon, Best Buy, Newegg and others continue to sell hundreds of different models and brands that bundle unofficial versions of Google’s Android operating system and are frequently marketed ([via online influencers](https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/)) as a way to access a broad array of streaming services and live broadcasts without a subscription.

Image: fbi.gov.

In addition to enlisting the user’s TV box in ad fraud networks, these off-brand streaming devices almost universally come with residential proxy software pre-installed. This software rents the user’s Internet address out to anonymous paying customers, who run the gamut from aggressive content scraping firms to ticket scalpers and outright cybercriminals.

What’s more, because these generic (and generally dirt cheap) TV boxes are all horribly insecure by default and bereft of any kind of authentication, installing one on your home or office network only invites further mischief. In January, the proxy tracking service Synthient documented how multiple botnets had [rapidly enslaved millions of TV boxes](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) using a complex interplay of security vulnerabilities in both the residential proxy software and the streaming devices themselves.

## SHOW ME THE MONEY

Bitsight said it tracked approximately 38,000 TV boxes globally phoning home to the expired Fengwo Group domain, and based on that number the report estimates this ad fraud network brings in revenues of close to $50,000 a day (not counting substantial revenue from the residential proxy side of the business). However, Falé emphasized that these estimates are highly conservative and based on telemetry from just one of the Fengwo Group’s core (but older) domains.

As for the Fengwo Group’s claim to have 120,000 “digital humans” at their disposal, Bitsight’s report concludes it could be just a clever marketing scheme and/or a way to avoid drawing suspicion to the company’s operations.

“Historically, when dealing with proxy services or DDoS, we sometimes see these websites undertake inconspicuous facades, so as not to advertise their DDoS capability or botnet size,” Falé wrote in the report. “This could also be the case here.”

If the Fengwo Group truly does have tens of thousands of “AI humans” at its beck and call, it does not appear to have dedicated any of them to fielding inquiries from its own website. KrebsOnSecurity sought comment from the Fengwo Group by emailing the contact address listed on the company’s homepage, but the request bounced back with the reply, “Your message couldn’t be delivered to postmaster@fwgcloud[.]com. Their inbox is full, or it’s getting too much mail right now.”

As Bitsight’s analysis shows, when it comes to TV boxes and streaming sticks, it’s best to stick to name brands from reputable manufacturers, and then to be sparing and careful with any apps you choose to install on the device — as [many of those can bundle residential proxy software as well](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/). Google says consumers can confirm whether or not a device is built with the official Android TV OS and Play Protect certification by following [these instructions](https://support.google.com/googleplay/answer/7165974).

Additionally, Synthient maintains [a running list of IoT devices](https://github.com/synthient/public-research/blob/main/2026/01/kimwolf/product_names.csv) that have been known to ship to consumers with residential proxy software and other malicious apps pre-installed. Careful readers will notice Synthient’s list includes other IoT devices apart from streaming sticks and boxes: As the FBI has warned, residential proxy software has also been found in other popular consumer IoT devices from random brands, particularly digital photo frames.
											
		
			
	
	

	
		
			
					

				


	
			

## 
			51 thoughts on “Read This Before You Buy That TV Streaming Stick”		



		
				
- 
		
			

			
			
				

Fake news
							

			
							
		
	
	
- 
		
			

			
			
				

*** Install me now to get free access to all channels ***
							

			
							
		
	
	
- 
		
			

			
			
				

^ fake person
							

			
							
		
	
	
- 
		
			

			
			
				

I think **you** are the fake news
							

			
							
		
	

	
- 
		
			

			
			
				

I suppose your primary reader base understands well enough, but a one-sentence explanation of ad fraud would strengthen this article!
							

			
							
		
	
	
- 
		
			

			
			
				

Please do explain ad fraud.
							

			
							
		
	
	
- 
		
			

			
			
				

Many ads are pay-per-click so you can make money by setting up crappy websites with ads and then having bots visit them and click on the ads.
							

			
							
		
	
	
- 
		
			

			
			
				

it isn’t 2013
							

			
							
		
	

	
- 
		
			

			
			
				

If you are browsing an online newspaper and you click an ad, the advertiser pays the publisher for that click.  The publisher’s content brought you to the page, and once there, you clicked an ad that brought you to the advertiser’s site.  These payments are the publisher’s revenue stream (aside from subscriptions, if they offer those), and the advertiser spent that money because they are buying your attention.

This company Fengwo is using Blockly + cheap developers to build absolute trash “news” sites full of AI-slop “articles” that no human would read.  They have no audience, no humans visit these websites.  Fengwo uses the TV sticks to make it look like the sites have a lot of traffic from humans on mobile phones, which is why sticks are masquerading as Samsung and Xiaomi devices.  And because the sites appear to have visitors, Fengwo can sign up with online ad networks (“we’re a sports news site and we have 10,000 unique visitors a month, look at our traffic stats!”) that will run ads on those fake news articles.  When a TV stick clicks on an ad, it looks like a human clicked that ad, and so the advertiser pays the “publisher” (Fengwo in this case) and the ad network in the middle takes a cut.  This is how advertising makes the internet free for users – you don’t pay for Facebook or pay to use Google search because the advertisers are paying Meta and Google for your ad clicks while you are using those services.

The “fraud” here is that the advertiser doesn’t want to show ads to bots, bots don’t buy sneakers and shampoo.  Fengwo is not a real publisher (they are not paying reporters and designers to create compelling content that brings real humans to their sites), they are using their TV stick bot network to make it seem like they are operating legit content sites to attract advertisers and then using fake clicks to steal money from advertisers.
							

			
							
		
	
	
- 
		
			

			
			
				

Thanks.

But what happens when peopl euse ad blockers.  Is there any way that those blocked ads somehow get clicked also?  I always wondered about this.
							

			
							
		
	
	
- 
		
			

			
			
				

The ad blocker applies not to the ad (the source), but to the ad being displayed at your local instance (the sink). So, an ad blocker will remove you from the revenue stream mechanism that Meg G. described, but will not change it.
If a website or service provider notices that their ads do not get delivered to you (they would need to make an effort to measure this) then they might decide to block you from using their service.
However, this does not affect the bot networks, because these obviously will happily click away without the owner of the TV and stick ever noticing.
							

			
							
		
	

	
- 
		
			

			
			
				

vine ripened tomato and pedro up there provided two of em
							

			
							
		
	

	
- 
		
			

			
			
				

Just unplug the stick when you’re not using it.
							

			
							
		
	
	
- 
		
			

			
			
				

Unplug the stick when you’re not using it! Problem solved.
							

			
							
		
	
	
- 
		
			

			
			
				

Tell me you didn’t read the part where he said it does ad fraud while it’s connected without telling me …
							

			
							
		
	
	
- 
		
			

			
			
				

did they invent wireless electricity where you’re from?
							

			
							
		
	
	
- 
		
			

			
			
				

How can you use the TV stick without connecting it?
							

			
							
		
	
	
- 
		
			

			
			
				

Umm … it works while you’re using it. Unplugging it prevents its use for ad fraud but still allows it to function as a residential proxy while you’re watching tv. Read gooder?
							

			
							
		
	
	
- 
		
			

			
			
				

Did you not read the part where it said it does the ad clicking only when the stick isn’t being used to stream?  If you unplug it after streaming, it no longer clicks the ads.  People really can’t be this dense.
							

			
							
		
	
	
- 
		
			

			
			
				

But will you always remember to unplug the TV every time you finish using it? Sooner or later someone will forget.
							

			
							
		
	
	
- 
		
			

			
			
				

Did YOU not read the part where while it is being used to stream it is functioning as a proxy that is being used for other fraud/illegal activities? Having this thing plugged in EVER is bad.
							

			
							
		
	

	
- 
		
			

			
			
				

WHAT STICKS LIKE THIS NEED ARE ON-OFF SWITCHES ON THE EXTERNAL PART OF THEIR STICK WHICH DISENGAGES THE CIRCUIT PHYSICALLY.
							

			
							
		
	

	
- 
		
			

			
			
				

Have this exact model. Last night it halted on ATV boot.
It did a android update, then disabled the existing Prime app. Also tasked me with updating Play Store Uninstalled Prime, downloaded a diff version from Playstore, and AMZ worked fine again.

I was enthused that H96 was doing software updates. Not so much now.

This unit is used on multi units, but not left plugged into the HDMI. So port blocking may help?
							

			
							
		
	
	
- 
		
			

			
			
				

throw it in the bin unless you’re cool with knowingly facilitating fraud.

If you’re of the nerdy variety, I recommend installing something like LibreELEC on an SBC/mini PC instead.
							

			
							
		
	
	
- 
		
			

			
			
				

You’re asking about the safety and legitimacy of a TV box that goes ahead and uninstalls the apps you installed so that it can install its own app store and make you re-download these apps from them? No, that doesn’t sound sketchy at all. If you continue to use this device, you will be enabling ad fraud and cybercrime, full stop. Clear enough?
							

			
							
		
	

	
- 
		
			

			
			
				

When I write The History of the Decline and Fall of Internet I’m going to need a lot more than 6 Volumes and 12 years.
							

			
							
		
	
	
- 
		
			

			
			
				

Yeah I have been trying to figure out how many pages it would take to write a proper popular science book on the history of cybercrime and it turns out I don’t think one could be written anymore. It would probably need one of those 10-16 volume sets where each book covers a 5-10 year period from the 1960s or 1970s on, and a book to cover the entire period before then. I would enjoy writing that but certainly not without being paid upfront and I am not seeing that. One nice thing about AI is it still cannot compose nonfiction without data and much of that is not documented.

Hey, Brian, what percentage, do you think, of cybercrime goes in prosecuted now versus in the past? In the 1980s and 1990s it was sorta rare because it was hard to track and prosecute and kinda rare comparatively (heck, the ability to do data taps didn’t even exist until the early 1990s, and leaving backdoored binaries was pretty rare until the late 1990s/early 2000s), then I think it became a percentage game since there are just so many skids, thieves, state actors and crazies now that most victims never even manage to get a case opened. It often strikes me as weird which ones do that aren’t big money cases.

An overview series of books would be neat. Not like grab all these different ones but something recent that doesn’t go TOO deeply into any specific case or require legal cases.
							

			
							
		
	

	
- 
		
			

			
			
				

Is Zapper Box vulnerable in any way shape or form?
							

			
							
		
	
	
- 
		
			

			
			
				

Europeans and Americans disagree on account of the colour of the zuppa
							

			
							
		
	

	
- 
		
			

			
			
				

Brian, but what if the device does NOT come pre-infected?
In the world of auto-updates of software and firmware, even the hardware which is now completely legal and crap-free, could convert itself to a proxy or ad network later any time.
							

			
							
		
	
	
- 
		
			

			
			
				

True, see for example the recent case of Windows Update installing adware after an LG monitor is connected. 

The solution is to only use devices with Open Source OSes that you control, and look at what updates contain before applying them.
							

			
							
		
	

	
- 
		
			

			
			
				

I have a brother-in-law that uses one of these devices on his TV. I’m also pretty sure that if I brought this up to him and explained to him what was going on in the background he could care less. As long as he gets cheap TV and gets to screw the man by not paying paying for the streaming service, he he could care less. I’m sure he’s not alone.
							

			
							
		
	
	
- 
		
			

			
			
				

THIS!  98% of the people are the same.
							

			
							
		
	
	
- 
		
			

			
			
				

Perhaps it might help to convince him if you point out that he’s sporting the electric bill for the fraudster? The bill’s probably not very high, but it reframes it as him also being taken advantage of.
							

			
							
		
	
	
- 
		
			

			
			
				

too true.
							

			
							
		
	

	
- 
		
			

			
			
				

1. Does this mean that the ad revenue earned in previous years by the Fraud Provider (insert name here) is supect? YES.
2. Does it mean that the payouts can be retrieved by those large ad companies like Google or Amazon? Maybe.
3. Does it mean that the millions of small and medium businesses that paid these ad companies for thousands of “clicks” (which were not real human clicks!) can recover what they paid?  NO WAY.

What a sad state of affairs.
							

			
							
		
	
	
- 
		
			

			
			
				

what about brand name TV boxes such as Xiaomi? I don’t bother with them myself (I use a hardwired HDMI out connection from my phone for streaming) but I promised to set up a few of these boxes for tech phobic elder friends want the feel if a cable box and a remote.
Brand name suggestions would be super appreciated, thank you!
							

			
							
		
	
	
- 
		
			

			
			
				

Is this in anyway related to Ningo Fengwo group? (A prominent group linked to well known families)
Mentioned here:
[https://michael7924.substack.com/p/chinese-turbocharging-maker-terminates](https://michael7924.substack.com/p/chinese-turbocharging-maker-terminates)
and
[https://min.news/en/economy/dd0c59854fc23ac7c8d9b4fad57e3360.html](https://min.news/en/economy/dd0c59854fc23ac7c8d9b4fad57e3360.html)

Can you clarify please.
							

			
							
		
	
	
- 
		
			

			
			
				

China.  Soon hard drives will wifi your data back to ccp.
							

			
							
		
	
	
- 
		
			

			
			
				

Look from this “angle”  – This fraudulent scheme financially benefits the CEO of Fengwo Holding Group while actively exploiting small, medium, large and home businesses across the world (US, Europe, and Asia). These companies invest their (sometimes limited) budgets to promote their brands, but their marketing efforts reach are diminishing. Ultimately, the invested funds are pocketed directly by the Fengwo Group.
							

			
							
		
	
	
- 
		
			

			
			
				

Hot take: fake-clicking on ads is a good thing. Make advertisements worthless, because they’ve infiltrated every part of our homes. Make it unprofitable to run ads and let’s bring the price of services to where it belongs. Instead of free gmail that steals all your data you pay $2/mo for a normal service with privacy.
							

			
							
		
	
	
- 
		
			

			
			
				

“fake-clicking on ads is a good thing” ehhhh… not when someone is unwittingly paying for the electricity and someone else is making a profit off it. 

Besides, we’ve seen over the past 85 years or so that when ads become unprofitable they throw more ads at us, tell us we can get rid of the ads by paying, and then throw ads at the people who pay too. This is not the way to get rid of ads. Block ads on your network and don’t patronize any service that forces them on you.
							

			
							
		
	
	
- 
		
			

			
			
				

@Jimothy

Paid ad-free webmail exists. Posteo is one for €/$1 per month. I’ve been pretty happy with it for the most part.
							

			
							
		
	
	
- 
		
			

			
			
				

The problem with paid email is it links your financial information to your email. I don’t mind so much paying for something like email with actual money, but I don’t like app stores managing and tracking that, and I don’t like the feeling of my email and real name and address all being collected. It’s one of the things I am grateful are not all “paid for” services FOR privacy reasons. Hard enough to have even a single scintilla of privacy even without that (you might think there is, but let me teach you a think or two about PII and IPs.
							

			
							
		
	

	
- 
		
			

			
			
				

While I agree with your POV, the fundamental intent of these boxes and who they are marketed to simply isn’t the “I’ll pay more for _____” group.  You & I are in the “I’ll pay more for better privacy & security group”…the people that buy these devices are in the “I only care about cheap / free TV group”.  Where you & I should agree to disagree is around advertising / click fraud.  Make these ads worthless and the universe’s real money machine – advertising – will figure out a way to advertise.
							

			
							
		
	

	
- 
		
			

			
			
				

Clearly you never spent decades of the best years of your life coding and backdooring internet enabled devices and routers, or you would have an inkling as to why it isn’t that easy unless you are the vendor or some third party contracted by them to provide the software.
							

			
							
		
	
	
- 
		
			

			
			
				

Website for incompetence lawyers is this
							

			
							
		
	
	
- 
		
			

			
			
				

Hello,
my honeypot just got a remote code execution attempt with the user agent: KrebsOnSecurity.
It seems the bad boys have noticed your article. 😀 (reach out to me if you are interested on the full data I gathered)
							

			
							
		
	
	
- 
		
			

			
			
				

Be generous and tell us which port and type.

“the bad boys have noticed your article.”
Yeah which one.
							

			
							
		
	

	
- 
		
			

			
			
				

The detail about the device checking for an active HDMI signal before switching between proxy relaying and ad fraud is particularly wild. It’s a clever, if malicious, way to ensure the user doesn’t notice any performance degradation while actively watching TV. Most people assume cheap hardware just runs poorly because of bad components, never suspecting an entire background operation is pausing just to keep the video stream smooth. It really shows how sophisticated these low-cost hardware supply chain exploits have become.
							

			
							
		
	
	
- 
		
			

			
			
				

sWhy no link to subscribe and  cost?
							

			
							
		
	
		

		
				

Comments are closed.
		
	
	

			
		
	


			

        Advertisement

                        Advertisement

			
				
		
	
	
				
                				
				
								
				
								
	

	
					© Krebs on Security - [Mastodon](https://infosec.exchange/@briankrebs)
