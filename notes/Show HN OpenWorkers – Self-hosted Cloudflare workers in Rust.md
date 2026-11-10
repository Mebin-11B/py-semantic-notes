---
title: "Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust"
url: https://openworkers.com/introducing-openworkers
clipped: 2026-06-17 02:05:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: OpenWorkers – Self-hosted Cloudflare workers in Rust](https://openworkers.com/introducing-openworkers)

## Digest Summary
OpenWorkers is a self‑hosted implementation of Cloudflare Workers written in Rust, enabling developers to run Worker‑compatible scripts outside Cloudflare’s edge network. The provided example demonstrates a basic Worker module exporting an async `fetch` handler that accesses a KV store (`env.KV.get("key")`) and executes a PostgreSQL‑style query (`env.DB.query("SELECT * FROM users WHERE id = $1",[1])`). The handler aggregates the KV value and query result into a JSON response (`Response.json({ data, rows })`). The page includes a logo image and a GitHub icon, indicating the project’s open‑source repository. This setup illustrates how OpenWorkers bridges familiar Cloudflare Worker APIs with Rust’s performance and ecosystem for on‑premise or custom cloud deployments.

## Discussion Summary
The discussion highlights strong interest in a self‑hosted workers runtime as a way to avoid vendor lock‑in and to mirror Cloudflare Workers’ developer experience, while acknowledging the challenges of replicating edge‑scale infrastructure and ensuring robust sandbox security. Commenters repeatedly request thorough testing evidence, production‑grade documentation, and clear failure‑handling or tracing mechanisms, especially for long‑running AI agent workloads. Concerns are raised about persistence, storage integration, and the effort required compared with traditional container or Node/Deno deployments. Overall sentiment is cautiously optimistic, praising the architectural approach but calling for more maturity, tooling, and guidance before broad adoption.

---

## Full Article

```
```
export default {
  async fetch(request, env) {
    const data = await env.KV.get("key");
    const rows = await env.DB.query(
      "SELECT * FROM users WHERE id = $1",
      [1]
    );
    return Response.json({ data, rows });
  }
};
```
```