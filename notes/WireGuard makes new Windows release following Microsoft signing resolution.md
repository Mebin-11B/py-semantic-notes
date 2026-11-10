---
title: "WireGuard makes new Windows release following Microsoft signing resolution"
url: https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html
clipped: 2026-06-17 01:19:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [WireGuard makes new Windows release following Microsoft signing resolution](https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html)

## Digest Summary
WireGuardNT v0.11 and WireGuard for Windows v0.6 have been released, updating both the low‑level kernel driver/API (WireGuardNT) and the higher‑level management UI, CLI tools, and utilities (WireGuard for Windows). New capabilities include removal of individual allowed IPs without dropping traffic and support for very low IPv4 MTUs. The release focuses on extensive bug fixes, performance gains, and code simplification achieved by raising the minimum supported Windows version, eliminating legacy compatibility layers. Toolchain components have been upgraded: a newer EWDK for the driver, updated Clang/LLVM/MingW for userspace, a recent Go release for the UI, and refreshed EV code‑signing infrastructure. The built‑in updater will prompt users to install the update; the installer is also available at https://download.wireguard.com/windows-client/wireguard-installer.exe. Testing has been performed on Windows 10 build 10240 (the oldest supported version). A prior Microsoft signing‑certificate block was resolved after brief bureaucratic delay, allowing the release to proceed.

## Discussion Summary
The discussion centers on Microsoft’s recent developer‑account deactivations that impacted projects such as WireGuard, VeraCrypt and others. Commenters express relief that the specific cases were reversed quickly, but they also criticize the opaque verification process, inadequate communication, and the broader code‑signing mandate that they view as a systemic risk to open‑source software. The prevailing view attributes the problem to bureaucratic incompetence rather than deliberate malice, while many call for clearer policies and safeguards to prevent similar disruptions for smaller developers.

---

## Full Article

[ANNOUNCE] WireGuardNT v0.11 and WireGuard for Windows v0.6 Released
====================================================================

**Jason A. Donenfeld**
[Jason at zx2c4.com](mailto:wireguard%40lists.zx2c4.com?Subject=Re%3A%20%5BANNOUNCE%5D%20WireGuardNT%20v0.11%20and%20WireGuard%20for%20Windows%20v0.6%20Released&In-Reply-To=%3CCAHmME9rTCt5V%3D4ULQ2XM1DkWMdG_b4VJJCGF4aMBnd6VVnFsXA%40mail.gmail.com%3E "[ANNOUNCE] WireGuardNT v0.11 and WireGuard for Windows v0.6 Released")  
*Fri Apr 10 14:20:51 UTC 2026*

---

```
Hey folks,

I generally don't send announcement emails for the Windows software,
because the built-in updater takes care of notifying the relevant
users. But because this hasn't been updated in so long, and because of
recent news articles, I thought it'd be a good idea to notify the
list.

After a lot of hardwork, we've released an updated Windows client,
both the low level kernel driver and api harness, called WireGuardNT,
and the higher level management software, command line utilities, and
UI, called WireGuard for Windows.

There are some new features -- such as support for removing individual
allowed IPs without dropping packets (as was added already to Linux
and FreeBSD) and setting very low MTUs on IPv4 connections -- but the
main improvement is lots of accumulated bug fixes, performance
improvements, and above all, immense code streamlining due to
ratcheting forward our minimum supported Windows version [1]. These
projects are now built in a much more solid foundation, without having
to maintain decades of compatibility hacks and alternative codepaths,
and bizarre logic, and dynamic dispatching, and all manner of crust.
There have also been large toolchain updates -- the EWDK version used
for the driver, the Clang/LLVM/MingW version used for the userspace
tooling, the Go version used for the main UI, the EV certificate and
signing infrastructure -- which all together should amount to better
performance and more modern code.

But, as it's our first Windows release in a long while, please test
and let me know how it goes. Hopefully there are no regressions, and
we've tested this quite a bit -- including on Windows 10 1507 Build
10240, the most ancient Windows that we support which Microsoft does
not anymore -- but you never know. So feel free to write me as needed.

As always, the built-in updater should be prompting users to click the
update button, which will check signatures and securely update the
software. Alternatively, if you're installing for the first time or
want to update immediately, our mini 80k fetcher will download and
verify the latest version:
- https://download.wireguard.com/windows-client/wireguard-installer.exe
- https://www.wireguard.com/install/

And to learn more about each of these two Windows projects:
- https://git.zx2c4.com/wireguard-windows/about/
- https://git.zx2c4.com/wireguard-nt/about/

Finally, I should comment on the aforementioned news articles. When we
tried to submit the new NT kernel driver to Microsoft for signing,
they had suspended our account, as I wrote about first in a random
comment [2] on Hacker News in a thread about this happening to another
project, and then later that day on Twitter [3]. The comments that
followed were a bit off the rails. There's no conspiracy here from
Microsoft. But the Internet discussion wound up catching the attention
of Microsoft, and a day later, the account was unblocked, and all was
well. I think this is just a case of bureaucratic processes getting a
bit out of hand, which Microsoft was able to easily remedy. I don't
think there's been any malice or conspiracy or anything weird. I think
most news articles currently circulating haven't been updated to show
that this was actually fixed pretty quickly. So, in case you were
wondering, "but how can there be a new WireGuard for Windows update
when the account is blocked?!", now you know that the answer is,
"because the account was unblocked."

Anyway, enjoy the new software, and let me know how it works for you.

Thanks,
Jason

[1] https://lists.zx2c4.com/pipermail/wireguard/2026-March/009541.html
[2] https://news.ycombinator.com/item?id=47687884
[3] https://x.com/EdgeSecurity/status/2041872931576299888
```

---

---

[More information about the WireGuard
mailing list](https://lists.zx2c4.com/mailman/listinfo/wireguard)