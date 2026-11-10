---
title: "Branchless Rust: Making a Filter 4x Faster by Removing an If"
url: https://www.greyblake.com/blog/branchless-rust/
clipped: 2026-08-31 12:22:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Branchless Rust: Making a Filter 4x Faster by Removing an If](https://www.greyblake.com/blog/branchless-rust/)

## Digest Summary
The article examines a hot‑path filter in Rust that selects elements greater than a threshold from a slice of f64 values. Benchmarking on an Intel i7‑10875H shows the idiomatic iter().filter(...).collect() is fastest when the branch predictor can reliably guess (1 % or 99 % selectivity) but slows dramatically at ~50 % selectivity because each unpredictable if x &gt; threshold causes frequent mispredictions, incurring ~15‑20 cycle penalties per miss. Pre‑allocating the output vector yields only a marginal gain, confirming the bottleneck is branch misprediction, not reallocations.
A branchless version replaces the conditional push with unconditional writes to a pre‑sized buffer, advancing the write index by (x &gt; threshold) as usize. This converts the control dependency into a data dependency, eliminating the mispredicted branch. Benchmarks show up to a 4× speedup in the worst case, making runtime flat across selectivities, while the best case (highly predictable branch) becomes slower due to unnecessary writes. The author advises using branchless code only after profiling hot loops with unpredictable branches, as it reduces readability and can hurt best‑case performance.

---

## Full Article

# [Branchless Rust: Making a Filter 4x Faster by Removing an if](https://www.greyblake.com/blog/branchless-rust/)

         Serhii Potapov  August 02, 2026  #[rust](https://www.greyblake.com/tags/rust/)  #[branchless](https://www.greyblake.com/tags/branchless/)  #[optimization](https://www.greyblake.com/tags/optimization/) 

    

DISCLAIMER: this article contains parts of text written with help of an LLM.

Most of my career I spent in the domain world programming, where correctness matters much more
than performance. Using Rust already made things fast enough. Avoid the N+1 SQL queries problem
and usually we are good.

But recently I found myself in a situation where I actually had to optimize a hot path.
This is how I discovered the branchless programming technique, and its results blew my mind.
Let me share it with you on a small example.

## The problem

Let's keep things simple. We need to filter a slice of numbers and return the elements that are
greater than a given threshold (a typical problem that database engines solve all day long).
Normally I would write the following code:
 ` `pub fn filter_iter(input: &[f64], threshold: f64) -> Vec<f64> {
    input.iter().copied().filter(|&x| x > threshold).collect()
}` ` 

Easy to read, idiomatic, correct. Usually I would not touch it ever again.
But what if this beast happens to be on a hot path? Let's benchmark it!

The input is one million random  `f64`  values uniformly spread over  `0.0..100.0` .
Instead of one threshold we will try several, chosen so that the filter keeps 1%, 25%, 50%, 75%
or 99% of the elements. For example, the threshold  `50.0`  keeps about a half.

The benchmarks are made with [criterion](https://crates.io/crates/criterion) and live in the
[branchless-rust-benchmarks](https://github.com/greyblake/branchless-rust-benchmarks) repo,
so you can reproduce everything on your own machine.

## Puzzling results

Here is what criterion reports on my laptop (Intel i7-10875H):
keptoutput sizetime
1%~10k0.59 ms
25%~250k2.69 ms
50%~500k3.94 ms
75%~750k2.75 ms
99%~990k1.49 ms

Look at the 50% row. We copy only half of the elements, yet it is the slowest case of all.
Keeping 99% means copying almost twice as much data, and still it is 2.6 times faster.

The amount of input is identical in every row, and the amount of output clearly does not
explain the timings. Something else is going on.

## First instinct: preallocate

Let's rule out the usual suspect first.  `collect()`  does not know the output size in advance,
so the  `Vec`  grows and reallocates along the way. Every Rust developer has a reflex for that:
preallocate!
 ` `pub fn filter_prealloc(input: &[f64], threshold: f64) -> Vec<f64> {
    let mut out = Vec::with_capacity(input.len());
    for &x in input {
        if x > threshold {
            out.push(x);
        }
    }
    out
}` ` 

The result at 50% kept: 3.87 ms. About 2% faster.
The reallocations were real, but they were never the bottleneck. Then what is?

## What CPUs do behind our back

Let's stop for a moment and refresh how CPUs actually work.

A modern CPU does not execute one instruction at a time. It runs a deep
[pipeline](https://en.wikipedia.org/wiki/Instruction_pipelining): while one instruction executes,
the next ones are already being fetched and decoded. This works beautifully, until the
instruction stream hits a fork in the road:
 ` `if x > threshold { /* keep */ } else { /* skip */ }` ` 

Which way does the road go? The CPU cannot know until the comparison actually finishes.
And it refuses to wait. Instead it guesses (the hardware responsible for guessing is called the
[branch predictor](https://en.wikipedia.org/wiki/Branch_predictor)) and speculatively runs ahead
along the guessed path.

The predictor is like a barista who starts making your usual order the moment you walk in.
If you are a regular, this is fantastic: the coffee is ready when you reach the counter.
If you order something random every day, the barista keeps pouring drinks into the sink.

A wrong guess is expensive. The CPU has to throw away everything it started speculatively,
flush the pipeline and restart from the fork. On a typical modern x86 core this costs around
15-20 cycles.
The comparison itself costs about one.

Now [our table](https://www.greyblake.com/blog/branchless-rust/#puzzling-results) starts to make sense:

- Keep 1%: the answer is almost always "skip". The predictor guesses "skip" and is right
99% of the time. Nearly free.

- Keep 99%: the same story in the opposite direction.

- Keep 50% of random data: there is no pattern to learn. The predictor is reduced to a coin
flip and is wrong on every second element. That is half a million pipeline flushes. At 15-20
cycles each it adds up to roughly 2 ms of pure penalty on a 4 GHz core, which is pretty much
the gap between the 50% and the 99% rows.

Note that the villain is not the branch itself. It is the branch that depends on unpredictable
data. Which suggests a fun experiment.

## The smoking gun

If mispredictions are the problem, we should be able to keep the same data, the same threshold
and the same code, and change only the order of the elements. Let's sort the input (outside of
the measured section, of course) and rerun the 50% case:
input, 50% kepttime
shuffled4.15 ms
sorted0.93 ms

Same million floats. Same threshold. Same function. 4.5 times faster. On sorted data the
branch says "skip" for the entire first half and "keep" for the entire second half. Such a
pattern even the simplest predictor learns after one miss.

Stack Overflow has a question with 27K upvotes and it's exactly about that effect:
["Why is processing a sorted array faster than processing an unsorted array?"](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array).

Of course, sorting the input is not a fix: sorting costs much more than the filtering itself,
and we usually need the original order anyway. But now we know what exactly to fix.
Can we keep the data shuffled and still avoid the coin flip?

## Welcome branchless programming

The idea of branchless programming is to remove the unpredictable branch entirely, so there is
nothing to guess. Instead of deciding whether to write an element, we always write it, and use
the comparison to decide where the next element goes:
 ` `pub fn filter_branchless(input: &[f64], threshold: f64) -> Vec<f64> {
    let mut out = vec![0.0; input.len()];
    let mut n = 0;
    for &x in input {
        out[n] = x;
        n += (x > threshold) as usize;
    }
    out.truncate(n);
    out
}` ` 

Take a minute to appreciate the trick:

- Every element is written to  `out[n]`  unconditionally.

-  `(x > threshold) as usize`  is  `1`  when we keep the element and  `0`  otherwise.

- If the element is kept, the cursor  `n`  moves forward. If not, the next iteration simply
overwrites the rejected value.

- At the end  `n`  holds the number of kept elements, and  `truncate(n)`  cuts off the garbage tail.

The comparison is still there, but its result is now used as a number, not as a decision
where the program goes next. In compiler terms, we turned a control dependency into a data
dependency. Indeed, in the generated assembly the comparison becomes a  `seta`  instruction that
just produces 0 or 1. There is no fork in the road anymore, so there is nothing to mispredict.

(A careful reader may object:  `out[n] = x`  performs a bounds check, and the loop condition is
also a branch. True! But those branches go the same way a million times in a row, so the
predictor handles them for free. Only the unpredictable branch had to go.)

The results:
keptiterbranchless
1%0.59 ms1.09 ms
25%2.69 ms1.05 ms
50%3.94 ms1.03 ms
75%2.75 ms1.02 ms
99%1.49 ms1.11 ms

The worst case became almost 4 times faster. And look how flat the branchless column is:
the running time does not depend on the data anymore, exactly as we wanted.

Notice the price we paid though. At 1% kept the idiomatic version wins, because an almost
always correctly predicted branch is nearly free, while the branchless version always pays for
one million writes. Branchless code is not faster in general: it trades the best case for
the worst case.

## Should you go branchless?

Most of the time, no. Branchless code is harder to read and easier to get wrong. Besides,
compilers know a lot of tricks and already do a lot of this work for us.

Only when a profiler points at a hot loop, and the loop contains a branch on unpredictable data
this technique can pay off big.

## Conclusions

- A branch is cheap. A mispredicted branch is not.

- That is why the same filter is slowest around 50% selectivity on shuffled data: the branch
predictor is reduced to a coin flip.

- Branchless programming replaces the unpredictable branch with plain arithmetic: always write,
conditionally advance. The worst case got almost 4 times faster and became independent of
the data.

- It is a trade, not magic: the best case gets worse, and readability suffers. Reserve it for
measured hot paths.

## Links

- [branchless-rust-benchmarks - code and benchmarks from this article](https://github.com/greyblake/branchless-rust-benchmarks)

- [Why is processing a sorted array faster than processing an unsorted array? - Stack Overflow](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array)

- [Branch predictor - Wikipedia](https://en.wikipedia.org/wiki/Branch_predictor)

- [Mispredicted branches can multiply your running times - Daniel Lemire](https://lemire.me/blog/2019/10/15/mispredicted-branches-can-multiply-your-running-times/)

- [Branchless Programming in C++ - Fedor Pikus, CppCon 2021](https://www.youtube.com/watch?v=g-WPhYREFjk)

## P.S.

This post went viral on [Reddit](https://www.reddit.com/r/rust/comments/1ve5j4h/branchless_rust_making_a_filter_4x_faster_by/)
and [HackerNews](https://news.ycombinator.com/item?id=49151991).

Since it's being discussed a lot and it seems to be very important for some people: yes, I used LLM to help me to assemble the article. I've added a DISCLAIMER at the top.

For me, as for many of others, LLM is just a tool that helps to archive a goal faster. I am not pushing the content blindly: I structure it, read it, review it, and edit until I am satisfied with the result.

[Back to top](https://www.greyblake.com/blog/branchless-rust/#)
    
    
      
        

### Index

        
          [The problem](https://www.greyblake.com/blog/branchless-rust/#the-problem)
        
        
          [Puzzling results](https://www.greyblake.com/blog/branchless-rust/#puzzling-results)
        
        
          [First instinct: preallocate](https://www.greyblake.com/blog/branchless-rust/#first-instinct-preallocate)
        
        
          [What CPUs do behind our back](https://www.greyblake.com/blog/branchless-rust/#what-cpus-do-behind-our-back)
        
        
          [The smoking gun](https://www.greyblake.com/blog/branchless-rust/#the-smoking-gun)
        
        
          [Welcome branchless programming](https://www.greyblake.com/blog/branchless-rust/#welcome-branchless-programming)
        
        
          [Should you go branchless?](https://www.greyblake.com/blog/branchless-rust/#should-you-go-branchless)
        
        
          [Conclusions](https://www.greyblake.com/blog/branchless-rust/#conclusions)
        
        
          [Links](https://www.greyblake.com/blog/branchless-rust/#links)
        
        
          [P.S.](https://www.greyblake.com/blog/branchless-rust/#p-s)
