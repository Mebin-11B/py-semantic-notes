---
title: "Show HN: Smol machines – subsecond coldstart, portable virtual machines"
url: https://github.com/smol-machines/smolvm
clipped: 2026-06-17 01:15:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Smol machines – subsecond coldstart, portable virtual machines](https://github.com/smol-machines/smolvm)

## Digest Summary
- smolvm is a cross‑platform CLI for creating and running lightweight Linux micro‑VMs on macOS (Hypervisor.framework) and Linux (KVM) via libkrunVMM/libkrunfw.  
- VMs start in <200 ms with sub‑second cold‑start times, defaulting to 4 vCPUs and 8 GiB RAM; memory is elastic through virtio ballooning and idle vCPU threads sleep in the hypervisor.  
- A VM can be packaged into a single “.smolmachine” file for portable rehydration on any host with matching architecture, requiring no runtime downloads.  
- Ephemeral runs (`smolvm machine run`) support optional networking (`--net`) and host‑allow‑list (`--allow-host`) to restrict egress; network is disabled by default.  
- Persistent VMs (`machine create/start/stop`) retain installed packages and allow exec commands, volume mounts (directories only), and SSH‑agent forwarding without exposing private keys.  
- `smolvm pack create` converts an image (e.g., python:3.12‑alpine) into a self‑contained executable that runs the workload directly.  
- Configuration can be declaratively expressed in a TOML “Smolfile”, specifying image, networking, allowed hosts, init scripts, volumes, and SSH‑agent usage.  
- Resource limits can be overridden with `--cpus` and `--mem`.  
- On macOS the binary must be signed with Hypervisor.framework entitlements; on Linux `/dev/kvm` access is required.  
- The project is Apache‑2.0 licensed and hosted at github.com/smol‑machines/smolvm.

## Discussion Summary
The comments are overwhelmingly positive, praising the project’s speed, isolation, and ergonomic blend of container‑like workflows with micro‑VM performance. Users express interest in its sub‑second startup, language‑agnostic packaging, and potential for benchmarking, agent execution, and per‑customer back‑ends, while noting the responsive development team. Recurrent questions focus on image sourcing and registries, support for Windows/WSL, integration with existing orchestrators, resource specification, digital signing, GPU access, and handling of nested containers, indicating demand for broader platform and feature compatibility.

---

## Full Article

[![smol machines](https://github.com/smol-machines/smolvm/raw/main/assets/logo.png)](https://github.com/smol-machines/smolvm/blob/main/assets/logo.png)

[![Discord](https://camo.githubusercontent.com/397741123d69503a0a224452a3629154669e9a870686f0c21c68527c7d8faa07/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d4a6f696e2d3538363546323f6c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/E5r8rEWY9J)
[![Release](https://camo.githubusercontent.com/f908428715a4564a8b4dc231a0fb725c62afb07cb6144146a47b08aa3a629d97/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f736d6f6c2d6d616368696e65732f736d6f6c766d3f6c6162656c3d52656c65617365)](https://github.com/smol-machines/smolvm/releases)
[![License](https://camo.githubusercontent.com/5b60841bea9e11d9d0b0950d690c9bc554e06385634056a7d5d62a15d1a4eabe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368655f322e302d626c75652e737667)](https://github.com/smol-machines/smolvm/blob/main/LICENSE)

Ship and run software with isolation by default.

This is a CLI tool that lets you:

1. Manage and run custom Linux virtual machines locally with: sub-second cold start, cross-platform (macOS, Linux), elastic memory usage.
2. Pack a stateful virtual machine into a single file (.smolmachine) to rehydrate on any supported platform.

```
# install (macOS + Linux)
curl -sSL https://smolmachines.com/install.sh | bash

# for coding agents — install + discover all commands
curl -sSL https://smolmachines.com/install.sh | bash && smolvm --help
```

Or download from [GitHub Releases](https://github.com/smol-machines/smolvm/releases), and place it into `~/.local/share/`.

```
# run a command in an ephemeral VM (cleaned up after exit)
smolvm machine run --net --image alpine -- sh -c "echo 'Hello world from a microVM' && uname -a"

# interactive shell
smolvm machine run --net -it --image alpine -- /bin/sh
# inside the VM: apk add sl && sl && exit
```

**Sandbox untrusted code** — run untrusted programs in a hardware-isolated VM. Host filesystem, network, and credentials are separated by a hypervisor boundary.

```
# network is off by default — untrusted code can't phone home
smolvm machine run --image alpine -- nslookup example.com
# fails — no network access

# lock down egress — only allow specific hosts
smolvm machine run --net --image alpine --allow-host registry.npmjs.org -- wget -q -O /dev/null https://registry.npmjs.org
# works — allowed host

smolvm machine run --net --image alpine --allow-host registry.npmjs.org -- wget -q -O /dev/null https://google.com
# fails — not in allow list
```

**Pack into portable executables** — turn any workload into a self-contained binary. All dependencies are pre-baked — no install step, no runtime downloads, boots in <200ms.

```
smolvm pack create --image python:3.12-alpine -o ./python312
./python312 run -- python3 --version
# Python 3.12.x — isolated, no pyenv/venv/conda needed
```

**Use local container images** — for CI, air-gapped hosts, and fast iteration. Feed `--image` a `docker save` / `podman save` archive, pipe one on stdin, or point it at an unpacked rootfs directory. Image work is delegated to your container tooling; smolvm just boots the result.

```
# build locally, run in the VM with no push/pull
docker build -t myapp .
docker save myapp | smolvm machine run --image - -- ./app

# from an archive file (boots with no network)
smolvm machine run --image ./myapp.tar -- ./app

# from an already-unpacked rootfs directory
smolvm machine run --image ./rootfs/ -- ./app
```

**Persistent machines for development** — create, stop, start. Installed packages survive restarts.

```
smolvm machine create --net --name myvm
smolvm machine start --name myvm
smolvm machine exec --name myvm -- apk add sl
smolvm machine exec --name myvm -it -- /bin/sh
# inside: sl, ls, uname -a — type 'exit' to leave
smolvm machine stop --name myvm
```

**Use git and SSH without exposing keys** — forward your host SSH agent into the VM. Private keys never enter the guest — the hypervisor enforces this. Requires an SSH agent running on your host (`ssh-add -l` to check).

```
smolvm machine run --ssh-agent --net --image alpine -- sh -c "apk add -q openssh-client && ssh-add -l"
# lists your host keys, but they can't be extracted from inside the VM

smolvm machine exec --name myvm -- git clone git@github.com:org/private-repo.git
```

**Declare environments with a Smolfile** — reproducible VM config in a simple TOML file.

```
image = "python:3.12-alpine"
net = true

[network]
allow_hosts = ["api.stripe.com", "db.example.com"]

[dev]
init = ["pip install -r requirements.txt"]
volumes = ["./src:/app"]

[auth]
ssh_agent = true
```

```
smolvm machine create --name myvm -s Smolfile
smolvm machine start --name myvm
```

More examples: [python](https://github.com/smol-machines/smolvm/tree/main/examples/python-app) · [node](https://github.com/smol-machines/smolvm/tree/main/examples/node-app) · [doom](https://github.com/smol-machines/smolvm/tree/main/examples/doom-web)

Each workload gets real hardware isolation — its own kernel on [Hypervisor.framework](https://developer.apple.com/documentation/hypervisor) (macOS) or KVM (Linux). [libkrun](https://github.com/containers/libkrun) VMM with custom kernel: [libkrunfw](https://github.com/smol-machines/libkrunfw). Pack it into a `.smolmachine` and it runs anywhere the host architecture matches, with zero dependencies.

Images use the [OCI](https://opencontainers.org/) format — the same open standard Docker uses. Any image on Docker Hub, ghcr.io, or other OCI registries can be pulled and booted as a microVM. No Docker daemon required.

Defaults: 4 vCPUs, 8 GiB RAM. Memory is elastic via virtio balloon — the host only commits what the guest actually uses and reclaims the rest automatically. vCPU threads sleep in the hypervisor when idle, so over-provisioning has near-zero cost. Override with `--cpus` and `--mem`.

|  | smolvm | Containers | Colima | QEMU | Firecracker | Kata |
| --- | --- | --- | --- | --- | --- | --- |
| Isolation | VM per workload | Namespace (shared kernel) | Namespace (1 VM) | Separate VM | Separate VM | VM per container |
| Boot time | <200ms | ~100ms | ~seconds | ~15-30s | <125ms | ~500ms |
| Architecture | Library (libkrun) | Daemon | Daemon (in VM) | Process | Process | Runtime stack |
| Per-workload VMs | Yes | No | No (shared) | Yes | Yes | Yes |
| macOS native | Yes | Via Docker VM | Yes (krunkit) | Yes | No | No |
| Embeddable SDK | Yes | No | No | No | No | No |
| Portable artifacts | `.smolmachine` | Images (need daemon) | No | No | No | No |



| Host | Guest | Requirements |
| --- | --- | --- |
| macOS Apple Silicon | arm64 Linux | macOS 11+ |
| macOS Intel | x86\_64 Linux | macOS 11+ (untested) |
| Linux x86\_64 | x86\_64 Linux | KVM (`/dev/kvm`) |
| Linux aarch64 | aarch64 Linux | KVM (`/dev/kvm`) |

* Network is opt-in (`--net` on `machine create`). TCP/UDP only, no ICMP.
* Volume mounts: directories only (no single files). Mounting at `/workspace` (`-v /host/dir:/workspace`) takes priority over the default storage-disk workspace — your host directory is used instead.
* macOS: binary must be signed with Hypervisor.framework entitlements.
* `--ssh-agent` requires an SSH agent running on the host (`SSH_AUTH_SOCK` must be set).
* GPU acceleration requires libkrun built with `GPU=1` and virglrenderer + a Vulkan driver on the host (see [GPU Acceleration](https://github.com/smol-machines/smolvm#gpu-acceleration) below).

smolvm exposes the host GPU to guests via **virtio-gpu / Venus** (Vulkan-over-virtio). Guest workloads see a real Vulkan device; on Linux + Intel this renders as:

```
ANGLE (Intel, Vulkan 1.4 (Virtio-GPU Venus (Intel(R) UHD Graphics ...)), venus)
```

**macOS** — virglrenderer and MoltenVK are bundled in the smolvm distribution. No extra installs needed.

**Linux** — virglrenderer and a host Vulkan driver must be installed from the system package manager:

| Distro | Packages |
| --- | --- |
| Alpine | `apk add virglrenderer mesa-vulkan-intel` (or `mesa-vulkan-ati` for AMD) |
| Debian/Ubuntu | `apt install virglrenderer0 mesa-vulkan-drivers` |

> virglrenderer depends on libEGL and libdrm from the host GPU driver stack — these are hardware-specific and cannot be bundled. Any GPU-capable Linux host will already have them installed via its GPU driver.

```
# CLI
smolvm machine run --gpu --image alpine -- vulkaninfo --summary

# Smolfile
# gpu = true
# gpu_vram = 2048   # MiB, default 4096
```

The guest Vulkan loader must be pointed at the virtio ICD:

```
export VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/virtio_icd.x86_64.json
```

See [`examples/headless-browser/`](https://github.com/smol-machines/smolvm/blob/main/examples/headless-browser) for a working Chromium setup using ANGLE + Venus for hardware-accelerated WebGL inside a headless VM.

See [docs/DEVELOPMENT.md](https://github.com/smol-machines/smolvm/blob/main/docs/DEVELOPMENT.md).

[Apache-2.0](https://github.com/smol-machines/smolvm/blob/main/LICENSE) · made by [@binsquare](https://github.com/BinSquare) · [twitter](https://x.com/binsquares) · [github](https://github.com/smol-machines/smolvm)