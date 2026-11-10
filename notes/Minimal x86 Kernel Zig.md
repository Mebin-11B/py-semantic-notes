---
title: "Minimal x86 Kernel Zig"
url: https://github.com/lopespm/zig-minimal-kernel-x86
clipped: 2026-06-17 01:43:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Minimal x86 Kernel Zig](https://github.com/lopespm/zig-minimal-kernel-x86)

## Digest Summary
The repository “zig‑minimal‑kernel‑x86” hosts a minimal x86 kernel implementation written in the Zig programming language. The page currently returns an access restriction message (“You can’t perform that action at this time”), limiting visibility of additional details. An accompanying screenshot is referenced but not described. No further technical specifications, code excerpts, or documentation are available in the provided text.

## Discussion Summary
The overall reaction is favorable, with commenters praising the implementation as neat and providing a clarification that although the image boots in QEMU, a bootloader like GRUB will likely be necessary for real‑world hardware. A reference to additional resources on Zig bare‑bones development is also shared, suggesting users see practical potential but recognize extra steps for deployment.

---

## Full Article

Minimal x86 Kernel - built in Zig
=================================

A minimal bare-metal kernel written entirely in Zig (zero assembly files).
It boots on an x86 (i386) machine via the Multiboot 1 protocol and prints a
coloured greeting to the VGA text-mode display, then halts the CPU.

The project is designed to be cross-compiled from any host (including Apple
Silicon Macs) and tested instantly with QEMU. It can be booted directly via
QEMU's built-in Multiboot loader or through a GRUB rescue ISO.

1. QEMU loads the ELF binary using its built-in Multiboot 1 support.
2. The CPU starts in 32-bit protected mode at the `_start` entry point.
3. `_start` sets up a 16 KiB stack and jumps to `kmain`.
4. `kmain` clears the VGA text buffer and writes a message to the screen.
5. The CPU enters an infinite `hlt` loop.

| Tool | Version | Install |
| --- | --- | --- |
| **Zig** | 0.14.0+ | [ziglang.org/download](https://ziglang.org/download/) or `brew install zig` |
| **QEMU** | any recent | `brew install qemu` / `nix-env -iA nixpkgs.qemu` |
| **Docker** | any recent | [docker.com](https://www.docker.com/) *(only needed for GRUB ISO builds)* |

Zig bundles its own LLVM back-end and linker, so cross-compilation to
`x86-freestanding-none` works out of the box on any host OS and architecture
(macOS ARM, Linux x86\_64, etc.). Docker is only required for building the
GRUB ISO, since `grub-pc-bin` is an x86 Linux package.

### Option 1: Direct Multiboot (no GRUB)

```
# Build the kernel (produces zig-out/bin/kernel)
zig build

# Boot it in QEMU (opens a graphical VGA window)
zig build run

# Or use the helper script (curses mode, auto-kills after a few seconds)
chmod +x run.sh
./run.sh
```

To run QEMU manually with custom flags:

```
qemu-system-i386 -kernel zig-out/bin/kernel
```

You should see this:

[![Screenshot 2026-02-17 at 23 58 16](https://private-user-images.githubusercontent.com/3640622/551244410-e53f6920-c06b-4586-b551-6b916a7b3d5a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDExMzIsIm5iZiI6MTc4MTY0MDgzMiwicGF0aCI6Ii8zNjQwNjIyLzU1MTI0NDQxMC1lNTNmNjkyMC1jMDZiLTQ1ODYtYjU1MS02YjkxNmE3YjNkNWEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAxMzUyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzAwYzg4YTk2ZWRjNTI5OTA5ZjBlNzkxNmM4MmZmYTNlOGRkYWVlYTIxYjBlYTM0NmQ3YThjN2Q3NmNmOGFkYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.KlvFrGQMJd-33Byof-0cgP1trIWDW0rTTC3iwna5Pss)](https://private-user-images.githubusercontent.com/3640622/551244410-e53f6920-c06b-4586-b551-6b916a7b3d5a.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDExMzIsIm5iZiI6MTc4MTY0MDgzMiwicGF0aCI6Ii8zNjQwNjIyLzU1MTI0NDQxMC1lNTNmNjkyMC1jMDZiLTQ1ODYtYjU1MS02YjkxNmE3YjNkNWEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAxMzUyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzAwYzg4YTk2ZWRjNTI5OTA5ZjBlNzkxNmM4MmZmYTNlOGRkYWVlYTIxYjBlYTM0NmQ3YThjN2Q3NmNmOGFkYiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.KlvFrGQMJd-33Byof-0cgP1trIWDW0rTTC3iwna5Pss)

### Option 2: GRUB rescue ISO

This builds a bootable ISO with a GRUB menu using Docker, then launches it
in QEMU:

```
chmod +x run-grub.sh
./run-grub.sh
```

You should see this:

[![Screenshot 2026-02-19 at 00 29 04](https://private-user-images.githubusercontent.com/3640622/551839018-b8f3c05b-8f3a-4478-bb3f-fcfabcfc5c01.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDExMzIsIm5iZiI6MTc4MTY0MDgzMiwicGF0aCI6Ii8zNjQwNjIyLzU1MTgzOTAxOC1iOGYzYzA1Yi04ZjNhLTQ0NzgtYmIzZi1mY2ZhYmNmYzVjMDEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAxMzUyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmRmY2MwNTQ1ZGJlM2IyMGFhNTNiNjZhMDczYzE4MzFjYTQ1Yzk0NDYwOWMwY2NkMzA0YTJlMWI2ZWFkZDhlZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.nYoD0w8y3Mw5ZVhAGLG8YIxd2wPfB3tZX8ePeGe6FAQ)](https://private-user-images.githubusercontent.com/3640622/551839018-b8f3c05b-8f3a-4478-bb3f-fcfabcfc5c01.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDExMzIsIm5iZiI6MTc4MTY0MDgzMiwicGF0aCI6Ii8zNjQwNjIyLzU1MTgzOTAxOC1iOGYzYzA1Yi04ZjNhLTQ0NzgtYmIzZi1mY2ZhYmNmYzVjMDEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDYxNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MTZUMjAxMzUyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmRmY2MwNTQ1ZGJlM2IyMGFhNTNiNjZhMDczYzE4MzFjYTQ1Yzk0NDYwOWMwY2NkMzA0YTJlMWI2ZWFkZDhlZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.nYoD0w8y3Mw5ZVhAGLG8YIxd2wPfB3tZX8ePeGe6FAQ)

The script performs the following steps:

1. Builds the kernel with `zig build`
2. Creates an `iso/boot/grub/` directory structure with a `grub.cfg`
3. Runs `grub-mkrescue` inside a Docker container (`--platform linux/amd64`)
   to produce `zig-kernel.iso`
4. Boots the ISO with `qemu-system-i386 -cdrom zig-kernel.iso`

```
zig-kernel/
├── build.zig          Zig build script (target, linker, QEMU run step)
├── build.zig.zon      Package manifest
├── linker.ld          Linker script (section layout, entry point)
├── run.sh             Quick-test shell script (direct Multiboot via QEMU)
├── run-grub.sh        Full GRUB ISO build + QEMU boot script
└── src/
    └── main.zig       Entire kernel: Multiboot header, VGA driver, kmain
```

```
 HOST (macOS ARM / any OS)                    EMULATED x86 MACHINE (QEMU)
 ─────────────────────────                    ──────────────────────────────

 ┌──────────────┐   zig build    ┌────────────────────┐
 │  src/main.zig│───────────────▶│  zig-out/bin/kernel│  (i386 ELF binary)
 │  linker.ld   │  cross-compile │  Multiboot 1 magic │
 │  build.zig   │  x86-free-     │  at offset 0       │
 └──────────────┘  standing-none └─────────┬──────────┘
                                          │
                               qemu-system-i386 -kernel
                                          │
                                          ▼
                               ┌──────────────────────┐
                               │      QEMU / TCG      │
                               │  (x86 CPU emulation) │
                               └─────────┬────────────┘
                                          │
                    ┌─────────────────────┼───────────────────────┐
                    │   Emulated i386 hardware                    │
                    │                     │                       │
                    │   1. Multiboot      │                       │
                    │      loader reads   ▼                       │
                    │      ELF, puts   ┌───────────┐              │
                    │      CPU in      │  _start   │  32-bit      │
                    │      protected   │  (naked)  │  protected   │
                    │      mode        └────┬──────┘  mode        │
                    │                       │                     │
                    │              set up   │ stack               │
                    │                       ▼                     │
                    │                 ┌──────────┐                │
                    │                 │  kmain   │                │
                    │                 └────┬─────┘                │
                    │                      │                      │
                    │          ┌───────────┼───────────┐          │
                    │          │           │           │          │
                    │          ▼           ▼           ▼          │
                    │   clearScreen()  print(...)   hlt loop      │
                    │          │           │                      │
                    │          ▼           ▼                      │
                    │   ┌──────────────────────────────────┐      │
                    │   │  VGA Text Buffer at 0xB8000      │      │
                    │   │  80×25 grid, 16-bit per cell     │      │
                    │   │  (ASCII byte + colour attribute) │      │
                    │   └──────────────────────────────────┘      │
                    │                     │                       │
                    └─────────────────────┼───────────────────────┘
                                          │
                                          ▼
                               ┌──────────────────────┐
                               │   QEMU VGA Window    │
                               │                      │
                               │  ════════════════    │
                               │  Hello from the      │
                               │    Zig Kernel!       │
                               │  ════════════════    │
                               │                      │
                               └──────────────────────┘
```

* **Target:** `x86-freestanding-none` — 32-bit, no OS, no libc
* **Boot protocol:** Multiboot 1 — a 12-byte header (magic `0x1BADB002`,
  flags, checksum) placed in the first 8 KiB of the ELF
* **VGA output:** Direct memory-mapped I/O to `0xB8000` using Zig's
  `volatile` pointer semantics — no drivers, no BIOS calls
* **Red zone:** Disabled — the System V ABI red zone would be corrupted by
  hardware interrupts
* **SSE/AVX:** Disabled — avoids the need to save/restore FPU state
* **No assembly files:** The Multiboot header is a Zig `extern struct`
  exported to a linker section; the entry point uses inline `asm volatile`