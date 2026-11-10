---
title: "Windows API Is Successful Cross-Platform API"
url: https://retrocoding.net/windows-api-is-successful-cross-platform-api
clipped: 2026-06-17 01:08:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Windows API Is Successful Cross-Platform API](https://retrocoding.net/windows-api-is-successful-cross-platform-api)

## Digest Summary
None

## Discussion Summary
None

---

## Full Article

You might find the title a little bit odd. Hold your thought for a moment and hear me out. I'm a big believer that in technology, and life, something that comes from consensus from a big, top-down standardisation body usually fails. The internet is an example of the implementation of a top-down approach when a scientist submits a paper for an RFC and *iterates* on it until it's *de-facto* protocol of the internet.

The keyword here is *iterate*. Most of the standard body tries to cover many use cases, primarily their members' interests. This leads to bloated, inefficient and largely unused standards. While their nimbler competition is being adopted, iterated, and expanded. In the internet protocol use cases, OSI Model is now essentially *just a theory* taught in networking training, certification, and classes. In the real world, the internet **is** TCP/IP, and it's TCP IP that runs on computers, phones, and other devices.

Adoption Driven By Pragmatism
=============================

A successful standard is driven by pragmatism. One such standard is POSIX. This standard came from the need to standardise API across UNIX variants and clones. Most modern operating systems implement this standard. From well-known operating systems kernels such as Linux and Darwin (a.k.a Apple macOS) to hobbyist operating systems like Redox and Managarm implements POSIX as their user-space API. Why did I put Windows aside, you might say? I'll talk about that later.

The reason they're implementing POSIX is because of the rich ecosystem it offers. All tooling from GNU, like GCC, will run on a POSIX-compliant operating system. If you build an operating system kernel and then adopt POSIX as your user-space API and decent terminal, you're off to a good start in accessing the breadth of software selections running on your operating system.

Apple took this path when they built Darwin, the kernel of macOS, or previously NeXTStep. NeXT built their kernel by combining Mach and BSD code and then used GCC as its compiler of choice. This way, NeXT saved tremendous time compared to if they built everything alone. They can focus on building the UI which matters to their customers. This was also true for Linux. All software built with POSIX in mind can run on top of Linux. The conformance to POSIX was born due to necessity and pragmatism.

Windows API
===========

Unlike NeXT, Windows was written from scratch without considering POSIX compatibility. It was written as a GUI layer on top of a less powerful MS-DOS kernel. Microsoft built the API to enable programmers to create programs on top of then, just released Windows. The early versions of Windows had their SDK in a single header called `<Windows.h>`. The first Windows SDK fits in seven 400KB diskettes and has only two headers: `STYLE.H` and `WINDOWS.H`. The `Windows.h` header was only 2000+ lines of code. It was a very lean SDK.

![The Windows 1.0 Windows Header](https://cdn.hashnode.com/res/hashnode/image/upload/v1667407385104/2gTV-u67-.png)

Windows 95 is the beginning of 32-bit computing for Microsoft, and the API is being upgraded to cater to 32-bit computing. Microsoft dubbed the new API: "Win32". Windows has grown significantly that `Windows.h` is no longer a single header. It includes other headers from other subsystems. Microsoft rewrote Windows to Windows NT with mostly unchanged API, expanded the API to 'wide-character', and made Windows [supports early Unicode encoding](https://en.wikipedia.org/wiki/Unicode_in_Microsoft_Windows).

From that point, Windows API keeps expanding. Microsoft added a bunch of new technology that I lost count of. Sometimes, however, Microsoft did not do a good job when naming their API. [Dynamic Data Exchange](https://learn.microsoft.com/en-us/windows/win32/dataxchg/about-dynamic-data-exchange), for example, evolved to COM, which was then branded as OLE and OLE Automation. They have unintelligible names that do not explain what they do. It's a shame, tho, as COM (or OLE) is a very useful piece of technology. The branding obscured its usability despite its apparent complexity and boilerplate. The pattern has been imitated by Mozilla and even Apple in their driver framework. [Beno Rice](https://jeamland.net/) explained it in this video:

Microsoft added more APIs because they could: CryptoAPI, DirectX, and so forth. Windows becomes a rich desktop platform. They bundled all of the different APIs and renamed them to simply **Windows API**

Windows API as Pragmatic Cross-Platform Desktop API
===================================================

Windows dominates the Desktop Operating system with more than 80% market share. As Windows grows in market share, so do programs written for Windows. It's not unusual for people to only write a desktop application for Windows. Rather than writing for gazillion desktop environments like GTK or Qt, programmers prefer a predictable and stable API with many learning resources. Microsoft has done a very good job taking care of their ISV (Independent Software Vendors) by building Visual Studio, a remarkable programming IDE and forming MSDN, Microsoft Developer Network, which in my opinion, is the most comprehensive API documentation.

Those programs written by Windows programmers are usable, and people want to run that on systems like Linux. Hence, the [WINE project](https://www.winehq.org/) was born. It loads the executable and then redirects Windows API calls to Linux (or macOS) calls. Surprisingly, this effort is successful. Most programs can run on top of Wine. A company called [Codeweavers](https://www.codeweavers.com/) packages Wine and sells it for a fee for an easy-to-use version of Wine. While doing Windows Retrocoding, I use CrossOver to test my programs on macOS. It runs well and never fails on me.

![Dependency Walker 32-bit running on macOS over Crossover](https://cdn.hashnode.com/res/hashnode/image/upload/v1667410872784/fj6fHqIhG.png)

Windows is also **the platform** for Games. Microsoft has won the API wars between Direct3D and OpenGL. Microsoft's domination in PC gaming is undisputed. However, there is still a sizeable portion of users wishing to run Windows on their Linux Desktop. Steam, the major distribution channel for games on Windows, implements their own version of Wine for gaming and names it Proton. It allows games which originally written **only** for Windows to run on Linux.

The compatibility rate of games running on Proton is also pretty good. I tried running Final Fantasy XIII on a Linux machine, and it worked.

Windows API is Successful Desktop Runtime
=========================================

Windows uses a [Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable) file format, which is originally only intended to be run on top of Windows. However, the format and the API are now generally available for all three major desktop operating systems using Wine, Crossover, or Proton.

In the 90s and early 2000s, Java was marketed as a platform in which one code (bytecode) is run on multiple platforms. It is true for non-x86-based platforms. However, in most cases, Portable Executable is "portable" as it can be executed without modification and recompilation. Now you can run desktop applications, which were originally only written only for Windows, on Linux and macOS. Even if Windows' market share is only 80% of the desktop computing market. Windows API has a 100% market share as it can run on all three major Desktop operating systems.

Windows API and executable format adoption are not imposed by any standard body. Heck, Windows API still has undocumented functions and behaviours, and even Microsoft has blocked the effort to standardise it to an ISO. The adoption was done out of necessity, and people find it useful.