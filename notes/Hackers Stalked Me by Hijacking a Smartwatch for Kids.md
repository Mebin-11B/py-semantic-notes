---
title: "Hackers Stalked Me by Hijacking a Smartwatch for Kids"
url: https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/
clipped: 2026-08-31 12:22:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Hackers Stalked Me by Hijacking a Smartwatch for Kids](https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/)

## Digest Summary
A low‑cost children’s smartwatch sold by CJC and manufactured by YiQingTeng Electronics runs on the SETracker platform; similar devices use the NewGPS2012 and SinoTrack platforms.  
Researchers Stykas and Solferini examined &gt;70 GPS‑enabled watches and car accessories and identified three Shenzhen‑based supply chains that together produce tens of millions of units.  
All three platforms exhibit critical security flaws, often as simple as missing authentication, allowing any attacker to:
  • Access or spoof any device’s location, disable or unlock cars, and replace emergency contacts.
  • Intercept, modify, or spoof text and audio messages.
  • Eavesdrop via microphone, capture photos/video on camera‑enabled models, and hijack GPS tracking.  
Server‑side vulnerabilities expose consumer data, permit remote code execution, and show evidence of prior unauthorized access.  
Companies (SETracker, SinoTrack, NewGPS2012) have either denied issues or claimed fixes; the researchers’ exploits still work on two platforms.  
The findings highlight a widespread, low‑cost attack surface affecting millions of children’s wearables and vehicle trackers.

---

## Full Article

[Skip to main content](https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/#main-content)Save this storySave this story

On a rainy New York morning earlier this week, a WIRED reporter strapped to his wrist a lavender and pink plastic child’s [smartwatch](https://www.wired.com/gallery/best-smartwatches/) and headed to work. As he approached his nearby subway station to commute to WIRED’s office, he texted Vangelis Stykas, the Greek security researcher who had shipped him the watch via Amazon, to let him know that he was going into the station and might lose cell signal.

“I know,” Stykas wrote back.

In fact, Stykas had been monitoring the reporter’s location via the watch since the moment he left his apartment. The watch’s GPS feature, intended to let a parent track their child, was malfunctioning, but the wearable device was still picking up and transmitting to a faraway server identifiers from every nearby Wi-Fi network, which allowed Stykas to nonetheless pinpoint the reporter’s exact location as he walked down a particular Brooklyn block.

A WIRED reporter wearing the GPS-enabled smartwatch while holding an umbrella and walking to the subway earlier this week.
Courtesy of Andy Greenberg

When the reporter arrived at WIRED’s Manhattan headquarters half an hour later, Stykas hijacked a feature in the watch that allowed him to silently take a photo from its camera, capturing the moment when the reporter stepped into an elevator. After a few minutes, he took another snap of the reporter at his desk, then used a different feature to pick up audio from the watch’s microphone, transmitting it to another researcher, Felipe Solferini, who listened as the reporter’s coworker described his weekend visit to an art exhibition. At no point did the watch show any sign that it was listening, taking photos, or otherwise being hacked.

As WIRED reporter Andy Greenberg entered the elevator at WIRED's New York office, the hackers used the smartwatch to surreptitiously take a photo…
Courtesy of Vangelis Stykas

…and then again as he sat at his desk.
Courtesy of Vangelis Stykas

The watch’s insecurity and the spying it enabled might be expected given the gadget’s pedigree: It’s sold by an obscure company called CJC, costs less than $30, and was made by an equally obscure manufacturer, YiQingTeng Electronics, in Shenzhen, China. More troubling, perhaps, is that the online platform it’s built on—and the one that allowed Stykas and Solferini to so thoroughly hack it—is used by dozens of other brands of smartwatch, many of which have likely been left vulnerable to the same forms of digital stalking.

At the Black Hat cybersecurity conference today, Stykas and Solferini plan to present their findings from analyzing the supply chain and security of more than 70 GPS-enabled watches and car accessories. They found that more than 30 of those geolocation devices use the technology and backend servers of YiQingTeng, also identified by the brand name Wonlex, the name of a partner firm Shenzhen 3G Electronics, or their associated app, SETracker. Another 30-plus brands of tracking devices for cars and kids are all run on another Shenzhen-based platform known as NewGPS2012.

Combined with another major GPS platform known as SinoTrack that sells car trackers and smartwatches, the two researchers found that tens of millions of GPS tracker gadgets came from just three supply chains. All three, the researchers found in their analysis, had significant security flaws—in some cases as simple as a lack of authentication that allowed anyone to access any device—leaving children’s watches vulnerable to tracking by a hacker, location disabling and spoofing, interception and spoofing of text and audio messages sent to them, replacement of emergency contacts with ones a hacker chose, silent audio eavesdropping, as well as photo and video capture for camera-enabled devices. (Once the GPS started working on the smartwatch WIRED tested, the hackers showed that feature, too, could be hijacked to follow the wearer’s every move.)

For some GPS-enabled car accessories, the researchers found they could similarly track the devices’ locations or spoof messages to them that could potentially unlock or disable cars, though the researchers didn’t go so far as to test this out on actual vehicles. They also say they found server-side vulnerabilities that exposed consumer information, would have allowed them to execute their own code on the servers, or even in one case appeared to show that someone else had already gained unauthorized access to the system’s backend.

“Millions of kids are being exposed and vulnerable to exploitation. It's just catastrophic. It's really low-hanging fruit for a lot of bad actors,” Stykas says. “Your criminal mind is the only limitation in exploiting those devices.”

## The Watches Watching Your Kids

The researchers say they’ve been warning the companies behind all three Shenzhen-based GPS platforms about their vulnerabilities for months. When WIRED reached a representative of SETracker, the person initially claimed in an email that “the issues you mentioned have been resolved long before,” adding that “we attach great importance to the security of Setracker and keep strengthening its security continuously.” When WIRED pointed out that researchers had been able to hack a smartwatch running on SETracker just this week, the person repeated their claim that the issues had been fixed, then asked for evidence of the exploitation, which WIRED provided.

Only today, hours before the researchers’ talk at Black Hat, did the researchers find that their hacking techniques against SETracker’s platform have stopped working—though they’re still not sure if the flaws they found are fully fixed. After this article published, SETracker wrote in a statement that it had blocked certain ports on its servers used by a “legacy” version of its clients' systems, forcing “a small subset of clients” on that older system to upgrade to protect “a small number of devices” that were affected. “The vulnerability has now been thoroughly remediated,” the SETracker staffer wrote. “Thank you for your oversight and attention.”

Sinotrack and the NewGPS2012 platform didn’t respond to WIRED’s requests for comment, and the researchers say their hacking techniques against those systems still appear to work.

For more than a decade, cybersecurity experts and privacy advocates have warned that cheap, GPS-enabled [children’s smartwatches](https://www.wired.com/story/kid-smartwatch-security-vulnerabilities/) and aftermarket [vehicle](https://www.wired.com/2016/03/thousands-trucks-buses-ambulances-may-open-hackers/) [accessories](https://www.wired.com/2015/08/hackers-cut-corvettes-brakes-via-common-car-gadget/) are riddled with security vulnerabilities that leave kids and drivers susceptible to hacking and tracking. But the sheer number of different brands and models of those devices has often made identifying the truly insecure gadgets feel nearly impossible for consumers.

More than any specific vulnerability, Solferini and Stykas say, they wanted to highlight that much of that daunting diversity among GPS devices—along with consumers’ sense of choice among them—is essentially an illusion.

“A parent in Sweden buying a ‘SafeKid’ watch and a parent in Spain buying a ‘SaveFamily’ watch are both sending their child's location data to the same vulnerable myaqsh.com backend on Alibaba Cloud in mainland China, without knowing it,” they write in a whitepaper shared with WIRED ahead of their Black Hat presentation, referring to the online services of YiQingTeng. “The white-label model means a vulnerability in one backend aﬀects dozens of consumer brands at the same time, and consumers have no way to tell which backend their product uses.”

The smartwatch WIRED tested was made by Shenzhen-based YiQingTeng Electronics and runs on the SETracker platform used by dozens of brands and millions of devices.
Courtesy of Jobanny Cabrera

Solferini and Stykas aren’t revealing the full details of the vulnerabilities they discovered in the three major platforms, in part because not all of them have been fixed despite sharing their findings with the companies for months. In the case of YiQingTeng, the manufacturer of the watch WIRED tested, however, they say an authentication security flaw would have allowed anyone to send commands to any SETracker-based device. That would let hackers exploit and take over devices at random or to target specific watches if they can determine an identifier for them, such as the parent’s email address the device is registered to. (To hack the smartwatch worn by a WIRED reporter, for instance, the reporter gave Stykas his email address but no other information about the device. Stykas says he could have easily targeted devices in other ways, such as hacking numerous watches and searching through them to find the nearest vulnerable devices or one associated with a target’s identifying information.)

In the case of SinoTrack, the researchers say they found that an account intended for demonstration purposes could be used to send commands to any of the platform’s millions of devices. They also found a SQL injection vulnerability—a flaw that essentially allows anyone to send commands disguised as data that are then executed by the SinoTrack server—that gave them access to tens of thousands of devices’ locations, passwords, and vehicle records.

Finally, for NewGPS2012 devices, the researchers say they found similar SQL injection vulnerabilities and were able to run their own code on the company’s servers. They also say they found evidence of a previous compromise of the company’s systems, suggesting other unauthorized users or hackers may have had access to it for an unknown period of time.

## Dozens of Devices, Years of Warnings

Given the sheer number of different brands and resellers of those Shenzhen-manufactured gadgets, the researchers didn’t confirm the vulnerability of all of the individually branded devices they found to use YiQingTeng’s SETracker platform or the NewGPS2012 platform. WIRED couldn’t independently confirm each device’s vulnerability either. But the table below lists brands whose products were based at least in part on those platforms, as well as the company’s response when WIRED reached out for comment on the researchers’ findings.

Stykas and Solferini’s Black Hat talk is far from the first warning about the dangers of cheap GPS devices—even from these researchers themselves. Stykas and another researcher, Michael Gruhn, revealed a broad collection of vulnerabilities in GPS-enabled devices in 2018, which they called [Trackmageddon](https://www.bleepingcomputer.com/news/security/-trackmageddon-vulnerabilities-discovered-in-gps-location-tracking-services/). GPS-enabled automotive devices plugged into the OBDII port on cars’ dashboards have proven [again](https://www.wired.com/2015/08/hackers-cut-corvettes-brakes-via-common-car-gadget/) and [again](https://www.wired.com/2016/03/thousands-trucks-buses-ambulances-may-open-hackers/) to be vulnerable to hacking and tracking.

Children’s GPS-enabled watches have also been shown to be especially prone to critical privacy and security vulnerabilities: [Pen Test Partners](https://www.pentestpartners.com/security-blog/tracking-and-snooping-on-a-million-kids/) and the [Norwegian government](https://www.forbrukerradet.no/side/significant-security-flaws-in-smartwatches-for-children/) issued warnings about certain hackable children’s watches in 2017 and 2018, and another study by the Münster University of Applied Sciences in 2020 tested six children’s smartwatches and [found serious vulnerabilities in five](https://www.wired.com/story/kid-smartwatch-security-vulnerabilities/). “It was crazy," Sebastian Schinzel, one of the Münster researchers, told WIRED at the time. "Everything was basically broken."

Yet somehow, Stykas says, people keep putting cheap, GPS-enabled devices on their loved ones. And the companies that make them, too, have often completely ignored his warnings about the hackable bugs in their devices. As he tested his surveillance techniques against the newly purchased smartwatch on a WIRED reporter’s wrist a few days ago, they worked as well as ever, and some of the devices’ flaws remain unpatched even now.

“I really hoped we could tell a nice story that there were vulnerabilities and they fixed them. But in many cases, they didn’t,” Stykas says. “It's a position I really didn't want to be in.”

Updated: 8/7/2026, 12:53 EDT: This story now includes additional comment, given after publication, from SETracker and KUSS.

## Comments

[Back to top](https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/#main-content)Join the discussion

## Comments

[Back to top](https://www.wired.com/story/hackers-stalked-me-by-hijacking-a-smartwatch-for-kids/#main-content)

## You Might Also Like

- 

In your inbox: WIRED's [most ambitious, future-defining stories](https://www.wired.com/newsletter/the-big-story?sourceCode=BottomStories)
- 

[AI slop backlash](https://www.wired.com/story/the-ai-slop-backlash-is-actually-having-an-impact/) is actually having an impact
- 

Big Story: The cop who [took on Flock](https://www.wired.com/story/the-cop-who-took-on-flock/)
- 

The rise of [the 1am job interview](https://www.wired.com/story/the-rise-of-the-1-am-job-interview/)
- 

Watch: [I stole a car by hacking this hidden device](https://www.wired.com/video/watch/i-stole-a-car-by-hacking-this-hidden-device)Written by WIRED StaffTopics[GPS](https://www.wired.com/tag/gps/)[surveillance](https://www.wired.com/tag/surveillance/)[hacks](https://www.wired.com/tag/hacks/)[privacy](https://www.wired.com/tag/privacy/)[security](https://www.wired.com/tag/security/)[cybersecurity](https://www.wired.com/tag/cybersecurity/)[smartwatch](https://www.wired.com/tag/smartwatch/)[black hat](https://www.wired.com/tag/black-hat/)[DefCon](https://www.wired.com/tag/defcon/)[Top Dell Coupon Codes: 20% Off for August 2026](https://www.wired.com/story/dell-coupon-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Get 20% off with verified Dell promo code, plus today’s coupons for up to $600 off laptops, Alienware monitors, and all things tech.Scott Gilbertson[Meta Quest Promo Codes and Coupons for August 2026](https://www.wired.com/story/meta-quest-promo-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Experience cutting-edge VR and save up to 20% with coupons for the latest games, Meta Quest 3, Ray-Ban AI glasses, and more deals.Harry Rabinowitz[Top Starz Promo Codes & Deals for 2026](https://www.wired.com/story/starz-promo-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Ready to stream award-winning series, hit movies, and exclusive originals? Our comprehensive guide helps you find every active Starz coupon, free trial, and discount code to save big on your subscription this 2026.Molly Higgins[Top Theragun Promo Codes: 15% Off in September 2026](https://www.wired.com/story/therabody-promo-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Save on the science-backed devices you’ve been eyeing with 15% off Theragun discount code and 30% off other great deals.Molly Higgins[Top AirDoctor Coupon Codes for August 2026](https://www.wired.com/story/airdoctor-coupon-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Save up to $400 on top air purifiers and filters with verified AirDoctor promo codes and special offers for 2026.Molly Higgins[Is It Possible to Make Smart Glasses That Aren’t Creepy?](https://www.wired.com/story/is-it-possible-to-make-privacy-friendly-smart-glasses/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)As more big companies invest in glasses that record audio and video and pack AI on board, privacy concerns are only getting louder.Boone Ashworth[Top Shark Promo Codes for August 2026](https://www.wired.com/story/shark-promo-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Shark makes some seriously powerful vacuums, from handheld vacs to steam mops. Don’t miss $100 off, 10% off, and more limited-time coupons from WIRED. Nena Farrell [Top Chegg Coupon Codes: Save on Textbooks, Study, and Writing](https://www.wired.com/story/chegg-coupon-code/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Unlock Chegg promo codes, student discounts, and free trials for Chegg Study and Chegg Writing.Molly Higgins[7 States’ Water Systems Hit by Cyberattacks Likely Tied to Iran](https://www.wired.com/story/security-news-this-week-7-states-water-systems-hit-by-cyberattacks-likely-tied-to-iran/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Plus: The FBI eyes AI-powered tech to detect future crimes, Russia charges Telegram’s founder, xAI sues to stop a state’s “nudification” ban, and the Democrats learn a lesson about getting scammed.Matt Burgess[Top NordVPN Coupons: 75% Off, Plus 3 Months Free in August 2026](https://www.wired.com/story/nordvpn-coupon/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Save up to 77% on 2-year plans and get 3 free months with our NordVPN discount codes.Scott Gilbertson[A Security Pro Hacked North Korean Hackers. He Found They’d Breached Hundreds of Networks Worldwide](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)For nearly two years, researcher Vangelis Stykas has maintained access to North Korean hackers’ servers. His work shows they pulled off intrusions in a shocking number of systems across the globe.Matt Burgess[Walmart Promo Codes: Up to 65% Off for August 2026](https://www.wired.com/story/top-walmart-promo-codes/#intcid=_wired-article-bottom-recirc_d0dc2879-d16d-456d-baf5-588c01dc1286_modern-bert)Score $10 off with our Walmart promo codes and coupon, and shop flash deals up to 65% off today.Molly Higgins
