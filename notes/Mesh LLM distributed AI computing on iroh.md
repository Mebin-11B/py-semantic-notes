---
title: "Mesh LLM: distributed AI computing on iroh"
url: https://www.iroh.computer/blog/mesh-llm
clipped: 2026-08-31 12:22:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Mesh LLM: distributed AI computing on iroh](https://www.iroh.computer/blog/mesh-llm)

## Digest Summary
Mesh LLM is a peer‑to‑peer platform that aggregates GPUs and memory from any number of machines into a single OpenAI‑compatible inference service (localhost:9337/v1). Each node runs an iroh endpoint, identified by a public key, which establishes authenticated QUIC connections (with NAT‑traversal and relay fallback) to other nodes without a central server. Requests are handled in three ways: locally on the node’s GPU, routed to a peer already hosting the model, or split across several nodes in a pipeline (“Skippy”) that partitions a model by layer ranges (e.g., layers 0‑15, 16‑31, …) so modest hardware can run very large models, up to 235 B‑parameter mixture‑of‑experts giants. The system ships with 40+ models, from laptop‑sized to massive, and uses a custom gossip layer to manage mesh membership, version compatibility, and trust. Installation is lightweight (~18 MB), supporting private or public meshes, and a forthcoming mobile app will use iroh’s Swift SDK and the ACP agent standard. Mesh LLM is open source and already deployed on hundreds of thousands of devices.

---

## Full Article

[Blog Index](https://www.iroh.computer/blog)

When people picture running a large language model, they picture a data center. Racks of GPUs that belong to someone else, a metered API, and a bill that grows every month you succeed. You send your prompts off to a black box and hope the price, the model, and the privacy policy all stay the way they were when you signed up.

For a lot of teams that is a bad trade. You give up control over when models change, where your data goes, and what hardware runs your workloads. And as usage grows, so does the bill, with no lever to pull except "pay more."

[Mesh LLM](https://meshllm.cloud) is a different shape. It pools the GPUs and memory you already have, across as many machines as you want to add, and exposes the whole thing as one OpenAI-compatible API. Start one node. Add more later. Let the mesh decide whether a model runs on the box in front of you, routes to a peer, or splits across several machines.

## [The problem: AI is expensive, and it is somebody else's](https://www.iroh.computer/blog/mesh-llm#the-problem-ai-is-expensive-and-it-is-somebody-elses)

The popular models are monoliths. Most people reach them through a UI or an API key and pay a large provider to run everything. That is convenient, and it is also a surrender. You do not control when the model gets updated, what memory it runs in, or what hardware sits underneath.

Plenty of businesses and services that depend on these models want the opposite: more control, more pluggability, lower cost. They have GPUs sitting in offices, in closets, under desks. What they are missing is a way to make those machines act like one.

## [Mesh LLM: run the models yourself](https://www.iroh.computer/blog/mesh-llm#mesh-llm-run-the-models-yourself)

The pitch is simple. Run bigger models without buying bigger GPUs. Share compute privately with your team, or publicly with the world, to power agents and chat. Point any OpenAI client at [http://localhost:9337/v1](http://localhost:9337/v1) and stop caring where the work actually happens.

Under the hood, Mesh LLM distributes model compute across a mesh of iroh endpoints. A request can be served three ways:

- Run it locally, on this machine's GPU.

- Route it to a peer that already has the model loaded.

- Split a model too big for any single box across several machines, as a pipeline.

## [How it works](https://www.iroh.computer/blog/mesh-llm#how-it-works)

The architecture is pluggable. Plugins declare what they provide in a manifest, the runtime starts them, routes calls, and exposes their capabilities over MCP, HTTP, inference, and mesh events. The catalog ships with 40+ models, from half-a-billion-parameter models that fit on a laptop to 235B mixture-of-experts giants.

For the giants, Mesh LLM has a split mode (internally, "Skippy"). A model gets partitioned by layer ranges into stages: layers 0 to 15 on one node, 16 to 31 on the next, and so on down the pipeline. Activations flow from one stage to the next, so several modest machines can run a model none of them could hold alone. The OpenAI client never sees any of this. It still just talks to localhost.

## [How it uses iroh](https://www.iroh.computer/blog/mesh-llm#how-it-uses-iroh)

Every node, whether it serves models or only sends requests, boots an iroh endpoint. That endpoint is the node's identity, a public key, and its only network surface. There is no central server. iroh handles the hole-punching, NAT traversal, and relay fallback needed to open a direct, authenticated QUIC connection between any two nodes, wherever they sit.

To keep that working across the open internet, Mesh LLM runs two iroh relays in different regions, so nodes that cannot reach each other directly always have a fallback path nearby.

The whole protocol rides on QUIC's ALPN negotiation. There are three:
ALPNWhat it carriesmesh-llm/1Main mesh: gossip, routing, HTTP tunnels, plugin channelsmesh-llm-control/1Owner control plane (config sync, ownership attestation)skippy-stage/2Latency-sensitive activation transport for split models

Inside the main  `mesh-llm/1`  connection, everything is a bidirectional QUIC stream tagged with a single leading byte that says what kind of stream it is. One connection carries gossip, inference, route queries, and peer-lifecycle events, all demuxed by that first byte:
ByteStream typeDescription0x01GOSSIPpeer announcements (models, GPU, RTT, capabilities)0x04TUNNEL_HTTPinference requests proxied to a peer0x05ROUTE_REQUEST"which models do you host?"0x06PEER_DOWNdead-peer notification0x07PEER_LEAVINGgraceful shutdown0x08PLUGIN_CHANNELplugin RPC0x0eDIRECT_PATH_REQUESTshare direct addresses for NAT traversal

The neat part is what this buys you. iroh gives authenticated, NAT-traversing QUIC between any two machines, addressed by public key. So "route to a peer" and "stream activations to the next pipeline stage" become the same primitive as "talk to localhost," just with a different endpoint ID. The networking stops being something you have to think about.

iroh provides the secure transport. Mesh LLM builds its own gossip layer on top, so it controls exactly who gets admitted to the mesh, which versions are compatible, and which peers to trust.

## [Getting started](https://www.iroh.computer/blog/mesh-llm#getting-started)

Users can install the lightweight software (about 18 MB) and either join the
public mesh or configure private deployments. The system presents itself as
 `localhost:9337/v1`  to any standard OpenAI client.

A mobile app is coming, built on iroh's Swift SDK. The plan is to speak ACP, the
emerging agent standard, so other clients can join the mesh too. The throughline
is the same one that motivated the whole project: more peer to peer, fewer
closed servers, and no lock-in.

- [See the code](https://github.com/Mesh-LLM/mesh-llm)

- [Mesh LLM Website](https://meshllm.cloud)
Iroh is a dial-any-device networking library that just works. Compose from an ecosystem of ready-made protocols to get the features you need, or go fully custom on a clean abstraction over dumb pipes. Iroh is open source, and already running in production on hundreds of thousands of devices.To get started, take a look at our [docs](https://iroh.computer/docs), dive directly into [the code](https://github.com/n0-computer/iroh), or chat with us in our [discord channel](https://iroh.computer/discord).
