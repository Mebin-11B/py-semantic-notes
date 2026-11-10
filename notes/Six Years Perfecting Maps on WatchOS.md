---
title: "Six Years Perfecting Maps on WatchOS"
url: https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/
clipped: 2026-06-17 01:08:45
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - watchos app design
  - swiftui mapping engine
  - mobile cartography
  - offline navigation
  - apple watch development
  - liquid glass ui
related:
  - "[[watchOS App Design]]"
  - "[[SwiftUI Mapping Engine]]"
  - "[[Offline Navigation]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Developer David Smith shares his six-year journey of engineering and designing a custom, SwiftUI-native mapping engine and user interface for the Apple Watch app Pedometer++.
>
> **Key points:**
> - The developer chose to build a custom SwiftUI map rendering engine instead of using Apple's MapKit, avoiding MapKit's dark mode constraint, overlay limitations, and lack of detailed topographic maps.
> - Transitioning from slow server-generated tiles to local SwiftUI rendering enabled robust offline navigation for wilderness adventurers.
> - To complement watchOS 26's Liquid Glass UI layering, a custom basemap with high contrast and dark mode variants was commissioned from cartographer Andy Allen.
> - The final design features a vertical stack layout with metrics in the top-left, requiring a tap to enter "browse mode" for panning and zooming.
>
> **Concept links:** [[watchOS App Design]], [[SwiftUI Mapping Engine]], [[Mobile Cartography]], [[Offline Navigation]], [[Apple Watch Development]], [[Liquid Glass UI]]
>
> **Suggested connections:**
> - [[watchOS App Design]] — rules and challenges of designing functional user interfaces for very small screens.
> - [[SwiftUI Mapping Engine]] — building custom map rendering frameworks in Apple's SwiftUI.
> - [[Offline Navigation]] — designing applications that function reliably without cell signal or network connectivity.
<!-- ai-summary:end -->


# [Six Years Perfecting Maps on WatchOS](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/)

## Digest Summary
- Since the Apple Watch’s launch, the developer spent six years creating a native watchOS mapping experience for the Pedometer++ app.  
- Early versions relied on server‑generated tiles and required a network round‑trip, which was unsuitable for offline navigation.  
- In 2021 a fully SwiftUI‑based map rendering engine was built, enabling performant tile‑based maps and overlay of location data directly on the watch.  
- Multiple UI concepts were trialed to balance map interaction with workout metrics on the limited screen; the final layout uses a modal approach with metrics in the top‑left and the map as the primary page, entered by a tap to “browse mode.”  
- With watchOS 26’s Liquid Glass, a custom basemap was commissioned from cartographer Andy Allen, optimized for contrast, saturation, and a dark‑mode variant to maintain legibility under glassy layers.  
- The design was refined with designer Rafa Conde, leading to the shipped version praised for readability and native feel.  
- The author avoids Apple’s MapKit on watchOS because it forces dark mode, limits animation/overlay control, and lacks detailed topographic coverage required for the app’s use cases.

## Discussion Summary
Comments express disappointment that Apple Watch lacks a first‑party hiking or topographic map and GPX import, viewing this as a notable shortfall even on premium models. Third‑party solutions such as custom static‑tile maps and pedometer apps are praised for detail and engineering, though concerns arise about subscription transparency and occasional UI bugs. Users note Apple Maps’ watch implementation can be intrusive during workouts and suffer reliability issues, leading some to prefer alternative devices like Garmin while still appreciating the effort behind the independent apps.

---

## Full Article

![Cloughhead](https://fast.crossforward.com/resources/cloughhead.jpeg)

I love going on wilderness adventures. I am rarely happier than when I am far off into the mountains without a soul in sight. As a result, I have spent a lot of time learning how to safely explore and navigate when Iâm away from civilization. The most important habit Iâve found for not getting lost is to be *very* regular in checking your location as you go, and the best way Iâve found to do that is to have a map on my wrist.

![Pedometer++](https://fast.crossforward.com/resources/hero-map-transformation.png)

For more than **six** years Iâve been working towards creating the best possible mapping experience on the Apple Watch. With yesterdayâs [launch of Pedometer++ 8](https://david-smith.org/blog/2026/04/28/pedometer-v8/), I feel like this design journey has reached a meaningful destination. I would contend that Pedometer++âs watchOS mapping support is the absolute best available on the App Store.

So I wanted to walk through the journey it took to get here.

### Early Efforts

I have wanted a good map on my wrist since the Apple Watch launched. This wasnât realistically possible until watchOS 6, which brought SwiftUI to the platform and, for the first time, made *ârealâ* apps possible. But in those early days, the screens were tiny, and the processors slow. I couldnât *quite* get to where I wanted.

![](https://fast.crossforward.com/resources/20200528_server-maps.png)

This was my very first attempt that shipped in Pedometer++. These maps were generated completely on the server, which involved sending the relevant workout data roundtrip every time I wanted to refresh the display. This system let me validate the idea, but it was never going to be practically useful for navigation or regular use, and could never work offline.

### Custom Mapping Engine

I knew that if I wanted to make progress towards this goal, Iâd need to work at a lower level, so I got to work building a fully SwiftUI-native map rendering engine. SwiftUI was the only choice because itâs all that watchOS supported, and proved to be helpful for putting maps into widgets, which also only support SwiftUI.

![](https://fast.crossforward.com/resources/20211122_custom_engine.png)

In 2021, I got this engine to a place where I could reliably and performantly render a map on watchOS. With it, I can render any tile-based maps and overlay location information on top.

### Map Designs

Next came the question of how best to surface data to users. App design on watchOS is a really fun â but frustrating â challenge. You are designing for a relatively tiny screen, which must be operated one-handed. In this case, I want the user to be able to read the map and use it to navigate, while also having access to other workout-related information.

This began a long series of design attempts, most of which (if Iâm being honest) were kinda awful.

![Bad designs](https://fast.crossforward.com/resources/bad_designs.png)

In the end, I settled on a âmodalâ approach where the user can switch between a map screen and a metrics screen using a button on the top-left corner.

![Modal Maps](https://fast.crossforward.com/resources/modal-maps.png)

This interface provides one context where the user can freely pan/zoom around the map and another where I can use the more standard watchOS tabbed page interface for metrics and controls. I shipped this to Pedometer++, but there was always something that didnât quite sit right with me about it.

This design felt like a compromise, and not in a good way. I felt that in order to achieve the goal of making the map interactive, I couldnât have the map be part of any UI structure that involved swipes. As the screens on Apple Watches got larger, it felt less needed in order to give the map enough space to be useful.

So I set about trying alternative designs. **SO** many designs.

![Many more designs](https://fast.crossforward.com/resources/loads_of_designs.png)

For a while, I thought that I needed to find a way to put the metrics at the bottom of the screen. However, that would lead to other problems on longer outings or for workouts that arenât navigation-focused. So I kept iterating and came up with even *more* designs.

![Even more designs](https://fast.crossforward.com/resources/more-and-more-designs.png)

All of these designs suffered from the same fundamental issue: they required the app to display only a fixed set of fields at a time.

I could make the interface configurable, but one of the *fundamental* rules of watchOS design is that you should avoid any interaction that takes more than a few seconds on the watch. Any user-configurable setup is inherently fiddly, so I didnât like this approach.

### Dark Mode, Liquid Glass, & Cartography

Around the same time I was still wrestling with the design challenges of how best to structure the app, Apple announced watchOS 26, and the arrival of [Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/liquid-glass#Introduction-to-Liquid-Glass). One of the core design aspects of Liquid Glass is layering stacking elements on top of each other, but another is the types of colors that work best with each other.

I was previously using [Thunderforest Outdoors](https://www.thunderforest.com/maps/outdoors/) as my basemap for the app. I love the content this map includes, but when I started overlaying glassy elements over it I found that it wasnât well-suited for Liquid Glass.

Soâ¦ I commissioned a custom map. Working with the incredible cartographer [Andy Allan](https://www.thunderforest.com/custom/), we created a completely new basemap that would look fantastic with Liquid Glass.

![](https://fast.crossforward.com/resources/thunderforest-light.png)

We simplified the map visually, increased the contrast of the elements, and made the map elements more saturated to prevent them from becoming a muddy mess when shown below glass.

With this work done, I had another opportunity: I could finally have a dark mode variant of the map tiles. While helpful on iOS, this really shines on watchOS. Andy and I really worked toward something which would be incredibly legible at armâs length.

![](https://fast.crossforward.com/resources/thunderforest-dark.png)

The result of these efforts is that now I have a great map for watchOSâ¦ but a design that didnât match that greatness.

![](https://fast.crossforward.com/resources/20250911_dark-old-design.png)

### Striving for Great

I kept trying. To get me out of my design rut, I enlisted the help of the fantastic designer [Rafa Conde](https://rafa.design/). I needed a fresh set of eyes on this and very quickly, this partnership paid off. They proposed a variety of alternative layouts, but when I saw this one I *knew* it was **the one**.

![](https://fast.crossforward.com/resources/raffa-map.png)

The layering of the metrics on the top-left corner, with the map being the top page of a vertical stack, was the correct answer. This design handles interactivity by requiring a tap on the map first to enter âbrowse modeâ.

### Tweaking and Polishing

Now that I had the overall concept locked in, the real fun began, actually building the app and dialing in all the details. I fairly quickly took Rafaâs concept and turned it into a working prototype. This let me validate the idea in the fieldâ¦ literally. After walking a few hundred miles with it, I was confident it was the correct approach.

![](https://fast.crossforward.com/resources/20260210_first-shot.png)

Next, I needed to dial in the font and make more subtle design choices.

![Map fonts](https://fast.crossforward.com/resources/map-fonts.png)

After a bit more iteration, I arrived at the design that shipped yesterday. It is legible, useful, and (in my humble opinion) beautiful.

![](https://fast.crossforward.com/resources/finished-map.png)

It feels really good to be able to cap off this six-year journey with a design I couldnât be more proud of. This screen represents so much accumulated effort and learning. It finally gives me a design which feels native on the platform, but also novel and unique.

Here is the evolution of this design over the last six years:

![](https://fast.crossforward.com/resources/map-evolve-white-small.gif)

### Postscript: Considering MapKit

While my work on watchOS mapping massively predates the arrival of Appleâs MapKit onto the platform, it is probably worth explaining why I decided to do all of this custom work to avoid using it.

Fundamentally, I find that MapKit is great for *basic* uses, but doesnât provide nearly the level of configurability and utility which I want Pedometer++ to offer. For example:

* MapKit on watchOS always shows in dark mode, which generally is a good default, but closes the door on some accessibility and user choice reasons. I needed it to be a user-selectable option.
* While MapKit on watchOS has gotten better over time in terms of what you can do with it, I still find it a bit limiting in terms of animations and overlays.
* MapKitâs coverage is improving with regards to topographic contours and trail marking, but there are far too many places where the MapKit map is essentially blank, but I know there should be more rich details available. For example, here is my map vs MapKit at the trailhead of one of my favorite hikes in Scotland.

![MapKit comparision](https://fast.crossforward.com/resources/mapkit-comparison.png)