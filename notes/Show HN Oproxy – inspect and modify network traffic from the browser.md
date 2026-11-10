---
title: "Show HN: Oproxy – inspect and modify network traffic from the browser"
url: https://github.com/sauravrao637/oproxy
clipped: 2026-06-17 00:51:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Oproxy – inspect and modify network traffic from the browser](https://github.com/sauravrao637/oproxy)

## Digest Summary
oproxy is an open‑source MITM proxy that runs locally (or in Docker) and supports HTTP, HTTPS, and SOCKS5 traffic. It captures requests and responses, displaying headers, bodies, status, timing, tags, notes, and inspector data for JWT, GraphQL, gRPC, and WebSocket frames. Captured sessions can be replayed, exported as HAR, cURL, Fetch, or Python snippets, and imported back. Traffic can be modified via rule sets, map‑remote/local, access controls, throttling, breakpoints, mock responses, DNS overrides, capture filters, Lua scripts, or upstream proxy chaining. An authenticated Assistant interface allows OpenAI‑compatible chat models to inspect state and apply confirmed changes. The service runs as a forward HTTP proxy (default port 8080), optionally provides SOCKS5 and additional TLS listeners, and serves a management UI and API on the same endpoint. Persistent volumes store CA certificates and session data. Build requirements are Rust ≥ 1.85, Node.js ≥ 22, and Yarn via Corepack; Docker images are also provided. The MIT‑licensed tool is intended for developers testing browsers, CLIs, mobile apps, APIs, and automated test suites.

## Discussion Summary
The comment expresses inquisitive interest, asking how the tool measures up against mitmproxy and inviting hands‑on testing. It requests user feedback on the experimental assistant, indicating a willingness to gather practical impressions and evaluate its usability. The tone is open‑minded and exploratory, seeking comparative insight and real‑world experience to inform further development.

---

## Full Article

oproxy is a local HTTP, HTTPS, and SOCKS5 proxy for inspecting, replaying, and modifying traffic.

It is for developers testing browsers, CLIs, mobile apps, API clients, services, and test suites on their own machine or in a local Docker container.

* Capture HTTP traffic and HTTPS traffic after trusting the local oproxy CA.
* View requests, responses, headers, bodies, status, timing, tags, notes, and selected inspector data.
* Replay captured requests and open them in Compose.
* Build manual requests with headers, query params, auth, raw bodies, variables, collections, and cURL export.
* Export captures as HAR or generated cURL, Fetch, and Python snippets.
* Modify traffic with rule sets, map-remote, map-local, access rules, throttling, breakpoints, mock responses, DNS overrides, capture filters, Lua scripts, and upstream proxy chaining.
* Use the authenticated Assistant to inspect state and prepare confirmed proxy changes through an OpenAI-compatible chat model.
* Run from source or Docker with persistent volumes for CA material and local state.

[Short demo video](https://github.com/sauravrao637/oproxy/blob/master/docs/assets/demo.webm)

```
docker run --rm \
  --name oproxy \
  --network host \
  -e OPROXY_BIND_HOST=0.0.0.0 \
  -e OPROXY_MITM_ENABLED=true \
  -v oproxy-certs:/app/certs \
  -v oproxy-storage:/app/storage \
  ghcr.io/sauravrao637/oproxy:latest
```

Open `http://127.0.0.1:8080`.

Or build locally:

```
docker build -t oproxy:latest .
```

```
docker compose up --build
```

The included Compose file uses host networking, persists `/app/certs` and `/app/storage`, and sets `OPROXY_BIND_HOST=0.0.0.0`.

Requirements:

* Rust 1.85 or newer
* Node.js 22 or newer
* Yarn via Corepack

```
corepack enable
yarn --cwd src/design install --frozen-lockfile
yarn --cwd src/design build
cargo run --release
```

Open `http://127.0.0.1:8080`.

```
curl -x http://127.0.0.1:8080 http://example.com
```

The request appears in the Sessions view.

```
curl http://127.0.0.1:8080/admin/ca -o oproxy-ca.crt
curl --cacert oproxy-ca.crt -x http://127.0.0.1:8080 https://example.com
```

For browser HTTPS capture, install the CA from `http://127.0.0.1:8080/admin/ca` into the browser or OS trust store.

* Act as a forward HTTP proxy on `OPROXY_PORT`/`port`, default `8080`.
* Serve the local management UI and API from the same listener.
* Intercept HTTPS CONNECT traffic when MITM is enabled and the client trusts the generated CA.
* Optionally listen for SOCKS5 CONNECT traffic on `socks5_port`.
* Optionally run a second TLS listener with `https_port`.
* Capture live sessions in memory with bounded session and body retention.
* Save and load sessions explicitly with admin endpoints.
* Export HAR, cURL, Fetch, and Python snippets, redacted by default.
* Import HAR files and oproxy JSON session data.
* Stream session-change notifications with server-sent events.
* Inspect JWT, GraphQL, gRPC, and WebSocket frame metadata when matching traffic is captured.

* Debug a browser or CLI request without changing application code.
* Replay a captured request after editing headers or body in Compose.
* Test a frontend against mock responses or local fixture files.
* Route a subset of traffic to a staging service.
* Reproduce slow or bandwidth-limited responses.
* Pause matching requests or responses before they continue.
* Validate how a client behaves when requests are blocked, redirected, or rewritten.

[![oproxy sessions screenshot](https://github.com/sauravrao637/oproxy/raw/master/docs/assets/sessions-screenshot.png)](https://github.com/sauravrao637/oproxy/blob/master/docs/assets/sessions-screenshot.png)

[![oproxy compose screenshot](https://github.com/sauravrao637/oproxy/raw/master/docs/assets/compose-screenshot.png)](https://github.com/sauravrao637/oproxy/blob/master/docs/assets/compose-screenshot.png)

MIT