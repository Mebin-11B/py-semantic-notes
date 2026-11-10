---
title: "Fedware: Government apps that spy harder than the apps they ban"
url: https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/
clipped: 2026-06-17 01:24:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Fedware: Government apps that spy harder than the apps they ban](https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/)

## Digest Summary
The article documents extensive data‑collection practices in dozens of U.S. federal agency Android apps, coining the term “Fedware.” It notes that the White House app (v 47.0.1) requests precise GPS, biometric fingerprint, storage modification, auto‑start, overlay, Wi‑Fi, and badge‑notification access, and embeds three trackers, including Huawei Mobile Services Core. Similar over‑permissions are found in other apps: the FBI’s myFBI Dashboard requests 12 permissions and includes four trackers (one from Google AdMob); FEMA’s app requests 28 permissions; IRS2Go has three trackers and ten permissions; and TSA’s MyTSA uses nine permissions with location access. Border‑control apps (CBP Mobile Passport Control, CBP One, Mobile Fortify) request numerous “dangerous” permissions, retain facial‑recognition data for up to 75 years, and share it across DHS, ICE, and the FBI. ICE’s SmartLINK, built by a GEO Group subsidiary, collects geolocation, facial images, voice prints, medical data, and contacts, granting unlimited data‑use rights. The government also purchases bulk location data from brokers such as Venntel, circumventing the Carpenter warrant requirement. A 2023 GAO report found that about 60 % of privacy and security recommendations issued since 2010 remain unimplemented, highlighting systemic oversight gaps.

## Discussion Summary
The comments express strong criticism of federal mobile apps, focusing on excessive data collection, inclusion of sanctioned Chinese SDKs, and perceived government incompetence. Many highlight privacy risks, call for limiting or removing these apps, and argue that web alternatives would suffice for basic information delivery. Some acknowledge limited justification for specific functions, such as location in emergency apps, while others complain about the site’s distracting animations and the onerous personal‑information requirements of services like PACER. Overall, the tone is skeptical and wary of governmental digital surveillance.

---

## Full Article

The federal government released an app yesterday, March 27th, and it's spyware.

Listen to this article

Failed to load audio

The [White House app](https://play.google.com/store/apps/details?id=gov.whitehouse.app&ref=sambent.com) markets itself as a way to get "unparalleled access" to the Trump administration, with press releases, livestreams, and policy updates. The kind of content that every RSS feed on the planet delivers with one permission: network access. But the White House app, version 47.0.1 (because subtlety died a long time ago), requests [precise GPS location, biometric fingerprint access, storage modification, the ability to run at startup, draw over other apps, view your Wi-Fi connections, and read badge notifications](https://www.ibtimes.com/white-house-app-settings-grant-full-control-over-your-device-users-warned-extreme-risks-3800465?ref=sambent.com). It also ships with [3 embedded trackers](https://reports.exodus-privacy.eu.org/en/reports/search/gov.whitehouse.app/?ref=sambent.com) including Huawei Mobile Services Core (yes, the Chinese company the US government sanctioned, shipping tracking infrastructure inside the sitting president's official app), and it has an ICE tip line button that redirects straight to ICE's reporting page.

This thing also has a "Text the President" button that auto-fills your message with "Greatest President Ever!" and then collects your name and phone number. There's no specific privacy policy for the app, just a generic whitehouse.gov policy that doesn't address any of the app's tracking capabilities.

The White House app might actually be one of the milder ones. I've been going through every federal agency app I can find on Google Play, pulling their permissions from [Exodus Privacy](https://reports.exodus-privacy.eu.org/?ref=sambent.com) (which audits Android APKs for trackers and permissions), and what I found deserves its own term. I'm calling it Fedware.

Ok so let me walk you through what the federal government is running on your phone.

The FBI's app, [myFBI Dashboard](https://reports.exodus-privacy.eu.org/en/reports/com.fbi.dashboard/latest/?ref=sambent.com), requests 12 permissions including storage modification, Wi-Fi scanning, account discovery (it can see what accounts are on your device), phone state reading, and auto-start at boot. It also contains [4 trackers, one of which is Google AdMob](https://reports.exodus-privacy.eu.org/en/reports/com.fbi.dashboard/latest/?ref=sambent.com), which means the FBI's official app ships with an ad-serving SDK while also reading your phone identity. From what I found, the FBI's news app has more trackers embedded than most weather apps.

The FEMA app requests [28 permissions](https://reports.exodus-privacy.eu.org/en/reports/gov.fema.mobile.android/latest/?ref=sambent.com) including precise and approximate location, and has gone from 4 trackers in older versions down to 1 in v3.0.14. Twenty-eight permissions for an app whose primary function is showing you weather alerts and shelter locations. To put that in context, the AP News app delivers the same kind of disaster coverage with a fraction of the permissions.

IRS2Go has [3 trackers and 10 permissions](https://reports.exodus-privacy.eu.org/en/reports/search/gov.irs/?ref=sambent.com) in its latest version, and according to a [TIGTA audit](https://www.taxnotes.com/lr/resolve/tax-notes-today-federal/irs2go-smartphone-app-is-secure-tigta-says/w1dp?ref=sambent.com), the IRS released this app to the public before the required Privacy Impact Assessment was even signed, which violated OMB Circular A-130. The app shares device IDs, app activity, and crash logs with third parties, and TIGTA found that the IRS never confirmed that filing status and refund amounts were masked and encrypted in the app interface.

Federal Government Apps

Civilian News / RSS Apps

MyTSA comes in lighter with [9 permissions and 1 tracker](https://reports.exodus-privacy.eu.org/en/reports/gov.dhs.tsa.mytsa/latest/?ref=sambent.com), but still requests precise and approximate location. The TSA's own [Privacy Impact Assessment](https://www.dhs.gov/sites/default/files/publications/privacy_tsa_pia_028_a_mytsamobileapp_march2017.pdf?ref=sambent.com) says the app stores location locally and claims it never transmits GPS data to TSA. I'll give them credit for documenting that, because most of these apps have privacy policies that read like ransom notes.

CBP Mobile Passport Control is where things get genuinely alarming. This one requests [14 permissions including 7 classified as "dangerous"](https://reports.exodus-privacy.eu.org/en/reports/gov.dhs.cbp.pspd.mpc/latest/?ref=sambent.com): background location tracking (it follows you even when the app is closed), camera access, biometric authentication, and full external storage read/write. And the whole CBP ecosystem, from CBP One to CBP Home to Mobile Passport Control, feeds data into a network that retains your faceprints for [up to 75 years](https://www.americanimmigrationcouncil.org/research/cbp-one-overview?ref=sambent.com) and shares it across DHS, ICE, and the FBI.

The government also built a facial recognition app called [Mobile Fortify](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify?ref=sambent.com) that ICE agents carry in the field. It draws from [hundreds of millions of images](https://www.biometricupdate.com/202512/ices-use-of-cbp-biometric-surveillance-app-built-on-paper-thin-oversight?ref=sambent.com) across DHS, FBI, and State Department databases. ICE Homeland Security Investigations signed a [$9.2 million contract with Clearview AI](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition?ref=sambent.com) in September 2025, giving agents access to over 50 billion facial images scraped from the internet. DHS's own internal documents admit Mobile Fortify can be used to amass biographical information of ["individuals regardless of citizenship or immigration status"](https://www.biometricupdate.com/202512/ices-use-of-cbp-biometric-surveillance-app-built-on-paper-thin-oversight?ref=sambent.com), and CBP confirmed it will ["retain all photographs"](https://www.biometricupdate.com/202512/ices-use-of-cbp-biometric-surveillance-app-built-on-paper-thin-oversight?ref=sambent.com) including those of U.S. citizens, for 15 years.

Photos submitted through CBP Home, biometric scans from Mobile Passport Control, and faces captured by Mobile Fortify all feed this system. And the EFF found that ICE [does not allow people to opt out of being scanned](https://www.eff.org/deeplinks/2025/11/rights-organizations-demand-halt-mobile-fortify-ices-handheld-face-recognition?ref=sambent.com), and agents can use a facial recognition match to determine your immigration status even when other evidence contradicts it. A U.S.-born citizen was told he could be deported based on a biometric match alone.

[SmartLINK](https://themarkup.org/the-breakdown/2022/06/27/meet-smartlink-the-app-tracking-nearly-a-quarter-million-immigrants?ref=sambent.com) is the ICE electronic monitoring app, built by BI Incorporated, a subsidiary of the GEO Group (a private prison company that profits directly from how many people ICE monitors), under a $2.2 billion contract. The app collects geolocation, facial images, voice prints, medical information including pregnancy data, and phone numbers of your contacts. ICE's contract gives them ["unlimited rights to use, dispose of, or disclose"](https://themarkup.org/the-breakdown/2022/06/27/meet-smartlink-the-app-tracking-nearly-a-quarter-million-immigrants?ref=sambent.com) all data collected. The app's former terms of service allowed sharing "virtually any information collected through the application, even beyond the scope of the monitoring plan." SmartLINK went from 6,000 users in 2019 to over 230,000 by 2022, and in 2019, ICE used GPS data from these monitors to coordinate one of the largest immigration raids in history, arresting around 700 people across six cities in Mississippi.

And if you think your location data is safe because you use regular apps and avoid government ones, the federal government is buying that data too. Companies like [Venntel collect 15 billion location points from over 250 million devices every day](https://www.aclu.org/news/privacy-technology/new-records-detail-dhs-purchase-and-use-of-vast-quantities-of-cell-phone-location-data?ref=sambent.com) through SDKs embedded in over 80,000 apps (weather, navigation, coupons, games). DHS, FBI, DOD, and the DEA [purchase this data without warrants](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data?ref=sambent.com), creating a constitutional loophole around the Supreme Court's 2018 Carpenter v. United States ruling that requires a warrant for cellphone location history. The Defense Department even [purchased location data from prayer apps to monitor Muslim communities](https://www.eff.org/issues/location-data-brokers?ref=sambent.com). Police departments used similar data to track racial justice protesters.

And then there's the [IRS-ICE data sharing deal from April 2025](https://www.propublica.org/article/trump-irs-share-tax-records-ice-dhs-deportations?ref=sambent.com). The IRS and ICE signed a Memorandum of Understanding allowing ICE to receive names, addresses, and tax data for people with removal orders. ICE submitted 1.28 million names. The IRS [erroneously shared the data of thousands of people who should never have been included](https://www.pbs.org/newshour/politics/data-of-thousands-of-taxpayers-wrongly-shared-with-dhs-court-filing-says?ref=sambent.com). The acting IRS Commissioner, Melanie Krause, [resigned in protest](https://www.cnn.com/2025/04/08/politics/irs-dhs-sign-data-deal-undocumented-immigrants/index.html?ref=sambent.com). The chief privacy officer quit. One person leaving changes nothing about the institution, and the data was already out the door. A federal judge blocked further sharing in November 2025, ruling it likely violates IRS confidentiality protections, but by then the IRS was already building an automated system to give ICE bulk access to home addresses with minimal human oversight. The court order is a speed bump, and they'll find another route.

The apps, the databases, and the data broker contracts all feed the same pipeline, and no single agency controls it because they all share it.

The [GAO reported in 2023](https://www.gao.gov/products/gao-23-106443?ref=sambent.com) that nearly 60% of 236 privacy and security recommendations issued since 2010 had still not been implemented. Congress has been told twice, in 2013 and 2019, to pass comprehensive internet privacy legislation. It has done neither. And it won't, because the surveillance apparatus serves the people who run it, and the people who run it write the laws. Oversight is theater. The GAO issues a report, Congress holds a hearing, everyone performs concern for the cameras, and then the contracts get renewed and the data keeps flowing. It's working exactly as designed.

The federal government publishes content available through standard web protocols and RSS feeds, then wraps that content in applications that demand access to your location, biometrics, storage, contacts, and device identity. They embed advertising trackers in FBI apps. They sell the line that you need their app to receive their propaganda while the app quietly collects data that flows into the same surveillance pipeline feeding ICE raids and warrantless location tracking. Every single one of these apps could be replaced by a web page, and they know that. The app exists because a web page can't read your fingerprint, track your GPS in the background, or inventory the other accounts on your device.

You don't need their app. You don't need their permission to access public information. You already have a browser, an RSS reader, and the ability to decide for yourself what runs on your own hardware. Use them.

Question 1

How many embedded trackers does the White House app contain?

Question 2

Which Chinese company's tracking SDK is embedded in the White House app?

Question 3

Which FBI app tracker is used for serving targeted advertisements?

Question 4

How many permissions does the FEMA app request?

Question 5

How long does DHS retain faceprints collected through CBP apps?

Question 6

How much is CBP's contract with Clearview AI worth?

Question 7

How many location data points does Venntel collect per day?

Question 8

What private prison company's subsidiary built SmartLINK for ICE?

Question 9

What Supreme Court case ruled that warrants are required for cellphone location history?

Question 10

What percentage of GAO privacy recommendations from 2010 onward have still not been implemented?