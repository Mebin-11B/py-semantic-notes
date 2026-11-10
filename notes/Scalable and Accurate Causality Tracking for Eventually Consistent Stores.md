---
title: "Scalable and Accurate Causality Tracking for Eventually Consistent Stores"
source: "https://link.springer.com/chapter/10.1007/978-3-662-43352-2_6"
author:
  - "[[Paulo Sérgio Almeida]]"
  - "[[Carlos Baquero]]"
  - "[[Ricardo Gonçalves]]"
  - "[[Nuno Preguiça]]"
  - "[[Victor Fonte]]"
published: 2014-01-01
created: 2026-06-18
description: "In cloud computing environments, data storage systems often rely on optimistic replication to provide good performance and availability even in the presence of failures or network partitions. In this scenario, it is important to be able to accurately and efficiently..."
tags:
  - "clippings"
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - distributed systems
  - eventually consistent stores
  - causality tracking
  - logical clocks
related:
  - "[[Distributed Systems]]"
  - "[[Eventually Consistent Stores]]"
  - "[[Causality Tracking]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A proposed logical clock framework for eventually consistent stores that achieves accurate, scalable causality tracking without the linear overhead of traditional version vectors.
>
> **Key points:**
> - Distributed key-value stores rely on replication, which requires tracking causality to resolve concurrent writes without losing update history.
> - Existing version vectors either scale poorly (linear to clients/writes) or lose causality information, resulting in false conflicts.
> - The authors present a logical clock mechanism that maintains concise metadata linear only to the number of server replicas.
>
> **Concept links:** [[Distributed Systems]], [[Eventually Consistent Stores]], [[Causality Tracking]], [[Logical Clocks]]
>
> **Suggested connections:**
> - [[Optimistic Replication]] — resolving conflict states in multi-master database networks.
> - [[Vector Clocks]] — traditional methods of causality tracking and their scalability limitations.
<!-- ai-summary:end -->

## Abstract

In cloud computing environments, data storage systems often rely on optimistic replication to provide good performance and availability even in the presence of failures or network partitions. In this scenario, it is important to be able to accurately and efficiently identify updates executed concurrently. Current approaches to causality tracking in optimistic replication have problems with concurrent updates: they either (1) do not scale, as they require replicas to maintain information that grows linearly with the number of writes or unique clients; (2) lose information about causality, either by removing entries from client-id based version vectors or using server-id based version vectors, which cause false conflicts. We propose a new logical clock mechanism and a logical clock framework that together support a traditional key-value store API, while capturing causality in an accurate and scalable way, avoiding false conflicts. It maintains concise information per data replica, only linear on the number of replica servers, and allows data replicas to be compared and merged linear with the number of replica servers and versions.

## References

## Editor information

### Editors and Affiliations

## Rights and permissions

## About this paper

### Cite this paper

Almeida, P.S., Baquero, C., Gonçalves, R., Preguiça, N., Fonte, V. (2014). Scalable and Accurate Causality Tracking for Eventually Consistent Stores. In: Magoutis, K., Pietzuch, P. (eds) Distributed Applications and Interoperable Systems. DAIS 2014. Lecture Notes in Computer Science(), vol 8460. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-662-43352-2\_6

- [.RIS](https://citation-needed.springer.com/v2/references/10.1007/978-3-662-43352-2_6?format=refman&flavour=citation "Download this article's citation as a .RIS file")
- [.ENW](https://citation-needed.springer.com/v2/references/10.1007/978-3-662-43352-2_6?format=endnote&flavour=citation "Download this article's citation as a .ENW file")
- [.BIB](https://citation-needed.springer.com/v2/references/10.1007/978-3-662-43352-2_6?format=bibtex&flavour=citation "Download this article's citation as a .BIB file")
- DOI https://doi.org/10.1007/978-3-662-43352-2\_6
- Publisher NameSpringer, Berlin, Heidelberg
- Print ISBN978-3-662-43351-5
- Online ISBN978-3-662-43352-2
- eBook Packages [Computer Science](https://link.springer.com/search?facet-content-type=%22Book%22&package=11645&facet-start-year=2014&facet-end-year=2014) [Computer Science (R0)](https://link.springer.com/search?facet-content-type=%22Book%22&package=43710&facet-start-year=2014&facet-end-year=2014) [Springer Nature Proceedings Computer Science](https://link.springer.com/search?facet-content-type=%22Book%22&package=85344&facet-start-year=2014&facet-end-year=2014)

### Keywords

*These keywords were added by machine and not by the authors. This process is experimental and the keywords may be updated as the learning algorithm improves.*

## Publish with us

[Policies and ethics](https://www.springernature.com/gp/policies/book-publishing-policies)

[^1]: Almeida, P.S., Baquero, C., Fonte, V.: Interval tree clocks. In: Baker, T.P., Bui, A., Tixeuil, S. (eds.) OPODIS 2008. LNCS, vol. 5401, pp. 259–274. Springer, Heidelberg (2008)

[Chapter](https://link.springer.com/doi/10.1007/978-3-540-92221-6_18) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Interval%20tree%20clocks&pages=259-274&publication_year=2008&author=Almeida%2CP.S.&author=Baquero%2CC.&author=Fonte%2CV.)

[^2]: Birman, K.P., Joseph, T.A.: Reliable communication in the presence of failures. ACM Trans. Comput. Syst. 5(1), 47–76 (1987)

[Article](https://doi.org/10.1145%2F7351.7478) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Reliable%20communication%20in%20the%20presence%20of%20failures&journal=ACM%20Trans.%20Comput.%20Syst.&volume=5&issue=1&pages=47-76&publication_year=1987&author=Birman%2CK.P.&author=Joseph%2CT.A.)

[^3]: Brewer, E.A.: Towards robust distributed systems (abstract). In: Proceedings of the Nineteenth Annual ACM Symposium on Principles of Distributed Computing, PODC 2000, p. 7. ACM, New York (2000)

[Chapter](https://doi.org/10.1145%2F343477.343502) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Towards%20robust%20distributed%20systems%20%28abstract%29&publication_year=2000&author=Brewer%2CE.A.)

[^4]: Charron-Bost, B.: Concerning the size of logical clocks in distributed systems. Information Processing Letters 39, 11–16 (1991)

[Article](https://doi.org/10.1016%2F0020-0190%2891%2990055-M) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1122945) [MATH](http://www.emis.de/MATH-item?0735.68003) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Concerning%20the%20size%20of%20logical%20clocks%20in%20distributed%20systems&journal=Information%20Processing%20Letters&volume=39&pages=11-16&publication_year=1991&author=Charron-Bost%2CB.)

[^5]: DeCandia, G., Hastorun, D., Jampani, M., Kakulapati, G., Lakshman, A., Pilchin, A., Sivasubramanian, S., Vosshall, P., Vogels, W.: Dynamo: amazon’s highly available key-value store. In: Proceedings of Twenty-First ACM SIGOPS SOSP, pp. 205–220. ACM (2007)

[Google Scholar](https://scholar.google.com/scholar?&q=DeCandia%2C%20G.%2C%20Hastorun%2C%20D.%2C%20Jampani%2C%20M.%2C%20Kakulapati%2C%20G.%2C%20Lakshman%2C%20A.%2C%20Pilchin%2C%20A.%2C%20Sivasubramanian%2C%20S.%2C%20Vosshall%2C%20P.%2C%20Vogels%2C%20W.%3A%20Dynamo%3A%20amazon%E2%80%99s%20highly%20available%20key-value%20store.%20In%3A%20Proceedings%20of%20Twenty-First%20ACM%20SIGOPS%20SOSP%2C%20pp.%20205%E2%80%93220.%20ACM%20%282007%29)

[^6]: Gilbert, S., Lynch, N.: Brewer’s conjecture and the feasibility of consistent available partition-tolerant web services. ACM SIGACT News, 2002 (2002)

[Google Scholar](https://scholar.google.com/scholar?&q=Gilbert%2C%20S.%2C%20Lynch%2C%20N.%3A%20Brewer%E2%80%99s%20conjecture%20and%20the%20feasibility%20of%20consistent%20available%20partition-tolerant%20web%20services.%20ACM%20SIGACT%20News%2C%202002%20%282002%29)

[^7]: Golding, R.A.: A weak-consistency architecture for distributed information services. Computing Systems 5(4), 379–405 (1992)

[Google Scholar](https://scholar.google.com/scholar_lookup?&title=A%20weak-consistency%20architecture%20for%20distributed%20information%20services&journal=Computing%20Systems&volume=5&issue=4&pages=379-405&publication_year=1992&author=Golding%2CR.A.)

[^8]: Kistler, J.J., Satyanarayanan, M.: Disconnected operation in the Coda file system. In: Thirteenth ACM Symposium on Operating Systems Principles, vol. 25, pp. 213–225. Asilomar Conference Center, Pacific Grove (1991)

[Chapter](https://doi.org/10.1145%2F121132.121166) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Disconnected%20operation%20in%20the%20Coda%20file%20system&pages=213-225&publication_year=1991&author=Kistler%2CJ.J.&author=Satyanarayanan%2CM.)

[^9]: Klophaus, R.: Riak core: building distributed applications without shared state. In: ACM SIGPLAN Commercial Users of Functional Programming, CUFP 2010, p. 14:1. ACM, New York (2010), [http://doi.acm.org/10.1145/1900160.1900176](http://doi.acm.org/10.1145/1900160.1900176)

[Google Scholar](https://scholar.google.com/scholar_lookup?&title=Riak%20core%3A%20building%20distributed%20applications%20without%20shared%20state&publication_year=2010&author=Klophaus%2CR.)

[^10]: Lakshman, A., Malik, P.: Cassandra: a decentralized structured storage system. SIGOPS Oper. Syst. Rev. 44, 35–40 (2010)

[Article](https://doi.org/10.1145%2F1773912.1773922) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Cassandra%3A%20a%20decentralized%20structured%20storage%20system&journal=SIGOPS%20Oper.%20Syst.%20Rev.&volume=44&pages=35-40&publication_year=2010&author=Lakshman%2CA.&author=Malik%2CP.)

[^11]: Lamport, L.: Time, clocks and the ordering of events in a distributed system. Communications of the ACM 21(7), 558–565 (1978)

[Article](https://doi.org/10.1145%2F359545.359563) [MATH](http://www.emis.de/MATH-item?0378.68027) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Time%2C%20clocks%20and%20the%20ordering%20of%20events%20in%20a%20distributed%20system&journal=Communications%20of%20the%20ACM&volume=21&issue=7&pages=558-565&publication_year=1978&author=Lamport%2CL.)

[^12]: Mahajan, P., Setty, S., Lee, S., Clement, A., Alvisi, L., Dahlin, M., Walfish, M.: Depot: Cloud storage with minimal trust. In: OSDI 2010 (October 2010)

[Google Scholar](https://scholar.google.com/scholar?&q=Mahajan%2C%20P.%2C%20Setty%2C%20S.%2C%20Lee%2C%20S.%2C%20Clement%2C%20A.%2C%20Alvisi%2C%20L.%2C%20Dahlin%2C%20M.%2C%20Walfish%2C%20M.%3A%20Depot%3A%20Cloud%20storage%20with%20minimal%20trust.%20In%3A%20OSDI%202010%20%28October%202010%29)

[^13]: Malkhi, D., Terry, D.: Concise version vectors in winFS. In: Fraigniaud, P. (ed.) DISC 2005. LNCS, vol. 3724, pp. 339–353. Springer, Heidelberg (2005)

[Chapter](https://link.springer.com/doi/10.1007/11561927_25) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Concise%20version%20vectors%20in%20winFS&pages=339-353&publication_year=2005&author=Malkhi%2CD.&author=Terry%2CD.)

[^14]: Parker, D.S., Popek, G., Rudisin, G., Stoughton, A., Walker, B., Walton, E., Chow, J., Edwards, D., Kiser, S., Kline, C.: Detection of mutual inconsistency in distributed systems. Transactions on Software Engineering 9(3), 240–246 (1983)

[Article](https://doi.org/10.1109%2FTSE.1983.236733) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Detection%20of%20mutual%20inconsistency%20in%20distributed%20systems&journal=Transactions%20on%20Software%20Engineering&volume=9&issue=3&pages=240-246&publication_year=1983&author=Parker%2CD.S.&author=Popek%2CG.&author=Rudisin%2CG.&author=Stoughton%2CA.&author=Walker%2CB.&author=Walton%2CE.&author=Chow%2CJ.&author=Edwards%2CD.&author=Kiser%2CS.&author=Kline%2CC.)

[^15]: Petersen, K., Spreitzer, M.J., Terry, D.B., Theimer, M.M., Demers, A.J.: Flexible update propagation for weakly consistent replication. In: Sixteen ACM Symposium on Operating Systems Principles, Saint Malo, France (October 1997)

[Google Scholar](https://scholar.google.com/scholar?&q=Petersen%2C%20K.%2C%20Spreitzer%2C%20M.J.%2C%20Terry%2C%20D.B.%2C%20Theimer%2C%20M.M.%2C%20Demers%2C%20A.J.%3A%20Flexible%20update%20propagation%20for%20weakly%20consistent%20replication.%20In%3A%20Sixteen%20ACM%20Symposium%20on%20Operating%20Systems%20Principles%2C%20Saint%20Malo%2C%20France%20%28October%201997%29)

[^16]: Preguiça, N., Baquero, C., Almeida, P.S., Fonte, V., Gonçalves, R.: Brief announcement: Efficient causality tracking in distributed storage systems with dotted version vectors. In: Proceedings of the 2012 ACM Symposium on PODC, pp. 335–336. ACM (2012)

[Google Scholar](https://scholar.google.com/scholar?&q=Pregui%C3%A7a%2C%20N.%2C%20Baquero%2C%20C.%2C%20Almeida%2C%20P.S.%2C%20Fonte%2C%20V.%2C%20Gon%C3%A7alves%2C%20R.%3A%20Brief%20announcement%3A%20Efficient%20causality%20tracking%20in%20distributed%20storage%20systems%20with%20dotted%20version%20vectors.%20In%3A%20Proceedings%20of%20the%202012%20ACM%20Symposium%20on%20PODC%2C%20pp.%20335%E2%80%93336.%20ACM%20%282012%29)

[^17]: Ramasubramanian, V., Rodeheffer, T.L., Terry, D.B., Walraed-Sullivan, M., Wobber, T., Marshall, C.C., Vahdat, A.: Cimbiosys: a platform for content-based partial replication. In: Proceedings of the 6th USENIX Symposium on NSDI, Berkeley, CA, USA, pp. 261–276 (2009)

[Google Scholar](https://scholar.google.com/scholar?&q=Ramasubramanian%2C%20V.%2C%20Rodeheffer%2C%20T.L.%2C%20Terry%2C%20D.B.%2C%20Walraed-Sullivan%2C%20M.%2C%20Wobber%2C%20T.%2C%20Marshall%2C%20C.C.%2C%20Vahdat%2C%20A.%3A%20Cimbiosys%3A%20a%20platform%20for%20content-based%20partial%20replication.%20In%3A%20Proceedings%20of%20the%206th%20USENIX%20Symposium%20on%20NSDI%2C%20Berkeley%2C%20CA%2C%20USA%2C%20pp.%20261%E2%80%93276%20%282009%29)

[^18]: Ratner, D., Reiher, P.L., Popek, G.J.: Roam: A scalable replication system for mobility. MONET 9(5), 537–544 (2004)

[Google Scholar](https://scholar.google.com/scholar_lookup?&title=Roam%3A%20A%20scalable%20replication%20system%20for%20mobility&journal=MONET&volume=9&issue=5&pages=537-544&publication_year=2004&author=Ratner%2CD.&author=Reiher%2CP.L.&author=Popek%2CG.J.)

[^19]: Raynal, M., Singhal, M.: Logical time: Capturing causality in distributed systems. IEEE Computer 30, 49–56 (1996)

[Article](https://doi.org/10.1109%2F2.485846) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Logical%20time%3A%20Capturing%20causality%20in%20distributed%20systems&journal=IEEE%20Computer&volume=30&pages=49-56&publication_year=1996&author=Raynal%2CM.&author=Singhal%2CM.)

[^20]: Schwarz, R., Mattern, F.: Detecting causal relationships in distributed computations: In search of the holy grail. Distributed Computing 3(7), 149–174 (1994)

[Article](https://link.springer.com/doi/10.1007/BF02277859) [MATH](http://www.emis.de/MATH-item?0813.68096) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Detecting%20causal%20relationships%20in%20distributed%20computations%3A%20In%20search%20of%20the%20holy%20grail&journal=Distributed%20Computing&volume=3&issue=7&pages=149-174&publication_year=1994&author=Schwarz%2CR.&author=Mattern%2CF.)

[^21]: Torres-Rojas, F.J., Ahamad, M.: Plausible clocks: constant size logical clocks for distributed systems. Distributed Computing 12(4), 179–196 (1999)

[Article](https://link.springer.com/doi/10.1007/s004460050065) [Google Scholar](https://scholar.google.com/scholar_lookup?&title=Plausible%20clocks%3A%20constant%20size%20logical%20clocks%20for%20distributed%20systems&journal=Distributed%20Computing&volume=12&issue=4&pages=179-196&publication_year=1999&author=Torres-Rojas%2CF.J.&author=Ahamad%2CM.)

[^22]: Wang, W., Amza, C.: On optimal concurrency control for optimistic replication. In: Proc. ICDCS, pp. 317–326 (2009)

[Google Scholar](https://scholar.google.com/scholar?&q=Wang%2C%20W.%2C%20Amza%2C%20C.%3A%20On%20optimal%20concurrency%20control%20for%20optimistic%20replication.%20In%3A%20Proc.%20ICDCS%2C%20pp.%20317%E2%80%93326%20%282009%29)