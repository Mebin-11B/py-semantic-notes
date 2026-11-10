---
title: "A Matter Wi-Fi Light Bulb in Rust on the Raspberry Pi Pico 2 W"
url: https://github.com/melastmohican/rust-rpico2-embassy-examples
clipped: 2026-06-17 00:51:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A Matter Wi-Fi Light Bulb in Rust on the Raspberry Pi Pico 2 W](https://github.com/melastmohican/rust-rpico2-embassy-examples)

## Digest Summary
The repository provides Rust Embassy example applications for the Raspberry Pi Pico 2 (RP2350) board. The RP2350 features dual‑core Arm Cortex‑M33 and RISC‑V cores and exposes I²C0 (GPIO4 SDA, GPIO5 SCL), I²C1 (GPIO2 SDA, GPIO3 SCL), UART0 (GPIO0 TX, GPIO1 RX) and UART1 (GPIO8 TX, GPIO9 RX). Examples include:

- **hs3003_i2c**: reads temperature (‑40 °C to +125 °C, ±0.2 °C) and humidity (0‑100 % RH, ±1.5 %) from a Renesas HS3003 via I²C0 (GPIO4/5).  
- **adxl345_i2c**: reads 13‑bit 3‑axis acceleration (±16 g) from an ADXL345 on I²C0.  
- **zermatt** / **zermatt_snow**: drives an Adafruit 2.2″ 320×240 TFT via SPI (GPIO18 SCK, GPIO19 MOSI, GPIO16 MISO, GPIO20 DC, GPIO21 RST, GPIO17 TCS), rendering static or animated graphics using an async framebuffer and DMA.  
- **ds18b20**: obtains 9‑12‑bit temperature (‑55 °C to +125 °C, ±0.5 °C) from a DS18B20 1‑Wire sensor using a cycle‑accurate PreciseDelay on Cortex‑M33 (GPIO16).  
- **dht11**: reads temperature (0‑50 °C, ±2 °C) and humidity (20‑90 % RH, ±5 %) from a DHT11 via async dht‑sensor crate; requires release mode and a pull‑up resistor.  
- **matter_wifi_light**: implements a Matter‑compatible Wi‑Fi light bulb using rs‑matter, BLE commissioning, and Wi‑Fi connectivity; an external LED on GPIO15 (220‑330 Ω series) mirrors the light state.  
- **blinky**: simple LED blink on GPIO15, sharing wiring with the Matter example. All examples are built and run with `cargo run --example `.

## Discussion Summary
The discussion highlights growing confidence in using Rust for embedded smart‑home development, especially on the RP2350 platform. Contributors note that a fully standards‑compliant Matter device can be built with a no‑std, async architecture, leveraging the rs‑matter stack and embassy framework. Technical observations focus on radio coexistence challenges, such as tuning the SPI clock to prevent bus corruption when BLE and Wi‑Fi run concurrently. Overall sentiment is positive, emphasizing Rust’s increasing approachability compared with traditional C++ SDKs while acknowledging the need for careful hardware configuration.

---

## Full Article

Rust Embassy Examples for Raspberry Pi Pico 2
=============================================

This repository contains examples for the Raspberry Pi Pico 2 (RP2350) board, written in Rust using the [Embassy](https://embassy.dev/) async framework.

```
cargo generate --git https://github.com/ImplFerris/pico2-template.git --name rust-rpico2-embassy-examples
```

**Board:** Raspberry Pi Pico 2

* **MCU:** RP2350 (Dual-core Arm Cortex-M33 and RISC-V cores)
* **On-board peripherals:**

[![Raspberry Pi Pico 2 Pinout](https://camo.githubusercontent.com/7b92bb330378f426ed7f531c7842803bf42c3f3f90f805022804cd1bbdbe423a/68747470733a2f2f7777772e72617370626572727970692e636f6d2f646f63756d656e746174696f6e2f6d6963726f636f6e74726f6c6c6572732f696d616765732f7069636f2d322d72342d70696e6f75742e737667)](https://camo.githubusercontent.com/7b92bb330378f426ed7f531c7842803bf42c3f3f90f805022804cd1bbdbe423a/68747470733a2f2f7777772e72617370626572727970692e636f6d2f646f63756d656e746174696f6e2f6d6963726f636f6e74726f6c6c6572732f696d616765732f7069636f2d322d72342d70696e6f75742e737667)

* **I2C pins:**
  + **I2C0 SDA:** GPIO4
  + **I2C0 SCL:** GPIO5
  + **I2C1 SDA:** GPIO2
  + **I2C1 SCL:** GPIO3
* **UART pins:**
  + **UART0 TX:** GPIO0, **UART0 RX:** GPIO1
  + **UART1 TX:** GPIO8, **UART1 RX:** GPIO9

Reads temperature and humidity from an HS3003 sensor using the Embassy async framework.

```
cargo run --example hs3003_i2c
```

**Wiring (Arduino Modulino Thermo):**

```
     Modulino -> RPi Pico 2
----------    --------------
GND (black) -> GND
VCC (red)   -> 3.3V
SCL (yellow)-> GPIO5 (Pin 7) (I2C0 SCL)
SDA (blue)  -> GPIO4 (Pin 6) (I2C0 SDA)
```

**About HS3003:**

The Renesas HS3003 is a high-performance temperature and humidity sensor:

* Temperature range: -40°C to +125°C (±0.2°C accuracy)
* Humidity range: 0% to 100% RH (±1.5% accuracy)
* 14-bit resolution for both measurements
* Ultra-low power consumption

Reads accelerometer data from an ADXL345 sensor over I2C0 using Embassy.

```
cargo run --example adxl345_i2c
```

**Wiring:**

```
     ADXL345 -> RPi Pico 2
----------    --------------
GND (black) -> GND
VCC (red)   -> 3.3V
SCL (yellow)-> GPIO5 (Pin 7) (I2C0 SCL)
SDA (blue)  -> GPIO4 (Pin 6) (I2C0 SDA)
```

**About ADXL345:**

The ADXL345 is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g. Digital output data is formatted as 16-bit twos complement and is accessible through either an SPI (3- or 4-wire) or I2C digital interface.

Displays a 320x240 image of Zermatt on the Adafruit 2.2" TFT LCD display in landscape mode.

```
cargo run --example zermatt
```

**Wiring (Eye-SPI Breakout):**

```
     Raspberry Pi Pico 2              Eye-SPI Breakout
   +-----------------------+      +---------------------------+
   |                       |      |                           |
   |  3V3 (Pin 36) --------+------+-> VIN   (Red Wire)        |
   |  GND (Pin 38) --------+------+-> GND   (Black Wire)      |
   |  GPIO18 (Pin 24) -----+------+-> SCK   (Blue Wire)       |
   |  GPIO19 (Pin 25) -----+------+-> MOSI  (Green Wire)      |
   |  GPIO16 (Pin 21) -----+------+-> MISO  (Yellow Wire)     |
   |  GPIO20 (Pin 26) -----+------+-> DC    (White Wire)      |
   |  GPIO21 (Pin 27) -----+------+-> RST   (Orange Wire)     |
   |  GPIO17 (Pin 22) -----+------+-> TCS   (Blue Wire)       |
   |                       |      |                           |
   +-----------------------+      +---------------------------+
```

Displays a 320x240 image of Zermatt on the Adafruit 2.2" TFT LCD display with animated falling snow, utilizing a physics engine and the Embassy async framework to draw to an off-screen `lcd-async` framebuffer and dispatch via DMA without blocking the CPU.

```
cargo run --example zermatt_snow
```

Wiring is identical to the `zermatt` example.

Reads temperature from a DS18B20 waterproof temperature sensor probe over a 1-Wire bus using Embassy. It utilizes a custom, cycle-accurate `PreciseDelay` implementation to achieve jitter-free sub-microsecond timing required by the 1-Wire protocol on the RP2350's Cortex-M33 core.

```
cargo run --example ds18b20
```

**Wiring Schematic:**

```
                              Raspberry Pi Pico 2
                           +-----------------------+
                           |                       |
                           | [ ] 1      40 [ ] USB |
                           | [ ] 2      39 [ ]     |
                           | [ ] 3      38 [G]ND --+-------+ (black)
                           | [ ] 4      37 [ ]     |       |
                           | [ ] 5      36 [3]V3 --+---+   |
                           |  ...        ...       |   |   |
                           | [ ] 20     21 [ ] ----+---+---|---+ (white, GPIO16)
                           +-----------------------+   |   |   |
                                                       |   |   |
                                                       |   |   |
                   +-----------------------------+     |   |   |
                   |     DS18B20 Sensor / Probe  |     |   |   |
                   |      (Bottom/Flat Side)     |     |   |   |
                   |                             |     |   |   |
                   |     [GND]   [DAT]   [VCC]   |     |   |   |
                   +-------|-------|-------|-----+     |   |   |
                           |       |       |           |   |   |
                           |       +-------+--[5K1]----+   | (Pull-Up Resistor
                           |       |       |   Resistor    |  between DAT & VCC)
                           |       |       +---------------+ (red)
                           +-------|-----------------------+ (black)
                                   |
                                   +--------------------------- (white)
```

**Breadboard Layout:**

[![DS18B20 Breadboard Wiring Layout](https://github.com/melastmohican/rust-rpico2-embassy-examples/raw/main/pico-DS18B20_bb.png)](https://github.com/melastmohican/rust-rpico2-embassy-examples/blob/main/pico-DS18B20_bb.png)

**About DS18B20:**

The DS18B20 is a 1-Wire digital thermometer that provides 9-bit to 12-bit Celsius temperature measurements. It communicates over a 1-Wire bus, requiring only one data line (and ground) to interface with the microcontroller. It has a temperature range of -55°C to +125°C with ±0.5°C accuracy from -10°C to +85°C.

Reads temperature and humidity from a DHT11 sensor using the Embassy async framework. It utilizes the async API of the `dht-sensor` crate combined with our cycle-accurate `PreciseDelay` implementation.

```
cargo run --example dht11 --release
```

Note: Due to timing sensitivity of the DHT11 protocol during the bit-read phase, you must run this example in **release** mode.

**Wiring Schematic:**

```
                     Raspberry Pi Pico 2             DHT11 Module
                   +---------------------+      +---------------------+
                   |                     |      |                     |
                   | GND (Pin 38) -------+----->| GND                 |
                   | 3V3 (Pin 36) -------+----->| VCC                 |
                   | GPIO16 (Pin 21) ----+----->| DAT (Data)          |
                   |                     |      |                     |
                   +---------------------+      +---------------------+
```

Important

**Pull-up Resistor:**

* **If using a DHT11 module board:** It likely already has a built-in pull-up resistor. No extra component is needed.
* **If using a bare 4-pin DHT11 sensor:** You must add an external 4.7kΩ to 10kΩ pull-up resistor between the DAT (Data) and VCC lines.

**About DHT11:**

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed). It has a temperature range of 0°C to 50°C (±2°C accuracy) and humidity range of 20% to 90% RH (±5% accuracy).

Implements a Matter-compatible Wi-Fi light bulb using the rs-matter stack. It uses BLE for commissioning and Wi-Fi for network connectivity, allowing you to add the Pico 2 W directly into Apple Home, Google Home, or Home Assistant! When toggled from your smart home app, it turns an external LED on and off.

```
cargo run --example matter_wifi_light --release
```

**Provisioning in Home Assistant:**

1. Run the example on your Pico 2 W. It will begin advertising over Bluetooth.
2. Open the Home Assistant companion app on your smartphone.
3. Go to **Settings** -> **Devices & Services** -> **Add Integration** -> **Add Matter device**.
4. When prompted for a setup code, enter the default `3497-0112-332` (or scan the QR code link printed in the terminal logs).
5. Home Assistant will connect to the Pico 2 W over BLE, ask for your Wi-Fi credentials, and securely transmit them to the device.

   [![Home Assistant Provisioning](https://github.com/melastmohican/rust-rpico2-embassy-examples/raw/main/HAApp.jpg)](https://github.com/melastmohican/rust-rpico2-embassy-examples/blob/main/HAApp.jpg)
6. The Pico 2 W will connect to your Wi-Fi network and immediately appear as a standard light bulb. You can use the Home Assistant interface to toggle the light on and off!

   [![Home Assistant Toggle](https://github.com/melastmohican/rust-rpico2-embassy-examples/raw/main/HAToggle.png)](https://github.com/melastmohican/rust-rpico2-embassy-examples/blob/main/HAToggle.png)
7. The external LED wired to your Pico 2 W will instantly mirror the state!

   [![Matter Wi-Fi Light Circuit](https://github.com/melastmohican/rust-rpico2-embassy-examples/raw/main/matter_wifi_light.jpg)](https://github.com/melastmohican/rust-rpico2-embassy-examples/blob/main/matter_wifi_light.jpg)

**Wiring Schematic:**

```
           Raspberry Pi Pico 2 W                   External Components
         +------------------------+
         |                        |
         |         GP15 (Pin 20)  |---------[ 220-330 Ohm Resistor ]-----+
         |                        |                                      |
         |         GND (Pin 18)   |------------------[ LED - ] <---+     |
         |                        |                                |     |
         +------------------------+                     (Cathode / |     |
                                                         Short Leg) |     |
                                                                   |     |
                                                        [ LED + ] -+-----+
                                                        (Anode /
                                                         Long Leg)
```

Blinks an external LED connected to GPIO15. This is useful for boards like the Raspberry Pi Pico 2 W, where the onboard LED is connected to the wireless chip rather than a standard microcontroller GPIO.

```
cargo run --example blinky
```

**Wiring:** Same wiring as the `matter_wifi_light` example.