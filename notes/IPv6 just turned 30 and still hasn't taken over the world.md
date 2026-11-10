---
title: "IPv6 just turned 30 and still hasn't taken over the world"
url: https://www.theregister.com/2025/12/31/ipv6_at_30/
clipped: 2026-06-17 02:04:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - ipv6
  - internet protocols
  - network address translation
  - infrastructure migration
  - backward compatibility
  - quic
related:
  - "[[Internet Protocols]]"
  - "[[Infrastructure Migration]]"
  - "[[Network Address Translation]]"
---


<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Three decades after RFC 1883 defined IPv6, global adoption remains below 50% due to dual-stack complexity, lack of backward compatibility, and NAT extending IPv4's lifespan.
>
> **Key points:**
> - IPv6 expanded address space from 32-bit (4.3 billion) to 128-bit (340 undecillion) to prevent IPv4 exhaustion.
> - Lack of backward compatibility required expensive dual-stack configurations, hindering early adoption.
> - Network Address Translation (NAT) and technologies like QUIC reduced the immediate need for unique public IP addresses.
> - Mobile networks, cloud providers, and large infrastructure projects (e.g., Starlink, Huawei) drive current gradual IPv6 adoption.
>
> **Concept links:** [[Ipv6]], [[Internet Protocols]], [[Network Address Translation]], [[Infrastructure Migration]], [[Backward Compatibility]], [[Quic]]
>
> **Suggested connections:**
> - [[Internet Protocols]] — the evolution of fundamental routing and transport protocols on the web.
> - [[Infrastructure Migration]] — the challenges and economic trade-offs of legacy system upgrades.
> - [[Network Address Translation]] — the technology that prolonged IPv4 viability.
<!-- ai-summary:end -->
# [IPv6 just turned 30 and still hasn't taken over the world](https://www.theregister.com/2025/12/31/ipv6_at_30/)

## Digest Summary
IPv6, defined in RFC 1883 (1995), expanded address space from 32‑bit (≈4.3 billion) to 128‑bit (≈3.4 × 10³⁸) addresses, aiming to prevent IPv4 exhaustion. Adoption remains under 50 % globally according to Google, APNIC, and Cloudflare data. Key factors limiting deployment:

* IPv6 is not backward‑compatible with IPv4, requiring dual‑stack or migration, raising cost and complexity.
* It introduced few functional enhancements beyond address size; many security, QoS, and plug‑and‑play features were later added to IPv4.
* Network Address Translation (NAT) extended IPv4 usability, allowing many devices to share a single public address and delaying the need for IPv6.
* Vendor support, migration ROI, and legacy infrastructure lacking dual‑stack capability hindered uptake.

Despite limited rollout, IPv6 supports growth in mobile, broadband, cloud, IoT, and advanced routing (e.g., Segment Routing). Some operators adopt IPv6 when IPv4 address costs rise. Emerging technologies such as QUIC and name‑based DNS/ security models reduce reliance on permanent IP addresses, further altering IPv6’s perceived necessity. Organizations like Huawei and Starlink have secured massive IPv6 blocks, contributing to gradual increases in adoption rates.

## Discussion Summary
Overall sentiment reflects mixed experience with IPv6: adoption has steadily risen to roughly half of global traffic, driven by mobile networks and some enterprise or IoT deployments, yet many users and small operators still rely on IPv4 due to dual‑stack complexity, inconsistent ISP support, and perceived lack of tangible benefits. Common frustrations include difficult configuration, address length, and privacy concerns, while critics label the protocol a failure or unnecessary because it is not backward‑compatible. Conversely, proponents argue that IPv6 resolves address‑space limits and is essential for future growth, emphasizing the need for clearer incentives and broader education.

---

## Full Article

FEATURE In the early 1990s, internetworking wonks realized the world was not many years away from running out of Internet Protocol version 4 (IPv4) addresses, the numbers needed to identify any device connected to the public internet. Noting booming interest in the internet, the internet community went looking for ways to avoid an IP address shortage that many feared would harm technology adoption and therefore the global economy.

A possible fix arrived in December 1995 in the form of [RFC 1883](https://datatracker.ietf.org/doc/html/rfc1883), the first definition of IPv6, the planned successor to IPv4.

The most important change from IPv4 to IPv6 was moving from 32-bit to 128-bit addresses, a decision that increased the available pool of IP addresses from around 4.3 billion to over 340 undecillion – a 39-digit number. IPv6 was therefore thought to have future-proofed the internet, because nobody could imagine humanity would ever need more than a handful of undecillion IP addresses, never mind the entire range available under IPv6.

As billions of devices and people came online, first using PCs and then wielding smartphones, conventional wisdom assumed that network operators would move to IPv6 rather than persist with IPv4.

Yet according to data from [Google](https://www.google.com/intl/en/ipv6/statistics.html#tab=ipv6-adoption), [the Asia Pacific Network Information Center (APNIC)](https://stats.labs.apnic.net/ipv6/XA), and [Cloudflare](https://radar.cloudflare.com/adoption-and-usage), less than half of all netizens use IPv6 today.

To understand why, know that IPv6 also suggested other, rather modest, changes to the way networks operate.

"IPv6 was an extremely conservative protocol that changed as little as possible," APNIC chief scientist Geoff Huston told *The Register*. "It was a classic case of mis-design by committee."

And that notional committee made one more critical choice: IPv6 was not backward-compatible with IPv4, meaning users had to choose one or the other – or decide to run both in parallel.

For many, the decision of which protocol to use was easy because IPv6 didn't add features that represented major improvements.

"One big surprise to me was how few features went into IPv6 in the end, aside from the massive expansion of address space," said Bruce Davie, a veteran computer scientist recently honored with a [lifetime achievement award](https://www.sigcomm.org/awards/sigcomm-award-recipients) by the Association for Computing Machinery's Special Interest Group on Data Communications, which lauded him for "fundamental contributions in networking systems through design, standardization, and commercialization of network protocols and systems."

Davie said many of the security, plug-and-play, and quality of service features that didn't make it into IPv6 were eventually implemented in IPv4, further reducing the incentive to adopt the new protocol. "Given the small amount of new functionality in v6, it's not so surprising that deployment has been a 30 year struggle," he said.

Another innovation that meant IPv6 made less sense was network address translation (NAT), which allows many devices to share a single public IPv4 address. NAT meant IPv4 network operators could connect thousands of devices with a single IP address, meaning their existing IP addresses became more useful.

"These solutions were relatively easy to deploy, aligned with existing expertise, and avoided large-scale infrastructure changes," said Alvaro Vives, manager of the learning and development team at RIPE NCC, the regional internet registry for 76 nations across Europe, the Middle East, and Central Asia.

Because NAT stalled IPv6 adoption, vendors didn't rally behind the new protocol.

"Migration costs, complexity, and training requirements remain high, while short-term ROI is low," Gartner distinguished VP analyst Andrew Lerner told *The Register*. "Performance parity across applications and devices is inconsistent, and some organizations even disable IPv6 for better performance. Lack of dual-stack support in legacy infrastructure is another barrier," he added.

### A misunderstood protocol

While IPv6 didn't take off as expected, it's not fair to say it failed.

"IPv6 wasn't about turning IPv4 off, but about ensuring the internet could continue to grow without breaking," said John Curran, president and CEO of the American Registry for Internet Numbers (ARIN).

"In fact, IPv4's continued viability is largely because IPv6 absorbed that growth pressure elsewhere – particularly in mobile, broadband, and cloud environments," he added. "In that sense, IPv6 succeeded where it was needed most, and must be regarded as a success."

RIPE NCC's Alvaro Vives agrees. "What IPv6 got right was its long-term design," he told *The Register*. "It provides a vast address space that allows networks to be planned more simply and consistently. This has enabled innovation, from large mobile networks to the Internet of Things and advanced routing techniques such as Segment Routing over IPv6."

Gartner's Lerner thinks the time has come for organizations to develop detailed IPv6 migration plans.

"Validate application compatibility, and ensure new infrastructure supports IPv6," he advised. "Pilot deployments and lab testing with DNS64/NAT64 are recommended. Over time, IPv6 adoption will accelerate as private IPv4 space depletes and cloud providers introduce pricing models that favor IPv6."

APNIC's Huston, however, thinks that IPv6 has become less relevant to the wider internet.

"I would argue that we actually found a far better outcome along the way," he told *The Register*. "NATS forced us to think about network architectures in an entirely different way."

That new way is encapsulated in a new technology called Quick UDP Internet Connections (QUIC), that doesn't require client devices to always have access to a public IP address.

"We are proving to ourselves that clients don't need permanent assignment of IP address, which makes the client side of network far cheaper, more flexible, and scalable," he said.

Huston thinks IPv6 has also become less relevant to servers.

"These days the Domain Name Service (DNS) is the service selector, not the IP address," Huston told *The Register*. "The entire security framework of today's Internet is name based and the world of authentication and channel encryption is based on service names, not IP addresses."

"So folk use IPv6 these days based on cost: If the cost of obtaining more IPv4 addresses to fuel bigger NATs is too high, then they deploy IPv6. Not because it's better, but if they are confident that they can work around IPv6's weaknesses then in a largely name based world there is no real issue in using one addressing protocol or another as the transport underlay."

But there are plenty of organizations that still see a need for IPv6. [Huawei sought 2.56 decillion IPv6 addresses](https://www.theregister.com/2024/12/06/apnic_huawei_ipv6/) and Starlink appears to have acquired[150 sextillion](https://www.theregister.com/2025/10/29/nded/), which is helping to [push more countries](https://www.theregister.com/2025/06/27/ipv6_adoption_statistics/) past 50 percent IPv6 adoption. ®