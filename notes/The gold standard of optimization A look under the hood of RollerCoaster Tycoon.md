---
title: "The gold standard of optimization: A look under the hood of RollerCoaster Tycoon"
url: https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/
clipped: 2026-06-17 01:28:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - assembly programming
  - game engine optimization
  - retro engineering
  - memory footprint
related:
  - "[[Assembly Programming]]"
  - "[[Game Engine Optimization]]"
  - "[[Software Optimization]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A reverse-engineering review of RollerCoaster Tycoon (1999) reveals extreme assembly-level and memory footprint optimizations by Chris Sawyer.
>
> **Key points:**
> - Chris Sawyer wrote RollerCoaster Tycoon almost entirely in Assembly, allowing precise control over registers and memory.
> - Memory optimizations include using minimal integer sizes for specific fields (e.g., 1-byte shop prices) to maximize cache efficiency.
> - The game uses clever coordinate math, lookup tables, and custom rendering loops to handle hundreds of simulated guests on low-end hardware.
>
> **Concept links:** [[Assembly Programming]], [[Game Engine Optimization]], [[Retro Engineering]], [[Memory Footprint]]
>
> **Suggested connections:**
> - [[Software Optimization]] — principles of performance tuning at the hardware level.
> - [[OpenRCT2]] — the modern open-source rewrite and its discoveries of Sawyer's original codebase.
<!-- ai-summary:end -->

# [The gold standard of optimization: A look under the hood of RollerCoaster Tycoon](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/)

## Digest Summary
RollerCoaster Tycoon (1999) is renowned for its performance, achieved primarily through Chris Sawyer’s use of hand‑written Assembly and aggressive low‑level optimizations. A reverse‑engineered clone, OpenRCT2, confirms many techniques: monetary values employ the smallest suitable integer size (e.g., 1‑byte for shop prices, 4‑byte for park total), reducing memory bandwidth. Frequent multiplication/division by powers of two is replaced with left/right bit‑shifts, and game formulas are deliberately crafted to fit these powers, minimizing costly arithmetic. Design decisions also serve performance: guests wander randomly instead of selecting rides then pathfinding, eliminating per‑agent route calculations. When pathfinding is required (e.g., reaching exits or repairs), the engine imposes a depth limit (default 5 junctions, extended for mechanics or map‑owned guests) to cap CPU load, with failures exposed as guest complaints. Crowd simulation avoids collision detection; multiple agents occupy the same tile, and only aggregate density influences guest happiness. These combined hardware‑aware coding practices and gameplay‑centric compromises enable thousands of agents to run smoothly on 1999 hardware.

## Discussion Summary
The discussion highlights historical reliance on hand‑written assembly in early PC and console games to meet performance limits, noting examples such as Warcraft, StarCraft, RollerCoaster Tycoon, and Blackthorne, while acknowledging that modern compilers now automatically replace many power‑of‑two divisions with shifts. Contributors express admiration for the original low‑level work, reference contemporary optimization challenges in games like Factorio, and debate the relevance of explicit bit‑shift tricks versus built‑in compiler optimizations. Overall sentiment is appreciative of past engineering feats, with nuanced views on the continuing role of manual low‑level optimization.

---

## Full Article

Due to some lucky circumstances, I recently had the chance to appear in one of the biggest German gaming podcasts, [Stay Forever](https://www.stayforever.de/), to talk about the technology of [RollerCoaster Tycoon](https://en.wikipedia.org/wiki/RollerCoaster_Tycoon_(video_game)) (1999). It was a great interview, and I strongly recommend to listen to the whole episode [here](https://www.stayforever.de/2026/02/rollercoaster-tycoon-sf-161/), at least if you speak german. If not, don’t worry—this article covers what was said (and a little more).

![](https://larstofus.com/wp-content/uploads/2026/03/image-1.png?w=288)

RollerCoaster Tycoon and its sequel are often named as some of the best-optimized games out there, written almost completely in Assembly by their creator, Chris Sawyer. Somehow this game managed to simulate full theme parks with thousands of agents on the hardware of 1999 without breaking a sweat. An immensely impressive feat, considering that even nowadays a lot of similar building games struggle to hit a consistent framerate.

![](https://larstofus.com/wp-content/uploads/2026/03/image-4.png?w=1024)

So how did Chris Sawyer manage to achieve this?

There are a lot of answers to this question, some of them small and focused, some broad and impactful. The one which is mentioned first in most articles is the fact that the game was written in the low-level language Assembly, which, especially at the time of the game’s development, allowed him to write more performant programs than if he had used other high-level languages like C or C++.

Coding in Assembly had been the standard for game development for a long time but at this point in time was basically a given-up practice. Even the first Doom, which was released six years earlier, was already mostly written in C with only a few parts written in Assembly, and nobody would argue that Doom was in any way an unoptimized game.

It’s hard to check for sure, but it’s likely that RCT was the last big game developed in this way. How big the performance impact was at the time is hard to quantify, but for what it’s worth, it was probably higher than it would be nowadays. Compilers have gotten much better at optimizing high-level code, and many optimizations that you’d need to do manually back then can be handled by compilers nowadays.

But besides the use of assembly, the code of RCT was aggressively optimized. How do we know this if the source code has never been released? We have something that’s almost as good: A 100% compatible re-implementation of it, [OpenRCT2](https://openrct2.io/).

![](https://larstofus.com/wp-content/uploads/2026/03/image-5.png?w=300)

Written by (very) dedicated fans, OpenRCT2 manages to reimplement the entirety of RollerCoaster 1&2, using the original assets. Even though this is NOT the original source code, especially in its earlier versions, this re-implementation is a very, very close match to the original, being based on years of reverse engineering. Note that by now, OpenRCT2 contains more and more improvements over the original code. I’ll note some of those changes as we come across them.

Also, I won’t go through all optimizations, but I will pick some examples, just to illustrate that every part of the game was optimized to the brink.

Types of Money
--------------

How would you store a money value in a game? You would probably start by thinking about the highest possible money value you might need in the game and choose a data type based on that. Chris Sawyer apparently did the same thing, but in a more fine-grained way.

![](https://larstofus.com/wp-content/uploads/2026/03/image.png?w=554)

Different money values in the code use different data types, based on what the highest expected value at that point is. The variable that stores the overall park value, for example, uses 4 bytes since the overall park value is expected to use quite high numbers. But the adjustable price of a shop item? This requires a far lower number range, so the game uses only one byte to store it. Note that this is one of the optimizations that has been removed in OpenRCT2, which changed all occurrences to a simple 8-byte variable, since on modern CPUs it doesn’t make a performance difference anymore.

Replacing math operations with bitshifting
------------------------------------------

When reading through OpenRCT2’s source, there is a common syntax that you rarely see in modern code, lines like this:

Thanks to operator overloading, the ‘<<’ operator can mean a lot of things in C++. What the line effectively does is the same as what most coders would write like this:

What the ‘<<’ operator does here is called bit shifting, meaning all the bits that store the value of the variable are shifted to the left, in this case by two positions, with the new digits being filled in with zeros. Since the number is stored in a binary system, every shift to the left means the number is doubled.

At first this sounds like a strange technical obscurity, but when multiplying numbers in the decimal system we basically do the same. When you multiply 57 \* 10, do you actually ‘calculate’ the multiplication? Or do you just append a 0 to the 57? It’s the same principle just with a different numerical system.

The same trick can also be used for the other direction to save a division:

This is basically the same as

RCT does this trick all the time, and even in its OpenRCT2 version, this syntax hasn’t been changed, since compilers won’t always do this optimization for you.

(Note: I got a lot of notes and comments about this optimization being pointless, since modern compilers do those bitshifts automatically. While this is true for most modern compilers nowadays, it’s not done reliably, depending on your settings. MSVC seems to skip it if optimizations are off, and I could even get an unoptimized result from a slightly older clang-version. That’s probably the reason OpenRCT2 still does bitshifting manually.)

The even more interesting point about those calculations, however, is how often the code is able to do this. Obviously, bit shifting can only be done for multiplications and divisions involving a power of two, like 2, 4, 8, 16, etc. The fact that it is done that often indicates that the in-game formulas were specifically designed to stick to those numbers wherever possible, which in most modern development workflows is basically an impossibility. Imagine a programmer asking a game designer if they could change their formula to use an 8 instead of a 9.5 because it is a number that the CPU prefers to calculate with. There is a very good argument to be made that a game designer should never have to worry about the runtime performance characteristics of binary arithmetic in their life, that’s a fate reserved for programmers. Luckily, in the case of RCT the game designer and the programmer of the game are the same person, which also offers a good transition to the third big optimization:

Game Design for Performance
---------------------------

RCT was never a pure one-man-project, even though it is often described as one. All the graphics of the game and its add-ons, for example, were created by Simon Foster, while the sound was the responsibility of Allister Brimble.

But it’s probably correct to call it a Chris Sawyer Game, who was the main programmer and only game designer in unison.

This overlap in roles enables some profound optimizations, by not only designing the game based on the expected game experience, but also informed by the performance characteristics of those design decisions.

One great example for this is the pathfinding used in the game. When writing a game design document for a park building game, it’s very easy to design a solution in which guests first decide on which attraction they want to visit (based on the ride preferences of the individual guest), and then walk over to their chosen attraction.

![](https://larstofus.com/wp-content/uploads/2026/03/image-9.png?w=1024)

From a tech point of view, this design, however, is basically a worst case scenario. Pathfinding is an expensive task, and running it for potentially thousands of agents at the same time is a daunting prospect, even on modern machines.

That’s probably why the guest behavior in RCT works fundamentally different. Instead of choosing a ride to visit and then finding a path to it, the guests in RCT walk around the park, basically blind, waiting to stumble over an interesting ride by accident. They follow the current path, not thinking about rides or needs at all. When reaching a junction, they will select a new walking direction almost randomly, only using a very small set of extra rules to avoid dead ends, etc.

This “shortcoming” is actually easy to spot in the game, when following a guest around the park for a while. They don’t walk anywhere on purpose, even when complaining about hunger and thirst, they wouldn’t think of looking for the nearest food stall, they just continue until they randomly walk by a food stall.

This doesn’t mean that RCT doesn’t do any pathfinding at all; there are cases where a traditional pathfinder is used. For example, if a mechanic needs to reach a broken ride or a guest wants to reach the park exit, those cases still require traditional, and therefore expensive, pathfinding.

But even for those cases, RCT has some safety nets installed to avoid framespikes. Most importantly, the pathfinder has a built-in limit on how far it is allowed to traverse the path network for an individual path request. If no path has been found before hitting this limit, the pathfinder is allowed to cancel the search and return a failure as result. As a player, you can actually see the pathfinder failures in real-time by reading the guest thoughts:

![](https://larstofus.com/wp-content/uploads/2026/03/image-7.png?w=436)

Yep, every time a park guest complains about not being able to find the exit, this is basically the Pathfinder telling the game that there might be a path, but for the sake of performance, it won’t continue searching for it.

This part is especially fascinating to me, since it turns an optimization done out of technical necessity into a gameplay feature. Something that can barely happen in “modern” game development, where the roles of coders and game designers are strictly separated. In case of the pathfinding limit, even more game systems were connected to it. By default, the pathfinder is only allowed to traverse the path network up to a depth of 5 junctions, but this limit isn’t set in stone. Mechanics, for example, are seen as more important for the gameplay than normal guests, which is why they are allowed to run the pathfinder with a search limit of 8 junctions.

But even a normal park guest is allowed to run the pathfinder for longer, for example by buying a map of the park, which is sold at the information kiosk.

When searching a path for a guest who bought a map, the pathfinder limit is increased from 5 to 7, making it easier for guests to find the park exit.

Changing the design of a game to improve its performance can seem like a radical step, but if done right, it can result in gains that no amount of careful micro-optimization could ever achieve.

Crowds without traffic jams
---------------------------

Another example of this is how RCT handles overcrowded parks. Congested paths are a common sight in every theme park, and obviously, the game also has to account for them somehow. But the obvious solution, implementing some form of agent collision or avoidance system, would do to the framerate what Kryptonite does to Superman.

![](https://larstofus.com/wp-content/uploads/2026/03/image-8.png?w=849)

The solution, again, is just to bypass the technical challenge altogether. The guests in RCT don’t collide with each other, nor do they try to avoid each other. In practice, even thousands of them can occupy the same path tile:

However, this doesn’t mean that the player doesn’t need to account for overcrowded parks. Even though guests don’t interact with guests around them, they do keep track of them. If too many other guests are close by, this will affect their happiness and trigger a complaint to the player. The outcome for the player is similar, as they still need to plan their layout to avoid too crowded paths, but the calculations needed for this implementation are a magnitude faster to handle.

RCT might have been the “perfect storm” for this specific approach to optimization, but this doesn’t mean that it can’t be done anymore, nowadays. It just means more dialogue between coders and game designers is needed, and often, the courage to say “No” to technical challenges. No matter how much you’d wish to solve them.

If you read my rumblings up to this point, you can follow me at [Mastodon](https://mastodon.gamedev.place/@LarsThiessen), [Bluesky](https://bsky.app/profile/larstofus.bsky.social), or [LinkedIn](https://www.linkedin.com/in/lars-thie%C3%9Fen-a640ba141/), or subscribe to this blog directly below this article. I publish new articles about game programming, Unreal, and game development in general about every month.