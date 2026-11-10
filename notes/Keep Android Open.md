---
title: "Keep Android Open"
url: https://f-droid.org/2026/02/20/twif.html
clipped: 2026-06-17 01:42:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Keep Android Open](https://f-droid.org/2026/02/20/twif.html)

## Digest Summary
F‑Droid’s weekly report (20 Feb 2026) notes ongoing concerns over Google’s announced Android lock‑down, which the team says remains scheduled despite public relief. To raise awareness, F‑Droid and partners have added warning banners to their clients, urging users to contact local authorities. Development on F‑Droid Basic continues; version 2.0‑alpha3 introduces translated strings, CSV export of installed apps, install‑history tracking, mirror chooser, screenshot prevention, tool‑tips, a three‑dot overflow menu, persistent sort order, Material Design 3 styling, and a bug fix for missing icons. Existing Basic users (1.23.x) must enable “Allow beta updates” manually. The report lists major app updates: Buses 1.10, Conversations & Quicksy 2.19.10+free, Dolphin Emulator 2512, Image Toolbox 3.6.1, Luanti 5.15.1, several Nextcloud components (e.g., Nextcloud 33.0.0, Talk 23.0.0), ProtonVPN 5.15.70.0 (now WireGuard‑only), Offi 14.0 (requires Android 8+), QUIK SMS 4.3.4, SimpleEmail 1.5.4. Five apps were removed (e.g., Chord Shift, OpenAthena™) and one added (NeoDB You). About 287 apps received updates. The notice invites RSS subscription, forum participation, and donations via the provided pages.

## Discussion Summary
The discussion is largely critical of Google’s move to restrict sideloading and enforce developer verification, viewing it as a threat to Android’s openness and to independent AOSP‑based distributions. Commenters emphasize the importance of community‑driven alternatives, regulatory engagement, and potential forks, while expressing frustration over the missing “advanced flow” and the impact on side‑loaded apps and custom ROMs. Some note the difficulty of app distribution compared with iOS, suggest migration to Linux‑based phones or other ecosystems, and warn that increased lock‑down could diminish user control and device longevity.

---

## Full Article

### This Week in F-Droid

### TWIF curated on Friday, 20 Feb 2026, Week 8

#### F-Droid core

During our talks with F-Droid users at [FOSDEM26](https://fosdem.org/2026/) we were baffled to learn most were relieved that Google has canceled their plans to lock-down Android.

*Why baffled?* Because no such thing actually happened, the plans announced last August are still scheduled to take place. We see a battle of PR campaigns and whomever has the last post out remains in the media memory as the truth, and having journalists just copy/paste Google posts serves no one.

*But Google saidâ¦* Said what? That thereâs a magical âadvanced flowâ? Did you see it? Did anyone experience it? When is it scheduled to be released? Was it part of Android 16 QPR2 in December? Of 16 QPR3 Beta 2.1 last week? Of Android 17 Beta 1? No? Thatâs the issueâ¦ As time marches on people were left with the impression that everything was done, fixed, Google âwasnât evilâ after all, this time, yay!

While we all have bad memories of âbannersâ as the dreaded ad delivery medium of the Internet, after FOSDEM we decided that we have to raise the issue back and have everyone, who cares about Android as an open platform, informed that we are running out of time until Google becomes the gate-keeper of all users devices.

Hence, the [website](https://f-droid.org/en/) and starting today our clients, with the updates of **[F-Droid](https://f-droid.org/en/packages/org.fdroid.fdroid)** and **[F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic)**, feature a banner that reminds everyone how little time we have and how to voice their concerns to whatever local authority is able to understand the dangers of this path Android is led to.

*We are not alone in our fight, [IzzyOnDroid](https://izzyondroid.org/) added a banner too, more F-Droid clients will add the warning banner soon and other app downloaders, like **[Obtainium](https://f-droid.org/en/packages/dev.imranr.obtainium.fdroid/)**, already have an in-app warning dialogue.*

Regarding **[F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic)** rewrite, development continues with a new release `2.0-alpha3`:

> * Updated Translations
> * Export installed apps list as CSV
> * Add install history feature
> * Add mirror chooser setting
> * Add prevent screenshots setting
> * Show tool-tips for all app bar buttons
> * Create 3-dot overflow menu for My Apps for less frequently used actions
> * Persist sort order of My Apps
> * Adapt strings according to Material Design 3 guidelines
> * Apply string suggestions (Thanks Lucas)
> * Fix missing icon bug in pre-approval dialog

*Note that if you are already using F-Droid Basic version `1.23.x`, you wonât receive this update automatically. You need to navigate to the app inside F-Droid and toggle âAllow beta updatesâ in top right three dot menu.*

In apps news, weâre slowly getting back on track with post Debian upgrade fixes *(if your app still uses Java 17 is there a chance you can upgrade to 21?)* and post FOSDEM delays. Every app is important to us, yet actions like the Google one above waste the time we could have put to better use in Gitlab.

**[Buses](https://f-droid.org/en/packages/org.billthefarmer.buses)** was updated to `1.10` after a two year hiatus.

**[Conversations](https://f-droid.org/en/packages/eu.siacs.conversations)** and **[Quicksy](https://f-droid.org/en/packages/im.quicksy.client)** were updated to `2.19.10+free` improving on cleaning up after banned users, a better QR workflow and better tablet rotation support. These are nice, but another change raises our interest, *âPlay Store flavor: Stop using Google library and interface directly with Google Play Service via IPCâ*. Sounds interesting for your app too? Is this a path to having one single version for both F-Droid and Play that is fully FLOSS? We donât know yet, but we salute any trick that removes another proprietary dependency from the code. If curious feel free to take a look at [the commit](https://codeberg.org/iNPUTmice/Conversations/commit/1abb22b542343642aacb4f7bd82f0bb2bc380ea4).

**[Dolphin Emulator](https://f-droid.org/en/packages/org.dolphinemu.dolphinemu)** was updated to `2512`. We missed one version in between so the changelogs are huge, luckily the devs publish highly detailed posts about updates. So weâll start with [âRelease 2509â](https://dolphin-emu.org/blog/2025/09/16/dolphin-progress-report-release-2509/) *(about 40 mins to read)*, we side-track with [âStarlight Spotlight: A Hospital Wii in a New Lightâ](https://dolphin-emu.org/blog/2025/11/14/starlight-spotlight/) *(for about 50 mins)*, we continue to the current release in [âRelease 2512â](https://dolphin-emu.org/blog/2025/12/22/dolphin-progress-report-release-2512/) *(40 more minutes)* and we finish with [âRise of the Triforceâ](https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/) delving in history for more than one hour.

**[Image Toolbox](https://f-droid.org/en/packages/ru.tech.imageresizershrinker)** was updated to `3.6.1` adding many fixes andâ¦ [some AI tools](https://github.com/T8RIN/ImageToolbox/releases/tag/3.6.0). *Were you expecting such helpers? Will you use them?*

**[Luanti](https://f-droid.org/en/packages/net.minetest.minetest)** was updated to `5.15.1` adding [some welcomed fixes](https://docs.luanti.org/about/changelog/#5150--5151). *If your game world started flickering after the last update make sure to update.*

Nextcloud apps are getting an update almost every week, like **[Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client)** was updated to `33.0.0`, **[Nextcloud Cookbook](https://f-droid.org/en/packages/de.lukasneugebauer.nextcloudcookbook)** to `0.27.0`, **[Nextcloud Dev](https://f-droid.org/en/packages/com.nextcloud.android.beta)** to `20260219`, **[Nextcloud Notes](https://f-droid.org/en/packages/it.niedermann.owncloud.notes)** to `33.0.0` and **[Nextcloud Talk](https://f-droid.org/en/packages/com.nextcloud.talk2)** was updated to `23.0.0`.

But are you following the server side too? *Nextcloud Hub 26 Winter* was just released adding a plethora of features. If you want to read about them, see the 30 minutes post [here](https://nextcloud.com/blog/nextcloud-hub26-winter/) or watch the one hour long video presentation from the team [here](https://peertube.nextcloud.com/w/kHaPaxLJJNAxkoh2f47teX).

**[ProtonVPN - Secure and Free VPN](https://f-droid.org/en/packages/ch.protonvpn.android)** was updated to `5.15.70.0` adding more control to auto-connects, countries and cities. Also all connections are handled now by WireGuard and Stealth protocols as the older OpenVPN was removed making the app almost 40% smaller.

**[Offi](https://f-droid.org/en/packages/de.schildbach.oeffi)** was updated to `14.0` with a bit of code polish. Unfortunately for Android 7 users, the app now needs Android 8 or later.

**[QUIK SMS](https://f-droid.org/en/packages/dev.octoshrimpy.quik.fdroid)** was updated to `4.3.4` with [many fixes](https://github.com/octoshrimpy/quik/releases/tag/v4.3.4). But [Vishal](https://forum.f-droid.org/u/vdbhb59) praised the duplicate remover, the default auto de-duplication function and found that the bug that made deleted messages reappear is fixed.

**[SimpleEmail](https://f-droid.org/en/packages/org.dystopia.email)** was updated to `1.5.4` after a 2 year pause. Itâs just a fixes release, updating translations and making the app compatible with Android 12 and later versions.

#### Removed Apps

##### 5 apps were removed

* Chord Shift: Shift plain text notes
* OpenAthenaâ¢ for Android: OpenAthenaâ¢ lets common drones spot precise locations
* Tibetan Keyboard: Keyboard for Tibetan script
* Tibetan Pad: Read Tibetan script
* Tomdroid: Note taker

#### Newly Added Apps

##### 1 app was newly added

* **[NeoDB You](https://f-droid.org/en/packages/day.vitayuzu.neodb)**: A native Android app for NeoDB designed with Material 3/You

#### Updated Apps

##### 287 more apps were updated

(expand for the full list)

Thank you for reading this weekâs TWIF ð

Please subscribe to the [RSS feed](https://f-droid.org/feed.xml) in your favourite RSS application to be updated of new TWIFs when they come up.

You are welcome to join the [TWIF forum thread](https://forum.f-droid.org/t/new-twif-submission-thread/23546). If you have any news from the community, post it there, maybe it will be featured next week ð

To help support F-Droid, please check out the [donation page](https://f-droid.org/en/donate/) and contribute what you can.