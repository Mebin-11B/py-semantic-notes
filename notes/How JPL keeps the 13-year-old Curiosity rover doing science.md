---
title: "How JPL keeps the 13-year-old Curiosity rover doing science"
url: https://spectrum.ieee.org/curiosity-rover-jpl-mars-science
clipped: 2026-06-17 00:49:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How JPL keeps the 13-year-old Curiosity rover doing science](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science)

## Digest Summary
- Curiosity has traveled ~37 km, drilled 42 rocks, and returned ~763 k photos after 13 years on Mars; its continued operation relies on software updates and hardware management.  
- Hardware: Curiosity and Perseverance both use RAD‑750 processors with similar memory; Perseverance adds a dedicated visual‑odometry processor for autonomous driving.  
- Major software fix (Sol 2172): after a NAND memory anomaly on computer B, engineers restored computer A, repurposed 64 MB of NOR storage (previously flight‑software copies) as a file system, enabling A to run the mission with <1 % of its original memory (“R‑Hope” release).  
- Primary wear concerns: front‑wheel damage from sharp, buried rock tips and consumable actuator cycles; power loss from the RTG’s gradual decay is the main limiting factor.  
- Mitigations include reducing computer‑on time, parallelizing tasks (e.g., driving while communicating), and improving power‑usage monitoring.  
- Lessons for future missions emphasize early operator involvement in software architecture, granular power budgeting, and robust fault‑tolerant memory handling to extend rover lifespans.

## Discussion Summary
Comments emphasize the low cost of robotic missions compared with crewed flights and advocate allocating more budget to probes. There is enthusiasm for technological upgrades such as a newer radiation‑hard processor, and appreciation for Curiosity’s longevity and continued science return. Several remarks praise the skill required for remote rover operations while also recognizing the challenges and value of human spaceflight. Overall tone is positive toward continued robotic exploration, with balanced acknowledgment of both robotic and crewed mission merits.

---

## Full Article

Thirteen years ago last August, I was [camped out](https://spectrum.ieee.org/msl-what-to-expect-on-sunday-night) in NASA’s Jet Propulsion Laboratory press room in Pasadena, Calif., waiting to see whether the [Curiosity rover](https://robotsguide.com/robots/curiosity) would survive its descent and skycrane-assisted landing on the surface of Mars. It did, and [it was awesome](https://spectrum.ieee.org/curiosity-rover-alive-and-well-on-surface-of-mars).

Since then, Curiosity (also known as Mars Science Laboratory) has [traveled nearly 37 kilometers](https://science.nasa.gov/mission/msl-curiosity/location-map/), drilled into and sampled [42 different rocks](https://science.nasa.gov/resource/curiositys-42-drill-holes/), and as of publication has snapped nearly [763,000 photos](https://mars.nasa.gov/msl/multimedia/raw-images/?order=sol+desc%2Cinstrument_sort+asc%2Csample_type_sort+asc%2C+date_taken+desc&per_page=50&page=0&mission=msl). The fact that this robot is still [hard at work](https://www.jpl.nasa.gov/news/nasas-perseverance-curiosity-panoramas-capture-two-sides-of-mars/), getting [real science done](https://www.nasa.gov/missions/mars-science-laboratory/curiosity-rover/nasas-curiosity-finds-organic-molecules-never-seen-before-on-mars/) at the age of 13, is absolutely incredible—not only is Mars an actively hostile environment for robots, but the only kind of maintenance that [JPL](https://spectrum.ieee.org/tag/jpl) engineers can do is to send very, very careful software updates.

Nevertheless, the clever folks at JPL have managed to keep Curiosity safe, warm, mobile, and sciencing, despite well-worn wheels and less and less power every day. One of those folks is [Alexandra Holloway](https://www.linkedin.com/in/alexandraholloway/), the assistant team chief for engineering operations for Curiosity, who spoke to **IEEE Spectrum** about keeping Curiosity roving, what its future looks like, and how JPL has used that experience to make [rovers](https://spectrum.ieee.org/tag/rovers) like Perseverance even more capable.

**How astonished should we be that after 13 years on Mars, Curiosity is not only still doing science, but actually getting more capable?**

![A woman with large green eyes and a shaved head](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science) Alexandra Holloway is the assistant team chief for engineering operations on the Curiosity Mars rover at the Jet Propulsion Laboratory.Alexandra Holloway

**Alexandra Holloway:** I’m astonished! The longevity comes from a lot of ongoing work. It’s not just that Curiosity was built robustly; it’s also because we’re continuously putting in effort to ensure it can continue to have that lifespan. I think about all the different kinds of embedded systems there are, from cars to refrigerators, and none of them have the kind of longevity that we have with the rover. It’s mind-boggling, and it’s inspiring.

**Is the** [**Perseverance rover**](https://robotsguide.com/robots/perseverance)**, which is nine years younger than Curiosity, significantly different in terms of its hardware and software?**

**Holloway:** In terms of hardware, the rovers are actually very similar. Both use a [RAD 750 processor](https://www.baesystems.com/en/article/bae-systems-rad750--single-board-computers-guide-insight-mars-landing) and have the same amount of memory. However, Perseverance has an extra processor specifically for visual odometry, which allows it to drive autonomously. [This difference reflects their primary mission designs](https://www.youtube.com/watch?v=Q_P0swqaZDk): Perseverance was designed for driving long distances, while Curiosity is a mission focused on sampling as it goes. So Perseverance’s onboard scheduling capabilities are there to optimize its driving. In fact, just last year, Perseverance surpassed [Curiosity’s driving distance](https://science.nasa.gov/mission/msl-curiosity/location-map/) after only about three years on Mars.

**Do you have some examples of significant tweaks the team has made to keep Curiosity roving?**

**Holloway:** One of my favorite examples comes from a [processor anomaly](https://science.nasa.gov/blog/sol-2204-curiosity-science-is-baaaack/) that happened on Sol 2172 [Ed. note: “Sol” is the term for a Martian day—about 24 hours and 40 minutes]. Curiosity has two computers, A and B. We landed on A, swapped to B due to [a NAND memory anomaly early on (Sol 200)](https://llis.nasa.gov/lesson/11201). For years, we were chugging along on B, until one day there was a problem—B booted up, but it couldn’t mount its drive partition. We’d never seen this before. To preserve B’s data, we swapped back to A, which we hadn’t trusted in two thousand Sols. A also had a degraded memory, with only two gigabytes of usable storage space instead of four. We painstakingly transferred data from B over to A and then down to Earth, and eventually we ran out of stuff we wanted to transfer, which was really good, because A then started acting funny in the same way it did on Sol 200. It was acting like its memory was coming unsoldered. That’s bad.

We quickly swapped back to B, formatted it, and got it working again. The problem then became that we couldn’t trust A’s memory at all, but we needed a second computer as a “lifeboat” for diagnostics and transfers if B failed again. We realized we had one other place of memory: where we keep our flight software. We have four copies of the flight software (two current versions and two older versions) in different banks of very small amounts of memory, just 32 megabytes each. What if we just jettisoned the old flight software copies and used that 64-megabyte NOR memory as our file system for computer A?

So [that’s what we did](https://ieeexplore.ieee.org/document/9697661). It was so elegant! Computer A is operating with less than 1 percent of its original memory, but we can run a mission on it. A small mission, but we haven’t had to jettison any core capabilities. We can still drive, we can manage data, we can even theoretically do science. Everything works fine, just much slower and much smaller. That flight software release was even called “[R-Hope](https://www.computer.org/csdl/proceedings-article/smc-it/2021/856000a007/1ANLcTE5g3e)“ because we hoped it would work.

**What are the constraints on Curiosity’s lifespan?**

**Holloway:** Our biggest hardware challenge is [wheel wear](https://spectrum.ieee.org/if-necessary-mars-rover-curiosity-could-rip-its-own-wheels-off-to-stay-mobile). It looks like we’re driving on this sandy terrain with some rocks in it, and our intuition said that we could just drive over these rocks and they’d get pushed down into the sand and it would be no big deal. But what we ended up seeing was that those little rocks are actually the tips of giant boulders buried in the sand, and they’re razor sharp. Our wheels were getting ripped apart driving over them, especially our front wheels, so [we started driving backwards](https://www.jpl.nasa.gov/news/curiosity-adds-reverse-driving-for-wheel-protection/).

We also monitor consumables. We consider the number of times we move our actuators. That’s a consumable. Curiosity hasn’t [taken a selfie](https://www.nasa.gov/image-article/curiositys-dusty-selfie/) in a while, and one of the reasons is that it’s really hard on the joint actuators. Our onboard memory is a consumable, but surprisingly we’re not anywhere near our life cycle for memory. Our biggest consumable is power; we have an [RTG](https://mars.nasa.gov/internal_resources/788/), a [nuclear power](https://spectrum.ieee.org/tag/nuclear-power) source, which decreases its output as it ages.

Newer missions are flying [Snapdragon](https://www.qualcomm.com/snapdragon/overview) [processors], but Curiosity’s RAD 750 is a power hog. One of the things that we’ve rolled out that’s going really well is a way of reducing the amount of time we spend with the computer powered on, by harvesting time when we finish activities early and going to sleep, which lets us turn off the computers and some of the heating. Another thing we’re looking at is doing stuff in parallel when we’re on, like being able to drive or use the arm while communicating with an orbiter.

So power is decreasing, and that’s causing us to do all this parallelism work and become more efficient and nuanced in the way we operate. But we are not having any degraded science output at this time. Our wheels are still going, our arm is still okay for now, knock on wood. I would say maybe the bottleneck is budget.

Curiosity Rover’s Impact on Future Mars Exploration
---------------------------------------------------

**What have you learned from Curiosity that will improve future missions?**

**Holloway:** As an embedded flight software person, I think about how we can change, add, or modify software capabilities during the mission. There’s definitely a sweet spot for loading and patching flight software—some of these concepts were pioneered on Spirit and Opportunity and then inherited by Curiosity and Perseverance, making it easier to understand and change the software.

Some of the things that I wish we had now on [the Mars Science Laboratory] include a better understanding of where our power is going. I want to see how much power each component is drawing every minute, so that we could architect a software system that could balance loads better. We have some of this information that was built in by the engineers who designed the rover, but as an operator, I want something slightly different. So if I were building a mission, I would have those discussions earlier and get operators into the room to say, “what do you want your data products to look like?”

The key takeaway for designing future missions is to talk to all your users early in the design process. It needs to happen upfront.

**What does Curiosity’s long-term future look like?**

**Holloway:** That’s a conversation that happens, and it’s a really delicate one. We have a lot of science instruments, and a lot of them have to do with contact science and sampling and rely on the arm. If we lose the arm, what science can we still do? Well, we have a lot of remote sensors too, like cameras, environmental sensors, and radiation sensors. All of these things are important for the future of [space exploration](https://spectrum.ieee.org/tag/space-exploration) and humans on Mars.

From a power perspective, our RTG is projected to start degrading science output in the sixth extended mission, but we’re going to be fine through 2035 and potentially even beyond that. So we have a long and exciting future ahead of us. We need to figure out the best way of operating within our constraints, but we’re still kicking.

From Your Site Articles

Related Articles Around the Web