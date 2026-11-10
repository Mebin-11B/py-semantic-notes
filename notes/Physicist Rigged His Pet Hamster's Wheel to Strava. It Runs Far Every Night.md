---
title: "Physicist Rigged His Pet Hamster's Wheel to Strava. It Runs Far Every Night"
url: https://www.runnersworld.com/news/a73355106/hamster-wheel-strava-running/
clipped: 2026-08-31 12:22:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Physicist Rigged His Pet Hamster's Wheel to Strava. It Runs Far Every Night](https://www.runnersworld.com/news/a73355106/hamster-wheel-strava-running/)

## Digest Summary
Thijs de Buck, an MRI physicist in Utrecht, rigged his hamster Mollie’s wheel with a magnet and hall‑sensor that feed rotation data to an ESP32 microcontroller. A nightly script converts the counts into a Strava‑compatible .FIT file and uploads it via the Strava API. Initial attempts with a cheap bicycle computer failed because its sensor entered standby after five minutes of inactivity and only reported total distance. The custom system provides live speed on an OLED display, automated personal‑best tracking, and selectable run titles. Recorded activities show Mollie running 5.5–6 miles (≈9–10 km) over 3.5–4.5 hours per night, with a peak of 10.8 km in the first week. The hamster’s Strava account, which required a paid subscription, quickly amassed thousands of likes, 1,200 kudos and 600 followers, and completed Strava’s 400‑minute challenge in two days. De Buck, an avid runner, plans to compare his weekly mileage to Mollie’s and to test the platform’s race‑time predictions.

---

## Full Article

[Skip to Content](https://www.runnersworld.com/news/a73355106/hamster-wheel-strava-running/#main-content)Runner's World; Strava/Thijs de Buck, Getty Images

I use [Strava](https://www.runnersworld.com/news/a71444923/strava-wedding-running-marriage/) for the obvious stuff, like [runs](https://www.runnersworld.com/training/a69240317/run-faster-program-whats-holding-you-back/), HIIT classes, and the occasional commute that goes full workout when I’m desperate to get my steps in. I’m not a pet owner, but I can understand a dog walk making it on there, too. The dog may be involved, but at least you’re still the one doing the walking.

But workouts uploaded from a hamster wheel? That feels like new territory.

Thijs de Buck, an MRI physicist based in Utrecht, the Netherlands, recently [posted on Reddit](https://www.reddit.com/r/SideProject/comments/1v9uyq0/i_built_a_speeddistance_tracker_for_my_hamster/) that he built a speed and distance tracker for his hamster’s wheel, with the data automatically uploaded to [Mollie’s own Strava account](https://www.strava.com/athletes/1400361231). Mollie, his 10-month-old hamster, is now committed to logging nightly runs with distance, pace, and time.

One recent activity showed 6.06 miles in 4 hours and 37 minutes. The next night, Mollie logged 5.55 miles in 3 hours and 56 minutes.[View full post on Strava](https://www.strava.com/activities/19607460598)

At first, de Buck just wanted to know how much distance Mollie was covering after dark.

“I bought a very cheap bicycle computer pretty much right away,” he told Runner’s World.

That worked at first, because the [bike computer](https://www.bicycling.com/bikes-gear/a61242143/best-bike-computers/) also used a magnet and sensor. But there was one very hamster-specific problem to deal with, as the sensor would shift into standby mode once Mollie stopped running for more than five minutes.

“So if Mollie would take a lunch break at 1 a.m., we’d have no idea how far he’d have run after that,” de Buck said.

The bike computer also only gave him total distance, and that just wasn’t going to cut it. De Buck wanted the full Strava treatment because apparently even hamsters deserve splits, uploads, and post-run analysis.

The build itself is clever, but the basic idea is simple. As de Buck explains it, a magnet on the wheel passes a hall sensor, which detects each rotation. An ESP32—basically a tiny programmable computer—keeps track of the data overnight. In the morning, he says a script on his laptop collects the information, turns it into a Strava-compatible .FIT file, and uploads the activity through the Strava API.

“All that remains is for me to manually add a photo of Mollie, and for Mollie to do the actual hard work during the night,” de Buck said.

De Buck could have stopped once the runs were uploading, but a hamster Strava account needed all the extra features. There’s a tiny organic light-emitting diode (OLED) display to show Mollie’s live speed, a code that helps for automated personal-best tracking, and more than 100 possible run titles, including “The Fast and the Furriest” and “No Rest for the Whiskered,” naturally.Strava/Thijs de Buck

The one thing he didn’t plan for was that auto-uploading the files this way required a paid account.

“There was really only one reasonable solution: my hamster now has Strava Premium,” de Buck said.

A hamster with this much performance data was always going to find an audience. De Buck said the account picked up thousands of likes, more than 1,200 kudos, and more than 600 followers within a week. He also signed Mollie up for Strava’s August 400-minute challenge, and Mollie completed it on Day 2—a wake-up call for anyone still ignoring their own monthly challenges.

Mollie has been with de Buck since Christmas, and his life outside training sounds, quite frankly, pretty focused. De Buck described it as “eat-sleep-run-repeat,” with Mollie spending much of the day hidden underground before waking up and alternating between food and wheel time.Courtesy Thijs de BuckDe Buck and Mollie during a recent training session.

And the little guy’s not exactly phoning it in. De Buck said Mollie is averaging almost 10 kilometers per night, with a current record of 10.8 kilometers after the first week of tracking.

“I really believe he’ll be able to exceed that soon,” he said.

Mollie also has a weirdly consistent schedule for a hamster. Over one seven-day stretch, he started within the same 10-minute window on five nights, between 9:54 and 10:04 p.m. He tends to run in short bursts, sometimes reaching about 4 to 5 kilometers per hour on the live monitor, then hops off for water.

“Even elite athletes need to stay hydrated,” de Buck joked.

De Buck is a runner himself, which helps explain why the project ended up with this level of data. He said he loves “tracking every possible stat” during [marathon training](https://www.runnersworld.com/training/a61475836/how-to-master-marathon-member/), so wanting more information about Mollie’s nightly mileage felt natural. He is also dealing with a minor injury at the moment, which gave him more time to work on the setup.

“When I get back, I think it’ll be a nice challenge to try to match Mollie’s weekly running distance,” he said. “I don’t normally hit 70km a week!”

The next milestone is Mollie’s 20th run, when Strava should start giving race predictions.

“I can’t wait to see his estimated 5K and marathon times,” de Buck said, “and whether he’ll manage to improve those predictions over time! Although I’m a bit worried he’ll have a better marathon time than me.”[Sean Abrams](https://www.runnersworld.com/author/227802/sean-abrams/)

Sean Abrams was the Senior Editor, Growth and Engagement at Men’s Health. He’s a former hip hop dancer who likes long walks on the beach and large glasses of tequila. You can find his previous work at Maxim, Elite Daily, and AskMen.  Watch Next Advertisement - Continue Reading Below

## [News](https://www.runnersworld.com/news/)

[Peres Jepchirchir Dominates the Sydney Marathon](https://www.runnersworld.com/news/a73560744/sydney-marathon-2026-women-winner/)

[Addisu Gobena Wins 2026 Sydney Marathon](https://www.runnersworld.com/news/a73560739/2026-sydney-marathon-men-recap-results/)

[2026 Sydney Marathon Results](https://www.runnersworld.com/news/a73560582/2026-sydney-marathon-results/)

[Blandine L’Hirondel Wins UTMB](https://www.runnersworld.com/news/a73560256/utmb-womens-winner-2026-blandine-lhirondel/)Advertisement - Continue Reading Below

[2026 UTMB Results](https://www.runnersworld.com/news/a73559592/2026-utmb-results-men-women/)

[Ben Dhiman Wins 2026 UTMB](https://www.runnersworld.com/news/a73559546/ben-dhiman-utmb-men-race-recap-2026/)

[How to Watch the 2026 Sydney Marathon](https://www.runnersworld.com/news/a73546745/2026-sydney-marathon-streaming-broadcast-info/)

[John Landy’s Legendary Act of Sportsmanship](https://www.runnersworld.com/news/a73485631/john-landy-sportsmanship-mile-ron-clarke/)

[Vanessa Fraser Runs 4:31 Mile With Her Dog](https://www.runnersworld.com/news/a73487713/vanessa-fraser-dog-mile-personal-best/)

[Jenny Simpson Reveals Heart Condition](https://www.runnersworld.com/news/a73487839/jenny-simpson-running-cardiac-event-update/)

[Officials Admit Marathon Course Error](https://www.runnersworld.com/news/a73476635/edmonton-marathon-course-mistake/)

[Elite Fields Released for 2026 NYC Marathon](https://www.runnersworld.com/news/a73474083/2026-nyc-marathon-elite-field-announced/)Advertisement - Continue Reading Below
