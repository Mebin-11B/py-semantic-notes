---
title: "Show HN: AsteroidOS 2.0 – Nobody asked, we shipped anyway"
url: https://asteroidos.org/news/2-0-release/index.html
clipped: 2026-06-17 01:43:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - smartwatches
  - asteroidos
  - wearables
  - open-source os
  - embedded systems
  - qml
related:
  - "[[WiiFin – Jellyfin Client for Nintendo Wii]]"
  - "[[Open-Source OS]]"
  - "[[Wearables]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The open-source smartwatch operating system AsteroidOS releases version 2.0, introducing an Always-On-Display, redesigned system apps, improved synchronization, and expanded watch compatibility.
>
> **Key points:**
> - AsteroidOS 2.0 features UI updates including a customizable QuickPanel, 7 launcher styles, and a bedside Nightstand mode.
> - Performance improvements deliver smoother rendering, better power management, and longer battery life.
> - The release expands hardware compatibility, fully supporting 19 smartwatches with experimental support for 5 more.
> - Synchronization updates improve integration with clients like Gadgetbridge, Amazfish, and Telescope.
>
> **Concept links:** [[Smartwatches]], [[Asteroidos]], [[Wearables]], [[Open-Source Os]], [[Embedded Systems]], [[Qml]]
>
> **Suggested connections:**
> - [[WiiFin – Jellyfin Client for Nintendo Wii]] — another community-driven homebrew/open-source effort targeting constrained hardware.
> - [[Open-Source OS]] — independent operating systems created for privacy, customizability, and longevity.
> - [[Wearables]] — the hardware and software space of portable consumer electronics.
<!-- ai-summary:end -->
# [Show HN: AsteroidOS 2.0 – Nobody asked, we shipped anyway](https://asteroidos.org/news/2-0-release/index.html)

## Digest Summary
AsteroidOS 2.0 introduces an Always‑On‑Display, a highly customizable QuickPanel, seven new launcher styles, and expanded wallpaper/watch‑face integration. UI enhancements include nightstand mode with charging status, new background “breathing” animation, triangulated flat‑mesh wallpapers, a 2048‑style game (Diamonds), redesigns of weather, timer, flashlight, calculator, and bootsplash, plus unified icons, Noto Sans system font, Twemoji, and support for round screens with flat‑tyre shapes. Performance gains cover smoother UI rendering, longer battery life, and numerous stability fixes. The release adds full support for 19 watches (e.g., Fossil Gen 4‑6, Huawei Watch 2, LG W7, multiple Ticwatch models) and experimental support for five additional devices. Synchronisation clients now include Gadgetbridge 0.73.0, Amazfish (SailfishOS/Linux), and Telescope (UBports). Community contributions span translations (49 languages), watch‑face creation, ports of games and health apps, and tooling for secondary LCDs. Infrastructure updates feature a larger server, MediaWiki documentation, Matrix chat, and a community package repository. The team invites developers, translators, and designers to contribute via GitHub, Weblate, or the Matrix channel.

## Discussion Summary
The comments express strong approval of an open‑source smartwatch platform, highlighting its Linux foundation, long‑term maintainability, and ability to extend device life beyond manufacturer support. Praise focuses on the practical use of QML for constrained screens and the value of community‑driven development. Recurrent concerns include limited hardware availability, especially in the US, fragmented device support, and missing features such as broader Wi‑Fi use, Rust integration, and better app infrastructure. Overall sentiment is enthusiastic, with calls for expanded compatibility and technical enhancements.

---

## Full Article

AsteroidOS 2.0 Has Landed
=========================

Asteroids travel steadily, occasionally leaving observable distance. It has been a while since our last release, and now it's finally here!

AsteroidOS 2.0 has arrived, bringing major features and improvements gathered during its journey through community space. Always-on-Display, expanded support for more watches, new launcher styles, customizable quick settings, significant performance increases in parts of the User Interface, and enhancements to our synchronization clients are just some highlights of what to expect.

VIDEO

Milestones Reached
------------------

Design, Usability, and App Improvements
---------------------------------------

* [New QuickPanel](https://github.com/AsteroidOS/asteroid-launcher/pull/180)  
  The former QuickSettings top menu on the homescreen has been reworked into a highly customizable QuickPanel with many more settings toggles, app short cuts and remorse timer driven power off.
    
   [![Quick Panel](https://asteroidos.org/public/img/news-img/2-0-quickpanel.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=34s)
* [New App Launchers](https://github.com/AsteroidOS/asteroid-settings/pull/35)  
  Seven more App Launcher styles have been added. Those can be selected in the new Launcher settings page.
    
   [![App Launchers](https://asteroidos.org/public/img/news-img/2-0-launchers.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=223s)
* [Enhanced Wallpaper](https://github.com/AsteroidOS/asteroid-settings/pull/39) and [Watchface gallery](https://github.com/AsteroidOS/asteroid-settings/pull/40)  
  Watchfaces are now paired with the user selected Wallpaper already in the Watchface gallery. Helping to find your favourite combination at a glance. Both pages received major performance improvements.
    
   [![Watchface gallery](https://asteroidos.org/public/img/news-img/2-0-watchface-selector.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=168s)
* [Nightstand mode](https://github.com/AsteroidOS/asteroid-settings/pull/49)  
  Use your watch as a bedside clock or simply show charging much more clearly. Selected watchfaces show a large charging status when power is connected.
  The nightstand settings page makes this mode very versatile.
    
   [![Nightstand](https://asteroidos.org/public/img/news-img/2-0-nightstand.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=142s)
* [New background animation](https://github.com/AsteroidOS/qml-asteroid/pull/47/files)  
  Reworked design for a more organic feeling of "breathing".
    
   [![Flatmesh](https://asteroidos.org/public/img/news-img/2-0-flatmesh.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=110s)
* [New wallpapers](https://github.com/AsteroidOS/asteroid-wallpapers/pull/4)  
  Extending on the well received flatmesh design, triangulated wallpapers turned out to fit beautifully.
    
   [![Wallpapers gallery](https://asteroidos.org/public/img/news-img/2-0-wallpapers.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=204s)
* [Diamonds](https://github.com/AsteroidOS/asteroid-diamonds)  
  A 2048 like game with a fresh twist. Suited nicely for small resolutions and displays.
    
   [![Diamonds app](https://asteroidos.org/public/img/news-img/2-0-diamonds.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=386s)
* [Weather app design overhaul](https://github.com/AsteroidOS/asteroid-weather/pull/12)  
  Embracing the new possibilities Noto Sans and its vast variety of font styles offers. The weather app got refined towards better legibility and presentation of very long place names.
    
   [![Weather app](https://asteroidos.org/public/img/news-img/2-0-weather.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=31s)
* [Timer app redesign](https://github.com/AsteroidOS/asteroid-timer/pull/10)  
  The timer app works in the background now. It got optimised for use on round watches. The design is now consistent with the stopwatch.
    
   [![Timer app](https://asteroidos.org/public/img/news-img/2-0-timer.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=320s)
* [Flashlight app](https://github.com/AsteroidOS/asteroid-flashlight)  
  Yup, it flashes light. Most useful, so it got added to the stock selection.
    
   [![Flashlight app](https://asteroidos.org/public/img/news-img/2-0-flashlight.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=61s)
* [Animated Bootsplash logo](https://github.com/AsteroidOS/meta-asteroid/commit/b8f4403139cabf0ff83a663968d901c668151180)  
  A very small touch. But yet another possibility for designers to get involved.
    
   [![Bootlogo](https://asteroidos.org/public/img/news-img/2-0-boot.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc)
* [Round screens with a flat tyre shape](https://github.com/AsteroidOS/meta-asteroid/pull/41) are now supported.
    
   [![Flat tyre](https://asteroidos.org/public/img/news-img/2-0-flat-tyre.jpg)](https://www.youtube.com/watch?v=U6FiQz0yACc&t=125s)
* [Calculator app with new layout](https://github.com/AsteroidOS/asteroid-calculator/pull/4)  
  Improved button layout for easier operation and better legibility, especially on round displays.
* [New UI elements and polished icons](https://github.com/AsteroidOS/asteroid-icons-ion/pull/18/files)  
  Improved toggles, progress bars and other UI elements by unifying the design and removing inconsistencies.
* [More translations (49 languages)](https://hosted.weblate.org/projects/asteroidos/)  
  More then 20 languages added since our last release thanks to much welcome community effort.
* [Noto Sans system font](https://github.com/notofonts)  
  Supporting the localisation efforts, Noto Sans offers consistent font styles for many languages with custom character set.
* [Color Emoji](https://github.com/AsteroidOS/meta-asteroid/pull/56)  
  Underlining the flat nature of our UI, we moved from Noto Color Emoji to Twemoji.
* [Ringtone vibration pattern](https://github.com/AsteroidOS/asteroid/issues/99)  
  Customise all the things! Here, the vibration pattern on incoming calls.

Performance and System Enhancements
-----------------------------------

* **Optimized Rendering**  
  Significant performance improvements have been made to the User Interface, resulting in smoother animations and transitions.
* **Battery Life Improvements**  
  Various optimizations have been implemented to extend battery life during daily use.
* **Stability Fixes**  
  Numerous bug fixes and stability improvements have been applied across the system.

Expanded Watch Support
----------------------

Since 1.0 we added support for the following watches:

* Fossil Gen 4 Watches (firefish/ray)
* Fossil Gen 5 Watches (triggerfish)
* Fossil Gen 6 Watches (hoki)
* Huawei Watch (sturgeon)
* Huawei Watch 2 (sawfish/sawshark)
* LG Watch W7 (narwhal)
* Moto 360 2015 (smelt)
* MTK6580 (harmony/inharmony)
* OPPO Watch (beluga)
* Polar M600 (pike)
* Ticwatch C2+ & C2 (skipjack)
* Ticwatch E & S (mooneye)
* Ticwatch E2 & S2 (tunny)
* Ticwatch Pro, Pro 2020 and LTE (catfish/catfish-ext/catshark)
* Ticwatch Pro 3 (rover/rubyfish)

And partial support for the following watches:

* Casio WSD-F10/F20 (koi, ayu) - bricking have been reported on some watches
* LG Watch Urbane 2 (nemo) - missing too many features
* Moto 360 1st gen (minnow) - has underwhelming performance, it is the only watch we have ported with a TI SoC.
* Samsung Gear 2 (rinato) - too unstable and too bad power management
* Samsung Gear Live (sprat) - in an unusable state due to persistent display issues

We have created an "Experimental" category in our watch gallery for the above 5 watches since we do not consider those suitable for daily use. We will however continue to provide install images for these watches, and we welcome new contributors with fresh ideas to help improve support! We also continue to monitor supported watches and for example recently demoted the Sony Smartwatch 3 (tetra) due to unresolved hardware support issues.

The Samsung Gear 2 (rinato) is our first watch supported with a mainline Linux kernel and therefore without the use of libhybris. The Asus Zenwatch 2 (sparrow) also has very basic support for running on a mainline Linux kernel.

For a complete list of supported devices and installation instructions, please visit our [installation guide](https://asteroidos.org/install/).

Apart from adding new watches, the community has also been actively enhancing the support for our existing range of watches.
Visit our newly created [feature matrix page](https://asteroidos.org/install/features/) to find out about the detailed support level for your watch.

Synchronisation Clients
-----------------------

Thanks to Noodlez, initial AsteroidOS support has been added to [Gadgetbridge version 0.73.0](https://codeberg.org/Freeyourgadget/Gadgetbridge/src/branch/master/CHANGELOG.md).

### [Amazfish](https://github.com/piggz/harbour-amazfish) (SailfishOS and Linux Desktop)

Jozef Mlich has added AsteroidOS support to Adam Piggs Amazfish. Initially [developed for SailfishOS](https://sailfishos-chum.github.io/apps/harbour-amazfish/), Amazfish is now also [available in kirigami flavour for linux desktops](https://github.com/piggz/harbour-amazfish).

### [Telescope](https://open-store.io/app/telescope.asteroidos) (UBports Ubuntu Touch)

After our initial release [StefWe](https://github.com/StefWe) created [Telescope](https://github.com/AsteroidOS/telescope) a sync client for UBports.

Community Contributions
-----------------------

This release would not have been possible without the dedicated efforts of our community contributors. We extend our heartfelt thanks to everyone who reported issues, submitted patches, and provided feedback during the development cycle.

Over the years, the AsteroidOS community has expanded its reach, with community translators adding over 20 languages to the [AsteroidOS Weblate](https://hosted.weblate.org/projects/asteroidos/#languages). Translating into your local language is the easiest way to get involved. Your help is most valuable to make AsteroidOS fit for use in your region.

Watchface creation has been a popular community activity lately. We are happy to present the new and comprehensive [watchfaces creation and design guide](https://asteroidos.org/wiki/watchfaces-creation/). It is garnished with testing and deployment scripts to simplify the process further.
Our community came up with funny and beautiful new watchfaces. Those are all collected in the [unofficial watchfaces repository](https://github.com/AsteroidOS/unofficial-watchfaces).

moWerk has contributed a variety of watchfaces. Two highlights are the minimalistic [pulsedot](https://youtu.be/cXeWRX6N6Sg) and a classic Monty Python inspired [silly walks watchface](https://twitter.com/eLtMosen/status/1403642123338014722).

MagneFire did show-off [Doom](https://twitter.com/MagneFire_/status/1230159641004445696), [Super Tux Kart](https://fosstodon.org/@MagneFire/107105850296484856), [gpSP](https://twitter.com/MagneFire_/status/1220789841673236485) and other [emulated games](https://twitter.com/MagneFire_/status/1353443545831510016) on his watch. The native 2048 port called diamonds was recently included into the stock set of apps.

Dodoradio worked on a few unusual watches, like the [LG Watch W7](https://asteroidos.org/install/narwhal/) with its physical hands to be taken into account. And the [Casio WSD-FXX series](https://github.com/AsteroidOS/meta-smartwatch/pull/140) sporting multifunctional secondary displays. Along with some more conventional ports such as the Fossil Gen5 and Polar M600. For watches with GPS, he contributed a [Map app with waypoint functionality](https://git.dodorad.io/dodoradio/asteroid-map/about) to the community repository. His initial version of the often requested [asteroid-health](https://git.dodorad.io/dodoradio/asteroid-health) app is already capable of automatically tracking steps and heartrate with minimal impact on battery life.

Beroset implemented the new [Nightstand mode](https://asteroidos.org/news/nightstand/index.html). In addition to his efforts in maintaining the build tools, Beroset has also developed [host-tools](https://github.com/beroset/asteroid-hosttools) which make it easier to work on watches from a Linux host. Furthermore, he has included a user-friendly [GUI for deploying watchfaces](https://wiki.asteroidos.org/index.php/Watchface_and_Package_Installation#Scripted_method) and created [asteroid-weatherfetch](https://github.com/beroset/asteroid-weatherfetch), a convenient app that downloads weather data using the watches [IP connection](https://wiki.asteroidos.org/index.php/IP_Connection).

PostmarketOS now offers our launcher and core apps, thanks to postmarketOS developer PureTryOut, who moved our buildsystem from qmake to cmake along the way.

The program [lcd-tools](https://github.com/AsteroidOS/lcd-tools) by lecris and MagneFire was originally developed to control the secondary LCD on the TicWatch Pro. And got extended by dodoradio and beroset to make use of many more features the Casio secondary displays offer.

MagneFire, jrt, moWerk and beroset joined the AsteroidOS team.

Infrastructure
--------------

Our website [asteroidos.org](https://asteroidos.org) has seen a major content extension.

* A [FAQ](https://asteroidos.org/faq/) section has been added to provide a quick overview of our project.
* The Install page has grown into a gallery of supported watches over time with now 30 watches listed. We renamed it to "[Watches](https://asteroidos.org/watches/)" and plan to evolve this page into a purchase guide to aid new users in choosing a supported watch. A first step was to resize the images of all watches to correctly reflect the relative size differences between them, to be able to compare their dimensions.
* The [Documentation](https://asteroidos.org/wiki/documentation/) pages are frequently updated by community members and nicely keep up with the current state of development. We recently moved them into a MediaWiki. This enables users without deeper knowledge to contribute to the documentation much more easily.

The creator of the unofficial [Subreddit](https://www.reddit.com/r/AsteroidOS/) gave us full access, making it an official channel alongside our [Mastodon account](https://fosstodon.org/@AsteroidOS).

As we already mentioned in a [previous blog post](https://asteroidos.org/news/farewell-freenode), we moved all our communication from freenode to Matrix and Libera.chat. You are invited to join the AsteroidOS Matrix channel using this link. <https://matrix.to/#/#Asteroid:matrix.org>

With 2.0 we introduce a community repository, to improve discoverability and simplify the installation of precompiled packages, while building the foundation for a possible graphical software center in the future. Currently, the repository consists of a few debugging tools, community watchfaces, games and emulators. Developers are welcome to create pull requests on the [meta-community](https://github.com/AsteroidOS/meta-asteroid-community) repo for packaging.

After moving our infrastructure to a larger server, we have seen an increase in the frequency of nightly releases. However, it is worth noting that completely rebuilding all packages for all 30 watch system images still takes almost a week. Therefore, we can expect the nightlies to be ready on weekends.

Getting Involved
----------------

Interested in contributing to AsteroidOS? Whether you're a developer, designer, or enthusiast, there are many ways to get involved:

* **Join our [community forums](https://asteroidos.org/community/)** to discuss ideas and share feedback.
* **Report issues or suggest features** on our [GitHub repository](https://github.com/AsteroidOS/asteroid).
* **Help with translating AsteroidOS to your language** [using Weblate](https://hosted.weblate.org/projects/asteroidos/).
* **Contribute to the codebase** by tackling open issues or developing new features.

Your participation helps make AsteroidOS better for everyone.

Download AsteroidOS 2.0
-----------------------

Ready to experience the latest features and improvements? Download AsteroidOS 2.0 from our [official website](https://asteroidos.org/watches/) and follow the installation instructions for your device.

Thank you for your continued support. We hope you enjoy AsteroidOS 2.0!

The Future
----------

As you might have noticed, the current releases linked on the installation pages have feature parity with the 2.0 release. At some point, we decided to switch from our stable 1.0 release to a quasi 1.1 nightly rolling release, as the 1.0 release became too old to maintain. In the future, we would like to change our release cycle to offer more frequent stable releases. A stable release will always be stable. But not too old to no longer be maintainable.

For the future, we are going to set up a roadmap for features we would like to see in an eventual next release.
Based on recent early community work, we might see features like:

* Combined fitness app (Privacy minded heart rate monitoring and step counter tracking)
* WiFi setup via the settings app
* Web based Watchface creation tool
* Web based flash tool
* App store for making community contributions easily available

---

Written by AsteroidOS Team on the 17/02/2026