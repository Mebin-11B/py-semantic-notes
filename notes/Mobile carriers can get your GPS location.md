---
title: "Mobile carriers can get your GPS location"
url: https://an.dywa.ng/carrier-gnss.html
clipped: 2026-06-17 01:50:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Mobile carriers can get your GPS location](https://an.dywa.ng/carrier-gnss.html)

## Digest Summary
Apple’s iOS 26.3 adds a privacy option that blocks cellular networks from receiving precise GNSS (GPS, GLONASS, Galileo, BeiDou) coordinates via the modem introduced in 2025. Historically, carriers have obtained location through two mechanisms: (1) coarse positioning from cell‑tower triangulation, accurate to tens‑hundreds of metres; and (2) control‑plane protocols that request the device’s GNSS fix. In 2G/3G this uses the Radio Resources LCS Protocol (RRLP); in 4G/5G it uses LTE Positioning Protocol (LPP). These protocols operate invisibly to users, allowing carriers to supply single‑digit‑metre accuracy when they query the phone. The capability has been employed by law‑enforcement agencies (e.g., U.S. DEA in 2006) and national security services (e.g., Israel’s GSS tool) to collect precise location data, including for COVID‑19 contact tracing. The new iOS setting lets users disable GNSS responses to carriers and receive notifications of such requests, aiming to curb mass surveillance that leverages these built‑in positioning protocols.

## Discussion Summary
The comments express strong concern about pervasive location tracking by carriers and device software, emphasizing that users lack clear control or notification when precise GPS data is shared and calling for stronger accountability and the ability to disable sharing with real‑time alerts. Contributors note that such tracking has existed for years, primarily for emergency services, and that carriers can also infer location via tower triangulation. Technical workarounds, including mesh‑network alternatives and settings to limit precise location, are discussed alongside suggestions for stricter privacy legislation and broader public awareness.

---

## Full Article

Mobile carriers can get your GPS location
=========================================

2026-01-31

In iOS 26.3, Apple introduced a new privacy feature which limits “precise location” data made available to cellular networks via cell towers. The feature is only available to devices with Apple’s in-house modem introduced in 2025. The announcement says

> Cellular networks can determine your location based on which cell towers your device connects to.

This is well-known. I have served on a jury where the prosecution obtained location data from cell towers. Since cell towers are sparse (especially before 5G), the accuracy is in the range of tens to hundreds of metres.

**But this is not the whole truth**, because cellular standards have built-in protocols that make your device silently send GNSS (i.e. GPS, GLONASS, Galileo, BeiDou) location to the carrier. This would have the same precision as what you see in your Map apps, in single-digit metres.

In 2G and 3G this is called [Radio Resources LCS Protocol (RRLP)](https://projects.osmocom.org/projects/security/wiki/RRLP)

> So the network simply asks “tell me your GPS coordinates if you know them” and the phone will respond.

In 4G and 5G this is called [LTE Positioning Protocol (LPP)](https://tech-academy.amarisoft.com/LTE_LPP.html)

> RRLP, RRC, and LPP are natively control-plane positioning protocols. This means that they are transported in the inner workings of cellular networks and are practically invisible to end users.

It’s worth noting that GNSS location is never *meant* to leave your device. GNSS coordinates are calculated entirely passively, your device doesn’t need to send a single bit of information. Using GNSS is like finding out where you are by reading a road sign: you don’t have to tell anyone else you read a road sign, anyone can read a road sign, and the people who put up road signs don’t know who read which road sign when.

These capabilities are not secrets but somehow they have mostly slid under the radar of the public consciousness. They have been used in the wild for a long time, such as by the DEA in the US in 2006:

> [T]he DEA agents procured a court order (but not a search warrant) to obtain GPS coordinates from the courier’s phone via a ping, or signal requesting those coordinates, sent by the phone company to the phone.

And by Shin Bet in Israel, which tracks everyone everywhere all the time:

> The GSS Tool was based on centralized cellular tracking operated by Israel’s General Security Services (GSS). The technology was based on a framework that tracks all the cellular phones running in Israel through the cellular companies’ data centers. According to news sources, it routinely collects information from cellular companies and identifies the location of all phones through cellular antenna triangulation and GPS data.

Notably, the Israeli government started using the data for contact tracing in March 2020, only a few weeks after the first Israeli COVID-19 case. An individual would be sent an SMS message informing them of close contact with a COVID patient and required to quarantine. This is good evidence that the location data Israeli carriers are collecting are far more precise than what cell towers alone can achieve.

A major caveat is that I don’t know if RRLP and LPP are the exact techniques, and the only techniques, used by DEA, Shin Bet, and possibly others to collect GNSS data; there could be other protocols or backdoors we’re not privy to.

Another unknown is whether these protocols can be exploited remotely by a foreign carrier. Saudi Arabia has abused SS7 to spy on people in the US, but as far as I know this only locates a device to the coverage area of a Mobile Switching Center, which is less precise than cell tower data. Nonetheless, given the abysmal culture, competency, and integrity in the telecom industry, I would not be shocked if it’s possible for a state actor to obtain the precise GNSS coordinates of anyone on earth using a phone number/IMEI.

Apple made a good step in iOS 26.3 to limit at least one vector of mass surveillance, enabled by having full control of the modem silicon and firmware. They must now allow users to disable GNSS location responses to mobile carriers, and notify the user when such attempts are made to their device.

---