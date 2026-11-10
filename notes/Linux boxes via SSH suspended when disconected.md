---
title: "Linux boxes via SSH: suspended when disconected"
url: https://shellbox.dev/
clipped: 2026-06-17 01:58:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - cloud computing
  - virtual machines
  - ssh integration
  - usage-based billing
related:
  - "[[Cloud Computing]]"
  - "[[Virtual Machines]]"
  - "[[Usage-Based Billing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Shellbox provides on-demand virtual machines that suspend state on SSH disconnect and resume upon reconnection to minimize billing costs.
>
> **Key points:**
> - Shellbox offers VMs with 2 vCPUs, 4 GB RAM, 50 GB SSD, and HTTPS URL endpoints.
> - Instances preserve their system state by automatically pausing when the user disconnects and resuming on reconnection.
> - Billing is usage-based at $0.05/hour when running and $0.005/hour when paused, with automated stop limits.
>
> **Concept links:** [[Cloud Computing]], [[Virtual Machines]], [[SSH Integration]], [[Usage-Based Billing]]
>
> **Suggested connections:**
> - [[Developer Tooling]] — systems that simplify local-to-cloud development workflows.
> - [[Serverless Infrastructure]] — comparison with other container and VM auto-suspension systems.
<!-- ai-summary:end -->

# [Linux boxes via SSH: suspended when disconected](https://shellbox.dev/)

## Digest Summary
Shellbox provides on‑demand Linux virtual machines accessible solely via SSH. Each instance includes 2 vCPUs, 4 GB RAM and a 50 GB SSD, with a public HTTPS URL and automatic TLS termination. Boxes retain state by pausing on disconnect and resume on reconnection; they stop automatically when the account balance falls below $5. Billing is usage‑based at $0.05 per hour while running and $0.005 per hour while stopped, with prepaid balances, refunds for unused funds, and cost‑control limits. Core CLI commands include `create ` to provision a box, `connect ` to SSH in, `list` to view status and URLs, `billing` for balance and usage details, and `funds ` to add credit. File transfer works via standard `scp`. The service requires no special client or browser plugins, and each box receives a unique public URL.

## Discussion Summary
The comments show a mixed reaction: many view the pricing as higher than comparable providers and question its practicality without a public IP, while others find the on‑demand, suspend‑when‑idle model intriguing and see potential for cost‑saving dev environments or specialized hardware access. Comparisons to existing services such as Hetzner, DigitalOcean, AWS, and similar platforms are common, and several users request clearer documentation, sign‑up flow, and feature details like storage persistence, SFTP support, and security assurances. Overall interest coexists with skepticism about value and usability.

---

## Full Article

We [launched on Hacker News](https://news.ycombinator.com/item?id=46638629). Someone commented: *"Have fun racing to the bottom."*

They have a point. Beating a $4/month Hetzner box sounds impossible. It's not. This post explains how.

**TL;DR:** $0.02/hr running. $0.50/month parked. Cheaper than Hetzner under 186 hrs/month.

What is Shellbox?
-----------------

[Shellbox](https://shellbox.dev/#synopsis) is Linux boxes via SSH. It feels like a 24/7 server - your tmux sessions persist, background jobs resume, `scp` just works - but when you disconnect, the box stops. And so does billing.

Open VS Code, Zed, or a terminal. Connect. That's it. No web console, no "start instance" button, no CLI tools. When you're done, close your laptop. The box suspends, you stop paying, and everything's still there when you come back.

The Problem with Always-On Pricing
----------------------------------

Traditional cloud providers charge you for a VM whether you're using it or not. Hetzner's [CX22](https://www.hetzner.com/cloud) (2 vCPU, 4GB RAM, 40GB SSD) costs a flat rate around the clock. Great if you're running a production server. Wasteful if you're a developer who codes a few hours a day.

"But AWS and Azure let you stop instances!" True. [AWS t3.medium](https://aws.amazon.com/ec2/pricing/on-demand/) costs $0.0416/hr when running. Stop it, and you still pay ~$4/month for 50GB [EBS storage](https://aws.amazon.com/ebs/pricing/). [Azure B2s](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/) is similar. That's 8x our stopped cost, and their running rate is 2x ours.

Developers don't use their dev boxes 24/7. Most of us work 4-8 hours a day, maybe less. Why pay for the other 16-20 hours?

How We Make It Work
-------------------

The key insight: Hetzner (and most providers) need to reserve memory for each VM, even when it's idle. Memory is expensive. Our boxes can stop and resume instantly. When stopped, we need zero memory - just disk space for the snapshot.

Our bottleneck is disk, not memory. And disk is cheap.

The Math
--------

Let's compare shellbox vs the alternatives for a similar spec (2 vCPU, 4GB RAM, 50GB disk):

Shellbox formula: `running_hrs * $0.02 + stopped_hrs * $0.000694`

AWS/Azure formula: `running_hrs * $0.0416 + $4/month storage`

If you use your box less than 186 hours per month, shellbox is cheaper than Hetzner. That's ~8.5 hrs every weekday, or ~6 hrs/day if you code weekends too. AWS/Azure with stop/start is never cheaper than either - you're paying premium rates for the privilege of stopping.

What About Abuse?
-----------------

Won't cheap stopped instances attract crypto miners and other abuse?

Nope. Our *running* costs are roughly 3x Hetzner's rate. If you want to mine bitcoin or run botnets, you'd do it much cheaper elsewhere. Our pricing model naturally selects for legitimate dev workloads: burst usage with long idle periods.

The Competition
---------------

We're not the only ones trying to solve this. Here's how we compare:

**[Sprites.dev](https://sprites.dev)** offers persistent Linux environments with checkpoint/restore. Their pricing: $0.07/CPU-hour + $0.04375/GB-hour. For a 2 vCPU, 4GB RAM instance, that's roughly **$0.315/hr** while running - over 15x our rate. They use Firecracker too, but charge memory by the hour. Also: no real SSH access, only their CLI/API.

**[Exe.dev](https://exe.dev)** offers persistent SSH VMs at $20/month for up to 25 VMs - but here's the catch: all 25 VMs share a pool of just 2 CPUs and 8GB RAM total. Run a few VMs and you're quickly resource-starved. It's a flat subscription, so you pay whether you use them or not.

**AWS and Azure** offer pay-as-you-go too - but it's not the same experience. You have to log into a web console to start your instance, wait 30-60 seconds for it to boot, and remember to stop it when you're done or you keep paying. That's not "connect and code" - that's instance management.

Shellbox also offers features beyond the basics: `duplicate` lets you clone a box instantly - useful for testing changes without risking your setup. Each box gets a web endpoint (`https://<box>.shellbox.dev`) that wakes the VM on request, so you can expose dev servers without keeping the box running 24/7.

How It Works (Technical Details)
--------------------------------

We run on [Hetzner auction servers](https://www.hetzner.com/sb) - dedicated hardware at steep discounts. This gives us predictable costs and full control.

The stack: [Caddy](https://caddyserver.com/) handles TLS and routes traffic. Behind it, a custom Python SSH server built on [asyncssh](https://asyncssh.readthedocs.io/) manages connections. HTTP requests to your box's URL endpoint go through an HTTP proxy that wakes the VM if needed.

Each box runs in an isolated microVM. By default, new boxes use [Firecracker](https://firecracker-microvm.github.io/) for fast snapshots. [Cloud Hypervisor](https://www.cloudhypervisor.org/) is also available via `--ch` when you need Docker and nested virtualization support. Both offer sub-second boot times, strong isolation, and minimal overhead.

**Core/External architecture.** The server is split into two parts. Core handles SSH connections - it's intentionally dumb, stateless, and stable. External handles all business logic: VM lifecycle, billing, commands. External runs as a subprocess, invoked fresh for each operation.

This split enables two things. First, fast disconnects: when you close your session, Core returns immediately. It fires off a background call to External which handles the snapshot and cleanup - you don't wait for it. Second, hot-swappable logic: we can update pricing, add new commands (like `duplicate`), or change billing algorithms without restarting the server or disturbing connected users. The next External call just picks up the new code.

**Snapshots.** When your last session disconnects, the hypervisor pauses the VM and dumps memory to disk. Memory snapshots are memory-mapped files stored on NVMe - the OS pages them efficiently, and resume takes under a second. Rootfs images live on larger HDDs. When you reconnect, we restore from snapshot and you're back exactly where you left off - same processes, same shell history, same everything.

**Btrfs and reflinks.** Our HDD storage uses [btrfs](https://btrfs.readthedocs.io/), which enables copy-on-write via reflinks. When you run `duplicate` to clone a box, we don't copy the entire 50GB disk image - we create a reflink using `cp --reflink=auto`. This is instant (just metadata), and the clone shares blocks with the original. Space is only consumed as you make changes. Creating a new box from the base image works the same way. This is why `duplicate` completes in under a second regardless of disk size.

The Honest Take
---------------

Shellbox isn't for everyone:

* Running 24/7? Use Hetzner. We'll cost you 3x more.
* Need massive RAM? We're currently at 4GB (more options coming).
* Running production? We don't guarantee uptime.

But if you're a developer who wants a Linux box to hack on for a few hours a day, we're probably the cheapest option that actually works. Real SSH. Real persistence. Real savings.

Try it: `ssh shellbox.dev help`