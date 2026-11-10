---
title: "Bitter Lessons from the ISSpresso"
url: https://mceglowski.substack.com/p/bitter-lessons-from-the-isspresso
clipped: 2026-06-17 01:05:25
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Bitter Lessons from the ISSpresso](https://mceglowski.substack.com/p/bitter-lessons-from-the-isspresso)

## Digest Summary
None

## Discussion Summary
Comments collectively praise the visual quality and comprehensiveness of the fracture‑control flow diagram, describing it as striking, thorough, and artistically impressive. The accompanying explanations are valued for clarifying the high cost and difficulty of space projects. Readers also express interest in the inverter discussion, noting practical observations about small heating devices affecting inverter performance and requesting deeper insight into how inductive versus resistive loads impact design. The Pressurized Payloads Interface Requirements document receives similar appreciation for its detailed diagrams and potential aesthetic uses.

---

## Full Article

The Italian space agency’s official technical report on designing the ISSpresso barely masks their astronauts’ horror at the conditions they found when they first drifted aboard the International Space Station. The Americans were up there drinking instant coffee, like *animali*.

After two years, four prototypes, and a great deal of paperwork, Lavazza and the Italian space agency sent a proper espresso machine to the ISS in 2015. On Earth, a basic Lavazza espresso maker costs about $150 and weighs 3.5 kilograms. The coffee machine’s spaceborne cousin was a 20kg box about the size of an oven. The cost to build it was not disclosed, but was likely in the single-digit millions

Asking how a coffee machine got to be so huge and expensive in space is a good way of understanding the cost drivers in human space flight.

Espresso machines are not particularly lethal on Earth, but almost anything on the space station can kill the crew if it’s built wrong. So the ISSpresso had to prove to NASA’s satisfaction that it would not take out the station’s electrical system, interfere with the radio, leak boiling water, catch fire, dazzle the crew with bright lights, electrocute anyone, be dangerously hot, make loud noises, emit noxious gas, shatter into fragments, smell weird, or shake apart in the harsh conditions at launch. (The sharp pin that punctures the coffee capsule required a special safety waiver.)

The authors of the technical paper on ISSpresso include a list of some of the NASA standards they had to comply with to get their machine certified for launch and orbital coffeemaking.

These documents are not light reading. It can be tempting to dismiss them as NASA run wild, and there are certainly some requirements (like handle shape or enclosure color) that seem arbitrary. There is also a lot of bureaucratic connective tissue, like the standards for harmonizing processes between NASA and the European and Japanese space agencies, who all build their hardware to slightly different specs.

But most of the technical requirements in this list have substance. They fall into a few broad categories:

* Making sure nothing on the payload damages the space station, either in normal operation or if something goes haywire.
* Lots and lots of fussiness about electrical behavior and electromagnetic interference.
* Consistency in interface design with other ISS hardware.
* Demanding proof that the ISSpresso can take a physical beating (especially during launch), endure kicks from astronaut feet, sudden decompression to vacuum, abrupt surges or sags in voltage and water pressure, and other environmental insults.
* Ensuring the heating element doesn’t burn anything or set itself on fire. This is a trickier requirement in space, where air doesn’t cool things by convection.
* Fluid handling requirements specific to the zero g environment. The ISSpresso has to contain spills and not fill the cabin with a mist of boiling water. It also has to play nice with ISS plumbing.
* Astronaut-proofing the enclosure, which will inevitably be kicked and used as a handhold. This includes making sure nothing can hurt a clumsy astronaut (sharp edges, pointy switches, pinch points) or break if it’s yanked on.
* Proving that the ISSpresso won’t shake apart during launch or damage whatever it launches with.
* Antimicrobial measures for all wetted surfaces and plumbing.
* Basic OSHA-type stuff like noise limits.

None of these requirements are frivolous, and some of them reflect dangers unique to spaceflight. If the plastic cover shatters on your espresso maker back home, you’ll be mildly inconvenienced. But if that cover shatters in space, it can pose an acute inhalation and eye hazard.

The many technical requirements are enforced by the Safety Review Process, itself a highly regimented standard. The Process takes designers through a series of project milestones and official reviews that ultimately satisfy NASA that each requirement on their lists has been met.

The Safety Review Process begins with a friendly chat about general design ideas, and then ratchets up in rigor and unpleasantness. By the final milestone, a NASA bureaucrat is shining a light bulb in your face and screaming at you to confess everything you know about mission risk. It’s not enough to tell NASA that you plan to put your payload on a truck and drive it to Kennedy Space Center for launch; you have to analyze the g-forces for every crane movement and specify how fast the truck will go. Any conceivable failure mode has to be identified in a Hazard Report, along with the proposed fix, and that fix has to be certified.

A helpful flowchart from a NASA safety document (SSP 52005 Revision C) showing how to handle fracture risk

There is a truism in aerospace: when you pay $500 for an aviation-certified thumbtack, what you’re really paying for is the ten binders of compliance documents, certifications, and tests that accompany it through the production process, along with a promise that someone will go to jail if any part of that process is falsified.

The Process is painful, but it’s not unique to NASA. We run versions of it in aviation, military, and medical contexts, wherever human lives are at stake. It is often ridiculous and everyone hates it. But some version of it is the only way to be sure systems behave as intended.

Let me illustrate this with a moving personal anecdote!

I live in a solar-powered home in rural New Mexico. The house is not connected to the electrical grid; instead, power from solar panels feeds a rack of batteries, and a machine called an inverter draws power from the batteries and turns it into household current.

The solar system in my home is supposed to be decoupled. One wall of the electrical closet has all the solar gear; the other has a standard junction box with circuit breakers like you find in a normal home. From the house’s perspective, alternating current flows in just like it would from a power line. And on the solar side of the system, the inverter doesn’t know or care about what’s happening inside the house. As long as the total power draw stays under a generous maximum, everything is supposed to just work.

That’s the theory.

But after upgrading the inverter last year, I found myself beset by electrical gremlins. A few times a day the lights would dim, and I could hear the pump in my aquarium start to make a choking noise. At those times, a display on the inverter showed the A/C voltage dipping. Sometimes the inverter would reboot, taking down power for the whole house for a minute. There was no discernible pattern in when or how often this happened.

I thought I could live with the problem until it started killing my furnace. The first couple of times, the victim was a transformer, a $25 part on the circuit board that I learned to replace myself. But the third time around, the voltage drop burned out the entire logic board, forcing an expensive repair that left me without heat for a week.

At this point it was November, and heating the house had become a game of Russian roulette. I knew that every minute the furnace stayed on, a blip in the electrical system might kill it. No one I talked to could identify a cause. I had to figure out what was causing the drops in voltage before the house became unlivable.

Being a software guy, I decided to try binary search. I turned off half the circuit breakers to the house one day, then the other half the next, to see which side the problem was on. Soon I had isolated it to one part of the house, and then to a single circuit in the bathroom.

There I found the culprit: a Japanese shower toilet.

The toilet had a small heating element that turned on and off to keep the water in the bidet attachment and seat warm. Whenever the heater came on, its modest appetite for electricity was somehow enough to destabilize the inverter, which then briefly delivered lower voltage to the entire rest of the house. While most appliances could handle these dips, the furnace could not, and died dramatically. Even though the toilet’s power demand was low, there was something about its Japanese expectations for voltage and frequency (just a little bit off the US standard) that made the American-made inverter crazy.

Figuring that out took me several weeks and a few thousand dollars. My mistake was believing that the power system really was decoupled—that nothing in the house could affect things upstream of the junction box. That is what the inverter specs and circuit diagrams all said. That is what customer support told me. But it wasn’t true.

Since that time, I’ve learned that small heaters (like coffee makers or kettles) can be kryptonite to an inverter, and that this is common folk knowledge among solar installers. But the consequence, that a guest can do damage to my home by plugging in a hair dryer, is still unsettling and counterintuitive.

This is the class of problem all those NASA interface requirements are trying to forestall. If you’ve ever had a faulty wiring harness in your car (hello Jeep owners!) you know what a nightmare it is to try to chase down intermittent, poorly localized faults. NASA inflicts eye-watering certification costs on itself and its partners to avoid trying to diagnose this stuff in space, where half the systems can’t be powered off, and where there’s a high chance of killing the crew if you break something.

Undoubtedly, some proportion of NASA’s Safety Review Process is overkill. But even if we could cut regulatory overhead by 75%, a device like the ISSpresso would still cost a few hundred thousand dollars to develop and end up built like a tank. The blast radius of malfunctioning hardware on human-rated spacecraft is simply too big to avoid doing some version of the safety dance.

This has uncomfortable consequences for space dreamers.

There is a widespread belief that launch costs are what has been holding back space exploration, and a corresponding excitement now that they are dropping by a potential two orders of magnitude. Many SpaceX fans in particular believe that Starship solves every problem by being huge and cheap. And they are partially right! It would be much easier to send people to Mars on a 1200 ton rocket than to try to fit all the equipment they need into a 60 ton transit habitat engineered like a Swiss watch.

But cheap launches can’t solve the equipment problem. Ultimately, whatever we put inside the spacecraft has to work as advertised, and until we have hundreds of person-years of experience living in space habitats, the only way to guarantee that will be an expensive process of flight qualification and testing.

That means future human missions to space will have the same cost profile as big space telescopes do today—a few hundred million spent to launch stuff, and billions spent inventing equipment and trying to get it to work right.

A view of the impressive internal plumbing on the ISSpresso

Like all our problems, this one gets worse on Mars.

The defining feature of a human mission to Mars is that risks are sequential and cumulative. Every link in the chain has to go right, or the mission fails. This means early visits to Mars will have safety and reliability requirements that make the Space Station look like a middle school science fair.

These requirements will be especially tight for the surface part of a mission. Any equipment that lands on Mars will have to demonstrate that it can launch from Earth, sit dormant for six months, survive entry and landing, and then work in partial gravity and dust without breaking for 17 months. Machinery that is pre-positioned on Mars in advance of the crew (a common risk-cutting measure in mission designs) will also have to prove that it can sit out in the weather for two or more years.

To make matters worse, any payloads sent to the surface will be severely constrained by weight. This is not for want of big rockets to send them to Mars, but a consequence of the fact that landing heavy payloads is hard, with the difficulty going up as some integer exponent of the landed mass.

Whenever you need a combination of light weight, reliability, and autonomy in a space context, it is time to bring your wallet to your lips and kiss it goodbye. We saw an example of this [last week in the context of Mars Sample Return](https://mceglowski.substack.com/p/what-happened-with-mars-sample-return), where a rover whose sole purpose was to move a few titanium tubes from the ground into a box wound up costing half a billion dollars.

The same pathology is going to bedevil us when we finally get to Mars, even if launches there from Earth are free.

Astronaut Samantha Cristoforetti enjoys a space espresso aboard the ISS

It’s pretty frustrating to enter an era of cheap rockets and still not be able to do fun things. Early Mars concepts (like NASA’s Design Reference Architectures) agonized over how to fit the mission into the minimum number of launches, which were the most expensive line item in the budget.

If Starship and New Glenn succeed, we can have all the mission mass we want. But that just runs us into the next-biggest item on the cost list, the reliability and testing issues that are the subject of this post.

So what do we do to make certification and testing cheaper?

1. **Fly more.** If there are a dozen space stations that all need an espresso maker, then that makes designing ISSpresso 2.0 and later models much easier. A proven flight record replaces a lot of first-principles testing.
2. **Fly more robots**. Robots don’t drink coffee, but there are science missions that could use a pressurized hot water source, and validating such equipment where it doesn’t pose risk to astronauts makes it easier to adapt it for human space flight later. This holds for all kind of devices and sensors that would be useful on manned spacecraft.
3. **Learn to land on Mars**. Right now we can land 2-3 tons on Mars at a time, in an error ellipse that is about 20 kilometers long. For a realistic human mission, we need to be able to land 100 tons or more at 100-meter precision, so that we can pre-position equipment and land in our favorite crater. This capability would also make it cheap to send big dumb robots in large numbers to Mars, instead of the very expensive, artisanally hand-crafted robots we send now.
4. **Fix the safety ratchet.** It is easy to add safety constraints and hard to undo them. You and I will probably die before we’re allowed to take a bottle of water through airport security again.

   Many NASA rules around software reliability date back to the 1970s and don’t make sense in the smartphone era. Harsh limits on electromagnetic interference impose a testing burden on innocent components that probably don’t need it. And some of restrictions on flammability and wiring are a hangover from the Apollo I fire in 1967. There needs to be a mechanism for relaxing rules to adapt to changing conditions, or else the space program will fossilize in its own paperwork.
5. **Let amateurs fly stuff**. People are inventive, and we should let gifted engineers try things in space without interference from the safety bureaucracy, as long as they don’t hurt anyone. Hopefully the new era of cheap launches will enable some risk-taking and invention by talented amateurs, and the stuff that doesn’t blow up can then carry over into our official space program.

1. The technical paper on designing the ISSpresso is very readable and fun. [ISSpresso Development and Operations](https://sci-hub.ru/10.1016/S2468-8967(16)30038-6) (2015) DOI 10.1016/S2468-8967(16)30038-6
2. For more on the special challenges of handling liquids in space, along with the vaguely vaginal coffee cup invented for space use, see *[How Advances in Low-g Plumbing Enable Space Exploration](https://www.nature.com/articles/s41526-022-00201-y)* (2022) DOI 10.1038/s41526-022-00201-y
3. Behold in all its splendor the [Pressurized Payloads Interface Requirements](https://snebulos.mit.edu/projects/reference/International-Space-Station/SSP57000RE.pdf) document for ISS.