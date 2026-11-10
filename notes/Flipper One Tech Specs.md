---
title: "Flipper One Tech Specs"
url: https://docs.flipper.net/one/general/tech-specs
clipped: 2026-06-17 00:59:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hardware specifications
  - pentesting tools
  - single board computers
  - embedded controllers
  - modular hardware
related:
  - "[[Pentesting Tools]]"
  - "[[Single Board Computers]]"
  - "[[Embedded Controllers]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Flipper One is an upcoming handheld pentesting device featuring a Rockchip RK3576 processor, dual Ethernet ports, an RP2350 microcontroller, and an M.2 expansion slot.
>
> **Key points:**
> - Processing is handled by an 8-core Rockchip CPU and a Raspberry Pi RP2350 microcontroller driving a grayscale LCD.
> - Connectivity is highly expanded, incorporating USB-C 3.1, HDMI 2.1, dual RJ45 Gigabit Ethernet, Wi-Fi 6, and Bluetooth.
> - Critics note the removal of physical radios (NFC, RFID, IR) that defined the original Flipper Zero, moving the design closer to a mini-computer.
>
> **Concept links:** [[Hardware Specifications]], [[Pentesting Tools]], [[Single Board Computers]], [[Embedded Controllers]], [[Modular Hardware]]
>
> **Suggested connections:**
> - [[Pentesting Tools]] — specialized hardware for security testing and signal analysis.
> - [[Single Board Computers]] — high-performance compact computing architectures.
> - [[Embedded Controllers]] — microcontrollers like the RP2350 used for low-latency hardware control.
<!-- ai-summary:end -->

# [Flipper One Tech Specs](https://docs.flipper.net/one/general/tech-specs)

## Digest Summary
Flipper One is a handheld device (155 mm × 67 mm × 40 mm) built from PC/ABS body, anodized‑aluminum brackets, TPU bumpers, and a Gorilla‑Glass screen. It features a 256 × 144 monochrome LCD (64‑level grayscale) driven via QSPI.

**Connectivity**  
- USB‑C 1: USB 3.1 (5 Gbps), DisplayPort Alt‑Mode, PD charging  
- USB‑C 2: USB 3.1 host‑only, power out  
- USB‑A: USB 3.1 host‑only, power out  
- HDMI 2.1 full‑size, CEC, 4K @ 120 Hz  
- Dual RJ45 gigabit Ethernet (Realtek RTL8211F)  
- 3.5 mm TRRS audio jack, Nuvoton NAU8822 codec  
- microSD (UHS‑I SDR104) and nano‑SIM slots  
- M.2 Key B expansion (PCIe 2.1 × 1, USB 2.0/3.1, SATA 3, UART, I²C, etc.)

**Processing**  
- Main CPU: Rockchip RK3576 (8 cores: 4 × Cortex‑A72 + 4 × Cortex‑A53, up to 2.2 GHz)  
- GPU: Mali‑G52 MC3 (OpenGL ES 1.1/2.0, OpenCL 2.1, Vulkan 1.2)  
- NPU: 6 TOPS @ int8 (supports int4/int8/int16, fp16, bf16, tf32)  
- MCU: Raspberry Pi RP2350B (dual Cortex‑M33 + dual RISC‑V Hazard3 @ 150 MHz, 520 KB SRAM, 16 MB flash)

**Memory & Storage**  
- 8 GB LPDDR5 RAM  
- 64 GB UFS 2.2 internal, plus microSD slot

**Power**  
- 24 000 mWh (≈7 000 mAh) battery, TI BQ25792 charger, PD up to 26 V  
- Battery gauge TI BQ28Z610

**Additional hardware**  
- Wi‑Fi 6 (MT7921AUN, 2×2 MIMO) and Bluetooth 5.2 integrated  
- Touchpad with haptic feedback, five app buttons, D‑pad, power button, PTT button  
- GPIO and debug ports expose numerous signals for custom expansion.

## Discussion Summary
The comments show mixed reactions to the Flipper One. Reviewers appreciate the added Ethernet ports, higher‑end Wi‑Fi, cellular and AI capabilities, and see potential for router or portable server use. At the same time many note the device’s larger size, high price, power draw and modest grayscale display as drawbacks. A recurring criticism is the removal of NFC, RFID, IR and other radio functions that defined earlier models, leading to disappointment despite the expanded feature set.

---

## Full Article

this page describes the full technical specifications of the flipper one since the device is under active development, specifications may change flipper one outline size and weight ⚠️ final weight is pending — value below is a placeholder flipper one — front view with dimensions width 155 mm (6 1 inches) height 67 mm (2 64 inches) depth 40 mm (1 57 inches) weight tbd grams (tbd ounces) materials flipper one materials body pc/abs buttons pc/abs screen gorilla glass heat sink anodized aluminum bracket anodized aluminum lanyard loop anodized aluminum bumpers tpe monochrome lcd display resolution 256 × 144 pixels grayscale 64 levels (6 bit) interface qspi (driven by mcu) ports flipper one top and back ports flipper one audio port and usb c1 flipper one ethernet ports flipper one microsd and sim slots usb c1 usb 3 1 (5 gbps), displayport alt mode, usb power delivery (input and output) usb c2 usb 3 1 (5 gbps), host only, power output usb a usb 3 1 (5 gbps), host only, power output hdmi out full size, v2 1, cec support, 4k @ 120 hz ethernet 2× rj45, gigabit 3 5 mm audio jack stereo out and microphone input (trrs) microsd card slot supports uhs i sdr104 sim card slot nano sim (4ff), passively connected to m 2 port controls flipper one controls touchpad fast scrolling, haptic feedback app buttons 5 buttons below the screen power button power on / sleep / off, ctrl+alt+del menu, kill app 5 button d pad directional navigation back button return app switcher single click = alt+tab, double click = extra menu push to talk (ptt) button controllable in linux userspace main cpu — rk3576 flipper one cpu and mcu cpu rockchip rk3576 cores 8 — 4× high performance arm cortex a72 + 4× efficiency arm cortex a53, up to 2 2 ghz gpu arm mali g52 mc3 — opengl es 1 1/2 0/3 2, opencl 2 1, vulkan 1 2 npu 6 tops @int8 — supports int4, int8, int16, fp16, bf16, tf32 low power mcu — rp2350 mcu raspberry pi rp2350b cores dual arm cortex m33 @ 150 mhz + dual risc v hazard3 @ 150 mhz sram 520 kb flash 16 mb memory and storage ram 8 gb lpddr5 internal storage 64 gb ufs 2 2 microsd card slot ⚠️ (uhs i sdr104 — needs verification) battery and power battery energy 24000 mwh battery capacity 7000 mah ⚠️ (not final) charger ic ti bq25792, up to 3 32 a fuel gauge ti bq28z610 charging via usb c1 port, usb power delivery supported wi fi & bluetooth module wxt2am2101 wi fi chipset mediatek mt7921aun wi fi modes wi fi 6e (802 11ax), 2 4 / 5 / 6 ghz bands, 2×2 mimo bluetooth 5 2 (integrated in mt7921aun) module interface usb 3 0 gigabit ethernet ports 2× ethernet (1 gbit/s) phy ic realtek rtl8211f cg video output hdmi v2 1, full size connector (type a), cec support, up to 4k\@120 hz displayport v1 4 alt mode via usb c1, up to 4k\@120 hz audio codec nuvoton nau8822 speaker ⚠️ needs clarification 3 5 mm jack stereo out + microphone input (trrs) m 2 expansion port the m 2 expansion port is at the back of the device, under the back plate flipper one m 2 expansion port m 2 type key b supported sizes 2230 (via extender), 2242, 3042, 3052 supported thickness up to s3 (single sided modules) interfaces pcie 2 1 x1 / usb 2 0 / usb 3 1 / sata3 / serial audio / uart / i2c / sim card m 2 port pinout flipper one m 2 port pinout description pin pin description — — 1 config 3 3 3v 2 3 gnd 3 3v 4 5 gnd full card power off# (o)(0/1 8v or 3 3v) 6 7 usb d+ w disable1# (o)(0/1 8v/3 3v) 8 9 usb d gpio 9/das/dss (i/o)/led 1# (i)(0/3 3v) 10 11 gnd connector key b — — connector key b gpio 5 (i/o)(0/1 8v) 20 21 config 0 gpio 6 (i/o)(0/1 8v) 22 23 gpio 11 (i/o)(0/1 8v) gpio 7 (i/o)(0/1 8v) 24 25 dpr (o)(0/1 8v) gpio 10 (i/o)(0/1 8v) 26 27 gnd pla s2# (i)/gpio 8 (i/o)(0/1 8v) 28 29 pern1/usb3 1 rx /ssic rxn uim reset (i) 30 31 perp1/usb3 1 rx+/ssic rxp uim clk (i) 32 33 gnd uim data (i/o) 34 35 petn1/usb3 1 tx /ssic txn uim pwr (i) 36 37 petp1/usb3 1 tx+/ssic txp devslp (o) 38 39 gnd gpio 0 (i/o)/smb clk (i/o)/(0/1 8v) 40 41 pern0/sata b+ gpio 1 (i/o)/smb data (i/o)/(0/1 8v) 42 43 perp0/sata b gpio 2 (i/o)/alert# (i)(0/1 8v) 44 45 gnd gpio 3 (i/o)(0/1 8v) 46 47 petn0/sata a gpio 4 (i/o)(0/1 8v) 48 49 petp0/sata a+ perst# (o)(0/1 8v/3 3v) 50 51 gnd clkreq# (i/o)(0/1 8v/3 3v) 52 53 refclkn pewake# (i/o)(0/1 8v/3 3v) 54 55 refclkp nc 56 57 gnd nc 58 59 antctl0 (i)(0/1 8v) coex3 (i/o)(0/1 8v) 60 61 antctl1 (i)(0/1 8v) coex txd (o)(0/1 8v) 62 63 antctl2 (i)(0/1 8v) coex rxd (i)(0/1 8v) 64 65 antctl3 (i)(0/1 8v) sim detect (o) 66 67 reset# (o)(0/1 8v) susclk (o)(0/1 8v/3 3v) 68 69 config 1 3 3 v/vbat 70 71 gnd 3 3 v/vbat 72 73 vio cfg (i) or gnd 3 3 v/vbat 74 75 config 2 gpio pinout flipper one gpio port pinout description pin pin description 3 3 v power, up to 2a efuse 3v3 gnd ground mcu gpio 40 pio adc0 pwm8 a m40 m41 mcu gpio 41 pwm8 b adc0 pio cpu gpio4 b4 d spdif rx0 m0 i2c3 sda m0 uart2 rx m1 can1 rx m2 b4 b5 cpu gpio4 b5 d can1 tx m2 uart2 tx m1 i2c3 scl m0 spdif tx0 m0 cpu gpio4 b2 d sai1 sdo3 m0 sai1 sdi1 m0 pdm1 sdi1 m1 spi4 miso m2 b2 b3 cpu gpio4 b3 d pwm2 ch7 m0 spi3 csn1 m2 spi4 csn0 m2 pdm1 sdi0 m1 sai4 sd0 m0 sai1 sdi0 m0 cpu gpio4 b0 d sai1 sdo1 m0 sai1 sdi3 m0 pdm1 clk1 m1 spi4 clk m2 uart5 tx m1 uart6 rtsn m0 uart2 rtsn m1 b0 b1 cpu gpio4 b1 d uart2 ctsn m1 uart6 ctsn m0 uart5 rx m1 spi4 mosi m2 pdm1 sdi2 m1 sai1 sdi2 m0 sai1 sdo2 m0 cpu gpio4 a6 d sai4 lrck m0 pdm1 clk0 m1 spi3 miso m2 i2c4 sda m1 uart6 rx m0 can0 rx m2 a6 a7 cpu gpio4 a7 d pwm2 ch6 m0 spi3 clk m2 sai4 sdi1 m0 sai1 sdo0 m0 cpu gpio4 a4 d sai4 sclk m0 pdm1 sdi3 m1 spi3 mosi m2 i2c4 scl m1 uart6 tx m0 can0 tx m2 a4 a5 cpu gpio4 a5 d i2c2 sda m2 uart5 ctsn m1 spi4 csn1 m2 sai1 lrck m0 cpu gpio4 a2 d sai1 mclk m0 sai4 mclk m0 pwm2 ch5 m0 a2 a3 cpu gpio4 a3 d pwm2 ch4 m1 i2c2 scl m2 uart5 rtsn m1 spi3 csn0 m2 sai1 sclk m0 5v power, up to 2a efuse 5v gnd ground cpu usb 2 0 data+ d+ d cpu usb 2 0 data debug port pinout flipper one debug port pinout description pin pin description 3v3 ⚠️ mcu power 1 2 mcu reset mcu swd clock 3 4 mcu swd io mcu uart tx 5 6 mcu uart rx mcu gpio 41 7 8 mcu gpio 40 cpu reset 9 10 cpu uart0 tx cpu uart0 rx 11 12 cpu gpio0 d2 cpu gpio0 d3 13 14 gnd

Have a question?

Our support team and an awesome community will get you an answer in a flash. Please leave your questions in English.

To ask a question or participate in discussions, you'll need to authenticate first.