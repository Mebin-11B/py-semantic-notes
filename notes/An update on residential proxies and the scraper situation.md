---
title: "An update on residential proxies and the scraper situation"
url: https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/
clipped: 2026-08-31 12:22:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [An update on residential proxies and the scraper situation](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/)

## Digest Summary
The article details the ongoing wave of web‑scraper attacks that leverage residential and mobile IP addresses. Attackers control compromised devices—often via malware on PCs, media‑streaming hardware, or VPN‑based services such as Bright Data—to issue millions of short, human‑like requests that rarely load images or CSS, making IP‑based blocking ineffective. The shutdown of Google’s IPIDEA botnet temporarily reduced traffic, but new networks (e.g., NetNut) have revived the threat. Operators range from outright criminals to companies advertising “ethically sourced” proxy pools, and some AI model developers use their own scrapers with identifiable user‑agents while adhering to robots.txt. Defenses employed by sites include proof‑of‑work systems (Anubis), commercial human‑verification services, login or paywall gating, and data‑poisoning tools like iocaine. LWN has optimized its infrastructure and selective throttling to mitigate impact without hindering legitimate crawlers (search engines, Internet Archive). Recent coordinated takedowns by Google and law‑enforcement have offered brief relief, but the article warns that the arms race will persist.

---

## Full Article

[LWN.net
            News from the source](https://lwn.net/)
            
           
        
- [Content](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/#t)
- [Weekly Edition](https://lwn.net/current/)
- [Archives](https://lwn.net/Archives/)
- [Search](https://lwn.net/Search/)
- [Kernel](https://lwn.net/Kernel/)
- [Security](https://lwn.net/Security/)
- [Events calendar](https://lwn.net/Calendar/)
- [Unread comments](https://lwn.net/Comments/unread)
- 
- [LWN FAQ](https://lwn.net/op/FAQ.lwn)
- [Write for us](https://lwn.net/op/AuthorGuide.lwn)

- [Edition](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/#t)
- [Return to the Front page](https://lwn.net/Articles/1081916/)

 

        User:  
		Password:    |
           
           
            |
           
           
           
        
               
               [Log in](https://lwn.net/Login/) /
               [Subscribe](https://lwn.net/subscribe/) /
               [Register](https://lwn.net/Login/newaccount)
               
               

# An update on the scraper situation

For humans, by humans

Every article on LWN.net is written for humans, by humans. If you've
enjoyed this article and want to see more like it, your subscription goes a
long way to keeping the slop at bay.  We are offering [a free one-month trial subscription](https://lwn.net/Promo/nst-bots1/claim) (no credit card required) to get you started.

           By Jonathan CorbetJuly 10, 2026
           
Our article "[Fighting the AI scraper bot
scourge](https://lwn.net/Articles/1008897/)", published in early 2025, discussed the problem of widespread
scraping of web sites in search of training data for large language models
and related projects.  This activity overwhelms sites with traffic.  Over a
year after that article is published, the problem is still growing.  The
hammering of sites by shadowy actors has reached new heights, and the open
web is becoming increasingly difficult to maintain.  Where is this traffic
coming from, and what can be done about it?

#### Residential proxies

As was described last year, scraper attacks come from a huge number of
sources across the net.  It is not unusual to see coordinated requests from
millions of unique IP addresses over the course of a few hours, each of
which hits the site at most two or three times.  Attacker-controlled data,
such as the user-agent field, is entirely fictional; each hit is meant to
look like just another human with a web browser.  There are ways to tell
the difference — the bots usually do not fetch images or CSS, for example —
but, by the time that determination is made, the address in question will
not be used again.  Blocking the address at that point is just a waste of
time.

This traffic comes predominantly from residential and mobile networks,
directed by central command-and-control nodes.  Software is installed on
ordinary systems that takes orders from a control node, fetches web pages
on demand, and forwards the resulting data back to the controller.  Much of
the time, this activity occurs without the knowledge or consent of the
owner of the device in question.  The term "residential proxies" is used to
describe systems that are used in this way.

There are a few different (on the surface, at least) types of operator
running residential-proxy networks to attack web sites.  One type is purely
criminal, running scrapers on systems that have been compromised with some
sort of malware.  At the beginning of the year, Google [acted
to take down a bot network called IPIDEA](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network) and provided a lot of
information about how these operations work.  The shutdown of IPIDEA
correlated with a significant reduction in scraper traffic here at LWN;
things were relatively peaceful for a few months.  That period of peace has
since come to an end, though.

More recently, media-streaming devices have been [identified](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/)
as a major carrier of malicious scraping software.  Sometimes the devices
are compromised at the source; other times, they are just poorly secured
and easily compromised after the fact.

The second sort of operator works more overtly, pretending to a degree of
legitimacy and offering "ethically sourced" IP addresses.  A company called
Bright Data is one of the most prominent of these; it happily advertises
its prowess at getting around web-site access controls and traffic limits.
Bright Data offers a "free" VPN service; all that is needed is for the user
to give Bright Data the ability to route traffic through the user's device
— to become a part of the company's residential-proxy network, in other
words.  Every phone or other device that makes use of this VPN becomes yet
another endpoint that will be used to attack web sites.

There are many other examples of this type of operator out there; often
they offer a library that app developers can link into their offerings and
be paid for hijacking their users' network connections.  One of them even
sent us a query about running an ad for its SDK on LWN; that was, it
suffices to say, a short conversation.  In general, these companies range
from those that aspire toward some appearance of legitimacy, advertising
"GDPR compliance" for example, to others that are just overtly sleazy.

While these residential-proxy networks are used for web-site scraping, it
is worth emphasizing that these operators have the ability to run code that
accesses resources on whatever networks millions of devices happen to be
connected to.  To assume that this type of access would only be used for
scraping would be naive at best.

Then, of course, there are the high-profile companies developing models as
their core business.  These companies do their own scraping; the traffic
that can be easily attributed to them is clearly identified in the
user-agent field and, as a general rule, observes measures like
robots.txt.  They, too, will scrape an entire site, repeatedly,
seemingly on the theory that articles written in 2003 might somehow have
changed in the last day, but they do not generate overwhelming amounts of
traffic from millions of systems and are not the biggest problem.

What isn't clear is who is using the residential proxies; somebody
is paying them to run these attacks on web sites.  There is no
evidence (that I am aware of) that the frontier-model companies are using
those networks.  If it were to turn out that they are doing so, though,
the increase in global astonishment would barely register.  Those companies
are feeding their models somehow, they are not forthcoming about how they
get their training data, and they have not distinguished themselves with
their level of respect toward content creators — or toward anybody who
might have concerns about their operations.

For every public model, though, there must be a vast number of undercover
models.  Many companies are surely trying to build their own; after all, we
are reliably informed that AI is going to take over the world and the
companies that come out on top of that race will be worth untold amounts of
money.  There must be shadowy government agencies in many countries working
on their own models and groping for training data wherever they can find
it.  Large-scale criminal organizations (to the extent that they are
distinct from governments) probably also want to have their own models.
These tools are seen as weapons, and there is an arms race underway.  The
Internet as a whole is caught in the crossfire.

#### Defending the open Internet

In response to all of this, web-site operators have been scrambling to
defend their sites while minimizing the effect on their actual users.  [Anubis](https://lwn.net/Articles/1028558/), which attempts to fend off scrapers by
requiring a proof of work, is now widespread.  Other sites use commercial
services, which sometimes make themselves known with a "prove you are
human" button.  Or sites force users to pick out squares containing
streetlights (but only those with LED bulbs), place puzzle pieces, or hum a
song while holding down the space bar.  Many site features have been placed
behind login gates or paywalls.  Some sites attempt to actively poison the
data sent to scrapers with tools like [iocaine](https://lwn.net/Articles/1056953/).

Both the need to set up and maintain these mechanisms, and the requirement
that users cope with them to access a web site, constitute a heavy tax
placed on the world as a whole by scrapers and those who pay them.

Recently, LWN was subjected to what was, by far, the heaviest scraper attack
yet.  Thanks to the defenses that have been implemented, the site bore the
traffic well enough that most actual readers probably did not even notice.
There have been requests to describe the measures we have taken to defend
the site; for obvious reasons we do not wish to discuss them in any detail.
It is an arms race at this level too.

What we can say is that we have tried to minimize the impact on real
readers as much as possible.  We have not gone with tools like Anubis,
partly because it causes annoying delays for those trying to get to the
site, but also partly because it seems inevitable that the scrapers will
eventually find their way around it.  Indeed, there are some indications
that is already happening.  A proof-of-work requirement is not a huge
obstacle when you have millions of other people's machines to do the work
on.

There is also a desire to not impede the operation of legitimate search
engines, the Internet Archive, and other such groups.  Some sites may add
explicit allowlists to, for example, give the dominant search engine access
to the site.  Such measures have the effect of further entrenching a
monopoly that already serves us poorly and should be avoided.  We have,
thus far, succeeded in that.

We have aggressively optimized parts of the site, and found ways to
minimize expensive operations during times when the site is under attack.
Anonymous readers may occasionally encounter one of those measures;
logged-in users will not.  Amusingly, the response time when the site is
under attack is often better than during the calm times, when the defensive
measures are dormant.  We have learned better than to think that the
problem is solved, though; consideration must be given to our next steps
once the current measures are no longer effective.

On July 2, Google [announced](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks)
that it had, in coordination with the US Federal Bureau of Investigation
and others, taken down a residential-proxy network called "NetNut".  For
the time being, that action would, indeed, seem to have succeeded in
reducing the level of scraper attacks somewhat.  Experience shows, though,
that this welcome peace will only last so long.  Google takes pains to
point out that its Play Store will now check for NetNut-infected apps, but
all of the major vendors are silent on the topic of why it is so easy to
put apps with residential-proxy functionality into their app stores.

It would be good to find a more lasting solution before the entire Internet
is driven behind defensive walls, and the open network that inspired so
much creativity is lost.  The industry that is driving these attacks seems
entirely at ease with turning independent web sites into smoking craters
after having pillaged their contents — an attitude that extends to the
planet and its economies as well.  Some of us, though, object to that idea
and will fight against it.  Someday, with luck, the world as a whole will
decide to hold the companies behind large language models and related
technologies to a minimal ethical standard.  Until then, though, this
behavior will continue, and we will have no choice but to defend ourselves
against it.
            
            
             to post comments
            

        

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 10, 2026 15:59 UTC (Fri)
                               by KJ7RRV (subscriber, #153595)
                              [[Link](https://lwn.net/Articles/1082329/)] (8 responses)
      
      
      
      
      
How can one avoid unintentionally running one of these proxies? It's easy enough on a desktop/laptop to just check for unexpected network usage (and I doubt Linux machines are a common target of these Trojans, not to mention the fact that most Linux users get software mostly or entirely from distro repos), but for those who use proprietary apps on smartphones (Android, in my case), where it's not always as easy to monitor network usage, is there a way to scan installed apps for these malicious SDKs?

      
          
            
            
            
          
        
     

     
    
    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 10, 2026 16:25 UTC (Fri)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082330/)] 
      
      
      
      
      If you're using Google Play Services, turn on Play Protect and have that scan every so often - this will catch any apps that Google has found contain one of these proxies.

Other than that, you can ask Android to tell you how much mobile data an app used; go to "Settings", then "Apps", and it's in the "App Info" screen for individual apps. You can also disable "Background data" if you're suspicious of an app - that stops it using data when you don't have it open and are on mobile; IIRC, this also covers WiFi networks set as "metered", but ICBW on that one.

      
          
            
            
            
          
        
     

     
    

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 10, 2026 20:26 UTC (Fri)
                               by mirabilos (subscriber, #84359)
                              [[Link](https://lwn.net/Articles/1082343/)] (1 responses)
      
      
      
      
      
TEMU is rumoured to contain one. AFAIHH it just runs in the foreground while the device users browse its marketplace.

Note this is hearsay. I have not installed that äpp nor sniffed its traffic myself. But it was the first one where I heard about what is now called residential proxies, via “trojaned” äpps, and from multiple sources.

I’m sure the “link fetchers” from GAFAM äpps can also occasionally do that…

      
          
            
            
            
          
        
     

     
    
    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 13, 2026 10:16 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082503/)] 
      
      
      
      
      
There was an interesting paper recently in ACM TCS from ByteDance: [https://dl.acm.org/doi/10.1145/3816021](https://dl.acm.org/doi/10.1145/3816021)

And by interesting, what caught my attention was:

“Starting in 2020, ByteDance began exploring the use of edge nodes as a partial replacement for CDNs. These nodes mainly consist of idle computing resources on the Internet (e.g., smart home devices and outdated servers), and they are collected by third-party companies and sold in bundles to us at a heavily discounted price compared to CDNs.”

Uh, wut? Third-party companies, selling access to "idle [edge and home] computing resources", and large tech companies like ByteDance are customers for this? Uhmm.. What devices, what companies? What... consent?

      
          
            
            
            
          
        
     

     
    

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 10, 2026 21:42 UTC (Fri)
                               by rgmoore (✭ supporter ✭, #75)
                              [[Link](https://lwn.net/Articles/1082348/)] (2 responses)
      
      
      
      
      How can one avoid unintentionally running one of these proxies?

Some of the other posters have commented on how to avoid these kinds of proxies on your own system, but I want to point out that individual action won't be enough to solve the broader problem.  I don't want to discourage anyone from trying to keep their own system clean, but we will never get rid of these kinds of proxies by encouraging each person with a mobile device to avoid them.  You need to block access to a large majority of the available devices to make any real progress, and voluntary programs that involve real effort are never going to get that level of participation.  This stuff needs to be taken care of at the system level- getting the apps out of app stores, making this kind of thing clearly illegal and prosecuting the offenders, etc.- not the individual user level.

      
          
            
            
            
          
        
     

     
    
    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 10, 2026 23:40 UTC (Fri)
                               by KJ7RRV (subscriber, #153595)
                              [[Link](https://lwn.net/Articles/1082365/)] 
      
      
      
      
      
Thank you for the reminder! I completely understand that, and apologize for any impression my comment may have given that this is primarily a problem to be solved by individual users; that was certainly not my intention. I just want to make sure I am not personally contributing to the problem, however small any one user's part may be; I'm not asking everyone with a smartphone to research every app they use.

      
          
            
            
            
          
        
     

     
    

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Aug 8, 2026 12:43 UTC (Sat)
                               by Funcan (guest, #44209)
                              [[Link](https://lwn.net/Articles/1087876/)] 
      
      
      
      
      
I think many of the sorts of people reading this might be able to help *detect* them at an individual level, and help with raising awareness. Manufacturers are starting to react to complaints about this, and "Why is my smart fridge reading porn sites?" (or camera, baby monitor, TV, etc) articles should have an effect. There are also people convicted of crimes primarily on the evidence that their home IP address was responsible for some piece of traffic, so "Insecure LG smart TV could get you jailed for piracy" is another good headline

      
          
            
            
            
          
        
     

     
    

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 11, 2026 3:04 UTC (Sat)
                               by duelafn (subscriber, #52974)
                              [[Link](https://lwn.net/Articles/1082370/)] 
      
      
      
      
      
I can't answer the monitoring issue, but NetGuard (on f-droid or play store) can block network access per-app. I fully deny network access to about a third of my apps that want network, about another third get access only when the screen is on. Not a perfect fix, but a nice layer of protection.

      
          
            
            
            
          
        
     

     
    

    
      

### How to avoid running a residential proxy (especially on Android phones)?

      
      

 Posted Jul 11, 2026 3:15 UTC (Sat)
                               by marcH (subscriber, #57642)
                              [[Link](https://lwn.net/Articles/1082371/)] 
      
      
      
      
      
For apps you use very rarely but don't want to keep uninstalling and re-installing (the latest, different version), there is a "pause app" button available when you long-press the app. Except... it inexplicably pauses the app only for 1 day :-(

But there is another, permanent option. Long press -> App Info -> Screen Time! You can set it to zero and it stays at zero. It's called "Screen Time" but it seems to block background usage too, hopefully some Android developer can confirm.

(and yes of course this sort of advice is only useful for techies and will do nothing to save the open web)

      
          
            
            
            
          
        
     

     
    

    
      

### Thanks for your efforts and keep up the good work!

      
      

 Posted Jul 10, 2026 16:08 UTC (Fri)
                               by wtarreau (subscriber, #51152)
                              [[Link](https://lwn.net/Articles/1082328/)] (4 responses)
      
      
      
      
      
Hi Jon,

I think that many of us here are totally aware of the problem these bots and proxies are causing to web sites like this one, and the difficulties in fighting them. At least I can say that I haven't noticed anything abnormal on the site here, so your actions were fine from the user experience perspective. Thanks for this!

You're right, it's important never to publicly explain the counter-measures that you apply. Very often some are extremely simple and effective (some easy tricks I've deployed 9 months ago that I imagined would only last one week are still working fine). Also they're often very specific to the site and would hardly adapt to other ones (except for the main principle), so there's little to share by explaining everyone how your specific site is fighting these.

I noticed a 30% drop of traffic on July 2nd, after a 50% one on June 25th that I couldn't explain (mostly attributed to user-agent "sleepbot"). So yes, it seems that such networks are progressively getting dismantled, probably to re-appear somewhere else soon, given that infected browsers (and their unsuspecting users) are just waiting for another C&C to take care of them :-/

I must confess I'm a bit worried about the risk of losing a lot of legit content indexing on the net in the coming years due to installed counter-measures against non-humans. If sites cannot be found via search engines it will become a problem. All this due to AI startups racing in training their own models (or variants).

Maybe it would work better to set up a static central registry of the whole internet's contents that could be scraped by such companies as much as they want without killing small web sites. It could still take a lot of time before we start to see something like this happen though.

      
          
            
            
            
          
        
     

     
    
    
      

### Thanks for your efforts and keep up the good work!

      
      

 Posted Jul 10, 2026 17:15 UTC (Fri)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082335/)] (1 responses)
      
      
      
      
      
The central registry you propose sort of exists in the form of Common Crawl: [https://commoncrawl.org/](https://commoncrawl.org/)

The idea is that you contribute resources to their project, they have _one_ scraper that downloads web content in a polite way (respecting rate limits and robots.txt), and then anyone who wants to can make use of the scraped content without having to re-scrape it.

There are some problems with the approach, but I'm generally pretty happy when I see Common Crawl go by in the server logs because I know that's a bunch of unrelated projects that don't need to send us multiple requests.

      
          
            
            
            
          
        
     

     
    
    
      

### Thanks for your efforts and keep up the good work!

      
      

 Posted Jul 10, 2026 17:46 UTC (Fri)
                               by wtarreau (subscriber, #51152)
                              [[Link](https://lwn.net/Articles/1082337/)] 
      
      
      
      
      
>  The central registry you propose sort of exists in the form of Common Crawl: [https://commoncrawl.org/](https://commoncrawl.org/)

Oh, thanks for the link, I wasn't aware. I'll try to make sure not to block that one!

      
          
            
            
            
          
        
     

     
    

    
      

### Thanks for your efforts and keep up the good work!

      
      

 Posted Aug 6, 2026 23:34 UTC (Thu)
                               by fest3er (guest, #60379)
                              [[Link](https://lwn.net/Articles/1087581/)] (1 responses)
      
      
      
      
      

In my opinion, they aren't scrapers or 'bots. I call all of them internet bandits, legitimate search engines and archivers notwithstanding; they are robbers and thieves, stealing whatever they can to sell to fences who buy and resell stolen property.

I developed my own bandit blocking methods. At one point, my firewall was blocking around 1.2 million IP addresses (imagine that). I made adjustments. Presently, it blocks 33k IPs, 600 /24s, 8000 /16s, and 700 other-sized net blocks. In fact, I presently have over 2M IPs collected, which break down to 690k /24s and 46k /16s. The IPs break down to:
- 1.7M with one access,
- 230k with two accesses each,
- 194k with 3-10,000 accesses each,
- 50 with over 10,000 each, and
- one with over 65,000 accesses.

Without these methods, phpBB's 'users in the last 5 minutes' would have exceeded 5000, and probably would've been over 10k. There would've been 10-50 established TCP conns and many more in close/wait states.

With my methods, there are only several established TCP conns and 30 or more conns in close or wait states. Traffic over the past week has averaged around 16kB/s.

For sure, my crude methods block legitimate users; I whitelist them should they contact me. I'd like to fine-tune my processes, but don't necessarily have the time or knowledge (like employing statistical processing which should reveal the difference between human and 'bot accesses). I'm tempted to redirect some of them to a honey pot and/or a tar pit.

The legitimate worldwide 'internet services' industry needs to band together to address the problem. Here are a few of the things that came to mind (in no particular order):

- Unify world-wide RDAP data; each region seems to record data differently, and seems to record different (or not all) data.

- Expand RDAP to make it easy for all internet users to identify the assignees who use IP addresses and netblocks, returning country, and company name where applicable or the person's name.

- Expand RDAP to identify standard uses and statuses of netblocks and IPs (end users, VPS farms, cloud server farms, web server farms, search engines, stolen nets, gateway routers, et alia), and require assignees to keep that data up-to-date.

- Provide tools (source code) so all internet users can look for general parity between incoming and outgoing traffic. (Have my private network or any of my systems been hijacked?)

- Require IP assignees to identify FQDNs that resolve to each of their IPs/nets.

- Require FQDN owners to identify all IPs that each FQDN resolves to.

- Require cloud providers to monitor their systems for improper use (such as scraping and probing) and block/ban such users.

- Prohibit companies from claiming to scrape and probe IP and sites "for your benefit" when they are really doing it for their own benefit and profit.

- Require ISPs and others to allow end users to easily assign/relate properly acquired FQDNs to their IPs.

We users of the internet deserve to be able to easily identify who is connecting to our private internetworks. For example, if Acme Systems Engineering is probing my gateway in a harrassing way, I should be able to blacklist all of their IPs. If someone using Peaker Cloud Computing Services is hammering away at my gateway using multiple IPs, I should be able to block of of Peaker's IPs used in their cloud services. The system should be nearly trivial to use and should return data that are easily read by humans and easily parsed by systems.

[This is probably enough for one comment....]

      
          
            
            
            
          
        
     

     
    
    
      

### Thanks for your efforts and keep up the good work!

      
      

 Posted Aug 7, 2026 5:31 UTC (Fri)
                               by anselm (subscriber, #2796)
                              [[Link](https://lwn.net/Articles/1087612/)] 
      
      
      
      
      

Here are a few of the things that came to mind (in no particular order):

[…]

While these proposals are undoubtedly all well-intentioned and make a lot of sense, they sound like way too much hassle to get everyone to comply with. In fact, we should keep things simple and straightforward, and merely require the ubiquitous implementation of [RFC 3514](https://datatracker.ietf.org/doc/html/rfc3514). Tadaa! Problem solved.

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 10, 2026 20:42 UTC (Fri)
                               by roc (subscriber, #30627)
                              [[Link](https://lwn.net/Articles/1082349/)] (20 responses)
      
      
      
      
      
> all of the major vendors are silent on the topic of why it is so easy to put apps with residential-proxy functionality into their app stores.

Google's rules already forbid non-user-authorized "residential proxies": [https://support.google.com/googleplay/android-developer/a...](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en)
But if the user gives genuine consent to it, should they still be banned? That's a tough call.

Of course developers can and do violate those rules. Then the problem is that it's not really possible in general to detect that code is going to break those rules just by inspecting it. So how do you detect violations other than by people reporting them and then shutting them down after the fact? That's roughly what happens now and it's better than nothing, but still whack-a-mole.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 10, 2026 22:29 UTC (Fri)
                               by rgmoore (✭ supporter ✭, #75)
                              [[Link](https://lwn.net/Articles/1082359/)] (19 responses)
      
      
      
      
      Google's rules already forbid non-user-authorized "residential proxies" But if the user gives genuine consent to it, should they still be banned? That's a tough call.

No, they shouldn't be allowed.  Banning them is at least as much about protecting the whole internet from their pernicious effects as it is about protecting the individual user, so it shouldn't be up to the individual user any more than emissions controls should be up to the individual driver.

I would also argue that for any user to give "genuine consent", they would need to be given the option to have the same app without the proxy.  If you let the author condition use of their app on accepting the proxy, consent is at least somewhat coerced.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 10, 2026 23:11 UTC (Fri)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1082364/)] 
      
      
      
      
      
> I would also argue that for any user to give "genuine consent", they would need to be given the option to have the same app without the proxy. If you let the author condition use of their app on accepting the proxy, consent is at least somewhat coerced.

And do they ask the VICTIM for consent? Of course not, they know consent would be refused.

Let's say I run a web server. The whole point of this scheme is bypass/dodge my attempts to prevent my site being DoS'd by scrapers. Whether it's criminal or not (in Europe it probably is), the whole point of this is to attack my server in a manner to which "you knew or should have known" I would have refused to consent to.

I find it hard to think of any use to which such a network would be put, that is not in violation of England's Computer Fraud And Abuse Act. Whether said act could be enforced is another matter :-( , but consenting to your computer being used for such things could also be criminal under the "going equipped to ..." rules ...

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 11, 2026 5:28 UTC (Sat)
                               by roc (subscriber, #30627)
                              [[Link](https://lwn.net/Articles/1082380/)] (14 responses)
      
      
      
      
      
The "I should be able to run whatever code I want on my device" people would surely object.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 10:29 UTC (Sun)
                               by tux3 (subscriber, #101245)
                              [[Link](https://lwn.net/Articles/1082433/)] (6 responses)
      
      
      
      
      
I'm one of those people, but in the sense of supporting third-party package managers (à la F-Droid).

But then people will also "consent" to being scammed over the phone, because we often don't really understand what we're consenting to when the person asking for consent is also the attacker.
There's a parallel with Public Health as a medical field. If you allow that the general public of non-experts sometimes make bad choices for themselves and others, there's a balance in intervening without creating a system where people are stripped of all autonomy.
Sham doctors can't officially practice medicine or advertise snake-oil as a panacea. I'm sure you can still find them if you really look, they just can't be near anything official that could trick the average person into "consenting" with a scam.

So I'd let people install arbitrary things if they really go look for them, but I wouldn't let botnets advertise on the official app store.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 11:45 UTC (Sun)
                               by mb (subscriber, #50428)
                              [[Link](https://lwn.net/Articles/1082436/)] (5 responses)
      
      
      
      
      
> there's a balance in intervening without creating a system where people are stripped of all autonomy.

Absolutely not.

Google has *no* business "intervening" with my actions whatsoever.
I am an adult and I can do decisions on my own.
I do not need Google to "take care of me" and install a 24 hour barrier so that I "won't hurt myself".

If I fall for a scam, then it is my own fault. I am an adult. I don't need mommy Google to take care of that.

This is obviously not about user's security.
Google has obviously been locking down their platform, step by step, over the last couple of years.
And they won't stop here.

Give me *one* button to opt out of this nonsense.
No nagging, no scare questions, no 24h delays, no nothing. Just a button "I'm grown up already, no need for mommy Google to protect me".

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 12:06 UTC (Sun)
                               by pizza (subscriber, #46)
                              [[Link](https://lwn.net/Articles/1082439/)] (4 responses)
      
      
      
      
      
> Google has *no* business "intervening" with my actions whatsoever.

You get to say that only *after* you've built (and maintain) your own smartphone platform from does not rely on any ongoing Google services or resources.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 12:21 UTC (Sun)
                               by mb (subscriber, #50428)
                              [[Link](https://lwn.net/Articles/1082440/)] (3 responses)
      
      
      
      
      
>You get to say that only *after* ...

Obvious nonsense. Here's what gives me the right to do that at any time: [https://www.gesetze-im-internet.de/gg/art_5.html](https://www.gesetze-im-internet.de/gg/art_5.html)

Android is not a free market product that I can choose to use or not to use.
Android (or iOS) use is mandatory for an increasing amount of daily tasks.

I *wish* I *could* drop Android and use something I built on my own or any other alternative product of my choice.
This is not possible in the real world we live in, though.
And that is why regulatory actions against Google are necessary to keep user's freedoms.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 13:26 UTC (Sun)
                               by pizza (subscriber, #46)
                              [[Link](https://lwn.net/Articles/1082445/)] (2 responses)
      
      
      
      
      
> Obvious nonsense. Here's what gives me the right to do that at any time: [https://www.gesetze-im-internet.de/gg/art_5.html](https://www.gesetze-im-internet.de/gg/art_5.html)

Uh, that appears to be solely about freedom of expression and learning [1]; which as far as I can tell you're fully exercising?

It says nothing about third parties being obligated to enable you to express yourself, much less require said third parties to build, maintain, and support systems that do what *you* want.  Nor does it appear to have any bearing on markets or commerce in general.

Meanwhile, Google's device-restricting actions are backstopped by EU laws that make it expressly illegal to break DRM.   Repealing that would achieve far more freedom (to both individuals and markets) than piling volumes of status-quo-entrenching regulations on top.

[1] while also making it clear that said freedoms are not absolute ("The freedom of doctrine does not absolve off from fidelity to the Constitution" according to Firefox's translation)

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 12, 2026 13:43 UTC (Sun)
                               by mb (subscriber, #50428)
                              [[Link](https://lwn.net/Articles/1082446/)] (1 responses)
      
      
      
      
      
>much less require said third parties to

Google is not a random third party in the market anymore.
Google is infrastructure at this point.

And as such Google must be criticized for their actions and regulated if they exploit their market position.

And yes, I can say this and you can do nothing about it. "You get to say that only *after*..." is completely false.
If you say that I can't criticize Google for their actions unless I build a system on my own you are completely wrong.
You are trying to move the goal posts.

>EU laws

Yes, there are many more things to criticize, beyond Google.

>Repealing that would achieve far more freedom

You know, I can be against multiple things at the same time.
There is no need to select and prioritize.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 13, 2026 11:29 UTC (Mon)
                               by pizza (subscriber, #46)
                              [[Link](https://lwn.net/Articles/1082507/)] 
      
      
      
      
      
> Google is infrastructure at this point.

....Then Google should be able to collect taxes to pay for said infrastructure. 

You don't get to have it both ways.

> If you say that I can't criticize Google for their actions unless I build a system on my own you are completely wrong.

No, I'm saying that it is highly naive to expect Google to cater to *your* wants (not even "needs") while you freeload off of their services and rely on what their enormous engineering staff produces.

> There is no need to select and prioritize.

When you have (very) limited resources at your disposal, most folks want to put those to where they will be the most effective.  But hey, you do you.

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 13, 2026 16:56 UTC (Mon)
                               by rgmoore (✭ supporter ✭, #75)
                              [[Link](https://lwn.net/Articles/1082694/)] (6 responses)
      
      
      
      
      

The "I should be able to run whatever code I want on my device" people are wrong.  It's the same old saw about your right to swing your fist ending at my nose.  Your right to run what you want on your device ends when it starts causing damage to other people's devices.  If you want to run a proxy on your device, you are responsible for making sure it isn't DDOSing someone's web site.  If you aren't willing or able to take that responsibility, don't run a proxy.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 13, 2026 18:24 UTC (Mon)
                               by mb (subscriber, #50428)
                              [[Link](https://lwn.net/Articles/1082714/)] (3 responses)
      
      
      
      
      
Google has to stop playing Police and State.

If I punch you in the nose or if I DoS your server there already are more than enough processes in place to make me not do that and punish me if I do it anyway.
There is absolutely no need for restricting what I can run on my device. Except for Google establishing a locked down eco system, of course.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 14, 2026 7:56 UTC (Tue)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082740/)] 
      
      
      
      
      
+100 to this. Having vast technocratic-corporates act as police, judge and jury, with 0 transparency and (unless you complain on social media and somehow manage to go viral) 0 means of effective appeal is dystopian. Bollocks to that.

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 20, 2026 1:54 UTC (Mon)
                               by ssmith32 (subscriber, #72404)
                              [[Link](https://lwn.net/Articles/1083547/)] (1 responses)
      
      
      
      
      
Google, also, per your logic, can run whatever code they like on their servers, including code that rejects your code from their app store, which runs on their servers.

Google does not police or prevent you from running residential proxies on your phone. They prevent you from placing that code for download _on their servers_ .

Even the most ardent free software folks do not argue that you have a right to be platformed by any platform of your choice.. only to build your own platform. 

Sideload your proxy onto your phone to your hearts content - google won't stop you.

Heck, run a whole other OS on the phone - google won't stop you there either.

You are, in fact, arguing that google be forced to run code on their servers at your whim.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 20, 2026 5:17 UTC (Mon)
                               by mb (subscriber, #50428)
                              [[Link](https://lwn.net/Articles/1083548/)] 
      
      
      
      
      
>Google, also, per your logic, can run whatever code they like on their servers

True

> Sideload [...] google won't stop you.

Except they do?

[https://keepandroidopen.org/](https://keepandroidopen.org/)

Over the last couple of years they have been installing a massive amount of anti features to make sideloading harder and harder.
We are at the point where I cannot buy a phone and install what I want right away.
There is absolutely no sign that they will stop here.

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 19, 2026 13:51 UTC (Sun)
                               by Segora (subscriber, #8209)
                              [[Link](https://lwn.net/Articles/1083497/)] (1 responses)
      
      
      
      
      
The analogy is flawed in multiple ways:

1. Conflating capability with action: Just like most people would balk at the notion of restraining every human just because they _could_ hit somebody on the nose, it seems vastly imbalanced to constrain all their devices because they could be used to cause harm to others.

2. Locus of control: The brain controls whether the fist gets to travel towards someone else's nose. In the implied restriction system, a third party would determine the limits of capability of a device.

3. Misattributing the Source of Harm: Putting the blame on the tool rather than on how it's used discounts legitimate uses like development, security auditing and self-sovereignty.

As already covered in other comments, a more balanced approach would be to sanction the use of devices to cause harm, rather than their existence.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 20, 2026 12:01 UTC (Mon)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1083538/)] 
      
      
      
      
      
> 1. Conflating capability with action: Just like most people would balk at the notion of restraining every human just because they _could_ hit somebody on the nose, it seems vastly imbalanced to constrain all their devices because they could be used to cause harm to others.

What you are missing in this particular case, is that pretty much the SOLE use of these botnets is to cause harm to other people.

It is illegal in ?all? European jurisdictions to access a computer system in a manner that is not sanctioned by the owner of said system. Pretty much the only use of these botnets is to get round the attempts of said owners to block unwanted access.

In other words, I cannot think of any use of these botnets that is not illegal. Can you come up with any? Tools that have a high potential for mis-use often need to be licenced. These botnets should be licenced, and I strongly suspect there will be no use-cases that warrant the issuance of said licence.

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 11, 2026 14:49 UTC (Sat)
                               by ibukanov (subscriber, #3942)
                              [[Link](https://lwn.net/Articles/1082407/)] (2 responses)
      
      
      
      
      
What about offering a cheaper version in return for the user consent to allow to use their network?

I also wonder why does not BrightData not offer users just to run their software for money on devices? Maybe it will be the next step.

      
          
            
            
            
          
        
     

     
    
    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 11, 2026 20:12 UTC (Sat)
                               by josh (subscriber, #17465)
                              [[Link](https://lwn.net/Articles/1082419/)] 
      
      
      
      
      
> What about offering a cheaper version in return for the user consent to allow to use their network?

Nuke it from orbit. If app stores are doing any good at all, this is the kind of thing they should block.

      
          
            
            
            
          
        
     

     
    

    
      

### Preventing this at the app store level is hard

      
      

 Posted Jul 13, 2026 16:57 UTC (Mon)
                               by rgmoore (✭ supporter ✭, #75)
                              [[Link](https://lwn.net/Articles/1082691/)] 
      
      
      
      
      

I would say that allowing a cheaper version that includes the proxy could count as informed consent as long as the vendor was completely honest about what they were asking of customers running the proxy.  But that still only counts the customer consent aspect; it doesn't deal with the pernicious uses of residential proxies.  I still believe there are valid reasons for blocking any service, like these residential proxies, that causes massive damage to third parties who weren't give a say.

      
          
            
            
            
          
        
     

     
    

    
      

### IP blocks should be neither authentication nor authorization

      
      

 Posted Jul 10, 2026 20:59 UTC (Fri)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082346/)] (99 responses)
      
      
      
      
      
> more lasting solution before the entire Internet is driven behind defensive walls

It already is in large part. Have you tried browsing the internet from outside a well-known residential or end-user-VPN IP block? Tons of sites block access out of the gate or put up so many "click the traffic lights" gates that they might as well have blocked you. 

Residential VPNs are, yes, often scummy, but also an understandable reaction to much of the internet using routing tables as a proxy for proof of humanity. You can't stamp them out, either: there will always be people willing to trade their home bandwidth for trinkets. You can't stop them without stamping out general-purpose computing altogether, and I don't think anyone wants that.

What we need instead is an open protocol through which network clients can provide proof of interactive humanity under zero knowledge in such a way as to resist cloning and Sybil attacks. I believe recent advances in zkVMs and remote attestation make such a protocol possible. If we had it, 

1. residential VPNs would cease to be special and incentives for scummy tricks would disappear,

2. assurance of humanity could shift from annoying interstitials to automatic protocol exchange (because we could prove recent human interaction end-to-end authenticated from hardware without sacrificing privacy), and

3. site operators could, in principle, create a market for non-interactive access permits (e.g. under an anonymous cap-and-trade scheme), naturally rate-limiting accesses while avoiding the monopoly-reinforcing effects of just whitelisting IP blocks owned by this or that archive or search engine.

Interactive users couldn't sell their interactivity for trinkets without setting up robots to manipulate their input devices or doing tedious link-clicking themselves. Channel- and hardware-binding would mitigate proxy attacks, again anonymously. Remote attestation doesn't have to be a privacy nightmare. It can *enable* privacy!

Such a scheme would be compatible with free software operating systems too, since input attestation would be pass-through. You'd just prove, remotely, that the same TPM generated both the input attestation and your TLS session key. Linux can drive this hardware just fine.

Privacy-preserving protocols like this have become practical just recently, over the past few years. It's a shame we haven't yet begun to explore their potential. The alternative is something like the Cloudflare Monetization Gateway [1], which accomplishes similar goals, but without the privacy or the democracy. A world where Cloudflare becomes de-facto internet gatekeeper is a worse world than one with an open attestation ecostystem.

[1] [https://blog.cloudflare.com/monetization-gateway/](https://blog.cloudflare.com/monetization-gateway/)

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 4:11 UTC (Sat)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1082378/)] (95 responses)
      
      
      
      
      
Accessibility tools work by automating user interactions.  In fact, one of Windows’s accessibility frameworks is called “Microsoft UI Automation”.

Unless one imposes an allowlist of accessibility tools, one won’t be able to use hardware attestation to prevent automating a user’s actions.  What one can do is tie them to a user identity, and therefore rate-limit or ban abusive users.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 6:08 UTC (Sat)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082383/)] (94 responses)
      
      
      
      
      
> Unless one imposes an allowlist of accessibility tools

Accessibility tools translate one form of user input into another. They don't generate interactions out of thin air. They can carry through attestations made against their original inputs. Besides: what you really want to do is attest physical human presence, and there are multiple ways to do that, of which using attested input stamps is just one.

> What one can do is tie them to a user identity

Requiring identity linkability for everyone is far worse than complicating accessibility tools for a few.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 19:53 UTC (Sat)
                               by nhippi (subscriber, #34640)
                              [[Link](https://lwn.net/Articles/1082411/)] (89 responses)
      
      
      
      
      
> Requiring identity linkability for everyone is far worse than complicating accessibility tools for a few.

I don't really see a long term way for web without Micropayments. If rendering your page costs you 0.01c, you ask for 0.02c. Should be cheap enough for regular users to not care, but expensive enough for botnets to have to with what they crawl and with what volumes.

Unfortunately, nobody is really working on easy to use, frictionless anonymous micropayments. So I guess this is the end of open internet.  

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 20:07 UTC (Sat)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082418/)] (7 responses)
      
      
      
      
      
It's a quirk of human psychology that there's this huge behavioral discontinuity as a price reaches zero. People hate the anxiety that micropayment schemes produce. There's a reason "nickel and diming you" is common idiom. If there are to be micropayments, they're going to be limited, practically speaking, to autonomous systems.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 21:23 UTC (Sat)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082422/)] (1 responses)
      
      
      
      
      
There was a project that seemed almost perfect for that: Scroll. 

You paid for a subscription ($7 a month, AFAIR) and then the participating sites got a proportional share of it (with some adjustments). And in exchange, you gained an ad-free browsing experience.

I totally loved it. Unfortunately, it got gobbled up by Twitter and promptly killed.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 11, 2026 22:55 UTC (Sat)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082425/)] 
      
      
      
      
      
Google Contributor was also very good. Similar model. I loved it, along with the three other people who tried it. 

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 23:37 UTC (Mon)
                               by marcH (subscriber, #57642)
                              [[Link](https://lwn.net/Articles/1082733/)] (4 responses)
      
      
      
      
      
> It's a quirk of human psychology that there's this huge behavioral discontinuity as a price reaches zero. People hate the anxiety that micropayment schemes produce.

Exactly why mobile phone operators have invented their "unlimited" plans with... various GB maximum/month. It's a genius psychology trick that removes that "How many bytes to open this page?" anxiety. It's genius because it's as simple as saying the opposite of the truth - and it works!

That same "Alternative Facts" genius has been successfully leveraged in other areas - but I digress :-)

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 6:32 UTC (Tue)
                               by anselm (subscriber, #2796)
                              [[Link](https://lwn.net/Articles/1082739/)] (2 responses)
      
      
      
      
      It's genius because it's as simple as saying the opposite of the truth - and it works!

My mobile phone plan started out years ago with a fairly-low-but-acceptable monthly data cap but the limit has by now ascended into such stratospheric heights that, as far as I'm concerned, it might as well not exist at all. There are probably people who manage to bump up against it but I'm not one of them. I have no problem with “unlimited” really meaning “unlimited (within reason)” if it prevents bandwidth hogs making things worse for everyone else.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 12:39 UTC (Tue)
                               by marcH (subscriber, #57642)
                              [[Link](https://lwn.net/Articles/1082752/)] (1 responses)
      
      
      
      
      
That is fair: the truth is often "practically unlimited unless you pre-download more TV series than you have time to watch". But my main point stands: the "unlimited" is what adresses the micro-payment anxiety. I think that anxiety is strong because humans are so bad with numbers.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 4:35 UTC (Thu)
                               by mathstuf (subscriber, #69389)
                              [[Link](https://lwn.net/Articles/1083102/)] 
      
      
      
      
      
Back when it was the home Internet service doing data caps, I really wanted ads to have to specify "time to cap exhaustion at advertised maximum speed" as well. That "400 Mbps" isn't very useful if you slam into the data cap on day 3. As I did when visiting my parents while they were trialing some 4G home internet box (they went back to cable Internet service after that).

      
          
            
            
            
          
        
     

     
    

    
      

### Unlimited mobile data plans

      
      

 Posted Jul 14, 2026 8:55 UTC (Tue)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082748/)] 
      
      
      
      
      And regulation has taken care of that trick, in many jurisdictions; if the plan is "unlimited", there can be no limits applied just because you've used more than a certain amount of data.

Which is why you get plans with 50GB of full speed data, and unlimited data at 1 Mbit/s on top of that, or plans where users who use more than 1 TB/month are selected to experience worse effects from congestion (but are unaffected where the cellular network is not congested), or other variants that make it clear that you're not getting a truly unlimited plan.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 12, 2026 21:54 UTC (Sun)
                               by JanC_ (subscriber, #34940)
                              [[Link](https://lwn.net/Articles/1082479/)] (1 responses)
      
      
      
      
      
People often visit thousands of web pages a day. Do you really think people want to pay hundreds of euros/dollars a month on top of all the costs they already have…?

(And of course the scummy sites full of spyware, and other ways to scam users will remain free under this scheme!)

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 12, 2026 22:13 UTC (Sun)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082480/)] 
      
      
      
      
      
How does it follow from payments *existing* that the typical user would pay hundreds per month?

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 9:34 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082502/)] (75 responses)
      
      
      
      
      There's a huge social problem with frictionless anonymous micropayments (and one that's hard to solve via technical means): how do you stop bad actors from being the primary users of the system?

For the system to be useful, it has to be able to transfer large sums of money to the sites; if you're collecting 0.02¢ per page render, you need to be able to collect $20 million if you're hit by 1 billion accesses. That creates two social problems:

- If I'm a bad actor, what makes it not worth my while infecting millions of clients with malware to collect 0.02¢ per client via my dodgy network of apparently legitimate (but actually not) sites?

- If I'm a payer, how do I recover my money if a bad actor infects my device and causes it to access billions of pages? How do you distinguish "payment made due to bad actor" from "payer had buyer's remorse"?

- If I'm a bad actor, how do you stop me accessing millions of pages to copy, then using the money recovery mechanism to ensure that I don't actually pay, without preventing legitimate payers from having access to the money recovery mechanism?

These are all really hard problems to solve - and our current systems don't solve them particularly well, but they just about manage on the basis that no-one in the network is truly anonymous, and thus you can use the courts to recover your money. That stops working if, instead of a small number of large cases, you have a truly large number of "de minimis" cases.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 11:04 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082506/)] (17 responses)
      
      
      
      
      
Perfect is the enemy of good enough perhaps.

There are distributed payment systems in fairly wide use today, 1 in particular which is viable for micro-payments down to about a ¢. They just don't do recovery. So the answer to "but recovery is hard" quite possibly is that you can not solve it and the resulting system may still be adequate for use - if not as perfect as you'd advocate for.

Indeed, a number of people would argue that some centralised 'recovery' authority able to reverse transactions at a network level would be a *malfeature* in any distributed, online, (micro)-payments system. Non-reversability (at a network level), they would argue to be an essential feature (and this would *not* preclude availing of legal action to recover funds).

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 11:59 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082508/)] (16 responses)
      
      
      
      
      Your last paragraph is self-contradictory; legal action involves a centralized "recovery" authority (the legal system) getting involved to force the reversal of a payment, but you're also saying that the existence of that authority is a malfeature that should not exist. It can't be both.

Without it, though, you face the fraud problems; sophisticated users can avoid being bitten too badly by fraud, but you're going to have to solve the mass-market chicken-and-egg problem somehow. Most people won't risk their money without a decent chance of a high reward, and without most people being willing to use whatever "fraud is your problem" payments network you create, sites have no incentive to require people to use it (since by doing so, they lose all their users).

And that, in a nutshell, is the issue that any micropayments system has to solve somehow. How do you bootstrap popularity of a micropayments system if payees won't come on board en-masse until there's a significant number of people willing to pay with it, and payers won't come on board until there's either very low risk of fraud, or payees have signed up en-masse?

After all, if there is a system that is completely viable for small payments, there would be a site like Patreon, Ko-fi, Substack, or similar that accepts it - but none of the big "pay your content creator" sites do accept alternatives to cards.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 12:14 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082510/)] (15 responses)
      
      
      
      
      
To be clear, I wrote in reply to the possibility /micro-payment system/ must have some kind of recovery mechanism, even though (as you stated) that is technically very hard to solve, which kind of falls out of your comment.

I agree, it is technically hard to solve, and I agree with you it is a social problem. So I'm pointing out that there are micro-payment systems which just ignore that problem, and it is indeed left as a social problem to solve. In which case problem #3 is solved - it can't happen. Problem #2 is potentially solvable, depending on context. Problem #1 is partly solved - the resources were paid for, and the server of the resources was not (financially) harmed.

The implication in your comment was there was a problem that the micro-payment system itself had to solve somehow, even though it was hard to solve / unsolvable at the technical level. I'm saying micro-payment systems definitely already exist, with reasonably non-trivial use, and they do so without having tried to tackle the problem you (possibly) implied needing solving. 

I.e., the micro-payment system can go ahead and be used, and that social issue of recoverability can be left for later solving (by probably a plethora of different social solutions, which may evolve). It's not an obstacle as such.

I can pay for a variety of things (digital services particularly) with said micro-payment system. I can buy (e)SIMs, VPNs, email hosting, VPs, Proton accounts and other similar services, AI hosting, contract developors, donate to various orgs (inc. FSF), etc., etc.. It's already bootstrapped and being used. Maybe it's not perfect enough for you, but it's good enough for a chunk of users.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 12:17 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082512/)] (14 responses)
      
      
      
      
      If you don't solve these problems to a point where, as an unsophisticated user, my funds are not at risk if I'm hacked, then you're limited to being something for sophisticated users, which means that the web as a whole can't use the system, since most users aren't sophisticated.

Any such system that's good enough for mass adoption would be in a good position to replace PayPal, Venmo, Patreon and Ko-fi; once you've done that, then you've got a system that's viable for the mass market. Until then, you have a minority use system that's suitable for sophisticated users, but excludes most of the world.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 12:52 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082643/)] (13 responses)
      
      
      
      
      
Nothing would stop a PayPal like entity acting as a gateway to whatever underlying micro-payment system. If a PayPal like frontend is what is needed for "normal" users, nothing technical stops that.

The fundamental issue, as you already stated, is that the blocker is a social issue. Though, it's just /not/ the one you stated. Rather, the reason we can't have a global, ubiquitous, universal access, distributed micro-payments systems is the same reason that the existing PayPals, Venmos, etc., can't act as a gateway to such a system: The governments of the world do not want it - they only want something they can control.

And so long as there are different and unaligned blocks of states in the world, we can never have that global, ubiquitous, universal access system.

And even if all were aligned, they would not allow us to have a /private/ system, and quite probably also not a universal-access system.

However, at the technical level, the micro-payments system(s) are built and are in-use. I wish LWN would integrate something with the accounts system, so I could add "Pay for LWN subscription" to my list of digital stuff I can pay for with distributed Internet money.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 13:00 UTC (Mon)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082649/)] (1 responses)
      
      
      
      
      
There are almost certainly complications on our end to receiving payment in that way, but I don't think we would be opposed in principle — letting people pay us is always a good idea. The difficult part would probably be integrating things with our payment processor.

Could I ask what form of distributed internet money you prefer, just so that I know what to look for when investigating the possibility?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 14:33 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082681/)] 
      
      
      
      
      
My preferred one would be Monero. It's technically beautiful. It's private. Transaction fees are low enough to be viable for ¢ level payments. BTC is obviously the big one - but higher fees.

I don't know about your payment processor. There are open-source distributed Internet money payment processing platforms you can self-host, and integrate yourself into your site. E.g., BTCPayServer, MoneroPay (moneropay.eu) - I don't know how good those are. There are also service providers, like mixpay.me. Some of the big payment processors are starting to get into accepting some crypto payments - but usually heavily constrained by jurisdiction, which may make it less attractive for the payer even if it might be more convenient for the payee.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 13:10 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082648/)] (10 responses)
      
      
      
      
      But that in turn is the core of the problem - there's nothing unsolved in the technical arena there.

What we lack is the PayPal-like frontends that make it usable for the ordinary person - and I don't buy your "government blocks it" conspiracy theory, given that entities like Coinbase, Crypto.com, Binance, Kraken and others are perfectly permitted to trade in various cryptocurrencies, and there exist entities like MetaMask on top that also supply cryptocurrency wallets in the open and legally.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 13:59 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082652/)] (9 responses)
      
      
      
      
      
It's not a conspiracy theory. Governments will not allow global, universal-access distributed payments system to integrate easily with their own financial systems (inc. the kinds of retail-user friendly entities you gave examples of). Firstly, because there are a number of unaligned blocks of states, and at least 2 of those blocks wish to heavily limit (if not entirely block) access to/integration with the payments system in their own blocks to certain other blocks/states. Secondly, because nearly all are implacably opposed to entities/people within their blocks having access to distributed, universal-access payments systems.

Those are not conspiracy theories, those are basic facts of regulations that governments have brought in and are bringing in more and more regulations to strengthen.

All the entities you mention are legally or de facto unavailable to many people across the world. MetaMask is open-source and can't be stopped even if Consensys disappeared tomorrow, but it does not integrate with the traditional financial system either (AFAIK).

We can not have a global, universal access, distributed micro-payments because of those social reasons. What we have today are a number of 'islands' of gated-access micro-payments systems, with high-friction or even fully-blocked channels between them; and running in parallel alongside those systems are a couple of much smaller - but growing - truly distributed, universal-access micro-payments systems.  At best, if somehow all those blocks were aligned, we could have a global, semi-distributed, *gated-access* micro-payments system, given the stance of many governments; but then we'd still have the truly distributed, universal-access micro-payments systems running alongside them.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 14:02 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082677/)] (8 responses)
      
      
      
      
      But, while we have these entities, they're worse for unsophisticated users than things like PayPal (which is also not a "global, universal-access payments system" by your standard, since it's blocked in some states).

And I'm saying that unless you can displace at least one of PayPal, Ko-fi, Patreon or Venmo, you've not got a system that's suitable as a micropayments system; you've got something that sophisticated users who can manage their own fraud risk can use, but not something suitable for the mass market.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 15:12 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082683/)] (7 responses)
      
      
      
      
      
>  unless you can displace at least one of PayPal, Ko-fi, Patreon or Venmo, you've not got a system that's suitable as a micropayments system; 

The point is we have no universal micropayments system because we have high regulatory friction.

A universal micropayments system would not displace the examples you give, rather those examples would become gateways to such a universal system - in addition to allowing those who wished to directly interact with said universal micro-payments system with software under their own control. 

That none of those examples you give easily be integrated with (and are not universally accessible - e.g., I don't think I can use Venmo, and possibly you can't either if I remember correctly about where you're based), is because of a lack of a suitable universal micro-payments system. Which is cause of high regulatory friction (including severe fragmentation). Which is a social problem. ;)

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 15:19 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082685/)] 
      
      
      
      
      
And to be clear: I can't buy an eSIM with Venmo - cause I can't access Venmo. Even if I have access to something like PayPal, many other people do not and it could well be that the person/entity I want to make a financial transaction with does not have access. 

For a large chunk of the world, it is very difficult to conclude financial transactions with them, via the "retail friendly" way - and the methods available are not suitable for micro-payments (and are not recoverable either!). For a certain section of the world there is no available method.

*Other* than the distributed Internet money methods - those work well. And the friction of the other methods is such that even many "normal users" will be willing to overcome the UI-overheads. We /could/ easily have the retail friendly UIs, and integration with the types of entities you list, if not for the high regulatory friction.

So it's all social, as far as I'm concerned.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 15:31 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082686/)] (5 responses)
      
      
      
      
      You're looking too far into the future - I'm saying that if there exists a system that's suitable for micropayments, there would be a Ko-fi, PayPal (friends and family only - I'm not expecting the full gamut of PayPal services to be taken over by it), Venmo, Zelle, or similar service competitor built around that system, and demonstrating that the system is suitable by being a friend-to-friend money transfer system for people in the USA (only - I'm not expecting this to be a global system) that outcompetes the existing payment systems.

If you can't build a system that's better than the existing payment systems for one country, then your assertion that your system is better than the existing payment systems is suspect; why hasn't someone used the network to outcompete the existing players?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 16:10 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082689/)] (4 responses)
      
      
      
      
      
Well,

a) even within a country there is very high regulatory friction (true for at least 2 of the biggest blocks in the world)

b) despite that friction, there are a number of places that do accept universal, distributed, micro-payments. And I find it as easy, if not easier, to use than the "retail friendly" stuff. 

E.g., I topped up my kid's eSIM and I can just open the app on my Linux desktop, type my password (optional - my desktop is already obviously secured, but belt and braces), copy the address and amount from the payer's site (or the payer's processor) and send the payment. And it clears within a few minutes. 

With the "retail friendly" stuff you prefer, the flow is similarish, but I type stuff (CC card) into the processor form, plus I have to type more stuff to satisfy algorithms, then I have to wait while it redirects through 1 or more websites - which sometimes fails - then I have to open an app on my Android phone, so I have to authenticate to my phone, then open the app and authenticate on it with another PIN, then I have to confirm the push notification - which sometimes will have failed to arrive. Then I have to go back to the website and click on a button there, and then wait for it to redirect back from the processor iframe or page to the original site.  Also, sometimes, for whatever reason, the bank decides something is suspicious and blocks stuff and I have to phone them - sometimes that can take quite a while. Sometimes I'm abroad, and this can be a real PITA because of timezones (plus, cost of international phone calls - maybe I was buying the eSIM cause that was my Internet and phone access!).

I don't really see the major UI win for the "retail friendly" thing, the distributed Internet money micro-payments thing is actually a /lot/ easier and _far more reliable_ for me. But YMMV.

Also, because I want to have a phone that isn't a complete blob of god-knows-what crap from some big mobile company and all the companies that paid them to push their crap into said blob, and instead run a bit-more-open/far-fewer-blobs OS on my phone, this "retail friendly" app sometimes has failures after updates and I have to spend an hour on the phone to the bank to get them to clear some weird failure condition that so I can reauthenticate my phone. But that's another discussion.

Finally, the internet, distributed micro-payments thing is still very young. It is kind of normal that early technology still doesn't have optimal UI or adoption. If "it must have optimal UI and UX" is a precondition for believing anyone should use it, then... it's catch-22 (esp. if a great part of the UX hinges on adoption).

Again, perfect is the enemy of good. Despite the lack of perfection, there are many use-cases where distributed Internet money beats the "retail friendly" stuff. And in time, it can go from "good enough for these use-cases" to "good enough for more", and with enough time, maybe we see enough adoption that the regulatory friction becomes unsustainable (particularly as our generation, which is driving the regulation because of vested interests, ages out of holding the reins of power).

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 8:47 UTC (Tue)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082746/)] (3 responses)
      
      
      
      
      You are, however, by definition a "sophisticated user" taking responsibility for your own fraud and security risks.

The whole point of regulation is that unsophisticated users demonstrably don't have the knowledge and experience to take care of those risks, so we push them to the payment networks to handle. And that's why I'm focusing on the "why isn't there a retail platform suitable for unsophisticated users?" - because if you can't do that, you've not got a solution to the hard problems in payments, just to the easy ones.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 6:32 UTC (Thu)
                               by raof (subscriber, #57409)
                              [[Link](https://lwn.net/Articles/1083105/)] (2 responses)
      
      
      
      
      And, to amplify that point, the “regulatory friction” preventing this hypothetical universal payment system from becoming mainstream is the technical solution to the fraud and security risks that a mainstream system requires. I am, in fact, reasonably convinced that it is approximately the only feasible technical solution — that any solution to these problems will look a lot like the current regulatory environment, perhaps with some actors shuffled around.

I've certainly never seen a serious attempt to solve these problems which would not rapidly devolve into something looking like the current arrangement (but generally worse).

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 8:46 UTC (Thu)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1083111/)] (1 responses)
      
      
      
      
      
> I've certainly never seen a serious attempt to solve these problems which would not rapidly devolve into something looking like the current arrangement (but generally worse). 

The growing ecosystem of digital services using various kinds of decentralised, distributed Internet money would disagree with that.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 10:53 UTC (Thu)
                               by pizza (subscriber, #46)
                              [[Link](https://lwn.net/Articles/1083120/)] 
      
      
      
      
      
> > I've certainly never seen a serious attempt to solve these problems which would not rapidly devolve into something looking like the current arrangement (but generally worse).

> The growing ecosystem of digital services using various kinds of decentralised, distributed Internet money would disagree with that.

"that growing ecosystem of digital services" has _never _ seriously attempted to solve those problems.  Quite the opposite, in fact.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 12:04 UTC (Mon)
                               by kleptog (subscriber, #1183)
                              [[Link](https://lwn.net/Articles/1082509/)] (25 responses)
      
      
      
      
      
I wouldn't expect the unit of transaction to be a "page". What does that even mean for a single page app?

I would think some kind of credit token system, where a token is valid for a single or group of sites for a fixed period. So you would go to wikipedia and it would ask for a credit token. Your browser would negotiate and then authenticate with a payment broker and you would get a token that would be (e.g) 5c for one day access under some reasonable rate limit. Your browser couldn't just start accessing random sites because the credit token is for one site only. I'm sure people could come up with something.

But there would have to be something in it for me. Like, no more ads.

The problem is, this infra would cost money which has to be paid for somehow. To get a micro-payments system off the ground it would require many open-source projects and commercial projects to stick in their own time and money to implement it. The operational cost is not that high, but the initial cost to build it is huge. At least for the open-source projects, the internet would have to literally fall apart before there's enough will to make a micro-payments setup happen, some groups will oppose it out of principle. Just like there are reasonable use-cases for being able to monitor HTTPS traffic without killing security but it is opposed out of principle.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 12:08 UTC (Mon)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082511/)] (24 responses)
      
      
      
      
      It's worse than your last paragraph implies, because the operational costs are huge, too. You have to handle allegations of fraud, both genuine and malicious, as well as actual fraud.

And that adds up to a huge cost for someone - you can simply refuse to handle fraud, and make it the payer's issue, but then, as has happened with things like eGold, you fall apart because you're a haven for crooks. Or, you end up being a broker like PayPal - but again, if someone can do payments brokering cheaper than PayPal, why haven't they taken over PayPal's market?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 22:13 UTC (Mon)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082730/)] (12 responses)
      
      
      
      
      
OK, so someone hacks your account and steals 50 cents of your daily distributed tokens. Big deal. Or you're a site operator and you have to refund 5 cents for a page view.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 6:18 UTC (Tue)
                               by kleptog (subscriber, #1183)
                              [[Link](https://lwn.net/Articles/1082737/)] (10 responses)
      
      
      
      
      
> Or you're a site operator and you have to refund 5 cents for a page view.

I dont see what that would ever be necessary. If the website was accessed then there is a payment required. The fact the site got the token proves there was an request. Where the token came from is not relevant.

If someone hacks my account and then uses that money to buy lotto tickets, the seller of the tickets is never obligated to refund them. It's only between me and my bank.

Suppose each token is worth one cent and that buys you one day of access to one site. Either the scanner has 1000 distinct tokens which means it cost €10, or they use the same token but then they identify themselves as the same actor and so the same rate limit.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 8:44 UTC (Tue)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082745/)] (7 responses)
      
      
      
      
      
If someone hacks my account and then uses that money to buy lotto tickets, the seller of the tickets is never obligated to refund them. It's only between me and my bank.

In the jurisdictions I'm aware of, that's not true - if someone uses my bank card to purchase lotto tickets, then the seller of the tickets either has to show that they required a second factor for authentication (e.g. a PIN), or they get to refund the bank. And this also applies with stolen cash; if I can show that the cash you accepted was stolen from me (unusual that anyone can do this, mind), you get to make me whole (since you accepted stolen property), and the person you gave the lotto tickets to has a debt to you that they've got to repay.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 16:02 UTC (Tue)
                               by kleptog (subscriber, #1183)
                              [[Link](https://lwn.net/Articles/1082893/)] (6 responses)
      
      
      
      
      
> In the jurisdictions I'm aware of, that's not true - if someone uses my bank card to purchase lotto tickets, then the seller of the tickets either has to show that they required a second factor for authentication (e.g. a PIN), or they get to refund the bank.

At least here, it's the bank that is liable, and they have a contract with the merchant to shift the liability to them. You can't go after the merchant yourself. It's actually fairly evil that the CC company takes 3% but shifts the liabilities to the merchants, that's cartels for you.

But credit cards are one of the more cumbersome payment methods around. It's easier when the site shows a QR code, you scan it, and approve the payment, done.

> And this also applies with stolen cash; if I can show that the cash you accepted was stolen from me (unusual that anyone can do this, mind), you get to make me whole (since you accepted stolen property), and the person you gave the lotto tickets to has a debt to you that they've got to repay. 

You're going to have to give me a citation here, because I can't find any examples of this. It appears many countries special case cash so that if you do a cash transaction in good faith you're in the clear. If it wasn't so, people wouldn't accept cash and commerce would fall apart.

(At least for the US it appears to be a common-law principle. For NL it's Article 3:86 BW which protects all good faith transactions in general.)

I really can't imagine any situation where someone stealing money (or equivalent) from you could lead to you having a claim against a third-party.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 16:06 UTC (Tue)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082897/)] 
      
      
      
      
      You, as the recipient of the cash, are handling stolen goods (at least in the USA and UK). That requires you, as the handler of stolen goods, to return them to the original owner once you become aware that they're stolen, in order for the transaction to count as a "good faith" transaction.

In practice, this is extremely hard to prove - it's not enough that I show that person A stole cash from me, and that they spent cash with you, but I also have to show that person A spent the cash they stole from me with you. But, in that circumstance, where you have the cash that was stolen from me, you're on the hook to return it to me, and you get a claim against the thief.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 19:48 UTC (Tue)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1082902/)] (4 responses)
      
      
      
      
      
> You're going to have to give me a citation here, because I can't find any examples of this. It appears many countries special case cash so that if you do a cash transaction in good faith you're in the clear. If it wasn't so, people wouldn't accept cash and commerce would fall apart.

As far as I'm aware the only way the UK "special case"s cash is as "legal tender". That means, if I owe you money and I offer you legal tender, the OFFER is sufficient to wipe the debt. In law, you have to either accept the cash, or write off the debt.

The only reason cash is "special" is that - as farnz points out - it's incredibly difficult to prove it's stolen. Unless of course it's never officially entered circulation and there's a record of the serial numbers, or it's plastered all over with the ATM ink that explodes everywhere if there's an attempt to steal / break into the ATM.

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    
    
      

### Cash payments are special 

      
      

 Posted Jul 15, 2026 21:44 UTC (Wed)
                               by kleptog (subscriber, #1183)
                              [[Link](https://lwn.net/Articles/1083093/)] (3 responses)
      
      
      
      
      
Which is why I asked for references, because all the ones I could find specifically say they cash is special. See for example [1] which specifically notes the situation was settled for banknotes in the UK in an important case in 1758 which I'm too lazy to look up.

In particular:

> When the identifiability of an asset falls toward zero, the owner’s incentive to search for it after a theft falls toward zero, the buyer’s incentive to investigate title falls toward zero, and the value of any title rule as a deterrent to theft falls toward zero. At that limit, the efficient legal rule is not a better-calibrated allocation between owner and purchaser. It is the abolition of the contest: the recipient in good faith and for value takes a fresh title good against the whole world, and the transaction is final.

If the hypothetical tokens for payment for web access are effectively anonymous and fungible, then every transaction is by definition in good faith and final.

See also the "Money has no earmark" rule.

[1] [https://singulargrit.substack.com/p/the-asset-the-law-gav...](https://singulargrit.substack.com/p/the-asset-the-law-gave-up-on)

      
          
            
            
            
          
        
     

     
    
    
      

### Cash payments are special 

      
      

 Posted Jul 16, 2026 8:42 UTC (Thu)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1083110/)] 
      
      
      
      
      
> If the hypothetical tokens for payment for web access are effectively anonymous and fungible, then every transaction is by definition in good faith and final.

Just to thread that in with another sub-thread here (which I know Jon has indicated that it should be left to peter out) - this is why Monero (in addition to the much lower transaction fees) is better for online payments to something like Bitcoin. Monero's ledger is not transparent, and hence Monero is fungible - not so for Bitcoin. 

      
          
            
            
            
          
        
     

     
    

    
      

### Cash payments are special 

      
      

 Posted Jul 16, 2026 9:28 UTC (Thu)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1083114/)] (1 responses)
      
      
      
      
      I followed that link, and looked up the case law it references; the key to it is that there are two separate rules around the return of stolen goods:

- Compensation for loss; someone stole a car from me, you took it in, failed to make adequate checks for whether it was stolen, and parted it out. I now have a claim against you for the value of the stolen car. The case law the site you reference references says that a good faith cash transaction definitionally cannot fall under this rule - not checking at all qualifies as "adequate checks" for cash, since otherwise it would be impossible for a cash economy to function.

- Return of actual stolen property. This is impossible for coins (since any suitable identifying marks would make it not a coin), but is possible, if improbable, for bank notes; if the victim of theft can show that they scrupulously and accurately record the serial numbers of all bank notes of that value that they receive and lose (both spent and stolen), and you have a stolen note in your possession, then this is enough to establish that you must either return the stolen bank note or something of equal value.

Case law only deals with the first of those situations; the second is as-yet untested in court, but based on similar cases with postage stamp collections, it's plausible that the courts would rule that because I'd shown that you had the specific cash stolen from me, you have to return it to me.

      
          
            
            
            
          
        
     

     
    
    
      

### Cash payments are special 

      
      

 Posted Jul 16, 2026 14:24 UTC (Thu)
                               by kleptog (subscriber, #1183)
                              [[Link](https://lwn.net/Articles/1083257/)] 
      
      
      
      
      
> Return of actual stolen property. This is impossible for coins (since any suitable identifying marks would make it not a coin), but is possible, if improbable, for bank notes; if the victim of theft can show that they scrupulously and accurately record the serial numbers of all bank notes of that value that they receive and lose (both spent and stolen), and you have a stolen note in your possession, then this is enough to establish that you must either return the stolen bank note or something of equal value. 

Nope. That was the whole point of the Miller vs Race 1758 case. At the time cash notes were a sort of "bearer cheques" and so easily identifiable: they had a bank name and a person's signature on it. The judge ruled that, even though the bank note was easily identifiable, it had currency and as far as the law was concerned not identifiable (no earmark).

It has no Wikipedia article, but the equivalent case in Scotland is here: [https://en.wikipedia.org/wiki/Crawfurd_v_The_Royal_Bank](https://en.wikipedia.org/wiki/Crawfurd_v_The_Royal_Bank)

> In a unanimous decision, the judges decided "that money is not subject to any vitium reale; and that it cannot be vindicated from the bona fide possessor, however clear the proof [of] the theft may be";

      
          
            
            
            
          
        
     

     
    

    
      

### Who is on the hook

      
      

 Posted Jul 14, 2026 13:08 UTC (Tue)
                               by corbet (editor, #1)
                              [[Link](https://lwn.net/Articles/1082754/)] (1 responses)
      
      
      
      
      If somebody buys an LWN subscription with a stolen credit-card number, we definitely end up having to refund it — and pay a chargeback fee as well.  Merchants only get the credit-card guarantee in settings where the card itself is physically present.  So I wouldn't assume that some future micropayment system would be more friendly to the selling side.

That said, solving the micropayment problem is a bit off-topic for LWN, unless, of course, you actually have the code to do it.  So perhaps it's time to let this subthread wind down.

      
          
            
            
            
          
        
     

     
    
    
      

### Who is on the hook

      
      

 Posted Jul 14, 2026 15:45 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082892/)] 
      
      
      
      
      
If you _want_ to experiment with micropayments, there's an x402 project that you can deploy right now: [https://www.linuxfoundation.org/press/linux-foundation-is...](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol)

And it's even on-topic, given that it's managed by our very own Linux Foundation!

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 8:40 UTC (Tue)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082744/)] 
      
      
      
      
      For starters, it's not guaranteed to be 50¢; if I put in enough money to cover my likely use once a year (say when I get my tax return, if I'm US-based), it's potentially a lot more when you're looking at 0.02¢ for a page view.

And it's not just a 5¢ refund - it's the cost of determining if I'm legitimate (since if you refund upon request, all the people you want to block will automate demanding a refund), too, plus the cost of handling me if you decide my refund request is not legitimate, but I pursue you further.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 23:25 UTC (Mon)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082731/)] (10 responses)
      
      
      
      
      
If you're interested in this space, check out the Etherium ecosystem, its compute "juice", and various slashing strategies. You don't have to be some kind of "crypto bro" to appreciate the hardness of the problems you get when you try to simultaneously have 1) accountability, and 2) anonymity.

In the present discussion, we can model web fetches as "spends" of some token (whether it's monetary or not!). Accessing a web page? That's a spend. How do you prevent people just copying access credentials to 1,000 machines and spending them in parallel? That's the double-spend problem, which crypto people have given a ton of thought. How do you maintain rate limits tied to an actor? This problem is isomorphic to wallet management. How do you give humans some reasonable number of accesses per day without enabling crawlers to simulate 10,000 "humans" per box?

The solution is going to come down to some zero-knowledge identity attestation scheme. You just can't have regular people competing on an open market with big scrapers for access tokens, and the only way you can distinguish regular people (so they get free or cheap access tokens) and bots (who should pay market rate) is to remotely attest a unique human identity in such a way as to prevent creating infinity "humans" out of thin air but also reveal nothing about which human is doing want. Devilishly hard problem.

There *are* points in mechanism-design space where all this stuff works out, but it's *absolutely* not trivial, especially if you want to maintain privacy. All the people in this thread saying we should "just" rate-limit humans or machines or that we should "just" bootstrap a micropayments ecosystem are barely scratching the surface of how hard this problem really is. It's not so much even the cryptography (tons of recent progress here) but the social bootstrapping stuff.

What's worse is that our social structures aren't set up to incentivize solving the problem. No VC is going to get 1,000x returns on this stuff, academia and the state get distracted for various reasons, and on and on in ways I don't want to get into. It's a nasty chicken-and-egg problem that's important to solve.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 8:01 UTC (Tue)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1082742/)] (9 responses)
      
      
      
      
      
Quite apart from the social and finance technical side there is also the issue that however you prefer to solve this problem you have just turned a simple stateless cacheable request into something that probably needs at least one database write or lookup or both and so it will both require a lot more resources to serve and be slower.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 15:48 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082894/)] (8 responses)
      
      
      
      
      
This is not necessary, actually. You can do it statelessly via JWTs. Essentially, you just need to verify the asymmetric signature.

And given that all traffic now is served over encrypted HTTPS, we already need to do that for each request. In theory, this can even be folded into client TLS certificates.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 19:29 UTC (Tue)
                               by NYKevin (subscriber, #129325)
                              [[Link](https://lwn.net/Articles/1082910/)] (6 responses)
      
      
      
      
      
How can you prevent double spending if the recipient does nothing with the JWT after validating it?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 22:05 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082929/)] (4 responses)
      
      
      
      
      
A typical JWT access token expires within minutes. 10-15 minute expiration is very common.

A website would need to:

1. Validate that the token signature comes from a correct CA, and that the site is the correct audience for the token.
2. Check that it's not expired, with a reasonable clock skew window.
3. Rate-limit based on the token ID so that the bad actor can't DDoS your site during the token validity window.

This can all be done statelessly without any database. All the state can live in the token issuer that will also do all the billing-related stuff.

JWT as it exists now is not very suitable for this because of the privacy concerns. But there are multiple possible ways to fix them (and no, they don't require blockchain or ZKPs).

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 15:02 UTC (Wed)
                               by NYKevin (subscriber, #129325)
                              [[Link](https://lwn.net/Articles/1083075/)] (3 responses)
      
      
      
      
      
Step 3 is not stateless. You need to maintain a token bucket and update it with each request.

The state is ephemeral, which does make the problem easier. But it is very much "not free."

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 17:23 UTC (Wed)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1083082/)] (2 responses)
      
      
      
      
      
Sure, but it doesn't need to be a global state. And realistically, it's not a problem to store a couple of megabytes of data. Assuming that each client ID is 128 bits, that's around 64k clients. If each one of them provides you with even 10 cents, that's a good problem to have!

Moreover, it won't even require a lot of local storage if you use random-based sampling. This was my interview question many years ago :) 

The idea is to select a random number from 0 to N and if it's equal to N, you start tracking the requests for this user. Then a standard token bucket is sufficient. You can dynamically vary N depending on the overall load.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 8:13 UTC (Thu)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1083108/)] (1 responses)
      
      
      
      
      
In what weird kind of dream world do you live in where people are willing or even able to pay 10 cents per request or even per day for every website they visit?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 17:28 UTC (Thu)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1083267/)] 
      
      
      
      
      
10 cents is the upper limit per day for all the websites that you visit. The idea is that rate-limiting would only affect a visitor if they are already hammering the site with unreasonable number of requests.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 22:08 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082930/)] 
      
      
      
      
      
Sorry, misunderstood your question. The entity that mints the token should also do the crediting. The act of creating the token itself is the billable action. If you don't use the minted token, then too bad for you.

      
          
            
            
            
          
        
     

     
    

    
      

### Proof of humanity or payment

      
      

 Posted Jul 15, 2026 10:10 UTC (Wed)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1082936/)] 
      
      
      
      
      This also feels like it combines nicely with quotemstr's proposal that you have some form of "proof of humanity" to bypass rate limiting. If I can prove my humanity to the token issuer (TLS client cert, JWT, whatever), I get a reduced rate, while someone who can't (or doesn't want to) can pay full rate for access tokens.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 22:00 UTC (Mon)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082727/)] (18 responses)
      
      
      
      
      
There probably needs to be a daily limit. E.g. a million pages, that's more than a human can reasonably do, yet not really an issue for any real CDN/server.

I'd love for Scroll to be resurrected. There are also cryptocrap versions, but they're DoA as all cryptocrap is.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 22:04 UTC (Mon)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082729/)] (1 responses)
      
      
      
      
      
> There probably needs to be a daily limit.

How do you determine the principal? A daily limit *for who*?

>  E.g. a million pages

A million pager per, what, person? How is individual personhood established? What prevents a scraping outfit identifying as a small town's worth of people? The whole concept of rate-limiting per-person per-day sounds easy at first but is fiendishly hard if you think about it and care about privacy.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 15:35 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082890/)] 
      
      
      
      
      
> How do you determine the principal? A daily limit *for who*?

A subscriber. Feel free to create multiple ones, you just have to pay (for example) $10 a month for each one.

> What prevents a scraping outfit identifying as a small town's worth of people? 

Nothing. And that's the goal. No Kafkaesque attestations, no complicated surveillance state. Each time you request a page, the page's operator gets credited (with obvious sanity checks).

Want to scrape my Git by following all the links recursively? Be my guest. You'll just have to pay for it.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 8:06 UTC (Tue)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1082743/)] (15 responses)
      
      
      
      
      
A million requests is a lot for most servers. Certainly more than even most unreasonable individual scrapers do on most pages in a day and, depending on which rarely called (and thus uncached) pages they dig up to request, possibly more than a server can handle in total in a day.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 13:11 UTC (Tue)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082755/)] (9 responses)
      
      
      
      
      
Your comment made me curious about how the numbers being thrown around compare to LWN's average, sustainable traffic. So I went and poked at the logs, and found that LWN.net served 1,380,129 page requests yesterday, which was not a particularly heavy day. When there's an active scraper attack that number can be significantly higher.

Even so, only 722,949 of the requests were for actual pages that we have; 657,180 were either 404s or redirections, mostly from HTTP to HTTPS.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 15:31 UTC (Tue)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082889/)] (8 responses)
      
      
      
      
      
Why not get lwn on the HSTS preload list? And set up a HTTPS DNS record while you're at it?

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 16:37 UTC (Tue)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082899/)] (7 responses)
      
      
      
      
      
Most of the traffic still requesting HTTP is from bots or other automated processes that are unlikely to respect the HSTS preload list. Note that we do serve a HSTS header with a duration of one year, so in theory any client that loads a single page from LWN.net should not try HTTP again for at least a year. In practice, we see plenty of clients that do, in fact, ignore the permanent redirects and HSTS header and continue to request the HTTP version of the site first.

As for the HTTPS DNS record — I didn't know that kind of record existed, so I've learned something new today. It probably doesn't make sense to set it up without getting our DNSSEC situation sorted out, but it's a good idea.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 16:47 UTC (Tue)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082900/)] 
      
      
      
      
      
FWIW, given how many scrapers are headless Chromium, I'd be a bit more optimistic about the preload list.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 20:21 UTC (Tue)
                               by zdzichu (subscriber, #17118)
                              [[Link](https://lwn.net/Articles/1082913/)] (4 responses)
      
      
      
      
      
Maybe disable plain HTTP? Browsers default to HTTPS connections if I'm not mistaken. Port 80 is legacy.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 20:43 UTC (Tue)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082916/)] (3 responses)
      
      
      
      
      
We've considered it. We only started redirecting HTTP to HTTP around ... two years ago, I think? So we wanted to give it time for people to update their bookmarks, feed readers, and so on. It might be worth taking another look at whether it's really worth continuing to listen on port 80, though.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 12:49 UTC (Wed)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082941/)] 
      
      
      
      
      
Correction: we've redirected HTTP to HTTPS for many years, but changed how that was accomplished in our backend relatively recently, and it is that change that I was remembering.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 13:12 UTC (Wed)
                               by Wol (subscriber, #4433)
                              [[Link](https://lwn.net/Articles/1082917/)] (1 responses)
      
      
      
      
      
Or just serve a page that says "waiting 10 secs to redirect to https ..."

That'll slow down any crawler that waits for previous requests to complete, and will make real humans update their links :-) without inconveniencing said humans *that* much.

Cheers,
Wol

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 13:16 UTC (Wed)
                               by daroc (editor, #160859)
                              [[Link](https://lwn.net/Articles/1082950/)] 
      
      
      
      
      
Well, there are two problems with that:

1. Scrapers often don't complete requests on real time; they receive the redirection, and the redirected URL goes on a queue that gets processed minutes or hours later, often by a different IP address.

2. I don't think there's an elegant way to redirect after a timeout without using JavaScript (which we try to keep to a minimum) or tying up server resources with an open connection.

Honestly, clients hitting port 80 isn't a huge problem. Those redirects are relatively cheap to serve compared to serving a page with dynamic content on it. It's annoying, clutters the logs, and they should really take the hint, but it isn't the end of the world.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 5:25 UTC (Wed)
                               by PhilippWendler (subscriber, #126612)
                              [[Link](https://lwn.net/Articles/1082932/)] 
      
      
      
      
      
AFAIU the HTTPS DNS record is useful for telling browser to use HTTPS (and potentially HTTP2), independently of DNSSEC. It is not like TLSA or SSHFP, which contain certificates and need to be authenticated in order to make sense.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 14, 2026 15:42 UTC (Tue)
                               by Cyberax (✭ supporter ✭, #52523)
                              [[Link](https://lwn.net/Articles/1082891/)] (4 responses)
      
      
      
      
      
A million requests is just about 12 requests per second over the course of the day. That's just not a lot even for dynamic content. And what I meant is the total _daily_ limit for a user for all the sites. 

Suppose that we have a Scroll-like service for $10 a month, so around 30 cents per day spread proportionally over visited sites. My poor Forgejo was able to serve around 250 requests per second so that 1 million requests would have been exhausted in little more than 1 hour, getting me 30 cents. During that time, my server would consume about 0.6kWh of electricity rendering all that data. So I would get a small profit given my low local prices.

Anyway, the numbers can be tweaked in either direction, with different pricing tiers.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 12:14 UTC (Wed)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1082937/)] (3 responses)
      
      
      
      
      
It is extremely rare that you get the luxury of having the requests a day equally distributed across every second of the day.

PHP on a cloud server likely has a single digit or small double digit number of workers and for something not cached it can easily take a second to generate a page.

Sure, if you only count compiled languages your 250 requests/s might be realistic but the reality is that there are plenty of PHP, NodeJs, Python, Ruby or even Perl based websites that will never reach that and aren't deployed on huge servers because their normal traffic is nowhere near that high.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 16:51 UTC (Wed)
                               by NYKevin (subscriber, #129325)
                              [[Link](https://lwn.net/Articles/1083078/)] (2 responses)
      
      
      
      
      
> It is extremely rare that you get the luxury of having the requests a day equally distributed across every second of the day.

Just to clarify for folks who haven't done this before: If you graph queries-per-second against time, for the vast majority of web-related services, you get a sinusoid with a period of 1 day, a fairly significant amplitude (relative to the average), and in most cases, the graph looks completely different on the weekend. You must provision for the daily peak and not the average, or else you will fall over. Load balancing, caching, and other middlebox technologies can make the graph a bit flatter (at the origin server), but it will still have a daily peak and you will still need to deal with it.

This is not only true for the origin server, but also for most if not all of its backends (and their backends recursively). You really only get flat QPS from batch jobs running continuously, and even those are often spiky in practice.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 15, 2026 16:57 UTC (Wed)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1083081/)] (1 responses)
      
      
      
      
      
> You must provision for the daily peak and not the average,

Well, for January 3rd (boxing day / St. Stephen's day sales) / FA Cup final / $INSERT_APPROPRIATE_ANNUAL_EVENT_HERE.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 16, 2026 8:16 UTC (Thu)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1083109/)] 
      
      
      
      
      
With most sites you can probably get away with some flakyness on the busiest day of the year (unless that is specifically what the site is designed to serve of course if it is an event related website) but you certainly won't get away with it on every daily peak.

      
          
            
            
            
          
        
     

     
    

    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 15, 2026 13:54 UTC (Wed)
                               by gmatht (subscriber, #58961)
                              [[Link](https://lwn.net/Articles/1082945/)] (11 responses)
      
      
      
      
      
To serve an HTTPS page we already have to negotiate mutually trust CertAuthorities. It does not seem to be any harder to negotiate mutually trusted charities. Like Micropayments, Proof-of-Donation isn't just digging holes to fill them up again*. As to 1-3:

1. A bad-actor could transfer microcash that already been earmarked for charity to one of the wallet's owner's trusted charities, but it is not clear what this would achieve other than annoying people. A bad-actor who just wanted to be annoying could be much more annoying than that.
2. Like Proof-of-Work, you don't get your microcash/microwatts back. Just hope that "donating" a few bucks of your microcash was the worst the bad-actor did. Charities tend to be heavily regulated so it seems unlikely a "trusted charity" would be the bad actor, and they wouldn't be "trusted" for very long in any case.
3. N/A

In case people can't negotiate trusted authorities, can't be bothered setting up a microcash wallet (or it has been drained for some reason), one could still fall back on Proof-of-Work.

* It should be noted that in principle Proof-of-Work could involve asking users to solve problems that you are genuinely interested in the answer to (E.g. protein folding perhaps). However solving an interesting problem is probably too much work just to download a webpage, and might be better used as a way to bootstrap some sort of microdonation wallet rather than something you do for each random webhost you access.

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 15, 2026 15:28 UTC (Wed)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1083074/)] (10 responses)
      
      
      
      
      The challenge is that most people don't negotiate certificate authorities; your browser author picks some for you, and you just expect HTTPS to work.

Asking people to set up a wallet is already a big deal; if that wallet's not one they're using anyway (which micropayments assume they will have), it's likely that they'll refuse. And for any "anti-scraper" measures to make a big difference, they need to become a social norm that everyone engages in, otherwise people will simply stop going to the sites that have anti-scraper measures, in favour of ones that don't.

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 16, 2026 8:11 UTC (Thu)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1083107/)] 
      
      
      
      
      
It is not even just non-technical people who wouldn't. I know I would boycott sites like that out of principle unless they are extremely crucial (think government or health insurance services I can't avoid crucial) to my life.

      
          
            
            
            
          
        
     

     
    

    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 16, 2026 9:16 UTC (Thu)
                               by gmatht (subscriber, #58961)
                              [[Link](https://lwn.net/Articles/1083113/)] (8 responses)
      
      
      
      
      
Well, there is no reason the browser couldn't pick a default set of charities either.

Manually Setting up a wallet is a pain. It might be easier to set up some sort of alt-coin mining wallet or some way of "spending" Folding@Home certificates etc (assuming they are fraud proof or can be made so, e.g. only giving certs for work than improves on an existing folding.) etc. This would seem nicer than being made to wait for several seconds of Proof-of-Work every other time I click on a webpage. (Hmm, in the meanwhile, would getting a Static IP help with that I wonder? CGNAT IP are probably treated like trash by webmins.)

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 16, 2026 9:26 UTC (Thu)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1083116/)] (7 responses)
      
      
      
      
      How, exactly, do you expect the browser to force me to donate to a set of charities, given that there are multiple open source options where someone can remove the "forced donation" code and re-release the browser without it?

With CAs, it's trivial - the browser picks trusted CAs, and I get the benefits of trusted CAs automatically, simply because the browser chose them. In a "proof of donation" situation, however, the thing I need is not a charity, but a donation - and unless the browser makes the donation on my behalf (from what fund of money, for example, and how does it ensure that it only donates for unique users), it doesn't work.

The hard part of all of the possible solutions is getting it past the apathetic and opposed so that it becomes part of the social norms. The easy part is the technical bits of showing that you've done something (a microtransaction, proof of work, mining a cryptocurrency, whatever).

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 17, 2026 8:42 UTC (Fri)
                               by gmatht (subscriber, #58961)
                              [[Link](https://lwn.net/Articles/1083294/)] (6 responses)
      
      
      
      
      
'How, exactly, do you expect the browser to force me to donate to a set of charities, given that there are multiple open source options where someone can remove the "forced donation" code and re-release the browser without it?' 

You absolutely could do that, assuming the browser even tried to force you. Then the web would fallback to work the way it does now, with many important websites regularly freezing up for a few seconds while forcing your browser to do Proof-of-Work, (or other nonsense like forcing you to do a Captcha just to view a single public facing webpage). Websites could instead deny you service entirely, but I imagine that would be rare.  The webmaster might find Proof-of-Work wasteful, but if their goal is to rate-limit requests it may not make much difference to them whether they are limited by Proof-of-Donation, Proof-of-Work or Captcha. 

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 17, 2026 8:45 UTC (Fri)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1083295/)] (5 responses)
      
      
      
      
      But why would I bother doing proof of donation/work/payment if websites don't accept it yet? And why would websites move to proof of donation/work/payment if browsers don't do it yet?

There's a deep chicken-and-egg problem to solve here first, which is that when no user does the new thing, there's no incentive for websites to move away from what they do today; but when no website does the new thing, there's no incentive for users to put time and effort into a thing that does nothing for them. How do you break that cycle?

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 17, 2026 9:10 UTC (Fri)
                               by gmatht (subscriber, #58961)
                              [[Link](https://lwn.net/Articles/1083296/)] (4 responses)
      
      
      
      
      
Well, the chicken and egg problem is common to every new feature, and many browsers support versions of HTML past 1.0.

The only real challenge is how do we make setting up a wallet trivially easy (as in a user shouldn't even have to know it is there; for proof-of-donation the webmaster doesn't even need a wallet). I guess the first stage would be to just have sort of proof-of-work coin so that you could save up proof-of-work so that the next dozen or so webpages you load start instantly. I guess most coin miners would work for this, though they are a little heavyweight (and they tend to be flagged by virus scanners). Blockchain probably isn't really necessary anyway. Getting paid for proof-of-useful-work (protein folding, random useful medium size NP problems, cold-storage), or getting a couple of bucks of Proof-of-Donation coin off your ISP are possible options.

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 17, 2026 9:47 UTC (Fri)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1083299/)] (2 responses)
      
      
      
      
      
It is not common to any new feature, just to features you need to force on the user for the user to be interested in them at all.

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 17, 2026 10:20 UTC (Fri)
                               by gmatht (subscriber, #58961)
                              [[Link](https://lwn.net/Articles/1083302/)] (1 responses)
      
      
      
      
      
I don't see anyone suggesting that we force anyone to use Proof-of-Donation. Are you responding to me, or viewpoint you have seen elsewhere?

      
          
            
            
            
          
        
     

     
    
    
      

### Proof-of-Donation a compromise between Proof-of-Work and Micro-payments

      
      

 Posted Jul 20, 2026 7:22 UTC (Mon)
                               by taladar (subscriber, #68407)
                              [[Link](https://lwn.net/Articles/1083550/)] 
      
      
      
      
      
I am talking about the users of your particular website, you won't exactly make your users jump through hoops to adopt a system to give you a micropayment for every request unless you refuse requests without that proof attached, i.e. force your users to use it.

      
          
            
            
            
          
        
     

     
    

    
      

### The chicken-and-egg problem for any solution

      
      

 Posted Jul 17, 2026 10:34 UTC (Fri)
                               by farnz (subscriber, #17727)
                              [[Link](https://lwn.net/Articles/1083297/)] 
      
      
      
      
      The chicken-and-egg is the significant problem here, though. Everything else is a solved technical problem, and you can copy pre-existing solutions to build your system.

But, as the developers of CLNP found, just because you have a technical solution to a problem doesn't mean that you can get it adopted, even with significant support. In the case of new versions of HTML, adoption happened because the browsers could unilaterally adopt new features without user involvement; once browsers had adopted the feature, websites could use it, and once websites used it, users could move to new browsers without significant cost to get the features they needed to see the latest and greatest websites.

Even then, though, the existence of sites like [Can I Use](https://caniuse.com/ciu/index) points to the fact that the chicken-and-egg problem remains - some features [are barely supported at all](https://caniuse.com/ambient-light) even if they'd be useful for some sites, while [others are widely available and can be relied upon](https://caniuse.com/x-doc-messaging).

It's worth noting, in that context, that there's basically been two routes to features becoming widely available in the Can I Use tables of recent years:

- Apple or Google implement it, force it on all Safari or Chrome (including Android WebView) users as a compulsory feature, and then sites start using it because there's enough users to make it worthwhile. However, at this point, I don't see that as plausible; Google and Apple are both big enough to just ride out scrapers, and therefore won't speculatively implement it.

- Websites use it, with a fallback to a lesser option, and browsers implement it because their developers really like the idea of avoiding the fallback or because users clamour for the improvements they get by avoiding the fallback.

      
          
            
            
            
          
        
     

     
    

    
      

### Micropayments (was Re: UI automation is necessary for accessibility)

      
      

 Posted Jul 13, 2026 23:35 UTC (Mon)
                               by dskoll (subscriber, #1630)
                              [[Link](https://lwn.net/Articles/1082732/)] (2 responses)
      
      
      
      
      

I seem to recall, oh, about 2.5 decades ago, that micropayments were being touted as the solution to spam, so much so that they made the [FUSSP](https://www.rhyolite.com/anti-spam/you-might-be.html#e-postage) list.

I suspect micropayments for viewing web pages will be about as successful as micropayments for sending email.

      
          
            
            
            
          
        
     

     
    
    
      

### Micropayments (was Re: UI automation is necessary for accessibility)

      
      

 Posted Jul 14, 2026 8:00 UTC (Tue)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082741/)] (1 responses)
      
      
      
      
      
One of the ideas to solve spam was Adam Back's "hashcash". So... yeah.. that just disappeared and went nowhere, and has no relevance at all today.

</sarcasm>

      
          
            
            
            
          
        
     

     
    
    
      

### Micropayments (was Re: UI automation is necessary for accessibility)

      
      

 Posted Jul 14, 2026 13:22 UTC (Tue)
                               by dskoll (subscriber, #1630)
                              [[Link](https://lwn.net/Articles/1082837/)] 
      
      
      
      
      

A proof-of-work system has nothing to do with micropayments that involve actual cash.

      
          
            
            
            
          
        
     

     
    

    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 3:14 UTC (Mon)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1082492/)] (3 responses)
      
      
      
      
      
Not complicating, allowlisting.  You would need to create an explicit list of permitted devices and OSs for this to work.  It's not feasible.

What you can do is impose a per-person or per-device rate limit.

      
          
            
            
            
          
        
     

     
    
    
      

### UI automation is necessary for accessibility

      
      

 Posted Jul 13, 2026 4:36 UTC (Mon)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082497/)] (2 responses)
      
      
      
      
      
No, complicating. You don't need end-to-end wihtelisting. You don't need perfection: you just need to make working around the attestations more annoying than paying a human in some third-world country to do the same thing.

An attested, channel-bound input-delivery path exist in the context of an otherwise open OS. All I have to do as a client is present recent proof of human interaction performed locally. If that interaction comes from voice input and I send keystrokes, I can nevertheless staple the voice-produced proof of recent human interaction. Tons of ways to cryptographically frustrate replay attacks, proxying, and so on.

You've asserted a few times now that you can rate limit people or rate limit devices. You can do these things. There are other things you can do too, and if you insist that only your two options exist, you're going to lock us into a low-openness, low-privacy internet in which actions are linkable, because that's how you enforce rate limits.

Sure, you could create some kind of zcash-like interaction-token system to prevent double-"spending" network-request tokens without linking individual "transactions", but who's going to bootstrap it the system? Who gets to decide how many unlinkable request tokens each person gets per hour or day? How are they distributed? 

Do I just buy interaction tokens at market price? How do I, a person, out-compete some scraping outfit with infinity venture capital? If I get some subsidy, what prevents my selling my tokens to scrapers?

There are answers to all these questions. It's a fascinating and emerging field. But now you're talking about a whole ecosystem someone has to bootstrap and maintain. So, in practice, once CAPTCHAs fail (as they have), and once PoW fails (as it has), then what's left is a "papers, please" internet of long-term linkable identities. I do not want this internet.

I'd rather use a damn mouse someone certified about not lying about rough input timestamps.

      
          
            
            
            
          
        
     

     
    
    
      

### Unlinkable per-person per-site rate limits

      
      

 Posted Jul 13, 2026 19:26 UTC (Mon)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1082716/)] (1 responses)
      
      
      
      
      
Rate limits can be per-person per-site, without different sites being able to detect the same person is using both, and without exposing a person’s legal identity.  Zero-knowledge proofs make this possible.

      
          
            
            
            
          
        
     

     
    
    
      

### Unlinkable per-person per-site rate limits

      
      

 Posted Jul 13, 2026 19:36 UTC (Mon)
                               by quotemstr (subscriber, #45331)
                              [[Link](https://lwn.net/Articles/1082718/)] 
      
      
      
      
      
Linkable *per site* identities are also a problem, and you haven't addressed Sybil issues at all. Come on, this whole thread has been you asserting stuff without actually constructing an argument.

      
          
            
            
            
          
        
     

     
    

    
      

### IP blocks should be neither authentication nor authorization

      
      

 Posted Jul 11, 2026 11:02 UTC (Sat)
                               by muase (subscriber, #178466)
                              [[Link](https://lwn.net/Articles/1082394/)] 
      
      
      
      
      
> Privacy-preserving protocols like this have become practical just recently, over the past few years. It's a shame we haven't yet begun to explore their potential. The alternative is something like the Cloudflare Monetization Gateway

I think a maybe better interesting alternative – funnily enough also from Cloudflare – is CAP: [https://developers.cloudflare.com/fundamentals/reference/...](https://developers.cloudflare.com/fundamentals/reference/cryptographic-personhood/)

CAP uses WebAuthn to basically do two things: see if your device has an attested WebAuthn hardware authenticator it can trust, and then it ask the trusted hardware to perform biometric user authentication. 

And this is kinda clever, because this means it simply uses WebAuthn as an open standard, and everyone can implement it independently of Cloudflare. The only downside is that with this approach the same user can be re-identified; I think an extension to WebAuthn could help with that. 

      
          
            
            
            
          
        
     

     
    

    
      

### IP blocks should be neither authentication nor authorization

      
      

 Posted Jul 11, 2026 14:15 UTC (Sat)
                               by fraetor (subscriber, #161147)
                              [[Link](https://lwn.net/Articles/1082404/)] 
      
      
      
      
      
Mozilla has been exploring this recently with anonymous credentials to allow different services to assert identity via zero-knowledge proofs.

It essentially acts as a web-wide rate limit, under the theory that bot traffic is problematic not because it is automated, but rather because a single bot operator can produce way more traffic than an individual person would.

High level post on the goals:
[https://blog.mozilla.org/en/firefox/privacy-security/keep...](https://blog.mozilla.org/en/firefox/privacy-security/keeping-the-web-open-and-private-in-the-bot-era/)

And the Hacks post that goes into the technical details:
[https://hacks.mozilla.org/2026/06/pact-anonymous-credenti...](https://hacks.mozilla.org/2026/06/pact-anonymous-credentials-for-the-web/)

      
          
            
            
            
          
        
     

     
    

    
      

### IP blocks should be neither authentication nor authorization

      
      

 Posted Jul 13, 2026 10:43 UTC (Mon)
                               by paulj (subscriber, #341)
                              [[Link](https://lwn.net/Articles/1082504/)] 
      
      
      
      
      
Indeed. This is fundamentally a spam / sybil attack problem. And ultimately it requires a web architecture with some protections against this. Proof of interactive humanity may not always be enough. It may stop higher-rate crawlers, but it will not allow one to stop human-bot-farms (if one wished).  In some cases, someone may wish to deny lower-rate human-bot-farms too; in other cases it might not matter. 

We need some kind of privacy architecture for the Internet that allows for different levels commitment by the resource accessor to the resource owner and hosters. E.g., a commitment of humanness; a commitment of a pseudonymous, longer-term, more stable identity with some reputation attached; a commitment of financial resources (i.e., some micro-payment that is paid, or some bond that is committed towards good behaviour on the network); a commitment of real identity, verified by some reputable body (either provided up-front, or revealable by the reputable body if some bad behaviour is reported).

And absolutely, we need to build this on relatively distributed and private protocols. For if we do not, we will have that de facto Cloudflare gatekeeper you mention.

      
          
            
            
            
          
        
     

     
    

    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 10, 2026 22:34 UTC (Fri)
                               by koverstreet (subscriber, #4296)
                              [[Link](https://lwn.net/Articles/1082360/)] (10 responses)
      
      
      
      
      
I started seeing a ton of AI crawlers hammer all my git endpoints, and they're going right past the anubis checks; it seems a least some crawlers are using full web browsers that can do the proof of work.

Ouch.

So I'm back to a script that I run regularly that just scrapes the hammering IPs from the nginx log and iptables blocks them...

      
          
            
            
            
          
        
     

     
    
    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 11, 2026 0:21 UTC (Sat)
                               by joey (guest, #328)
                              [[Link](https://lwn.net/Articles/1082367/)] (9 responses)
      
      
      
      
      
I'm coming to the conclusion that it doesn't make sense to have a whole public gitweb or cgit or similar on the web anymore. There are a few pages of that are valuable to provide to my users, like the most recent commit log and the current file tree, and a things like commits that I link to specifically from blog posts. But the ability to explore deeply through the whole git history is a marginal value, and the value proposition for that has overall gone negative. The interested user can make their own clone and use their own tools on it.

LWN's mailing list archives may have a similar value distribution.

      
          
            
            
            
          
        
     

     
    
    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 11, 2026 0:58 UTC (Sat)
                               by koverstreet (subscriber, #4296)
                              [[Link](https://lwn.net/Articles/1082369/)] (6 responses)
      
      
      
      
      
I use cgit pretty frequently, and my users are perusing it regularly too, so it's pretty painful here.

Realistically, the solution needs to be some kind of throttling baking into the webserver, and a more efficient cgit implementation with some caching would help a lot. I've hit quite a few perf issues with git, I'm hoping now that they're starting to use Rust in the core codebase that'll make performance work easier.

Definitely not excited by the prospect of yet more sysadmin work, though.

And. If web access to too many git repos gets shut down I have to imagine the AI companies would switch to just chain cloning repos with no caching. Everything they're doing is just really anti social.

      
          
            
            
            
          
        
     

     
    
    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 11, 2026 3:32 UTC (Sat)
                               by danielbaumann (subscriber, #38804)
                              [[Link](https://lwn.net/Articles/1082373/)] (5 responses)
      
      
      
      
      
I started to use basic auth with a "dummy" user and password that is written on the webpage. It's unexpected/inconvenient for non-regular/first-time/one-time-only human visitors, but it works for now.

      
          
            
            
            
          
        
     

     
    
    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 11, 2026 5:27 UTC (Sat)
                               by koverstreet (subscriber, #4296)
                              [[Link](https://lwn.net/Articles/1082381/)] 
      
      
      
      
      
Heh, the cat and mouse games are getting out of hand...

      
          
            
            
            
          
        
     

     
    

    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 11, 2026 14:02 UTC (Sat)
                               by dskoll (subscriber, #1630)
                              [[Link](https://lwn.net/Articles/1082399/)] (1 responses)
      
      
      
      
      

Yes, I do the same Basic Auth trick with the username and password disclosed on the front page and it seems to be working very well for now.  I check the user agent and if it's git, I don't require the authentication, so a  `git clone`  works without authentication.  At some point, I suspect the scrapers will catch on and we'll be one step further along the arms race. 🙁

      
          
            
            
            
          
        
     

     
    
    
      

### CGit accesses are indeed problematic

      
      

 Posted Jul 13, 2026 3:31 UTC (Mon)
                               by zaitseff (subscriber, #851)
                              [[Link](https://lwn.net/Articles/1082495/)] 
      
      
      
      
      
To add what some have already said: I also found that incessant accesses to my CGit repositories was causing significant load on my 14-year-old 1RU server, with well over 50,000 accesses per day, over and over again.

My first thought was to put in HTTP Basic Authentication, but that just made the bots try (and fail) more often: it got to the point where I was seeing up to half a million IP addresses trying to access the repos each and every day!  The bots' motto must be "must try harder"!

I ended up doing the following:

1. Returning a 410 Gone response to my CGit instance,
2. Moving the CGit frontend to another hostname and URL prefix (both previously unadvertised), and
3. Putting HTTP Basic Authentication in front of those new URLs.

Finally:

4. Git repos over HTTPS also need Basic auth, unless it comes from a recognisable Git client.

After three months, I've seen accesses on the old URLs go from 500,000 to a trickle of 300-500 per day.  I can live with that!

      
          
            
            
            
          
        
     

     
    

    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 12, 2026 11:59 UTC (Sun)
                               by alx.manpages (subscriber, #145117)
                              [[Link](https://lwn.net/Articles/1082438/)] 
      
      
      
      
      
Heh!  Nice trick!

I gave up with similar stuff, but maybe I should give this one a try.

Currently, I serve my cgit under a different server_name, so if the user passes the appropriate domain name in the header fields, they're allowed, but otherwise they can only see the basic static site.  I tell the secret domain name to users that I want to give access to, and they put it in their hosts file, with the same IP of my public DNS name (so they can update it with whatever the DNS says in the future).

      
          
            
            
            
          
        
     

     
    

    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 12, 2026 18:14 UTC (Sun)
                               by ecm (subscriber, #129897)
                              [[Link](https://lwn.net/Articles/1082453/)] 
      
      
      
      
      
We also did this between 2025 October and 2026 January for our hgweb, though we've switched to Anubis with some success since.

Blogged about it at [https://pushbx.org/ecm/dokuwiki/blog/pushbx/2026/0616_upd...](https://pushbx.org/ecm/dokuwiki/blog/pushbx/2026/0616_update_on_the_anti-scraping_measures_for_our_hgweb)

      
          
            
            
            
          
        
     

     
    

    
      

### Dumb transport is very efficient

      
      

 Posted Jul 11, 2026 4:04 UTC (Sat)
                               by DemiMarie (subscriber, #164188)
                              [[Link](https://lwn.net/Articles/1082375/)] 
      
      
      
      
      
The dumb transport just requires a static file server, which means it is vastly more efficient on the server side unless it (for some reason) requires far more bandwidth.

      
          
            
            
            
          
        
     

     
    

    
      

### Anubis doesn't seem to be working anymore here

      
      

 Posted Jul 12, 2026 9:08 UTC (Sun)
                               by danc (subscriber, #74798)
                              [[Link](https://lwn.net/Articles/1082432/)] 
      
      
      
      
      
A while ago I replaced my cgit installations with stagit. It generates a basic view of your git repositories as static HTML pages. You get a page for every commit with diffs, and a complete log of the master branch. Not much else. It's perfect for putting small personal projects online, and the cost to serve the static HTML is negligible.

[https://codemadness.org/stagit.html](https://codemadness.org/stagit.html)

There are quite a few forks of it floating around with extra features, like rendering Markdown READMEs and so forth.

      
          
            
            
            
          
        
     

     
    

    
      

### Have your cake and eat it too

      
      

 Posted Jul 11, 2026 3:31 UTC (Sat)
                               by marcH (subscriber, #57642)
                              [[Link](https://lwn.net/Articles/1082372/)] (3 responses)
      
      
      
      
      
> Google takes pains to point out that its Play Store will now check for NetNut-infected apps, but all of the major vendors are silent on the topic of why it is so easy to put apps with residential-proxy functionality into their app stores.

Amusingly, the interwebs were up in arms about the recent "Android Developer Verification" changes. In summary:

- it's too easy to publish random stuff on the app stores. Yet:
- it's increasingly difficult to publish random stuff on the app stores!

How about: security is extremely hard? Security as in: blocking and catching bad people while not bothering honest people (low security "friction").

Even harder on the wild, borderless internet. Amazing all this has been working at all. With hindsight, maybe this was all some kind of short-lived miracle... Lucky us who lived at that time and could experience it!

      
          
            
            
            
          
        
     

     
    
    
      

### Have your cake and eat it too

      
      

 Posted Jul 11, 2026 9:23 UTC (Sat)
                               by shalem (subscriber, #4062)
                              [[Link](https://lwn.net/Articles/1082391/)] 
      
      
      
      
      
The problem with "Android Developer Verification" is not Google enforcing this for the official Android Playstore, that is fine. The problem is Google abusing their Android monopoly to force "Android Developer Verification" to also apply to apps loaded through third party stores like fdroid.

Although this is a slippery slope I could live with Google using their gatekeeper capabilities to only allow third party app stores which have gone through some sort of registration process with Google to avoid creating a third party app store malware loophole.

Google should have no say over what goes into third part app stores, that should be up to the third party app-stores. This will likely require an unfortunately unavoidable added process for Google to revoke the "app store" capability from badly behaving add stores.

      
          
            
            
            
          
        
     

     
    

    
      

### Have your cake and eat it too

      
      

 Posted Jul 11, 2026 14:07 UTC (Sat)
                               by Zentaya (guest, #185040)
                              [[Link](https://lwn.net/Articles/1082379/)] (1 responses)
      
      
      
      
      
Unfortunately android developer verification is not going to help with netnut infested apps.

Malware infected apps are rampant in the play store even now. ADV will not help with that.

What it will do is prevent apps installed from f-droid and other sources, that are much less likely to contain malware anyway.

      
          
            
            
            
          
        
     

     
    
    
      

### Have your cake and eat it too

      
      

 Posted Jul 13, 2026 13:45 UTC (Mon)
                               by marcH (subscriber, #57642)
                              [[Link](https://lwn.net/Articles/1082651/)] 
      
      
      
      
      
> Unfortunately android developer verification is not going to help with netnut infested apps.
> Malware infected apps are rampant in the play store even now. ADV will not help with that.

Can you predict the stock market too?

> What it will do is prevent apps installed from f-droid and other sources, ...

Yes, blocking bad actors is often used as an excuse for vendor lock-in. It's easier to do both at the same time and just lock everything down. As I just wrote, being selective takes a lot more effort - including carefully crafted user interfaces: one of the most important and most underrated parts of security. So, as long as there is little regulation then why bother? Just lock down everything.

> ... that are much less likely to contain malware anyway.

Right, why would malware authors waste time with third-party stores that 1) are barely used, 2) tend to be used by more technical users.

      
          
            
            
            
          
        
     

     
    

    
      

### another possible source of scraper traffic

      
      

 Posted Jul 14, 2026 19:48 UTC (Tue)
                               by bentley (subscriber, #93468)
                              [[Link](https://lwn.net/Articles/1082909/)] (2 responses)
      
      
      
      
      
I've worked for a company that considers itself to be an ai company for the past 1.5 years (not one of the labs, but a smaller startup), and I can maybe add a bit of detail about another possible source of this traffic.

As context, one of the big advances in making LLMs useful over the past couple years is the idea of an "agent loop".  Instead of asking the LLM to directly answer a question or to write some code, it iteratively calls "tools" to interact with the world, bouncing back and forth between inference and tool calls.  For example, the agent might run some shell commands then based on the result look up documentation then based on that content write a script and etc.

So the actual traffic source is agents aggressively looking up documentation to complete their goals.  In the case of something like Claude Code or Codex these requests come directly from a person's computer (on a residential internet connection), and I'm not sure to what extent the software identifies itself in the UA or respects robots.txt.  In the case of something like ChatGPT or Claude web (or anything else hosted) I wouldn't be surprised if they use residential proxy services to ensure they can access content.  This might also go part of the way to explaining some requests to several decade old articles - in my own (non-ai-assisted) work I've found LWN articles to be tremendously useful, so I would not be surprised if agents are looking up old pages to try to figure out how to (eg) write or fix a driver.

      
          
            
            
            
          
        
     

     
    
    
      

### another possible source of scraper traffic

      
      

 Posted Jul 14, 2026 19:52 UTC (Tue)
                               by corbet (editor, #1)
                              [[Link](https://lwn.net/Articles/1082911/)] (1 responses)
      
      
      
      
      That might explain some requests for old articles.  It doesn't explain systematically going through the entire set of old articles, from one end to the other, with each request coming from a different IP address, though.

      
          
            
            
            
          
        
     

     
    
    
      

### another possible source of scraper traffic

      
      

 Posted Jul 14, 2026 20:54 UTC (Tue)
                               by rgmoore (✭ supporter ✭, #75)
                              [[Link](https://lwn.net/Articles/1082914/)] 
      
      
      
      
      

That's what I'd assume, too.  An AI agent looking something up is going to follow a pattern at least somewhat similar to a human being looking something up.  They'll start by looking at a few pages, spend some time digesting the contents, and then maybe come back for some related topics.  Maybe the AI agent will be more aggressive about downloading a bunch of articles at once, but it's still going to be focused on whatever task it's been given.  An AI agent that's trying to write a device driver is going to look at articles at least somewhat related to device drivers. It isn't going to dig up articles on a long-ago DPL election or arguments about which init system to use they way a deliberate attempt to scan the whole archive would.

      
          
            
            
            
          
        
     

     
    

    
      

### Free TV is part of it

      
      

 Posted Jul 16, 2026 2:48 UTC (Thu)
                               by mbcook (subscriber, #5517)
                              [[Link](https://lwn.net/Articles/1083096/)] 
      
      
      
      
      
There are a number of “free TV” boxes that I’ve heard get heavily advertised. From the discussion I remember they’re all basically the same thing. They work like a MLM where the people selling them have to buy the boxes and take all the risks including importing. 

And where does the money come from? This. It’s a residential botnet for rent. I’d be floored if AI scraping *wasn’t* a big customer. 

Also, while I understand you don’t want to explain why what you’re doing works I still think it would make a great article.

Perhaps you could explain things after they stop working, or maybe on a delay of six months or a year if they’re no longer effective at that point. I imagine it’s pretty compelling content even once out of date. 

      
          
            
            
            
          
        
     

     
    

    
      

### A couple of services that may be of help

      
      

 Posted Jul 23, 2026 16:19 UTC (Thu)
                               by fabiop (guest, #24661)
                              [[Link](https://lwn.net/Articles/1084505/)] 
      
      
      
      
      
Managing the network of a small university I found out a couple services which helped us (their basic versions are free as in beer and are alternative to more known commercial services, hope not to spam):
* shadowserver: they notice us bad connections coming from our network, so we can identify bad clients;
* abuseipdb: they keep a list of bad IPs you can filter on your firewall (in my case it is a Linux machine, which loads the IPs using ipset), you can also report them bad IPs using fail2ban.
Hope it may be of help.

      
          
            
            
            
          
        
     

     
    

 
 

 

            
            
            

            
            Copyright © 2026, Eklektix, Inc.
            This article may be redistributed under the terms of the
              [Creative
              Commons CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/) license
            Comments and public postings are copyrighted by their creators.
            Linux  is a registered trademark of Linus Torvalds
