---
title: "The footgun of right-to-left decorative characters"
url: https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters
clipped: 2026-08-31 12:22:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The footgun of right-to-left decorative characters](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters)

## Digest Summary
Unicode includes decorative characters such as the Manichaean Punctuation Fleuron (U+10AB1). Because this fleuron is classified as a right‑to‑left (R) strong type, it influences the layout of surrounding weak characters, causing numbers that follow it to appear before it (e.g., “𐫱400” renders as “400𐫱”). This behavior follows the Unicode Bidirectional Algorithm, which assigns each character a bidi type (L, R, EN, WS, etc.) and resolves ordering based on strong types, with weak types inheriting direction from nearby strong characters. To prevent unwanted reordering, the fleuron can be isolated using the HTML  element or CSS `unicode-bidi: bidi-override;`, which forces the character to retain its intended position regardless of surrounding text direction. These methods work across modern browsers, though legacy support (e.g., IE) is limited.

---

## Full Article

CONTENTS⤴︎Manichaeism and UnicodeFixing with HTML and CSS				
							

Fleurons, and other printer's ornaments are decorative elements used in typography. Many of these have made it into fonts in the digital age, with Unicode supporting classic fleurons like ❦ and ❧,
1
These are slowly getting introduced into the blog styling, formal post Coming Soon™. 
 but also additional symbols-turned-visual indicators ranging from the aptly named ❀ (White Florette) to the lesser known ᪥ (Tai Tham Sign Dokmai
2
Dokmai means 'flower' in Tai Tham scripts like Northern Thai or Lao.
). I was recently exploring using 𐫱 as a delineator between the date and post categories, but found that it was unexpectedly rendering in the middle of the tag:

  May 14
  𐫱
  [400 Divisadero](https://blog.alexbeals.com/category/400-divisadero)

It should render like this. Why doesn't it?

  May 14
  𐫱
  [400 Divisadero](https://blog.alexbeals.com/category/400-divisadero)

## Manichaeism and Unicode

𐫱 is the Manichaean Punctuation Fleuron, part of a block in Unicode for adapting religious texts from Manichaeism. If you care to know what Manichaeism is, it was a world religion from the 3rd century AD which collapsed through a combination of active persecution, competition from Christianity, Islam, and Buddhism, and the death of the empires that had tied themselves to it.
3
Also they foolishly didn't allow post-deceased converts like some [fast-growing religions](https://en.wikipedia.org/wiki/Baptism_for_the_dead#Latter-day_Saint_practice_and_teachings).
 If you don't care, you just need to know that they had a pretty flower icon...and wrote from right-to-left.

While most Manichaean scripts are solely written in right-to-left, they're not as constrained on a website:
4
Look at me Mom! עברית(HEBREW) and عربي(ARABIC) and 𐫖𐫀𐫗𐫏𐫐𐫏𐫀𐫗(MANICHAEAN) all in one sentence!
 whatever rendering algorithm Chrome uses to layout text needs to handle bidirectional text consisting of both left-to-right and right-to-left characters. Unicode is well-described, so there's a Unicode Bidirectional Algorithm that explains how to do this, but because Unicode is so complex this [requires ~20k words and 51 revisions](https://www.unicode.org/reports/tr9/)—let's stick to a TL;DR.

Each character has a bidirectional character type (visible in [UnicodeData.txt](https://www.unicode.org/Public/UNIDATA/UnicodeData.txt)). This can be strong types, like  `L`  (for left) for stuff like the letter "A" or  `R`  (for right) for Hebrew text; weak types, like  `EN`  for European Numbers such as 0; or neutral, like  `WS`  for whitespace like tabs and spaces.
5
[Here's the table](https://www.unicode.org/reports/tr9/#Table_Bidirectional_Character_Types) if you're curious. 
 Strong types will take precedence, and weak types will defer to their surrounding strong types.

The Manichaean fleuron is  `R`  typed, and so it rearranges the weak block of the digits  `400`  (though they remain internally ordered as 400 instead of 004), rendering  `𐫱 <span>400 Divisadero</span>`  as "𐫱 400 Divisadero".

## Fixing with HTML and CSS

Luckily this is fixable if we remember that we have to do it! We can wrap the fleuron with the  `<bdi>`  HTML tag to isolate the directionality from the text around it: 𐫱 400 Divisadero. You can also do the same thing with the CSS style  `unicode-bidi: bidi-override;` :
6
'Bidi' for bi-directional.
 𐫱 400 Divisadero, which has marginally better support across browsers.
7
Though who really cares about IE.

 `<bdi>` 
unicode-bidi

Just remember to do this the next time you reach for something like 𞢹 or 𐩕.

- 

These are slowly getting introduced into the blog styling, formal post Coming Soon™.  [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:sprinkle)

- 

Dokmai means 'flower' in Tai Tham scripts like Northern Thai or Lao. [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:dokmai)

- 

Also they foolishly didn't allow post-deceased converts like some [fast-growing religions](https://en.wikipedia.org/wiki/Baptism_for_the_dead#Latter-day_Saint_practice_and_teachings). [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:mormons)

- 

Look at me Mom! עברית(HEBREW) and عربي(ARABIC) and 𐫖𐫀𐫗𐫏𐫐𐫏𐫀𐫗(MANICHAEAN) all in one sentence! [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:chaos)

- 

[Here's the table](https://www.unicode.org/reports/tr9/#Table_Bidirectional_Character_Types) if you're curious.  [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:table)

- 

'Bidi' for bi-directional. [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:bidi)

- 

Though who really cares about IE. [↩︎](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters#fnref1:ie)

			
					

				
			

## 1 comment

			
								
- 
					

					

The plain-text way to fix this is to put U+200E LEFT-TO-RIGHT MARK just after the fleuron. This ensures things still look right even after copy-paste
				
							
		
		
				
			
									
			
			
			Post Comment
		
		
		
				
		

### Next snippet

[How to dump iOS app's source codeMay 24, 2026](https://blog.alexbeals.com/posts/dumping-ipas)

### Previous snippet

[Tips and tricks for macOS lldbApril 28, 2026](https://blog.alexbeals.com/posts/tips-and-tricks-for-macos-lldb)

### Recent snippets

[Fixing UnitedWifi​.com not working on my Mac laptopAugust 27, 2026](https://blog.alexbeals.com/posts/fixing-unitedwificom)[Find out who owns a building in SFJune 14, 2026](https://blog.alexbeals.com/posts/find-out-who-owns-a-building-in-sf)[Deeplinking to Venmo usersMay 24, 2026](https://blog.alexbeals.com/posts/deeplinking-to-venmo-users)[How to dump iOS app's source codeMay 24, 2026](https://blog.alexbeals.com/posts/dumping-ipas)[The footgun of right-to-left decorative charactersMay 19, 2026](https://blog.alexbeals.com/posts/the-footgun-of-right-to-left-decorative-characters)[View all snippets](https://blog.alexbeals.com/snippets)[View all posts](https://blog.alexbeals.com/list)		
			

	
		
			
				
			
		
	

	×
