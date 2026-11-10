---
title: "Watching Go's new garbage collector move through the heap - The Consensus"
url: https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html
clipped: 2026-08-31 12:26:36
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [Watching Go's new garbage collector move through the heap - The Consensus](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html)

## Full Article

[go](https://theconsensus.dev/t/go.html)

# Watching Go's new garbage collector move through the heap

Go 1.26 made Green Tea the default GC. We observe its cache-friendliness with perf, visualize the heap to see how Go allocates, and poke at a sparse-page problem a non-moving collector like Go's struggles with.By Phil EatonJuly 19, 2026Artwork by [Andrea Chersia](https://www.instagram.com/xinamito?utm_source=theconsensus.dev&utm_medium=referral) [Focus](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html?focus=1) 

You are getting early access to this article as a subscriber. Your support makes articles like this possible. Thank you.

Go 1.25, released last year, introduced a new garbage collector: [Green Tea](https://go.dev/blog/greenteagc?utm_source=theconsensus.dev&utm_medium=referral). And in Go 1.26, released a few months ago, Green Tea became the default. That linked article is excellent. We’ll recap it and take a look at a few programs that benefit the most. And we’ll look at some programs that don’t benefit, that trigger Go’s residual garbage collector bugaboo: its non-moving collector cannot reclaim sparse pages.

Taking a step back, Go manages memory by allocating objects of the same size class (an object’s size is rounded up to the nearest size class) within a contiguous chunk (or span in Go terminology) of one or more 8KiB pages. Size-segregated allocation is common in some malloc implementations (like tcmalloc, which Go’s allocator [descends from](https://go.dev/doc/gc-guide?utm_source=theconsensus.dev&utm_medium=referral)).

Let’s observe this happening in Go, and then compare it with C#. We’ll randomly allocate objects of three different sizes (small, medium and large). Then we’ll check their heap addresses, walk the address space and print out when we hit one of our objects, one character printed out for each 32-bytes we walk.

First install Go and C#. ` `sudo apt update -y
sudo apt-get install -y dotnet-sdk-10.0
curl -fsSL https://go.dev/dl/go1.26.0.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
export PATH=$PATH:/usr/local/go/bin
` ` 

Here’s the pseudocode we’re going for. ` `struct Small  { a [32]byte }
struct Medium { a [64]byte }
struct Large  { a [128]byte }

constructors = [Small, Medium, Large]
live = [] # stop objects from being collected
for i in range(100):
  live.push(new constructors[rand() % len(constructors)])

for pass in [0, 1]:
  if pass == 1:
    runtime.gc() # trigger the GC

  records = []
  for obj in live:
    records.push((runtime.addressof(obj), runtime.typeof(obj), runtime.sizeof(obj)))
  records.sort(key = r -> r.address)

  cell = 32
  cursor = records[0].address
  for (addr, typ, size) in records:
    while cursor < addr: # no object of ours here
      print("."); cursor += cell
    head = typ.name[0]
    print(upper(head) + "-" * (size/cell - 1)) # "S" / "M-" / "L---"
    cursor += size
` ` 

Let’s build it in Go. ` `package main

import (
	"bytes"
	"cmp"
	"fmt"
	"math/rand"
	"reflect"
	"runtime"
	"slices"
)

type (
	Small  struct{ _ [32]byte }  // 32 bytes
	Medium struct{ _ [64]byte }  // 64 bytes
	Large  struct{ _ [128]byte } // 128 bytes
)

type object struct {
	addr uintptr
	size int
	name byte // 'S' / 'M' / 'L'
}

func main() {
	allocs := []func() any{
		func() any { return new(Small) },
		func() any { return new(Medium) },
		func() any { return new(Large) },
	}
	live := make([]any, 100) // keep refs so GC can't reclaim, and so we know each type
	for i := range live {
		live[i] = allocs[rand.Intn(len(allocs))]()
	}

	for pass := 0; pass < 2; pass++ {
		if pass == 1 {
			runtime.GC() // Go never moves objects: pass 1 is identical to pass 0
		}
		objs := make([]object, len(live))
		for i, o := range live {
			t := reflect.TypeOf(o).Elem()
			objs[i] = object{reflect.ValueOf(o).Pointer(), int(t.Size()), t.Name()[0]}
		}
		slices.SortFunc(objs, func(a, b object) int { return cmp.Compare(a.addr, b.addr) })

		fmt.Printf("\n=== pass %d (base 0x%x) ===\n", pass, objs[0].addr)
		draw(objs)
	}
}

func draw(objs []object) {
	const cell, width = 32, 60

	last := objs[len(objs)-1]
	base := objs[0].addr
	grid := make([]byte, int((last.addr+uintptr(last.size)-base)/cell))
	for i := range grid {
		grid[i] = '.'
	}
	for _, o := range objs {
		c0 := int((o.addr - base) / cell)
		grid[c0] = o.name
		for k := 1; k < o.size/cell; k++ {
			grid[c0+k] = '-'
		}
	}

	prev := -1
	for off := 0; off < len(grid); off += width {
		row := grid[off:min(off+width, len(grid))]
		if len(bytes.Trim(row, ".")) == 0 { // row holds none of our objects
			continue
		}
		if prev >= 0 && off != prev+width {
			fmt.Println("             ...")
		}
		fmt.Printf("0x%09x  %s\n", base+uintptr(off)*cell, row)
		prev = off
	}
}
` ` 

heapwalk.go

Run it and you’ll see something like this. ` `$ go run heapwalk.go

=== pass 0 (base 0xba4841580c0) ===
0xba4841580c0  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xba484158840  M-M-M-M-....................................................
             ...
0xba48415bcc0  ............................SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
             ...
0xba4841add40  ..........................L---L---L---L---L---L---L---L---L-
0xba4841ae4c0  --L---L---L---L---L---L---L---L---L---L---L---L---L---L---L-
0xba4841aec40  --L---L---L---L---L---L---L---L---L---L---

=== pass 1 (base 0xba4841580c0) ===
0xba4841580c0  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xba484158840  M-M-M-M-....................................................
             ...
0xba48415bcc0  ............................SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
             ...
0xba4841add40  ..........................L---L---L---L---L---L---L---L---L-
0xba4841ae4c0  --L---L---L---L---L---L---L---L---L---L---L---L---L---L---L-
0xba4841aec40  --L---L---L---L---L---L---L---L---L---L---
` ` 

So even though we allocated randomly among objects of different sizes, we can observe the Go runtime fitting objects of each size next to each other.

And even after we ran the garbage collector it didn’t move anything around.

Now let’s take a look at C#. ` `using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

var allocs = new Func<object>[] { () => new Small(), () => new Medium(), () => new Large() };
var live = new object[100]; // keep refs so GC can't reclaim, and so we know each type
var rnd = new Random();
for (int i = 0; i < live.Length; i++) live[i] = allocs[rnd.Next(allocs.Length)]();

// A reference on 64-bit .NET is a plain 8-byte pointer, so reinterpreting one
// with Unsafe.As gives the object's address. Object sizes are measured from
// the heap: allocate several, the smallest gap between consecutive addresses
// is the (aligned) object size, header included.
var size = new Dictionary<Type, int>();
foreach (var make in allocs)
{
    var keep = new object[16];
    var a = new nint[keep.Length];
    for (int i = 0; i < keep.Length; i++) keep[i] = make();
    for (int i = 0; i < keep.Length; i++) a[i] = Unsafe.As<object, nint>(ref keep[i]);
    Array.Sort(a);
    nint best = nint.MaxValue;
    for (int i = 1; i < a.Length; i++)
        if (a[i] - a[i - 1] > 0 && a[i] - a[i - 1] < best) best = a[i] - a[i - 1];
    size[keep[0].GetType()] = (int)best;
}

for (int pass = 0; pass < 2; pass++)
{
    if (pass == 1) GC.Collect();

    // An address is only valid until the next collection, so pause the GC
    // while we take them.
    var addrs = new nint[live.Length];
    GC.TryStartNoGCRegion(1 << 20);
    for (int i = 0; i < live.Length; i++) addrs[i] = Unsafe.As<object, nint>(ref live[i]);
    GC.EndNoGCRegion();

    var objs = new (nint Addr, int Size, char Name)[live.Length];
    for (int i = 0; i < live.Length; i++)
        objs[i] = (addrs[i], size[live[i].GetType()], live[i].GetType().Name[0]);
    Array.Sort(objs, (x, y) => x.Addr.CompareTo(y.Addr));

    Console.WriteLine($"\n=== pass {pass} (base 0x{(long)objs[0].Addr:x}) ===");
    Draw(objs);
}

static void Draw((nint Addr, int Size, char Name)[] objs)
{
    const int cell = 32, width = 60; // cell = the smallest object's size

    var last = objs[^1];
    nint b = objs[0].Addr;
    var grid = new char[(last.Addr + last.Size - b) / cell];
    Array.Fill(grid, '.');
    foreach (var o in objs)
    {
        int c0 = (int)((o.Addr - b) / cell);
        grid[c0] = o.Name;
        for (int k = 1; k < o.Size / cell; k++) grid[c0 + k] = '-';
    }

    int prev = -1;
    for (int off = 0; off < grid.Length; off += width)
    {
        var row = new string(grid, off, Math.Min(width, grid.Length - off));
        if (row.Trim('.').Length == 0) continue; // row holds none of our objects
        if (prev >= 0 && off != prev + width) Console.WriteLine("             ...");
        Console.WriteLine($"0x{(long)b + (long)off * cell:x9}  {row}");
        prev = off;
    }
}

class Small  { public long a, b; }
class Medium { public long a, b, c, d, e, f; }
class Large  { public long a, b, c, d, e, f, g, h, i, j, k, l, m, n; }
` ` 

HeapWalk.cs

Build and run it. ` `$ dotnet run HeapWalk.cs
=== pass 0 (base 0x7aea1080a1e0) ===
0x7aea1080a1e0  L---L---L---M-M-SL---L---SM-M-M-M-SL---L---L---L---M-L---SSL
0x7aea1080a960  ---L---M-M-L---M-SL---L---SM-L---M-L---L---L---M-L---L---M-L
0x7aea1080b0e0  ---SL---SSL---L---M-L---L---M-L---L---L---SM-SL---L---SL---L
0x7aea1080b860  ---L---SSSL---L---M-SL---SM-L---SL---M-L---M-L---M-L---SSL--
0x7aea1080bfe0  -L---SSSM-SM-L---M-M-L---M-L---

=== pass 1 (base 0x7aea1080a1e0) ===
0x7aea1080a1e0  L---L---L---M-M-SL---L---SM-M-M-M-SL---L---L---L---M-L---SSL
0x7aea1080a960  ---L---M-M-L---M-SL---L---SM-L---M-L---L---L---M-L---L---M-L
0x7aea1080b0e0  ---SL---SSL---L---M-L---L---M-L---L---L---SM-SL---L---SL---L
0x7aea1080b860  ---L---SSSL---L---M-SL---SM-L---SL---M-L---M-L---M-L---SSL--
0x7aea1080bfe0  -L---SSSM-SM-L---M-M-L---M-L---
` ` 

And we immediately notice that objects of the same size are not grouped together. (Later on, in a different workload, we'll also notice C# moving objects around in memory.)

The documentation for Go and C# will tell you as much about the behavior of both, but I think it’s nice to also see it demonstrated like this.

Now that we’ve seen how Go memory is allocated, let’s look at how it’s cleaned up.

# Mark and sweep[#](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html#mark-and-sweep)

The garbage collector starts at specific roots (e.g. globals and locals) and, historically in Go, follows each pointer until the GC visits all accessible objects. The mark phase. Then, in a second pass, the GC frees any allocated objects that have not been visited. Since these now-freed objects were not accessible from the root tree in the mark phase, they are by definition dead. The sweep phase.

A challenge arises when you have objects A that point to objects B/C/D of different sizes. Objects of different sizes are allocated in different sections of memory in Go. Or even if you have objects A that point to other objects A that were created at very different times; they’re going to exist in very different parts of memory. In both cases, the GC following pointers now introduces random memory access which is measurably less cache friendly.

In Green Tea, Go now scans a memory span for objects and pointers and queues up future spans for scanning based on pointers it has found, rather than following every pointer roughly as it sees one. And while we can’t show this random access behavior happening without applying patches to Go itself (so that we could observe the mark path as it visits each object), we can observe it happening with  `perf`  showing both fewer cache misses (per kilo instruction) and faster overall program runs.

Here’s the pseudocode for our workload. ` `struct Node {a,b,c,d *Node}

mode = packed | scattered

nodes = new [2_000_000]*Node
for i in 0..nodes.len:
  nodes[i] = Node{
    a: nodes[(mode == packed ? i + 1 : rand()) % nodes.len],
    b: nodes[(mode == packed ? i + 2 : rand()) % nodes.len],
    c: nodes[(mode == packed ? i + 3 : rand()) % nodes.len],
    d: nodes[(mode == packed ? i + 4 : rand()) % nodes.len]
  }

for i in 0..100:
  trigger_gc()

keepalive(nodes) # prevent `nodes` from being garbage collected
` ` 

In order to make the program measurement a little fairer (the scattered version has to do significant work generating random numbers) we’ll separate out the generation of node index offsets: ` `import array
import random
import sys

n = 2_000_000
order = sys.argv[1] if len(sys.argv) > 1 else ""

if order == "packed":
    a = array.array("I", ((i + k) % n for i in range(n) for k in (1, 2, 3, 4)))
elif order == "scattered":
    r = random.Random(1)
    a = array.array("I", (r.randrange(n) for _ in range(n * 4)))
else:
    sys.exit("usage: gen.py packed|scattered")

assert a.itemsize == 4 and sys.byteorder == "little"  # matches Go's uint32 cast
with open(order+".idx", "wb") as f:
  a.tofile(f)
` ` 

generate_indexes.py

And the Go workload becomes: ` `package main

import (
        "io"
        "os"
        "runtime"
        "unsafe"
)

type Node struct {
        a, b, c, d *Node
}

func main() {
        n := 2_000_000

        raw, err := io.ReadAll(os.Stdin)
        if err != nil {
                panic(err)
        }
        idx := unsafe.Slice((*uint32)(unsafe.Pointer(&raw[0])), n*4)

        nodes := make([]*Node, n)
        for i := range nodes {
                nodes[i] = &Node{}
        }
        for i, nd := range nodes {
                nd.a = nodes[idx[i*4]]
                nd.b = nodes[idx[i*4+1]]
                nd.c = nodes[idx[i*4+2]]
                nd.d = nodes[idx[i*4+3]]
        }

        for i := 0; i < 100; i++ {
                runtime.GC()
        }

        runtime.KeepAlive(nodes) // keep `nodes` from seeming to fall out of scope
}
` ` 

readorder.go

Now generate the index files from the Python script. Then build two versions of the Go workload: one with Green Tea and one without. ` `python3 generate_indexes.py scattered
python3 generate_indexes.py packed
go build -o readorder_greentea readorder.go
GOEXPERIMENT=nogreenteagc go build -o readorder_oldgc readorder.go
` ` 

Let’s time the two garbage collectors and the two workloads with  `perf`  while collecting information on cache misses. ` `$ for bin in readorder_oldgc readorder_greentea; do
  for input in packed.idx scattered.idx; do
    echo "=== $bin < $input ==="
    perf stat -e cache-references,cache-misses -r 5 \
      sh -c "exec ./$bin < $input" > /dev/null
  done
done

=== readorder_oldgc < packed.idx ===

 Performance counter stats for 'sh -c exec ./readorder_oldgc < packed.idx' (5 runs):

     1,130,709,755      cache-references                                                        ( +-  0.70% )
       290,434,782      cache-misses                     #   25.69% of all cache refs           ( +-  1.02% )

             4.230 +- 0.145 seconds time elapsed  ( +-  3.44% )

=== readorder_oldgc < scattered.idx ===

 Performance counter stats for 'sh -c exec ./readorder_oldgc < scattered.idx' (5 runs):

    13,247,268,612      cache-references                                                        ( +-  0.38% )
     2,325,799,796      cache-misses                     #   17.56% of all cache refs           ( +-  0.15% )

            11.052 +- 0.154 seconds time elapsed  ( +-  1.39% )

=== readorder_greentea < packed.idx ===

 Performance counter stats for 'sh -c exec ./readorder_greentea < packed.idx' (5 runs):

       481,414,281      cache-references                                                        ( +-  0.27% )
       257,894,055      cache-misses                     #   53.57% of all cache refs           ( +-  0.04% )

           2.69560 +- 0.00385 seconds time elapsed  ( +-  0.14% )

=== readorder_greentea < scattered.idx ===

 Performance counter stats for 'sh -c exec ./readorder_greentea < scattered.idx' (5 runs):

     3,398,491,016      cache-references                                                        ( +-  1.02% )
     2,195,902,796      cache-misses                     #   64.61% of all cache refs           ( +-  0.10% )

            6.9610 +- 0.0108 seconds time elapsed  ( +-  0.16% )
` ` 

We see very clear improvement for each workload with the new GC. But cache misses seem to have increased with the new GC? That’s not what we expected.

There are two things at play here. First,  `cache-references`  and  `cache-misses`  in perf usually correspond to L3 cache. So while the percentage of L3 cache misses in the new GC might have gone up, it doesn’t really tell us anything about behavior at the L1 or L2 cache level. And again, we saw the speedup ourselves. So we’re missing something.

Second, the program runtime largely changed between the old GC and the new GC and we haven’t normalized that.  `perf`  has an  `instructions`  metric we can key on to calculate a standard normalized metric: Misses Per Kilo Instructions (MPKI).

So let’s run  `perf`  again and ask for  `instructions`  too and calculate MPKI ourselves. ` `import json, subprocess

for binary in ["readorder_oldgc", "readorder_greentea"]:
    for inp in ["packed.idx", "scattered.idx"]:
        out = subprocess.run(
            ["perf", "stat", "-j", "-e", "instructions,cache-misses", "-r", "5",
             "sh", "-c", f"exec ./{binary} < {inp}"],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True).stderr

        c = {}
        for line in out.splitlines():
            line = line.strip().lstrip("[").rstrip("],")
            if line.startswith("{"):
                r = json.loads(line)
                c[r["event"].split(":")[0]] = float(r["counter-value"])

        print(f"{binary:<20} {inp:<14} {1000 * c['cache-misses'] / c['instructions']:6.2f} MPKI")
` ` 

perf.py

Run it. ` `$ python3 perf.py
readorder_oldgc      packed.idx       1.59 MPKI
readorder_oldgc      scattered.idx   12.70 MPKI
readorder_greentea   packed.idx       1.81 MPKI
readorder_greentea   scattered.idx   15.39 MPKI
` ` 

And we’re still not seeing what we expect! L3 MPKI actually went up with the new GC. But we saw the performance improvements ourselves!

At this point if you want to keep hunting for the cache improvements to show up you’re going to need to switch to a bare metal x86/amd64 Linux machine because most virtual machines do not expose [PMU counters](https://easyperf.net/blog/2018/06/01/PMU-counters-and-profiling-basics?utm_source=theconsensus.dev&utm_medium=referral) needed for L1 events.

I grabbed myself a Vultr bare metal machine and kept going. We will ask  `perf`  for  `L1-dcache-loads`  and  `L1-dcache-load-misses`  to get L1 metrics. Then we’ll calculate MPKI for both the L1 cache and the L3 cache. ` `import json, statistics, subprocess

print(f"{'binary':<21}{'ordering':<12}{'elapsed(s)':>10}{'L1miss%':>9}"
      f"{'L1-MPKI':>9}{'L3miss%':>9}{'L3-MPKI':>10}")
print("-" * 80)

for binary in ["readorder_oldgc", "readorder_greentea"]:
    for order in ["packed", "scattered"]:
        runs = []
        for _ in range(5):
            out = subprocess.run(
                ["perf", "stat", "-j", "-e",
                 "instructions,duration_time,L1-dcache-loads,L1-dcache-load-misses,"
                 "cache-references,cache-misses",
                 "sh", "-c", f"exec ./{binary} < {order}.idx"],
                stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True).stderr
            c = {}
            for line in out.splitlines():
                line = line.strip().lstrip("[").rstrip("],")
                if line.startswith("{"):
                    r = json.loads(line)
                    c[r["event"].split(":")[0]] = float(r["counter-value"])
            runs.append(c)

        secs = [r["duration_time"] / 1e9 for r in runs]
        ins = statistics.fmean(r["instructions"] for r in runs)
        l1 = statistics.fmean(r["L1-dcache-load-misses"] for r in runs)
        l1l = statistics.fmean(r["L1-dcache-loads"] for r in runs)
        l3 = statistics.fmean(r["cache-misses"] for r in runs)
        l3r = statistics.fmean(r["cache-references"] for r in runs)
        el = f"{statistics.fmean(secs):.2f}±{statistics.stdev(secs):.2f}"
        print(f"{binary:<21}{order:<12}{el:>10}"
              f"{100 * l1 / l1l:>9.1f}{1000 * l1 / ins:>9.2f}"
              f"{100 * l3 / l3r:>9.1f}{1000 * l3 / ins:>10.2f}")
` ` 

perf2.py

Give it a run. ` `$ python3 perf2.py
binary               ordering    elapsed(s)  L1miss%  L1-MPKI  L3miss%   L3-MPKI
--------------------------------------------------------------------------------
readorder_oldgc      packed       4.47±0.32      0.9     2.23     26.2      1.61
readorder_oldgc      scattered   11.44±0.85     12.9    31.57     17.5     12.76
readorder_greentea   packed       2.70±0.01      1.0     1.98     53.8      1.81
readorder_greentea   scattered    7.01±0.04      7.3    14.06     63.2     15.37
` ` 

And now we finally start to see what we’re expecting: while L1 cache miss percentages stay the same or decrease, L1 MPKI more markedly decreases. More of the reads fit into L1 (and possibly L2) cache and didn't even need to get to the L3 cache. The L3 cache misses stop mattering as much. So here, concretely, is at least one of the areas that the Green Tea GC improved on.

Now let’s take a look at one of the areas where the Go garbage collector still struggles.

# Worst-case cleanup[#](https://theconsensus.dev/p/2026/07/19/observing-gos-garbage-collector-old-and-new.html#worst-case-cleanup)

Because Go will never move memory around to compact or defragment it, we can easily get into a seemingly-ridiculous scenario where we free up a huge percentage of our objects but Go cannot entirely reclaim unused memory.

Let’s go back to our initial program drawing out memory allocation for S/M/L objects. This time, after we allocate our objects, we’ll free 90% of them. We’d hope for memory usage to shrink 90%, but we’ll see it actually does not happen because Go does not compact or move objects around. ` `package main

import (
	"bytes"
	"cmp"
	"fmt"
	"math/rand"
	"reflect"
	"runtime"
	"runtime/debug"
	"slices"
)

type (
	Small  struct{ _ [32]byte }  // 32 bytes
	Medium struct{ _ [64]byte }  // 64 bytes
	Large  struct{ _ [128]byte } // 128 bytes
)

type object struct {
	addr uintptr
	size int
	name byte // 'S' / 'M' / 'L'
}

func main() {
	allocs := []func() any{
		func() any { return new(Small) },
		func() any { return new(Medium) },
		func() any { return new(Large) },
	}
	live := make([]any, 50000) // keep refs so GC can't reclaim, and so we know each type
	for i := range live {
		live[i] = allocs[rand.Intn(len(allocs))]()
	}

	for pass := 0; pass < 2; pass++ {
		if pass == 1 {
			for i := range live {
				if i%10 != 0 { // free 90% of the objects
					live[i] = nil
				}
			}
			runtime.GC()         // but the survivors can't be moved,
			debug.FreeOSMemory() // so nothing closes up and nothing goes back
		} else {
			runtime.GC()
		}
		objs := make([]object, 0, len(live))
		for _, o := range live {
			if o == nil {
				continue
			}
			t := reflect.TypeOf(o).Elem()
			objs = append(objs, object{reflect.ValueOf(o).Pointer(), int(t.Size()), t.Name()[0]})
		}
		slices.SortFunc(objs, func(a, b object) int { return cmp.Compare(a.addr, b.addr) })

		fmt.Printf("\n=== pass %d (%d live, base 0x%x) ===\n", pass, len(objs), objs[0].addr)
		draw(window(objs, 16*1024)) // first 16 KiB of the heap, same region both passes
		stats(objs)
	}
	runtime.KeepAlive(live)
}

// window returns the objects sitting in the first n bytes of the heap.
func window(objs []object, n uintptr) []object {
	end := objs[0].addr + n
	for i, o := range objs {
		if o.addr >= end {
			return objs[:i]
		}
	}
	return objs
}

func stats(objs []object) {
	const span = 8192 // Go's span/page granularity

	liveBytes := 0
	spans := map[uintptr]bool{}
	for _, o := range objs {
		liveBytes += o.size
		spans[o.addr&^(span-1)] = true
	}

	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	kib := func(x uint64) float64 { return float64(x) / 1024 }

	fmt.Printf("  live data      %8.1f KiB\n", float64(liveBytes)/1024)
	fmt.Printf("  spans pinned   %8d      (%d if the survivors were packed)\n",
		len(spans), (liveBytes+span-1)/span)
	fmt.Printf("  runtime        HeapInuse %.1f KiB | HeapIdle %.1f KiB | HeapReleased %.1f KiB\n",
		kib(m.HeapInuse), kib(m.HeapIdle), kib(m.HeapReleased))
}

func draw(objs []object) {
	const cell, width = 32, 60

	last := objs[len(objs)-1]
	base := objs[0].addr
	grid := make([]byte, int((last.addr+uintptr(last.size)-base)/cell))
	for i := range grid {
		grid[i] = '.'
	}
	for _, o := range objs {
		c0 := int((o.addr - base) / cell)
		grid[c0] = o.name
		for k := 1; k < o.size/cell; k++ {
			grid[c0+k] = '-'
		}
	}

	prev := -1
	for off := 0; off < len(grid); off += width {
		row := grid[off:min(off+width, len(grid))]
		if len(bytes.Trim(row, ".")) == 0 { // row holds none of our objects
			continue
		}
		if prev >= 0 && off != prev+width {
			fmt.Println("             ...")
		}
		fmt.Printf("0x%09x  %s\n", base+uintptr(off)*cell, row)
		prev = off
	}
}
` ` 

heapwalk_free.go

Run it. ` `$ go run heapwalk_free.go

=== pass 0 (50000 live, base 0x10a2674ac000) ===
0x10a2674ac000  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674ac780  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674acf00  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674ad680  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674ade00  L---L---L---....L---L---L---L---L---L---L---L---L---L---L---
0x10a2674ae580  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674aed00  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674af480  L---L---L---L---L---L---L---L---L---L---L---L---L---L---L---
0x10a2674afc00  L---L---L---L---L---L---L---
  live data        3639.9 KiB
  spans pinned        464      (455 if the survivors were packed)
  runtime        HeapInuse 6320.0 KiB | HeapIdle 5520.0 KiB | HeapReleased 5488.0 KiB

=== pass 1 (5000 live, base 0x10a2674acc00) ===
0x10a2674acc00  L---........................L---............................
0x10a2674ad380  ................L---............................L---........
0x10a2674adb00  L---....................................................L---
0x10a2674ae280  ................L---........L---............L---............
0x10a2674aea00  ............L---............................................
0x10a2674af180  ........L---............L---....................L---........
0x10a2674af900  ............................L---
  live data         364.6 KiB
  spans pinned        463      (46 if the survivors were packed)
  runtime        HeapInuse 6320.0 KiB | HeapIdle 5552.0 KiB | HeapReleased 5512.0 KiB
` ` 

The interesting thing is that (in simple scenarios) we can “move” (well, copy) objects ourselves to avoid fragmentation and to recover memory. ` `package main

import (
	"bytes"
	"cmp"
	"fmt"
	"math/rand"
	"reflect"
	"runtime"
	"runtime/debug"
	"slices"
	"unsafe"
)

type (
	Small  struct{ _ [32]byte }  // 32 bytes
	Medium struct{ _ [64]byte }  // 64 bytes
	Large  struct{ _ [128]byte } // 128 bytes
)

type object struct {
	addr uintptr
	size int
	name byte // 'S' / 'M' / 'L'
}

func main() {
	allocs := []func() any{
		func() any { return new(Small) },
		func() any { return new(Medium) },
		func() any { return new(Large) },
	}
	live := make([]any, 50000) // keep refs so GC can't reclaim, and so we know each type
	for i := range live {
		live[i] = allocs[rand.Intn(len(allocs))]()
	}
	// pass 2 moves the survivors in here, by hand
	var packedS []Small
	var packedM []Medium
	var packedL []Large

	for pass := 0; pass < 3; pass++ {
		switch pass {
		case 1:
			for i := range live {
				if i%10 != 0 { // free 90% of the objects
					live[i] = nil
				}
			}
		case 2:
			for i, o := range live {
				switch v := o.(type) {
				case *Small:
					packedS = append(packedS, *v)
				case *Medium:
					packedM = append(packedM, *v)
				case *Large:
					packedL = append(packedL, *v)
				}
				live[i] = nil
			}
		}
		runtime.GC()
		debug.FreeOSMemory()

		objs := make([]object, 0, len(live))
		for i := range packedS {
			objs = append(objs, object{uintptr(unsafe.Pointer(&packedS[i])), 32, 'S'})
		}
		for i := range packedM {
			objs = append(objs, object{uintptr(unsafe.Pointer(&packedM[i])), 64, 'M'})
		}
		for i := range packedL {
			objs = append(objs, object{uintptr(unsafe.Pointer(&packedL[i])), 128, 'L'})
		}
		for _, o := range live {
			if o == nil {
				continue
			}
			t := reflect.TypeOf(o).Elem()
			objs = append(objs, object{reflect.ValueOf(o).Pointer(), int(t.Size()), t.Name()[0]})
		}
		slices.SortFunc(objs, func(a, b object) int { return cmp.Compare(a.addr, b.addr) })

		fmt.Printf("\n=== pass %d (%d live, base 0x%x) ===\n", pass, len(objs), objs[0].addr)
		draw(window(objs, 16*1024)) // first 16 KiB of the survivors' range
		stats(objs)
	}
	runtime.KeepAlive(live)
	runtime.KeepAlive(packedS)
	runtime.KeepAlive(packedM)
	runtime.KeepAlive(packedL)
}

// window returns the objects sitting in the first n bytes of the range.
func window(objs []object, n uintptr) []object {
	end := objs[0].addr + n
	for i, o := range objs {
		if o.addr >= end {
			return objs[:i]
		}
	}
	return objs
}

func stats(objs []object) {
	const span = 8192 // Go's span/page granularity

	liveBytes := 0
	spans := map[uintptr]bool{}
	for _, o := range objs {
		liveBytes += o.size
		spans[o.addr&^(span-1)] = true
	}

	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	kib := func(x uint64) float64 { return float64(x) / 1024 }

	fmt.Printf("  live data      %8.1f KiB\n", float64(liveBytes)/1024)
	fmt.Printf("  spans pinned   %8d      (%d if the survivors were packed)\n",
		len(spans), (liveBytes+span-1)/span)
	fmt.Printf("  runtime        HeapInuse %.1f KiB | HeapIdle %.1f KiB | HeapReleased %.1f KiB\n",
		kib(m.HeapInuse), kib(m.HeapIdle), kib(m.HeapReleased))
}

func draw(objs []object) {
	const cell, width = 32, 60

	last := objs[len(objs)-1]
	base := objs[0].addr
	grid := make([]byte, int((last.addr+uintptr(last.size)-base)/cell))
	for i := range grid {
		grid[i] = '.'
	}
	for _, o := range objs {
		c0 := int((o.addr - base) / cell)
		grid[c0] = o.name
		for k := 1; k < o.size/cell; k++ {
			grid[c0+k] = '-'
		}
	}

	prev := -1
	for off := 0; off < len(grid); off += width {
		row := grid[off:min(off+width, len(grid))]
		if len(bytes.Trim(row, ".")) == 0 { // row holds none of our objects
			continue
		}
		if prev >= 0 && off != prev+width {
			fmt.Println("             ...")
		}
		fmt.Printf("0x%09x  %s\n", base+uintptr(off)*cell, row)
		prev = off
	}
}
` ` 

heapwalk_free_manual.go

And run it. ` `$ go run heapwalk_free_manual.go

=== pass 0 (50000 live, base 0xa615561a0c0) ===
0xa615561a0c0  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa615561a840  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa615561afc0  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa615561b740  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa615561bec0  M-M-M-......................................................
             ...
0xa615561dcc0  ............................SSSS
  live data        3654.9 KiB
  spans pinned        465      (457 if the survivors were packed)
  runtime        HeapInuse 6224.0 KiB | HeapIdle 5680.0 KiB | HeapReleased 5632.0 KiB

=== pass 1 (5000 live, base 0xa615561a0c0) ===
0xa615561a0c0  M-..........................M-......M-......................
0xa615561a840  ..M-......M-..M-......M-..........M-........................
0xa615561afc0  ..............M-..................................M-........
0xa615561b740  ....M-
  live data         373.0 KiB
  spans pinned        465      (47 if the survivors were packed)
  runtime        HeapInuse 6232.0 KiB | HeapIdle 5672.0 KiB | HeapReleased 5672.0 KiB

=== pass 2 (5000 live, base 0xa6155710000) ===
0xa6155710000  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155710780  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155710f00  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155711680  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155711e00  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155712580  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155712d00  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155713480  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
0xa6155713c00  M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-
  live data         373.0 KiB
  spans pinned         48      (47 if the survivors were packed)
  runtime        HeapInuse 2768.0 KiB | HeapIdle 9104.0 KiB | HeapReleased 9040.0 KiB
` ` 

Which is kind of neat.

Let’s compare it though to if we take our C# sample and clean up 90% of the objects. ` `#nullable enable
using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

var allocs = new Func<object>[] { () => new Small(), () => new Medium(), () => new Large() };

// A reference on 64-bit .NET is a plain 8-byte pointer, so reinterpreting one
// with Unsafe.As gives the object's address. Object sizes are measured from
// the heap: allocate several, the smallest gap between consecutive addresses
// is the (aligned) object size, header included.
var size = new Dictionary<Type, int>();
foreach (var make in allocs)
{
    var keep = new object[16];
    var a = new nint[keep.Length];
    for (int i = 0; i < keep.Length; i++) keep[i] = make();
    for (int i = 0; i < keep.Length; i++) a[i] = Unsafe.As<object, nint>(ref keep[i]);
    Array.Sort(a);
    nint best = nint.MaxValue;
    for (int i = 1; i < a.Length; i++)
        if (a[i] - a[i - 1] > 0 && a[i] - a[i - 1] < best) best = a[i] - a[i - 1];
    size[keep[0].GetType()] = (int)best;
}

var live = new object?[50_000]; // the only refs to our objects: nulling one frees it
var rnd = new Random();
for (int i = 0; i < live.Length; i++) live[i] = allocs[rnd.Next(allocs.Length)]();

for (int pass = 0; pass < 2; pass++)
{
    if (pass == 1)
        for (int i = 0; i < live.Length; i++)
            if (i % 10 != 0) live[i] = null; // free 90% of the objects

    // Full compacting collection that also returns freed memory to the OS.
    GC.Collect(GC.MaxGeneration, GCCollectionMode.Aggressive);

    int n = 0;
    foreach (var o in live) if (o != null) n++;

    var addrs = new nint[n];
    GC.TryStartNoGCRegion(1 << 20); // addresses are only valid until the next GC
    for (int i = 0, j = 0; i < live.Length; i++)
        if (live[i] != null) addrs[j++] = Unsafe.As<object?, nint>(ref live[i]);
    GC.EndNoGCRegion();

    var objs = new (nint Addr, int Size, char Name)[n];
    for (int i = 0, j = 0; i < live.Length; i++)
        if (live[i] != null)
        {
            objs[j] = (addrs[j], size[live[i]!.GetType()], live[i]!.GetType().Name[0]);
            j++;
        }
    Array.Sort(objs, (x, y) => x.Addr.CompareTo(y.Addr));

    int w = 0; // the objects sitting in the first 16 KiB of the range
    while (w < objs.Length && objs[w].Addr < objs[0].Addr + 16 * 1024) w++;

    Console.WriteLine($"\n=== pass {pass} ({n} live, base 0x{(long)objs[0].Addr:x}) ===");
    Draw(objs[..w]);
    Stats(objs);
}
GC.KeepAlive(live); // keep `live` from seeming to fall out of scope

static void Draw((nint Addr, int Size, char Name)[] objs)
{
    const int cell = 32, width = 60; // cell = the smallest object's size

    var last = objs[^1];
    nint b = objs[0].Addr;
    var grid = new char[(last.Addr + last.Size - b) / cell];
    Array.Fill(grid, '.');
    foreach (var o in objs)
    {
        int c0 = (int)((o.Addr - b) / cell);
        grid[c0] = o.Name;
        for (int k = 1; k < o.Size / cell; k++) grid[c0 + k] = '-';
    }

    int prev = -1;
    for (int off = 0; off < grid.Length; off += width)
    {
        var row = new string(grid, off, Math.Min(width, grid.Length - off));
        if (row.Trim('.').Length == 0) continue; // row holds none of our objects
        if (prev >= 0 && off != prev + width) Console.WriteLine("             ...");
        Console.WriteLine($"0x{(long)b + (long)off * cell:x9}  {row}");
        prev = off;
    }
}

static void Stats((nint Addr, int Size, char Name)[] objs)
{
    const int chunk = 8192; // 8KiB = Go's span size, for an apples-to-apples density measure

    long liveBytes = 0;
    var chunks = new HashSet<nint>();
    foreach (var o in objs)
    {
        liveBytes += o.Size;
        chunks.Add(o.Addr & ~(nint)(chunk - 1));
    }

    Console.WriteLine($"  live data      {liveBytes / 1024.0,8:f1} KiB");
    Console.WriteLine($"  8KiB chunks    {chunks.Count,8}      ({(liveBytes + chunk - 1) / chunk} if the survivors were packed)");
}

class Small  { public long a, b; }                                     // 32 bytes: 16-byte header + 2 longs
class Medium { public long a, b, c, d, e, f; }                         // 64 bytes
class Large  { public long a, b, c, d, e, f, g, h, i, j, k, l, m, n; } // 128 bytes
` ` 

HeapWalkFree.cs

Compile and run it. ` `$ dotnet run HeapWalkFree.cs

=== pass 0 (50000 live, base 0x7e928000aad0) ===
0x7e928000aad0  M-M-L---M-M-SSL---M-L---M-M-L---M-L---M-M-SM-L---L---SM-M-M-
0x7e928000b250  SM-SL---L---L---L---SM-L---SM-SM-M-M-M-L---SSM-L---L---L---L
0x7e928000b9d0  ---M-SM-M-M-SSL---M-SSL---L---L---SM-M-M-M-SL---M-M-SL---M-L
0x7e928000c150  ---M-SL---M-L---L---L---L---M-L---SM-SM-L---M-L---L---L---L-
0x7e928000c8d0  --M-SL---M-M-SSSL---M-SL---SM-L---L---L---L---M-SM-M-M-M-M-L
0x7e928000d050  ---L---SL---L---M-SL---SSSL---M-L---M-SM-M-L---SL---L---SL--
0x7e928000d7d0  -.L---M-M-L---SSL---SL---L---M-SL---M-SM-L---M-M-SM-SM-M-SSS
0x7e928000df50  SL---M-M-M-M-SM-M-L---L---M-M-M-SL---L---M-SSM-L---L---M-M-S
0x7e928000e6d0  L---L---L---M-SM-SM-SM-M-L---L---
  live data        3646.1 KiB
  8KiB chunks         458      (456 if the survivors were packed)

=== pass 1 (5000 live, base 0x7e9282c0aa70) ===
0x7e9282c0aa70  M-M-L---L---M-M-SL---M-M-M-M-M-SL---SSSM-M-L---L---M-SL---SS
0x7e9282c0b1f0  M-L---M-L---M-L---L---L---SL---SSM-L---L---SSL---L---SM-SSL-
0x7e9282c0b970  --SSSM-L---SSSSSL---M-SL---SSM-L---M-M-L---SSM-SSL---M-M-L--
0x7e9282c0c0f0  -M-SSM-SM-M-SSM-M-M-M-L---L---L---SM-M-SSL---L---M-M-M-M-L--
0x7e9282c0c870  -SM-L---L---M-L---M-SL---SSM-L---L---SL---L---M-L---L---SM-S
0x7e9282c0cff0  M-L---L---M-SL---SL---SSM-M-SL---L---M-L---SSSSL---SM-M-SSM-
0x7e9282c0d770  M-L---L---L---M-M-L---L---SL---SM-SSM-SM-L---SL---M-M-SL---L
0x7e9282c0def0  ---L---SM-SM-SM-SM-M-L---L---L---L---SL---SM-SSM-SM-SM-L---L
0x7e9282c0e670  ---L---M-M-M-M-SM-SSL---SL---L---
  live data         369.2 KiB
  8KiB chunks          47      (47 if the survivors were packed)
` ` 

Which looks pretty good![go](https://theconsensus.dev/t/go.html)[c#](https://theconsensus.dev/t/csharp.html)

Noticed a mistake? Have a question or comment? Write to [the editor](https://theconsensus.dev/cdn-cgi/l/email-protection#f989919095b98d919c9a96978a9c978a8c8ad79d9c8f).

## Comments

More

## The Consensus Weekly

Want to learn about new articles on The Consensus, new funding announcements, and new job postings?

Join [The Consensus Weekly](https://theconsensus.dev/weekly.html) for free.

Want a peek? Check out the [archives](https://theconsensus.dev/weekly.html#archive).

## Job Openings

Taipei[Software Quality Assurance Engineer - Linux, PC, IoT](https://job-boards.greenhouse.io/canonical/jobs/7975990?utm_source=theconsensus.dev&utm_medium=referral)[qa](https://theconsensus.dev/t/qa.html)[developer](https://theconsensus.dev/t/developer.html)[Canonical](https://theconsensus.dev/company/canonical.html)Enterprise open source, secured and delivered by the publisher of Ubuntu.[Learn more ↗](https://job-boards.greenhouse.io/canonical/jobs/7975990?utm_source=theconsensus.dev&utm_medium=referral)Remote+1RemoteSan Francisco[Software Engineer - Sharded Postgres (Neki)](https://job-boards.greenhouse.io/planetscale/jobs/4009936009?utm_source=theconsensus.dev&utm_medium=referral)[developer](https://theconsensus.dev/t/developer.html)[infrastructure](https://theconsensus.dev/t/infrastructure.html)[PlanetScale](https://theconsensus.dev/company/planetscale.html)The fastest and most reliable database for Postgres & Vitess.[Learn more ↗](https://job-boards.greenhouse.io/planetscale/jobs/4009936009?utm_source=theconsensus.dev&utm_medium=referral)Palo Alto[Software Engineer (Platform Team)](https://boards.greenhouse.io/spacex/jobs/8558859002?utm_source=theconsensus.dev&utm_medium=referral)[developer](https://theconsensus.dev/t/developer.html)[infrastructure](https://theconsensus.dev/t/infrastructure.html)[SpaceX](https://theconsensus.dev/company/spacex.html)SpaceX designs, manufactures and launches the world’s most advanced rockets and spacecraft.[Learn more ↗](https://boards.greenhouse.io/spacex/jobs/8558859002?utm_source=theconsensus.dev&utm_medium=referral)[See all](https://theconsensus.dev/jobs.html)

## Funding and Acquisitions

🇺🇸 Cambridge HQ[Transfyr](https://theconsensus.dev/company/transfyr.html)Making science more observable, interpretable, and reproducible.Raised a $25M Seed round on August 27, 2026.[Read more ↗](https://www.transfyr.ai/news/building-transfyr?utm_source=theconsensus.dev&utm_medium=referral)🇺🇸 San Francisco HQ[Arga Labs](https://theconsensus.dev/company/arga-labs.html)Real-World SandboxesRaised a $10M Seed round on August 26, 2026.[Read more ↗](https://www.argalabs.com/blog/making-ai-agents-ready-for-the-real-world?utm_source=theconsensus.dev&utm_medium=referral)🇳🇱 Amsterdam HQ[Neno](https://theconsensus.dev/company/neno.html)Start, manage and scale your business without the admin headacheRaised a €6.6M Seed round on August 25, 2026.[Read more ↗](https://www.neno.co/resources/content/blog/neno-raises-%E2%82%AC6.6-million-to-build-ai-native-financial-services-for-europe-s-smes?utm_source=theconsensus.dev&utm_medium=referral)[See all](https://theconsensus.dev/funding.html)

## Events

Boston Apache DataFusion Meetup[September Meetup](https://luma.com/yexgqifv?utm_source=theconsensus.dev&utm_medium=referral)BostonSeptember 3, 2026[DataFusion](https://theconsensus.dev/t/datafusion.html)ClickHouse[Rows & Columns Summit](https://rowsandcolumnssummit.com/?utm_source=theconsensus.dev&utm_medium=referral)San FranciscoSeptember 22, 2026[databases](https://theconsensus.dev/t/databases.html)United States PostgreSQL Association[Postgres Summit US 2026](https://2026.postgressummit.us/?utm_source=theconsensus.dev&utm_medium=referral)New York CitySeptember 30, 2026[postgresql](https://theconsensus.dev/t/postgresql.html)[See all](https://theconsensus.dev/events.html)
