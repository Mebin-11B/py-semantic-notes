---
title: "Hybrid Logical Clocks"
source: "https://www.bartoszsypytkowski.com/hybrid-logical-clocks/"
author:
  - "[[Bartosz Sypytkowski]]"
published: 2020-04-22
created: 2026-06-18
description: "In this blog post we'll going to talk about timestamps. But to start with weneed to answer the basic question: what are we using timestamps for? Two mostcommon cases are: 1. We want to timestamp our records so later we can query data within specific    time bounds"
tags:
  - "clippings"
---
In this blog post we'll going to talk about timestamps. But to start with we need to answer the basic question: *what are we using timestamps for?* Two most common cases are:

1. We want to timestamp our records so later we can query data within specific time bounds eg. generating weekly reports.
2. We want to use them to order our records to say if one of them *happened before* another. This is important property especially for (distributed) databases, which often use timestamps to manage the order in which transactions should be executed (and when they should be aborted).

Now, the next question is: can we use a standard date (in.NET represented as `DateTime`) for both of these goals? As it turns out, not really. While in real life we perceive time going only in one direction, in computers it may happen that calling date API two times in a row, the second one will return value earlier than the first one. This is the problem we want to solve.

While this may seem to sound like totally abstract problem, it might really happen and [had caused real outages](https://www.wired.com/2012/07/leap-second-glitch-explained/?ref=bartoszsypytkowski.com) in the past.

## When time does not move forward...

Unfortunately there are several situations, when the time API of our operating system can go back in time. Here, we'll shortly cover two common examples of such situation.

### Hardware clocks and OS time API

Before we continue, first we need to understand the relationship between clocks in our hardware and timestamp value provided by the operating system.

First, everyone by now probably know that clocks on most of the commodity hardwarde, including most data centers, are not perfect. The reason is simple: pretty much every hardware needs clock, but high-precision clocks (like atomic clocks) are very expensive. Most of the machines nowadays use much cheaper, quartz (or similar) clocks, which usually tick with frequency between 32kHz up to 4MHz. Each machine knows how many ticks are needed to make a given time interval to pass.

The problem with quartz is that its "ticking" frequency is not constant and can be changed by different environmental effects - temperature most of all others - and therefore our timestamp can be skewed. Since we cannot really change physical properties of the materials, this issue is solved on software level, usually as a result of measuring several network-separated clocks living on different machines. This however may mean, that sometimes in order to adjust our clock, we may need to reset it to a different point in time. And sometimes it may be in the observed past.

You might have heard, that OS also provide so called monotonic clock (which subsequent timestamps can only move forward). It's true. In fact most operating systems provide different options for time retrieval:

1. Standard way is to read actual date and time of a day using either `clock_getttime(CLOCK_REALTIME)` (Linux) or `GetSystemTimePreciseAsFileTime(&ts)` (Windows). In most platforms these differences are wrapped into uniform API eg. `DateTime.UtcNow` on.NET. This time is not monotonic, as it can move backward in time (meaning two subsequent calls CAN produce lower value on the second call).
2. Another way is to get a monotonic timestamp via `clock_gettime(CLOCK_MONOTONIC)` / `QueryPerformanceCounter(&ts)` - which on.NET are both represented under common `System.Diagnostics.Stopwatch` class. This API can be used to represent amount of time that passed since a given moment.

While initially monotonic clock seems to be good for our use case, in practice it's not, as it's not being adjusted for clock drifts and for this reason cannot be used as a realtime clock replacement.

### Solar time vs. UTC

One inherent reason for clock inacuracies comes from the very definition of UTC. As you probably know the solar day is not exactly equal to 24h. This is why we have leap years, when we add one extra day to make up for all of the fractions skipped over several years.

Similar thing happens in much smaller scale. The reason behind it is that UNIX time (arguably used in majority of current datacenters) assumes that each day is exactly 24h. It makes some calcullations like "how many days passed since X?" very easy to compute. However in practice solar day is not a constant - as Earth rotation is slowing over time, the day (and our notion of 24 "hours" with it) is taking longer to pass.

UTC adjustes clock to changes in Earth rotation by introducing extra second from time to time, just like we do we leap years. This means that sometimes minute can indeed have 61 seconds. The problem is that UNIX time doesn't understand that concept. How it solves is? It's simple: it counts the same second twice! This phenomenon is known as **leap second**, and it means that the next second after `23:59:59` could be... `23:59:59`. When that happens, it's very bad from the perspective of time-based ordering.

At the present day quite popular (but not always used) way of dealing with leap seconds - known as **leap second smearing** - is backed into time synchronization protocols and relies on time server announcing leap second happening at some specific point in the future. All of the subordinate servers after acknowleding that fact start to slow counting their hardware clock ticks in order to amortize incoming extra second, so that by the time it happens we could just skip it over, just like it never existed.

### Network Time Protocol

When talking about time synchronization protocols, we definitelly should mention NTP (Network Time Protocol), which is currently an industry standard and used by pretty much all network connected devices.

The basic concept behind NTP is to have a reference point - a server(s) considered to have a more precise and reliable clock - which will be used as a source of "correct" time for our own server. Additionally, in order to make that solution more scalable, machines organize themselves into layers (a.k.a. **stratums**), so that lower-level stratums serve as refernce point to higher ones. At the root we have high-precision atomic clocks, but their actual addresses can be changed by an OS administrators.

![stratum](https://pthree.org/wp-content/uploads/2013/11/stratum.png)

Now, NTP can perform time adjustment in one of two ways:

1. Introducing a skew. It's similar to smearing we talked about above. When a one server notices that its own time is higher or lower than its "reference point", it internally starts speeding up or slowing down counting ticks of its own hardware clock to eventually match the received time.
2. On rare occassions clock can drift more than 128ms from its remote source. In that case skewing is considered not to be enough, and local clock resets its value to match the received one. This may mean that our timestamp indeed will go back.

Now, there are few more problems with NTP: it's fairly slow and is uses its own set of assumptions - like the network delay of request and response being symetric - which is not always ideal and was the reason why other protocols like PTP (Precision Time Protocol) were invented. If you're interested more about details of these two protocols, I recommend you reading [this article](https://www.redhat.com/en/blog/combining-ptp-ntp-get-best-both-worlds?ref=bartoszsypytkowski.com).

## Complex problem, easy solution workaround

The big problem related to the issues mentioned above is that, there's not a lot we can do about them from the scope of user applications, mostly because the stuff we talked about is treated as a black box in hands of operating systems.

However some application-level solutions have been proposed to bring us some compromise between monotonicity and real time guarantees. Here, we'll talk about [Hybrid Logical Clocks](http://users.ece.utexas.edu/~garg/pdslab/david/hybrid-time-tech-report-01.pdf?ref=bartoszsypytkowski.com). While the paper is quite complex, the actual (working) solution is fairly simple. We're going to comply with.NET `DateTime` (UTC), which can be represented on 64 bits representing number of ticks - in.NET each *tick* is standardized to be equal to 100 nanoseconds. Now that's a pretty high precision. Lets ask ourselves: how often do we need to use nanosecond precision? Are microseconds enough? Are milliseconds?

Depending on our requirements, we may sacrifice some of the tail bits to lower our precision in order to receive a space, that we're going to use for different purpose:

- 4bits → 1.6µs
- 8bits → 25.6µs
- 12bits → 409.6µs
- 16bits → 6.5ms

The choice is yours. Here, I'll be using 16bit space. Of course there are situations when this is not enough, like high frequency trading systems, but arguably it still gives us a plenty of precision - remember, where talking about time and ordering, not measurements (for these you should use monotonic clock).

```fsharp
module Hlc

open System
open System.Threading

let [<Literal>] private Mask = 0xffL // 16 bits
let private osTime () = DateTime.UtcNow.Ticks &&& ~~~Mask
let mutable private latest = osTime()
```

So, here we're going to read a current UTC time given from our operating system, trimmed by the last 16 bits. We're also going to keep the highest time value known so far in the special (static) field. This will be our watermark, so that we know that the timestamp we're going to provide should never drop below that value - otherwise our clock would not be monotonic.

Now, lets try to write a function to get a current timestamp - what we're going to do here is to get current (trimmed) UTC clock value and compare it against our `latest` value we got so far. If the UTC value is less than what we expected - so the clock value tried to go "back in time" - we simply pick the highest value instead and increment it by 1 - this counter increment will be stored on the 16 bits we cleared at the beginning, which gives us 65536 calls before we start overflowing counter on the date segment. So unless you're going to call this method dozens (hundreds?) of millions of times every second, you're safe. Even then, it's not a big deal until it happens constantly.

This will let us assign different (monotonically increasing) timestamps every time even when we had to serve multiple calls while the gap between current OS time and our latest noticed one still holds:

```fsharp
let rec now () : DateTime =
    let ticks = Volatile.Read &latest
    let current = Math.Max(osTime(), ticks) + 1L
    if Interlocked.CompareExchange(&latest, current, ticks) = ticks 
    then DateTime(current, DateTimeKind.Utc)
    else now ()
```

What you see here is a lock-free implementation of update pattern over our `latest` field - since it's static and mutable, we need to guarantee that it's updated safely. We can do that by using compare-and-swap operators, which in.NET are realized by `System.Threading.Interlocked` class.

Here we'll simply read the latest value, update it and try to write it - if the field's value has changed in the meantime (eg. because it was updated from another thread), our `Interlocked.CompareExchange` method will return different value that what we just read. In that case we'll simply retry the operation.

Now, while we have implemented our time provider, there's one more case to cover: *if our service communicates with other remote services, the state of their clocks may be different from ours (read: they may be "in the future" relatively to us), which in some case, like determining which operation happened as the last one, will always cause current service operations to loose*.

For this reason we need to be able to sync time from remote services with the one we're keeping locally:

```fsharp
let rec sync (remoteDate: DateTime) =
    let ticks = Volatile.Read &latest
    let current = Math.Max(ticks, remoteDate.Ticks)
    if Interlocked.CompareExchange(&latest, current, ticks) = ticks then ()
    else sync remoteDate
```

Here, we'll simply pick remote time and compare it against our own, letting the highest one be our new "latest" observed timestamp.

Calling the `Hlc.sync` method manually may be inconvenient. You can make it a bit easier eg. by including it as part of deserialization process.

What's worth noticing, this clock implementation guarantees monotonicity with fairly precise date and time measurements. However it doesn't guarantee that provided timestamps will be unique across services - there's a possibility that different machines will generate the same timestamp without knowing about each other while serving concurrent requests. For that reason HLC timestamps sometimes come together with some unique and ordered process identifier, building composite `(<timestamp>,<process-id>)` pair which is guaranteed to be unique.