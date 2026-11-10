---
title: "Vercel April 2026 security incident"
url: https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/
clipped: 2026-06-17 01:14:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Vercel April 2026 security incident](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)

## Digest Summary
Vercel, the cloud platform behind Next.js, disclosed a security incident affecting a limited subset of customers. Unauthorized access originated from a compromised Google Workspace account belonging to a Vercel employee, which was obtained via a breach at the AI service Context.ai. The attacker leveraged the OAuth credentials of the third‑party Google Workspace app (client ID 110671459871‑30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com) to infiltrate Vercel environments and retrieve environment variables that were not marked as “sensitive,” thus not encrypted at rest. Vercel confirmed that all customer environment variables are encrypted by default and that core services, including Next.js, Turbopack, and other open‑source projects, remain unaffected. The company has engaged incident‑response experts, notified law enforcement, and urged customers to review and re‑classify environment variables, rotate secrets, and enable the sensitive‑variable feature. A threat actor claiming affiliation with the “ShinyHunters” extortion group posted alleged stolen data—access keys, source code, employee records, and internal dashboard screenshots—and mentioned a $2 million ransom demand, though Vercel has not confirmed negotiations.

## Discussion Summary
The comments express strong concern and criticism over Vercel’s recent OAuth‑token breach, highlighting the extensive potential impact on development tools, CI pipelines, and secrets. Readers repeatedly note the company’s vague disclosures, limited actionable guidance, and the broader risk of concentrated trust in a few managed platforms. Many suggest immediate credential rotation, tighter isolation of environment variables, or moving to self‑hosted alternatives, while others link the incident to rising AI‑driven attack surfaces and call for more robust architectural safeguards. Overall sentiment is distrustful and calls for greater transparency and security controls.

---

## Full Article

![Vercel](https://www.bleepstatic.com/content/hl-images/2026/04/19/vercel-header-lg.jpg)

*Update 4/19/26: Added additional information from Vercel that was disclosed after publishing.*

Cloud development platform Vercel has disclosed a security incident after threat actors claimed to have breached its systems and are attempting to sell stolen data.

Vercel is a cloud platform that provides hosting and deployment infrastructure for developers, with a strong focus on JavaScript frameworks.

The company is known for developing Next.js, a widely used React framework, and for offering services such as serverless functions, edge computing, and CI/CD pipelines that enable developers to build, preview, and deploy applications.

In a security bulletin published today, the company said a limited subset of customers was affected by a security breach.

"We've identified a security incident that involved unauthorized access to certain internal Vercel systems," [warns Vercel](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident).

"We are actively investigating, and we have engaged incident response experts to help investigate and remediate. We have notified law enforcement and will update this page as the investigation progresses."

The company says its services have not been impacted and that it is working with impacted customers.

Vercel says it is taking steps to protect its customers, advising them to [review environment variables](http://vercel.com/all-env-vars), use its [sensitive environment variable feature](https://vercel.com/docs/environment-variables/sensitive-environment-variables), and to rotate secrets if needed.

After publishing this story, Vercel updated its advisory to state that the breach stemmed from the compromise of a third-party AI tool's Google Workspace OAuth application.

Vercel is advising Google Workspace administrators and Google account owners to check for the following application:

```
OAuth App: 110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com
```

Vercel CEO Guillermo Rauch later shared additional details [on X](https://x.com/rauchg/status/2045995362499076169), stating that the initial access occurred after a Vercel employee's Google Workspace account was compromised via a breach at the AI platform Context.ai.

According to Rauch, the attacker then escalated access from the compromised account into Vercel environments, where they were able to access environment variables that were not marked as sensitive and therefore not encrypted at rest.

While intended to contain non-sensitive information, the attacker gained further access after enumerating these variables.

"Vercel stores all customer environment variables fully encrypted at rest. We have numerous defense-in-depth mechanisms to protect core systems and customer data," Rauch said.

"We do have a capability, however, to designate environment variables as 'non-sensitive.' Unfortunately, the attacker got further access through their enumeration."

The company's investigation has confirmed that Next.js, Turbopack, and its other open-source projects remain safe.

Vercel has also rolled out updates to its dashboard, including an overview page of environment variables and an improved interface for managing sensitive environment variables.

Customers are strongly advised to review environment variables for sensitive information and enable the sensitive variable feature to ensure they are encrypted at rest.

If you have any information regarding this incident or other undisclosed attacks, you can contact us confidentially via Signal at 646-961-3731 or at tips@bleepingcomputer.com.

Hacker claims to be selling stolen Vercel data
----------------------------------------------

The disclosure comes after a threat actor claiming to be "ShinyHunters" posted on a hacking forum that they had breached Vercel and were selling access to company data.

It should be noted that while the hacker claims to be part of the ShinyHunters group, threat actors linked to recent attacks attributed to the ShinyHunters extortion gang have denied to BleepingComputer that they are involved in this incident.

In the forum post, the hacker claimed to be selling access keys, source code, and database data allegedly stolen from Vercel, along with access to internal deployments and API keys.

"This is just from Linear as proof, but the access I'm about to give you includes multiple employee accounts with access to several internal deployments, API keys (including some NPM tokens and some GitHub tokens)," reads the forum post.

![A screenshot of a forum post shared by the threat actor on Telegram](https://www.bleepstatic.com/images/news/security/attacks/v/vercel/hacking-forum-post.jpg)

**A screenshot of a forum post shared by the threat actor on Telegram**

The attacker also shared a text file containing Vercel employee information, which consists of 580 data records containing names, Vercel email addresses, account status, and activity timestamps. They also shared a screenshot of what appears to be an internal Vercel Enterprise dashboard.

BleepingComputer has not been able to independently confirm if the data or screenshot is authentic.

In messages shared on Telegram, the threat actor also claimed they were in contact with Vercel regarding the incident and that they discussed an alleged ransom demand of $2 million.

BleepingComputer contacted Vercel with additional questions about the breach, including whether any sensitive data or credentials were exposed and if they are negotiating with the attackers, and will update this story if we receive a response.

*Update 4/19/26 6:14 PM ET: Updated article to add further information disclosed by Vercel.  
Update 4/19/26 7:21 PM ET: Updated article with additional information from Vercel's CEO.*

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

[Get the whitepaper](https://hubs.li/Q04jQ9z40)