---
title: "Flock Hardcoded the Password for America's Surveillance Infrastructure 53 Times"
url: https://nexanet.ai/blog/53-times-flocksafety-hardcoded-the-password-for-americas-surveillance-infrastructure
clipped: 2026-06-17 02:01:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Flock Hardcoded the Password for America's Surveillance Infrastructure 53 Times](https://nexanet.ai/blog/53-times-flocksafety-hardcoded-the-password-for-americas-surveillance-infrastructure)

## Digest Summary
A default organization‑wide ArcGIS API key was hard‑coded into 53 publicly accessible JavaScript bundles served by Flock Safety. The key—created automatically when the company signed up for an ArcGIS developer account—had no referrer, IP or scope restrictions and was granted 50 “portal:app:access:item” privileges, allowing read access to private ArcGIS items. Querying the API revealed that these items host the unified “FlockOS” mapping layer, which aggregates data from roughly 12 000 law‑enforcement, community and private deployments, including:

- License‑plate and people detections, hotlist alerts, and vehicle‑search records  
- Real‑time locations of patrol cars, body‑camera units, drones, and Raven audio sensors  
- Camera inventories, serial numbers, uptime, and registrant contact information  
- Flock911 incident layers with call IDs, transcript tokens and audio playback data  

A separate, unauthenticated token‑minting flaw enabled generation of valid ArcGIS tokens for the same production environment. The vulnerabilities were disclosed in November 2025; after 55 days the API key remained unrotated and the token issue unfixed. The exposure provides a single point of entry to nationwide surveillance data, raising significant intelligence‑gathering and domestic‑privacy risks.

## Discussion Summary
The comments express strong criticism of Flock’s privacy practices and distrust of the company’s competence, portraying its surveillance technology as invasive and poorly evaluated by municipal officials. Many contributors highlight difficulties in removing installed cameras and question the legitimacy of the company’s security claims, while also noting recent efforts to improve internal security staffing. Skepticism appears regarding technical explanations in related articles, and there is a broader concern that public camera feeds should remain openly accessible, reflecting a desire for greater oversight and transparency.

---

## Full Article

|  |  |
| --- | --- |
| Vendor | Flock Safety |
| Affected Products | Flock Safety's ArcGIS, FlockOS, Aerodome, Flock911 |
| Vulnerability Type | Hardcoded API Key Exposure (CWE-798) |
| Exposure Count | 53 separate instances across public-facing assets compromising 50 data layers |
| Data at Risk | ~5,000 police departments, ~6,000 community deployments, and ~1,000 private businesses |
| Status | Remediated following responsible disclosure |

Executive Summary
-----------------

I discovered a Default ArcGIS API key embedded in Flock Safety's public-facing JavaScript bundles. This single credential granted access to the company's ArcGIS mapping environment, and 50 private layers, the same infrastructure that consolidates license plate detections, patrol car locations, drone telemetry, body camera locations, 911 call data, and surveillance camera locations from approximately 12,000 law enforcement, community, and private sector deployments nationwide.

The key was not restricted by referrer, IP, or origin allowing it to be used by anyone, anywhere. It was exposed publicly across **53 separate Flock Safety front-end bundles and environments**, each instance independently granting access to their ArcGIS mapping platform.

---

Background: What is Flock Safety?
---------------------------------

Across the United States, license plate readers, drones, and audio sensors quietly record the movements of millions of people every day. Flock Safety operates one of the largest and most rapidly expanding of these networks, with hundreds of thousands of cameras generating over 30 billion vehicle detections each month, and an undisclosed amount of people detections.

At the center of this infrastructure is **FlockOS**, which Flock markets under the headline *"One map. Smarter Response."* According to their own documentation, the ArcGIS-powered interface "consolidates all data streams and the locations of each connected asset, enabling greater situational awareness and a common operating procedure." ([Source: ClearGov Resource Document](https://cleargov.com/resource/cg-prod-v2/projects/documents/8491cdf11839242bf5e2.pdf))

That "one map" is not a metaphor. It is the ArcGIS stack itself and the exposed API key unlocked it.

---

The Vulnerability
-----------------

The exposed credential was an organization-wide ArcGIS API key tied directly to Flock Safety's ArcGIS mapping environment. It appeared in client-side JavaScript bundles served from development subdomains that were publicly accessible.

Querying the ArcGIS API with this key returned metadata confirming its scope and the extent of Flock's misconfiguration:

![Flock API Key (Redacted)](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fapi_key_red.2ibfbev5yn8r8.png&w=1080&q=75)

The credential was tagged appTitle: "Default API Key", the auto-generated key Esri creates at account signup. According to [Esri's ArcGIS documentation](https://developers.arcgis.com/python/latest/guide/part1-what-is-geocoding/):

> "An API key is a permanent access token that defines the scope and permission for granting your public-facing application access to specific, ready-to-use services **and private content**... **An API key is created for you when you sign up for an ArcGIS Developer account.**"

The key's metadata listed 50 "portal:app:access:item: privileges each granting access to a private ArcGIS item.

Given Flock's centralized "one map" architecture where participating agencies contribute data to shared, Flock-owned layers rather than maintaining separate instances each of those 50 private items likely aggregates data from hundreds or thousands of agencies. A single Detections layer would contain hotlist hits from all ~5,000 participating police departments. A single Mobile Units layer would show patrol car positions across every integrated agency.

Esri's documentation warns:

> "For the highest level of security, always set the API key scopes and referrers before deploying an application."

Flock applied no referrer restrictions, no IP allowlist, and no scope limitations. They took the default key, granted it access to 50 private items, and embedded it in client-side JavaScript bundles across 53 publicly accessible endpoints:

53 Exposed Endpoints (hostnames redacted):

`[redacted].flocksafety.com` `[redacted].flocksafety.com/.../flock-DzA9VKXM.js``[redacted].flocksafety.com/.../index-slKO6jum.js``[redacted].flocksafety.com/.../index-BBRurSLX.js`

Show all 53 endpoints

`[redacted].flocksafety.com/.../index-BPxp6hzB.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-BoZI8MYY.js``[redacted].flocksafety.com/.../notificationExpireWorker-_11bsRZ0.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-NGZrpZsD.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-na0tVtmO.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-BpcA2uVs.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-DLZtzWUN.js``[redacted].flocksafety.com/.../index-xrDxc-Lv.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-J-ZVyGSG.js``[redacted].flocksafety.com/.../notificationExpireWorker-4m9KycyN.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-by_qQfZs.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-reQjrWVk.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-XS3Uur-m.js``[redacted].flocksafety.com/.../index-ztnhrNoG.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-HA5zO2gU.js``[redacted].flocksafety.com/.../notificationExpireWorker-8Pe_fNZM.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-Dro5OKrq.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-wJjUIzMY.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-9gsy_LJ6.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker--KqStPhO.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-3cNFqmkh.js``[redacted].flocksafety.com/.../index-Bas-zpR9.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-B1jQx_EB.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-DYLz-f8O.js``[redacted].flocksafety.com/.../notificationExpireWorker-Bix-gxWk.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-5vLUhmkY.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-DA2TrQ_9.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-D6gTd4TT.js``[redacted].flocksafety.com/.../index-DGGtSpOn.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-D1Fw4UF9.js``[redacted].flocksafety.com/.../notificationExpireWorker-wjAN01b6.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-BoXGrJ_I.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-CYEuywlF.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-BM2HGkks.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-DW-LQUZh.js``[redacted].flocksafety.com/.../index-BtFbKoWO.js``[redacted].flocksafety.com/.../notificationExpireWorker-Bs_qqZKK.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-W6tR54zI.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-D3Gi0z83.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-gofSdgry.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-HayKEVyk.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-BzI_7Vif.js``[redacted].flocksafety.com/.../index-DrW4QnA-.js``[redacted].flocksafety.com/.../subjectMessageExpireWorker-D3Gi0z83.js``[redacted].flocksafety.com/.../notificationExpireWorker-Bs_qqZKK.js``[redacted].flocksafety.com/.../notificationAnalyticsTracker-W6tR54zI.js``[redacted].flocksafety.com/.../visualSearchExpireWorker-gofSdgry.js``[redacted].flocksafety.com/.../visualSearchExpiringWorker-HayKEVyk.js``[redacted].flocksafety.com/.../prepared911ExpireWorker-BzI_7Vif.js`

Each endpoint independently served the same unrestricted credential 53 times, and any one of them could have been used to access Flock's ArcGIS environment.

---

FlockOS: The Unified Attack Surface
-----------------------------------

The FlockOS map component signature reveals the unified layer architecture:

```
ru=({
  esriMapsApiKey: t,
  baseLayers: n,
  dynamicLayers: i,
  featureLayers: o,
  markerLayers: a,
  nonClusteredMarkerLayers: s,
  clusteredMarkerLayers: l,
  heatmapLayers: h,
  focusedMarkers: p,
  selectedLayers: g,
  setSelectedLayers: A,
  onBaseLayerChange: y,
  onCustomMapLayerSelectionChange: b
})
```

A single component consumes the Esri API key alongside every layer type: base maps, dynamic overlays, feature layers, clustered and non-clustered markers, and heatmaps. Layer selection state is managed uniformly across all data sources.

Internal permission flags from JavaScript bundles confirm FlockOS's role as the unified interface:

* canUseFlockOS911
* canUseCAD
* canDispatchDrone
* canManageIntegrations

**FlockOS is the interface; ArcGIS is the substrate.** The exposed API key granted access to the common mapping layer where all Flock Safety applications converge: camera inventories, mobile units, detection outputs, hotlists, search geometries, drone telemetry, Raven analytics, officer-accessible views, and Flock911 incidents.

---

Exposed Data Categories
-----------------------

### Surveillance Infrastructure

* Camera deployments operated by police departments, communities, and private businesses
* Third-party devices connected via Wing Gateways
* Raven audio gunshot detection sensors
* Drone assets with live status

![Camera Type Data](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcamera_type_data.1h25kt47fhm1b.png&w=1080&q=75)

### Law Enforcement Location Data

* Live and historical patrol car GPS positions
* Axon body-worn camera locations
* Officer mobile app location data (phone, smartwatch)
* Trailers and auxiliary GPS trackers
* CAD (Computer-Aided Dispatch) event layers and patrol history

![Mobile PD Car Location](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FMobile_PD_Car_Location.3qqfg0p15tg8f.png&w=3840&q=75)

### People and Vehicle Intelligence

* People detection alerts with camera IDs, time windows, confidence thresholds, and expiration timestamps
* People searches rendered as tracked objects on the map
* Vehicle alerts and vehicle description alerts
* Vehicle searches persisted alongside detections
* Audio alerts including gunshot detection popups with classification (single shot vs. multiple shots)

![People Detection Alert](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fperson_detection_alert.1m8cz2zsupdid.png&w=1920&q=75)

### Hotlists and Investigative Data

* Hotlist detections with topic names, alert reasons, filter IDs, deduplicated detection IDs, license plate numbers, and time/location data
* Saved search filters—analyst searches persisted as spatial objects
* Search footprints—the actual polygons and radii investigators draw when selecting geographic areas of interest

![Detections](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FDetections_Image.3fm6-cczu7lis.png&w=3840&q=75)![More Searches LPR](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FMore_Searches_LPR_for_LP.2__scyozreu85.png&w=3840&q=75)

### Personally Identifiable Information

* Camera registrant names
* Email addresses
* Phone numbers
* Location types (law enforcement, non-law enforcement, private)
* Postal addresses
* Counts of interior and exterior cameras per location
* Arrays of associated camera locations

![Camera Registry Demo](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcamera_registry_demo.1tyafngpwiae_.png&w=3840&q=75)

### Camera Registry and Asset Data

Each camera record exposed:

* Physical deployment location
* Device serial numbers
* Device uptime percentages
* Operational status
* Flock support and service metadata

![Camera Metadata (Tampa)](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FCamera_Metadata_Tampa.3a0osl117ip-1.png&w=3840&q=75)

### Flock911 Emergency Data

A dedicated ArcGIS FeatureServer layer for Flock911 incidents exposed:

* Live incident locations
* Call IDs
* Transcript access tokens
* Per-word transcript timing data
* Audio scrub positions and playback state
* Incident classification
* Active and selected incident identifiers

Audio and transcript data flows through the same map context as cameras, patrol units, and alerts. No separate security boundary exists at the mapping layer.

![Flock911 Layer](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflock911_layer.25ymwasve5wcd.png&w=1080&q=75)![Flock Transcript](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflock_transcript.2p3semyqw1vsn.png&w=1920&q=75)

### Drone Telemetry (Aerodome Integration)

Every status chip rendered on the patrol/device tray (via hQ) only recognizes the values: `Docked`, `Buffering`, `Recording`, `Inactive`, `Offline`, `Off`, `ON`, `ONLINE`, `ACTIVE`, `Charging`, and `Uploading`. Statuses in the "online/charging/buffering" group render as green; "inactive/offline/off" renders gray; and "recording" renders red. This confirms the complete set of device states actively rendered on the shared map UI.

![Drone Layers](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdrone_layers.2o4pt073_7biu.png&w=1080&q=75)![Drone Demo](https://nexanet.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdrone_demo.0m5xqlkihckf6.png&w=1080&q=75)

---

Pattern of Credential Exposure
------------------------------

The exposed Default API Key was not an isolated incident.

I separately disclosed an additional critical vulnerability involving unauthenticated ArcGIS token minting. This vulnerability allows unauthenticated users to obtain valid ArcGIS tokens scoped to Flock Safety's production environment from their development environment, tokens titled "Flock Safety Prod" that grant access to the geographic mapping of Flock's camera network locations.

* **November 13, 2025** — Initial disclosure sent to Flock Safety security team
* **November 14, 2025** — First follow-up requesting confirmation of receipt
* **November 19, 2025** — Second follow-up; Flock Safety finally acknowledges receipt
* **January 7, 2026** — Vulnerability remains unpatched (55+ days)

I am withholding specific technical details to prevent exploitation while the vulnerability remains unpatched. However, its existence more than 55 days after responsible disclosure with no remediation, demonstrates a systemic pattern of credential mismanagement.

### Comparing the Exposed Credentials

| Property | Default API Key | Flock Safety Prod |
| --- | --- | --- |
| Portal Item Access | 50 private items | None |
| Camera Network Access | Yes (via item access) | Yes (direct FeatureLayer) |
| Source | Dev site JS bundles | Unauthenticated token minting |
| Status | Fixed (June 2025) | Unpatched (55+ days) |

Both keys operated under the same active subscription with nearly one million available credits. Critically, **development environments were configured with broader access than production**, and those development sites were publicly accessible.

---

Scope Limitations and Evidentiary Standard
------------------------------------------

The 50 "portal:app:access:item" privileges reference private item IDs that cannot be inventoried without actively querying each one which I did not do. However, ArcGIS collaboration features allow partner organizations to share layers into another organization's portal, and evidence suggests this capability was actively used.

An individual at a sheriff's office with an active Flock deployment confirmed during the course of this research that their agency shares ArcGIS layers directly with Flock Safety's organization. This corroborates the technical architecture documented in Esri's collaboration documentation and aligns with the privilege structure observed in the exposed credential metadata.

What I *can* state with certainty:

1. The API key's metadata explicitly listed 50 `portal:app:access:item:` privileges granting access to private ArcGIS items
2. Esri's own documentation confirms that such privileges grant access to "hosted feature services, web maps, web scenes, tile layers" and other private portal content
3. A law enforcement source with direct knowledge of their agency's Flock integration confirmed that layer sharing with Flock Safety's ArcGIS organization occurs in practice
4. The key appeared across 53 publicly accessible endpoints with no referrer restrictions, IP limitations, or access controls
5. Many of the photo's I've used as examples are from publicly exposed ArcGIS datasets owned by Police Departments, that have relevant Flock Safety data in them.

Taken together, these findings establish that the exposed credential provided a viable technical pathway to access shared law enforcement data. The precise contents of each private layer remain unverified, yet the circumstantial evidence is substantial.

---

Why This Matters: National Security Implications
------------------------------------------------

### Intelligence Value of Movement Data

Foreign intelligence services would not need access to communications content if they could reliably observe movement at this scale. Historical location data revealing the presence, routines, and associations of politicians, federal agents, intelligence personnel, military leadership, or special operations units constitutes intelligence in its own right.

Consider a scenario: If members of SEAL Team 6 or Delta Force disappear from roadways for several days, that absence is itself a signal. If, during the same timeframe, a primary French translator also vanishes from routine movement patterns, the signal sharpens. A coordinated absence across these roles would strongly suggest the initiation of a special operations mission inferred solely from movement data collected by a nationwide license plate reader network. A top secret clearance wouldn't be needed for top secret information.

China has previously compromised hotel infrastructure for years at a time, not to surveil ordinary guests, but to capture rare overlaps where officials from different countries stayed in the same location on the same night. ([Source](https://www.nytimes.com/2018/12/11/us/politics/trump-china-trade.html)) If adversaries are willing to infiltrate hotel systems for fragments of movement data, the intelligence value of a nationwide, centralized surveillance map should be self-evident.

### Domestic Risks

Persistent, indiscriminate movement tracking enables coercion, blackmail, and influence operations that do not require access to communications content. Members of Congress, senior military leaders, diplomats, corporate executives and their spouses and children are all placed at heightened risk. With sufficient coverage and time, patterns of life emerge. Affairs, undisclosed meetings, sensitive relationships, and routine behaviors become visible once movement data is collected and correlated at scale.

This is not a theoretical concern. The documented history of law enforcement misuse of license plate reader systems, including Flock's own platforms, demonstrates that access to movement data is routinely weaponized for personal purposes by those entrusted with it.

#### Documented Cases of Flock Camera Misuse

**Braselton, Georgia (November 2025):** Police Chief Michael Steffman was arrested and charged with stalking, harassment, and multiple counts of misusing automated license plate recognition systems after a months-long Georgia Bureau of Investigation probe revealed he used Flock cameras to track and harass multiple individuals. Steffman resigned hours before his arrest after serving the department for 20 years. Subsequent public records analysis by the grassroots coalition Get The Flock Out revealed that Steffman had searched Flock data from agencies in other states, including Capitola, California, demonstrating the cross-jurisdictional reach enabled by Flock's network sharing capabilities. ([Source](https://lookout.co/georgia-police-chief-arrested-for-using-flock-cameras-for-stalking-and-harassment-searched-capitola-data-earlier-this-year/story))

**Sedgwick, Kansas (2023–2024):** Police Chief Lee Nygaard used Flock Safety license plate readers to track his ex-girlfriend's vehicle 164 times and her new boyfriend's vehicle 64 times over a four-month period. He logged false justifications including "missing child," "drug investigation," and "suspicious activity" to conceal the personal nature of his searches. Nygaard also followed the couple in his patrol vehicle outside city limits. He resigned during the misconduct investigation. His police certification was revoked, though he faced no criminal charges. ([Source](https://local12.com/news/nation-world/police-chief-gets-caught-using-license-plate-cameras-to-track-his-ex-girlfriend-228-times-arrests-charges-probation-flock-safety-follow-stalk-new-boyfriend-broke-up-out-of-town-misuse))

**Orange City, Florida (2024–2025):** Officer Jarmarus Brown was arrested and charged with stalking and unauthorized computer access after using Flock license plate readers to track his ex-girlfriend's whereabouts for approximately seven months. An audit revealed he had repeatedly run tags for three specific vehicles. A fellow officer had warned Brown to "stop running her vehicle in that system because he could get in trouble" a warning Brown ignored. Brown also placed a GPS AirTag in the victim's wallet without her knowledge. When confronted by investigators, Brown admitted the situation was "dumb as hell on my end." He was served termination paperwork following his arrest. ([Source](https://www.clickorlando.com/news/local/2025/02/05/dumb-as-hell-orange-city-officer-accused-of-stalking-woman-using-license-plate-readers/))

These cases share common patterns: trusted officials often in leadership positions weaponizing surveillance tools against women with no connection to criminal investigations. The systems provided few meaningful barriers to misuse, and detection typically occurred only after victims independently reported suspicious behavior.

### Congressional Concerns Validated

My research directly supports Senator Ron Wyden's claims that "Flock cannot live up to its commitment to protect the privacy and security of Oregonians" ([Letter to Flock](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_flock.pdf)) and his urging for the "Federal Trade Commission (FTC) investigate Flock Safety... and, where appropriate, hold the company responsible for its negligent cybersecurity practices" ([Letter to FTC](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_flockpdf.pdf)).

---

On Flock's Security Claims
--------------------------

After the City of Staunton canceled its Flock Safety contract, CEO Garrett Langley sent an unsolicited email to Staunton Police Department ([source](https://www.ci.staunton.va.us/home/showpublisheddocument/13448/639017375545800000)) stating:

> "I'm writing to you directly because I want there to be zero confusion about what's happening. **Flock has never been hacked. Ever.**"

That statement is technically correct only in the narrowest sense. The absence of a breach was not the result of internal security controls, audits, or monitoring but of responsible disclosure. I identified the vulnerability and reported it so it could be remediated.

The absence of a hack does not imply the presence of security. Had this credential been found by anyone else, this may have been one of the largest data breaches and national security incidents of this decade.

### On Compliance Claims

In the same communication, Flock asserted:

> "**Flock is CJIS compliant**"  
> "**Flock adheres to the highest security standards, including NDAA, SOC 2 (Type II), SOC 3, ISO 27001, HECVAT, FERPA, and alignment with NIST and CAIQ.**"

As a cybersecurity professional who has conducted dozens of compliance assessments, these statements are familiar. Compliance frameworks are often mistaken for guarantees of security, when in reality they are **scoped evaluations of specific controls**, not comprehensive examinations of an organization's risk posture. The scope of what is tested is defined by the company being assessed, which means compliance reflects what was reviewed, not everything that exists.

I requested access to Flock's audit reports; they were not provided. What I can say is this: a default, organization-wide API key embedded across 53 publicly reachable development and production-adjacent web assets would not survive even a basic review for exposed secrets or subdomains. Its persistence strongly suggests that this attack surface was either excluded from the assessment scope or insufficiently tested.

When a default, organization-wide credential persists across 53 publicly reachable assets, the failure is not merely procedural, it is architectural. The exposed surface was not a peripheral feature or isolated test environment. It was development infrastructure configured with privileges that would have granted access to private ArcGIS items shared within Flock Safety's organization.

What You Can Do
---------------

**If you're a resident:** File a public records request for your city's Flock Safety contract and any internal audit logs. Attend the next city council meeting where surveillance procurement is discussed. The EFF maintains a [Street-Level Surveillance](https://www.eff.org/issues/street-level-surveillance) resource for tracking these deployments.

**If you're a journalist:** The technical evidence presented here is a starting point. I'm available for follow-up. There are more threads to pull.

**If you're in law enforcement:** Ask your vendor hard questions. Request their penetration test results. Demand to know where your agency's data lives and who else can access it. Your officers' safety depends on infrastructure that adversaries cannot trivially compromise.

**If you're a policymaker:** Senator Wyden's letters to Flock and the FTC are public record. Support an investigation. Mandate independent security audits for any vendor handling law enforcement location data.

---

Conclusion
----------

Although the API key has now been rotated, the lesson remains. If a single cybersecurity researcher in his early twenties could gain direct technical access to an exposure of this magnitude, a well-resourced foreign adversary operating with intent could observe far more.

Flock Safety did not merely leak an API key. They exposed the operational heartbeat of the nation, and they did so repeatedly, across 53 separate instances.

That reality should concern everyone.