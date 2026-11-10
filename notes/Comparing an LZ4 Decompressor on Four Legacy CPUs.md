---
title: "Comparing an LZ4 Decompressor on Four Legacy CPUs"
url: https://bumbershootsoft.wordpress.com/2026/05/09/comparing-an-lz4-decompressor-on-four-legacy-cpus/
clipped: 2026-06-17 00:59:01
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Comparing an LZ4 Decompressor on Four Legacy CPUs](https://bumbershootsoft.wordpress.com/2026/05/09/comparing-an-lz4-decompressor-on-four-legacy-cpus/)

## Digest Summary
The article documents four hand‑written LZ4 decompression implementations for legacy CPUs (Zilog Z80, Intel 8080/8086, and MOS 6502) and analyzes how each architecture’s features affect the algorithm. LZ4’s block format consists of sequences of literals followed by a back‑reference, encoded in a single length byte (high nibble = literal length, low nibble + 4 = back‑reference length) plus a two‑byte little‑endian offset; extended lengths use extra bytes of 0xFF. The author’s variation relies on two decoder constraints: the final sequence is literals only and offsets are never zero, allowing termination with a zero‑offset pair instead of full frame data. 

For the Z80, the LDIR instruction efficiently copies blocks, and only two long‑lived pointers (source, destination) are needed, with occasional stack swaps to handle extended back‑reference lengths. The 8080 mirrors the Z80 code but replaces LDIR with manual loops and substitutes SBC HL,BC with byte‑wise subtractions, increasing accumulator use and register saves. The 8086 exploits its richer register set and string instructions (LODSB, STOSB, MOVSB, REP) to avoid stack usage, handling far pointers and segment registers for 1 MiB address space. The 6502, lacking multi‑register pointers and block‑copy ops, uses zero‑page scratch space and a helper routine to emulate LDIR, incurring heavy accumulator traffic and RAM‑based temporary storage. The article also outlines each CPU’s API conventions (register or memory‑based pointers, calling‑convention preservation) and notes how historical decoder constraints simplify implementation.

## Discussion Summary
The feedback expresses that the material is challenging yet enjoyable, appreciating the design that avoids costly conditional checks by using three constraints that allow unrestricted operation. The reader perceives the approach as efficient and streamlined, emphasizing the benefit of eliminating expensive tests and enabling full‑throttle execution. Overall, the impression is that the strategy simplifies implementation while maintaining performance.

---

## Full Article

A few years ago, I needed to save some cartridge space in a SNES project, and I did so by [compressing that data](https://bumbershootsoft.wordpress.com/2023/10/21/lz4-decompression-on-the-65816/) with the [LZ4 compression algorithm](https://lz4.org/) from 2012. I found that working within the constraints of the SNES allowed me to take some convenient shortcuts during decompression and I have since found those constraints and shortcuts to be widely relevant on the 8- and 16-bit platforms my hobby programming often involves. I accumulated two more implementations (for Motorola’s [6809](https://bumbershootsoft.wordpress.com/2024/02/24/lz4-decompression-on-the-6809/) and [68000](https://bumbershootsoft.wordpress.com/2025/07/12/lz4-decompression-on-the-68000/) processors) as I worked on projects for the Tandy Color Computer and the Sega Genesis.

Now, as a consequence of my [recent experiences with the Sorcerer](https://bumbershootsoft.wordpress.com/2026/04/25/staying-a-spell-with-the-exidy-sorcerer/), I found myself with *four* new implementations, for the Z80, two CPUs related to it (the Intel 8080 and 8086), and the 6502. As I mentioned at the time, the Z80 implementation in particular was *very* straightforward, and it informed the other three pretty directly.

My article about this for the 68000 was kind of desultory—it’s pretty clear on rereading it that the only thing I found interesting about it was the way the 16-bit code ended up bearing more in common with the 8-bit 6809 code than the 16-bit 65816 code. I expect this article to be my last hurrah on the subject, so I’d also like to give it more respect and more scope. I’ll start with my potted summary of how LZ4 works and what variations I made to it, but then also look at *why* LZ4 is so friendly to the Z80, especially as it compares to the 8080 and 6502. After that, I’ll use the LZ4 implementation as a worked example of [last week’s article comparing all these CPUs](https://bumbershootsoft.wordpress.com/2026/05/02/comparing-the-z80-and-6502-to-their-relatives/) by showing how the Z80 implementation can be easily transformed into the 8080 and x86 implementations, and some of the very different implementation decisions the 6502 version must make.

**Fair warning:** This article is very long and very dry compared to my usual fare. If you want to see the same function implemented in four different assembly languages, this is the good stuff and go on and have fun. If not, maybe come back next week when I expect to be goofing around with high level languages again.

A Review of LZ4
---------------

*(I’ve repeated this section in every implementation article so that readers don’t have to click back for context; if you’ve seen this all before, feel free to skip ahead to the section “Other Restrictions on LZ4 Encoders.” You’re not missing anything.)*

LZ77-class decompressors all work on the same two basic tricks:

* If a string of data repeats itself throughout the text, you specify an offset and a length within the output to copy. This will be shorter than repeating the data itself.
* If the length of the amount to repeat kicks you past the original end of the output, keep repeating the values that you originally wrote. This matches what happens with a naïve copy loop, anyway, so this normally works out. It also means that this class of decompressors can do run-length encoding for free, even when the run is a copy of multiple bytes instead of just one.

LZ4’s block format hinges on the insight that we can think of a compressed stream as *alternating* between strings of copied values and backreferenced ranges. Backreferences might follow one another directly, but if two blocks of literals are adjacent, that’s just a single block of literals. As such, the fundamental unit of decompression is a string (possibly length zero) of literals, followed by a backreference. The format specification calls this pair a *sequence.*

A sequence begins with a single byte giving the length of both the next literal string and the next backreference; the top four bits represent the string length directly, and the bottom four bits represent the backreference length after adding four to it. (If your backreference is shorter than four, it’s not worth the space to create a new sequence compared to just copying the literals again. Thus, four is the shortest meaningful backreference.) This is followed by that many literal characters to copy into the output, and then a two-byte little-endian value to indicate how far back in the output to copy the backreference from.

It may, of course, come to pass that your literal string is longer than 15, or your backreference is longer than 19. To represent this, the length nybble for that part is recorded as 15 and additional bytes are added to the stream to indicate how much to add to the length. These bytes occur right after the initial lengths byte for the literal string, or just after the offset for the backreference. Bytes are read and added to the length until one of them is not 255; then that value too is added in to produce the final result. (This does mean that a literals length of exactly fifteen needs an extra length byte of zero to indicate that we did in fact mean fifteen exactly.)

### Our Variation

Encoders have to worry about a few extra constraints, because there are old decoders that rely on hacks to allow decompression to go way faster. Since we’re decoding, we don’t have to care about those, but one of them is extremely useful to us: We are guaranteed that the final sequence contains only literals. The compressed data ends just before what would otherwise be an offset word.

The other important fact about offset words is that they may never be zero. After all, that would mean we would need to copy from underneath the very byte we were writing!

Combined, these facts are what let us dispense with the traditional frame data: we can simply null-terminate the compressed data with a pair of zero bytes and use “our alleged backreference has offset zero” as the signal to stop decompressing.

### Other Restrictions on LZ4 Decoders

There are three restrictions placed on the LZ4 encoder when creating compressed blocks. We only rely on the first.

* The last sequence is only literals.
* The last sequence has *at least five* literal characters in it, unless it is the only sequence in the entire block.
* The backreference in the next-to-last sequence begins *at least 12 bytes before the end of the block.*

The specification explicitly states that a consequence of this is that no string of less than 13 bytes can be compressed. It also describes these rules as being “in place to ensure compatibility with a wide range of historical decoders which rely on these conditions for their speed-oriented design.” That’s interesting to me, because my own exploitation of these rules was to ensure correctness more easily and to reduce the amount of state the decoder needed. Speed was not really involved at all.

I can, at least, come up with an easy efficiency-oriented reason to insist on the last sequence being only literals; the LZ4 frame format (which I have discarded) signals termination by pre-declaring the size of the compressed data. Insisting on ending with literals means we only have to actually adjust or check that counter after copying a block of literals. Without this restriction, we’d have to juggle the check in with reading the *extended length bytes of the backreference.*

I am utterly in the dark as the the advantages the last two restrictions might grant, though, particularly since while decoding we generally won’t *know* that we’re in the last two sequences and neither of these restrictions apply to any *previous* sequences within the block. My best guess on the second is that for every block but the last you can transfer four bytes unconditionally with a 32-bit move and just adjust your destination pointer if it turns out that copied too much, and you will still (thanks to the minimum backreference size being four bytes long) never blow out your destination buffer. I don’t even have *bad* guesses for what the final restriction buys us.

LZ4 On Our Various Chips
------------------------

Before digging into the details of the implementations, let’s take a high-level look at how the decompression algorithm interacts with the capabilities of our four CPUs.

### Our Yardstick: The Zilog Z80

The LZ4 decompression algorithm revolves around making block copies, which the Z80 is quite good at thanks to the **`LDIR`** instruction. However, that is not the only way it fits well with the chip. We can only conveniently use two pointers at once on the Z80, with the remaining three general-purpose registers managing the overall computation and the index registers kept at a bit of a remove from the rest of the instruction set. LZ4 only needs two long-lived pointers as well; the source and destination pointers. A third pointer value shows up regularly as the alternate source pointer when copying from a backreference; however, this pointer effectively *temporarily replaces* the source pointer over its lifetime; it is, with one slight wobble, computed, used exclusively in place of the source pointer, and then thrown out. This means that to the extent that we *won’t* be able to fit everything in registers, our usage of the stack can restrict itself to storing temporary values.

The “wobble” shows up with long-running backreference copies. If the backreference part of a sequence is more than 19 bytes long, the remaining bytes in the length data appear *after* the offset. This requires us to stash the backreference pointer briefly after computing it so that we may read a few more bytes from the source pointer first. While the Z80 is not really well-suited to keeping local variables on a stack, it inherits an instruction from the 8080 that allows it to swap **`HL`** with the top value on the stack. This turns out to be sufficient to let us juggle our source pointers as needed, and everything works out.

### Doing Things the Hard Way: The Intel 8080

The 8080 implementation almost exactly matches the Z80 one, except for assembler syntax. There are only two Z80-specific capabilities we use at all in the implementation: the **`LDIR`** block-copy command, and the single instruction **`SBC HL,BC`**. We replace the block copies with hand-written loops, and break out the 16-bit subtraction into a pair of 8-bit subtractions. These operations mean we make heavier use of the accumulator, and as a result we do need to save and restore registers to the stack a bit more frequently.

The translation here was otherwise very direct; we can read the 8080 version as being *exactly* the Z80 version with some blocks of instructions filling in for the missing ones.

### Doing More With More: The Intel 8086

The 8086 has enough spare registers, and enough expressive capability, that we do not need to touch the stack at any point the 8-bits do. We *do* still hit the stack a bit though; the customary ABI preserves some of the registers we use, and we shouldn’t violate that without a good reason. Furthermore, I expanded the scope of the 8086 implementation to work with “far pointers”, covering the entire 1MB address range. This required some juggling of the segment registers, and I felt the code was a bit clearer if it used the stack while doing so.

Beyond that, we get extremely good use out of the “string” instructions that serve as autoincrementing loads, stores, and moves. Not only do these serve the same purpose as the Z80’s **`LDIR`** instruction, they are actually useful in even more places in the implementation. A consequence of this, however, is that we often find that the main accumulator gets overwritten by *different* intermediate computations than it does on the 8-bit editions, which resulted in me shifting around some parts of the order of operations as a result.

### And Now For Something Completely Different: The MOS Technology 6502

The 6502 is vastly more restricted, when viewed from the perspective of the Z80 or its relatives. It has *zero* registers that can double as pointers, its 8-bit stack struggles to accomplish much beyond preserving values in strict stack discipline, and it offers even less direct support for 16-bit operations than the 8080.

The gap narrows considerably, however, when we shift the perspective to what the 6502 is actually *good* at. I dedicated [an entire article](https://bumbershootsoft.wordpress.com/2022/11/15/cleanly-organizing-8-bit-dataflows/) to the differences in implementation philosophy encouraged by the 6502 compared to the Z80, and much of that analysis applies here. The weaker stack and smaller register bank mean that the 6502 relies far more heavily on scratch space elsewhere in RAM, but that very reliance means that we have *no register pressure whatsoever.* All arithmetic goes through the accumulator, and 16-bit values can’t be used out of any registers at all, so conceptually all the operands are coming out of memory and returning to it once processing is complete.

The LZ4 algorithm is definitely a less comfortable fit overall, though. The 6502 is much less comfortable with pointers than the Z80, or even the 8080, is, and we will have only limited opportunities to work around that. In my old article, I noted that the 6502 vastly prefers to work with arrays than with pointers, and that furthermore, when we have multiple arrays, it wishes to be working with corresponding indices *within* those arrays. I ended up writing an entire helper function to implement what the Z80 does with **`LDIR`**, and it was able to provide that abstraction of corresponding indices; however, the decompressor *as a whole* is not afforded that luxury. It is, after all, kind of the whole point of compressed data that we will be advancing the destination’s pointer more rapidly than the source’s!

Designing the API
-----------------

The Z80 API is straightforward, and is basically dictated by the fact that we’re going to lean on **`LDIR`** for our copy operations. **`HL`** will be our source pointer, pointing to the beginning of the compressed data, and **`DE`** will be our destination pointer, pointing to the beginning of the buffer we wish to fill with decompressed data. Registers **`ABC`** will all be scratch registers for the function, and on function exit, both **`HL`** and **`DE`** will point one byte past the last byte read or written.

As I mentioned above, the 8080 implementation is extremely close to the Z80 one and as a result it will enjoy an identical API.

The 8086 was a bit more fraught. We’ve now reached a point where things like “calling conventions” actually exist, and the C compilers I’ve worked with are pretty consistent about what they expect. **`BP`** is used as a frame pointer to access arguments that were pushed on the stack prior to the call, 16 bit return values are returned in **`AX`**, the high 16 bits of 32-bit return values are returned in **`DX`**, those two along with **`CX`** are scratch registers, and everything else is preserved. This is extremely inconvenient for comparison purposes with my other implementations, so I’ve bent it heavily.

I have retained the notion that the function’s API should closely match the block-copy instruction. For the 8086, that means these must be *[far pointers](https://bumbershootsoft.wordpress.com/2022/08/05/memory-models-and-far-pointers/)* that range over the full 1MB of address space, with **`DS:SI`** as the source pointer and **`ES:DI`** as the destination pointer. While these are normally all preserved, I let the routine update **`SI`** and **`DI`** for use as a pair of return values (again, pointing just past their final byte processed). Those two pointers aside, I do also ensure that all segment registers are preserved alongside **`BP`** and **`BX`**.

The 6502 API is, like the others, dictated by the actual processing we do, but since its architecture is so different, the API is likewise distinct. Here, we set aside four bytes of scratch space in the zero page to hold the source and destination pointers. The routine updates those memory locations directly, leaving them in their final locations on function exit. Four additional scratch bytes are necessary as well, but I implemented the function such that they do not need to be in the zero page. Like most functions of any complexity, this one trashes all three of the 6502’s registers.

Implementation on the Z80 and Intel Chips
-----------------------------------------

Let’s now look at the implementations in detail. The 8080, Z80, and 8086 implementations are so similar that it’s worth simply tracking them in parallel.

We open with a function prologue… or we would, if we had one. Only the 8086 has one; it needs to save off the **`BX`** register because it will be trashing it over the course of the function and it needs to restore the caller’s value on the way out.

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             -----------------
lz4dec:                                                     push bx
```

After that, we begin our main loop by reading the next byte from the compressed data and advancing the source pointer. We’ll need to split this into two 4-bit values over the course of the function, so we’ll need to stash a copy of the original byte for later.

The 8080 and Z80 code here is actually identical, though the instructions look very different. When reading a byte out of the memory location specified by **`HL`**, 8080 syntax refers to it as the pseudo-register **`M`**. Furthermore, instructions that work on register pairs are distinct from those that work on single registers, so they are usually named only by their high byte (so, **`H`** for what the Z80 calls **`HL`**, and so on). A further exception, which we also see here, is that the register pair that the Z80 calls **`AF`**—the accumulator and flags—is instead called **`PSW`**—the processor status word.

The 8086 code, on the other hand, is much different. Instead of pushing the byte read to the stack, it simply stores it in the **`BL`** register where it will be left alone until needed. More interestingly, it uses one of the CPU’s “string processing” instructions. The three basic instructions are **`LODSB`**, **`STOSB`**, and **`MOVSB`**:

* **`LODSB`** (“Load String Byte”) is equivalent to **`MOV AL,[DS:SI]; ADD SI,1`**. This instruction replaces the first two instructions in the 8-bit case.
* **`STOSB`** (“Store String Byte”) is the reverse; it is equivalent to **`MOV [ES:DI],AL; ADD DI,1`**.
* **`MOVSB`** (“Move String Byte”) combines them into **`MOV [ES:DI], [DS:SI]; ADD SI,1; ADD DI,1`**. This is roughly equivalent to the Z80’s **`LDI`** instruction.
* It is also possible to move 16-bit words (with **`AX`** as the other register in the load and store cases) by replacing the **`B`** with a **`W`**. Once the CPU goes 32-bit, a double-word variant also appears relying on **`EAX`**.
* There is a “direction” flag that causes the pointers to be decremented instead of incremented; calling conventions all demand that this flag be set to increment mode at all function boundaries, and we don’t mess with it here.
* The store- and move-string instructions may be repeated by prefixing the instruction with **`REP`**. This uses **`CX`** as a count register, and functions analogously to **`LDIR`** or **`LDDR`** depending on the direction flag.

The end result is that in this brief snippet the 8086 code is one instruction shorter:

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             -----------------
.main:  mov a,m               ld a,(hl)                     lodsb
        inx h                 inc hl
        push psw              push af                       mov bl,al
```

Now we need to handle the literals. The 8086 code is, again, pretty straightforward; it isolates the high nybble by shifting **`AL`** right 4, then skips ahead to backreference processing if the result is zero. Otherwise it calls our **`.rdlen`** helper function to finalize the length and does the block copy with **`REP MOVSB`**. The Z80 and 8080 code is similar, with **`LDIR`** handling the block copy on the Z80 side and the 8080 (which lacks this instruction) filling it in with a more manual loop. There’s an interesting difference in the way they collect the high nybble, though:

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
        rrc                   rrca                          mov cl,4
        rrc                   rrca                          shr al,cl
        rrc                   rrca
        rrc                   rrca
        ani 15                and 15
        jz .bkref             jr z,.bkref                   jz .bkref
        call .rdlen           call .rdlen                   call .rdlen
.lp1:   mov a,m               ldir                          rep movsb
        stax d
        inx h
        inx d
        dcx b
        mov a,c
        ora b
        jnz .lp1
```

The 8080, it turns out, doesn’t have any shift instructions. Instead, it has four “rotate accumulator” instructions, two of which are 9-bit rotations through the carry and two of which are 8-bit rotations strictly within the register (with the carry bit mirroring the bit that moves from least to most significant). On the 8080, we need to rotate right four times to swap the high and low nybbles and then mask out the upper bits. On the Z80, we actually *have* a proper shift-right instruction **`SRL A`** but this instruction, as part of its extended instruction set, is 2 bytes long and takes 8 cycles to execute, while **`RRCA`**, which it inherited from the 8080, is only 1 byte and takes only 4 cycles to execute. Copying the 8080’s more roundabout processing is both smaller and faster. This is one of those cases I noted more abstractly last week: the Z80 rewards staying within the 8080’s constraints when it’s not very awkward to do so.

The literals of this sequence handled, we now move on to the backreference part. Step one is always to read a 16-bit value from the compressed data and end decompression if it is zero. Once again, the string operations dramatically simplify the memory access on the 8086 side, and its 16 bit registers mean that the zero test may be done with a single operation as well:

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
.bkref: mov c,m               ld c,(hl)                     lodsw
        inx h                 inc hl
        mov b,m               ld b,(hl)
        inx h                 inc hl
        mov a,c               ld a,c                        test ax,ax
        ora b                 or b
        jz .done              jr z,.done                    jz .done
```

(The **`TEST`** instruction is basically an **`AND`** that throws away the result; when passed the same register twice it basically asks the CPU to set the Zero and Sign flags according to that register’s value.)

At this point, things start to diverge. Several things need to happen, and which operations interfere with what are different on each chip:

* Construct the backreference pointer by subtracting the offset we just read from the destination pointer.
* Read the rest of the backreference length out of the original source pointer, and add 4 to it.
* Do the block copy with the backreference pointer standing in for the source pointer.
* End this sequence with the source pointer one byte past the last length byte we read (or just past the offset, if this backreference was 18 characters or less).

Keeping the source pointer happy means it will need to be saved and restored to the stack, on the 8-bits, and that also means that we’ll need to pop the length byte before pushing the source pointer onto the stack. This all works out very neatly, with a high level procedure something like this:

* Pop the length byte from the stack and isolate the low nybble this time.
* Save **`HL`** to the stack. This is our source pointer that we’ll be setting aside, but also then…
* Compute **`HL = DE-BC`** to get our backreference pointer. The Z80’s extended instructions make this easy. The 8080 has to do more work, which also means re-saving and re-restoring the accumulator.
* *Swap the backreference and source pointers,* finalize the backreference length by reading any extra length bytes, then swap them *back* and do the bulk copy.
* Pop the source pointer back into **`HL`**, ready to begin the next sequence, and jump back to the top to begin processing the next sequence of literals.

The 8086, however, has to reorganize things a bit. The 8-bits were able to load their 16-bit offset directly into **`BC`** because that is what its 16-bit math demanded, and that meant that it was free to use **`A`** to hold the initial backreference length during the subtraction. The 8086, however, loaded *into* **`AX`** with its **`LODSW`** instruction, and needs to completely finish computing the backreference pointer before dealing with the length at all. Fortunately, since it isn’t using the stack to hold temporary values, this is just a matter of register moves. The backreference pointer is computed in **`DX`** and exchanged with **`SI`** as needed; the saved length value remains in **`BL`** for as long as we need it and is copied over once it’s necessary to be passed to **`.rdlen`**.

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
        pop     psw           pop af                        ; Below
        ani     15            and 15
        push    h             push hl
        mov     h,d           ld h,d                        mov dx,di
        mov     l,e           ld l,e
        push    psw           or a                          sub dx,ax
        mov     a,l           sbc hl,bc
        sub     c
        mov     l,a
        mov     a,h
        sbb     b
        mov     h,a
        pop     psw
        xthl                  ex (sp),hl
        ; above               ; above                       mov al,bl
                                                            and al,15
        call .rdlen           call .rdlen                   call .rdlen
        inx b                 inc bc                        add cx,4
        inx b                 inc bc
        inx b                 inc bc
        inx b                 inc bc
        xthl                  ex (sp),hl                    xchg dx,si
                                                            push ds
                                                            push es
                                                            pop ds
.lp2:   mov a,m               ldir                          rep movsb
        stax d
        inx h
        inx d
        dcx b
        mov a,c
        ora b
        jnz .lp2
        pop h                 pop hl                        mov si,dx
                                                            pop ds
        jmp .main             jr .main                      jmp .main
```

There’s one last subtlety we can see in the 8086 code; when we swap the pointers, we also need to copy the value of **`ES`** into **`DS`** for the copy so that the backreference pointer has the correct segment as well, then restore it once we’re done. It’s a bit inconvenient to move values in and out of segment registers; I just do stack operations here because it’s clear and simple.

We also can see some counterintuitive optimization in the 8-bit code; we add 4 to **`BC`** simply by calling **`INC BC`** four times. This turns out to be both faster and shorter than trying to add 4 to **`BC`** directly with 8- or 16-bit math.

All that’s left in the main function is the exit; each function needs to restore the stack and return. On the 8-bits, this involves popping the unused backreference length off the stack; on the 8086, it involves restoring the **`BX`** register, which we aren’t allowed to permanently trash in our calling convention.

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
.done:  pop psw               pop af
                                                            pop bx
        ret                   ret                           ret
```

Now we need to implement the **`.rdlen`** helper function. This function takes an initial length in **`A`** (**`AL`**), and returns a final length in **`BC`** (**`CX`**). If the initial length is under 15, that is also the final length; otherwise it keeps reading bytes and adding them to the total length until we read a byte whose value is not 255. The first thing to do is to copy our 8-bit (really, 4-bit) value into the 16-bit result and quit immediately if the value isn’t 15:

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
.rdlen: mvi b,0               ld b,0                        xor ah,ah
        mov c,a               ld c,a                        mov cx,ax
        cpi 15                cp 15                         cmp cl,15
        rnz                   ret nz                        jne .rdend
```

The 8-bits handle this by zeroing the destination high byte and copying the low byte; the 8086 handles it by zeroing the high byte of **`AX`** and copying the whole word over. The 8086 also lacks **`RET NZ`**, and instead jumps to the end of the function if it needs to quit immediately.

Reading an 8-bit value and adding it to a 16-bit counter is old hat for us at this point, but the 8086 gets to be a little sneaky here; since it zeroed out **`AH`** at the top of the function, it can load bytes exclusively into **`AL`** and then just do 16-bit adds. The 8-bit chips need to use the accumulator to carry out the add, but also need to preserve the byte read for the final check, so there’s some stack work here too.

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
.rdlp:  mov a,m               ld a,(hl)                     lodsb
        inx h                 inc hl
        push psw              push af                       add cx,ax
        add c                 add c
        jnc .rdok             jr nc,.rdok
        inr b                 inc b
.rdok:  mov c,a               ld c,a
        pop psw               pop af
```

Finally we loop back if the value we had read was 255. The easiest way to check this on all platforms is to do an 8-bit increment on it and see if that makes it zero.

```
        Intel 8080            Zilog Z80                     Intel 8086
    ------------------    -----------------             ------------------
        inr a                 inc a                         inc al
        jz .rdlp              jr z,.rdlp                    jz .rdlp
.rdend: ret                   ret                           ret
```

That gets us all three implementations for the ’80 cousins. Let’s shift gears to the more distinct 6502 now.

Implementation on the 6502
--------------------------

It turns out that, at least at first, the 6502 code doesn’t diverge that much from the Z80. While the golden rule of 6502 data processing is that we want that data to be in arrays and processing to be in corresponding elements, the only part of LZ4 compression that lets us *do* that is the bulk copy that the Z80 handles with **`LDIR`**. Pretty much everywhere else, we will be locking down the **`Y`** register and using the “indirect indexed” mode as an expensive pointer mechanism. With **`src`** and **`dest`** as 4 bytes of data in the zero page that also serve as our arguments and return values, we can map those to **`HL`** and **`DE`** and our handling of the literals in a sequence tracks very closely:

```
        MOS 6502              Zilog Z80
    ----------------      -----------------
lz4dec: ldy #$00              ld a,(hl)
        lda (src),y
        inc src               inc hl
        bne +
        inc src+1
+       pha                   push af
        lsr                   rrca
        lsr                   rrca
        lsr                   rrca
        lsr                   rrca
                              and 15
        beq .bkref            jr z,.bkref
        jsr .rdlen            call .rdlen
        jsr .ldir             ldir
```

(Syntax note: 6502 code requires a lot more of these short-term jumps when it’s doing its 16-bit math, so I’m using **`+`** as a temporary label. Branching to **`+`** just means “skip to the next **`+`** label” in each case.)

The only real divergence at this point, beyond **`INC HL`** and **`LDIR`** requiring more work, is that the 6502 does have proper logical-shift instructions and doesn’t need a masking step. Our replacement for **`LDIR`** turns out to have quite a lot going on in it, so we’ll hold off on the details there. Suffice to say that we have created another 16-bit variable—not necessarily in the zero page this time—named **`.count`** and it is the length value produced by **`.rdlen`** and consumed by **`.ldir`**, much like those uses of **`BC`** in the Z80 code.

The backreference processing on the 6502 diverges *completely* from the Z80 code, to the point that there’s no sense in putting the Z80 code alongside it for reference. It begins by reading the 16-bit offset from the compressed data stream to produce the backreference pointer, much like on the Z80, but instead of shuffling data around on the top of the stack, or even storing out the offset to more scratch RAM, we instead *do the subtraction as we load* and store *that* result to our scratch RAM under the name **`.bksrc`**:

```
        MOS 6502
    ----------------
.bkref: sec
        lda dest
        sbc (src),y
        sta .bksrc
        iny
        lda dest+1
        sbc (src),y
        sta .bksrc+1
```

As part of this read we’ve bumped up the **`Y`** register to let us quickly index the next two bytes. Our next step will be to renormalize the **`src`** pointer and the **`Y`** register so that when we visit the **`.rdlen`** function it will be ready to go:

```
        MOS 6502
    ----------------
        dey
        clc
        lda src
        adc #$02
        sta src
        bcc +
        inc src+1
+
```

Unlike the Z80 and 8080, where repeated 16-bit **`INC`** instructions are the fastest way to add small numbers, the calculus flips in favor of direct 16-bit math on the 6502 basically immediately. Note that we check the carry flag this time instead of the zero flag, since we could have skipped over the page boundary without hitting it exactly, and also note that it remains both shorter and faster to do this branch-or-increment dance than it does to add zero to the high byte with carry.

With this work done, we now need to see if the offset was zero, which is a bit more problematic here because we didn’t actually *store* it. We used it immediately to create **`.bksrc`**. What we *can* do, however, is see whether the result of the subtraction changed anything. If **`.bksrc != dest`**, then the offset wasn’t zero and we can proceed with processing:

```
        MOS 6502
    ----------------
        lda dest
        cmp .bksrc
        bne .bkok
        lda dest+1
        cmp .bksrc+1
        bne .bkok
```

Otherwise, it *was* zero and we need to pop our useless length byte and return, just like on the Z80.

```
        MOS 6502
    ----------------
        pla
        rts
```

Assuming everything was fine, though, it’s time to pop our *still useful* length byte, isolate the backreference part, and complete the length read, including adding the extra four to the counter. Like the 8086, no juggling is necessary here because we never displaced the **`src`** pointer.

```
        MOS 6502
    ----------------
.bkok:  pla
        and #$0f
        jsr .rdlen
        clc
        lda .count
        adc #$04
        sta .count
        bcc +
        inc .count+1
+
```

*Now* it is time to juggle some values. We will be hardcoding the pointer locations for our **`.ldir`** helper function as **`src`** and **`dest`**, so we need to stash the original **`src`** and replace it with with the value in **`.bksrc`** before the call.

```
        MOS 6502
    ----------------
        lda src
        ldx .bksrc
        pha
        stx src
        lda src+1
        ldx .bksrc+1
        pha
        stx src+1
        jsr .ldir
```

Stackwork can be expensive, but using the stack here produces shorter code than just using **`.bksrc`** itself as swap space, and if **`.bksrc`** is not on the zero page, the code is faster, too.

We are now at the very end of the loop. This is where we finally re-sync with the Z80 code, restoring the original **`src`** pointer and jumping back to the start of the loop:

```
        MOS 6502              Zilog Z80
    ----------------      -----------------
        pla                   pop hl
        sta     src+1
        pla
        sta     src
        jmp     lz4dec        jr lz4dec
```

### Implementing the Length Reader

With the main function complete, it’s time to move on to the helper functions. Both of these end up relying on the fact that I’ve kept the **`Y`** register mostly locked to zero, and *strictly* locked to zero at all loop points and function boundaries.

We’ll look at **`.rdlen`** first. It ends up synchronizing much more closely with the Z80 version. There isn’t much to say about it that we didn’t say about the eighters’ implementations, so here I’ll just quote the two in parallel:

```
        MOS 6502              Zilog Z80
    ----------------      -----------------
.rdlen: sta     .count        ld c,a
        sty     .count+1      ld b,0
        cmp     #$0f          cp 15
        bne     .rdone        ret nz
.rdlp:  lda     (_src),y      ld a,(hl)
        inc     src           inc hl
        bne     +
        inc     src+1
+       tax                   push af
        clc                   add c
        adc     .count
        sta     .count
        bcc     .rdok         jr nc,.rdok
        inc     .count+1      inc b
.rdok:                        ld c,a
                              pop af
        inx                   inc a
        beq     .rdlp         jr z,.rdlp
.rdone: rts                   ret
```

Like the 8086, the 6502 has no conditional return statement so we use a simple branch-to-a-normal-return-statement instead. Also like the 8086, I stash the accumulator in a register (here, **`X`**) instead of relying on the stack like the Z80 does.

More interestingly, I actually played around a bit with consolidating the updates to **`src`** at the end of the function, relying instead on **`INY`** instructions inside of it. Based on a few other drafts and some napkin math, this turned out to only become worth it once your sequences extended to a kilobyte or so. Given the data I work with, I stuck with this. I think it’s clearer, anyway.

### Supporting LDIR on the 6502

Now we turn to a *new* helper function that we’ve only needed on the 6502, and we finally get to write some code that plays well with indirect-indexed addressing. We need to write a function that does the same work that the **`LDIR`** or **`REP MOVSB`** instructions did, taking a 16-bit counter (in the **`.count`** variable) and copying that many bytes from the buffer in **`src`** to **`dest`**. At the end of the function, **`src`** and **`dest`** should each point one byte past the last byte copied in their respective buffers.

The 6502, unlike even the 8080, does not have a 16-bit decrement operator, so we’re going to need to organize this as two nested loops, one for looping the low byte of the counter, and the other for looping the high byte. We also would really prefer to let our decrement options also be our loop-end test, which on the 6502 means it has to be a test against zero. We want the loop to end with something like **`DEC COUNTER; BNE LOOP; DEC COUNTER+1; BNE LOOP`**, but that carries a subtle trap. If the initial value of **`COUNTER`** here is *an even multiple of 256*—that is, if the byte in **`COUNTER`** is zero to start with—this actually works. If it isn’t, you will end up iterating the wrong number. A starting value of **`$0100`** loops 256 times, as we’d expect. A starting value of **`$0101`**, however, only loops once, and a starting value of **`$00d6`** will loop 65,750 times!

This bug isn’t unique to the 6502; the identical bug, for the identical reason, appears in the ColecoVision BIOS in some functions, because someone decided they wanted to rely on the automatic flag updates of the 8-bit decrements instead of doing a proper 16-bit check like we did in the 8080 code. The solution is simple enough, though; we need to check that low byte and increment the high byte if, and *only* if, the low byte isn’t zero.

```
        MOS 6502
    ----------------
.ldir:  ldx     .count
        beq     .llp
        inc     .count+1
```

I loaded into **`X`** instead of **`A`** here because I intend to keep the low byte of the counter in a register for faster access. We’ll need **`Y`** to index the **`src`** and **`dest`** arrays, and since the copy is in sync, we use it directly for both.

The core loop is pretty simple, with an odd little division of responsibility for both; the **`Y`** register counts up, incrementing the high byte of both **`src`** and **`dest`** any time it wraps around *as an offset.* The low bytes of **`src`** and **`dest`** can be completely unrelated and this all still works fine. The **`X`** register, on the other hand, is counting *down* the total bytes copied, and it decrements the high byte of the counter once it hits zero itself. That loop wastes no space:

```
        MOS 6502
    ----------------
.llp:   lda     (src),y
        sta     (dest),y
        iny
        bne     +
        inc     src+1
        inc     dest+1
+       dex
        bne     .llp
        dec     .count+1
        bne     .llp
```

We aren’t done when this loop is, though. We need to add the value in **`Y`** to both **`src`** and **`dest`** to get their final values right. We’ve been incrementing the high bytes along the way—we had to, in order to reach later parts of the buffer with just an 8-bit offset—and now we must add what’s left over. We also reset **`Y`** to zero on the way out so that the main function can use **`src`** and **`dest`** normally with no extra work.

```
        MOS 6502
    ----------------
        clc
        tya
        adc     src
        sta     src
        bcc     +
        inc     src+1
+       clc
        tya
        adc     dest
        sta     dest
        bcc     +
        inc     dest+1
+       ldy     #$00
        rts
```

Relying on this function for both copies *technically* does some wasted work here; the backreference pointer doesn’t need that final update since we trash it immediately afterwards. Past a certain point, though, overall brevity and clarity have to win.

Catching Our Breath
-------------------

This article ended up a lot longer than I expected, and in the service of an honestly kind of questionable goal. If you made it this far, I salute you. As for what *I’ve* ended up getting out of this, I’ve been [collecting these drafts in their own directory in my repository](https://github.com/michaelcmartin/bumbershoot/tree/master/asm/lz4core) so the practical outcome of this is that I now can LZ4-compress my data for Bumbershoot projects whenever I want.

From a craftsmanship standpoint, switching so rapidly between CPUs was an interesting experience for me. I’ve gotten quite a lot more experience with the Z80 lately, and working with both the 8080 and 8086 underlined a lot of the habits I’d picked up along the way. Usually I’ve stumbled a bit in my Z80 work, because the less appropriate habits of 6502 or 68000 programming would wrong-foot me from time to time, but working on this project is the first time in a long time where I’ve felt that stumbling in the *other direction.* I’ve had a much stronger Z80 focus over the past year or so and it’s really showing. On the plus side, I think that means at this point that my proficiency in both is up to par, and I simply need to remind myself to shift gears properly as needed from project to project.

Next week we’ll do something more freewheeling and fun, I promise.