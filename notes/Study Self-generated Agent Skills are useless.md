---
title: "Study: Self-generated Agent Skills are useless"
url: https://arxiv.org/abs/2602.12670
clipped: 2026-06-17 01:44:07
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Study: Self-generated Agent Skills are useless](https://arxiv.org/abs/2602.12670)

## Digest Summary
SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks is a research paper that proposes a benchmark named SkillsBench for evaluating the performance of agent skills across a variety of tasks. The work appears to be affiliated with Cornell University, as indicated by multiple Cornell logos, and is hosted on arXiv. Supporting visual elements include the arXiv and Cornell logos, a license icon, and logos for BibSonomy and Reddit, suggesting possible data sources or platforms referenced in the study. No additional technical details, methodology, results, or conclusions are provided in the extracted text.

## Discussion Summary
Comments converge on the view that skills generated solely from an LLM’s latent knowledge add little or even harm performance, while human‑curated or hybrid skills markedly improve outcomes. Contributors note that models excel at consuming external procedural information but struggle to create novel, reliable guidance, especially without tool access or research. Many emphasize the need for human‑in‑the‑loop refinement, systematic evaluation, and minimalistic, context‑specific skill design. Some see limited utility for self‑generated skills in capturing tool‑use hints, yet overall sentiment favors curated or collaborative skill creation over purely autonomous generation.

---

## Full Article

[Submitted on 13 Feb 2026 (

[v1](https://arxiv.org/abs/2602.12670v1)

), last revised 14 Jun 2026 (this version, v4)]

Title:SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks
===============================================================================

Authors:[Xiangyi Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+X)

,

[Yimin Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Y)

,

[Wenbo Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+W)

,

[Bingran You](https://arxiv.org/search/cs?searchtype=author&query=You,+B)

,

[Zonglin Di](https://arxiv.org/search/cs?searchtype=author&query=Di,+Z)

,

[Yifeng He](https://arxiv.org/search/cs?searchtype=author&query=He,+Y)

,

[Shenghan Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+S)

,

[Kyoung Whan Choe](https://arxiv.org/search/cs?searchtype=author&query=Choe,+K+W)

,

[Jiankai Sun](https://arxiv.org/search/cs?searchtype=author&query=Sun,+J)

,

[Shuyi Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+S)

,

[Chujun Tao](https://arxiv.org/search/cs?searchtype=author&query=Tao,+C)

,

[Binxu Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+B)

,

[Xuandong Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+X)

,

[Hejia Geng](https://arxiv.org/search/cs?searchtype=author&query=Geng,+H)

,

[Xiaojun Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+X)

,

[Junwei Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+J)

,

[Xiaokun Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+X)

,

[Hanwen Xing](https://arxiv.org/search/cs?searchtype=author&query=Xing,+H)

,

[Yubo Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Y)

,

[Qunhong Zeng](https://arxiv.org/search/cs?searchtype=author&query=Zeng,+Q)

,

[Di Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+D)

,

[Yuanli Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y)

,

[Roey Ben Chaim](https://arxiv.org/search/cs?searchtype=author&query=Chaim,+R+B)

,

[Penghao Jiang](https://arxiv.org/search/cs?searchtype=author&query=Jiang,+P)

,

[Haotian Shen](https://arxiv.org/search/cs?searchtype=author&query=Shen,+H)

,

[Luyang Kong](https://arxiv.org/search/cs?searchtype=author&query=Kong,+L)

,

[Xinyi Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+X)

,

[Runhui Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+R)

,

[Xuanqing Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+X)

,

[Jiachen Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+J)

,

[Xin Lan](https://arxiv.org/search/cs?searchtype=author&query=Lan,+X)

,

[Yueqian Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+Y)

,

[Wengao Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+W)

,

[Junwei He](https://arxiv.org/search/cs?searchtype=author&query=He,+J)

,

[Songlin Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+S)

,

[Yue Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Y)

,

[Yipeng Gao](https://arxiv.org/search/cs?searchtype=author&query=Gao,+Y)

,

[Yijiang Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Y)

,

[Ze Ma](https://arxiv.org/search/cs?searchtype=author&query=Ma,+Z)

,

[Liqiang Jing](https://arxiv.org/search/cs?searchtype=author&query=Jing,+L)

,

[Tianyu Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+T)

,

[Kaixin Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+K)

,

[Yiqi Xue](https://arxiv.org/search/cs?searchtype=author&query=Xue,+Y)

,

[Haoran Lyu](https://arxiv.org/search/cs?searchtype=author&query=Lyu,+H)

,

[Yizhuo He](https://arxiv.org/search/cs?searchtype=author&query=He,+Y)

,

[Yuchen Tian](https://arxiv.org/search/cs?searchtype=author&query=Tian,+Y)

,

[Shutong Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+S)

,

[Bowei Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+B)

,

[Yixuan Gao](https://arxiv.org/search/cs?searchtype=author&query=Gao,+Y)

,

[Bo Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+B)

,

[Litong Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+L)

,

[Sikai Cheng](https://arxiv.org/search/cs?searchtype=author&query=Cheng,+S)

,

[Jiajun Bao](https://arxiv.org/search/cs?searchtype=author&query=Bao,+J)

,

[Shuaicheng Tong](https://arxiv.org/search/cs?searchtype=author&query=Tong,+S)

,

[Shuwen Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+S)

,

[Terry Yue Zhuo](https://arxiv.org/search/cs?searchtype=author&query=Zhuo,+T+Y)

,

[Tinghan Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+T)

,

[Qi Qi](https://arxiv.org/search/cs?searchtype=author&query=Qi,+Q)

,

[Miao Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+M)

,

[Longtai Liao](https://arxiv.org/search/cs?searchtype=author&query=Liao,+L)

,

[Zelin Tan](https://arxiv.org/search/cs?searchtype=author&query=Tan,+Z)

,

[Chang Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+C)

,

[Xilin Tang](https://arxiv.org/search/cs?searchtype=author&query=Tang,+X)

,

[Srinath Tankasala](https://arxiv.org/search/cs?searchtype=author&query=Tankasala,+S)

,

[Boqin Yuan](https://arxiv.org/search/cs?searchtype=author&query=Yuan,+B)

,

[Yaoyao Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+Y)

,

[Jianhong Tu](https://arxiv.org/search/cs?searchtype=author&query=Tu,+J)

,

[Chenguang Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+C)

,

[Yizhou Sun](https://arxiv.org/search/cs?searchtype=author&query=Sun,+Y)

,

[Wei Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+W)

,

[Aaron Taylor](https://arxiv.org/search/cs?searchtype=author&query=Taylor,+A)

,

[Ziyue Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Z)

,

[Changkun Guan](https://arxiv.org/search/cs?searchtype=author&query=Guan,+C)

,

[Zhikang Dong](https://arxiv.org/search/cs?searchtype=author&query=Dong,+Z)

,

[Xinyu Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+X)

,

[Steven Dillmann](https://arxiv.org/search/cs?searchtype=author&query=Dillmann,+S)

,

[Han-chung Lee](https://arxiv.org/search/cs?searchtype=author&query=Lee,+H)

,

[Dawn Song](https://arxiv.org/search/cs?searchtype=author&query=Song,+D)

View a PDF of the paper titled SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks, by Xiangyi Li and 76 other authors

[View PDF](https://arxiv.org/pdf/2602.12670)
[HTML (experimental)](https://arxiv.org/html/2602.12670v4)
> Abstract:Agent Skills are structured packages of procedural knowledge that augment large language model (LLM) agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark whose current inventory contains 87 tasks across 8 domains paired with curated Skills and deterministic verifiers. Our latest aggregate evaluation runs the 87-task benchmark under matched no-Skills and curated-Skills conditions for 18 model-harness configurations. Curated Skills raise the average pass rate from 33.9% to 50.5% (+16.6 percentage points; 25.5% normalized gain), with configuration-level gains ranging from +4.1 to +25.7 pp. Focused Skills with at most three modules outperform larger or exhaustive bundles, and smaller models with Skills can match larger models without them. SkillsBench establishes paired evaluation as the foundation for rigorous measurement of Skill efficacy on agentic, expertise-heavy work.

Submission history
------------------

From: Xiangyi Li [

[view email](https://arxiv.org/show-email/c4ce445a/2602.12670)

]

**[[v1]](https://arxiv.org/abs/2602.12670v1)**

Fri, 13 Feb 2026 07:06:06 UTC (1,366 KB)

**[[v2]](https://arxiv.org/abs/2602.12670v2)**

Sat, 7 Mar 2026 00:51:15 UTC (1,364 KB)

**[[v3]](https://arxiv.org/abs/2602.12670v3)**

Fri, 13 Mar 2026 07:33:01 UTC (1,364 KB)

**[v4]**

Sun, 14 Jun 2026 21:21:07 UTC (1,085 KB)