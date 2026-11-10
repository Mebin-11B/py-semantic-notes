---
title: "Scammers are abusing an internal Microsoft account to send spam links"
url: https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/
clipped: 2026-06-17 00:58:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Scammers are abusing an internal Microsoft account to send spam links](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/)

## Digest Summary
Scammers have exploited a loophole that lets them send spam emails from Microsoft’s internal address [email protected], which is normally used for legitimate account alerts such as two‑factor authentication codes. By creating new Microsoft accounts that appear as genuine customers, the attackers can dispatch messages with subject lines mimicking official notifications (e.g., fraud alerts or private messages) and embed links to malicious sites. The Spamhaus Project reported seeing this abuse for several months and warned that automated notification systems should not permit such customization; they have notified Microsoft. Microsoft confirmed an ongoing investigation, stating it is strengthening detection, blocking mechanisms, and removing violating accounts. Similar abuse of corporate email accounts has been observed with other firms (e.g., Betterment, Namecheap), indicating a broader issue beyond Microsoft.

## Discussion Summary
The comments express concern over the difficulty of verifying legitimate domains, noting that large companies such as Microsoft, Booking, PayPal, and even the FBI have had their domains abused for phishing despite extensive domain portfolios. Contributors highlight the lack of publicly available, comprehensive lists of authorized sending domains, which hampers users’ ability to spot fraudulent messages. There is also uncertainty about how email providers treat spam originating from authentic corporate domains, questioning whether penalties affect only the compromised domain or extend to the broader corporate namespace.

---

## Full Article

For months, scammers have been taking advantage of a loophole that allows them to send spammy emails from an internal Microsoft email address typically used for sending legitimate account alerts.

It’s not clear how the scammers are abusing the system, but they have been able to set up new Microsoft accounts as if they are new customers and use that access to send out emails purportedly from the tech giant, potentially tricking people into thinking these emails are genuine.

Microsoft doesn’t yet appear to have gotten a handle on the issue.

Last week, I received several, similarly structured emails containing subject lines and web links to scammy sites from Microsoft across different email accounts. These [crudely made](https://mastodon.social/@zackwhittaker/116562360000833298) emails were sent from `msonlineservicesteam@microsoftonline.com`, an email account that Microsoft uses to send important notifications to users, such as two-factor authentication codes and other critical alerts about their online account.

Some of these emails’ subject lines resembled official emails that would alert users to fraudulent transactions, while other emails claimed to have a private message waiting for the recipient at a web address mentioned in the email body.

![a copy of the spammy email, which comes from "msonlineservicesteam@microsoftonline.com" but contains clearly spammy content.](https://techcrunch.com/wp-content/uploads/2026/05/spam-7f0198d1a59491c8.jpg)

**Image Credits:**TechCrunch (screenshot)

In [a social post on Tuesday](https://infosec.exchange/@spamhaus/116601270466207765), anti-spam nonprofit The Spamhaus Project said it had also seen Microsoft’s account notification email address being abused to send spam and that the activity dated back “several months.”

“Automated notification systems should not allow this level of customization,” wrote Spamhaus. The nonprofit added that it has notified Microsoft of the issue.

When contacted by TechCrunch earlier this week, Microsoft acknowledged our inquiry but did not comment by press time.

In a statement provided after publication by Emelia Katon, representing Microsoft via a third-party public relations agency, the company said: “We are actively investigating and taking action against these phishing reports to help keep customers protected. This includes further strengthening our detection and blocking mechanisms, while removing accounts that violate our Terms of Use.”

This is the latest in a rash of incidents in which hackers or scammers have abused company systems to trick unsuspecting customers in recent months. Earlier this year, hackers broke into a platform used by fintech firm Betterment to [send out fraudulent notifications](https://techcrunch.com/2026/01/12/fintech-firm-betterment-confirms-data-breach-after-hackers-send-fake-crypto-scam-notification-to-users/) that purported to triple the value of any crypto users send in — a widely known scam used to steal people’s cryptocurrency.

Back in 2023, hackers [similarly abused access](https://www.bleepingcomputer.com/news/security/namecheaps-email-hacked-to-send-metamask-dhl-phishing-emails/) to an email account run by Namecheap to send out phishing emails aimed at stealing people’s credentials.

Other users commenting on social media say that other companies’ email addresses are also being used to send out spam, suggesting the issue is not limited to Microsoft.

*Updated with a response from Microsoft.*