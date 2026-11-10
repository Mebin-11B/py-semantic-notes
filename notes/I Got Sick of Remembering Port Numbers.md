---
title: "I Got Sick of Remembering Port Numbers"
url: https://gregraiz.com/blog/local-vibe/
clipped: 2026-06-17 01:09:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - local development
  - ports management
  - reverse proxy
related:
  - "[[Local Development]]"
  - "[[Ports Management]]"
  - "[[Reverse Proxy]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** local.vibe is a macOS-only, open-source Go utility that routes custom `.vibe` hostnames to local development ports over HTTPS, eliminating the need to remember port numbers.
>
> **Key points:**
> - Runs as a background daemon reverse proxy utilizing dnsmasq, local CA trust (Keychain), and a pf port-forwarding rule.
> - Automatically assigns unused ports to projects defined in a local `vibe.json`, exposing them as custom subdomains (e.g., `https://blog.vibe`).
> - Features a browser-based dashboard at `https://local.vibe` for monitoring, starting, stopping, and editing running services.
> - Exposes an HTTP API (`/setup.md`) that allows AI coding agents (like Claude Code or Cursor) to configure and query the environment.
>
> **Concept links:** [[Local Development]], [[Ports Management]], [[Reverse Proxy]], [[DNS Resolution]], [[macOS Utilities]], [[AI Agent Integration]]
>
> **Suggested connections:**
> - [[Local Development]] — workflows, server configurations, and tools for building software locally.
> - [[Reverse Proxy]] — architectural patterns for routing traffic to multiple internal port endpoints.
<!-- ai-summary:end -->

# [I Got Sick of Remembering Port Numbers](https://gregraiz.com/blog/local-vibe/)

## Digest Summary
The post describes “local.vibe,” a macOS‑only, open‑source tool (MIT licensed) that eliminates the need to remember local development port numbers. Implemented as a single Go binary, it installs dnsmasq, a pf port‑forwarding rule, and a trusted local CA, then runs as a daemon communicating via a Unix‑socket reverse proxy. For each project, a `vibe.json` defines a name and command; when started, local.vibe auto‑assigns an unused port, injects it as `$PORT`, and creates a `.vibe` hostname (e.g., `https://blog.vibe`) that proxies to the service over HTTPS. A dashboard at `https://local.vibe` lists running services, supports start/stop, editing, emoji icons, and grid or list views. It also provides built‑in proxies such as `tailscale.vibe` and `hass.vibe`. An HTTP API (e.g., `http://localhost:7999/setup.md`) enables AI agents to query or control the environment. Installation is a one‑line `setup.sh` after cloning the repository.

## Discussion Summary
The discussion centers on practical methods for managing service ports, with users sharing personal setups that combine configuration files, custom scripts, and tools like outport.dev and a GitHub “sonar” utility. Participants note advantages of automatic start‑stop mechanisms and resolver tricks, while also highlighting drawbacks such as AI agents mishandling process lifecycles and default port choices that feel inconvenient. Overall, the comments reflect a constructive exchange of alternatives, a desire for clearer port naming, and mild frustration with existing defaults and automation shortcomings.

---

## Full Article

I Got Sick of Remembering Port Numbers
======================================

I run a lot of stuff locally. Jekyll blogs, Flask APIs, Next.js apps, AI tools, little scripts that do one thing well. Each one lives on some port. Each session, Iâd open a new browser tab and think: was that one on 3000? Or did I move it to 5173 because something else grabbed 3000? What about that Tailscale URL for my home server?

The real annoyance is that it wasnât just one machine. It was layers. Local ports fighting each other. Hostnames I couldnât remember. Scripts that would happily steal whatever port they wanted if I started them in the wrong order.

I wanted a simple launcher for all the things that arenât traditional desktop apps. Not Finder, Alfred or Raycast. Something that understood localhost.

The problem is **port rot**: the slow accumulation of services, forgotten ports, and dead browser tabs that makes your local dev environment feel like a junk drawer. Worse many of these things donât need to be running all the time. They should run when needed and then quietly spin down.

So I built [local.vibe](https://github.com/graiz/local.vibe).

What it does
------------

Tell your coding agent about local.vibe and itâll drop a `vibe.json` in any project:

```` |  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` {   "name": "blog",   "cmd": "bundle exec jekyll s" } ``` | ````

Run `vibe start`. Now `https://blog.vibe` works in any local browser. No more port numbers. No more âwait, which tab was that?â

It can auto-assigns a free port, passes it to your app as `$PORT`, and proxies the `.vibe` hostname to it. A local certificate gets trusted in your Keychain so HTTPS just works. The daemon watches the process; if it crashes or rebinds.

The dashboard lives at https://local.vibe and shows everything running at once.

Start, stop, edit, add an emoji icon. Switch between grid and list view.

Bookmarks work too. `tailscale.vibe` can redirect to your Tailscale machine. `hass.vibe` can proxy to your Home Assistant. Anything youâd type into a browser tab can become a `.vibe` name.

Why a single binary
-------------------

Itâs built in Go. Local.vibe is a single binary. One `setup.sh`, and it installs dnsmasq, a pf port-forwarding rule, and the local CA. After that, itâs just running.

The whole thing communicates over a Unix socket acting as a reverse proxy. No external services, no accounts, no telemetry.

The agent angle
---------------

One thing I didnât expect to be useful but actually is: the setup guide endpoint.

```` |  |  |
| --- | --- |
| ``` 1 ``` | ``` curl http://localhost:7999/setup.md ``` | ````

Paste that into Claude Code or Cursor and the agent understands your local.vibe setup. It can register new routes, check whatâs running, start and stop apps via the HTTP API. That turned out to be a genuinely useful integration to get projects onboarded quickly.

Try it
------

```` |  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` git clone https://github.com/graiz/local.vibe.git cd local.vibe ./setup.sh ``` | ````

Itâs open source, macOS only for now, MIT licensed. If youâre drowning in port numbers, give it a spin. Iâd love to know what breaks, whatâs missing, and whether the setup holds up on machines that arenât mine. Drop a comment below or open an issue on [GitHub](https://github.com/graiz/local.vibe).