---
title: "Shipmap.org"
url: https://www.shipmap.org/
clipped: 2026-06-17 02:02:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Shipmap.org](https://www.shipmap.org/)

## Digest Summary
The Shipmap.org visualisation displays global merchant‑fleet movements for 2012 on a bathymetric base map. Data combine exactEarth AIS location/speed records with Clarksons Research static vessel information, cross‑checked by UCL Energy Institute to add engine, hull, and vessel characteristics. CO₂ emissions per hour are calculated using the IMO Greenhouse Gas Study 2014 methodology. Users can pan, zoom, and animate ship positions via a timeline, toggle layers (ports, routes, background), and filter or colour ships by five categories: Container (20‑ft slot count), Dry bulk, Tanker, Gas bulk (cubic metres), and Vehicles (all measured in thousand tonnes). Counters show hourly CO₂ (thousands of tonnes) and freight capacity. The map uses WebGL, a custom GEBCO‑2014 bathymetry grid, and Natural Earth land/river data. First‑quarter data are incomplete, causing fewer early‑year ships. High‑resolution print versions are available, and embedding is permitted with attribution to Kiln and UCL. Funded by the European Climate Foundation.

## Discussion Summary
The comments are overwhelmingly positive, describing the visualization as striking, informative, and enjoyable, while highlighting its ability to reveal major shipping routes, seasonal port closures, geopolitical hubs, and economic impacts. Viewers note the usefulness of real‑time or newer data, suggestions for globe‑based projections, clearer land coloring, and integration with commodity or climate information. Several remarks discuss regulatory and environmental effects, such as fuel sulfur limits and emerging Arctic routes, and many request updated datasets or interactive features, but overall appreciation dominates.

---

## Full Article

Back to map

New! Stunning high-res maps for print
-------------------------------------

Due to popular demand the designers of this map, [Kiln](https://kiln.digital), are now selling stunning high-resolution versions of the world âroutesâ view. There are two versions available: coloured by ship type over the inky-blue base map; or just the ship in a single colour a transparent background so you can overlay or print onto whatever background colour you like. Contact [[email protected]](https://www.shipmap.org/cdn-cgi/l/email-protection#7e161b1212113e15171210501a1719170a1f12) for pricing and further information.

![](https://www.shipmap.org/images/colored_preview.jpg)
![](https://www.shipmap.org/images/transparent_preview.jpg)

Can I embed this map?
---------------------

Yes. You are welcome to embed this map. Please include a link back to [Kiln](https://www.kiln.digital) somewhere in the text of your article. Use the following embed code for a fully responsive embed that will adjust to the width of your website. Feel free to change the height and/or give it a fixed width if you prefer.

What can I see?
---------------

You can see movements of the global merchant fleet over the course of 2012, overlaid on a bathymetric map. You can also see a few statistics such as a counter for emitted CO2 (in thousand tonnes) and maximum freight carried by represented vessels (varying units).

What can I do?
--------------

You can pan and zoom in the usual ways, and skip back and forward in time using the timeline at the bottom of the screen. The controls at the top right let you show and hide different map layers: port names, the background map, routes (a plot of all recorded vessel positions), and the animated ships view. There are also controls for filtering and colouring by vessel type.

What the are types of ships shown?
----------------------------------

The merchant fleet is divided into five categories, each of which has a filter and a CO2 and freight counter for the hour shown on the clock. The ship types and units are as follows:

* Container (e.g. manufactured goods): number of container slots equivalent to 20 feet (i.e. a 40-foot container takes two slots)
* Dry bulk (e.g. coal, aggregates): combined weight of cargo, fuel, water, provisions, passengers and crew a vessel can carry, measured in thousand tonnes
* Tanker (e.g. oil, chemicals): same as dry bulk
* Gas bulk (e.g. liquified natural gas): capacity for gases, measured in cubic metres
* Vehicles (e.g. cars): same as dry bulk

Why do ships sometimes appear to move across land?
--------------------------------------------------

In some cases this is because there are ships navigating via canals or rivers that arenât visible on the map. Generally, though, this effect is an artefact of animating a ship between two recorded positions with missing data between, especially when the positions are separated by a narrow strip of land. We may develop the map to remove this effect in the future.

Why are there fewer ships visible in the first part of the year?
----------------------------------------------------------------

Unfortunately the data we are using for the map is incomplete for the first few months of the year: roughly January to April.

Who created this map?
---------------------

The map was created by [Kiln](https://www.kiln.digital) based on data from the [UCL Energy Institute](http://www.bartlett.ucl.ac.uk/energy) (UCL EI)

Website: Duncan Clark & Robin Houston from Kiln

Data: Julia Schaumeier & Tristan Smith from the UCL EI

Music: Bach Goldberg Variations played by [Kimiko Ishizaka](http://www.opengoldbergvariations.org)

How was the map created?
------------------------

UCL EI took data showing location and speed of ships and cross-checked it with another database to get the vessel characteristics, such as engine type and hull measurements. With this information they were able to compute the CO2 emissions for each observed hour, following the approach laid out in the Third IMO Greenhouse Gas Study 2014. Kiln took the resulting dataset and visualized it with WebGL on top of a specially created base map, which shows bathymetry (ocean depth), based on the [GEBCO\_2014 Grid](http://www.gebco.net) (version 20150318), as well as continents and major rivers from [Natural Earth](http://www.naturalearthdata.com/).

Where did you get the data and who paid?
----------------------------------------

Our data sources for shipping positions are [exactEarth](http://www.exactearth.com) for AIS data (location/speed) and [Clarksons Research UK World Fleet Register](http://www.clarksons.com/services/research/) (static vessel information). We are very grateful to our funders, the [European Climate Foundation](http://europeanclimate.org/).

I want one too!
---------------

If you want to have an installation in your foyer, museum, living room, you can contact us at [[email protected]](https://www.shipmap.org/cdn-cgi/l/email-protection#ee868b828281ae85878280c0879a). Weâd be happy to work on a bespoke version.

[![](https://www.shipmap.org/images/iiba.png)](http://www.informationisbeautifulawards.com/showcase/1580-shipmap-org)

Back to map