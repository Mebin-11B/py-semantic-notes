---
title: "Tailscale Peer Relays is now generally available"
url: https://tailscale.com/blog/peer-relays-ga
clipped: 2026-06-17 01:43:23
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Tailscale Peer Relays is now generally available](https://tailscale.com/blog/peer-relays-ga)

## Digest Summary
Tailscale Peer Relays are now generally available, offering customer‑deployed, high‑throughput relaying on any Tailscale node. Recent updates improve throughput by optimizing interface selection, reducing lock contention, and distributing traffic across multiple UDP sockets, resulting in performance close to a full mesh even when direct peer‑to‑peer paths are blocked. A new `--relay-server-static-endpoints` flag lets relays advertise fixed IP:port pairs, enabling deployment behind load balancers or strict firewalls (e.g., in public‑cloud subnets) where automatic endpoint discovery fails. Peer Relays integrate with Tailscale’s observability stack: `tailscale ping` can report relay usage and latency; metrics `tailscaled_peer_relay_forwarded_packets_total` and `tailscaled_peer_relay_forwarded_bytes_total` are exposed for Prometheus/Grafana monitoring. They can replace subnet routers, support full‑mesh private subnets, and maintain Tailscale’s end‑to‑end encryption and least‑privilege access. Enabling a relay requires a CLI command and ACL grants, and the feature is available on all Tailscale plans, including the free tier.

## Discussion Summary
Comments show a generally favorable view of Tailscale’s ease of use, performance gains, and the new peer‑relay architecture, especially for NAT‑traversal and low‑latency scenarios. Users also highlight practical applications such as gaming, remote development, and cloud‑run workloads. At the same time, concerns recur about the proprietary client components, dependence on a commercial service, potential future pricing changes, and limited documentation of low‑level behavior. Requests for open‑source alternatives and clearer technical details reflect a desire for transparency while acknowledging the convenience the platform currently provides.

---

## Full Article

When Tailscale works best, it feels effortless, almost boring. Devices connect directly, packets take the shortest possible path, and performance ceases to be a pressing concern.

But real-world networks aren’t always that cooperative. Firewalls, NATs, and cloud networking constraints can block direct peer-to-peer connections. When that happens, Tailscale relies on relays ([DERP](https://tailscale.com/docs/reference/connection-types#derp-connections/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026)) to keep traffic moving securely and reliably.

Today, we’re excited to announce that [Tailscale Peer Relays](https://tailscale.com/docs/features/peer-relay/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026) is now generally available (GA). Peer relays bring customer-deployed, high-throughput relaying to production readiness, giving you a tailnet-native relaying option that you can run on any Tailscale node. Since their [beta release](https://tailscale.com/blog/peer-relays-beta/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026), we’ve shaped Tailscale Peer Relays to deliver major improvements in performance, reliability, and visibility.

What started as a way to work around hard NATs has grown into a production-grade connectivity option. One that gives teams the performance, control, and flexibility they need to scale Tailscale in even the most challenging network environments.

![A flowchart: A Your Network container, with "Your Resource" heading into "Peer relay." From there, traffic hits a "Peer relay ip port exception at the edge of "Network Firewall," and then hits three checkpoints, heading into Resources.](https://cdn.sanity.io/images/w77i7m8x/production/54ca4bc979f85ed7d8a2fa2fb1d78b431083dafc-1055x630.svg?w=3840&q=75&fit=clip&auto=format)

We have made big throughput improvements for Tailscale Peer Relays that are especially noticeable when many clients are forwarding through them. Connecting clients now select a more optimal interface and address family when more than one are available within a single relay, which helps bootstrap and improve overall connection quality. On the relay itself, throughput has increased: packets are handled more efficiently on every Peer Relay because of lock contention improvements, and traffic is now spread across multiple UDP sockets where available.

Together, these changes deliver meaningful gains in both performance and reliability across day-to-day tailnet traffic. Even when direct peer-to-peer connections aren’t possible, peer relays can now achieve performance much closer to a true mesh.

In some environments, particularly in public cloud networks, automatic endpoint discovery isn’t always possible. Instances may sit behind strict firewall rules, rely on port forwarding or load balancers in peered public subnets, or operate in setups where opening arbitrary ports simply isn’t an option. In many cases, the infrastructure in front of those instances can’t run Tailscale directly, making standard discovery mechanisms ineffective.

Peer relays now integrate with static endpoints to address these constraints. Using the `--relay-server-static-endpoints` flag with `tailscale set`, a peer relay can advertise one or more fixed `IP:port` pairs to the tailnet. These endpoints can live behind infrastructure such as an AWS Network Load Balancer, enabling external clients to relay traffic through the peer relay even when automatic endpoint discovery fails.

![Flowchart: A Private Subnet container, with "AWS Resource" inside. A two-way flow from AWS to a Peer Relay has a checkmark in the middle. Traffic is also coming to that Peer Relay, inside a Public Subnet box, from a Static Endpoint inside that Public Subnet, which is sending traffic back to a Network load balancer, and then to a Laptop outside the subnet. Another branch from AWS heads through the Public subnet, to "other Internet-bound traffic," into a NAT gateway, and then to Internet.](https://cdn.sanity.io/images/w77i7m8x/production/25965fd10d29e2384de6d8b1db1bd39cee38dd3d-1055x630.svg?w=3840&q=75&fit=clip&auto=format)

This unlocks high-throughput connectivity in restrictive cloud environments where traditional NAT traversal and endpoint discovery don’t work. Customers can now deploy peer relays behind load balancers and still provide reliable, high-performance relay paths to clients outside those networks.

For many customers, this also means peer relays can replace subnet routers, unlocking full-mesh deployments with core Tailscale features like [Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026) and [MagicDNS](https://tailscale.com/docs/features/magicdns/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026).

Now in general availability, Tailscale Peer Relays also integrate more deeply into Tailscale’s visibility and observability tooling, making relay behavior clear, measurable, and auditable.

Peer relays integrate directly with [tailscale ping](https://tailscale.com/docs/reference/tailscale-cli#ping/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026), allowing you to see whether a relay is being used, whether it’s reachable, and how it impacts latency and reliability when testing connectivity. This removes much of the guesswork from troubleshooting. When issues arise, it’s easy to determine whether traffic is being relayed, whether the relay is healthy, and whether it’s contributing to degraded performance.

For ongoing observability, Tailscale Peer Relays now expose client metrics such as `tailscaled_peer_relay_forwarded_packets_total` and `tailscaled_peer_relay_forwarded_bytes_total`. These metrics can be scraped and exported to monitoring systems like Prometheus and Grafana alongside existing Tailscale client metrics, enabling teams to track relay usage, understand traffic patterns, detect anomalies, and monitor tailnet health at scale.

With general availability, Tailscale Peer Relays become a core building block for scaling Tailscale in real-world networks. They enable:

* High-throughput, low-latency connections when direct paths are unavailable
* Deployments in restricted cloud environments through static endpoints
* Full mesh in private subnets, with controlled ingress/egress paths

At the same time, Tailscale Peer Relays deliver intelligent, resilient path selection across the tailnet, along with first-class observability, auditability, and debuggability. All of this comes without compromising on Tailscale’s foundational guarantees: end-to-end encryption, least-privilege access, and simple, predictable operation.

Getting started is straightforward. Tailscale Peer Relays can be enabled on any supported Tailscale node using the CLI, controlled through grants in your ACLs, and deployed incrementally alongside existing relay infrastructure; you can read more [in our docs](https://tailscale.com/docs/features/peer-relay/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026).

Peer Relays are available on all Tailscale plans, including our free Personal plan. If you need deployment support or have specific throughput goals, don't hesitate to [reach out](https://tailscale.com/contact/sales/?utm_source=blog&utm_medium=content&utm_campaign=tailscale-winter-update-2026).