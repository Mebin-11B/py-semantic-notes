---
title: "CP/M-386 – CP/M for 386 protected mode, derived from CP/M‑68K"
url: https://github.com/johnsonjh/cpm386
clipped: 2026-08-31 12:22:22
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [CP/M-386 – CP/M for 386 protected mode, derived from CP/M‑68K](https://github.com/johnsonjh/cpm386)

## Digest Summary
CP/M‑386 is an early‑stage port of CP/M to 386 protected‑mode, derived from CP/M‑68K. It runs on 386+ hardware with ≥2 MiB RAM, supporting BIOS or UEFI (with CSM), VGA, 8042 PS/2, 8250/16450/16550 UARTs, CMOS RTC, and 8253/8254 PIT. The BDOS reports version 2.2 and matches CP/M‑68K 1.3 and CP/M 2.2, implements most CP/M‑Plus (CP/M 3) functions, ≈60 % of DOS‑Plus additions, and about half of the MP/M extensions; missing features are primarily multi‑user, multitasking, message queuing, and process control calls. Unique BDOS extensions provide direct video access, high‑resolution timing, PRNG, etc. Building requires cpmtools ≥ 2.23, gcc‑16 (or clang) and 32‑bit support libraries; supported on NetBSD, FreeBSD (with rebuilt cpmtools), and recent Linux releases (CentOS Stream 9, Fedora 36, Debian 12, Ubuntu 18.04/22.04, Alpine 3.24, openSUSE Leap 15.4). Pre‑compiled binaries and QEMU launch commands (multiboot kernel or floppy MBR) are supplied. Contributions must avoid large LLM‑generated code; AI tool use follows the LLVM AI Tool Use Policy and may be revoked. The project is MIT‑licensed, with unlimited rights granted by Bryan W. Sparks of DeviceLogics LLC.

---

## Full Article

[Skip to content](https://github.com/johnsonjh/cpm386#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [johnsonjh](https://github.com/johnsonjh)    
    /
    
      [cpm386](https://github.com/johnsonjh/cpm386)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fjohnsonjh%2Fcpm386)    You must be signed in to change notification settings

  

  
- 
          [Fork
    1](https://github.com/login?return_to=%2Fjohnsonjh%2Fcpm386)
  

  
- 
        
        [Star
          55](https://github.com/login?return_to=%2Fjohnsonjh%2Fcpm386)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     master[Branches](https://github.com/johnsonjh/cpm386/branches)[Tags](https://github.com/johnsonjh/cpm386/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[518 Commits](https://github.com/johnsonjh/cpm386/commits/master/)518 Commits

## Folders and files

NameNameLast commit messageLast commit date[LICENSES](https://github.com/johnsonjh/cpm386/tree/master/LICENSES)[LICENSES](https://github.com/johnsonjh/cpm386/tree/master/LICENSES)  [.codespellrc](https://github.com/johnsonjh/cpm386/blob/master/.codespellrc)[.codespellrc](https://github.com/johnsonjh/cpm386/blob/master/.codespellrc)  [.gitignore](https://github.com/johnsonjh/cpm386/blob/master/.gitignore)[.gitignore](https://github.com/johnsonjh/cpm386/blob/master/.gitignore)  [.gitlab-ci.yml](https://github.com/johnsonjh/cpm386/blob/master/.gitlab-ci.yml)[.gitlab-ci.yml](https://github.com/johnsonjh/cpm386/blob/master/.gitlab-ci.yml)  [.sizes.txt](https://github.com/johnsonjh/cpm386/blob/master/.sizes.txt)[.sizes.txt](https://github.com/johnsonjh/cpm386/blob/master/.sizes.txt)  [.sizes.txt.license](https://github.com/johnsonjh/cpm386/blob/master/.sizes.txt.license)[.sizes.txt.license](https://github.com/johnsonjh/cpm386/blob/master/.sizes.txt.license)  [BSDmakefile](https://github.com/johnsonjh/cpm386/blob/master/BSDmakefile)[BSDmakefile](https://github.com/johnsonjh/cpm386/blob/master/BSDmakefile)  [CODE_OF_CONDUCT.md](https://github.com/johnsonjh/cpm386/blob/master/CODE_OF_CONDUCT.md)[CODE_OF_CONDUCT.md](https://github.com/johnsonjh/cpm386/blob/master/CODE_OF_CONDUCT.md)  [Dockerfile](https://github.com/johnsonjh/cpm386/blob/master/Dockerfile)[Dockerfile](https://github.com/johnsonjh/cpm386/blob/master/Dockerfile)  [FUTURE.md](https://github.com/johnsonjh/cpm386/blob/master/FUTURE.md)[FUTURE.md](https://github.com/johnsonjh/cpm386/blob/master/FUTURE.md)  [GNUmakefile](https://github.com/johnsonjh/cpm386/blob/master/GNUmakefile)[GNUmakefile](https://github.com/johnsonjh/cpm386/blob/master/GNUmakefile)  [LICENSE](https://github.com/johnsonjh/cpm386/blob/master/LICENSE)[LICENSE](https://github.com/johnsonjh/cpm386/blob/master/LICENSE)  [README.md](https://github.com/johnsonjh/cpm386/blob/master/README.md)[README.md](https://github.com/johnsonjh/cpm386/blob/master/README.md)  [absaddr.h](https://github.com/johnsonjh/cpm386/blob/master/absaddr.h)[absaddr.h](https://github.com/johnsonjh/cpm386/blob/master/absaddr.h)  [aclock.h](https://github.com/johnsonjh/cpm386/blob/master/aclock.h)[aclock.h](https://github.com/johnsonjh/cpm386/blob/master/aclock.h)  [aclockdv.c](https://github.com/johnsonjh/cpm386/blob/master/aclockdv.c)[aclockdv.c](https://github.com/johnsonjh/cpm386/blob/master/aclockdv.c)  [aclockvt.c](https://github.com/johnsonjh/cpm386/blob/master/aclockvt.c)[aclockvt.c](https://github.com/johnsonjh/cpm386/blob/master/aclockvt.c)  [alvtst.c](https://github.com/johnsonjh/cpm386/blob/master/alvtst.c)[alvtst.c](https://github.com/johnsonjh/cpm386/blob/master/alvtst.c)  [bdosdef.h](https://github.com/johnsonjh/cpm386/blob/master/bdosdef.h)[bdosdef.h](https://github.com/johnsonjh/cpm386/blob/master/bdosdef.h)  [bdosinc.h](https://github.com/johnsonjh/cpm386/blob/master/bdosinc.h)[bdosinc.h](https://github.com/johnsonjh/cpm386/blob/master/bdosinc.h)  [bdosmain.c](https://github.com/johnsonjh/cpm386/blob/master/bdosmain.c)[bdosmain.c](https://github.com/johnsonjh/cpm386/blob/master/bdosmain.c)  [bdosmisc.c](https://github.com/johnsonjh/cpm386/blob/master/bdosmisc.c)[bdosmisc.c](https://github.com/johnsonjh/cpm386/blob/master/bdosmisc.c)  [bdosrw.c](https://github.com/johnsonjh/cpm386/blob/master/bdosrw.c)[bdosrw.c](https://github.com/johnsonjh/cpm386/blob/master/bdosrw.c)  [bios.c](https://github.com/johnsonjh/cpm386/blob/master/bios.c)[bios.c](https://github.com/johnsonjh/cpm386/blob/master/bios.c)  [biosdef.h](https://github.com/johnsonjh/cpm386/blob/master/biosdef.h)[biosdef.h](https://github.com/johnsonjh/cpm386/blob/master/biosdef.h)  [bringup.c](https://github.com/johnsonjh/cpm386/blob/master/bringup.c)[bringup.c](https://github.com/johnsonjh/cpm386/blob/master/bringup.c)  [bringup.h](https://github.com/johnsonjh/cpm386/blob/master/bringup.h)[bringup.h](https://github.com/johnsonjh/cpm386/blob/master/bringup.h)  [capslock.c](https://github.com/johnsonjh/cpm386/blob/master/capslock.c)[capslock.c](https://github.com/johnsonjh/cpm386/blob/master/capslock.c)  [ccp.c](https://github.com/johnsonjh/cpm386/blob/master/ccp.c)[ccp.c](https://github.com/johnsonjh/cpm386/blob/master/ccp.c)  [ccpdef.h](https://github.com/johnsonjh/cpm386/blob/master/ccpdef.h)[ccpdef.h](https://github.com/johnsonjh/cpm386/blob/master/ccpdef.h)  [cleartpa.c](https://github.com/johnsonjh/cpm386/blob/master/cleartpa.c)[cleartpa.c](https://github.com/johnsonjh/cpm386/blob/master/cleartpa.c)  [cls.c](https://github.com/johnsonjh/cpm386/blob/master/cls.c)[cls.c](https://github.com/johnsonjh/cpm386/blob/master/cls.c)  [conbdos.c](https://github.com/johnsonjh/cpm386/blob/master/conbdos.c)[conbdos.c](https://github.com/johnsonjh/cpm386/blob/master/conbdos.c)  [conctl.c](https://github.com/johnsonjh/cpm386/blob/master/conctl.c)[conctl.c](https://github.com/johnsonjh/cpm386/blob/master/conctl.c)  [cpmrng.c](https://github.com/johnsonjh/cpm386/blob/master/cpmrng.c)[cpmrng.c](https://github.com/johnsonjh/cpm386/blob/master/cpmrng.c)  [cpmrng.h](https://github.com/johnsonjh/cpm386/blob/master/cpmrng.h)[cpmrng.h](https://github.com/johnsonjh/cpm386/blob/master/cpmrng.h)  [delay.c](https://github.com/johnsonjh/cpm386/blob/master/delay.c)[delay.c](https://github.com/johnsonjh/cpm386/blob/master/delay.c)  [disk.c](https://github.com/johnsonjh/cpm386/blob/master/disk.c)[disk.c](https://github.com/johnsonjh/cpm386/blob/master/disk.c)  [disk.h](https://github.com/johnsonjh/cpm386/blob/master/disk.h)[disk.h](https://github.com/johnsonjh/cpm386/blob/master/disk.h)  [disk_v86.s](https://github.com/johnsonjh/cpm386/blob/master/disk_v86.s)[disk_v86.s](https://github.com/johnsonjh/cpm386/blob/master/disk_v86.s)  [diskdefs](https://github.com/johnsonjh/cpm386/blob/master/diskdefs)[diskdefs](https://github.com/johnsonjh/cpm386/blob/master/diskdefs)  [dskutil.c](https://github.com/johnsonjh/cpm386/blob/master/dskutil.c)[dskutil.c](https://github.com/johnsonjh/cpm386/blob/master/dskutil.c)  [dumpdir.c](https://github.com/johnsonjh/cpm386/blob/master/dumpdir.c)[dumpdir.c](https://github.com/johnsonjh/cpm386/blob/master/dumpdir.c)  [dumpfcb.c](https://github.com/johnsonjh/cpm386/blob/master/dumpfcb.c)[dumpfcb.c](https://github.com/johnsonjh/cpm386/blob/master/dumpfcb.c)  [ed.c](https://github.com/johnsonjh/cpm386/blob/master/ed.c)[ed.c](https://github.com/johnsonjh/cpm386/blob/master/ed.c)  [esctilde.c](https://github.com/johnsonjh/cpm386/blob/master/esctilde.c)[esctilde.c](https://github.com/johnsonjh/cpm386/blob/master/esctilde.c)  [fileio.c](https://github.com/johnsonjh/cpm386/blob/master/fileio.c)[fileio.c](https://github.com/johnsonjh/cpm386/blob/master/fileio.c)  [fparse.c](https://github.com/johnsonjh/cpm386/blob/master/fparse.c)[fparse.c](https://github.com/johnsonjh/cpm386/blob/master/fparse.c)  [getsn.c](https://github.com/johnsonjh/cpm386/blob/master/getsn.c)[getsn.c](https://github.com/johnsonjh/cpm386/blob/master/getsn.c)  [gfxtest.c](https://github.com/johnsonjh/cpm386/blob/master/gfxtest.c)[gfxtest.c](https://github.com/johnsonjh/cpm386/blob/master/gfxtest.c)  [hd.c](https://github.com/johnsonjh/cpm386/blob/master/hd.c)[hd.c](https://github.com/johnsonjh/cpm386/blob/master/hd.c)  [hello.c](https://github.com/johnsonjh/cpm386/blob/master/hello.c)[hello.c](https://github.com/johnsonjh/cpm386/blob/master/hello.c)  [illegal.c](https://github.com/johnsonjh/cpm386/blob/master/illegal.c)[illegal.c](https://github.com/johnsonjh/cpm386/blob/master/illegal.c)  [io.h](https://github.com/johnsonjh/cpm386/blob/master/io.h)[io.h](https://github.com/johnsonjh/cpm386/blob/master/io.h)  [iosys.c](https://github.com/johnsonjh/cpm386/blob/master/iosys.c)[iosys.c](https://github.com/johnsonjh/cpm386/blob/master/iosys.c)  [iotest.c](https://github.com/johnsonjh/cpm386/blob/master/iotest.c)[iotest.c](https://github.com/johnsonjh/cpm386/blob/master/iotest.c)  [julia.c](https://github.com/johnsonjh/cpm386/blob/master/julia.c)[julia.c](https://github.com/johnsonjh/cpm386/blob/master/julia.c)  [kbd.c](https://github.com/johnsonjh/cpm386/blob/master/kbd.c)[kbd.c](https://github.com/johnsonjh/cpm386/blob/master/kbd.c)  [kbd.h](https://github.com/johnsonjh/cpm386/blob/master/kbd.h)[kbd.h](https://github.com/johnsonjh/cpm386/blob/master/kbd.h)  [layout.inc](https://github.com/johnsonjh/cpm386/blob/master/layout.inc)[layout.inc](https://github.com/johnsonjh/cpm386/blob/master/layout.inc)  [linker.ld](https://github.com/johnsonjh/cpm386/blob/master/linker.ld)[linker.ld](https://github.com/johnsonjh/cpm386/blob/master/linker.ld)  [lrbc.c](https://github.com/johnsonjh/cpm386/blob/master/lrbc.c)[lrbc.c](https://github.com/johnsonjh/cpm386/blob/master/lrbc.c)  [ls.c](https://github.com/johnsonjh/cpm386/blob/master/ls.c)[ls.c](https://github.com/johnsonjh/cpm386/blob/master/ls.c)  [lz4dec.inc](https://github.com/johnsonjh/cpm386/blob/master/lz4dec.inc)[lz4dec.inc](https://github.com/johnsonjh/cpm386/blob/master/lz4dec.inc)  [mandel.c](https://github.com/johnsonjh/cpm386/blob/master/mandel.c)[mandel.c](https://github.com/johnsonjh/cpm386/blob/master/mandel.c)  [mbentry.s](https://github.com/johnsonjh/cpm386/blob/master/mbentry.s)[mbentry.s](https://github.com/johnsonjh/cpm386/blob/master/mbentry.s)  [mboot.sh](https://github.com/johnsonjh/cpm386/blob/master/mboot.sh)[mboot.sh](https://github.com/johnsonjh/cpm386/blob/master/mboot.sh)  [mem.c](https://github.com/johnsonjh/cpm386/blob/master/mem.c)[mem.c](https://github.com/johnsonjh/cpm386/blob/master/mem.c)  [memmap.c](https://github.com/johnsonjh/cpm386/blob/master/memmap.c)[memmap.c](https://github.com/johnsonjh/cpm386/blob/master/memmap.c)  [memmap.h](https://github.com/johnsonjh/cpm386/blob/master/memmap.h)[memmap.h](https://github.com/johnsonjh/cpm386/blob/master/memmap.h)  [mk386.c](https://github.com/johnsonjh/cpm386/blob/master/mk386.c)[mk386.c](https://github.com/johnsonjh/cpm386/blob/master/mk386.c)  [mklz4raw.c](https://github.com/johnsonjh/cpm386/blob/master/mklz4raw.c)[mklz4raw.c](https://github.com/johnsonjh/cpm386/blob/master/mklz4raw.c)  [mltiboot.c](https://github.com/johnsonjh/cpm386/blob/master/mltiboot.c)[mltiboot.c](https://github.com/johnsonjh/cpm386/blob/master/mltiboot.c)  [mltiboot.h](https://github.com/johnsonjh/cpm386/blob/master/mltiboot.h)[mltiboot.h](https://github.com/johnsonjh/cpm386/blob/master/mltiboot.h)  [more.c](https://github.com/johnsonjh/cpm386/blob/master/more.c)[more.c](https://github.com/johnsonjh/cpm386/blob/master/more.c)  [numlock.c](https://github.com/johnsonjh/cpm386/blob/master/numlock.c)[numlock.c](https://github.com/johnsonjh/cpm386/blob/master/numlock.c)  [od.c](https://github.com/johnsonjh/cpm386/blob/master/od.c)[od.c](https://github.com/johnsonjh/cpm386/blob/master/od.c)  [pause.c](https://github.com/johnsonjh/cpm386/blob/master/pause.c)[pause.c](https://github.com/johnsonjh/cpm386/blob/master/pause.c)  [pip.c](https://github.com/johnsonjh/cpm386/blob/master/pip.c)[pip.c](https://github.com/johnsonjh/cpm386/blob/master/pip.c)  [pit.c](https://github.com/johnsonjh/cpm386/blob/master/pit.c)[pit.c](https://github.com/johnsonjh/cpm386/blob/master/pit.c)  [pit.h](https://github.com/johnsonjh/cpm386/blob/master/pit.h)[pit.h](https://github.com/johnsonjh/cpm386/blob/master/pit.h)  [pktio.h](https://github.com/johnsonjh/cpm386/blob/master/pktio.h)[pktio.h](https://github.com/johnsonjh/cpm386/blob/master/pktio.h)  [platform.h](https://github.com/johnsonjh/cpm386/blob/master/platform.h)[platform.h](https://github.com/johnsonjh/cpm386/blob/master/platform.h)  [pmode.c](https://github.com/johnsonjh/cpm386/blob/master/pmode.c)[pmode.c](https://github.com/johnsonjh/cpm386/blob/master/pmode.c)  [pmode.h](https://github.com/johnsonjh/cpm386/blob/master/pmode.h)[pmode.h](https://github.com/johnsonjh/cpm386/blob/master/pmode.h)  [pmode.s](https://github.com/johnsonjh/cpm386/blob/master/pmode.s)[pmode.s](https://github.com/johnsonjh/cpm386/blob/master/pmode.s)  [printenv.c](https://github.com/johnsonjh/cpm386/blob/master/printenv.c)[printenv.c](https://github.com/johnsonjh/cpm386/blob/master/printenv.c)  [prng.c](https://github.com/johnsonjh/cpm386/blob/master/prng.c)[prng.c](https://github.com/johnsonjh/cpm386/blob/master/prng.c)  [rc.c](https://github.com/johnsonjh/cpm386/blob/master/rc.c)[rc.c](https://github.com/johnsonjh/cpm386/blob/master/rc.c)  [reboot.c](https://github.com/johnsonjh/cpm386/blob/master/reboot.c)[reboot.c](https://github.com/johnsonjh/cpm386/blob/master/reboot.c)  [rm.c](https://github.com/johnsonjh/cpm386/blob/master/rm.c)[rm.c](https://github.com/johnsonjh/cpm386/blob/master/rm.c)  [rtc.c](https://github.com/johnsonjh/cpm386/blob/master/rtc.c)[rtc.c](https://github.com/johnsonjh/cpm386/blob/master/rtc.c)  [rtc.h](https://github.com/johnsonjh/cpm386/blob/master/rtc.h)[rtc.h](https://github.com/johnsonjh/cpm386/blob/master/rtc.h)  [stage1.s](https://github.com/johnsonjh/cpm386/blob/master/stage1.s)[stage1.s](https://github.com/johnsonjh/cpm386/blob/master/stage1.s)  [stage2.s](https://github.com/johnsonjh/cpm386/blob/master/stage2.s)[stage2.s](https://github.com/johnsonjh/cpm386/blob/master/stage2.s)  [stat.c](https://github.com/johnsonjh/cpm386/blob/master/stat.c)[stat.c](https://github.com/johnsonjh/cpm386/blob/master/stat.c)  [sync.c](https://github.com/johnsonjh/cpm386/blob/master/sync.c)[sync.c](https://github.com/johnsonjh/cpm386/blob/master/sync.c)  [termtest.c](https://github.com/johnsonjh/cpm386/blob/master/termtest.c)[termtest.c](https://github.com/johnsonjh/cpm386/blob/master/termtest.c)  [test110.c](https://github.com/johnsonjh/cpm386/blob/master/test110.c)[test110.c](https://github.com/johnsonjh/cpm386/blob/master/test110.c)  [test211.c](https://github.com/johnsonjh/cpm386/blob/master/test211.c)[test211.c](https://github.com/johnsonjh/cpm386/blob/master/test211.c)  View all files

## Repository files navigation

# CP/M-386

CP/M‑386 is CP/M for 386 protected mode, derived from CP/M‑68K.

- [Overview](https://github.com/johnsonjh/cpm386#overview)

- [Hardware support](https://github.com/johnsonjh/cpm386#hardware-support)

- [CP/M compatibility](https://github.com/johnsonjh/cpm386#cpm-compatibility)

- [Build requirements](https://github.com/johnsonjh/cpm386#build-requirements)

- [Optional dependencies](https://github.com/johnsonjh/cpm386#optional-dependencies)

- [Downloads](https://github.com/johnsonjh/cpm386#downloads)

- [Compilation](https://github.com/johnsonjh/cpm386#compilation)

- [Docker build](https://github.com/johnsonjh/cpm386#docker-build)

- [Build output](https://github.com/johnsonjh/cpm386#build-output)

- [QEMU testing](https://github.com/johnsonjh/cpm386#qemu-testing)

- [QEMU notes](https://github.com/johnsonjh/cpm386#qemu-notes)

- [Included utilities](https://github.com/johnsonjh/cpm386#included-utilities)

- [Contributing](https://github.com/johnsonjh/cpm386#contributing)

- [Future plans](https://github.com/johnsonjh/cpm386#future-plans)

- [Code statistics](https://github.com/johnsonjh/cpm386#code-statistics)

- [Mirrors](https://github.com/johnsonjh/cpm386#mirrors)

- [License](https://github.com/johnsonjh/cpm386#license)

## Overview

CP/M‑386 is currently in the very early development stages.

- Full 32‑bit [protected mode](https://en.wikipedia.org/wiki/Protected_mode)
implementation with
[Ring‑3 TPA](https://en.wikipedia.org/wiki/Protection_ring).

- Bootable via 3.5" 1.44MB floppy disk
[boot sector](https://en.wikipedia.org/wiki/Boot_sector) or
[Multiboot](https://en.wikipedia.org/wiki/Multiboot_specification) kernel.

- Supports [VGA text](https://en.wikipedia.org/wiki/VGA_text_mode) ( `0xB8000` )
and/or [COM1 serial](https://en.wikipedia.org/wiki/Serial_port)
(9600/N/8/1,  `0x3F8` ) consoles.

- No CD/USB/network/sound/other drivers (yet).

## Hardware support

- Compatible with 386 (and later systems) with 2MB (or more) memory.

- Systems using either PC BIOS or UEFI (with CSM) are supported.

- VGA, 8042 PS/2, 8250/16450/16550 UART, CMOS RTC, and 8253/8254 PIT
are supported.

## CP/M compatibility

CP/M‑386 should be highly source‑compatible with other implementations:

System
BDOS coverage

CP/M‑68K 1.3
100%

CP/M 2.2
100%

CP/M‑Plus
74%

DOS‑Plus
62%

MP/M 2.1
50%

The system currently reports BDOS 2.2 to applications.

- The CP/M‑386 BDOS is at full parity with CP/M‑68K 1.3 and
CP/M 2.2.

- A large majority of the CP/M‑Plus (CP/M 3) BDOS is also
supported.

- More than 60% of the DOS‑Plus additions have been implemented.

- Approximately half of the MP/M extensions have been completed.

- The missing functionality is largely the multi‑user, multi‑tasking,
message queuing, and process control calls that don't apply to a
single‑user CP/M implementation.

- Unique CP/M‑386‑specific BDOS extensions have been added to accommodate
new features like direct video access, high‑resolution timing, PRNG, etc.

## Build requirements

The following dependencies are required to compile CP/M‑386:

- [AWK](https://en.wikipedia.org/wiki/AWK)

- [Cpmtools](https://www.moria.de/~michael/cpmtools/files)†

- [GNU Binutils](https://www.gnu.org/software/binutils/)

- [GNU Coreutils](https://www.gnu.org/software/coreutils/)

- [GNU GCC](https://gcc.gnu.org/) or [LLVM Clang](https://clang.llvm.org)

- [GNU Make](https://www.gnu.org/software/make/)

- [LZ4](https://lz4.org/)

- [NASM](https://nasm.us/)

†Be sure to use  `cpmtools`  version 2.23 or later.  Older
versions may appear to work but have several known bugs.

## Optional dependencies

- [diff](https://en.wikipedia.org/wiki/Diff)

- [QEMU](https://www.qemu.org)

- [sed](https://en.wikipedia.org/wiki/Sed)

- [util-linux](https://en.wikipedia.org/wiki/Util-linux) (for  `column` )

## Downloads

- Download the
[current CP/M‑386 build](https://johnsonjh.gitlab.io/cpm386/cpm386.zip).

- View the
[GitLab CI/CD](https://gitlab.com/johnsonjh/cpm386/-/pipelines/latest) logs.

## Compilation

Building CP/M‑386 is supported on the current releases of NetBSD
and FreeBSD‡, as well as Red Hat Enterprise Linux 9 (or later),
CentOS Stream 9 (or later), and Fedora 36 (or later).

- GCC build (recommended):
 `make -Orecurse -j "$(nproc 2> /dev/null || printf '%s' 1)"` 

- Clang build:
 `make -Orecurse -j "$(nproc 2> /dev/null || printf '%s' 1)" CC="clang" OPTFLAGS="-O1"` 

- It is recommended to use GCC as Clang‑compiled i386 code is larger.

- Clang‑compiled builds will need to use  `OPTFLAGS=-O1`  (or  `-Os`  or
 `-Oz` ) to avoid exceeding the 384 KiB allocated for the ramdisk, or the
kernel size + Ring-0 stack exceeding conventional memory.

- Be sure to  `make clean`  if switching compilers or adjusting compiler flags.

- You may need to adjust the  `make -j`  argument depending on your operating
system (e.g.,  `gnproc` ,  `sysctl -n hw.ncpu` ,  `getconf NPROCESSORS_ONLN` ,
 `psrinfo -p` ).

- 32‑bit support libraries are required to run the test suite ( `make test` ).

- ‡At the time of writing, FreeBSD is shipping non‑functional
 `cpmtools2`  packages with broken  `mkfs.cpm`  functionality.  To successfully
build on FreeBSD, you must rebuild  `cpmtools`  and ensure it is not
linked with  `libdsk` .  If you receive a  `Disc rejected by driver`  error on
FreeBSD from  `mkfs.cpm` , your tools are broken and cannot be used to
build CP/M‑386.

## Docker build

If you are unable to build CP/M‑386 natively on your system, a
Docker‑based Fedora build is available.

- First, build the  `cpm386/cpm386-build`  container:
 `docker build --progress plain -t cpm386/cpm386-build:latest -f Dockerfile .` 

- Next, build CP/M‑386 using this container:
 `docker run --rm -v "$(pwd -P)":/src -w /src cpm386/cpm386-build:latest \
  make -Orecurse -j "$(nproc 2> /dev/null || printf '%s' 1)"` 

Additional targets (i.e.,  `clean` ,  `test` ,  `lint` ,  `update-readme` ) and
builds using the Clang compiler ( `CC="clang" OPTFLAGS="-O1"` ) are also
supported.

## Build output

- The build produces four primary artifacts:

File
Description

 `cpm386.elf` 
Multiboot kernel image

 `floppy.img` 
Bootable 3.5" 1.44MB floppy disk image

 `blankfd.img` 
Blank CP/M 3.5" 1.44MB floppy disk image

 `blankhd.img` 
Blank CP/M 8MB hard disk image

- The  `` [mboot.sh](https://github.com/johnsonjh/cpm386/blob/master/mboot.sh) convenience script (tested on GNU/Linux systems
with GRUB2) can be used to create bootable multiboot media (such as a USB
drive or SD card) using the  `cpm386.elf`  file.

- The  `floppy.img`  file can be written directly to a 1.44MB floppy disk.

- NOTE: This disk image does not contain a CP/M filesystem!
It can be removed from the drive once system is up and running.

- The blank images are useful because CP/M‑386 does not yet have a
 `FORMAT`  utility.

## QEMU testing

- [Multiboot](https://en.wikipedia.org/wiki/Multiboot_specification)
kernel (recommended):
 `qemu-system-i386 -m 2M -serial stdio -monitor none -kernel "cpm386.elf"` 

- Floppy [boot sector](https://en.wikipedia.org/wiki/Boot_sector) loader:
 `qemu-system-i386 -m 2M -serial stdio -monitor none -drive if=floppy,format=raw,file="floppy.img" -boot a` 

## QEMU notes

- Use  `-nographic -display none -vga none`  to disable VGA video (and use only serial console).

- Use  `-serial none`  to disable the serial UART (and use only VGA console).

- To attach media to QEMU, use:
 `-drive if=floppy,format=raw,file="blankfd.img"
-drive if=ide,format=raw,file="blankhd.img",index=0` 

## Included utilities

Program
Description

 `ACLOCKDV.386` 
[aclock](https://github.com/tenox7/aclock) (VGA text console version)

 `ACLOCKVT.386` 
[aclock](https://github.com/tenox7/aclock) (ANSI terminal version)

 `ALVTST.386` 
Get Allocation Vector test ( `DRV_ALLOCVEC` , [BDOS 27](https://www.seasip.info/Cpm/bdos.html))

 `CAPSLOCK.386` 
Caps‑Lock key behavior utility (BDOS 235)

 `CLEARTPA.386` 
Clears (zeros) and optionally verifies the TPA

 `CLS.386` 
Clear screen (BDOS 221)

 `DELAY.386` 
Delay test ( `P_DELAY` , [BDOS 141](https://www.seasip.info/Cpm/bdos.html#141))

 `DEMO.SUB` 
SUBMIT demonstration

 `DUMPDIR.386` 
Directory entry dump utility ( `F_SFIRST` / `F_SNEXT` , [BDOS 17](https://www.seasip.info/Cpm/bdos.html#17)/[18](https://www.seasip.info/Cpm/bdos.html#18))

 `DUMPFCB.386` 
File control block dump utility ( `F_OPEN` , [BDOS 15](https://www.seasip.info/Cpm/bdos.html#15))

 `ED.386` 
ED (A WIP port of the DRI CP/M Context Editor, August 1982)

 `ENV.DAT` 
Environment data file

 `ESCTILDE.386` 
Escape and Tilde key behavior utility (BDOS 237)

 `FPARSE.386` 
Filename parsing test ( `F_PARSE` , [BDOS 152](https://www.seasip.info/Cpm/bdos.html#152))

 `GETSN.386` 
Display serial number ( `S_SERIAL` , [BDOS 107](https://www.seasip.info/Cpm/bdos.html#107))

 `GFXTEST.386` 
Graphics and framebuffer demo (BDOS 229/230/231/233)

 `HD.386` 
Hex dump utility

 `HELLO.386` 
Hello world - the first CP/M‑386 program! ( `C_WRITESTR` , [BDOS 9](https://www.seasip.info/Cpm/bdos.html#9))

 `ILLEGAL.386` 
Ring‑3 protection and exception handler test

 `IOTEST.386` 
File I/O BDOS tests

 `JULIA.386` 
Draw a Julia set fractal (terminal version)

 `LRBC.386` 
Query and/or set Last Record Byte Count

 `LS.386` 
List files (with sizes)

 `MANDEL.386` 
Draw a Mandelbrot set fractal (terminal version)

 `MEM.386` 
Memory map utility (BDOS 227/228)

 `MORE.386` 
UNIX  `more` ‑style pager

 `NUMLOCK.386` 
Num‑Lock key behavior utility (BDOS 236)

 `OD.386` 
Octal dump utility

 `PAUSE.386` 
Wait for keypress ( `C_RAWIO` , [BDOS 6](https://www.seasip.info/Cpm/bdos.html#6))

 `PIP.386` 
PIP (A port of Zilog CP/M-Z8000 PIP v1.0A, January 1984)

 `PRINTENV.386` 
Print environment and system data

 `PRNG.386` 
PRNG test and demo utility (BDOS 253/254)

 `PROFILE.SUB` 
SUBMIT script (automatically executed at boot)

 `RC.386` 
Return code test and query ( `P_CODE` , [BDOS 108](https://www.seasip.info/Cpm/bdos.html#108))

 `README.TXT` 
Sample text file

 `REBOOT.386` 
Reboot utility (BDOS 220)

 `RM.386` 
UNIX  `rm` ‑like interactive file deletion utility ( `F_DELETE` , [BDOS 19](https://www.seasip.info/Cpm/bdos.html#19))

 `SEROFF.386` 
Disable serial console (BDOS 223)

 `SERON.386` 
Enable serial console (BDOS 223)

 `STAT.386` 
STAT (A port of Zilog CP/M‑Z8000 STAT v1.0C January 1984)

 `SYNC.386` 
Synchronize disks ( `DRV_FLUSH` , [BDOS 48](https://www.seasip.info/Cpm/bdos.html#48))

 `TERMTEST.386` 
Terminal and keyboard test utility

 `TEST110.386` 
String delimiter test ( `C_DELIMIT` , [BDOS 110](https://www.seasip.info/Cpm/bdos.html#110))

 `TEST211.386` 
Numeric format test ( `C_DECNUM` , [BDOS 211](https://www.seasip.info/Cpm/bdos.html#211))

 `TEXTMODE.386` 
Query and/or set the text mode and cursor state (BDOS 229/230/231/234)

 `TICKS.386` 
High‑resolution timer tests (BDOS 225/226)

 `TOD.386` 
Get (and set) Time of Day clock ( `T_SET` / `T_GET` , [BDOS 104](https://www.seasip.info/Cpm/bdos.html#104)/[105](https://www.seasip.info/Cpm/bdos.html#105))

 `TOUCH.386` 
Create an empty file ( `F_MAKE` , [BDOS 22](https://www.seasip.info/Cpm/bdos.html#22))

 `TRUNCATE.386` 
File truncation utility (LRBC aware)

 `TRUNCTST.386` 
Truncation tests ( `F_TRUNCATE` , [BDOS 99](https://www.seasip.info/Cpm/bdos.html#99))

 `TSEC.386` 
Get date and time ( `T_SECONDS` , [BDOS 155](https://www.seasip.info/Cpm/bdos.html#155))

 `VER.386` 
Display OS version ( `S_OSVER` , [BDOS 163](https://www.seasip.info/Cpm/bdos.html#163))

 `VGAFONT.386` 
Load a [text console font](https://github.com/viler-int10h/vga-text-mode-fonts) or restore the ROM font (BDOS 232)

 `VGAOFF.386` 
Disable VGA text console (BDOS 222)

 `VGAON.386` 
Enable VGA text console (BDOS 222)

 `VGATEXT.386` 
VGA text direct access demo (BDOS 224)

## Contributing

- Do not open pull requests with large amounts of LLM‑generated code.
These will be immediately rejected.

- There is no AI‑generated code in the core operating system at
this time (though there are AI‑generated tests, comments, and analysis),
as the project is intended to be as much of a learning experience for me as
it is a useful OS port.

- Usage of AI (artificial intelligence) tools by contributors is currently
permitted, subject to the same terms and conditions as the
[LLVM AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html), but
this permission may be withdrawn at any time and without notice.

## Future plans

See [FUTURE.md](https://github.com/johnsonjh/cpm386/blob/master/FUTURE.md).

## Code statistics

        
                Language
                Files
                Lines
                Blank
                Comment
                Code
                Complexity
                Bytes
                Uloc
        
        
                C
                74
                46383
                8781
                7916
                29686
                6065
                1281910
                17654
        
                C Header
                24
                3338
                646
                1481
                1211
                11
                123146
                1646
        
                Assembly
                8
                1939
                339
                418
                1182
                1
                47942
                999
        
                Makefile
                2
                1804
                346
                220
                1238
                382
                60008
                881
        
                Markdown
                3
                630
                76
                0
                554
                0
                26225
                486
        
                Shell
                1
                298
                88
                63
                147
                31
                8491
                116
        
                Linker Script
                2
                207
                39
                0
                168
                0
                5159
                96
        
                Dockerfile
                1
                97
                8
                12
                77
                35
                3197
                82
        
                YAML
                1
                87
                6
                15
                66
                0
                3875
                70
        
                Plain Text
                1
                53
                0
                0
                53
                0
                924
                53
        
        
                Total
                117
                54836
                10329
                10125
                34382
                6525
                1560877
                21976
        

## Mirrors

- The canonical home of this software is
 `` [https://gitlab.com/johnsonjh/cpm386](https://gitlab.com/johnsonjh/cpm386),
with a mirror on [GitHub](https://github.com/johnsonjh/cpm386).

## License

- CP/M‑386 is distributed under the terms of the permissive
[MIT License](https://github.com/johnsonjh/cpm386/blob/master/LICENSE).

- Bryan W. Sparks of DRDOS, Inc. dba DeviceLogics LLC, successor
in interest to Digital Research, Inc.’s CP/M assets, explicitly
grants an unlimited authorization to use, distribute, modify, enhance, and
otherwise make available CP/M technology, including the CP/M operating
systems and their derivatives.

## About

CP/M-386: CP/M for 386 protected mode, derived from CP/M-68K[gitlab.com/johnsonjh/cpm386](https://gitlab.com/johnsonjh/cpm386)

### Topics

[386](https://github.com/topics/386)[cpm](https://github.com/topics/cpm)[cpm22](https://github.com/topics/cpm22)[cpm3](https://github.com/topics/cpm3)[cpm386](https://github.com/topics/cpm386)[cpm68k](https://github.com/topics/cpm68k)[cpm86](https://github.com/topics/cpm86)[cpmplus](https://github.com/topics/cpmplus)

### Resources

[Readme](https://github.com/johnsonjh/cpm386#readme-ov-file)[MIT license](https://github.com/johnsonjh/cpm386#MIT-1-ov-file)

### Code of conduct

[Code of conduct](https://github.com/johnsonjh/cpm386#coc-ov-file)[Activity](https://github.com/johnsonjh/cpm386/activity)

### Stars

55 stars

### Watchers

1 watching

### Forks

[1 fork](https://github.com/johnsonjh/cpm386/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fjohnsonjh%2Fcpm386&report=johnsonjh+%28user%29)

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
