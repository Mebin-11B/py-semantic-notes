---
title: "We X-Rayed a Suspicious FTDI USB Cable"
url: https://eclypsium.com/blog/xray-counterfeit-usb-cable/
clipped: 2026-06-17 01:53:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hardware security
  - counterfeit hardware
  - x-ray analysis
  - printed circuit board (pcb)
related:
  - "[[Hardware Security]]"
  - "[[Counterfeit Hardware]]"
  - "[[Supply Chain Security]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Eclypsium uses industrial X-ray analysis to contrast a counterfeit FTDI USB-to-UART cable with an authentic one, identifying critical hardware bypasses.
>
> **Key points:**
> - A suspicious FTDI cable exhibiting high-speed transfer errors was analyzed using an industrial X-ray system.
> - Comparison with an authentic DigiKey cable revealed missing ground planes, poor decoupling placement, and omitted isolation passives.
> - Counterfeit cables often omit safety and integrity components to cut costs, exposing systems to electromagnetic noise or hardware failure.
>
> **Concept links:** [[Hardware Security]], [[Counterfeit Hardware]], [[X-Ray Analysis]], [[Printed Circuit Board (PCB)]]
>
> **Suggested connections:**
> - [[Supply Chain Security]] — hardware-level auditing of electronic components.
> - [[Hardware Debugging]] — using non-destructive imaging to diagnose hardware failures.
<!-- ai-summary:end -->

# [We X-Rayed a Suspicious FTDI USB Cable](https://eclypsium.com/blog/xray-counterfeit-usb-cable/)

## Digest Summary
Eclypsium used an industrial X‑ray system to compare a suspect FTDI USB‑to‑UART cable with a verified authentic cable purchased from DigiKey. The suspect cable exhibited functional failures at higher transfer speeds, prompting analysis. X‑ray inspection revealed several construction differences: the authentic cable showed copper ground pours, ground stapling, decoupling components placed close to the FTDI IC, additional isolation passives on the USB data lines, a thermal pad under the IC, engineered strain‑relief, more solder on the USB‑A connector tabs, a smaller silicon process, and better passive alignment. The questionable cable lacked these features. The study highlights that visual and X‑ray cues can indicate counterfeit hardware, but detection is non‑trivial. Eclypsium stresses that counterfeit components pose broader supply‑chain risks, especially when they involve network gear or servers that may contain hidden backdoors, and urges organizations to prioritize hardware‑level supply‑chain security.

## Discussion Summary
The comments convey cautious concern about the security risks posed by integrated chips in modern communication cables, especially regarding counterfeit and potentially malicious hardware. While the promotional nature of the story is noted, interest remains in its relevance and technical details. Several contributors discuss personal experimentation with supply‑chain attacks to illustrate hardware‑root‑of‑trust vulnerabilities, and there is consensus that such hidden implants are alarming. A common suggestion is that greater transparency or regulation, such as exposing internal chips, could mitigate these threats.

---

## Full Article

We recently got an industrial X-Ray machine in the Eclypsium office to use to ~~make the next Doctor Manhattan~~ do serious cybersecurity research. In between X-raying yet-to-be released industrial IT technologies on behalf of giant companies whose names we cannot reveal, we have done some other fun experiments.

![Eclypsium researcher preparing to x-ray a suspicious USB cable.](https://eclypsium.com/blog/xray-counterfeit-usb-cable/)![Eclypsium researcher preparing to x-ray a suspicious USB cable.](https://eclypsium.com/wp-content/uploads/xray-machine-1.png)

One thing we’ve done with it so far was to x-ray some FTDI USB to UART cables. We had an old cable lying around that seemed a little suspicious and dysfunctional. It worked at slow speeds but it failed when transferring firmware images from a product. These failures drove us to purchase the known good cables from DigiKey, which worked as expected. It is possible that this older cable came from a factory which also produced older generations of authentic FTDI cables, but this particular chip didn’t meet the performance requirements for the FTDI brand. Or maybe it was just a production run based on stolen FTDI IP. Or it is actually completely unrelated to any FTDI IC but has been programmed to claim to be FTDI in software. Unless we could match the silicon exactly to a known supply chain, we can really only speculate.

In either case, we wanted to see the difference between the suspicious cable and a newer, more obviously “legit” one that cost about $20 from [DigiKey](https://www.digikey.com/en/products/detail/ftdi-future-technology-devices-international-ltd/TTL-234X-3V3/6823715). It is not a stretch to assume that a suspicious looking cable is a counterfeit. [FTDI has publicly announced issues with counterfeit devices](https://ftdichip.com/anti-counterfeit-products/). They have even fought back with [drivers which brick counterfeit chips](https://hackaday.com/2014/10/22/watch-that-windows-update-ftdi-drivers-are-killing-fake-chips/). Some people have even referred to this as vendor sanctioned malware.

Here’s what the two cables look like to the naked eye:

Take a look at the two x-ray images below and see if you can tell which one is suspicious, and which one is authentic. Then scroll down and we’ll tell you what we see.

![Xray of an authentic USB cable.](https://eclypsium.com/blog/xray-counterfeit-usb-cable/)![Xray of an authentic USB cable.](https://eclypsium.com/wp-content/uploads/usb-cable-xray-1.png)
![](https://eclypsium.com/blog/xray-counterfeit-usb-cable/)![](https://eclypsium.com/wp-content/uploads/usb-cable-xray-2.png)

Before we tell you the answer, here are some clues to look out for in each picture. The authentic cable has the following features visible in the X-Ray image, not shared with the suspicious cable:

1. Ground pours (reduces impedance and ground loops while improving EMI resistance and thermal dissipation). While there is some [debate about the actual value of copper ground pours](https://resources.altium.com/p/shaky-ground-arguments-against-copper-pours), they are still used by reputable manufacturers.
2. Ground stapling
3. Decoupling passives nearer to the main integrated circuit (IC)
4. More isolation passives for USB data pins
5. Thermal pad under IC
6. Engineered strain relief for wire connections
7. More solder for mechanical tabs on USB A connector
8. Smaller/newer silicon process
9. Better passive alignment

**The Big Reveal, and the Implications for Supply Chain Security**
------------------------------------------------------------------

OK, the top image above is the authentic cable. The bottom image is the more questionable one.

Did you get it right? If not, go back and see if you can pinpoint the various clues.

The point is that, even when you know what to look for, spotting a counterfeit isn’t necessarily easy. The consequences for a consumer buying a shady USB cable likely aren’t too bad. But what happens when an enterprise gets counterfeit network gear with a backdoor pre-installed? Or when a major bank receives grey market servers with another company’s data on them? Eclypsium has helped major worldwide organizations discover exactly these types of supply chain issues.

Supply chain risk is growing rapidly. As AI data center projects capture more and more of the global supply for chips, memory, storage, and other key resources, the secondary market for all of these is heating up. The speed and complexity of these supply chains leaves gaps that cyber adversaries can exploit to introduce vulnerable components and backdoors into tech that makes its way into critical infrastructure.

To learn more, grab our white paper on [Why Supply Chain Security Demands Focus on Hardware](https://eclypsium.com/why-supply-chain-security-demands-focus-on-hardware/)