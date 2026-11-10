---
title: "Mesh over Bluetooth LE, TCP, or Reticulum"
url: https://github.com/torlando-tech/columba
clipped: 2026-06-17 01:34:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - mesh networks
  - decentralized communication
  - offline networking
  - cryptography
  - android development
related:
  - "[[Mesh Networks]]"
  - "[[Decentralized Communication]]"
  - "[[Offline Networking]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Columba is a native Android messaging client running on the Reticulum mesh-networking stack, enabling secure offline communications.
>
> **Key points:**
> - Trades messages (LXMF) and calls (LXST) offline using Bluetooth LE, Wi-Fi, TCP, and LoRa.
> - Manages cryptographic identities locally, offering end-to-end encryption without central servers.
> - Integrates Material Design 3 and offline vector/raster maps for secure location sharing.
> - Runs over Reticulum, a networking stack designed to tolerate low bandwidth and high latency.
>
> **Concept links:** [[Mesh Networks]], [[Decentralized Communication]], [[Offline Networking]], [[Cryptography]], [[Android Development]]
>
> **Suggested connections:**
> - [[Mesh Networks]] — utilizing multi-hop ad-hoc topologies to route messages without internet access.
> - [[Decentralized Communication]] — establishing peer-to-peer relationships using local public-key cryptography.
<!-- ai-summary:end -->


# [Mesh over Bluetooth LE, TCP, or Reticulum](https://github.com/torlando-tech/columba)

## Digest Summary
Columba is a native Android messaging and voice application built for the Reticulum mesh‑network stack. It exchanges LXMF (Lightweight Extensible Message Format) messages and LXST voice calls without relying on internet, cellular, or central servers. Connectivity options include Bluetooth LE, Wi‑Fi, TCP to any Reticulum server, and LoRa via RNode, enabling communication from local proximity to global ranges. Security is provided by end‑to‑end encryption; users generate and manage cryptographic identities locally, with support for multiple identities, QR‑code sharing, and export/import of keys (including compatibility with other Reticulum clients). The app incorporates Material Design 3, custom colour themes, and offline map support (vector/raster MBTiles) with secure location sharing. Distribution is via the GitHub releases page and optional NomadNet download; APK verification details are in SECURITY.md. Reticulum itself is a low‑bandwidth, high‑latency‑tolerant networking stack capable of operating over diverse media.

## Discussion Summary
The comments express optimism about emerging offline‑communication projects while noting that current solutions remain insufficient, prompting multiple new efforts. There is a hopeful expectation that a satisfactory option will appear soon. Technical concerns are highlighted, specifically LoRa’s limited bandwidth restricting message size to very short texts. Additionally, there is curiosity about how alternative platforms such as Reticulum compare to existing mesh‑network implementations like Meshtastic or Meshcore, indicating a desire for performance comparisons.

---

## Full Article

[![alt text](https://github.com/torlando-tech/columba/raw/main/columba-icon.svg)](https://github.com/torlando-tech/columba/blob/main/columba-icon.svg)

Columba is a simple messaging and voice app for the [Reticulum](https://github.com/markqvist/Reticulum) network on Android. Send [LXMF](https://github.com/markqvist/LXMF) messages and make [LXST](https://github.com/markqvist/LXST/tree/master/LXST) voice calls without relying on the internet, cell towers, or any central servers.

Built with a native Android interface and Material Design 3, Columba brings mesh networking to your pocket in a familiar, easy-to-use package.

[![](https://private-user-images.githubusercontent.com/239676438/520570612-77532689-3568-4224-a75d-62fb08a4ad33.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTcwNjEyLTc3NTMyNjg5LTM1NjgtNDIyNC1hNzVkLTYyZmIwOGE0YWQzMy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iYWFiYjQ1ZjYyYjA1MGYwNmNjMmQ1MDFkN2M2YWY3ZTIyMmVlYTRlY2RiNzVlNDNjMjExMWUyMDExYTMwYmUwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.xnr-EHTXh8xkSEq32dR4WrKrC3v6vAc5TODONkB-7r0)](https://private-user-images.githubusercontent.com/239676438/520570612-77532689-3568-4224-a75d-62fb08a4ad33.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTcwNjEyLTc3NTMyNjg5LTM1NjgtNDIyNC1hNzVkLTYyZmIwOGE0YWQzMy5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iYWFiYjQ1ZjYyYjA1MGYwNmNjMmQ1MDFkN2M2YWY3ZTIyMmVlYTRlY2RiNzVlNDNjMjExMWUyMDExYTMwYmUwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.xnr-EHTXh8xkSEq32dR4WrKrC3v6vAc5TODONkB-7r0) [![](https://private-user-images.githubusercontent.com/239676438/520570645-70804d27-6307-441f-b29f-b32ecfe72098.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTcwNjQ1LTcwODA0ZDI3LTYzMDctNDQxZi1iMjlmLWIzMmVjZmU3MjA5OC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNzBlMWE3NTg3NjhlNTgxNjkzYTI2ODg3YjAyY2U3NTcwODRmNzJlNjM1MjhiNWRiNDg5NDAzNDkzZjRiNjA3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0._0MTM8x4my3K6-KdS9iv5cZE9zWX5KcHkWMNsiktaFs)](https://private-user-images.githubusercontent.com/239676438/520570645-70804d27-6307-441f-b29f-b32ecfe72098.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTcwNjQ1LTcwODA0ZDI3LTYzMDctNDQxZi1iMjlmLWIzMmVjZmU3MjA5OC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lNzBlMWE3NTg3NjhlNTgxNjkzYTI2ODg3YjAyY2U3NTcwODRmNzJlNjM1MjhiNWRiNDg5NDAzNDkzZjRiNjA3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0._0MTM8x4my3K6-KdS9iv5cZE9zWX5KcHkWMNsiktaFs) [![](https://private-user-images.githubusercontent.com/239676438/520573977-c2d2c9ad-63da-42e0-a045-bc30ec3bb128.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTczOTc3LWMyZDJjOWFkLTYzZGEtNDJlMC1hMDQ1LWJjMzBlYzNiYjEyOC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NWE0NDVjZGVkNjEyOTk1NDE0YjExODQzNWU4MDBiN2NhMjk0ZjA3ZWQ1ODM2NzI4MGRiOGRjMmZkOGFiNDI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.uRl0nqbDkmCFr24jzCougf2hwK9KqHlwwIqnZo_1Fog)](https://private-user-images.githubusercontent.com/239676438/520573977-c2d2c9ad-63da-42e0-a045-bc30ec3bb128.jpg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODE2NDA1NzUsIm5iZiI6MTc4MTY0MDI3NSwicGF0aCI6Ii8yMzk2NzY0MzgvNTIwNTczOTc3LWMyZDJjOWFkLTYzZGEtNDJlMC1hMDQ1LWJjMzBlYzNiYjEyOC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYxNlQyMDA0MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NWE0NDVjZGVkNjEyOTk1NDE0YjExODQzNWU4MDBiN2NhMjk0ZjA3ZWQ1ODM2NzI4MGRiOGRjMmZkOGFiNDI1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.uRl0nqbDkmCFr24jzCougf2hwK9KqHlwwIqnZo_1Fog)

* **Message without infrastructure** - Send messages even when the internet is down or unavailable
* **Connect multiple ways** - Use Bluetooth LE to connect to those around you anywhere, Wifi for those at home, LoRa radio via [RNode](https://github.com/markqvist/RNode_Firmware) for those at a distance, or use TCP to connect to any Reticulum server around the world
* **Stay private** - End-to-end encryption with no accounts, no tracking, and no central servers
* **Share location** - Share your location securely with others, viewable from a dedicated map
* **Download maps for offline use** - Download or import map files. Supports vector and raster, in MBTiles format
* **Browse NomadNetwork** - Access nomadnet pages over Reticulum networks
* **Build your network** - Help relay traffic for others and expand the mesh
* **Keep your identity** - Generate your messaging identity right on your device
* **Manage multiple identities** - Easily swap between multiple identities
* **Export and import identities** - Keep an external backup of your keys, or migrate to a new device. Import from other Reticulum clients like [Sideband](https://github.com/markqvist/Sideband)
* **Share your identity via QR Code** - Built in QR code scanner and generator for sharing your identity with others
* **Custom Color Themes** - Don't like the default colors? Rice to your heart's content!

Download the latest release from [Releases](https://github.com/torlando-tech/columba/releases) and install on your Android device. See [SECURITY.md](https://github.com/torlando-tech/columba/blob/main/SECURITY.md) for APK verification instructions.

[![Get it on Obtainium](https://raw.githubusercontent.com/ImranR98/Obtainium/main/assets/graphics/badge_obtainium.png)](https://apps.obtainium.imranr.dev/redirect.html?r=obtainium://add/https://github.com/torlando-tech/columba)

Alternatively, you can download the apk via [NomadNet](https://github.com/markqvist/NomadNet) at `8d1788fdb4e9f85303cfdf7481e721c7:/page/index.mu`

[Reticulum](https://github.com/markqvist/Reticulum) is a networking stack that lets devices communicate directly with each other, forming resilient mesh networks. It is optimized for low bandwidth, high latency connections, and can communicate over nearly any medium. Columba uses [LXMF](https://github.com/markqvist/LXMF) (Lightweight Extensible Message Format) to send messages across the Reticulum network, and uses a native Android implementation of [ble-reticulum](https://github.com/torlando-tech/ble-reticulum) to enable messaging over BLE with other Android and Linux devices.

Want to learn more? Visit [Reticulum's documentation](https://reticulum.network/).

Columba, latin for "dove," is a [constellation](https://en.wikipedia.org/wiki/Columba_(constellation)) in the southern sky depicting a dove. Doves are commonly a symbol of peace and hope, and have been used as messengers throughout history.