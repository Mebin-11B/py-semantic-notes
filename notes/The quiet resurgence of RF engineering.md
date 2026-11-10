---
title: "The quiet resurgence of RF engineering"
url: https://atempleton.bearblog.dev/quiet-resurgence-of-rf-engineering/
clipped: 2026-06-17 01:11:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The quiet resurgence of RF engineering](https://atempleton.bearblog.dev/quiet-resurgence-of-rf-engineering/)

## Digest Summary
RF engineering, once viewed as stagnant, is now experiencing renewed demand across several sectors. Satellite launches rose from ~260 in 2015 to ~2,700 in 2024, driving a space‑based RF market valued at $18.6 bn (projected to double by 2033) and supporting $613 bn of global space economics. Commercial constellations (e.g., Starlink) and defense programs (e.g., SDA’s 500‑satellite LEO architecture, $35 bn through 2029) require extensive transceivers, antennas, and amplifiers.  

5G rollout multiplies RF component needs: each base station’s MIMO chains increase from 2–4 (4G) to 64–256, expanding the RF market toward $50 bn. Emerging 6G research (sub‑THz, ISAC) adds further hardware challenges.  

Automotive radar, mandated by EU safety rules, contributes a $7 bn RF segment, while Wi‑Fi 7, IoT (21 bn devices in 2025) and other wireless applications broaden the demand base.  

Talent supply is constrained—73 % of EE employers cannot fill RF roles within six months, salaries exceed $130 k, and competition from semiconductor hiring intensifies. Companies (e.g., Mini‑Circuits, Keysight, Baylor University) are creating university pipelines to address the shortage. Overall, RF engineering growth is modest (≈7 % EE BLS projection) but sustained by multi‑industry demand and limited talent availability.

## Discussion Summary
Comments show a generally positive view that RF engineering is far from stagnant, with growth driven by 5G/6G, aerospace, automotive, drones, and emerging physical‑AI applications. Many note increasing hiring demand, especially in space and defense, while also highlighting regional disparities—strong activity in China and limited opportunities in the US and parts of Europe. Concerns recur about high tool costs, the steep learning curve, aging expertise, modest salaries, and a shrinking pipeline of new electrical engineers. Open‑source tools and SDR are seen as easing entry for software‑oriented newcomers.

---

## Full Article

The Quiet Resurgence of RF Engineering
======================================

*14 Apr, 2026*

I've worked in the aerospace industry for the past 8 years, and for most of that time I felt like I could confidently say that RF engineering felt like it was a quiet, non evolving field. The advice I heard early on, and that I watched a lot of other people follow, was to go into software. Machine learning, cloud infrastructure, web development. That's where the growth was, that's where the money was, and honestly, that's where most new graduates went (myself included at the time). I studied Information Systems in college, not electrical engineering. RF was nowhere on my radar.

But aerospace has a way of pulling you into hardware whether you planned on it or not. I started my career at NASA, building telemetry platforms, ETL pipelines, and spacecraft visualization tools. Pure software work. Then I moved to a private aerospace company. Much smaller than NASA (approx 130 employees at the time I joined), and it required me to wear a ton of hats to work on ground systems. That's where things shifted. When you're responsible for ground station services, even when most of it now is *software defined* you can't stay in the software lane entirely. I found myself doing link budget analysis, troubleshooting RF anomalies, and developing a working understanding of the RF hardware chain that I never expected to need.

That experience is part of why I've been paying attention to what's happening in RF more broadly. I've been feeling a shift over the past several years — more demand, fewer people, and more urgency from the companies I talk to. RF engineering is not only alive, it's rebounding in a significant way. I wanted to dig into whether my gut feeling here is actually backed by data, or if I'm just seeing what I want to see from inside the aerospace bubble.

What Actually Happened to RF
----------------------------

To be fair to the people who called RF a shrinking field, they weren't wrong, at least for a stretch. After the dot-com bust in the early 2000s, the telecom industry consolidated hard. Companies merged, manufacturing moved offshore, and a lot of RF design work either disappeared or got absorbed into a handful of large defense contractors. The broader electrical engineering job market stagnated. [Electronic Design](https://www.electronicdesign.com/technologies/embedded/article/21255051/electronic-design-electronics-and-electrical-engineering-jobs-on-the-declinecan-they-be-saved) has documented this trend not just for RF, but across EE as a whole. I feel confident that if the field as a whole is shrinking, then the subfield of RF was also in decline.

And then software exploded. The engineers who might've gone into EE or RF design a generation earlier went down the software "FAANG" route instead. University enrollment in RF specific coursework drifted down. Though I'll be honest, hard numbers on this are annoyingly hard to find so this is more of my gut assumption. What we do know is that today, companies [openly describe the difficulty](https://filtronic.com/blogs_challenges-of-recruiting-rf-engineers/) of recruiting RF engineers, pointing to a generation that chose software over EE.

But here's the thing that gets missed in the narrative: it never actually went away. The defense sector has been keeping it alive this entire time. Raytheon, Lockheed Martin, Northrop Grumman, these companies never stopped hiring people who understand beam patterns, power amplifiers, and antenna design. The majority of RF engineering job postings have historically come from aerospace and defense. RF didn't die. It just receded from the civilian sector while quietly remaining essential to national security and defense.

So What Changed
---------------

The resurgence didn't come from one place. It's coming from several industries all hitting the same wall at roughly the same time; a shortage of engineers who can work at the hardware level.

### The Space Boom

This is the one I see most directly in my work, and it *feels* the most dramatic. In 2015, roughly [260 spacecraft were launched](https://ourworldindata.org/grapher/yearly-number-of-objects-launched-into-outer-space) into space globally. By 2024, that number hit approximately 2,695. A 10x increase in under a decade. The overwhelming majority of that growth came from commercial constellations, with SpaceX's Starlink deploying over 1,500 satellites in 2023 alone.

Every single one of those satellites needs RF hardware. Starlink operates in Ku-band for user links and Ka-band for gateways, with V-band planned for Starlink V2. Kuiper and OneWeb follow similar architectures in Ka-band. Each spacecraft carries transceivers, antennas, filters, and amplifiers — and each ground station that talks to them needs the same. The amount of RF hardware per spacecraft adds up fast, and the launch cadence isn't slowing down.

The money tells the same story. The global space economy hit a record [$613 billion in 2024](https://www.spacefoundation.org/2025/07/22/the-space-report-2025-q2/), with commercial making up roughly 78% of that. The [space based RF market](https://www.openpr.com/news/4298716/space-based-rf-and-microwave-technology-market-size-share) alone was valued at $18.6 billion and is projected to nearly double by 2033.

And it's not just commercial. On the defense side, the Space Development Agency is building the [Proliferated Warfighter Space Architecture](https://payloadspace.com/ndsa-explainer/) — a LEO constellation targeting 500+ satellites. Only a few dozen are on orbit today, but nearly $35 billion has been committed through 2029. Even with the growing push toward optical links, these spacecraft still carry RF communications hardware and telemetry payloads, and that is unlikely to change anytime soon.

### 5G Wide Adoption

I think 5G's impact on RF demand is genuinely understated. A typical 4G base station has 2 or 4 transmit-receive chains. A 5G MIMO radio integrates anywhere from 64 to 256. That's an 8x to 16x increase in the power amplifiers, low-noise amplifiers, and antenna switches needed per installation. Multiply that across [642 operators and 374 commercial launches](https://gsacom.com/technology/5g/), and you start to see why the [RF component market](https://www.mordorintelligence.com/industry-reports/rf-components-market) is pushing toward $50 billion with no signs of stoppage.

The design challenges make it worse. Millimeter wave frequencies introduce path loss that demands arrays with manufacturing tolerances at the millimeter scale. Additionally, thermal management, ex. dissipating 300+ watts from tower-mounted hardware with passive cooling, isn't something you can solve reliably in software.

### 6G Is Already In The Works

It's early, but 6G isn't vaporware. [3GPP](https://www.3gpp.org/specifications-technologies/releases/release-20) has been actively working on 6G study items since 2024, with first specifications targeted for late 2028 and commercial deployments expected around 2030. The EU, South Korea, and major telecom players like Ericsson, Nokia, and Samsung are all investing heavily into this research.

The RF challenges are genuinely new territory. Sub-terahertz frequencies and [integrated sensing and communication](https://www.ericsson.com/en/blog/2024/6/integrated-sensing-and-communication) (ISAC), which 3GPP officially scoped into 6G in the middle of last year, push well beyond what current design tools can handle. Worth noting though — the original vision for sub-THz has already been [scaled back](https://the-mobile-network.com/2026/04/6g-reality-check-and-update/) from outdoor cellular to mostly short-range indoor use cases like data centers and factories. But even with a narrower scope, all of this research eventually has to become hardware, and the people who know how to do that are already stretched thin.

### The "Drivers" That Don't Get Headlines

Space and cellular seem to dominate the conversation, but there are quieter contributors that I think are what make this feeling more durable rather than cyclical.

Automotive radar is a sneaky one. The EU now [mandates automatic emergency braking](https://spectrum.ieee.org/europe-mandates-automatic-emergency-braking) in all new vehicles and, while the regulation is *technically* sensor-agnostic, most implementations rely on radar. Every new car with adaptive cruise control or collision avoidance has RF hardware running on board. That market alone is projected to hit $7+ billion this year. Then there's Wi-Fi 7, operating across three bands simultaneously, and the ever expanding IoT landscape with over 21 billion connected devices as of 2025. Anything that communicates wirelessly needs RF work behind it, and that list just keeps growing.

The Talent Shortage
-------------------

What makes this an interesting pattern, is that the supply side is genuinely broken. [IEEE survey data](https://k2staffinginc.com/electrical-engineering-talent-shortages-how-recruiters-bridge-the-gap/) shows 73% of EE employers can't fill positions within six months, up from 45% five years ago. [EE Times](https://www.eetimes.com/engineer-demand-exposes-talent-gap-in-rf-development/) has reported specifically on the RF talent gap and its growing demand.

And it's not just direct competition for RF roles either. RF and semiconductor careers often pull from the same shrinking pool of EE graduates, and right now the semiconductor side is in a hiring frenzy of its own. The CHIPS Act has poured billions into domestic fab expansion, AI chip demand is exploding, and the semiconductor industry is projecting a [67,000 worker shortfall by 2030](https://www.semiconductors.org/chipping-away-assessing-and-addressing-the-labor-market-gap-facing-the-u-s-semiconductor-industry/). All of that competes directly with RF employers for the same talent. When everyone is fighting over the same small group of EE grads, RF companies, which tend to be smaller and less visible than the big chip fabs, often lose out.

Salaries reinforce this. Average RF engineer comp is pushing past $130K, with top-end design positions listing above $200K.

The real signal to me is what companies are doing about it. [Mini-Circuits](https://blog.minicircuits.com/bridging-the-gap-between-the-university-and-the-rf-industry/) and Keysight are investing directly in university partnerships because they can't wait for the academic pipeline to refresh itself. Baylor launched a new Graduate Certificate in Microwave/RF Engineering in 2024, one of the few new programs I've seen pop up, but I imagine it won't be the last. When industry starts building its own talent pipeline, that tells me the shortage isn't a blip.

Looking Forward
---------------

I don't want to oversell this. I don't think RF is going to become a field with an insane growth pattern. [The BLS](https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm) projects 7% growth for EE broadly, faster than average sure, but not a hockey stick. The demand is real, it's coming from multiple directions at once, and the supply is genuinely constrained.

My own path is a small version of this story. I came in as a software engineer and had to learn RF on the job because there wasn't someone else to hand it off to. I say this as someone who made that transition, you *absolutely* can learn enough RF to be effective in your role, and I'd encourage anyone in aerospace or wireless to do it (honestly it's a fun niche to get into anyway). But there's a difference between understanding link budgets and SDR anomalies versus designing a phased array from scratch. The latter takes years of dedicated focus. The underlying physics (electromagnetics, thermodynamics, materials science, manufacturing tolerances) don't reduce to algorithms. You have to build intuition for it, and that's not something you can shortcut.

I may one day expand on learning this stuff on the job and on the fly, but I do want to shoutout [PySDR](https://pysdr.org/). It's a free resource built exactly for software engineers. It uses Python as the bridge between hardware and software concepts, and starts with no RF knowledge assumptions from the beginning and doesn't spend a ton of time over explaining the math.

The people who stuck with RF through the lean years are now some of the most sought-after engineers I've come across. And for anyone trying to figure out where to focus, either as a primary discipline or as a secondary skill set like it was for me, I think RF is worth a serious look right now.

---

**Who Am I?**

Anthony Templeton is a software engineer passionate about high-performance computing and aerospace applications. You can connect with me on [LinkedIn](https://www.linkedin.com/in/anthony-f-templeton/) or check out more of my work on [GitHub](https://github.com/ATTron).