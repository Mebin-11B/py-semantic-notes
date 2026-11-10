---
title: "Disrupting the largest residential proxy network"
url: https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network
clipped: 2026-06-17 01:50:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Disrupting the largest residential proxy network](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network)

## Digest Summary
Google Threat Intelligence Group (GTIG) and partners disrupted the IPIDEA residential proxy network, one of the world’s largest. The operation combined: (1) legal takedown of domains that controlled proxy‑enabled devices; (2) dissemination of technical intelligence on IPIDEA SDKs and proxy software to platform providers, law‑enforcement, and researchers, aiming to block the SDKs that silently enroll user devices; (3) integration of detections into Google Play Protect to warn, remove, and block apps containing IPIDEA SDKs. GTIG estimates the actions removed millions of devices from the network, affecting downstream reseller arrangements. Residential proxies route traffic through consumer ISP IPs, enabling threat actors to hide malicious activity. IPIDEA’s SDKs have been linked to botnets (BadBox2.0, Aisuru, Kimwolf) and to over 550 threat groups in a single week (January 2026), including actors from China, DPRK, Iran, and Russia. The network is associated with numerous branded proxies (e.g., 360 Proxy, Door VPN, Luna Proxy) and offers SDKs for Android, Windows, iOS, and WebOS that monetize apps per download.

## Discussion Summary
The comments express mixed reactions to recent actions against certain proxy services, praising Google Play Protect’s enforcement while questioning why similar providers remain untouched. Contributors argue that paid, legitimate residential proxies can be lawful and useful, contrasting them with malicious malware‑laden apps. Many call for broader access to residential proxies to avoid content restrictions, yet others criticize the perceived selective targeting and raise concerns about hidden malware in device ecosystems. Overall, the discussion balances support for security measures with calls for consistent, fair treatment of proxy technologies.

---

## Full Article

### Introduction

This week Google and partners took action to disrupt what we believe is one of the largest residential proxy networks in the world, the IPIDEA proxy network. IPIDEA’s proxy infrastructure is a little-known component of the digital ecosystem leveraged by a wide array of bad actors.

This disruption, led by Google Threat Intelligence Group (GTIG) in partnership with other teams, included three main actions:

1. Took legal action to take down domains used to control devices and proxy traffic through them.
2. Shared technical intelligence on discovered IPIDEA software development kits (SDKs) and proxy software with platform providers, law enforcement, and research firms to help drive ecosystem-wide awareness and enforcement. These SDKs, which are offered to developers across multiple mobile and desktop platforms, surreptitiously enroll user devices into the IPIDEA network. Driving collective enforcement against these SDKs helps protect users across the digital ecosystem and restricts the network's ability to expand.
3. These efforts to help keep the broader digital ecosystem safe supplement the protections we have to safeguard Android users on certified devices. We ensured Google Play Protect, Android’s built-in security protection, automatically warns users and removes applications known to incorporate IPIDEA SDKs, and blocks any future install attempts.

We believe our actions have caused significant degradation of IPIDEA’s proxy network and business operations, **reducing the available pool of devices for the proxy operators by millions.** Because proxy operators share pools of devices using reseller agreements, we believe these actions may have downstream impact across affiliated entities.

### Dizzying Array of Bad Behavior Enabled by Residential Proxies

In contrast to other types of proxies, residential proxy networks sell the ability to route traffic through IP addresses owned by internet service providers (ISPs) and used to provide service to residential or small business customers. By routing traffic through an array of consumer devices all over the world, attackers can mask their malicious activity by hijacking these IP addresses. This generates significant challenges for network defenders to detect and block malicious activities.

A robust residential proxy network requires the control of millions of residential IP addresses to sell to customers for use. IP addresses in countries such as the US, Canada, and Europe are considered especially desirable. To do this, residential proxy network operators need code running on consumer devices to enroll them into the network as exit nodes. These devices are either pre-loaded with proxy software or are joined to the proxy network when users unknowingly download trojanized applications with embedded proxy code. Some users may knowingly install this software on their devices, lured by the promise of “monetizing” their spare bandwidth. When the device is joined to the proxy network, the proxy provider sells access to the infected device’s network bandwidth (and use of its IP address) to their customers. 

While operators of residential proxies often extol the privacy and freedom of expression benefits of residential proxies, Google Threat Intelligence Group’s (GTIG) research shows that these proxies are overwhelmingly misused by bad actors. IPIDEA has become notorious for its role in facilitating several botnets: its software development kits played a key role in adding devices to the botnets, and its proxy software was then used by bad actors to control them. This includes the [BadBox2.0 botnet we took legal action against](https://blog.google/innovation-and-ai/technology/safety-security/google-taking-legal-action-against-the-badbox-20-botnet/) last year, and the Aisuru and Kimwolf botnets more recently. We also observe IPIDEA being leveraged by a vast array of espionage, crime, and information operations threat actors. In a single seven day period in January 2026, GTIG observed over 550 individual threat groups that we track utilizing IP addresses tracked as IPIDEA exit nodes to obfuscate their activities, including groups from China, DPRK, Iran and Russia. The activities included access to victim SaaS environments, on-premises infrastructure, and password spray attacks. Our research has found significant overlaps between residential proxy network exit nodes, likely because of reseller and partnership agreements, making definitive quantification and attribution challenging. 

In addition, residential proxies pose a risk to the consumers whose devices are joined to the proxy network as exit nodes. These users knowingly or unknowingly provide their IP address and device as a launchpad for hacking and other unauthorized activities, potentially causing them to be flagged as suspicious or blocked by providers. Proxy applications also [introduce security vulnerabilities](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) to consumers’ devices and home networks. When a user’s device becomes an exit node, network traffic that they do not control will pass through their device. This means bad actors can access a user’s private devices on the same network, effectively exposing security vulnerabilities to the internet. GTIG’s analysis of these applications confirmed that IPIDEA proxy did not solely route traffic through the exit node device, they also sent traffic to the device, in order to compromise it. While proxy providers may claim ignorance or close these security gaps when notified, enforcement and verification is challenging given intentionally murky ownership structures, reseller agreements, and diversity of applications.

### The IPIDEA Proxy Network

Our analysis of residential proxy networks found that many well-known residential proxy brands are not only related but are controlled by the actors behind IPIDEA. This includes the following ostensibly independent proxy and VPN brands: 

* 360 Proxy (360proxy\.com)
* 922 Proxy (922proxy\.com)
* ABC Proxy (abcproxy\.com)
* Cherry Proxy (cherryproxy\.com)
* Door VPN (doorvpn\.com)
* Galleon VPN (galleonvpn\.com)
* IP 2 World (ip2world\.com)
* Ipidea (ipidea\.io)
* Luna Proxy (lunaproxy\.com)
* PIA S5 Proxy (piaproxy\.com)
* PY Proxy (pyproxy\.com)
* Radish VPN (radishvpn\.com)
* Tab Proxy (tabproxy\.com)

The same actors that control these brands also control several domains related to Software Development Kits (SDKs) for residential proxies. These SDKs are not meant to be installed or executed as standalone applications, rather they are meant to be embedded into existing applications. The operators market these kits as ways for developers to monetize their applications, and offer Android, Windows, iOS, and WebOS compatibility. Once developers incorporate these SDKs into their app, they are then paid by IPIDEA usually on a per-download basis.