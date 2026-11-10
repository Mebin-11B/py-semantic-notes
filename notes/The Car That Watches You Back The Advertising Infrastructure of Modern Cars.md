---
title: "The Car That Watches You Back: The Advertising Infrastructure of Modern Cars"
url: https://nobodyaskedforthis.lol/posts/connected-car/
clipped: 2026-06-17 01:07:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Car That Watches You Back: The Advertising Infrastructure of Modern Cars](https://nobodyaskedforthis.lol/posts/connected-car/)

## Digest Summary
None

## Discussion Summary
The comments express strong dissatisfaction with contemporary automotive technology, criticizing the integration of LLM‑generated content, cellular connectivity, and advertising infrastructure that treat drivers as data products. There is a recurring desire for a fully disconnected, simple vehicle, exemplified by a basic model without network features. Concerns also focus on the high purchase price, costly financing, and escalating insurance, which together reinforce the perception that modern cars compromise privacy and freedom while imposing financial burdens. Overall, the sentiment is negative toward current car design and business practices.

---

## Full Article

On the morning of November 24, 2025, automotive journalist Zerin Dube opened the door of his Jeep Grand Cherokee, settled into the driverâs seat, and pressed the start button. The dashboard came up. The infotainment screen ran its boot animation, blinked to the home view, and then loaded an advertisement on top of the home view. Not a service reminder, not a recall notice. A promotional offer: **$1,500 in Loyalty Retail Bonus Cash** toward the purchase of a new Jeep, timed to appear at startup, configured to linger for fifteen seconds, and programmed to return at the next ignition cycle if he failed to dismiss it quickly enough.

He photographed the screen and posted it to X. The caption: âLate stage capitalism popping up on our Grand Cherokee.â

![A Jeep Grand Cherokee infotainment screen displaying a $1,500 Loyalty Retail Bonus Cash promotional offer over the home view.](https://nobodyaskedforthis.lol/_astro/cover.CnDJPfAi_QpaIq.webp)

Zerin Dube's photograph of the startup ad, posted to X on November 24, 2025.

The photograph captured something people had been watching develop in fragments (a feature added here, a terms-of-service update there) but hadnât yet seen stated plainly. Dubeâs Jeep had not been hacked. Nothing had gone wrong. [The advertisement came from Stellantis](https://jalopnik.com/2034692/pop-up-ads-appearing-stellantis-infotainment/), the company that built the truck, over the truckâs own cellular connection, to a screen in a vehicle the owner had paid for outright.

To turn it off permanently, Stellantis directed owners to call the [Brand Connect](https://www.driveuconnect.com/contact-us.html) customer service line at 800-777-3600 during business hours.

This is a story about how a machine most people still think of as property became something else: a platform with monetized inventory and a data feed pointed back at the manufacturer. It is also about the sequence of technical decisions that made that transformation possible. The story starts, depending on where you draw the line, either in 1986 with a nine-inch Buick touchscreen, or in 2012 with a Tesla that changed everything, or in the 1990s when engineers began replacing steel cables with electronic signals and nobody outside the industry particularly noticed.

---

### Forty Years of Glass

![A 1986 Buick Riviera coupe in profile, photographed against a neutral backdrop.](https://nobodyaskedforthis.lol/_astro/buick.DHtR1vu9_Z2cjkq1.webp)

The 1986 Buick Riviera. The first production car with a touchscreen.

The [1986 Buick Riviera](https://automotivehistory.org/the-first-car-with-a-touchscreen-is-from-1986/) arrived in showrooms carrying what GM called the Graphic Control Center: a nine-inch cathode-ray tube touchscreen managing 91 vehicle functions without conventional switches or knobs. It beeped audibly with each touch. Drivers complained it was distracting to navigate at speed. It was dropped after two model years.

![Close-up of the 1986 Buick Riviera&#x27;s nine-inch CRT touchscreen mounted in the center console, displaying menu options for trip, audio, climate, and gauges.](https://nobodyaskedforthis.lol/_astro/buick-touchscreen.Cfub2Byy_16RnKY.webp)

GM's Graphic Control Center. Ninety-one functions, one CRT, an audible beep on every press. It survived two model years.

The concept spent the next fifteen years in development. Lexus introduced a touch-operated navigation system in the 2001 LS430 that was functional and cautious. BMW installed iDrive in the 2002 7 Series: an 8.8-inch display controlled by a single rotary knob that replaced most of the center console controls. Drivers trying to adjust the climate control while moving found themselves drilling through nested menus with a dial. BMW relented and added physical shortcuts after two years of customer complaints. iDrive survived its early reputation and eventually became one of the better systems in the industry, but the lesson (that removing buttons is not the same thing as improving control) did not travel as widely as it should have.

The decisive break came in 2012. [Tesla began deliveries of the Model S](https://www.techradar.com/news/car-tech/the-new-tesla-s-has-the-most-insane-in-car-touchscreen-multimedia-system-ever-1185159) with a 17-inch portrait-orientation touchscreen at its center, running a full web browser, integrated with Google Maps, and controlling virtually every function in the car: climate, suspension, sunroof, charging settings, media, navigation. There was a steering wheel with shortcut keys, window switches, a hazard light button, and a glove box release. Everything else was the screen.

[Safety researchers pointed to Fittsâs Law](https://www.nngroup.com/articles/tesla-big-touchscreen/), the principle that acquiring a touch target requires visual confirmation in a way that a physical knob with a learned position does not, and published studies showing that touchscreen-heavy interfaces increased cognitive load. The studies were accurate. The market did not care. Within a decade, a 12-inch screen was unremarkable. Mercedes-Benz developed the Hyperscreen, a 56-inch curved display spanning the full width of the EQS dashboard with three screens beneath a single piece of Gorilla Glass. The Jeep Grand Wagoneer shipped with seven screens.

![The Mercedes-Benz EQS Hyperscreen: a 56-inch curved display spanning the full width of the dashboard, divided into three panels under one continuous piece of glass.](https://nobodyaskedforthis.lol/_astro/hyperscreen.DYnycms2_1nW43D.webp)

The Mercedes-Benz Hyperscreen. Three displays, fifty-six inches, one piece of Gorilla Glass.

This proliferation of screens has a useful parallel in consumer electronics. [We have previously noted](http://nobodyaskedforthis.lol/posts/anker-nano-45w/) that Anker added a small OLED display to its Nano 45W charger, a screen that tells you in real time how many watts your phone is drawing, which your phone is already displaying six inches away. The automotive version of this logic produced instrument clusters that display your speed digitally while an analog speedometer sits alongside it, and eventually produced dashboards where a screen replaces the climate knobs, the audio controls, the seat heater buttons, and the parking brake switch, each function now two or three taps into a sub-menu. The screen was not added because it made these things easier. The screen was added because a screen is what modern things look like, and because once installed, it could be updated remotely and eventually monetized.

---

### From Cables to Code

The touchscreen is the visible part of a deeper transformation: the systematic replacement of the carâs mechanical connections with electronic ones.

Until the late 1980s, the relationship between a driverâs inputs and a carâs physical systems was largely direct. Pressing the accelerator pulled a steel cable that opened the throttle body. Turning the steering wheel rotated a column connected mechanically to the front wheels. The brake pedal pushed hydraulic fluid through lines to calipers at each corner. Driver intention was transmitted by force.

[Drive by wire](https://en.wikipedia.org/wiki/Drive_by_wire) began replacing the accelerator cable in production vehicles in the early 1990s. Instead of a physical cable, a sensor reads pedal position and reports it to an engine control unit, which commands the throttle electronically. The advantages were real: the ECU could coordinate throttle position with fuel injection, transmission shift points, traction control, and stability management in ways a cable could never accommodate. By the 2000s, electronic throttle control was standard across virtually the entire industry. The physical cable between the pedal and the engine was gone.

Steering followed. Hydraulic power steering (an engine-driven pump moving fluid to assist the driver) was replaced by electric power steering, which uses a motor on the rack instead. Most electric power steering systems still retain a mechanical column: turn the wheel and the wheels follow through a physical connection. [Steer-by-wire](https://gomechanic.in/blog/the-by-wire-system-explained/) eliminates even that. [Infiniti introduced a production steer-by-wire system in 2013](https://en.wikipedia.org/wiki/Drive_by_wire), retaining a mechanical fallback. In a full steer-by-wire vehicle, the steering wheel is a sensor and the wheels are moved by actuators. The driverâs input is a signal, not a force. Brake-by-wire follows the same trajectory, replacing the hydraulic master cylinder with electronic actuators, and is present in several current production models.

This architecture is connected internally by the [CAN bus](https://en.wikipedia.org/wiki/CAN_bus) (Controller Area Network), a communications standard from the 1980s that allows a vehicleâs dozens of electronic control units to talk to each other over a shared network. The CAN bus was designed for reliability within a closed system, and it has almost no built-in authentication. When a message arrives on the bus, there is no native mechanism to verify who sent it. The assumption when the standard was designed was that nothing external would ever reach the bus. That assumption dissolved when vehicles were given cellular modems and internet-connected infotainment systems.

---

### The Update That Came While You Slept

Tesla introduced [over-the-air (OTA) software updates](https://recharged.com/articles/tesla-over-the-air-updates-explained) as a production feature with the Model S in 2012. The premise was genuinely useful. Rather than requiring a dealership visit for software changes, the car connects to Wi-Fi at night, downloads an update, and installs it while parked. Bug fixes, safety improvements, new features, all deployed remotely across the entire fleet.

The early demonstrations were compelling. When Consumer Reports cited inadequate braking distances in the Model 3, Tesla issued an update within days that reduced stopping distance by 19 feet. During Hurricane Irma in 2017, Tesla temporarily unlocked additional range on software-limited batteries for Florida owners who needed to evacuate.

OTA updates are now standard across the connected vehicle industry. BMW, Ford, Volkswagen, and GM deploy them regularly. The capability is table stakes.

What has become clearer is that the same mechanism that delivers improvements can remove features, restrict settings, and gate capabilities behind payment, often without the ownerâs agreement and sometimes without notice. [Tesla removed the adjustable regenerative braking setting](https://www.autoevolution.com/news/tesla-ota-update-reinstates-low-regenerative-braking-mode-214000.html) from its vehicles in a 2020 update, leaving drivers with a single level regardless of preference. The option partially returned in 2023. Tesla also removed Autopilot features from used vehicles, requiring new owners to repurchase capabilities the previous owner had paid for. The hardware remained, but access did not transfer with the title.

[Tesla settled a class action in 2021 for $1.5 million](https://www.hotcars.com/tesla-software-update-cut-ev-range-owners-move-to-sue/) after owners alleged an OTA update had reduced battery charging capacity in Model S vehicles. A subsequent suit alleged a Model S and Model X update reduced driving range by 20 percent, with some owners receiving error codes indicating degraded or inoperable batteries. Some paid over $500 to third parties to reverse the update. Others faced battery replacement bills exceeding $15,000.

[BMWâs heated seat subscription](http://nobodyaskedforthis.lol/posts/bmw-heated-seats/), eighteen dollars a month to operate warming elements already wired into the car, is the same logic applied more visibly. BMW eventually withdrew the program in most markets after the backlash, but the withdrawal did not change the underlying architecture. The seat hardware is still in the car, and the software still controls whether it works.

Polestar sells a 68-horsepower performance upgrade as an OTA download. The question of whether a manufacturer can alter a productâs capabilities after sale via software has not been definitively resolved legally. In practice, the terms of service accepted at purchase typically grant broad rights over software modifications. You bought the hardware. They retained control of what it does.

This pattern of products that continue to require your compliance after youâve paid for them, that collect telemetry, that require an account, that update overnight and behave differently in the morning, is not exclusive to cars. [We have covered it in the Theragun](http://nobodyaskedforthis.lol/posts/theragun/), which now connects to your wearables and tracks recovery sessions, and [in the Ember mug](http://nobodyaskedforthis.lol/posts/the-mug-firmware/), which refuses to heat your coffee until it finishes a 40MB firmware update. Then thereâs [the Mill compost bin](http://nobodyaskedforthis.lol/posts/mill-food-recycler/), which costs $999 and reports your food scraps to a cloud. The car is the largest and most consequential version of a phenomenon already well underway in the kitchen, the bathroom, and the gym bag. Everything is becoming a subscription with telemetry, and the vehicle is merely the highest-stakes implementation of that design philosophy.

---

### The Attack Surface

In July 2015, security researchers [Charlie Miller and Chris Valasek](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) sat in an office in St. Louis and remotely accessed a 2014 Jeep Cherokee being driven by journalist Andy Greenberg on a highway. Through a vulnerability in the Uconnect infotainment system, and from there to the CAN bus, they commanded the air conditioning, the radio, the windshield wipers, and the transmission. They cut the engine at highway speed and disabled the brakes in a parking lot.

Chrysler recalled 1.4 million vehicles. The demonstration made a point that has only grown more relevant: the infotainment systemâs cellular connection is a path to vehicle systems that were never designed to receive commands from outside.

In 2024, researchers led by Sam Curry found a [vulnerability in Kiaâs web portal](https://www.helpnetsecurity.com/2025/04/04/cybersecurity-risks-cars/) allowing them to reassign control of the internet-connected features of any Kia manufactured after 2013. The vulnerability was in the manufacturerâs cloud infrastructure, not the car itself. The cloud talked to the vehicleâs telematics unit, which talked to vehicle systems. In late 2024, a data leak from Volkswagenâs software subsidiary Cariad exposed [precise GPS location data for approximately 800,000 electric vehicles](https://arxiv.org/pdf/2508.15306) across VW, Audi, Å koda, and SEAT. The data was stored in Amazon cloud infrastructure with insufficient access controls. It wasnât extracted through a sophisticated exploit; it was simply accessible.

Researchers at Northeastern University [published findings in early 2026 on Teslaâs cellular stack](https://news.northeastern.edu/2026/02/18/connected-cars-hacking-research/), identifying vulnerabilities to IMSI catching attacks (techniques that spoof cellular towers to intercept traffic). Tesla acknowledged the vulnerabilities were in modem components supplied by Qualcomm and Quectel. The modem is in the car, and the vulnerability is present regardless of whose name is on the component.

Audi vehicles through at least 2024 shipped with software containing [well-known vulnerabilities](https://www.helpnetsecurity.com/2025/09/09/connected-car-cybersecurity-europe/), including components with no active maintainers. Of automotive cybersecurity incidents between 2023 and 2024, [92 percent were remote attacks](https://www.einfochips.com/blog/cybersecurity-for-the-next-gen-mobility/).

The cellular modem that receives Stellantisâs promotional pop-up is the same modem that received the Uconnect exploit a decade earlier. Always-on connectivity, cloud-connected accounts, and logged-in user profiles are each both a requirement for advertising delivery and a component of the attack surface available to anyone who finds a way in.

---

### Three Companies Want to Be Your Carâs Operating System

While automakers fight over whose software runs the dashboard, three technology companies have been running a parallel campaign to own the voice layer: the microphones, the assistant, the conversational interface between driver and vehicle. Each has taken a different approach. All three have ended up in the same place, which is the car interior, listening.

**Google** moved earliest and most completely. The Polestar 2, launched in 2020, was the first production vehicle to run [Android Automotive OS natively](https://en.wikipedia.org/wiki/Polestar_2). Not Android Auto, the phone-mirroring app, but Android Automotive, a full operating system running on the vehicleâs own hardware, independent of any connected phone. The distinction matters: a car running Android Automotive is running Google software at the level of the operating system. Google Maps, Google Assistant, and the Google Play Store are built into the vehicle itself. The carâs infotainment is, in a meaningful sense, an Android device.

[The list of vehicles now running Google Built-in](https://www.androidheadlines.com/android-automotive) is long and growing: multiple Volvo and Polestar models, the Chevrolet Silverado, Tahoe, Suburban and Equinox. The GMC Sierra and Yukon and Hummer EV, the Cadillac Lyriq and Escalade IQ and CT5, the Honda Accord and Prologue, the Ford Explorer (2025+), the Lincoln Aviator and Nautilus, the Nissan Rogue, and as of 2026, the Mazda CX-5.

Volvo has deepened this relationship significantly, [announcing in 2025 that it would serve as one of Googleâs reference hardware platforms](https://www.volvocars.com/intl/media/press-releases/6B411DC79F4F8965/) for future Android development in cars. The companies demonstrated Google Gemini running in a Volvo EX90 at Google I/O 2025. Gemini is now rolling out via OTA update to Polestar and Volvo vehicles with Android Automotive OS, a conversational assistant capable of handling compound requests like âfind a supermarket on my way home and text Joe that Iâm on my way.â The carâs voice interface has become a large language model deployed in a vehicle that also runs Google Maps, Google Play, and Googleâs advertising infrastructure. The data implications of this combination have not been extensively discussed in the marketing materials.

**Amazon** took a different approach. Rather than replacing the operating system, get the assistant into whatever is already there. The [Echo Auto](https://www.amazon.com/All-New-Echo-Auto-release-Alexa/dp/B09X27YPS1) is a small rectangle (roughly credit-card-sized, about as thick as a box of Tic-Tacs) that sticks to the dashboard, connects to the driverâs phone via the Alexa app, and plays through the carâs existing audio system via Bluetooth or the auxiliary input. Five microphones, tuned to hear over road noise and air conditioning. It costs roughly $55.

![The Amazon Echo Auto: a small black rectangle, roughly the size of a credit card, mounted to a car dashboard, with a row of microphone perforations along the top edge.](https://nobodyaskedforthis.lol/_astro/echo.BJdA4lhS_3aulW.webp)

The Echo Auto. Five microphones, one Amazon logo, the smallest possible Alexa.

The Echo Auto is, functionally, the smallest possible implementation of the thing Amazon already installed in your kitchen, your living room, and your bedroom. Amazon has moved systematically to put Alexa in every room of every home, and the car was the remaining room. [We covered the Amazon Smart Microwave](http://nobodyaskedforthis.lol/posts/microwave/), the appliance that responds to âAlexa, microwave for two minutesâ the same way pressing the button marked â2:00â does. The Echo Auto extends that logic to a room that moves at seventy miles per hour, where hands-free control has a slightly stronger safety argument and the commercial opportunity is considerably larger.

For vehicles that donât need the aftermarket add-on, Amazon has built Alexa directly into the infotainment systems of [an extensive roster of manufacturers](https://www.amazon.com/alexa-auto/b?node=17744356011): Acura, Alfa Romeo, Audi, BMW, Ford, Lincoln, Mazda, MINI, Nissan, Rivian, and Volkswagen, among others. The integration depth varies considerably by brand and model year. Some allow voice control of vehicle functions; others treat Alexa as a media and smart-home interface that happens to be accessible from the car. Lexus offered Alexa integration and then [discontinued it in October 2023](https://www.gearbrain.com/which-cars-have-amazon-alexa-2525958778.html). Alexa integration with Lexus vehicles is no longer functional.

The commercial logic of Amazonâs automotive ambitions is not opaque. Alexa already routes music purchases, smart home device sales, and product reorders through Amazonâs commerce infrastructure. A driver who asks Alexa to add something to their shopping list, find the nearest gas station, or order paper towels for delivery has done so through a system that Amazon owns end to end. The car is another point of purchase. [We have previously noted](http://nobodyaskedforthis.lol/posts/amazon-astro/) that the Amazon Astro, a $1,600 home robot discontinued in 2024, was essentially a presence-and-observation device whose primary capability was being in the room with you. The Echo Auto is that logic made portable and more plausible: a microphone in your commute, connected to the largest commercial infrastructure in American retail.

**Spotify** tried a different approach entirely, and it failed so completely that it serves as a useful data point.

The [Spotify Car Thing](https://carthing.spotify.com/) launched in early 2021 with an invite-only rollout, reached broader availability in February 2022 at $89.99, and was discontinued from production by July 2022 after Spotify took a [$31 million write-down](https://www.engadget.com/spotify-stops-manufacturing-car-thing-132028146.html). It was a physical controller for Spotify: a four-inch touch screen, a large rubberized dial, four shortcut preset buttons, and a microphone for voice commands. It mounted to the dashboard via vent clips and connected to your phone via Bluetooth. It streamed nothing independently. All audio came through the paired phone, over the phoneâs data plan, through the carâs audio system via a separate Bluetooth connection. It was, in the most literal sense, a remote control for an app.

![The Spotify Car Thing mounted to a car vent: a four-inch touchscreen displaying playback controls, with a large rubberized rotary dial and four shortcut buttons below.](https://nobodyaskedforthis.lol/_astro/carthing.BYlnOwSM_gRVTD.webp)

The Spotify Car Thing. Manufactured at a loss for sixteen months, then remotely deactivated on December 9, 2024.

Spotify described the Car Thing as an [âexploration,â](https://www.musicbusinessworldwide.com/spotifys-car-thing-officially-non-operational-less-than-three-years-after-it-rolled-out-in-the-us/)a way to learn more about how people listen in the car. What they learned, apparently, was that people would not pay $89.99 for a Spotify remote when their phone already controlled Spotify, in a world where CarPlay and Android Auto already displayed Spotify on the dashboard screen. Production ended after five months. In December 2023, Spotify announced that all existing Car Things would be [completely deactivated on December 9, 2024](https://www.billboard.com/business/streaming/spotify-car-thing-deactivated-stop-working-date-1235693625/). Not unsupported. Deactivated. Users were directed to reset the device and bring it to an e-waste recycling center. Billboard called it âthe Zune of the 2020s.â A class action lawsuit followed. Spotify eventually offered refunds for customers who contacted support before January 14, 2025.

Enthusiasts attempted to develop custom firmware to keep the devices functional after deactivation. Spotify subsequently tightened its API access, making third-party firmware harder to sustain. The Car Thing was bricked not once but twice, first by the shutdown and then by the API restrictions that foreclosed the communityâs workaround.

The Car Thing sits neatly in a category this publication has written about extensively: hardware that exists to solve a problem the user has not expressed, manufactured at a loss, discontinued before it reaches the userâs second birthday, and ultimately sent to an e-waste facility while still physically functional. The [Coolest Cooler](http://nobodyaskedforthis.lol/posts/the-coolest-cooler/) raised $13.3 million and delivered frustration. The Car Thing raised no outside capital, sold at a loss, and delivered a functional product that was then remotely killed. Both are monuments to the difficulty of making people buy something they donât need for a problem they donât have. The Car Thingâs epitaph, in the marketing language of its creator, was that it âunlocked helpful learnings.â The learnings, apparently, were that this was not worth doing.

---

### The Screen You Canât Escape

Before examining what is happening inside vehicles, it helps to map the advertising environment that surrounds the car on every side. The driving experience, from departure to destination and every stop between, passes through an advertising infrastructure so dense and continuous that it begins to resemble infrastructure itself, the way the highway is infrastructure: something that shapes the journey without being the journeyâs purpose.

**At the pump.** [GSTV (Gas Station TV)](https://www.adexchanger.com/ctv-roundup/gstv-wants-to-turn-gas-stations-into-a-video-ad-marketplace/) runs video content and advertising across screens at more than 27,000 gas stations in the United States, reaching approximately 115 million unique monthly viewers. The viewer is the person pumping gas. You swipe your card, lift the nozzle, click it into the filler neck, squeeze the handle, and lock the trigger. The screen above the keypad starts playing video at you, at a volume calibrated to be heard over the pump motor. You cannot mute it. You cannot turn away from it without turning your back on the nozzle. There is one channel, no DVR, no channel surfing, no means of fast-forwarding, and the average fueling session runs four to five minutes.

![A Conoco gas station fueling pump with a video display embedded above the keypad, playing a full-motion advertisement to a customer holding the nozzle.](https://nobodyaskedforthis.lol/_astro/conoco.ZMupxxLE_Z29DEat.webp)

A GSTV display, embedded in the pump. Average viewing time: four to five minutes per fill-up. The audience cannot leave.

GSTV presented research at the 2024 IAB NewFronts claiming its [attention metrics surpass digital video, social media, connected television, and linear broadcast](https://www.admonsters.com/new-study-reveals-gstv-dominates-ad-attention/), with 7,702 attentive seconds per thousand impressions and brand recall rates 1.5 times above industry benchmarks. [PepsiCo has incorporated GSTV into its core video strategy](https://digiday.com/future-of-tv/extension-broadcast-buy-advertisers-buying-ads-gas-station-screens/). Spark Foundry, one of the larger media buying agencies, consolidated GSTV into its video team alongside television and streaming buys. GSTV pitches at the annual upfront market, competing for television network budgets.

The targeting is more sophisticated than it appears. [GSTV works with a data partner that collects mobile device IDs](https://www.adexchanger.com/ctv-roundup/gstv-wants-to-turn-gas-stations-into-a-video-ad-marketplace/) from phones near its gas station screens, then matches those against third-party providers including Experian and Acxiom to create audience segments. GSTV cannot identify the specific individual at the pump, but it can identify that people who frequent a particular gas station in a particular zip code tend toward homeownership or outdoor recreation, and route appropriate creative to that screen. Conversion is measured through partnerships with Foursquare that track subsequent retail visits. The pump does not know your name. It knows your phone is there, and it knows where your phone goes next.

**Inside the store.** You hang the nozzle back on the pump, walk through the automatic doors for a Slurpee, and the speakers in the ceiling are running an ad for Slurpees.

In November 2024, 7-Eleven announced a partnership with [Qsic](https://www.getqsic.com/), an audio retail media company, to build what it explicitly describes as one of the largest commercial radio stations in America. Gulp Radio was broadcasting in more than 4,000 stores as of April 2025, with expectations for deployment across more than [] 12,000 7-Eleven, Speedway, and Stripes locations by the end of July](<https://www.cstoredive.com/news/7-eleven-qsic-radio-station-gulp-media/750712/>), well ahead of original projections.

Networked smart speakers stream individual audio feeds into each store. [Ads are targeted by location and time of day](https://www.cstoredive.com/news/7-eleven-qsic-radio-station-gulp-media/750712/). Coffee ads in the morning, when coffee demand peaks. The system âzonesâ audio so that different content plays in different parts of the store; the beer ads play from the speaker over the beer cooler, audible while you have the door open and a six-pack in your hand. Voice talent is generated by text-to-speech, eliminating recording studios and allowing campaigns to update instantly. A sensor measures ambient decibel levels and adjusts speaker volume automatically, ensuring audibility above store noise while also confirming for advertisers whether and how loudly each ad played. [Products advertised on Gulp Radio see average sales lift of 5 to 9 percent](https://www.cstoredive.com/news/7-eleven-qsic-radio-station-gulp-media/750712/). A Slurpee promotion achieved 11 percent unit sales growth. Qsic plans to integrate 7-Elevenâs transactional data to optimize ad frequency by purchase pattern.

Qsic is not alone. In 2023, Mood Mediaâs Vibenomics division and Stingray Advertising announced a partnership creating what they described as the [largest U.S. in-store retail media network](https://www.globenewswire.com/news-release/2023/07/25/2710344/0/en/Mood-Media-s-Vibenomics-and-Stingray-Advertising-Create-Largest-US-In-Store-Retail-Media-Network.html), reaching over 800 million monthly shoppers through audio advertising across [more than 25,000 locations](https://us.moodmedia.com/company/news/mood-media-s-vibenomics-and-stingray-advertising-create-largest-us-in-store-retail-media-network/) covering Kroger, Albertsons, Safeway, Rite Aid, and others. [Stingray operates across more than 140,000 locations worldwide](https://www.stingray.com/advertising-sales/in-store-retail-media/), and acquired DMI in October 2025, adding 8,500 further U.S. locations to its audio network.

**The route itself.** Back in the car, the navigation application showing the route to the next destination is displaying promoted pins placed by businesses that paid for the placement. [Google Maps displays these markers](https://www.digitalauthority.me/resources/resources-google-map-ads/) along the route whether or not the driver searched for the business. Waze, also owned by Google, has displayed pop-up banners at the top of the navigation screen at red lights near sponsored locations, [with a prominent âDrive Thereâ button](https://www.autoevolution.com/news/the-most-awful-google-maps-update-ever-everything-you-need-to-know-about-pop-up-ads-236705.html). [Google has filed a patent](https://www.motorauthority.com/news/1143831_google-maps-might-suggest-destinations-based-on-ads-you-hear) for a system that would integrate the audio stream with the navigation layer, so that an advertisement heard through the carâs speakers could trigger a suggested navigation detour. The patent has not shipped. The intent is documented.

![A Google Maps view showing nearby grocery stores. Most listings are marked with a circular pin; a smaller number are marked with a square pin, indicating they are sponsored placements.](https://nobodyaskedforthis.lol/_astro/grocery.RGvjn8iD_1ENWYc.webp)

Sponsored listings on Google Maps. The only visual difference from organic results is the marker shape: squares are paid placements, circles are not.

The driver who stops at a 7-Eleven, hears a Gulp Radio ad for a product near the register, sees a GSTV ad at the pump, and then opens Google Maps navigation is moving through a single continuous advertising environment. Each transition (car to pump, pump to store, store back to car) passes through a different medium with a different operator, but the commercial logic is identical. Your attention is there, your purchase intent is measurable, your location is known, and the inventory will be sold.

---

### What Is Already in the Car

The advertising infrastructure arriving in vehicles parallels what has been built for web, mobile, and connected television, and in some cases is importing that infrastructure directly.

On the open web, publishers sell inventory through automated real-time auctions where advertisers bid on individual pageview impressions. On mobile, the same auction infrastructure operates through in-app advertising with device-level identifiers tracking users across apps. On connected television (Roku, Amazon Fire, Samsung TVs) the same programmatic systems have extended to the living room screen, with viewing behavior used to target ads against household profiles. [We have covered the Roku home screen in detail](http://nobodyaskedforthis.lol/posts/roku-home-screen/): the screen that appears before you have chosen to do anything, already running full-motion video advertising, on a device you purchased, in a room you live in.

In-vehicle advertising is being built on the same foundations. [Stellantisâs Grand Cherokee pop-up](https://jalopnik.com/2034692/pop-up-ads-appearing-stellantis-infotainment/) was a direct, guaranteed placement: the manufacturer delivered a specific message to a specific set of vehicle identification numbers at a scheduled time, the oldest form of media buying, equivalent to a network upfront buy, except the inventory was the dashboard of a vehicle the recipient owned.

The [4screen platform](https://sherwood.news/business/the-rise-of-in-car-ads-automakers-now-view-infotainment-screens-as-huge/), operating across sixteen vehicle brands including Toyota, Volkswagen, Mercedes-Benz, and Stellantis, runs contextual advertising. A gas station promotion triggered by a low tank reading, or a restaurant suggestion calibrated to time of day and route. Conversion is measured by tracking whether the vehicle parks at the advertised location within three days. The location data required for that measurement is the same telemetry data that exists in the vehicleâs records for other purposes.

Ford has filed patents for a system using exterior cameras to [read roadside billboards and display matched advertising on the infotainment screen](https://sherwood.news/business/the-rise-of-in-car-ads-automakers-now-view-infotainment-screens-as-huge/), and a separate system that listens to in-car conversations and serves targeted advertising based on detected keywords. Both remain patents. The microphones and cameras they would require are already in production vehicles, deployed for hands-free calling, driver monitoring, and parking assistance.

The CarPlay removal is the same dynamic viewed from the manufacturerâs side. [GM is phasing out Apple CarPlay and Android Auto](https://news.dealershipguy.com/p/gm-to-phase-out-apple-carplay-and-android-auto-across-all-vehicles-by-2028-2025-10-24) from its entire vehicle lineup by 2028. GM earned [$5.4 billion](https://www.carluex.store/blogs/news/why-automakers-dropping-carplay-2026) from connected services in 2025. Every minute a driver spends in CarPlay is a minute the manufacturer cannot collect location data, serve its own content, or accumulate the behavioral record that feeds that revenue. [The connected car data market is projected at $26.4 billion by 2030](https://www.webpronews.com/the-14-billion-dashboard-war-why-automakers-are-racing-to-kill-apple-carplay-and-android-auto/). The in-vehicle advertising market specifically is projected at $6.7 billion by 2034.

There is an uncomfortable irony in the CarPlay story. Apple CarPlay and Android Auto, the systems manufacturers are fighting to remove so they can control the advertising inventory, both already contain advertising. Google Maps promoted pins appear inside CarPlay. Googleâs automotive data ambitions extend through Android Auto and, more completely, through Android Automotive OS. The fight over who controls the screen is, in part, a fight over whose ads run on it. The driver is not a participant in this negotiation.

---

### What the Car Knows

In 2023, [the Mozilla Foundation reviewed the privacy policies of twenty-five major automakers](https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/), producing what they described as the worst results the project had ever seen across any product category. All twenty-five failed.

[Nineteen of the twenty-five (76 percent) stated they can sell personal data.](https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/). Fifty-six percent stated they can share data with government or law enforcement in response to an informal request, not a court-issued warrant Nissanâs privacy policy reserves the right to infer driversâ [âpreferences, characteristics, psychological trends, predispositions, behavior, attitudes, intelligence, abilities, and aptitudesâ](https://www.theregister.com/2023/09/06/mozilla_vehicle_data_privacy/) and sell those inferences to third parties. BMW, Tesla, and Toyota can collect data [including sexual activity, immigration status, race, facial expressions, weight, and genetic information](https://insite.ipwea.org/connected-cars-fail-on-data-privacy-says-mozilla/).

General Motors secretly shared detailed telematics [with the data broker LexisNexis Risk Solutions](https://www.eff.org/deeplinks/2024/06/car-makers-shouldnt-be-selling-our-driving-history-data-brokers-and-insurance), which used braking patterns, acceleration, and time-of-day driving data to adjust insurance rates for drivers who had not been told their data was being sold. The program ended after a 2023 New York Times investigation. The data already shared was not recalled.

[Tesla allows users to opt out of vehicle data collection](https://www.theregister.com/2023/09/06/mozilla_vehicle_data_privacy/), but warns that doing so means Tesla cannot notify owners of vehicle issues in real timet. Toyotaâs Connected Services cannot be fully declined without disabling Bluetooth connectivity and aspects of the vehicle warranty. [Only two of the twenty-five automakers Mozilla reviewed](https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/) (Renault and Dacia, both subject to European GDPR) stated that drivers have the right to have their personal data deleted.

---

### The Controls You Have Online, and the Ones You Donât Have in Your Car

When you visit a website under GDPR jurisdiction, a consent management platform loads before the page content. You are shown a list of data processing purposes (analytics, personalization, advertising) and given a mechanism to decline some or all of them. The Reject All button is often small, the language often deliberately confusing, the consent architecture systematically abused since its introduction. But the mechanism exists. A regulator can investigate its implementation.

On iOS, since [Appleâs App Tracking Transparency framework arrived with iOS 14.5 in April 2021](https://tinuiti.com/blog/privacy-prep/apple-ios-idfa-guide/), every app that wants to track users across other apps must present a standardized prompt asking permission before doing so. Previously, the advertising identifier (the IDFA) was available to any app by default. Apple inverted that. Opt-in is now required, the prompt is not optional, and the language is standardized. Users who decline cannot have their IDFA accessed. [Estimates suggested the opt-in rate fell to roughly 25 to 30 percent after the change](https://www.avenga.com/magazine/apple-idfa/). The change cost Meta an estimated $10 billion in annual advertising revenue in 2022. It was a meaningful transfer of control, achieved through a platform-level technical requirement.

Android devices carry an [advertising identifier that users can reset or delete in settings](https://www.avenga.com/magazine/apple-idfa/), breaking the continuity of ad targeting. Browser-level tools (ad blockers, Firefoxâs Enhanced Tracking Protection, Safariâs Intelligent Tracking Prevention) degrade behavioral data available to advertisers. Connected television platforms carry advertising identifiers resettable in device settings. [As of 2025, nineteen U.S. states](https://blog.lucidprivacy.io/cookie-consent-beyond-2025/) have enacted consumer privacy laws with opt-out rights for targeted advertising.

None of this infrastructure has a direct equivalent in the automobile.

[A 2025 study by Privacy4Cars](https://www.automotive-fleet.com/10246048/privacy4cars-benchmarks-49-brands-on-handling-consumer-data-privacy-requests) evaluated the consumer data rights processes of 49 automotive brands against 12 criteria based on industry best practices. Only five brands scored 3.0 or above on a 5.0-point scale, meaning fewer than half of the identified best practices were adopted. Honda and Acura topped the list at 4.6 after settling with the California Privacy Protection Agency and implementing changes within weeks. Most brands scored significantly lower.

There is no standardized consent mechanism at vehicle purchase for the advertising uses of your driving data. There is no first-use prompt comparable to Appleâs ATT framework, no advertising identifier you can reset from the infotainment settings screen, no Global Privacy Control signal the car reads and honors. The consent was in the purchase agreement at the dealership, dense legal language presented during a transaction where attention was on financing terms and floor mats, broad enough to cover data uses that werenât clearly articulated and may not have existed yet at the time of signing.

The Stellantis opt-out is a phone number, business hours only. The Tesla opt-out disables safety monitoring. The Toyota opt-out degrades vehicle functionality and affects warranty terms. None of these are equivalent to clicking Reject All on a cookie banner, or to the buried settings menu on an Android phone. Privacy4Cars founder and CEO Andrea Amico has described the situation as equivalent to not wanting to be tracked on a desktop computer, [except the desktop computer came with no settings, the operating system is controlled by the manufacturer, and the browser is locked](https://www.automotive-fleet.com/10246048/privacy4cars-benchmarks-49-brands-on-handling-consumer-data-privacy-requests).

The web developed its consent infrastructure (imperfect, gamed, frequently cynical) because regulators required it and platforms competed on privacy. Appleâs ATT changes happened because Apple decided user privacy was a competitive advantage worth disrupting the advertising industry to protect. Neither of those forces has yet operated on the automotive industry with comparable effect.

---

### Where This Goes

The driver who starts their car in the morning is already in the advertising environment before leaving the driveway, if the infotainment screen has a manufacturer push waiting on startup. They pump gas through a GSTV screen running video they cannot mute. They walk into the convenience store and hear a Gulp Radio ad for a product near the register. They get back in the car, open Google Maps, which displays promoted pins along the route. The podcast they play has dynamically inserted programmatic spots served against their listener profile. The vehicleâs telematics system logs where all of this happened, when, and for how long.

These are not separate systems that happen to intersect. They are the outer edges of a single advertising infrastructure whose connective tissue is location data (the carâs GPS, the phoneâs GPS, the mobile device IDs collected near the pump screen, the vehicleâs cellular connection) and whose monetization logic is identical across each medium. Attention is there, purchase intent is measurable, and the inventory will be sold.

The technology companies have their own positions in this landscape. Google is the operating system in a growing fraction of vehicles, the navigation app in most of the rest, and the data recipient in both. Amazon is the voice layer in the home and increasingly in the car, connected to the largest commercial fulfillment infrastructure in American retail. Spotifyâs Car Thing was the reminder that not every attempt to colonize this space succeeds, but its failure was a failure of product-market fit and not a failure of commercial logic. The car remained, as Spotifyâs spokesperson put it, âan important place for audio.â [What happened next is that the audio became the vehicleâs operating system](http://nobodyaskedforthis.lol/posts/microwave/), with a major technology company behind the voice that answers.

The in-car advertising market was valued at $1.8 billion in 2025 and is [projected to reach $6.7 billion by 2034](https://dataintelo.com/report/in-car-advertising-platform-market). GM earned [$5.4 billion](https://www.carluex.store/blogs/news/why-automakers-dropping-carplay-2026)from connected services last year alone. Retail media (the category that includes Gulp Radio, GSTV, and the in-store audio networks) is projected to reach [$81.6 billion in advertising spending in 2025,](https://www.gstv.com/press) comprising nearly a quarter of all U.S. digital advertising dollars. These are the targets the business decisions documented in this piece are being made to hit.

The consumer controls that exist online (however imperfect, however frequently gamed) emerged because regulators demanded them and platforms competed on them. Neither of those forces has yet operated on the automobile with comparable effect. [The California Privacy Protection Agency has moved against Honda](https://www.automotive-fleet.com/10246048/privacy4cars-benchmarks-49-brands-on-handling-consumer-data-privacy-requests). European regulators under GDPR have begun scrutinizing connected vehicle data practices. The UNECE R155 regulation requires cybersecurity management systems for new vehicle type approvals. But the pace of regulatory development has consistently lagged the pace of deployment.

In the meantime: [BMW would like $18 a month for the seats you already bought](http://nobodyaskedforthis.lol/posts/bmw-heated-seats/). [The mug has a firmware update](http://nobodyaskedforthis.lol/posts/the-mug-firmware/). [The microwave has an Alexa](http://nobodyaskedforthis.lol/posts/microwave/). And the car would like a word with its advertisers, through the speakers you paid for, on the cellular connection you pay for monthly, in the cabin where the windows seal out the weather and seal in the audience.

The consumer remedies, where they exist, are unserious. Add a Pi-Hole to the trunk. Buy a 2007 Camry. Neither scales, neither is factory-supported, and neither stops the next car you sit in from trying again.

Zerin Dube tapped the X button. The advertisement disappeared, the Jeep started normally, and nothing was broken.

At the next ignition cycle, the offer came back.

---

*Reporting draws on research from the [Mozilla Foundation](https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/), [Privacy4Cars](https://www.automotive-fleet.com/10246048/privacy4cars-benchmarks-49-brands-on-handling-consumer-data-privacy-requests), [Help Net Security](https://www.helpnetsecurity.com/2025/04/04/cybersecurity-risks-cars/), the [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2024/06/car-makers-shouldnt-be-selling-our-driving-history-data-brokers-and-insurance), [AdExchanger](https://www.adexchanger.com/ctv-roundup/gstv-wants-to-turn-gas-stations-into-a-video-ad-marketplace/), [Digiday](https://digiday.com/future-of-tv/extension-broadcast-buy-advertisers-buying-ads-gas-station-screens/), [Sherwood News](https://sherwood.news/business/the-rise-of-in-car-ads-automakers-now-view-infotainment-screens-as-huge/), [Jalopnik](https://jalopnik.com/2034692/pop-up-ads-appearing-stellantis-infotainment/), [C-Store Dive](https://www.cstoredive.com/news/7-eleven-qsic-radio-station-gulp-media/750712/), [Wired](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/), [Cars.com](https://www.cars.com/articles/gm-to-remove-apple-carplay-android-auto-from-future-vehicles-517813/), [Android Headlines](https://www.androidheadlines.com/android-automotive), [Volvo Cars](https://www.volvocars.com/intl/media/press-releases/6B411DC79F4F8965/), and [Upstream Security](https://www.einfochips.com/blog/cybersecurity-for-the-next-gen-mobility/).*