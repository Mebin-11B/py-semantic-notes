---
title: "Defeating a 40-year-old copy protection dongle"
url: https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle
clipped: 2026-06-17 01:49:39
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Defeating a 40-year-old copy protection dongle](https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle)

## Digest Summary
The article describes reverse‑engineering a parallel‑port copy‑protection dongle used by a 1990s RPG II compiler (RPGC.EXE) and its associated tools (SEU.EXE) for an accounting package running on Windows 98/DOS. The dongle, marked “Software Security Inc.” and “RUNTIME”, is required by the compiler, which embeds the same protection routine into every compiled executable. Disassembly with Reko revealed a 0x90‑byte routine in segment 0800 that performs IN/OUT operations on the LPT1 port, accumulates responses in BH and BL, and returns a constant value in BX. Since the routine takes no input, the result is fixed; BH is hard‑coded to 0x76, leaving BL as the only variable. Brute‑forcing BL (0–255) via a script in DOSBox identified the correct value (0x06), making the magic number 0x7606. Patching the first four bytes of the routine to “MOV BX,7606h; RETF” bypasses the dongle check for all compiler executables, enabling compilation and execution of the legacy RPG software without hardware. The author plans to release the patched compiler as a historical artifact.

## Discussion Summary
The discussion reflects a nostalgic but pragmatic view of legacy hardware dongles, noting their simple design and the ease with which they were historically cracked, while recognizing that some users still prefer tangible protection over cloud‑based licensing. Commenters highlight the challenges of maintaining obsolete dongle‑dependent systems, the business incentive for perpetual licenses and vendor lock‑in, and concerns about legal risks of reverse‑engineering old software. Technical details about emulation and patching are shared, and there is general agreement that modern licensing has largely moved beyond such rudimentary mechanisms.

---

## Full Article

![image](https://dmitrybrant.com/images/20260105204922.jpg)

That’s right — this little device is what stood between me and the ability to run an *even older* piece of software that I recently unearthed during an expedition of software archaeology.

For a bit more background, I was recently involved in helping a friend’s accounting firm to move away from using an *extremely* legacy software package that they had locked themselves into using for the last four decades.

This software was built using a programming language called [RPG](https://en.wikipedia.org/wiki/IBM_RPG) (“Report Program Generator”), which is older than COBOL (!), and was used with IBM’s midrange computers such as the System/3, System/32, and all the way up to the AS/400. Apparently, RPG was subsequently ported to MS-DOS, so that the same software tools built with RPG could run on personal computers, which is how we ended up here.

This accounting firm was actually using a Windows 98 computer (yep, in 2026), and running the RPG software inside a DOS console window. And it turned out that, in order to run this software, it requires a special hardware copy-protection dongle to be attached to the computer’s parallel port! This was a relatively common practice in those days, particularly with “enterprise” software vendors who wanted to protect their very important™ software from unauthorized use.

![image](https://dmitrybrant.com/images/20260105204921.jpg)

Sadly, most of the text and markings on the dongle’s label has been worn or scratched off, but we can make out several clues:

* The words “Stamford, CT”, and what’s very likely the logo of a company called “Software Security Inc”. The only evidence for the existence of this company is this record of them exhibiting their wares at [SIGGRAPH conferences](https://history.siggraph.org/exhibitor/software-security-inc/) in the early 1990s, as well as several [patents](https://patentimages.storage.googleapis.com/e6/69/0e/9f00041c0a3840/US5337357.pdf) issued to them, relating to software protection.
* A word that seems to say “RUNTIME”, which will become clear in a bit.

My first course of action was to take a disk image of the Windows 98 PC that was running this software, and get it running in an emulator, so that we could see what the software actually does, and perhaps export the data from this software into a more modern format, to be used with modern accounting tools. But of course all of this requires the hardware dongle; none of the accounting tools seem to work without it plugged in.

Before doing anything, I looked through the disk image for any additional interesting clues, and found plenty of fascinating (and archaeologically significant?) stuff:

![image](https://dmitrybrant.com/images/w98rpg.png)

* We’ve got a compiler for the RPG II language (excellent!), made by a company called Software West Inc.
* Even better, there are *two versions* of the RPG II compiler, released on various dates in the 1990s by Software West.
* We’ve got the complete source code of the accounting software, written in RPG. It looks like the full accounting package consists of numerous RPG modules, with a gnarly combination of DOS batch files for orchestrating them, all set up as a “menu” system for the user to navigate using number combinations. Clearly the author of this accounting system was originally an IBM mainframe programmer, and insisted on bringing those skills over to DOS, with mixed results.

I began by playing around with the RPG compiler in isolation, and I learned very quickly that it’s the RPG compiler itself that requires the hardware dongle, and then the compiler automatically injects the same copy-protection logic into any executables it generates. This explains the text that seems to say “RUNTIME” on the dongle.

The compiler consists of a few executable files, notably `RPGC.EXE`, which is the compiler, and `SEU.EXE`, which is a source editor (“Source Entry Utility”). Here’s what we get when we launch SEU without the dongle, after a couple of seconds:

![image](https://dmitrybrant.com/images/seu1.png)

A bit rude, but this gives us an important clue: this program must be trying to communicate over the parallel port over the course of a few seconds (which could give us an opportunity to pause it for debugging, and see what it’s doing during that time), and then exits with a message (which we can now find in a disassembly of the program, and trace how it gets there).

A great tool for disassembling executables of this vintage is [Reko](https://github.com/uxmal/reko). It understands 16-bit real mode executables, and even attempts to decompile them into readable C code that corresponds to the disassembly.

![image](https://dmitrybrant.com/images/rekorpg3.png)

And so, looking at the decompiled/disassembled code in Reko, I expected to find `in` and `out` instructions, which would be the telltale sign of the program trying to communicate with the parallel port through the PC’s I/O ports. However… I didn’t see an `in` or `out` instruction anywhere! But then I noticed something: Reko disassembled the executable into two “segments”: `0800` and `0809`, and I was only looking at segment `0809`.

![image](https://dmitrybrant.com/images/rekorpg2.png)

If we look at segment `0800`, we see the smoking gun: `in` and `out` instructions, meaning that the copy-protection routine is definitely here, and best of all, the entire code segment is a mere 0x90 bytes, which suggests that the entire routine should be pretty easy to unravel and understand. For some reason, Reko was not able to decompile this code into a C representation, but it still produced a disassembly, which will work just fine for our purposes. Maybe this was a primitive form of obfuscation from those early days, which is now confusing Reko and preventing it from associating this chunk of code with the rest of the program… who knows.

Here is a GitHub Gist with the [disassembly of this code](https://gist.github.com/dbrant/1d1a9ba2a2a41d5ba7be50ccb3d36d6c), along with my annotations and notes. My x86 assembly knowledge is a little rusty, but here is the gist of what this code does:

* It’s definitely a single self-contained routine, intended to be called using a “far” `CALL` instruction, since it returns with a `RETF` instruction.
* It begins by detecting the address of the parallel port, by reading the [BIOS data area](https://wiki.osdev.org/Memory_Map_(x86)#BIOS_Data_Area_(BDA)). If the computer has more than one parallel port, the dongle must be connected to the *first* parallel port (LPT1).
* It performs a loop where it writes values to the data register of the parallel port, and then reads the status register, and accumulates responses in the `BH` and `BL` registers.
* At the end of the routine, the “result” of the whole procedure is stored in the `BX` register (`BH` and `BL` together), which will presumably be “verified” by the caller of the routine.
* Very importantly, there doesn’t seem to be any “input” into this routine. It doesn’t pop anything from the stack, nor does it care about any register values passed into it. Which can only mean that the result of this routine is *completely constant*! No matter what complicated back-and-forth it does with the dongle, the result of this routine should always be the same.

With the knowledge that this routine must exit with some magic value stored in `BX`, we can now patch the first few bytes of the routine to do just that! Not yet knowing which value to put in `BX`, let’s start with 1234:

```
BB 34 12       MOV BX, 1234h
CB             RETF
```

Only the first four bytes need patching — set `BX` to our desired value, and get out of there (`RETF`). Running the patched executable with these new bytes still fails (expectedly) with the same message of “No dongle, no edit”, but it fails immediately, instead of after several seconds of talking to the parallel port. Progress!

Stepping through the disassembly more closely, we get another major clue: The only value that `BH` can be at the end of the routine is 76h (this is hard-coded into the routine). So, our total value for the magic number in `BX` must be of the form 76xx. In other words, only the `BL` value remains unknown:

```
BB __ 76       MOV BX, 76__h
CB             RETF
```

Since `BL` is an 8-bit register, it can only have 256 possible values. And what do we do when we have 256 combinations to try? Brute force it! I whipped up a script that plugs a value into that particular byte (from 0 to 255) and programmatically launches the executable in DosBox, and observes the output. Lo and behold, it worked! The brute forcing didn’t take long at all, because the correct number turned out to be… *6*. Meaning that the total magic number in `BX` should be 7606h:

```
BB 06 76       MOV BX, 7606h
CB             RETF
```

![image](https://dmitrybrant.com/images/seu2.png)

Bingo!  
And then, proceeding to examine the other executable files in the compiler suite, the parallel port routine turns out to be *exactly the same*. All of the executables have the exact same copy protection logic, as if it was rubber-stamped onto them. In fact, when the compiler (`RPGC.EXE`) compiles some RPG source code, it seems to copy the parallel port routine from itself into the compiled program. That’s right: the patched version of the compiler will produce executables with the same patched copy protection routine! Very convenient.

I must say, this copy protection mechanism seems a bit… simplistic? A hardware dongle that just passes back a constant number? Defeatable with a four-byte patch? Is this really worthy of a patent? But who am I to pass judgment. It’s possible that I haven’t fully understood the logic, and the copy protection will somehow re-surface in another way. It’s also possible that the creators of the RPG compiler (Software West, Inc) didn’t take proper advantage of the hardware dongle, and used it in a way that is so easily bypassed.

In any case, Software West’s RPG II compiler is now free from the constraint of the parallel port dongle! And at some point soon, I’ll work on purging any PII from the compiler directories, and make this compiler available as an artifact of computing history. It doesn’t seem to be available anywhere else on the web. If anyone reading this was associated with Software West Inc, feel free to get in touch — I have many questions!