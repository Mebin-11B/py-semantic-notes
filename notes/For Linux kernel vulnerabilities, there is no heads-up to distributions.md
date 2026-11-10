---
title: "For Linux kernel vulnerabilities, there is no heads-up to distributions"
url: https://www.openwall.com/lists/oss-security/2026/04/30/10
clipped: 2026-06-17 01:09:42
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [For Linux kernel vulnerabilities, there is no heads-up to distributions](https://www.openwall.com/lists/oss-security/2026/04/30/10)

## Digest Summary
CVE‑2026‑31431 (“CopyFail”) is a Linux kernel local‑privilege‑escalation flaw introduced in kernel 4.14 (commit 72548b093ee38a6d4f2a19e6ef1948ae05c181f7). The issue was patched in the stable branches 6.18.22 (commit fafe0fa2995a0f7073c1c358d7d3145bcc9aedd8), 6.19.12 (commit ce42ee423e58dffa5ec03524054c9d8bfd4f6237) and upstream 7.0 (commit a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5). Older long‑term kernels—6.12, 6.6, 6.1, 5.15, 5.10—remain unpatched; backporting is complicated by API changes. An attempted backport failed, and a temporary mitigation was provided as a patch disabling the “authencesn” crypto module (attached as 0001‑crypto‑disable‑authencesn‑module‑for‑CVE‑2026‑31431.patch). The author notes that kernel vulnerability notices are not automatically forwarded to distribution mailing lists unless the reporter does so.

## Discussion Summary
The comments criticize the current Linux kernel vulnerability disclosure flow, arguing that relying on individual reporters to notify downstream distributions is inadequate and that the kernel security team should assume that responsibility. Many express concern over premature public release of the exploit and its impact on shared‑hosting providers, while also noting that several distributions have already applied patches or can mitigate the issue with workarounds such as eBPF filters or default nosuid mounts. Opinions acknowledge that not every system is affected, but consensus calls for improved coordination and stronger default security settings.

---

## Full Article

[[<prev]](https://www.openwall.com/lists/oss-security/2026/04/30/9) [[next>]](https://www.openwall.com/lists/oss-security/2026/04/30/11) [[<thread-prev]](https://www.openwall.com/lists/oss-security/2026/04/30/6) [[thread-next>]](https://www.openwall.com/lists/oss-security/2026/04/30/11) [[day]](https://www.openwall.com/lists/oss-security/2026/04/30/) [[month]](https://www.openwall.com/lists/oss-security/2026/04/) [[year]](https://www.openwall.com/lists/oss-security/2026/) [[list]](https://www.openwall.com/lists/oss-security/)

```
Message-ID: <87se8dgicq.fsf@gentoo.org>
Date: Thu, 30 Apr 2026 05:52:37 +0100
From: Sam James <sam@...too.org>
To: oss-security@...ts.openwall.com
Cc: Jan Schaumann <jschauma@...meister.org>
Subject: Re: CVE-2026-31431: CopyFail: linux local privilege
 scalation

Eddie Chapman <eddie@...k.net> writes:

> On 29/04/2026 21:23, Jan Schaumann wrote:
>> Affected and fixed versions
>> ===========================
>> Issue introduced in 4.14 with commit
>> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in
>> 6.18.22 with commit
>> fafe0fa2995a0f7073c1c358d7d3145bcc9aedd8
>> Issue introduced in 4.14 with commit
>> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in
>> 6.19.12 with commit
>> ce42ee423e58dffa5ec03524054c9d8bfd4f6237
>> Issue introduced in 4.14 with commit
>> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in
>> 7.0 with commit
>> a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5
>> https://git.kernel.org/stable/c/fafe0fa2995a0f7073c1c358d7d3145bcc9aedd8
>> https://git.kernel.org/stable/c/ce42ee423e58dffa5ec03524054c9d8bfd4f6237
>> https://git.kernel.org/stable/c/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5
>
> So this is one of the worst make-me-root vulnerabilities in the kernel
> in recent times. I see that on the 11th of April 6.19.12 & 6.18.22
> were released with the fix backported.
>
> Longterm 6.12, 6.6, 6.1, 5.15, 5.10 have not received the fix and I
> don't see anything in the upstream stable queues yet as I write. My
> guess is backporting that far back is not as straightforward. As this
> was introduced in 2017 all those older kernels are affected, right? Or
> am I missing something?

It does not apply cleanly, no. Attached is the workaround we're going to
use. I'm not an expert on IPSec but I think this is the lesser evil.

I attempted a backport but ran into a few API changes and wasn't
confident enough to muck around with it, especially for something to
deploy immediately.

> [...]
>
> What went wrong, has the embargo been broken early today? Not looking
> to point any fingers, those who make things happen in our communities
> work dam hard and deserve respect and support, especially with the
> extra burden of AI slop now.

Note that for Linux kernel vulnerabilities, unless the reporter chooses
to bring it to the linux-distros ML, there is no heads-up to
distributions.

It did not happen here.

>
> Eddie

sam


View attachment "0001-crypto-disable-authencesn-module-for-CVE-2026-31431.patch" of type "text/x-patch" (1543 bytes)

Download attachment "signature.asc" of type "application/pgp-signature" (419 bytes)
```

[Powered by blists](https://www.openwall.com/blists/) - [more mailing lists](https://lists.openwall.net)

Please check out the
[Open Source Software Security Wiki](https://oss-security.openwall.org/wiki/), which is counterpart to this
[mailing list](https://oss-security.openwall.org/wiki/mailing-lists/oss-security).

Confused about [mailing lists](https://www.openwall.com/lists/) and their use?
[Read about mailing lists on Wikipedia](https://en.wikipedia.org/wiki/Electronic_mailing_list)
and check out these
[guidelines on proper formatting of your messages](https://www.complang.tuwien.ac.at/anton/mail-news-errors.html).