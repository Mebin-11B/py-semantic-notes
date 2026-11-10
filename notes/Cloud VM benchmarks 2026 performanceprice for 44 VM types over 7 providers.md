---
title: "Cloud VM benchmarks 2026: performance/price for 44 VM types over 7 providers"
url: https://devblog.ecuadors.net/cloud-vm-benchmarks-2026-performance-price-1i1m.html
clipped: 2026-06-17 01:35:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cloud VM benchmarks 2026: performance/price for 44 VM types over 7 providers](https://devblog.ecuadors.net/cloud-vm-benchmarks-2026-performance-price-1i1m.html)

## Digest Summary
- Tested 44 VM families from seven major cloud providers (AWS, GCP, Azure, OCI, Linode/Akamai, DigitalOcean, Hetzner) in 2‑vCPU configurations, covering multiple regions to capture performance variance.  
- New CPUs introduced: AMD EPYC Turin, Intel Granite Rapids, Google Axion (ARM), Azure Cobalt 100, Ampere One M.  
- Benchmark suite (Docker image) comprised DKbench (primary), Geekbench 5, Phoronix tests (7‑zip, nginx, OpenSSL), and FFmpeg x264 transcoding, run on Debian 13 (Ubuntu 24.04 for a few cases).  
- Single‑thread results: EPYC Turin delivers the highest per‑thread throughput; Granite Rapids offers higher and more stable performance than prior Intel generations; Axion matches EPYC Genoa on ARM; Cobalt 100 sits between Graviton‑3 and Graviton‑4.  
- Multi‑thread scaling follows SMT rules (2 vCPU = 1 full core for Intel/AMD).  
- Pricing uses on‑demand rates in the cheapest US/EU regions; reserved 1‑/3‑year rates shown without prepayment; OCI provides uniform pricing with 50 % spot discount; GCP sustained‑use discounts omitted for fairness.  
- Recommendation: avoid older CPU generations (Skylake, Broadwell, Rome) due to lower efficiency and higher cost per performance.

## Discussion Summary
The comments contrast cloud services with self‑hosted bare‑metal, noting that owning hardware often delivers lower cost per performance, especially for CI and batch workloads, while also requiring additional effort for maintenance, upgrades and fault handling. AMD EPYC (Turin/Genoa) CPUs receive consistent praise for strong single‑core and multi‑core benchmarks, and Hetzner is highlighted as offering good price‑performance despite recent price hikes. Cloud advantages are acknowledged for production environments, scalability and reduced operational burden, with some concern about vendor lock‑in, particularly with Oracle. Hybrid deployments are suggested as a practical compromise.

---

## Full Article

Cloud VM benchmarks 2026: performance / price
=============================================

Published: Feb 27, 2026 on [dev.to](https://dev.to/dkechag/cloud-vm-benchmarks-2026-performance-price-1i1m) by Dimitrios Kechagias

[#aws](https://devblog.ecuadors.net/tag-aws.html) [#googlecloud](https://devblog.ecuadors.net/tag-googlecloud.html) [#cloud](https://devblog.ecuadors.net/tag-cloud.html) [#devops](https://devblog.ecuadors.net/tag-devops.html)

Time for the (not exactly) yearly cloud compute VM comparison. I started testing back in October 2025, but the benchmarking scope was increased, not just due to more VM families tested (44), but also due to testing the instances over more regions to attain a possible range of performance, as in many cases not all instances are created equal. I will not spoil much if I tell you that there is one new CPU that dominates the top-end results more clearly than any previous year.

**Quick Overview**

Like [last time](https://dev.to/dkechag/cloud-provider-comparison-2024-vm-performance-price-3h4l), this is all about **generic CPU performance** and especially what you can actually **get per $ spent** on compute VM instances. Due to the focus on CPU workloads, burstable instances are not included. Single-thread performance is evaluated separately, as there are always workloads that cannot be further parallelized. For multi-thread, each instance type is tested in a 2vCPU configuration which is usually the minimum unit you can order (it corresponds to a single core for SMT-enabled systems, like all Intel and most AMD). The more threads your workload can utilize, the more multiples of that unit you can order.

The comparison should help you maximize performance or price depending on your requirements, by either using the optimal VM types of your provider, or perhaps by launching on a different provider.

If you don't need all the details, you can use the TOC below to jump to what's relevant to you.

**Table Of Contents:**

What's new
----------

I kept the same **7 providers** as last year (which was down from my max 10 providers from [the 2023 comparison](https://dev.to/dkechag/cloud-vm-performance-value-comparison-2023-perl-more-1kpp)), but expanded to **44 VM types** tested.

Other changes:

* **New CPUs:** AMD **EPYC Turin** (whose performance [I had explored separately](https://dev.to/dkechag/c4d-vms-on-google-cloud-breaking-records-again-with-epyc-turin-14ic)) and Intel **Granite Rapids** are available on the x86 front, while several new ARM solutions are tested: Google **Axion** ([also explored separately](https://dev.to/dkechag/google-axion-a-new-leader-in-arm-server-performance-4im9) last year), Azure **Cobalt 100** and Ampere **AmpereOne M**.
* **More testing:** Some extra benchmarks added. More testing across regions. In the past I only focused on that for small providers, but the big-three have also shown inconsistency, so the main performance and performance/price numbers will show a range.

The contenders (2026 edition)
-----------------------------

As mentioned, I will focus on **2x vCPU** instances, as that's the minimum scalable unit for a meaningful comparison (and generally minimum for several VM types), given that most **AMD** and **Intel** instances use Hyper-Threading (HT) / Simultaneous Multi Threading (SMT). So, for those systems a vCPU is a Hyper-Thread, or half a core, with the 2x vCPU instance giving you a full core with 2 threads. This will become clear in the scalability section.

I am skipping some very old instance types that are obviously uncompetitive. I am still trying to configure at **2GB/vCPU** of **RAM** (which is variably considered as "compute-optimized", or "general-purpose") and **30GB SSD** (not high-IOPS) boot disk for the price comparison to make sense (exceptions will be noted).

The **pay-as-you-go**/**on-demand** prices refer to the lower cost region in the US (or Europe). For providers with variable pricing, cheapest regions are almost always in the US. Unlike last year, I will not include the **100% sustained** discounts for GCP, as they are not technically **on-demand** so I may have been unfair to other providers.

For providers that offer **1 year** and **3 year** committed/reserved discounted prices, the no-downpayment price was listed with that option. The prices were valid for **January 2026** - please check for current prices before making final decisions.

As a guide, here is an overview of the various generations of AMD, Intel and ARM CPUs from older (top) to newer (bottom), roughly grouped horizontally in per-core performance tiers, based on this and the previous comparison results:

[![Chart of CPU rankings](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fihxwrtvu3iezsrccaih2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fihxwrtvu3iezsrccaih2.png)

This should immediately give you an idea of roughly what performance tier to expect based on the CPU type alone, with the important note that for SMT-enabled instances you get a single core for every 2x vCPUs.

A general tip is that you should avoid old CPU generations, as due to their lower efficiency (higher running costs) the cloud providers will actually **charge you more for less performance**. I will even not include types that were already too old to provide good value last year, to focus on the more relevant products.

### Amazon Web Services (AWS)

| Instance Type | CPU type | RAM/SSD | Price $/Month | 1Y Res. $/Month | 3Y Res. $/Month | Spot $/Month |
| --- | --- | --- | --- | --- | --- | --- |
| C5a.large (R) | AMD Rome | 4/30 | 64.45 | 41.09 | 29.41 | 29.08 |
| C5.large (S) | Intel Skylake | 4/30 | 68.10 | 45.47 | 31.60 | 28.02 |
| C6a.large (M) | AMD Milan | 4/30 | 63.83 | 43.04 | 29.45 | 28.20 |
| C6i.large (I) | Intel Ice Lake | 4/30 | 70.66 | 47.55 | 32.45 | 29.02 |
| C6g.large (G2) | AWS Graviton2 | 4/30 | 55.03 | 36.64 | 26.86 | 26.61 |
| C7a.large (G) | AMD Genoa | 4/30 | 84.82 | 56.92 | 38.69 | 32.07 |
| C7i.large (SR) | Intel Sapphire Rapids | 4/30 | 74.07 | 49.81 | 33.95 | 24.62 |
| C7g.large (G3) | AWS Graviton3 | 4/30 | 58.46 | 40.65 | 28.97 | 29.31 |
| C8a.large (T) | AMD Turin | 4/30 | 88.94 | 64.94 | 44.19 | 31.82 |
| C8i.large (GR) | Intel Granite Rapids | 4/30 | 77.65 | 51.84 | 35.43 | 28.74 |
| C8g.large (G4) | AWS Graviton4 | 4/30 | 66.22 | 44.62 | 30.50 | 27.93 |

[Amazon Web Services](https://aws.amazon.com/) (**AWS**) pretty much originated the whole "cloud provider" business - even though smaller connected VM providers predated it significantly (e.g. Linode comes to mind) - and still dominates the market. The **AWS** platform offers extensive services, but, of course, we are only looking at their Elastic Cloud (EC2) VM offerings for this comparison.

There are 2 new CPUs introduced since last year. Intel's **Granite Rapids** makes an appearance, while the AMD **EPYC Turin**-powered **C8a** follows the previous **C7a** in having SMT disabled (providing a full core per vCPU). I don't want to spoil much, but if you take the fastest CPU by a margin, and disable SMT, expect some impressive "per-2vCPU" results...

With EC2 instances you generally know what you are getting (instance type corresponds to specific CPU), although there's a multitude of ways to pay/reserve/prepay/etc which makes pricing very complicated, and pricing further varies by region (I used the lowest cost US regions). In the 1Y/3Y reserved prices listed, there is no prepayment included - you can lower them a bit further if you do prepay. The spot prices vary even more, both by region and are updated often (especially for newly introduced types), so you'd want to keep track of them.

### Google Cloud Platform (GCP)

| Instance Type | CPU type | RAM/SSD | Price $/Month | 1Y Res. $/Month | 3Y Res. $/Month | Spot $/Month |
| --- | --- | --- | --- | --- | --- | --- |
| n2-2\* (I) | Intel Ice Lake | 4/30 | 63.45 | 40.19 | 29.65 | 22.15 |
| n2d-2\* (M) | AMD Milan | 4/30 | 55.46 | 35.22 | 26.06 | 13.10 |
| c2d-2 (M) | AMD Milan | 4/30 | 68.28 | 43.76 | 31.82 | 15.87 |
| t2d-2 (M) | AMD Milan | 8/30 | 63.68 | 40.86 | 29.76 | 12.14 |
| c3-4/2\*\* (SR) | Intel Sapphire Rapids | 4/30 | 63.69 | 40.72 | 29.54 | 11.09 |
| c3d-4/2\*\* (G) | AMD Genoa | 4/30 | 56.32 | 36.08 | 26.23 | 9.90 |
| n4d-2 (T) | AMD Turin | 4/30 | 53.77 | 34.46 | 25.08 | 22.47 |
| c4a-2 (AX) | Google Axion (Arm) | 4/30 | 56.90 | 38.09 | 26.49 | 19.74 |
| c4d-2 (T) | AMD Turin | 3/30 | 57.57 | 36.86 | 26.79 | 23.40 |
| n4-2 (E) | Intel Emerald Rapids | 4/30 | 57.47 | 36.80 | 26.74 | 19.50 |
| c4-2 (E) | Intel Emerald Rapids | 4/30 | 63.69 | 40.72 | 29.54 | 27.20 |
| c4-lssd-4/2\*\* (GR) | Intel Granite Rapids | 8/30+375GB SSD | 103.75 | 65.45 | 47.57 | 43.70 |

\* *`min_cpu_platform` needs to be set to get tested CPU.*  
\*\* *Extrapolated 2x vCPU instance - type requires 4x vCPU minimum size.*

The [GCP Platform](https://cloud.google.com/) (**GCP**) follows **AWS** quite closely, providing mostly equivalent services, but lags in market share (3rd place, after **Microsoft Azure**). We are looking at the Google Compute Engine (GCE) VM offerings, which is one of the most interesting in respect to configurability and range of different instance types. However, this variety makes it harder to choose the right one for the task, which is exactly what prompted me to start benchmarking all the available types. To add extra confusion, some types may come with an older (slower) CPU if you don't set `min_cpu_platform` to the latest available for the type - so you need the extra configuration to get a faster machine for the same price.

This year, we have the addition of the AMD **EPYC Turin** (**c4d** and **n4d**), they are not yet in all regions/zones, but availability is expanding. We also had the introduction of two Intel-based 4th gen instances (**n4** and **c4**). They both feature **Emerald Rapids**, however the latter can be configured with a local SSD, in which case they come with the newer Intel **Granite Rapids**. Until GCP allows setting `min_cpu_platform` to **Granite Rapids** (they are thinking about it AFAIK), you have to pay for the extra SSD to get the performance. Last year [I covered separately](https://dev.to/dkechag/google-axion-a-new-leader-in-arm-server-performance-4im9) the introduction of the Google **Axion** - powered **c4a** ARM type, but it is on a full VM comparison for the first time.

At this point, I should mention that the reason I did more extensive testing this year across different regions is the disappointing performance of **Emerald Rapids** in practice, compared to its showing on my original benchmarks. It seems that as it started to get used, exhibited a performance variance that looks consistent with boost behavior + node contention (i.e. more sensitive to noisy neighbors). I suspect this is why GCP offers the option to turn boost clock off in **Emerald Rapids** instances for "*consistent performance*".

GCP prices vary per region and feature some strange patterns. For example when you reserve, **t2d** instances which give you a full AMD **EPYC** core per vCPU and **n2d** instances which give you a Simultaneous Multi-Thread (i.e. HALF a core) per vCPU have the same price per vCPU, but **n2d** is cheaper on demand and gets a 20% discount for sustained monthly use.

Note that **c3**, **c3d** and **c4-lssd** types have a 4x vCPU minimum. This breaks the price comparison, so I am extrapolating to a 2x vCPU price (half the cost of CPU/RAM + full cost of 30GB SSD). GCP gives you the option to disable cores (you select "visible" cores), so while you have to pay for 4x vCPU minimum, you can still run benchmarks on a 2x vCPU instance for a fair comparison.

### Microsoft Azure

| Instance Type | CPU type | RAM/SSD | Price $/Month | 1Y Res. $/Month | 3Y Res. $/Month | Spot $/Month |
| --- | --- | --- | --- | --- | --- | --- |
| D2as\_v5 (M) | AMD Milan | 8/32 | 65.18 | 39.40 | 26.26 | 15.16 |
| D2ls\_v5 (I) | Intel Ice Lake | 4/32 | 64.45 | 38.98 | 25.98 | 17.37 |
| D2pls\_v5 (A) | Ampere Altra | 4/32 | 52.04 | 31.65 | 21.26 | 11.57 |
| D2pls\_v6 (CO) | Azure Cobalt 100 | 4/32 | 47.66 | 29.07 | 19.59 | 11.18 |
| D2ls\_v6 (E) | Intel Emerald Rapids | 4/32 | 67.59 | 42.82 | 27.82 | 20.04 |
| D2als\_v6 (G) | AMD Genoa | 4/32 | 61.09 | 37.07 | 24.71 | 13.36 |

[Azure](https://azure.microsoft.com/en-gb/) is the #2 overall Cloud provider and, as expected, it's the best choice for most Microsoft/Windows-based solutions. That said, it does offer many types of Linux VMs, with quite similar abilities as **AWS**/**GCP**. The various types are not easy to use as on **AWS**/**GCP** though, for some reason even enterprise accounts start with zero quota on many types, so I had to request quota increases to even test tiny instances.

The v6 instances are new for the comparison, featuring AMD **EPYC Genoa**, Intel **Emerald Rapids** and Azure's own **Cobalt 100** ARM CPU.

The **Azure** pricing is at least as complex as **AWS**/**GCP**, plus the pricing tool seems worse. They also lag behind the other two major providers in CPU releases - **Turin** and **Granite Rapids** are still in closed preview at the time of writing this.

### Oracle Cloud Infrastructure (OCI)

| Instance Type | CPU type | RAM/SSD | Price $/Month | Spot $/Month |
| --- | --- | --- | --- | --- |
| Standard.E6 (T) | AMD Turin | 4/30 | 29.00 | 15.13 |
| Standard.A1 (A) | Ampere Altra | 4/30 | 20.24 | 10.75 |
| Standard.A2 (AO) | Ampere AmpereOne | 4/30 | 17.32 | 17.32 |
| Standard.A4\* (AM) | Ampere AmpereOne M | 4/30 | 19.22 | 10.24 |

\* *Limited availability currently.*

[Oracle Cloud Infrastructure](https://www.oracle.com/cloud/) (**OCI**) was the biggest surprise in my [2023 comparison test](https://dev.to/dkechag/cloud-vm-performance-value-comparison-2023-perl-more-1kpp). It was a pleasant surprise, not only does **Oracle** offer by far the most generous free tier (credits for the **A1** type ARM VM credits equivalent to sustained 4x vCPU, 24GB RAM, 200GB disk for free, forever), their paid ARM instances were the best value across all providers - especially for on-demand. The free resources are enough for quite a few hobby projects - they would cost you well over $100/month in the big-3 providers.

Note that registration is a bit draconian to avoid abuse, make sure you are not on a VPN and also don't use *oracle* anywhere in the email address you use for registration. You start with a "free" account, which gives you access to a limited selection of services and apart from the free-tier eligible **A1** VMs, you'll struggle to build any other types with the free credit you get at the start.

Upgrading to a regular paid account (which still gives you the free tier credits), you get a selection of VMs. New this year are the AMD **EPYC Turin Standard.E6** VMs and the next generation ARM **Standard.A4** type powered by the **AmpereOne M** CPU. If you recall from last year, the **AmpereOne A2** instances were slower in quite a few tasks than the older **Altra A1**. Ampere really needed a step forward, and **AmpereOne M (A4)** finally delivers meaningful gains in this yearâs dataset. I had trouble building older-gen AMD instances, so in the end I did not include them. I also could only build **Standard.A4** in one region (Ashburn), even though I tried in Phoenix which Oracle had in the availability list, to no avail.

**Oracle** Cloud's prices are the same across all regions, which is nice. They do not offer any reserved discounts, but do offer a 50% discount for preemptible (spot) instances. One complication is that their prices are per "Oracle CPU" (OCPU). This seemed to make sense originally, as it corresponded to physical cores - the A1 instances had 1 OCPU per core, so 1 OCPU = 1 vCPU, while SMT x86 had 1 OCPU = 2 vCPU (threads). But then, possibly thinking that their users are getting comfortable with it, they threw a wrench by making 1 OCPU for newer (still non-SMT) ARM types A2 and A4 be equal to 2 vCPU / 2 full Cores. I can't think of a reason for this other than to confuse their customers.

### Akamai (Linode)

| Instance Type | CPU type | RAM/SSD | Price $/Month |
| --- | --- | --- | --- |
| Linode 4GB\* (M) | AMD Milan | 4/80 | 24.00 |
| G7 4x2 (M) | AMD Milan | 4/80 | 43.00 |
| G8 4x2 (T) | AMD Turin | 4/40 | 45.00 |

\* *Shared core.*

[Linode](https://cloud.linode.com/), the venerable cloud provider (predating AWS by several years), has now been part of [Akamai](https://www.akamai.com/solutions/cloud-computing) for a few years.

From the previous years we saw that their shared core types ("Linodes") are the best bang for buck, but it depends on what CPU you are assigned on creation. It seems that currently the most common configuration features an AMD **EPYC Milan**. I tried to build quite a few and that's what you usually get (if you manage to build an ancient Intel or AMD Rome, try again), I did not see any newer CPUs pop up. The latest **EPYC Turin** though is available as a dedicated CPU instance. They now mark dedicated instances with their generation, so a **G8** should always be the same CPU. As always, the dedicated instances come with SMT, so you are normally getting a core per 2 vCPUs, while the shared instances are virtual cores, so twice the vCPUs gives you twice the multi-thread performance - the caveat is that performance per thread varies depending on how busy the node that holds your VM is.

It is a bit of an annoyance that without testing your VM after creation you can't be sure of what performance to expect, unless you go for the more expensive dedicated VMs, but otherwise, Akamai/Linode is still easy to set up and maintain and has fixed, simple pricing across regions.

### DigitalOcean

| Instance Type | CPU type | RAM/SSD | Price $/Month |
| --- | --- | --- | --- |
| Basic 2/4\* (B) | Intel Broadwell | 4/80 | 24.00 |
| PremInt 2/4\* (C) | Intel Cascade L | 4/120 | 32.00 |
| PremAMD 2/4\* (R) | AMD Rome | 4/80 | 28.00 |

\* *Shared core.*

[DigitalOcean](https://m.do.co/c/e23449764852) was close to the top of the perf/value charts a few years ago, providing the best value with their shared CPU **Basic** "droplets". I am actually using DigitalOcean droplets to help out by hosting a free weather service called [7Timer](https://7timer.info/), so feel free to use my [affiliate link](https://m.do.co/c/e23449764852) to sign up and get $200 free - you will help with the free project's hosting costs if you end up using the service beyond the free period. Apart from value, I chose them for the simplicity of setup, deployment, snapshots, backups.

However, they seem to have stopped upgrading their fleet for quite a while now, so you end up with some very old CPUs. If you don't mind the low per-thread performance, they are still not a bad value, given the low prices. I like their simple, region-independent and stable pricing structure, but I wish they would upgrade their shared core data centers.

### Hetzner

| Instance Type | CPU type | RAM/SSD | Price $/Month |
| --- | --- | --- | --- |
| CCX13 (M) | AMD Milan | 8/80 | 17.27 |
| CAX11 (A\*\*)\* | Ampere Altra | 4/40 | 5.46 |
| CPX22 (G\*\*)\* | AMD Genoa | 4/80 | 8.63 |
| CX23 (R\*\*)\* | AMD Rome | 4/40 | 4.31 |
| CX23 (S\*\*)\* | Intel Skylake | 4/40 | 4.31 |

\* *Limited/Eu-only availability.*  
\*\* *Shared core.*

[Hetzner](https://www.hetzner.com/cloud/) is a quite old German data center operator and web host, with a very budget-friendly public cloud offering. They are often recommended as a reliable extra-low-budget solution, and I've had much better luck with them than other similar providers.

On the surface, their prices seem to be just a fraction of those of the larger providers, so I did extended benchmark runs over days to make sure there is no significant oversubscribing - except perhaps the cheapest variant (**CX23**). Only the **CCX13** claims dedicated cores. Ironically, those dedicated instances vary significantly in performance depending on which data center you create them in. In the end, the **CPX22** (AMD) and **CAX11** (ARM) shared core instances are the most stable in performance across instances and regions.

Note that the cheap shared-core types are not widely available, not found in the US regions and they even show no availability at times in the European regions. And while I included a **CX23** with **EPYC Rome**, you will normally get a slower **Skylake**. I will not include the shared instances in the price/performance charts this time around, as I am thinking that the limited availability does not make them equal contenders.

Test setup & Benchmarking methodology
-------------------------------------

In order to have much more test runs, I streamlined the test suite into a docker image [which you can run yourself](https://hub.docker.com/r/dkechag/cloud-bench). Almost all instances were on 64bit **Debian 13**, although I had to use **Ubuntu 24.04** on a couple, and Oracle's ARM were only compatible with **Oracle Linux**. To run the entire suite on a system with docker you would do:

```
docker run -it --rm dkechag/cloud-bench
```

Enter fullscreen mode

Exit fullscreen mode

The suite comprises of:

### Benchmark::DKbench

As every year, the main weight is on my [my own benchmark suite](https://metacpan.org/pod/Benchmark::DKbench), which you can now also run on its [own docker image](https://hub.docker.com/r/dkechag/dkbench). It has both proven very good at approximating real-world performance differences in the type of workloads we use [at SpareRoom](https://www.spareroom.co.uk), and is also good at comparing single and multi-threaded performance (with scaling to hundreds of threads if needed). To run DKbench by itself on a system with docker:

```
docker run -it --rm dkechag/dkbench
```

Enter fullscreen mode

Exit fullscreen mode

I created multiple instances in different regions and recorded min and max of all runs (both single-thread and dual-thread).

### Geekbench 5

I have kept Geekbench, both because it can help you compare results from previous years and because **Geekbench 6** seems to be much worse - especially in multi-threaded testing (I'd go as far to say [it looks broken to me](https://dev.to/dkechag/how-geekbench-6-multicore-is-broken-by-design-44ig)).

I simply kept the best of 2 runs, you can browse the results [here](https://browser.geekbench.com/user/ecuador). There's an Arm version too at <https://cdn.geekbench.com/Geekbench-5.4.0-LinuxARMPreview.tar.gz>.

### Phoronix (openbenchmarking.org)

Apart from being popular, Phoronix benchmarks can help benchmark some specific things (e.g. AVX512 extensions) and also results are [openly available](https://openbenchmarking.org).

I ran the following benchmarks:

```
phoronix-test-suite benchmark compress-7zip
```

Enter fullscreen mode

Exit fullscreen mode

Very common application and very common benchmark - average compression/decompression scores are recorded.

* **nginx 3.0 100 connections**

```
phoronix-test-suite benchmark nginx
```

Enter fullscreen mode

Exit fullscreen mode

Select option 3.

```
phoronix-test-suite benchmark openssl
```

Enter fullscreen mode

Exit fullscreen mode

Select option 1. This benchmark uses SSE/AVX up to AVX512, which might be important for some people. Older CPUs that lack the latest extensions are at a disadvantage.

### FFmpeg / libx264

Blender's [Big Buck Bunny](https://peach.blender.org/) video was transcoded to an H264 mp4 via FFmpeg, both in single and dual-thread mode.

Results
-------

The raw results can be accessed [on this spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vTy4d10zpOxD-VRaSp5Z9-EoljTOaIs8RBCQFSKsIFNwvG2Q2ogHznMIfghm5OwC_A_Abwi-2g74Fkc/pubhtml) (or [here](https://browser.geekbench.com/user/ecuador) for the full Geekbench results).

In the graphs that follow, the y-axis lists the names of the instances, with the CPU type in parenthesis:

```
(GR) = Intel Granite Rapids
(E)  = Intel Emerald Rapids
(SR) = Intel Sapphire Rapids
(I)  = Intel Ice Lake/Cooper Lake
(C)  = Intel Cascade Lake
(S)  = Intel Skylake
(B)  = Intel Broadwell
(T)  = AMD Turin
(G)  = AMD Genoa
(M)  = AMD Milan
(R)  = AMD Rome
(G4) = Amazon Graviton4
(G3) = Amazon Graviton3
(G2) = Amazon Graviton2
(CO) = Azure Cobalt 100
(AM) = Ampere AmpereOne M
(AO) = Ampere AmpereOne
(A)  = Ampere Altra
```

Enter fullscreen mode

Exit fullscreen mode

### Single-thread Performance

Single-thread performance can be crucial for many workloads. If you have highly parallelizable tasks you can add more vCPUs to your deployment, but there are many common types of tasks where that is not always a solution. For example, a web server can be scaled to service any number of requests in parallel, however the vCPU's thread speed determines the minimum response time of each request.

* **DKbench Single-Threaded Performance**

We start with the latest DKbench, running the 19 default benchmarks (Perl & C/XS) which cover a variety of common server workloads. I tried to build 2-3 instances at different times across at least 3 regions (if the provider allowed), to get a min/max range of performance. Here are the results for single thread:

[![Bar Chart comparing single-threaded performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3tkstqiazoc8zuf4m25g.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3tkstqiazoc8zuf4m25g.png)

I think it's the first time in my series of comparisons where a CPU had this clear of a performance lead. AMD's **EPYC Turin** is simply a tier above anything else. **AWS** has the fastest setup with that CPU, while **GCP**âs more expensive **C4d** seems to vary a lot in performance when their own, cheaper **N4d** gave more consistent results. Overall, if you are looking for maximum performance per thread, **EPYC Turin** seems to be the answer if your cloud provider has it.

In the 2024 comparison Intel **Emerald Rapids** did quite well, but it turns out that is only on non-busy nodes, where the cpu allows for a generous boost - at least for **GCP**. This is reflected as the range you see on the graph. The new **Granite Rapids** seems to fix this, providing a bit higher, but mainly more stable performance. So, a solid step forward from Intel, it's just that **Turin** is really impressive.

As we are waiting for **AWS** to release **Graviton5** publicly, **GCP**âs **Axion** is the leader for ARM solutions, impressively offering **EPYC Genoa**-level performance per thread. I tested Azure's own **Cobalt 100** for the first time - it sits between **Graviton3** and **Graviton4** performance. Ampere's new **AmpereOne M** finally offers some tangible improvement over the aging **Altra**, but only matches **AWS**'s older **Graviton3**.

Lastly, among the lower-cost providers, **DigitalOcean** has lagged behind in performance, signaling that their fleet is due for an upgrade. Both **Akamai** and **Hetzner** offer some fast **Milan** instances, although for both providers you are not guaranteed what performance level you are going to get when creating an instance - there is the variation shown in the chart. It's not oversubscribing, the performance is stable, it's just that groups of servers are setup differently.

### Multi-thread Performance & Scalability

DKbench runs the benchmark suite single-threaded and multi-threaded (2 threads in this comparison as we use 2x vCPU instances) and calculates a scalability percentage. The benchmark obviously uses highly parallelizable workloads (if that's not what you are running, you'd have to rely more on the single-thread benchmarking). In the following graph 100% scalability means that if you run 2 parallel threads, they will both run at 100% speed compared to how they would run in isolation. For systems where each vCPU is 1 core (e.g. all ARM systems), or for "shared" CPU systems where each vCPU is a thread among a shared pool, you should expect scalability near 100% - what is running on one vCPU should not affect the other when it comes to CPU-only workloads.

Most Intel/AMD systems though give you a single core that has 2x threads (Hyper-Threads / HT in Intel lingo - or Simultaneous Multi Threads / SMT if you prefer) as a 2x vCPU unit. Those will give you scalability well below 100%. A 50% scalability would mean you have the equivalent of just 1x vCPU, which would be very disappointing. Hence, the farther up you are from 50%, the more performance your 2x vCPUs give you over running on a single vCPU.

[![Bar Chart comparing scalability](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx86k7r4dwsmiib6qsfpg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx86k7r4dwsmiib6qsfpg.png)

As expected, the ARM and shared CPUs are near 100%, i.e. you are getting twice the multithreaded performance going from 1x to 2x vCPUs. You also get that from three x86 types: **AWS's** **Genoa C7a** and **Turin C8a** alongside **GCP's** older **Milan t2d**.

From the rest we note that, traditionally, AMD does SMT better than Intel, although the latter has improved from the dismal **Ice Lake** days when it barely managed over 50%.

Bizarrely, the **Akamai AMD Turin** give an unusually high (given SMT) scalability of 71.9%. I have verified the result several times, and I can't figure out what their setup is - the single-threaded performance at the same time is very low compared to every other **Turin**.

* **DKbench Multi-Threaded Performance**

From the single-thread performance and scalability results we can guess how running DKbench multithreaded will turn out, but in any case here it is:

[![Bar Chart comparing multi-threaded performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Foc9ban68sechvm7ywre2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Foc9ban68sechvm7ywre2.png)

Give the clearly fastest instance two full cores instead of threads and you get the **Turin**-powered **AWS C8a** completely dominating the chart. Interestingly, the **Google Axion** seems at least as good here as the leader from the previous comparison, the **Genoa C7a** - with **Graviton4** very close and **Cobalt 100** trailing not far behind.

The SMT-enabled **Turin** instances follow, with the Top-10 completing with the venerable **Milan** in a non-SMT **Tau** instance. Long time followers of these comparisons may remember this was the top of the chart in the [2023 edition](https://dev.to/dkechag/cloud-vm-performance-value-comparison-2023-perl-more-1kpp).

At the bottom, as expected we have very old Intel **Broadwell/Skylake** not-as-old **Ice Lake** and AMD **Rome**.

The old Geekbench 5 is provided for comparison reasons (and [I don't trust Geekbench 6](https://dev.to/dkechag/how-geekbench-6-multicore-is-broken-by-design-44ig)):

[![Bar Chart comparing Geekbench 5 performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvlospeaqaoismxjeehtg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvlospeaqaoismxjeehtg.png)

Both for single and multi-core, the results are very close to what we get with DKbench. Which is a good thing, as both suites try a range of benchmarks to get a balanced generic CPU score.

Moving on to some popular specific benchmarks - starting with 7zip which is sensitive to memory latency and cache:

[![Bar Chart comparing 7zip performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6355h7vqjhr1ym1cifv2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6355h7vqjhr1ym1cifv2.png)

While **Turin** still leads overall, **Axion** and **Graviton4** are impressive and actually even beat it in the decompress part of the benchmark. In fact, **Cobalt 100** is the top performer for decompression, but overall the ARM solutions show great performance.

Results from the 100 connections benchmark:

[![Bar Chart comparing NGINX performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkx66ymebvas7fhk1ok8y.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkx66ymebvas7fhk1ok8y.png)

Another **Turin** showcase, with the non-SMT **AWS C8a** in particular almost doubling the score of the second and tripling the score of the **C7a**. **Granite Rapids** is also making a great showing.

It's the first time I am running this popular benchmark, and I am a bit puzzled about some of the **Milan** types coming last.

* **FFmpeg H264 Video Compression**

Another first for this comparison is video compression using FFmpeg and libx264. Results for both single and dual-thread mode:

[![Bar Chart comparing FFmpeg performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe9px3ultzdif361lg408.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe9px3ultzdif361lg408.png)

Once more, **EPYC Turin** comes first. If we look at single-thread performance only **Granite Rapids** comes somewhat close. When using 2 full cores **Axion** can pull ahead of all SMT (i.e. single core) instances except **Turin**.

Lastly, in case you have software that can be accelerated by AVX512, I am including an OpenSSL RSA4096 benchmark. They are Intel's extensions so they are on all their CPUs since **Skylake**, whereas **Genoa** was the first AMD CPU to implement them. Older AMD CPUs and ARM architectures will be at a disadvantage in this benchmark:

[![Bar Chart comparing OpenSSL performance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1l4lca3btg9xzgkuhs6p.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1l4lca3btg9xzgkuhs6p.png)

Like in our previous comparison, AMD outperforms Intel at their own game. It's quite a margin for **Turin** and even **Genoa** is ahead of anything Intel. Intel does not seem to be prioritising vector performance, as even the latest **Granite Rapids** does not bring much improvement over the aging **Ice Lake**.

As expected, ARM and older AMD CPUs that don't support AVX512 are slower than Intel **Skylake** and newer.

### Performance / Price (On Demand / Pay As You Go)

One factor that is often even more important than performance itself is the performance-to-price ratio.

I will start with the "on-demand" price quoted by every provider. While I listed monthly costs on the tables, these prices are actually charged per minute or hour, so there's no need to reserve for a full month.

* **DKbench single-thread performance/price**

The first chart is for single-thread performance/price. I will have to separate Hetzner's shared instances because they are not available in the US and sometimes run out even in Europe (esp. **CX23**), so I feel they are not exact competition - **CCX13** though is available and is included.

[![Bar Chart comparing single-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs1l09dc02hj2n4pupg8x.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs1l09dc02hj2n4pupg8x.png)

**Hetzner** and **Oracle** top the list like last year. However, thanks to the incredible performance of **Turin**, **Oracle** pretty much matches **Hetzner's** dedicated instance in performance to cost. They are followed by **Linode** and also **GCP's n4d**. The latter, again thanks to the leading single-thread performance of AMD's latest CPU even manages to bring better value than **DigitalOcean**, which is then followed by in-house ARM solutions like **Google Axion** and **Azure Cobalt 100**.

**AWS** is definitely the worst value on-demand. Their **Turin** is the best they can do, while their previous gen and older CPUs are the worst values on the table. Unlike the previous comparison, even **Azure** seems to do better in value.

At this point I think we should see the limited availability **Hetzner** VMs in comparison to the best value dedicated:

[![Bar Chart comparing Hetzner single-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fezrx436emvt91uu4goa7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fezrx436emvt91uu4goa7.png)

The inexpensive shared-cpu types offer unbeatable value - if you manage to get them. The top one overall (**Rome CX23**) is actually the hardest to provision, as the **CX23** type usually gives you a slow **Skylake**.

* **DKbench multi-thread performance/price**

Moving on to 2x threads for evaluating multi-threaded performance:

[![Bar Chart comparing multi-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhahthezmlwxaafuqx03s.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhahthezmlwxaafuqx03s.png)

All the non-SMT VMs get a bump here, hence **Oracle**'s ARM take the lead with the new **AmpereOne M**, with **Hetzner** and shared core **Linode** following closely. The second tier consists of **Google Axion** and **Azure Cobalt 100**, as well as **DigitalOcean** droplets. **AWS's** non-SMT **Turin** is not that far behind this time, although their older gen 5/6 x86 are again at the very bottom of the chart.

The **Hetzner** shared-core instances get the bump as well, they provide superb on-demand value compared to the competition:

[![Bar Chart comparing Hetzner multi-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmmiipujq0u0fa4f52fgn.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmmiipujq0u0fa4f52fgn.png)

### Performance / Price (1-Year reserved)

The three largest (and most expensive) providers offer significant 1-year reservation discounts. To get the maximum discount you have to lock into a specific VM type, which is why it is extra important to know what you are getting out of each. Also, for **AWS** you can actually automatically apply the 1 year prices to most on-demand instances by using third party services like [DoIT's Flexsave](https://www.doit.com/flexsave/) (included in their free tier!), so this segment may still be relevant even if you don't want to reserve.

* **DKbench single-thread performance/price (1Y)**

The first chart is again for single-thread performance/price.

[![Bar Chart comparing 1Y single-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwccot1ws9h9j9bbj1068.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwccot1ws9h9j9bbj1068.png)

The 1-year discount is enough for **GCP**âs **Turin** to match **Oracle** near the top of the value ranking. On **Azure** you get some good value running **Cobalt 100** or **Genoa**. If you are on **AWS** your best bet are the latest **C8** family.

* **DKbench multi-thread performance/price (1Y)**

Moving on to evaluating multi-threaded performance using 2x vCPUs:

[![Bar Chart comparing 1Y multi-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8twn8sdb3olybbdzqn33.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8twn8sdb3olybbdzqn33.png)

**OCI** ARM instances are still at the top, joined by **Azure Cobalt 100** with **Axion** almost keeping up. This is the first instance where **AWS** can offer similar value, thanks to the **C8a** with the fast **Turin** offering twice the physical cores, making up for the higher price.

### Performance / Price (3-Year reserved)

* **DKbench single-thread performance/price (3Y)**

Finally, for very long term commitments, **AWS**, **GCP** and **Azure** provide 3-year reserved discounts:

[![Bar Chart comparing 3Y single-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3r2akqt9nhb4yvlqgvze.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3r2akqt9nhb4yvlqgvze.png)

**GCP** with its **Turin** instances finally comes just ahead of **Oracle** and even **Hetzner's** dedicated VM. **Azure** also provide good value with their **Cobalt 100** and **Turin** types. It should be noted that even if **AWS** lags behind the other, at a 3 year commitment it still offers better value than the "classic" value providers **Akamai** and **DigitalOcean**.

* **Multi-thread performance/price (3Y)**

Switching to multi-thread, the number of physical cores per vCPU makes the difference:

[![Bar Chart comparing 3Y multi-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxmi0rw6r2pckeb1g92s2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxmi0rw6r2pckeb1g92s2.png)

I didnât expect this, but **Azure Cobalt 100** tops the chart! It is followed by **GCP** and **OCI** ARM solutions, but **AWS's** and **GCP's** **Turin** are not far behind.

### Performance / Price (Spot / Preemptible VMs)

The large providers (**AWS**, **GCP**, **Azure**, **OCI**) offer their spare VM capacity at an - often heavy - discount, with the understanding that these instances can be reclaimed at any time when needed by other customers. This "spot" or "preemptible" VM instance pricing is by far the most cost-effective way to add compute to your cloud. Obviously, it is not applicable to all use cases, but if you have a fault-tolerant workload or can gracefully interrupt your processing and rebuild your server to continue, this might be for you.

**AWS** and **OCI** will give you a 2-minute warning before your instance is terminated. **Azure** and **GCP** will give you 30 seconds, which should still be enough for many use cases (e.g. web servers, batch processing etc).

The discount for **Oracle's** instances is fixed at 50%, but varies wildly for the other providers per region and can change often, so you have to be on top of it to adjust you instance types accordingly.

For a longer discussion on spot instances see [2023's spot performance/price comparison](https://dev.to/dkechag/cloud-provider-price-performance-comparison-spot-vms-for-max-value-jpm). Then you can come back to this year's results below.

* **DKbench single-thread performance/price (Spot)**

Applying the lowest January 2026 US spot prices we get:

[![Bar Chart comparing Spot single-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F628lc9zvmxwgv6w4opcx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F628lc9zvmxwgv6w4opcx.png)

We get that **Oracle's Turin** will always be top value, as it has a fixed spot price. From the big 3, **GCP** and **Azure** offer the deepest discounts (**Genoa** and **Cobalt 100** types), the former getting top place here. If you compare to the 3 year reservation chart, you are getting about twice the performance per dollar. **AWS** is much less generous, if you are on their cloud, **Turin** is once more your best bet. But even with **AWS** you are getting better value if you are using spot instances than other low cost providers.

* **Multi-thread performance/price (Spot)**

The multi-thread chart:

[![Bar Chart comparing Spot multi-threaded performance/price](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fde4xnw2wgwnkx8fln8ys.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fde4xnw2wgwnkx8fln8ys.png)

**Azure's Cobalt 100** tops the chart with **OCI's AmpereOne M** following. Interestingly, in third place and best for the **GCP** cloud, is the aging **t2d Milan** which was noted as a great value in [previous years](https://dev.to/dkechag/cloud-vm-performance-value-comparison-2023-perl-more-1kpp). **AWS** once more has **Turin** saving the day by just making it into the top 10. You can get great value with all providers that offer spot instances, but you do have to monitor prices.

Conclusions
-----------

As always, I [provide all the data](https://docs.google.com/spreadsheets/d/e/2PACX-1vTy4d10zpOxD-VRaSp5Z9-EoljTOaIs8RBCQFSKsIFNwvG2Q2ogHznMIfghm5OwC_A_Abwi-2g74Fkc/pubhtml) so you can draw your own conclusions. If you have highly specialized workloads, you may want to rely less on my benchmarks. However, for most users doing general computing, web services, etc. I'd say you are getting a good idea about what to expect from each VM type. In any case, I'll share my own conclusions, some reasonably objective, others perhaps somewhat subjective.

### Overview

Letâs begin with some quick take-aways, especially for things that are new this year:

* **AMD Turin** is an absolute beast. It's so fast that it's usually a good value even when priced higher.
* **Intel Granite Rapids** is a solid step forward, avoiding the inconsistent performance of its predecessor (**Emerald Rapids**).
* On the ARM side, **Google Axion** shows up as a genuinely high-performance option, while **Azure Cobalt 100** and **Ampere AmpereOne M** add more variety and better value tiers than older ARM offerings.
* **Hetzner** offers amazing value, with **Oracle** following (with a great free tier too).
* From the big-3, **GCP** and **Azure** battle it out in price/performance, when **AWS** is usually more expensive.

### General Tips

* Upgrade to the modern CPU types when possible. Older VMs are slower and tend to be more expensive due to higher operational costs.
* Plan your usage and consider making reservations (3-year preferred) to lower costs where applicable. Remember, you can get free 1y reservation prices through 3rd parties (e.g. [DoIT](https://www.doit.com/flexsave/)) if you are with **AWS**.
* Leverage spot VMs as much as possible. They are essentially the only way the cloud can compete with the cost of buying and running your own servers. Check prices periodically and across all regions that interest you to find the best deals.
* Remember that *vCPUs* are not always comparable: ARM systems and very few x86 systems like **AWS's C8a/C7a** and **GCP's t2d**, provide a full CPU core per vCPU. Most others give you a full core per 2x vCPUs.

### Recommendations per use-case

I'll further comment with my picks for various usage scenarios:

* **Budget solution**: If **Oracle's** free tier is not enough for your project, look at **Hetzner** - especially if you are fine with non-US regions and perhaps limited availability to use the shared-CPU types (preferably **CPX** or **CAX**). However, if you can use spot instances, **Azure** can offer you ARM instances and **Oracle** and **GCP** can offer you either ARM or AMD instances with almost comparable performance/price.
* **Best overall value (performance/price) for non-shared CPU**: If you can't use spot instances (best value) or reserve for 1+ years, **Oracle** pretty much tops the performance/price charts with both ARM and x86 (AMD) options. And the charts do not even include the free 4x **A1** vCPUs that can make a big difference for small projects. If reservations are an option, in the common case of multi-threaded workloads, you can match **OCI** (or even beat it when committing for 3 years) with **Azure Dpls\_v6**, **GCP c4a/n4d** or perhaps **AWS C8a**. If you only care about single threaded performance, look at **GCP n4d/c4d**.
* **Maximum performance**: It's clear that **Turin**-powered VMs from all large providers are on a different level to anything else. The best one performance-wise is the non-SMT **AWS C8a**.

### Summary per cloud provider

Finally, I'll make some comments per provider. Besides, we can't always pick a provider or switch, so we have to try to work with what's available to us.

* **AWS:** They were the top ARM performers in my previous comparisons, but as **Graviton5** is still in private beta, **Google Axion** now leads. However, they offer the fastest compute cloud VMs overall in the **C8a** with non-SMT **EPYC Turin**. That VM family's performance makes **AWS's** traditionally higher prices provide some decent value, especially if you can use spot VMs, or reserve (or use a service like [Flexsave](https://www.doit.com/flexsave/)). Because **AWS** does not discount older gens as deeply as others, the **C8a** is usually the best value even for Spot instances.
* **GCP:** It's pretty clear that you should be on GCP's 4th gen ARM or AMD instances if you care about both performance and value. The **n4d Turin** is the best bet for most cases - in all my tests so far it performs pretty much the same as **c4d** at a lower price. Only if your work load can use all cores on your system, the **Axion c4a** will be a bit better still, but that's about it for standard instances. For spot instances things change per-region and usually previous gen instances will give you the best performance per price. It could be **t2d** or **c3d** like in the tested region, but there are also regions where **c2d** or **n2** (as long as you set `min_cpu_platform="Intel Ice Lake"`) come out ahead.
* **Azure:** Who'd have expected Azure developing in-house ARM CPUs, but here we are and **Cobalt 100** might not be as fast as **Google Axion**, but it's not far behind and it's offered at competitive prices, so you'll get similar - or possibly better for spot instances - value compared to GCP.
* **Oracle:** I definitely recommend Oracle for whoever has small projects where a 4-core ARM VM, which **Oracle** provides for free, covers most of the requirements. Their non-free instances are also very competitive, with their on-demand prices comparable to 1-3 year reservation prices from the "Big 3" (**Oracle** doesn't do reservation discounts), with the best value being the **AmpereOne M A4** and **Turin E6** for ARM and x86 respectively. The **A4** are not yet widely available and if you have a free account you will have further limitations as to what VMs you can provision.
* **Akamai:** The *Linode* shared-CPU instances still offer a good value (second to only Hetzner and Oracle if you only consider on-demand pricing), however you need to build and check each instance to make sure it gets an **EPYC Milan** (4-digit CPU code ending in **3**, check it with `cat /proc/cpuinfo` on Linux), otherwise you might be paying the same for less. In most of my test instances I would indeed get a **Milan** though. At least for dedicated instances you now select a "generation", so basically you pick the CPU. They are not as good value as the **Linodes**, but the **G8** is the best of them in both performance and value, although it's kind of a bizarre **Turin** setup where single-thread performance is on a lower tier than any other provider, but SMT gives a surprisingly (and inexplicable to me) high boost when multi-threading.
* **DigitalOcean:** Although they still provide decent value, they have fallen quite behind **Akamai**, as there have not been any upgrades. In fact, there is quite a bit of over-subscribing, so performance drops lower than usual. I still use their **Premium AMD** shared-cpu instances for projects due to the history of reliability I've had with them, but if I want faster servers I have to look elsewhere, which is a shame. They also have the easiest upgrading an instance from one type to another with one click (as long as the target has at least as much disk space). As with the other lower cost providers, you do not know exactly what performance level a VM will have until you provision it. If you'd want to give them a try, feel free to use my [affiliate link](https://m.do.co/c/e23449764852) to sign up and get $200 in credits while supporting the free weather service [7Timer!](https://www.7timer.info).
* **Hetzner:** I am very suspicious of extreme "budget" cloud providers, but **Hetzner** has many longtime satisfied users. Their reputation seems quite solid - most complains I've read online are from banning people, usually with good reason. Their prices seemed too good to be true, so I suspected oversubscribing. Well, they don't seem to be worse than the likes of **Akamai** or **DigitalOcean**, VMs seemed to perform at reasonably stable performance levels for hours to days at a time, perhaps with the exception of the absolute cheapest, the **CX23**. Interestingly, the dedicated core **CCX13** had more performance fluctuation than the shared-core **CPX22**, as long as that one comes with the fast **EPYC Genoa** I was seeing when testing. Unfortunately, the **CPX22** is available only in eu-central and ap-southeast, but if that's OK with you it is the best value and fastest overall.

Finally, remember that choosing a cloud provider involves considering network costs, fluctuating prices, regional requirements, RAM, storage, and other factors that vary between providers. This comparison will only assist with part of your decision.

**To see the comments or leave new ones, visit [original article on DEV.to](https://dev.to/dkechag/cloud-vm-benchmarks-2026-performance-price-1i1m).**