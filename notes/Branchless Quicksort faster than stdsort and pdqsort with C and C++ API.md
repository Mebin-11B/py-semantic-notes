---
title: "Branchless Quicksort faster than std:sort and pdqsort with C and C++ API"
url: https://tiki.li/blog/blqsort
clipped: 2026-06-17 00:52:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Branchless Quicksort faster than std:sort and pdqsort with C and C++ API](https://tiki.li/blog/blqsort)

## Digest Summary
Branchless Quicksort (blqs) is a single‑header library providing C and C++ interfaces for fast sorting. Benchmarks on an Apple M1 (Clang ‑O3) and an AMD Ryzen 3 (GCC ‑O3) show that the single‑threaded version sorts 50 M doubles faster than conventional std::sort; on the M1 the multithreaded variant gains an additional 3–4× speedup. The algorithm avoids branch misprediction by using a 1024‑element auxiliary buffer for branchless partitioning, copying blocks alternately to left/right pointers without conditional jumps. For small partitions (2–12 elements) it employs custom sorting‑network code paths. Pivot selection uses median‑of‑medians and switches to heapsort when a large imbalance is detected; already‑sorted partitions are detected early. When sorting non‑trivially‑copyable types (e.g., strings), blqs falls back to a BlockQuicksort variant that operates on indices and minimizes swaps, borrowing ideas from pdqsort. The library is used via `blqs::sort(begin, end)` in C++ or `blqsort(array, size)` in C after defining `BLQS_TYPE` and `BLQS_CMP`. It also supports custom structs through standard comparison operators or macro‑defined comparators.

## Discussion Summary
The discussion is largely appreciative of the new Rust sorting implementations, noting their strong performance relative to existing C++ and standard library sorts and praising the clear, simple code. Several commenters raise technical questions about the reliance on default construction and copying, asking whether move‑construction could reduce overhead and whether the temporary buffers are unnecessary. Others suggest broader comparisons, such as against vectorized bitonic‑network sorts, and seek clarification on the purported branch‑less technique, indicating mild uncertainty but overall positive reception.

---

## Full Article

Fast Branchless Quicksort using Sorting-Networks with C and C++ Interface
-------------------------------------------------------------------------

Performance results naturally depend on the underlying hardware. The following benchmarks show the execution times for sorting 50 million `doubles` using different sorting implementations. The measurements were taken on an *Apple M1* system using *Clang* and on an *AMD Ryzen 3 Linux* system using *GCC*, both compiled with the `-O3` option.

| Implementation | Apple M1 | AMD Ryzen |
| --- | --- | --- |
| std::sort | 1.33s | 5.56s |
| pdqsort | 1.33s | 2.81s |
| **blqsort** (single threaded) | ~~0.93s~~ **0.66** | 1.98s |

For a fair comparison, the [single-threaded version](https://github.com/chkas/blqsort/blob/main/cpp/test_double.cpp) of `blqs` was used here. On an M1, the threaded versions are another factor of 3 to 4 faster. In terms of runtime, the C++ versions differ only very little from the C version.

### blqsort

Full source code is included on [Github](https://github.com/chkas/blqsort).There are four implementations of **blqsort** here, each provided as a single header file.

### Branchless programming

On modern CPUs, **avoiding branch misprediction** is a key technique to speed up programs. This branchless approach:

```
for (int i = 0; i < 10000; i++) {
    small_numbers[smlen] = numbers[i];
    smlen += (numbers[i] < 500);
}
```

is much faster than the conventional version with a conditional branch:

```
for (int i = 0; i < 10000; i++) {
    if (numbers[i] < 500) {
        small_numbers[smlen] = numbers[i];
        smlen += 1;
    }
}
```

[This paper](https://arxiv.org/abs/1604.06697) by *Edelkamp* and *Weiß* shows how partitioning performance in Quicksort can be improved by avoiding conditional branches.

The strategy of using an auxiliary buffer for **branchless partitioning** is inspired by [fluxsort](https://github.com/scandum/fluxsort). The “auxiliary buffer” here means a 1024‑element stack array, not heap memory.

First, 1024 elements are copied from one side into an auxiliary buffer to make room for subsequent operations. Then, we alternately copy a 1024-element block to the left and right in a branchless manner. The left pointer is only incremented if the element is smaller than the pivot, otherwise, the right pointer is incremented - branchless, of course.

This involves more more than double the necessary copy operations. For data types that are cheap to copy, however, this is much less expensive than the branch mispredictions that would otherwise occur.

### Pivot strategy, bad input and sorting network

To avoid the `O(n²)` runtime caused by bad input data, the program can group identical elements together and switch to *heapsort* for that specific part if it detects a big imbalance during partitioning. The program also checks if a partition is already sorted.

For larger parts, it uses a median-of-medians strategy to find a good pivot. In addition, critical partitioning loops are explicitly unrolled.

For 2 to 16 elements, the algorithm uses custom sorting networks. This approach requires a separate code path for each size but sorts small subsets with very few swaps using a branchless *sort‑2* primitive. [Source for sorting networks](https://bertdobbelaere.github.io/sorting_networks.html)

C++
---

For types with higher copy costs that are not `is_trivially_copyable` (such as strings), the buffer-based branchless approach becomes less efficient. In such cases, a **BlockQuicksort** (*Edelkamp* and *Weiß*) variant is used instead. This processes only the element indices in a branchless manner and then moves the actual data with fewer swaps. Some ideas are from [pdqsort](https://github.com/orlp/pdqsort).

### Usage

You only need to include `blqs.h`, and it can be used just as easily as *std::sort*.

```
#include "blqs.h"

double data[SIZE];

blqs::sort(data, data + SIZE);
```

For the C++ multithreaded variant, which uses C++ threads, include `blqs_thr.h` instead of `blqs.h`. The function call remains the same.

C
-

In C, the code specialized for the data type is generated using `#define`.

### Usage

```
#define BLQS_CMP(a, b) ((a) < (b))
#define BLQS_TYPE double
#include "blqsort.h"

double data[SIZE];

blqsort(data, SIZE);
```

For the C multithreaded variant, which uses POSIX threads, include `blqsort_thr.h` instead of `blqsort.h`. The function call remains the same here as well.

Sorting Custom Data Structures
------------------------------

In practice, we often need to sort custom data structures. This is where *SIMD* libraries like *Google Highway* - while very fast for simple numbers - become difficult to use.

Using *std::sort* or *blqsort* gives you much more flexibility.

### C++

```
#include "blqs.h"

struct entry {
    int id;
    int value;

    bool operator<(const entry& other) const {
        return id < other.id;
    }
};

struct entry data[SIZE];

blqs::sort(data, data + SIZE);
```

### C

```
struct entry {
    int id;
    int value;
};
#define BLQS_CMP(a, b) (((a).id) < ((b).id))
#define BLQS_TYPE struct entry
#include "blqsort.h"

struct entry data[SIZE];

blqsort(data, SIZE);
```

Execution times for sorting 50 million of these `structs`.

| Implementation | Apple M1 | AMD Ryzen |
| --- | --- | --- |
| std::sort | 3.46s | 4.75s |
| pdqsort | 3.46s | 4.72s |
| **blqsort** | ~~0.90s~~ 0.76 | 2.16s |

### Links

[When ‘if’ slows you down, avoid it.](https://tiki.li/blog/branchless)

[Interactive sorting demo](https://tiki.li/sorting)

---

christof.kaser@gmail.com