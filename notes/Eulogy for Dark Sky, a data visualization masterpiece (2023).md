---
title: "Eulogy for Dark Sky, a data visualization masterpiece (2023)"
url: https://nightingaledvs.com/dark-sky-weather-data-viz/
clipped: 2026-06-17 02:00:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Eulogy for Dark Sky, a data visualization masterpiece (2023)](https://nightingaledvs.com/dark-sky-weather-data-viz/)

## Digest Summary
Apple discontinued the Dark Sky weather app on iOS on Jan 1 2023 after acquiring the company in 2020 and integrating its forecast technology into Apple Weather with iOS 16. The article highlights Dark Sky’s information‑design strengths: context‑sensitive graphics, hyper‑local forecasts, and a default 12‑hour view that starts at “now.” Screenshots illustrate how the app emphasizes relevant data—storm timing, rain probability, temperature distribution—and offers a “Time Machine” view for past weather. Weekly forecasts provide hyper‑local temperature ranges, rain likelihood, and micro‑trends. Design details include preserving temperature magnitudes in visual “pills,” substituting precise precipitation values with categorical labels (light/medium/heavy), and using arrows for wind direction. User feedback notes that Apple Weather presents information less efficiently, lacking features such as Dark Sky’s precipitation graph. The author, Srini Kadamati, now builds data‑management tools for biomedical research and has taught data visualization at Dataquest.io and Preset.io.

## Discussion Summary
Comments express strong nostalgia for Dark Sky’s precise hyper‑local forecasts and minimalist UI, contrasting it with Apple’s weather app, which many view as less accurate, feature‑reduced, and aesthetically driven after the acquisition. Users note missing features such as historical data and cite a perception that the original app offered a unique “spark of joy.” Numerous alternatives—including open‑source clones, Breezy Weather, Weathergraph, WeatherStrip, Windy, and government graphs—are recommended for similar functionality, while some critique broader design choices and corporate handling of the service.

---

## Full Article

On January 1, 2023, Apple sunsetted (pun intended) the Dark Sky mobile app on iOS. Apple purchased the company behind the popular weather application in early 2020, then announced that it would be shutting down the Dark Sky applications (first on Android, then on iOS and web), and finally stated in 2022 that the forecast technology would be integrated into the Apple Weather app with iOS 16.

![A comparison of Dark Sky with Apple Weather. The Dark Sky app is white. It's interface has a simple location marker with a list of forecasted temperature readings. Buttons at the bottom allow users to toggle between maps, forecasts, notifications and reports. The Apple Weather app has an image of the sky. It has current weather, hourly weather temperatures, and a 10-day forecast. ](https://i0.wp.com/dvsnightingale.wpenginepowered.com/wp-content/uploads/2023/03/darksky1.png?resize=720%2C669&ssl=1)

Comparison of Dark Sky with Apple Weather.

But Dark Sky was *much* more than just an API or a set of “forecast technologies.” The design of the Dark Sky mobile application represented a hallmark of information design because the team clearly obsessed over how people would actually use the app on a daily basis.

Here’s a gallery of screenshots I personally took in the last year.

The design of Dark Sky was so wonderful that I could understand the *shape* of the weather at a glance, even from a zoomed out view of the app.

Common use cases for a weather app
----------------------------------

Before we can dissect what makes the design of this app so special, let’s define the most common use cases for a weather app. A good weather app attempts to address a range of use cases in a person’s life. Here are some common use cases for a weather app, starting with the contextual goals first:

You’ll notice that the questions I want to answer vary based on the context and situation I’m in. This is the perfect situation for software that embraces good information design principles.

In [Magic Ink](http://worrydream.com/MagicInk/), Bret Victor defined information design “as the design of context-sensitive information graphics.” Unlike static graphics, like a weather map in a newspaper, information graphics in software can be highly dynamic and can incorporate [context from the user’s environment.](http://worrydream.com/MagicInk/#inferring_context_from_the_environment)

Dark Sky aggressively leaned into these ideas, and the team worked hard to turn nearly everything in the application into a context-sensitive information graphic. Let’s dive deeper into some examples where this notion is in full display.

**Weather forecast for the day at a precise location**
------------------------------------------------------

I’ll start by listing my goals when trying to understand the upcoming weather for the day:

The default experience for the Dark Sky application is to show weather for the next 12 hours at my precise location. Here are three screenshots from the app, from different days and locations. **What do you notice?**

The app contextualizes the information that’s presented based on what’s most relevant.

In the left-most screenshot, the context of the weather storm that’s passing by my location and some potential light rain is emphasized to the user. The wind advisory and dip in the “feels like” temperature also make honorable mentions. In combination with the clickable **Wind Advisory** warning, I can quickly understand that the storm has passed my specific location but I should still be mindful of the wind.

In the middle screenshot, the storm front heading my direction, the imminent rain starting within the hour, and the hours of rain later in the day are emphasized front and center. Based on my interest in the rain, I scrolled down (not shown in screenshot) to switch from temperature to rain probability for the main weather view.

In the right-most screenshot, the temperature distribution throughout the day is emphasized.

There are lots of little details that are easy to miss, as well. For example, all three screenshots above start showing weather information starting at the current moment (“now”) and onwards. This is brilliant, because I only occasionally care about weather from a few hours or days ago. (To accommodate those situations, the app did have a unique Time Machine view to explore past weather data.)

Weather forecast for the week
-----------------------------

Let’s revisit our goals when trying to understand the weather for the week:

While many other weather apps focus on helping me understand the weather at the city level, the Dark Sky app differentiates itself by enabling me to understand the weather with a *hyperlocal* view. I can view the weather at specific addresses and landmarks and understand how the weather might be different in a city center compared to the towns around it.

By default, the Dark Sky app shows the weekly weather summary at my current location (screenshot on the left).  I can *contextualize* the weekly weather view by clicking the search icon and typing in the alternative location I’m interested in (screenshot on the right).

At a glance, I can quickly understand:

* Which days are likely to rain.
* Which days have wide temperature ranges (low lows and high highs).
* The general shape of the weather (micro-trends).

Gallery of subtle design elements
---------------------------------

In the first few sections, I laid the groundwork by diving a bit more deeply into specific aspects of Dark Sky. Now that I’ve hopefully engaged your critical design eye, I’d like to elevate other elements in the app’s design in a more rapid-fire fashion. I hope that this section will provide some ideas and inspiration for people designing their own data-rich applications.

**Preserving temperature magnitudes in ranges**

To represent data visually, the data needs to be mapped from “data space” to “pixel space”. In some domains and scenarios, you want to ensure the magnitudes are carried over, and in others you want to [rescale the values](https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)) to a fixed scale so the resulting charts are more consistent in the space and pixels they take up.

In the Dark Sky app, the “temperature pills” representing the forecasted temperatures for the upcoming week preserve their existing magnitude more effectively in the visualization. The temperature values are more tightly *integrated* with the visual representation, making the combined experience more amenable to quick comparison across multiple days.

Many weather apps opt for the design pattern on the right, where all temperature ranges are rescaled to take up the same amount of space in the app.

**Replacing numbers with rough categories**

Interpreting hourly distributions of rainfall or snowfall can be difficult. Is 0.25 inches of rain a lot over the next hour? What about 0.2 inches of snow per hour for the next hour, then 0.15 for the hour after that? How do I prepare for these circumstances?

To help users stay informed and take action, the app will often replace precise forecast distributions of rainfall and snowfall with *rough* categories instead. This design choice has two positive effects on users:

* It contextualizes the forecast to simpler categories that can help us quickly make changes in our life if needed.
  + Light snow that starts and stops means that my snow shoveling company won’t come out, but heavy snow means they likely will.
  + Heavy snow means I should probably make sure my outdoor furniture is better covered and ready to take the snow.
* It removes a sense of artificial precision that doesn’t *really* exist because weather forecasts fundamentally have very high uncertainty and error bands.

**Contextualized storm map**

Simple color scales combined with arrows go a very long way to conveying relevant storm information.

**W****ind direction**

Instead of conveying wind direction using text (“NW” or “Northwest”), the app uses arrows! If the wind shifts directions throughout the day, I can *feel* the wind direction changing using my body.

**Complaints from former Dark Sky users**
-----------------------------------------

As you can tell, I could probably write an *entire book* about the design of Dark Sky.

Instead, I want to share some passionate comments from other Dark Sky fans. While most of them aren’t data viz or design nerds, they *feel* that the Apple Weather app is not a sufficient replacement. These people relied on Dark Sky to make decisions and grew very attached to an application that integrated deeply into their lives.

Here are some examples:

* [0000GKP on Reddit](https://www.reddit.com/r/ios/comments/z11dr9/comment/ix8hqjp/?utm_source=reddit&utm_medium=web2x&context=3): “I have already made the transition to the Weather app. **The information is presented in a much less efficient manner than Dark Sky so it takes more effort to get it**, but it is all there (except for cloud cover).”
* [TheGeckoDude on Reddit](https://www.reddit.com/r/ios/comments/z11dr9/comment/j0bh6j7/?utm_source=reddit&utm_medium=web2x&context=3): “Is there anything that has the precipitation graph similar to dark sky? **The biggest thing I will miss from dark sky is that graph. I’m outside a lot and it is super helpful for knowing when to take cover or when it might rain**. I need to find a feature like that because the vague weather precipitation info will not cut it for me.”

Let’s make data shine!
----------------------

Dark Sky started with publicly available data, augmented it with contextualized predictions, rigorously iterated on data visualization design, and packaged all of this into a contextualized experience to make weather data *useful* for me in my daily life.

While the availability of data has never been higher, we’re still missing software experiences that contextualize that data to make our lives better. Data alone isn’t enough.

The world needs more Dark Sky-like experiences to help us improve our spending habits, help us sleep better, and more. If you’re working on information software, I hope you can be inspired by the body of design and engineering work that Dark Sky pioneered.

##### Srini Kadamati

Srini Kadamati currently helps build better data management tools for biomedical research at Manifold.ai. Previously, he taught data visualization and data skills at Dataquest.io and Preset.io.