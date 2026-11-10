---
title: "OpenBSD on Motorola 88000 Processors"
url: http://miod.online.fr/software/openbsd/stories/m88k1.html
clipped: 2026-06-17 01:25:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [OpenBSD on Motorola 88000 Processors](http://miod.online.fr/software/openbsd/stories/m88k1.html)

## Digest Summary
The Motorola 88000 (m88k) was a short‑lived RISC family (≈1988‑1994) intended to replace the CISC 68000 line. The first generation used an 88100 CPU with optional external 88200 CMMU chips that provided cache and MMU functions on a shared P‑Bus, enabling automatic cache coherency and flexible multi‑processor designs. Speeds ranged from 16 MHz to 33 MHz. The second generation integrated cache and MMU into the 88110 core, targeting 50–100 MHz, but suffered reliability problems; production ceased when Motorola shifted to PowerPC development. Few vendors adopted m88k, notable users being Data General’s AViiON workstations, which later moved to Intel CPUs.

Operating systems for m88k were proprietary (Motorola’s AT&T System III/V, Data General’s DG/UX, Omron’s UniOS) and a research copy of CMU Mach, whose source enabled an OpenBSD port. Nivas Madhur introduced OpenBSD/mvme88k in 1995, but the project stalled after his departure. Steve Murphree revived it (1998‑1999), delivering a functional kernel and userland, though compiler support was problematic: GCC 2.8 could compile, but GCC 2.95 failed to build itself for m88k, forcing continued use of the older compiler with optimizations disabled. Subsequent development faced hardware issues (SCSI termination, board instability) and required extensive manual configuration to achieve a usable OpenBSD system on MVME 187/188 boards.

## Discussion Summary
The comment reflects a personal history with the 88000 reference manuals, noting that they served as an early introduction to RISC architecture and were regarded positively. It expresses curiosity about why Apple has not selected the 88000 design for its CPUs, indicating an interest in the factors influencing corporate processor choices without providing specific conclusions. The overall tone is inquisitive and appreciative of the architecture’s educational value.

---

## Full Article

(Follow [this link](http://miod.online.fr/software/openbsd/stories/m88k.html) to go back to the main m88k page.)

PART 1: The Forsaken RISC Architecture
======================================

No, it's no typo
----------------

Many people know, or have heard of, the
[Motorola](https://en.wikipedia.org/wiki/Motorola)
[68000](https://en.wikipedia.org/wiki/Motorola_68000_series)
architecture. These processors have been used in many machines:
in the first generations of
[Apple Macintosh](https://en.wikipedia.org/wiki/Mac_(computer))
computers, in the ever-rivals
[Amiga](https://en.wikipedia.org/wiki/Amiga)
and
[Atari ST](https://en.wikipedia.org/wiki/Atari_ST) home computers,
in many workstations
built by
[Sun](https://en.wikipedia.org/wiki/Sun_Microsystems),
[HP](https://en.wikipedia.org/wiki/Hewlett-Packard)
and
[NeXT](https://en.wikipedia.org/wiki/NeXT)
(to name only a few), but also in many industrial
systems and boards built by
Motorola,
[Tadpole](https://en.wikipedia.org/wiki/Tadpole_Computer),
[Heurikon](https://en.wikipedia.org/wiki/Heurikon)
or
[Performance Technologies](https://en.wikipedia.org/wiki/Performance_Technologies)
(to name only a few.)

The 68000 architecture has been very successful, but due to its
[CISC](https://en.wikipedia.org/wiki/Complex_instruction_set_computer)
nature with
complex addressing modes and many instructions, Motorola was not able to keep
up in the speed competition.

In order to be able to deliver performance and megahertz, another processor
architecture was needed, one which could scale more easily.

At this point you're probably expecting me to write about the
[PowerPC](https://en.wikipedia.org/wiki/PowerPC),
which also turned out to
be a successful architecture, used in the next generations of Apple Macintosh
computers, in workstations (from
[IBM](https://en.wikipedia.org/wiki/IBM)
and
[Bull](https://en.wikipedia.org/wiki/Groupe_Bull), mostly),
and in the iconic
[BeBox](https://en.wikipedia.org/wiki/BeBox).

But between the 68000 and the PowerPC, there's the black
sheep of the family.
A processor architecture which made a lot of promises, but did
not deliver them, and was destined to be
[consigned to
oblivion](https://en.wikipedia.org/wiki/Consign_to_Oblivion),
as if it had been a bad dream.

That processor architecture is the Motorola
[88000](https://en.wikipedia.org/wiki/Motorola_88000)
architecture, or m88k for short.

m88k in a nutshell
------------------

There have been two generations of 88000 processors before Motorola reassigned
all its engineers to the PowerPC.

The first generation consists of the
[88100](https://en.wikipedia.org/wiki/Motorola_88100)
CPU, with optional external
88200
so-called CMMU:
a chip which provides both cache memory and memory management facilities.
The choice of separate chips allowed designs which did not need an
[MMU](https://en.wikipedia.org/wiki/Memory_management_unit)
to be completed quickly and cheaply, and
[NCD](https://en.wikipedia.org/wiki/Network_Computing_Devices)
used the 88100 a lot in its
[X terminals](https://en.wikipedia.org/wiki/X_terminal) line
for that reason.

All the CMMUs sit on the same so-called P-Bus with the processor, and
work closely with it to perform their duties. And by the virtue of sharing that
bus, they can monitor each other to achieve automatic cache coherency
across processors. Moreover, they can also make themselves visible to all
processors, as they answer to specific commands on dedicated address ranges:
this allows a given processor to perform a cache invalidation or any MMU
operation on behalf of another processor (by sending commands to the CMMUs
associated to that processor)
without needing to interrupt that processor.
This makes multiprocessor implementation, from a software point of view,
much easier than on more classical architectures.

Another perceived advantage of these separate components, is
that depending upon your needs for cache memory, it is possible to use more
than one 88200 chip per processor. In fact, while the basic designs would use
two (one for instruction cache, one for data cache),
higher performance designs could use up to eight such CMMU companions
(having more than eight, in addition to becoming a serious board space problem,
would also cause bus latency and signal strength problems, as all the chips had
to be connected to the same high-speed P-Bus.)
This limited the speed at which the 88100 and 88200 chips could run; and they
were built in speeds ranging from 16MHz to 33MHz, most of them being 25MHz
parts.

The second generation tries to learn from the 88100 drawbacks and reverts to a
more traditional architecture, bringing back the cache and MMU into the
[88110](https://en.wikipedia.org/wiki/Motorola_88110)
processor (and, for systems programmers, a much simpler exception model.)
Initially supposed to run at 50MHz, with the aim of
reaching 100MHz in the future, these processors suffered from hardware problems,
and for a while, none of the early 50MHz processors would run reliably at that
speed, and had to be sold as 40MHz parts, a speed at which they did not
misbehave *that* much...

Even though these defects were eventually fixed, and parts running faster than
50MHz even started to get produced (there is evidence of existing 60MHz chips),
Motorola was more than happy to pull the plug when IBM knocked on its door
asking for help with the PowerPC project, leading to the short-lived
[AIM](https://en.wikipedia.org/wiki/AIM_alliance)
(Apple, IBM, Motorola) alliance.

Some parts of the 88110 design made their way to the first PowerPC processors,
in particular the external busses of the PowerPC 601 are very similar to those
of the 88110.

m88k hardware
-------------

Because of its short lifespan (roughly, 1988-1994) and, for the first
generation, system design complexity, the 88000 architecture did
not convince many hardware companies to build their systems on this
architecture.

To this day, there isn't much information left about these systems.
**Paul Weissmann** of
[OpenPA](https://www.openpa.net/) fame, had started a similar,
but less ambitious, effort to document the m88k ecosystem, as
"badabada". This site is no longer online, but there is a mirror of the
last version of that site
[on
the Internet Archive](http://web.archive.org/web/20111011081627/http://badabada.org:80/),
as well as on the current incarnation of the
[m88k.com](https://m88k.com/orig/) website.

The most well-known users of these processors were:

* [Data General](https://en.wikipedia.org/wiki/Data_General)
  chose to use the 88100 (and later the 88110) for its
  [AViiON](https://en.wikipedia.org/wiki/Aviion)
  workstation line, but switched to
  [Intel](https://en.wikipedia.org/wiki/Intel)
  [Pentium](https://en.wikipedia.org/wiki/Pentium_(original))
  processors after Motorola stopped producing 88000 processors.

  [![](http://miod.online.fr/software/openbsd/stories/t_av300_open.jpg)](http://miod.online.fr/software/openbsd/stories/av300_open.jpg)

  AViiON 300 pizza box, open (click for a larger picture.)

  Note how the memory modules are put in a reclined position,
  in order to keep the height small enough.

  ![](http://miod.online.fr/software/openbsd/stories/av400_front.jpg)

  AViiON 400 deskside, front.

  (Picture by Chris Tribo)

  Note the metal feet which double the ground surface of the system.

  There is a large fan tray at the bottom of the chassis, these
  feet made sure the fans would not get obscured.

m88k operating systems
----------------------

Motorola used its own version of
[AT&T](https://en.wikipedia.org/wiki/Bell_Labs) Unix
[System III](https://en.wikipedia.org/wiki/UNIX_System_III),
then later
[System V](https://en.wikipedia.org/wiki/UNIX_System_V), on
its VME boards line. Data General used its own
[DG/UX](https://en.wikipedia.org/wiki/DG/UX)
flavour of Unix. Omron had
a BSD-based flavour called UniOS.

All these systems were proprietary, with little or no diffusion of their source
code.

However, CMU Mach, being a research operating system, had most of its source
code available under a free license (a few parts, such as the IBM
[RS/6000](https://en.wikipedia.org/wiki/IBM_RS/6000)
port,
were encumbered due to the reuse of proprietary source code, and are probably
lost nowadays - I spent some time in the early 2000s to track that particular
code down, to no avail.)
  
*(If you happen to have a copy of that source code, or know more about its
whereabouts, please get in touch with me!)*

The existence of the CMU Mach code for the Luna-88K allowed a Motorola employee,
**Nivas Madhur**, to port OpenBSD to the MVME187 in 1995,
and this is how the m88k story in OpenBSD started.

If that port had not existed, the m88k architecture would probably be even less
known today.

OpenBSD/mvme88k, the early days
-------------------------------

Nivas Madhur's code was imported in OpenBSD shortly after the creation of the
OpenBSD source code repository, in october 1995.

But Madhur did not have time to work in OpenBSD, and when he left Motorola
some time later, there was noone left to take care of the port. Before he left,
he shared his latest code with
**Dale Rahn**, who was taking care of the
[mvme68k](https://www.openbsd.org/mvme68k.html)
port to the 68000-based Motorola VME cards, as these boards had everything in
common, but the processor.

Rahn intended to replace the existing
[OpenBSD/mvme88k](https://www.openbsd.org/mvme88k.html)
code with that new
version, but would not have time and resources to maintain the port after that.

The kernel was taken care of on march 3rd, 1996 in two commits.
  
[First
commit:](https://github.com/openbsd/src/commit/be4a5d153bc5792d6fa724f2f244dd83a1b58a73)

```
Third try at importing the mvme88k port. This is a working kernel
from nivas.
Userland and compiler still need to be worked on.
Make certain what directory the import is done from.
```

[Second
commit:](https://github.com/openbsd/src/commit/127f0020bfe7e3c1b6465fa9faaf93e481387e83)

```
Cleanup after import. This also seems to bring up the current version.
```

...and userland was taken care of
[on march 25th.](https://github.com/openbsd/src/commit/7f7ae0fd385af19d2c0439d121453b7fd9e658d1)

```
Ok here is the mvme88k userland, minus a few important pieces.
as, ld change need to be merged. It is known that shared libraries and C++
do not work.
If anyone wants to step forward and take over the mvme88k port please do.
It was dumped on me when the original developer, Nivas, left his previous
job and started a new one.

I am trying to get the port in a shape that someone could take over.
```

The kernel was a potpourri of bits and pieces taken from everywhere:

* the m88k-specific parts were taken from CMU Mach.
* the onboard devices drivers were taken from OpenBSD/mvme68k...
* ...which in turn had borrowed some parts, such as the SCSI controller driver, from the
  [NetBSD/amiga](https://wiki.netbsd.org/ports/amiga/) port.

---

Not much happened until august 1998, where
**Steve Murphree, Jr.**,
started to take over the port and make it a reality.

On november 1st, he fixed a severe bug in the
[the
encoding of the xcr instruction](https://github.com/openbsd/src/commit/5c9b75c33110e67fac7c3402d6f041770486fccf)
in the assembler.

Unfortunately, Murphree was the kind of developer who is working on his own for
a while, appears to dump all his work on the tree in a few commits, mixing
unrelated changes, and disappears again for a while. This was fine as long as
he was the only one working on mvme88k, but that would not work on the long
term.

In december 1998, he reached a state where the system was running stably and
able to recompile most of itself. The last missing part, configuration
directives for the compiler (at that time gcc 2.8.1), were committed on february
1999.

On february 15th, he completed an OpenBSD/mvme88k snapshot build. This was the
first OpenBSD/mvme88k snapshot ever successfully built, and would be the last
one for more than four years, although noone could have known this yet.

On may 26th, **Marc Espie** would update the system compiler to the may 17th
snapshot of EGCS, which was becoming close to being the future gcc 2.95.

More updates followed in june and july, until august 23rd, when the official
gcc 2.95.1 release was imported.

A note about EGCS and GCC:

---

If you don't know, or don't remember, that part of GCC history, the development
of GCC, in the 2.x series, had become more and more conservative, and GCC
remained "stuck" at the 2.7.2.1 version for years, and only released the 2.8
version under the pressure of C++ developers and users, who needed the better
C++ support provided by GCC 2.8.

At the same time, several groups formed in
order to improve on GCC, with a strong focus on better optimizations in order
to make better use of modern hardware. The largest of these groups was the
"Pentium GCC" group, who did a lot of work on the i386 backend for the
Intel 80386 family.

Eventually, all the groups merged together and released
what was called EGCS, the Experimental GNU Compiler System (pronounced "eggs".)

There was some friction between GCC and EGCS, but then, given the much
better dynamic of EGCS, the
[FSF](https://en.wikipedia.org/wiki/Free_Software_Foundation) decided
to stop the development of GCC and appoint EGCS as the new GCC, and what
should have been EGCS 1.2 was released as GCC 2.95.

---

Unfortunately, this compiler update broke on mvme88k - the 2.8
compiler was already known to not always produce correct code, and compiler
optimization had to be disabled when targeting mvme88k, but 2.95
had reached a state where it could not even recompile itself, even with
optimization disabled.

Because of this, Murphree kept working on the port, but still using the 2.8
compiler, and disabling the build of the new compiler, until he could either
get help or figure out himself how to fix gcc.

---

That setback also made him concentrate on other parts of the OpenBSD tree, and
he contributed support for the
[68060](https://en.wikipedia.org/wiki/Motorola_68060)-based
MVME172 and MVME177 boards to the OpenBSD/mvme68k port in early 2000.
He also took over maintainance of the
[ahc](https://man.openbsd.org/ahc)
driver for the
[Adaptec](https://en.wikipedia.org/wiki/Adaptec)
AIC-78xx
[SCSI](https://en.wikipedia.org/wiki/SCSI)
controller family that year in march.

---

My own path crossed the m88k later that year. I had been intrigued by
this port to an architecture I had not been aware of and, in september on
[IRC](https://en.wikipedia.org/wiki/IRC),
I "met" **Manuel Odendahl**, who was completing his computer science studies
in
[Karlsruhe](https://en.wikipedia.org/wiki/Karlsruhe),
[Germany](https://en.wikipedia.org/wiki/Germany),
and had made good contacts with people at
[JPAVES
Unix Online Gmbh](https://web.archive.org/web/20030812163945/http://www.jpaves.de/TEXT/),
a company selling Unix-related services, from development to support.
That company had a bunch of Motorola 88000 hardware which was being
decommissionned. He got me in contact with
Eckhard SchÃ¶nknecht at JPAVES, and I started organizing a trip to
Karlsruhe.

That trip was planned for early october, but got almost cancelled because there
were *(as usual...)* strikes in France happening at the same time, and the
gas depots were being blocked by truck drivers during the end of september.
The trip back and forth from my place was over 1300 km, there was no way I
could do it without having to refill a few times.
Fortunately for me, the strike ended just in time for me to be able to go on
the road without risking to run out of gas.

After meeting Manuel Odendahl at his parents place in
[Strasbourg](https://en.wikipedia.org/wiki/Strasbourg),
France, we drove to Karlsruhe to pick the seven MVME188 systems there.
The agreement between us was that I would bring three of them to Manuels' dorm
at
[Hadiko](https://www.hadiko.de/)
for him and the computer club he was part of,
and keep the remaining four for me (as well as a bunch of spare parts,
cables, etc.) And of course, because nothing but software is free in this
world, I was to pay JPAVES DM 1500 (about EUR 750)
for all that hardware.

OpenBSD developer **Christian Weisgerber**, who was living not far away,
joined us in Karlsruhe, albeit later than expected (the JPAVES offices were at
the western end of *Kaiserallee*, but he made a mistake and parked at the
eastern end of *KaiserstraÃe*, and had to walk much, much, much, much more
than he expected...) to help with moving the hardware.

I was however worried that I would need a MVME187 board in order to be able to
help the OpenBSD/mvme88k port, as this was the only board known to work at
the moment; so it was agreed that I also would get a MVME187 board in addition
to the seven ~~sins~~ chassis.

Thus, after collecting all the MVME188 gear, we drove with one of JPAVES's
employees to the guy's own place; he then went to his own machine room, logged
on a terminal, halted the operating system, powered down a small VME rack,
carefully removed a MVME187 board from it, and handed it to me.

This was an average 25MHz MVME187 board with 32MB of memory, which would
hopefully be good enough to get me started.

![](http://miod.online.fr/machineroom/years/2003/vmecage.jpg)

The MVME187 board mentioned above, along with a MVME177 board sporting a memory mezzanine, sharing a 3-slot VME chassis.
Due to the lack of proper disk spuds for that chassis, one
of the disks is simply put on top of a thick sheet of foam,
to insulate it from the chassis.

*(Not only did that board get me started, as you will see below,
but it was my main mvme88k workhorse for many years,
until I could replace it with a 33MHz board. To this day, I still
have this board, and occasionally run it for a test drive.)*

---

All I needed now was a way to setup that machine. For some reason, I had
completely missed the 2.5 binaries built by Steve Murphree (which were not
really the
[2.5](https://www.openbsd.org/25.html)
release but a 2.4-CURRENT snapshot close to the release cutoff.)

I kept asking him for a snapshot of recent binaries.

```
Date: Thu, 28 Dec 2000 23:57:58 +0000
From: Miod Vallat
To: Steve Murphree
Subject: m88k news ?

Hello,

  looking at source-changes, you've had some time to play with mvme88k
machines. That's wonderful !

  Do you think you'll have a snapshot (just base + comp + bsd will be
enough) for me soon ?

  I have a somewhat working mvme68k setup, so I should be able to create
a working, bootable disk in no time... I just need to populate it.

Cheers,
Miod
```

Murphree promised a snapshot for "the first weekend in Jan." Then other delays
prevented him to deliver anything.

Fortunately, I noticed the 2.5 bits some time later.

```
Date: Mon, 5 Feb 2001 22:27:24 +0000
From: Miod Vallat
To: Steve Murphree
Subject: I'm so stupid (mvme88k)

Hello,

  I just realized doing a ftp search that the 2.5/mvme88k snapshot was
still available from some places. I didn't found it on ftp.openbsd.org
when I got the m88k boxens because I naively was looking into
snapshots/, not a release directory. So I basically wasted my time while
I could manage to get something working on the mvme187, and upgrading to
-current myself.

  I'm fetching the files right now, will probably take some days (a few
hours each day, that is), but then I'll have something to play with if
your snapshot gets late.

Later,
Miod
```

(I was still using a
[dial-up Internet
connection](https://en.wikipedia.org/wiki/Dial-up_Internet_access)
at that time. A slow one, at 31.2Kbps,
as my phone line was not even stable at 33.6Kbps. Hence downloads of large files
such as OpenBSD snapshots would really take *hours* to complete.)

Since the MVME187 board I had been given did not have a recent PROM version, it
was lacking the network-related commands and could not netboot. I had to find
a way to setup a disk with mvme88k boot blocks and put the bsd.rd
installer in the root filesystem. (There was no miniroot ready-to-run
image you could simply dump on a disk using dd on another machine,
at that time, either.)

Thankfully, among the spare parts I had obtained from JPAVES, was a MVME147
board (25MHz 68030, 8MB of memory) with a fried Ethernet controller, which
could run OpenBSD/mvme68k. I had to configure networking using
[SLIP](https://en.wikipedia.org/wiki/Serial_Line_Internet_Protocol),
and it actually ran quite well that way until I could replace the board with
another similar MVME147 board in complete working condition, about one year
later.
  
I used it to setup the mvme88k disk. This was an easy task to do in theory, yet
it took me more time than expected due to SCSI termination problems:
the disk I intended to use for the MVME187 had termination resistors plugged
in, which I had not noticed; and of course I had put it before the mvme68k disk
in the SCSI chain, causing the machine to see the new disk to set up but no
longer see the disk to boot from, and I could not understand why.
It took me some time to notice the resistor pack beneath the disk.

A note about SCSI chain termination:

---

All SCSI devices are connected in a chain, with cables. Similarly to a 10base2
(BNC) network, the chain must be terminated with resistors at both ends.
Usually, one end of the chain is the SCSI controller found onboard the
computer, or in an expansion board, and it contains the proper termination
resistors.
  
The last device in the chain must take care of the termination; this can be done
either with a dedicated resistor pack, often used with external SCSI devices in
their own enclosurse, simply known as an "external SCSI terminator", or by
putting actual resistors on a reserved location on the last device.
  
In order to make people's lives simpler, these resistor packs were replaced with
simple configuration jumpers (in other words, the resistors were now always
present on the SCSI devices, and the jumper would control whether the SCSI chain
would pass through them or skirt them.)
  
When hotplugging capabilities were added to SCSI hardware, the high-end devices
could also work in an "automatic termination" mode, where they could detect if
they are the last device of the chain, and would automatically enable their
termination resistors in this case.
  
If, like me in the above scenario, you made the misake of putting termination
resistors in the middle of the chain, everything placed after the resistors will
become invisible to the SCSI controller.
So be careful when tinkering with multiple SCSI devices on old hardware!

---

```
Date: Fri, 16 Feb 2001 00:16:56 +0000
From: Miod Vallat
To: Steve Murphree
Subject: This damn mvme88k SBC works !

Hello,

  the 187 boots 2.5 bsd.rd fine. However, bsd panics (and has weird
behaviour before, such as not finding the ethernet address of the
built-in ie chip). So, I'm trying to build a -current kernel from 2.5
bsd.rd, under a chrooted envrionment.

  Of course, build fails )-:

  Tweaking -L args to ld makes the link phase work (i.e. libgcc.a is
found), and I'm going to test this kernel in a minute. Oh, BTW, is there
any reason to have twice -lgcc in the LD commandline in
arch/mvme88k/conf/Makefile.mvme88k ?

  Attached is the dmesg - seems there is some overlapping problem, which
makes me wonder if the msgbuf change from between 2.6 and 2.7 has been
made correctly for 88k... And the msgbuf seems too small to contain the
whole dmesg. Anyway, kernel is M187, not GENERIC.

  Okay, time to launch a make build on the box and have an up-to-date
userland. And after that, count me in for serious hacking on this arch !

Miod, happy

v=0x802
\^O\M-l\^D\M-lreal mem  = 33550336
avail mem = 28889088 (7053 pages)
using 435 buffers containing 1781760 bytes of memory
mainbus0 (root) machine type MVME187
bugtty0 at mainbus0 addr 0xfff45000: bugtty
pcctwo0 at mainbus0 addr 0xfff00000: rev 0
clock0 at pcctwo0 ipl 5: VME1x7
sclock0 at pcctwo0 ipl 5: VME1x7
nvram0 at pcctwo0 offset 0xc0000: MK48T08 len 8192
cl0 at pcctwo0 offset 0x45000 ipl 3 console
siop0 at pcctwo0 offset 0x47000 ipl 2: version 0 target 7
scsibus0 at siop0: 8 targets
siop0: target 0 now synchronous, period=100ns, offset=8
probe(siop0:0:0): Sense Error Code 0
sd0 at scsibus0 targ 0 lun 0: <CONNER, CFA540S, 0FAE> SCSI2 0/direct fixed
sd0: 510MB, 2800 cyl, 4 head, 93 sec, 512 bytes/sec, 1045242 sec total
vme0 at pcctwo0 offset 0x40000: vector base 0x80, system controller
vme0: using BUG parameters
vme0: 1phys 0x02000000-0xefff0000 to VME 0x02000000-0xefff0000
vme0: 2phys 0xff000000-0xff7f0000 to VME 0xff000000-0xff7f0000
vme0: 3phys 0x00000000-0x00000000 to VME 0x00000000-0x00000000
vme0: 4phys 0x00000000-0x00000000 to VME 0x00000000-0x00000000
vme0: vme to cpu irq level 1:1
vmes0 at vme0
vmel0 at vme0
ie0 at pcctwo0 offset 0x46000 ipl 1: address 08:00:3e:21:06:d9
boot device: sd0
root on sd0a
rootdev=0x400 rrootdev=0x800 rawde
```

---

I could now start building a more recent userland, in small, and a bit
erratic *(read: driven by the immediate need of getting a particular binary
to work)*, steps. At that time, some of the kernel introspection commands, such as
[ps](https://man.openbsd.org/ps),
were directly accessing kernel memory through the help of the
BSD-specific
[libkvm](https://man.openbsd.org/kvm)
(they still do this, but for kernel coredumps only, nowadays;
access to the live kernel information is done with a
[sysctl](https://man.openbsd.org/man2/sysctl.2)-based
interface), and did not work with the more recent kernel I had built.

So I needed to build a new libkvm, and then the tools depending on it.
But in order to build a new libkvm, I also needed an up-to-date
[make](https://man.openbsd.org/make)
binary. So I made progress with some trial-and-error, or skipping some build
steps (such as computing preformatted manual pages) when they would not work
yet in the current state of my system.

Near the end of february, I had most of the userland rebuilt and a more stable
system. However, I still had some problems.

```
Date: Fri, 2 Mar 2001 00:24:56 +0000
From: Miod Vallat
To: Steve Murphree
Subject: mvme88k status

[...]
- mvme187 isn't 100% stable : after 6 or 7 days it hangs without notice.
  You can ping the machine, enter ddb but that's all. active process is
  waiting for an i/o to complete, but nothing happens. This happened
  twice to me, I'll try to reproduce it on a deterministic fashion...
[...]
- I added a configuration for OpenBSD-m88k to openssl for it to compile
  with -O0 instead of -O3, built fine but this doesn't work ! ssh-keygen
  fails, ssh fails, and so on. Were you able to have openssl work on
  your machines ?
[...]
```

That last part was caused by
option CRYPTO
missing from my kernel configuration (I was using the M187 kernel,
not the GENERIC kernel, per Steve Murphree's recommendation, to
save on kernel compilation times as it had fewer device drivers and options,
and had not noticed this option was missing.)

Needless to say, I learned my lesson and switched to GENERIC kernels
shortly after. But then I stumbled upon strange kernel behaviours.
Eventually we found out that the boot loader's stack was set up way too low in
memory, and the GENERIC kernel had grown large enough to have part of its data
overlapping that area, which got then corrupted by the boot loader prior to
passing control to the kernel.
This was easily fixed by linking the second stage boot loader at a higher
address.

---

I got busy with release work for the upcoming
[2.9](https://www.openbsd.org/29.html)
release and did not do anything on mvme88k for a while.

In july, Joe Warren-Meeks asked for an mvme88k port status update on
misc@; in
the following conversation I had with him, I gave him a summary of the work
needed to update the 2.5 binaries to the current code. As you can see, this
was everything but user-friendly.

```
Date: Tue, 10 Jul 2001 01:16:41 +0000
From: Miod Vallat
To: Joe Warren-Meeks
Subject: Re: mvme88k

> Ok, cool.. apart from programming (which i'm not good enough at) is
> there anything I can do to help?

Well, programming (-;

If you've got one mvme88k machine to spare with a large disk, you can
try to track -current on your machine and report any problems - I know
of some, but I'll probably miss others.

Basically the procedure is as follow (not for the faint of heart):
- install the 2.5 snapshot
- install -CURRENT sources
- compile and install new bootloader:
   cd /usr/src/sys
   make obj && make depend && make && make install
   cd /usr/mdec
   cp -pf bootsd /boot
   ./installboot /boot ./bootxx /dev/rsd0a
- compile a kernel, reboot using this kernel
- if kernel always panics at boot, ask me to commit the CLKF_INTR fix,
  fetch current with this patch, and resume previous step
- recreate devices:
  cp /usr/src/etc/etc.mvme88k/MAKEDEV /dev
  cd /dev
  ./MAKEDEV all
- install new include files:
  cd /usr/src/include
  make prereq && make includes
- recompile libkvm
- compile basic process instrumentation tools: ps, vmstat, etc
- try a make build. You might experience kernel panics or hangs, or
  other nice things. After this, awk won't probably work, as well as as,
  be sure to keep the 2.5 snapshot tarballs handy to be able to
  restore'em when needed. The reward is that you can get openssh working
  on your machine. Yay!

Other nice things you can do is write manual pages for the
mvme88k-specific devices: ssh (ex-siop), ve, vs, vx...

Miod
```

I neglected the mvme88k port for some time, being busy with work on the
other architectures and the
[3.0](https://www.openbsd.org/30.html)
release work, and would only
resume working on cleaning the mvme88k kernel in november.

---

Early december, Steve Murphree told me he had working MVME197 support and,
as a consequence of this work, he had massive changes to make to the mvme88k
kernel code. He shared his code with me on december 5th.

*(Of course, by "working MVME197 support", he only meant that the kernel had been
able to boot and probe devices. Userland was not working correctly yet,
[init](https://man.openbsd.org/init)
would try to drop into a shell, but
[/bin/sh](https://man.openbsd.org/sh)
would segfault almost immediately.
Murphree would blame this onto other kernel changes at that time which indeed
caused quite some instability on all platforms, and got eventually reverted some
time later. But the real cause was a bug in his code, which would escape us
and wouldn't be fixed until many, many years.)*

His code
[landed](https://github.com/openbsd/src/commit/9d6f92a19b35a235e7eac3f24e7ce2df2cc7b097)
[in the tree](https://github.com/openbsd/src/commit/42b0d09a7a3beb413b5085549163464d1d52e30f)
in december 13th. Unfortunately, he had been working
on a source tree from around mid-june, and there had been many changes occurring
since there, not all of them being my work.
All these changes went undone in seconds when he dropped his files.

In modern parlance, he had forgotten (or not cared) to do a *rebase* of
his code, before dumping it into the OpenBSD source tree.
Since
[cvs](https://man.openbsd.org/man1/cvs.1),
the
[SCM](https://en.wikipedia.org/wiki/Version_control) software
OpenBSD is using, will not let you overwrite a file with an out-of-date version,
unless you are explicitly telling it to ignore that "detail",
this was **not** accidental.
It is likely that he copied his latest files over a recent checkout,
which prevented cvs from complaining, as the files metadata was
matching the repository.
But in any case, whatever he did to commit this code, it was, at best,
sloppy behaviour.

*(And please spare me "had you been using git..." pontifications, for
the only open source SCM existing at that time was CVS; neither
[git](https://en.wikipedia.org/wiki/Git)
nor
[Subversion](https://en.wikipedia.org/wiki/Apache_Subversion)
did exist yet.)*

After updating my source tree, I did not notice that he had reverted some
changes yet. But trying to build a kernel failed quickly. At this point, I
thought it was just a minor mistake, so I went on to fix one problem.
Then another. Then another. Then another...
About ten commits later, I was finally able to link a kernel, and not even sure
it would boot.

In retrospect, I could have done this better, since I still had a copy of the
code he had shared with me on december 5th. I could extract it, gather the
version number of all mvme88k files, compare to the version numbers at the time
he did his code dump, and do the "rebase" operation for each file.
This could even be scripted to be done quickly, and if there had not been many
conflicts, this could probably be done in a few hours at most. But then, if
Murphree had behaved that way, this might have been because there were too
many conflicts and he couldn't be bothered with fixing them at the moment. Who
knows.

This is pointless speculation anyways, because I had completely forgotten I
**still** had this archive lying around.
Truth to be told, I only rediscovered it while writing this story, 24 years
later.

Also, since I couldn't believe Murphree had done such a wrong cvs operation
anyway, I was not expecting having to fix that many files.

Example commit messages from my attempts at getting a kernel to build show my
increasing frustration during this evening.

```

```

* Make this run successfully through config(8), for starters...
* Steve, please pay attention to warnings.
  cpp namespace pollution is BAD.
* One more free commit, thanks to smurph@, in order to get GENERIC going.
* Uncle miod had a GENERIC mvme88k and he wanted the kernel to compile, eieio...
* This one was way too tricky at (almost) 3am. Now GENERIC enters the link phase.
* Fill the M88100 blanks...
* Even more one-liners to get the kernel to link.

I mentioned this on the OpenBSD developers' chatroom at some point. I did not
want to be too harsh on Murphree, because this is all volunteer work, and we're
all doing our best, so in my opinion I was not in position to

*demand*

he
fix his mess (while I would never have accepted such a sloppy attitude
from a paid coworker at my dayjob.)
But

**Theo de Raadt**

had a different opinion.

```
<miod> this would distract me while I am fixing smurph's lack of CVS knowledge.
<deraadt> he needs a beating
<miod> no, he needs to get a cvs course first.
<espie> tell us, how different this is.
<miod> doing s/foo/bar on rev 1.4 and commiting this over 1.8 is sure very fun to fix.
<deraadt> miod, you misunderstand
<deraadt> tell him to fix it.
<deraadt> don't do his shit work
<deraadt> show him that you are going to hold him accountable
<miod> no, you misunderstand. if I ask him to fix this, the results will be WORSE
<deraadt> no, they will not be.
<deraadt> demand that they not be worse
<espie> then you back out the result and ask him again.
<miod> and wait for ten years?
<deraadt> miod, EXACTLY what espie said
<espie> and ask him again.
<deraadt> miod, so what?
<deraadt> You have a file that works.
<miod> hmm.
<deraadt> Remove his changes.
<espie> and  if he doesn't comply, you send Theo to his house to `explain'.
<deraadt> really!  Why else will he learn!
<deraadt> hurt him.  that is the only time he will learn.
<deraadt> right now, back that file out.
<miod> you know what? he will NOT care. he has HIS tree from before rome was built, and he is happy with it.
<deraadt> yes he will care.
<deraadt> ok, shall I make him care because you are a wimp?
<miod> ok. deal. I'll backout his work in a few moments.
<deraadt> OK, his account is now disabled.
<deraadt> Until you guys resolve your differences.
<deraadt> I will let you tell him his account is off.
<miod> I'm not a wimp. I am just sometimes not rude enough, whatever funny it might sound.
<deraadt> Get this resolved; getting it half resolved will mean I just just enable his and disable yours ;-)
<deraadt> OK?
<espie> Heh, don't disable miod's account, I still get a kick out of his broken english commit messages.
<miod> and how will he be able to fix this if his account his disabled? please at least let it on
<deraadt> Like, DUH
<deraadt> By sending you diffs, moron
<miod> oh. eh. it's late there.
```

Theo de Raadt shot first by disabling Murphree's access to the source tree, and
sending him that email:

```
Date: Sun, 16 Dec 2001 16:39:47 -0700
From: Theo de Raadt
To: Steve Murphree
Cc: Miod Vallat
Subject: account

I have disabled your account because I hear that you are doing cvs
tree violations, breaking portable or partially portable code, not
working with others nicely, causing other developers grief.

We had to train mickey in the same way years ago.

I'll let you talk to miod about it; he'll tell me when to re-enable
it.

really, dude... this matters.  You do not commit changed versions of
a 1.4 rev file on top of a 1.8 that has other fixes.  That is just
BULLSHIT.
```

The chatroom conversation continued in private messages after that.

```
<deraadt> there you go miod, don't you feel better?
<miod> will surely help me a lot. I'm writing a message to smurph at the moment...
<deraadt> i decided to be nice and set the tone for you
<deraadt> now i suggest you not play too nice
<deraadt> if you play too nice, he will not listen to you in the future
<deraadt> and instead it will come down to me again having to yell for you
<deraadt> next time, i will tell you to go to hell and live with it
<deraadt> nice people finish last.
<deraadt> he needs you
<deraadt> he will not do release engineering for 88k
<deraadt> but i bet you will do it
<deraadt> so he has to be real nice to you
<deraadt> or what he is doing is just a brain fuck
<deraadt> and we do not welcome brain fucks in our tree
<miod> ok, ok, ok. I dislike this but I know I have to be rude. Let's see how this resolves.
```

So I
[reverted](https://github.com/openbsd/src/commit/0d02aa375a676f8dff9f7afd21e01ff0231e32f9)
the mvme88k part of the tree back to what its state was a few
days ago.

```
Revert the mvme88k to 20011212. Recent changes had not been merged correctly,
and I am fed up with dissecting diffs to put back code that disappeared.
This will likely be fixed shortly.
```

Immediately after, I sent this mail to Murphree.

```
Date: Sun, 16 Dec 2001 23:54:56 +0000
From: Miod Vallat
To: Steve Murphree
Subject: Re: account

> I have disabled your account because I hear that you are doing cvs
> tree violations, breaking portable or partially portable code, not
> working with others nicely, causing other developers grief.
>
> We had to train mickey in the same way years ago.
>
> I'll let you talk to miod about it; he'll tell me when to re-enable
> it.
>
> really, dude... this matters.  You do not commit changed versions of
> a 1.4 rev file on top of a 1.8 that has other fixes.  That is just
> BULLSHIT.
>
Ok, Theo went a bit too far in my opinion, but basically realizing that
you didn't spend some time to merge your diffs correctly and that some
diffs have disappeared was not the best news of the week-end.

Are you not confident with cvs to do such a merge, or were you a bit
hasty? Do you need help doing this?

Anyways, all it takes is that you submit a diff against -current code
that doesn't put files back in time, and your account will be back for
you to commit it.

Sorry for trouble,
Miod
```

Theo de Raadt disagreed with the tone of that mail and gave me "hints" in
private.

```
<deraadt> dealt with him?
<deraadt> no cc?
<miod> I did not put you in cc:
<miod> want a copy?
<deraadt> sure, lemme see what you said to him ;-)
<miod> I'll bet you'll find that I have been too nice
<deraadt> heh
<deraadt> lemme give you another hint
<deraadt> start with the sentence "you are killing me"
<deraadt> then change it
<miod> I'm all ears
<deraadt> replace words
<deraadt> over and over and over
<miod> haha
<deraadt> until you have something that still says "you are killing me"
<deraadt> without using those words
<deraadt> really
<deraadt> i do this sometimes ;-)
<miod> bounced the message to you.
<deraadt> WAY TOO NICE
<deraadt> sigh
<deraadt> you didn't learn anything.
<miod> see? told you.
<deraadt> how many hours did you spend before you gave up?
<deraadt> tell me how many hours
<miod> heck, this is the first time I do this in OpenBSD. I am knowned [sic]
       for being very rude in such situations in my real work, though
<deraadt> come on, estimate it
<deraadt> how many
<miod> can't say, I was also working on my new pmap code. 2 to 4 hours.
<deraadt> 4 hours only?
<deraadt> are you serious?
<miod> I was 1/3 of the remerge work. means 8 hours still left to do this
       correctly.
<deraadt> ok, send this sentence.
<deraadt> "I spent 4 hours trying to fix bugs in code I do not understand, and I expected
          there was 8 hours minimum left.  It was your responsibility to not make me do
          this".
<deraadt> send that.
<deraadt> THAT is the truth.
<deraadt> isn't it 100% true?
<miod> no, I understand the code. It's just a PITA.
<deraadt> so say that.
<deraadt> you need to involve him.
<deraadt> will he take you seriously?
<deraadt> anyways, your own battle
<deraadt> bye
```

It took a few days for Murphree to cool off.

```
Date: Mon, 17 Dec 2001 09:12:39 +0000
From: Miod Vallat
To: Steve Murphree
Subject: Re: account

> What exactly did I break that was so troublesome?  Did you email me?  Please
> tell me things that might irk you.  I cannot read minds.  No, I find out
> about it from Theo telling me my account has been disabled.  Peachy.

You did not ``break'' things. It just seems that you didn't cvs update
all the files, hence you commited changes to old revisions against
-current revisions. I spend several hours this week-end to solve
conflicts and get your changes correctly merged in half of the files.

I was about to send you a mail about this. Then I did the mistake of
mentioning this on icb, and Theo was awake.
And once he decided to close your account, whatever I said, I could not
get him NOT to do it.

> Let me tell what you have done:  You have single handedly taken something
> away from me that I hold very dear.  Something I was very proud of.  Feel
> good about it?  I pray no one ever does that to you.  No one deserves this.

Do you think I enjoy this as well?

> Hey, don't get me wrong.  I like the stuff you have done.  I thought you and
> I thought alike.  I liked having someone else interested in the mvme88k
> port.  I thought it was a good thing.  I'm disappointed.  So very, very
> disappointed.

I respect your work as well. I did not want things to end like this at
all. Now, let's work on addressing this issue, shall we?

Miod
```

---

```
Date: Mon, 17 Dec 2001 19:46:55 +0000
From: Miod Vallat
To: Theo de Raadt
Subject: smurph's account

Well, we had a long discussion by mail about this. Steve was sure upset
first, then he calmed down and we discussed the issues.

It turns out he acknowledges that he commited his m88k changes a bit too
early, and had planned to fix the merge issues a bit later. On the other
hand, I acknowledged I was too harsh in my commit messages, so this did
not help the situation anyway.

So the plan at the moment is that he will fix the current ahc problems,
commit the necessary changes, and then commit his mvme88k changes again,
but correctly. You can reenable his account any time now.

Miod
```

We had that private conversation shortly after.

```
<miod> I'm just back, and replying to your message
<smurph> I'm going to try to get that stuff back in tonight. layer by layer, so
         to speak. Any thing you see that I might need to watch out for?
<miod> if you can make sure that GENERIC compiles, that's a good start.
<miod> did theo reenable your account yet?
<smurph> No need to. Unless you just want to. I'm over it as far as I'm concerned. That
         stuff just hit me hard though. But I meant what I said about you and your work.
         You are just the sort to make OpenBSD better.
[...]
<smurph> yes, Theo enabled it.
<miod> so it's finally over, I guess.
<smurph> Thanks dude. That's nice of you to do so. Yeah, it's over. I don't harbor
         things. I'm not like my mother!! :)
<miod> I'm going to sleep now (4:15am), cul8r
<smurph> hasta! Good night.
```

*(My sleep schedule really was a mess, these years. It has changed a lot since
then, and if you see me awake at 4:15am nowadays, this will be because I've just
waken up, not because I am about to crash...)*

Murphree split his changes in smaller pieces and made sure to not discard
existing changes this time, starting on the 19th.

```
Date: Wed, 19 Dec 2001 09:21:46 +0000
From: Miod Vallat
To: Steve Murphree
Subject: Re: CVS: cvs.openbsd.org: src

> CVSROOT:      /cvs
> Module name:  src
> Changes by:   smurph@cvs.openbsd.org  2001/12/19 00:04:42
>
> Modified files:
>       sys/arch/mvme88k/conf: GENERIC M187 M188 M197
>       sys/arch/mvme88k/dev: bussw.c cl.c clock.c dart.c mainbus.c
>                             nvram.c pcctwo.c sram.c syscon.c vx.c
>       sys/arch/mvme88k/include: cpu_number.h cpus.h param.h
>       sys/arch/mvme88k/mvme88k: cmmu.c eh.S locore.S
>                                 locore_c_routines.c m18x_cmmu.c
>                                 machdep.c pmap.c pmap_table.c
>
> Log message:
> Introduce brdtyp and change what cputyp means.

You know, I like the fact that you are commiting this in several parts.
It helps knowing why each file was affected, and provides the ability,
in case of problems, to find stable revisions more easily.

Miod
```

---

With the tension resolved and the source tree back to a good state, it was time
to start working on the immediate major problem: the compiler.

```
Date: Thu, 27 Dec 2001 00:50:55 +0000
From: Miod Vallat
To: Steve Murphree
Subject: mvme88k gcc 2.95 kernel does not work yet...

Well, I was able to finally get one kernel compiled and linked on a
sparc.
But, somehow, I think there's still a long road to drive:

187-Bug>BO 6 0 gcc295
Booting from: VME328, Controller 6, Drive 0
Loading: gcc295

Volume: M88K

IPL loaded at: $009F0000
Boot: bug device: ctrl=6, dev=0

bootxx: first level bootstrap program [$Revision: 1.1 $]

\
>> OpenBSD/mvme88k bootsd [$Revision: 1.2 $]
1769472+147456+205664+[68940+80842]=0x22ac7a
Start @ 0x10020 ...
Controler Address @ ffff9000 ...
MVME187 board configuration #A: 1 CPUs 2 CMMUs
CPU0 is attached with 2 MC88200 CMMUs
CPU0 is master CPU
[ using 149782 bytes of bsd a.out symbol table ]
Copyright (c) 1982, 1986, 1989, 1991, 1993
        The Regents of the University of California.  All rights reserved.
Copyright (c) 1995-2001 OpenBSD. All rights reserved.  http://www.OpenBSD.org

panic: kernel diagnostic assertion "(align & (align - 1)) == 0" failed: file "/src/current/src/sys/arch/mvme88k/compile/M187/../../../../uvm/uvm_map.c", line 843
Stopped at      _Debugger:              tb0     0x0,    r0  ,0x84
RUN AT LEAST 'trace' AND 'ps' AND INCLUDE OUTPUT WHEN REPORTING THIS PANIC!
DO NOT EVEN BOTHER REPORTING THIS WITHOUT INCLUDING THAT INFORMATION!
ddb> trace
stack base = 0xeee07d80
(0) _Debugger(stackless)
(1) _panic+0x138(?, 14f640, 0x150558, 14fef0, 34b, 0xffffffff, 0xffffffff, 0xff
ffffff)
(2) ___assert+0x2c
(3) _uvm_map_findspace+0x5c
(4) _uvm_map+0x184
(5) _uvm_km_init+0x118
(6) _uvm_init+0x60
(7) _main+0x68
(8) master_start+0x64
ddb>


That's a start...
```

I did not spend much time on this, though, and kept being busy with other
OpenBSD activities. However, eventually, I had been able to build an almost
complete userland, so that we could have more recent binaries available than the
old 2.5 binaries.

```
Date: Tue, 7 May 2002 23:08:32 +0000
From: Miod Vallat
To: Paul Weissmann, Steve Murphree
Subject: mvme88k news

Well, I have updated my mvme88k status page and there is an incomplete,
but working, 3.1-beta snapshot. No bsd.rd to install though, still
fighting toolchain problems.

http://XXX.XXX.XXX.XXX/~miod/mvme88k

Miod
```

---

In august that year, I had the opportunity to get more mvme88k hardware,
including a MVME197LE board; I also got my hands on some errata information,
which can be found (among other documents which are not on bitsavers yet)
on
[this page](http://miod.online.fr/motorola/).

```
Date: Sat, 17 Aug 2002 22:21:23 +0000
From: Miod Vallat
To: Steve Murphree
Subject: mvme 197 errata

Hello,

  I have a 20 page document here. It contains:
"MVME197 ERRATA" rev 1.10, 3/24/94
"MVME197DP/SP ERRATA" rev 1.0, 3/17/94
88110 Rev 4.2 (3E34M) Errata Documentation Package, Version 1.6, 9/15/93
88110 Rev 5.1 (2E66S) Errata Documentation Package, Version 1.0, 9/15/93

Is this the one you have? Do you want a copy of this document?

Excerpts:

1) ERRATA: Line transfers initiated by the VMEchip2 can lock the board.
2) ERRATA: Conflicts with the DCAM2 during invalidate cycles.
3) ERRATA: I2C Serial Bus not fully functional.
4) ERRATA: VMEbus Slave Mapping
5) ERRATA: The BusSwitch ISEL registers have their write data path reversed.
6) ERRATA: sd/ld.x problem with the 88110
7) ERRATA: Local Reset Does Not Function Properly
8) ERRATA: XMEM Instruction Execution to VMEbus Slave Fails To Lock The Bus.

Some of them are fixed on recent boards, I also have the history of the
PCB revisions, etc.

I need to sort this out and give you more details.

Miod
```

Meanwhile, Marc Zyngier of Linux fame had gotten a 4-processor MVME188 machine
and asked me whether OpenBSD could run on it.

```
Date: Sun, 5 Jan 2003 23:19:54 +0000
From: Miod Vallat
To: Marc Zyngier
Subject: MVME188

Bon, j'ai testÃ© mes cartes MVME188{,A} cet aprÃ¨s-midi, et comme par
hasard, le support MVME188 a Ã©tÃ© cassÃ© par les commits censÃ©s apporter
le support MVME197 (qui n'a jamais marchÃ© chez moi...). De longues
heures de dÃ©boguage en perspective.
[So, I have tested my MVME188{,A} boards this afternoon and, how surprising,
it turns out MVME188 support got broken by the changes supposed to bring
MVME197 support (which has never been working here...). I'm expecting
many hours of debugging.]

Par contre, en triant mes HYPERmodule, j'ai vu que j'avais un mignon
4P128 (4 CPU, 8 CMMU) Ã  25 MHz, moi aussi. Faudra vraiment que je bosse
sur le SMP un jour. Un MVME188A avec un 4P128 ne tiendra pas la route
face Ã  un MVME197DP Ã  50MHz, mais il y a de meilleures chances que le
188 tourne Ã  nouveau avant que le 197 tourne tout court...
[However, while sorting my HYPERmodule, I noticed that I have a nice
25MHz 4P128 (4 CPU, 8 CMMU), too. Gonna have to work on SMP at some
point. A 4P128 MVME188A won't win against a 50MHz MVME197DP, but is
very likely to get running again before the 197 ever runs...]

Miod
```

But, just like the gcc 2.95 behaviour investigation, this did not turn into
anything: on MVME188 boards, the kernel would boot but never start init,
and I gave up quite quickly.

Things were looking bad for that port, and with a lack of an in-tree toolchain,
its days were now numbered.

(Follow [this link](http://miod.online.fr/software/openbsd/stories/m88k2.html) to go forward to the next part.)