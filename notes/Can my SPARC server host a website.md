---
title: "Can my SPARC server host a website?"
url: https://rup12.net/posts/can-my-sparc-server-host-my-website/
clipped: 2026-06-17 01:45:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Can my SPARC server host a website?](https://rup12.net/posts/can-my-sparc-server-host-my-website/)

## Digest Summary
A 2001 Sun Netra X1 SPARC server (500 MHz UltraSPARC IIe, 1 GB ECC SDRAM, IDE disks) was repurposed to host a static website. The OS is OpenBSD 7.8, installed via PXE/TFTP/NFS because the machine lacks optical or USB boot. Only essential packages were added (git, vim, neofetch, htop, rsync); the built‑in OpenBSD httpd serves HTML/CSS from /var/www, with directory listings disabled and hidden files blocked. The system runs ~55 MB RAM, with sshd and httpd as the only network services. A Cloudflare tunnel provides outbound‑only connectivity: a modern host (e.g., Proxmox LXC) runs cloudflared, forwarding traffic to the Netra’s internal address (192.168.1.248:80). pf is configured with a default‑deny policy, allowing ssh from local subnets (192.168.1.0/24, 10.0.1.0/24) and HTTP only from the tunnel host (10.0.1.210). No dynamic content, CGI, or PHP is used, minimizing attack surface while demonstrating that legacy SPARC hardware can reliably serve static web pages when combined with contemporary tunneling and firewall techniques.

## Discussion Summary
Comments collectively recall the extensive use of Sun and SPARC hardware for web hosting during the late‑1990s and early‑2000s, emphasizing its durability and historical prevalence. Many note that such machines can still run simple sites, though they acknowledge limitations for higher traffic and consider the practice unremarkable today. Some criticize the framing of the topic as clickbait, while others express fatigue with repeated discussions of legacy hardware for hosting, suggesting modern solutions like cloud services are more appropriate. Overall sentiment blends nostalgia with practical skepticism.

---

## Full Article

> **TL;DR:** Iâm hosting a website on a 25-year-old Sun Netra X1 SPARC server running OpenBSD 7.8. The setup includes: Noctua fan mods for quiet operation, `httpd` serving static HTML/CSS, OpenBSDâs `pf` firewall with default-deny rules, and Cloudflare tunnels to expose it safely without port forwarding. The server pulls ~55MB of RAM and serves pages from my garage. Check it out live at [sparc.rup12.net](https://sparc.rup12.net) - because why not?

---

What?!
------

Hereâs a crazy idea, can I expose and host a website on a 2001 [Sun MicroSystems](https://en.wikipedia.org/wiki/Sun_Microsystems) [Netra X1](https://www.filibeto.org/sun/lib/hardware/datasheets/sun_netra_x1.pdf) SPARC Server? [Yes, yes I can](https://sparc.rup12.net). Letâs get into how I set this up.

Hardware
--------

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/server.jpeg)

Not so long ago, I ordered from eBay a [Sun Fire V100](https://dogemicrosystems.ca/wiki/Sun_Fire_V100) server. But somehow, the seller made a mistake, and sent me a Netra X1. Now, these systems are quite similar, and to be honest I did not mind. (the seller did give me a discount on the next system I buy ï¸â¥ï¸). The Netra X1 is a more commodity grade server, this means it completely headless (no video output), and uses standard SD-RAM (ECC) and runs a pair of IDE Hard Disks. At the center of this server is a 500 Mhz UltraSparcIIe CPU and a whopping 1GB of said SD-RAM. This was a *lot* of RAM back then, but I guess it makes sense for its server-esque purpose.

This isnât my first Sun hardware rodeo. I previously restored a [Sun Ultra 1 Creator workstation from 1995](https://rup12.net/posts/adventures-with-sun-ultra-1-workstation/) if you want to see where this obsession started.

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/cpu.jpeg)

Oh, and I did some HDD archeology, it seems this is a decommissioned server from Ford (the car company). I am not sure what it used to do, but the disks were obviously not wiped. Rest assured, the data is gone and both drives were formatted by me.

To go along with this server, I have a nice Sun rack in my garage, as well as a [Cisco 2960-S](https://www.cisco.com/c/en/us/support/switches/catalyst-2960-s-series-switches/series.html) network switch. However, at the time of writing, both of them are sitting on my workbench, humming along as I test some hardware modifications I made to both of them. Yes, I **made some tweaks**. Namely, both the Cisco switch and the Netra were quite loud. Not, aircraft taking off loud, but still loud for having them be in a place I record videos in. To remedy that, I replaced most of their internal fans with [Noctua](https://www.noctua.at/en) 40mm fans. For the Cisco I even had to 3D print a [part](https://www.thingiverse.com/thing:6275275) to replace one big blower fan with 2 smaller ones. Now both these devices are almost completely quiet, at the cost of some higher temperatures.

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/cisco.jpeg)

To install the operating system on the Netra I had to use PXE Boot and TFTP/NFS, as it had no optical drive and it cannot boot from USB. Oh, and I will explain how I did that in a **future post**. While I was hoping to use Solaris here, I realized it is just too ancient. Exposing such an OS to the internet would cause all kinds of issues. I opted for the tried and true **[OpenBSD](https://www.openbsd.org/)**, as a secure and optimal choice (NetBSD was also something I was considering, but decided to go with OpenBSD due to their security-first philosophy). Letâs get into it.

Software
--------

OpenBSD works like a charm. Once I was able to boot the system (and run the installer), I ran into almost no issues. Even though it is running on a 25 year old system it still works rather well. Once I had OpenSSH set up, it was using around 55MB of RAM. While I am not as familiar with OpenBSD as I am with Linux, I find working on it to be rather straightforward. Package management is done via the `pkg_*` utility, and there seems to be a plethora of [packages](https://www.openbsdhandbook.com/package-search/) available even for the `Sparc64` architecture (I even got Rust running ð¦).

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/neofetch.webp)

The packages I found necessary for this adventure were: `git`, `vim`, `neofetch`, `htop`, `rsync`. Yes, thatâs it. To install the packages it is as easy as running:

```
pkg_add neofetch
```

The web server of choice here was `httpd`, even though `nginx` was available (and I was more used to that one), `httpd` seems to be a common choice on OpenBSD so I went with that. As I was a bit unfamiliar with the configuration of the server I turned to, wherever else, but my coding assistant. Working with [Kiro](https://kiro.dev) I worked out the `httpd` configuration file in `/etc/httpd.conf` and made a few tweaks (removed directory listing). And set it up so that I just use only the features I need. No CGI, no PHP, no caching. Oh and, the `httpd` package already natively comes with OpenBSD. ð

```
types { include "/usr/share/misc/mime.types" }
 
server "default" {
    listen on * port 80
    root "/htdocs"
 
    # Disable directory listings
    directory no auto index
 
    # Drop requests for hidden files
    location "/**/.*" {
        block return 404
    }
}
```

Whatâs great about `httpd` is that itâs `www` user is chrooted into `/var/www` so it makes it slightly more secure. And since I am exposing a server in my house, I need it to be as secure as I can.

One `rcctl start httpd` later, and I have a web server running! ð¥³ Huzzah! Now, itâs time to build my **web application**!

The website
-----------

To make this plausible (and secure), I wanted to make the application as simple as possible. So, basic HTML and CSS it is! It also fits the 2001 aesthetic, back when The Internet was a lot more human and *marquees* ruled the roost. The web page I decided to make is a simple *about* page, pulling inspiration (and content) from my [actual about page](https://rup12.net/about). While I could easily cobble up an `index.html` together, after all itâs just HTML and CSS, and Iâve been writing that for almost as long as this server is old. Iâve decided to test out something new.

Recently, more and more coding assistants have implemented a feature where they can call up a *sub* or a *specialized agent* to do certain tasks. The reasoning behind this, as far as I am able to figure out is that you do not want to give your main agent **all** the tools, MCP servers and prompts. Weâre still dealing with prompt economics after all. And this [sub agent](https://kiro.dev/docs/cli/chat/subagents/#custom-subagents) can have additional special instructions on how to perform itâs tasks. My main agent (I call it `oxide`) is configured in such a way that it has access to tools and prompts so it is able to help me learn and write real good Rust code. But it has nothing special that can help it work with front-end web creation. Say hello to `front-end-specialist`.

Now this agent has access to a few MCP Servers and a wonderful prompt that tells it what kind of front end web I like. Simple, as vanilla as possible, minimal JS, and `htmx` where possible. So how does this work? Well the workflow is the following:

### Step 1:

I tell my main agent (`oxide`) that I am building a retro inspired server (with all the Sun/OpenBSD details) and that I want to build a simple `index.html` that would use the data from my [about](https://rup12.net/about) page as well as would outline a bit from this server. Oh, and it would show the output from `neofetch` as content in a `<pre>` tag.

### Step 2:

Then, the main agent would `fetch` the data from my page, and prompt the `front-end-specialist` with the information and instructions. As well as the request to write down the `index.html` in the current directory.

And just like that, we got [this](https://sparc.rup12.net). Wow!

Tunneling
---------

Okay, so how do we get this thing to the internet? Port Forwarding? Dynamic DNS? IPv6? Not a chance! Iâm not exposing an IP address of a server in my garage to the internet. ð There must be a way to, proxy this! I was thinking of some sort of reverse proxy in the cloud, setting up a server to do something. But, then Iâve learned of something wonderful! CloudFlareâs [tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) ð.

**Simply put:** This is a way to create a *tunnel* between CloudFlare and a system running the `cloudflared` daemon. This creates an *outbound* connection, so technically I am not exposing any ports at all. The biggest security benefit here is that there are no inbound connections to my network.

Yes, there is a *however*. The `cloudflared` [daemon](https://github.com/cloudflare/cloudflared) does not really work on `Sparc64`, and while it is open source and written in Go. I cannot really compile it myself there, as Go (unlike Rust) does not support the `Sparc64` CPU architecture. So how do I get this daemon running on the Netra. Well, thatâs the neat part, *I donât*.

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/neat.webp)

CloudFlareâs tunnel daemon also supports the ability to forward traffic to a remote host. This means I can install `cloudflared` on some more modern host running on the same network, and just forward traffic to the Netra. This can be something as simple as Raspberry Pi, butâ¦ wait! I have a entire [Proxmox](https://www.proxmox.com/en/) setup running at home. Iâm sure I can make a container to do just this. And after a quick search through the [Proxmox LXC helper scripts](https://community-scripts.github.io/ProxmoxVE/scripts) I found *exactly* what I need.

Just run this command in the shell of your Proxmox host, and it will install the `cloudflared` daemon, and everything it needs to be running.

```
# This goes in the VM Host shell
### ð¨ WARNING: Never run Bash scripts of the internet without checking, even if it was me who shared them
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/cloudflared.sh)"
### ð¨ WARNING: Never run Bash scripts of the internet without checking, even if it was me who shared them
```

To configure the daemon, you need to edit the configuration file in `/usr/local/etc/cloudflared/config.yaml`:

```
tunnel: sparc # Name of the tunnel
credentials-file: /root/.cloudflared/<UUID>.json
 
ingress:
  - hostname: sparc.rup12.net
    service: http://192.168.1.248:80 # The Netra X1
  - service: http_status:404
```

Here I just forward all traffic to `192.168.1.248` which is that Netra server, on port **80**. Boom ð¥ done! Iâll leave [instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/) from my friends over at Cloudflare on how to set up tunnels, but this is rather straightforward. Lastly, I need to configure a **DNS CNAME** to point to a specific URL that features the *UUID* of my Tunnel: `<uuid>.cfargotunnel.com`

In rather simple terms, here is how this architecture looks like:

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/sparc_web.webp)

Before we go, some security
---------------------------

I love OpenBSDâs security-first philosophy. So to play that part I did the following to improve this servers security.

Since this server is exposed to the internet, I implemented several layers of security:

* **Firewall**: Configured OpenBSDâs `pf` with default-deny rules. Only SSH from my local networks (192.168.1.0/24 and 10.0.1.0/24) and HTTP exclusively from the Cloudflare tunnel container (10.0.1.210)
* **Minimal attack surface**: Disabled all unnecessary services - only running `httpd`, `sshd`, and essential system daemons
* **Static content only**: Like I said, no CGI, no scripting, no dynamic content - just HTML and CSS served by `httpd`
* **Network isolation**: The Cloudflare tunnel creates an outbound-only connection, so no inbound ports are exposed on my home network
* **Current software**: Running OpenBSD 7.8 with plans to upgrade to new releases when they are out

Done?
-----

Yeah, thatâs it. You can go and see the website **RIGHT NOW** ð (unless itâs down for some reason). Is this something the world needs? Not really. Is this something I need? *absolutely*! I have a few more things to fix up, namely figure out how to track the visitors on my website (I want to see if I actually get some hits), and put the server back in the rack so it can live out itâs days where it belongs!

Here:

![](https://rup12.net/post-content/can-my-sparc-server-host-my-website/rack.jpeg)