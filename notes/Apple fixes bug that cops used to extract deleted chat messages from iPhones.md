---
title: "Apple fixes bug that cops used to extract deleted chat messages from iPhones"
url: https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/
clipped: 2026-06-17 01:13:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Mobile Security
  - Encryption
  - Privacy Policy
  - iOS Development
  - Forensics
related:
  - "[[Mobile Security]]"
  - "[[Encryption]]"
  - "[[Privacy Policy]]"
  - "[[iOS Development]]"
  - "[[Forensics]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Apple patched a bug where iOS cached notifications for up to a month, allowing law enforcement forensic tools to extract deleted Signal and WhatsApp messages.
>
> **Key points:**
> - The security flaw allowed notifications for deleted messages to be stored inside the device's system notification database.
> - The issue was revealed after the FBI successfully extracted deleted Signal messages from a suspect's iPhone using forensic software.
> - Signal President Meredith Whittaker urged Apple to fix the bug, stating notifications shouldn't persist in any OS notification database.
> - The patch was back-ported to iOS 18 and older versions, restoring the security of automatic message deletion features.
>
> **Concept links:** [[Mobile Security]], [[Encryption]], [[Privacy Policy]], [[iOS Development]], [[Forensics]]
>
> **Suggested connections:**
> - [[Mobile Security]] — how OS-level caching can bypass app-level encryption and privacy controls.
> - [[Privacy Policy]] — the tension between law enforcement forensic tools and consumer device encryption.
<!-- ai-summary:end -->

# [Apple fixes bug that cops used to extract deleted chat messages from iPhones](https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/)

## Digest Summary
Apple issued an iOS/iPadOS update that stops a bug where notification payloads were cached on devices for up to a month, permitting deleted or self‑destructing messages to be recovered. The issue, first reported by 404 Media, showed that the FBI could retrieve deleted Signal messages because their content remained in the system’s notification database after the app deleted them. Signal’s president asked Apple to eliminate the retention of notifications for deleted messages; Apple’s fix, back‑ported to iOS 18, removes the stored data. Apple has not explained why the notifications were originally retained and did not comment on the FBI’s forensic methods. Privacy advocates warned that the bug undermined security features (e.g., timed‑message deletion) used by at‑risk users to protect communications from device seizure.

## Discussion Summary
The comments focus on privacy risks from notifications that persist in device storage after display, noting that Apple and Google’s services route content through servers and cache it locally, undermining end‑to‑end encryption. Users highlight a recent fix that removes cached entries when an app is deleted but criticize Signal’s lack of user alerts and the broader inability of apps to prevent OS‑level storage. There is general distrust of closed platforms, calls for generic “message received” alerts, and speculation about similar issues on Android, while acknowledging the recent iOS update addressed the specific bug.

---

## Full Article

Apple released a software update on Wednesday for iPhones and iPads fixing a bug that allowed law enforcement to extract messages that had been deleted or disappeared automatically from messaging apps. This was because notifications that displayed the messages’ content were also cached on the device for up to a month.

In a security notice on its website, Apple [said that the bug](https://support.apple.com/en-us/127002) meant “notifications marked for deletion could be unexpectedly retained on the device.”

This is a clear reference to an issue [revealed by 404 Media](https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database-2/) earlier this month. The independent news outlet reported that the FBI had been able to extract deleted Signal messages from someone’s iPhone using forensic tools, due to the fact that the content of the messages had been displayed in a notification and then stored inside a phone’s database — even after the messages were deleted inside Signal.

After the news, Signal president Meredith Whittaker said the messaging app maker asked Apple to address the issue. “Notifications for deleted messages shouldn’t remain in any OS notification database,” Whittaker [wrote in a post on Bluesky](https://bsky.app/profile/meredithmeredith.bsky.social/post/3mjhq7fuabk2w).

#### Contact Us

Do you have more information about how authorities are using forensic tools on iPhones or Android devices? From a non-work device, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or

[email](mailto:lorenzo@techcrunch.com/)[.](mailto:lorenzo@techcrunch.com/)

It’s unclear why the notifications’ content was logged to begin with, but today’s fix suggests it was a bug.

Apple did not immediately respond to a request for comment asking why the notifications were being retained. The company also [backported the fix](https://support.apple.com/en-us/127003) to iPhone and iPad owners running the older iOS 18 software.

Privacy activists expressed alarm when they learned that the FBI had found a way around a security feature that is used daily by at-risk users. Signal, like other messaging apps such as WhatsApp, allows users to set up a timer that instructs the app to automatically delete messages after a set amount of time. This feature can be helpful for anyone who wants to keep their conversations secret in the event that authorities seize their devices.