---
title: "πFS"
url: https://github.com/philipl/pifs
clipped: 2026-06-17 00:49:19
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - data compression
  - information theory
  - software satire
related:
  - "[[SQLite Is a Library of Congress Recommended Storage Format]]"
  - "[[Case study Creative math – How AI fakes proofs]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** πFS is a satirical proof-of-concept filesystem that claims '100% compression' by indexing the location of byte sequences within the infinite, normal digits of Pi.
>
> **Key points:**
> - Explains the concept of πfs, a filesystem that stores files by referencing their index and length in the digits of Pi.
> - Points out the reliance on the Bailey-Borwein-Plouffe formula to retrieve arbitrary binary segments.
> - Explains the irony that the indexing overhead and metadata size exceed the size of the original data.
> - Analyzes it as an information-theory joke and thought experiment about limits of data compression.
>
> **Concept links:** [[Data Compression]], [[Information Theory]], [[Mathematics Concepts]], [[Filesystem Design]], [[Software Satire]]
>
> **Suggested connections:**
> - [[SQLite Is a Library of Congress Recommended Storage Format]] — contrasts standard data storage models with satirical mathematical indexing.
> - [[Case study Creative math – How AI fakes proofs]] — connects mathematics, proofs, and theoretical computer science.
<!-- ai-summary:end -->

# [πFS](https://github.com/philipl/pifs)

## Digest Summary
πfs is a prototype filesystem that treats the digits of π as an infinite data source. It assumes π is normal (digits uniformly distributed) and thus contains every possible finite byte sequence; files are identified by their index and length within π, extracted via the Bailey–Borwein–Plouffe (BBP) formula. The implementation builds with autotools and libfuse (e.g., `sudo apt-get install autotools-dev automake libfuse-dev`, then `./autogen.sh && ./configure && make && make install`). Mounting uses `πfs -o mdd= `, where the metadata directory stores filenames and the π indices for each file. Because locating long byte sequences directly is costly, the prototype stores each byte separately, looking up individual occurrences in π. Metadata persistence is required to retrieve file locations; loss of metadata does not affect the underlying data in π. Performance is slow (e.g., minutes for small files) as this is an initial proof‑of‑concept. Planned enhancements include variable‑length search, arithmetic coding, parallel lookup, cloud‑based π access, and integration with Hadoop.

## Discussion Summary
The discussion treats the Pi‑based filesystem as an entertaining curiosity rather than a viable storage solution, noting that indexing overhead typically outweighs any compression benefit and that the implementation is slow and inefficient. Participants reference information‑theoretic limits, the unproven normality of π, and analogous projects, while expressing both admiration for the clever concept and skepticism about its practical value. The consensus frames it as a playful thought experiment with limited real‑world applicability, raising questions about metadata size, performance, and theoretical assumptions.

---

## Full Article

πfs: Never worry about data again!
==================================

πfs is a revolutionary new file system that, instead of wasting space storing
your data on your hard drive, stores your data in π! You'll never run out of
space again - π holds every file that could possibly exist! They said 100%
compression was impossible? You're looking at it!

πfs is dead simple to build:

Firstly, you must install autoconf, automake, libfuse packages in your system.
For example, if you have Debian try:

```
sudo apt-get install autotools-dev
sudo apt-get install automake
sudo apt-get install libfuse-dev
```

```
./autogen.sh
./configure
make
make install
```

πfs is dead simple to use:

```
πfs -o mdd=<metadata directory> <mountpoint>
```

where the *metadata directory* is where πfs should store its metadata (such
as filenames or the locations of your files in π) and *mountpoint* is your
usual filesystem mountpoint.

What does π have to do with my data?
------------------------------------

π (or pi) is one of the most important constants in mathematics and has a
variety of interesting properties (which you can read about at [wikipedia](http://en.wikipedia.org/wiki/Pi))

One of the properties that π is conjectured to have is that it is *normal*,
which is to say that its digits are all distributed evenly, with the
implication that it is a *disjunctive sequence*, meaning that all possible
finite sequences of digits will be present somewhere in it. If we consider
π in base 16 (hexadecimal) , it is trivial to see that if this conjecture
is true, then all possible finite files must exist within π. The first
record of this observation dates back to [2001](http://www.netfunny.com/rhf/jokes/01/Jun/pi.html).

From here, it is a small leap to see that if π contains all possible files,
why are we wasting exabytes of space storing those files, when we could just
look them up in π!

Every file that could possibly exist?
-------------------------------------

That's right! Every file you've ever created, or anyone else has created or
will create! Copyright infringement? It's just a few digits of π! They were
always there!

But how do I look up my data in π?
----------------------------------

As long as you know the index into π of your file and its length, its a
simple task to extract the file using the [Bailey–Borwein–Plouffe formula](http://en.wikipedia.org/wiki/BBP-type_formula)
Similarly, you can use the formula to initially find the index of your file

Now, we all know that it can take a while to find a long sequence of digits
in π, so for practical reasons, we should break the files up into smaller
chunks that can be more readily found.

In this implementation, to maximise performance, we consider each individual byte
of the file separately, and look it up in π.

So I've looked up my bytes in π, but how do I remember where they are?
----------------------------------------------------------------------

Well, you've obviously got to write them down somewhere; you could use a piece of
paper, but remember all that storage space we saved by moving our data into π? Why
don't we store our file locations there!?! Even better, the location of our files in
π is metadata and as [we all know](http://datatechnologytoday.wordpress.com/2010/09/07/on-the-importance-of-metadata/)
metadata is becoming more and more important in everything we do. Doesn't it feel
great to have generated so much metadata? Why waste time with old fashioned data
when you can just deal with metadata, and lots of it!

Yeah, but what happens if lose my file locations?
-------------------------------------------------

No problem, the locations are just metadata! Your files are still there, sitting
in π - they're never going away, are they?

Why is this thing so slow? It took me five minutes to store a 400 line text file!
---------------------------------------------------------------------------------

Well, this is just an initial prototype, and don't worry, there's always Moore's law!

Where do we go from here?
-------------------------

There's lots of potential for the future!

* Variable run length search and lookup!
* Arithmetic Coding!
* Parallelizable lookup!
* Cloud based π lookup!
* πfs for Hadoop!