---
title: "Understanding the Go Runtime: The Scheduler"
url: https://internals-for-interns.com/posts/go-runtime-scheduler/
clipped: 2026-06-17 01:33:40
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Go Runtime
  - GMP Model
  - Goroutine Scheduling
  - Work Stealing
  - Context Switching
  - Concurrency
related:
  - "[[Prolog Coding Horror]]"
  - "[[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article details Go's GMP scheduler architecture, explaining how goroutines (G), threads (M), and processors (P) coordinate for lock-free concurrency and fast context switching.
>
> **Key points:**
> - The GMP model divides scheduling into Goroutines (G), OS Threads (M), and Scheduling Contexts (P).
> - A P contains local run queues, a runnext fast-pass slot, and local memory caches to avoid global locking on hot paths.
> - When system calls block threads (M), the runtime detaches the P and hands it to a free thread to keep work moving.
> - Stack growth and preemption (both cooperative and signal-based asynchronous) prevent goroutines from starving CPU cores.
>
> **Concept links:** [[Go Runtime]], [[GMP Model]], [[Goroutine Scheduling]], [[Work Stealing]], [[Context Switching]], [[Concurrency]]
>
> **Suggested connections:**
> - [[Prolog Coding Horror]] — related comparison of runtime concurrency models.
> - [[Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc]] — related systems runtime architecture.
<!-- ai-summary:end -->

# [Understanding the Go Runtime: The Scheduler](https://internals-for-interns.com/posts/go-runtime-scheduler/)

## Digest Summary
The article explains Go’s GMP scheduler architecture and the lifecycle of a goroutine.

- **GMP model**: G (goroutine) holds a small stack, registers, status, and M pointer; M (OS thread) executes code and owns a special g0 goroutine for runtime work; P (processor) provides scheduling context, a local run queue (up to 256 Gs), run‑next slot, free‑list cache, and per‑P mcache. The number of Ps equals GOMAXPROCS.

- **Global scheduler state (schedt)** stores the global run queue, global free list, idle P/M lists, spinning‑thread count, and GC/trace flags, protected by a short‑lived lock.

- **Goroutine lifecycle**: creation reuses dead Gs from local/global free lists; initialized to _Grunnable and placed in a P’s run‑next slot; runs on an M/P, then may block (channel, mutex, sleep) via gopark, or enter a syscall (entersyscall) while retaining its P. System‑call blocking can trigger sysmon to reassign the P. Stack growth doubles the stack when needed. Preemption occurs cooperatively via compiler‑injected checks or asynchronously via SIGURG; preempted Gs return to _Grunnable.

- **Scheduling loop**: schedule() repeatedly calls findRunnable(), which checks GC/trace work, a global‑queue fairness grab (every 61 calls), the local run‑next slot, the local queue, the global queue (batch), netpoller, and finally work‑stealing from other Ps. If no work, the M may spin briefly before parking.

- **Context switch**: mcall/gogo save/restore only SP, PC, BP (~50‑100 ns), far faster than OS thread switches.

The design decouples Ms, Ps, and Gs to keep cores busy, minimize lock contention, and enable fast, scalable goroutine execution.

## Discussion Summary
The provided input contains only a single comment expressing personal enjoyment of two GopherCon talks, without any broader discussion or additional viewpoints to aggregate. Consequently, there is insufficient material to form a 50–100‑word summary of overall sentiment, themes, or collective opinions.

---

## Full Article

In the [previous article](https://internals-for-interns.com/posts/go-memory-allocator/)
we explored how Go’s memory allocator manages heap memory â grabbing large arenas from the OS, dividing them into spans and size classes, and using a three-level hierarchy (mcache, mcentral, mheap) to make most allocations lock-free. A key detail was that each **P** (processor) gets its own memory cache. But we never really explained what a P *is*, or how the runtime decides which goroutine runs on which thread. That’s the scheduler’s job, and that’s what we’re exploring today.

The scheduler is the piece of the runtime that answers a deceptively simple question: **which goroutine runs next?** You might have hundreds, thousands, or even millions of goroutines in your program, but you only have a handful of CPU cores. The scheduler’s job is to multiplex all those goroutines onto a small number of OS threads, keeping every core busy while making sure no goroutine gets starved.

If you’ve ever used goroutines and channels, you’ve already benefited from the scheduler without knowing it. Every `go` statement, every channel send and receive, every `time.Sleep`âthey all interact with the scheduler. Let’s see how it works.

Let’s start with the fundamental building blocks â the three structures that the entire scheduler is built around.

The GMP Model
-------------

The scheduler is built around three concepts, commonly called the **GMP model**: **G** (goroutine), **M** (machine/OS thread), and **P** (processor). We touched on these during the bootstrap article, but now let’s look at them properly.

Let’s look at each one.

### G â Goroutine

A **G** is a goroutine â the Go runtime’s representation of a piece of concurrent work. Every time you write `go f()`, the runtime creates (or reuses) a G to track that function’s execution.

What does a G actually carry? The struct has a lot of fields, but the ones I think are most useful for understanding how it works are: a small **stack** (starting at just 2KB), some **saved registers** (stack pointer, program counter, etc.) so the scheduler can pause it and resume it later, a **status** field that tracks what the goroutine is doing (running, waiting, ready to run), and a pointer to the **M** currently running it. The full struct in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go#L473)
has a lot more â fields for panic and defer handling, GC assist tracking, profiling labels, timers, and more.

Compare that to an OS thread, which typically starts with a 1â8MB stack and carries a lot of kernel state. A goroutine is *dramatically* lighter â that’s why you can have millions of them in a single program. An OS thread? You’ll start feeling the pressure at a few thousand.

So goroutines are the work. But someone has to actually execute that work â the CPU doesn’t know what a goroutine is. It only knows how to run threads.

### M â Machine (OS Thread)

An **M** (defined in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go#L618)
) is an OS thread â the thing that actually executes code. The scheduler’s job is to put goroutines onto Ms so they can run.

Every M has two goroutine pointers that are worth knowing about. The first is **`curg`** â the user goroutine currently running on this thread. That’s your code. The second is **`g0`** â and every M has its own. g0 is a special goroutine that’s reserved for the runtime’s own housekeeping â scheduling decisions, stack management, garbage collection bookkeeping. It has a much larger stack than regular goroutines: typically 16KB, though it can be 32KB or 48KB depending on the OS and whether the race detector is enabled. Unlike regular goroutines, the g0 stack **doesn’t grow** â it’s fixed at allocation time, so it has to be big enough upfront to handle whatever the runtime needs to do. When the scheduler needs to make a decision (which goroutine to run next, how to handle a blocking operation), it switches from your goroutine to this M’s g0 to do that work. Think of g0 as the M’s “manager mode” â it runs the scheduling logic, then hands control back to a user goroutine.

An M also has a pointer to the **P** it’s currently attached to. This is important: without a P, an M can’t run Go code. It’s just an idle OS thread sitting there doing nothing. Why does an M need a P at all?

### P â Processor

This is the clever part of the design. A **P** (defined in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go#L772)
) is not a CPU core and it’s not a thread â it’s a **scheduling context**. Think of it as a workstation: it has everything a goroutine needs to run efficiently, and an M has to sit down at one before it can do any real work.

Why not just let Ms run goroutines directly? The problem is system calls. When an M enters the kernel, the entire OS thread blocks â and if all the scheduling resources were attached to the M, they’d be stuck too. The run queue, the memory cache, everything would be frozen until the syscall returns. By putting all of that on a separate P, the runtime can detach the P from a blocked M and hand it to a free one. The work keeps moving even when a thread is stuck.

So each P carries its own **local run queue** â a list of up to 256 goroutines that are ready to run. It also has a **runnext** slot, which is like a fast-pass for the very next goroutine to execute. There’s a **gFree list** where finished goroutines are kept around so they can be recycled instead of allocated from scratch. It even carries its own **mcache** â the per-P memory cache we saw in the [memory allocator](https://internals-for-interns.com/posts/go-memory-allocator/)
article. And because each P has its own copy of all this stuff, the threads using it don’t need to fight over shared locks all the time â that’s a nice bonus.

The number of Ps is controlled by `GOMAXPROCS`, which defaults to the number of CPU cores. So on an 8-core machine, you have 8 Ps, meaning at most 8 goroutines can truly run in parallel at any moment. But you can have far more Ms than Ps â some might be blocked in system calls while others are actively running goroutines. The key is that only `GOMAXPROCS` of them can be running Go code at any given time.

This decoupling is the heart of the scheduler’s design, and we’ll see why it matters so much as we go through the rest of the article.

So we have Gs, Ms, and Ps â but somebody needs to keep track of all of them. That’s the `schedt` struct.

### The Scheduler State (schedt)

The **`schedt`** struct (defined in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go#L930)
) is the global scheduler state. There’s exactly one instance of it â a global variable called `sched` â and it holds everything that doesn’t belong to any specific P or M. Think of it as the shared bulletin board that the Ps and Ms check when they need to coordinate.

What lives there? First, the **global run queue** (`runq`) â a linked list of goroutines that aren’t in any P’s local queue. These are goroutines that overflowed from a full local queue, or that came back from a system call and couldn’t find a P. There’s also a **global free list** (`gFree`) of dead goroutines waiting to be recycled â when a P’s local free list runs out, it refills from here, and when a P has too many dead goroutines, it dumps some back. The same two-level pattern we saw in the memory allocator: local caches for the fast path, shared pool as backup.

Then there are the **idle lists**. When a P has no M running it, it goes on the `pidle` list. When an M has no work and no P, it goes on the `midle` list and sleeps. The scheduler also tracks how many Ms are currently **spinning** (looking for work) in `nmspinning` â we’ll explain what spinning means [later in the article](https://internals-for-interns.com/posts/go-runtime-scheduler/#spinning-threads)
â and whether the **GC is requesting a stop-the-world pause** in `gcwaiting`. All of this shared state is protected by `sched.lock` â but the lock is designed to be held very briefly, because the hot path (picking a goroutine from a local queue) doesn’t touch `schedt` at all.

Beyond `schedt`, the runtime keeps **master lists** of every G, M, and P that has ever been created â the global variables `allgs`, `allm`, and `allp`. These aren’t used for scheduling decisions. They exist so the runtime can find *everything* when it needs to do something global, like scanning all goroutine stacks during garbage collection or checking for stuck system calls in sysmon.

Here’s the full picture:

![Go Scheduler Diagram](https://internals-for-interns.com/images/posts/go-scheduler-diagram.webp)

Now that we’ve set the stage, it’s time to see the actors in action. Let’s follow a goroutine through its lifetime and see how it moves across this battlefield.

The Life of a Goroutine
-----------------------

Let’s follow the life of a goroutine from birth to death â and sometimes back again. The states are defined in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go#L17)
, but rather than listing them, let’s walk through the story.

### Birth: Creation and First Steps

It starts when you write `go f()`. The compiler turns this into a call to `newproc()` (in [`src/runtime/proc.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/proc.go#L5295)
), and the runtime needs a G struct to represent this new goroutine. But it doesn’t necessarily allocate one from scratch â first, it checks the current P’s **local free list** of dead goroutines. If there’s one available, it gets recycled, stack and all. If the local list is empty, it tries to grab a batch from the **global free list** in `schedt`. Only if both are empty does the runtime allocate a new G with a fresh 2KB stack. This reuse is why goroutine creation is so cheap â most of the time, it’s just pulling a G off a list and reinitializing a few fields.

If the G was recycled from the free list, it’s already in **\_Gdead** state â that’s where goroutines go when they finish. If it was freshly allocated, it starts in **\_Gidle** (a blank struct, never used before) and immediately transitions to **\_Gdead**. Either way, the G is in **\_Gdead** before setup begins. Wait â dead already? Yes, but only technically. **\_Gdead** means “not in use by the scheduler” â it’s the state for goroutines that are either being set up or finished and waiting for reuse. The runtime uses it as a safe “parked” state while it configures the G’s internals.

During initialization, the runtime prepares the goroutine so it’s ready to run. It sets the **stack pointer** to the top of its stack, points the **program counter** at your function so it knows where to start executing, and places a return address pointing to `goexit` â the goroutine cleanup handler. This way, when your function finishes and returns, execution naturally lands in `goexit` without needing any special “is it done?” check.

Once setup is complete, the G moves to **\_Grunnable** and goes into the current P’s **runnext** slot, displacing whatever was there before. This means the new goroutine will run very soon â right after the current goroutine yields.

Now the goroutine is alive â sitting on a run queue, ready to execute, just waiting for an M to pick it up.

### Running

When the scheduler picks this G off the queue, it transitions to **\_Grunning**. This is the active state â the goroutine is executing your code on an M, with a P. This is where it spends its productive time.

But goroutines rarely run straight through to completion. At some point, something will interrupt the flow, and what happens next depends on *why* the goroutine stopped. This is where the story branches.

### Blocking and Unblocking

Maybe the goroutine tries to receive from an empty channel, or acquire a locked mutex, or sleep. Here’s a detail that might surprise you: there’s no external “scheduler thread” that swoops in and parks the goroutine. **The goroutine parks itself.**

Let’s say your goroutine does `<-ch` on an empty channel. The channel implementation sees there’s nothing to receive, so it calls `gopark()` to park the goroutine until a value arrives. The goroutine switches to the g0 stack, changes its own status to **\_Gwaiting**, and adds itself to the channel’s wait queue. After that, it’s gone from the scheduler’s perspective â not on any run queue, just sitting on the channel’s internal wait list. The M doesn’t go to sleep though. It calls `schedule()` and picks up the next goroutine. From the M’s point of view, one goroutine parked and another one started running â the M stayed busy the whole time.

`gopark()` also records *why* the goroutine is blocking â channel receive, mutex lock, sleep, select, and so on. This is what shows up when you look at goroutine dumps or profiling data, so you can tell exactly what each goroutine is waiting for.

Now for the other side: what happens when the thing the goroutine was waiting for finally happens? Say another goroutine sends a value on that channel. The sender finds our goroutine on the channel’s wait queue, copies the value directly to it, and calls `goready()`. This changes the goroutine’s status back to **\_Grunnable** and places it in the sender’s **runnext** slot â meaning it’ll run very soon, right after the sender yields. This runnext placement creates a tight back-and-forth between producer and consumer goroutines. G1 sends, G2 receives and runs immediately, G2 sends back, G1 receives and runs immediately â almost like coroutines handing off to each other, with minimal scheduling overhead.

### System Calls

Blocking on channels and mutexes is one thing â the goroutine parks, but the M and P stay free. System calls are a different beast, because they block the entire OS thread.

When a goroutine makes a system call â reading a file, accepting a network connection, anything that enters the kernel â the **entire OS thread blocks**. Before entering the kernel, the goroutine calls `entersyscall()`, which saves its context and changes its status to **\_Gsyscall**. But here’s an important detail: the M **doesn’t give up its P**. It keeps it. Why? Because most system calls are fast â a few microseconds â and the goroutine will come back and keep running on the same P as if nothing happened. No locks, no coordination, no overhead.

But as soon as the goroutine is in \_Gsyscall, it’s in danger of **losing** its P. If the system call takes too long, **sysmon** can come along and **retake the P** â detach it from the blocked M and hand it to another thread so the goroutines in its run queue keep running. This is where the G-M-P decoupling really pays off: the thread is stuck in the kernel, but the work moves on.

When the system call finishes, the goroutine checks whether it still has its P. If it does â great, keep going. If sysmon took it, the goroutine tries to grab any idle P. And if there are no idle Ps at all, it puts itself on the **global run queue** and waits to be picked up. We’ll cover sysmon in more detail in a following article.

So far we’ve seen goroutines block voluntarily â on channels, mutexes, and system calls. But there’s something more subtle happening behind the scenes every time a goroutine calls a function.

### Stack Growth

There’s another thing that can happen while a goroutine is running: it can run out of stack space. Go goroutines start with a tiny 2KB stack, and unlike OS threads, they don’t get a fixed-size stack upfront. Instead, the compiler inserts a small check called the **stack growth prologue** at the beginning of most functions. This check compares the current stack pointer against the stack limit â if there’s not enough room for the next function call, the runtime steps in.

When that happens, the runtime allocates a new, larger stack (typically double the size), copies the old stack contents over, adjusts all the pointers that reference stack addresses, and frees the old stack. The goroutine then continues running on its new, bigger stack as if nothing happened. This is what allows Go to run millions of goroutines â they start small and only grow when they actually need the space.

This stack check is worth mentioning here because, as we’ll see in the next section, the scheduler piggybacks on it for cooperative preemption.

### Preemption

The goroutine might also be stopped involuntarily. Everything we’ve seen so far â blocking on channels, making system calls, finishing â involves the goroutine cooperating. But what if a goroutine never yields? A tight computational loop without any function calls, channel operations, or memory allocations would never give the scheduler a chance to run anything else on that P.

Go has two answers. The first is **cooperative preemption**: the compiler inserts a small check at the beginning of most functions that tests whether the goroutine has been asked to yield. When the runtime wants to preempt a goroutine, it flips a flag, and the next function call triggers the check and hands control back to the scheduler. This is cheap â it reuses the stack growth check that’s already there â but it only works at function calls.

The second is **asynchronous preemption**: for goroutines stuck in tight loops with no function calls, the runtime sends an OS signal (`SIGURG` on Unix) directly to the thread. The signal handler interrupts the goroutine, saves its context, and yields to the scheduler. This is the heavy hammer â it works even when cooperative preemption can’t.

In both cases, the preempted goroutine transitions directly to **\_Grunnable** and goes back on a run queue â it’ll get another chance to run soon. There’s also a special **\_Gpreempted** state, but that’s reserved for when the GC or debugger needs to fully suspend a goroutine via `suspendG`. In either case, it’s **sysmon** that detects goroutines running too long (more than **10ms**) and triggers the preemption. We’ll explore the details in the system monitor article.

### Death and Recycling

Finally, the goroutine’s function returns. Remember that the PC was set up to point at `goexit` during creation? So the return falls through to `goexit0()`, and the goroutine handles its own death. It changes its own status to **\_Gdead**, cleans up its fields, drops the M association, and puts itself on the P’s free list. Then it calls `schedule()` to find the next goroutine for this M.

The G isn’t freed or garbage collected. It sits on the free list, stack and all, waiting to be recycled. This is a key optimization â allocating and setting up a new G is much more expensive than reinitializing a dead one. And this is where the story comes full circle: a new `go` statement might pull this same G off the free list, reinitialize it, and send it through the whole journey again.

### The Self-Service Pattern

There’s a pattern running through all of these stages: the goroutine is always the one doing the work of its own state transitions. There’s no central scheduler thread pulling the strings â the goroutine parks itself, adds itself to wait queues, cleans itself up, and invokes the scheduler to pick the next G. The scheduler is really just a set of functions that goroutines call *on themselves*, using the M’s g0 stack to do the bookkeeping.

Most goroutines spend their lives bouncing between **\_Grunnable**, **\_Grunning**, and **\_Gwaiting** â ready, running, waiting, ready, running, waiting â until they finally finish and return to **\_Gdead**.

With the data structures and states in place, let’s look at the core algorithm â the loop that drives everything.

The Scheduling Loop
-------------------

Now for the heart of the scheduler: the `schedule()` function (in [`src/runtime/proc.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/proc.go#L4135)
). This is a loop that runs on every M, on the g0 stack, and its job is simple: find a runnable goroutine and execute it. When the goroutine stops running (it blocks, finishes, or gets preempted), control returns to `schedule()`, and the loop starts again.

Here’s the rough shape:

![Go Scheduler Loop](https://internals-for-interns.com/images/posts/go-scheduler-loop.webp)

The goroutine runs until it yields control back to the schedulerâeither voluntarily (by blocking on a channel, calling `runtime.Gosched()`, etc.) or involuntarily (via preemption). Then we’re back at `schedule()`, looking for the next goroutine.

The `schedule()` function itself is straightforward. It checks a few special cases (is this M locked to a specific goroutine?), and then calls `findRunnable()` to get the next goroutine. Once it has one, it calls `execute()` to run it.

The interesting part is `findRunnable()`âthat’s where all the decisions happen. Let’s break down exactly how it searches for work.

Finding Work: The Search Order
------------------------------

`findRunnable()` (in [`src/runtime/proc.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/proc.go#L3389)
) is the function that answers “what should I run next?” It searches multiple sources in a specific order, and it keeps looking until it finds something â if there’s truly nothing to do, it parks the M to sleep until work appears, and then resumes the search.

Here’s the search order:

### 1. GC and Trace Work

Before looking for user goroutines, the scheduler checks if there’s runtime work to do. If the GC is active and needs a mark worker, that takes priority. If execution tracing is enabled and its reader goroutine is ready, that also takes priority. The runtime’s own needs come first.

### 2. The Global Queue Fairness Check

Every **61st** schedule call, the scheduler grabs a **single goroutine** from the global run queue before looking at the local queue. Why 61? It’s a prime number, which helps avoid synchronization patterns where the check always lines up with the same goroutine. The point is to prevent starvation: if goroutines are constantly being added to local queues, the ones sitting in the global queue could wait forever without this check.

### 3. The Local Run Queue

This is the fast path, and where most goroutines come from. The scheduler first checks the **runnext** slotâa priority position that holds the single goroutine most likely to run next. If runnext is set, the goroutine gets it and **inherits the current time slice**, meaning it doesn’t reset the scheduling tick. This is an optimization for producer-consumer patterns: if G1 sends on a channel and wakes G2, G2 goes into runnext and runs immediately, almost like a direct handoff.

If runnext is empty, the scheduler takes from the ring bufferâa lock-free circular queue of up to 256 goroutines. Only the owning M writes to this queue (single producer), so no locks are needed for the common case.

### 4. The Global Run Queue (Again)

If the local queue is empty, check the global queue. This time, instead of grabbing just one goroutine, the scheduler grabs a **batch**. This amortizes the cost of acquiring the global lock (`sched.lock`). One lock acquisition, many goroutines.

### 5. Network Polling

Before resorting to stealing, the scheduler checks the **netpoller** to see if any network I/O is ready. If any goroutines were blocked waiting for network operations and those operations are now complete, those goroutines become runnable. We’ll talk about how the netpoller works in a future article.

### 6. Work Stealing

If all the above came up empty, it’s time to steal. The scheduler looks at **other Ps’ local queues** and takes half of their goroutines. This is the mechanism that keeps all cores busy even when work is unevenly distributed.

### 7. Last Resort: Park

If there’s truly nothing to do anywhereâno local work, no global work, no network I/O, nothing to stealâthe M releases its P, puts it on the idle P list, and parks itself to sleep. It will be woken up later when new work appears.

But that “parking” decision isn’t as straightforward as it sounds. Should a thread go to sleep the moment it runs out of work, or should it hang around for a bit in case something shows up?

Spinning Threads
----------------

There’s a subtle balance to strike here. When a thread runs out of work â its local queue is empty, there’s nothing to steal â should it go to sleep immediately? If it does, and new work arrives a microsecond later, there’s nobody awake to pick it up. Another thread has to be woken from sleep, which costs time. On the other hand, if too many idle threads stay awake burning CPU cycles looking for work that isn’t there, that’s pure waste.

Go’s answer is **spinning threads**. When an M runs out of work, it doesn’t park right away. Instead, it enters a spinning state â actively checking queues and trying to steal â for a brief period before giving up and going to sleep. The runtime limits the number of spinners to at most **half the number of busy Ps** â so on an 8-core machine with 6 busy Ps, up to 3 threads can spin at once. Enough to be responsive, not so many that they waste CPU.

The other side of the coin is when new work appears â say a new goroutine is created or a channel unblocks. The runtime is even more conservative here: it only wakes up a sleeping thread if there are **zero** spinners. If there’s already a spinning thread out there, it’ll pick up the new work. The goal is simple: always have someone ready to grab new work, but not too many someones.

All of these mechanisms â blocking, unblocking, system calls, preemption â involve switching from one goroutine to another. Let’s look at what that switch actually costs.

Context Switching
-----------------

Let’s talk briefly about what happens during a goroutine context switch, because it’s what makes the whole system fast.

When the scheduler switches from one goroutine to another, it needs to save where the current goroutine was and restore where the next one left off. The good news is that a goroutine’s state is surprisingly small. The `mcall()` assembly function only saves **3 values** â the stack pointer, the program counter, and the base pointer â into a tiny `gobuf` struct. That’s it. Why so few? Because goroutine switches happen at function call boundaries, and at those points the compiler has already spilled any important registers to the stack following normal calling conventions. The switch only needs to save enough to find the stack again.

**`gogo()`** does the opposite: it restores those saved values and jumps right into the goroutine. Together, `mcall()` and `gogo()` are the mechanism behind every voluntary goroutine switch. For async preemption (where the goroutine is interrupted mid-execution by a signal), the full register set has to be saved â but that’s the exception, not the common path.

And it’s fast. A goroutine context switch takes roughly **50â100 nanoseconds** â about 200 CPU cycles. Compare that to an OS thread context switch, which involves saving the full register set and switching kernel stacks â that costs **1â2 microseconds**, 10 to 40 times slower. This is a big part of why goroutines scale so much better than threads.

Let’s wrap up what we’ve learned.

Summary
-------

The Go scheduler multiplexes goroutines onto OS threads using the **GMP model**: **Gs** (goroutines) are the work, **Ms** (OS threads) provide the execution, and **Ps** (processors) carry the scheduling context â local run queues, memory caches, and everything needed to run goroutines efficiently. The global **schedt** struct ties it all together with shared state like the global run queue, idle lists, and the spinning thread count.

We followed a goroutine through its whole life â from creation (recycling dead Gs when possible), through running, blocking (where the goroutine parks itself), system calls (where the P detaches so other goroutines keep running), stack growth, and preemption (both cooperative and asynchronous). At the end, the goroutine cleans up after itself and goes back on the free list for reuse.

The scheduling loop in `schedule()` and `findRunnable()` drives it all â checking the local queue, the global queue for fairness every 61 ticks, the netpoller, and stealing from other Ps before giving up. **Spinning threads** keep the system responsive by staying awake briefly to catch new work, and **context switching** between goroutines costs only about 50â100 nanoseconds thanks to the small amount of state involved.

If you want to explore the implementation yourself, the main scheduler code lives in [`src/runtime/proc.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/proc.go)
, with data structures in [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/go1.26.0/src/runtime/runtime2.go)
and assembly routines in `src/runtime/asm_*.s`.

In the [next article](https://internals-for-interns.com/posts/go-garbage-collector/)
, we’ll look at the **garbage collector** â how it tracks which objects are still alive and reclaims the rest, all while your program keeps running.