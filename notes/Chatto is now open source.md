---
title: "Chatto is now open source"
url: https://www.hmans.dev/blog/chatto-is-open-source
clipped: 2026-08-31 12:22:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Chatto is now open source](https://www.hmans.dev/blog/chatto-is-open-source)

## Digest Summary
Chatto, a group‑chat application, has been released as open‑source software and can be self‑hosted. Install via Homebrew (`brew install chattocorp/tap/chatto`) or download binaries for Linux (x86_64/ARM64), macOS, and Windows. The server runs as a single executable, serves its own frontend, and requires minimal resources. All personal and chat data are encrypted at rest with per‑user keys that are deleted upon account removal; no federation or third‑party analytics occur. Clients can connect to multiple independent servers simultaneously. Built‑in voice/video calls and screen‑sharing are end‑to‑end encrypted and scale with the host’s capacity.  

Chatto Cloud, entering public beta soon, offers paid hosting on European‑owned infrastructure with automatic scaling, nightly backups, and zero‑downtime upgrades; hosted servers remain fully compatible with self‑hosted deployments.  

Current version is 0.4, considered production‑ready. Roadmap targets 0.5 (content reporting, moderation, multi‑server UI improvements) and a 1.0 release within 6–12 months, with possible breaking changes. Community support and a low‑volume newsletter are provided for updates and feedback.

---

## Full Article

[â Back](https://www.hmans.dev/)  

Hot damn. This is the big one. 

Iâm happy to announce that Chatto, the group and team chat application that Iâve been working on for the past year or so, is now officially Open Source, and available for anyone to self-host. 

The fastest way to give it a try is through Homebrew:  ` `brew install chattocorp/tap/chatto
chatto init
chatto run` `  

See Chattoâs [Getting Started Guide](https://docs.chatto.run/getting-started/introduction/) for details. Or stick around to hear more! 

## Chat Just Got Real

 

Chatto aims to be the group chat application that you actually enjoy using. Youâre probably familiar with the one that rhymes with âknackâ, or the one that rhymes with âbeamsâ, or the one that rhymes with âthis gourdâ. 

Chatto is just like those. Except youâre going to love how compact and snappy it is. And that itâs Open Source. And you can just self-host it. For free, too! (A weird thing to write, but the OSS chat app space has become very weird in many ways!) 

This is what it looks like:  

If you want to see it in action, drop by the [Chatto HQ Community](https://chat.chatto.run)! 

Itâs designed to be extremely easy to self-host on your own infrastructure. In its most basic shape, you just run the executable, and thatâs it. It even serves its own frontend! 

Itâs very light on resources, and probably has the snappiest frontend that youâve ever used in an app like this. It puts data protection and privacy first, with all personal and chat data fully encrypted at rest with per-user keys that get shredded when a user decides to delete their account. 

Each Chatto server powers a single community, with no federation of data between servers, nor any third-party tracking or analytics. If you want to hang out in multiple servers at once, the client will simply connect to all of them directly. If you want to host multiple communities, just spin up multiple Chatto processes. Easy! 

Chatto comes with full support for voice and video calls, with screen-sharing, built in. Calls are fully end-to-end encrypted and will scale to as many participants as your infrastructure can handle. 

And you can use it today, for free, by self-hosting it on your own server. Binaries are available for Linux (x86_64 and ARM64), macOS, and Windows; head over to the [Chatto Self-Hosting Documentation](https://docs.chatto.run/) site to get started. 

## Chatto Cloud

  

If you prefer someone else to take care of the hosting, Iâm also happy to announce that Chatto Cloud will soon enter public beta. Chatto Cloudâs offering is very simple: it provides paid hosting for Chatto servers â and thatâs it. No premium subscriptions, no ads, no icky bits. Just hosting. 

And itâs really good hosting! Chatto Cloud is launching with fully European and European-owned infrastructure, with more regions slated for launch in early 2027. Every Chatto server on Chatto Cloud benefits from automatic scaling, nightly backups of all data, and zero-downtime version upgrades. 

Thereâs no lock-in; servers hosted through Chatto Cloud are 100% compatible with self-hosted ones, and you can pack up your data and move into or out of Chatto Cloud at any time. 

If you want to get notified about the start of the beta, please see the end of this post for a low-volume newsletter you can subscribe to. 

## Whatâs Next for Chatto

 

Chatto is now at version 0.4. I consider it stable enough for production use, but there are a few important features still missing â head over to the [Chatto Roadmap](https://github.com/orgs/chattocorp/projects/1) if you want an overview. 

The focus for Chatto 0.5 will be on additional safety features (content reporting and moderation) as well as polishing the client, particularly its multi-server functionality. I have some fun stuff planned for this that I canât wait to put into peopleâs hands. 

I expect Chatto to hit 1.0.0 in about 6-12 months. Until then, there may still be breaking changes, even though Iâll be trying to keep them to a minimum. If you do decide to self-host, please be ready to update to new versions as they are released. 

## Get in Touch

 

Itâs been an exciting journey so far and Iâm looking forward to finding out whatâs ahead. If youâre self-hosting Chatto, Iâm super eager to hear from you about your experience â please donât hesitate to head over to the [Chatto HQ community](https://chat.chatto.run/) and get in touch. 

Also please feel free to drop by and say hello if youâre interested in Chatto for your company, Open Source project, or similar. Iâd love to learn more about your requirements, and help you get set up. 

## Links

 
- [Chatto HQ Community](https://chat.chatto.run/) - we have a  `#self-hosting`  support channel! 
- [Chatto Self-Hosting Documentation](https://docs.chatto.run/) 
- [GitHub Repository](https://github.com/chattocorp/chatto) 
- [Chatto on Bluesky](https://bsky.app/profile/chatto.run) 

## Newsletter

 

If you want to be notified about new releases or the start of Chatto Cloudâs beta, youâre invited to subscribe to the Chatto announcements newsletter. Itâs super low-volume (~1 email per month), and is only used for notifying you when exciting new stuff becomes available.   

Powered by [Buttondown](https://buttondown.com/refer/hmans).
