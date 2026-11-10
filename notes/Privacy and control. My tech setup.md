---
title: "Privacy and control. My tech setup"
url: https://toidiu.com/blog/2025-12-25-privacy-and-control/
clipped: 2026-06-17 02:05:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Privacy and control. My tech setup](https://toidiu.com/blog/2025-12-25-privacy-and-control/)

## Digest Summary
The author argues that “privacy” is often misunderstood and should be reframed as “control” over digital identity, emphasizing that most users’ threat models focus on who can influence their information consumption, advertising exposure, and political persuasion. Based on a personal threat model, the author recommends a set of tools and practices:

- **Password management:** Use a self‑hosted solution such as GNU pass to avoid third‑party storage; Bitwarden is suggested for a richer UI.  
- **Messaging:** Prefer Signal over platforms like WhatsApp; Venmo is disabled.  
- **Mobile OS:** Run GrapheneOS on Android to sandbox apps, restrict permissions, and optionally disable the Play Store and location services, which also improves battery life.  
- **Email:** Operate a personal domain (e.g., [user]@example.com) and use Tuta for secure, affordable email without self‑hosting.  
- **Web browsing:** Firefox with Privacy Badger and uOrigin to block tracking; social media accessed only via containerized browsers.  
- **Calendars/contacts:** Self‑host CalDAV on a Raspberry Pi (sabre.io/baikal) and sync via DAVx⁵.  
- **Domain registration & DNS:** Use Cloudflare Registrar for lower renewal costs and Cloudflare’s 1.1.1.1 DNS, citing perceived alignment of incentives.

The post cites recent articles on Facebook’s covert Snapchat monitoring and Meta/Yandex de‑anonymizing Android browsing as context for the security concerns.

## Discussion Summary
The comments express cautious support for privacy‑focused mobile OSes such as GrapheneOS, noting practical obstacles like incompatibility with apps that rely on Google Integrity APIs and the risk of losing access to essential services, especially in jurisdictions with digital‑only government requirements. Participants acknowledge the need to evaluate workflow breakage before switching and appreciate users who adopt such systems. Skepticism is voiced toward large infrastructure providers, particularly Cloudflare, with concerns about control and potential abuse. Alternative tools such as NetGuard and uBlock Origin are mentioned as viable compromises.

---

## Full Article

"I don't need to care about privacy because I have nothing to hide." is an
argument that I have heard countless times. I found this argument difficult to
counter in the past, yet deep-down I knew the reasoning was flawed.

The problem is that the word "privacy" is diluted and mean different things to
different people. Instead of "privacy" we really should be talking about
"control". Framed in this context, we can more concretely talk about why it's
important to protect your digital identity.

For me privacy is not the primary driver, because like you mentioned, it doesn't
make sense for the common folk and doesn't actually fall into people's threat
model (journalists on the other hand should care). I am personally motivated by
the notion of "control". Can someone else meditate how I experience the world
and what information I consume? Whether that is censoring, influencing how much
time I have to spend watching ads or which ads I am allowed to watch. Can they
influence how I vote? Watch the talk [In Defense of
Privacy](https://www.youtube.com/watch?v=1oCDLbCyalM) for a more on this.

Many of the convenient tools we use today (email, messaging, social media,
password manager) are essential for daily life but they also yield control over
to organizations (Google, Facebook, Amazon) that don't necessarily have our best
interest in mind [1][2].

**Discussion**

My setup
--------

> Questioning how "incentives align" is a really good litmus test for most
> things.

Most of the following recommendations are based on my own threat model and
comfort level. There will always be a compromise between effort and easy. It's
best to pick what fits your lifestyle.

### Password manager

Use a password manager! I use [GNU pass](https://www.passwordstore.org/) because
I don't want to hand over my passwords to a 3rd party. I typically only use the
password manager from my laptop and don't access passwords from my phone (I
consider this a better security practice). I have been meaning to try out
[passage](https://github.com/FiloSottile/passage). I would also recommend
[Bitwarden](https://bitwarden.com/) for those who want a better UI experience.

### Messaging

Signal for messaging is preferable [3]. (Whatsapp is an
unfortunate exception and I hate that I need it to stay connected to friends and
family).

### Phone

I run [GrapheneOS](https://grapheneos.org/features) on my Android. This allows
me to sandbox, disable or uninstall apps rather than allowing super-privileged
Google/ISP apps from doing whatever they want on my personal device. By default,
[Google Play apps are
unpriviledged](https://grapheneos.org/features#sandboxed-google-play) and have
to work within the sandbox model. GrapheneOS also allows you to restrict
permissions at a granular level, including network access. You can also disable
apps that you only use occasionally (Venmo, ride-sharing, Google play store).

I try to use opensource alternatives for apps on F-Droid. Did you know disabling
Google play store (also location services) increases your battery life by a lot!
Not running bloated stock OS also means your 5 year old phone is still fast and
usable (wtf do I need to but a new phone every 2 years?). I barely use social
media and don't install it on my phone (I use social media in Browser containers
to limit 3rd party cookies).

### Email

I have a personal domain, which I use for email i.e. [[email protected]](https://toidiu.com/cdn-cgi/l/email-protection). This
allows me to switch providers whenever I want (e.g. lack of trust in Google,
ProtonMail can raise their prices). These days I am using
[Tuta](https://tuta.com/) as my email provider because they are fast, offer a
better price and have a strong focus on secure email. Also I can't be bothered
to host my own email server.

### Browsing

I use firefox with privacy badger and uOrigin because I do not opt into
companies personally targeting me (can be contentious since some sites use this
to make money).

I host my calendar and contacts on a raspberrypi, which you can only access on
localhost. The Caldav server is [Baïkal](https://sabre.io/baikal), gets the job
done. I use [DAVx⁵](https://www.davx5.com/) to sync the contacts on my phone.

### Domain Registrar

Disclaimer: Cloudflare is my current employer. I switched to Cloudflare
Registrar recently (prior to being employed by Cloudflare) because they offered
a lower price when my previous Registrar raised the price at renewal. I don't
think Cloudflare really cares to make money on domain registration and so it
passed my "incentives align" test.

### DNS resolution

**Edit**: some folks have called out my conflict of interest with Cloudflare and
the sensitivity of DNS. I think thats fair. Here is a [Reddit thread of other
DNS
providers](https://www.reddit.com/r/dns/comments/1c8huvl/need_private_dns_list/)
so readers can make their own choice.

Disclaimer: Cloudflare is my current employer. I use Cloudflare's DNS because I
trust them more than other companies; purely based on their business and how
their incentives align (https://one.one.one.one/). There are other
secure/anonymous ones out there.

### Banking

Venmo is disabled. I do have a Banking app that I only use to deposit checks.
Here is a list of [Banking
apps](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/)
that work with GrapheneOS ([credit](https://news.ycombinator.com/item?id=46447862)).

Resources
---------

* [1] https://arstechnica.com/tech-policy/2024/03/facebook-secretly-spied-on-snapchat-usage-to-confuse-advertisers-court-docs-say/
* [2] https://arstechnica.com/security/2025/06/meta-and-yandex-are-de-anonymizing-android-users-web-browsing-identifiers/
* [3] https://www.youtube.com/live/AyH7zoP-JOg?t=222s