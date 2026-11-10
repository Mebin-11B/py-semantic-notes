---
title: "Stonebraker on CAP theorem and Databases"
url: https://perspectives.mvdirona.com/2010/04/stonebraker-on-cap-theorem-and-databases/
clipped: 2026-06-17 01:50:48
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - cap theorem
  - strong consistency
  - eventual consistency
  - nosql databases
  - database reliability
related:
  - "[[CAP Theorem]]"
  - "[[Strong Consistency]]"
  - "[[NoSQL Databases]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Michael Stonebraker critiques the NoSQL community's reliance on the CAP theorem, arguing that eventual consistency does not protect against common database errors and strong consistency remains viable and preferred.
>
> **Key points:**
> - Stonebraker argues that most database errors (application bugs, administrative errors, implementation faults) cause permanent data loss regardless of consistency models.
> - Eventual consistency models are often adopted under the assumption that partitions are frequent, but Stonebraker claims real-world network partitions are relatively rare.
> - The article advocates for strong consistency as a default, noting it simplifies application design and is increasingly scalable.
>
> **Concept links:** [[Cap Theorem]], [[Strong Consistency]], [[Eventual Consistency]], [[Nosql Databases]], [[Database Reliability]]
>
> **Suggested connections:**
> - [[CAP Theorem]] — trade-offs between consistency, availability, and partition tolerance.
> - [[Strong Consistency]] — why maintaining solid state guarantees simplifies software architecture.
> - [[NoSQL Databases]] — the architectural choices of early distributed databases.
<!-- ai-summary:end -->

# [Stonebraker on CAP theorem and Databases](https://perspectives.mvdirona.com/2010/04/stonebraker-on-cap-theorem-and-databases/)

## Digest Summary
Mike Stonebraker’s recent CACM blog post critiques the NoSQL community’s interpretation of Brewer’s CAP theorem, arguing that eventual consistency does not mitigate common database errors such as application bugs, administrative mistakes, or implementation faults, which result in permanent data loss unless an offline backup exists. He highlights that deferred delete—a practice of marking records for later garbage collection—offers limited protection against accidental deletions. Stonebraker also notes that network partitions, while theoretically central to CAP, are relatively rare, though networking misconfigurations and equipment failures remain significant failure vectors. The article questions whether eventual consistency is the appropriate default for large‑scale workloads, emphasizing that full consistency can be achieved at scale (e.g., Amazon SimpleDB’s recent support) and often simplifies application development while reducing implementation errors. The author advises against discarding strong consistency prematurely, as it can be cost‑effective and enhance reliability for many applications.

## Discussion Summary
Comments note the 2010 article’s continued relevance and emphasize the significance of its date. Opinions diverge on consistency models: several remarks argue that eventual consistency fails in many error‑prone scenarios and that full consistency should be used when feasible, while others contend that eventual consistency suits the majority of business cases and remains practical. The discussion also critiques Stonebraker’s claim that partition events are rare, highlighting the broader impact of global cloud distribution and the trade‑offs between consistency, availability, and partition tolerance.

---

## Full Article

[Mike Stonebraker](http://en.wikipedia.org/wiki/Michael_Stonebraker) published an excellent blog posting yesterday at the [CACM site](http://cacm.acm.org/): [Errors in Database Systems, Eventual Consistency, and the CAP Theorem](http://cacm.acm.org/blogs/blog-cacm/83396-errors-in-database-systems-eventual-consistency-and-the-cap-theorem/fulltext). In this article, Mike challenges the application of [Eric Brewer’s](http://www.eecs.berkeley.edu/~brewer/) [CAP Theorem](http://en.wikipedia.org/wiki/CAP_theorem) by the [NoSQL](http://en.wikipedia.org/wiki/NoSQL) database community. Many of the high-scale NoSQL system implementers have argued that the CAP theorem forces them to go with an eventual consistent model.

Mike challenges this assertion pointing that some common database errors are not avoided by eventual consistency and CAP really doesn’t apply in these cases. If you have an application error, administrative error, or database implementation bug that losses data, then it is simply gone unless you have an offline copy. This, by the way, is why I’m a big fan of deferred delete. This is a technique where deleted items are marked as deleted but not garbage collected until some days or preferably weeks later. Deferred delete is not full protection but it has saves my butt more than once and I’m a believer. See [On Designing and Deploying Internet-Scale Services](https://mvdirona.com/jrh/talksAndPapers/JamesRH_Lisa.pdf) for more detail.

CAP and the application of eventual consistency doesn’t directly protect us against application or database implementation errors. And, in the case of a large scale disaster where the cluster is lost entirely, again, neither eventual consistency nor CAP offer a solution. Mike also notes that network partitions are fairly rare. I could quibble a bit on this one. Network partitions should be rare but net gear continues to cause more issues than it should. Networking configuration errors, black holes, dropped packets, and brownouts, remain a popular discussion point in post mortems industry-wide. I see this improving over the next 5 years but we have a long way to go. In [Networking: the Last Bastion of Mainframe Computing](https://perspectives.mvdirona.com/2009/12/19/NetworkingTheLastBastionOfMainframeComputing.aspx), I argue that net gear is still operating on the mainframe business model: large, vertically integrated and expensive equipment, deployed in pairs. When it comes to redundancy at scale, 2 is a poor choice.

Mike’s article questions whether eventual consistency is really the right answer for these workloads. I made some similar points in “[I love eventual consistency but…](https://perspectives.mvdirona.com/2010/02/24/ILoveEventualConsistencyBut.aspx)” In that posting, I argued that many applications are much easier to implement with full consistency and full consistency can be practically implemented at high scale. In fact, [Amazon SimpleDB](http://aws.amazon.com/simpledb/) recently announced support for full consistency. Apps needed full consistency are now easier to write and, where only eventual consistency is needed, its available as well.

Don’t throw full consistency out too early. For many applications, it is both affordable and helps reduce application implementation errors.

–jrh

Thanks to [Deepak Singh](http://www.linkedin.com/in/dsingh) for pointing me to this article.

James Hamilton

e: [jrh@mvdirona.com](mailto:jrh@mvdirona.com)

w: [http://www.mvdirona.com](https://mvdirona.com/)

b: [http://blog.mvdirona.com](https://blog.mvdirona.com/) / [http://perspectives.mvdirona.com](https://perspectives.mvdirona.com/)