---
title: "gRPC: From service definition to wire format"
url: https://kreya.app/blog/grpc-deep-dive/
clipped: 2026-06-17 01:45:59
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [gRPC: From service definition to wire format](https://kreya.app/blog/grpc-deep-dive/)

## Digest Summary
The article explains the full gRPC stack, from service contracts to the wire format. A .proto file defines messages and RPC methods; protoc generates client stubs and server code for many languages, ensuring a contract‑first API. gRPC supports four streaming models—unary, server‑streaming, client‑streaming, and bidirectional—plus metadata (key‑value headers, with binary values ending in “‑bin”) for authentication, tracing, etc. Transport relies on HTTP/2: each RPC maps to a single HTTP/2 stream, allowing multiplexed calls over one TCP connection. URLs follow the pattern `/{package}.{service}/{method}`. Calls consist of HEADERS frames (metadata), DATA frames (length‑prefixed messages), and trailing HEADERS frames (status). Each message is wrapped in a 5‑byte header (1‑byte compression flag, 4‑byte length) followed by the protobuf payload. Application status is conveyed in trailers (`grpc-status`, `grpc-message`), while richer errors use `google.rpc.Status` serialized into `grpc-status-details-bin`. Optional per‑message compression is negotiated via `grpc-accept-encoding` and `grpc-encoding` headers. gRPC can run over alternative transports such as Unix domain sockets or named pipes, and gRPC‑Web adapts the protocol for browsers by embedding trailers in the body.

## Discussion Summary
The comments convey a mixed view of gRPC and protobuf: users appreciate the contract‑first model and the simplicity of defining messages, yet many encounter unnecessary complexity, undocumented configurations, and rough edges that feel burdensome for small services. Issues highlighted include over‑engineered dependencies, vague or overly specific error types, difficulty with health checks, and challenges when teams diverge from a centralized .proto repository. Some suggest language‑specific experiences vary, and a proposed improvement is exposing .proto files during the initial handshake to ease integration.

---

## Full Article

In our previous posts ([part 1](https://kreya.app/blog/protocolbuffers-wire-format/) and [part 2](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)), we demystified Protocol Buffers and learned how data is encoded into compact binary.

But Protobuf is just the payload. To send this data between microservices, we need a transport protocol. Enter **gRPC**.

While many developers use gRPC daily, few look under the hood to see how it actually works. In this post, we’ll go beyond the basics and explore the full gRPC protocol stack: from the high-level service architecture and streaming models down to the low-level HTTP/2 framing and byte-level wire format.

The contract-first philosophy[​](https://kreya.app/blog/grpc-deep-dive/#the-contract-first-philosophy "Direct link to The contract-first philosophy")
-----------------------------------------------------------------------------------------------------------------------------------------------------

At the heart of gRPC lies the contract-first approach. Unlike REST, where API documentation (like OpenAPI) is often an afterthought, gRPC enforces the structure upfront using Protocol Buffers (`.proto` files).

This contract defines not just the data structures (Messages), but the service capabilities (RPCs):

```
package fruit.v1;  
  
service FruitService {  
      
    rpc GetFruit(GetFruitRequest) returns (Fruit);  
  
      
    rpc ListFruits(ListFruitsRequest) returns (stream Fruit);  
  
      
    rpc Upload(stream Fruit) returns (UploadSummary);  
  
      
    rpc Chat(stream ChatMessage) returns (stream ChatMessage);  
}
```

This definition is the source of truth.
From this single file, the protobuf compiler (`protoc`) generates client stubs and server boilerplate in almost any language (Go, Java, C#, Python, etc.),
ensuring that the client and server always agree on the API shape.

Streaming models[​](https://kreya.app/blog/grpc-deep-dive/#streaming-models "Direct link to Streaming models")
--------------------------------------------------------------------------------------------------------------

One of the biggest differentiators of gRPC is its native support for streaming.
This isn't just "chunked transfer encoding", it's first-class API semantics.

* **Unary**: Looks like a standard function call or REST request. The client sends one message, the server sends one back.
* **Server streaming**: Perfect for subscriptions or large datasets. The client sends a query, and the server returns multiple results over time.
* **Client streaming**: Useful for sending a stream of data (like telemetry from an IoT device) where the server processes messages as they arrive.
* **Bidirectional streaming**: True real-time communication. Both sides can send messages independently. This is often used for chat apps or multiplayer games.

In addition to the actual data, gRPC allows sending metadata.
Metadata is a list of key-value pairs (like HTTP headers) that provide information about the call.
Keys are strings, and values are typically strings, but can also be binary data.
The key names are case-insensitive and must not start with `grpc-` (reserved for gRPC internals).
The keys of binary values must end with `-bin`.

Metadata is essential for cross-cutting concerns that shouldn't be part of the business logic payload:

* **Authentication**: Usage of Bearer tokens (e.g., `Authorization: Bearer <token>`).
* **Tracing**: Passing trace IDs (e.g., `transport-id: 12345`) to track requests across microservices.
* **Infrastructure**: Hints for load balancers or proxies.

Metadata can be sent by both the client (at the start of the call) and the server (at the start as headers, or at the end as trailers).

Under the hood: the transport layer[​](https://kreya.app/blog/grpc-deep-dive/#under-the-hood-the-transport-layer "Direct link to Under the hood: the transport layer")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

So how does this contract map to the network? gRPC is built on top of HTTP/2,
leveraging its advanced features to make these streaming models possible.

The most important concept is streams.
Every gRPC call, whether it's a simple unary request or a long-lived bidirectional stream,
is mapped to a single HTTP/2 stream.
This allows multiplexing: you can have thousands of active gRPC calls on a single TCP connection,
with their frames interleaved.
This prevents opening thousands of connections that would be needed with HTTP/1.1.
While it solves the HTTP/1.1 "head-of-line blocking" issue,
TCP-level blocking remains a concern if packets are lost.

### Constructing the URL[​](https://kreya.app/blog/grpc-deep-dive/#constructing-the-url "Direct link to Constructing the URL")

Before we send any bytes, we need to address the resource. In gRPC, the URL is generated automatically from the `.proto` definition: `/{Package}.{Service}/{Method}`.

For `GetFruit`, the path becomes:
`/fruit.v1.FruitService/GetFruit`

This standardization means clients and servers never argue about URL paths.

### The HTTP/2 frames[​](https://kreya.app/blog/grpc-deep-dive/#the-http2-frames "Direct link to The HTTP/2 frames")

A gRPC call typically consists of three stages, each mapping to HTTP/2 frames:

1. **Request headers and metadata** (`HEADERS` frame): contains metadata like `:path`, `:method` (`POST`), and `content-type` (`application/grpc`).
2. **Data messages** (`DATA` frames): the actual application data.
3. **Response trailers** (`HEADERS` frame): the final status of the call.

Since gRPC is built on HTTP/2, metadata is simply mapped to HTTP/2 headers.
String values are sent as-is (e.g. `user-agent: grpc-kreya/1.18.0`).

Binary values are base64-encoded and the key must end with `-bin`.
Libraries usually handle this encoding/decoding transparently.

### The length-prefixed message[​](https://kreya.app/blog/grpc-deep-dive/#the-length-prefixed-message "Direct link to The length-prefixed message")

Inside the HTTP/2 `DATA` frame, gRPC wraps your protobuf message with a mechanism called length-prefixed framing.
Even in a streaming call, every single message is independent and prefixed with a 5-byte header:

| Byte | Purpose | Description |
| --- | --- | --- |
| 0 | Compression Flag | 0 = Uncompressed 1 = Compressed |
| 1-4 | Message Length | 4-byte big-endian integer indicating the size of the payload |

#### Visualizing the bytes[​](https://kreya.app/blog/grpc-deep-dive/#visualizing-the-bytes "Direct link to Visualizing the bytes")

Let's reuse the fruit message from our [previous post](https://kreya.app/blog/protocolbuffers-wire-format/)

which encodes to 10 bytes of protobuf data: `08 96 01 12 05 41 70 70 6c 65`.

When sending this over gRPC, we prepend the header:

* **Compression**: `0` (no compression)
* **Length**: `10` (`0x0A`)

The final 15-byte gRPC message looks like this:

```
00 00 00 00 0a 08 96 01 12 05 41 70 70 6c 65│  │           └─ The protobuf payload (10 bytes)│  └───────────── Payload message length (0xA = 10 bytes)└──────────────── Compression flag (0 = false)
```

This simple framing allows the receiver to read exactly the right number of bytes for the next message, decode it, and repeat, enabling fluid streaming.

### Status and trailers[​](https://kreya.app/blog/grpc-deep-dive/#status-and-trailers "Direct link to Status and trailers")

In REST, you check the HTTP status code (200, 404, 500).
In gRPC, the HTTP status is almost always `200 OK`, even if the logic failed!

The actual application status is sent in the trailers (the very last HTTP/2 header frame).
This separation is crucial: it allows a server to successfully stream 100 items and then report an error on the 101st processing step.

A typical trailer block looks like this:

```
grpc-status: 0  
grpc-message: OK
```

(Status `0` is OK. Non-zero values represent errors like `NOT_FOUND`, `UNAVAILABLE`, etc.)

### Rich errors[​](https://kreya.app/blog/grpc-deep-dive/#rich-errors "Direct link to Rich errors")

Sometimes, a simple status code and a string message aren't enough.
You might want to return validation errors for specific fields or other error details.
The rich error model (specifically `google.rpc.Status`) solves this.

Instead of just `grpc-status` and `grpc-message`,
the server returns a detailed protobuf message serialized as base64 into the `grpc-status-details-bin` trailer.
This standard message contains:

1. **Code**: The gRPC status code.
2. **Message**: The developer-facing error message.
3. **Details**: A list of `google.protobuf.Any` messages containing arbitrary error details (e.g., `BadRequest`, `PreconditionFailure`, `DebugInfo`).

```
message Status {  
    
  int32 code = 1;  
  
    
  string message = 2;  
  
    
  repeated google.protobuf.Any details = 3;  
}
```

Clients can decode this trailer to get structured, actionable error information.

### Compression[​](https://kreya.app/blog/grpc-deep-dive/#compression "Direct link to Compression")

Depending on the environment, bandwidth can be precious,
especially on mobile networks.
gRPC has built-in support for compression to reduce the payload size.

#### How it works[​](https://kreya.app/blog/grpc-deep-dive/#how-it-works "Direct link to How it works")

1. **Negotiation**: The client sends a `grpc-accept-encoding` header (e.g., `br, gzip, identity`) to tell the server which algorithms it supports.
2. **Encoding**: If the server decides to compress the response, it sets the `grpc-encoding` header (e.g., `br`).
3. **Flagging**: For each message, the **compression flag** (byte 0 of the 5-byte header) is set to `1`.
4. **Payload**: The message payload is compressed using the selected algorithm.

Let's look at how the wire format changes when compression is enabled.
Note that compressing our tiny "Apple" message with brotli results in a larger size due to overhead,
but the structure remains the same:

```
01 00 00 00 0e 8f 04 80 08 96 01 12 05 41 70 70 6c 65 03│  │           └─ The compressed payload│  └───────────── Length of compressed message (0xE = 14 bytes)└──────────────── Compression flag (1 = true)
```

This happens per-message.
It is even possible to have different compression settings for the request and the response (asymmetric compression).

Alternative transports[​](https://kreya.app/blog/grpc-deep-dive/#alternative-transports "Direct link to Alternative transports")
--------------------------------------------------------------------------------------------------------------------------------

While gRPC usually runs over TCP/IP with HTTP/2, the protocol is agnostic enough to run elsewhere.

* **Unix Domain Sockets**: Perfect for local IPC. It bypasses the TCP network stack for maximum efficiency.
* **Named Pipes**: The equivalent on Windows.

This flexibility allows gRPC to be the universal glue between components,
whether they are on different continents or on the same chip.

The browser gap (gRPC-Web)[​](https://kreya.app/blog/grpc-deep-dive/#the-browser-gap-grpc-web "Direct link to The browser gap (gRPC-Web)")
------------------------------------------------------------------------------------------------------------------------------------------

There is one place gRPC struggles: **the Browser**.
Web browsers do not expose the low-level HTTP/2 framing controls required for gRPC (specifically, reading trailers and granular stream control).

This challenge is addressed by gRPC-Web, a protocol adaptation that:

1. Encodes trailers inside the data stream body (so the browser doesn't need to read HTTP trailers).
2. Supports text-based application-layer encoding (base64) to bypass binary constraints.

We will cover more on how exactly gRPC-Web works in a future post.

Closing[​](https://kreya.app/blog/grpc-deep-dive/#closing "Direct link to Closing")
-----------------------------------------------------------------------------------

gRPC is more than just a serialization format, it's a complete ecosystem that standardizes how we define, generate, and consume APIs.
By understanding the layers, from the `.proto` contract to the 5-byte header on the wire,
you can debug issues more effectively and design better systems.

Tools like [Kreya](https://kreya.app) abstract this complexity away for daily testing,
but knowing what happens under the hood puts you in control when things get tricky.

Further Reading[​](https://kreya.app/blog/grpc-deep-dive/#further-reading "Direct link to Further Reading")
-----------------------------------------------------------------------------------------------------------