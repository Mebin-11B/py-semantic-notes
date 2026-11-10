---
title: "Assembly Hall of Shame"
url: https://github.com/xoreaxeaxeax/asm-hall-of-shame
clipped: 2026-08-31 12:22:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Assembly Hall of Shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame)

## Digest Summary
The “Assembly Hall of Shame” (github.com/xoreaxeaxeax/asm‑hall‑of‑shame) benchmarks the absolute worst‑case latency of single x86 instructions by crafting micro‑architectural stalls rather than optimizing speed. Each entry records a single scored instruction, the timing method, and the resulting cycle count (normalized to the CPU base clock).  
Key strategies include: loading 512 B FPU/MMX/XMM state with fxrstor64 from a high‑latency PCIe MMIO region while other cores hammer a different MMIO register, forcing the load to queue behind non‑posted transactions; unaligned vmovdqu loads that trigger GPU‑side non‑posted accesses; lock‑prefixed memory ops straddling cache‑line boundaries to invoke external bus locks; subnormal floating‑point operands that invoke microcode assists; saturating write‑combining buffers with many movnti stores followed by mfence; exhaustive cache dirtying to force DRAM write‑back; MSR writes to high‑latency registers (e.g., MCG_CTL); and exhausting the hardware entropy pool.  
Reported latencies range from 1 cycle (nop) to 198 000 000 000 000 cycles (≈62 s) on an AMD Ryzen 7 5800H using the fxrstor64 + MMIO hammer technique. The project is authored by Christopher Domas.

---

## Full Article

[Skip to content](https://github.com/xoreaxeaxeax/asm-hall-of-shame#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      

  

  

      

        
            
  
      
    
    
      [xoreaxeaxeax](https://github.com/xoreaxeaxeax)    
    /
    
      [asm-hall-of-shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fxoreaxeaxeax%2Fasm-hall-of-shame)    You must be signed in to change notification settings

  

  
- 
          [Fork
    18](https://github.com/login?return_to=%2Fxoreaxeaxeax%2Fasm-hall-of-shame)
  

  
- 
        
        [Star
          935](https://github.com/login?return_to=%2Fxoreaxeaxeax%2Fasm-hall-of-shame)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/xoreaxeaxeax/asm-hall-of-shame/branches)[Tags](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[1 Commit](https://github.com/xoreaxeaxeax/asm-hall-of-shame/commits/main/)1 Commit

## Folders and files

NameNameLast commit messageLast commit date[artifacts](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/artifacts)[artifacts](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/artifacts)  [clflush](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/clflush)[clflush](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/clflush)  [cpuid](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/cpuid)[cpuid](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/cpuid)  [denormal](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/denormal)[denormal](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/denormal)  [enter](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/enter)[enter](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/enter)  [fdiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fdiv)[fdiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fdiv)  [fldl](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fldl)[fldl](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fldl)  [fsin](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fsin)[fsin](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fsin)  [fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fxrstor64)[fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fxrstor64)  [fyl2x](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fyl2x)[fyl2x](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/fyl2x)  [idiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/idiv)[idiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/idiv)  [in](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/in)[in](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/in)  [lock_hammer_fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/lock_hammer_fxrstor64)[lock_hammer_fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/lock_hammer_fxrstor64)  [lock_hammer_mmio](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/lock_hammer_mmio)[lock_hammer_mmio](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/lock_hammer_mmio)  [mfence](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mfence)[mfence](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mfence)  [mov](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov)[mov](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov)  [mov_cr3](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov_cr3)[mov_cr3](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov_cr3)  [mov_rax](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov_rax)[mov_rax](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/mov_rax)  [nop](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/nop)[nop](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/nop)  [nop16](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/nop16)[nop16](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/nop16)  [out](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/out)[out](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/out)  [rdmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdmsr)[rdmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdmsr)  [rdrand](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdrand)[rdrand](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdrand)  [rdseed](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdseed)[rdseed](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdseed)  [rdtsc](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdtsc)[rdtsc](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/rdtsc)  [split_lock](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/split_lock)[split_lock](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/split_lock)  [split_lock_hammer](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/split_lock_hammer)[split_lock_hammer](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/split_lock_hammer)  [tools](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/tools)[tools](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/tools)  [vmovdqu32_zmm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu32_zmm)[vmovdqu32_zmm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu32_zmm)  [vmovdqu_xmm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_xmm)[vmovdqu_xmm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_xmm)  [vmovdqu_ymm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_ymm)[vmovdqu_ymm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_ymm)  [vmovdqu_ymm_unaligned](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_ymm_unaligned)[vmovdqu_ymm_unaligned](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vmovdqu_ymm_unaligned)  [vpgatherdd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vpgatherdd)[vpgatherdd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/vpgatherdd)  [wbinvd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/wbinvd)[wbinvd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/wbinvd)  [wrmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/wrmsr)[wrmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/tree/main/wrmsr)  [.gitignore](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/.gitignore)[.gitignore](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/.gitignore)  [LICENSE](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/LICENSE)[LICENSE](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/LICENSE)  [Makefile](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/Makefile)[Makefile](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/Makefile)  [README.md](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/README.md)[README.md](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/README.md)  View all files

## Repository files navigation

# Assembly Hall of Shame

## Overview

Instruction latency analysis usually focuses on performance
optimization—making code run as fast as possible.  The  `Assembly Hall of Shame`  takes the opposite approach: searching for the absolute floor of
single-instruction performance.

## 🏆 Current Champions 🏆

### x86: [fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame#1-trophy-fxrstor64-trophy)

Strategy: Use  `fxrstor64`  to load 512-byte FPU/MMX/XMM state from a
high-latency MMIO region in the PCIe fabric, then starve the fabric while the
load is in flight — a fleet of hammer cores pounds a different high-latency
MMIO register with tight 4-byte reads, saturating the PCIe root complex and
endpoint with non-posted transactions, so CPU 0's 512-byte  `fxrstor64`  must
queue behind all that contending traffic.

Contender: AMD Ryzen 7 5800H
 `; CPU 0 — timed instruction
movl $0xfcc68830, %rsi
fxrstor64 %rsi

; CPUs 1..N — hammer loop against a different high-latency location
movl 0xfcc68858, %eax` 

🏆 Score: 198,002,498,236 cycles

🏆 Time: 62 seconds

## Honorable Mentions

A spec-violating [unaligned ymm0 load](https://github.com/xoreaxeaxeax/asm-hall-of-shame#3-vmovdqu-ymm-unaligned--) that forced
non-posted dword transactions from stalled GPU registers was used to break the
fundamental design of System Management Mode in
[smiiiiiiiiiiiiiiii](https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii).
 `vmovdqu 0xfcc003b1, %ymm0` 

## Rules

- Instructions may use whatever setup is necessary, but only a single
instruction is eligible to be scored.

- Trapped/emulated/virtualized instructions may only time the trap, not the
handler.

- Instructions must not be interruptible.   `rep movs` ,  `pause` , etc. are
disqualified.

- Times are normalized based on the CPU base clock frequency.

- All platforms must be in their factory stock configurations - no hardware
modifications.

## x86 Leaderboard

### 27. [nop](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/nop)

Strategy:  `nop`  does nothing. It opens the leaderboard accordingly.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 ` `nop
` ` 

Score: 1 cycles

Time: 0 nanoseconds

### 26. [nop16](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/nop16)

Strategy: Regular  `nop`  was too short, but how do we make nothing take
longer? Try a  `lonnnnnng nop` .

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 ` `data16 data16 data16 data16 data16 data16 data16 nopl 0x00000000(%%eax,%%eax,1)
` ` 

Score: 20 cycles

Time: 7 nanoseconds

### 25. [rdtsc](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/rdtsc)

Strategy: Just a reference instruction to get our bearings.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `rdtsc` 

Score: 49 cycles

Time: 18 nanoseconds

### 24. [idiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/idiv)

Strategy: Use 128-bit dividend (rdx:rax=2:0) with small divisor to push the
quotient above the ceiling imposed by sign-extension, driving the longest path
through the divider microcode.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `xorq %rax, %rax   ; rax = 0  (low 64 bits of dividend)
movq $2, %rdx     ; rdx = 2  (high 64 bits: full dividend = 2^65)
movq $5, %rbx     ; divisor → quotient = 2^65/5 ≈ 7.4×10^18
idivq %rbx` 

Score: 77 cycles

Time: 28 nanoseconds

### 23. [enter](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/enter)

Strategy: Use maximum nesting depth (31) to force 30 display-pointer loads
and pushes through the microcode display-walk path.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `enter $0, $31       ; 0 bytes allocated, nesting depth 31 (maximum)` 

Score: 112 cycles

Time: 41 nanoseconds

### 22. [fldl](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/fldl)

Strategy: Try a small denormal to trigger an FP microcode assist.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `    movabsq $0x0000000000000001, %rax
    movq    %rax, -8(%rsp)
    fldl    -8(%rsp)` 

Score: 133 cycles

Time: 49 nanoseconds

### 21. [clflush](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/clflush)

Strategy: Just ensure the cache line is dirty.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `clflush (%rax)          ; rax -> dirty cache line resident in L3` 

Score: 165 cycles

Time: 60 nanoseconds

### 20. [fsin](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/fsin)

Strategy: Use exponent 0x7ff to reach 'special value' processing in
microcode; positive/negative, NaN/inf doesn't seem to make a difference, go with
QNaN.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `    movabsq $0x7fffffffffffffff, %rax
    movq    %rax, -8(%rsp)
    fldl    -8(%rsp)
    fsin` 

Score: 257 cycles

Time: 94 nanoseconds

### 19. [mfence](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/mfence)

Strategy: Saturate all write-combining line-fill buffers with  `movnti` 
stores to distinct cache lines, forcing  `mfence`  to drain the full LFB write
path to the uncore before retiring.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `movnti %r9,  0*64(%rdi)   ; ×16 distinct cache lines — saturate the write-combining LFBs
; …
movnti %r9, 15*64(%rdi)
mfence                     ; must drain all pending LFB writes before retiring` 

Score: 326 cycles

Time: 120 nanoseconds

### 18. [mov cr3](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/mov_cr3)

Strategy: Nothing for now, just check how long it takes to invalidate the
TLB.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `mov %rax, %cr3` 

Score: 352 cycles

Time: 110 nanoseconds

### 17. [fadd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/denormal)

Strategy: Hit x87 FP microcode assist path by using denormal source operand.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `fldl   subnorm    ; 1e-310: value < DBL_MIN, biased exponent = 0
faddl  subnorm    ; source is subnormal → FP microcode assist` 

Score: 677 cycles

Time: 249 nanoseconds

### 16. [split lock](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/split_lock)

Strategy: Align  `lock` -prefixed operand to straddle cache-line
boundary, forcing CPU to assert the external bus lock rather than using the fast
MESI cache-coherence path.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `; split_ptr % 64 == 63 — dword spans bytes 63 (line N) and 64–66 (line N+1)
lock xaddl %r9d, (%rdi)` 

Score: 865 cycles

Time: 319 nanoseconds

### 15. [fdiv](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/fdiv) -

Strategy: Use subnormal divisor, hardware hands control to microcode
assist, assist normalizes operand, performs the division, then restores
architectural state.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `    movabsq $0x3ff0000000000000, %rax   ; 1.0 (normal dividend)
    movq    %rax, -8(%rsp)
    fldl    -8(%rsp)                     ; ST(0) = 1.0

    movabsq $0x0000002000000000, %rax   ; 6.79e-313 (subnormal divisor)
    movq    %rax, -8(%rsp)
    fdivl   -8(%rsp)                     ; ST(0) = 1.0 / subnormal → FP assist` 

Score: 883 cycles

Time: 325 nanoseconds

### 14. [cpuid](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/cpuid)

Strategy: Use [rakefield](https://github.com/xoreaxeaxeax/rakefield) to find
the highest latency CPUID leaves.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 ` `movl $6, %eax
cpuid
` ` 

Score: 1248 cycles

Time: 460 nanoseconds

### 13. [rdrand](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/rdrand)

Strategy: Execute in a tight loop to deplete the hardware entropy pool faster than it can be refilled, forcing subsequent calls to stall while the entropy source recovers.

Contender: Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz
 `rdrand %rax` 

Score: 5,579 cycles

Time: 2.057 microseconds

### 12. [wrmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/wrmsr)

Strategy: Use [project:nightshyft](https://github.com/xoreaxeaxeax/nightshyft)
to identify high latency MSRs.  MCG_CTL on Zen look like a winner: may be a
microcode quiesce and synchronize on MCA error banks across hardware units, some
potentially off-die, requiring fabric-level communication rather than a simple
local register write.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `movl $0x17b, %ecx       ; MCG_CTL
wrmsr` 

Score: 34,304 cycles

Time: 10.742 microseconds

### 11. [out](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/out)

Strategy: Target an I/O port that straddles a NIC device register boundary,
triggering the device to quiesce its TX DMA engine on each write.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `mov $0xf019, %dx
outl %eax, %dx` 

Score: 49,857 cycles

Time: 15.580 microseconds

### 10. [rdmsr](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/rdmsr)

Strategy: Use [project:nightshyft](https://github.com/xoreaxeaxeax/nightshyft)
to identify high latency model-specific-registers: VIA uses an undocumented
register at 0x133 that gives wildly high response time.  No idea what it does.

Contender: VIA Eden Processor 800MHz
 `movl $0x133, %ecx ; undocumented MSR
rdmsr` 

Score: 161,602 cycles

Time: 202.004 microseconds

### 9. [wbinvd](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/wbinvd)

Strategy: Fully load L1/L2/L3 caches with dirty lines to force DRAM
writeback of entire hierarchy.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `wbinvd` 

Score: 1,616,480 cycles

Time: 506.165 microseconds

### 8. [in](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/in)

Strategy: Target I/O port mapped to an ACPI PM block where an unaligned
4-byte read decodes into multiple non-posted loads from wherever this port goes.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `mov $0x0413, %dx
inl %dx, %eax` 

Score: 12,524,415 cycles

Time: 3.921769 milliseconds

### 7. [mov](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/mov)

Strategy: Use [mmiotic](https://github.com/xoreaxeaxeax/mmiotic) to identify
high-latency deadspace in PCIe fabric, hit unkown GPU register.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `movl 0xfcc003b0, %esi` 

Score: 443,937,696 cycles

Time: 139.010268 milliseconds

### 6. [mov rax](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/mov_rax) -

Strategy: Search MMIO space for slowest registers in PCIe fabric, hit
unknown GPU register, use 8-byte MMIO read to get two dword register accesses,
which isn't technically allowed but works anyway.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `movq 0xfcc003b0, %rax` 

Score: 887,716,864 cycles

Time: 277.971228 milliseconds

### 5. [vmovdqu xmm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/vmovdqu_xmm) -

Strategy: Search MMIO space for slowest registers in PCIe fabric, hit
unknown GPU register, use 16-byte MMIO read to get four dword register accesses,
which isn't technically allowed but works anyway.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `vmovdqu 0xfcc003b0, %xmm0` 

Score: 1,774,555,776 cycles

Time: 555.664133 milliseconds

### 4. [vmovdqu ymm](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/vmovdqu_ymm) -

Strategy: Search MMIO space for slowest registers in PCIe fabric, hit
unknown GPU register, use 32-byte MMIO read to get eight dword register
accesses, which still isn't technically allowed but works anyway.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `vmovdqu 0xfcc003b0, %ymm0` 

Score: 3,549,079,296 cycles

Time: 1.111345034 s

### 3. [vmovdqu ymm (unaligned)](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/vmovdqu_ymm_unaligned) -

Strategy: Search MMIO space for slowest registers in PCIe fabric, hit
unknown GPU register, use 32-byte unaligned MMIO read to get nine dword
register accesses, which is even less allowed than the aligned version, but
works anyway.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `vmovdqu 0xfcc003b1, %ymm0` 

Score: 4,453,212,256 cycles

Time: 1.394428818 seconds

### 2. [fxrstor64 (baseline)](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/fxrstor64) -

Strategy: Use [mmiotic](https://github.com/xoreaxeaxeax/mmiotic) to identify
high-latency deadspace in PCIe fabric, isolate region near 0's and offset state
to avoid MXCSR corruption (possibly VGA buffer?), use fxrstor64 to load 512-byte
FPU/MMX/XMM state from MMIO, forcing CPU to process 512 bytes of I/O
transactions through slowest available memory aperture.

Contender: AMD Ryzen 7 5800H
 `movl $0xfcc68830, %rsi
fxrstor64 %rsi` 

Score: 74,584,168,512 cycles

Time: 23.354502677 seconds

### 1. 🏆 [fxrstor64](https://github.com/xoreaxeaxeax/asm-hall-of-shame/blob/main/lock_hammer_fxrstor64) 🏆

Strategy: Extend [fxrstor64 (baseline)](https://github.com/xoreaxeaxeax/asm-hall-of-shame#2-fxrstor64-baseline) by starving the fabric while the
load is in flight — a fleet of hammer cores pounds a different high-latency
MMIO register with tight 4-byte reads, saturating the PCIe root complex and
endpoint with non-posted transactions, so CPU 0's 512-byte fxrstor64 must queue
behind all that contending traffic.

Contender: AMD Ryzen 7 5800H with Radeon Graphics (Trigkey S5)
 `; CPU 0 — timed instruction
movl $0xfcc68830, %rsi
fxrstor64 %rsi

; CPUs 1..N — hammer loop against a different high-latency location
movl 0xfcc68858, %eax` 

🏆 Score: 198,002,498,236 cycles

🏆 Time: 62 seconds

### ??. xrstor64 (AMX, MMIO) 

Strategy: Leverage extended AVX state in Sapphire Rapids with MMIO approach
from fxrstor64:  `xsave`  state area is 8KB vs 512 bytes, 16x size ->
1,000,000,000,000 cycles

Contender: TODO
 `; XCR0 must enable AMX components (bits 17-18); state area ~8KB
xrstor64 (%rsi)         ; rsi -> MMIO region, same technique as fxrstor64` 

## ARM Leaderboard

- T.B.D.

## RISC-V Leaderboard

- T.B.D.

## Author

The assembly hall-of-shame is a research effort from Christopher Domas ([@xoreaxeaxeax](https://x.com/xoreaxeaxeax/)).

## About

Racing to the bottom of CPU performance

### Resources

[Readme](https://github.com/xoreaxeaxeax/asm-hall-of-shame#readme-ov-file)[MIT license](https://github.com/xoreaxeaxeax/asm-hall-of-shame#MIT-1-ov-file)[Activity](https://github.com/xoreaxeaxeax/asm-hall-of-shame/activity)

### Stars

935 stars

### Watchers

8 watching

### Forks

[18 forks](https://github.com/xoreaxeaxeax/asm-hall-of-shame/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fxoreaxeaxeax%2Fasm-hall-of-shame&report=xoreaxeaxeax+%28user%29)

## Releases

## Packages

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
