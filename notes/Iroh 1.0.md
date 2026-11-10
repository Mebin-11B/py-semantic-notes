---
title: "Iroh 1.0"
url: https://www.iroh.computer/blog/v1
clipped: 2026-06-17 00:42:38
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Iroh 1.0](https://www.iroh.computer/blog/v1)

## Digest Summary
Iroh 1.0 is a networking library that replaces IP‑based addressing with user‑controlled cryptographic keys, enabling devices to be reachable regardless of location or NAT state. The release stabilizes the wire protocol and language APIs, guaranteeing interoperability between any iroh v1 endpoints. Core technical features include a custom QUIC implementation with multipath routing and hot‑swap capability, QUIC‑based NAT traversal with encrypted connection metadata, and local‑first discovery allowing direct peer connections without internet access. The library compiles to WebAssembly for browser use and supports custom transports such as BLE, LoRa (in development), and Wi‑Fi Aware under the same dial‑by‑key abstraction. After pausing FFI support, iroh now offers stable bindings for Rust, Python, Node.js, Swift, and Kotlin, facilitating integration into iOS and Android apps. Public relays have handled over 200 million endpoint creations in the past month; relays are open‑source, rate‑limited, and updated within 24 hours of each release. Version 0.35 support ends Dec 31 2026; future major releases will modify the wire protocol, while minor updates remain backward compatible.

## Discussion Summary
The comments convey a largely positive impression of Iroh’s ease of embedding secure, QUIC‑based peer‑to‑peer connections and its helpful developer community, with several users reporting successful production deployments and praising its Rust implementation and relays. At the same time, many raise concerns about the project’s positioning versus established tools such as Tailscale, Netbird or libp2p, question the completeness of documentation, pricing model, and lack of features like WebRTC, Go bindings, or built‑in discovery, and seek clarification on key management, anonymity, and offline‑peer support. Overall, enthusiasm is tempered by calls for clearer value articulation and broader ecosystem support.

---

## Full Article

VIDEO

It's a simple idea really, and it's the right abstraction for the future of the internet. IP addresses can break, without warning, and it's outside of your device's control. Keys, however, are created & controlled by you. They stay the same as your device moves, and are yours to throw away, or not. IP addresses can be private and inaccessible behind firewalls, but with iroh your device can be securely addressable no matter where it is.

We think this is how the internet should work, which is why iroh exists, and today we're delighted to announce iroh version 1.0.

This is our first stable release, but the project has grown significantly over the 65 versions that led to 1.0. iroh is already used all over the place. **The public relays we run have seen more than 200 million endpoints created, *in the last 30 days alone.*** Developers are using iroh to stream video, train large language models, talk to agents, secure chats, play games, send files, and many more things than we could jam into this list. Iroh is a fundamental technology aimed at a fundamental shift in the internet, and it's running on millions of devices today.

After more than 4 years of building in the open, we have a foundation we're both proud of.

* We shifted onto open standards, preferring IETF drafts whenever possible
* We built our own implementation of [QUIC multipath](https://datatracker.ietf.org/doc/draft-ietf-quic-multipath/), so iroh can build & manage multiple routes within the same connection, and hot swap paths as conditions change
* We implemented [QUIC NAT traversal](https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/), so we can establish direct connections while keeping connection details encrypted
* We added full local-first configurations so iroh can find & connect to local devices, without internet access
* We built & continually check that iroh can compile to WASM & run in the browser
* We worked with power users to add hooks, so you can inject logic to control how connections should work
* We've even added support for [custom transports](/blog/iroh-0-97-0-custom-transports-and-noq), so you can plug in technologies like [Bluetooth Low-Energy (BLE)](https://github.com/mcginty/iroh-ble-transport/), LoRa (under construction), WiFi Aware, or even [Tor](https://github.com/n0-computer/iroh-tor-transport) to build connections, and all of this fits under the same dial-by-key abstraction

The power of that key can't be overstated. We use it to secure the connection. And because all data that comes from the connection is secured by that key, we can build up from that same key into identity, permissions, and attribution. We can also use that same key as an address we can dial, no matter where it is in the world. It turns the internet into a secure localhost.

Iroh connections are also far more efficient. It's normal to see 95% of data transferred in a connection pass directly between devices. Going direct means fewer hops through the cloud, which lowers your egress bill. It's also fewer hops through routers, which means the internet is more efficient overall.

We previously paused FFI support because of maintenance overhead with API churn and promised to bring it back with a stable 1.0 API. Now we're follwing through on this promise: In addition to the Rust crate, we now officially support Python, Node.js, Swift, and Kotlin. This makes your application use case even easier, making it possible to embed iroh into your swift iOS application or your Kotlin Android app.
Check out the [documentation](https://docs.iroh.computer/languages) and [generated API docs](https://n0-computer.github.io/iroh-ffi/).

Iroh version 1.0 asserts stability for both the wire protocol and language APIs: an iroh v1 endpoint will be able to communicate with another iroh v1 endpoint, regardless of minor version or language.

In the future we may version these two aspects independently, for example: we may release version 2 of a given language API, but keep compatibility over the wire. **Any change that affects the wire stability of iroh will always coincide with a major release.**

Version 1.0 is the first major release of iroh, which we're announcing in conjunction with our support schedule for customers: [Read our support schedule](https://docs.iroh.computer/about/release-policy#support-policy)

In short:

* Major and minor versions after 1.0 are supported on a schedule.
* The 0.35 minor version won't receive further releases. Public relay support for 0.35x continues through Dec 31, 2026, more on that in the section below.
* We do not plan to support canary (0.9x) and release candidates (1.0.0-rcX) after today.

It's important to note there are a significant number of bug fixes and improvements in 1.0, so if you encounter an issue on an earlier release we want you to try updating to the 1.0 to ensure it is still an issue there before opening a bug report.

We maintain a set of public relays, most commonly accessed via the "n0" preset for building an endpoint.

| Release | Final day of public relay operation |
| --- | --- |
| v1.0 | until End of Life |
| v0.35x | Dec 31, 2026 |
| v0.9x & v1.0.0-rcX | Sept 30, 2026 |

We will bump public relays to their latest version shortly after each release, usually within 24 hours. Wire-breaking relay changes will get new URLs so older clients keep working.

As always, relay binaries themselves are open source, and we offer hosted relays through iroh services. Public relays are rate-limited for relayed traffic, which can change at any time.

The internet should be built on dialing keys. On connections that just work. On connections that are secure, and default to being direct. With 1.0 you now have a mature networking stack that you can put into your app with confidence. Now is the time to come build on iroh, and we can't wait to see what you come up with.

Check out the [iroh quickstart guide](https://docs.iroh.computer/quickstart) for application developers.

Join the discussion on [reddit](https://www.reddit.com/r/rust/comments/1u6it5w/iroh_10_dial_keys_not_ips/) | [hackernews](https://news.ycombinator.com/item?id=48542480) | [bluesky](https://bsky.app/profile/iroh.computer/post/3modkbhkxvs26) | [x.com](https://x.com/iroh_n0/status/2066534955421708692)

Iroh is a dial-any-device networking library that just works. Compose from an ecosystem of ready-made protocols to get the features you need, or go fully custom on a clean abstraction over dumb pipes. Iroh is open source, and already running in production on hundreds of thousands of devices.

To get started, take a look at our

[docs](https://iroh.computer/docs)

, dive directly into

[the code](https://github.com/n0-computer/iroh)

, or chat with us in our

[discord channel](https://iroh.computer/discord)

.