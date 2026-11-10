---
title: "What Is Apache Kafka®? Architecture, Use Cases, and How It Works"
source: "https://www.confluent.io/what-is-apache-kafka/"
author:
published:
created: 2026-05-31
description: "Apache Kafka® is an open source distributed event streaming platform used to publish, store, and process real-time data streams. Learn how Kafka works, its architecture, and common use cases."
tags:
  - "clippings"
processed: true
processed_at: 2026-05-31
summary_status: done
concepts:
  - event streaming
  - distributed systems
  - message brokers
  - data pipelines
  - event-driven architecture
related:
  - "[[Comparing Message Queues and Message Brokers Understanding the Differences]]"
  - "[[RAFT vs. KRAFT]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Apache Kafka is an open-source distributed event streaming platform designed for high-throughput, fault-tolerant, and horizontally scalable real-time data streaming and storage.
>
> **Key points:**
> - Originally developed at LinkedIn, Kafka evolved from a messaging queue into a complete event streaming system that runs as a distributed cluster of brokers.
> - It utilizes an ordered, durable, and partitioned log model where producers publish events to topics, and consumers pull records independently using self-managed offsets.
> - Kafka delivers low latency (~2ms) and high availability, making it ideal for event-driven microservices, data pipelines, and real-time streaming ETL/analytics.
> - Confluent (founded by Kafka's creators) provides a fully managed, cloud-native distribution that simplifies scaling and operations without infrastructure overhead.
>
> **Concept links:** [[Event Streaming]], [[Distributed Systems]], [[Message Brokers]], [[Data Pipelines]], [[Event-Driven Architecture]]
>
> **Suggested connections:**
> - [[Comparing Message Queues and Message Brokers Understanding the Differences]] — Explains how Kafka's persistent commit log and consumer-controlled offsets differ from traditional task queues.
> - [[RAFT vs. KRAFT]] — Details how Kafka has shifted from ZooKeeper to its own Raft-based consensus protocol (KRaft) for distributed metadata management.
<!-- ai-summary:end -->

## What Is Apache Kafka®?

Apache Kafka is an open source distributed system used to publish, subscribe to, store, and process [streams of events](https://www.confluent.io/learn/event-streaming/) or records in real time.

Originally created to handle real-time data feeds at LinkedIn, Kafka quickly evolved from a messaging queue to a powerful event streaming system, capable of handling over one million messages per second or trillions of messages per day.

It is designed for [high throughput](https://www.confluent.io/blog/scaling-kafka-streams/), fault tolerance, and [horizontal scalability](https://www.confluent.io/learn/horizontal-vs-vertical-scaling-kafka/), and is commonly used for [building real-time data pipelines](https://www.confluent.io/learn/build-streaming-data-pipelines/) and [event-driven applications](https://www.confluent.io/learn/event-driven-architecture/). Learn how its inherent scalability and reliability is transforming modern applications, analytics, and AI.

![Rise of Kafka](https://images.ctfassets.net/8vofjvai1hpv/5AdHQjlfro7CvJtvMMexd5/c38d2749aeba2210a7c90654b13ff918/what-is-kafka-header.png?w=1382&h=778&q=90&fm=webp&bg=transparent)

## Apache Kafka® in 60 Seconds

**Definition**: Apache Kafka is an open source event streaming system maintained by the Apache Software Foundation.

Originally developed at LinkedIn and later donated to the [Apache Software Foundation](https://en.wikipedia.org/wiki/The_Apache_Software_Foundation), Kafka is written in Java and runs as distributed clusters across multiple servers.

- **Type:** Distributed event streaming platform
- **Primary function:** Publish, store, process, and replay event streams
- **Core components:** Producers, Consumers, Topics, Brokers, Partitions
- **Common use cases:** Data pipelines, stream processing, microservices integration, event-driven systems
- **Language:** Java (clients available in many languages)
![](https://www.youtube.com/watch?v=hyfX3_RB5cw)

### A Timeline: The History of Kafka

**2010 – Developed at LinkedIn**

**2011 – Open sourced**

**2012 – Donated to Apache Software Foundation**

**2015+ Rapid ecosystem expansion (Kafka Streams, Kafka Connect, cloud services)**

How did Kafka go from LinkedIn → ASF → ecosystem growth in just 5 years? Its unique capabilities solving massive-scale data challenges and quickly established it as de facto standard for distributed event streaming.

## Why Kafka?

Kafka has numerous advantages. Today, developers and architects use Kafka to build the newest generation of scalable, real-time data streaming applications and pipelines.

While these can be achieved with a range of technologies available in the market, below are the main reasons Kafka is so popular:

### High Throughput

Kafka is capable of handling high-velocity and high-volume data, processing [millions of messages](https://developer.confluent.io/podcast/handling-2-million-apache-kafka-messages-per-second-at-honeycomb/?session_ref=direct) per second. This makes it ideal for applications requiring real-time data processing and integration across multiple servers.

### High Scalability

Kafka clusters can be scaled up to a thousand brokers, handling trillions of messages per day and petabytes of data. Kafka's partitioned log model allows for elastic expansion and contraction of storage and processing capacities. This scalability ensures that Kafka can support a vast array of data sources and streams.

### Low Latency

Kafka can deliver a high volume of messages using a cluster of machines with latencies as low as 2ms. This low latency is crucial for applications that require real-time data processing and immediate responses to data streams.

### Permanent Storage

Kafka safely and securely stores streams of data in a distributed, durable, and fault-tolerant cluster. This ensures that data records are reliably stored and can be accessed even in the event of server failure. The partitioned log model further enhances Kafka's ability to manage data streams and provide exactly-once processing guarantees.

### High Availability

Kafka can extend clusters efficiently over availability zones, or connect clusters across geographic regions. This high availability makes Kafka fault-tolerant with no risk of data loss. Kafka’s design allows it to manage multiple subscribers and external stream processing systems seamlessly.

[Benchmarking RabbitMQ vs Kafka vs Pulsar](https://www.confluent.io/blog/kafka-fastest-messaging-system/?session_ref=direct)

### Is Apache Kafka a Message Queue?

Apache Kafka is often compared to traditional message queues like [RabbitMQ](https://www.confluent.io/learn/rabbitmq/) or [ActiveMQ](https://www.confluent.io/hub/confluentinc/kafka-connect-activemq).

However, Kafka differs in key ways:

- Kafka retains messages for a configurable period (or indefinitely).
- Consumers control their own offset position.
- Kafka is optimized for high-throughput distributed streaming rather than simple task queues.

**Queues for Kafka – Messaging and Streaming Converge**

Many organizations use both Apache Kafka for high-throughput streaming and traditional [message queues](https://www.confluent.io/learn/message-broker-vs-queue/) for task distribution and job processing. But this dual-estate approach creates operational overhead that doesn’t come cheap.

Queues for Kafka introduces two main capabilities to Kafka:

- Multiple consumers can cooperatively process messages from the same topic
- Developers can code in Kafka like it’s a task queue

Learn how this can help organizations [consolidate messaging infrastructure](https://www.confluent.io/blog/kafka-queue-semantics-share-consumer-ga/).

## How Does Apache Kafka Work?

Kafka consists of a storage layer and a compute layer, which enable efficient, real-time data ingestion, streaming data pipelines, and storage across distributed systems. It stores records durably on disk and replicates data across brokers to ensure fault tolerance. [Its distributed, client-server architecture](https://developer.confluent.io/courses/architecture/get-started/) includes:

- ### Clusters and Brokers:
	1. Groups of Kafka servers that store and manage data.
- ### Topics:
	- Named streams of records.
		- Events streamed to a topic are partitioned (i.e., divided and stored across brokers and clusters) and replicated.
- ### Partitions
	- Ordered, immutable sequences of records.
- ### Client Applications:
	- Producers publish records to Kafka topics.
		- Consumers consume records from Kakfa topics.
- ### Consumer Groups:
- - Sets of independent, cooperating consumer applications that share a common identifier (e.g., group.id)

This design facilitates simplified data streaming between Kafka and external systems, so you can easily manage real-time data and scale within any type of infrastructure.

| **Real-Time Processing at Scale** | **Durable, Persistent Storage** | **Publish + Subscribe** |
| --- | --- | --- |
| A data streaming platform would not be complete without the ability to process and analyze data as soon as it's generated. The Kafka Streams API is a powerful, lightweight library that allows for on-the-fly processing, letting you aggregate, create windowing parameters, perform joins of data within a stream, and more. It is built as a Java application on top of Kafka, which maintains workflow continuity without requiring extra clusters to manage. | Kafka provides durable storage by abstracting the distributed commit log commonly found in distributed databases. This makes Kafka capable of acting as a “source of truth,” able to distribute data across multiple nodes for a highly available deployment, whether within a single data center or across multiple availability zones. This durable and persistent storage ensures data integrity and reliability, even during server failures. | Kafka features a humble, immutable commit log. Users can subscribe to it, and publish data to any number of systems or real-time applications. Unlike traditional messaging queues, Kafka is a highly scalable, fault-tolerant distributed system. This allows Kafka to scale from individual applications to company-wide deployments. For example, Kafka is used to manage passenger and driver matching at Uber, provide real-time analytics and predictive maintenance for British Gas' smart home, and perform numerous real-time services across all of LinkedIn. |

## What Is Kafka Used For?

Commonly used to build real-time streaming data pipelines and real-time streaming applications, Kafka supports a vast array of use cases. Any company that relies on, or works with data, can find numerous benefits in utilizing Kafka.

### Data Pipelines

In the context of Apache Kafka, a streaming data pipeline means ingesting the data from sources into Kafka as it’s created, and then streaming that data from Kafka to one or more targets. This allows for seamless data integration and efficient data flow across different systems.

### Stream Processing

Stream processing includes operations like filters, joins, maps, aggregations, and other transformations that enterprises leverage to power many use cases. Kafka Streams, a stream processing library built for Apache Kafka, enables enterprises to process data in real-time, making it ideal for applications requiring immediate data processing and analysis.

### Streaming Analytics

Kafka provides high throughput event delivery. When combined with open-source technologies such as Druid, it can form a powerful Streaming Analytics Manager (SAM). Druid consumes streaming data from Kafka to enable analytical queries. Events are first loaded into Kafka, where they are buffered in Kafka brokers, then they are consumed by Druid real-time workers. This allows for real-time analytics and decision-making.

### Streaming ETL

Real-time ETL with Kafka combines different components and features such as Kafka Connect source and sink connectors, used to consume and produce data from/to any other database, application, or API; Single Message Transforms (SMT)—an optional Kafka Connect feature; and Kafka Streams for continuous data processing in real-time at scale. Altogether they ensure efficient data transformation and integration.

### Event-Driven Microservices

Apache Kafka is the most popular tool for [event-driven microservices](https://www.confluent.io/use-case/event-driven-microservices-communication/) because it solves many issues related to microservices orchestration, while enabling attributes that microservices aim to achieve, such as scalability, efficiency, and speed. Kafka also facilitates inter-service communication, preserving ultra-low latency and fault tolerance. This makes it essential for building robust and scalable microservices architectures.

By using Kafka's capabilities, organizations can build highly efficient data pipelines, process streams of data in real time, perform advanced analytics, and develop scalable microservices—all ensuring they can meet the demands of modern data-driven applications.

## Apache Kafka in Action

![](https://images.ctfassets.net/8vofjvai1hpv/4SLkmj6QrpolaVpL0c0bVX/0441ec6dad62ee7c40559653ae9aaec1/kafka_keyword_diagram.svg)

![](https://www.youtube.com/watch?v=9CrlA0Wasvk)

## Who Uses Kafka?

Some of the world’s biggest brands use Kafka:

| ![Airbnb logo](https://images.ctfassets.net/8vofjvai1hpv/mlUnrhHfKG0MQXg4x7Ymq/4f51c522d475d1463832c608d502dd8c/airbnb.png?w=159&h=50&q=100&fm=png&bg=transparent) | ![Netflix](https://images.ctfassets.net/8vofjvai1hpv/4MagiEidg7Q1m3cMjzfn89/de653e49bb8a5abf70e2f1b1e33219c9/netflix.png?w=151&h=41&q=100&fm=png&bg=transparent) |
| --- | --- |
| ![Goldman Sachs](https://images.ctfassets.net/8vofjvai1hpv/1sekmib2IQEjJ8Y2mYtrza/dfc1cd91f668ea867c897fca66a45453/goldman.png?w=127&h=52&q=100&fm=png&bg=transparent) | ![Linkedin](https://images.ctfassets.net/8vofjvai1hpv/43l4dxuf1ok0uKQ4T55D17/56ad5de3268ed9c22f40e369c6cf13d0/linkedin.png?w=152&h=40&q=100&fm=png&bg=transparent) |
| ![Microsoft](https://images.ctfassets.net/8vofjvai1hpv/2AuhukvC1L60LTYbu1ObXK/50593789bf1b4a89b07dd130d71f283f/microsoft.png?w=153&h=33&q=100&fm=png&bg=transparent) | ![New York Times](https://images.ctfassets.net/8vofjvai1hpv/5PSvMApKs6XbsdAOr69D8u/68335b347398f2dd3db239bb333fb4e4/nyt.png?w=76&h=62&q=100&fm=png&bg=transparent) |
| ![Intuit](https://images.ctfassets.net/8vofjvai1hpv/3F8tYKcfHkItqfKEsAZfj1/d1e45bd08b7fd5cc2022f659af147884/intuit.png?w=124&h=37&q=100&fm=png&bg=transparent) |  |

### How Does Confluent Relate to Kafka?

Founded by the original developers of Kafka, Confluent delivers the most complete [distribution of Kafka](https://www.confluent.io/compare/apache-kafka-vs-confluent/), improving Kafka with additional community and commercial features designed to enhance the streaming experience of both operators and developers in production, at massive scale.

If you love Kafka but not managing it, Confluent's data streaming platform goes beyond Kafka so that your best people can focus on delivering value to your business.

### Cloud-Native

We’ve re-engineered Kafka to provide a best-in-class cloud experience, for any scale, without the operational overhead of infrastructure management. Confluent offers the only truly [cloud-native experience for Kafka](https://www.confluent.io/confluent-cloud/kora/) —delivering the serverless, elastic, cost-effective, highly available, and self-serve experience that developers expect.

### Complete

Creating and maintaining real-time applications requires more than just open-source software and access to scalable cloud infrastructure. Confluent makes Kafka enterprise-ready and provides customers with the complete set of tools they need to build apps quickly, reliably, and securely. Our fully managed features come ready out of the box, for every use case from proof of concept (POC) to production.

### Everywhere

Distributed, complex data architectures can deliver the scale, reliability, and performance to unlock previously unthinkable use cases, but they're incredibly complex to run. Confluent's complete, multi-cloud data streaming platform makes it easy to get data in and out of Kafka with Connect, manage the structure of data using Confluent Schema Registry, and process it in real time using Apache Flink or Kafka Streams. Confluent meets customers wherever they need to be—powering and uniting real-time data across regions, clouds, and on-premises environments.

## Get Started With Apache Kafka in Minutes

You can [download Kafka and run it yourself](https://developer.confluent.io/quickstart/kafka-local/), or use a [fully managed Kafka service](https://www.confluent.io/learn/kafka-serverless/) such as Confluent Cloud.

By integrating historical and real-time data into a single source of truth, Confluent makes it easy to build an entirely new category of modern, event-driven applications, gain a universal data pipeline, and unlock powerful new use cases with full scalability, security, and performance. Try Confluent for free with $400 in free credits to spend during your first four months.

[Get Started](https://www.confluent.io/get-started/)

### Frequently Asked Questions About Apache Kafka

### What problem does Apache Kafka solve?

Apache Kafka solves the challenge of reliably moving and processing large volumes of data between systems in real time.

### Is Apache Kafka a database?

No. Kafka is not a traditional database. It is a distributed log system designed to store event streams temporarily or long-term for processing.

### Is Apache Kafka hard to learn?

Kafka concepts like topics and partitions are straightforward, but operating clusters at scale requires distributed systems knowledge.

### What language is Apache Kafka written in?

Apache Kafka is written in Java and Scala.

### Who uses Apache Kafka?

Kafka is used by thousands of organizations worldwide, including large enterprises and digital-native companies building real-time systems.

### What is the difference between Apache Kafka and Confluent?

Apache Kafka is the open source project. Confluent provides enterprise features, cloud services, governance, and managed infrastructure in a data platform built around Kafka.