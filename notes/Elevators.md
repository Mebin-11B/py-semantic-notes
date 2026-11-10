---
title: "Elevators"
url: https://john.fun/elevators
clipped: 2026-08-31 12:17:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Elevators](https://john.fun/elevators)

## Digest Summary
Basic single‑car control uses the SCAN algorithm (full up‑then‑down sweep) or its variant LOOK, which reverses at the highest requested floor.  
Multi‑car systems rely on a central scheduler assigning requests to the nearest car; more advanced schemes evaluate suitability.  
Performance is measured by wait‑time distribution; common metrics include the proportion of rides within 30 s or 90 s and percentiles (p90, p50).  
Traffic patterns vary by time of day; morning lobby‑to‑upper‑floor demand creates the longest waits, while evening traffic reverses direction.  
Otis’ Relative System Response (RSR) scores each car using ETA, load penalty, anti‑bunching, direction‑match, idle‑nearby, and low‑load bonuses; scores are recomputed every 5 s, allowing dynamic reassignment.  
Benchmarks show LOOK can outperform RSR at high load factors or in small banks, whereas RSR reduces wait times under moderate traffic.  
Destination‑dispatch kiosks, despite early knowledge of destinations, often increase waits because they limit the 5‑second re‑optimization flexibility, benefiting only very tall buildings with many cars.  
A full simulation interface is available for exploring these algorithms.

---

## Full Article

[← john.fun](https://john.fun/)

Everyone has shared the frustration of waiting for an elevator that never seems to arrive. "I pressed the button, why isn't it coming?" you ask. For something as commonplace as elevators, they are far more complex than meets the eye.

Over the course of this article, we'll unravel the mysteries of elevators. The way you push their buttons, and how they push yours.1x5x25x

## One Car

The simplest elevator algorithm is called SCAN and was patented in 1961. The elevator starts at the lobby and goes all the way to the top floor before reversing and coming back down. It picks up and drops off anybody on the way.

Most of the time you don't actually need to go to the TOP floor. If the elevator goes only as high as requested before reversing, the algorithm is called the LOOK algorithm. This is the algorithm most people know and expect.1x5x25xadd five calls

## Multiple Cars

Here's where the mystery begins. If there are multiple elevators, how do the cars coordinate who picks up who?

In the most basic system, there's a central scheduler that tells each elevator which floors to stop on. When a new request comes in, it's assigned to the closest elevator. As we'll soon see however, we can do better.1x5x25x

## Long Waits

How do you actually measure how good an elevator algorithm is? The obvious metric is how long you wait for the elevator to arrive.

A very simple measure is "how often does the elevator arrive within 30 seconds?" Or "how often does the elevator arrive within 90 seconds?"-wait < 30s-wait < 90s1x5x25xflow14/minreset

## Applied Stats

More rigorously, we want to look at the DISTRIBUTION of wait times. If we plot the wait time across thousands of rides, we get the histogram below.p50—p90—25x100x500xflow14/minreset

A p90 of 2m means 90% of the time, riders wait 2m or less for the elevator. A p50 of 1m means half the time the elevator arrives within 1m.

People don't usually remember the average amount of time they wait. They fixate on those times when the elevator took FOREVER, the p90 case.

## Morning Rush

Not all passenger traffic is created equal. Imagine a large corporate office building. In the mornings, nearly all traffic is dominated by trips from the lobby to the upper levels.

In the evening this flips as everyone leaves the building. The lunch rush is a bit of both, and the remaining traffic is often from floor to floor.MorningLunchEveningInterfloor-wait < 30s-wait < 90s5x25x100xflow14/minreset

The distribution of wait times varies drastically depending on the time of day and the traffic patterns the elevators are facing. Morning rush notoriously has the worst wait statistics.

## Smarter Elevators

When analyzing the LOOK elevator algorithm, we LOOKED (ha ha) at how riders are assigned to cars. We naively assigned each request to the nearest car but said we could do better.

What if the nearest car is full? We can get smarter with Otis' RSR (Relative System Response) algorithm. RSR scores each car for how well suited it is to pick up a passenger. Lower scores being better.RSR pickup scoreScore=ETA to pickup+onboard load penalty+same-direction anti-bunching penalty-direction-match bonus-idle-nearby bonus-low-load bonusAnti-BunchingPenalize a car if another car is already headed to the same floor in the same direction.Idle NearbyReward idle cars within two floors of the caller.

RSR also re-optimizes every 5 seconds. A passenger that's going to be picked up by elevator A can be re-routed to elevator B if elevator A encounters delays. This re-optimization turns out to be key for streamlining traffic flow.

In the graphic below, each elevator lights up when it's the best choice to service a call from floor 3 if the button happened to be pressed at that exact moment. This constantly changes as the elevators move, showing the optimizer in motion.

## LOOK vs RSR

Armed with our elevator analysis toolkit, we can benchmark the performance of LOOK vs RSR to see how much a smarter elevator algorithm actually improves wait time.LOOK-wait < 30s-wait < 90sRSR-wait < 30s-wait < 90s1x25x250xflow8/minreset

Interestingly as the flow rate gets higher, LOOK actually starts to outperform RSR. When the elevators are always full and stopping on every floor, the extra rules don't matter as much.

LOOK also tends to outperform RSR in small buildings with fewer elevators per bank. Sometimes it's better to just keep things simple.

Another metric you can track is journey time, how long you're actually waiting in the elevator before getting to your floor. RSR and LOOK have different characteristics here as well but that's beyond the scope of this article.

## Destination Dispatch

Not all elevators have buttons in them. Some of the fancy new elevators have a kiosk on each floor that allows you to specify what floor you're heading to before the elevator even arrives. The kiosk then points you to which elevator you should wait for.

This is called Destination Dispatch. At first glance, it seems great. The elevator optimizer now has full knowledge of who is going where, certainly we can use this to reduce wait times right?RSR-wait < 30s-wait < 90sDestination Dispatch-wait < 30s-wait < 90s1x25x250xflow8/minreset

It turns out these fancy kiosks are in general worse for wait times compared to the traditional good ol' up and down buttons. There are certainly edge cases when the kiosks can win out (extremely tall buildings with 8+ cars per elevator bank) but for the majority of cases, simple up down buttons reign supreme.

This counterintuitive result is all thanks to the rebalancing step where every 5 seconds, the system re-optimizes each elevator's path. The kiosk enforces rigidity, you must get in the assigned elevator.

The state of the world 30sec after you called your elevator might be very different but the system is unable to adapt. Turns out the loss in flexibility is not worth the extra information for the optimizer.

## Full Sim

Here's a simulation with all the buttons and knobs to play with. Go crazy!MorningLunchEveningInterfloor-wait < 30s-wait < 90sfloors8cars4flow18/min1x25x100xLookRSRDestination Dispatchresethistogram

## Conclusion

This article just scratches the surface of elevator algorithms. Next time you're stuck waiting for an elevator, try not to take it personally. The elevator did hear you, it just has a lot to think about.
