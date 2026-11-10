---
title: "RAFT vs. KRAFT"
source: "https://medium.com/memphis-dev/raft-vs-kraft-45587fe8a898"
author:
  - "[[Elchin Gasimov]]"
published: 2022-12-28
created: 2026-05-31
description: "In this article, we will look at the difference between RAFT - the widely known consensus algorithm and KRAFT— which Confluent developed to"
tags:
  - "clippings"
processed: true
processed_at: 2026-05-31
summary_status: done
concepts:
  - consensus algorithms
  - log replication
  - distributed systems
  - metadata replication
  - push vs pull model
related:
  - "[[Consensus Algorithms]]"
  - "[[Distributed Systems]]"
  - "[[Message Brokers]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** This article compares the traditional push-based Raft consensus algorithm with Confluent's pull-based KRaft (Kafka Raft) variation used to manage Kafka metadata without ZooKeeper.
>
> **Key points:**
> - Raft maintains consensus using a leader-based push model for leader election, log replication, and safety.
> - KRaft modifies Raft by using a pull-based log replication model, matching Kafka's default broker-to-controller architecture.
> - KRaft's pull model scales better and prevents consumer backpressure, but can consume CPU cycles due to periodic polling.
> - Raft's push model ensures real-time consistency but can struggle with consumers of varying processing capacities.
> - Both algorithms are widely used for metadata coordination and message queue durability, such as in Memphis, RabbitMQ, and Kafka.
>
> **Concept links:** [[Consensus Algorithms]], [[Log Replication]], [[Distributed Systems]], [[Metadata Replication]], [[Push vs Pull Model]]
>
> **Suggested connections:**
> - [[Consensus Algorithms]] — consensus algorithms for distributed state synchronization.
> - [[Distributed Systems]] — engineering concepts for scaling, replication, and consensus.
> - [[Message Brokers]] — systems that utilize consensus algorithms for fault-tolerant queue coordination.
<!-- ai-summary:end -->

In this article, we will look at the difference between **RAFT -** the widely known consensus algorithm and **KRAFT** — which Confluent developed to remove Kafka’s dependency on Zookeeper.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KPvHsdBjFmdqRj5V5P9l9Q.jpeg)

Before going into the differences, let’s learn what RAFT is and how it is used.

**RAFT** is a consensus algorithm for managing a replicated log.

We have several options to consider when designing replicated log mechanisms in distributed systems.

Given a leaderless approach, quorums are used for reading and writing to achieve consistency.  
Given the leader-based approach, consensus algorithms like RAFT and Paxos can be used to achieve consistency.

RAFT decomposes the consensus problem into three relatively independent subproblems:

**1\. Leader election:** a new leader must be chosen when an existing leader fails.

**2\. Log replication:** the leader must accept log entries from clients and replicate them across the cluster, forcing the other logs to agree with its own push-based model.

**3\. Safety:** the key safety property for Raft is the State Machine Safety Property. if any server has applied a particular log entry to its state machine, then no other server may apply a different command for the same log index.

Raft implements consensus by first electing a distinguished leader, then giving the leader complete responsibility for managing the replicated log.  
The leader accepts log entries from clients, replicates them on other servers(push-based model), and tells servers when it is safe to apply log entries to their state machines.  
Having a leader simplifies the management of the replicated log.

For example, the leader can decide where to place new entries in the log without consulting other servers, and data flows in a simple fashion from the leader to other servers.  
A leader can fail or become disconnected from the other servers, in which case a new leader is elected.

KRAFT — is the Kafka version of RAFT algorithm proposed to replicate metadata changes(event sourced) from controllers to brokers.

Its difference from the standard Raft algorithm is the **Log replication part.**

In KRAFT, metadata changes are pulled from active controllers and stored in memory as well as on the disk of the broker. Brokers periodically pull metadata changes from controllers and apply them to their own local storage.

When we look at Kafka’s internal architecture, it can obviously be seen that the pull-based approach is already used in data replication — follower brokers pulling data changes from leader brokers.

To follow the default used architecture, Kafka made changes in the Log-replication part of RAFT to implement metadata changes replication so that metadata changes are pulled from the active controller by the brokers rather than the controller pushing the metadata changes to the brokers.

To summarize, RAFT — is based on a **push** model where the leader takes the responsibility to keep track of the next index, match the index of all the followers, and drive the replication process across the cluster. This is also the standard RAFT algorithm that is **push-based**, where the leader pushes changes to followers.

## Get Elchin Gasimov’s stories in your inbox

Join Medium for free to get updates from this writer.

Kafka’s RAFT uses a **pull-based** model where brokers pull metadata changes from the active controller to follow its default architecture.

## Conclusion

Let’s understand what are the pros and cons of each algorithm.

**Pull-based model (aka KRAFT)**

- Pro: Scalability — Being pull-based model,reduce strain on the leader to push data to followers (aka replicas).
- Pro: Consumers can more effectively control the rate of their individual consumption, having such control enables them to prevent back pressure.
- Con: Resource consuming — Consumers are polling data while there is no available data and therefore a waste of CPU cycles.

**Push-based model (aka RAFT)**

- Pro: Consistency — Getting data whenever created in real-time manner.
- Con: Different consumers can have diverse requirements and capabilities so that back pressure can happen.

Do not forget that there is no silver bullet in the system design, each system designer should consider the used model based on the system’s own requirements and needs.

## Summary

Modern distributed systems(message brokers, databases) rely on RAFT or its variations for leader election, log replication, and safety.

Memphis uses RAFT to maintain data coordination between brokers such as configuration, location, data, and status information.

RabbitMQ uses RAFT to implement durable, replicated FIFO queues.

On the other hand, there are also other systems that use a variation of RAFT based on their needs or due to architectural, and scalability reasons.

Kafka created and uses a pull-based variation of RAFT (namely, KRAFT) to maintain its metadata changes.

Do not forget that there is no silver bullet for all systems. Architects should consider the chosen algorithm based on their system’s requirements and needs.

## References:

[Designing Data-Intensive Applications / Martin Keppmann](https://dataintensive.net/)  
[Distributed Systems University of Cambridge Computer Science Tripos, Part IB Michaelmas term 2021/22 / Dr. Martin Kleppmann](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/dist-sys-notes.pdf)  
[Concluent — KIP-500](https://cwiki.apache.org/confluence/display/KAFKA/KIP-500%3A+Replace+ZooKeeper+with+a+Self-Managed+Metadata+Quorum)  
[Kafka with Raft](https://www.youtube.com/watch?v=5tp3NMW7GzA)  
[Distributed systems: RAFT](https://www.youtube.com/watch?v=uXEYuDwm7e4&list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB&index=19)  
[RAFT-In Search of Understandable Consensus algorithm](https://raft.github.io/raft.pdf)