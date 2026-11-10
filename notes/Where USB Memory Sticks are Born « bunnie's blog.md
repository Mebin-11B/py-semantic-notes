---
title: "Where USB Memory Sticks are Born « bunnie's blog"
url: https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/
clipped: 2026-08-31 12:26:42
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Where USB Memory Sticks are Born « bunnie's blog](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/)

## Full Article

[« Name that Ware, February 2013](https://www.bunniestudios.com/blog/2013/name-that-ware-february-2013/)
			[Winner, Name that Ware February 2013 »](https://www.bunniestudios.com/blog/2013/winner-name-that-ware-february-2013/)
		

		
			

## Where USB Memory Sticks are Born

			
				

In January, I had the fortune of being a [keynote speaker at LCA2013](http://www.australianscience.com.au/interviews/do-what-it-takes-to-solve-the-problem-and-no-more-a-small-talk-with-bunnie-huang/). One of the [tchotchkes](http://www.merriam-webster.com/dictionary/tchotchke) I received from the conference organizers was a little USB memory stick.

I thought it was a neat coincidence that I was in a factory that manufactured exactly such memory sticks about a week before the conference. In fact, I managed to score a rare treat: the factory owner gave me a sheet of raw chip-on-flex, prior to bonding and encapsulation, to take home.

The USB sticks start life as bare FLASH memory chips. Prior to mounting on PCBs, the chips are screened for capacity and functionality. Below is a photo of the workstation where this happens:

In the image, you can see stacks of bare-die FLASH chips, awaiting screening with a probe card. I love the analog current meter and the use of rubber bands to hold it all together. The probe card has tiny needles on it that touch down on microscopic (less than 100-micron square) contacts on the chip surfaces. Below is what a probe card looks like.

Below is an image through the microscope on the micro-probing station, showing the needles touching down on the square pads at the edge of the FLASH chip’s surface.

Interestingly, this all happens in an absolutely non-clean-room environment. Workers are pretty much handling chips with tweezers and hand suction vises, and mounting the devices into these jigs by hand.

Once the chips are screened for functionality, they are placed by hand onto a PCB. This is not an unusual practice, pretty much every value-oriented wirebonding facility I’ve visited relies on the manual placement of bare die. The photo below shows a controller IC being placed on a panel of PCBs. The bare die are in the right hand side of the photo, sitting in the beige colored waffle pack.

The lady is using some sort of tool made out of hand-cut bamboo. I still haven’t figured out exactly how they work, but every time I’ve seen this process they are using what looks like a modified chopstick to place the chips on the board. My best guess is that the bamboo sticks have just the right surface energy to adhere to the silicon die, such that silicon will stick to the tip of the bamboo rod. A dot of glue is pre-applied to the bare boards, so when the operator touches the die down onto the glue, the surface tension of the glue pulls the die off of the bamboo stick.

It’s trippy to think that the chips inside my USB stick were handled using modified chopsticks.

The chips are then wirebonded to the board using an automated bonding machine which uses image recognition to find the location of the bond pads (this is part of the reason they can get away with manual die placement).
[https://bunniefoo.com/ntw/usb1q13.mp4](https://bunniefoo.com/ntw/usb1q13.mp4)

([view in HD](http://bunniefoo.com/ntw/usb1q13_hd.mp4))

The first half of the video above starts out with the operator pulling off and replacing a mis-bonded wire by hand, and re-feeding the wire into the machine. Given that these wires are thinner than a strand of hair, and that the bonding pads are microscopic, this is no mean feat of manual dexterity.

Here’s a scan of the partially-bonded but fully die-mounted PCB that I was given as a memoir from my visit (I had since crushed some of the wire bonds). The panel contains eight USB sticks, each consisting of a FLASH memory chip and a controller IC that handles the bridging between USB and raw FLASH, a non-trivial task that includes managing bad block maps and error-correction, among other things. The controller is probably an 8051-class CPU running at a few dozen MHz.

Once the panels are bonded and tested, they are overmolded with epoxy, and then cut into individual pieces, ready for sale.

Interestingly, the entire assembly prior to encapsulation is flexible. The silicon chips have been thinned down by grinding off their back sides to the point where they can tolerate a small amount of flexing, and the PCB is also so thin, it is flexible.

For those of you interested in this kind of thing, here’s the die marking from the FLASH chip; apparently it is made by Intel:

Here is also a die shot of the controller chip:

And now you know where those tiny USB thumb drives are born.

Thanks to David Cranor for contributing images. Images used with permission.

PS: chopsticks

								
				

					
												This entry was posted on Tuesday, February 12th, 2013 at 12:56 am and is filed under [Made in China](https://www.bunniestudios.com/blog/category/chumby/made-in-china/).						You can follow any responses to this entry through the [RSS 2.0](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/feed/) feed. 

													Both comments and pings are currently closed.
						
					
				

			
		

	

	

### 27 Responses to “Where USB Memory Sticks are Born”

	
		
		
	

	
			
- 
				
				
						[jstults](http://www.variousconsequences.com) says:		
		
		
			[February 12, 2013 at 1:10 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1196601)		

		

No pics of the station where they load the spyware?

		
				
				
		
- 
				
				
						Brett_cgb says:		
		
		
			[April 28, 2013 at 2:38 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219107)		

		

It’s in there – you just missed it.

You don’t think that the only thing they at the die testing station is test the dice? They have everything they need for programming the dice.

(I don’t seriously believe that spyware is loaded, but this could be where customer specified preloaded files would be written to the dice.)

		
				
				
		
- 
				
				
						Willrandship says:		
		
		
			[April 28, 2013 at 11:22 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219297)		

		

Unless they’re ordering in major bulk, the customer-specified preloading would be easier to do on finished products. Adding on a process is easier than modifying one in this case, IMO. You can just grab the number you need from the pile of drives in the nearest bin, instead of setting up a dedicated line to programming the chips during construction.

		
				
				

		
- 
				
				
						[J. Peterson](http://www.saccade.com) says:		
		
		
			[February 12, 2013 at 3:48 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1196639)		

		

Wow – fascinating.  Magic chopsticks – who would’ve guessed?

Do you know how the needles on the test jig are set into place?  This seems like an exacting job that needs to be re-done for each new chip that comes onto the line.  Is there a special manufacturer for them, or does the factory fabricate them themselves?

		
				
				
		
- 
				
				
						Brett_cgb says:		
		
		
			[April 28, 2013 at 2:41 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219109)		

		

I believe there is an entire industry that supports making probe cards (PCBs with carefully mounted probe needles). Every silicon manufacturer has to test their product, and they all need probe cards.

		
				
				

		
- 
				
				
						[Four short links: 12 February 2013 - O'Reilly Radar](http://radar.oreilly.com/2013/02/four-short-links-12-february-2013.html) says:		
		
		
			[February 13, 2013 at 7:35 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1197098)		

		

[…] Your USB Sticks Are Made With Chopsticks (Bunnie Huang) — behind-the-scenes on how USB sticks are made. […]

		
				
				
		
- 
				
				
						Semilog says:		
		
		
			[February 13, 2013 at 1:08 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1197165)		

		

Chopstick or spudger? 

[http://en.wikipedia.org/wiki/Spudger](http://en.wikipedia.org/wiki/Spudger)

		
				
				
		
- 
				
				
						bunnie says:		
		
		
			[February 13, 2013 at 3:28 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1197197)		

		

If someone put a pair of these in front of me in a Chinese restaurant I would use them to eat my food without question. :)

		
				
				

		
- 
				
				
						Nate says:		
		
		
			[February 14, 2013 at 3:07 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1197403)		

		

I use chopsticks all the time for working with small solder joints. The balsa ones are better than bamboo if you want more absorption (say, flux).

You don’t need a clean room for working with the die after it’s been manufactured. Depackaging and rebonding work fine in a normal household environment, just ask Chris Tarnovsky.

		
				
				
		
- 
				
				
						[openmakersdaily](http://www.openmakersdaily.org) says:		
		
		
			[February 14, 2013 at 8:57 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1197698)		

		

I already had some keys like that and I had a question: 

what are the two 0603 sized pads at the opposite of the usb connector made for? I never had the time to solder a LED in this place :)

(they are visible in groups of 4 in usb1q13_back.jpg )

		
				
				
		
- 
				
				
						[Wait Out The Cold With These 14 Articles From Throughout The Week | Macgasm](http://www.macgasm.net/2013/02/16/wait-out-the-cold-with-these-14-articles-from-throughout-the-week/) says:		
		
		
			[February 17, 2013 at 12:29 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1198520)		

		

[…] Where USB Memory Sticks are Born, USB sticks are assembled in a less than high-tech environment. […]

		
				
				
		
- 
				
				
						karabo says:		
		
		
			[February 20, 2013 at 2:16 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1199794)		

		

tell me something, how much would that cost, with branding?

		
				
				
		
- 
				
				
						[Ian Farquhar](http://dreamscape.com.au) says:		
		
		
			[February 26, 2013 at 3:16 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1201564)		

		

What surprises me is that the flash suppliers haven’t integrated a controller onto the flash die.  Same for SD cards, where the controller chip is usually piggy backed onto a corner of the flash.

Is this some process issue, perhaps?  Given the easy integration of flash blocks in normal logic, I would expect not, but maybe not at the extreme levels of density here.  Even so, this is hardly like a DRAM process.

Given that portable storage is currently the largest consumer of medium-capacity flash dies, and it is an incredibly cost-sensitive market, surely there is a technical reason this isn’t done?

		
				
				
		
- 
				
				
						[mingqianguo](http://dzsc.com) says:		
		
		
			[March 2, 2013 at 7:44 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1202723)		

		

Controller need high ESD protection, USB support 5v signal but smaller process is harder to protect, more easily to damaged by high voltage.

		
				
				
		
- 
				
				
						Jarrow says:		
		
		
			[May 6, 2013 at 1:15 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1220840)		

		

You called it.  The chip fabrication procedures for memory and CPU differ considerably.  Trying to shoehorn controllers onto memory wafers dramatically decreases flawless yields.  Given how cutthroat the commodity fab business is, that would quickly send the experimenter out of business.  

That is not to say that someone with a large enough bankroll and a good enough fab couldn’t built a process that does it cost competitively, but it would probably take tens to hundreds of millions to build up, and would be money lost with the next drop in feature size. 

Realistically, until we get to the point of widescale custom printing on an atomic scale, separate chips made with separate processes are more cost effective.

		
				
				

		
- 
				
				
						Michael says:		
		
		
			[March 1, 2013 at 6:26 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1202470)		

		

For those that are curious, a L73A die is a MLC 32Gb NAND device built on a 29nm process (probably at the IMFT facility).

		
				
				
		
- 
				
				
						alex says:		
		
		
			[March 12, 2013 at 8:20 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1205253)		

		

hi Bunnie,

how can i contact you in private ?

I would to develop a new idea with UDP’s manufacturers and I have seen pictures of those factories in your blog.

Thanks 

Alex ( from Spain )

		
				
				
		
- 
				
				
						[game cards](http://www.gamecardmarkt.nl) says:		
		
		
			[April 9, 2013 at 7:40 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1213929)		

		

Hi bunny, i would like to ask for some think ee in priv, can you give me your fapange or twitter? best

		
				
				
		
- 
				
				
						[rndm(mod) » Hand placing flash die to make USB drives](http://randommod.com/2013/04/27/hand-placing-flash-die-to-make-usb-drives/) says:		
		
		
			[April 27, 2013 at 9:10 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219042)		

		

[…] It’s a stretch to call this one a hack, but USB thumb drives are around us constantly and we always assumed that the boards inside were machine populated (like with a pick and place machine). [Bunnie] tells us otherwise. He recently had the chance to tour a factory where USB flash drives are made. […]

		
				
				
		
- 
				
				
						[Hand placing flash die to make USB drives | Make, Electronics projects, electronic Circuits, DIY projects, Microcontroller Projects - makeelectronic.com](http://makeelectronic.com/hand-placing-flash-die-to-make-usb-drives.html) says:		
		
		
			[April 28, 2013 at 12:57 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219084)		

		

[…] It’s a period to summons this digit a chop, however USB thumb forces are about us constantly furthermore we always putative that the accommodates confidential were robot populated (comparable beside a harvest besides arrange device). [Bunnie] recounts us else. He recently had the adventure to trip a workshop where USB flare compels are made. […]

		
				
				
		
- 
				
				
						Freidoun says:		
		
		
			[April 28, 2013 at 2:09 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219102)		

		

Nothing special with bamboo stick. I wet them with propanol , small items stick to the tip and are released when dried or soldered/glued

		
				
				
		
- 
				
				
						Jonam says:		
		
		
			[April 28, 2013 at 6:08 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219261)		

		

I am amazed that this sort of process is still being done for these USB Flash drives.

Way back in 1985 when I was doing my uni thesis on IC design, my University would get multi-project chips made at a local foundry. To make use of the relevant part of the chip for my work, I had to manually place (using Araldite) and then wire bond bare chips onto a PCB to allow me to test and use each die.

It was difficult work in that the wire-bonding machine was an old Kulicke and Soffa wedge bonder that the Uni must have got second-hand from somewhere. Often, due to problems with the machine, I would have to do a fair bit of rework using the finest tweezers and scalpel blades I could get from RS components. Happy days!

		
				
				
		
- 
				
				
						Alex says:		
		
		
			[April 30, 2013 at 6:28 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1219755)		

		

hi Bunnie,

how can i contact you in private ?

I would to develop a new idea with UDP’s manufacturers and I have seen pictures of those factories in your blog.

Thanks

Alex ( from Spain )

		
				
				
		
- 
				
				
						[Flash memory through the ages | Parallel Points](http://parallelpoints.com/flash-memory-through-the-ages/) says:		
		
		
			[May 5, 2013 at 4:50 am](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1220577)		

		

[…] was reading bunnie’s recent post on the manufacturing techniaues used in USB flash-drives… bare die manipulated by hand with a […]

		
				
				
		
- 
				
				
						[Pen drive Malaysia](http://www.itgifts.com.my) says:		
		
		
			[July 1, 2013 at 6:35 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1236901)		

		

What a comprehensive usb flash drive article.

Have learn something useful today.  

Greeting from Malaysia!!

		
				
				
		
- 
				
				
						[http://pyry.lehdonvirta.com/](http://pyry.lehdonvirta.com/2011/12/13/timo-soini-suoritti-suomen-historian-suurimman-trollauksen/) says:		
		
		
			[July 31, 2013 at 9:23 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1249539)		

		

What i do not understood is in fact how you
are now not actually much more well-favored than you may be right now.

You are so intelligent. You understand thus significantly
relating to this matter, produced me in my view believe it from a lot of numerous
angles. Its like women and men aren’t involved until it is something to do with Woman gaga! Your personal stuffs nice. All the time handle it up!

		
				
				
		
- 
				
				
						Pasquale says:		
		
		
			[September 24, 2013 at 10:43 pm](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/#comment-1270793)		

		

Hello Bunnie,

I need to talk to this company or similar. Can you tell me the name or the site of this manufacturer.
In advance thank you.    

Pasquale

		
				
				
	

	
		
		
	
 

	
	

	
		
			
- Name*Email*
			
			
			
			
			
			
- 

[Sponsor bunnie on Github](https://github.com/sponsors/bunnie)

- 

## Categories

			
					
- [Administrative](https://www.bunniestudios.com/blog/category/administrative/)

	
- [baochip](https://www.bunniestudios.com/blog/category/baochip/)

	
- [betrusted](https://www.bunniestudios.com/blog/category/betrusted/)

	
- [Biology](https://www.bunniestudios.com/blog/category/ponderings/biology/)

	
- [chibitronics](https://www.bunniestudios.com/blog/category/chibitronics/)

	
- [chumby](https://www.bunniestudios.com/blog/category/chumby/)

	
- [covid-19](https://www.bunniestudios.com/blog/category/covid-19/)

	
- [Feminism](https://www.bunniestudios.com/blog/category/ponderings/feminism/)

	
- [gongkai](https://www.bunniestudios.com/blog/category/gongkai/)

	
- [Hacking](https://www.bunniestudios.com/blog/category/hacking/)

	
- [IRIS](https://www.bunniestudios.com/blog/category/iris/)

	
- [Made in China](https://www.bunniestudios.com/blog/category/chumby/made-in-china/)

	
- [Made in Italy](https://www.bunniestudios.com/blog/category/hacking/made-in-italy/)

	
- [name that ware](https://www.bunniestudios.com/blog/category/hacking/name-that-ware/)

	
- [NeTV](https://www.bunniestudios.com/blog/category/hacking/netv/)

	
- [novena](https://www.bunniestudios.com/blog/category/novena/)

	
- [open source](https://www.bunniestudios.com/blog/category/hacking/open-source/)

	
- [Ponderings](https://www.bunniestudios.com/blog/category/ponderings/)

	
- [precursor](https://www.bunniestudios.com/blog/category/betrusted/precursor/)

	
- [Social](https://www.bunniestudios.com/blog/category/social/)

	
- [The Factory Floor](https://www.bunniestudios.com/blog/category/the-factory-floor/)

	
- [Uncategorized](https://www.bunniestudios.com/blog/category/uncategorized/)

			

			
- 

## Pages

			
				
- [2012 Name That Ware Calendar](https://www.bunniestudios.com/blog/2012-name-that-ware-calendar/)

- [Contact bunnie](https://www.bunniestudios.com/blog/contact-bunnie/)

- [Crosslicense 1.0 (XL-1.0)](https://www.bunniestudios.com/blog/crosslicense-1-0-xl-1-0/)

- [On Influenza A (H1N1)](https://www.bunniestudios.com/blog/on-influenza-a-h1n1/)

- [On MicroSD Problems](https://www.bunniestudios.com/blog/on-microsd-problems/)

	
- [On Hacking MicroSD Cards](https://www.bunniestudios.com/blog/on-microsd-problems/on-hacking-microsd-cards/)

- [The $12 “Gongkai” Phone](https://www.bunniestudios.com/blog/the-12-gongkai-phone/)

- [The Factory Floor, Part 1 of 4:The Quotation (or, How to Make a BOM)](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/)

	
- [The Factory Floor, Part 2 of 4:On Design for Manufacturing](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-2-of-4on-design-for-manufacturing/)
	
- [The Factory Floor, Part 3 of 4: Industrial Design for Startups](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-3-of-4-industrial-design-for-upstarts/)
	
- [The Factory Floor, Part 4 of 4:Picking (and Maintaining) a Partner](https://www.bunniestudios.com/blog/the-factory-floor-part-1-of-4the-quotation-or-how-to-make-a-bom/the-factory-floor-part-4-of-4picking-and-maintaining-a-partner/)

- [Why the Best Days of Open Hardware are Yet to Come](https://www.bunniestudios.com/blog/why-the-best-days-of-open-hardware-are-yet-to-come/)

- [Add a VGA LCD to a Chumby](https://www.bunniestudios.com/blog/add-a-vga-lcd-to-a-chumby/)

- [Dvorak on the Tandy 102](https://www.bunniestudios.com/blog/dvorak-on-the-tandy-102/)

- [HackDAC](https://www.bunniestudios.com/blog/hackdac/)

	
- [HackDAC Implementation](https://www.bunniestudios.com/blog/hackdac/hackdac-implementation/)
	
- [HackDAC Theory](https://www.bunniestudios.com/blog/hackdac/hackdac-theory/)

- [Hacking the PIC 18F1320](https://www.bunniestudios.com/blog/hacking-the-pic-18f1320/)

- [Modifying the S400 Scanner for Watermark Enhancement](https://www.bunniestudios.com/blog/modifying-s400-scanner-for-watermark-enhancement/)

- [Pictures of Logic Gates in Silicon](https://www.bunniestudios.com/blog/pictures-of-logic-gates-in-silicon/)

- [Some hacks I’ve done](https://www.bunniestudios.com/blog/some-hacks-ive-done/)

- [Diodes, Solitons, and Taoism](https://www.bunniestudios.com/blog/diodes-solitons-and-taoism/)

- [Name that Ware Contest Rules](https://www.bunniestudios.com/blog/name-that-ware-contest-rules/)
			

			
- 

## Stuff

	

- [bunniestudios logo merch](https://www.cafepress.com/bunniestudios)

- [Factpub Whitepaper](https://bunniefoo.com/bunnie/factpub.pdf)

- [Old home page](https://bunniestudios.com/bunnie/)

- [PhD thesis](https://bunniestudios.com/bunnie/phdthesis.pdf)

	

- 
				
					Search for:
					
					
				
			
- 

## Meta

		
						
- [Log in](https://www.bunniestudios.com/wordpress/wp-login.php)
			
- [Entries feed](https://www.bunniestudios.com/blog/feed/)
			
- [Comments feed](https://www.bunniestudios.com/blog/comments/feed/)

			
- [WordPress.org](https://wordpress.org/)
		

				
	

	

		bunnie's blog is proudly powered by [WordPress](http://wordpress.org/)		[Entries (RSS)](https://www.bunniestudios.com/blog/feed/) and [Comments (RSS)](https://www.bunniestudios.com/blog/comments/feed/).
