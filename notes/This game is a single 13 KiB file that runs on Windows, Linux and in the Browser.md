---
title: "This game is a single 13 KiB file that runs on Windows, Linux and in the Browser"
url: https://iczelia.net/posts/snake-polyglot/
clipped: 2026-06-17 02:00:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [This game is a single 13 KiB file that runs on Windows, Linux and in the Browser](https://iczelia.net/posts/snake-polyglot/)

## Digest Summary
A 13 KB single‑file Snake game runs natively on Windows, Linux, and in browsers. The author built three separate implementations—C with WinAPI for i686 Windows, C with X11 for x86_64 Linux, and JavaScript using HTML5 Canvas—each 3–5 KB compiled/minified. The Windows binary uses a custom PE header that embeds a shell script; a decompressing stub expands a compressed payload, and Windows app‑help suppresses an initial 0xc0000005 error after the first run. The Linux version wraps an LZMA‑compressed ELF64 binary in a shell dropper that extracts and executes the payload while skipping the wrapper. The browser version places harmless garbage before the HTML, then hides it via CSS. All three components are concatenated so each OS selects its appropriate segment, producing a final 13 312‑byte file. Gameplay follows classic Snake rules: arrow/WASD control, ESC to quit, R to reset, P to pause, space to start; food yields 10 points (20 for rare yellow fruit), a new level after ten foods randomizes a maze guaranteeing a path to food, and snake speed scales with length.

## Discussion Summary
The comments express strong admiration for how minimal binaries can deliver rich experiences, noting the impressiveness of size‑reduction tricks such as embedding the dynamic linker path in unused header fields. Readers show curiosity about whether these optimizations are manual or tool‑driven and request robust analysis tools that tolerate unconventional executables. Experiences running the program across browsers, Linux, and Windows highlight practical challenges and solutions, while the discussion extends to similar compact projects, praising the elegance of single‑file, polyglot applications and encouraging further experimentation.

---

## Full Article

![cover](https://iczelia.net/media/cover-snake-polyglot.png)

Not that long ago I became aware of Justine Tunney's [cosmopolitan libc](https://github.com/jart/cosmopolitan) project. It's a toolkit that allows you to compile C source code into a single binary that runs natively on multiple operating systems, including Windows, Linux, various flavours of BSD, even including booters.

Unfortunately, back then the project didn't seem to support GUI interfaces and produces quite swollen binaries. Hence I decided to take a stab at a similar (simpler? harder? up to you to decide) challenge: create a video game (<16 KiB) that runs natively on Windows, Linux and in the Browser, all from a single source file.

The Game [⎇](https://iczelia.net/posts/snake-polyglot/#the-game)
----------------------------------------------------------------

It's a pretty standard Snake game with the same rules and interface on all platforms. You control a snake that grows longer as it eats food, and the goal is to avoid running into walls. The snake is controlled using either the arrow keys or WASD keys. It can be terminated via `ESC` (if permissible by the platform), reset via `R`, and paused via `P`. Spacebar starts the game.

The game keeps track of your score. Each piece of food eaten increases your score by 10 points, except yellow fruit (which spawns with a 15% chance) that gives you 20 points. Fruit spawns at a fixed rate and despawns after a certain time if not eaten. The despawn timer is proportional to the speed of the snake at the time of spawning, which itself is proportional to the snake's length.

Once ten fruit are eaten, the game proceeds to the next level, randomizing the walls' layout. The maze is created as to ensure that there is always a path from the snake's head to any piece of food. The initial placement of the snake is also randomized, but always in a position that has at least five empty tiles in the direction the snake is facing.

[**Download the game here (13,772 bytes)**](https://iczelia.net/media/ede115f31fb3fcc3c27bad1b6da5cfee30bd692c3fc04ca1e8f0e8f43787b66f.com).

The Polyglot [⎇](https://iczelia.net/posts/snake-polyglot/#the-polyglot)
------------------------------------------------------------------------

I implemented the game three times in total: once in C for the i686 Visual C platform using WinAPI, once in C for the x86\_64 Linux platform using clang and X11, and once in JavaScript for the browser using HTML5 Canvas. Each implementation is around 3-5 KiB in size when compiled/minified.

The Windows implementation was produced using a compressing script that prepends a decompressing stub. This stub has a quite unusual PE header that has many freely controllable bytes after the `MZ` signature. This allows us to place a shell script there that skips over the remainder of the file, rendering the (valid) PE executable runnable on Windows while also making the entire file a valid shell script, that will do (thus far) nothing on Linux.

Because the PE file is so awkward, we rely on Windows' apphelp mechanism. Without compatibility mode, executing for the first time will yield the message:

> "The application was unable to start correctly (0xc0000005). Click OK to close the application."

Which should disappear after re-running.

The Linux implementation was produced using a similar approach; we use `lzma` for decompression and a small shell dropper that extracts the compressed ELF64 binary and runs it, skipping over the head and the tail of the file.

The HTML version is also packed and abuses the fact that browsers will happily process all the benign garbage at the start of the file before reaching the actual HTML content. Then we make it invisible/unobtrusive through a bit of CSS magic.

Finally, we concatenate all three files together in such an order that each platform will pick the correct part of the file to execute. The final file is exactly 13,312 bytes in size.

Technical Details [⎇](https://iczelia.net/posts/snake-polyglot/#technical-details)
----------------------------------------------------------------------------------

```
0000: 4d5a 3d3b 3a3c 3c27 6b73 270a 5045 0000  MZ=;:<<'ks'.PE..  <- Windows PE header start
0010: 4c01 0000 01db 617f 10d0 1773 7947 ebf9  L.....a....syG..     As shell script: assign to MZ,
[Snip: i686 Windows code.]                                          start ignored heredoc to skip
1040: c6aa 3cb1 246e a942 ae6f 3e70 4979 9c58  ..<.$n.B.o>pIy.X     to the 'ks' marker.
1050: 344d 2d09 88b1 fbd3 9e68 401c bfff e5ab  4M-......h@.....
1060: cba1 731a 6b79 6c04 54df 9602 0a6b 730a  ..s.kyl.T....ks.  <- 'ks' marker
1070: 7461 696c 202d 632b 3432 3934 2024 307c  tail -c+4294 $0|  <- Drop 4292 bytes (PE), keep 5061 (ELF).
1080: 6865 6164 202d 6320 3530 3631 7c6c 7a6d  head -c 5061|lzm  <- Decode into /tmp/a, mark executable,
1090: 6120 2d64 633e 2f74 6d70 2f61 3b63 686d  a -dc>/tmp/a;chm     run and cleanup.
10a0: 6f64 202b 7820 2f74 6d70 2f61 3b28 2f74  od +x /tmp/a;(/t
10b0: 6d70 2f61 2672 6d20 2f74 6d70 2f61 293b  mp/a&rm /tmp/a);
10c0: 6578 6974 0a5d 0000 4000 ffff ffff ffff  exit.]..@.......
10d0: ffff 003f 9145 8468 3d89 a6da 8acc 93e2  ...?.E.h=.......
10e0: 4ed9 0498 44e9 9d40 f246 7273 6131 ea63  N...D..@.Frsa1.c
[Snip: LZMA-packed x86_64 Linux code.]
2460: de86 e198 4589 dc46 cd5b c84f 6218 4861  ....E..F.[.Ob.Ha
2470: 16af 0622 18a1 8a86 371d 2b5a 7948 7761  ..."....7.+ZyHwa
2480: 6439 4cc7 27ff fbda fb1c 3c68 746d 6c3e  d9L.'.....<html>  <- Start of HTML content
2490: 3c74 6974 6c65 3e53 6e61 6b65 3c2f 7469  <title>Snake</ti
24a0: 746c 653e 3c73 7479 6c65 3e64 6976 7b68  tle><style>div{h
24b0: 6569 6768 743a 3130 3025 3b6d 6172 6769  eight:100%;margi
24c0: 6e3a 303b 6261 636b 6772 6f75 6e64 3a23  n:0;background:#
24d0: 3163 3163 3163 7d64 6976 7b64 6973 706c  1c1c1c}div{displ
24e0: 6179 3a67 7269 643b 706c 6163 652d 6974  ay:grid;place-it
24f0: 656d 733a 6365 6e74 6572 7d63 616e 7661  ems:center}canva
2500: 737b 696d 6167 652d 7265 6e64 6572 696e  s{image-renderin
2510: 673a 7069 7865 6c61 7465 643b 6f75 746c  g:pixelated;outl
2520: 696e 653a 307d 2a7b 6d61 7267 696e 3a30  ine:0}*{margin:0  <- CSS to hide the garbage
2530: 3b70 6164 6469 6e67 3a30 3b66 6f6e 742d  ;padding:0;font-     and the padding of elements.
2540: 7369 7a65 3a30 3b7d 3c2f 7374 796c 653e  size:0;}</style>
2550: 3c64 6976 3e3c 6361 6e76 6173 2068 6569  <div><canvas hei
2560: 6768 743d 2234 3830 2220 6964 3d22 6322  ght="480" id="c"
2570: 2074 6162 696e 6465 783d 2230 2220 7769   tabindex="0" wi
2580: 6474 683d 2236 3430 223e 3c2f 6361 6e76  dth="640"></canv
2590: 6173 3e3c 2f64 6976 3e3c 7363 7269 7074  as></div><script
[Snip: Packed JavaScript code for the game.]
3590: 5d2f 2e65 7865 6328 7229 3b29 7769 7468  ]/.exec(r);)with
35a0: 2872 2e73 706c 6974 2861 2929 723d 6a6f  (r.split(a))r=jo
35b0: 696e 2873 6869 6674 2829 293b 6576 616c  in(shift());eval
35c0: 2872 293c 2f73 6372 6970 743e            (r)</script>
```