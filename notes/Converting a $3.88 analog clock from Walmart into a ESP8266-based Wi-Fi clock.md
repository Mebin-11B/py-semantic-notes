---
title: "Converting a $3.88 analog clock from Walmart into a ESP8266-based Wi-Fi clock"
url: "https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock"
clipped: 2026-06-17 01:47:14
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - internet of things
  - hardware hacking
  - esp8266 microcontroller
  - ntp synchronization
  - non-volatile memory
related:
  - "[[Embedded Systems]]"
  - "[[DIY Hardware]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A DIY project details converting a cheap analog quartz clock into an auto-syncing, Wi-Fi-enabled NTP clock using an ESP8266 and EERAM.
>
> **Key points:**
> - Modifies a cheap quartz clock movement to control its Lavet stepping motor using bipolar pulses from an ESP8266.
> - Leverages Network Time Protocol (NTP) to auto-synchronize the clock and adjust for daylight savings.
> - Utilizes a Microchip 47L04 Serial EERAM to store and restore clock hand positions across power outages.
> - Provides a local web interface hosted on the ESP8266 for setup, diagnostics, and vector-drawn clock face status.
>
> **Concept links:** [[Internet Of Things]], [[Hardware Hacking]], [[Esp8266 Microcontroller]], [[Ntp Synchronization]], [[Non-Volatile Memory]]
>
> **Suggested connections:**
> - [[ESP8266 Microcontroller]] — the core wireless processing module used in this build.
> - [[Internet of Things]] — shows how analog consumer devices can be retrofitted with network interfaces.
<!-- ai-summary:end -->

# [Converting a $3.88 analog clock from Walmart into a ESP8266-based Wi-Fi clock](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock)

## Digest Summary
The repository hosts an Arduino sketch for the ESP8266 module that enables an inexpensive analog quartz clock to show the local time. By connecting the ESP8266 to Wi‑Fi, the sketch obtains current time data and drives the clock’s stepper or motor mechanism to position the hands accurately. The project’s purpose is to retrofit a low‑cost analog clock with network‑based time synchronization, requiring only the ESP8266 hardware and the provided software. No additional components or external time sources are needed beyond standard Wi‑Fi access. The code and instructions are organized for straightforward compilation and upload to the ESP8266, allowing the analog display to reflect real‑time updates automatically.

## Discussion Summary
The comments collectively praise the project’s inventive use of inexpensive SRAM‑EEPROM backup and its hackable, open‑source nature, while also noting enthusiasm for similar DIY clock upgrades, GPS or NTP synchronization, and LED projection ideas. Several participants raise practical concerns about long‑term drift, power consumption, battery life, and reliable stepper control, suggesting Hall‑sensor feedback, protective H‑bridge circuitry, and DST handling improvements. Comparisons to commercial radio‑controlled or Wi‑Fi clocks highlight cost and convenience trade‑offs, and many express interest in extending the design with alternative displays or more robust time‑source integration.

---

## Full Article

ESP8266 WiFi Analog Clock
=========================

This project uses an WEMOS D1 Mini ESP8266 module and an Arduino sketch to connect to a NTP (Network Time Protocol) server to automatically retrieve and display the local time on a inexpensive analog quartz clock. The ESP8266 reconnects to the NTP server every 15 minutes which keeps the clock accurate. The clock also automatically adjusts for daylight savings time.

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/Clock-face.JPEG)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/Clock-face.JPEG)

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/Clock-back.JPEG)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/Clock-back.JPEG)

WEMOS D1 Mini ESP8266 Module with EERAM IC and Components on a Piece of Perfboard

  
  

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/Schematic.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/Schematic.jpg)

Schematic

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/AnalogClock.gif)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/AnalogClock.gif)

I'm using an analog clock with a quartz movement I found at my local Walmart for $3.88. Whatever analog clock you decide to use, its quartz movement will need to be modified so that it can be controlled by the ESP8266 module. Open up the movement (most of them snap together without any fasteners), disconnect the internal coil of the Lavet stepping motor from its quartz oscillator and then solder a wire to each of the coil's leads to make connections for the ESP8266. If you search around on the web you'll find articles showing how others have done it. Be careful when working with the coil. The coil's wires are typically thinner than a human hair and extremely fragile.

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/Clock%20Movement.jpeg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/Clock%20Movement.jpeg)

Modified Clock Movement

The sketch: AnalogClock.ino should be (I hope) clear enough, but here, in brief, is a summary of how it operates. Ten times each second the ESP8266 compares the time displayed on the analog clock to the actual time retrieved from an NTP server. If the analog clock lags behind the actual time, the ESP8266 advances the clock's second hand until the clock agrees with the actual time. If the time displayed on the analog clock is ahead of the actual time, the ESP8266 simply waits until the actual time catches up with the analog clock since it can't move the clock's hands backwards.

The ESP8266 advances the analog clock's second hand by generating bipolar pulses, alternately positive and negative to the clock's Lavet motor coil. Because of differences in clock mechanisms, you may need to increase or decrease the "PULSETIME" constant in the sketch by few milliseconds to make your mechanism step reliably. Experimentally, I found that 30 milliseconds works best for my movement.

The biggest problem with using these cheap analog clocks for a project like this is that the clocks don't provide any type of feedback to indicate the position of the clock's hands. Thus if power is interrupted to the ESP8266 controlling the clock, the ESP8266 "forgets" where the clock's hands are positioned. To get around this problem, the positions of the hour, minute and second hands are stored in a [Microchip 47L04 Serial EERAM](https://www.microchip.com/wwwproducts/en/47L04) (4Kbit SRAM with EEPROM backup) and updated each second as the clock's hands positions change. If power is interrupted, the ESP8266 can retrieve the last position of the clock's hands from the EERAM when power is reapplied.

The very first time that the sketch is run, the user will be directed to a simple web page (see below) served by the ESP8266 which is used to tell it where the analog clock's hands are initially positioned. From that point on, the ESP8266 will use the data stored in the EERAM to "remember" the positions of the clock's hands.

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/screen1.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/screen1.jpg)

Analog Clock Setup Page

  
  

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/screen2.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/screen2.jpg)

Arduino Serial Monitor During Analog Clock Startup

  
  
Once the ESP8266 finishes its initialization and starts operation, it serves a simple web page showing the clock's status. The status page can optionally show a graphic image representing the clock's Face drawn using Scalable Vector Graphics, or HTML Canvas, or no image at all.
  
  

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/screen3.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/screen3.jpg)

Analog Clock Status Page Using Scalable Vector Graphics to Draw the Clock Face

  
  

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/screen4.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/screen4.jpg)

Analog Clock Status Page Using the HTML Canvas Element to Draw the Clock Face

  
  

[![](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/raw/master/images/screen5.jpg)](https://github.com/jim11662418/ESP8266_WiFi_Analog_Clock/blob/master/images/screen5.jpg)

Analog Clock Status Page Displaying Text Only
