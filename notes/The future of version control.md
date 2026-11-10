---
title: "The future of version control"
url: https://bramcohen.com/p/manyana
clipped: 2026-06-17 01:28:45
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The future of version control](https://bramcohen.com/p/manyana)

## Digest Summary
Manyana is a prototype version‑control system that demonstrates a CRDT‑based approach. By using Conflict‑Free Replicated Data Types, merges always succeed and produce the same result regardless of merge order, eliminating traditional blocking conflicts. The system flags edits that touch the same region as “conflicting,” presenting informative markers that show which side deleted or added each line, rather than opaque blobs. Line ordering becomes deterministic, preventing divergent resolutions across branches. History is stored as a single “weave” structure containing every line with metadata, so merges do not require finding a common ancestor or traversing a DAG. Rebase can be performed without discarding history by replaying commits onto a new base and annotating a primary ancestor. The current implementation is a 470‑line Python demo operating on individual files; it lacks features such as cherry‑picking and local undo but includes a design outline for them. The code is released to the public domain with a full design document in the README.

## Discussion Summary
The discussion shows mixed reactions to the CR‑based version‑control concept. Many participants view existing systems—Git, Jujutsu, and various merge‑tool UI extensions—as already addressing most pain points, stressing that semantic conflicts, scalability and workflow conventions remain central challenges. Skepticism arises about the practicality of CRDTs for code merges, the limited prototype size, and the need for real‑world data, while some express curiosity about AI‑assisted conflict resolution and higher‑level, AST‑driven approaches. Overall, there is cautious interest in novel ideas but a prevailing belief that incremental tooling improvements are more immediately valuable.

---

## Full Article

I’m releasing [Manyana](https://github.com/bramcohen/manyana), a project which I believe presents a coherent vision for the future of version control — and a compelling case for building it.

It’s based on the fundamentally sound approach of using CRDTs for version control, which is long overdue but hasn’t happened yet because of subtle UX issues. A CRDT merge always succeeds by definition, so there are no conflicts in the traditional sense — the key insight is that changes should be flagged as conflicting when they touch each other, giving you informative conflict presentation on top of a system which never actually fails. This project works that out.

One immediate benefit is much more informative conflict markers. Two people branch from a file containing a function. One deletes the function. The other adds a line in the middle of it. A traditional VCS gives you this:

```
<<<<<<< left
=======
def calculate(x):
    a = x * 2
    logger.debug(f"a={a}")
    b = a + 1
    return b
>>>>>>> right
```

Two opaque blobs. You have to mentally reconstruct what actually happened.

Manyana gives you this:

```
<<<<<<< begin deleted left
def calculate(x):
    a = x * 2
======= begin added right
    logger.debug(f"a={a}")
======= begin deleted left
    b = a + 1
    return b
>>>>>>> end conflict
```

Each section tells you *what happened* and *who did it*. Left deleted the function. Right added a line in the middle. You can see the structure of the conflict instead of staring at two blobs trying to figure it out.

CRDTs (Conflict-Free Replicated Data Types) give you eventual consistency: merges never fail, and the result is always the same no matter what order branches are merged in — including many branches mashed together by multiple people working independently. That one property turns out to have profound implications for every aspect of version control design.

**Line ordering becomes permanent.** When two branches insert code at the same point, the CRDT picks an ordering and it sticks. This prevents problems when conflicting sections are both kept but resolved in different orders on different branches.

**Conflicts are informative, not blocking.** The merge always produces a result. Conflicts are surfaced for review when concurrent edits happen “too near” each other, but they never block the merge itself. And because the algorithm tracks *what each side did* rather than just showing the two outcomes, the conflict presentation is genuinely useful.

**History lives in the structure.** The state is a *weave* — a single structure containing every line which has ever existed in the file, with metadata about when it was added and removed. This means merges don’t need to find a common ancestor or traverse the DAG. Two states go in, one state comes out, and it’s always correct.

One idea I’m particularly excited about: rebase doesn’t have to destroy history. Conventional rebase creates a fictional history where your commits happened on top of the latest main. In a CRDT system, you can get the same effect — replaying commits one at a time onto a new base — while keeping the full history. The only addition needed is a “primary ancestor” annotation in the DAG.

This matters because aggressive rebasing quickly produces merge topologies with no single common ancestor, which is exactly where traditional 3-way merge falls apart. CRDTs don’t care — the history is in the weave, not reconstructed from the DAG.

Manyana is a demo, not a full-blown version control system. It’s about 470 lines of Python which operate on individual files. Cherry-picking and local undo aren’t implemented yet, though the [README](https://github.com/bramcohen/manyana) lays out a vision for how those can be done well.

What it *is* is a proof that CRDT-based version control can handle the hard UX problems and come out with better answers than the tools we’re all using today — and a coherent design for building the real thing.

The code is public domain. The full design document is in the [README](https://github.com/bramcohen/manyana).