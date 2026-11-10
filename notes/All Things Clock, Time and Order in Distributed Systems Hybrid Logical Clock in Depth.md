---
title: "All Things Clock, Time and Order in Distributed Systems: Hybrid Logical Clock in Depth"
source: "https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-hybrid-logical-clock-in-depth-7c645eb03682"
author:
  - "[[Kousik Nath]]"
published: 2021-04-03
created: 2026-06-18
description: "The first article of this series discussed physical time, the second article discussed logical time predominantly vector clock and version v"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:2000/format:webp/0*HxkpeyUqPx5InTTC)

Photo by Brandi Redd on Unsplash

## Setting The Context

The [first article](https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-physical-time-in-depth-3c0a4389a838) of this series discussed physical time, the [second article](https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-logical-clocks-in-real-life-2-ad99aa64753) discussed logical time predominantly vector clock and version vectors, the [third article](https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-logical-clock-vs-google-true-time-dba552f2d842) mostly discussed Google True Time and related systems in detail.

By now, we know the following points:

- Using a centralized clock in a distributed system is an ideal solution but an unreliable one as it becomes a single point of failure.
- Physical clocks are not reliable in ordering events and transactions **at an unprecedented scale** as clocks across nodes vary significantly due to their **physical properties, geographic placement, network communication, leap second, clock going backward** issues, etc.
- Logical clocks help us to define order across nodes but at the cost of **eventual consistency,** **implementation complexity, space usage, and performance in the system**. Also, logical timestamps have no correlation to physical time. Hence at some point in time, if you want to find out a snapshot of data across nodes with respect to some physical time, you can’t do that.
- Google True Time kind of systems are essentially physical clocks with tight upper bound but **not every company can run the same infrastructure or optimize their network like Google**. In fact, most of the modern companies which depend on cloud providers like AWS, Azure, OCI, etc don’t even have their private infrastructure. Also, True Time waits out the uncertainty period of time for a maximum of `7 ms` which can cause **noticeable performance issues**.

Questions arise, are we done? If we want to create a new database system, what options do we have to define ordering?

- Most likely, we don’t have the option of having True Time-like infrastructure.
- Should we go ahead with physical time?  
	How will we ensure our clocks are synced well enough so that we don’t end up with tens or hundreds of millisecond time difference in physical clocks?
- Is logical clock the way to go?  
	What if **the system needs a stronger consistency guarantee** than eventual consistency? Logical clocks won’t help.
- If our database has to support transactions across nodes, we need a mechanism to find a **global snapshot** of related data at some point in physical time.

Is there any suitable alternative that can address the above requirements?

## The Hybrid Time / Hybrid Logical Clock ( HLC )

HLC is a kind of Lamport logical clock of physical clocks in a general-purpose distributed system — it builds on top of a physical clock of the nodes in the system and tries to tie itself closely with physical time.

HLC is a tuple of two components: the **physical component** which keeps track of **physical time across the system** and the **logical component** which keeps track of the ordering of events ( causality ) **happening within the same physical time**. **Every node in the system has its own instance of HLC**. When an HLC is instantiated, its physical component is initialized to `**CLOCK_MONOTONIC**` or `**CLOCK_REALTIME**` value in \*unix systems and logical component is initialized to `0`.

### HLC Assumptions

HLC is designed to work on a system where nodes are **coarsely (irregularly) synchronized to NTP or any suitable time protocol**. Hence there are a couple of assumptions:

- **NTP Synchronization:** The first assumption is — every node in the distributed system has NTP daemon installed which synchronizes the node's clock `T_node` to reference clocks ( GPS or atomic clocks ) `T_ref` through NTP. This is a fair expectation from a production system.  
	NTP also provides a possible error bound `E` for each such synchronization. Hence, the error in physical time is bounded:  
	`|T_ref - T_node| ≤ E`. Note that for a clock, `E` can vary from one sync to another. As you can remember from the [first article](https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-physical-time-in-depth-3c0a4389a838), the lesser the stratum number a clock synchronizes to, the lesser is the error bound.  
	**Caution:** If the error is unbounded, the algorithm accumulates error over time. However, It can be mathematically proved that the error remains bounded.
- **Monotonic Physical Clocks:** HLC assumes that physical clocks are monotonically increasing. Technically physical clocks (`**CLOCK_REALTIME**` in \*unix systems) can go backward, however, this is rare. In most cases, NTP can adjust offsets to make clocks slow or fast over a larger period of time. In an extreme case, by monitoring the NTP daemon, **if it’s identified that a clock goes backward, the associated node can remove itself from the cluster**.

### HLC Properties

HLC holds couple of important properties:

- HLC is always **monotonically increasing**. It provides the flexibility of physically meaningful time stamp with bounded error as just described.
- HLC instances are compared as a tuple: first compare the physical component as it has the highest precedence, then compare the logical component if the physical component is same.
- The physical component is not specifically attached to the physical time of any particular node, rather it gets updated every time a higher physical time is seen by the executing node. It keeps on **increasing monotonically**. If we compare two hybrid time instances `ht1` and `ht2`, and  
	`ht1.physical > ht2.physical`, then `ht1 > ht2` or the event associated with `ht2` happens before the one associated with `ht1`.
- If `ht1.physical = ht2.physical`, it’s impossible to know which event happened before which one. Here the logical component swings into action. It’s nothing but a **monotonically increasing counter** which keeps on incrementing for hybrid time instances having the same physical component. Hence, if `ht1.physical = ht2.physical` and  
	`ht1.logical > ht2.logical`, then `ht1 > ht2` or the event associated with `ht2` happens before the one associated with `ht1`.
- **HLC is a superposition on NTP**, the algorithm **does not modify the physical time of nodes**. This ensures that other processes running in the same machine are not interrupted when they are tightly dependent on the node’s physical time.

The above properties make HLC acts as a **distributed global clock**.

### System Properties

- Nodes in a system exchange HLC through RPC calls usually. So if an event `e` in node A happens before another event `f` in node B, A makes an RPC call to B including its HLC.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WBGO3z_d3hoQ8Ij9l720mg.png)

Figure 1: HLC components

### Algorithm and Implementation

If an event `e` happens before another event `f ` ( e **→** f ) and  
`HLC(e) = [p_e, l_e]`, `HLC(f) = [p_f, l_f]` where `HLC(i)` is the hybrid time when event `i` happens, then:

- Either `p_e < p_f`
- Or, `p_e = p_f` and `l_e < l_f`
- Hence, both `e` and `f` are **comparable in lexicographic way**.

### Implementation Notes

- The following implementation is not thread safe. You need to use read and write locks which are out of scope for this discussion.
- The real production level implementations could be different and more efficient in terms of space usage. However, the goal here is to just understand the algorithm.

The following algorithm has been taken from the paper: *“Technical Report: HybridTime — Accessible Global Consistency with High Clock Uncertainty”* published in 2014. It’s a very easy and quite well adopted algorithm in real life systems.

Algorithm 1: The Hybrid Time

### Step By Step Explanation

Line 10–17: Defines the `TimeStamp` class containing physical and logical components.

Line 20–31: Defines an abstraction of physical clock on a node. The method `PhysicalClock.now()` returns the current physical time on the particular node. The node should be NTP synchronized to keep the output as accurate as possible.

Line 34: Defines `lastPhysical` which keeps track of the latest physical time the node has seen in the cluster. When the nodes across the cluster communicate with each other, `lastPhysical` gets updated accordingly.

Line 35: The variable `nextLogical` defines the logical component associated with a physical timestamp.

Line 41–56: Implements `now()` which returns the current hybrid time in the node.

- Line 43: We first get the current physical time on the node.
- Line 45: Check if the current physical time is greater than the latest physical time seen.
- Line 46: If yes, the physical component alone is enough to define causality, we can keep the logical component as `0`.
- Line 47: Since the latest seen physical time `lastPhysical` lags behind the current physical time on the node, we update the variable.
- Line 48: Assign `nextLogical` to `1`. If the node comes across the same physical time in future, `nextLogical` will help establish the causality as described earlier.

Line 58–67: Defines how the hybrid time is updated when the current physical time is less than or equal to `lastPhysical`.

- Line 59: Get the latest hybrid time `now` with the method just described in line 41–56.
- Line 61–62: If the physical component of `now` is greater than the physical component included in the message, ignore the message since updating here violates our policy of having monotonically increasing time.
- Line 65: Else, the incoming timestamp contains higher physical component, hence update `lastPhysical` to the physical component of the message.
- Line 66: Set `nextLogical` to `nextLogical` of the incoming message `+1`. Incrementing the logical component ensures that sending of the event from some node `X` happens before receiving the message at the current node. Since both their physical components are same, the logical component clearly helps us to establish the causality.

## The Good in HLC

- HLC can be implemented in constant space, it does not grow like vector clocks. So no space overhead.
- Easier to understand implementation.
- HLC is close to physical time hence easier to find events or transaction snapshots with respect to physical time.

## HLC Limitations

HLC is not as efficient as Google True Time. While you don’t need to wait out the uncertainty time period like True Time, you need to identify proper strategy how to update HLC across nodes. Couple of options are there:

- While a read transaction happens, if it spans across several nodes, keep track of the maximum HLC seen and update clocks accordingly. It’s actually much more complex, easier said than done.
- Like YugabyteDB, propagate HLC clocks in raft replication to update follower clocks.
- Let every node sync its own HLC with other nodes in the cluster continuously and periodically in the background. How such behaviour affect transactions is to be clearly thought of.

## HLC Use Cases

Some major use cases are:

- HLC helps to find a consistent snapshot of data across nodes at some point in time thus helping in defining **global consistency in databases**. New age multi cloud NewSQL systems which need **strong consistency** take this advantage.
- HLC can help manage multiple versions of data hence enabling Multi Version Concurrency Control (MVCC) which is very important for scaling transactions.

## HLC in Real Life

HLC is inspired from Google’s True Time. Hence few new age distributed relational data stores have followed the suit and adopted HLC.

### HLC in YugabyteDB

[YugabyteDB](https://www.yugabyte.com/) offers all traditional relational database features (e.g; ACID transactions with strong consistency) in a distributed manner. Typically NoSQL data stores come with auto sharding capability but traditional RDMS systems lack that feature. Yugabyte like systems try to bridge that gap.

## Get Kousik Nath’s stories in your inbox

Join Medium for free to get updates from this writer.

Yugabyte relies on HLC for scalable distributed operations, following are some notable use cases:

- Yugabyte manages related replicas as raft groups where the raft leaders accept write requests and propagate monotonic sequence of logs along with HLC to all of its followers. Thus the followers get to update their HLC in case the leader has higher HLC. By the way, do you know what Raft is? No worries, we have it covered in 3 part series: [part 1](https://codeburst.io/making-sense-of-the-raft-distributed-consensus-algorithm-part-1-3ecf90b0b361), [part 2](https://codeburst.io/making-sense-of-the-raft-distributed-consensus-algorithm-part-2-4f12057b019a), [part 3](https://codeburst.io/making-sense-of-the-raft-distributed-consensus-algorithm-part-3-9f3a5cdba514).
- During read operation in a node, based on the current computed HLC, Yugabyte determines which updates should be visible to the client since all the updates have HLC associated to them.
- Yugabyte implements MVCC based on HLC.
- For a distributed transaction spanning across multiple nodes, the nodes write the transaction records in pending state with provisional data. When nodes commit their data, a safe commit HLC is calculated accordingly and transaction is confirmed to the end user or application.

### HLC in Cockroach DB

Cockroach DB also uses similar algorithm for time stamping. However it applies several tricks during transactions to make sure that commits across different nodes are ordered appropriately.

In case you are curious, CockroachDB’s implementation can be found [here](https://github.com/cockroachdb/cockroach/blob/master/pkg/util/hlc/hlc.go).

## Bonus ( Optional Reading )

If you have understood the algorithm above and its implementation, take a look at the following algorithm which is described in another paper: “ *Logical Physical Clocks and Consistent Snapshots in Globally Distributed Databases* ”. This was proposed in 2014 and the implementation is pretty much same as the above, just little more verbose.

**Gist of the Algorithm:** `LogicalTime` component in the following algorithm closely tracks the overall monotonic physical time in the cluster. `Causality` component keeps track of the happens before relation when the logical time does not change — similar to what `nextLogical` of `HybridTime` does in algorithm 1. Algorithm 2 ensures that the difference between the physical and logical component i.e; `|logical time — physical time|` does not grow unbounded.

Look at the below illustration, even if at node 1, physical time is `1` and logical time is `10`, as the message propagates through other nodes in the cluster, the gap between `pt` and `l` decreases. The algorithm assumes that while a message is getting transferred from a node `i` to another node `j`, the physical time at `j` increases by at least `1`. This is a fair assumption. In fact, if the physical time at node `j` increases by an interval `d`, the difference between `pt` and `l` decrease fast in the system. If the logical time is higher than the physical time, physical time catches up and vice versa.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Czht_xGkYvSCGPbqFxpPlw.png)

Figure 2: Time propagation in HLC across nodes

Confused with the above figure? No worries, let’s look at the implementation below to make sense of it:

Algorithm 2: HLC

### Step By Step Explanation

Line 9–15: Defines `PhysicalTime` which is nothing but a representation of the current wall clock time in a node.

Line 17–49: Defines `LogicalTime` which is comparable to another instance of the same type. Logical time is **monotonically increasing**.

- Line 24–26: The `copyOf` method creates a clone of the supplied logical time. We’ll see it in action in some time.

Line 51–71: Defines `Causality` which is essentially a **monotonically increasing counter for HLC having the same logical time**. The instances are comparable to each other.

Line 73–77: Defines `Message` — nodes in the system communicates with each other by passing messages. While sending a message, a node attaches its current `LogicalTime` and related `Causality` to it.

Line 79–98: Defines the hybrid logical time `Time`. It contains an instance of `LogicalTime` and `Causality`. `Time` instances are comparable to each other.

- Line 89–97: We show lexicographic comparison of `Time` instances. However, since `LogicalTime` and `Causality` are comparable to themselves, we could compare them directly among each other as well.
- **Lexicographic comparison helps to retrieve events in ordered fashion when they are stored in some data store**.

Line 115–121: It’s an abstraction over how physical time on the current node is retrieved. Java’s `System.currentTimeMillis()` provides Linux Kernel’s `**CLOCK_REALTIME**` value or the wall clock time.

Line 123–138: Describes how hybrid time is calculated while sending an event to other nodes or executing a local event:

- Line 125: Creates a local copy of the current `logicalTime` in `logicalTimeCopy`.
- Line 126–128: Set the logical time to the maximum of the current logical time and current physical time of the node.
- Line 130–131: If the logical time is still same, we increment the `causality` counter to record happens before relation.
- Line 133–134: If the logical time is updated to the current physical time of the node, then we reset `causality` to `0`.
- Line 137: Return an instance of hybrid time `Time` to the caller which propagates the current logical time and causality information.

Line 140–162: Defines how the hybrid time is updated while receiving an event:

- Line 144: Creates a copy `logicalTimeCopy` of the current logical time.
- Line 145–146: Set `logicalTime` to the maximum of `logicalTimeCopy`, logical time included in the incoming message and the current physical time on the node.
- Line 148–149: If all of these components are same, set `causality` to maximum of current causality in the node and causality included in the message `+1`.
- Line 151–152: If the logical time included in the message lags behind the current logical time on the node, increment the current causality indicating reception of the message.
- Line 154–155: If the logical time is updated to the logical time of the incoming message, we have to update the `causality` to the message’s causality `+1`.
- Line 157–158: If the logical time is updated to the current physical time of the node, reset causality back to `0`.

Line 161: Return the `Time` instance to the caller.

## Conclusion

With this article, we complete the extremely comprehensive series “ *All Things Clock, Time and Order in Distributed Systems* ” series. Wow!!!

We have analyzed why and when of Physical Clocks, Logical Clocks, Google True Time and finally Hybrid Logical Clock in a step by step manner. With each of these articles,we have seen real life examples e.g; how Riak uses version vector logical clocks, Cassandra still relies on physical clock, Google Spanner uses True Time and new age systems like YugaByte uses Hybrid Time. We also examined how the fundamental parameters like consistency guarantee of these systems impact the decision of which clock implementation has to be chosen. We looked into the vector clock implementation of Voldemort key value store in [part 2](https://medium.com/geekculture/all-things-clock-time-and-order-in-distributed-systems-logical-clocks-in-real-life-2-ad99aa64753) and two different implementations of Hybrid Time in this article.

The intention of this series was very clear: not only converge extremely scattered theory of time and clocks into an easy to understand series of articles, but more importantly, as an engineer, look into real life use cases and implementations, so that if you get an opportunity to work on such systems and algorithms in future, you can refer back to this series and get some calibrated insights.

This is one of the deep series of articles I have written and a lot of efforts have gone behind. If you have reached this much, it means you found this series beneficial.

Please consider hitting claps multiple times and share this on LinkedIn, Twitter for a better reach.

Do let me know if you have any feedback to share.