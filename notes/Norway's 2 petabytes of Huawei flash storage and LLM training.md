---
title: "Norway's 2 petabytes of Huawei flash storage and LLM training"
url: https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910
clipped: 2026-06-17 00:57:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - data storage
  - llm training
  - infrastructure procurement
related:
  - "[[How Claude Code works in large codebases]]"
  - "[[The Eternal Sloptember]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Norway's National Library utilizes 2 petabytes of Huawei flash storage to train regional large language models on historical archives, raising sovereignty and procurement debates.
>
> **Key points:**
> - Describes the National Library of Norway's procurement of 2PB of Huawei storage for digitizing archives and LLM training.
> - Highlights debates over national security, sovereignty, and reliance on Chinese hardware providers.
> - Discusses LLM training on regional datasets to preserve linguistic heritage.
>
> **Concept links:** [[Data Storage]], [[LLM Training]], [[National Security]], [[Digital Preservation]], [[Infrastructure Procurement]]
>
> **Suggested connections:**
> - [[How Claude Code works in large codebases]] — contrasts cloud-based/local AI workloads with physical data infrastructure.
> - [[The Eternal Sloptember]] — discusses the challenges and implications of training and deploying language models.
<!-- ai-summary:end -->

# [Norway's 2 petabytes of Huawei flash storage and LLM training](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910)

## Digest Summary
Norway’s National Library is building a sovereign Norwegian‑language large language model (LLM) to preserve the nation’s cultural heritage. The project, mandated by the Ministry of Culture, leverages the library’s digitized collection—20 PB of unique material stored in a 3‑2‑1 preservation system (≈60 PB total). Data preparation runs on an on‑premises AI pipeline that includes an Nvidia DGX H200, a 384‑core CPU cluster and multiple Huawei OceanStor Dorado all‑flash arrays providing 2 PB of low‑latency storage for ingestion, cleaning, deduplication and formatting. Processed data are then transferred to the national Sigma2 Olivia supercomputer (HPE Cray EX), which hosts 448 GPUs, 64 512 CPU cores and a 5.3 PB CrayClusterStor E1000 system for training. Key challenges identified are: moving petabyte‑scale data from a high‑durability archive to a high‑throughput AI pipeline; lack of standard evaluation tools for a bilingual, dialect‑rich Norwegian LLM; and governance/orchestration across the preservation archive, AI environment, and supercomputer. The initiative highlights Huawei flash storage’s significant role in European AI infrastructure.

## Discussion Summary
The comments express strong skepticism toward Norway’s “sovereign AI” effort, questioning the necessity and feasibility of building a dedicated Norwegian‑language large model. Contributors note that major providers already train on multilingual data, that the announced hardware appears insufficient for full‑scale training, and that the financial and political commitment required is doubtful. While acknowledging the cultural value of localized models, the overall view is that the project is likely a misallocation of resources and may not yield practical benefits.

---

## Full Article

FLASH

Norway’s 2 petabytes of Huawei flash storage and LLM training
=============================================================

Norway’s National Library is developing a large language model (LLM) that understands the Norwegian language and is using 2 PB of Huawei OceanStor Dorado flash storage in its AI training data pipeline.



Marius Husnes, the Head of IT Platform at the library ([Nasjonlbiblioteket](https://www.nb.no/en/)) discussed the project at Huawei’s ID Forum 2026 in Paris, saying that no commercial LLM provider was developing a local (Norwegian) language LLM. He asserted that any country with its own language that did not have a sovereign LLM trained in that language was at a disadvantage as a globally trained, English-speaking LLM would not know about that country’s history, news and culture that was described in the local language.

Norway’s Ministry of Culture tasked the National Library with building a sovereign AI (LLM) as the library has the single largest digital collection of Norwegian books, newspapers, web pages and so forth in the country. Like many state libraries it is entitled to receive copies of every published book and broadcasted content. Its [legal deposit mandate](https://www.nb.no/en/digitizing-at-the-national-library/) in this area extended beyond books, as it was duty-bound to collect and preserve all of Norway’s cultural heritage.

An agreement with Norwegian newspapers permitted LLM training on copyrighted content and, Husnes said: ”No private company has this.”

The library was also well-placed to do this as it had been digitizing its collection since 2005 and had amassed 20 PB of unique data stored in 3-2-1 form (3 copies, 2 media types, 1 off-site), meaning some 60 PB overall. The digitization process for the raw text, sound, moving pictures, still images and web content involved much OCR scanning, and generated a lot of metadata, and also APIs for online access.

The bulk of the data was deposited in a digital disk plus tape archive, a preservation system. Husnes’ task was to get this data to the LLM training system. He said the bottlemeck was not compute; it was data quality, cleaning and pipeline throughput. There were two main processing stages. First there was in-house computation, using an Nvidia DGX H200 system, a 384 core CPU cluster and multiple Huawei [OceanStor Dorado](https://www.blocksandfiles.com/ai-ml/2025/11/03/huaweis-ai-focussed-all-flash-storage/1609725) all-flash arrays, totalling 2 PB of flash capacity. This is low-latency storage for the data pipelines and training preparation.

Husnes - training national LLM.

The pipeline has data ingestion, cleaning, deduplication, format normalization, validation and preparation steps.Once the data has passed through the pipeline it’s sent to Norway’s national supercomputer, the [Sigma2](https://www.sigma2.no/) Olivia system, for the actual training runs. The Olivia system is an HPE Cray Supercomputing EX system, with 448 GPUs and 64,512 CPU cores. It uses a 5.3 PB Cray [ClusterStor](https://www.blocksandfiles.com/ai-ml/2024/05/02/hpe-launches-cost-effective-storage-system-for-hpc-and-ai/1587031) E1000 storage system.

One large problem area has been over-coming two different storage system needs. The 60 PB preservation system is optimized for durability and cost, not fast IO, and has a high read latency, being designed for infrequent access. The AI Pipeline storage is designed for high-throughput, low-latency, parallel data IO. Husnes said he learnt that nobody was talking about the problems involved in moving PB-scale datasets from an archive to, and through, an AI data pipeline system. His team had to find out how to do it themselves.

Husnes - preservation and AI pipeline storage.

The LLM training is ongoing and he finished his talk with a summary of what his team is stll learning about:

* Evaluation - there are no standard evaluation tools to assess a sovereign Norwegian LLM.The language has two written forms, multiple dialects and historical changes. They are building their own evaluation tool on the fly.
* Governance - who controls access to a sovereign LLM? Who decides what it can be used for? These are institutional and political questions with no easy answers.
* Orchestration - making three systems; preservation archive + on-prem AI environment + national Sigma2 supercomputer, work smoothly together is an ongoing project.

Our takeaways here are, one, that Huawei storage is playing a serious and significant role in the European market, and two, that any country developing a sovereign, local language LLM would do well to consult with Husnes and get acquainted with what’s involved.

As Husnes put it; Norway is a small country solving a problem every non-English-speaking nation will face: how do you build AI that reflects your language, your culture and your history? AI needs custodians, not just builders.