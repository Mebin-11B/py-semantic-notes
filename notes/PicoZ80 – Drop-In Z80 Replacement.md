---
title: "PicoZ80 – Drop-In Z80 Replacement"
url: https://eaw.app/picoz80/
clipped: 2026-06-17 01:19:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [PicoZ80 – Drop-In Z80 Replacement](https://eaw.app/picoz80/)

## Digest Summary
picoZ80 is a drop‑in replacement for the Z80 DIP‑40 CPU that fits directly into legacy Z80‑based computers. It uses a dual‑core RP2350 Cortex‑M33 (up to 300 MHz) whose three PIO blocks provide cycle‑accurate control of the host’s address, data and control lines, preserving original Z80 bus timing while handling every transaction in real time. The board includes 8 MiB external PSRAM (64 × 64 KB banks) and 16 MiB SPI Flash, offering 4 MiB of banked address space per CPU context and 512‑byte‑granular ROM/RAM banking. A co‑processor ESP32‑S3 adds Wi‑Fi, Bluetooth, SD‑card storage and a web‑based management interface; configuration is driven by a single JSON file on the SD card, eliminating recompilation. Virtual‑device support maps any 512‑byte block or I/O range to C functions, enabling floppy/QuickDisk emulation, virtual disks, and other peripherals. Firmware runs on two 5‑MiB partitions with OTA updates via USB or the ESP32. The architecture separates real‑time bus handling (Core 1) from non‑real‑time tasks (Core 0) via an inter‑core message queue, while PIO state machines manage address/data phases, control signals, refresh cycles, wait‑state insertion and T1 synchronization to maintain precise timing across the host system.

## Discussion Summary
The discussion centers on retro‑computer hardware experimentation, especially using the RP2350 to act as a bus‑level participant or in‑circuit emulator for systems like the C64, Z80‑based machines, and Sharp MZ series. Contributors express enthusiasm for cartridge‑based approaches that avoid invasive CPU swaps, note practical tips such as simplifying power regulation, and highlight the potential for detailed debugging through trace memory and cycle‑accurate control. While the project is framed as a hobbyist endeavor, participants also consider possible industrial relevance, acknowledging cost concerns and the broader appeal of preserving and extending classic computing platforms.

---

## Full Article

picoZ80
=======

Overview
--------

The

**picoZ80**

continues the tranZPUter theme, replacing a physical Z80 in a host or industrial computer with a
faster CPU, more memory, virtual devices, networking (WiFi, BT), rapid application loading from SD card and WiFi management.

It is a custom PCB designed to drop directly into the Z80 DIP-40 CPU socket of any legacy Z80-based computer. Rather than using a discrete Z80 processor, the board hosts an

**RP2350B**

microcontroller â a dual-core 150MHz Cortex-M33 device capable of running at up to 300MHz â whose programmable I/O (PIO) state machines take full, cycle-accurate control of the Z80 address, data, and control buses.

The picoZ80 is not a simple emulator adapter. Every bus transaction is handled in real time by the RP2350's PIO engines, giving the host system exactly the same bus timing it would see from a real Z80. At the same time, the RP2350's second core and abundant on-chip SRAM, combined with 8MB of external PSRAM and 16MB of Flash, allow an almost unlimited range of capabilities to be layered on top of the raw Z80 interface â including accelerated execution, virtualised memory, ROM banking, virtual disk drives, and full machine-persona emulation.

An

**ESP32**

co-processor provides WiFi and Bluetooth connectivity, SD-card mass storage, and a browser-based management interface. All configuration is driven from a single human-readable

`config.json`

file stored on the SD card, meaning no recompilation is required to reconfigure the board's memory map, ROM images, or driver selection.

The picoZ80 has been demonstrated running within multiple Sharp MZ machines. A set of personas are being developed for these
machines, indeed for other Z80 systems in time, to provide much needed features, such as banked RAM/ROM, floppy disk emulation,
QuickDisk emulation, ROM Filing System, TranZPUter Filing System, all capable of being functional simultaneously.
The configuration is entirely JSON-driven, adding support for a new Z80-based host is a matter of editing a configuration file and, where new I/O behaviour is required, adding a small C driver
into the codebase.

* Drop-in Z80 replacement  
  - installs in any Z80 DIP-40 socket. The host sees normal Z80 bus timing throughout.
* Cycle-accurate PIO bus interface  
  - three RP2350 PIO state machines handle address, data, and control signals simultaneously at full Z80 bus speed.
* Large memory space  
  - 8MB PSRAM organised as 64 banks Ã 64KB, giving a total of 4MB of banked address space accessible per CPU context.
* ROM/RAM banking  
  - memory blocks are configurable in 512-byte granularity and can be mapped as ROM, RAM, physical host memory, or virtual function handlers.
* Virtual device framework  
  - any 512-byte block of memory or I/O port range can be backed by a C function, enabling fully virtualised peripherals.
* Machine personas  
  - the Z80 firmware can be configured via a JSON config to work within any Z80 host. Personas are available for multiple Sharp MZ machines (MZ-700, MZ-80A, MZ-80B, MZ-2000, MZ-2200, MZ-2500, MZ-1500). The first non-Sharp persona â the Amstrad PCW-9512 â is now supported, with more machines planned. Targeted build variants (BaseZ80, SharpZ80, AmstradZ80) allow machine-specific firmware for reduced binary size.
* Floppy and QuickDisk emulation  
  - WD1773-compatible floppy disk controller and Sharp QuickDisk drive emulation, using DSK/RAW/D88 images on the SD card.
* WiFi and web management  
  - the onboard ESP32 provides a seven-page Bootstrap web interface for configuration, file management, OTA firmware updates, and persona selection.
* ICE debug shell  
  - a 51-command ICE debugger accessible over USB CDC serial provides breakpoints (8 simultaneous), single-step execution, execution trace, Z80 register inspection, memory and I/O read/write, a built-in Z80 disassembler and assembler, disk imaging, bus diagnostics, and system status monitoring.
* Dual firmware partitions  
  - two independent 5MB firmware slots allow safe OTA upgrades; the active partition is selected from the web interface or bootloader.
* USB firmware update  
  - the bootloader exposes a USB bridge for firmware flashing without requiring a hardware debugger.

---

Hardware
--------

The picoZ80 PCB (revision 2.5) is a compact, multi-layer board designed to fit within the physical footprint of the Z80 DIP-40 package and the clearance available inside typical retro-computer cases. All logic operates at 3.3V; level shifting and drive current considerations for the 5V host bus are handled in the schematic design.

The board integrates five subsystems on a single PCB: the RP2350B processor, the Z80 bus interface, the ESP32 co-processor, the power supply, and a USB hub.

Key Components

* RP2350B (Cortex-M33 dual-core)  
  - primary processor, running at up to 300MHz. Executes the Z80 emulation hot loop on Core 1 and handles file I/O, USB, and ESP32 relay on Core 0. 512KB on-chip SRAM. The RP2350B variant (as opposed to RP2350A) provides 48 GPIO pins required for the full Z80 bus.
* 16MB SPI Flash  
  - stores the bootloader, two application firmware slots, two configuration slots, and a general configuration partition. Total addressable layout spans 0x10000000â0x11000000.
* 8MB PSRAM (SPI)  
  - external pseudo-static RAM providing 64 banks Ã 64KB of banked address space for the emulated CPU. Connected to the RP2350 via a dedicated SPI peripheral.
* ESP32 co-processor  
  - provides WiFi (802.11 b/g/n, AP and client modes), Bluetooth, SD-card reader, and web server. Communicates with the RP2350 via a binary IPC protocol over 50MHz FSPI (with CRC32 integrity checking, pre-allocated DMA channels, and burst sector transfers of up to 16 sectors per transaction) and a 460.8kbaud UART for control commands.
* SD card slot  
  - FAT32, managed by the ESP32. Stores `config.json`, ROM images, disk images (DSK, QuickDisk, RAM disk), and TZFS/RFS filing system trees.
* USB hub  
  - on-board USB hub for host connectivity and firmware update bridging.
* 3.3V power supply  
  - efficient buck converter drawing from the 5V present on the Z80 socket VCC pin.

Board Design

The picoZ80 hardware is designed in KiCad. The current revision is

**v2.5**

. Schematic and PCB layout files are available in the project repository under

`kicad/PICOZ80/`

.

The schematic is divided into five sheets:

Sheet 1 â RP2350B Processor

All RP2350B GPIO assignments, decoupling, 12MHz crystal oscillator, 16MB Flash, and 8MB PSRAM connections. The RP2350B QFN-80 package is chosen specifically for its 48-GPIO count â the full Z80 bus (16 address + 8 data + 12 control signals) plus ESP32 SPI/UART and USB signals consume virtually every available pin.

![picoZ80 Schematic Sheet 1 â RP2350B Processor](https://eaw.app/images/picoZ80_sch_rp2350.png)

Sheet 2 â ESP32 Co-processor

ESP32-S3-PICO-1 module, SD card interface (SPI), chip antenna, debug header, and inter-processor communication lines (FSPI bus at 50MHz, UART at 460.8kbaud). The SD card signals and inter-processor SPI/UART are clearly separated in this sheet.

![picoZ80 Schematic Sheet 2 â ESP32 Co-processor](https://eaw.app/images/picoZ80_sch_esp32.png)

Sheet 3 â Z80 Bus Interface

The 40-pin DIP socket connections and bus interface resistor network. Address lines A0âA15, data lines D0âD7, and all Z80 control signals (MREQ, IORQ, RD, WR, M1, RFSH, BUSREQ, BUSACK, HALT, INT, NMI, WAIT, CLK, RESET) are routed through series resistors to dedicated RP2350 GPIO pins monitored by the PIO state machines.

![picoZ80 Schematic Sheet 3 â Z80 Bus Interface](https://eaw.app/images/picoZ80_sch_z80_interface.png)

Sheet 4 â Power Supply

TLV62590BV 5V-to-3.3V synchronous buck converter with input/output filtering capacitors. The converter must supply the combined load of the RP2350B at up to 300MHz, 8MB PSRAM, ESP32, and USB hub from the single 5V VCC pin of the Z80 DIP-40 socket.

![picoZ80 Schematic Sheet 4 â Power Supply](https://eaw.app/images/picoZ80_sch_power_supply.png)

Sheet 5 â USB Hub Controller

CH334F USB hub controller with Mini-B connector, 12MHz crystal, and downstream ports routed to both the RP2350 (for firmware update bridging) and the ESP32 (for direct USB access on newer board revisions).

![picoZ80 Schematic Sheet 5 â USB Hub Controller](https://eaw.app/images/picoZ80_sch_usb_hub.png)

PCB

The PCB was designed as small as possible to accommodate all the necessary circuity and fit within the limits of a DIP-40 socket.

The smallest components which could be manually assembled were used, ie. 0402/0603 passive devices and 0.5mm IC pitch spacing to reduce overall size and a 6 layer stackup selected to fit all required components.

Initial designs, v2.0 and v2.1 were manually assembled with point application of solder, manual part placement and a hot-air rework station. Version 2.2 was manually assembled with a stencil and reflow oven. v2.3a and v2.5 were assembled at a PCB Fab.

PCB Overview
PCB 6 Layer Routing Overview
PCB Assembled
PCB Component Placement and Bill of Materials

Click

[here](https://eaw.app/hardware/ibom_picoZ80_v2.5.html)

to view an interactive PCB component placement diagram and Bill of Materials.

---

Architecture
------------

Dual-Core Design

The RP2350B's two Cortex-M33 cores are given completely separate responsibilities, communicating through an intercore message queue (

`queue_t`

).

**Core 0**

handles all non-real-time tasks: USB bridge and CDC serial, firmware update coordination, file I/O (relayed to the ESP32 over UART), ESP32 command dispatch (floppy/QuickDisk image changes, config reloads, version queries), partition management, and watchdog supervision. A hardware watchdog timer monitors the boot sequence and main loop, with boot progress tracked through RP2350 scratch registers that survive watchdog resets. Comprehensive fault handlers capture register state and diagnostic information to PSRAM, enabling post-reset analysis of hard faults, bus faults, and usage faults. A persistent PSRAM log (

`plogf`

) captures boot-critical messages before USB becomes available, complementing the standard

`debugf`

debug output system.

**Core 1**

runs the CPU emulation hot loop exclusively. It services the PIO FIFOs to process Z80 bus transactions, resolves each address against the memory map, and either passes the transaction to physical host hardware (PHYSICAL type), services it from PSRAM (RAM/ROM types), or calls a virtual device handler function (FUNC type). Latency on this path is minimised by keeping the inner loop in SRAM and using the 512KB RP2350 SRAM as a fast look-up table for memory-block pointers.

PIO Bus Interface

The Z80 bus interface is implemented entirely in RP2350 PIO assembly (

`z80.pio`

). The RP2350 provides three PIO blocks (PIO 0, PIO 1, PIO 2), each with four state machines. The Z80 firmware uses all three PIO blocks:

* PIO 0 â Address and data bus (GPIO 0â23)  
  - handles the 16-bit address bus (A0âA15, GPIO 0â15) and the bidirectional 8-bit data bus (D0âD7, GPIO 16â23). State machines run the `z80_addr` and `z80_data` programs simultaneously, pushing address words and driving or sampling data bytes in synchrony.
* PIO 1 â Control signals, cycle execution, and DRAM refresh (GPIO 16â47)  
  - runs the main bus control programs against the upper GPIO range: the cycle state machine (`z80_cycle`) orchestrates all Z80 bus cycles including integrated DRAM refresh generation, bus request/acknowledge (`z80_busrq`), NMI detection (`z80_nmi`), clock synchronisation (`z80_clk_sync`), and interrupt-acknowledge handling (`z80_int_ack`).
* PIO 2 â Host timing, reset, and wait states  
  - manages the time-critical interactions between the RP2350 and the host Z80 bus that must remain correct even when Core 1 is servicing internal memory. Four dedicated state machines run in PIO 2:
  + **RESET detection** (`z80_reset`) â monitors the host RESET line and signals Core 1 so that the emulation state can be reinitialised cleanly on every hardware reset.
  + **Wait-state generator** (`z80_wait`) â inserts configurable T-cycle wait states (controlled by the `tcycwait` JSON parameter) by asserting /WAIT on the host bus, stretching individual bus cycles to match the timing requirements of slower peripherals or banked ROM/RAM.
  + **T1 synchronisation** (`z80_sync`) â detects the rising edge of T1 on each bus cycle (the point at which the Z80 places a valid address on the bus) and signals Core 1 via IRQ. This synchronisation is essential for applications that rely on the host clock for precise timing â including software delay loops and time-sensitive I/O such as cassette motor control and serial bit-banging â ensuring that RP2350 internal memory operations do not introduce perceptible timing drift.

The full set of PIO programs in

`z80.pio`

, grouped by PIO block:

| PIO | Program | Function |
| --- | --- | --- |
| 0 | `z80_addr` | Outputs 16-bit address (A0âA15) onto the bus and signals cycle start. |
| 0 | `z80_data` | Drives or samples D0âD7, with tri-state control during BUSRQ. |
| 0 | `z80_cycle` | Top-level bus cycle sequencer â orchestrates fetch, read, write, I/O, and DRAM refresh cycles. |
| 0 | `z80_fetch` | Opcode-fetch bus cycle (M1 + MREQ + RD). |
| 1 | `z80_mem_read` | Memory read bus cycle (MREQ + RD). |
| 1 | `z80_mem_write` | Memory write bus cycle (MREQ + WR). |
| 1 | `z80_io_read` | I/O read bus cycle (IORQ + RD). |
| 1 | `z80_io_write` | I/O write bus cycle (IORQ + WR). |
| 1 | `z80_busrq` | Manages BUSREQ/BUSACK, releasing /IORQ, /MREQ, /RFSH, /M1, /HALT, /WR, /RD. |
| 1 | `z80_nmi` | Detects NMI assertion and signals Core 1. |
| 1 | `z80_clk_sync` | Synchronises PIO state machines to the Z80 CLK signal. |
| 1 | `z80_int_ack` | Handles interrupt-acknowledge cycles (M1 + IORQ). |
| 2 | `z80_reset` | Monitors the host RESET line and signals Core 1 to reinitialise emulation state. |
| 2 | `z80_wait` | Inserts configurable T-cycle wait states on the host bus (controlled by `tcycwait`). |
| 2 | `z80_sync` | Detects T1 on each bus cycle and signals Core 1 via IRQ, synchronising internal memory operations to the host clock. |

State machines communicate via PIO IRQ flags rather than polling, which eliminates inter-machine latency: IRQ 0 signals address/cycle start, IRQ 1 signals the data phase, IRQ 2 indicates T1 detection, IRQ 3 signals a RESET event, IRQ 4 signals NMI, and IRQ 6 signals an active BUSRQ.

Because PIO programs execute independently of the Cortex-M33 cores, the bus interface continues to respond deterministically even when Core 1 is occupied with PSRAM accesses or virtual device calls.

Three-Tier Memory Model

Memory accesses are resolved through three tiers of increasing latency:

**Tier 1 â RP2350 SRAM (512KB, zero wait states)**

A 128-entry array of 32-bit

`membankPtr`

values, one per 512-byte block of the full 64KB Z80 address space, gives Core 1 an O(1) block-type lookup for every bus transaction. This array is the inner dispatch table: each entry encodes the block type and, for PSRAM-backed blocks, the PSRAM offset.

**Tier 2 â External PSRAM (8MB, SPI)**

The PSRAM holds 64 banks of 64KB RAM or ROM images, plus a 64KB

`memPtr`

pointer array, a 64KB

`memioPtr`

function-pointer array, and a 64KB

`ioPtr`

I/O function-pointer array. PSRAM access latency is deterministic and handled via the RP2350's SPI peripheral with DMA.

**Tier 3 â 16MB SPI Flash**

Firmware, ROM images, and the minified

`config.json`

are stored in Flash. ROM images are copied from Flash to PSRAM at boot time and are then served from PSRAM at runtime. The Flash is not accessed during normal Z80 bus transactions.

Memory blocks are configured in

**512-byte granularity**

. The available block types are:

| Type | Description |
| --- | --- |
| `PHYSICAL` | Pass-through to real host hardware â the RP2350 releases the bus and lets the physical host memory respond. |
| `PHYSICAL_VRAM` | As PHYSICAL but with additional wait states for host video RAM timing. |
| `PHYSICAL_HW` | Pass-through for host hardware registers. |
| `RAM` | Read/write â backed by PSRAM bank. |
| `ROM` | Read-only â backed by PSRAM bank; write cycles are silently ignored. |
| `VRAM` | PSRAM-backed video RAM; write cycles are also mirrored to the physical host VRAM. |
| `FUNC` | Virtual device â each access triggers a C function call, enabling arbitrary I/O emulation. |
| `PTR` | Per-byte redirect â each byte of the 512-byte block can point to any other block or type. |

Flash Memory Layout

The 16MB Flash is partitioned as follows:

| Partition | Address Range | Size | Contents |
| --- | --- | --- | --- |
| Bootloader | `0x10000000â0x1001FFFF` | 128KB | USB bridge, firmware update, partition selector |
| App Slot 1 | `0x10020000â0x1051FFFF` | 5MB | Main Z80 firmware (partition 1) |
| App Slot 2 | `0x10520000â0x10A1FFFF` | 5MB | Main Z80 firmware (partition 2) |
| App Config 1 | `0x10A20000â0x10C9FFFF` | 2.5MB | ROM images + minified config JSON (slot 1) |
| App Config 2 | `0x10CA0000â0x10F1FFFF` | 2.5MB | ROM images + minified config JSON (slot 2) |
| General Config | `0x10F20000â0x10FFEFFF` | 892KB | Core settings, scratch space |
| Partition Table | `0x10FFF000â0x11000000` | 4KB | Active slot, checksums, metadata |

Each configuration slot can hold up to 64 ROM images and a 64KB minified JSON configuration. The active slot is recorded in the partition table and can be switched from the web interface or by holding the appropriate button during boot.

---

Machine Personas
----------------

The active persona is selected via the web interface Personality page or by editing `config.json`.

Peripheral and Filing-System Drivers

The firmware supports a targeted build system that produces machine-specific binaries:

`pZ80-BaseZ80`

includes all drivers (Sharp + Amstrad),

`pZ80-SharpZ80`

includes only Sharp MZ drivers, and

`pZ80-AmstradZ80`

includes only Amstrad PCW drivers. Each target is controlled by compile-time defines (

`INCLUDE_SHARP_DRIVERS`

,

`INCLUDE_AMSTRAD_DRIVERS`

). The following peripheral drivers are available:

Sharp MZ Series

When built with

`INCLUDE_SHARP_DRIVERS`

, the following Sharp peripheral drivers are compiled in and can be bound to any virtual hardware persona via the JSON configuration:

* MZ700.c â Sharp MZ-700 peripheral set  
  - handles the MZ-700's characteristic bank-switching, video, and keyboard I/O at the peripheral level.
* MZ80A.c â Sharp MZ-80A peripheral set  
  - full MZ-80A machine emulation including the SA-1510 monitor ROM, 2KB VRAM, Intel 8253 PIT (Programmable Interval Timer with all six counter modes), Intel 8255 PPI (Programmable Peripheral Interface), LS367 keyboard scanner, and the MEMSW/MEMSWR memory swap mechanism for CP/M support (swaps monitor ROM at 0x0000 with RAM at 0xC000). Supports both physical (real hardware) and virtual (PSRAM-based) operation, including mixed mode where the driver runs virtually but a physical floppy controller is used. Sub-interfaces: RFS, MZ80AFI, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18.
* MZ2000.c â Sharp MZ-2000 peripheral set  
  - full MZ-2000 machine emulation with boot/normal memory mode switching (BST/NST), character and graphics VRAM overlay with bank select, Intel 8253 PIT (4 MHz), Intel 8255 PPI (cassette and memory mode control), Z80 PIO (keyboard and VRAM paging), and MB8866 FDC. Supports both physical mode (drop-in Z80 replacement in a real MZ-2000 with automatic boot/normal mode detection) and virtual mode (full PSRAM-based emulation with IPL ROM mirroring). Sub-interfaces: RFS, MZ80AFI, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18.
* MZ2200.c â Sharp MZ-2200 peripheral set  
  - MZ-2200 machine emulation based on MZ-2000 architecture with 8253 PIT, 8255 PPI, Z80 PIO, MB8866 FDC, and colour CRT. Supports BST/NST memory mode switching with VRAM overlay. Sub-interfaces: RFS, MZ-8BFI/E0054PA, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18.
* MZ80B.c â Sharp MZ-80B peripheral set  
  - MZ-80B machine emulation with 2K IPL ROM, BST/NST mode switching, monochrome display with dual graphic VRAM pages, 8253 PIT (31.25 kHz), 8255 PPI, Z80 PIO, and graphic page select. All 10 expansion board interfaces supported. Sub-interfaces: MZ-8BFI/E0054PA, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18, MZ-1R23, MZ-1R37, PIO-3034, Celestite, MZ-1E30.
* MZ2500.c â Sharp MZ-2500 (SuperMZ) peripheral set  
  - MZ-2500 machine emulation with 8-page MMU (64 memory blocks), compatibility modes (MZ-2000, MZ-80B, native), OPN YM2203 FM+PSG sound, G-CRTC graphics controller, MB8876 FDC, 16-entry graphic palette, interrupt controller, RTC, joystick ports. Virtual mode supports interrupt-driven software via custom fetchByte and RETI handlers that execute physical M1 bus cycles (needed for the gate array's M1-timed internal clocks), D88 native disk format with sparse/contiguous auto-detection, and one-shot interrupt suppression during initialisation. Sub-interfaces: MZ-8BFI/E0054PA, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18, MZ-1R23, MZ-1R37, PIO-3034, Celestite, MZ-1E30.
* MZ1500.c â Sharp MZ-1500 peripheral set  
  - MZ-700 superset with inbuilt Quick Disk drive, Programmable Character Generator (PCG), stereo PSG sound (SN76489AN), Z80 PIO printer interface, 8253 PIT, and DIP switch MZ-700/MZ-1500 mode selection. Sub-interfaces: RFS, MZ-1E05, MZ-1E14, MZ-1E19, MZ-1R12, MZ-1R18, MZ-1R23, MZ-1R37, PIO-3034, Celestite.
* WD1773.c â Floppy disk controller  
  - emulates a WD1773 FDC supporting 80-track, 2-head, 8-sector-per-track disk images in DSK, RAW, and D88 formats stored on the SD card. WD1773 registers are mapped as FUNC-type I/O blocks.
* QDDrive.c â QuickDisk drive  
  - emulates the Sharp QuickDisk sequential-access miniature drive using QD image files on the SD card. The driver provides full Z80 SIO/2 emulation (Channel A for spiral track data, Channel B for motor/status control), complete with hunt-phase sync byte detection, motor control via RTS, and inter-core asynchronous file operations for SD card access.
* RFS.c â ROM Filing System  
  - implements the RFS banking and filing interface, allowing MZF program files to be loaded from the SD card. The RFS persona includes CP/M v2.23 (48K), the custom SA-1510 BASIC interpreter, and Microsoft BASIC v4.7, all enhanced with SD card read/write access so programs and data can be loaded and saved directly from the SD card without cassette or floppy hardware.
* TZFS.c â TranZPUter Filing System *(work in progress)*  
  - TZFS integration framework is in place but additional logic for the virtual I/O processor is still under development. Machine emulation switching, file management, CP/M boot, and I/O read/write commands will be available once this work is complete.
* MZ-1E05.c â Floppy disk interface unit  
  - emulates the Sharp MZ-1E05 floppy disk controller unit, which is based on the WD1773 FDC.
* MZ8BFI.c â MZ-8BFI / E0054PA floppy disk interface (MZ-2000)  
  - emulates the MZ-2000's floppy disk interface using the MB8866/WD1773-compatible FDC. Unlike the MZ-1E05, the MZ-8BFI has no onboard driver ROM â the FDC code resides in the MZ-2000 IPL ROM. Supports D88 disk image format. 40 cylinders, 2 heads, 16 sectors/track, 256-byte sectors.
* MZ-1E14.c â QuickDisk controller with BIOS ROM (MZ-700 / MZ-800)  
  - emulates the MZ-1E14 QuickDisk controller, which includes an onboard BIOS ROM for the MZ-700 and MZ-800 machines.
* MZ-1E19.c â QuickDisk controller without BIOS ROM (MZ-800 / MZ-2000 / MZ-2200 / MZ-2500)  
  - emulates the MZ-1E19 QuickDisk controller, which has no onboard BIOS ROM and targets the MZ-800, MZ-2000, MZ-2200, and MZ-2500 machines.
* MZ-1R12.c â 32KB battery-backed RAM board  
  - emulates the Sharp MZ-1R12 32KB battery-backed RAM expansion. Rather than using a real battery, the RAM image is persisted to and restored from the SD card. The board is commonly used to store an application so it is instantly available at boot, avoiding long cassette load times.
* MZ-1R18.c â 64KB RAM board  
  - emulates the Sharp MZ-1R18 64KB RAM expansion, typically used as a RAMFILE disk for program storage or to provide additional memory for custom applications requiring more than the standard address space.
* MZ-1R23.c â MZ-1R23 Kanji ROM / MZ-1R24 Dictionary ROM  
  - emulates the 128KB Kanji ROM (16Ã16 JIS patterns) and optional 256KB Dictionary ROM boards. ROM files loaded from SD card. I/O ports B8hâB9h with auto-increment read.
* MZ-1R37.c â MZ-1R37 640KB EMM (Expanded Memory Manager)  
  - emulates a 640KB expanded memory board with 20-bit address space and I/O port address latching.
* PIO-3034.c â IO DATA PIO-3034 320KB EMM  
  - emulates a 320KB expanded memory board with 19-bit address counter and auto-increment data port.
* Celestite.c â Celestite LAN / Memory composite board  
  - emulates a Wiznet W5100 Ethernet controller (register file), interrupt controller, UFM persistent storage, integrated MZ-1R12 32KB CMOS RAM (expandable to 64KB), and optional MZ-1R37 640KB EMM. I/O ports 60hâ6Fh. The netfs.py file server address is configurable via the JSON `ip` parameter (e.g. `"192.168.1.210:6800"`). Phase 2 implementation provides real TCP/IP networking via the ESP32 bridge â W5100 socket commands (OPEN, CONNECT, LISTEN, SEND, RECV, CLOSE) are forwarded to the ESP32 which performs actual BSD socket operations, enabling the Celestite board to communicate with network services such as the netfs.py file server.
* SASI.c + MZ1E30.c â MZ-1E30 SASI hard disk interface  
  - emulates the Sharp MZ-1E30 SASI hard disk controller for MZ-2500/MZ-80B. Supports up to 4 disk targets (~21.4 MB each, 256-byte blocks), 32KB IPL ROM, and on-demand sector I/O from SD card disk images. SASI commands: TEST\_UNIT\_READY, REQUEST\_SENSE, READ(6), WRITE(6), SEEK(6), INQUIRY. I/O ports 0xA4â0xA5 (SASI bus), 0xA8â0xA9 (ROM access).

Amstrad PCW Series

When built with

`INCLUDE_AMSTRAD_DRIVERS`

, the following Amstrad peripheral drivers are compiled in:

* PCW9512.c + uPD765.c â Amstrad PCW-9512 peripheral set  
  - complete Amstrad PCW-9512 emulation with gate array (ASIC), NEC uPD765 FDC (CPC DSK format), 512KB RAM with 4-bank 16KB paging, 8041 daisy wheel printer controller, bootstrap sequence emulation, and physical disk imaging. Virtual and physical modes supported.

Additional Sharp MZ personas and support for other Z80-based machines â including the Tatung Einstein â will be added in due course.

Multiple personas can coexist in the JSON configuration, each associated with a different PSRAM bank. Switching persona changes the active memory map and loaded ROM images without rebooting the host.

Network File Server (netfs.py)

The picoZ80 project includes a Python-based network file server (

`tools/NetFileServer/netfs.py`

) that runs on a Windows or Linux PC and serves MZF program files to the Sharp MZ BASIC

`NETx:`

device over the network. When the picoZ80 is fitted with a Celestite board (or virtual Celestite driver), BASIC programs running on the MZ can load, save, and list files from the PC's filesystem using standard BASIC commands with the

`NETx:`

device prefix.

```
python3 netfs.py [--port 6800] [--dir ./mzf_files] [--dir2 path] ... [--dir7 path]
```

The server supports units 1â7 (

`NET1:`

to

`NET7:`

), each mapped to a separate directory on the PC. Commands supported: DIR (directory listing), READ (load file data), WRITE (save file), INFO (file metadata), DELETE, and CLOSE. The server is multi-threaded, handles MZF header parsing and creation, and includes a 30-second connection timeout for crash recovery.

---

Build Instructions
------------------

Prerequisites

* CMake 3.20+  
  - used as the build system for the RP2350 firmware.
* ARM GCC toolchain  
  - `arm-none-eabi-gcc`, typically installed via `apt install gcc-arm-none-eabi`.
* Docker  
  - required for the ESP32 firmware build, which runs inside the official Espressif IDF container (`espressif/idf:release-v5.4`). No native ESP-IDF installation is needed.
* Python 3  
  - required by the Pico SDK build tools.
* Perl  
  - used by the build script for automatic version incrementing.

Directory Structure

All paths are relative to a user-chosen root directory, referred to here as `<root>`. The build scripts use a `PICO_PATH` variable at the top of each script which must be updated to match this root before first use. The expected layout after setup is:

```
<root>/
âââ get_and_build_sdk.sh      # clones and builds pico-sdk and pico-examples
âââ build_tzpuPico.sh         # builds the RP2350 firmware (and optionally ESP32)
âââ picoZ80.h.tmpl            # board definition template, copied into the SDK at build time
âââ pico-sdk/                 # cloned by get_and_build_sdk.sh
âââ pico-examples/            # cloned by get_and_build_sdk.sh
âââ projects/
    âââ Z80/                  # Zeta Z80 emulator library (cloned manually)
    âââ tzpuPico/             # main picoZ80/pico6502 project (cloned manually)
```

Step 1 â Clone the Projects

```
mkdir -p <root>/projects
cd <root>/projects

# Clone the main tzpuPico project
git clone <tzpuPico-repo-url> tzpuPico

# Clone the Zeta Z80 emulator library
git clone <zeta-repo-url> Z80
```

Step 2 â Set PICO\_PATH in the Build Scripts

Edit the `PICO_PATH` variable at the top of both `get_and_build_sdk.sh` and `build_tzpuPico.sh` to point to your chosen root directory:

```
export PICO_PATH=/your/chosen/root/
```

Step 3 â Get and Build the Pico SDK

`get_and_build_sdk.sh` clones the Raspberry Pi Pico SDK (`develop` branch) and pico-examples (`master` branch) into the root, initialises all submodules, then builds the SDK against the RP2350 target. Run this once before the first firmware build, and again whenever you want to update the SDK.

```
cd <root>
./get_and_build_sdk.sh
```

The script clones into `<root>/pico-sdk/` and `<root>/pico-examples/`, then builds the SDK with:

```
cmake -DPICO_BOARD=pimoroni_pga2350 -DPICO_PLATFORM=rp2350-arm-s -DPICO_SDK_PATH=<root>/pico-sdk/ ..
make
```

Step 4 â Build the RP2350 Firmware

`build_tzpuPico.sh`

handles the complete RP2350 build: it copies the

`picoZ80.h`

board definition into the SDK, backs up the current version, runs CMake and

`make -j4`

, increments the version number on a successful build, and copies the resulting firmware files into

`projects/tzpuPico/fw/uf2/`

and

`projects/tzpuPico/fw/bin/`

with version-stamped filenames. The

`fw/uf2/`

directory holds the

**Bootloader**

UF2 image (used for initial USB mass-storage flashing); the

`fw/bin/`

directory holds the

**application partition**

pure binary (

`.bin`

) images used for OTA updates. Application partitions are placed at non-standard flash addresses that the UF2 format cannot express, so plain binary is used for all OTA transfers.

The script accepts an optional argument:

```
cd <root>

# Standard release build (RP2350 only)
./build_tzpuPico.sh

# Debug build (RP2350 only, CMAKE_BUILD_TYPE=Debug)
./build_tzpuPico.sh DEBUG

# Full build â RP2350 firmware plus ESP32 firmware via Docker
./build_tzpuPico.sh ALL
```

Targeted Build System

The build system produces machine-specific firmware binaries to reduce firmware size when only a subset of drivers is needed:

| Target | Binary Prefix | Drivers Included | Compile-time Defines |
| --- | --- | --- | --- |
| `BaseZ80` | `pZ80-BaseZ80` | All drivers (Sharp + Amstrad) â universal binary | `INCLUDE_SHARP_DRIVERS`, `INCLUDE_AMSTRAD_DRIVERS` |
| `SharpZ80` | `pZ80-SharpZ80` | Sharp MZ drivers only â smaller firmware | `INCLUDE_SHARP_DRIVERS` |
| `AmstradZ80` | `pZ80-AmstradZ80` | Amstrad PCW drivers only â smaller firmware | `INCLUDE_AMSTRAD_DRIVERS`, `TARGET_MODEL_AMSTRAD` |

Each target model has its own directory under `src/model/` with a dedicated `CMakeLists.txt`, entry point, and linker scripts. Use the `BaseZ80` target for maximum compatibility or select a machine-specific target for a smaller binary that fits more comfortably in the 5MB firmware partition.

Build ESP32 Firmware Separately

The ESP32 firmware can also be built independently using Docker. Add the following alias to your shell profile (`~/.bashrc` or `~/.zshrc`), then invoke `idf54` from the `esp32/` directory:

```
# Add to shell profile
alias idf54='docker run --rm --privileged \
  --volume /dev:/dev \
  --volume /sys:/sys:ro \
  --volume /dev/bus/usb:/dev/bus/usb \
  -v $PWD:/project \
  -w /project \
  -it espressif/idf:release-v5.4 idf.py "$@"'

cd <root>/projects/tzpuPico/esp32
idf54 build

# Firmware binary: build/tzpuPico_esp32.bin
# Upload via the OTA web page (ota-esp32.htm) or flash directly via USB
```

---

Flashing
--------

Initial RP2350 Flash

There is no physical BOOTSEL or Reset button on the picoZ80 board. Both signals are exposed on the 6-pin debug header:

| Pin 1 | Pin 2 | Pin 3 | Pin 4 | Pin 5 | Pin 6 |
| --- | --- | --- | --- | --- | --- |
| SWCLK | SWD | Reset RP2350 | Reset ESP32 | GND | BOOTSEL |

To enter the RP2350 bootloader mass-storage mode, use a jumper or probe on the debug header:

1. Hold **Pin 6 (BOOTSEL)** low.
2. Apply power, or assert **Pin 3 (Reset RP2350)** low then release it â the RP2350 begins booting.
3. Release BOOTSEL promptly after power-on or reset. Holding it low beyond the initial boot moment prevents the RP2350 from accessing FlashRAM.
4. Connect the picoZ80 USB port to a PC â the RP2350 enumerates as a USB mass-storage device.
5. Copy `Bootloader_<version>.uf2` to the mounted drive. The RP2350 self-flashes the bootloader and reboots.

All subsequent RP2350 firmware updates can be performed via the OTA web page without touching the debug header.

Initial ESP32 Flash

The ESP32 is flashed using

`esptool`

via a Python virtual environment. On newer board revisions the ESP32 appears as its own USB device; on original boards with a single USB port it was accessible only through the RP2350 acting as a USB-UART bridge. In both cases

**Pin 4 (Reset ESP32)**

on the debug header is used to hold the ESP32 in reset during the RP2350 boot sequence when required.

Set up the esptool environment once:

```
python3 -m venv ./venv/
source ./venv/bin/activate
cd $HOME/esptool
```

Then flash all four ESP32 firmware components in one command, adjusting `PORT` to match the device node assigned by your OS and `BINPATH` to the directory containing the built binaries:

```
PORT=/dev/tty.usbmodem141403   # adjust to your system
BINPATH=/path/to/build/output

python3 ./esptool.py \
  -p ${PORT} -b 115200 \
  --before default_reset --after hard_reset \
  --chip esp32s3 \
  write_flash \
  --flash_mode dio --flash_size 4MB --flash_freq 80m \
  0x0     ${BINPATH}/bootloader.bin \
  0x8000  ${BINPATH}/partition-table.bin \
  0x9000  ${BINPATH}/ota_data_initial.bin \
  0x10000 ${BINPATH}/sd_card.bin
```

All subsequent ESP32 firmware updates can be performed via the OTA web page (

`ota-esp32.htm`

) without requiring esptool.

**Board revision note:**

Original picoZ80 boards (v2.0 to v2.2) have a single USB port connected to the RP2350. On these boards the ESP32 must be programmed via the RP2350 acting as a USB-UART bridge. Newer board revisions add a second USB port connected directly to the ESP32, allowing esptool to address it independently.

OTA Updates (after initial flash)

* RP2350 OTA  
  - navigate to `http://<device-ip>/ota-rp2350.htm`, select the versioned `.bin` file from `fw/bin/`, and upload. The application partitions live at non-standard flash addresses, so pure binary (not UF2) is required. The bootloader verifies the image checksum before activating the new partition.
* ESP32 OTA  
  - navigate to `http://<device-ip>/ota-esp32.htm` and upload the ESP32 firmware binary. The ESP32 reboots automatically into the new firmware. The same page also accepts a versioned **FilePack** archive that updates the ESP32 web filesystem on the SD card â see [FilePack Upload](https://eaw.app/picoz80/#esp32-filepack) below.

SD Card Preparation

Format the SD card as FAT32. Place `config.json` in the root directory. Create subdirectories for ROM images, disk images, and filing system trees as referenced in your configuration. Once the board is running, the SD card can also be managed entirely through the web File Manager page.

---

Debugging
---------

The picoZ80 supports full source-level debugging of both RP2350 cores and the ESP32 co-processor. The RP2350 is debugged over SWD using a CMSIS-DAP probe, with OpenOCD providing a two-target GDB server (one port per core). The ESP32-S3 is debugged over its built-in USB-JTAG interface using the Xtensa toolchain GDB.

RP2350 â SWD Debugging

**Hardware connection**

Connect an ARM DAPLink / CMSIS-DAP probe (e.g. Raspberry Pi Debug Probe, Black Magic Probe, or any CMSIS-DAP-compatible adapter) to the 6-pin debug header on the picoZ80 board. Only three connections are required:

| Debug Header Pin | Signal | SWD Function |
| --- | --- | --- |
| Pin 1 | `SWCLK` | Serial Wire Clock |
| Pin 2 | `SWDIO` | Serial Wire Data |
| Pin 5 | `GND` | Ground reference |

**Starting OpenOCD**

OpenOCD exposes two GDB server ports â port

`3333`

for Core 0 and port

`3334`

for Core 1. The picoZ80 requires a small modification to the standard OpenOCD RP2350 target script to enable true SMP debugging with separate GDB ports per core. Copy the standard script and uncomment the

`target smp`

line:

```
sudo cp /usr/local/share/openocd/scripts/target/rp2350.cfg \
        /usr/local/share/openocd/scripts/target/rp2350_tzpu.cfg
```

Then edit `rp2350_tzpu.cfg` â find the `target smp` line inside the `if {[string compare $_USE_CORE SMP] == 0}` block and remove the leading `#`:

```
# Before (rp2350.cfg):
    #target smp $_TARGETNAME_0 $_TARGETNAME_1

# After (rp2350_tzpu.cfg):
    target smp $_TARGETNAME_0 $_TARGETNAME_1
```

This single change activates SMP mode so that OpenOCD registers Core 0 on GDB port 3333 and Core 1 on port 3334, allowing each core to be attached and stepped independently. Launch OpenOCD from the project root before starting GDB:

```
openocd -f interface/cmsis-dap.cfg -f target/rp2350_tzpu.cfg -c "adapter speed 5000"
```

**Global GDB initialisation (`~/.gdbinit`)**  
GDB requires explicit permission to auto-load per-directory `.gdbinit` files. Add the following to `~/.gdbinit`, adjusting the paths to match your project location (shown here relative to the project root â use absolute paths in `~/.gdbinit` if you run GDB from varying directories):

```
set history save on
set history filename ~/.gdb_history
set history size 65536
add-auto-load-safe-path build/bin/model/BaseZ80/.gdbinit:build/bin/model/Bootloader/.gdbinit
```

Bootloader Debugging

Copy the appropriate per-core `.gdbinit` file to the Bootloader build directory, then launch `gdb-multiarch`. The `.gdbinit.bootloader.3333` file connects to Core 0 (port 3333) and logs output to `gdb_core0.txt`; `.gdbinit.bootloader.3334` connects to Core 1 (port 3334) logging to `gdb_core1.txt`. Open two terminals to debug both cores simultaneously:

```
# Terminal 1 â Core 0
cd build/bin/model/Bootloader
cp ../../../../.gdbinit.bootloader.3333 .gdbinit
gdb-multiarch Bootloader.elf

# Terminal 2 â Core 1
cd build/bin/model/Bootloader
cp ../../../../.gdbinit.bootloader.3334 .gdbinit
gdb-multiarch Bootloader.elf
```

Main Firmware Debugging

The main firmware `.gdbinit` files (`.gdbinit.3333` and `.gdbinit.3334`) define a custom `xac <address> <count>` command that dumps memory as combined hex and ASCII output, connect to the respective GDB port, and continue execution. This is useful for inspecting PSRAM bank contents and memory-mapped device state without halting the emulation loop:

```
# Terminal 1 â Core 0
cd build/bin/model/BaseZ80
cp ../../../../.gdbinit.3333 .gdbinit
gdb-multiarch BaseZ80_0x10020000.elf

# Terminal 2 â Core 1
cd build/bin/model/BaseZ80
cp ../../../../.gdbinit.3334 .gdbinit
gdb-multiarch BaseZ80_0x10020000.elf

# Memory dump example (in GDB prompt):
(gdb) xac 0x20000000 64
```

ESP32 â USB Debugging

The ESP32-S3 co-processor has a built-in USB-JTAG interface â no external debug probe is required. Connect a USB cable from a host PC directly to the ESP32 USB port on the picoZ80 board.

Start OpenOCD using the ESP32-S3 built-in JTAG configuration:

```
openocd -f board/esp32s3-builtin.cfg
```

Then launch the Xtensa GDB pointing at the ESP32 firmware ELF (located at `esp32/build/main.elf` relative to the project root) and attach to the OpenOCD GDB server:

```
xtensa-esp32s3-elf-gdb esp32/build/main.elf
(gdb) target extended-remote :3333
```

Ensure the ELF was built from the same source revision as the firmware flashed to the device so that symbols and addresses align correctly.

---

Configuration (JSON)
--------------------

All picoZ80 behaviour is controlled by

`config.json`

on the SD card. The RP2350 reads this file at boot via the ESP32, minifies it, and stores the result in Flash. If no SD card is present, the previously stored configuration is used. The configuration can be edited directly in the browser using the Config Editor page.

The top-level structure is:

```
{
  "esp32": {
    "core": {
      "device": "Z80",
      "mode":   0
    },
    "wifi": {
      "override":  1,
      "wifimode":  "client",
      "ssid":      "MyNetwork",
      "password":  "MyPassword",
      "ip":        "192.168.1.192",
      "netmask":   "255.255.255.0",
      "gateway":   "192.168.1.1",
      "dhcp":      0,
      "webfs":     "webfs",
      "persist":   0
    }
  },
  "rp2350": {
    "core": {
      "cpufreq":   300000000,
      "psramfreq": 133000000,
      "voltage":   1.10
    },
    "z80": [
      {
        "memory":  [ ... ],
        "io":      [ ... ],
        "drivers": [ ... ]
      }
    ]
  }
}
```

esp32 â ESP32 Configuration

The `esp32` top-level object configures the ESP32 co-processor. It contains two sub-objects: `core` and `wifi`.

esp32.core

| Key | Type | Description |
| --- | --- | --- |
| `device` | string | CPU device type â tells the ESP32 which processor personality to use. Valid values: `"Z80"` (picoZ80), `"6502"` (pico6502), `"6512"` (pico6512). |
| `mode` | integer | Default boot mode: `0` = client (station) mode, `1` = Access Point mode. This value is persisted in NVS and used on next boot if the WiFi manager has not overridden it. |

esp32.wifi

The `wifi` object provides a mechanism to inject WiFi credentials and network settings from `config.json`, overriding whatever is stored in NVS. This is useful for initial provisioning or for deploying a known-good network configuration without using the web WiFi Manager. Set `override` to `0` to ignore the config file entirely and rely on previously persisted NVS settings.

| Key | Type | Description |
| --- | --- | --- |
| `override` | 0/1 | Master switch. `1` = apply all settings below; `0` = ignore this block and use persisted NVS settings. |
| `wifimode` | string | `"ap"` for Access Point mode (ESP32 creates its own network); `"client"` for client/station mode (ESP32 joins an existing network). |
| `ssid` | string | WiFi network name (SSID) to create (AP mode) or join (client mode). |
| `password` | string | WiFi passphrase for the SSID. |
| `ip` | string | Fixed IP address (e.g. `"192.168.1.192"`). Used in both AP and client modes when `dhcp` is `0`. |
| `netmask` | string | Subnet mask (e.g. `"255.255.255.0"`). |
| `gateway` | string | Default gateway address (e.g. `"192.168.1.1"`). |
| `dhcp` | 0/1 | Client mode only. `1` = obtain address via DHCP; `0` = use the fixed `ip`/`netmask`/`gateway` above. |
| `webfs` | string | Override the web filesystem root directory on the SD card (default `"webfs"`). Allows alternate web UI assets to be served. |
| `persist` | 0/1 | `1` = write the resolved WiFi settings back to NVS so they survive reboots even after `override` is cleared; `0` = apply for this session only. |

core â RP2350 Operating Parameters

| Key | Type | Description |
| --- | --- | --- |
| `cpufreq` | integer | RP2350 system clock frequency in Hz (e.g. `300000000` for 300 MHz). |
| `psramfreq` | integer | PSRAM SPI clock frequency in Hz (e.g. `133000000` for 133 MHz). |
| `voltage` | float | RP2350 core voltage in volts (e.g. `1.10`). Higher clock speeds may require higher voltage. |

memory â Memory Map

The `memory` array defines the Z80 memory map. Each entry covers a contiguous region of the 64KB Z80 address space, rounded to 512-byte block boundaries.

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this entry is active. |
| `addr` | hex string | Start address in the Z80 address space (e.g. `"0x0000"`). |
| `size` | hex string | Size of the region (e.g. `"0x2000"` for 8KB). |
| `type` | string | Block type: `PHYSICAL`, `PHYSICAL_VRAM`, `PHYSICAL_HW`, `RAM`, `ROM`, `VRAM`, `FUNC`, `PTR`. |
| `bank` | integer | PSRAM bank number (0â63) for RAM/ROM/VRAM types. |
| `tcycwait` | integer | Number of additional T-cycle wait states to insert on access. |
| `tcycsync` | integer | Enable synchronisation with T1 rising edge. |
| `task` | string | Optional task identifier for FUNC-type blocks. |
| `file` | string | SD-card path to a ROM image to load into this block at boot. |
| `fileofs` | integer | Byte offset within the ROM image file to start reading from. |

```
"memory": [
  {
    "enable":   1,
    "addr":     "0x0000",
    "size":     "0x1000",
    "type":     "ROM",
    "bank":     0,
    "tcycwait": 0,
    "tcycsync": 0,
    "task":     "",
    "file":     "/TZFS/tzfs.rom",
    "fileofs":  0
  },
  {
    "enable":   1,
    "addr":     "0x1000",
    "size":     "0xCFFF",
    "type":     "RAM",
    "bank":     0,
    "tcycwait": 0,
    "tcycsync": 0,
    "task":     "",
    "file":     "",
    "fileofs":  0
  },
  {
    "enable":   1,
    "addr":     "0xD000",
    "size":     "0x1000",
    "type":     "PHYSICAL_VRAM",
    "bank":     0,
    "tcycwait": 2,
    "tcycsync": 0,
    "task":     "",
    "file":     "",
    "fileofs":  0
  }
]
```

io â I/O Port Map

The `io` array maps Z80 I/O port ranges to handlers. I/O cycles are distinguished from memory cycles by the Z80 IORQ signal, which the PIO control state machine monitors.

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this entry is active. |
| `addr` | hex string | Start I/O port address (e.g. `"0xE0"`). |
| `size` | hex string | Number of ports in the range. |
| `type` | string | `PHYSICAL` (pass to host), `FUNC` (call C handler). |
| `func` | string | Handler function name for FUNC type. |

```
"io": [
  {
    "enable": 1,
    "addr":   "0xE0",
    "size":   "0x08",
    "type":   "FUNC",
    "func":   "mz700_io"
  },
  {
    "enable": 1,
    "addr":   "0x00",
    "size":   "0xE0",
    "type":   "PHYSICAL"
  }
]
```

drivers â Machine Drivers

The `drivers` array binds named driver instances to the Z80 context. Each driver has one or more **interfaces** (listed under the `"if"` key), each of which can load ROM images, remap address ranges, remap I/O port ranges, and receive parameter files.

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this driver is loaded. |
| `name` | string | Driver name (must match a compiled-in driver, e.g. `"MZ700"`, `"RFS"`, `"TZFS"`). |
| `type` | string | `PHYSICAL` or `VIRTUAL`. |
| `if` | array | Array of interface objects (see below). |

**Interface object** (`if[]`):

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this interface is active. |
| `name` | string | Interface instance name. |
| `type` | string | `PHYSICAL` or `VIRTUAL`. |
| `rom` | array | ROM images to load into PSRAM at boot. |
| `addrmap` | array | Address remapping rules for this interface. |
| `iomap` | array | I/O port remapping rules for this interface. |
| `param` | array | Parameter files passed to the driver. |

**rom[] entry:**

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this ROM entry is active. |
| `file` | string | SD-card path to the ROM binary. |
| `loadaddr` | array | Load-address descriptors (position, addr, bank, size, wait states). |

**addrmap[] entry:**

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this mapping is active. |
| `srcAddr` | hex string | Source address in the Z80 space. |
| `size` | hex string | Size of the mapped region. |
| `dstAddr` | hex string | Destination address after remapping. |

**iomap[] entry:**

| Key | Type | Description |
| --- | --- | --- |
| `enable` | 0/1 | Whether this I/O mapping is active. |
| `srcAddr` | hex string | Source I/O port. |
| `size` | hex string | Number of ports. |
| `dstAddr` | hex string | Destination port after remapping. |
| `16bit` | 0/1 | Whether 16-bit I/O addressing is used. |

```
"drivers": [
  {
    "enable": 1,
    "name":   "MZ700",
    "type":   "PHYSICAL",
    "if": [
      {
        "enable": 1,
        "name":   "main",
        "type":   "PHYSICAL",
        "rom": [
          {
            "enable":   1,
            "file":     "/MZ700/mz700.rom",
            "loadaddr": [
              {
                "enable":   1,
                "position": 0,
                "addr":     "0x0000",
                "bank":     0,
                "size":     "0x1000",
                "tcycwait": 0,
                "tcycsync": 0
              }
            ]
          }
        ],
        "addrmap": [
          {
            "enable":  1,
            "srcAddr": "0x0000",
            "size":    "0x1000",
            "dstAddr": "0x0000"
          }
        ],
        "iomap": [
          {
            "enable":  1,
            "srcAddr": "0xE0",
            "size":    "0x08",
            "dstAddr": "0xE0",
            "16bit":   0
          }
        ],
        "param": [
          {
            "enable": 1,
            "file":   "/config/mz700.cfg"
          }
        ]
      }
    ]
  },
  {
    "enable": 1,
    "name":   "MZ-1E05",
    "type":   "PHYSICAL",
    "if": [
      {
        "enable": 1,
        "name":   "fdc0",
        "type":   "PHYSICAL",
        "rom":    [],
        "addrmap": [],
        "iomap": [
          {
            "enable":  1,
            "srcAddr": "0xD8",
            "size":    "0x04",
            "dstAddr": "0xD8",
            "16bit":   0
          }
        ],
        "param": [
          {
            "enable": 1,
            "file":   "/DSK/MZ700/disk0.dsk"
          }
        ]
      }
    ]
  }
]
```

Complete Minimal Configuration Example

The following is a minimal configuration that boots an MZ-700 with ROM, 48KB RAM, host VRAM, and the WD1773 floppy controller:

```
{
  "rp2350": {
    "core": {
      "cpufreq":   300000000,
      "psramfreq": 133000000,
      "voltage":   1.10
    },
    "z80": [
      {
        "memory": [
          { "enable":1, "addr":"0x0000", "size":"0x1000", "type":"ROM",
            "bank":0, "tcycwait":0, "tcycsync":0, "task":"",
            "file":"/MZ700/mz700.rom", "fileofs":0 },
          { "enable":1, "addr":"0x1000", "size":"0xCFFF", "type":"RAM",
            "bank":0, "tcycwait":0, "tcycsync":0, "task":"", "file":"", "fileofs":0 },
          { "enable":1, "addr":"0xD000", "size":"0x1000", "type":"PHYSICAL_VRAM",
            "bank":0, "tcycwait":2, "tcycsync":0, "task":"", "file":"", "fileofs":0 },
          { "enable":1, "addr":"0xE000", "size":"0x2000", "type":"PHYSICAL",
            "bank":0, "tcycwait":0, "tcycsync":0, "task":"", "file":"", "fileofs":0 }
        ],
        "io": [
          { "enable":1, "addr":"0xE0", "size":"0x08", "type":"FUNC", "func":"mz700_io" },
          { "enable":1, "addr":"0xD8", "size":"0x04", "type":"FUNC", "func":"wd1773_io" }
        ],
        "drivers": [
          {
            "enable":1, "name":"MZ700", "type":"PHYSICAL",
            "if": [{ "enable":1, "name":"main", "type":"PHYSICAL",
                     "rom":[], "addrmap":[], "iomap":[], "param":[] }]
          },
          {
            "enable":1, "name":"MZ-1E05", "type":"PHYSICAL",
            "if": [{ "enable":1, "name":"fdc0", "type":"PHYSICAL",
                     "rom":[], "addrmap":[], "iomap":[],
                     "param":[{ "enable":1, "file":"/DSK/MZ700/disk0.dsk" }] }]
          }
        ]
      }
    ]
  }
}
```

---

ICE (Debug Shell)
-----------------

The picoZ80 includes a built-in interactive ICE (In-Circuit Emulator) debug shell over the second USB CDC serial channel. Connect a terminal emulator (115200 baud, 8N1) to the debug serial port â it appears as the second COM/ttyACM port when the picoZ80 is connected via USB. The shell prompt is

`dbg>` 

.

The firmware is available in two variants: a standard build without the debug shell, and a DBGSH build that includes the full ICE debugger. The DBGSH variant is identified by the

`_DBGSH`

suffix in the firmware filename.

Command Reference

The debug shell provides 51 commands for real-time inspection and control of the Z80 CPU emulation:

| Command | Syntax | Description |
| --- | --- | --- |
| **help** | `help` | Show all available commands. |
| **regs** | `regs` | Dump Z80 registers (AF, BC, DE, HL, IX, IY, SP, PC, I, R, IM, IFF1/2, flags, HALT, MEMPTR, cycle count). |
| **dm** | `dm <p|f|v|r> <addr> [len]` | Dump memory. `p` = physical Z80 bus, `f` = fetch (M1 cycle), `v` = virtual PSRAM, `r` = RP2350 address space. |
| **cmp** | `cmp [f] <phys> <virt> <len>` | Compare physical bus memory with virtual PSRAM. Optional `f` uses fetch (M1) cycles instead of read cycles. Reports mismatches with addresses and values. |
| **dis** | `dis [p|v] [addr] [count]` | Disassemble Z80 code with full opcode decoding. |
| **asm** | `asm [addr]` | Interactive Z80 assembler â enter mnemonics line by line, empty line or `.` to exit. |
| **memmap** | `memmap [block]` | Dump SRAM bank pointers and memory banking layout. |
| **memptr** | `memptr [addr]` | Dump PSRAM memPtr table for address mapping. |
| **iomap** | `iomap [port]` | Show I/O port handlers and memory-mapped I/O configuration. |
| **status** | `status` | System overview: CPU freq, PSRAM clock, host clock, emulation speed, uptime. |
| **ver** | `ver` | Firmware version and flash partition info. |
| **drivers** | `drivers` | List active drivers with interface details. |
| **hold** | `hold` | Pause Z80 CPU emulation. |
| **release** | `release` | Resume Z80 CPU emulation. |
| **go** | `go` | Continue execution (release hold; breakpoints remain active). |
| **cont** | `cont` | Alias for `go`. Continue execution (release hold; breakpoints remain active). |
| **step** | `step [n]` | Single-step one or n instructions, displaying registers before and after each step. |
| **bp** | `bp <addr>` | Set a breakpoint at the given address (up to 8 simultaneous breakpoints). |
| **bc** | `bc <n|*>` | Clear breakpoint slot n, or `*` to clear all breakpoints. |
| **bl** | `bl` | List all active breakpoints. |
| **wm** | `wm <[p|v]> <addr> <byte>...` | Write bytes to memory. `p` = physical Z80 bus, `v` = virtual PSRAM, omit for auto (follows memory map). Auto-holds CPU for physical/mapped writes. |
| **fill** | `fill [p|v] <addr> <len> [w|d] <val>` | Fill memory with a constant value. `p` = physical, `v` = virtual, omit for auto. Default 8-bit; `w` = 16-bit, `d` = 32-bit (little-endian). Auto-holds CPU when needed. |
| **copy** | `copy <pv|fp|vp> <src> <len> <dst>` | Copy memory between physical and virtual. `pv` = physical read to virtual, `fp` = physical fetch to virtual, `vp` = virtual to physical write. Auto-holds CPU. |
| **memtest** | `memtest <addr> <len> [pattern]` | Test physical memory with three passes: write+read, write+fetch, interleaved. Default pattern: ascending bytes. Reports errors per pass. |
| **in** | `in <port>` | Read a Z80 I/O port. |
| **out** | `out <port> <byte>` | Write to a Z80 I/O port (CPU must be held). |
| **trace** | `trace <on|off|dump [n]|clear|rt|byte ...>` | Enable/disable execution trace, dump last n entries, or clear the 512-entry ring buffer. `rt` enables real-time trace output to the debug console as instructions execute. `byte` enables byte-level tracing of memory/IO transactions. |
| **verify** | `verify <on|off>` | Toggle full opcode fetch verification. When on, every fetch is verified against readPhysicalMem (50% speed reduction). When off (default), only checks 0x00/0xFF opcodes. |
| **fwait** | `fwait <0-4>` | Force extra wait states on M1 (opcode fetch) cycles. 0 = off (default). Useful for debugging timing-sensitive code. Shows current value if no parameter given. |
| **iowait** | `iowait <0-8>` | Force extra wait states on I/O read and write cycles. 0 = off (default). Stretches I/O cycles for diagnosing peripherals with slow response times. Shows current value if no parameter given. |
| **corrupt** | `corrupt [clear]` | Display detected fetch corruptions (PC, fetched opcode, verified opcode). `clear` resets the log. |
| **fdctrace** | `fdctrace <on|off|dump>` | Enable, disable, or dump FDC I/O trace. `dump` shows the last 64 WD1773 register operations from the ring buffer, showing port, direction, value, and status. |
| **qdtrace** | `qdtrace <on|off|dump>` | Enable, disable, or dump Quick Disk I/O trace. `dump` shows the last 64 operations, showing port, direction, value, and tape position. |
| **piodbg** | `piodbg [clear]` | Display RP2350 PIO hardware diagnostics for all three PIO blocks (PIO 0, PIO 1, PIO 2). Shows FDEBUG sticky error flags, FSTAT, FIFO levels, per-state-machine program counters, GPIO output-enable state, and GPIO pin levels. `clear` resets the FDEBUG sticky flags. |
| **load** | `load <p|v> <file> <addr> [len] [ofs]` | Load a file from the ESP32 SD card into Z80 memory. `p` = write to physical bus, `v` = write to virtual PSRAM bank 0. `file` is relative to `/sdcard/` on the ESP32. `addr` is the Z80 start address. If `len` is omitted the entire file is loaded (up to 64KB); if specified, loads that many bytes (max 1MB). Optional `ofs` is the file offset to start reading from. Auto-holds CPU for physical writes. Uses PSRAM bank 63 as scratch buffer. |
| **save** | `save <p|pf|v> <file> <addr> <len>` | Save Z80 memory to a file on the ESP32 SD card. `p` = read via physical bus, `pf` = read via physical fetch (M1 cycles), `v` = read from virtual PSRAM bank 0. `file` is relative to `/sdcard/`. `addr` is the Z80 start address, `len` is bytes to save (max 64KB). Auto-holds CPU for physical reads. Performs periodic DRAM refresh during physical reads. |
| **dir** | `dir [path]` | List files on the ESP32 SD card. Optional path is relative to `/sdcard/`. |
| **echo** | `echo [on|off]` | Toggle character echo. |
| **reset** | `reset` | Force a Z80 CPU reset. |
| **set** | `set <reg|flags|memmap|memptr|iomap> <idx> <val>` | Modify a Z80 register, flags, memory map, PSRAM memPtr, or I/O map entry at runtime. Allows hot-patching registers and memory/IO configuration without reloading. |
| **hist** | `hist [n]` | Display command history. Shows the last n entries (default: all). History is preserved across sessions via ESP32 NVS. |
| **savehst** | `savehst` | Force-save command history to ESP32 NVS immediately. |
| **ipl** | `ipl` | Perform an IPL reset (BST mode) by toggling 8255 PPI Port C bit 3. Resets the machine to boot mode without a full Z80 reset. Useful for MZ-80B/MZ-2000/MZ-2500 machines. |
| **mmutrace** | `mmutrace` | Dump machine-specific trace information (MMU state, I/O register snapshots, etc.). Output varies by persona â each driver registers its own trace handler. |
| **intcount** | `intcount` | Show the interrupt acknowledge count and current interrupt state. Useful for debugging interrupt-driven software. |
| **psync** | `psync [start end]` | Synchronise physical memory to PSRAM by reading physical bus and writing to virtual memory. Optional address range; defaults to full address space. Useful for diagnostics after DMA operations. |
| **dskimage** | `dskimage <filename> [cylinders] [heads]` | Image a physical floppy disk to a CPC DSK file on the SD card. Injects Z80 code into the host to read all tracks via the host FDC. Auto-detects geometry if cylinders/heads are omitted. Supports 720K (80x2) and 180K (40x1) formats. |
| **busdiag** | `busdiag` | Display bus diagnostics including PIO state, signal levels, and bus contention status. |
| **fdcimage** | `fdcimage` | Display FDC imaging status and progress. |
| **fdcdiag** | `fdcdiag` | Display FDC diagnostic information (controller state, register dump). |
| **gadiag** | `gadiag` | Display gate array diagnostic information (command state, interrupt routing). |

**Breakpoints**

â up to 8 breakpoints can be active simultaneously. When a breakpoint is hit, the CPU is automatically held and the hit address is displayed. Use

`go`

to continue or

`step`

to single-step from the breakpoint.

**Execution trace**

â when enabled, every executed instruction's PC, opcode, and flags register are recorded in a 512-entry ring buffer. Use

`trace dump`

to inspect recent execution history with full disassembly.

**Memory access modes**

â

`dm p`

reads memory via the physical Z80 bus (triggering real hardware responses),

`dm f`

reads using fetch (M1) cycles,

`dm v`

reads directly from the virtual PSRAM (zero bus activity), and

`dm r`

reads the RP2350's own address space (Flash, SRAM, peripherals).

---

Networking
----------

The picoZ80 supports three networking modes, selectable at build time via pre-built ESP32 sdkconfig files. Each mode determines how the web interface and configuration pages are accessed.

Operating Modes

| Mode | sdkconfig File | WiFi | USB NCM | Console | Web Access |
| --- | --- | --- | --- | --- | --- |
| WiFi Only | `sdkconfig.mode_wifi_only` | Yes | No | USB Serial/JTAG | Via WiFi AP or connected network |
| WiFi + NCM | `sdkconfig.mode_wifi_and_ncm` | Yes | Yes | TinyUSB CDC-ACM | Via WiFi and `http://192.168.7.1` |
| NCM Only | `sdkconfig.mode_ncm_only` | No | Yes | TinyUSB CDC-ACM | Via `http://192.168.7.1` only |

**USB NCM (Network Control Model)**

presents a virtual Ethernet adapter over the ESP32's USB OTG port. When the picoZ80 is connected to a host computer via USB, the host sees a standard network interface. A built-in DHCP server on the picoZ80 automatically assigns the host an IP address â no manual configuration is required. The web interface is then accessible at

`http://192.168.7.1`

.

**NCM Only mode**

is the recommended default for boards shipped without WiFi certification. It provides full web interface functionality (configuration, firmware updates, file management, persona selection) without any radio frequency emission. The WiFi antenna matching network does not need to be populated on the PCB.

**WiFi + NCM mode**

enables both interfaces simultaneously. The HTTP server binds to all interfaces, so the web pages are accessible from either WiFi or the USB network connection. WiFi connects asynchronously so the USB NCM interface is available immediately at power-on.

To switch modes, copy the appropriate

`sdkconfig.mode_*`

file to

`sdkconfig`

in the ESP32 build directory, rebuild, and flash the ESP32 firmware.

FCC / RED Regulatory Notice

**Important:**

The picoZ80 board has not been submitted for FCC (USA) or RED (EU) intentional radiator certification. As shipped, the board must have the WiFi antenna matching components unpopulated and the ESP32 firmware built with the

**NCM Only**

configuration (

`sdkconfig.mode_ncm_only`

). In this configuration no radio frequency energy is emitted and the board does not fall under intentional radiator regulations.

End users who wish to use WiFi may populate the antenna matching network on the PCB, build the ESP32 firmware with

`sdkconfig.mode_wifi_only`

or

`sdkconfig.mode_wifi_and_ncm`

, and operate the board under the hobbyist/experimental exemption applicable in their jurisdiction. Any party wishing to sell the board commercially with WiFi enabled must first obtain FCC and/or RED certification for the complete assembly.

---

Web Interface
-------------

The ESP32 co-processor hosts a web management interface built with Bootstrap 4. Connect to the picoZ80's WiFi network (or configure client mode to join your existing network) and navigate to

`http://<device-ip>/`

â by default

`http://192.168.4.1/`

in Access Point mode. In NCM mode, the web interface is accessed at

`http://192.168.7.1`

via the USB network connection. See

[Networking](https://eaw.app/picoz80/#networking-modes)

above for mode details.

On first power-up in WiFi mode the board starts in AP mode. Use the WiFi Manager page to configure client mode and assign a fixed IP address on your network. All pages share a common left-hand navigation bar giving one-click access to Status, Config Editor, Config GUI, File Manager, Settings (Firmware â ESP32 / RP2350, WiFi Manager), and Persona. In NCM Only mode, the WiFi Manager page is not present and the navigation bar shows the same set of pages minus WiFi Manager.

Dashboard â Status (index.htm)

The landing page shows the board's live state across three panels:

* WiFi Configuration / Network Configuration  
  - in WiFi modes this panel shows the current SSID, assigned IP address, netmask, and gateway. In NCM Only mode this panel is titled **Network Configuration** and shows the USB NCM network status (IP address, netmask) instead â there is no SSID or WiFi-related information. The board name (`tzpuPico`) and copyright string are served as template variables by the ESP32 web server.
* Version Information  
  - ESP32 partition table showing all OTA slots with type, sub-type, flash address, size, firmware version, build timestamp, and which slot is currently running. This makes it straightforward to confirm which firmware is active after an OTA update.
* RP2350 Partitions  
  - the RP2350 flash partition table with partition number, address, size, checksum, active/running flag, license, author, description, version, build date, and copyright â giving a complete snapshot of the RP2350 firmware state alongside the ESP32 information.

Two dropdown menus in the top-right navbar are available on every page:

* Actions menu  
  - **Change Floppy Disk 1 / 2** â select a new DSK image file from the SD card and mount it in the virtual WD1773 floppy controller slot 1 or slot 2 without rebooting. The currently loaded disk image filename is displayed next to each entry (or "none" if no image is loaded).  
  - **Change QD Disk** â swap the active QuickDisk image file on the fly. The currently loaded QD image filename is shown next to the entry.  
  - **Reload RP2350 Config** â send a reload command to the RP2350 over the ESP32âRP2350 UART; the RP2350 re-parses `config.json` and re-applies the memory map and driver configuration without a full power cycle.
* Reboot menu  
  - **ESP32** â soft-reboot the ESP32 co-processor (restarts the web server and WiFi stack, RP2350 is unaffected).  
  - **RP2350B** â reset the RP2350 processor (re-runs the bootloader and reloads the active firmware slot, host CPU is paused during reset).  
  - **Host** â assert the host computer's reset line, rebooting the legacy computer in the Z80 socket without affecting the picoZ80 board itself.  
  - **IPL Reset** â perform an IPL (Initial Program Load) reset by toggling 8255 PPI Port C bit 3, returning the machine to boot mode (BST). Available on MZ-80B, MZ-2000, MZ-2200, and MZ-2500 personas â equivalent to pressing the IPL button on the original hardware.  
  - **RP2350 UF2 Boot** â force the RP2350 into ROM UF2 USB boot mode via the custom bootloader. The ESP32 resets the RP2350 with the BOOT pin held, then sends a magic ID over UART that causes the bootloader to call `reset_usb_boot()`. The RP2350 presents as a USB mass-storage device for UF2 drag-and-drop flashing. This is the primary recovery method when the main application is broken (e.g. bad clock/voltage settings) â the custom bootloader runs at safe defaults and remains responsive.  
  - **RP2350 UF2 Boot (App)** â request the running RP2350 application to enter UF2 USB boot mode via SPI command. This is a fallback for situations where the bootloader itself needs replacing â the running application calls `reset_usb_boot()` directly. Only works when the application is running and responsive to SPI commands.

![picoZ80 Web Interface â Status Dashboard](https://eaw.app/images/picoZ80_web_status.png)

Config Editor (config.htm)

The Configuration Editor page gives full editting control over the jSON configuration file.
Change the configuration using the wysiwyg editor, save as needed and click Apply to reprocess the
configuration.

The SD card keeps automatic numbered backups of every saved configuration (

`config.json;1`

,

`config.json;2`

, â¦ with the highest number being the most recent), so it is always possible to roll back to a
previous working configuration. Edited configurations are saved back to the SD card; clicking Apply or a "Reload" menu action
then sends a reload command to the RP2350 over the ESP32âRP2350 UART, causing the RP2350 to re-parse and re-apply the new configuration
and causes the ESP32 to parse and reload it's configuration.

![picoZ80 Web Interface â Config Editor](https://eaw.app/images/picoZ80_web_config.png)

GUI Configuration (configgui.htm)

The GUI Configuration page provides a graphical form-based editor for the picoZ80 configuration, complementing the raw JSON

[Config Editor](https://eaw.app/picoz80/#config-editor)

. Instead of editing JSON directly, all settings are presented as labelled input fields, dropdown menus, and editable tables. Changes are saved to

`config.json`

on the SD card (the existing file is backed up automatically before saving). For advanced editing, the Config Editor remains available for direct JSON manipulation.

The page is organised into four tabs:

**RP2350 Global**

â global core settings that apply to both firmware partitions unless overridden at the partition level:

* **Core Voltage** â RP2350 core voltage in volts (e.g. 1.10 V).
* **CPU Frequency (MHz)** â RP2350 clock speed. Valid range is displayed alongside the field.
* **PSRAM Frequency (MHz)** â PSRAM SPI clock frequency. Higher values improve emulation speed but may reduce stability on some boards.

![picoZ80 Web Interface â GUI Configuration: RP2350 Global](https://eaw.app/images/picoZ80_web_configgui_core.png)

**Partition 1 / Partition 2**

â per-partition configuration. Each partition tab has the same layout:

* **Core Settings** â partition-specific overrides for Core Voltage, CPU Frequency, and PSRAM Frequency. If set, these take precedence over the global values for this partition.
* **Memory Regions** â an editable table defining the Z80 memory map. Each row specifies a memory block with: hex **Address**, **Size**, **Type** (ROM, RAM, PHYSICAL, or FUNC), **T-States** (wait states), **Bank** (PSRAM bank number), **Track** (T-cycle sync flag), **File** (ROM image filename on the SD card), **File Offset**, and a **Load** checkbox. Rows can be added or removed with the **Add Memory Region** and delete buttons.
* **I/O Regions** â an editable table defining the Z80 I/O port map. Each row specifies: **Address**, **Size**, **Type**, and **Function** (the driver handler). Add or remove rows as needed.
* **Drivers** â lists the active peripheral drivers (e.g. MZ80AFI, RFS, MZ-1E30, Celestite) with enable/disable toggles. The **Add Driver** button presents a dropdown of all available interface drivers for the selected persona, including floppy controllers, QuickDisk, RAM/ROM boards, SASI hard disk, and LAN interfaces. Each driver's ROM files, disk images, and parameters can be configured inline.

![picoZ80 Web Interface â GUI Configuration: Partition 1](https://eaw.app/images/picoZ80_web_configgui_part1.png)
![picoZ80 Web Interface â GUI Configuration: Partition 1](https://eaw.app/images/picoZ80_web_configgui_part1a.png)

![picoZ80 Web Interface â GUI Configuration: Partition 2](https://eaw.app/images/picoZ80_web_configgui_part2.png)
![picoZ80 Web Interface â GUI Configuration: Partition 2](https://eaw.app/images/picoZ80_web_configgui_part2a.png)

**ESP32**

â ESP32 co-processor settings:

* **Core** â ESP32 device type (e.g. S3S).
* **Network Interfaces** â enable/disable controls for both WiFi and USB NCM networking:
  + **WiFi Enable** â checkbox to enable or disable WiFi (requires reboot; ignored if WiFi is not compiled into the firmware).
  + **NCM Enable** â checkbox to enable or disable USB NCM networking (requires reboot).
  + **NCM Retries** â maximum connection retry cycles (0 = retry forever, 5â1000 = max attempts).
  + **NCM Retry Period** â delay between retries in seconds (0 = increasing backoff from 1s up to 60s, 1â120 = fixed interval).
  + **NCM IP Address** â the USB NCM gateway IP address (default: 192.168.7.1). When connecting two picoZ80 boards to the same host, each must use a different subnet (e.g. 192.168.7.1 and 192.168.8.1). Changes take effect after reboot and are persisted in NVS.
  + **NCM Netmask** â the USB NCM subnet mask (default: 255.255.255.0). Changes take effect after reboot.
  + **USB Product Name** â the USB device product string reported to the host operating system. macOS uses this as the NCM network interface label. Each board auto-generates a unique name from its MAC address (e.g. "picoZ80-3C4E"); override here to set a custom name (e.g. "picoZ80-MZ700"). Leave blank for auto-generation. Changes take effect after reboot.
* **WiFi Configuration** â SSID, password, IP address, netmask, WiFi mode (Access Point or Client), DHCP (Enabled or Disabled), WebFS directory path, polling period, and TX power. These settings mirror the WiFi Manager page but are editable here as part of the full configuration.

![picoZ80 Web Interface â GUI Configuration: ESP32](https://eaw.app/images/picoZ80_web_configgui_esp32.png)
![picoZ80 Web Interface â GUI Configuration: ESP32](https://eaw.app/images/picoZ80_web_configgui_esp32a.png)

Click

**Save Configuration**

to write the changes to

`config.json`

on the SD card (the previous version is backed up automatically) and automatically send a reload command to the RP2350, applying the new configuration without a full power cycle. Click

**Reload**

to re-read the current

`config.json`

from the SD card â useful if you have made a mistake and want to discard your changes and start again from the last saved state.

File Manager (filemanager.htm)

The File Manager provides a full web-based file browser for the SD card, providing a directory listing layout to view files
on the SD card.

It is intended for general SD card maintenance: uploading ROM images, floppy disk images (DSK), QuickDisk images (QD), RAM disk images, and web filesystem updates without needing to remove the card.

Each entry has action buttons to copy, delete, download, or edit text files, and a

**Select File**

upload button at the top allows new files to be transferred from the PC. Directory navigation allows descending into subdirectories such as

`roms/`

,

`dsk/`

,

`qd/`

, and

`ram/`

.

Uploading tar or gzip files will automatically have the tar or gzip (or tar.gz) file unpacked and extracted in the current SD
directory.

Multiple files can be selected using the checkboxes in the leftmost column (or the "Select All" checkbox in the header). When one or more items are selected,

**Download N Items**

and

**Delete Selected**

buttons appear in the panel header. The download function fetches each file sequentially with a progress modal â directories are automatically downloaded as tar archives. A

**Backup SD**

button downloads the entire SD card contents as a single archive to the local computer. These features are particularly useful when the picoZ80 is installed inside a host machine and physically removing the SD card is impractical.

![picoZ80 Web Interface â File Manager](https://eaw.app/images/picoZ80_web_filemanager.png)

Persona Selection (personality.htm)

The Persona page configures the active machine personality independently for each of the two RP2350 firmware partitions. Each partition has its own column of radio buttons covering every supported Sharp MZ machine type:

* **Basic CPU** â bare Z80 emulation with no machine-specific drivers; useful for generic Z80 development.
* **MZ-80A** and **MZ-80B** â Sharp MZ-80 series (1Z-013A monitor ROM, MZ-80 keyboard, standard memory map).
* **MZ-700** â Sharp MZ-700 with bank-switched VRAM, keyboard controller, and optional floppy/QuickDisk drivers.
* **MZ-800** â Sharp MZ-800 with extended video modes and QuickDisk support.
* **MZ-1500** â Sharp MZ-1500 with QuickDisk and optional floppy.
* **MZ-2000**, **MZ-2200**, **MZ-2500** â later Sharp MZ series with high-resolution video and extended memory.

Selecting a persona and clicking

**Select Personae**

writes the corresponding pre-built

`config.json`

to the SD card (backing up the current file first) and triggers a configuration reload. Because each firmware partition can hold a different persona, the board can be switched between, for example, an MZ-700 personality on partition 1 and an MZ-80A personality on partition 2 without any SD card editing.

![picoZ80 Web Interface â Persona Selection](https://eaw.app/images/picoZ80_web_persona.png)

Firmware Updates â ESP32 (ota-esp32.htm)

The ESP32 OTA page reports the full software inventory of the ESP32 before accepting a firmware upload:

* Modules panel  
  - shows the version of each ESP32 software component: the main ESP32 application, the NVS (non-volatile storage) library, the WiFi stack, the FilePack (web filesystem packager), and the WebFS (in-flash web file system). This makes it easy to confirm all components are consistent after an update.
* ESP32 Partitions panel  
  - shows the full ESP32 OTA partition table (otadata, nvs, phy\_init, ota\_0, ota\_1) with addresses, sizes, firmware versions, build timestamps, and which OTA slot is currently active (marked "Yes").
* ESP32 Firmware Upload panel  
  - accepts the ESP32 binary (`.bin`) produced by the ESP-IDF build. After upload the ESP32 reboots into the new firmware and the old slot is retained as a fallback.
* FilePack Upload panel  
  - uploads a versioned **FilePack** archive to the SD card. A FilePack bundles all ESP32 static web assets (HTML, CSS, JavaScript templates, and ancillary files) into a single distributable archive. On upload the ESP32 unpacks the archive to the SD card web filesystem directory; any file being replaced is automatically renamed to include its previous version number (e.g. `webfs` â `webfs.2.80`), preserving the old version for rollback. This matches the VAX/VMS style versioning used elsewhere on the SD card, where each successive revision of an editable file is preserved with a numeric suffix: `config.json;1`, `config.json;2`, and so on â ensuring no edit is ever silently overwritten.

![picoZ80 Web Interface â ESP32 Firmware Update](https://eaw.app/images/picoZ80_web_ota_esp32.png)

Firmware Updates â RP2350 (ota-rp2350.htm)

The RP2350 OTA page manages the two RP2350 firmware partitions:

* RP2350 Partitions panel  
  - lists all three partitions: partition 0 (Bootloader), partition 1 (first application slot, e.g. "Z80 CPU Emulator"), and partition 2 (second slot). Each row shows the flash address, size, checksum, active/running flag, license, author, description, version, and build date. The currently running partition is marked "Yes" in the Active column.
* RP2350 Firmware Upload panel  
  - accepts a pure binary `.bin` firmware file from `fw/bin/`. UF2 is **not** used here â application partitions are located at non-standard flash addresses that UF2 cannot express, so the OTA transfer uses raw binary. Use the **Partition 1** / **Partition 2** radio buttons to select the target slot. Two additional checkboxes are available: **Clear App Config** erases the ROM images and minified JSON configuration partition associated with the target slot (useful when upgrading to a firmware version with an incompatible config schema), and **Clear Flash Header** resets the flash partition header to factory defaults, rebuilding the partition table from scratch while preserving the bootloader configuration. The upload is verified by checksum before the new partition is activated.
* RP2350 Active Partition panel  
  - independently switches the active partition without uploading new firmware. Selecting a partition here triggers an automatic reboot into the chosen slot â useful for switching between two pre-loaded firmware variants (e.g. Z80 and a test build) without any file transfer.

![picoZ80 Web Interface â RP2350 Firmware Update](https://eaw.app/images/picoZ80_web_ota_rp2350.png)

WiFi Manager (wifimanager.htm)

**Note:**

The WiFi Manager page is only available when the ESP32 firmware is built with WiFi enabled (

`sdkconfig.mode_wifi_only`

or

`sdkconfig.mode_wifi_and_ncm`

). In NCM Only mode this page is not present in the navigation â network connectivity is provided automatically via USB NCM with no user configuration required.

The WiFi Manager configures how the picoZ80 connects to a wireless network. The top panel shows the currently active WiFi configuration (SSID, assigned IP, netmask, and gateway). The Configure WiFi form below it exposes all settings:

* WiFi Mode  
  - **Access Point**: the picoZ80 broadcasts its own SSID and you connect directly to it (useful during initial setup or when no infrastructure network is available). **Client**: the picoZ80 joins an existing WiFi network as a station.
* SSID and Password  
  - the name and passphrase of the network to join (client mode) or to broadcast (AP mode).
* DHCP Mode  
  - **Enabled**: the board requests an address from the network's DHCP server. **Disabled**: use a static IP, netmask, and gateway as entered in the fields below. A fixed IP is recommended so that the web interface address is always predictable.

Settings are saved to the ESP32's NVS (non-volatile storage) by clicking

**Save**

and take effect on the next reboot.

![picoZ80 Web Interface â WiFi Manager](https://eaw.app/images/picoZ80_web_wifimanager.png)

Action Menu and Reboot Menu

The two dropdown menus in the top-right navigation bar are available on every page of the web interface, providing quick access to runtime operations and system reset functions without navigating away from the current page.

The

**Action Menu**

(cog icon) provides runtime operations that take effect immediately without a reboot: swapping floppy disk or QuickDisk images on the fly, and triggering a live configuration reload on the RP2350. The currently loaded disk image filenames are displayed next to each entry so the operator can see at a glance which images are mounted.

The

**Reboot Menu**

(rotate icon) provides targeted reset options for each subsystem â ESP32, RP2350, host computer, and IPL â plus two UF2 recovery options for reflashing the RP2350 via USB mass-storage when the board is physically inaccessible inside a host machine. The two UF2 entries provide complementary recovery paths: the bootloader route works even when the main application is broken, while the app route works even when the bootloader needs replacing.

![picoZ80 Web Interface â Action Menu](https://eaw.app/images/picoZ80_web_actionmenu.png)
![picoZ80 Web Interface â Reboot Menu](https://eaw.app/images/picoZ80_web_reboot_menu.png)
âââââââââââââââââââââââââââââââââââ

Reference Sites
---------------

The table below contains all the sites referenced in the design and programming of the picoZ80.

| Site | Language | Description |
| --- | --- | --- |
| [RP2350 Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/rp2350.html) | English | Official Raspberry Pi RP2350 technical reference and datasheet. |
| [Pico SDK](https://github.com/raspberrypi/pico-sdk) | English | Raspberry Pi Pico C/C++ SDK â build system and hardware abstraction used by the picoZ80 firmware. |
| [Z80 CPU User Manual](https://www.zilog.com/docs/z80/um0080.pdf) | English | Zilog Z80 CPU family user manual â bus timing, instruction set and signal descriptions. |
| [ESP-IDF](https://github.com/espressif/esp-idf) | English | Espressif IoT Development Framework used for the ESP32 co-processor firmware. |
| [Sharp MZ Series](https://sharp-mz.com) | English | Community resource for Sharp MZ computer hardware, software and technical documentation. |

---

Manuals and Datasheets
----------------------

The table below contains all the datasheets and manuals referenced in the design and programming of the picoZ80.

| Datasheet | Language | Description |
| --- | --- | --- |
| [RP2350](https://eaw.app/Downloads/RP2350_Datasheet.pdf) | English | Raspberry Pi RP2350 microcontroller datasheet. |
| [ESP32-S3](https://eaw.app/Downloads/ESP32-S3_Datasheet.pdf) | English | Espressif ESP32-S3 SoC datasheet â WiFi/BT co-processor on the picoZ80 board. |
| [APS6404L PSRAM](https://eaw.app/Downloads/APS6404L_PSRAM_Datasheet.pdf) | English | 8MB SPI PSRAM datasheet â the main extended RAM used for memory banking. |
| [W25Q128 Flash](https://eaw.app/Downloads/W25Q128_Flash_Datasheet.pdf) | English | Winbond 16MB SPI NOR Flash datasheet â stores firmware and ROM images. |
| [TLV62590](https://eaw.app/Downloads/TLV62590_Datasheet.pdf) | English | Texas Instruments 5Vâ3.3V synchronous buck converter powering the picoZ80 from the Z80 DIP-40 VCC pin. |
| [CH334F](https://eaw.app/Downloads/CH334F_Datasheet.pdf) | English | CH334F 4-port USB 2.0 hub controller â provides USB hub functionality for firmware updates. |

---

Project Preview
---------------

Demonstration VideospicoZ80 running RFS (ROM Filing System) â Demo 1

The picoZ80 installed in a Sharp MZ-700, running the ROM Filing System (RFS) persona. The video demonstrates the virtual disk and memory banking capabilities of the board.

[

Your browser does not support the HTML5 video tag.
](../videos/picoZ80_rfs_demo_1.mp4)

picoZ80 v2.5 â Z80 CPU Tester

A short clip showing a Z80 CPU Tester board testing the picoZ80. The tester verifies that the picoZ80 is a genuine Z80, identifies it as an NMOS Z80, and runs test code at 8 MHz to confirm correct operation.

[

Your browser does not support the HTML5 video tag.
](../videos/picoZ80v2.5_Tester.mp4)

picoZ80 v2.5 â MZ-80A with Cassette Tape (CMT)

The picoZ80 v2.5 installed in a Sharp MZ-80A, loading a program from a physical cassette tape. Cassette loading is extremely time-sensitive â the Z80 must bit-bang the serial data stream from the tape hardware in real time with no margin for timing errors. This video demonstrates that the picoZ80 handles the critical CMT timing identically to a real Z80.

[

Your browser does not support the HTML5 video tag.
](../videos/PicoZ80v2.5_MZ80A_CMT.mp4)

picoZ80 v2.5 â MZ-80A with Floppy Disk

The picoZ80 v2.5 in a Sharp MZ-80A, reading from a real floppy disk controller and physical disk drive. Floppy disk access requires precise, time-critical interaction between the Z80 and the WD1773 FDC hardware â DRQ must be serviced within tight timing windows or data is lost. This video demonstrates that the picoZ80 interacts with real time-critical hardware the same as a genuine Z80.

[

Your browser does not support the HTML5 video tag.
](../videos/PicoZ80v2.5_MZ80A_Floppy.mp4)

picoZ80 v2.5a â MZ-2000

The picoZ80 v2.5a installed in a Sharp MZ-2000, running fully physical â all ROM, RAM, and VRAM accesses pass through to the real MZ-2000 hardware. The floppy disk controller is virtualised, with the picoZ80 emulating the MB8866 FDC and serving disk images from the SD card while the rest of the machine runs on its original hardware.

[

Your browser does not support the HTML5 video tag.
](../videos/PicoZ80v2.5a_MZ2000.mp4)

---

Commercial Use Restriction
--------------------------

**No commercial use permitted without express written permission.**

The picoZ80 hardware design (schematics, PCB layout, KiCad files), firmware, and all associated software are made available for personal, educational, and non-commercial use only. No part of this design â including but not limited to the PCB artwork, bill of materials, firmware binaries, source code, or documentation â may be used, reproduced, manufactured, sold, or incorporated into any commercial product or service without the express written permission of the author (Philip D. Smart).

To request a commercial licence or discuss permitted uses, please contact the author via the

[eaw.app](https://eaw.app)

website.

---

Credits
-------

The picoZ80 project builds on the work of several individuals and open-source projects. Their contributions are gratefully acknowledged.

* Manuel Sainz de Baranda y GoÃ±i  
  Author of the **Z80** C-language Z80 CPU emulator library ([github.com/redcode/Z80](https://github.com/redcode/Z80)). This high-accuracy, cycle-accurate Z80 emulator core is used by the picoZ80 firmware when running Z80 instructions internally on the RP2350, providing precise flag behaviour and undocumented opcode support. The library is used under the terms of the GNU General Public License v3.
* Raspberry Pi Ltd  
  Authors of the **Pico SDK** and RP2350 hardware. The PIO assembler, C SDK, CMake toolchain integration, and RP2350B silicon make the cycle-accurate bus interface possible.
* Espressif Systems  
  Authors of the **ESP-IDF** framework and ESP32 hardware. The ESP32 co-processor, WiFi stack, OTA library, and NVS storage framework underpin the web management interface.
* Philip Smart  
  Hardware design (KiCad schematics and PCB layout), RP2350 PIO firmware, ESP32 web application, JSON configuration system, Sharp MZ machine persona drivers, and all project documentation.
* Grok (xAI)  
  AI assistant that provided valuable help during PIO state machine debugging â particularly in diagnosing timing edge cases and cycle-accurate bus interaction issues in the RP2350 PIO programs.
* Claude (Anthropic)  
  AI assistant contributing to this project across multiple areas: authoring and structuring the project documentation, analysing the FSPI/UART interface between the RP2350 and ESP32 and providing firmware improvement recommendations, and ongoing firmware development assistance.

---

Licenses
--------

The picoZ80 project is composed of several components, each covered by its own licence:

| Component | Licence |
| --- | --- |
| picoZ80 RP2350 firmware (PIO, C sources) | GNU General Public License v3 |
| picoZ80 ESP32 firmware and web interface | GNU General Public License v3 |
| Z80 CPU emulator library (Manuel Sainz de Baranda y GoÃ±i) | GNU General Public License v3 |
| KiCad hardware design files (schematics, PCB, Gerbers) | Creative Commons BY-NC-SA 4.0 |
| Documentation and user guides | Creative Commons BY-NC-SA 4.0 |
| Raspberry Pi Pico SDK | BSD 3-Clause |
| ESP-IDF framework | Apache License 2.0 |
| Bootstrap 4 (web interface) | MIT License |

In short: the firmware and software you build from this project's source code are open-source under the GPL v3; the hardware designs and documentation are licensed under CC BY-NC-SA 4.0 (non-commercial use only â commercial licensing available on request); third-party libraries retain their own licences as listed above. See the

`LICENSE`

and

`NOTICE`

files in the repository for full details.

---

Licence Terms
-------------

**Copyright © 2019–2026 Philip Smart. All rights reserved.****Hardware Designs — CC BY-NC-SA 4.0**

All hardware designs (KiCad schematics, PCB layouts, Gerber fabrication files, bills of materials) are licensed under the

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

. You are free to share and adapt the designs for

**non-commercial purposes only**

, provided you give appropriate credit and distribute any modifications under the same licence.

**Commercial manufacture or sale requires a separate licence**

— please contact

[info@eaw.app](mailto:info@eaw.app)

.

**Firmware & Software — GNU GPL v3**

The firmware and software source code are free software under the

[GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html)

. You may redistribute and modify the code under the GPL v3 terms. Any distributed modifications must also be licensed under GPL v3 with source code made available.

**Trademark & Attribution**

The names

**picoZ80**

,

**pico6502**

, and

**engineers@work**

are trademarks of Philip Smart. You may not use these names to promote derivative products without written permission. You may not remove or alter copyright notices, author attribution, or boot/splash screen credits. Re-branding this project and presenting it as your own work is expressly prohibited. See the

`NOTICE`

file in the repository for full details.

**Commercial Licensing**

If you are a manufacturer or distributor interested in producing picoZ80 or pico6502 boards for commercial sale, please contact:

[info@eaw.app](mailto:info@eaw.app)

. Personal, educational, and hobbyist/club use is always permitted under the open-source licences above.

The full licence texts are included in the repository as

`LICENSE`

,

`LICENSE-HARDWARE.txt`

, and

`LICENSE-SOFTWARE.txt`

.

---

Wireless Regulatory Notice
--------------------------

**This device incorporates an ESP32-S3-PICO-1 wireless module that is capable of transmitting in the 2.4 GHz ISM band, making it an intentional radiator under radio-frequency regulations worldwide (including FCC Part 15 Subpart C in the United States, and the Radio Equipment Directive 2014/53/EU in the European Union) when WiFi is enabled.****NCM-Only Default for Uncertified Boards**

Because the picoZ80 as a finished assembly has not undergone FCC or RED certification, boards must be shipped with the WiFi antenna matching network

**unpopulated**

and the ESP32 firmware built using the

**NCM Only**

configuration (

`sdkconfig.mode_ncm_only`

). In this configuration no radio frequency energy is emitted and the board is not subject to intentional radiator regulations. The full web interface remains accessible over USB at

`http://192.168.7.1`

. See the

[Networking — FCC / RED Regulatory Notice](https://eaw.app/picoz80/#regulatory-notice)

section above for further details.

Although the ESP32-S3-PICO-1 module itself carries pre-existing regulatory certifications (FCC, CE, and others), those module-level certifications

**do not automatically extend to a finished product**

that incorporates the module. The pre-certified module exemption permits

**individual hobbyists**

to build a limited number of devices for

**personal, experimental, or educational use**

without obtaining separate equipment authorisation.

**Important Limitations**

* Assembled devices with WiFi enabled **must not be sold, offered for sale, gifted, or otherwise distributed** to third parties unless the finished product has been independently tested and granted its own equipment authorisation (e.g. FCC ID, CE marking with a Notified Body assessment) in the relevant jurisdiction.
* Boards shipped or distributed to others must use the **NCM Only** firmware configuration with the WiFi antenna matching network unpopulated.
* Building this project for personal use in limited quantities with WiFi enabled is generally permitted under hobbyist and experimental-use provisions (e.g. FCC § 15.23), provided the device does not cause harmful interference.
* Regulatory requirements vary by country. Builders outside the United States should consult their national radio-frequency authority for applicable rules.

**Builder’s Responsibility**

It is the builder’s sole responsibility to ensure that any device constructed from these designs complies with all applicable radio-frequency regulations in their jurisdiction. The author provides these designs for personal, educational, and hobbyist use and makes no representation that a device built from them satisfies the regulatory requirements for commercial distribution.