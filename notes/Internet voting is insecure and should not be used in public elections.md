---
title: "Internet voting is insecure and should not be used in public elections"
url: https://blog.citp.princeton.edu/2026/01/16/internet-voting-is-insecure-and-should-not-be-used-in-public-elections/
clipped: 2026-06-17 01:55:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Internet voting is insecure and should not be used in public elections](https://blog.citp.princeton.edu/2026/01/16/internet-voting-is-insecure-and-should-not-be-used-in-public-elections/)

## Digest Summary
Internet voting remains insecure and cannot be made safe with existing technology. All such systems suffer three core vulnerabilities: (1) voter‑device malware can alter selections; (2) server‑side malware or insider attacks can modify ballots; (3) county‑office systems that process internet ballots are equally vulnerable to hacking. Unlike paper ballots, a single global attacker can affect large numbers of votes undetected. End‑to‑end verifiable internet voting (E2E‑VIV) adds further weaknesses: verification apps may be compromised, receipt‑free designs are complex and rarely used, and there is no reliable dispute‑resolution mechanism for voters who detect fraud. The recently announced “VoteSecure” SDK, promoted by Bradley Tusk’s Mobile Voting Foundation, exhibits the same security gaps; developers acknowledge the flaws and lack a viable remedy. The scientific consensus, reflected in decades of peer‑reviewed research, holds that no known or foreseeable technology can secure internet voting for public elections. Consequently, election officials should treat press releases about internet voting with caution and rely on established, peer‑reviewed security analyses.

## Discussion Summary
The comments collectively emphasize trust as the decisive factor in elections, viewing paper‑based voting as the more reliable and auditable method because its vulnerabilities and safeguards are well understood. Concerns dominate regarding the security, secrecy, and scalability of internet voting, with many highlighting the ease of large‑scale manipulation and the difficulty of guaranteeing a trustworthy system. A smaller subset argues that strong cryptographic techniques, blockchain or rigorous oversight could make online voting feasible, but most remain skeptical that such safeguards can be universally achieved. Overall sentiment favors maintaining or reverting to paper or hybrid voting processes.

---

## Full Article

*Signed by a group of 21 computer scientists expert in election security*

Executive summary
-----------------

Scientists have understood for many years that internet voting is insecure and that there is no known or foreseeable technology that can make it secure. Still, vendors of internet voting keep claiming that, somehow, their new system is different, or the insecurity doesn’t matter. Bradley Tusk and his Mobile Voting Foundation keep touting internet voting to journalists and election administrators; this whole effort is misleading and dangerous.

**Part I.**  All internet voting systems are insecure. The insecurity is worse than a well-run conventional paper ballot system, because a very small number of people may have the power to change any (or all) votes that go through the system, without detection. This insecurity has been known for years; every internet voting system yet proposed suffers from it, for basic reasons that cannot be fixed with existing technology.

**Part II.** Internet voting systems known as “End-to-End Verifiable Internet Voting” are also insecure, in their own special ways.

**Part III.**  Recently, Tusk announced an E2E-VIV system called “VoteSecure.”  It suffers from all the same insecurities.  Even its developers admit that in their development documents.  Furthermore, VoteSecure isn’t a complete, usable product, it’s just a “cryptographic core” that someone might someday incorporate into a usable product.

**Conclusion.**  Recent announcements by Bradley Tusks’s Mobile Voting Foundation suggest that the development of VoteSecure somehow makes internet voting safe and appropriate for use in public elections.  This is untrue and dangerous.  All deployed Internet voting systems are unsafe, VoteSecure is unsafe and isn’t even a deployed voting  system, and there is no known (or foreseeable) technology that can make Internet voting safe.

Part I.  All internet voting systems are insecure
-------------------------------------------------

Internet voting systems (including vote-by-smartphone) have three very serious weaknesses:

1. Malware on the voter’s phone (or computer) can transmit different votes than the voter selected and reviewed. Voters use a variety of devices (Android, iPhone, Windows, Mac) which are constantly being attacked by malware.
2. Malware (or insiders) at the server can change votes. Internet servers are constantly being hacked from all over the world, often with serious results.
3. Malware at the county election office can change votes (in those systems where the internet ballots are printed in the county office for scanning). County election computers are not more secure than other government or commercial servers, which are regularly hacked with disastrous results.

Although conventional ballots (marked on paper with a pen) are not perfectly secure either, the problem with internet ballots is the ability for a single attacker (from anywhere in the world) to alter a very large number of ballots with a single scaled-up attack.  That’s much harder to do with hand-marked paper ballots; occasionally people try large-scale absentee ballot fraud, typically resulting in their being caught, prosecuted, and convicted.

Part II.  E2E-VIV internet voting systems are also insecure
-----------------------------------------------------------

Years ago, the concept of “End-to-End Verifiable Internet Voting” (E2E-VIV) was proposed, which was supposed to remedy some of these weaknesses by allowing voters to check that their vote was recorded and counted correctly.  Unfortunately, all E2E-VIV systems suffer from one or more of the following weaknesses:

1. Voters must rely on a computer app to do the checking, and the checking app (if infected by malware) could lie to them.
2. Voters should not be able to prove to anyone else how they voted – the technical term is “receipt-free” – otherwise an attacker could build an automated system of mass vote-buying via the internet. But receipt-free E2E-VIV systems are complicated and counterintuitive for people to use.
3. It’s difficult to make an E2E-VIV checking app that’s both trustworthy and receipt-free. The best solutions known allow checking only of votes that will be discarded, and casting of votes that haven’t been checked; this is highly counterintuitive for most voters!
4. The checking app must be separate from the voting app, otherwise it doesn’t add any malware-resistance at all.  But human nature being what it is, only a tiny fraction of voters will do the extra steps to run the checking protocol.  If hardly anyone uses the checker, then the checker is largely ineffective.
5. Even if some voters do run the checking app, if those voters detect that the system is cheating (which is the purpose of the checking app), there’s no way the voters can prove that to election officials.  That is, there is no “dispute resolution” protocol that could effectively work.

Thus, the problem with all known E2E-VIV systems proposed to date is that the “verification” part doesn’t add any useful security: if a few percent of voters use the checking protocol and see that the system is sometimes cheating, the system can still steal the votes of all the voters that don’t use the checking protocol. And you might think, “well, if some voters catch the system cheating, then election administrators can take appropriate action”, but no appropriate action is possible: the election administrator can’t cancel the election just because a few voters claim (without proof) that the system is cheating!  That’s what it means to have no dispute resolution protocol.

All of this is well understood in the scientific consensus. The insecurity of non-E2E-VIV systems has been documented for decades.  For a survey of those results, see “[Is Internet Voting Trustworthy? The Science and the Policy Battles](https://scholars.unh.edu/unh_lr/vol21/iss2/9/)”. The lack of dispute resolution in E2E-VIV systems has been [known for many years as well](http://www2.seas.gwu.edu/~poorvi/Audiotegrity.pdf).

Part III. VoteSecure is insecure
--------------------------------

Bradley Tusk’s [Mobile Voting Foundation](https://www.mobilevoting.org/) contracted with the R&D company [Free and Fair](https://freeandfair.us/about/) to develop internet voting software. Their [press release of November 14, 2025](https://www.prnewswire.com/news-releases/the-mobile-voting-foundation-and-free--fair-release-votesecure-the-first-software-development-kit-for-secure-transparent-and-verifiable-mobile-voting-302615896.html) announced the release of an [open-source “Software Development Kit”](https://github.com/FreeAndFair/VoteSecure) and claimed “This technology milestone means that secure and verifiable mobile voting is within reach.”

After [some computer scientists examined](https://github.com/FreeAndFair/VoteSecure/issues/2#issue-3629697747) the open-source VoteSecure and [described serious flaws in its security](https://blog.citp.princeton.edu/2025/12/16/mobile-voting-projects-vote-by-smartphone-has-real-security-gaps/), Dr. Joe Kiniry and Dr. Daniel Zimmerman of Free and Fair responded. They say, in effect, that all the critiques are accurate, but they don’t know a way to do any better: “[We share many of [the critique’s] core goals, including voter confidence, election integrity, and resistance to coercion. Where we differ is not so much in values as in assumptions about what is achievable—and meaningful—in unsupervised voting environments.](https://github.com/FreeAndFair/VoteSecure/issues/5#issuecomment-3721078472)”

In particular,

In addition to the previously described flaws in the VoteSecure protocol, we note that its vote checking system is susceptible to mass automated vote-buying attacks1; and we have discovered a new flaw in the VoteSecure protocol that allows votes to be stolen2. *[click for details]*
[1] This conclusion is based on a technical analysis.  In the VoteSecure protocol, checking app can be run on a vote that is then cast; the checking app must be runnable on an alternate device than the voting app; that alternate device is likely a PC on which the user has control of installed software; user-installed software can extract decrypted randomizers; this allows the voter to participate in a mass vote-buying scheme. [2] “[Clash attacks on the VoteSecure voting and verification process](https://github.com/FreeAndFair/VoteSecure/issues/6)”, by Vanessa Teague and Olivier Pereira, January 13, 2026.

Based on our own expertise test, and especially in light of the response from Free and Fair, we stand by the original analysis: [Mobile Voting Project’s vote-by-smartphone has critical security gaps](https://blog.citp.princeton.edu/2025/12/16/mobile-voting-projects-vote-by-smartphone-has-real-security-gaps/).

Conclusion
----------

It has been the scientific consensus for decades that internet voting is not securable by any known technology. Research on future technologies is certainly worth doing. However, the decades of work on E2E-VIV systems has yet to produce any solution, or even any hope of a solution, to the fundamental problems.

Therefore, when it comes to internet voting systems, election officials and journalists should be especially wary of “science by press release.” Perhaps some day an internet voting solution will be proposed that can stand up to scientific investigation. The most reliable venue for assessing that is in peer-reviewed scientific articles. Reputable cybersecurity conferences and journals have published a lot of good science in this area. Press releases are not a reliable way to assess the trustworthiness of election systems.

Signed
------

*(affiliations for for identification only and do not indicate institutional endorsement)*

**Andrew W. Appel**, *Eugene Higgins Professor Emeritus of Computer Science, Princeton University*

**Steven M. Bellovin**, *Percy K. and Vida L.W. Hudson Professor Emeritus of Computer Science, Columbia University*

**Duncan Buell**, *Chair Emeritus — NCR Chair in Computer Science and Engineering, University of South Carolina*

**Braden L. Crimmins**, *PhD Student, Univ. of Michigan School of Engineering & Knight-Hennessy Scholar, Stanford Law*

**Richard DeMillo**, *Charlotte B and Roger C  Warren Chair in Computing, Georgia Tech*

**David L. Dill**, *Donald E. Knuth Professor, Emeritus, in the School of Engineering, Stanford University*

**Jeremy Epstein,** *National Science Foundation (retired) and Georgia Institute of Technology*

**Juan E. Gilbert**,  *Andrew Banks Family Preeminence Endowed Professor, Computer & Information Science, University of Florida*

**J. Alex Halderman**, *Bredt Family Professor of Computer Science & Engineering, University of Michigan*

**David Jefferson**, *Lawrence Livermore National Laboratory (retired)*

**Douglas W. Jones**, *Emeritus Associate Professor of Computer Science, University of Iowa*

**Daniel Lopresti**, *Professor of Computer Science and Engineering, Lehigh University*

**Ronald L. Rivest**, *Institute Professor, MIT*

**Bruce Schneier**, *Fellow and Lecturer at the Harvard Kennedy School, and at the Munk School at the University of Toronto*

**Kevin Skoglund**, *President and Chief Technologist, Citizens for Better Elections*

**Barbara Simons**, *IBM Research (retired)*

**Michael A. Specter**, *Assistant Professor, Georgia Tech*

**Philip B. Stark**,  *Distinguished Professor,  Department of Statistics, University of California*

**Gary Tan**, *Professor of Computer Science & Engineering, The Pennsylvania State University*

**Vanessa Teague**, *Thinking Cybersecurity Pty Ltd and the Australian National Universit*y

**Poorvi L. Vora**, *Professor of Computer Science, George Washington University*