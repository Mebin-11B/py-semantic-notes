---
title: "Updating Gun Rocket through 10 years of Unity Engine"
url: https://jackpritz.com/blog/updating-gun-rocket-through-10-years-of-unity-engine
clipped: 2026-06-17 01:15:14
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Updating Gun Rocket through 10 years of Unity Engine](https://jackpritz.com/blog/updating-gun-rocket-through-10-years-of-unity-engine)

## Digest Summary
Gun Rocket, originally created about a decade ago, was developed in Unity 4.6.0p1 (2015) and later migrated to Unity 5.5.0f3 (2018). The project’s version file confirms the latest editor version as 5.5.0f3, though Unity’s versioning scheme has shifted from simple numbers to year-based and now to high‑range numeric identifiers (e.g., 6000.4.1f1). Unity Hub lists only recent releases and pre‑releases, requiring access to the archive for older versions; the archive includes Unity 5 but not 4.6. Attempts to open the project in Unity 5.5.0f3 or 5.6.7f1 result in immediate closure with no log output, likely due to legacy license checks predating Unity Hub. The author plans to update the game for 2026, necessitating retrieval of a compatible Unity editor from the archive and addressing potential licensing or compatibility issues before proceeding with migration.

## Discussion Summary
Comments express skepticism toward Unity’s development, noting limited updates stem from a lack of significant releases rather than strong backward compatibility, and cite DOTS as still unready for production as shown by recent titles. There is curiosity about building a 3D shooter without a mainstream engine, with suggestions to use C++ libraries for graphics, physics, and networking. Opinions on UI themes diverge, with some dismissing dark mode as unnecessary while others argue it reduces eye strain for evening hobbyists. Writing style receives praise.

---

## Full Article

About 10 years ago I made [Gun Rocket](https://store.steampowered.com/app/391420/Gun_Rocket/).

It was early in my game development journey. I had released 5 prototype games on Game Jolt, and it was time to sit down and make something worth paying for. I started with the idea "What if [n++](https://store.steampowered.com/app/230270/N_NPLUSPLUS/)...but with the Asteroids ship?"

Development took about a month. The result was a game with 100 levels, multiple ships with different stats to pilot, and even a LAN multiplayer combat mode. Gun Rocket also stands out as my most lucrative personal project. After a successful Steam Greenlight process I was approached and licensed the Steam distribution rights for the game for a few years.

Recently I was reflecting on my game development journey. I tried to boot up Gun Rocket to play it. But it refused. No matter how hard I clicked the game would not open. The log is empty. I guess some driver or Windows API just doesn't work anymore.

So it is time to roll up my sleeves and bring Gun Rocket into 2026. Come along won't you? I could use the company.

Gun Rocket won't launch. What to do?
====================================

Let's start by opening the game in Unity Editor. We'll test the game in its current editor version and re-acquaint ourselves here before moving on. The version of a Unity project is stored in /ProjectSettings/ProjectVersion.txt. It's a simple file with a simple purpose. Here's what I see:

m\_EditorVersion: 5.5.0f3

Looking back at the git history of this file, I can see that I actually developed the game in 4.6.0p1 in 2015. The ProjectVersion file was created when migrating from 4.6 to 5.5 in 2018 hoping it would fix a bug (it didn’t). So there's our first interesting factoid about how Unity has changed. Crazy how time flies.

Anyway! Looks like Gun Rocket was most recently developed in Unity 5.5.0f3. The current Unity tech stream is 6.5 beta. That doesn't seem so bad! Just one major version bump, right?

WRONG!

Some time around 2017, Unity decided that its numbering was not corporate-friendly. At that time they were trying to expand from gaming into more verticals. I guess corporations love versioning their software by year, so that's what Unity did. It makes the messaging about long-term support easier. Let's say Unity supports a release for 3 years. When does that end? It's much easier to talk about that for Unity 2017 (2017 + 3 = 2020) than for Unity 5.5 (???).

Nowadays Unity is back to simple numbers. Today’s major version number is 6. At least...that's what the website says. Unity version numbers now look something like 6000.4.1f1. I find this hilarious. It reminds me of Loony Tunes technology naming. Roadrunner Catcher 3000 anyone? Again, there is a good reason for this. 6000 > 2023. 2023 is Unity's last year-named version. So all of the version sorting code will continue to Just Work TM. A Good Reason. But I still find it funny.

So I open Unity Hub and look for 5.5.0f3. It's not one of the readily available options. Unity presents Official Releases (long-term support and the latest supported minor release 6000.4.1f1), Pre-releases (currently just the 6000.5.0b1 beta), and ArChIvE. We'll be spending a lot of time in the archive. I like to think of it as the back room in the basement where folks store things they just can't bear to part with yet. It's super excellent that all of these versions are kept around. It means my ambition to bring Gun Rocket into 2026 has legs - if only barely. The archive only goes back to Unity 5. Good thing I upgraded from 4.6 in 2018!

Wow, all this history and we haven't even opened the editor yet. Let's try that now.

Uh Oh. Gun Rocket won't open in 5.5.0f3.
========================================

It does the same thing as the game build on Steam: just closes with no information in the log. Shoot.

Some Google research tells me this might be related to the license check. Unity 5 pre-dates Unity Hub. So sure, it makes sense that it could be a license check issue. I try to open from the Unity.exe rather than through Hub as suggested. No luck.

Ok then, let's try a newer version. I wanted to verify the game in 5.5, but I guess I am out-of-luck. I nab the most recent Unity 5: version 5.6.7f1. Again, it doesn't launch from Unity Hub, but that's what I expect at this point. What about launching from the Unity.exe?