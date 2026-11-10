---
title: "Show HN: Sub-millisecond VM sandboxes using CoW memory forking"
url: https://github.com/adammiribyan/zeroboot
clipped: 2026-06-17 01:31:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Sub-millisecond VM sandboxes using CoW memory forking](https://github.com/adammiribyan/zeroboot)

## Digest Summary
Zeroboot provides sub‑millisecond sandboxing for AI agents by launching each sandbox as a full KVM virtual machine with hardware‑enforced memory isolation. A one‑time “template” step boots a Firecracker VM, pre‑loads the desired runtime, and snapshots its memory and CPU state. Subsequent forks create new KVM VMs in ~0.8 ms by memory‑mapping the snapshot with `MAP_PRIVATE` (copy‑on‑write) and restoring the saved CPU registers. The resulting VMs are isolated from each other despite sharing the snapshot base. The project includes SDKs for Python (`from zeroboot import Sandbox`) and TypeScript (`import { Sandbox } from "@zeroboot/sdk"`), allowing code execution via a simple API (`POST https://api.zeroboot.dev/v1/exec`). The prototype is functional but not production‑hardened; contributors are invited to open issues. The code is released under the Apache‑2.0 license.

## Discussion Summary
The discussion acknowledges the security risk of duplicated entropy in cloned random number generators while praising the snapshot support added by the Firecracker team. Users report successful experiments with VM cloning, noting reliable operation but considerable setup effort for networking and a preference for clean systemd starts when startup latency is acceptable. There is enthusiasm for applying the technique to lightweight workloads such as Python interpreters, alongside questions about version specificity, CPU limits, memory overhead, and the complexity of scaling snapshots across production nodes.

---

## Full Article

![Zeroboot](https://github.com/zerobootdev/zeroboot/raw/main/assets/logo-light.svg)

**Sub-millisecond VM sandboxes for AI agents via copy-on-write forking**

[![License](https://camo.githubusercontent.com/35b94db23d3ed026343335f74d52ce31e74b77ad7dab4e4b89f49f2026e0937f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d2d322e302d626c7565)](https://github.com/zerobootdev/zeroboot/blob/main/LICENSE)
[![Rust](https://camo.githubusercontent.com/7cfec40ae345af0c0469e722fa5883390e9d3ca5b3c3258fd814230a0216da4b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d323032315f65646974696f6e2d6f72616e6765)](https://www.rust-lang.org)
[![API Status](https://camo.githubusercontent.com/197c21df42e701776d433b48446829e6d3e438d018ce17593fc0dc380de9913e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6170692d6c6976652d627269676874677265656e)](https://api.zeroboot.dev/v1/health)

---

[![demo](https://github.com/zerobootdev/zeroboot/raw/main/demo/demo.gif)](https://github.com/zerobootdev/zeroboot/blob/main/demo/demo.gif)

```
curl -X POST https://api.zeroboot.dev/v1/exec \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer zb_demo_hn2026' \
  -d '{"code":"import numpy as np; print(np.random.rand(3))"}'
```

| Metric | Zeroboot | E2B | microsandbox | Daytona |
| --- | --- | --- | --- | --- |
| Spawn latency p50 | **0.79ms** | ~150ms | ~200ms | ~27ms |
| Spawn latency p99 | 1.74ms | ~300ms | ~400ms | ~90ms |
| Memory per sandbox | ~265KB | ~128MB | ~50MB | ~50MB |
| Fork + exec (Python) | **~8ms** | - | - | - |
| 1000 concurrent forks | 815ms | - | - | - |

Each sandbox is a real KVM virtual machine with hardware-enforced memory isolation.

```
  Firecracker snapshot ──► mmap(MAP_PRIVATE) ──► KVM VM + restored CPU state
                              (copy-on-write)         (~0.8ms)
```

1. **Template** (one-time): Firecracker boots a VM, pre-loads your runtime, and snapshots memory + CPU state
2. **Fork** (~0.8ms): Creates a new KVM VM, maps snapshot memory as CoW, restores all CPU state
3. **Isolation**: Each fork is a separate KVM VM with hardware-enforced memory isolation

**Python** — [sdk/python](https://github.com/zerobootdev/zeroboot/blob/main/sdk/python)

```
from zeroboot import Sandbox
sb = Sandbox("zb_live_your_key")
result = sb.run("print(1 + 1)")
```

**TypeScript** — [sdk/node](https://github.com/zerobootdev/zeroboot/blob/main/sdk/node)

```
import { Sandbox } from "@zeroboot/sdk";
const result = await new Sandbox("zb_live_your_key").run("console.log(1+1)");
```

Working prototype. The fork primitive, benchmarks, and API are real, but not production-hardened yet. [Open an issue](https://github.com/adammiribyan/zeroboot/issues) if you're interested.

Zeroboot is open source. Self-host it on any Linux box with KVM, or use the managed API:

```
curl -X POST https://api.zeroboot.dev/v1/exec \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer zb_demo_hn2026' \
  -d '{"code":"import numpy as np; print(np.random.rand(3))"}'
```

Building the managed service for teams that don't want to run their own infra. Sign up for early access: <https://tally.so/r/aQGkpb>

* Forks share CSPRNG state from the snapshot. Kernel entropy is reseeded via RNDADDENTROPY but userspace PRNGs (numpy, OpenSSL) need explicit reseeding per fork. See [Firecracker's guidance](https://github.com/firecracker-microvm/firecracker/blob/main/docs/snapshotting/random-for-clones.md).
* Single vCPU per fork. Multi-vCPU is architecturally possible but not implemented.
* No networking inside forks. Sandboxes communicate via serial I/O only.
* Template updates require a full re-snapshot (~15s). No incremental patching.

[Apache-2.0](https://github.com/zerobootdev/zeroboot/blob/main/LICENSE)