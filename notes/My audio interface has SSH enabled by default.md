---
title: "My audio interface has SSH enabled by default"
url: https://hhh.hn/rodecaster-duo-fw/
clipped: 2026-06-17 01:12:26
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [My audio interface has SSH enabled by default](https://hhh.hn/rodecaster-duo-fw/)

## Digest Summary
The author examined a RODECaster Duo audio interface and discovered that its firmware can be captured and updated without signature verification. Using macOS Instruments, they located a gzipped tarball containing the device’s binaries and a shell script for updates; the device employs two boot partitions for redundancy. SSH is enabled by default, restricted to public‑key authentication, with two RSA and two Ed25519 keys pre‑installed. By connecting via Ethernet, the author accessed a root shell (kernel 5.10.17‑rt32‑yocto‑preempt‑rt‑rode, aarch64). Firmware updates are triggered over HID: sending ASCII ‘M’ puts the device in update mode, then a tar.gz archive and its MD5 checksum are copied to the exposed disk, followed by ‘U’ to flash and reboot. The lack of signature checks allowed the author to build a custom firmware image that enables password authentication and adds their own key, then flash it using the same HID sequence. They reported the issue to RODE but received no response.

## Discussion Summary
Comments express amazement that firmware can now be inspected and modified quickly with accessible tools, praising the openness of a simple tarball‑plus‑hash firmware format and wishing more devices were similarly open. Several remarks appreciate the detailed write‑up and the technical community behind it, while also noting nostalgia for older hardware architectures. Concerns arise about potential manufacturer lock‑downs, legal scrutiny and the implications of public disclosure, with some users seeking practical solutions for their own audio‑interface issues. Overall, the tone is supportive of openness but cautious about possible repercussions.

---

## Full Article

last year i bought a [Rodecaster Duo](https://rode.com/en-us/products/rodecaster-duo) to solve some audio woes to allow myself and my girlfriend to have microphones to our respective computers when gaming together and talking on discord in the same room without any echo, and to be able to swap that to my work pc easily. the rodecaster is really nice, it's pretty effortless to use and works great for our home. I would gladly recommend it to anyone looking for a similar solution.

as is usual for any device in my house, i try to ensure when it's time to update the firmware I have enough tooling in place to capture how firmware updates work, or to at a minimum capture a firmware blob to try and reverse engineer it and poke around for fun and/or to see the often horrific reality that is the industry we work in.

### fw update

I was feeling pretty lazy and assumed that rode would dump the firmware somewhere on my computer before flashing the device, so i set up Instruments on macos to capture disk activity, and found where the fw was dumped, and surprisingly it was just a gzipped tarball. The device I did this update on happened to have the ability to write to USB disks disabled, so the update actually failed.

Poking around a bit, i found the binaries of the stuff that actually runs on the device, as well as a shell script that handles the updates themselves. there are two partitions on the disk, so that if you brick one it boots from the other. It also doesn't have any signature checks or anything on the incoming firmware. I'm used to *many* vendors of this style of device requiring signed firmwares or something nowadays, kind of nice to actually own a device I can modify. I also noticed that ssh seemed to be enabled by default, and plugged in an ethernet cable and saw that ssh indeed is enabled w/ pubkey auth only. Here are the keys that are added by default:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCX/bCFTDgViuPvdFL/VMMVRrw9b5S8HcDQk17qoCEYwmI+IIG8rEAsLiaeCOwyhf9IN+8/LRaN0Z5ZfU3WMbmsKEg8zd1Yvqq74nFbhO47vbtzmCi9S4ucIKkBEVOyvyN5lt9hWf5t5nZSmlfldZK3Pem5y8wHM5A+K/gSnzp4gwQ1QYfFb068uQ+ciIdOhb8SkUs8CwzotglIbp19I6ZmXmsNj/TmpbUf5rMfUAf1gysZ5j1UdRWrvWVh5daqvZRsBBPbXEeJfDU3Nr3HR14XYt9mgexrz/5oyKSj/lQYLmh9cDfsxvkGNIQ8fF9l+n2L1KZM4lLgiGk4KFBjQHaIBZx9OebCiiZCO4NTJUBDk9a+SZpiDiipADV07s7vTInYyFA6GrmKtnq3M6upT4WJBvVuL/BMnK5yY1RZtoqox2/pcCg2rH5S1GIy0v0HFJisl7kWInlaG2mdsaCx19wAjCFe/qT9LyxjQ6+0rArI55/JJFDkNeMjrewRQwNdASjCox8vqXCBfjvsR9qv70/ywcymgsnLAnq2LuYg5FYwMMDYOvVnhACC+BYTdNDTn5oeMIjQCUenY/DPCHpJkf4YOf3YCMUTEU9tExhtwW/X+m21hS3+STLtTfqbUeg9CeuPQZgfl9vc65n3tMxAdlEGEDoTaNMAgr2TzJv92Ka9iQ==
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDaNyzPfIcEeQsfzyQs/wyX6mX52kiS+4eNHfCaxFlgj
```

since our update failed, i swapped to a windows pc and set up wireshark with USBPcap and then ran the update thru the rodecaster app. I roughly glanced at the pcap file and looked at where the update started, since it was a lot of traffic as I was also using it for audio on another computer. I wrote down the packet numbers I thought were interesting and threw them to claude code to dig thru the pcap while I was doing other stuff.

A bit later (cc only took 10 minutes or so but I was busy for a while) I came back to a breakdown of the structure, and a python script to manually update a device. The RODECaster App sends some HID control stuff to the device, one command to enter the update mode ([the 'M' command](https://gist.github.com/nicewrld/1e06ec264556b1148eea0323ea9db93b)), and then another ([the U command](https://gist.github.com/nicewrld/c9e67acfdc88ac5dd4bfca4390ae0921)) to trigger the update. Both are just single ASCII characters sent over [HID report](https://docs.kernel.org/hid/hidintro.html) 1.

I am but a yaml-writing slave and sometimes a below-average ghidra user, and don't often interact with hardware devices, so getting some help from CC in discovery was useful, as well as pointing me to resources to actually learn more about hid devices.

The structure was pretty simple, you send the m command, and then copy archive.tar.gz and archive.md5 (obviously just with md5sum of the archive) onto the newly exposed disk. then you send the U command to trigger the flashing itself.

so the flow is:

1. plug in the rodecaster and power it on (or vice versa)
2. send the 'M' command
3. mount the disk and copy `archive.tar.gz` and `archive.md5` to it
4. chmod 777 both of them because i dont care to figure out how to do it properly
5. unmount the disk
6. send the 'U' command
7. wait for the thing to reboot into your new firmware

### custom firmware

I was still working from my mac, and wanted to create some cfw to be able to ssh into the device, so i just [used a container](https://gist.github.com/nicewrld/2d45e7a4f8b18ae9a9d5288b3fec8720) to enable password authentication for ssh (don't shoot me) as well as add my own pubkey to the authorized keys, and dump out an archive for me to flash. you don't really need much to actually flash the device, see [here](https://gist.github.com/nicewrld/5773f284ae3f5d548fc00659323f63d8) (example of the functions its not really much to add the rest.)

run your script to flash the thing and bingo bongo you can ssh to it

### conclusion

I was really surprised that I could actually flash firmware so easily to this, and it is really nice to own a device. It's a really nice piece of kit and just kinda blends into the background and I never have to think about it. I don't really know why ssh was enabled, or why it had this key added by default, but I submitted a ticket to RODE for this as I could not find an obvious security email to report to. I did not hear back, but I will watch to see if future firmware updates change anything.

It's been a few months since i've done anything with this, and I am trying to just dump out my thoughts into a notepad and only very lightly edit it and then just poast. I really love all of the RODE stuff I have, and yet again just want to buy more gear.

if you want to ask me questions about this or have any questions, you can reach me with the primary letter of this domain, at this domain.

thanks computer, until next time