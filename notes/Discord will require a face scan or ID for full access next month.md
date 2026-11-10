---
title: "Discord will require a face scan or ID for full access next month"
url: https://www.theverge.com/tech/875309/discord-age-verification-global-roll-out
clipped: 2026-06-17 01:47:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Discord will require a face scan or ID for full access next month](https://www.theverge.com/tech/875309/discord-age-verification-global-roll-out)

## Digest Summary
Discord will globally roll out age verification next month, defaulting all accounts to a “teen‑appropriate” experience unless users prove they are adults. Verification relies first on an age‑inference model that uses account tenure, device and activity data, and community‑level patterns; it does not analyze private messages. Users who cannot be inferred as adults must submit a facial‑age estimate via a video selfie (processed locally) or provide a government ID to a third‑party vendor, after which the ID image is deleted promptly. Unverified teens will be blocked from age‑restricted servers, “stage” channels, and graphic content; such servers will appear as black screens until verification. Direct messages from unknown users will be filtered, and friend‑request warnings will appear. Discord discontinued its previous vendor after an October data breach exposed verification data and now uses a new vendor, emphasizing no biometric scanning or retention of personal details. The company expects limited impact on most users but acknowledges some user loss and plans mitigation strategies.

## Discussion Summary
The comments express strong concern about mandatory ID verification and data collection by platforms such as Discord, Google, and Meta, citing recent breaches and privacy risks. Many users advocate for self‑hosted, open‑source alternatives like Zulip, Matrix, IRC, and Signal, emphasizing control over data and resistance to corporate or governmental surveillance. Frustration with regulatory approaches that exempt politicians and the perceived drift of startups toward profit over user interests is common, while some suggest canceling paid services and returning to earlier, less centralized communication methods.

---

## Full Article

Discord [announced on Monday](https://discord.com/press-releases/discord-launches-teen-by-default-settings-globally) that it’s rolling out age verification on its platform globally starting next month, when it will automatically set all users’ accounts to a “teen-appropriate” experience unless they demonstrate that they’re adults.

“For most adults, age verification won’t be required, as Discord’s age inference model uses account information such as account tenure, device and activity data, and aggregated, high-level patterns across Discord communities. Discord does not use private messages or any message content in this process,” Savannah Badalich, Discord’s global head of product policy, tells *The Verge*.

Users who aren’t verified as adults will not be able to access age-restricted servers and channels, won’t be able to speak in Discord’s [livestream-like “stage” channels](https://discord.com/stages), and will see content filters for any content Discord detects as graphic or sensitive. They will also get warning prompts for friend requests from potentially unfamiliar users, and DMs from unfamiliar users will be automatically filtered into a separate inbox.

Direct messages and servers that are not age-restricted will continue to function normally, but users won’t be able to send messages or view content in an age-restricted server until they complete the age check process, even if it’s a server they were part of before age verification rolled out. Badalich says those servers will be “obfuscated” with a black screen until the user verifies they’re an adult. Users also won’t be able to join any new age-restricted servers without verifying their age.

**1/2**

*Unverified users won’t be able to enter age-restricted servers.*

 Image: Discord

Discord’s global age verification launch is part of [a wave of similar moves](https://www.theverge.com/analysis/715767/online-age-verification-not-ready) at other online platforms, driven by an international legal push for age checks and stronger child safety measures. This is not the first time Discord has implemented some form of age verification, either. It initially rolled out age checks for users [in the UK and Australia](https://www.theverge.com/news/650493/discord-age-verification-face-id-scan-experiment) last year, which some users figured out how to circumvent [using *Death Stranding*’s photo mode](https://www.theverge.com/report/714402/uk-age-verification-bypass-death-stranding-reddit-discord). Badalich says Discord “immediately fixed it after a week,” but expects users will continue finding creative ways to try getting around the age checks, adding that Discord will “try to bug bash as much as we possibly can.”

It’s not just teens trying to cheat the system who might attempt to dodge age checks. Adult users could avoid verifying, as well, due to concerns around data privacy, particularly if they don’t want to use an ID to verify their age. In October, one of Discord’s former third-party vendors [suffered a data breach](https://www.theverge.com/news/792032/discord-customer-service-data-breach-hack) that exposed users’ age verification data, including images of government IDs.

If Discord’s age inference model can’t determine a user’s age, a government ID might still be required for age verification in its global rollout. According to Discord, to remove the new “teen-by-default” changes and limitations, “users can choose to use facial age estimation or submit a form of identification to [Discord’s] vendor partners, with more options coming in the future.”

The first option uses AI to analyze a user’s video selfie, which Discord says never leaves the user’s device. If the age group estimate (teen or adult) from the selfie is incorrect, users can appeal it or verify with a photo of an identity document instead. That document will be verified by a third party vendor, but Discord says the images of those documents “are deleted quickly — in most cases, immediately after age confirmation.”

*Users can view and update their age group from their profile.*

 Image: Discord

Badalich also says after the October data breach, Discord “immediately stopped doing any sort of age verification flows with that vendor” and is now using a different third-party vendor. She adds, “We’re not doing biometric scanning [or] facial recognition. We’re doing facial estimation. The ID is immediately deleted. We do not keep any information around like your name, the city that you live in, if you used a birth certificate or something else, any of that information.”

“A majority of people are not going to see a change in their experience.”

Badalich goes on to explain that the addition of age assurance will mainly impact adult content: “A majority of people on Discord are not necessarily looking at explicit or graphic content. When we say that, we’re really talking about things that are truly adult content [and] age inappropriate for a teen. So, the way that it will work is a majority of people are not going to see a change in their experience.”

Even so, there’s still a risk that some users will leave Discord as a result of the age verification rollout. “We do expect that there will be some sort of hit there, and we are incorporating that into what our planning looks like,” Badalich says. “We’ll find other ways to bring users back.”

***Correction, January 9th:*** *Removed note about the types of metadata Discord’s inference model uses and added quote from Savannah Badalich, Discord’s global head of product policy*, *clarifying the use of the inference model.*

**Follow topics and authors** from this story to see more like this in your personalized homepage feed and to receive email updates.

* Stevie Bonifield
* Apps
* Gaming
* News
* PC Gaming
* Policy
* Tech