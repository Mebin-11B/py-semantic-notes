---
title: "When \"idle\" isn't idle: how a Linux kernel optimization became a QUIC bug | Cloudflare Blog"
url: https://blog.cloudflare.com/quic-death-spiral-fix/
clipped: 2026-08-31 12:26:29
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug | Cloudflare Blog](https://blog.cloudflare.com/quic-death-spiral-fix/)

## Full Article

[Skip to content](https://blog.cloudflare.com/quic-death-spiral-fix/#main-content)

CUBIC, standardized in [RFC 9438](https://www.rfc-editor.org/rfc/rfc9438.html), is the default congestion controller in Linux, and as a result governs how most TCP and QUIC connections on the public Internet probe for available bandwidth, back off when they detect loss, and recover afterward. At Cloudflare, our open-source implementation of QUIC,[quiche](https://github.com/cloudflare/quiche), uses CUBIC as its default congestion controller, meaning this code is in the critical path for a significant share of the traffic we serve.

In this post, weâll tell the story of a bug in which CUBIC's congestion window (cwnd) gets permanently pinned at its minimum and never recovers from a congestion collapse event.

The story starts with a [Linux kernel change](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) aimed at bringing CUBIC into line with the app-limited exclusion described in [RFC 9438 Â§4.2-12](https://www.rfc-editor.org/rfc/rfc9438.html#section-4.2-12) â a fix to a real problem in TCP that, when ported to our QUIC implementation, surfaced unexpected behaviors in quiche. It has a happy ending: an elegant (near-)one-line fix that broke the cycle.

## CUBIC's logic in a nutshell

Before we dive into the core problem, a quick refresher on Congestion Control Algorithms (CCAs) may help to set the stage.

The central knob a CCA turns is the congestion window ( `cwnd` ): the sender-side cap on how many bytes can be in flight (sent but not yet acknowledged) at any moment. A larger  `cwnd`  lets the sender push more data per round trip; a smaller  `cwnd`  throttles it. Every loss-based CCA, CUBIC included, is ultimately a policy for how to grow  `cwnd`  when the network looks healthy and how to shrink it when it doesn't.

In essence, CCAs aim to maximize data transfer by inferring the "available bandwidth" of the network; because no one wants to pay for a 1 Gbps subscription and only use a fraction of it. The family of loss-based algorithms, to which CUBIC belongs, operate on a fundamental premise: (1) if there is no packet loss, increase the sending rate (i.e. increase the bandwidth utilization); (2) if there is loss, loss-based algorithms assume that the network's capacity has been exceeded, and the sender must back off (i.e. decrease the bandwidth utilization).

This logic is built on several assumptions that have been revisited over the years. However, we'll save that discussion for another time.

## The symptom: a test that fails 61% of the time

Our investigation started with the report of unexpected failures in our ingress proxy integration test pipeline. This erratic behavior appeared in tests where CUBIC was evaluated in a scenario of heavy loss in the early part of the connection.Â 

Recovery after congestion collapse is an uncommon regime, but it is exactly the regime a congestion controller exists to handle. Most congestion control tests exercise the steady-state and growth phases of an algorithm; far fewer probe what happens at minimum cwnd, after the connection has been beaten down. Bugs in this corner of the state space are invisible in throughput dashboards, undetectable by static review, and only surface when you deliberately drive a CCA into it and watch whether it can climb back out â which is exactly what this test did.

The simulated test setup includes the following details:
- Quiche HTTP/3 client and server running at locally (localhost)
- RTT = 10ms (set up in the configuration)
- A 10 MB file download over HTTP/3
- Using CUBIC congestion control
- With 30% random packet loss injected during the first two seconds
- After two seconds, loss stops entirely
- The test has a generous 10-second timeout to complete the download, which is expected to be completed in four or five seconds

The expected behavior is straightforward: CUBIC should take some hits during the loss phase, reduce its congestion window, and once loss stops, steadily ramp up and finish the download well within the timeout. Instead, we observed in multiple 100-time runs that around 60% of our tests were not able to complete the download within the generous 10-second timeout.

## The anomaly: 999 state transitions with zero loss

We instrumented[quiche's qlog](https://github.com/cloudflare/quiche) output with packet loss events and built visualizations to understand what was happening inside the congestion controller:

Connection overview of a failing test. After T=2s, packet loss stops entirely â yet cwnd remains pinned at the minimum floor and the congestion state oscillates between recovery and congestion avoidance every ~14ms.

After the two-second (2000 ms) mark, packet loss stops entirely. However, the number of bytes in flight remains flat, which contradicts the core logic of the CUBIC algorithm: in the absence of loss, apply more gas to increase throttle (more bytes in our world). This raises the question: if the network is no longer dropping packets, why is the congestion window failing to grow?

When we zoom into that region, our analysis shows that CUBIC enters a rapid oscillation, shown in our plot as an extended recovery phase, between congestion avoidance state (the operational regime phase) and recovery state (the packet loss recovery state) â 999 transitions in approximately 6.7 seconds. Thatâs one transition every ~14ms â suspiciously close to the connection's RTT (10ms). Throughout this entire period, cwnd is locked at the minimum floor: 2700 bytes, or two full-size packets.

Clearly something in CUBIC's logic is misinterpreting the state of the connection. The key clue is the oscillation period: ~14ms matches the RTT. Whatever is triggering the recovery/avoidance flip is happening once per round trip, in lockstep with connection's ACK clock; the self-clocking rhythm in which each round-trip's ACKs from the client trigger the server's next send. Because this is a download (server to client), the ACKs in question travel client to server, and CUBIC's state machine runs on the server side: every time those ACKs land, bytes_in_flight drops to zero and the server sends the next two-packet burst, which is what triggers the bug.

To confirm this behavior was CUBIC-specific, we ran the same test with [Reno](https://dl.acm.org/doi/10.1145/235160.235162), another member of the loss-based family but with a different growth rate. The results were conclusive: 100% pass rate, showing Reno recovered cleanly after the loss phase, and revealing that this is a CUBIC-related bug.

Reno recovers cleanly after the loss phase ends at T=2s and completes the download by ~5s

## Tracing the root cause

Loss-based algorithms have two pedals, gas and brake, with a difference in how they accelerate. Well, CUBIC comes with some extra features. Here we are going to focus on bytes_in_flight == 0.

### TCP CUBIC after idle (Linux, 2017)

To understand the bug, we first need to understand the optimization it came from. In 2017,an issue was found with Linux kernel's CUBIC implementation. The[commit message](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) explains:

The epoch is only updated/reset initially and when experiencing losses. The delta "t" of  `now - epoch_start`  can be arbitrary large after app idle as well as the  `bic_target` . Consequentially the slope (inverse of  `ca->cnt` ) would be really large, and eventually  `ca->cnt`  would be lower-bounded in the end to 2 to have delayed-ACK slow-start behavior.

This particularly shows up when  `slow_start_after_idle`  is disabled as a dangerous cwnd inflation (1.5 x RTT) after few seconds of idle time.

The epoch is the reference timestamp CUBIC uses to anchor its growth curve:  `W_cubic(delta_t)`  is parameterized by  `delta_t = now - epoch_start` , and the epoch is reset whenever CUBIC restarts its growth function â most notably after a loss event reduces  `cwnd` . Between resets,  `delta_t`  grows monotonically with wall-clock time.

When an application goes idle (stops sending) for a while and then resumes, the CUBIC growth function  `W_cubic(delta_t)`  computes  `delta_t`  as  `now - epoch_start` , as illustrated in the figure below. Since the epoch wasn't updated during idle,  `delta_t`  is huge, producing an enormous target window â and CUBIC would immediately try to inflate  `cwnd`  to an unreasonable value.

Jana Iyengar's initial fix was to reset `epoch_start` when the application resumes sending. But Neal Cardwell [pointed out](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) the flaw in that approach:â¦it would ask the CUBIC algorithm to recalculate the curve so that we again start growing steeply upward from where cwnd is now (as CUBIC does just after a loss). Ideally we'd want the cwnd growth curve to be the same shape, just shifted later in time by the amount of the idle period.

The elegant solution, authored by Eric Dumazet, Yuchung Cheng, and Neal Cardwell, was to shift the epoch forward by the idle duration rather than resetting it. This preserves the shape of the CUBIC growth curve â just sliding it in time so that the algorithm picks up where it left off.

### The port to quiche (2020)

When CUBIC was [first implemented](https://blog.cloudflare.com/cubic-and-hystart-support-in-quiche/) in quiche, this idle-period adjustment was ported. However, QUIC, which runs in the user space, doesn't have TCP's kernel-level  `` [CA_EVENT_TX_START](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) callback. Instead, the quiche implementation checks for the idle condition inside  `on_packet_sent()` : ` `// cubic.rs â on_packet_sent() (simplified)
/// Updates the state when a packet is sent.
fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
    // If the sending burst is restarting (i.e., bytes_in_flight was zero before this send),
    // adjust the congestion recovery start time to account for the gap in sending.
    if bytes_in_flight == 0 {
        let delta = now - self.last_sent_time;
        self.congestion_recovery_start_time += delta;
    }
    // Record the time of this send event.
    self.last_sent_time = now;
}` ` 

### Where it breaks: the QUIC difference

The fix ported to quiche included a bug in the original kernel change which was fixed by a [followup change to the kernel cubic module](https://github.com/torvalds/linux/commit/c2e7204d180f8efc80f27959ca9cf16fa17f67db) about a week later. The commit message for the second fix explains:

 `tcp_cubic` : do not set  `epoch_start`  in the future	Tracking idle time in  `bictcp_cwnd_event()`  is imprecise, as  `epoch_start` 	is normally set at ACK processing time, not at send time.

Doing a proper fix would need to add an additional state variable,	and does not seem worth the trouble, given CUBIC bug has been there	forever before Jana noticed it.

Let's simply not set  `epoch_start`  in the future, otherwise	 `bictcp_update()`  could overflow and CUBIC would again	grow  `cwnd`  too fast.

As mentioned in the commit message, recovery start time is set during ACK processing, and the computation of the adjustment based on sent times can push the recovery start time into the future. This explains the oscillation between recovery and congestion avoidance seen on our test.Â  The trap only consistently triggers when every incoming ACK drives bytes_in_flight all the way to zero â which in practice means cwnd has collapsed to its minimum (two packets) and the application has data ready to send another full window the moment an ACK arrives. Outside this regime, bytes_in_flight == 0 is less likely to hold on every send, so it is less likely to trigger the bug.Â 

Why doesn't this also happen at connection start? The bug only triggers when the connection exits slow-start and switches over to congestion avoidance. Before exiting slow-start,  `congestion_recovery_start_time`  is not set, so the buggy branch in  `on_packet_sent`  has no recovery boundary to advance. During slow start CUBIC's  `cwnd`  grows by the same Reno-style ack-based rule shared by all loss-based CCAs â the cubic curve and its sensitivity to  `congestion_recovery_start_time`  only enter the picture once the connection is in congestion avoidance, meaning the trap needs three things at once: a real loss event to set the recovery boundary, congestion avoidance to be running, and  `cwnd`  collapsed to the two-packet floor.

The self-perpetuating recovery trap. At minimum cwnd, every ACK cycle triggers the idle period adjustment with an inflated delta.

At a minimum cwnd (two packets), the dynamics of the connection shift into a "death spiral" where the idle period optimization becomes a self-fulfilling prophecy. This trap operates in a continuous loop:
- Send and ACK packets: The sender transmits the entire two-packet window. After one RTT (~14ms), both packets are ACKed, causing bytes_in_flight to drop to zero.
- False idle detection: When the next burst is sent, on_packet_sent() sees bytes_in_flight == 0 and assumes the connection was idle, but it was congestion limited.
- Inflated delta: The calculation uses now - last_sent_time to determine the idle duration. When the congestion window ( `cwnd` ) is at its minimum,  `last_sent_time`  is the timestamp of the start of the previous RTT cycle. Therefore, the resulting delta is approximately 14ms (the connection's RTT + additional rounding errors). This RTT-sized delta is incorrectly applied as the "idle" time. The actual time the connection was idle (the processing gap between the last ACK arriving and the next packet being sent) is effectively 0. By measuring the full RTT instead of the true gap, the delta is inflated significantly, aggressively shifting the recovery start time forward, possibly into the future.
- Perceived recovery: Because the recovery start time is now in the future, the  `in_congestion_recovery()`  check returns true for every incoming ACK.Â  Processing of the next ACK exits recovery and sets the recovery start to the ACK time which is larger than last_sent_time, making it likely for the congestion controller to push the recovery time into the future when doing the next send.
- Stagnation: Since CUBIC skips  `cwnd`  growth for any packet perceived to be in a recovery period, the window remains pinned at two packets â ensuring the pipe drains completely on the next ACK and restarting the cycle.

And this loop repeats for thousands of cycles until the accumulation of small deviations â from scheduler jitter and ACK processing variance â lets the <= boundary in  `in_congestion_recovery()`  slip behind the next packet's send time, breaking the cycle.

## The fix: measuring idle from the right moment

Fixing the death spiral involves measuring the idle duration from when bytes_in_flight actually transitioned to zero (the last ACK processed) rather than the last packet sent.

### The code change

- Add last_ack_time timestamp to the CUBIC state.
- Update that timestamp when ACKs arrive.
- Use it for the idle delta computation: ` `// cubic.rs â on_packet_sent()
fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
    // Check if the connection was idle before this packet was sent.
    if bytes_in_flight == 0 {
        if let Some(recovery_start_time) = r.congestion_recovery_start_time {
            // Measure idle from the most recent activity: either the
            // last ACK (approximating when bif hit 0) or the last data
            // send, whichever is later. Using last_sent_time alone
            // would inflate the delta by a full RTT when cwnd is small
            // and bif transiently hits 0 between ACK and send.
            let idle_start = cmp::max(cubic.last_ack_time, cubic.last_sent_time);

            if let Some(idle_start) = idle_start {
                if idle_start < now {
                    let delta = now - idle_start;
                    r.congestion_recovery_start_time =
                        Some(recovery_start_time + delta);
                }
            }
        }
}` ` 

With the delta now reflecting the actual gap since the last ACK, the recovery boundary stops chasing the send time:

Old code: boundary advances one RTT per cycle, always landing on or ahead of the next send.

Fix: boundary barely moves; the next send lands ahead of it and cwnd grows.

For genuinely idle connections,  `last_ack_time`  is far in the past and the same expression captures the full idle duration, the original epoch-shift behavior is preserved.

## Validation

With the fix applied, the 100% pass rate of our quiche testing suite was restored.

After the fix, cwnd grows along the expected CUBIC curve and the download completes in ~4-5 seconds.

We don't worry about the losses at the end of the connection â that's expected because we fully utilized the router's allocated buffer. In other words, we are fully utilizing the available bandwidth in this test case.

## Takeaways

- "Idle" is harder to define than it sounds. Normal pipeline delays at small windows can look like idleness to simple checks.
- Minimum-cwnd dynamics are a unique corner case. The bug was invisible at high speeds and only triggered after severe loss.
- The fix was surprisingly small compared to the complexity of the behavior. After weeks of instrumenting qlogs and analyzing visualizations to find the root cause, the solution required changing just three lines of code. As we noted during the investigation: the effort to find the bug was massive, but the fix itself was basically one line of logic.

The fix described in this post has been contributed to  `cloudflare/quiche` , Cloudflare's open-source implementation of QUIC and HTTP/3. Our CCA efforts go beyond loss-based algorithms: we also use quicheâs modular congestion control design to experiment with and tune our model-based [BBRv3](https://blog.cloudflare.com/new-standards/#congestion-control) implementation, now enabled for a growing percentage of our QUIC deployments. Stay tuned for further updates on QUIC congestion control implementation and performance.Â  

If you're interested in congestion control, transport protocols, or contributing to open-source networking code, check out the quiche repository. We're always looking for talented engineers who love digging into problems like these, please explore our[open positions](https://www.cloudflare.com/careers/).

## Related tags

[Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)[Debugging](https://blog.cloudflare.com/tag/debugging/)[HTTP3](https://blog.cloudflare.com/tag/http3/)[Networking](https://blog.cloudflare.com/tag/networking/)[QUIC](https://blog.cloudflare.com/tag/quic/)[QUICHE](https://blog.cloudflare.com/tag/quiche/)[Rust](https://blog.cloudflare.com/tag/rust/)

Follow on Social Media
- Cloudflare

## Subscribe to receive notifications of new posts

Email address

Weâll never share your email address.Subscribe

Thanks for subscribing! Check your inbox to confirm.Search is temporarily unavailable.[Login opens in a new tab](https://dash.cloudflare.com/login)[Dashboard opens in a new tab](https://dash.cloudflare.com)[Contact Sales opens in a new tab](https://www.cloudflare.com/resource/contact-enterprise-sales/)[Start Building opens in a new tab](https://dash.cloudflare.com/sign-up)[opens in a new tab](https://x.com/cloudflare)[opens in a new tab](https://www.linkedin.com/company/cloudflare-inc-)[opens in a new tab](https://blog.cloudflare.com/rss/)All Categories
- [AI](https://blog.cloudflare.com/tag/ai/)
- [Developers](https://blog.cloudflare.com/tag/developers/)
- [Radar](https://blog.cloudflare.com/tag/cloudflare-radar/)
- [Product News](https://blog.cloudflare.com/tag/product-news/)
- [Security](https://blog.cloudflare.com/tag/security/)
- [Policy & Legal](https://blog.cloudflare.com/tag/policy/)
- [Zero Trust](https://blog.cloudflare.com/tag/zero-trust/)
- [Speed & Reliability](https://blog.cloudflare.com/tag/speed-and-reliability/)
- [Life at Cloudflare](https://blog.cloudflare.com/tag/life-at-cloudflare/)
- [Partners](https://blog.cloudflare.com/tag/partners/)English
- This Post is Available in
- [æ¥æ¬èª](https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/)
- [íêµ­ì´](https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/)
- Switch Site Language
- [English](https://blog.cloudflare.com/)
- [Deutsch](https://blog.cloudflare.com/de-de/)
- [EspaÃ±ol](https://blog.cloudflare.com/es-es/)
- [EspaÃ±ol (LatinoamÃ©rica)](https://blog.cloudflare.com/es-la/)
- [FranÃ§ais](https://blog.cloudflare.com/fr-fr/)
- [Italiano](https://blog.cloudflare.com/it-it/)
- [æ¥æ¬èª](https://blog.cloudflare.com/ja-jp/)
- [íêµ­ì´](https://blog.cloudflare.com/ko-kr/)
- [ç¹é«ä¸­æ](https://blog.cloudflare.com/zh-tw/)
- [ç®ä½ä¸­æ](https://blog.cloudflare.com/zh-cn/)
- [PortuguÃªs](https://blog.cloudflare.com/pt-br/)
- [Ð ÑÑÑÐºÐ¸Ð¹](https://blog.cloudflare.com/ru-ru/)
- [Bahasa Indonesia](https://blog.cloudflare.com/id-id/)
- [à¸ à¸²à¸©à¸²à¹à¸à¸¢](https://blog.cloudflare.com/th-th/)
- [Tiáº¿ng Viá»t](https://blog.cloudflare.com/vi-vn/)
- [Polski](https://blog.cloudflare.com/pl-pl/)
- [Ø§ÙØ¹Ø±Ø¨ÙØ©](https://blog.cloudflare.com/ar-ar/)
- [×¢××¨××ª](https://blog.cloudflare.com/he-il/)
- [Svenska](https://blog.cloudflare.com/sv-se/)
- [Nederlands](https://blog.cloudflare.com/nl-nl/)
- [TÃ¼rkÃ§e](https://blog.cloudflare.com/tr-tr/)LightDark
