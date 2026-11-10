---
title: "Publish on your own site, syndicate elsewhere"
url: https://indieweb.org/POSSE#
clipped: 2026-06-17 02:04:30
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - POSSE distribution model
  - IndieWeb publishing
  - canonical content ownership
  - feed syndication
related:
  - "[[POSSE]]"
  - "[[IndieWeb]]"
  - "[[Canonical Content Ownership]]"
  - "[[Feed Syndication]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The wiki article explains the POSSE (Publish on Own Site, Syndicate Elsewhere) model, focusing on ownership of data, syndication mechanics, and community discussion of its trade-offs.
> 
> **Key points:**
> - POSSE advocates publishing original content on a personal domain first, then copying or linking to social silos like Twitter or Mastodon.
> - The model reduces platform dependence, preserves canonical URLs under the author's control, and facilitates reverse syndication (backfeed).
> - Permashortlinks embedded in syndicated copies direct readers to the original, improving search rankings, discovery, and spam mitigation.
> - Developers can automate POSSE via API integration, preview interfaces, or tools in PHP, Python, and Docker.
> - Community members support the control POSSE offers, despite issues with API limits, walled gardens, and the effort required to manage multiple channels.
> 
> **Concept links:** [[POSSE]], [[IndieWeb]], [[Canonical Content Ownership]], [[Feed Syndication]]
> 
> **Suggested connections:**
> - [[POSSE]] — detailed specifications and patterns for federated publishing.
> - [[IndieWeb]] — movement promoting personal websites and decentralized protocols.
> - [[Feed Syndication]] — RSS, Atom, and automated copying across platforms.
<!-- ai-summary:end -->

# [Publish on your own site, syndicate elsewhere](https://indieweb.org/POSSE#)

## Digest Summary
POSSE (Publish (on your) Own Site, Syndicate Elsewhere) is a content‑distribution model where the author posts to their own domain first, then copies or links to third‑party silos (e.g., Twitter, Facebook, Mastodon). It reduces reliance on external services, preserves canonical URLs, ensures ownership, improves searchability, and allows reverse‑syndication (backfeed) of responses. Syndicated copies typically include a permashortlink back to the original, aiding discovery, spam mitigation, and SEO ranking.

Implementation for developers involves automatic posting of the original and then posting a copy with the original link to each chosen silo; the UI can be invisible or provide a preview. Two workflow patterns exist: (1) client → site → silo (server handles syndication) and (2) client → site and client → silo (manual selection). Popular destinations include Twitter, Facebook, Medium, WordPress.com, and ActivityPub services.

Libraries and tools supporting POSSE: PHP php‑helpers (POSSE namespace), Python SiloRider, Feed2Toot, Docker images, and various Micropub/Microsub integrations. Numerous IndieWeb sites (e.g., tantek.com, waterpigs.co.uk, aaronparecki.com) demonstrate POSSE with plugins, custom CMSes, or command‑line tools. Related models are COPE (Create Once, Publish Everywhere), POSE (Publish Once, Syndicate Everywhere), and PESOS/P ESETAS, which invert the ownership order.

## Discussion Summary
Comments broadly endorse using a personal website as the primary publishing platform and syndicating via RSS, newsletters, and social networks. Contributors cite substantial traffic from RSS feeds and search, appreciate control over content, and value the resilience against platform shutdowns. Challenges mentioned include automation limits, differing community norms across networks, and reduced reach when posting links on walled‑garden services. While many find the approach rewarding and sustainable, several note the extra effort required to tailor posts and maintain multiple distribution channels. Overall, the sentiment favors POSSE despite its practical complexities.

---

## Full Article

![Figure out how you want to fit into the network.](https://indieweb.org/images/6/6a/fit-into-the-network.png)

[![POSSE icon](https://indieweb.org/images/thumb/6/66/posse.svg/128px-posse.svg.png)](https://indieweb.org/File:posse.svg "POSSE icon")

POSSE icon

[![](https://indieweb.org/images/thumb/6/64/POSSE-2012-312.jpeg/320px-POSSE-2012-312.jpeg)](https://indieweb.org/File:POSSE-2012-312.jpeg)

**POSSE** is an abbreviation for **Publish (on your) Own Site, [Syndicate](https://indieweb.org/Category:syndication "Category:syndication") Elsewhere**, the practice of posting content on your own site first, then publishing copies or sharing links to third parties (like [social media](https://indieweb.org/social_media "social media") silos) with [original post links](https://indieweb.org/original_post_link "original post link") to provide viewers a path to directly interacting with your content.

[▶️ watch Zach’s 1min**\*** video intro to POSSE](https://www.youtube.com/watch?v=X3SrZuH00GQ&t=835s)

Why
---

**Let your friends read your posts, their way.** POSSE lets your friends keep using whatever they use to read your stuff (e.g. social media [silos](https://indieweb.org/silo "silo") like [Instagram](https://indieweb.org/Instagram "Instagram"), [Tumblr](https://indieweb.org/Tumblr "Tumblr"), [Twitter](https://indieweb.org/Twitter "Twitter"), [Neocities](https://indieweb.org/Neocities "Neocities"), etc.).

**Stay in touch with friends now**, not some theoretical future. POSSE is about staying in touch with current friends now, rather than the potential of staying in touch with friends in the future.

**Friends are more important than federation.** By focusing on relationships that matter to people rather than architectural ideals, from a human perspective, POSSE is more important than [federation](https://indieweb.org/federation "federation"). Additionally, if federated approaches take a POSSE approach first, they will likely get better adoption (everyone wants to stay in touch with their friends), and thereby more rapidly approach that federated future.

**POSSE is beyond blogging.** It's a key part of why and how the IndieWeb movement is [different](https://indieweb.org/different "different") from just "everyone blog on their own site", and also different from "everyone just install and run (YourFavoriteSocialSoftware)" etc. [monoculture](https://indieweb.org/monoculture "monoculture") solutions.

### Why In General

POSSE is considered a robust and preferable syndication model for the following reasons:

* **Reduce 3rd party dependence.** By posting directly to your own site, you're not dependent on 3rd Party services to do so -- if you can access your site, you can publish your content. On the contrary with PESOS, [when the 3rd party site is down](https://twitter.com/colinjohnston/status/772533151960707072), you are unable to add content.
* **Ownership.** By posting *first* on your own site, you create a direct ownership chain that can be traced back to you without any intervening 3rd party services (silos) TOS's getting in the way (which is a vulnerability of [PESOS](https://indieweb.org/PESOS "PESOS")).
* **Own canonical URLs to your content.** Canonical URLs to your content are on your domain.
* **Copies can cite the original.** By posting content first to your own site (and thus creating a permalink for it), copies that you post on 3rd Party services can link or cite the original on your site (see [syndication\_formats](https://indieweb.org/syndication_formats "syndication formats") and [POSSE Notes to Twitter](https://indieweb.org/Twitter#POSSE_Notes_to_Twitter "Twitter"))
* **Better search.** Searching public content on your own domain (with any web search engine of your choice) works better than depending on [silos](https://indieweb.org/silos "silos") exclusively to search your posts (e.g. Twitter for a while only showed recent tweets in search results. [Facebook](https://indieweb.org/Facebook "Facebook") still has very poor search results).
* [backfeed](https://indieweb.org/backfeed "backfeed") can be used to pull in (reverse syndicate) responses from other services
* allows taking advantage of other services' social layers and aggregation features while storing the canonical copy of your content on your own site
* ...

### Why Link To Your Original

Common POSSE practice is to link from POSSE copies to your original, using a [permashortlink](https://indieweb.org/permashortlink "permashortlink"). Here are a few reasons why:

* **Discovery of your original content.** [discovery](https://indieweb.org/discovery "discovery") of your original content from the copies on 3rd party services is enabled by the permashortlinks to your originals posted on said services
* **Subvert spammers who copy your posts.** When spammers (e.g. @sin3rss) mindlessly copy from your POSSE copies and repost, they also copy the link back to the original, and thus provide more distribution for people to find and view your original post. "[2011-01-09 internet aikido](http://tantek.com/2011/009/t3/value-searching-finding-past-tweets-self-hosting)" of a sort.
* **Better ranking for your original posts.** If/when your POSSE copies are themselves copied by others and (re)posted elsewhere (e.g. manual retweets, RSS bots etc.), when the copies link to your original posts, search engines figure that out by following those links back to the original and ranking it higher.

How to
------

### How to implement

This section is for web developers implementing POSSE.

#### In General

In general, when your content posting software posts something, it should also post a copy to the [silo](https://indieweb.org/silo "silo") destinations of your choice, with an [original post link](https://indieweb.org/original_post_link "original post link") (e.g. [permashortlink](https://indieweb.org/permashortlink "permashortlink") or [permashortcitation](https://indieweb.org/permashortcitation "permashortcitation")) back to your original.

The details of how to do so vary per destination. See the silo-specific sections below.

Once you have posted the copy to the silo, you should:

* link to the syndicated copy from the original in a **[posts-elsewhere](https://indieweb.org/posts-elsewhere "posts-elsewhere")** section on your post.

#### User Interface

The best user interface (UI) is automatic, dependable, and invisible. If you can implement POSSEing in a way that always does exactly what you want, predictably, then no explicit UI is needed.

##### Preview

One way to provide more predictability and inspire confidence is to show what will be POSSEd (within the limitations of the destination) as a preview before publishing

(needs screenshot)

#### 

[Twitter](https://indieweb.org/Twitter "Twitter") is perhaps the most popular POSSE destination and a good place to start.

If you can start posting notes (tweets) to your own site and POSSEing to Twitter, *instead of* posting directly to Twitter, you have taken a big step towards owning your data.

Details:

* API Access - [posting new tweets](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html) works nicely due to permanent API tokens, and the return value contains a URL to the posted
  + As of 2022-11, Twitter is rejecting new API access for applications used to POSSE/backfeed on the grounds that they may violate twitter’s rules and/or policies — ![](https://waterpigs.co.uk/photo-2021-04-22-100w.jpg) [Barnaby Walters](https://indieweb.org/User:Waterpigs.co.uk "User:Waterpigs.co.uk")
* Supports very complete web action endpoints, so semi-manual posting is easy to implement
  + What are these endpoints? Is this still the case in 2022? — ![](https://waterpigs.co.uk/photo-2021-04-22-100w.jpg) [Barnaby Walters](https://indieweb.org/User:Waterpigs.co.uk "User:Waterpigs.co.uk")

See [POSSE to Twitter](https://indieweb.org/Twitter#POSSE_to_Twitter "Twitter") for details on how to POSSE both notes and articles (blog posts) to Twitter.

#### Facebook

There are two options for POSSEing to Facebook currently:

#### Medium

#### WordPress

* How does veganstraightedge.com do it? (all his articles are manually POSSEd to WordPress.com)
* ![](https://www.boffosocko.com/logo.jpg) [Chris Aldrich](https://indieweb.org/User:Boffosocko.com "User:Boffosocko.com") uses a WordPress plugin [WordPress Crosspost](https://wordpress.org/plugins/wp-crosspost/) to POSSE from a self-hosted WordPress install to WordPress.com.

#### Ghost

* a community developed open source tool is available on [GitHub](https://github.com/wpowiertowski/posse); the tool uses Ghost webhooks to receive latest published post in JSON format and syndicates the posts to Mastodon and Bluesky accounts

#### Plain Text Notes

Some destinations (e.g. [SMS](https://indieweb.org/SMS "SMS") or [push notifications](https://indieweb.org/push_notification "push notification")) may require a pure plain text representation.

#### Software

Software and libraries to implement POSSE:

* PHP
  + The POSSE namespace in [php-helpers](https://github.com/barnabywalters/php-helpers) (might be moved to a separate package) contains various truncation, preparation and syndication functions including HTML => plaintext µblog syntax converter
* Python
  + [SiloRider](https://bolt80.com/silorider/) is a command-line tool, implemented in Python, that lets you implement POSSE to various services (Twitter and Mastodon as of 2018-08-01).
  + [Feed2Toot](https://gitlab.com/chaica/feed2toot) is another command-line python tool that parses any number of RSS feeds and posts their content on ActivityPub based services (tested with: Mastodon, Pleroma). Contains some neat bells and whistles like advanced post filtering, numerous options for feed parsing and toot formatting.
* Docker

#### Services

#### Publishing Flows

There's at least two ways to implement a POSSE content posting flow:

##### Client to site to silo

* The user writes a piece of content using a publishing client
  + Optional: client provides UI for selecting which 3rd party services to push to if it knows about them, with optional customizations for per service
* Having finished the content, the user publishes content to their server (optionally: with metadata of which 3rd party services and any customizations thereof)
  + Optional: client can generate a permalink knowing the state of the server, and publish to that permalink
* The server publishes the content, generates a permalink and summary (and/or customized content suited to 3rd party services) if necessary
* The server posts copies with permalinks to 3rd party services

Advantages:

* User only has to interact with one site over the internet, their own
* Syndication can be done fully automatically by the server

Disadvantages:

##### Client to site and silo

* The user writes a piece of content using a publishing client
* Having finished the content, the user publishes it to their server
* The client queries the server for the URL of the content it just pushed
* The publishing client presents the user with an interface for selecting:
  + Which 3rd party services to publish to
  + The exact content published to the services, pre-filled with a summary based on the produced content
* The user selects the services and submits the form
* The publishing client posts the content summaries out to the 3rd party services

Advantages:

* More user control over timing and editing of copies of content to 3rd party services

Disadvantages:

* Syndication requires a manual step each time
* Dependent on client connectivity directly to 3rd party services (problematic in flakey mobile situations, or when client is publishing using domain-censored internet access).

IndieWeb Examples
-----------------

The following IndieWebCamp participants' sites support a POSSE architecture. If you have an implementation, add it, make screenshots or a screencast or blog about it and post the details/link here. In date order (earliest first) :

### Tantek

**[Tantek.com](http://tantek.com)** as of 2010-01-01[[1]](http://tantek.com/2010/001/t1/declaring-independence-building-it) (2010-01-26 Twitter syndication started[[2]](https://twitter.com/t/status/8228455558) and caught up[[3]](http://tantek.com/2010/026/t2/tweeting-from-tantek-com)[[4]](https://twitter.com/t/status/8228820728)). [Tantek Çelik](https://indieweb.org/User:Tantek.com "User:Tantek.com") implemented POSSE in [Falcon](http://tantek.com/w/Falcon) on [tantek.com](http://tantek.com).

* all self-hosted posts are openly with [PuSH](https://indieweb.org/PuSH "PuSH") v0.4 + [h-feed](https://indieweb.org/h-feed "h-feed") and Atom real-time syndicated with a PubsubHubbub hub to [StatusNet](https://indieweb.org/StatusNet "StatusNet"), other subscribers etc. (also to [Google Buzz](https://indieweb.org/Google_Buzz "Google Buzz") til it shutdown)
* [note](https://indieweb.org/note "note") (and [article](https://indieweb.org/article "article") titles), [reply](https://indieweb.org/reply "reply"), [RSVP](https://indieweb.org/RSVP "RSVP") posts are [snowflake](https://indieweb.org/snowflake "snowflake") copied by the personal site server to Twitter with permashortlink citation links/references (see [Whistle](http://tantek.com/w/Whistle) for details) back to the original. Copies of notes to Twitter are also automatically recopied from there to Facebook.
  + [RSVPs](https://indieweb.org/RSVP "RSVP") to Facebook events are "copied" (more like propagated) to Facebook using [Bridgy](https://indieweb.org/Bridgy "Bridgy") publish
* [likes](https://indieweb.org/like "like") of tweets are "copied" (more like propagated) to Twitter using [Bridgy](https://indieweb.org/Bridgy "Bridgy") publish

### Barnaby Walters

**[Waterpigs.co.uk](http://Waterpigs.co.uk)** as of 2012-03-12. [Barnaby Walters](https://indieweb.org/User:Waterpigs.co.uk "User:Waterpigs.co.uk") implemented POSSE over at [waterpigs.co.uk](http://waterpigs.co.uk)

* as of 2012-09-25 all collections (notes, articles, activity) are [PuSH](https://indieweb.org/PuSH "PuSH")-subscribable [feeds](https://indieweb.org/feeds "feeds").
* Using the Client to Server to 3rd Parties flow --[Waterpigs.co.uk](https://indieweb.org/User:Waterpigs.co.uk "User:Waterpigs.co.uk") 06:08, 25 September 2012 (PDT)
* Syndicating to Twitter + Facebook
* As of 2014-06-19 [Taproot](https://indieweb.org/Taproot "Taproot") can now optionally post additional POSSE tweets when updating a note or article — example of [updated note](http://waterpigs.co.uk/notes/4WfKUc/) and [POSSE tweet for the update](https://twitter.com/BarnabyWalters/status/479721886503288832). Note that [Bridgy](https://indieweb.org/Bridgy "Bridgy") successfully backfeeds silo interactions from the update tweet as well as the original POSSE tweet

### Brennan Novak

**[brennannovak.com](https://brennannovak.com)** as of 2012-07-01[[5]](https://brennannovak.com/notes/10)[[6]](https://twitter.com/brennannovak/status/212243963011280897). [Brennan Novak](https://indieweb.org/User:Brennannovak.com "User:Brennannovak.com") implemented POSSE on his site [brennannovak.com](https://brennannovak.com) with copies posted to Twitter and Facebook

### Aaron Parecki

**[aaronparecki.com](http://aaronparecki.com)** as of 2012-08-19[[7]](http://aaronparecki.com/2012/232/note/1)[[8]](https://twitter.com/aaronpk/status/237344101928951808). [Aaron Parecki](https://indieweb.org/User:Aaronparecki.com "User:Aaronparecki.com") implemented POSSE on his site [aaronparecki.com](http://aaronparecki.com) with copies posted to Twitter containing permashortlinks back to originals on his own site.

### Sandeep Shetty

**[User:Sandeep.io](https://indieweb.org/User:Sandeep.io "User:Sandeep.io")** First post POSSE'd on 2012-11-05. I primarily syndicate to Twitter using a very lo-fi solution of adding silo (Facebook, Twiiter, Google+) provided share links to each post that I can manually click to prefill content, edit and post. I've avoided API integration because of the extensive experience I've had using Facebook API and dealing with it's random changes. "Integration" has high costs sometimes so I keep it as simple as possible.

### Ben Werdmuller

**[werd.io](http://werd.io)** as of 2013-05-31 [[9]](http://werd.io/view/51a7fb55bed7de2f06761712). [Ben Werdmuller](https://indieweb.org/User:Benwerd.com "User:Benwerd.com") implemented POSSE in his [idno](http://idno.co) platform via plugins. New content has an associated Activity Streams object type; POSSE plugins listen for post events associated with those object types and syndicate appropriately.

* Notes and articles are syndicated to Twitter and Facebook
* Images are syndicated to Facebook, Flickr and Twitter
* Places are syndicated to Foursquare
* More plugins are very easily possible; the Foursquare plugin took about an hour to build

### Shane Becker

* [Shane Becker](https://indieweb.org/User:Veganstraightedge.com "User:Veganstraightedge.com") using [Dark Matter](https://indieweb.org/Dark_Matter "Dark Matter") on veganstraightedge.com (since 2013-07-17[[10]](http://indiewebcamp.com/irc/2013-10-31/line/1383205887)) with automatic rel-syndication markup on manual POSSEing:

### Glenn Jones

**[glennjones.net](http://glennjones.net)** as of 2014-01-14 [Glenn Jones](https://indieweb.org/User:Glennjones.net "User:Glennjones.net") The blog implemented POSSE using a new version of [transmat.io](http://transmat.io) system. New content added to transmat is associated with objects types. A POSSE twitter plugins listens for post events syndicating content. At moment only notes are syndicated.

### Jeremy Keith

**[adactio.com](http://adactio.com)** as of 2014-05-27 [Jeremy Keith](https://indieweb.org/User:Adactio.com "User:Adactio.com") has implemented POSSE using his own custom CMS.

### Shane Hudson

**[shanehudson.net](https://shanehudson.net)** as of 2014-09-19 [Shane Hudson](https://indieweb.org/User:ShaneHudson.net "User:ShaneHudson.net") has implemented POSSE to Twitter for Craft CMS.

* Previously working on Wordpress but he was not keen on the UX.
* Has reply contexts working but has to manually copy the ID.
* Not yet POSSEing photos but plans to.
* Currently he has to manually copy the tweet from the main text box to a 140 character limit tweet text box. He plans to make that automatic.

### Ravi Sagar

<http://www.ravisagar.in/blog/implementing-posse-my-site> Implementing POSSE on my site as of 2018-02-21.

* The new blogs and notes are posted on Drupal
* <http://www.ravisagar.in/rss-social.xml> RSS Feed is generated for the blogs and notes tagged with "Share" keyword
* Using Rebrandly to create shortlinks for the RSS Feed
* Using Zapier to share the newly created rebrandly links to Twitter and Linkedin

### Ludovic Chabant

**[ludovic.chabant.com](https://ludovic.chabant.com)** as of 2018-07-30 [Ludovic Chabant](https://indieweb.org/wiki/index.php?title=User:Ludovic.chabant.com&action=edit&redlink=1 "User:Ludovic.chabant.com (page does not exist)") has implement POSSE to Twitter and Mastodon from [PieCrust CMS](https://indieweb.org/PieCrust "PieCrust"), using [SiloRider](https://indieweb.org/SiloRider "SiloRider")

* SiloRider is CMS independent -- it only relies on Microformats found in the published markup.
* New articles are posted as title and link.
* New microblogging updates are mostly copied verbatim (if the fit the external service's character limits), and support photo posts, including multi-photo posts.

### Adam Dawkins

**[adamdawkins.uk](https://adamdawkins.uk)** as of 2019-01-16  [Adam Dawkins](https://indieweb.org/User:Adamdawkins.uk "User:Adamdawkins.uk") has implemented POSSE using his own custom CMS.

* Notes have been POSSEd since he first started posting them on his own site, [on 2019-01-16](https://adamdawkins.uk/2019/1/16/this-tweet-originated-on-adamdawkins-uk-posse)

#### Examples

### Shaun Ewing

**[shaun.net](https://shaun.net)** as of 2020-01-16  [Shaun Ewing](https://indieweb.org/wiki/index.php?title=User:Shaun.net&action=edit&redlink=1 "User:Shaun.net (page does not exist)") has implemented POSSE using Jekyll, and custom APIs.

### capjamesg

![](https://jamesg.blog/assets/coffeeshop.jpg) [capjamesg](https://indieweb.org/User:Jamesg.blog "User:Jamesg.blog") has been syndicating his notes from his own site to:

* Twitter using brid.gy
* micro.blog using micro.blog's feed polling system
* The fediverse using fed.brid.gy

This syndication happens automatically whenever James posts a note using his [Micropub](https://indieweb.org/Micropub "Micropub") client or his [Microsub](https://indieweb.org/Microsub "Microsub") feed reader.

### Wojtek Powiertowski

**[behindtheviewfinder.com](https://behindtheviewfinder.com)** as of 2026-01-12 has been syndicating his posts from his Ghost blog to:

This syndication happens automatically whenever Wojtek publishes a new posts using his self-hosted [posse](https://github.com/wpowiertowski/posse) client.

### ... add more here ...

... Add a link to your POSSE–enabled site and the date you started syndicating copies of your content out to 3rd party social sharing/publishing services.

### Partial POSSE sites

Sites which only POSSE some of their content, and still post directly to the same silo they POSSE to.

Other partial POSSE sites:

* **[User:Hupili.net](https://indieweb.org/User:Hupili.net "User:Hupili.net")** implements a partial POSSE with the following setups:
  + [SNSAPI](https://indieweb.org/SNSAPI "SNSAPI") is a lightweight middleware to unify the data structure and interfaces of different social networking services. It gives the scripting flexibility for developer users to manipulate social silos.
  + [SNSRouter](https://indieweb.org/SNSRouter "SNSRouter") is a web UI built upon SNSAPI where one can read an aggregated timeline from different sites, mass forward messages, and update statuses on all channels.
  + As is said in one of the description paragraph above, this model is not truly POSSE. One can not (hardly) distinguish original/ syndicated status. I'm planning to put a page with permlink on my site upon each status update and then use SNSAPI to syndicate to other silos.

Other Approaches
----------------

### COPE

COPE is short for Create Once, Publish Everywhere (COPE), which explicitly lacks a first "Publish Once" step, and thus is more about duplicating the content across various destinations.

Without a first "Publish Once" step on a site you "Own", and thus lacking [original post permalinks](https://indieweb.org/original_post_permalink "original post permalink"), the COPE strategy fails to actually draw people to any one canonical place to read/view your stuff, and thus all it does is grow (likely) disjoint audiences across other people’s sites.

Articles:

### POSE

[POSE](https://indieweb.org/POSE "POSE"), Publish Once Syndicate Everywhere, was a broader predecessor of POSSE that also included publishing once on one particular [silo](https://indieweb.org/silo "silo"), and then syndicating out to other silos.

### PESOS

A similar but opposite approach is [PESOS](https://indieweb.org/PESOS "PESOS") where content is posted first to 3rd party services and then copied/syndicated into a personal site.

If exact copies of content are posted on both a personal site and 3rd party services, there's no way to tell (short of comparing possibly non-existent sub-second accurate published dates) whether a site is using POSSE or PESOS. Sites can provably support POSSE by including perma(short)links in syndicated copies that link/reference back to published originals.

### PESETAS

[PESETAS](https://indieweb.org/PESETAS "PESETAS") is like PESOS but copying/syndicating everything to a particular silo (without any involvement of a personal site).

For example, most silos support cross-posting to [Twitter](https://indieweb.org/Twitter "Twitter"), thus you could connect everything to your Twitter account and always (auto-)cross-post there to keep a copy.

E.g. [Tumblr](https://indieweb.org/Tumblr "Tumblr") has a UI for cross-posting to [Twitter](https://indieweb.org/Twitter "Twitter"). See [Webapps StackExchange post](http://webapps.stackexchange.com/questions/15315/customize-the-message-tumblr-sends-to-twitter) for documentation and screenshots of UI.

Tumblr is a better PESETAS destination however, since it is well established, allows for a wider variety of content, and allows more text, and links to URLs directly instead of linkwrapping them like Twitter does.

Brainstorming
-------------

### CRUD

All of the above, and to date (2013-222), POSSE has solely described syndicating the **C**reation of content on your site (publishing) to other sites. This model has been quite successful and perhaps may be sufficient.

However, it is worth exploring the potential utility of a full CRUD protocol for POSSE.

### Create

Create is the POSSE default. You create content on your site, you POSSE your creates to other sites. All of this is described above, and in silo-specific details on [silo](https://indieweb.org/silo "silo") pages.

### Read

Read as a verb is interesting when applied to POSSE.

At a minimum, it's useful to implement storing links to syndicated copies of your content to provide for the future possibility of reading from downstream POSSE copies.

See:

Actual direct uses of Reading from downstream POSSE copies:

* reverse-syndication / [backfeed](https://indieweb.org/backfeed "backfeed") of activity around the POSSE copy onto your original:

In addition, keeping a [u-syndication](https://indieweb.org/u-syndication "u-syndication") link to the POSSE copy enables deleting it to perform an Update or a Delete action, as described in the following sections.

### Update

If a POSSE destination allows updates/edits, then when you edit your post, you could propagate that update to the downstream POSSE copy as well.

* E.g. [Facebook](https://indieweb.org/Facebook "Facebook") allows editing the text of a post (including any links in the text), person tags, but not the image of a photo post

If the destination disallows updates/edits, like [Twitter](https://indieweb.org/Twitter "Twitter"), it is still possible to virtually POSSE updates by deleting the POSSE tweet and reposting, i.e.:

Consider only POSSEing updates to Twitter:

* if no one has replied to it yet (otherwise you'd break a threaded conversation on Twitter)
* if your changes would be shown in the truncated copy on Twitter (i.e. if your changes are past the 140 (more like 120) character horizon, no point in churning the Twitter copy).
* within a very short time window, maybe like 2-5 minutes, because otherwise the update will be seen as a duplicate to people who are reading you on Twitter.

All of these concerns are regarding the experience that you provide to your friends reading your tweets on Twitter, which of course should be the whole (design) reason you're bothering to POSSE to Twitter in the first place.

For details, see silo-specific POSSE sections:

* [Facebook](https://indieweb.org/Facebook "Facebook"): [POSSE to Facebook](https://indieweb.org/POSSE_to_Facebook "POSSE to Facebook") ([to-do](https://indieweb.org/to-do "to-do"): needs details re: edit text ok, but no photo editing, photo posts need delete/repost to simulate POSSE update)
* [Flickr](https://indieweb.org/Flickr "Flickr"): (UI supports manually updating the image of a photo post, but is that available in the API? and if so, file a [Bridgy](https://indieweb.org/Bridgy "Bridgy") Publish feature request GitHub issue to support POSSE Update to Flickr (including the image of a photo post)
* [Twitter: POSSE to Twitter](https://indieweb.org/Twitter#POSSE_to_Twitter "Twitter") ([to-do](https://indieweb.org/to-do "to-do"): copy the above delete/repost strategy to there)
* ...

### Delete

Deletes seem fairly straightforward to POSSE, especially to services which themselves propagate deletes to clients.

E.g. one can delete a note on Twitter at any point.

Similar to updates, consider:

* if there are already replies to a POSSE copy (or activity like favorites/retweets), consider keeping it to keep conversation threading (and others' favorites/retweets).

However, if you really feel like deleting the content from your site and POSSE copies (e.g. on Twitter), go ahead and do so.

Perhaps this is an opportunity for the UI for the deletion of a post to check to see if there's been any activity (replies, favorites, retweets) on the POSSE copy before performing the delete. One possible implementation could involve the UI informing the user of this activity (or lack of it) and reconfirming the delete request on a per-service basis.

#### IndieWeb Examples

* ![](https://grant.codes/img/me-100.jpg) [Grant Richmond](https://indieweb.org/User:Grant.codes "User:Grant.codes") supports POSSE deletes on twitter as of 2018-10-10, by checking if a post on his site has been unpublished / deleted and sending the appropriate api request for likes, reposts and notes.

FAQ
---

### Worry about search engines and duplicates

Q: Do we need to worry about search engines penalizing apparently duplicate posts?

A: That's why the POSSE copies SHOULD always link back to the originals. So that search engines can infer that the copies are just copies. Ideally POSSE copies on silos should use [rel-canonical](https://indieweb.org/rel-canonical "rel-canonical") to link back to the originals, but even without explicit rel-canonical, the explicit link back to the original is a strong hint that it is an original.

This is also an advantage of POSSE over PESOS. With PESOS - there's no way to tell what's the original and what's the copy - so they do look like duplicates.

### POSSE-post-discovery and backlinks

Q: Brid.gy can use [posse-post-discovery](https://indieweb.org/posse-post-discovery "posse-post-discovery") to find the relationship between a syndicated post and the original when there is not explicit link. Does this mean I should stop adding [backlinks](https://indieweb.org/backlink "backlink") to syndicated copies?

A: POSSEing without a [backlink](https://indieweb.org/backlink "backlink") is considered a last resort, and has some costs associated with it. See [posse-post-discovery#Tradeoffs](https://indieweb.org/posse-post-discovery#Tradeoffs "posse-post-discovery") for more details.

### POSSE or Send Webmentions First

In short, **POSSE first, then send [webmentions](https://indieweb.org/webmentions "webmentions")**.

See: [Webmention FAQ: POSSE or Send Webmentions First](https://indieweb.org/Webmention-faq#POSSE_or_Send_Webmentions_First "Webmention-faq") for details and reasoning.

Background
----------

Related conceptually:

* sometime before 2014-06-21[[11]](http://tantek.com/2012/173/t1/posse-core-indieweb-approach): *[POSE](https://indieweb.org/POSE "POSE")* (Publish Once Syndicate Everywhere) term defined at some point prior to POSSE. Conceptually it was looser than POSSE, as "once" could be interpreted as on a silo rather than your "own site", which POSSE (and the conceptual predecessors) made explicit.

Articles
--------

Articles and blog posts about POSSE, especially implementing it:

* 2013-12-04 Chloe Weil: [Hipster](http://chloeweil.com/blog/hipster)
* 2014-03-09 Sebastian Greger [An audience/context-conscious POSSE syndication plugin for WordPress](http://sebastiangreger.net/2014/03/audience-context-conscious-posse-syndication-plugin-wordpress/)
* 2015-11-03 Scott Gilbertson (Ars Technica) [How Google’s AMP project speeds up the Web—by sandblasting HTML](http://arstechnica.com/information-technology/2015/11/googles-amp-an-internet-giant-tackles-the-old-myth-of-the-web-is-too-slow/)
  > […] this nudges publishers toward an idea that's big in the IndieWeb movement: Publish (on your) Own Site, Syndicate Elsewhere (or POSSE for short).
  >
  > The idea is to own the canonical copy of the content on your own site but then to send that content everywhere you can. Or rather, everywhere you want to reach your readers. Facebook Instant Article? Sure, hook up the RSS feed. Apple News? Send the feed over there, too. AMP? Sure, generate an AMP page. No need to stop there—tap the new Medium API and half a dozen others as well.
  >
  > Reading is a fragmented experience. Some people will love reading on the Web, some via RSS in their favorite reader, some in Facebook Instant Articles, some via AMP pages on Twitter, some via Lynx in their terminal running on a restored TRS-80 (seriously, it can be done. See below). The beauty of the POSSE approach is that you can reach them all from a single, canonical source.
  >
  > […]
  >
  > For the Web's sake, let's hope Google sticks with AMP long enough to convince publishers that the real future is speeding up their own pages and embracing a POSSE-style approach.
* 2018-07-31 ![](http://werd.io/file/538d0a4cbed7de5111a1ad31/thumb.jpg) [Ben Werdmüller](https://indieweb.org/User:Werd.io "User:Werd.io"): [Stepping back from POSSE](https://werd.io/2018/stepping-back-from-posse) ([archived](http://web.archive.org/web/20180803184811/https://werd.io/2018/stepping-back-from-posse))
* 2023-10-23 [David Pierce](https://www.theverge.com/authors/david-pierce): [The poster’s guide to the internet of the future](https://www.theverge.com/2023/10/23/23928550/posse-posting-activitypub-standard-twitter-tumblr-mastodon) ([archived](http://web.archive.org/web/20231023182113/https://www.theverge.com/2023/10/23/23928550/posse-posting-activitypub-standard-twitter-tumblr-mastodon))
* 2024-09-27 [Molly White](https://www.mollywhite.net/): [POSSE: Reclaiming social media in a fragmented world](https://www.citationneeded.news/posse/)
* ...

POSSE as methodology for non-web scenarios
------------------------------------------

### POSSE git repositories

As discussed #indieweb it is also possible POSSE your git repositories to git "silos", such as [GitHub](https://indieweb.org/GitHub "GitHub") or [GitLab](https://indieweb.org/GitLab "GitLab"). An easy way of doing this was described by ![](https://avatar.cweiske.de/avatar/9e263681488308e5e5d5e548b2f9bc99) [Christian Weiske](https://indieweb.org/User:Cweiske.de "User:Cweiske.de") at [[12]](https://chat.indieweb.org/2016-12-16#t1481891974356000).

Sessions
--------

See Also
--------

* [POSSE reply](https://indieweb.org/POSSE_reply "POSSE reply")
* [PESOS](https://indieweb.org/PESOS "PESOS")
* [PESETAS](https://indieweb.org/PESETAS "PESETAS")
* [why](https://indieweb.org/why "why")
* [original post link](https://indieweb.org/original_post_link "original post link")
* [microsyntax](https://indieweb.org/microsyntax "microsyntax") for POSSEing to plain text destinations
* [rel-canonical](https://indieweb.org/rel-canonical "rel-canonical")
* Documentation on [syndication formats](https://indieweb.org/syndication_formats "syndication formats")
* [posts-elsewhere](https://indieweb.org/posts-elsewhere "posts-elsewhere")
* 2017-11-09 Nicolas Hoizey: [Medium is only an edge server of your POSSE CDN, your own blog is the origin](https://nicolas-hoizey.com/2017/11/medium-is-only-an-edge-server-of-your-posse-cdn-your-own-blog-is-the-origin.html)
* 2018-03-24 Hacker News comment thread: <https://news.ycombinator.com/item?id=16663850>
* HN ibid: "Why won't a link on these platforms suffice since they have their "cards"?"
* HN ibid: "This is an interesting thing, but too complicated and over-broad for the mere-mortal." <-- page introduction needs simplifying, simpler instructions to setup POSSE, acknowledge where POSSE usability is in the [Generations](https://indieweb.org/Generations "Generations") spectrum
* HN ibid: "Facebook is just a glorified RSS feed with centralized discover ability." <-- debunk with comparing [Facebook#Features](https://indieweb.org/Facebook#Features "Facebook") (and [Twitter#Features](https://indieweb.org/Twitter#Features "Twitter")) vs RSS plumbing feature set. A visual diagram/table comparison might help.
* HN ibid: "This really is not possible with RSS at all, especially since the silos don’t want to support RSS in any meaningful way." <-- perhaps add a whole subsection in "Why" explaining why RSS is insufficient compared to POSSE.
* 2021-11-07 Hacker News comment thread: <https://news.ycombinator.com/item?id=29115696>
* Recommend non-realtime POSSE to [Twitter](https://indieweb.org/Twitter "Twitter") and other [social media](https://indieweb.org/social_media "social media") due to their active use as part of the surveillance apparatus of local and national law enforcement: <https://theintercept.com/2020/07/09/twitter-dataminr-police-spy-surveillance-black-lives-matter-protests/>
* [Jetpack 8.9 adds Social Previews](https://jetpack.com/2020/09/01/jetpack-grow-subscribers-collect-donations/) which allows one to preview how your posts will appear on Facebook, Twitter, and Google search results before you hit the publish button!
* Consider a deliberate ethical use of POSSEing, e.g. see [Code of Ethics](https://www.thesocialdilemma.com/code-of-ethics/) for an example set of explicit self-stated “Rules of engagement”
* “Pluralistic is my mutli-channel publishing effort – a project to push the limits of POSSE (post own site, share everywhere)” [Pluralistic: 05 May 2021](https://pluralistic.net/2021/05/05/clarkes-third-law/#indistinguishable-from-magic)
* Cory Doctorow explains how he uses POSSE. This Week in Google (time offset 474s): <https://www.youtube.com/watch?v=qyU2cZLFsik&t=474s>
  > I try not to get locked into anyone else’s walled garden. I … pursue this publishing strategy they call POSSE, post own site syndicate everywhere …
* articles: 2018-02-06 Dries Buytaert [To PESOS or to POSSE?](https://dri.es/to-pesos-or-to-posse) and 2018-02-16 Dries Buytaert [My POSSE plan for evolving my site](https://dri.es/my-posse-plan-for-evolving-my-site)
* <https://twitter.com/SaraSoueidan/status/1539870410317221888>
  + "What Matthias said.  
      
    Write on your own blogs, syndicate elsewhere.  
      
    Own your content! There's nothing like it." [@SaraSoueidan](https://sarasoueidan.com) June 23, 2022
* Brainstorm: ![](https://tantek.com/logo.jpg) [Tantek Çelik](https://indieweb.org/User:Tantek.com "User:Tantek.com"): POSSE advantages are largely distribution (immediately) and [discovery](https://indieweb.org/discovery "discovery") (over time). if neither of those two are happening, then it's not worth keeping it around. Date-time-proof-of-posting can be solved by sending your original post (or a POSSE/tweet copy) to the Internet Archive and does not require keeping the POSSE/tweet copy.
* <https://andy-bell.co.uk/how-im-dealing-with-twitter-in-a-hands-off-manner/>
* Why: 2023-07-13 ![](https://adactio.com/icon.png) [Jeremy Keith](https://indieweb.org/User:Adactio.com "User:Adactio.com"): [The syndicate](https://adactio.com/journal/20323)
  > We’ll see how long it lasts. We’ll see how long any of them last. Today’s social media darlings are tomorrow’s Friendster and MySpace.
  >
  > When the current crop of services wither and die, my own website will still remain in full bloom.
* <https://mastodon.social/@davidpierce/111284796654263440>
* to-do: draw an updated diagram without Twitter (replace with Bluesky), and to Fediverse via BridgyFed with a line that ends in "Y" with 📤 📥 on the ends
* update any references / instructions to POSSE to Twitter to note historical importance and current lack of automated support
* [to-do](https://indieweb.org/to-do "to-do"): add a <http://micro.blog> section to the "How to" section; make sure to link to [micro.blog](https://indieweb.org/micro.blog "micro.blog")
* Why: 2024-02-24 [Pluralistic: Vice surrenders](https://pluralistic.net/2024/02/24/anti-posse/)
  > This is the moment for POSSE (Post Own Site, Share Everywhere), a strategy that sees social media as a strategy for bringing readers to channels that you control
* [Curation is the last best hope of intelligent discourse.](https://joanwestenberg.com/blog/curation-is-the-last-best-hope-of-intelligent-discourse)
* <https://hachyderm.io/@pluralistic@mamot.fr/111987590552793552>
* ^ actual permalink: <https://mamot.fr/@pluralistic/111987590098901216>
  + "If there was ever a moment when the obvious, catastrophic, imminent risk of trusting Big Tech intermediaries to sit between you and your customers or audience, it was now. This is \*not\* the moment to be "social first." This is the moment for POSSE (Post Own Site, Share Everywhere), a strategy that sees social media as a strategy for bringing readers to channels that \*you\* control:<https://pluralistic.net/2022/02/19/now-we-are-two/#two-much-posse14/>" [@pluralistic](https://mamot.fr/@pluralistic) February 24, 2024
* 2024-03-09 Molly White: [POSSE](https://www.mollywhite.net/micro/entry/202403091817)
  > I just finally deployed something I've been working on for a few weeks now: a feed of my writing, posting, reading, and other various activity that lives on my website at <https://www.mollywhite.net/feed>
* Why: to have another way to search your stuff, since sometimes (often? usually now?) large web web search engines like [Google](https://indieweb.org/Google "Google") or even [DDG](https://indieweb.org/DDG "DDG") are very poor at site-specific searching (e.g. site:<http://tantek.com>), whereas social media silos like Twitter are very good at profile-specific searches (e.g. from:t).
* IndieWeb Example: 2024-03-09 Molly White deployed automatic POSSE to Twitter/Mastodon/Bluesky: [POSSE](https://www.mollywhite.net/micro/entry/202403091817)
* <https://mastodon.social/@flokosiol/112438679946887082>
  > "Starting day 2 of #btconf with Laura Kalbag and some #indieweb vibes." ![Laura presenting a text slide on a stage.](https://files.mastodon.social/media_attachments/files/112/438/677/114/882/928/original/e6b1de40d67b5be6.jpeg) [@flokosiol](https://mastodon.social/@flokosiol) May 14, 2024

  with embedded photo of Laura presenting a text slide on a stage:
  > Social media etiquette:
  >
  > ---
  >
  > Post to your own site first, then mirror those posts to third-party platforms.

  — a rephrasing of POSSE.
* 2024-09-27 Molly White: [POSSE: Reclaiming social media in a fragmented world](https://www.citationneeded.news/posse/)
* don't POSSE to X, says Richard MacManus <https://cybercultural.com/p/web-values/>
* [Molly White talks POSSE and more at SXSW 2025](https://schedule.sxsw.com/2025/events/PP147154) 2025-03-09
* <https://changelog.com/friends/85#t=6099>