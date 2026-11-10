---
title: "Voxile: A ray-traced game made in its own engine and programming language"
url: https://elbowgreasegames.substack.com/p/voxray-games-pushes-major-update
clipped: 2026-06-17 01:36:37
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Voxile: A ray-traced game made in its own engine and programming language](https://elbowgreasegames.substack.com/p/voxray-games-pushes-major-update)

## Digest Summary
None

## Discussion Summary
The comments blend enthusiasm for the technical accomplishments with cautious appraisal of the game itself. Many express excitement about the Lobster language, the creator’s résumé, and the visual quality, noting a desire to try the game and compare its performance to other engines. At the same time, several points question the practical benefits of voxel‑based physics, criticize the game’s reliance on familiar Minecraft‑style mechanics, and highlight the mixed Steam rating, suggesting that technical novelty does not guarantee compelling gameplay. Overall, the tone is optimistic yet measured.

---

## Full Article

Voxile, the co-op, ray traced, micro-voxel, survival-crafting game from VoxRay Games, has just released its largest update yet: THE BUILDER’S UPDATE ([release notes here](https://x.com/voxraygames/status/2026416178697220137?s=20)). You can check out the [Steam demo here](https://store.steampowered.com/app/2803440/Voxile_Demo_Adventure__Survival/) and Voxile is now [40% off on Steam](https://store.steampowered.com/app/2283580/Voxile/) until March 9th.

Keep up with all the latest updates in [VoxRay Games Discord Channel](http://discord.gg/2eSepjKufp).

I first met Wouter van Oortmerssen for lunch in downtown San Francisco in July of 2023. Friends had put his studio on my radar (shout out to Dan Levine and Jeffrey Rosen) so when we connected on LinkedIn, I was excited to arrange an in-person meeting.

I expected to spend the afternoon chatting casually about high-level gamedev and design. I had seen video of Voxile’s high-fidelity, ray traced, global illumination with reflections. So my plan was to ask for a Steam key and then boot it up on my gaming rig when I got home. Instead, Wouter brandished a slender laptop from his backpack (with no wall power outlets in sight) and in seconds, the Voxile demo loaded up and was sustaining high frame rates without jitter in all its high-definition glory.

I climbed up from the tranquil beach to forage in the forest but was violently interrupted by an angry skeleton. After losing substantial health, I smashed him into pieces. As I caught my breath… I realized that the sun was arcing through the sky while all the shadows (even the shadows on the little voxel blades of voxel grass) were dynamically updating in real-time. Soon the sun had set and now the glow of flickering torchlight and phosphorescent mushrooms made the engine even more beautiful.

“Is this Unity or Unreal?” I asked even though I knew I had never seen anything like it before.

“Neither,” Wouter replied. “VoxRay Games uses our own custom engine written in our own custom programming language, [Lobster](https://strlen.com/lobster/).”

Wouter’s accomplished career had driven him to this moment ([just check out his github](https://github.com/aardappel)). There are very few game developers who have the talent, intelligence and fortitude to tackle game development at both the engine and language level. Let’s be clear, before Jai was a twinkle in Jon Blow’s eye: Wouter had invented and helped design ***[nine](https://strlen.com/programming-languages/)*** [languages](https://strlen.com/programming-languages/): Amiga E, FALSE, Bla (created during his Masters in Computer Science), Aardappel (invented during his PHD research), WadC, SHEEP, CubesScript, CryScript and Restructor.

Lobster is Wouter’s tenth language and was built from the ground up to enable prototyping games like Voxile. It amalgamates everything Wouter has learned at companies like: Amiga Inc., Crytek (building the original Cryengine for Far Cry), Maxis (SimCity), Gearbox (Borderlands 2) and Google (where he helped design [Web Assembly](https://webassembly.org/) and ***invented*** [FlatBuffers](https://flatbuffers.dev/) while working on LLVM and Android VR/gaming tech). If you’re technical, I recommend you watch some of Wouter’s lecture videos (linked above and below) to understand just how much Wouter knows about game engine coding and languages.

Wouter also believes in giving back to the greater gamedev ecosystem (something that is really important to EGG and its community). He wants to share his knowledge and his joy for games with others. Beyond all his open source contributions to major projects, he was also one of the creators of [SMU Guildhall](https://www.smu.edu/guildhall), teaching students how to build engine components (such as shader systems, skeletal character animation, scripting compilers) while supervising their Master’s projects. At DICE this year, I watched as a former student, upon seeing his former professor, ran across the room to thank Wouter for teaching him game development and inspiring him to start his successful gamedev career (he is now an executive at a prominent company).

In his spare time, Wouter made the 3D [Cube Engines](http://cubeengine.com/) including [Cube 2/Sauerbraten](http://sauerbraten.org/) with Lee Salzman for Mac, Windows and Linux (now open-sourced with over 1,000,000 downloads). It’s a performant multiplayer, deathmatch engine (like the Quake engine) but also enables real-time, multiplayer, map editing (and this was in the year 2000 almost a decade before Minecraft would make this a core mechanic).

After years of experience, Wouter decided it was time to form VoxRay Games and up-res, voxel-based world crafting. He successfully raised venture capital led by the well-known VC firm Accel. When he offered EGG a chance to join his round, it was a no-brainer for us to participate as well.

Most game engines interact with programming languages similar to the image below.

However, a game engine written in Lobster can be built like following diagram. Unlike Jai, which aims to replace 100% of C++, Wouter’s design paradigm only replaces 90% of it. C++ is still used with Lobster but it’s relegated to the leaf nodes of the call graph.

The result is record-speed compile times even after substantial changes to the code base. Cold start times are generally well under 2 seconds for Voxile. Nine out of ten changes in the VoxRay codebase don’t need to touch the C++ code at all. Most languages have either good static typing and performance or fast startup times but it’s very rare for them to have both. Lobster has both.

Lobster is therefore ideal for fast, iterative prototyping without rigidly confining the user to a particular engine architecture. Wouter himself has been able to quickly craft wildly different game ideas (each with bespoke engines instanced in Lobster) to “find the fun”. [You can check out his many prototype ideas here.](https://strlen.com/game-design-experiments/)

Voxile emerged from this prototyping crucible as the project with the most compelling gameplay and prettiest graphics.

Wouter has explained that his design goals for Voxile involve a growing list of foundational engine features that yield emergent properties:

* 3D Volumetric Worlds: Polygonal meshes are like a hollow shell without substance. Building and destroying are integral parts of Voxile and they are seamless, molecular properties of the entire micro-voxel world. I fondly remember [Red Faction](https://en.wikipedia.org/wiki/Red_Faction) from my childhood but even that was essentially a veneer of polygons used to simulate the destruction of pre-scripted set pieces whereas EVERYTHING in the Voxile world is buildable and destructible.
* Performant Ray Tracing: Dynamic shadows, global illumination, ambient occlusion and reflections are all built in to Voxile’s graphics pipeline and create a wonderful visual style. Art and design workloads are reduced because the engine automatically makes all the voxels look and feel right.
* Co-op Multiplayer: Both world crafting and destruction happen seamlessly and persistently in real-time. This opens the door for group gameplay and modding experiences like you find in Valheim, Minecraft, Helldivers, Peak, and more... For example: a level where you build a fortress with your friends by day before you have to defend it from zombie raiders at night can be trivially constructed in Voxile.
* Quest and Inventory Systems: Wouter has mentioned being heavily inspired by Fallout. Each Voxile world map can offer the player RPG-style quests, progression and upgrades.
* Tactile Combat: Weapons are juicy and responsive. Melee weapons have weight and impact to them while customizable range weapons, guns and explosives (why would Wouter add ***grenades*** to a “Builder’s Update”!?) cause procedural voxel damage. Just like the world, enemies exhibit voxel-based damage modeling. The result is like [Soldier of Fortune](https://en.wikipedia.org/wiki/Soldier_of_Fortune_(video_game))’s visceral damage system.
* UGC: The modding potential for Voxile is obvious and expansive. Making custom assets is like playing with Legos.

Just look at the way the look and feel of the game changes dramatically across worlds.

The Crystal Cathedral World

As new worlds get created, the prefabbed assets they contain become recyclable modules for future level design and modding (à la [LittleBIGPlanet](https://en.wikipedia.org/wiki/LittleBigPlanet)).

While Wouter has never publicly stated any plans whatsoever to use AI, it’s clear that with his skill and control over the language, the engine and the game, he could add any number of procedural world generation features to Voxile in the future… stuff that most other gamedevs could only dream of (or at the very least they’d have to submit a feature request ticket to their game engine provider).

In an industry that is hungry for growth and innovation, Wouter has created a full-stack, farm-to-table game technology that is truly one-of-a-kind. Everyone should take a moment to [check out the free Voxile Demo](https://store.steampowered.com/app/2803440/Voxile_Demo_Adventure__Survival/) and if you like the content or want a rich sandbox to mod your own worlds in… you should consider supporting his studio by [buying the game on Steam now for 40% off](https://store.steampowered.com/app/2283580/Voxile/). You can join the public [VoxRay Games Discord channel](https://discord.gg/2eSepjKufp) to keep tabs on their latest news. Wouter, congrats again on The Builder’s Update! EGG is excited by what you have built and to go on this journey with you.