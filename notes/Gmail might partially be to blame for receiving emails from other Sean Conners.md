---
title: "Gmail might partially be to blame for receiving emails from other Sean Conners"
url: https://boston.conman.org/2026/08/11.1
clipped: 2026-08-31 12:22:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Gmail might partially be to blame for receiving emails from other Sean Conners](https://boston.conman.org/2026/08/11.1)

## Digest Summary
The author recounts receiving emails meant for other individuals named Sean Conner because Gmail treats addresses with and without periods as equivalent (e.g., sean.conner@gmail.com = seanconner@gmail.com). This behavior, introduced after the author’s early‑adopter account was created, can cause “leakage” of messages across distinct users, especially for legacy accounts. A quoted Stack Exchange response describes a similar case where an early‑registered firstname.lastname@gmail.com address receives mail for a later‑registered firstnamelastname@gmail.com account, leading to misplaced bank, school, and other sensitive communications. Google’s official justification cites the RFC‑5321 requirement that the local‑part semantics are defined solely by the domain host, allowing Gmail to ignore periods to reduce confusion. The post also notes that while most ASCII characters are permitted in email local‑parts, some require escaping and are discouraged. The author expresses distrust of Gmail for confidential use due to these address‑handling issues.

---

## Full Article

# The Boston Diaries

        

The ongoing saga of Sean Conner, who doesn't live in Boston, nor does he even like Boston, but yet named his weblog/journal “The Boston Diaries.”
        

Go figure.
        

 

## [Tuesday, August 11, 2026](https://boston.conman.org/2026/08/11)

### [Gmail might partially be to blame for me receiving emails from other Sean Conners](https://boston.conman.org/2026/08/11.1)

I was reading the [Lobsters thread](https://lobste.rs/s/exgfc0/researcher_bought_noreply_net_companies)
about the article “[A researcher bought noreply.net. Companies started sending him secrets](https://arstechnica.com/security/2026/08/a-researcher-bought-noreply-net-companies-started-sending-him-secrets/)” when I
[left a comment](https://lobste.rs/s/exgfc0/researcher_bought_noreply_net_companies#c_uv25wk) about my own struggles with [receiving emails for other Sean Conners](https://boston.conman.org/2024/12/17.2).
That started a thread that swamped the comment section about other people who had similar stories,
so it's nice to know that I'm not alone.
Also,
here's one of my favorite comments in that thread
(for reasons that should be apparent):

I was about to say, "I know a guy with a whole blog series about that." But then I looked, and you were him.

[Lobsters comment from Jason McBrayer](https://lobste.rs/s/exgfc0/researcher_bought_noreply_net_companies#c_oj1jy0)

Heh.

But the thread as a whole left me with the idea that there's still a lot of people out there that barely understand email and aren't even sure what their own email even is.
Sad.

I did get an email about my comment from Keong Lim,
claiming it was mostly Google's fault for the confusion and linked to this fairly damning answer at Stack Exchange:

It is a lesson in human nature that so many experts simply recite Google's
pat answer on this as if an assertion were identical to empirical reality. 
I am one of the early account holders with the  `firstname.lastname@gmail.com` 
accounts.  About three years ago, I began receiving email directed to  `firstnamelastname@gmail.com` .  By triangulating the information I was able to
glean from their dry cleaners, car dealer, etc.  I was finally able to
contact these people (about 3,000 miles from me, BTW).  The DO have the same
account as me, minus the period.  We were able to determine that only a
portion of email "leaks" across accounts.  Unfortunately, the fact that I
had my account 10 years before they had theirs did not convince them to
leave the account to me.  Thus, I live with the occasional notice from the
bank, school, etc.  Because of this, I no longer use Gmail for anything
important or confidential.

The most disturbing thing to me is Google's insistence that they could not
have made a programming mistake when they clearly did.  These folks are
arrogant in their faux humility.

[Why does Google not consider dot in usernames of Gmail addresses?](https://webapps.stackexchange.com/questions/14668/why-does-google-not-consider-dot-in-usernames-of-gmail-addresses/90466#90466)

The “pat answer” is that Google is that it's cutting down on possible confusion over who receives firstname.lastname `@gmail.com`  and
firstnamelastname `@gmail.com` ,
but it seems that the “pat answer” is a somewhat later change to Gmail to ignore periods in the local part
(the part before the “@”)
of the email address.
I think Gmail is leaning heavily upon this portion of “[RFC-5321: Simple Mail Transfer Protocol](https://www.rfc-editor.org/rfc/rfc5321.txt)” to justify this:

#### 2.3.11. Mailbox and Address

As used in this specification, an "address" is a character string that
identifies a user to whom mail will be sent or a location into which mail
will be deposited.  …  Consequently, and due to a long history of problems
when intermediate hosts have attempted to optimize transport by modifying
them, the local-part MUST be interpreted and assigned
semantics only by the host specified in the domain part of the address.

(emphasis added)

I know I signed up early enough to Gmail to get  `sean.conner@gmail.com`  and at that time,
 `seanconner@gmail.com`  might have been considered a different email address.
After the change,
it appears that Gmail might get confused sometimes and mess up some legacy addresses at times.

While reading all that,
I did go down a small rabbit hole with what characters are actually allowed in an email address.
It's unclear if anything but ASCII is allowed,
but there are surprisingly little in ASCII that isn't allowed.
Out of the 95 defined graphic characacters (which I'm including the space character),
the following are not allowed:

  ASCII characters not allowed in an email address
  
    character name
  
  
      Space
    " Quotation Mark
    ( Left Parenthesis
    ) Right Parenthesis
    , Comma
    : Colon
    ; Semicolon
    < Less-than Sign
    > Greater-than sign
    @ Commercial At
    [ Left Square Bracket
    \ Reversed Solidus
    ] Right Square Bracket
  

Technically,
they could be used in an email address if they're escaped,
but it's discouraged heavily.

#### Discussions about this entry

- [Gmail might partially be to blame for receiving emails from other Sean Conners | Hacker News](https://news.ycombinator.com/item?id=49326229)

- [Gmail might partially be to blame for receiving emails from other Sean Conners - ZeroBytes](https://zerobytes.monster/post/15712337)

- [Gmail might partially be to blame for receiving emails from other Sean Conners - Lemmy: Bestiverse](https://lemmy.bestiver.se/post/1290608)

  
    
- [Current](https://boston.conman.org/2026/08)

    
- [Next](https://boston.conman.org/2026/08/15.1)

- [Previous](https://boston.conman.org/2026/08/08.1)

    
- [First](https://boston.conman.org/1999/12/04.1)
    
- [Last](https://boston.conman.org/2026/08/20.1)
    
- [Top](http://boston.conman.org/)
    
- [Home](https://www.conman.org/people/spc/)
    
- [About](https://boston.conman.org/about/)
    
- [Archive](https://boston.conman.org/archive/)
    
- [Search](https://boston.conman.org/refs/search.html)
    
- [Glossary](https://boston.conman.org/refs/glossary.html)
    
- [Copyright](https://boston.conman.org/refs/copyright.html)
    
- [Help](https://boston.conman.org/refs/help.html)
    
- [Accessibility](https://boston.conman.org/refs/access.html)
  
  

  

  

## Obligatory Picture

  
  

  
  
  
  
  
  

## Obligatory Contact Info

  
    
- [Comments?  sean@conman.org](mailto:sean@conman.org)
  
  
  

## Obligatory Feeds

  
    
- [RSS Feed](https://boston.conman.org/bostondiaries.rss)
    
- [Atom Feed](https://boston.conman.org/index.atom)
    
- [JSON Feed](https://boston.conman.org/index.json)
  
  
  

## Obligatory Links

  
    
- [Flutterby!](https://www.flutterby.com/)
    
- [KIRK.is](https://kirk.is/)
  
  
  

## Obligatory Miscellaneous

  
    
- [About the Source Code](https://boston.conman.org/about/)
    
- [Source Code](https://github.com/spc476/mod_blog)
  

  

## Obligatory AI Disclaimer

  

No AI was used in the
  making of this site, unless otherwise noted.

        

You have my permission to link freely to any entry here.  Go
        ahead, I won't bite.  I promise.
        
        

The dates are the permanent links to that day's entries (or
        entry, if there is only one entry).  The titles are the permanent
        links to that entry only.  The format for the links are
        simple: Start with the base link for this site: [https://boston.conman.org/](https://boston.conman.org/), then add the date you are
        interested in, say [2000/08/01](https://boston.conman.org/2000/08/01),
        so that would make the final URL:
        
        

[https://boston.conman.org/2000/08/01](https://boston.conman.org/2000/08/01)
        
        

You can also specify the entire month by leaving off the day
        portion.  You can even select [an arbitrary portion of time.](https://boston.conman.org/about/technical.html)
        
        

You may also note subtle shading of the links and that's
        intentional: the “closer” the link is (relative to the
        page) the “brighter” it appears.  It's an experiment in
        using color shading to denote the distance a link is from here.  If
        you don't notice it, don't worry; it's not all that
        important.
        
        

It is assumed that every brand name, slogan, corporate name,
        symbol, design element, et cetera mentioned in these pages is a
        protected and/or trademarked entity, the sole property of its
        owner(s), and acknowledgement of this status is implied.
        

        

Copyright © 1999-2026 by [Sean Conner.](mailto:sean@conman.org) All Rights
        Reserved.
