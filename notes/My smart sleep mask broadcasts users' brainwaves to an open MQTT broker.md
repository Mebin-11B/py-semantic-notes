---
title: "My smart sleep mask broadcasts users' brainwaves to an open MQTT broker"
url: https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/
clipped: 2026-06-17 01:45:24
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [My smart sleep mask broadcasts users' brainwaves to an open MQTT broker](https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/)

## Digest Summary
A Kickstarter‑funded smart sleep mask includes EEG, respiration, accelerometer, gyroscope sensors, vibration, heating, audio playback, and periorbital electrical muscle stimulation (EMS). Using Claude, the author reverse‑engineered its Bluetooth Low Energy interface: two channels (commands and data) with a proprietary packet format (header, direction, command type, payload, footer). Decompiling the Flutter Android APK revealed hard‑coded MQTT broker credentials shared by all units. Connecting to the broker exposed live telemetry from ~25 devices, including EEG streams at 250 Hz, air‑quality metrics, and occupancy data. The mask’s EMS can be triggered via the same command set, allowing remote electrical stimulation of any user. The author built a web dashboard to control the mask (sliders for vibration, heating, EMS, audio) and captured EEG samples showing REM‑like mixed frequencies and deep‑sleep delta activity. The security flaw—public credentials and unencrypted MQTT publishing—permits unrestricted access to personal brainwave data and control of the device; the researcher notified the manufacturer but did not name the product.

## Discussion Summary
Comments converge on strong criticism of the sleep‑mask’s security, highlighting the shared MQTT credentials, lack of encryption and the broader “shambolic” state of IoT device protection. Many express skepticism about the plausibility of the advertised EEG, stimulation and battery capabilities, questioning whether such hardware can function as described. There is concern that LLMs lower the barrier to reverse‑engineering, potentially encouraging insecure product launches. Some suggest local‑only integrations as a mitigation, while a few note the need for clearer regulation and naming of the company.

---

## Full Article

My smart sleep mask broadcasts users' brainwaves to an open MQTT broker
=======================================================================

*12 Feb, 2026*

I recently got a smart sleep mask from Kickstarter. I was not expecting to end up with the ability to read strangers' brainwaves and send them electric impulses in their sleep. But here we are.

The mask was from a small Chinese research company, very cool hardware -- EEG brain monitoring, electrical muscle stimulation around the eyes, vibration, heating, audio. The app was still rough around the edges though and the mask kept disconnecting, so I asked Claude to try reverse-engineer the Bluetooth protocol and build me a simple web control panel instead.

### Bluetooth

The first thing Claude did was scan for BLE (Bluetooth Low Energy) devices nearby. It found mine among 35 devices in range, connected, and mapped the interface -- two data channels. One for sending commands, one for streaming data.

Then it tried talking to it. Sent maybe a hundred different command patterns. Modbus frames, JSON, raw bytes, common headers. Unfortunately, the device said nothing back, the protocol was not a standard one.

### The app

So Claude went after the app instead. Grabbed the Android APK, decompiled it with jadx. Turns out the app is built with Flutter, which is a bit of a problem for reverse engineering. Flutter compiles Dart source code into native ARM64 machine code -- you can't just read it back like normal Java Android apps. The actual business logic lives in a 9MB binary blob.

But even compiled binaries have strings in them. Error messages, URLs, debug logs. Claude ran `strings` on the binary and this was the most productive step of the whole session. Among the thousands of lines of Flutter framework noise, it found:

* Hardcoded credentials for the company's message broker (shared by every copy of the app)
* Cloud API endpoints
* All fifteen command builder function names (e.g. to set vibration, heating, electric stimulation, etc.)
* Protocol debug messages that revealed the packet structure -- header, direction byte, command type, payload, footer

We had the shape of the protocol. Still didn't have the actual byte values though.

Claude then used [blutter](https://github.com/worawit/blutter), a tool specifically for decompiling Flutter's compiled Dart snapshots. It reconstructs the functions with readable annotations. Claude figured out the encoding, and just read off every command byte from every function. Fifteen commands, fully mapped.

### It works

Claude sent a six-byte query packet. The device came back with 153 bytes -- model number, firmware version, serial number, all eight sensor channel configurations (EEG at 250Hz, respiration, 3-axis accelerometer, 3-axis gyroscope). Battery at 83%.

Vibration control worked. Heating worked. EMS worked. Music worked. Claude built me a little web dashboard with sliders for everything. I was pretty happy with it.

That could have been the end of the story.

### The server

Remember the hardcoded credentials from earlier? While poking around, Claude tried using them to connect to the company's MQTT broker -- MQTT is a pub/sub messaging system standard in IoT, where devices publish sensor readings and subscribe to commands. It connected fine. Then it started receiving data. Not just from my device -- from *all of them*. About 25 were active:

* Sleep masks publishing live EEG brainwave data
* Air quality monitors reporting temperature, humidity, CO2
* Presence sensors detecting room occupancy

Claude captured a couple minutes of EEG from two active sleep masks. One user seemed to be in REM sleep (mixed-frequency activity). The other was in deep slow-wave sleep (strong delta power below 4Hz). Real brainwaves from real people, somewhere in the world.

![Live EEG](https://hatzistamou.com/img_assets/eeg_live.png)

### EMS

The mask also does EMS -- electrical muscle stimulation around the eyes. Controlling it is just another command: mode, frequency, intensity, duration.

Since every device shares the same credentials and the same broker, if you can read someone's brainwaves you can also send them electric impulses.

### Disclosure

For obvious reasons, I am not naming the product/company here, but have reached out to inform them about the issue.

This whole thing made me revisit Karpathy's [Digital Hygiene](https://karpathy.bearblog.dev/digital-hygiene/) post, and you probably should too.

---

*The reverse engineering -- Bluetooth, APK decompilation, Dart binary analysis, MQTT discovery -- was more or less one-shotted by Claude (Opus 4.6) over a 30' autonomous session.*

Update: this somehow reached #1 on [HN](https://news.ycombinator.com/item?id=47015294) and folks have been asking for the claude conversation transcript. I've added it [here](https://gist.github.com/aimihat/a206289b356cac88e2810654adf06a55).