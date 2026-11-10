---
title: "How is Groq raising more money?"
url: https://www.zach.be/p/how-the-hell-is-groq-raising-more
clipped: 2026-06-17 00:54:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - AI Hardware
  - Groq LPUs
  - SRAM Architecture
  - Datacenter Infrastructure
  - Venture Capital
  - Nvidia Licensing
related:
  - "[[Launch HN Kita (YC W26) – Automate credit review in emerging markets]]"
  - "[[When the cheap one is the cool one]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article explains how Groq continues as a private inference provider after licensing its chip tech to Nvidia, capitalizing on its datacenters.
>
> **Key points:**
> - Nvidia licensed Groq's LPU chip architecture and hired key executives in Dec 2025, but did not buy the corporate entity.
> - Groq operates GroqCloud using its all-SRAM LPUv1 chip architecture to offer high-speed, latency-sensitive inference for smaller models.
> - SRAM-based LPUs are limited by high-bandwidth memory (HBM) lack, making them unfeasible for large frontier-class models.
> - The company's value lies in its four operational datacenters, which are rare assets due to power and construction delays.
>
> **Concept links:** [[AI Hardware]], [[Groq LPUs]], [[SRAM Architecture]], [[Datacenter Infrastructure]], [[Venture Capital]], [[Nvidia Licensing]]
>
> **Suggested connections:**
> - [[Launch HN Kita (YC W26) – Automate credit review in emerging markets]] — related fintech and hardware capital raising.
> - [[When the cheap one is the cool one]] — related hardware/software design constraints.
<!-- ai-summary:end -->

# [How is Groq raising more money?](https://www.zach.be/p/how-the-hell-is-groq-raising-more)

## Digest Summary
Groq, an AI‑chip company whose technology was licensed by Nvidia and whose key technical staff joined Nvidia, continues operating as an independent corporate entity. The remaining business focuses on GroqCloud, a private inference service that leverages the company’s all‑SRAM architecture to deliver very high token‑per‑second rates for relatively small models (up to ~120 B parameters). This design trades higher token‑per‑dollar efficiency for lower cost per token, making it suitable for latency‑sensitive workloads but unsuitable for frontier‑size models due to limited high‑bandwidth memory. Groq maintains four fully operational datacenters, a rare asset given the difficulty of building new facilities. The firm is raising $650 M, potentially at a low valuation because most of its differentiating chip technology has been transferred to Nvidia, while its datacenter operations and expertise remain. Comparisons to larger AI‑infrastructure providers (CoreWeave, Nebius) highlight that Groq’s assets could be valued in the billions, though its hardware (LPU v1) is aging and newer LPU v3 chips are now sold by Nvidia to cloud providers, reducing Groq’s unique performance advantage.

## Discussion Summary
Comments express overall skepticism toward Groq’s value, citing high token costs, inconsistent performance, and reliability issues that led some users to avoid recommending the service. Several remarks highlight confusion about recent corporate actions, including Nvidia’s acquisition of assets and ambiguous statements about a “new company,” leaving the future direction unclear. A minority points to Groq’s unique fast‑inference capability as a potential advantage, but the prevailing sentiment remains critical, focusing on cost, instability, and uncertainty about the company’s strategic outlook.

---

## Full Article

Axios just dropped a bizarre scoop. Groq, the AI chip company company that was [acquired by Nvidia](https://www.zach.be/p/why-did-nvidia-acqui-hire-groq) in December of last year, [is raising $650M](https://www.axios.com/2026/05/28/groq-650-million-nvidia). How, exactly, is a company that successfully exited raising more capital?

Well, technically, [Nvidia did not acquire Groq](https://www.zach.be/p/why-did-nvidia-acqui-hire-groq). They [licensed Groq’s technology and hired Groq’s key technical executives](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale), but did not acquire the Groq corporate entity. That corporate entity continued to operate, focusing on [maintaining Groq’s datacenters and their inference API](https://www.zach.be/p/why-is-everybody-talking-about-groq). That API focuses on offering extremely fast inference on smaller models; their largest supported model is [GPT OSS 120B](https://console.groq.com/docs/models), which is likely at least 10x smaller than frontier models like GPT-5.5 or Claude Mythos. This is a technical limitation of Groq’s architecture; without large amounts of high-bandwidth memory (HBM) in each chip package, [the total cost to build and maintain a Groq cluster capable of serving a frontier model would be massive.](https://www.zach.be/p/why-is-everybody-talking-about-groq) However, their all-SRAM strategy lets them serve small models much faster than a conventional HBM-based chip, delivering more tokens-per-second at the cost of lower tokens-per-dollar. For certain applications, this makes sense.

More importantly, Groq has [four large datacenter deployments](https://groq.com/newsroom/groq-launches-european-data-center-footprint-in-helsinki-finland) that are already set up to serve inference workloads at scale. Building out new datacenters has been a [major challenge for startups and hyperscalars alike](https://www.tomshardware.com/tech-industry/artificial-intelligence/half-of-planned-us-data-center-builds-have-been-delayed-or-canceled-growth-limited-by-shortages-of-power-infrastructure-and-parts-from-china-the-ai-build-out-flips-the-breakers), so Groq’s datacenters represent a major strategic asset. However, it remains to be seen if the Groq name gives them a legitimate leg up, and or if their brand association with the LPU chip and a specific high-speed, high-cost inference strategy limits them.

As inference demand surges, existing datacenters are quickly reaching full utilization and companies are trying to build new ones as fast as possible. But between regulation, power issues, and expertise, [even large companies with experience building out datacenters are experiencing major delays](https://www.tomshardware.com/tech-industry/artificial-intelligence/half-of-planned-us-data-center-builds-have-been-delayed-or-canceled-growth-limited-by-shortages-of-power-infrastructure-and-parts-from-china-the-ai-build-out-flips-the-breakers) in their datacenter construction projects. And for venture investors, who primarily invest in startups, getting direct exposure to datacenter demand is very difficult; because datacenters are so hard to build, very few startups are actually doing so.

Groq already has four functional datacenters, as well as the talent to build and operate more. When [Nvidia licensed Groq’s technology](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale), Groq’s chip design team, compiler team, and software team joined Nvidia, but Groq’s datacenter team stayed to maintain GroqCloud inference services. This makes the remaining Groq company a unique asset -- a private inference datacenter operator with clear operational expertise, plus what is likely an extremely low valuation due to most of their differentiating technology being acquired by Nvidia.

Let’s look at the numbers for some publicly traded AI datacenter companies to compare. [CoreWeave is a 50 billion dollar company](https://finance.yahoo.com/quote/CRWV/) operating [43 AI datacenters](https://www.coreweave.com/ai-data-centers). [Nebius is worth about 50 billion dollars too](https://finance.yahoo.com/quote/NBIS/), with [only 11 datacenters](https://www.datacentermap.com/c/nebius/), though they are larger than CoreWeave’s. One could argue that Groq’s datacenters alone could make them worth billions of dollars.

Thanks for reading zach's tech blog! This post is public so feel free to share it.

[Share](https://www.zach.be/p/how-the-hell-is-groq-raising-more?utm_source=substack&utm_medium=email&utm_content=share&action=share)

Obviously, there are a couple issues with comparing Groq to CoreWeave and Nebius directly. Groq’s datacenters are all full of LPUv1 chips, [which are seven years old at this point](https://www.eetimes.com/groq-demos-fast-llms-on-4-year-old-silicon/). [And the new LPUv3 chips based on Groq’s architecture are being sold by Nvidia](https://www.nvidia.com/en-us/data-center/lpx/) to any cloud provider who wants them. That means that Groq’s biggest technical advantage, of very fast tokens, is no longer unique to them.

Plus, the value of Groq’s brand adds additional complexity to the calculation. On one hand, Groq was a massively successful outcome. On the other, getting “acquired” and then still operating is confusing. And their brand is strongly associated with ultra-high-speed inference, which may not end up dominating inference workloads compared to lower-speed batched inference. This is particularly worrying as major organizations like [Microsoft](https://finance.yahoo.com/markets/stocks/articles/microsoft-tightens-ai-tools-investors-230707366.html) and [Uber](https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/) are raising the alarm about the high cost of AI coding tools.

Maybe Nvidia is giving Groq a sweetheart deal on buying hardware based on Groq’s technology, which would make Groq a significantly more appealing investment. Ultimately, it remains to be seen if Groq can successfully outfit their existing datacenters with new hardware to remain competitive with other cloud providers. I’m also curious to see whether they stay committed to high-speed, high-cost tokenomics, and if that strategy ends up being successful or not in the long term.