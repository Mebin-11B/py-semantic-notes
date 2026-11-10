---
title: "Android Developer Verification"
url: https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html
clipped: 2026-06-17 01:24:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - app security
  - sideloading
  - developer ecosystems
  - platform control
  - digital sovereignty
  - open source software
related:
  - "[[Hardware Attestation as Monopoly Enabler]]"
  - "[[Discord will require a face scan or ID for full access next month]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Google is rolling out mandatory Android Developer Verification to curb sideloaded malware, requiring developers to register their identity and apps, which has sparked criticism over platform gatekeeping and user autonomy.
>
> **Key points:**
> - Android developer verification will require developers (including those distributing outside Google Play) to verify their identity to prevent anonymous malware distribution.
> - Beginning September 2026 in select countries and expanding globally in 2027, certified Android devices will restrict installation of unregistered apps, requiring ADB or a new "advanced flow" for sideloading.
> - To address hobbyists and students, Google is introducing a free "limited distribution" account that doesn't require a government ID but restricts app sharing to a maximum of 20 devices.
> - The developer community has reacted negatively, arguing that the system adds administrative burden, threatens open-source marketplaces, and moves Android closer to iOS's walled-garden model.
>
> **Concept links:** [[App Security]], [[Sideloading]], [[Developer Ecosystems]], [[Platform Control]], [[Digital Sovereignty]], [[Open Source Software]]
>
> **Suggested connections:**
> - [[Hardware Attestation as Monopoly Enabler]] — discussing how security verifications and attestation protocols are used by platform gatekeepers to centralize control and restrict third-party software.
> - [[Discord will require a face scan or ID for full access next month]] — exploring the growing trend of identity verification requirements across large digital platforms and services.
<!-- ai-summary:end -->

# [Android Developer Verification](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html)

## Digest Summary
Android developer verification is being rolled out to all developers via the Android Developer Console and Play Console to add a security layer against malware, especially from sideloaded sources. Key points:

- Developers distributing outside Google Play can create an account now; Play Console users should check for upcoming updates. Verified developers will have their apps automatically registered; otherwise a manual claim process applies.
- User download experience remains unchanged until September 2026, when enforcement begins in Brazil, Indonesia, Singapore, and Thailand, expanding globally in 2027. Unregistered apps will require ADB or an advanced sideloading flow.
- Integration enhancements: Android Studio will display app registration status during signed bundle/APK generation; Play Console will show per‑app status.
- Special provisions: a free “limited distribution” account (no government ID) for students/hobbyists to share with up to 20 devices (early access June 2026). Power users retain choice to install from any source.
- Timeline: Android Developer Verifier appears in system settings April 2026; registration deadline September 30 2026; global rollout in 2027.

## Discussion Summary
The discussion centers on widespread frustration with Google’s new Android Developer Verification system, which many see as an overly burdensome, slow, and intrusive process that threatens open‑source app stores and sideloaded software. Commenters argue it undermines user autonomy, imposes costly identity checks, and could disadvantage developers and users in restricted regions, while a minority point to potential security gains against malicious apps. Overall sentiment is largely negative, calling for alternatives such as custom ROMs, Linux‑based phones, or regulatory intervention, with limited support for the verification’s purported safety benefits.

---

## Full Article

![](https://blogger.googleusercontent.com/img/a/AVvXsEgKvPOrkQ6xhfp3JzKhlQS63WlgsKEc3iI6Jl6VdfitojtR0j9py3hJ3S3dkp2JF39HU6lUswIJpFupt2fm5uFfWB7408f4mhvHWsM8JeO5tk0-M0jHpk4A40an8gtipxyKpGJrGBtdE7JadUHnRodVFB9NIMkwmnNJFqWw0x1ncIAoVb9h13CeV1p_jyQ)

*Posted by Matthew Forsythe, Director Product Management, Android App Safety*

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp7z-fiVj1B5NnGKEaGJoMfWTJawStwh-CcY_xrjTaOS1UTWaf0Ex_tnqxhWGRx_rmxDR-GMTaeUVW896p0RBvwt8p_cxQ8gMU6cpMC0Ori8ammOxFIF2pxQsd9giZez-P-e5Kg-3fssWUhEGaXF0-UnfsS_kxAg9lLbDXl4hsTB1YMbfG3UkONUzG6Es/s16000/260317_ADV%20Blog_Header.png)

Android is for everyone. It’s built on a commitment to an open and safe platform. Users should feel confident installing apps, no matter where they get them from. However, our recent analysis found over **90 times** more malware from sideloaded sources than on Google Play. So as an extra layer of security, we are rolling out Android developer verification to help prevent malicious actors from hiding behind anonymity to repeatedly spread harm. Over the past several months, we’ve worked closely with the community to improve the design so we account for the many ways people use Android to balance openness with safety.

Start your verification today
-----------------------------

Today, we’re starting to **roll out Android developer verification to all developers** in both the new Android Developer Console and Play Console. This allows you to complete your verification and register your apps before user-facing changes begin later this year.

* If you only distribute apps outside of Google Play, you can create an account in [Android Developer Console](https://android.google.com/developerconsole) today.
* If you're on Google Play, check your [Play Console](https://play.google.com/console/u/0/developers/android-developer-verification) account for updates over the next few weeks. If you’ve already verified your identity here, then you’re likely already set.

Most of your users’ download experience will not change at all
--------------------------------------------------------------

While verification tools are rolling out now, the experience for users downloading your apps will not change until later this year. The user side protections will first go live in Brazil, Indonesia, Singapore, and Thailand this September, before expanding globally in 2027. We’ve shared this timeline early to ensure you have ample time to complete your verification.

Following this deadline, for the vast majority of users, the experience of installing apps will stay exactly the same. It’s only when a user tries to install an unregistered app that they’ll require ADB or [advanced flow](https://android-developers.googleblog.com/2026/03/android-developer-verification.html), helping us keep the broader community safe while preserving the flexibility for our power users.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLAfuJmgmy3cM1RmmUwCx9GJ2zf8j5y53m2tIlUkLvUU3QrAYczD3bDW4kP_bJXy7WPvW9IGIhNcoNyoOeUcMjQurDHQPVL4YJZEcF_ScwpJCyRbkAVG6ZyRdhydJ4Gmz2tL883XY3mxAKp6IPsCMWbFSTnDUyXJA-4CpC3qkgHcPhRX1kCwl401XPjlQ/s16000/260327_%5BABL_13%5D%20Inline%20asset%20for%20blog_v2.png)

*Developers can still choose where to distribute their apps. Most users’ download experience will not change*

Tailoring the verification experience to your feedback
------------------------------------------------------

To balance the need for safety with our commitment to openness, we’ve improved the verification experience based on your feedback. We’ve streamlined the developer experience to be more integrated with existing workflows and maintained choice for power users.

* **For Android Studio developers:** In the next two months, you’ll see your app's registration status right in Android Studio when you generate a signed App Bundle or APK.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6f-5qr7psaTT0Y5lQDMfTee4hH0LTk-LTkdqDckvou4K1kHAdDU6awUhU6ksHn2VkQhw9r8Y1RS6rv1cDFXGNwSyHlkSMP7QrbVpTFQNhhHYR_5lPisHw2Ak_2XVk263t-x1AIj4bQSYyHi1F-GPYGi8eLsv_MRUDMOQxLRoUTVNZ-Ypuz7za6hbMm3s/w400-h363/DeveloperVerificationAndroidStudio.png)

*You’ll see your app's registration status in Android Studio when you generate a signed App Bundle or APK.*

* **For Play developers:** If you've completed Play Console's developer verification requirements, your identity is already verified and we'll automatically register eligible Play apps for you. In the rare case that we are unable to register your apps for you, you will need to follow the manual app claim process. Over the next couple of weeks, more details will be provided in the Play Console and through email. Also, you’ll be able to register apps you distribute outside of Play in the Play Console too.

![](https://blogger.googleusercontent.com/img/a/AVvXsEgrL7u2zF7sQXhyJij9fpRMnkjwRDnWD8AJ3mkSJlK0kUOmx4H-Yc6w5sFyEG_rcV4rKqcXPL3WZD0gzrRt3ShZiZ2vtN6q0RwPrWZVpgZq1kC-ng_2g93dtB2bH8RgNGxKQwCSV0xjKMzkCIVCMzmRWM1rsu0QxxXr4PXjvNhDH8OHq9dzyXXr8c8hwdQ=s16000)

*The Android developer verification page in your Play Console will show the registration status for each of your apps.*

* **For students and hobbyists:** To keep Android accessible to everyone, we're building a free, no government ID required, limited distribution account so you can share your work with up to 20 devices. You only need an email account to get started. [Sign up for early access](https://google.qualtrics.com/jfe/form/SV_4N7NGE06NjJJdl4). We’ll send invites in June.
* **For power users:** We are maintaining the choice to install apps from any source. You can use the new [advanced flow](https://android-developers.googleblog.com/2026/03/android-developer-verification.html) for sideloading unregistered apps or continue using ADB. This maintains choice while protecting vulnerable users.

What’s next?
------------

We’re rolling this out carefully and working closely with developers, users, and our partners. In April, we’ll introduce Android Developer Verifier, a new Google system service that will be used to check if an app is registered to a verified developer.

* **April 2026:** Users will start to see Android Developer Verifier in their Google Systems services settings.
* **June 2026:** Early access: Limited distribution accounts for students and hobbyists.
* **August 2026:**
* **September 30, 2026:** Apps must be registered by verified developers in order to be installed and updated on certified Android devices in Brazil, Indonesia, Singapore, and Thailand. Unregistered apps can be sideloaded with ADB or advanced flow.
* **2027 and beyond:** We will roll out this requirement globally.

We’re committed to an Android that is both open and safe. Check out our [developer guides](https://developer.android.com/developer-verification) to get started today.