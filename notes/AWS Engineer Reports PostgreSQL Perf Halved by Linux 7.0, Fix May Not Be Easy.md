---
title: "AWS Engineer Reports PostgreSQL Perf Halved by Linux 7.0, Fix May Not Be Easy"
url: https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop
clipped: 2026-06-17 01:22:37
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [AWS Engineer Reports PostgreSQL Perf Halved by Linux 7.0, Fix May Not Be Easy](https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop)

## Digest Summary
- An AWS engineer reported that PostgreSQL throughput on a Graviton‑4 server drops to roughly 0.51× when running the Linux 7.0 development kernel, with latency increasing due to longer time spent in a user‑space spinlock.  
- The regression was traced to Linux 7.0’s change that removed PREEMPT_NONE as the default preemption mode, a modification previously discussed on Phoronix and upstreamed to the kernel.  
- A patch to restore PREEMPT_NONE as the default was posted to the Linux kernel mailing list, but its acceptance is uncertain.  
- Kernel maintainer Peter Zijlstra suggested the practical fix is to adapt PostgreSQL to use the Restartable Sequences (RSEQ) time‑slice extension, which was also upstreamed for Linux 7.0.  
- If PostgreSQL is not updated, Linux 7.0 stable—scheduled for release in about two weeks and slated for Ubuntu 26.04 LTS—may cause significant performance degradation for PostgreSQL workloads.

## Discussion Summary
The comments express concern that recent kernel changes, particularly the new pre‑emption handling introduced in Linux 7.0, risk breaking userspace applications such as PostgreSQL, with reported performance regressions up to 50 %. While some argue that adjusting kernel parameters or sysctl settings can mitigate the issue, there is criticism of the lack of a deprecation period allowing a transition. The discussion also references related kernel patches and articles, indicating a desire for a stable, backward‑compatible approach that does not force immediate code changes in dependent software.

---

## Full Article

An Amazon/AWS engineer raised the alarms on Friday over the current Linux 7.0 development kernel leading to the throughput for the PostgreSQL database server being around half that of prior kernel versions. The culprit halving the PostgreSQL performance is known but a revert looks like it may not happen and currently suggesting that PostgreSQL may need to be adapted.

Salvatore Dipietro of Amazon/AWS reported a throughput and latency regression for PostgreSQL. They found Linux 7.0 in its near-final form delivering around 0.51x the throughputof prior kernels on a Graviton4 server due to now much more time being spent in a user-space spinlock.

Bisecting the regression was traced back to the Linux 7.0 change of restricting the available preemption modes for the kernel. That change was previously covered on Phoronix within

[Linux 7.0 To Focus Just On Full & Lazy Preemption Models For Up-To-Date CPU Archs](https://www.phoronix.com/news/Linux-Restrict-Preempt-Modes)

and in turn upstreamed with the

[Linux 7.0 scheduler updates](https://www.phoronix.com/news/Linux-7.0-Scheduler)

.

As a result, yesterday posted to the Linux kernel mailing list was

[a patch](https://lore.kernel.org/lkml/20260403191942.21410-1-dipiets@amazon.it/)

to restore PREEMPT\_NONE as the default given the severity of the reported regression.

![pgbench regression benchmark](https://www.phoronix.net/image.php?id=2026&image=pgbench_regression)

While fixing an active performance regression, it looks like this change to restore PREEMPT\_NONE as the default preemption model might not be picked up. Peter Zijlstra who authored the original code simplifying the preemption modes has

[responded](https://lore.kernel.org/lkml/20260403213207.GF2872@noisy.programming.kicks-ass.net/#t)

that the "fix" is to make PostgreSQL make use of the Restartable Sequences (RSEQ) time slice extension. That

[time slice extension support](https://www.phoronix.com/news/Linux-TIP-Time-Slice-Extension)

was also upstreamed for Linux 7.0.

> "The fix here is to make PostgreSQL make use of rseq slice extension:
>   
>   
>  https://lkml.kernel.org/r/[[email protected]](https://www.phoronix.com/cdn-cgi/l/email-protection)
>   
>   
> That should limit the exposure to lock holder preemption (unless PostgreSQL is doing seriously egregious things)."

So if that stands and shifting the blame to PostgreSQL, Linux 7.0 stable could lead to a significant drop for PostgreSQL performance in some scenarios until that popular database server is updated.

Linux 7.0 stable is due out in about two weeks. This is also the kernel version powering Ubuntu 26.04 LTS to be released later in April.