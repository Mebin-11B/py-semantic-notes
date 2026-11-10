---
title: "The Tower Keeps Rising"
url: https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/
clipped: 2026-08-31 12:22:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Tower Keeps Rising](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/)

## Digest Summary
The essay reflects on AI‑assisted programming as a catalyst that reduces coordination friction in large software projects. While AI agents can quickly generate code (e.g., adding OAuth, caching, UI changes) and produce documentation on demand, the author argues that the primary limitation in complex systems is not individual coding speed but the shared understanding of architectural concepts, invariants, ownership, and design rationale. Historically, this shared language is built through documentation, code reviews, and direct interaction, which synchronizes team members. AI agents bypass many of these interactions, allowing isolated changes without requiring developers to internalize the broader system model. Consequently, the collective mental model erodes, similar to the biblical Tower of Babel, yet construction continues because the agents hide the loss of coherence. The author warns that continuous development without a common architectural language may lead to increasingly opaque codebases, even as the “tower” keeps rising.

---

## Full Article

[Armin Ronacher](https://lucumr.pocoo.org/about/)'s Thoughts and Writings
      
      
        
          
- [blog](https://lucumr.pocoo.org/)
          
- [archive](https://lucumr.pocoo.org/archive/)
          
- [projects](https://lucumr.pocoo.org/projects/)
          
- [travel](https://lucumr.pocoo.org/travel/)
          
- [talks](https://lucumr.pocoo.org/talks/)
          
- [about](https://lucumr.pocoo.org/about/)
        
      
      
        
  

# The Tower Keeps Rising

  
  

written on July 13, 2026
  

  

I feel that some vibecoded software changes somewhat randomly and unexpectedly.
That made me think about Bruegel’s [“The Tower of
Babel”](https://en.wikipedia.org/wiki/The_Tower_of_Babel_(Bruegel)) which shows
an already quite chaotic depiction of the Tower of Babel.  The story is usually
told as one about pride and ambition and ultimately why people no longer speak
the same language.  But it is also a story about the unity that makes
technological progress work.

The text begins with a technology upgrade:

And they said one to another, Go to, let us make brick, and burn them
thoroughly.  And they had brick for stone, and slime had they for morter.

They use it for a civilizational project:

let us build us a city and a tower, whose top may reach unto heaven

But when God assesses the situation the bricks are not what concern him:

the people is one, and they have all one language, […] and now nothing will be
restrained from them.[1](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/#fn-1)

The source of their power is coordination.  They share a language and with that
shared language they can combine their work into something no one of them could
build alone.  God does not take away the bricks or their knowledge of how to
make them.  He takes away their ability to understand one another, and
construction stops.

There is the appealing idea that AI-assisted programming means better tools
which lets us build more ambitious software.  That is certainly true at the
level of the individual and without doubt a developer with an agent will be
dramatically more capable of changing a codebase.  But large software projects
have never been limited only by how quickly an individual can produce code.
They are limited by how well people can coordinate their understanding of the
system they are changing.

The shared language of a software project is not English or Python but it is the
common understanding of what its concepts mean, where the boundaries are, which
invariants matter, who owns what, and why the system has the shape it does.
This language is rarely written down in one place.  It lives partly in
documentation and code, but also in code review, conversations, arguments, and
the experience of having to explain a change to somebody else.

Before agents, some of this shared understanding was maintained by friction.
If I wanted to change your storage layer, I usually had to read your code, ask
you questions, and perhaps coordinate with another team whose service depended
on it.  This was slow, and much of that slowness was waste but not all of it
was.  Some of it was the process by which your understanding became mine, and
by which both of us discovered whether we still agreed about how the system
worked.  This friction synchronizes people.

Agents remove much of that friction.  I can ask an agent to add OAuth, you can
ask one to add caching, and somebody else can ask one to rebuild the database
from first principles and make the UI pink.  Each change can be reasonable in
isolation.  The code can compile, the tests can pass, and the explanations can
be generated on demand.  None of us necessarily has to talk to the others, or
even acquire the part of the shared model that the change once would have forced
us to learn.

As I said many times before: agents do not feel pain, only humans do.  Agents
now let us act in parts of the system where we would previously have needed
other people and in code bases where the people would have revolted.

When I look at some vibecoded scaled-up projects the codebases become Babel not
because nobody can communicate, but because nobody needs to.  Every developer
has a tireless translator that can explain a corner of the tower and make
whatever local alteration they ask of it.  The changes keep landing, even as the
architectural language that would let the humans reason about them together
disappears.

But it’s not the biblical story.  At Babel, the loss of common language stops
construction whereas in AI-assisted engineering, construction can continue after
shared understanding has already collapsed.  The lack of an immediate failure is
what makes it curious and a bit disorienting.  The tower does not fall, and so
we do not notice what was lost.  It just keeps rising.

- 

[Genesis 11:3-6, KJV](https://www.biblegateway.com/passage/?search=Genesis%2011%3A3-6&version=KJV).[↩](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/#fnref-1)

  
  

This entry was tagged
    
      [ai](https://lucumr.pocoo.org/tags/ai/) and 
      [thoughts](https://lucumr.pocoo.org/tags/thoughts/)
  

  

    [copy as](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising.md) / [view](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising.md) markdown
  
  
  

      
      
        

© Copyright 2026 by Armin Ronacher.
        

          Content licensed under the Creative Commons
          Attribution-NonCommercial 4.0 International [License](https://creativecommons.org/licenses/by-nc/4.0/).
        

          Contact me via [mail](mailto:armin.ronacher@active-4.com),
          [bluesky](https://bsky.app/profile/mitsuhiko.at),
          [x](http://x.com/mitsuhiko), or
          [github](http://github.com/mitsuhiko).
        

          You can [sponsor me on github](https://github.com/sponsors/mitsuhiko/).
        

          More info: [imprint](https://lucumr.pocoo.org/about#imprint) &
          [AI transparency](https://lucumr.pocoo.org/ai-transparency).
          Subscribe via [atom](https://lucumr.pocoo.org/feed.atom) / [RSS](https://lucumr.pocoo.org/feed.xml).
        

          Color scheme:
           auto,
           light,
           dark.
