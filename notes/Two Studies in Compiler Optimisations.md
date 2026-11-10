---
title: "Two Studies in Compiler Optimisations"
url: https://www.hmpcabral.com/2026/03/20/two-studies-in-compiler-optimisations/
clipped: 2026-06-17 01:27:16
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Two Studies in Compiler Optimisations](https://www.hmpcabral.com/2026/03/20/two-studies-in-compiler-optimisations/)

## Digest Summary
- **Case 1 – Modular increment**:  
  - Naïve `next_naive(cur,count){return (cur+1)%count;}` compiles to a costly 32‑bit division.  
  - Providing the pre‑condition `cur
Read full article →

## Discussion Summary
None

---

## Full Article

Table of contents

Introduction
------------

While many performance-oriented programmers are intimately acquainted with the almost preternatural
ability of modern compilers to optimise their code, and many of us have spent countless hours on
[Compiler Explorer](https://godbolt.org/) examining the differences between the Assembly generated
by different versions of gcc and clang, most have likely not looked under the hood to see how the
magic happens. It is a testament to their quality that most of us simply treat compilers as black
boxes: more or less readable code goes in, fast binaries come out. Sometimes, however, seemingly
innocuous changes—perhaps even meant to help the compiler—can cause surprising performance
issues which we are hard-pressed to explain without a deeper understanding of the underlying
machinery.

In this post we’ll dive into the implementation of some of the LLVM optimisation passes using
two simple examples which, nonetheless, will help us pull back the veil on the complexity involved
in producing highly-optimised code. We will see how small source changes can trigger different
paths in the compiler’s internal processing with unexpected consequences, demonstrating how
achieving high performance can be as much an art as it is a science for both compiler developers and
users. I have also included a few exercises for those interested in getting their hands dirty, but
they are not required to follow along with the main text.

I use LLVM 22.1.0 as the reference implementation throughout this post. The
examples are written in (very basic) C++23 and target x86-64, and the Assembly code uses Intel
syntax. Prior knowledge of LLVM IR is not required but it can be helpful (I recommend [A Gentle Introduction to LLVM IR](https://mcyoung.xyz/2023/08/01/llvm-ir/)).

Case 1: Modular increment
-------------------------

### The scenario

Consider the following C++ function to get the next index into an array or vector of elements
accessed in a round-robin fashion, with `cur` being the current index and `count` the number of
elements:

```
unsigned next_naive(unsigned cur, unsigned count)
{
    return (cur + 1) % count;
}
```

As written, this code requires an expensive 32-bit division instruction (6 cycles with 12-cycle
latency on an Intel IceLake core, worse in previous generations). There are, of course, numerous
tricks to replace divisions by constants with cheaper arithmetic operations—powers of two being the
best-known case—but since here `count` is a dynamic runtime value the compiler cannot help us:

```
next_naive(unsigned int, unsigned int):
        lea     eax, [rdi + 1]
        xor     edx, edx
        div     esi
        mov     eax, edx
        ret
```

However, we know something the compiler doesn’t: because `cur` is an index, it must always be
strictly smaller than `count`. We can take advantage of this to replace the division with a much
cheaper conditional move by writing:

```
unsigned next_cmov(unsigned cur, unsigned count)
{
    auto n = cur + 1;
    return n == count ? 0 : n;
}
```

```
next_cmov(unsigned int, unsigned int):
        lea     ecx, [rdi + 1]
        xor     eax, eax
        cmp     ecx, esi
        cmovne  eax, ecx
        ret
```

Could the compiler have done this transformation on its own? Let’s try out the new C++23 `assume`
attribute:

```
unsigned next_assume(unsigned cur, unsigned count)
{
    [[assume(cur < count)]];
    return (cur + 1) % count;
}
```

```
next_assume(unsigned int, unsigned int):
        lea     ecx, [rdi + 1]
        xor     eax, eax
        cmp     ecx, esi
        cmovne  eax, ecx
        ret
```

Exactly the same code as for `next_cmov()`! So how did clang figure it out?

### Peephole optimisations

When trying to understand where a certain optimisation comes from (or where it might be missing),
the first step is to identify the pass where it occurs. Currently, the most convenient way to
investigate the effects of the different LLVM optimisation passes is to use Compiler Explorer’s Opt
Pipeline view:

![Screenshot of the Compiler Explorer interface, showing the compiler panel.  The 'Add New' menu is open, with the 'Opt Pipeline' option highlighted.](https://www.hmpcabral.com/assets/images/opt/opt_pipeline.png)

(You can get the same information locally by passing the `-mllvm -print-changed` options to clang,
but without the nice highlighted diffs.)

When looking through [the evolution](https://godbolt.org/z/Mrodr17aT) of the LLVM IR for
`next_assume()`, we quickly find that the transformation from a `urem` instruction (representing the
modulo operation) to an `icmp`+`select` pair (which is eventually translated into an x86
`cmp`+`cmov`) happens in
[InstCombine](https://github.com/llvm/llvm-project/tree/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Transforms/InstCombine):

```
   %cmp = icmp ult i32 %cur, %count
   call void @llvm.assume(i1 %cmp)
   %add = add i32 %cur, 1
-  %rem = urem i32 %add, %count
+  %0 = icmp eq i32 %add, %count
+  %rem = select i1 %0, i32 0, i32 %add
   ret i32 %rem
```

InstCombine is responsible for many of the [peephole
optimisations](https://en.wikipedia.org/wiki/Peephole_optimization) that do not modify the control
flow graph, such as converting multiplications by powers of two into left shifts. It proceeds by
[visiting](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/include/llvm/IR/InstVisitor.h)
all the instructions in a function and matching them to one of many hundreds of patterns using
a generic [pattern matching
mechanism](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/include/llvm/IR/PatternMatch.h).
The pass actually runs multiple times during compilation, since other passes typically
expose new optimisation opportunities by performing different simplifications, unrolling loops, etc.

In this case the main transformation logic is quite simple and self-contained. If we look through
the `lib/Transforms/InstCombine` directory in the LLVM repository, we’ll see that the code is neatly
organised into different files for the different categories of instructions matched by the pass,
each file containing visitor methods for the opcodes of interest. One of these files is
`InstCombineMulDivRem.cpp`, where we can find the relatively short `visitURem()` method and, at the
end of it:

```
  // For "(X + 1) % Op1" and if (X u< Op1) => (X + 1) == Op1 ? 0 : X + 1 .
  if (match(Op0, m_Add(m_Value(X), m_One()))) {
    Value *Val =
        simplifyICmpInst(ICmpInst::ICMP_ULT, X, Op1, SQ.getWithInstruction(&I));
    if (Val && match(Val, m_One())) {
      Value *FrozenOp0 = Op0;
      if (!isGuaranteedNotToBeUndef(Op0))
        FrozenOp0 = Builder.CreateFreeze(Op0, Op0->getName() + ".frozen");
      Value *Cmp = Builder.CreateICmpEQ(FrozenOp0, Op1);
      return createSelectInstWithUnknownProfile(
          Cmp, ConstantInt::getNullValue(Ty), FrozenOp0);
    }
  }
```

As the comment preceding the block describes, this snippet matches exactly the pattern we used in
`next_assume()` and generates the same optimisation we wrote by hand in `next_cmov()` for cases
where it can prove that the pre-increment value is less than the modulus. To make this
guarantee, the compiler cleverly reuses the same analysis used to fold the result of `icmp`
instructions, namely the [`simplifyICmpInst()`
function](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Analysis/InstructionSimplify.cpp#L3790).
Scrolling down its implementation you can see the numerous patterns it matches; of particular
interest to us here is the `simplifyICmpWithDominatingAssume` helper, which checks all the
assumptions applicable to either side of the comparison (in the form of calls to the `llvm.assume()`
intrinsic) to see whether they imply our condition of interest. This, finally, explains
how the information we encoded in our `assume` attribute enabled the compiler to remove that pesky
division.

Looking through the implementation of `simplifyICmpInst()` also shows us other options to
communicate this precondition. For example, this version of our function is optimised in a similar
way when assertions are enabled:

```
unsigned next_assert(unsigned cur, unsigned count)
{
    assert(cur < count);
    return (cur + 1) % count;
}
```

Here, the simplification analysis uses the conditional hidden in the `assert()` macro to figure out
that we only execute the `urem` instruction if `cur < count` (see the `isImpliedByDomCondition()`
method). This can have the unexpected consequence of making builds with assertions enabled *faster*
in some cases; we can restore performance by replacing disabled assertions with `assume` attributes,
which have no runtime impact.

---

**Exercise 1:** If we try to be clever and rewrite our function using bitwise operations to avoid
the potential branch, InstCombine sees right through our trickery and produces the exact same
output:

```
unsigned next_bitwise(unsigned cur, unsigned count)
{
    auto n = cur + 1;
    return n & -(n != count);
}
```

```
   %add = add i32 %cur, 1
-  %cmp = icmp ne i32 %add, %count
-  %conv = zext i1 %cmp to i32
-  %sub = sub nsw i32 0, %conv
-  %and = and i32 %add, %sub
+  %cmp.not = icmp eq i32 %add, %count
+  %and = select i1 %cmp.not, i32 0, i32 %add
   ret i32 %and
```

Trace the execution of the pass to figure out what patterns it matches to do this. Start with the
visitor for the `sub` instruction. ([rr](https://rr-project.org/) can be very useful for this.)

---

### Loop invariants

So far all the examples we’ve seen required us to explicitly indicate, one way or another, what the
relationship was between `cur` and `count` so the code could be optimised accordingly. In other
cases this relationship might be implicit, such as when iterating through the modulo values in
a loop:

```
void iterate_1(unsigned upto, unsigned count)
{
    for (unsigned i = 0, r = 0; i < upto; ++i, r = (r + 1) % count)
        // force the compiler to calculate r instead of discarding the whole loop
        asm("" :: "r" (r));
}
```

If we look at the generated Assembly, it doesn’t seem like the compiler is smart enough to deduce
the optimisation on its own:

```
iterate_1(unsigned int, unsigned int):
        test    edi, edi
        je      .LBB4_3
        xor     edx, edx
.LBB4_2:
        inc     edx
        mov     eax, edx
        xor     edx, edx
        div     esi
        dec     edi
        jne     .LBB4_2
.LBB4_3:
        ret
```

As is often the case, though, the compiler has simply noticed something we overlooked: our
optimisation relies on having `r < count`, but if `count` is zero this condition cannot be met.
It’s instructive to see exactly how the optimiser reaches this conclusion. If we look at the IR at
the input to the first InstCombine pass, we will find that the `(X + 1) % Op1` pattern from
`visitURem()` now matches `X` to the following phi instruction:

```
  %r.0 = phi i32 [ 0, %entry ], [ %rem, %for.body ]
```

When finding a phi instruction, `simplifyICmpInst()`
[checks](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Analysis/InstructionSimplify.cpp#L525)
that the comparison can be simplified for all possible input values to the phi (in this case, zero
and the last value calculated for `r`) and, if so, that it produces the same result for all of them.
With our code above there is no way to determine whether `0 < count` and the simplification fails.
If we cover our bases by adding a `if (count == 0) return;` statement before the loop, we can close
the gap and get the expected result:

```
.LBB4_2:
        inc     ecx
        cmp     ecx, esi
        cmove   ecx, eax
        dec     edi
        jne     .LBB4_2
```

But that doesn’t explain how the compiler determined that `%rem < %count` in the second input to the
phi, when we no longer have an explicit assumption or condition to that effect. That case is
handled by [yet another
pattern](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Analysis/InstructionSimplify.cpp#L3172)
deep in the bowels of the instruction folding routines, which specifically handles comparisons
between remainders of a given modulus and the modulus itself:

```
  // icmp pred (urem X, Y), Y
  if (match(LBO, m_URem(m_Value(), m_Specific(RHS)))) {
    switch (Pred) {
    // ...
    case ICmpInst::ICMP_NE:
    case ICmpInst::ICMP_ULT:
    case ICmpInst::ICMP_ULE:
      return getTrue(ITy);
    }
  }
```

Yes, it’s patterns all the way down.

---

**Exercise 2:** If we instead change the loop condition to `i < std::min(upto, count)` the compiler
is no longer able to replace the `urem` instruction. Starting from the `isImpliedByDomCondition()`
method mentioned earlier, try to figure out where you could add support to see through min/max
idioms when evaluating implied conditions, and whether you could reuse any existing analysis code.
What if we wanted to remove the now-redundant remainder entirely?

---

### All roads

It may seem unnecessary to define an extra auxiliary variable to hold the remainder when we could
simply calculate it from the loop counter itself, even if the generated code is efficient. Let’s
get rid of it:

```
void iterate_2(unsigned upto, unsigned count)
{
    for (unsigned i = 0; i < upto; ++i)
        asm("" :: "r" (i % count));
}
```

```
iterate_2(unsigned int, unsigned int):
        test    edi, edi
        je      .LBB5_3
        xor     eax, eax
        xor     ecx, ecx
        xor     edx, edx
.LBB5_2:
        inc     ecx
        cmp     ecx, esi
        cmove   ecx, eax
        inc     edx
        cmp     edi, edx
        jne     .LBB5_2
.LBB5_3:
        ret
```

It looks like the compiler recognises the same opportunity here: the division is still replaced with
a nice conditional move, using a separate register to hold the remainder. But this doesn’t look
like the work of the InstCombine code we saw earlier; and why are we *incrementing* the loop
counter, which requires an extra comparison, rather than decrementing it and using the zero flag, as
before?

This time, if we inspect the results of the different optimisation passes, we’ll see that the
transformation comes not from InstCombine but from another pass, CodeGenPrepare, which runs shortly
before instruction selection but after the loop strength reduction (LSR) responsible for converting
the counter increment into a decrement. InstCombine can no longer match the pattern it expects,
since it does not hold that `i < count`; and, because `i` is used inside the body of the loop to
calculate the remainder, LSR can no longer replace it with a down counter. CodeGenPrepare then acts
as a sort of last resort, identifying [a specific
pattern](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/CodeGen/CodeGenPrepare.cpp#L2156)
which it can transform into almost-optimal code.

This illustrates two points which we’ll explore more in depth in the next section:

1. Compiler passes (and their code) have a fair amount of redundancy as an engineering compromise to
   maximise coverage.
2. The order of passes, including when and where they are repeated, can have a significant influence
   on the final result.

---

**Exercise 3:** LLVM ships its optimiser, aptly named `opt`, as a modular binary separate from the
compiler front-end. Save our implementation of `iterate_2()` above in an `iterate.cpp` file and try
running the following command using your local clang install:

```
clang++ -O2 -S -emit-llvm -fno-discard-value-names -o- iterate.cpp \
    | opt -S -passes="require<profile-summary>,loop-reduce,codegenprepare" -
```

You should obtain output similar to what you can observe after the CodeGenPrepare pass in the
Compiler Explorer Opt Pipeline view. What happens if you add another `loop-reduce` pass at the end?

**Exercise 4:** If we make the same change to the loop condition in `iterate_2()` as in Exercise 2,
the remainder instruction is eliminated from the generated code. What pass does this and why didn’t
it work before?

---

Case 2: Endianness conversion
-----------------------------

### The scenario

Most binary formats, whether for storage, IPC, or networking, specify a particular byte order for
numeric fields; for example, SQLite database files use big-endian fields, while Protobuf `i32` and
`i64` fields are little-endian. The customary way to write host endianness-agnostic decoding
functions is to explicitly join the individual input bytes. For 32-bit values that looks something
like (assuming a 32-bit `int` so we don’t need casts):

```
uint32_t load_le32(const uint8_t* data)
{
    return data[0] | (data[1] << 8) | (data[2] << 16) | (data[3] << 24);
}

uint32_t load_be32(const uint8_t* data)
{
    return data[3] | (data[2] << 8) | (data[1] << 16) | (data[0] << 24);
}
```

On x86, which supports unaligned loads from memory, this generates optimal Assembly at `-O1` and
above:

```
load_le32(unsigned char const*):
        mov     eax, dword ptr [rdi]
        ret

load_be32(unsigned char const*):
        mov     eax, dword ptr [rdi]
        bswap   eax
        ret
```

Some developers, suffering from chronic DRYness and faced with the prospect of writing these
functions and their 64-bit equivalents for the umpteenth time, or perhaps working with integer sizes
other than 4 and 8 bytes, would prefer to write a single generic version instead:

```
static uint64_t load(const uint8_t* data, size_t sz, bool be)
{
    uint64_t val = 0;

    for (size_t i = 0; i < sz; ++i)
        val |= static_cast<uint64_t>(data[be ? sz - i - 1 : i]) << (8 * i);

    return val;
}

uint32_t load_le32(const uint8_t* data) { return load(data, 4, false); }
uint32_t load_be32(const uint8_t* data) { return load(data, 4,  true); }
uint64_t load_le64(const uint8_t* data) { return load(data, 8, false); }
uint64_t load_be64(const uint8_t* data) { return load(data, 8,  true); }
```

Code reviewers might then reasonably worry about whether there are any performance regressions
compared to the more traditional functions. Let’s see what happens when we compile:

```
load_le32(unsigned char const*):
        mov     eax, dword ptr [rdi]
        ret

load_be32(unsigned char const*):
        mov     eax, dword ptr [rdi]
        bswap   eax
        ret

load_le64(unsigned char const*):
        mov     rax, qword ptr [rdi]
        ret

load_be64(unsigned char const*):
        mov     rax, qword ptr [rdi]
        bswap   rax
        ret
```

It looks like our lazy (or perhaps far-sighted) developer is in the clear—at least if they don’t
need to use gcc which, at least as of version 15.2, cannot optimise this code. Let’s examine the
progression of the optimisation pipeline again to gain some insight into how the compiler pulls this
off.

### Instruction selection

Given what we’ve seen in the first half of the post, it may be somewhat surprising to find through
our [trusty Opt Pipeline Viewer](https://godbolt.org/z/T9YKGTeqW) that it takes all the way until
the instruction selection phase (also known as ISel) for the consecutive loads to be folded into
single 32- or 64-bit loads. We’ll see in the next section how we can enable earlier simplification
in some cases, but let’s take some time to understand what ISel is and how it implements folding.

Instruction selection is the first phase of the compiler back-end, which runs after all the generic
optimisation passes (in LLVM this distinction is also reflected in the separation between the `opt`
and `llc` binaries). Its purpose is to convert the LLVM IR produced by the optimiser into Machine
IR (MIR), a target-specific representation of the instruction stream suitable for downstream passes
such as scheduling or register allocation. Most LLVM targets, including x86, use SelectionDAG as
their instruction selection framework. We won’t go into the weeds of SelectionDAG here;
for our purposes, it suffices to know that it includes its own peephole optimiser called
DAGCombiner, analogous to InstCombine, which can capture simplification opportunities exposed by
code generation or specific to that target.

Much like InstCombine visits each instruction in a basic block, DAGCombiner visits each node in the
DAG built from those same instructions. It’s here, among the many transformations performed by the
`or` visitor, that we find the [`MatchLoadCombine()`
method](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp#L9700):

```
/// Match a pattern where a wide type scalar value is loaded by several narrow
/// loads and combined by shifts and ors. Fold it into a single load or a load
/// and a BSWAP if the targets supports it.
```

This is, of course, the exact pattern we see in the LLVM IR at the input to SelectionDAG, after
`load()` is inlined, constant arguments propagated, and the loops fully unrolled. What’s
interesting about this method, though, is that it doesn’t perform a simple pattern match as we’ve
seen before in InstCombine, but instead tracks the origin of every single byte at the output of the
`or` instruction recursively through the DAG (using the auxiliary [`calculateByteProvider()`
function](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp#L9272)),
not just from loads but also through bitwise operations, byte swaps, and zero/sign extensions. This
makes it powerful enough to also handle expressions like:

```
static uint64_t load_alt(const uint8_t* data, size_t sz, bool be)
{
    uint64_t val = 0;

    for (size_t i = 0; i < sz; ++i)
        val = (val << 8) | data[be ? i : sz - i - 1];

    return val;
}
```

In this case, however, [we find](https://godbolt.org/z/o666enfWv) that only the 32-bit functions are
fully optimised. Although we have exactly the same number of LLVM IR instructions as before, this
new version requires recursing deeper into the DAG to uncover the source of the bytes loaded
earliest (since we do two operations on the output variable per iteration, instead of one), hitting
the hard-coded limit of ten levels of recursion. This is a good example of how having a mental map
of the compiler’s internal processing, as well as sticking to more common patterns, can help us
avoid such pathological cases.

### Helping the compiler

Some seasoned C++ developers may have instinctively objected to this example. After all, if we only
have a few possible argument values known at compile-time, why wouldn’t we just template our
function rather than relying on the compiler to propagate the constants?

```
template <size_t sz, bool be>
static uint64_t load(const uint8_t* data)
{
    uint64_t val = 0;

    for (size_t i = 0; i < sz; ++i)
        val |= static_cast<uint64_t>(data[be ? sz - i - 1 : i]) << (8 * i);

    return val;
}

uint32_t load_le32(const uint8_t* data) { return load<4, false>(data); }
uint32_t load_be32(const uint8_t* data) { return load<4,  true>(data); }
uint64_t load_le64(const uint8_t* data) { return load<8, false>(data); }
uint64_t load_be64(const uint8_t* data) { return load<8,  true>(data); }
```

The [output](https://godbolt.org/z/obEjMjGs1) is unchanged, but this time the IR for the
little-endian functions is optimised into a single load long before we reach the instruction
selection stage, in a pass called
[AggressiveInstCombine](https://github.com/llvm/llvm-project/tree/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Transforms/AggressiveInstCombine).
Like InstCombine, this pass performs a variety of peephole optimisations, but it’s focused on those
which tend to be less commonly needed or take longer to run, which is why it runs only once at `-O2`
(and not at all at `-O1`). One of these optimisations is implemented in the
[`foldConsecutiveLoads()`
function](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Transforms/AggressiveInstCombine/AggressiveInstCombine.cpp#L790),
which matches patterns of the form “bitwise-or of (optionally) left-shifted, zero-extended,
consecutive loads”, such as the ones we find in our functions.

Since it relies on simple pattern matching, AggressiveInstCombine is not as powerful as DAGCombiner;
in particular, it cannot optimise the fold used in `load_alt()` above even for 32 bits. It also has
no impact on our big-endian loads because, as a middle-end optimisation pass (unlike DAGCombiner,
which is part of the compiler back-end), it tries to produce target-independent IR as much as
possible. Folding a big-endian load on a little-endian target, and vice-versa, would require adding
a target-specific byte-swap intrinsic which would complicate downstream analysis and optimisation
passes.

---

**Exercise 5:** Template the `load_alt()` function as in this section and examine the resulting
output. Does it match our earlier results? What does this tell us about the interaction between
templating and the optimisation pipeline?

**Exercise 6:** Instead of loading bytes in a different order depending on endianness, we can also
fix the order and optionally use the `__builtin_bswap64()` intrinsic on the return from `load()`.
How does this affect the ability of AggressiveInstCombine to optimise the code?

---

### Ordering, redux

Why didn’t AggressiveInstCombine come into play in our initial non-templated version? If we inspect
the optimisation pipeline, we’ll find that earlier the pass ran after `load()` was inlined but,
crucially, before the loop was unrolled, so there was no pattern to match yet. Function templates,
on the other hand, are instantiated separately for each unique combination of parameters, so by the
time they are inlined the loops have already been fully unrolled (since the iteration count is
known) and can be matched by `foldConsecutiveLoads()`. We can obtain the same result with the
initial code by manually running:

```
clang++ -S -emit-llvm -O2 -o- endianness.cpp \
    | opt -S -passes='aggressive-instcombine' - \
    | llc --x86-asm-syntax=intel
```

This also exemplifies an important principle of function inlining in LLVM (I’m not sure about other
compilers): whenever possible, callees are simplified before callers in order to improve the
accuracy of the inlining cost heuristics. The more information is available to the optimiser before
inlining, the better it can make those decisions. In general, in fact, the earlier in the pipeline
we can enable specific simplifications, the more optimised the final result will be (see the
exercises for more examples of this).

---

**Exercise 7:** If we comment out all of the specialised functions but `load_le32()` we get similar
results as when we template `load()`, i.e. AggressiveInstCombine successfully folds the
consecutive loads. What optimisation pass enables this? How can we restructure
performance-critical code to take advantage of it?

**Exercise 8:** If we now keep only `load_le64()` but replace `load()` with `load_alt()` above, the
DAGCombiner is able to fully optimise the resulting LLVM IR. Compare with our earlier results to
understand why this is the case.

---

If you’ve read this far you may be under the impression that, while they may not be magic,
optimisers are at the very least superhuman. Let’s quickly dispel that notion by looking at two
examples where the obvious thing to do turns out not to be so obvious for the compiler.

We’ll start by adding a small (and pretty useless) function to our initial example:

```
uint32_t load_le32(const uint8_t* data) { return load(data, 4, false); }

uint32_t load_add_le32(const uint8_t* data)
{
    return load_le32(data) + data[0];
}
```

Take a moment before continuing to consider how you would expect this function to be compiled. Two
loads and an add? Perhaps a load, zero extension of the low byte, and an add?

Now [compare](https://godbolt.org/z/MaM7n9aYT) with the actual result:

```
load_add_le32(unsigned char const*):
        movzx   ecx, byte ptr [rdi]
        movzx   edx, word ptr [rdi + 1]
        shl     edx, 8
        movzx   eax, byte ptr [rdi + 3]
        shl     eax, 24
        or      eax, edx
        or      eax, ecx
        add     eax, ecx
        ret
```

Huh. What happened here?

Remember that the loads aren’t folded together until we reach the ISel phase, so by the time
`load_le32()` is inlined it’s not yet fully optimised. It turns out DAGCombiner, when tracking the
origin of each byte in the load, specifically [rules
out](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/CodeGen/SelectionDAG/DAGCombiner.cpp#L9280)
bytes which are used elsewhere in the function to prevent introducing duplicate loads. This can be
sensible in general (even cache hits have a cost, after all), but it’s clearly suboptimal in this
case.

Can we make use of AggressiveInstCombine to “hide” the duplicate load from DAGCombiner? The answer
turns out to be yes, but we must be careful. This, for example, won’t work:

```
uint32_t load_add_le32(const uint8_t* data)
{
    return load<4, false>(data) + data[0];
}
```

Although AggressiveInstCombine does run after `load<4, false>()` is inlined here, it also
[refuses](https://github.com/llvm/llvm-project/blob/4434dabb69916856b824f68a64b029c67175e532/llvm/lib/Transforms/AggressiveInstCombine/AggressiveInstCombine.cpp#L654)
to create duplicate loads. As the saying goes, however, there’s no problem that cannot
be solved with another layer of indirection: if we instead call the function template from
`load_le32()`, we can get AggressiveInstCombine to optimise the unrolled loop *before* it’s inlined
in `load_add_le32()`, [producing](https://godbolt.org/z/xdGz479nq) the desired result (the
additional cleverness to avoid a second load comes courtesy of the GVN pass).

---

**Exercise 9:** What happens if we use `val & 0xFF` instead of `data[0]` in the examples above, and
why? Can you make a small change to make this work regardless of which function we call?

---

For our second and final act, let’s reconsider what we’re optimising for in the first place. We
have been focusing on performance in the sense of execution time by using the `-O<n>` flags. But
what about optimising for size with `-Os`? In this case, they happen to coincide: surely you cannot
get any faster *or* smaller than a single 32- or 64-bit load. But does the compiler agree?

Unfortunately, it [does not](https://godbolt.org/z/Yz5qjM53h). With the curious exception of
`load_be32()` (or, more precisely, `load<4, true>()`), it has decided that unrolling the loops would
go against its mandate to minimise code size, making it impossible for downstream passes to fold the
loads. The solution here is to nudge it politely using `#pragma unroll` before the loop, allowing
AggressiveInstCombine or DAGCombiner to do their job properly. (You can also avoid pragmas by
writing a recursive function template if that’s more to your taste.)

Conclusion
----------

What can we take away from this somewhat meandering exploration? Perhaps the overarching theme is:
get familiar with your compiler and what it can and cannot do for you. More actionable advice:

1. Use language facilities to make your intent clear. If you know something at compile-time, all
   else being equal, you can help the optimiser by stating it explicitly through e.g. C++ templates
   or Rust macros. In some cases it may even be preferable to choose at runtime from among a small
   set of specialised functions, instead of using a single generic function which cannot be
   optimised.
2. Maximise the potential for early optimisation through things like templating (again), auxiliary
   variables, explicit constraints, or specialised functions. Having at least a rough idea of the
   different optimisation passes and their order can help with this. The earlier the compiler can
   optimise something, the greater the opportunity for beneficial knock-on effects.
3. Stick to well-known patterns. The more common a construction is, the more likely that someone
   else already did the hard work of making the compiler recognise and optimise it. Simple code
   beats clever nine times out of ten.

---

Appendix: other resources
-------------------------

Haven’t had enough yet? Here are some helpful resources if you’re interested in diving deeper into
LLVM in general and the optimiser in particular: