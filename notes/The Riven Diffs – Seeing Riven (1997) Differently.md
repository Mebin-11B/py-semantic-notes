---
title: "The Riven Diffs – Seeing Riven (1997) Differently"
url: https://glthr.com/the-riven-diffs-1
clipped: 2026-06-17 02:04:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Riven Diffs – Seeing Riven (1997) Differently](https://glthr.com/the-riven-diffs-1)

## Digest Summary
None

## Discussion Summary
Comments express overall appreciation for the site’s content and its deep‑dive nature, describing it as neat, wonderful, and a pleasant find. Readers note a desire to postpone reading to avoid spoilers from a related game. There is a factual observation that the page’s update year (2026) makes the original 1997 title seem misleading, and a brief notice that one link appears dead. The tone is largely positive with minor technical remarks.

---

## Full Article

*This article, by* *Guillaume Lethuillier* *and* *Twitch*, [*is also published on Twitch’s website*](https://inkbeetle.com/rivendiffs/) *(which contains additional images by combining animated diffs, highlighted diffs, and pairs of original images).*

*Disclaimer: This article contains spoilers applicable to both versions of Riven.*

Just how stable is [Riven](https://en.wikipedia.org/wiki/Riven)? It is well known that Gehn’s unorthodox writing methods invariably produced ages that eventually fell apart, and Riven in particular is demonstrably close to its inevitable collapse. But do we see any symptoms of this in-game? Besides the endings, Riven appears perfectly normal to an untrained eye. But what if we look closer? What if there are anomalies in plain sight that we simply never noticed before?

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434014892/72d3f8f4-1c90-4559-b8b8-4fb6246ae94f.gif)

While Myst relied on the interpreted HyperCard engine, Riven uses the Mohawk engine instead. Conceptually, Myst operates on a simple one-view-per-card model where each image represents fixed render states (see [our previous articles](https://glthr.com/myst-graph)). In contrast, Riven’s Mohawk engine allows for dynamic changes within nodes by enabling multiple rendered views to coexist on the same card, with the engine displaying the appropriate render based on the current state of the game world. In short, where Myst’s cards represent static views, Riven’s cards can represent multiple different versions of the same viewpoint. This discovery led us to develop an exploration tool, the “Riven Explorer”, that allows for side-by-side comparison of these renders. Where the Myst Graph revealed development insights through *card* *relationships*, the Riven Explorer uncovers them through *visual* *differences*.

Since renders took significant amounts of time in the 90s, and different worldstates were often rendered at different stages in development, many renders have subtle differences beyond the changes caused directly by the player. Most of these are virtually impossible to notice due to the worldstate changes being evoked in separate locations from where the actual differences are visible. But when you compare card differences in-place, changing the worldstate without moving the camera, they can become much more obvious. Many differences are subtle, and are virtually impossible to notice without the use of direct comparisons. But with such tools, it reveals many places where tweaks to the 3D scene were made between renders, resulting in changes to the world far beyond the changes being made by the player.

The tool, evoked in [this article](https://glthr.com/riven-navigator), provides a methodical way to analyze the unique differences between images composing a given card. For instance, when a card contains three images (A, B, and C), the explorer generates three unique comparative analyses: A versus B, A versus C, and B versus C. These differential comparisons, that we call “diffs”, are visualized through two complementary modes:

* **Pixel differential rendering**: By default, the tool combines both images into a black-and-white composite, with red pixels highlighting mismatches between the two views. In many cases, the differences visible here will be caused by changes to the dithering or the color table, resulting in false positives, but quite often it can highlight small but very real changes that would otherwise be hard to spot.
* **Animated comparison**: Reviewers can toggle a rapid succession mode that alternates between the two images (similar to an animated GIF), making differences easily visible as points of motion in an image that is otherwise mostly unchanged.

Typically, a card will have multiple diffs. The number of differences follows [the triangular number sequence](https://en.wikipedia.org/wiki/Triangular_number): 1 render produces 0 diffs; 2 renders produce 1 diff; 3 renders, 3 diffs; 4 renders, 6; 5 renders, 10; and so on (sequence [A000217](https://oeis.org/A000217) on OEIS).

**Example of the tool in action**

**Example of pixel highlighting: the spider chair activated/deactivated, from Temple Island, card T11**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434249466/3084e18e-ffe3-43c0-a12f-6ef83f1f0a8d.png)

**The same diff, as an animation**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434285072/6af46eb6-4823-4188-9e2f-d7ea3454db08.gif)

We then began systematically examining these differences, expecting to find rendering glitches tied to game logic. This was a fun and almost philosophical experience: we actualized different moments in time from the same place, without having to move around to change the worldstate. It is like wearing magic glasses that represent the same location from different points in time. This article, and the follow-up articles to come, explore these findings in depth.

We use the following terminology throughout these articles:

* **ANOMALY**: An “anomaly” is a visible rendering quirk. These can be caused by many things, including changes to the underlying world geometry that occurred between renders, mismatched splices, or other errors. Many anomalies are visible from multiple cards. Many anomalies require specific worldstates in order to be visible.
* **CARD**: Anywhere the player can stand is a “[card](http://insidethelink.ortiche.net/wiki/index.php/Riven_engine_overview)”. A card can have many renders assigned to it depending on how many different worldstates are visible from any given spot. Walking or turning moves between cards, but different versions of one spot will share the same card.

  We label cards with a letter and a number. The number corresponds with the number of the card. However, different islands can share numbers, so we prefix each card label with a letter corresponding to the island’s label within the datafiles: B for Boiler, G for Survey (“garden”), J for Jungle, O for 233rd (“office”), P for Prison, R for Tay (“rebel”), and T for Temple. For example, card J127 (pictured at the top of this article) refers to card 127 within Jungle Island. These card numbers also correspond with the beginning of the filenames produced by the asset extraction tool [Riveal](https://archive.org/details/Riveal11.1) by Ron Hayter, which was used heavily in the research and preparation of these articles.

  *Note: some card numbers change between versions and languages. The numbers in this article are based on the 1.2 version from the English 10th Anniversary DVD. If you’re using a CD release or searching for assets dubbed into a different language, the cards may be numbered differently, but we haven’t found any differences in the actual content of the renders yet.*
* **WORLDSTATE**: The “worldstate” refers to the state of all the player-actionable things, such as the position of a lever or an elevator. Whenever the player performs an action or the story progresses, the worldstate changes.
* **PATCH**: A “patch” refers to a smaller picture or video that is placed on top of the background image in real-time by the engine. Patches are often used in places where many different worldstates are visible, to prevent the need for a huge number of renders covering every possible configuration. Patches are also used for the large number of very small videos that don’t cover the entire screen, such as when a spinning dome is visible in the distance. Patches are always rectangular, and are stored as separate images/videos within the datafiles, to be overlaid in real-time within the game.
* **SPLICE**: A “splice” refers to when the image data of a render has been copied from another image or another render. These are sometimes used when only part of an image needs to be re-rendered, but a patch would not be appropriate or desirable for whatever reason. Splices are edits which exist within the finished render itself, and are not separate files like patches are.
* **FMV**: An acronym for “full motion video”, referring to the many videos used throughout the game. Almost anytime you see motion, it’s an FMV. (Rare exceptions include the water rippling effects all over the game, and the various miniscule flying bugs that appear in places like Jungle Island.)
* **OCCLUSION**: In computer graphics, "occlusion" refers to when one object blocks vision to another object. When one object is in the foreground and blocking another object in the background, the background object is "occluded" by the foreground object. Several anomalies involve objects blocking one another in ways that are incorrect based on where they actually exist in 3d space; these are problems with occlusion.

**An example of a "Splice": the rectangular edges are easily visible in the differential comparison of J191**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434415907/1da5c2dd-0338-4471-956f-fbb583305a46.png)

Part 1: Jungle Island
=====================

Jungle Island is a location very familiar to many of us, but it has a large variety of anomalies, making it suitable as our first point of examination.

Several anomalies are associated with the state of the spinning dome (this is a recurring theme- every single spinning dome in the game has anomalies.) In cards J121, J124, J133, J154, and J421, the two semicircular “hinges” that sit at the base of the dome are occluded incorrectly, making them fully or partially obstructed by other geometry depending on whether or not the dome is flipped. In J124, you can also see the hinge switch from high to low polygon count.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434461513/b3f129f9-4e1b-41b3-a634-c3d28b308cb8.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434468759/1f870497-6591-4a17-8c82-25e14c1df32a.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434477575/7e7a2efb-9c3f-43c8-a4d3-c37f36737c01.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434487079/f1033b0c-53db-4da9-8a17-9042aec6b5e6.gif)

In card J130, the base of the dome visibly moves when the dome is flipped.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434511774/c14cf552-c3a1-47a8-9e16-4b83eca5e384.gif)

Card J154 is also the location of one of the Spyder easter egg renders. A direct comparison with a normal J154 card reveals that the camera is in a different spot. Also, the furthest of the spherical lamps in the easter egg has been raised/lit like many of the others along this walkway.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434525544/28d7dd7a-abfe-48fa-828f-d31874ed0289.gif)

In cards J110, J119, and J127, the foliage changes (quite drastically in J127) when the dome is flipped. J119 also has some leaves incorrectly occluded by parts of the dome when closed.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434542265/710ba59e-8103-40b2-9c77-594294b2aac9.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434549431/5fe5ed75-5f31-4881-bfa9-349058ea0b93.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434559299/5d24b53a-ab7c-42e9-ac27-3870ebc6963e.gif)

At the top of the wahrk gallows, in cards J178 or J264, the doorjamb to the prison changes depending on whether the door is open or closed. In card J264 the entire jamb changes, and in J178 the differential comparison makes it obvious where the images were spliced around the jamb.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767481033869/f968370a-a855-46ce-8520-33d8354179f5.png)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434579145/932fb096-c1a7-4e48-978b-b93a99e4cae3.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434589249/b424d117-c8e4-4355-904b-1105518f29f0.gif)

There are two patches applied when you’re standing in card J181, one for the submarine and one for submarine dock 5 (the schoolhouse).

When the submarine is raised out of the water, the submarine overlaps the railing in the foreground of J181.

Furthermore, there is a patch that shows dock 5 extended, which is correctly used to show an extended dock 5 in J181 when the prison door is open. However, the render of the closed prison door *already* has an extended dock 5, and there is no patch to show it retracted. As a result, if you retract dock 5 before opening the prison door, you can see the schoolhouse dock retract the moment the prison door finishes its opening FMV.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434619915/1591d57a-c93f-4f16-9731-05c82131f565.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434625015/adcae7eb-3b07-4d4b-ae50-081a59e68fc6.gif)

Inside the tunnels, differential comparison revealed a render that seems out of place. If you turn on exactly 3 of the lights in the tunnel, when you’re walking back towards the ocean, there is one render assigned to card J194 that’s actually a render from the perspective of J196. In the differentials, this looks like the tunnel changing shape between worldstates. In-game, this makes it seem like one of the steps towards the ocean darkens the lighting without moving forward at all. The incorrect render may be from earlier in development, as it has noticeably egregious banding on the dim/gray parts of the image, which isn’t a problem on the correct version visible from J196, or anywhere else in the tunnel. It’s likely card J194 should be completely black when 3 lights are on, as it’s barely lit (with a correct render) with 4 lights on.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434642412/dfe476de-6f1a-431a-a6c6-d85654bacd50.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434647418/c9583a8e-a262-4b86-b49e-2a124abc9259.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434654352/380358c2-2c2c-4593-bb06-c4be219f3698.gif)

Each of the 25 totems in the Tay book room can be raised or lowered individually. When you’re standing in the center of the room, individual image patches are used to allow arbitrary totems to be shown in the downwards state, and renders with Tay unlocked are made with the correct totems already lowered. However, the zoomed-in views on almost all of the 25 totems have *all* of the totems in the same state as the totem you’re currently zoomed in on. *(Exceptions: J217 and J225)*

Two anomalies are visible as a result: Firstly, and more obviously, when zoomed in on a totem, the visible edges of the 2 adjacent totems will be raised or lowered based on the state of the totem you’re currently zoomed in on. Secondly, in many of the totem views, a reflection of the room is visible on the water, which shows every other totem in the room raised or lowered in the reflection.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767481074206/13ba4a2a-b810-435a-b422-5629958772f3.png)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434692042/36145d0b-4720-425c-95f7-e7a582bdde02.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434684233/21635ce4-84a0-4b26-8e04-940fdabb5661.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434705080/4f82b9d0-943e-46d3-b4b0-b2df823fd949.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434701064/60b1dca7-00e0-4ba8-a352-1ae627db0535.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434707448/ccc5c504-590e-4182-9a3b-cad179706a1d.gif)

Also, for some reason, a few of the totem renders have bright blue pixels on the extreme right or left side:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434760979/86dc14d3-2fb3-4572-83f1-b55d3be8f3c1.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434767037/cdf0f4fe-148e-4ecf-8191-2c4374873da6.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434774842/4eea45e3-900f-4b0d-9eda-161a8c61e78e.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434781479/a6f0c9e9-ff5e-4e34-8217-0ed34a5e97dc.gif)

Furthermore, there are some changes to the lighting that occur. A shadow changes visibly in card J241 based on the totem state. In cards J211 and J213, all of the shadows cast by the totems disappear when the Tay book is unlocked.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434855383/c1572943-23b2-47c4-ae36-c6555834a104.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434861988/6c1d8942-2943-4ca0-be7c-ae255689f25f.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434864850/4a233dc3-c287-4401-a00f-61e0fa3324bc.gif)

At the big wahrk head staircase, at card J375, some bright white bits in the jungle disappear when the wahrk is open.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434910225/1276e2a2-c56c-4bbd-b911-266134f32eb7.gif)

Also, the angle of the camera in card J381 changes when the wahrk is open. Some foliage also changes, and the lighting overall becomes slightly brighter.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435264067/18965bf5-b58f-47fc-9e07-79b1da1c8522.gif)

At the maglev leading to Temple island, at card J806, the rocks on the far left are different based on whether or not the maglev is present or missing. Also, some of the details on the concrete are slightly moved.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434933578/03ee5371-0824-4079-8bf3-fcc79858d5d2.gif)

A few anomalies are present based on whether or not the sunners are present. In card J620, the rocks on the right change when the sunners are absent. Furthermore, in cards J620, J626, and J628, the horizon changes visibly based on the presence of the sunners. (In card J628, the mismatched horizon is only present if you enter the node while the sunners are awake/startled, probably to match the FMV).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434954149/65cee207-f3c6-4961-b54a-0ec72c263456.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434959744/467b08ab-1765-4bd2-88e4-7cd42ed43a9f.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434964419/41edef15-9aab-43cd-873b-4830eae1e091.gif)

In card J526, the shape of the background mountains change to match the FMV when you open the submarine hatch.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767434992469/106a4dc2-273d-4619-b9e5-44b0a2f3b323.gif)

In card J296, if dock 4 is retracted, a red spot appears on the rocks when the submarine is turned around. It also appears some of the rocks change, but it’s unclear which of these changes are just reflections of the submarine.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435006229/ec6639e2-3924-47e1-95a1-2ba762d46f97.gif)

In card J449, when the gallows shortcut ladder is still raised, submarine dock 2 will be completely missing when retracted (The extended dock is shown using a patch.) Furthermore, when dock 2 is visible in any worldstate, it becomes apparent that the submarine dock is on the wrong side of the walkway, a quirk also visible in J447.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435022563/88ca5bb4-3894-4ee7-bfa4-ddb41224cad4.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435057915/7bf63cb8-cba5-4a44-ad9c-53499e02cf56.png)

In cards J468, J470, J476, and J581, the diffs reveal that the shortcut ladder isn’t actually raised, the bottom half has merely been erased. Card J334 clearly shows that the ladder should be visible when raised.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767481128643/81211f71-1940-4066-8801-36f04fd80f5e.png)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435087378/c338f0e7-ab1c-47d8-8634-dd28d2973a84.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435102765/ea0d6de7-344a-480a-9ab0-c927ef5abe9d.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435109805/23772fa6-1eab-47c4-9575-360debade9d3.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435125051/dc1dc169-4c61-4fa2-8c75-79ff756ddbed.gif)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767553020211/419641c3-1566-481a-a136-87eb7b4d0107.gif)

Finally, in card J459, a detached shadow probably belonging to the shortcut ladder is visible on the leftmost cliffside at all times.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1767435166151/4de750d0-f86c-4d81-8469-e3039525bedc.gif)

Additional articles authored by Twitch are on their way, covering the large number of anomalies we have discovered across the entire game.