---
title: "Mullvad exit IPs are surprisingly identifying"
url: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/
clipped: 2026-06-17 01:02:27
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - virtual private networks
  - anonymity and privacy
  - fingerprinting
  - IP addresses
  - wireGuard
  - RNG seed vulnerability
related:
  - "[[Referer Reality]]"
  - "[[Reticulum, a secure and anonymous mesh networking stack]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Mullvad's deterministic assignment of exit IPs based on a user's WireGuard public key enables cross-server correlation and user fingerprinting, although Mullvad has since rolled out a scrambling mitigation.
>
> **Key points:**
> - Mullvad servers assign exit IPs deterministically based on the user's WireGuard public key (which rotates only every 1–30 days or never with third-party clients).
> - Due to the underlying behavior of seed-based RNGs (like Rust's `random_range`), the assigned exit IP occupies a constant percentile across different servers, severely restricting the overall combination space.
> - This correlation enables fingerprinting: tracking exit IPs across different servers narrows a user's identity down to a small percentage (~0.34%) of the user pool, allowing correlation attacks with >99% confidence.
> - Mitigations include Mullvad's server-side update to scramble exit IP positions, and user actions such as forcing key rotations or avoiding frequent server switches.
>
> **Concept links:** [[Virtual Private Networks]], [[Anonymity and Privacy]], [[Fingerprinting]], [[IP Addresses]], [[WireGuard]], [[RNG Seed Vulnerability]], [[Traffic Correlation]]
>
> **Suggested connections:**
> - [[Referer Reality]] — exploring how browser attributes, HTTP headers, and networking parameters like exit IPs can be combined to fingerprint users.
> - [[Reticulum, a secure and anonymous mesh networking stack]] — looking at alternative, cryptographic routing protocols designed to eliminate metadata leaks.
<!-- ai-summary:end -->

# [Mullvad exit IPs are surprisingly identifying](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/)

## Digest Summary
Mullvad assigns each WireGuard key a deterministic exit‑IP per server rather than randomizing on every connection. The key rotates every 1–30 days (or never with third‑party clients). Testing 9 servers with 3 650 keys showed only 284 distinct IP‑combination patterns despite a theoretical pool of >8 trillion possibilities. Each assigned IP occupies the same percentile within its server’s IP range, indicating a seed‑based RNG where the seed derives from the public key and the upper bound is the pool size. The RNG’s float multiplier is constant for a given seed, so changing the bound only scales the result, producing identical ratios across servers. Consequently, users sharing a key obtain correlated IPs, allowing fingerprinting: a float range estimate links ≈0.34 % of users (≈340 of 100 k active accounts) to the same IP pattern, giving >99 % confidence in identity correlation across different servers. Mitigations include limiting server switches per key and forcing key rotation by logging out of the Mullvad app.

## Discussion Summary
The discussion centers on Mullvad’s deterministic exit‑IP assignment, with many commenters viewing it as a privacy weakness that makes VPN users distinguishable and vulnerable to de‑anonymisation, especially compared with Tor’s design. Several participants argue that VPNs are unsuitable for true anonymity, citing IP pool blacklisting and the ease of fingerprinting, while others note the potential for site operators to exploit the stability for bans and suggest that a simple randomisation fix would be preferable. Overall sentiment is critical of the current approach and skeptical of VPNs as privacy tools.

---

## Full Article

*Update 5/29: Mullvad has begun rolling out a mitigation feature on their servers that scrambles exit IP positions, thereby fixing this issue. IPs are still deterministically selected based on the pubkey.*

Mullvad is one of the few VPN providers that offers multiple exit IPs for its servers. If two people connect to the same server, they will usually end up with different public IPs.

With only 578 servers (compared to [Proton VPN’s 20,000](https://protonvpn.com/vpn-servers)), this kind of vertical scaling makes sense to avoid cramming too many users onto one IP, which would be a problem on sites with overzealous IP blocks and ratelimits.

Surprisingly, the exit IP you are given is not randomized each time you connect to the server, but deterministically picked [based on your WireGuard key](https://github.com/mullvad/mullvadvpn-app/issues/3777#issuecomment-1196825360), which [rotates every 1 to 30 days](https://github.com/mullvad/mullvadvpn-app/blob/dd150ac3906fb8eccc60e2fabf9ee035636d1aa9/mullvad-types/src/wireguard.rs#L9) (unless you use a third-party client, in which case it never rotates).

But wait.. if each server assigns you an independently picked static exit IP, wouldn’t just a few of those be enough to uniquely identify you among every other Mullvad user?

Putting it to the test
----------------------

I wrote a script that repeatedly changes my pubkey and fetches exit IPs for a set of 9 servers. Leaving it running for a night produced data points for 3650 pubkeys, which is enough to map out the exit IP range for each server:

| Hostname | Start IP | End IP | # IPs |
| --- | --- | --- | --- |
| au-syd-wg-101 | 103.136.147.5 | 103.136.147.64 | 60 |
| cl-scl-wg-001 | 149.88.104.4 | 149.88.104.14 | 11 |
| de-ber-wg-007 | 193.32.248.245 | 193.32.248.252 | 8 |
| dk-cph-wg-002 | 45.129.56.196 | 45.129.56.226 | 31 |
| fi-hel-wg-201 | 185.65.133.10 | 185.65.133.75 | 66 |
| us-lax-wg-001 | 23.234.72.36 | 23.234.72.126 | 91 |
| us-nyc-wg-602 | 146.70.168.132 | 146.70.168.190 | 59 |
| us-sjc-wg-302 | 142.147.89.212 | 142.147.89.224 | 13 |
| za-jnb-wg-002 | 154.47.30.145 | 154.47.30.155 | 11 |

The sizes of these pools add up to over 8.2 trillion exit IP combinations, so you’d think that every pubkey would be assigned a unique set of IPs, since the odds of a collision are so astronomically low.

And yet, somehow all the 3650 pubkeys I tested were assigned just one of [284 combinations](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/pubkeys.txt).

What’s going on here?

Different IPs, same proportion
------------------------------

You can calculate a numerical position for an exit IP by counting its distance from the pool’s starting IP.

For example, the IP `103.136.147.53` assigned by `au-syd-wg-101` would have a 1-based index of 49 (X.X.X.53 - X.X.X.5 + 1).

Now, if you take the IP positions for any of the 284 combinations linked above, and you divide them by pool size, a common ratio emerges:

| Server | IP | Position | Pool size | Ratio |
| --- | --- | --- | --- | --- |
| au-syd-wg-101 | 103.136.147.53 | 49 | 60 | 0.816 |
| cl-scl-wg-001 | 149.88.104.12 | 9 | 11 | 0.818 |
| de-ber-wg-007 | 193.32.248.251 | 7 | 8 | 0.875 |
| dk-cph-wg-002 | 45.129.56.220 | 25 | 31 | 0.806 |
| fi-hel-wg-201 | 185.65.133.63 | 54 | 66 | 0.818 |
| us-lax-wg-001 | 23.234.72.109 | 74 | 91 | 0.813 |
| us-nyc-wg-602 | 146.70.168.179 | 48 | 59 | 0.813 |
| us-sjc-wg-302 | 142.147.89.222 | 11 | 13 | 0.846 |
| za-jnb-wg-002 | 154.47.30.153 | 9 | 11 | 0.818 |

Each IP lands within the same percentile of its pool, in this case, the 81st.

This explains the limited number of combinations, Mullvad will only assign neighboring exit IPs across all its servers. But why?

Feature or bug?
---------------

Curiously, the servers `cl-scl-wg-001` and `za-jnb-wg-002` consistently share IP indexes with each other across all 284 observed IP combinations.

The thing they have in common is a pool size of 11, and this gives us a clue about what’s happening.

In any language, if you initiate an RNG with a static seed, a rand-between call with the same bounds will always produce the same result:

```
use rand::{Rng, SeedableRng};
use rand::rngs::StdRng;

fn main() {
    let seed = 1234;
    for _ in 1..100 {
        let mut rng = StdRng::seed_from_u64(seed);
        let number = rng.random_range(0..1000);
        println!("{}", number) // will always print 56
    }
}
```

So, the shared indexes between these two servers indicate that Mullvad is probably using some sort of seed-based RNG to pick exit IP indexes, where the seed is the pubkey (or possibly the tunnel address) and the upper bound parameter is the pool size.

This is fairly straightforward, but what happens when the bounds are changed?

```
use rand::{Rng, SeedableRng};
use rand::rngs::StdRng;

fn main() {
    let seed = 12345;
    for bound in 10..100 {
        let mut rng = StdRng::seed_from_u64(seed);
        let number = rng.random_range(0..bound);
        let ratio = number as f64 / bound as f64;
        println!("{} {:.3} ", number, ratio)
    }
}
```

```
5 0.500 
5 0.455 
6 0.500 
6 0.462 
7 0.500 
7 0.467 
8 0.500 
9 0.529 
9 0.500 
10 0.526 
10 0.500 
11 0.524 
11 0.500 
12 0.522 
12 0.500 
13 0.520 
13 0.500 
14 0.519 
14 0.500 
15 0.517
...
```

As it turns out, the entropy pool of the RNG is unaffected by the bounds you provide, and at least in Rust, the same float is generated on each first call and applied as a multiplier to the bounds, like so: `min + round((max - min) * float)` (this may be a giant oversimplification)

This lines up with the behavior we’ve seen in Mullvad’s exit IP picking algorithm, so it’s safe to say that this is the cause of it.

Rust as the backend language makes sense too, considering that [the client](https://github.com/mullvad/mullvadvpn-app) is written in it.

The thing is, almost none of my programmer friends were able to accurately describe what `random_range` would produce in the second code snippet, and the actual behavior took me by surprise too. It’s reasonable to think that each increment to the bounds would skew with the entropy and result in a different number, even though that’s not what happens.

Is it possible that the Mullvad devs shared this common misconception, while actually intending for there to be an unbounded number of exit IP combinations? I don’t know, but it’s a funny thought.

Correlating identities
----------------------

I made a tool that can deduce the minimum and maximum float value for a given combination of IPs, available at <https://tmctmt.github.io/mullvad-seed-estimator/>.

![](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/tool.png)

This particular set of IPs in the screenshot resolves to a float value between 0.2909 and 0.2943 for a difference of 0.0034, which means that 0.34% of Mullvad users share these IPs. At a ball park estimate of a 100,000 active Mullvad users, this equates to 340 users.

This is definitely not as unique as I originally thought, but at the same time, >99% accuracy is really not that bad?

As an example, imagine that you are a moderator on a forum and you suspect that a new face is actually a sockpuppet of a user you banned the day prior. You check the IP logs, and despite using different Mullvad servers, both accounts resolve to the overlapping float ranges `0.4334 - 0.4428` and `0.4358 - 0.4423`. This gives you a >99% chance that they are the same person.

Now apply this to IP logs obtained through data breaches and legal channels and you can see how you could get deanonymized behind a VPN through similar correlation attacks.

Protecting yourself
-------------------

* Avoid switching servers more than once per pubkey
* Force rotate your pubkey by logging out of the Mullvad app