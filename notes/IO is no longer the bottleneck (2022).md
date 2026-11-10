---
title: "I/O is no longer the bottleneck? (2022)"
url: https://stoppels.ch/2022/11/27/io-is-no-longer-the-bottleneck.html
clipped: 2026-06-17 02:03:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [I/O is no longer the bottleneck? (2022)](https://stoppels.ch/2022/11/27/io-is-no-longer-the-bottleneck.html)

## Digest Summary
The post evaluates whether I/O has become the bottleneck for typical interview‑style text‑processing tasks. Measured sequential reads on the author's system reach 1.6 GB/s from a cold cache and 12.8 GB/s warm. An optimized C word‑frequency program (Ben Hoyt’s code) processes the 425 MiB “bible‑100.txt” at only 278 MiB/s (1.525 s). Moving the uppercase‑to‑lowercase conversion out of the main loop and letting clang vectorise raises throughput to ≈330 MiB/s, still far below raw read speed. The standard `wc -w` utility, which handles many delimiters, runs at ≈245 MiB/s (1.758 s). A hand‑written AVX2 implementation that scans 128‑byte blocks, broadcasts whitespace masks, and uses `PMOVMSKB` and bit‑trick loops achieves 1.45 GB/s on a warm cache (0.227 s) and ≈1.1 GB/s on a cold cache (0.395 s). Even with aggressive vectorisation, CPU‑bound parsing and hash‑map updates limit throughput to roughly 10‑15 % of raw sequential I/O, confirming that modern disk speeds are no longer the primary constraint.

## Discussion Summary
The discussion highlights that modern CPU performance is increasingly constrained by per‑core memory bandwidth, typically around 6 GB/s on x86 and up to 20 GB/s on Apple silicon, while advertised totals reflect all cores combined. It notes that even optimal parsers cannot surpass this limit for conventional formats like JSON and Protobuf, which require full parsing. Zero‑copy serialization is presented as a way to avoid the bottleneck, with the Lite³ format claimed to achieve dramatically higher throughput, and references are provided for further reading on related techniques.

---

## Full Article

I/O is no longer the bottleneck?
================================

*Nov 27th, 2022*

Recently Ben Hoyt [published a blog post](https://benhoyt.com/writings/io-is-no-longer-the-bottleneck/) claiming that contrary to popular belief, I/O is not the bottleneck in typical programming interview problems such as counting word frequencies from a stream. Sequential read speed has come a long way, while CPU speed has stagnated.

Sequential reads are indeed incredibly fast. Using the same method as linked in Ben Hoyt's post, I'm getting **1.6 GB/s** sequential reads on a cold cache, and **12.8 GB/s** on a warm cache (best of five).

But it should be possible to count word frequencies at a speed of 1.6 GB/s even on a single thread, right?

*(For the impatient: code is [available on GitHub](https://github.com/haampie/wc-avx2).)*

The optimized C implementation
------------------------------

Ben Hoyt's blog refers to an [earlier post](https://benhoyt.com/writings/count-words/) which includes a faster C version of the word frequency counter. I compiled `optimized.c` with GCC 12, using `-O3 -march=native` flags, and ran it on the 425MB input file (100 copies of the King James Version of the Bible).

The result was surprisingly bad:

```
$ time ./optimized < bible-100.txt > /dev/null

real    0m1.525s
user    0m1.477s
sys     0m0.048s
```

That is only **278 MB/s** on warm cache.

### Vectorization

Looking at the code I realized one of the hot loops had many branches, including an early exit, which prevents the compiler from vectorizing:

```
for (; i < num_process; i++) {
    char c = buf[i];
    if (c <= ' ') {
        break;
    }
    if (c >= 'A' && c <= 'Z') {
        c += ('a' - 'A');
        buf[i] = c;
    }
    hash *= FNV_PRIME;
    hash ^= (uint64_t)c;
}
```

My initial attempt to improve performance was to move this lowercase logic out of the loop, like so:

```
for (int i = 0; i < BUF_SIZE; ++i) {
    buf[i] = buf[i] >= 'A' && buf[i] <= 'Z' ?  buf[i] - 'A' + 'a' : buf[i];
}
```

This simple change improved performance to **330 MB/s** (using clang for better vectorization). Funnily enough, just adding these 3 lines before the loop, without deleting the original code gives comparable speed; strictly more work, but branch prediction does its job. Still, it's about a factor 5 away from cold cache sequential read speed.

Trying a simpler problem
------------------------

At this point I thought it was unlikely I could squeeze a lot of performance out of the word frequency counter. Sure, there are cache misses in the hash map, so maybe it could be optimized for better cache locality of common words. Or potentially short words can benefit from perfect hashing on the stack. But what will that give? Another 20%?

Instead, let's look at an informative baseline. Just count words without keeping track of frequencies; no tedious hash maps.

In fact there's a program for that: `wc -w`. Such a single-purpose tool must be fast, right?

```
$ time wc -w < bible-100.txt > /dev/null 

real    0m1.758s
user    0m1.718s
sys     0m0.040s
```

Unexpectedly the performance is terrible... **245.2 MB/s**. Why? Well, the man page says it's doing a different thing. The Ben Hoyt code only splits on `' '` whitespace, whereas `wc` uses `' '`, `'\n'`, `'\t'`, ... and even locale specific characters.

### How fast can word count be?

If the premise is that disk speed has caught up in the last decade, we should really be using new CPU features from that period. And that basically means: vectorize all the things. AVX2 is almost a decade old already. AVX-512 was available for the common people in 2017, but I'm on znver2, so I'll stick to AVX2.

Unfortunately, the compiler has a hard time autovectorizing word count. Maybe that proves the point of Ben Hoyt: disks got orders of magnitude faster "for free", but modern compilers don't magically generate machine code orders of magnitude faster. It's just difficult to translate branchy scalar programs into vectorized machine code.

### Masks

Part of word count can trivially be auto-vectorized: suppose for simplicity we have a register size of 128 bits, in which we can store 16 consecutive characters. It's easy to locate the whitespace by broadcasting it into a register ahead of time, and then doing a single `VPCMPEQB` comparsion operation:

```
       | 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 |
input: | h o w   m a n y   w o r d s   a | r e   h e r e ?
 mask: | 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 |
```

But after getting a mask in a vector register, how do you go about and count words? The only thing
I could think of is using a **Move Byte Mask** trick I've seen in [Cosmopolitan libc's  `strlen` implementation](https://github.com/jart/cosmopolitan/blob/b850b14300f112c238debf441746ef9ff93e8dba/libc/intrin/strlen.c#L32-L42). The relevant instruction `PMOVMSKB` moves the long bit mask into a 32 bit `int`, and then you do your usual bit tricks.

### Bit tricks

What are the usual bit tricks? One great candidate is **Find First Set** or `ffs` in short — this is a great name given how tedious it is to get bit tricks right. This instruction can be used to iterate over set bits, like so:

```
#include <stdio.h>

int main() {
    int mask = 0b0100000100001000;
    int prev = 0;
    while (mask) {
        int curr = __builtin_ffs(mask);
        if (curr > prev + 1)
            printf("Word start at %d\n", curr);
        prev = curr;
        if (curr == 32) // don't ask, sigh.
            break;
        mask = (mask >> curr) << curr;
    }
}
```

It outputs the following, corresponding to the mask example above:

```
Word start at 4
Word start at 9
Word start at 15
```

### Putting it together

I ended up writing this code explicitly using `immintrin.h` which is an absolutely dreadful experience. Next time I'll use a high-level API (in the past I've had a lot of fun vectorizing things interactively in the Julia REPL with [VectorizationBase.jl](https://github.com/JuliaSIMD/VectorizationBase.jl)). But at least I felt like I had some control over the generated machine code.

Using AVX2 with 256-bit registers, you need to align your data on 32 bits, which I did (of course not without messing it up first). I reserved 6 of the registers to hold all broadcasted whitespace characters. Then I explicitly unrolled the vectorized loop 4 times, so in every iteration we process 128 bytes of data.

It took an awful lot of time to fix the off-by-one bugs, but in the end I managed to get a working program, tested against a non-zero amount of text files on my computer:

```
$ ./wc-avx2 < bible-100.txt 
82113300
$ wc -w < bible-100.txt 
82113300
```

So, how fast?!

```
$ time ./wc-avx2 < bible-100.txt 
82113300

real    0m0.227s
user    0m0.186s
sys     0m0.041s
```

That comes down to **1.45 GB/s** (on a warm cache).

Sigh. So hand-optimized, single-threaded word count is only getting about 11% of the sequential disk read speed. And on a cold cache?

```
$ sysctl -w vm.drop_caches=3
$ time ./wc-avx2 < bible-100.txt
82113300

real    0m0.395s
user    0m0.196s
sys     0m0.117s
```

Still more time in *user* than *sys* :(. So yeah, maybe the disk speed has caught up statement is indeed true.

### Get the code

I've put my [code up on GitHub](https://github.com/haampie/wc-avx2). If you know better bit-tricks, feel free to submit a pull request.