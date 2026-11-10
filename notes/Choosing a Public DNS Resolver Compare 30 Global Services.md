---
title: "Choosing a Public DNS Resolver: Compare 30 Global Services"
url: https://evilbit.de/dns-resolver-guide.html
clipped: 2026-08-31 12:26:36
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Choosing a Public DNS Resolver: Compare 30 Global Services](https://evilbit.de/dns-resolver-guide.html)

## Full Article

Step 1 · Interactive finder
  

## Find a resolver for your requirements

  

Check what matters to you. Transport, DNSSEC, IPv6, jurisdiction and operator type are hard filters. The priorities are scored and ranked.
  
    
      
        

### My priorities

        Maximum privacy and no loggingMinimal or no query logging, privacy-first operator
        Block malware and phishingSecurity blocklist on by default or via a simple variant
        Block ads and trackersNetwork-wide ad and tracker filtering
        Parental controls and adult-content blockingFamily or adult-content filter available
        No filtering (unaltered DNS)Returns answers exactly as published
        Fully customizable filteringChoose your own blocklists or rules via an account
        Top-tier speed (global anycast)Large low-latency anycast network
        Non-commercial operatorNonprofit, registry, community or public-interest, not a for-profit company
      
      
        

### Must support encrypted DNS

        DNS-over-HTTPS (DoH)
        DNS-over-TLS (DoT)
        DNS-over-QUIC (DoQ)
        DNSCrypt
      
      
        

### Other requirements

        Must validate DNSSEC
        Must offer IPv6Provides IPv6 resolver addresses
        Operator jurisdiction
        
        Operator type
        
          Any
          Nonprofit, community or public-interest
          Commercial
        
        EDNS Client Subnet (ECS)
        
          Any
          Does not send ECS (more privacy)
          Sends ECS (better CDN routing)
        
      
      Clear all filters
    

    
      
        

## Recommended resolvers

        
      
      
    
  

  Step 2 · Live latency test
  

## Test DNS speed from your location

  

This measures DNS-over-HTTPS round-trip time from your browser to each DoH-capable resolver, so you can see which is fastest where you actually are. Plain-DNS-only resolvers cannot be tested this way. Results are a relative guide and include TLS and HTTP overhead, so run it a couple of times. Your browser queries each resolver directly, which reveals your IP address to them; nothing is sent anywhere else.
  
    
      Run speed test
      Benchmarks the DoH-capable resolvers, takes a few seconds.
    
    
    
      
        #ResolverMedianLatencyBest
        Press Run to benchmark from your location.
      
    
    

The test connects to each resolver by hostname, so your browser decides whether to use IPv4 or IPv6 (via Happy Eyeballs). On an IPv6-capable network most endpoints are measured over IPv6, otherwise over IPv4; this cannot be forced from the page.
    

Technique inspired by the open-source [DNS Speed Test](https://dnsspeedtest.online/) by Silviu Stroe (GPL-3.0); this is an independent implementation. It runs only when this page is served over HTTPS. For resolvers not testable here, that dedicated tool benchmarks a wider DoH set.
  

  Step 3 · Full comparison
  

## All 30 global public resolvers

  

Click a column header to sort. Search by name, operator, jurisdiction, or feature. Filter-variant addresses (malware, family, unfiltered) are listed in the Filtering cell. Where available, the Logging column links to the operator's published privacy policy (several follow RFC 8932).
  
    
  
  
    
      
        Resolver
        Jurisdiction
        Type
        Primary IPs (v4 / v6)
        Filtering (default and variants)
        DNSSEC
        Transports
        Logging
        ECS
      
      
    
  

  Evidence
  

## How to decide: what the research says

  

Findings from peer-reviewed DNS measurement studies that should shape the trade-offs above.
  
    
      
      
        

### Speed: plain DNS has the lowest latency, but encrypted keeps up

        

Encrypted transports (DoH and DoT) add latency per query, yet whole-page load times are often close to plain DNS, and DoH's overhead is small in practice. On lossy or high-latency links, plain Do53 still wins. Performance also varies by provider and region, so the fastest resolver depends on where you are.
        

Hounsel et al., WWW 2020; Böttger et al., IMC 2019; Chhabra et al., IMC 2021.
      
    
    
      
      
        

### Encrypted DNS resists tampering, not just snooping

        

The largest end-to-end study of encrypted DNS found queries are far less likely to be intercepted or altered in transit than plain DNS, with only minor overhead. Operator quality varies, though: about 25% of DoT providers in that study served invalid TLS certificates, so favour well-run providers.
        

Lu et al., IMC 2019.
      
    
    
      
      
        

### Encryption hides queries from the network, not from the resolver

        

Whichever provider you choose still sees every domain you look up. If that worries you, prefer no-logging operators, or an oblivious design (ODoH) where a proxy separates your identity from your queries so no single party sees both. Cloudflare and Apple have deployed ODoH.
        

Schmitt, Edmundson & Feamster, PoPETS 2019; Singanamalla et al., 2021.
      
    
    
      
      
        

### DNSSEC validation is what stops forged answers

        

Only a validating resolver protects you from spoofed records. Google, Cloudflare and Quad9 all validate, and they handled the first root-key (KSK) rollover without breaking users. If integrity matters, treat DNSSEC validation as a must.
        

Müller et al., IMC 2019.
      
    
    
      
      
        

### ECS trades speed for privacy

        

EDNS Client Subnet sends part of your IP to CDNs for better geo-routing. Google and OpenDNS send it for sharper CDN mapping; Cloudflare and standard Quad9 leave it off for privacy. Pick based on which you value more.
        

"A Look at the ECS Behavior of DNS Resolvers", IMC 2019.
      
    
    
      
      
        

### Jurisdiction and centralization matter too

        

The operator's legal home governs what can be compelled or logged, and a handful of providers now carry a large share of the world's recursive traffic. The U.S. NSA has also warned that external resolvers bypass internal DNS filtering and inspection, so weigh control against convenience.
        

Moura et al., IMC 2020; NSA guidance, 2021.
      
    
    
      
      
        

### DNS-over-QUIC is now the fastest encrypted transport

        

A 2022 measurement of DoQ found it already beats both DoT and DoH on response time, though about 40% of handshakes were slowed by QUIC's address-validation limit. Where your client and resolver both support it (Quad9, AdGuard, NextDNS, Control D, Mullvad, UncensoredDNS, and the Chinese majors here), DoQ is the encrypted option to prefer.
        

Kosek et al., PAM 2022.
      
    
    
      
      
        

### DNSCrypt: the oldest encrypted option, and the hardest to measure

        

DNSCrypt predates DoH, DoT, and DoQ (version 2 dates to 2013). It encrypts from the first packet using a resolver's pre-shared public key, so there is no plaintext hostname lookup and no dependency on certificate authorities, and its Anonymized DNS mode (2019) also hides client IPs. Among the resolvers here it is offered by Quad9, OpenDNS, AdGuard, NextDNS, Control D, and Yandex. Reliable usage numbers are scarce, though: population-scale measurements such as [APNIC Labs](https://stats.labs.apnic.net/edns) track DoH and DoT but not DNSCrypt, so there is no trustworthy public figure for how many people use it.
        

[DNSCrypt Project](https://dnscrypt.info/); APNIC Labs encrypted-DNS measurement.
      
    
    
      
      
        

### Encryption does not hide which sites you visit

        

Even over DoH, traffic analysis can identify the domains you visit with high accuracy, and the standard EDNS padding does not fully prevent it. If that threat model applies to you, pair encrypted DNS with Tor or an oblivious design rather than relying on padding.
        

Siby et al., NDSS 2020.
      
    
    
      
      
        

### Public resolvers do not behave the same way

        

A 2023 study of Extended DNS Errors across major resolvers found they disagreed on diagnostic error reporting in 94% of test cases, with Cloudflare the most precise. Implementation quality and standards compliance differ between providers, which affects troubleshooting and reliability.
        

Nosyk, Korczyński & Duda, IMC 2023.
      
    
  

  
    References
    
      
- A. Hounsel et al., "Comparing the Effects of DNS, DoT, and DoH on Web Performance", [WWW 2020 (arXiv:1907.08089)](https://arxiv.org/abs/1907.08089).
      
- T. Böttger et al., "An Empirical Study of the Cost of DNS-over-HTTPS", [ACM IMC 2019](https://conferences.sigcomm.org/imc/2019/program/).
      
- R. Chhabra, P. Murley, D. Kumar, M. Bailey, G. Wang, "Measuring DNS-over-HTTPS Performance Around the World", [ACM IMC 2021](https://conferences.sigcomm.org/imc/2021/accepted/).
      
- C. Lu et al., "An End-to-End, Large-Scale Measurement of DNS-over-Encryption: How Far Have We Come?", [ACM IMC 2019](https://conferences.sigcomm.org/imc/2019/program/).
      
- M. Kosek et al., "One to Rule Them All? A First Look at DNS over QUIC", [PAM 2022 (arXiv:2202.02987)](https://arxiv.org/abs/2202.02987).
      
- S. Siby et al., "Encrypted DNS => Privacy? A Traffic Analysis Perspective", [NDSS 2020 (arXiv:1906.09682)](https://arxiv.org/abs/1906.09682).
      
- P. Schmitt, A. Edmundson, N. Feamster, "Oblivious DNS: Practical Privacy for DNS Queries", [PoPETS 2019 (arXiv:1806.00276)](https://arxiv.org/abs/1806.00276).
      
- S. Singanamalla et al., "Oblivious DNS over HTTPS (ODoH)", [arXiv:2011.10121](https://arxiv.org/abs/2011.10121).
      
- M. Müller et al., "Roll, Roll, Roll your Root: Analysis of the First Ever DNSSEC Root KSK Rollover", [ACM IMC 2019](https://conferences.sigcomm.org/imc/2019/program/).
      
- "A Look at the ECS Behavior of DNS Resolvers", [ACM IMC 2019](https://conferences.sigcomm.org/imc/2019/program/).
      
- G. Moura, S. Castro, W. Hardaker, M. Wullink, C. Hesselman, "Clouding up the Internet: how centralized is DNS traffic becoming?", [ACM IMC 2020](https://conferences.sigcomm.org/imc/2020/accepted/).
      
- Y. Nosyk, M. Korczyński, A. Duda, "Extended DNS Errors: Unlocking the Full Potential of DNS Troubleshooting", [ACM IMC 2023](https://dl.acm.org/doi/10.1145/3618257.3624835).
    
  

  
    Operational and community data
    

Not peer-reviewed, but authoritative and continuously updated. Useful for checking the live state of the resolver ecosystem.
    
      
- ICANN [Identifier Technology Health Indicators (ITHI)](https://ithi.research.icann.org/): tracks the [share of resolvers that perform DNSSEC validation](https://ithi.research.icann.org/graph-m5.html) and [resolver concentration](https://ithi.research.icann.org/graph-m4.html) (how few resolvers serve most queries).
      
- DNS-OARC [workshop talks](https://www.youtube.com/DNS-OARC) and [past-event archive](https://indico.dns-oarc.net/): semi-annual operator and researcher presentations on encrypted DNS, resolver performance, and measurement.
      
- APNIC Labs [measurements](https://labs.apnic.net/measurements/) (the live data behind many OARC and ICANN talks, by Geoff Huston): [DNSSEC validation rate by country](https://stats.labs.apnic.net/dnssec), [use of public resolvers](https://stats.labs.apnic.net/rvrs), and [DoH and DoT adoption](https://stats.labs.apnic.net/edns).
    
  

  
    Recent operator news
    

Several of the resolvers above publish a blog or news feed, which is a useful way to track protocol support, privacy-policy changes, and outages. A few recent items:
    
      
- [Quad9](https://quad9.net/news/blog/): strict DNSSEC validation reaching all endpoints (15 June 2026), an updated privacy policy (June 2026), DoH3 and DoQ enabled (March 2026), and a public letter opposing resolver-level content enforcement in the EU (November 2025).
      
- [Cloudflare 1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/): Extended DNS Error 33 now signals when DNSSEC validation was bypassed (July 2026), a post-mortem on the .de TLD DNSSEC outage (May 2026), and the 2026 independent privacy examination (April 2026).
      
- [Control D](https://controld.com/blog): regular product updates plus ISO 27001 and ISO 27701 certification (March 2026).
      
- [UncensoredDNS](https://blog.uncensoreddns.org/blog/): full DoQ and DoH3 support (October 2025).
      
- [Mullvad](https://mullvad.net/en/blog): an active privacy and security blog, mostly covering its VPN and browser.
    
  

  
    Smaller, community-run, and regional resolvers
    

Niche, hobby, community, or country-specific services that are not in the comparison above. Worth knowing about, but check their current status and policies before relying on them. The European entries are catalogued by [European Alternatives](https://european-alternatives.eu/category/public-dns). Resolvers based in heavily censored or sanctioned regions may enforce local content rules or, conversely, exist mainly to bypass geo-blocks, so treat those with extra care.
    
      
- [DNS4all](https://dns4all.eu/) (194.0.5.3): European resolver focused on neutrality and performance; unfiltered.
      
- [BlahDNS](https://blahdns.com/): open-source hobby ad-blocking project with DoH, DoT, and DoQ, run on small regional servers.
      
- [LibreDNS](https://libredns.gr/): community resolver by LibreOps with ad-blocking and a no-logging policy; DoH and DoT.
      
- [Dismail.de](https://dismail.de/): privacy-focused German community resolver with no logging; DoH and DoT.
      
- [Foundation for Applied Privacy](https://applied-privacy.net/services/dns/) (Austria): non-profit, no-logging; DoH and DoT.
      
- [Freifunk München (FFMUC)](https://dns-setup.ffmuc.net/) (Germany): community non-profit, open source; plaintext plus DoH and DoT.
      
- [Restena](https://www.restena.lu/en/service/public-dns-resolver) (Luxembourg): the Restena Foundation national research network; DoH and DoT.
      
- [Digitale Gesellschaft](https://www.digitale-gesellschaft.ch/dns/) (Switzerland): non-profit with DNSSEC, DoH and DoT (German-language site).
      
- [dnsforge](https://dnsforge.de/) (Germany): community resolver that filters ads, tracking, and malware; open source.
      
- [DNSBunker](https://dnsbunker.org/) (185.250.250.61, Germany): private, non-commercial resolver, encrypted-only (DoH/DoH3/DoT/DoQ) with Hagezi ad and threat filtering, strict DNSSEC, and no query logs.
      
- [OpenBLD.net](https://openbld.net/) (ada.openbld.net, Kazakhstan): free community protective resolver with ADA (adaptive) and RIC (strict) profiles, ad, tracker and malware filtering with URLhaus threat intelligence; DoH, DoT, DNSSEC. Free tier is rate-limited (around 100k queries per day).
      
- [Digitalcourage](https://digitalcourage.de/support/zensurfreier-dns-server) and [Artikel10](https://dns.artikel10.org/) (Germany): privacy-focused non-profit resolvers with DoH and DoT (German-language sites).
      
- [FDN](https://www.fdn.fr/actions/dns/) (France): long-running associative ISP with a no-logging, no-censorship open resolver.
      
- [IIJ Public DNS](https://public.dns.iij.jp/) (Japan): public DoH and DoT resolver from Internet Initiative Japan, a major operator; blocks child-abuse (CSAM) domains.
      
- [CNNIC sDNS](http://www.sdns.cn/) (China): the Chinese registry's public resolver (the well-known 1.2.4.8); subject to local regulations.
      
- [Comss.one DNS](https://www.comss.one/) (Russia): ad-blocking resolver popular in the Russian-speaking community.
      
- [Shecan](https://shecan.ir/), Electro, Begzar, and [403.online](https://403.online/) (Iran): widely used inside Iran mainly to reach developer and cloud services that block Iranian IP addresses; special-purpose, with limited published policy.
      
- [Andrews & Arnold](https://www.aa.net.uk/dns/) (United Kingdom): non-filtering, no-logging, DNSSEC DoH from a respected UK ISP.
      
- [SWITCH](https://www.switch.ch/) (Switzerland): DoH from the Swiss national research-and-education network and .ch registry; malware protection, no ad blocking.
      
- [Njalla](https://njal.la/) (Sweden): no-logging DoH from the privacy-focused domain registrar.
      
- [DNS for Family](https://dnsforfamily.com/): free family-filtering DoH (blocks adult, gambling, malware, ads and trackers, with safe search), no logs, DNSSEC.
      
- [Safe Surfer](https://safesurfer.io/) (New Zealand): family-safety DoH blocking adult content and CSAM; free with paid tiers (logs anonymized).
      
- Legacy or discontinued services to avoid: Oracle Dyn, Level3 (4.2.2.x), UUNET (198.6.1.x, now part of Verizon), Freenom World, dns0.eu (use DNS4EU or NextDNS instead), and Norton ConnectSafe appear in older lists but are legacy, unofficial, or discontinued.
