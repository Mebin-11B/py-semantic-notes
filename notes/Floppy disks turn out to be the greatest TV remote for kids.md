---
title: "Floppy disks turn out to be the greatest TV remote for kids"
url: https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/
clipped: 2026-06-17 01:59:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hardware hacking
  - tangible user interfaces
  - microcontrollers
  - wi-fi integration
  - retrocomputing
related:
  - "[[Hardware Hacking]]"
  - "[[Tangible User Interfaces]]"
  - "[[Retrocomputing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The author built a tangible Chromecast remote for kids using floppy disks, an AVR microcontroller, and an ESP8266 Wi-Fi module.
>
> **Key points:**
> - Details a child-friendly remote using floppy disks to select and cast media to a TV.
> - Uses an ATmega controller to read the FAT filesystem from floppy disks via an FDC library.
> - Connects the ATmega to an ESP8266 to transmit commands over Wi-Fi to a server controlling Chromecast.
> - Implements electrical optimizations, including sleep modes and large capacitors, to handle drive power spikes.
> - Encloses the hardware in a laser-cut MDF case and adds precautions to protect the disk read head from wear.
>
> **Concept links:** [[Hardware Hacking]], [[Tangible User Interfaces]], [[Microcontrollers]], [[Wi-Fi Integration]], [[Retrocomputing]]
>
> **Suggested connections:**
> - [[Hardware Hacking]] — repurposing obsolete storage media to control modern IoT devices.
> - [[Tangible User Interfaces]] — designing physical interactions for children to simplify complex digital controls.
<!-- ai-summary:end -->


# [Floppy disks turn out to be the greatest TV remote for kids](https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/)

## Digest Summary
The author built a tangible TV remote for a 3‑year‑old using floppy‑disk hardware to trigger Chromecast playback. A floppy drive is powered by 18650 Li‑ion cells through an XL6009 boost converter; a 1000 µF capacitor stabilizes the ATmega’s supply during the multi‑amp spin‑up surge. Disk insertion is sensed via a custom rolling switch, since standard “disk‑change” pins are unused. An AVR‑based Arduino (ATmega) reads an “autoexec.sh” file from the disk’s FAT filesystem using the Arduino FDC library, then forwards the data via serial to an ESP8266 that handles WiFi communication. Both controllers employ sleep modes: the ATmega wakes on disk insertion, resets the ESP, sends “diskin”/“diskout” messages, reads the file, and powers down the drive; the ESP transmits the command to a netcat‑controlled server which issues Chromecast play/pause actions. The enclosure is laser‑cut MDF, and disks are labeled for selection. The system proved usable by the child, with head‑damage mitigated by moving the read head to an empty track after reading.

## Discussion Summary
Comments show strong enthusiasm for tangible, physical interfaces such as floppy‑disk‑style cards, NFC/RFID tags, and DIY Raspberry Pi setups as ways to simplify media selection for young children and provide parental limits. Many cite existing products like Yoto and share similar hobbyist projects, highlighting the tactile appeal and educational value. At the same time, several participants question the practicality for toddlers, argue that screen exposure at that age is undesirable, and note that complex solutions may be unnecessary compared to simpler parental controls. Overall, the idea is viewed as creative but its usefulness is debated.

---

## Full Article

Posted on

mandag, januar 12, 2026

in

[Hal9k](https://blog.smartere.dk/category/planets/hal9k/), [Planet Ubuntu-DK](https://blog.smartere.dk/category/planets/planet-ubuntu-dk-planets/), [Planets](https://blog.smartere.dk/category/planets/)

Modern TVs are very poorly suited for kids. They require using complicated remotes or mobile phones, and navigating apps that continually try to lure you into watching something else than you intended to. The usual scenario ends up with the kid feeling disempowered and asking an adult to put something on. That something ends up on auto-play because then the adult is free to do other things and the kid ends up stranded powerless and comatose in front of the TV.

[](https://blog.smartere.dk/wp-content/uploads/2026/01/20230908_224249.mp4)

Instead I wanted to build something for my 3-year old son that he could understand and use independently. It should empower him to make his own choices. It should be physical and tangible, i.e. it should be something he could touch and feel. It should also have some illusion that the actual media content was stored physically and not un-understandably in “the cloud”, meaning it should e.g. be destroyable — if you break the media there should be consequences. And there should be no auto-play: interact *once* and get *one* video.

Floppy disks are awesome!
-------------------------

And then I remembered the sound of a floppy disk. The mechanical click as you insert it, the whirr of the disk spinning, and the sound of the read-head moving. Floppy disks are the best storage media ever invented! Why else would the “save-icon” still be a floppy disk? Who hasn’t turned in a paper on a broken floppy disk, with the excuse ready that the floppy must have broken when the teacher asks a few days later? But kids these days have never used nor even seen a floppy disk, and I believe they deserve this experience!

Building on the experience from the [Big Red Fantus-Button](https://blog.smartere.dk/2023/10/fantus-button-part-2-the-physical-button-build-and-the-network-communication/), I already had a framework for controlling a Chromecast, and because of the `netcat | bash` shenanigans it was easily extendable.

My first idea for datastorage was to use the shell of a floppy disk and floppy drive, and put in an RFID tag; this has been done a couple of times on the internet, such as [RFIDisk](https://github.com/ItsDanik/rfidisk) or this [RaspberryPi based RFID reader](https://magazine.raspberrypi.com/articles/rfid-floppy-disk-reader) or this [video covering how to embed an RFID tag in a floppy disk](https://www.youtube.com/watch?v=MsiUxiEBAqs). But getting the floppy disk apart to put in an RFID tag and getting it back together was kinda wonky.

When working on the project in [Hal9k](http://hal9k.dk) someone remarked: “Datastorage? The floppy disk can store data!”, and a quick prototype later this worked really, *really*, well. Formatting the disk and storing a single small file, “autoexec.sh”, means that all the data ends up in track 0 and is read more or less immediately. It also has the benefit that everything can be checked and edited with a USB floppy disk drive; and the major benefit that all the sounds are completely authentic: click, whirrr, brrr brrr.

Autorun for floppy disks is not really a thing.
-----------------------------------------------

The next problem to tackle was how to detect that a disk is inserted. The concept of [AutoRun](https://en.wikipedia.org/wiki/AutoRun) from Windows 95 was a beauty: insert a CD-ROM and it would automatically start whatever was on the media. Great for convenience, quite questionably for security. While *in theory* [floppy disks are supported for AutoRun](https://learn.microsoft.com/da-dk/windows/win32/shell/autoplay-reg?redirectedfrom=MSDN), it turns out that floppy drives basically don’t know if a disk is inserted until the operating system tries to access it! There is a [pin 34 “Disk Change” that is supposed to give this information](https://en.wikipedia.org/wiki/Floppy_disk_drive_interface), but this is basically a lie. None of the drives in my possession had that pin connected to anything, and the internet mostly concurs. In the end I slightly modified the drive and added a simple rolling switch, that would engage when a disk was inserted.

[](https://blog.smartere.dk/wp-content/uploads/2026/01/insert_floppy_mechanism.mp4)

A floppy disk walks into a drive; the microcontroller says “hello!”
-------------------------------------------------------------------

The next challenge was to read the data on a microcontroller. Helpfully, there is the [Arduino FDC Floppy library](https://github.com/dhansel/ArduinoFDC) by dhansel, which I must say is *most* excellent. Overall, this meant that the part of the project that involved reading a file from the floppy disk FAT filesystem was basically the easiest part of all!

![](https://blog.smartere.dk/wp-content/uploads/2026/01/image-1.png)

A combined ATMega + ESP8266 UNO-like board. Not really recommended, but can be made to work.

However, the [Arduino FDC Floppy](https://github.com/dhansel/ArduinoFDC) library is *only* compatible with the AVR-based Arduinos, not the ESP-based ones, because it needs to control the timing very precisely and therefore uses a healthy amount of inline assembler. This meant that I would need one AVR-based Arduino to control the floppy disk, but another ESP-based one to do the WiFi communication. Such combined boards do exist, and I ended up using such a board, but I’m not sure I would recommend it: the usage is really finagly, as you need to set the jumpers differently for programming the ATmega, or programming the ESP, or connecting the two boards serial ports together.

A remote should be battery-powered
----------------------------------

A remote control should be portable, and this means battery-powered. Driving a floppy disk of of lithium batteries was interesting. There is a large spike in current draw when the disk needs to spin up of several amperes, while the power draw afterwards is more modest, a couple of hundred milliamperes. I wanted the batteries to be 18650s, because I have those in abundance. This meant a battery voltage of 3.7V nominally, up to 4.2V for a fully charged battery; 5V is needed to spin the floppy around, so a boost DC-DC converter was needed. I used an off the shelf XL6009 step-up converter board. At this point a lot of head-scratching occurred: that initial spin-up power draw would cause the microcontroller to reset. In the end a 1000uF capacitor at the microcontroller side seemed to help but not eliminate the problem.

![](https://blog.smartere.dk/wp-content/uploads/2026/01/image-1024x768.png)

One crucial finding was that the ground side of the interface cable should absolutely *not* be connected to any grounds on the microcontroller side. I was using a relatively simple logic-level MOSFET, the [IRLZ34N](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irlz34n-datasheet-en.pdf?fileId=5546d462533600a40153567206892720), to turn off the drive by disconnecting the ground side. If any ground is connected, the disk won’t turn off. But also: if any logic pin was being pulled to ground by the ATmega, that would also provide a path to ground. But since the ATmega cannot sink that much current this would lead to spurious resets! Obvious after the fact, but this took quite some headscratching. [Setting all the logic pins to input, and thus high impedance](https://github.com/mchro/FloppyDiskCast/commit/7a59d0754a0b9ad62af22d06c4fe978462e26150), finally fixed the stability issues.

![](https://blog.smartere.dk/wp-content/uploads/2026/01/image-7-1024x585.png)

After fixing the stability, the next challenge was how to make *both* of the microcontrollers sleep. Because the ATmega sleep modes are quite a lot easier to deal with, and because the initial trigger would be the floppy inserting, I decided to make the ATmega in charge overall. Then the ESP has a very simple function: when awoken, read serial in, when a newline is found then send off that complete line via WiFi, and after 30 seconds signal to the ATmega that we’re sleeping, and go back to sleep.

![](https://blog.smartere.dk/wp-content/uploads/2026/01/image-3-1024x677.png)

The overall flow for the ATmega is then:

1. A disk is inserted, this triggers a interrupt on the ATmega that wakes up.
2. The ATmega resets the ESP, waking it from deep sleep.
3. The ATmega sends a “diskin” message over serial to the ESP; the ESP transmits this over WiFi when available.
4. The ATmega turns on the drive itself, and reads the disk contents, and just sends it over serial to the ESP.
5. Spin down the disk, go to sleep.
6. When the disk is ejected, send a “diskout” message over serial, resetting the ESP if needed.
7. Go back to 1.

The box itself is just lasercut from MDF-board. For full details see the [FloppyDiskCast Git repository](https://github.com/mchro/FloppyDiskCast).

Server-side handlers
--------------------

Responding to those commands is still the `netcat | bash` from the [Big Red Fantus-Button](https://blog.smartere.dk/2023/10/fantus-button-part-2-the-physical-button-build-and-the-network-communication/), which was simply extended with a few more commands and capabilities.

![](https://blog.smartere.dk/wp-content/uploads/2026/01/image-9.png)

A few different disks to chose from, with custom printed labels.

`diskin` always sends a “play” command to the Chromecast.  
`diskout` always sends a “pause” command to the Chromecast.  
Other commands like `dad-music` are handled in one of two ways:

Common for both is that they should be idempotent actions, and the `diskin` shortcut will make the media resume without having to wait for the disk contents itself to be read and processed. This means that the “play/pause” disk just contains an empty file to work.

Questionable idea meets real-world 3 year old user
--------------------------------------------------

[](https://blog.smartere.dk/wp-content/uploads/2026/01/20231125_112423.mp4)

The little guy quickly caught on to the idea! Much fun was had just pausing and resuming music and his Fantus TV shows. He explored and prodded, and some disks *were* harmed in the process. One problem that I did solve was that the read head stayed on track 0 after having read everything: this means that when the remote with disk inside it is tumbled around, the disk gets damaged at track 0. To compensate for this, I move the head to track 20 after reading has finished: any damage is then done there, where we don’t store any data. As a bonus it also plays a little more mechanic melody.