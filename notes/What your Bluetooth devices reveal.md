---
title: "What your Bluetooth devices reveal"
url: https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/
clipped: 2026-06-17 01:44:26
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What your Bluetooth devices reveal](https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/)

## Digest Summary
Bluehood is a Python‑based Bluetooth scanner that passively monitors nearby devices to illustrate the privacy risks of constantly enabled Bluetooth. Using a standard Bluetooth adapter (e.g., on a Raspberry Pi or laptop), it logs device appearances, classifies them by vendor and BLE service UUIDs, and generates hourly/daily heatmaps, dwell‑time metrics, and correlation analyses. The tool filters randomized MAC addresses, stores data in SQLite, and offers a web dashboard with optional push notifications via tfy.sh. The author built Bluehood after the disclosure of WhisperPair (CVE‑2025‑36911), a critical vulnerability in Bluetooth audio devices, to assess what information is unintentionally broadcast. Observations include detection of delivery vehicles, neighbor movement patterns, and device co‑occurrence, all without active connections. The project highlights that many devices—hearing aids, medical implants, fleet‑managed vehicles, wearables—cannot disable Bluetooth, creating privacy trade‑offs especially for applications like Briar and BitChat that rely on Bluetooth mesh. Bluehood is distributed on GitHub and can be run via Docker or manual installation, requiring elevated Bluetooth privileges.

## Discussion Summary
The comments express strong concern about the pervasive, always‑on nature of Bluetooth and its use for passive tracking, noting that devices regularly broadcast identifiers that can be correlated to build movement profiles in homes, malls, traffic systems, and public spaces. Contributors highlight the lack of effective MAC randomization, cite real‑world examples of monitoring vehicles and neighbors, and call for stronger privacy safeguards. While some users show technical interest in detecting or auditing broadcasts, the dominant view is that current practices pose significant privacy risks and need tighter controls.

---

## Full Article

Building Bluehood, a Bluetooth scanner that reveals what information we leak just by having Bluetooth enabled on our devices.

If you’ve read much of this blog, you’ll know I have a [thing for privacy](https://blog.dmcc.io/privacy). Whether it’s [running my blog over Tor](https://blog.dmcc.io/journal/tor-relay-onion-location/), [blocking ads network-wide with AdGuard](https://blog.dmcc.io/journal/tailscale-adguard-dns/), or [keeping secrets out of my dotfiles with Proton Pass](https://blog.dmcc.io/journal/proton-pass-cli-linux-secrets/), I tend to think carefully about what data I’m exposing and to whom.

Last weekend I built [Bluehood](https://github.com/dannymcc/bluehood), a Bluetooth scanner that tracks nearby devices and analyses their presence patterns. The project was heavily assisted by AI, but the motivation was entirely human: I wanted to understand what information I was leaking just by having Bluetooth enabled.

The timing felt right. A few days ago, researchers at KU Leuven disclosed [WhisperPair](https://whisperpair.eu/) (CVE-2025-36911), a critical vulnerability affecting hundreds of millions of Bluetooth audio devices. The flaw allows attackers to hijack headphones and earbuds remotely, eavesdrop on conversations, and track locations through Google’s Find Hub network. It’s a stark reminder that Bluetooth isn’t the invisible, harmless signal we treat it as.

The Problem Nobody Talks About
------------------------------

We’ve normalised the idea that Bluetooth is always on. Phones, laptops, smartwatches, headphones, cars, and even medical devices constantly broadcast their presence. The standard response to privacy concerns is usually “nothing to hide, nothing to fear.”

But here’s the thing: even if you have nothing to hide, you’re still giving away information you probably don’t intend to.

From my home office, running Bluehood in passive mode (just listening, never connecting), I could detect:

* When delivery vehicles arrived, and whether it was the same driver each time
* The daily patterns of my neighbours based on their phones and wearables
* Which devices consistently appeared together (someone’s phone and smartwatch, for instance)
* The exact times certain people were home, at work, or elsewhere

None of this required any special equipment. A Raspberry Pi with a Bluetooth adapter would do the job. So would most laptops.

Devices You Can’t Control
-------------------------

What concerns me most isn’t that people choose to have Bluetooth enabled. It’s that many devices don’t give users the option to disable it.

Hearing aids are a good example. Modern hearing aids often use Bluetooth Low Energy so audiologists can connect and adjust settings or run diagnostics. Pacemakers and other implanted medical devices sometimes broadcast BLE signals for the same reason. The user can’t simply turn this off.

Then there are vehicles. Delivery vans, police cars, ambulances, logistics fleets, and trains often have Bluetooth-enabled systems for fleet management, diagnostics, or driver assistance. These broadcast continuously, and the drivers have no control over it.

Even consumer devices aren’t always straightforward. Many smartwatches need Bluetooth to function at all. GPS collars for pets require it to communicate with the owner’s phone. Some fitness equipment won’t work without it.

What’s interesting is that some of the most privacy-focused projects actually require Bluetooth to be enabled.

[Briar](https://briarproject.org/) is a peer-to-peer messaging app designed for activists and journalists operating in hostile environments. It doesn’t rely on central servers, and when the internet goes down, it can sync messages via Bluetooth or Wi-Fi mesh networks. It’s a genuinely useful tool for maintaining communications during internet blackouts or in areas with heavy surveillance.

[BitChat](https://bitchat.free/) takes this even further. It’s a decentralised messaging app that operates entirely over Bluetooth mesh networks—no internet required, no servers, no phone numbers. Each device acts as both client and relay, automatically discovering peers and bouncing messages across multiple hops to extend the network’s reach. The project explicitly targets scenarios like protests, natural disasters, and regions with limited or censored connectivity.

Both are genuinely excellent projects solving real problems. But to use them, you need Bluetooth enabled. And every device with Bluetooth enabled is broadcasting its presence to anyone nearby who cares to listen.

This creates a strange tension. Tools designed to protect privacy often require a feature that compromises privacy in other ways.

People often underestimate what patterns reveal. A bad actor with a Bluetooth scanner doesn’t need to know your name. They just need to observe behaviour over time.

Consider what someone could learn by monitoring Bluetooth signals in a residential area for a few weeks:

* When is the house typically empty?
* Does someone visit every Thursday afternoon?
* Is there a regular pattern that suggests shift work?
* When do the children come home from school?
* Which homes have the same delivery driver, suggesting similar shopping habits?

If there’s damage to your property, you could potentially go back through the logs and see which devices were in range at that time. A smartwatch on a dog-walker passing by. A phone in someone’s pocket. A vehicle with fleet tracking.

These might seem like edge cases, but they illustrate a broader point: we’re constantly leaving digital breadcrumbs we don’t even think about.

What Bluehood Actually Does
---------------------------

Bluehood is a Python application that runs on anything with a Bluetooth adapter. It continuously scans for nearby devices, identifies them by vendor and BLE service UUIDs, and tracks when they appear and disappear.

The key features:

* **Passive scanning**: It only listens. It doesn’t try to connect or interact with any device.
* **Device classification**: Phones, audio devices, wearables, vehicles, IoT devices, and more, identified by BLE fingerprints.
* **Pattern analysis**: Hourly and daily heatmaps, dwell time tracking, and detection of correlated devices.
* **Filtering**: Randomised MAC addresses (used by modern phones for privacy) are detected and hidden from the main view.
* **Web dashboard**: A simple interface for monitoring and analysis.

You can run it in Docker or install it directly. It stores data in SQLite and optionally sends push notifications via [ntfy.sh](https://ntfy.sh) when watched devices arrive or leave.

Running It
----------

The simplest way to try Bluehood is with Docker:

```
git clone https://github.com/dannymcc/bluehood.git
cd bluehood
docker compose up -d
```

The dashboard is available at `http://localhost:8080`.

If you prefer a manual install:

```
sudo pacman -S bluez bluez-utils python-pip  # Arch
sudo apt install bluez python3-pip           # Debian/Ubuntu

pip install -e .
sudo bluehood
```

Bluetooth scanning needs elevated privileges. You can either run as root, grant capabilities to Python, or use the included systemd service for always-on monitoring.

The Point of All This
---------------------

Bluehood isn’t a hacking tool. It’s an educational demonstration of what’s possible with commodity hardware and a bit of patience.

I built it because I wanted to see for myself what I was broadcasting. The results were sobering. Even with no malicious intent, anyone with basic technical knowledge could learn a lot about my household just by sitting in their car and running a script.

This isn’t about paranoia. It’s about understanding the trade-offs we make when we leave wireless radios enabled on our devices. For some use cases, Bluetooth is essential. For others, it’s just convenience. Being aware of what you’re exposing is the first step to making informed decisions about which category your devices fall into.

If you try Bluehood and it makes you think twice about your own Bluetooth habits, it’s done its job.

---

The source code is available on [GitHub](https://github.com/dannymcc/bluehood). Feedback and contributions welcome.