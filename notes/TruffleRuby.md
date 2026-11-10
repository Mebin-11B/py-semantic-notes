---
title: "TruffleRuby"
url: https://chrisseaton.com/truffleruby/
clipped: 2026-06-17 01:24:28
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [TruffleRuby](https://chrisseaton.com/truffleruby/)

## Digest Summary
The page catalogs scholarly works on TruffleRuby and related runtime technologies, listing authors, titles, venues, years, and PDF links. Core research topics include:

- Parallelization of dynamic languages and synchronization of built‑in collections (OOPSLA 2018).  
- Debugging native extensions for dynamic languages (ManLang 2018).  
- Rope specialization for Ruby strings (ManLang 2018).  
- Fast, flexible polyglot instrumentation for debuggers and tools (Programming 2018).  
- Cross‑language interoperability in multi‑language runtimes (TOPLAS 2018).  
- Practical partial evaluation to boost dynamic language performance (PLDI 2017).  
- Efficient, thread‑safe object representations for dynamically‑typed languages (OOPSLA 2016).  
- AST specialization and partial evaluation for high‑performance metaprogramming (META 2016).  
- PhD thesis on dynamic techniques for implementing Ruby (Manchester 2015).  
- Call‑target‑specific method arguments and guest‑language safepoints (ICOOOLPS 2015).  
- Zero‑overhead metaprogramming via reflection and MOP (PLDI 2015).  
- Modular composition of languages supporting C extensions (Modularity 2015).  
- Object storage model for the Truffle framework (PPPJ 2014).  
- “Debugging at full speed” for dynamic languages (DYLA 2014).

These publications collectively address performance optimization, tooling, interoperability, and language implementation strategies within the TruffleRuby ecosystem.

## Discussion Summary
The remarks express a unified tone of sorrow and condolence regarding the passing of Chris Seaton, highlighting that a speaker had met him shortly before his death at a conference. The comments characterize the event as a tragic loss, convey personal grief, and collectively extend wishes for his peace, reflecting a respectful and mournful sentiment toward his memory.

---

## Full Article

This page links to the literature and code related to the project. Note that any
views expressed are my own and not those of Oracle.

* B. Daloze, A. Tal, S. Marr, H. Mössenböck, E. Petrank. [Parallelization of Dynamic Languages: Synchronizing Built-in Collections](http://ssw.jku.at/General/Staff/Daloze/thread-safe-collections.pdf). In Proceedings of the Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA), 2018.
  [PDF](http://ssw.jku.at/General/Staff/Daloze/thread-safe-collections.pdf)
* J. Kreindl, M. Rigger, and H. Mössenböck. [Debugging Native Extensions of Dynamic Languages](https://arxiv.org/pdf/1808.00823.pdf). In Proceedings of 15th International Conference on Managed Languages & Runtimes (ManLang), 2018.
  [PDF](https://arxiv.org/pdf/1808.00823.pdf)
* K. Menard, C. Seaton, and B. Daloze. [Specializing Ropes for Ruby](https://chrisseaton.com/truffleruby/ropes-manlang.pdf). In Proceedings of 15th International Conference on Managed Languages & Runtimes (ManLang), 2018.  

  [PDF](https://chrisseaton.com/truffleruby/ropes-manlang.pdf)
* M. Van De Vanter, C. Seaton, M. Haupt, C. Humer, and T. Würthinger. [Fast, Flexible, Polyglot Instrumentation Support for Debuggers and other Tools](https://chrisseaton.com/truffleruby/fastflexible/fastflexible.pdf). In The Art, Science, and Engineering of Programming, Vol. 2, No. 3, 2018.  

  [PDF](https://chrisseaton.com/truffleruby/fastflexible/fastflexible.pdf)
* M. Grimmer, R. Schatz, C. Seaton, T. Würthinger, M. Luján. [Cross-Language Interoperability in a Multi-Language Runtime](https://chrisseaton.com/truffleruby/cross-language-interop.pdf). In ACM Transactions on Programming Languages and Systems (TOPLAS), Vol. 40, No. 2, 2018.  

  [PDF](https://chrisseaton.com/truffleruby/cross-language-interop.pdf)
* T. Würthinger, C. Wimmer, C. Humer, A. Wöss, L. Stadler, C. Seaton, G. Duboscq, D. Simon, M. Grimmer. [Practical Partial Evaluation for High-Performance Dynamic Language Runtimes](https://chrisseaton.com/truffleruby/pldi17-truffle/pldi17-truffle.pdf). In Proceedings of the Conference on Programming Language Design and Implementation (PLDI), 2017.  

  [PDF](https://chrisseaton.com/truffleruby/pldi17-truffle/pldi17-truffle.pdf)
* B. Daloze, S. Marr, D. Bonetta, H. Mössenböck. [Efficient and Thread-Safe Objects for Dynamically-Typed Languages](http://ssw.jku.at/General/Staff/Daloze/thread-safe-objects.pdf). In Proceedings of the ACM International Conference on Object Oriented Programming Systems Languages and Applications (OOPSLA), 2016.  

  [PDF](http://ssw.jku.at/General/Staff/Daloze/thread-safe-objects.pdf)
* C. Seaton. [AST Specialisation and Partial Evaluation for Easy High-Performance Metaprogramming](https://chrisseaton.com/truffleruby/meta16/meta16-ruby.pdf). In Proceedings of the 1st Workshop on Meta-Programming Techniques and Reflection (META), 2016.  

  [PDF](https://chrisseaton.com/truffleruby/meta16/meta16-ruby.pdf),
  [Slides](https://chrisseaton.com/truffleruby/meta16/meta16-ruby-slides.pdf)
* C. Seaton. [Specialising Dynamic Techniques for Implementing the Ruby Programming Language](https://chrisseaton.com/phd). PhD thesis, University of Manchester, 2015.  

  [Abstract](https://chrisseaton.com/phd),
  [PDF](https://chrisseaton.com/phd/specialising-ruby.pdf)
* M. Grimmer, C. Seaton, R. Schatz, T. Würthinger, H. Mössenböck. [High-Performance Cross-Language Interoperability in a Multi-Language Runtime](https://chrisseaton.com/truffleruby/dls15-interop/dls15-interop.pdf). In Proceedings of 11th Dynamic Languages Symposium (DLS), 2015.  

  [PDF](https://chrisseaton.com/truffleruby/dls15-interop/dls15-interop.pdf)
* F. Niephaus, M. Springer, T. Felgentreff, T. Pape, R. Hirschfeld. [Call-target-specific Method Arguments](https://raw.githubusercontent.com/HPI-SWA-Lab/TargetSpecific-ICOOOLPS/gh-pages/call_target_specific_method_arguments.pdf). In Proceedings of the 10th Implementation, Compilation, Optimization of Object-Oriented Languages, Programs and Systems Workshop (ICOOOLPS), 2015.  

  [PDF](https://raw.githubusercontent.com/HPI-SWA-Lab/TargetSpecific-ICOOOLPS/gh-pages/call_target_specific_method_arguments.pdf)
* B. Daloze, C. Seaton, D. Bonetta, H. Mössenböck. [Techniques and Applications for Guest-Language Safepoints](https://chrisseaton.com/truffleruby/icooolps15-safepoints/safepoints.pdf). In Proceedings of the 10th Implementation, Compilation, Optimization of Object-Oriented Languages, Programs and Systems Workshop (ICOOOLPS), 2015.  

  [PDF](https://chrisseaton.com/truffleruby/icooolps15-safepoints/safepoints.pdf)
* S. Marr, C. Seaton, S. Ducasse. [Zero-Overhead Metaprogramming: Reflection and Metaobject Protocols Fast and without Compromises](https://chrisseaton.com/truffleruby/pldi15-metaprogramming/pldi15-marr-et-al-zero-overhead-metaprogramming.pdf). In Proceedings of the 36th Conference on Programming Language Design and Implementation (PLDI), 2015.  

  [PDF](https://chrisseaton.com/truffleruby/pldi15-metaprogramming/pldi15-marr-et-al-zero-overhead-metaprogramming.pdf)
* M. Grimmer, C. Seaton, T. Würthinger, H. Mössenböck. [Dynamically Composing Languages in a Modular Way: Supporting C Extensions for Dynamic Languages](https://chrisseaton.com/truffleruby/modularity15/rubyextensions.pdf). In Proceedings of the 14th International Conference on Modularity, 2015.  

  [PDF](https://chrisseaton.com/truffleruby/modularity15/rubyextensions.pdf),
* A. Wöß, C. Wirth, D. Bonetta, C. Seaton, C. Humer, and H. Mössenböck. [An object storage model for the Truffle language implementation framework](https://chrisseaton.com/truffleruby/pppj14-om/pppj14-om.pdf). In Proceedings of the International Conference on Principles and Practices of Programming on the Java Platform (PPPJ), 2014.  

  [PDF](https://chrisseaton.com/truffleruby/pppj14-om/pppj14-om.pdf)
* C. Seaton, M. L. Van De Vanter, and M. Haupt. [Debugging at full speed](https://www.cristal.univ-lille.fr/dyla14/papers/dyla14-3-Debugging_at_Full_Speed.pdf). In Proceedings of the 8th Workshop on Dynamic Languages and Applications (DYLA), 2014.  

  [PDF](https://www.cristal.univ-lille.fr/dyla14/papers/dyla14-3-Debugging_at_Full_Speed.pdf),
  [Code](https://web.archive.org/web/20150117042919/https://lafo.ssw.uni-linz.ac.at/truffle/debugging/dyla14-debugging-artifact-0557a4f756d4.tar.gz)