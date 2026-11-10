---
title: "Finding the differences in a series of power supplies"
url: https://www.lttlabs.com/articles/2026/05/05/testing-psu-series
clipped: 2026-06-17 01:06:46
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Finding the differences in a series of power supplies](https://www.lttlabs.com/articles/2026/05/05/testing-psu-series)

## Digest Summary
None

## Discussion Summary
Comments show curiosity about the technical distinctions between higher‑wattage power supplies, questioning whether they achieve greater capacity solely through higher‑rated components or also incorporate higher‑quality parts. The discussion reflects interest in a detailed component‑by‑component comparison to understand design trade‑offs and performance implications, indicating a desire for deeper analysis beyond surface specifications.

---

## Full Article

Nearly every power supply you buy today will be part of a series - a collection of two to four power supplies with the same branding across different wattages(i.e. [FOCUS](https://seasonic.com/power-supplies/filter/product_cat-focus-series/), [RMe](https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/corsair-rme-series/), [MAG](https://www.msi.com/Power-Supply/Products#?tag=MAG-Series)).  These series will cover ranges of power like 500-800 W, 750-1000 W, or 1000-1200 W.

Why do manufacturers produce these series, how similar are the power supplies within a series, and is it a good assumption that models within a series will perform similarly?

We don't typically test all models in a series but we did for the recently released NZXT C Gold Core series that we'll look at in this article.

NZXT C Gold Core Case Study
---------------------------

The extent of the similarities will differ between manufacturers and series, but in this article we've tested and opened up the NZXT C Gold Core series of power supplies to explore this question.

Consider this photo of the inside of the three power supplies, it's a challenging game of spot the differences between the NZXT [C750 Gold Core](https://www.lttlabs.com/products/power-supplies/nzxt-c750-gold-core), [C850 Gold Core](https://www.lttlabs.com/products/power-supplies/nzxt-c850-gold-core), and [C1000 Gold Core](https://www.lttlabs.com/products/power-supplies/nzxt-c1000-gold-core).

NZXT C750 Gold Core, C850 Gold Core, and C1000 Gold Core Internals

All models in a series will typically share the chassis, PCB, electrical topology, heat management, feature set, and to a certain extent, performance(this will be covered more later).  From the series that we've inspected, we've found it easier to list the differences than the similarities.

#### What are the Hardware Differences?

The largest and most visible difference as you increase in wattage is the greater selection of cables to allow connection to more components.  This mostly manifests with additional PCIe cables, but there may be more subtle differences that might make a difference.  For the NZXT C Gold Core series, the 12V-2x6 connector on the 750 W model is limited to 300 W, the 12V-2x6 output of the 850 W and 1000 W models can supply the full 600 W.

NZXT C750 Gold Core, C850 Gold Core, and C1000 Gold Core Cables

The models can be contrasted in the compare tool on [LTTLabs.com](http://lttlabs.com).  Below is a link to the three NZXT C Gold Core power supplies investigated in this article.

> [NZXT C Gold Core Comparison Bin](https://www.lttlabs.com/comparison?slugs=nzxt-c750-gold-core%2Cnzxt-c850-gold-core%2Cnzxt-c1000-gold-core&binName=NZXT+C+Gold+Core+Power+Supplies&n=lkzfv69m1bn)

For an accounting of the components that change between models, Cybenetics typically have a relatively complete list for each model they certify.  Exploring the reports for the [C750 Gold Core](https://www.cybenetics.com/evaluations/psus/2900/), [C850 Gold Core](https://www.cybenetics.com/evaluations/psus/2899/), and [C1000 Gold Core](https://www.cybenetics.com/evaluations/psus/2897/), the main differences are in the switching components and bulk/filtering capacitors.

#### Component Level Changes

Many components can be shared, but more highly rated switching components are required due to the increased current; and larger bulk capacitors will store more energy to allow smooth operation for higher output wattages. There will also be small changes to components around the control, switching, and protections circuits to tune for their different operating ranges.

As can be seen in the photos below, all three models use the same PCB and assembly, supporting multiple models by leaving space for components to be switched out or left completely unpopulated.  Note the difference in number of capacitors in the top right, the colour/model of the capacitor in the bottom left, and the different transformer used for the 1000 W model.

NXZT C750 Gold Core Internals

---

Do they Produce Different Results?
----------------------------------

The best way to compare these power supplies is through the comparison tool on the LTT Labs website.  Below are three links to comparison bins with the NZXT C Gold Core series, NZXT C Gold series, and the entire set of both series.

> [NZXT C Gold Core Comparison Bin](https://www.lttlabs.com/comparison?slugs=nzxt-c750-gold-core%2Cnzxt-c850-gold-core%2Cnzxt-c1000-gold-core&binName=NZXT+C+Gold+Core+Power+Supplies&n=lkzfv69m1bn) - The three power supplies from this article

> [NZXT C Gold Comparison Bin](https://www.lttlabs.com/comparison?slugs=nzxt-c850-gold-atx-3-1%2Cnzxt-c1000-gold%2Cnzxt-c1200-gold&binName=NZXT+C+Gold+Core+Power+Supplies&n=lkzfv69m1bn) - The three C Gold power supplies

> [NZXT C Power Supplies Comparison Bin](https://www.lttlabs.com/comparison?slugs=nzxt-c750-gold-core%2Cnzxt-c850-gold-core%2Cnzxt-c1000-gold-core%2Cnzxt-c850-gold-atx-3-1%2Cnzxt-c1000-gold%2Cnzxt-c1200-gold&binName=NZXT+C+Gold+Core+Power+Supplies&n=lkzfv69m1bn) - All six power supplies

### Efficiency

While all three C Gold Core models are advertised as 80PLUS and Cybenetics ETA Gold, they're all actually rated Cybenetics ETA and 80PLUS Platinum.  It is not uncommon for manufacturers to advertise a lower tier of efficiency rating.  This is typically because in their own internal testing they can't *guarantee* that each model will meet that level due to manufacturing and component variance.

NZXT has told us that they did design these power supplies with the target of being near the Platinum efficiency level.  The models that we tested performed very similarly to each other, and match their advertised claims.

115 V Input Power Efficiency Graph

### Ripple Noise

The models performed very similarly when testing the output voltage ripple. The ideal voltage ripple is 0 V, but any results within the green shaded region are within specification.

I have no conclusive explanation for the difference in ripple noise on the 3.3V rail.  It could be that the higher rated components of the higher wattage models provide more stability for the Voltage Regulator Modules (VRMs).  Though it is also interesting that this doesn’t have any impact on the 5V rail.

115 V Output Voltage Ripple Graph

### Load Regulation

A series of power supplies will often have the same output ratings of the 5V and 3.3V rails

A series of power supplies will typically share 5V and 3.3V output circuitry for simplicity. This should result in similar performance in voltage regulation testing. The output voltages on all of the rails follow a similar pattern, with a similar magnitude of voltage drop.

The graph below shows the load regulation performance: how much each output power rail of the power supply deviates from the nominal voltage.

115 V Output Voltage Regularion Graph

### Brownout & Protections

The models also engage the protections at a similar level and perform similarly when testing the brownout duration.  All of the C Gold series have really high brownout durations, and the C Gold Core series all perform similarly to each other.  With relatively low brownout durations around 11-12 ms.

NZXT C1000 Gold Core 16 ms Brownout Waveform

---

Why Brand and Release a Series?
-------------------------------

With all of the similarities between the models, why release three different models?  Why not just build the C1000 Gold Core model and sell those?

The specific reasons will differ for the manufacturer and series, but it can make sense for a variety of business reasons.  Producing multiple models in a series allows them to release multiple power supplies while only having to design one.  Great efficiencies can be found from using the same 'infrastructure'(PCB, chassis, most components, heat management, manufacturing, etc.), and switching out individual components to optimize for each output rating.

It's also much easier to build a brand around a series than a single model, and it is much easier to upsell people on the next highest wattage within the same series in the name of future-proofing.  This can benefit the user as well.  When shopping for a power supply you have more selection at each wattage level instead of having to compromise in order to get the brand or series you prefer.

---

From this analysis we can see that some power supply series are incredibly similar.  It is important to note that this is not the case for all series and it may be that the highest or lowest wattage in a series will be based on a separate platform(design).

Ideally you can find testing and a review of the exact power supply that you're looking to purchase, but in general you can assume a similar level of performance from power supply models within a series.

---

---

Bonus Appendix
--------------

While I had the NZXT C1000 Gold Core opened, I also opened the NZXT C1000 Gold to take a couple side-by-side photos.

NZXT C1000 Gold Core(Black) and NZXT C1000 Gold(White)

---