---
title: "Active-Active geo-distribution"
source: "https://redis.io/active-active/"
author:
  - "[[Redis]]"
published: 2025-06-19
created: 2026-06-11
description: "Developers love Redis. Unlock the full potential of the Redis database with Redis Enterprise and start building blazing fast apps."
tags:
  - "clippings"
processed: true
processed_at: 2026-06-16
summary_status: done
concepts:
  - Distributed Systems
  - CRDT
  - Data Replication
  - Strong Eventual Consistency
  - Vector Clocks
related:
  - "[[MemoryDB Multi-Region - Amazon MemoryDB.md]]"
  - "[[RAFT vs. KRAFT.md]]"
  - "[[Valkey Managing Connection Storms in Valkey at Scale.md]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An overview of Redis Enterprise's CRDT-based Active-Active architecture, enabling local read/write latency and conflict-free data synchronization across geographically distributed clusters.
>
> **Key points:**
> - Active-Active architecture achieves low latency and region isolation by using Conflict-Free Replicated Data Types (CRDTs) to construct Conflict-Free Replicated Databases (CRDBs).
> - Operations are split into prepare and effect stages, guaranteeing exactly-once delivery and source FIFO consistency to all replicas without consensus protocols.
> - Local operations achieve near-strong consistency when using the WAIT command, while global operations rely on Strong Eventual Consistency (SEC) to guarantee convergence.
> - Conflict resolution uses vector clocks to categorize incoming updates as new, old, or concurrent, resolving conflicts via type-specific properties (e.g. commutative counters) or Last Write Wins (LWW).
> - Garbage collection in CRDBs relies on tombstones that are cleared only after their deletion state has been observed by all replicas.
>
> **Concept links:** [[Distributed Systems]], [[CRDT]], [[Data Replication]], [[Strong Eventual Consistency]], [[Vector Clocks]]
>
> **Suggested connections:**
> - [[MemoryDB Multi-Region - Amazon MemoryDB.md]] — both explain strategies for scaling in-memory databases globally.
> - [[RAFT vs. KRAFT.md]] — contrasts consensus-free replication models (CRDTs) with consensus-based protocols (Raft).
> - [[Valkey Managing Connection Storms in Valkey at Scale.md]] — details client connection behaviors in large-scale caching topologies.
<!-- ai-summary:end -->
## Active-Active geo-distribution (CRDTS-based)

An Active-Active architecture is a data resiliency architecture that distributes the database information over multiple data centers via independent and geographically distributed clusters and nodes. It is a network of separate processing nodes, each having access to a common replicated database such that all nodes can participate in a common application ensuring local low latency with each region being able to run in isolation.

Active-Active Architecture or an Active-Active Geo-Distributed topology is achieved by implementing [CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) (conflict-free replicated data types) in Redis Enterprise using a global database that spans multiple clusters. This is called a “conflict-free replicated database” or “CRDB.”

CRDB provides three fundamental benefits over other geo-distributed solutions:

- It offers local latency on read and write operations, regardless of the number of geo-replicated regions and their distance from each other.
- It enables seamless conflict resolution (“conflict-free”) for simple and complex data types like those of Redis core.
- Even if most of the geo-replicated regions in a CRDB (for example, 3 out of 5) are down, the remaining geo-replicated regions are uninterrupted and can continue to handle read and write operations, ensuring business continuity.

### Deployments & topologies

A CRDB is a database that is created across multiple Redis Enterprise clusters, which typically reside in different data centers around the world. The database in each one of the participating clusters is called a “CRDB instance.” As long as a CRDB dataset fits into the CRDB instance memory, each CRDB instance can be configured differently-composed from a different number of shards and run on a different number or type of cluster nodes

Furthermore, one CRDB instance may run on a multi-availability-zone (AZ) cluster configuration with high availability and data persistence enabled. A second CRDB instance may run on a single-AZ cluster configuration without high availability or data persistence. These CRDBs can run simultaneously in any cloud environment, including Google Cloud, Azure, and AWS. This increased flexibility optimizes infrastructure costs and database performance for your particular use case.

An application that uses a CRDB is connected to the local CRDB instance endpoint. Bi-directional database replication is used between all CRDB instances in a mesh-like topology, i.e., all writes by the application to a local instance are replicated to all other instances, as illustrated here:

![Redis](https://cdn.sanity.io/images/sy1jschh/production/db073ee89fb4c134f211ca19db4b1212116943aa-613x340.svg?w=3840&q=80&fit=clip&auto=format)

Note: Future releases of Redis Enterprise will feature additional topologies, such as ring.

### High-level architecture

#### Conflict-free Replicated Data Types Layer

The CRDB architecture is based on an alternative implementation of most Redis commands and data types (called Conflict-free Replicated Data Types, as explained above). In Redis Enterprise, our CRDB implementation is based on a proprietary Redis module built with the Redis module data type API.

**Read** *commands are handled locally using the local CRDB instance. The inherent consensus-free mechanism of the CRDT layer does not require “read repairs” common to other active-active implementations.*

*Write* commands are processed in two steps, following the principles of operation-based CRDT:

1. In the *prepare* step, the user’s request is processed using the local CRDB instance and a resulting *effect* is created.
2. In the *effect* step, the *effect* data generated above is distributed to all instances (including the local one) and applied.

Operation-based CRDTs require *effect* updates to be delivered to all CRDB instances with guarantees to be delivered exactly once, in a source FIFO consistency. The CRDB generally relies on the Redis replication mechanism, with a few modifications to fulfill these guarantees.

### High availability & disaster recovery

If one or more CRDB instances fail, other instances under the global CRDB continue to read and write, providing continuous availability and disaster recovery. Even if the majority of CRDB instances (for example, 3 out of 5) are down, the remaining CRDB instances are uninterrupted and can continue to take both reads and writes. In these types of regional failures, users who can’t connect to a local CRDB instance are typically diverted to another data center that points to one of the available CRDB instances. This provides continuous availability for application reads and writes, even when a user’s local CRDB instance is down.

On rare occasions, a CRDB instance may experience complete data loss and need database replication from scratch. This condition requires special handling, as the recovering CRDB instance may have sent updates to some of its peers. Since no further updates can be expected, we cannot assume all peers will eventually converge (some effect messages may have been received by some peers but not others). In this scenario, Redis Enterprise implements a reconciliation mechanism involving all relevant CRDB instances. Once reconciled, the recovering instance can simply do a full sync from any other replica.

### Consistency model

Multiple consistency characteristics are applied in a CRDB deployment:

- For local CRDB instance operations, near strong consistency is achieved when the [WAIT](https://redis.io/resources/latest/commands/wait/) command is implemented; otherwise, operations are categorized as having weak consistency.
- For global CRDB operations, Strong Eventual Consistency (SEC) characteristics ensure that any two CRDB instances that have received the same (unordered) set of updates will be in the same state without requiring a consensus protocol. Unlike eventual consistency systems that provide only a [liveness](https://en.wikipedia.org/wiki/Liveness) guarantee (i.e., updates will be observed eventually), [Strong Eventual Consistency](https://en.wikipedia.org/wiki/Eventual_consistency#Strong_eventual_consistency) adds a [safety](https://en.wikipedia.org/wiki/Safety_\(distributed_computing\)) guarantee.

### Conflict (free) resolution

CRDB conflict resolution is based on three CRDT principles:

- The outcome of concurrent writes is predictable and based on a set of rules.
- Applications don’t need to do anything about concurrent writes (but must be CRDB “dialect” compatible).
- The dataset will eventually converge to a single, consistent state.

### How conflict resolution works

Each CRDB instance separately maintains a [vector clock](https://en.wikipedia.org/wiki/Vector_clock) for each dataset object/sub-object. This vector clock is updated upon any update operation at the instance level or when another update operation for the same object arrives from another CRDB instance..

The following process is carried out separately at each CRDB instance upon receiving an update operation (and vector clock) from another instance:

**Stage 1:** Classify the update operation

A received update operation can represent (1) a new update, (2) an old update, or (3) a concurrent update.

The classification algorithm works as follows:

When Instance A receives an update from Instance B regarding object X:

- if: x\_vc\[b\] > x\_vc\[a\] – this is “new” update
- if: x\_vc\[b\] < x\_vc\[a\] – this is an “old” update
- if: x\_vc\[b\] ≸ x\_vc\[a\] – this is a “concurrent” update

Where x\_vc\[a\] is the vector clock of object X at Instance A and x\_vc\[b\] is the vector clock of object X at Instance B.

**Stage 2:** Update the object locally

- If the update was classified as “new,” update the object value in the local CRDB instance
- If the update was classified as “old,” do not update the object value in the local CRDB instance
- If the update was classified as “concurrent,” perform conflict resolution to determine if and how to update the object value in this CRDB instance

The CRDB conflict resolution algorithm is based on two main processes:

**Process 1**: Conflict resolution for a conflict-free data type/operation

In many concurrent update state cases, an update can be processed completely conflict-free based on the properties of the applicable data type. Here are a few examples:

- All operations are commutative and conflict-free when the data type is Counter (mapped to a CRDT’s Counter). **Example:** Counters tracking article popularity, shares, or retweets across regions.
- All operations are either [associative](https://en.wikipedia.org/wiki/Associative_property) or [idempotent](https://en.wikipedia.org/wiki/Idempotence) and are conflict-free when the data type is Set (mapped to a CRDT’s Add-Wins Observed-Removed Set), and the concurrent updates are ADD operations. **Example:** In fraud detection, when the application is tracking dubious events associated with an ID or credit card. The Redis Set cardinality associated with the ID or credit card is used to trigger an alert if it reaches a threshold.
- When the data type is Hash (mapped to a CRDT’s map) and the concurrent updates are over different Hash fields, all operations are conflict-free, as if they were implemented on different objects. **Example:** A shared corporate account with multiple users, using a plan in different locations or at different rates. The HASH object per account could contain innumerable fields per user, and individual user usage could be updated conflict-free, even when concurrent.

In all of these cases, the object value in this instance is updated according to the data-type policy.

**Process 2**: Conflict resolution using the Last Write Wins (LWW) mechanism

A conflict-resolution algorithm should be applied in cases of concurrent updates in a non-conflict-free data type, such as Redis String (mapped to a CRDT’s register). We have used the LWW approach to resolve such situations by leveraging the operation timestamp as a tiebreaker.

Note that our solution works in a strong eventually consistent manner, even if there is a timestamp skew between regions. For example, assume Instance A’s timestamp is always ahead of the other instances’ timestamps (i.e. in the case of a tiebreaker, Instance A always wins). This ensures behavior that is eventually consistent. **Example:** A password is changed for a user account accessed by multiple geographically distributed entities. In this case, the change would log out other users, which might be the right behavior for license enforcement scenarios

## Conflict resolution by example:

Strings

**Data type:** Strings  
**Use case:** Non-concurrent SETs  
**Conflict resolution:** Conflict-free

**Note**: no conflict, *key1,* was last set to “ *value3”* at *t5.*

#### Strings

**Data type:** Strings  
**Use case:** Concurrent SETs  
**Conflict resolution:** Last Write Wins (LWW)

**Note:** t2>t1 and due to LWW key1 was set to “value2.”

#### Strings

**Data type:** Strings  
**Use case:** APPEND vs. DEL  
**Conflict resolution:** Add wins

**Note:** *APPEND* is an ‘update’ operation treated like ‘add’ and therefore wins the *DEL* operation.

#### Strings

**Data type:** Strings  
**Use case:** Concurrent expiration  
**Conflict resolution:** Larger TTL wins

**Note:** At *t6,* *Instance B* persisted (with PERSIST *key1*), meaning its TTL was set to infinite (i.e. -1) larger than *100* that was set by *Instance A*.

#### Counters

**Data type:** Counters  
**Use case:** Concurrent increment/decrement operations  
**Conflict resolution**: Conflict-free

**Note:** In the CRDT layer, the counter value is the SUM of all operations.

#### Counters

**Data type:** Counters  
**Use case:** Concurrent delete and increment operations (Observed Remove in Counter Value)  
**Conflict resolution:** Add wins

**Note:** INCRBY is an ‘update’ operation treated like ‘add’ and therefore wins the DEL operation. In addition, the counter delete operation at t3by Instance A logically means reset the counter.

#### SETS

**Data type:** Sets  
**Use case:** Concurrent SADD operations to a Set  
**Conflict resolution:** Conflict-free

**Note:** This example is conflict-free because *SADD* is an associative operation.

#### Sets

**Data Type:** Sets  
**Use Case:** Concurrent SADD and SREM operations on a Set  
**Conflict Resolution:** Add wins

**Note:** Add wins in Set elements.

#### Sets

**Data Type:** Sets  
**Use Case:** Concurrent complex operation on a Set (Observed Remove)

**Conflict Resolution:** Add wins in Set elements

**Note**: At *t5* *Instance A* can only remove elements *A* and *B* from *key1.*

#### Sets

**Data type:** Sets  
**Use case:** Concurrent SADD operations to a Set  
**Conflict resolution:** Conflict-free

**Note:** This example is conflict-free because SADD is an associative operation.

##### Sets

**Data Type:** Sets  
**Use Case:** Concurrent SADD and SREM operations on a Set  
**Conflict Resolution:** Add wins

**Note:** Add wins in Set elements.

#### Sets

**Data Type:** Sets  
**Use Case:** Concurrent complex operation on a Set (Observed Remove)

**Conflict Resolution:** Add wins in Set elements

**Note**: At *t5* *Instance A* can only remove elements *A* and *B* from *key1.*

#### PUBLISH/SUBSCRIBE

**Data type:** Pub/Sub  
**Use case:** Published message propagates to all CRDB instances  
**Conflict resolution:** Conflict-free

**Note:** In a [*PUBLISH* reply](https://redis.io/resources/latest/commands/publish/), only local subscribers are counted.

#### Garbage collection

Garbage collection

**Data type:** Strings  
**Use case:** Garbage collection  
**Conflict resolution:** Conflict-free

**Note:** CRDTs extensively use tombstones. Tombstones become garbage after being observed by all instances.

Next section ► [Auto tiering](https://redis.io/auto-tiering/)