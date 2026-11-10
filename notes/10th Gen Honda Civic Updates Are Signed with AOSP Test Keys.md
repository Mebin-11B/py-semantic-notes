---
title: "10th Gen Honda Civic Updates Are Signed with AOSP Test Keys"
url: https://juniperspring.org/posts/honda-evil-valet/
clipped: 2026-06-17 00:47:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [10th Gen Honda Civic Updates Are Signed with AOSP Test Keys](https://juniperspring.org/posts/honda-evil-valet/)

## Digest Summary
The post updates a three‑year‑old project that reverse‑engineered the head‑unit of a 2021 Honda Civic. Honda’s OTA update mechanism accepts a signed AOSP test‑key package via USB; the recovery binary’s signature verification matches stock AOSP, allowing anyone with physical USB access to install arbitrary code without root privileges. This “evil valet” attack enables arbitrary execution on the head‑unit when the vehicle is unattended. The author released **ota‑builder**, a tool that formats USB drives and signs updates with the public test key, and **apk‑rebuilder**, which extracts resources, decompiles smali, repacks APKs, and pulls the ramdisk from Honda OTA files, facilitating analysis without distributing proprietary code. Ongoing tasks include cataloguing head‑unit firmware versions, refining a clean ARMv7 toolchain, supporting custom UI themes (complicated by Mitsubishi’s AOSP fork), and improving an aidl‑rebuilder for mapping AIDL interfaces. Documentation is minimized in favor of deterministic tooling that can be queried by LLMs. The repository remains open for contributions and pull requests.

## Discussion Summary
The comments convey strong criticism of Honda’s firmware update process, highlighting that update packages are signed with a publicly known test key and that signature checks are ineffective, allowing arbitrary code execution without root access. This is interpreted as evidence of poor security design and a lack of protective measures for owners. The discussion expands to broader automotive security concerns, referencing similar weaknesses in other manufacturers, questioning documentation practices, and speculating on potential exploit pathways such as CAN‑gateway access or custom operating system installations. Overall, the tone is skeptical and alarmed about vehicle security.

---

## Full Article

Three years ago, I published my initial work to understand and reverse engineer my car, specifically the headunit of my 2021 Honda Civic.

The initial response was incredibly encouraging. I’m writing to give a project update.

Keys to the Kingdom[#](https://juniperspring.org/posts/honda-evil-valet/#keys-to-the-kingdom)
---------------------------------------------------------------------------------------------

The biggest progress has been made while mapping out the update process.

Honda supports updating the headunit via USB. There are a number of Honda-specific checks, but ultimately the USB drive contains a signed AOSP update file that gets staged and applied via Android recovery. The good news? They left the publicly-known AOSP test key in `res/keys`\*, and, even though they modified the `recovery` binary, the `verify_file` signature logic matches stock AOSP.

So as long as you can properly format a USB drive and sign it with the publicly-known AOSP test key, you can install whatever you want to the headunit, without conventional root access (no need for `su` with `setuid`).
This means that, as long as the headunit has power and an attacker has physical access to the front-most USB port,
they have arbitrary code execution on the headunit via the update path.

This is an evil maid attack. Since it requires physical access to the cabin of the car rather than the hotel room, I call it an evil valet attack. Imagine a journalist drives to a hotel and leaves their car with the valet. The valet, who works for a three-letter agency, installs an update via USB. When the car is returned, the journalist doesn’t know the headunit has been modified. Since I want a cool vulnerability name, I’m calling this “EvilValet”.

This blog article is not intended as a technical writeup. If you want the gory details, see the technical docs.

I’ve also published a new tool, ota-builder, that allows people to easily prepare update files that will be accepted by the headunit. While in its early days, it should be trivial to now build an update file that, for example, installs an `su` binary with `setuid` set (i.e., to root the device).

\*I have strong reason to believe that all updates are signed with the publicly-known AOSP test key, but I don’t have access to every possible official update file, nor access to every headunit variant and its filesystem. My headunit has the AOSP test key in `res/keys`, though I’ve also installed HondaHack, so it’s possible that it injected the key into the keystore. However, I’ve also confirmed that `MRC_EU_SW_v12_4.zip`, a publicly-available EU software update file, is test key signed. This file was downloaded from a public forum and was never modified by me. So it seems highly likely that all updates are signed with the AOSP test key. Contributors are welcome to help support or refute this hypothesis.

Beyond the update process, the most useful work has been on apk-rebuilder. It has one very important job: take in a Honda Civic update file from the Internet, and produce a clean tree of output files that automates everything a reverse engineer would otherwise have to do manually, including:

* Resolving resources
* Reconstructing .smali code
* Repacking APK files
* Extracting the ramdisk
* And more

This also serves an important role because we can’t publish actual Honda source code. We publish a function that takes in an update file (that we don’t host) and spits out Honda .smali code, image assets, etc. The resulting output follows a clear directory structure that can be referenced in documentation without actually uploading the sensitive files themselves.

Outstanding Work - A Call for Contributors[#](https://juniperspring.org/posts/honda-evil-valet/#outstanding-work---a-call-for-contributors)
-------------------------------------------------------------------------------------------------------------------------------------------

There are a few outstanding things that would be nice to have.

### Known Versions[#](https://juniperspring.org/posts/honda-evil-valet/#known-versions)

The update process is fragile and relies heavily on version numbers. This doesn’t limit the ability to run unsigned code, because the version numbers can be “spoofed” (see the technical docs). But in order to build an update file in the first place you need to know what versions your headunit expects. Further, any changes to the headunit software that don’t match my build could lead to unexpected behavior and recovery loops.

If you drive a 10th gen Honda Civic and are tech-savvy, I encourage you to contribute to the “Known Versions, Display Audio Software” section of the repo.

If you’re feeling particularly brave, read through the `ota-builder` code and try and flash an update. But do so at your own risk; if your headunit differs from mine you could get stuck in a recovery loop and softbrick your device.

I have an experimental/work-in-progress toolchain on my local machine. It takes candidate .c code and compiles it for ARMv7, using the same compiler version and build flags as the original vendor binaries. This proved indispensable in my work to understand the update process. It makes heavy use of Docker. The current iteration is messy and largely specific to my workflow, but I’d like to publish a clean implementation.

### Custom Themes[#](https://juniperspring.org/posts/honda-evil-valet/#custom-themes)

I explored this a bit while vibe-coding apk-renderer. Custom themes are likely difficult to ship because they live in Mitsubishi’s fork of the AOSP framework,
and the headunit apps are minified to expect hardcoded resource IDs. Any attempt to ship a custom theme would likely involve surgically editing the vendor framework (and writing a tool to do so automatically).
None of this is trivial and probably isn’t worth the effort, but I welcome contributors.

### Improve aidl-rebuilder[#](https://juniperspring.org/posts/honda-evil-valet/#improve-aidl-rebuilder)

I started working on a tool to parse .smali files and generate/map out all AIDL interfaces on the headunit. This works but I haven’t reviewed it fully for accuracy. This opens up the door for custom apps such as virtual speedometers. Contributors welcome.

Thoughts on Documentation and LLMs[#](https://juniperspring.org/posts/honda-evil-valet/#thoughts-on-documentation-and-llms)
---------------------------------------------------------------------------------------------------------------------------

I’ve placed less emphasis on reference documentation and more on tooling. The idea is that if I can ship reliable, deterministic tools that map the headunit code to more digestible forms, then people can use LLMs to query those more digestible forms to answer whatever their specific questions are. This avoids having to maintain reference docs that can stray from the actual headunit code, because the headunit code is the source of truth.

For example, a user guide that explains how to connect to the headunit via ADB is still deemed useful. But a document explaining how some Java code works, when the Java code itself is available to an LLM, seems like a maintenance burden.

Wrapping up and Thanks[#](https://juniperspring.org/posts/honda-evil-valet/#wrapping-up-and-thanks)
---------------------------------------------------------------------------------------------------

At this point, I’ve done most of the investigative work I intend to do on the headunit.
This is one of those projects that I could toil endlessly on, but I’ll likely transition to other projects.
That said, the repo is by no means abandoned. PRs are always welcome.

Special thanks to Tunas for the memories, and to Hackaday for covering my original work.

See everyone sometime down the road 🌱

Eric