---
title: "Instagram's URL Blackhole"
url: https://medium.com/@shredlife/instagrams-url-blackhole-c1733e081664
clipped: 2026-06-17 01:45:31
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Instagram's URL Blackhole](https://medium.com/@shredlife/instagrams-url-blackhole-c1733e081664)

## Digest Summary
None

## Discussion Summary
The comments express overall appreciation for a concise, refreshing post and anticipation for future installments, while also highlighting several critiques of major platforms. Users note irony in Apple permitting phone‑antivirus apps despite its touted superiority and high developer fees, and they discuss growing difficulties with Instagram’s login walls and link access, including resistance to signing up. Additional remarks reference Facebook’s historical URL filtering and inject humor about iPhone viruses, reflecting a blend of praise, platform skepticism, and light‑hearted commentary.

---

## Full Article

Instagram’s URL Blackhole
=========================

While exploring the file system on a jailbroken iPhone 6s, I stumbled upon an interesting folder:

/var/mobile/Containers/Data/Application/5FEABFA4–7F9E-4DB7–9254-CB4C6C3F9A3A/Library/Application Support/{{InstagramUserId}}/com.instagram.IGDWellBeingDatabase/

Inside of this folder there was an SQLite database that included a “url\_blackhole” table with 4629 entries.

There are were a total of 4629 unique url\_chunks classified under 4 violation types:

* CYBERSECURITY\_PHISHING\_FOA (likely Foreign Origin Actor) — 4370 url\_chunks
* CYBERSECURITY\_GREYWARE\_OR\_SPYWARE — 239 url\_chunks
* CYBERSECURITY\_UNCATEGORIZED — 13 url\_chunks
* PHISHING — 7 url\_chunks

Attempting to visit any of these urls inside of Instagram, such as by clicking on the link in a direct message, presented multiple warnings:

The most common top level domain used for these urls is t.co, the url shortener created by Twitter, and still used by X.

Top Domains by Volume

t.co — 1571  
tinyurl.com — 179  
is.gd — 170  
tr.ee — 108  
linktr.ee — 101  
shorten.is — 71  
shorturl.at — 64  
shorten.ee — 56  
bit.ly — 52  
cutt.ly — 48  
goo.su — 45  
s.mkswft.com.storage.googleapis.com — 41  
pagina.pro — 31  
bom.so — 28  
cdn.videy.co — 26

Most were url redirectors, but for some reason s.mkswft.com.storage.googleapis.com stuck out to me.

Most of the links using that route were no longer working, but at least one was currently active:

[hxxps://s.mkswft.com.storage.googleapis.com/RmlsZTplNmVlMGEzNy0zOGM5LTRjNzAtOWM4Zi1kNjJiN2NkYTBlYTA=/vvvvcccccc.XML](https://s.mkswft.com.storage.googleapis.com/RmlsZTplNmVlMGEzNy0zOGM5LTRjNzAtOWM4Zi1kNjJiN2NkYTBlYTA=/vvvvcccccc.XML)

Trying to visit this link inside Instagram failed as the site’s security certificate was invalid. The webview browser and the external phone browser both threw certificate errors. I did the safe thing of bypassing those errors and landed at a fake virus page with a Google logo (hence the use of storage.googleapis.com).

Clicking repair will then take you to a live app in the Apple App store.

The next step would be downloading that app and reverse engineering it on a completely wiped jailbroken device that is running on a guest wifi network. I’ll have to save that research for another day.