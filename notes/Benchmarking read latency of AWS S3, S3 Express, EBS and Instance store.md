---
title: "Benchmarking read latency of AWS S3, S3 Express, EBS and Instance store"
source: "https://nixiesearch.substack.com/p/benchmarking-read-latency-of-aws"
author:
  - "[[Roman Grebennikov]]"
published: 2025-12-01
created: 2026-06-01
description: "Slow S3 access latency is a well known fact, but how slow, exactly? We compared read latency across different storage systems in AWS and found out that water is wet, sky is blue, and S3 is slow."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - AWS
  - Storage Hierarchy
  - Search Engine
  - Cloud Infrastructure
  - Latency Benchmarking
related:
  - "AWS"
  - "How flat is replacing fat in AWS data center networks.md"
  - "tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A comparative performance benchmark of AWS storage tiers (S3, S3 Express, EBS gp3, and NVMe Instance Store) analyzing read latency for low-latency search engine workloads.
>
> **Key points:**
> - Standard S3 exhibits p99 read latencies in the 100+ ms range, making direct search index queries unviable for high-performance requirements.
> - S3 Express (Directory Buckets) offers significantly lower latency than standard S3 but remains 5–10× slower than EBS gp3 block storage.
> - S3 Express exhibits a notable warm-up latency trend, improving over time under sustained request load due to AWS-side caching and resource scaling.
> - Scaling EC2 instance sizes increases network throughput via faster network interfaces (ENI) but does not improve per-request S3 read latency.
>
> **Concept links:** [[AWS]], [[Storage Hierarchy]], [[Search Engine]], [[Cloud Infrastructure]], [[Latency Benchmarking]]
>
> **Suggested connections:**
> - [[How flat is replacing fat in AWS data center networks.md]] — connects storage latency and networking constraints within the AWS ecosystem.
> - [[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]] — another search engine design discussion, focused on local-first vs cloud-first indexing.
<!-- ai-summary:end -->

I’m building [Nixiesearch](https://github.com/nixiesearch/nixiesearch), a S3-based search engine - think Elasticsearch, but without the operational nightmares. I often end up arguing with strangers online that while “decoupling storage and compute” sounds amazing in theory, in practice it’s a massive pain in the ass for low-latency workloads.

Running Lucene on top of s3 works well at small scales. The latency in your posts is a bit optimistic. I had seen p99 S3 latencies on the order of low 100s of ms. **At those latencies querying directly from s3 is not a winning strategy.**

As of Nixiesearch 0.8, we use S3 only for good old segment replication:

![](https://substackcdn.com/image/fetch/$s_!X83y!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f94763e-3f16-4360-9b25-43d05d0e424f_2276x820.png)

Segment replication. Similar to what OpenSearch/Elasticsearch are doing.

The actual search happens locally over index cached on and EBS volume.

If your index is under ~1M documents, this approach is fine. I even ran a LinkedIn poll across my bubble and learned that such tiny indexes are rare in the real world.

![](https://substackcdn.com/image/fetch/$s_!7EdT!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09557be9-5ee4-4942-8148-023d07a2814b_539x295.png)

10M-100M docs is the most popular index size, which was quite surprising.

The problem with this approach is that for big 100M indexes is that the initial index sync might take ages:

- S3 throughput depends on your instance’s network interface, [which is ~10 Gbit/s for most modern instance types.](https://docs.aws.amazon.com/ec2/latest/instancetypes/gp.html#general-purpose-network-performance)
- A single document with 1024-dim embeddings and byte quantization is ~1 KB. So 100M documents produce a chunky 100 GB index.
- Result: welcome to 100+ seconds of cold-start sync time.

“Why do you even care about initial sync?” you might ask. “Just run a fixed-size cluster 24/7 and forget about cold starts.” Because then you lose the ability to rapidly autoscale.

Elasticsearch is actually not that elastic.

![](https://substackcdn.com/image/fetch/$s_!9u10!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1999436-792a-4aa5-b982-058510b7a09c_2276x820.png)

In a perfect world you just search directly over S3 without doing initial sync, but only if you can eat the access latency.

So let’s benchmark and see how bad it is.

## Methodology

We focus on four storage options:

- **Regular S3 buckets**: regional, standard latency.
- **S3 Directory (S3 Express) buckets**: much lower latency but restricted to a single AZ.
- **EBS gp3 volumes**: typical EC2 block storage.
- **Instance store NVMe**: ephemeral but theoretically much faster.

For benchmarking, I wrote a tiny [s3bench](https://github.com/nixiesearch/s3bench/) tool that:

- Uses JVM NIO and O\_DIRECT for EBS/local reads to bypass filesystem caching.
- Uses raw S3 REST `GetObject` calls instead of the AWS SDK for more control over request behavior.

We run the benchmark on EC2 instances of various sizes within the same region/AZ.

The workload is going to mimic an access pattern of a search request: a lot of random reads of 4kb blocks grouped in small bursts:

![](https://substackcdn.com/image/fetch/$s_!6d3H!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28a5683a-dec5-4642-924c-6803497bf936_2334x885.png)

HNSW index traversal access pattern

## Results

After running the benchmark over S3, S3 Express, EBS gp3 and instance store on a m5id.large instance, we got these numbers:

![](https://substackcdn.com/image/fetch/$s_!MZC2!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F028f0020-073d-4a62-a185-75224b0ebd62_793x176.png)

read latency, milliseconds.

Key observations from a search-engine perspective:

- Yes, running search directly on S3 is painfully slow thanks to enormous 100+ ms p99 tail latency.
- S3 Express is **much, much** faster than standard S3, but still 5–10× slower than EBS.

But does read latency depends on instance size? Can we make it better with more expensive EC2 node?

![](https://substackcdn.com/image/fetch/$s_!rNyI!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd48f3ad-bd2f-4275-b03b-bd256b5c9f62_824x412.png)

S3 read latencies across different EC2 instances.

Looks like a hard no. You only get better throughput thanks to a faster ENI, not better per-request latency.

Another interesting observation for S3 Express endpoints that there’s a clear warm-up trend in latency:

![](https://substackcdn.com/image/fetch/$s_!i89T!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd852d85-8b05-4383-8d96-ed88a23e8569_787x485.png)

S3 Express latency over time.

You can clearly see that the more requests you send, the better latency you get due to caching and autoscaling inside the S3 itself.

## Final words

I still think it’s possible to run search over S3-hosted indexes within a reasonable latency budget:

- In practice, a cold search request needs ~5–10 round trips to S3.
- If each round trip is ~5 ms, you’re looking at ~50 ms overall latency - which is perfectly acceptable for many workloads.

Yes, S3 Express is more fragile from a reliability standpoint, and you’ll need to configure your indexer to publish to multiple S3 Express buckets to survive AZ outages.

But with the right setup, search-over-S3 can absolutely work.