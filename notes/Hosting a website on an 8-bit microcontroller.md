---
title: "Hosting a website on an 8-bit microcontroller"
url: https://maurycyz.com/projects/mcusite/
clipped: 2026-06-17 01:01:32
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Hosting a website on an 8-bit microcontroller](https://maurycyz.com/projects/mcusite/)

## Digest Summary
The article describes a proof‑of‑concept web server built on an AVR64DD32 8‑bit microcontroller (similar to an ATmega328). Because 10 BASE‑T Ethernet requires 10 Mbps (20 Mbps on the wire due to Manchester encoding), the AVR’s 12 MHz I/O limit makes direct Ethernet impractical. Instead, the author connects the MCU to a host PC via a simple serial link using SLIP (RFC 1055), which needs only a few milliwatts and a diode for polarity protection. The MCU implements a minimal IP stack: it handles fixed‑size IPv4 headers (40 bytes), swaps source/destination addresses, resets TTL, and omits fragmentation (relying on modern OSes that disable it). A custom TCP layer tracks connection state and retransmits lost packets; it is functional but still contains bugs. HTTP responses are hard‑coded, supporting a single URL. To expose the site publicly, the author routes traffic through a VPS using WireGuard and an HTTP proxy (/mcu path), avoiding the need for a dedicated public IP on the MCU. The setup demonstrates that an 8‑bit MCU can serve static web content over a serial‑based network link, albeit with limited performance and security.

## Discussion Summary
The comment expresses clear enthusiasm for observing HTML load incrementally, noting that the real‑time streaming of page elements feels nostalgic, reminiscent of early dial‑up experiences where images rendered line by line. The tone is positive, highlighting enjoyment of the visual feedback and a fondness for the retro‑style rendering process.

---

## Full Article

*Hosting a website on an 8-bit microcontroller.*
================================================

**2026-05-11** — **2026-05-18** ([Electronics](https://maurycyz.com/tags/electronics/)) ([Programming](https://maurycyz.com/tags/programming/))

In today's episode of "dumb things to do with an AVR microcontroller":

![A small perfboard screwed into a chamfered wooden block. The board contains a small SMD IC (on adapter board), a few pin headers and two LEDs.](https://maurycyz.com/projects/mcusite/webscale.jpg)
  
  
Does your server come with real wood?

[MCU website demo](https://maurycyz.com/mcu/)
(may go down if this gets posted to HN)

My victim is the AVR64DD32 which is quite similar to the Atmega328 of Arduino fame.
Compared to the older Atmega, these AVR DD lines are cheaper for the same memory, use a single programming pin and have nicer peripherals:

|  |  |
| --- | --- |
| CPU: | Single 8-bit AVR core @ 24 MHz (max) |
| RAM: | 8 kB (static RAM) |
| Flash: | 64 kB |
| EEPROM: | 256 bytes |
| Voltage: | 1.8 - 5.5 Volts |
| Cost: | $1 - $2 |

So that's the computer (a rather spacious one at that) but it'll need an internet connection to host a website.

*The obvious choice is Ethernet*, but even the slowest version (10BASE-T) still runs at 10 megabits/second.
Worse, it uses Manchester encoding:
a zero is sent as "10" and a one as "01", so 10 megabits of data is actually 20 megabits at the wire.

This is simply too fast for the AVR to generate.
While it's processor can run at 24 MHz, but all the peripherals and IO pins max out at a 12 MHz clock.
(although some other 8-bit chips should be able to do it)

The proper solution is to buy a dedicated ethernet chip from DigiKey, but then I'd be waiting weeks to finish this project.

... and ethernet is far from the only option:

*Serial Line Internet Protocol* (RFC 1055) is a very old and very simple standard for running networks over serial:

Before sending a packet, wrap it in 0xC0 bytes.
If the packet contains any 0xC0 bytes, replace them with 0xDB 0xDC.
To avoid ambiguity, any pre-existing 0xDB bytes are replaced with 0xDB 0xDD.

This scheme was widely used for connecting to the internet in the olden days:
A dial up modem creates a serial link over a phone line, and it's up the the computer to do anything with it.
(This also means that they are not limited to networking:
those same modems could be connected to a terminal for remote access)

... which is why SLIP is still supported by modern Linux:

```
# Just a normal USB to Serial adapter
stty -F /dev/ttyUSB0 115200 raw cs8
slattach -m -F -L -p slip /dev/ttyUSB0
# ... and now it's a network interface
```

The hardware on the microcontroller's end is trivial:

![](https://maurycyz.com/projects/mcusite/sch.png)
  
  
[www.c](https://maurycyz.com/projects/mcusite/www.c): Source code. [www.elf](https://maurycyz.com/projects/mcusite/www.elf): Prebuilt binary 

It does work with no external components, but I wanted some blinkenlights, and an idiot-proofing diode
for when I inevitably connect the power backwards.

Because it only draws a few milliwatts, it can run the server of the serial adapter's 5 volt rail:
it's really nice to only have one cable to deal with.

*Now it has an internet connection*, but that's hardly a server.

In order for my web page to get to your computer, it needs to pass through dozens of different networks.
To do this, each packet has an IP header:
40 bytes that contain the address of the source and destination computers, and some other stuff I don't really care about.

The protocol used to be a lot more complex, with features like packet fragmentation
that require a lot of memory to handle correctly, but I don't have to:
every modern operating system disables fragmentation and IPv6 removed it entirely.

This makes implementing it very easy:
Just swap around the source and destination of a recieved packet to generate the header for the response.
(and reset the TTL counter)

*The other protocol, TCP is a lot harder*:
Implementing it requires the microcontroller to track connection states,
periodically retransmit lost packets and handle a huge number edge cases.

It took several days to get my custom implementation working well enough, and it's
still got a few bugs.

As for implementing HTTP, I didn't:
The server always sends a hardcoded "response" back to the client.
This works fine as long as there's only a single URL on the site.

[
[Video of the page loading. See web or files directory: loading.mp4]
](/projects/mcusite/loading.mp4)

*Ok great*, but what if I want to share it with friends?
Unfortunately, for their requests to reach it, it needs a publically routable IPv4 address.
Not only are these expensive but it's impossible to get a good internet connection at my place.

(no, Starlink is not good)

I do have a machine with a publically routable address,
but it's at a datacenter near Helsinki:
I'd need a very long serial cable...

another cool thing Linux supports is wireguard, which creates a virtual network link over the internet.
This works even if one of the machines is behind (CG)NAT or other annoyances.

Problem solved:

have the Linux router box connect to the VPS to get a proper internet connection?

... except the MCU still doesn't have it's own IP address:
I could forward everything from my VPS's address to it, but that would break my normal website.

Instead, I setup the server to proxy any requests under `/mcu` to the server using a local address block.
This means that visitors aren't directly connecting to the MCU's TCP/IP stack...
but hey, it's the same setup that the Vape Server uses and no one complained.

(It also makes it slightly harder to break by sending SYN packets, but
it's not exactly hard to DDoS a server connected over what's effectively dial-up)

This whole problem wouldn't exist if we could just get our stuff together:
IPv6 has existed for thirty years but most people still don't have access.

*Related*:
==========