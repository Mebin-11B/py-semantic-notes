---
title: "Infographics: Operation Costs in CPU Clock Cycles, Take 2 - 6IT"
url: https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736
clipped: 2026-08-31 12:26:31
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Infographics: Operation Costs in CPU Clock Cycles, Take 2 - 6IT](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736)

## Full Article

[6IT.Dev](https://6it.dev/)

[Hare on Soft.ware](https://6it.dev/blog/page/1)

###### 

[6IT HareOn Soft.ware](https://6it.dev/blog/page/1)CategoryCategoryBook: D&D of MOGs

[Table of Contents](https://6it.dev/blog/page/1?category=book-dd-of-mogs&subcategory=table-of-contents)[1st beta of Vol. I-III](https://6it.dev/blog/page/1?category=book-dd-of-mogs&subcategory=1st-beta-of-vol-i-iii)[1st beta of Vol. IV-VI](https://6it.dev/blog/page/1?category=book-dd-of-mogs&subcategory=1st-beta-of-vol-iv-vi)[1st beta of Vol. VII-IX](https://6it.dev/blog/page/1?category=book-dd-of-mogs&subcategory=1st-beta-of-vol-vii-ix)On.System Architecture

[Requirement analysis](https://6it.dev/blog/page/1?category=onsystem-architecture&subcategory=requirement-analysis)[Design decisions](https://6it.dev/blog/page/1?category=onsystem-architecture&subcategory=design-decisions)[Distributed systems](https://6it.dev/blog/page/1?category=onsystem-architecture&subcategory=distributed-systems)[(Re)Actors](https://6it.dev/blog/page/1?category=onsystem-architecture&subcategory=reactors)On.Programming

[Tips and Tricks](https://6it.dev/blog/page/1?category=onprogramming&subcategory=tips-and-tricks)[Network Programming](https://6it.dev/blog/page/1?category=onprogramming&subcategory=network-programming)[Programming Languages](https://6it.dev/blog/page/1?category=onprogramming&subcategory=programming-languages)[Optimizations](https://6it.dev/blog/page/1?category=onprogramming&subcategory=optimizations)[Debugging](https://6it.dev/blog/page/1?category=onprogramming&subcategory=debugging)[Embedded](https://6it.dev/blog/page/1?category=onprogramming&subcategory=embedded)On.Hardware

[MCU](https://6it.dev/blog/page/1?category=onhardware&subcategory=mcu)[Wi-Fi](https://6it.dev/blog/page/1?category=onhardware&subcategory=wi-fi)On.Security

[Best Practices](https://6it.dev/blog/page/1?category=onsecurity&subcategory=best-practices)[Fraud Prevention](https://6it.dev/blog/page/1?category=onsecurity&subcategory=fraud-prevention)[Research](https://6it.dev/blog/page/1?category=onsecurity&subcategory=research)On.Development

[Development Philosophy](https://6it.dev/blog/page/1?category=ondevelopment&subcategory=development-philosophy)[Development Processes](https://6it.dev/blog/page/1?category=ondevelopment&subcategory=development-processes)[Team structure](https://6it.dev/blog/page/1?category=ondevelopment&subcategory=team-structure)[IT Careers & IT Hiring](https://6it.dev/blog/page/1?category=ondevelopment&subcategory=it-careers--it-hiring)Other

[Announcements](https://6it.dev/blog/page/1?category=other&subcategory=announcements)[Reports](https://6it.dev/blog/page/1?category=other&subcategory=reports)IT Hare School

[IT Hare school for dinosaurs](https://6it.dev/blog/page/1?category=it-hare-school&subcategory=it-hare-school-for-dinosaurs)[For dummies by dummies](https://6it.dev/blog/page/1?category=it-hare-school&subcategory=for-dummies-by-dummies)Much Ado About Hare

[Real People Behind The Hare](https://6it.dev/blog/real-people-behind-the-hare-1769?category=much-ado-about-hare)[Write for Us](https://6it.dev/blog/write-for-us-1774?category=much-ado-about-hare)[H.A.R.E. and Bunnylore](https://6it.dev/blog/hare-and-bunnylore-1764?category=much-ado-about-hare)

# Infographics: Operation Costs in CPU Clock Cycles, Take 2

June 19, 2026 by â¢ [âNo Bugsâ Bunny](https://6it.dev/blog/page/1?author=no-bugs-bunny-493) â¢ 

translated byÂ SherryÂ Ignatchenko

[âNo Bugsâ Bunny](https://6it.dev/blog/page/1?author=no-bugs-bunny-493)Sarcastic Architect

    

Hobbies: 
Thinking Aloud,Â Arguing with Managers,Â Annoying HRs,
Calling a Spade a Spade,Â Keeping Tongue in Cheek

This is a DRAFT of the second part of Chapter 4 - On CPU Physics and CPU Cycles, of the Vol.1 of an upcoming book "Efficient C++ Programming for Modern 64-bit CPUs" by Sherry Ignatchenko and Dmytro Ivanchykhin. Feel free to comment on it - especially if you see some factual inconsistencies, we'll be happy to fix them.

For the first part of Chapter 4, see [https://6it.dev/blog/on-cpu-physics-and-cpu-cycles-80730](https://6it.dev/blog/on-cpu-physics-and-cpu-cycles-80730).

## 

## Cold Hard Numbers

Now, armed with all the information above (and adding bits from [[Ignatchenko16a]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Ignatchenko16a), [[Fog]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Fog), and other sources listed below), we can make an all-important diagram to replace micro-benchmarks for many practical purposes, and indicate costs of most popular operations in the devâs vocabulary. 

DISCLAIMER: all the numbers below are accurate only within an order of magnitude!

Note that some of the items here were not discussed above, and may need some additional explanation:

### Multiplication / Division

Out of all the R-R operations out there, multiplication and especially division are rather special performance-wise. All the integer ops besides multiplication and division are Darn Cheapâ¢ - they usually tend to have latencies along the lines of 1, or if this particular op was deemed not-so-important by CPU designers â 2 CPU cycles; moreover, for non-multiply/divide ops usually there is no difference whatsoever depending on the bitness of the operands: that is, any op besides multiplication and division tends to take the same time for 8-bit, 16-bit, 32-bit, and 64-bit operands.

In contrast, multiplication tends to take 3-5 CPU cycles, and moreover, it may take a different number of CPU cycles for 32-bit and 64-bit operands. For divisions, it is even worse: even modern CPUs tend to take as much as 15 CPU cycles for 64-bit divisions (and we should be thankful even for these numbers, as [[Fog]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Fog) lists them at 100+ CPU cycles, ouch!).
For more recent CPUs, [[uops]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-uops) and [[Cortex-A78]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Cortex-A78) give us the following operation latencies (in CPU cycles):

Skylake-X (2017)

Zen 2 (2019)

Cortex-A78 (2020)

Alder Lake-P (2021)

Alder Lake-E (2021)

Zen 4 (2022)

Arch

x64/Intel

x64/AMD

AArch64

x64/Intel

x64/Intel

x64/AMD

IMUL R32, R32

3

3

2 (MUL, W-form)

3

3

3

IMUL R64, R64

3

3

2 (MUL, X-form)

3

5

3

IDIV R32

23-28

8-25

5-12 (DIV, W-form)

10-15

11-28

9-14

IDIV R64

37-96

8-41

5-20 (DIV, X-form)

14-18

11-24

9-19

To summarize it (for really modern 64-bit CPUs, i.e. roughly starting from 2019-2021):Â 
- in spite of all the improvements made, division is still Darn Expensiveâ¢ (though not as atrociously expensive as it used to be)
- while since about 2020, the difference between 32-bit and 64-bit division is not that drastic, it still exists
- as for multiplication â it is almost the same for 32-bit and 64-bit versions (except for certain E-cores).

TODO: add floating-point multiplication/division

### RTTI

RTTI can be quite expensive, with  `dynamic_cast<>`  being up to 5x more expensive than a simple virtual function call (sic!) [[TR]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-TR)[[Didriksen]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Didriksen). 

TODO: benchmark performance of virtual call vs typeid vs dynamic_cast (sources give very conflicting and potentially-outdated data, need to experiment ourselves)

Note though, that contrary to certain claims (see e.g. [[Fog04, section 7.23]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Fog04)), RTTI doesnât add anything to the instances of the class objects (for polymorphic classes, RTTI uses the same vfptr which is already there, and for non-polymorphic ones there is no RTTI at all). Still, RTTI does add to the code size.

### C++ Exceptions vs Return-value-and-check

C++ has long took a position that its exceptions are designed to be more efficient than C-style return-error-and-check-it. And in fact, for code where errors are extremely rare, it seems to stand. For example, micro-benchmarks from [[Nayar]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Nayar) indicate that return with error code takes 2 CPU cycles more than return without error code. OTOH, whenever C++ exception does happen, it costs a Damn Lotâ¢ - per [[Ongaro]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Ongaro), exceptions cost around 5â000 cycles (sic!), and per [[Nayar]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Nayar) â around 2â700 cycles. It means that if we have 1 exception per 100 function calls  â weâd be better using returns, but anywhere from 10â000 successful calls per exception and up â C++ exceptions win. 

Yes, we know that this goes against [[Fog04]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Fog04)âs claim of âAll functions have to save some information for the exception handler, even if no exception ever happens.â â but this statement is hopelessly outdated by 2026; this observation from [[Fog04]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Fog04) most likely refers to storing unwinding information within specially adjusted stack frames (see âThe Code Approachâ in [[TR, section 5.4]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-TR)), but for a long while all major compilers implement âThe Table Approachâ from the same section in [[TR]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-TR), which is currently commonly referred to as âzero-cost exceptionsâ.

### Atomics, CAS, and LL/SC

### FSB

Front-Side Bus

Historically, atomic operations (in particular, CAS=compare-and-swap) were introduced in FSB-based architectures using system-wide âLOCKâ over the FSB. These days, however, FSB being gone since early 2000s (thanks AMD64 and Opteron which pioneered switch to NUMA in x86/x64 world), it is all about some cache coherence protocol, usually some variation of MESI. As for cpu cycles involved, [[AlBahra]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-AlBahra) provides an estimate of about 15 CPU cycles for a CAS operation; for multi-socket NUMA scenarios, however, it can easily get up to 300-600 cycles.

In addition, atomics tend to have some unpleasant side-effects going beyond direct increase in latency; in times of FSB, atomics used to cause a global bus lock, which meant an observable performance hit on multi-core / multi-socket systems; these days, with FSB replaced with NUMA and MESI-like protocols, situation got better, but is still causing quite significant effects such as â[preventing] instruction level parallelism, significantly limiting the bandwidth (up to 30x in comparison with simple writes), even if there are no dependencies between the successive operationsâ [[SchweizerEtAl]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-SchweizerEtAl); see also [[Josuttis]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Josuttis) for a discussion on related effects such as write stalls.

### LL/SC

Load-Link / Store-Conditional. Store-conditional stores data only if there have been no updates to the location since the preceding Load-Link. 

Letâs also note that atomics support under RISC-V is not CAS-oriented, it is LL/SC oriented, with its own set of advantages and quirks; recent ARMs support both LL/SC and CAS, and x64 is traditionally CAS-oriented.

### Function Calls and Inlining

Historically, [[BulkaMayhew, p.115]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-BulkaMayhew) estimated the CPU cost of a function call at around 25â250 cycles, depending on the number of parameters. However, the book from 2000 feels quite dated now, and we havenât found a reasonably authoritative modern reference ð. That being said, based on our own experience, a function with a modest number of parameters tends to cost more like 15â30 cycles. â in direct costs, that is. This observation also seems consistent for non-Intel CPUs, as noted by [[Ruskin]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Ruskin).

As for indirect calls (calls via function pointer), [[Ignatchenko16a]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Ignatchenko16a) gives an estimate of 20-50 cycles, and for C++ virtual function costs â 30-60 cycles, which seems to be consistent with [[Ruskin]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Ruskin) too.
Last but not least, we need to consider what happens when compiler inlines a function. In such a case, not only we no longer incur those direct costs of function call (whether the call itself is direct, or indirect, or virtual) â but also compiler, after inlining, will optimize caller-function plus inlined callee-function as a whole.  Just as one example â if we have code like 
 `int square(int x) { 
  return x*x;
}
int cube(int x) {
  return x*x*x;
}
int g(int x) { 
  return square(x) + cube(x);
}
` 

, then when  `g()` Â  is compiled with  `square()` Â  and  `cube()`  inlined, x64 Clang  reduces it into simple  `mov  eax, edi
imul eax, eax
imul edi, eax
add  eax, edi` 

- as we can see, there are only 2 multiplications and one addition. 
However, when prohibiting inlining, effective generated code (even besides extra  `mov` Â s,  `push` Â es/ `pop` Â s, and manipulations with stack pointer which can be attributed to direct function call costs), results in 3  `imul` Â s, and 1  `add` Â , i.e. at least one  `imul` Â  was not optimized out due to lack of inlining. In other words â within non-inlined code, at least one  `imul` Â  represents lost opportunity cost due to lack of inlining. Which makes perfect sense BTW â if we think about it a bit, weâll realize that without inlining, such an optimizing out of an extra  `imul` Â  (by realizing that calculation of  `square()` Â  can be used as a part of calculation within  `cube()` Â , so compiler effectively rewrites  `x*x+x*x*x` Â  into  `(x*x)*(1+x)` Â , saving one multiplication) is not possible at all (sic!). And in practice, such lost opportunity costs can easily go into many dozens of CPU cycles; as another example â if we have two calls of a function  `f()` Â  with the same params, where  `f()` Â  can be arbitrarily expensive, compiler cannot optimize the second call to  `f()` Â  out until it is inlined (hey, what if  `f()` Â  has side effects?), but as soon as it can see the body of  `f()` Â  â it has enough information to realize âhey, it has no side effects, so we can optimize second call out!â. See also examples of inlining saving the day in [TODL: hint # about non-mutable semantics], and discussion on [[Carruth19]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Carruth19) in Chapter 12.

Letâs note (as it was highlighted by [[Godbolt19]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-Godbolt19)), that some (though not all) optimizations-enabled-by-inlining are not actually about inlining per se, theyâre about visibility of the function body to the compiler (see e.g. our example above re second call to function  `f()` ); OTOH, assuring visibility without inlining, while potentially possible (say, by declaring function in header with force-uninlining) is usually not too practical, so overall adage of âinlining helps compiler to optimizeâ still stands. 

### Thread Local Storage

Those  `thread_local` Â  variables (compared to direct access to data) are not free; moreover, implementations under different compilers vary significantly even for one single platform; while last time we checked, for x64 under GCC and Clang pointer to TLS was actually stored in FS register, and TLS access comes at a cost of one extra indirection, under MSVC it may incur up to 3 extra indirections â and while these places accessed are usually well-cached, theyâre still indirections, which raises the costs of accessing a  `thread_local`  variable ð. 

### Thread Context Switches

As for thread context switches, the general consensus is that theyâre âdamn expensiveâ (after all, it is most likely a reason why nginx outperforms Apache). But how expensive is âdamn expensive,â really?
From our own experience, context switches tend to cost somewhere between 10â000 and 100â000 CPU cycles. This goes well with some related real-world observations; for example, for Windows/x64 CRITICAL_SECTION, the default spin count  is 4000 iterations. It means that it usually makes sense to burn through 4000 spins â consuming at least 15â20K CPU cycles, and sometimes more like 40â50K â just waiting for a lock with the only aim being to avoid that Damn Thread Context Switchâ¢ (and with a chance that all 4000 spins are wasted and we go into the context switch anyway, incurring both costs of spinning, and costs of thread context switch!). Of course, that strongly implies the context switch spinlock tries to avoid, is significantly more expensive than those 15-50K CPU cycles wasted spinning.
That being said, many sources report much lower number. The discrepancy arises from the fact that it depends heavily on what exactly you're measuring. As [[LiEtAl]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-LiEtAl) explains, there are two different kinds of costs associated with context switching.

First, thereâs the direct cost of switching threads. This is the relatively lightweight part â typically around 2,000 CPU cycles.
But the indirect cost â primarily due to cache invalidation â tends to be much more significant. According to [[LiEtAl]](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#ref-LiEtAl), this can reach up to 3 million CPU cycles. Theoretically, with a completely random memory access pattern, a modern CPU with a 12MB L3 cache (and assuming around 150 cycles per cache miss - that's comparing L3 access to main memory access) could experience penalties up to 30 million cycles per context switch. In practice, though, itâs usually less severe, but even 1 million cycles clearly qualifies as âdamn expensiveâ.

### References

[Ignatchenko16a] [S. Ignatchenko, Operation Costs in CPU Clock Cycles](http://ithare.com/infographics-operation-costs-in-cpu-clock-cycles/) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Ignatchenko16a-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Ignatchenko16a-2) 

[Fog] [Agner Fog, Instruction tables. Lists of instruction latencies, throughputs and micro-operation breakdowns for Intel, AMD, and VIA CPUs](https://www.agner.org/optimize/instruction_tables.pdf) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Fog-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Fog-2) 

[uops] [uops.info table](https://uops.info/table.html) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-uops-1) 

[Cortex-A78] [ArmÂ® CortexÂ®-A78 Software Optimization Guide](https://developer.arm.com/documentation/102160/latest/) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Cortex-A78-1) 

[TR] [Technical Report on C++ Performance](https://www.open-std.org/jtc1/sc22/wg21/docs/TR18015.pdf) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-TR-1) [section 5.4 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-TR-2) [3 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-TR-3) 

[Didriksen] [Tino Didriksen, C++ dynamic_cast Performance](https://tinodidriksen.com/2010/04/cpp-dynamic-cast-performance/) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Didriksen-1) 

[Fog04] [Agner Fog, Optimizing software in C++](https://agner.org/optimize/optimizing_cpp.pdf) [section 7.23 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Fog04-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Fog04-2) [3 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Fog04-3) 

[Nayar] [Amit Nayar, Investigating the performance overhead of C++ exceptions](https://www.nutrient.io/blog/performance-overhead-of-exceptions-in-cpp/) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Nayar-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Nayar-2) 

[Ongaro] [Diego Ongaro, The Cost of Exceptions in C++](https://ongardie.net/blog/exceptions/) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Ongaro-1) 

[AlBahra] [Samy Al Bahra, Nonblocking Algorithms and Scalable Multicore Programming](https://queue.acm.org/detail.cfm?id=2492433) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-AlBahra-1) 

[SchweizerEtAl] [Hermann Schweizer, Maciej Besta, and Torsten Hoefler, Evaluating the Cost of Atomic Operations on Modern Architectures](https://htor.inf.ethz.ch/publications/img/atomic-bench.pdf) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-SchweizerEtAl-1) 

[Josuttis] [Nicolai Josuttis, The Price of Shared Pointers or Why Passing them by-reference can be Useful](https://www.youtube.com/watch?v=drhIIbmrjzg) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Josuttis-1) 

[BulkaMayhew] [Dov Bulka, David Mayhew, Efficient C++: Performance Programming Techniques](https://www.amazon.ca/Efficient-C-Performance-Programming-Techniques/dp/0201379503) [p.115 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-BulkaMayhew-1) 

[Ruskin] [Elan Ruskin, HOW SLOW ARE VIRTUAL FUNCTIONS REALLY?](https://web.archive.org/web/20210225014950/http://assemblyrequired.crashworks.org/how-slow-are-virtual-functions-really/) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Ruskin-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Ruskin-2) 

[Carruth19] [Chandler Carruth, There Are No Zero-cost Abstractions](https://www.youtube.com/watch?v=rHIkrotSwcc) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Carruth19-1) 

[Godbolt19] [Matt Godbolt, Optimizations in C++ Compilers](https://queue.acm.org/detail.cfm?id=3372264) [â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-Godbolt19-1) 

[LiEtAl] [Chuanpeng Li, Chen Ding, Kai Shen, Quantifying The Cost of Context Switch](https://www.usenix.org/legacy/events/expcs07/papers/2-li.pdf) [1 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-LiEtAl-1) [2 â©](https://6it.dev/blog/infographics-operation-costs-in-cpu-clock-cycles-take-2-80736#cite-LiEtAl-2) Tagged With: [C/C++](https://6it.dev/blog/page/1?tag=ccpp)

## Comments

### Leave a Comment

Your email address will not be published. Required fields are marked *Comment *Name *Email *WebsiteSave my name, email, and website for the next time I comment.POST COMMENT

This site uses Akismet to reduce spam. [Learn how your comment data is processed](https://akismet.com/privacy/)

SixÂ ImpossibleÂ ThingsÂ BeforeÂ BreakfastÂ Ltd. Â©Â 2026.Â AllÂ rightsÂ reserved.
