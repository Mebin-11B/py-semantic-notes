---
title: "I Could've Rickrolled the FIFA World Cup. All I Needed Was My ID"
url: https://bobdahacker.com/blog/fifa-hack
clipped: 2026-06-17 00:42:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-20
summary_status: done
concepts:
  - api security
  - client-side authorization
  - microsoft entra
related:
  - "[[API Security]]"
  - "[[Client-Side Authorization]]"
  - "[[Microsoft Entra]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article describes a critical vulnerability in FIFA's internal IT systems where client-side role validation allowed any registered user to bypass access controls and access live stream keys and management panels for the 2026 World Cup.
>
> **Key points:**
> - Registering on FIFA's public agent platform automatically added users to their internal Microsoft Entra tenant.
> - Internal applications (like `fdp.fifa.org` and `cis.fifa.org`) used client-side role validation but failed to enforce authorization on the backend API.
> - This lack of backend authorization exposed live production RTMP ingest URLs, preview manifests, stream keys, commentary notes, match stats, and direct Blob storage URLs.
> - The author details a chaotic reporting process involving emails, WhatsApp, convention centers, MediaKind, CISA, and the FBI to get the vulnerabilities patched, which FIFA did without official acknowledgment.
>
> **Concept links:** [[API Security]], [[Client-Side Authorization]], [[Microsoft Entra]], [[Vulnerability Disclosure]], [[Identity and Access Management]]
>
> **Suggested connections:**
> - [[API Security]] — the critical risk of relying on client-side security checks without backend enforcement (Broken Object Level Authorization / Broken Function Level Authorization).
> - [[Identity and Access Management]] — risks associated with tenant boundaries and default access configuration for external guest/registered users in Microsoft Entra ID.
<!-- ai-summary:end -->

# [I Could've Rickrolled the FIFA World Cup. All I Needed Was My ID](https://bobdahacker.com/blog/fifa-hack)

## Digest Summary
The author registered on FIFA’s public Agent Platform, which automatically added the account to FIFA’s Microsoft Entra (Azure AD) tenant used by all internal applications. Although the Angular front‑end displayed “no roles” and denied access, the backend APIs performed no role checks, allowing an unauthenticated “NO_ROLES” account to retrieve data from multiple production systems. The author accessed the Streaming Management panel (fdp.fifa.org), exposing live‑production RTMP ingest URLs and stream keys for every 2026 World Cup match and camera angle. These URLs could be used to replace live feeds, potentially hijacking broadcast content. The same account also accessed the Commentator Information System (cis.fifa.org), match‑management interfaces, analytics dashboards, and an Azure Function exposing internal spreadsheet files via direct Blob URLs. The vulnerability stemmed from client‑side only authorization. After reporting via email, phone, and contacts at MediaKind, CISA, and the FBI, FIFA patched the APIs to return 403 responses, but offered no direct acknowledgment or disclosure policy.

## Discussion Summary
The comments blend amusement with admiration for the reported FIFA vulnerability, noting the author’s similar experience with a past Qatar‑2022 exploit and the quick patch but lack of promised compensation. Readers express praise for the writing and the discovery while also highlighting serious security concerns, questioning how the API allowed unchecked JWTs and emphasizing the potential for large‑scale disruption if misused. Overall sentiment acknowledges the technical cleverness, finds the situation entertaining, and critiques FIFA’s response and oversight.

---

## Full Article

*They fixed it without ever responding to me. I had to call FIFA, MediaKind, HBS, CISA, and the FBI at 3am Tokyo time just to get someone to listen. This is that story.*

It Started With a Football Agent Registration
---------------------------------------------

So FIFA has this thing called the [FIFA Agent Platform](https://agents.fifa.org). It's a public portal where you can register to become a licensed football agent. You submit your ID, verify your email, and you're in. Simple enough.

What I didn't expect was what happened next.

When you register on agents.fifa.org, FIFA adds your account to their Microsoft Entra tenant (formerly Azure AD). That's the same tenant that powers **all** of FIFA's internal platforms. And I mean all of them.

My first two attempts actually failed because the lighting on my ID photos wasn't good enough:

![FIFA registration failed](/static/images/blogs/fifa/registration_failed.png)  
*"Registration failed during the last step of checking your identification." - apparently FIFA has higher standards for my selfie than my actual security*

But the third attempt went through. And I received this beautiful email:

![FIFA FAP confirmation email](/static/images/blogs/fifa/fap_confirmation.png)  
*Subject line: "FIFA - FAP - CONFIRMATION". Yes, FIFA's Agent Platform is officially called FAP. I cannot make this up. FAP CONFIRMATION. Moving on.*

The "Access Denied" That Wasn't
-------------------------------

After registration, I tried navigating to `fdp.fifa.org` - FIFA's Football Data Platform. The app authenticated me through the shared Entra tenant, checked my roles, found I had none, and showed me:

*"Sorry, you do not have any FIFA Football Data Platform role assigned to your account."*

Looks like it works, right? Access denied. Go away. Nothing to see here.

Except this was all **client-side**. The Angular app checked the JWT for a `NO_ROLES` marker and rendered the access-denied page. The backend APIs? They didn't check anything. They just served whatever you asked for.

Welcome to the Streaming Management Panel
-----------------------------------------

After bypassing the client-side guards, I landed on the Streaming Management panel. And my jaw hit the floor.

![Streaming Management panel showing all World Cup matches](/static/images/blogs/fifa/streaming_panel_overview.png)  
*Every single FIFA World Cup 2026 match. With streaming controls.*

This wasn't some dev environment. This wasn't test data. This was the **live production Streaming Management panel** for the FIFA World Cup 2026. Every match. Every camera angle. Every RTMP ingest URL. Every stream key.

Let me expand one of those matches so you can see what I mean:

![Expanded match showing all five camera RTMP URLs](/static/images/blogs/fifa/streaming_panel_expanded.png)  
*Five camera angles per match: PGM, Tactical, Camera1, High Behind Left, High Behind Right*

Each match had five camera feeds, each with:

* An **RTMP ingest URL** (where the camera sends video TO)
* A **preview manifest** (where you can WATCH the feed)
* An **output URL** (the HLS manifest that goes to broadcast partners)

The RTMP ingest URLs looked like this:

```
rtmp://in-6c81fc99-513f-4c76-82c2-877e0b93f2ea.westeurope.streaming.mediakind.com:1935/96886a14-9987-420f-814c-2f7cec5408ae
```

That UUID at the end? `96886a14-9987-420f-814c-2f7cec5408ae`. That's the **stream key** (not a real one). It's shared across all five camera angles for the same match. One key to rule them all.

The streaming infrastructure is hosted on [MediaKind](https://mediakind.com), FIFA's streaming technology partner. These are production endpoints. The same ones receiving live camera feeds from stadiums across the US, Mexico, and Canada.

I Opened VLC. It Was Live.
--------------------------

I had to confirm the preview manifests actually worked. So I copied one into VLC.

![VLC playing a live World Cup tactical camera feed](/static/images/blogs/fifa/vlc_live_feed.png)  
*That's a live tactical camera feed from an active FIFA World Cup 2026 match. Playing in VLC. On my PC. In Tokyo.*

I closed it immediately. But the damage was done (to my brain). Those preview URLs serve live video. During active matches. To anyone with the URL.

I Could Have Stopped the Streams
--------------------------------

It wasn't just read access. The Streaming Management panel had full controls. Start, stop, schedule. For every match. Every camera angle.

![Stream control confirmation dialog](/static/images/blogs/fifa/stream_control.png)  
*One click. That's all it would take to kill a live World Cup camera feed.*

I did not touch any of these controls. But they were there. Functional. Waiting for anyone with a NO\_ROLES account to press them.

The Nuclear Option
------------------

Let me spell out what this means.

Those RTMP ingest URLs are the literal pipe from the stadium cameras to FIFA's broadcast distribution chain. Camera -> RTMP ingest -> MediaKind -> broadcast partners -> your TV.

If an attacker pushed video to one of those RTMP endpoints with the stream key (which is RIGHT THERE in the URL), they would **replace the camera feed**. The PGM (Program) feed is the main broadcast output. Replace that, and every TV network receiving the FIFA feed shows whatever you pushed.

The stream key is shared across all five camera angles per match. A single attacker could hijack every camera simultaneously.

An attacker could have rickrolled the entire FIFA World Cup. Or played Subway Surfers gameplay. Live. On every TV network worldwide. During an active match.

I did not test this. I did not push anything to any RTMP endpoint. But the infrastructure was wide open.

But Wait, There's More
----------------------

The Streaming Management panel wasn't the only thing exposed. My NO\_ROLES account had access to the entire platform.

![FDP navigation showing full access](/static/images/blogs/fifa/fdp_full_nav.png)  
*Competitions, Matches, Teams, Tools, Exchange Platform, Analysis Dashboard, Commentator Information System, FIFA AI Pro, Admin. All accessible.*

The platform also had a full live match dashboard with an embedded video player, real-time event timeline, and match officials data:

![FDP match overview with live video](/static/images/blogs/fifa/fdp_match_overview.png)  
*Côte d'Ivoire vs Ecuador, live. Embedded video feed, yellow card timeline, match officials. The "LIVE" badge isn't decorative.*

### Advanced Analytics (Live Match)

![Advanced Analytics showing live possession and attempt data](/static/images/blogs/fifa/advanced_analytics.png)  
*Live possession control, attempt creation breakdowns, ball recovery timing, distance covered, and FIFA AI Pro integration*

### Match Management (Write Access)

Here's where it gets worse. The Management tab on fdp.fifa.org has write operations. And the backend accepts them from a NO\_ROLES account.

![Update Live Stats modal with Edit and Publish button](/static/images/blogs/fifa/update_live_stats.png)  
*"Update Live Stats" with a rich text editor, match time, match score fields, and an "Edit and Publish" button*

![Match management buttons](/static/images/blogs/fifa/management_buttons.png)  
*Attendance, Possession, Post Match Statistics, Team Registration Statistics, Analysis Finished, Score and Statistics, Adjust Kick-off Moment, Performance Data, Send Tactical Lineup, Event Ingress Details*

An attacker could:

* Modify editorial commentary notes and publish them to broadcast systems
* Adjust the official kick-off moment
* Send tactical lineup data
* Change scores and match statistics

This data feeds into the Commentator Information System and gets displayed on live television.

The Commentator Information System
----------------------------------

`cis.fifa.org` was also accessible with the NO\_ROLES account. This is the real-time dashboard that broadcast commentators use during live matches.

![CIS main dashboard](/static/images/blogs/fifa/cis_dashboard.png)  
*The FIFA World Cup 2026 dashboard. Live scores, upcoming matches, results.*

![CIS live match view](/static/images/blogs/fifa/cis_live_match.png)  
*Côte d'Ivoire vs Ecuador, 75th minute. Full tactical view with player positions, formations, live stats, substitution timeline, and squad data.*

When a commentator says "fun fact, Enner Valencia at 36 years and 222 days is the oldest outfield player to make a FIFA World Cup appearance for Ecuador" - this is where that comes from. My account could see every editorial note, every pre-match stats kit, every talking point prepared for every match.

The Exposed Dev Environment
---------------------------

As a bonus, I also found an Azure Function App at `xxxxxxxxx-spreadsheets-api.azurewebsites.net` that returned metadata and direct Azure Blob Storage download URLs for 23 internal FIFA files.

```
{
    "Size": 10,
    "Skip": 0,
    "Total": 23,
    "Items": [
        {
            "Name": "00_TransferCount_in_ENGLISH.xlsx",
            "BlobPath": "https://xxxxxxxxx.blob.core.windows.net/spreadsheet-storage/00_TransferCount_in_ENGLISH.xlsx"
        },
        {
            "Name": "0_pending_transfers_example.xlsx",
            "BlobPath": "https://xxxxxxxxx.blob.core.windows.net/..."
        },
        {
            "Name": "Debbie.xlsx",
            "BlobPath": "https://xxxxxxxxx.blob.core.windows.net/..."
        }
    ]
}
```

Transfer reports, revenue comparisons, board-level representation data, referee and coach statistics. And whatever Debbie.xlsx is. All accessible with zero role checks.

The Absolute Nightmare of Reporting This
----------------------------------------

OK so I found all of this while the World Cup was underway. Matches are happening. The RTMP URLs are active. Stream keys are exposed. And FIFA has no bug bounty program, no security.txt, and no published security contact.

What followed was the most stressful night of my life.

### Attempt 1: Email

I fired off the full disclosure to every FIFA email I could find or guess:

`[email protected]`, `[email protected]`, `[email protected]`, `[email protected]`, and some employee emails.

Five of them bounced. The rest went into the void. No response.

### Attempt 2: WhatsApp

I found Sebastian Runge (Head of Football Technology & Data at FIFA, 14 years at the org) on LinkedIn. His phone number was listed. I WhatsApped him. No response.

### Attempt 3: FIFA HQ Phone

Called `+41 43 222 7777`. Closed. It was Sunday evening in Zurich.

### Attempt 4: The FIFA Media Line

Called `+41 43 222 7272`. Also closed.

### Attempt 5: The Dallas Convention Center

The IBC (International Broadcast Centre) is at the Kay Bailey Hutchison Convention Center in Dallas. I called `+1 (214) 939-2700`. Got voicemail. Left a message.

### Attempt 6: MediaKind

This was the breakthrough. I called MediaKind's toll-free line `+1 833 211 8472`. Someone picked up. They understood the issue immediately. They asked me to email the details with the stream keys as proof. I did.

### Attempt 7: HBS (Host Broadcast Services)

Called `+41 41 726 0090`. They said they didn't have anyone who could help and hung up. Called back. No answer.

### Attempt 8: Infront Sports & Media

Called `+41 41 723 15 15` (HBS's parent company). No answer.

### Attempt 9: CISA

Here's where things got interesting. I discovered that CISA (Cybersecurity and Infrastructure Security Agency) is the **federal lead on cybersecurity for the FIFA World Cup 2026**, including broadcast systems. I called their 24/7 operations center at `+1 888 282 0870`.

They picked up. They listened. They asked me to email the details. I did.

### Attempt 10: The FBI

I have existing contacts at the FBI from previous cybersecurity work. I messaged them on Signal. They responded, said they had contacts and needed to package it the right way.

### The Timeline

| When | What |
| --- | --- |
| Night | Found the Streaming Management panel. Jaw hits floor. |
| Night | Opened preview manifest in VLC. Confirmed live. Closed immediately. |
| Night | Sent disclosure email to 10+ FIFA addresses. 5 bounced. |
| Night | WhatsApped Sebastian Runge. |
| Night | Called FIFA Zurich. Closed. Called FIFA Media line. Closed. |
| Night | Called Dallas Convention Center. Voicemail. |
| Night | Called MediaKind. **Someone answered.** Sent full report with stream keys. |
| Night | Called HBS. They hung up. Called back. No answer. |
| Night | Called CISA 24/7 line. They listened. Sent report. |
| Night | Messaged FBI contacts on Signal. They responded. |
| Next day | Vulnerability fixed. No response from FIFA. |

The Root Cause
--------------

The whole thing boils down to one architectural mistake: **client-side authorization with no server-side enforcement**.

FIFA's internal applications use Microsoft Entra for authentication and role-based access control. The Angular/React/Vue frontends check the JWT token for role claims and render access-denied pages accordingly. But the backend APIs trust any authenticated tenant member and serve data regardless of roles.

The attack chain:

1. Register on agents.fifa.org (public)
2. Get added to FIFA's Entra tenant
3. Authenticate against any FIFA internal app
4. Client says "access denied"
5. Server says "here's everything"

This pattern affected at least:

* **fdp.fifa.org** (Football Data Platform)
* **cis.fifa.org** (Commentator Information System)
* **xxxxxxxxx-spreadsheets-api.azurewebsites.net** (dev environment)

And potentially others using the same tenant.

The Fix
-------

Sometime between my reports and the next morning, the vulnerability was patched. My NO\_ROLES account returns 403 responses from the server, not just the client.

FIFA never responded. Not to acknowledge the report. Not to say thank you. Not to discuss compensation. Nothing.

But they did leave me on the FDP email distribution list. I'm still receiving official FIFA World Cup 2026 match documents: Start Lists, Tactical Lineups, Full Time Match Reports. All sent from `[email protected]`. In four languages.

To FIFA
-------

You fixed it fast. Credit where it's due. But:

* Get a security.txt file. Seriously. It's 2026.
* Publish a VDP (Vulnerability Disclosure Policy). You're running the biggest sporting event on earth.
* Client-side authorization is not authorization. Every intern learns this.
* When a researcher has to call CISA and the FBI to reach you, something is wrong.
* Hire me (just kidding... unless?)

So long and thanks for all the Fish :3

---

*Still think about those RTMP stream keys sometimes. Somewhere in a parallel universe, billions of people are watching Subway Surfers gameplay during the World Cup final. All it took was an ID.*