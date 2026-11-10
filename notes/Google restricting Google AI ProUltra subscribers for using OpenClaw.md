---
title: "Google restricting Google AI Pro/Ultra subscribers for using OpenClaw"
url: https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778
clipped: 2026-06-17 01:41:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - api policies
  - google antigravity
  - account suspension
  - terms of service
  - third-party clients
  - customer support failures
related:
  - "[[Google Antigravity]]"
  - "[[Terms of Service]]"
  - "[[Third-Party Clients]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Reports of Google implementing sudden, non-appealable 403 suspensions on Google AI Pro/Ultra subscribers for utilizing third-party OAuth integrations like OpenClaw.
>
> **Key points:**
> - Paid subscribers ($249/mo) of Google's Antigravity service reported sudden bans with 403 "service disabled" errors.
> - Google engineering confirmed a zero-tolerance policy against using Antigravity credentials in third-party clients (e.g., OpenClaw, pi harness) due to unauthorized use of the Private Cloud Code API.
> - Affected users detail a broken support hierarchy where Google One, Cloud, and Android support teams redirect customers to each other while billing continues.
> - Developers are responding by cancelling all Google subscriptions and migrating workflows to competitors like Anthropic's Claude Code.
>
> **Concept links:** [[API Policies]], [[Google Antigravity]], [[Account Suspension]], [[Terms of Service]], [[Third-Party Clients]], [[Customer Support Failures]]
>
> **Suggested connections:**
> - [[Google Antigravity]] — The AI development and CLI tool environment impacted by this ban wave.
> - [[Terms of Service]] — The legal terms governing API usage limits and third-party developer integrations.
<!-- ai-summary:end -->


# [Google restricting Google AI Pro/Ultra subscribers for using OpenClaw](https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778)

## Digest Summary
- A user’s Google AI Ultra (Antigravity) account was suspended for three days without prior warning after connecting Gemini models via the OpenClaw OAuth integration.  
- The user, paying $249 / month, was unable to log in, received a 403 “service disabled” error, and reported the issue to multiple support channels (Google One, Google Cloud, Antigravity feedback).  
- Internal investigation confirmed the suspension resulted from using credentials in the third‑party tool “OpenClaw,” which violates Google’s Terms of Service by employing Antigravity servers for a non‑Antigravity product. Google’s policy applies a zero‑tolerance stance, and the suspension is not reversible.  
- Affected users report similar bans, lack of response from support, and continued billing despite inaccessible services. Some describe the support process as a “catch‑22,” involving redirects between Google One, Cloud, and Android developer teams.  
- Workarounds discussed include creating new accounts, migrating data, and considering alternative AI platforms (Claude, Codex). No official resolution or timeline has been provided.

## Discussion Summary
Comments converge on frustration with Google’s immediate, non‑appealable bans on paid accounts that used third‑party tools to access subsidized tokens, describing the enforcement as draconian and support as ineffective. While many acknowledge the economic need to separate consumer‑grade subscriptions from programmatic API usage, they criticize the lack of warnings, transparent policies, and graduated responses. Comparisons to Anthropic’s more communicative approach are common, and users suggest using proper API tiers, alternative providers, or open‑source solutions to avoid similar issues. Overall sentiment is disappointment mixed with a call for clearer guidance and fairer handling.

---

## Full Article

I’m seeking assistance regarding a sudden restriction on my Google AI Ultra account that has persisted for three days. I received no prior warnings or notifications regarding a potential violation.

The only recent change in my workflow was connecting Gemini models via OpenClaw OAuth. If third-party integrations are the issue, I would expect the platform to block the integration rather than restrict a paid account ($249/mo) without communication.

I have already emailed support but haven’t received a response. Additionally, I found that accessing GCC support requires an additional fee, which seems unreasonable given the existing subscription cost. I WOULD LOVE TO GET THIS RESOLVED!!

Hello [@Aminreza\_Khoshbahar](https://discuss.ai.google.dev/u/aminreza_khoshbahar),

Thank you for bringing this to our attention. We have shared the issue to our internal teams for a thorough investigation.

To ensure our engineering team can investigate and resolve these issues effectively, we highly recommend filing bug reports directly through the Antigravity in-app feedback tool. You can do this by navigating to the top-right corner of the interface, clicking the Feedback icon, and selecting Report Issue.

Sir, I am logged out of my account and I can’t even get into the app!! This is so frustrating..

**[UPDATE]** Day 4, and still total silence from support. I’ve received zero acknowledgement through official channels or the feedback center. I am now in the process of moving all my data and subscriptions off Google. It’s staggering that an organization of this scale can be this unresponsive to a widespread issue.

Truly a **SHAMEFUL** standard of customer care.

[Mike\_L](https://discuss.ai.google.dev/u/Mike_L)



February 13, 2026, 10:01pm

5

I contacted the Google Cloud Support via “GCP Account Suspension Inquiry”. They told me to contact Google One Support, because the error is tied to the personal subscription, not to a “Google Cloud project billing account”. Google One support told me to contact Google Cloud support ![:joy:](https://d1dlmcr85iqnpo.cloudfront.net/images/emoji/twitter/joy.png?v=15 ":joy:")

From emails “gemini-code-assist-user-feedback” or “antigravity-support” still no answer.  
And it happens after some days after I bought the subscription for an year…

any update? please tell us how did u solved it!

Nope, still restricted, tried to escalate by Google One, But they can’t help with the problem either…

[Vision](https://discuss.ai.google.dev/u/Vision)



February 17, 2026, 12:29am

8

Same issue and same sentiment and I cancelled and removed billing for all Google products. Absolutely shameful treatment of paying customers. I emailed each of the contact emails for Antigravity and gemini-code-assist without reply. Unfortunately I prepaid for a year so it looks like I’ll have to sue a trillion-dollar company just to get the measly fee?

I have tried to contact everyone I could. And you all know how disgusting their supports are. I am totally disappointed with their customer service. After 3 weeks waiting, the result is that they cannot restore my account. I guess it is time to move on to Codex or Claude Code. Below is their reply after “full investigation by the internal team“:  
”Thank you for your continued patience as we have thoroughly investigated your account access issue. Please be assured that we conducted a comprehensive investigation, exploring every possible avenue to restore your access.

Our product engineering team has confirmed that your account was suspended from using our Antigravity service. This suspension affects your access to the Gemini CLI and any other service that uses the Cloud Code Private API.

Our investigation specifically confirmed that the use of your credentials within the third-party tool “open claw” for testing purposes constitutes a violation of the Google Terms of Service [1]. This is due to the use of Antigravity servers to power a non-Antigravity product.

I must be transparent and inform you that, in accordance with Google’s policy, this situation falls under a zero tolerance policy, and we are unable to reverse the suspension. I am truly sorry to share this difficult news with you.”

Ok so basicaly, there’s no way we can restore our accounts to use Antigravity anymore yeah? this is unexpected, but until we can figure out how to resolve this issue, I’ll just subscribed using different account

[DOJOTA](https://discuss.ai.google.dev/u/DOJOTA)



February 19, 2026, 5:40pm

11

I’m in the same situation…

[K8L](https://discuss.ai.google.dev/u/K8L)



February 19, 2026, 6:47pm

12

Hi [@Abhijit\_Pramanik](https://discuss.ai.google.dev/u/abhijit_pramanik) , could you please provide some help? This silence is unbearable.

[Dawid\_M](https://discuss.ai.google.dev/u/Dawid_M)



February 19, 2026, 7:10pm

13

I’m in contact with Google One but their actions are no help at all, for almost a week they haven’t done anything, they only asked for screenshots/recordings of the login attempt.

Why is there silence from Google? What is the user supposed to do? Create a new account and buy a new PRO/ULTRA, or what? Any information at all?!

I’ve got ban and the only difference from vanilla IDE experience was antigravity-cockpit extension. No reply to my appeal email last 12 hours.

I’m subscribing the AI Pro and just integrated Gemini to OpenCode yesterday. After a just day use, my account is suspended without any warnings. Simply the API returns 403 error to my OpenCode and Gemini CLI like this:

Failed to login. Message: This service has been disabled in this account for violation of Terms of Service. If you believe this is an error, contact [gemini-code-assist-user-feedback@google.com](mailto:gemini-code-assist-user-feedback@google.com).

I emailed to the contact this morning but didn’t get any response yet.

[ersione](https://discuss.ai.google.dev/u/ersione)



February 20, 2026, 1:02am

16

If this is indeed the case, I find it utterly absurd. It seems Google’s response is woefully inadequate; I should explore Claude or other alternatives.

Quick update for everyone stuck in this 403 loop: I just spent the last 8 days fighting through Tier 1 support. Google One support finally admitted on record it’s a ‘known WAF bug’, but then literally routed me to Android App Developer support because they have no backend access to fix it.

The entire support flowchart is completely broken, and they are still billing us $250/mo for bricked accounts. I just documented the entire Kafkaesque support loop over on the google\_antigravity subreddit. If you are stuck in this same Catch-22, go search for that post over there and share your Trajectory IDs in the comments so we can get some actual engineering eyes on this mass ban wave.

[Wangli](https://discuss.ai.google.dev/u/Wangli)



February 20, 2026, 4:31am

18

Hi [@K8L](https://discuss.ai.google.dev/u/k8l), just wanted to share some context regarding this situation as I see you are waiting for a response.

Yesterday, Abhijit actually posted a brief statement acknowledging these 403 ToS issues, noting that the internal team was ‘prioritizing a resolution.’ However, the message was deleted just a few minutes later.

Hoping for some transparency, I left a single, polite comment asking for clarification on why the update was removed. Surprisingly, my forum account was banned shortly after posting that question.

Currently, there seems to be no official communication regarding these 403 errors, although we can see active replies being made to other unrelated threads on the forum.

This situation is quite concerning for us as developers. The automated system is still triggering these mass bans daily during fixed time windows, without any warning and seemingly without a review of the current process.

Fingers crossed this message doesn’t get taken down and my account survives long enough for you guys to read it, haha.

Facing this issue too, I wrote an email to [gemini-code-assist-user-feedback@google.com](mailto:gemini-code-assist-user-feedback@google.com) “eight days ago”, and still got no response today. So disappointed

My account (pro) was also bricked for calling Gemini model from pi harness two times. No response from support and it’s been four days.