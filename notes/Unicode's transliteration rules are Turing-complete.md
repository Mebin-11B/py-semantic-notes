---
title: "Unicode's transliteration rules are Turing-complete"
url: https://seriot.ch/computation/uts35/
clipped: 2026-08-31 12:22:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Unicode's transliteration rules are Turing-complete](https://seriot.ch/computation/uts35/)

## Digest Summary
Unicode UTS #35 transliteration rules, as implemented in ICU, support unbounded rewriting with optional contexts, captures, quantifiers, and a cursor that can reposition after each replacement. By compiling a universal 2‑tag system into such rules, the author shows that a single rule file can simulate any Turing‑complete computation; the example encodes Liesbeth De Mol’s 2‑tag system for the Collatz function, demonstrating step‑by‑step transformation of unary strings. The construction guarantees at most one matching rule per step, halting exactly when the underlying tag system halts, establishing undecidability of termination for arbitrary rule sets. ICU imposes a pragmatic guard of 16 rewrites per input code point, though the specification itself imposes no limit. Beyond tag systems, the same mechanism implements Rule 110 (14 rules) and Wolfram’s prime‑generating cellular automaton (223 rules). Consequently, transliteration rule files are effectively programs, and accepting external rule data entails executing code, necessitating review and runtime bounds. Supporting files (collatz.txt, rule110.txt, primes.txt, uts35.py/.sh) illustrate these capabilities.

---

## Full Article

### Nicolas Seriot

#### [Computation](https://seriot.ch/computation/) > Unicode's Transliteration Rules Are Turing-Complete

# ð¦ Unicode's Transliteration Rules Are Turing-Complete

July 2026

- Hacker News [discussion](https://news.ycombinator.com/item?id=48829797)

- Reddit [discussion](https://www.reddit.com/r/programming/comments/1uqny65/unicodes_transliteration_rules_are_turingcomplete/)

See also: [Jira is Turing-Complete](https://seriot.ch/computation/jira.html)

Claim: As specified, the UTS #35 transliteration-rule language is
Turing-complete. An exception within Unicode, whose core algorithms are
deliberately bounded and always terminate. The specification defines a
revisiting cursor and no rewrite limit. The per-call cap that keeps every
call bounded is ICU's addition, not the spec's.

Table of Contents

- [Transliteration Rules](https://seriot.ch/computation/uts35/#1)

- [Proof: 2-Tag Systems](https://seriot.ch/computation/uts35/#2)

- [The Collatz Function](https://seriot.ch/computation/uts35/#3)

- [Correctness and Universality](https://seriot.ch/computation/uts35/#4)

- [ICU's Rewrite Guard](https://seriot.ch/computation/uts35/#5)

- [Demonstration: Rule 110](https://seriot.ch/computation/uts35/#6)

- [Demonstration: Prime Numbers Generator](https://seriot.ch/computation/uts35/#7)

- [Note on Security](https://seriot.ch/computation/uts35/#8)

- [Conclusion](https://seriot.ch/computation/uts35/#9)

- [Appendix: Files](https://seriot.ch/computation/uts35/#10)

I've been wondering for a while whether Unicode allows universal computation. The core Unicode algorithms (normalization, casing, bidi, collation) are deliberately bounded, but [UTS #35 transliteration rules](https://www.unicode.org/reports/tr35/tr35-general.html#Transforms), under their natural unbounded semantics, are not. This is a result I haven't found published before.

These rules ship as [locale data](https://github.com/unicode-org/cldr/tree/main/common/transforms) in [ICU](https://icu.unicode.org/), the Unicode library shipped in operating systems, browsers, runtimes, and databases. Whether a given rule file terminates on a given input is [undecidable](https://en.wikipedia.org/wiki/Halting_problem).

###  1. Transliteration Rules

A transliterator typically turns "Ã©" into "e", using a list of ordered [rewrite rules](https://www.unicode.org/reports/tr35/tr35-general.html#Conversion_Rules):
 ` `L { x } R > y ;
` ` 

The substring  `x`  is replaced by  `y`  when it sits between (optional) contexts  `L`  and  `R` . The [revisiting](https://www.unicode.org/reports/tr35/tr35-general.html#Revisiting) feature allows  `|`  in the replacement, which places the cursor inside the new text so that newly written material can trigger further rules.

Example:
 ` `x > y | z ;
za > w ;
` ` 

 `xa`  rewrites to  `y|za`  (cursor before  `z` ). The engine rescans and  `za`  matches, producing  `yw` .

Using the Python [PyICU](https://pypi.org/project/pyicu/) module:
 ` `from icu import Transliterator as T
t = T.createFromRules("", "x > y|z; za > w;")
print(t.transliterate("xa")) # yw
` ` 

Here is an excerpt of the [Latin-Katakana](https://github.com/unicode-org/cldr/blob/main/common/transforms/Latin-Katakana.xml#L126-L127) transform. Before  `i`  or  `e` ,  `c`  rewrites to  `s`  and the cursor backs up so the  `s`  rules re-fire. Same revisiting trick as above, shipped in production locale data.
 ` `c } i â | s ;
c } e â | s ;
` ` 

###  2. Proof: 2-Tag Systems Compilation

To prove UTS #35 universality, we compile [2-tag systems](https://en.wikipedia.org/wiki/Tag_system) ([Post, 1943](https://archive.org/details/sim_american-journal-of-mathematics_1943-04_65_2/page/n3/mode/2up)), a model proven universal ([Cocke & Minsky, 1964](https://dl.acm.org/doi/10.1145/321203.321206)), into transliteration rules.

A 2-tag system has one production per letter. Each step removes the first two letters and appends the production of the first one. It halts when fewer than two letters remain. 

###  3. The Collatz Function

Our example is [Liesbeth De Mol](https://doi.org/10.1016/j.tcs.2007.10.020)'s 2-tag system for the [Collatz](https://en.wikipedia.org/wiki/Collatz_conjecture) function (even n â n/2, odd n â (3n+1)/2):  `a â bc` ,  `b â a` ,  `c â aaa` , on the unary word  `aaa...a` . We prefix the word with a read marker  `M` , which pins the machine to the front. When no rule matches at  `M` , no rule matches anywhere.

The construction uses one rule per letter:
 ` `M a [abc] ([abc]*) > | M $1 b c ;
M b [abc] ([abc]*) > | M $1 a ;
M c [abc] ([abc]*) > | M $1 a a a ;
` ` 

The first rule matches the marker, the letter  `a` , one more letter, then captures everything else. The replacement writes the next configuration and puts the cursor back before the marker so the next step fires immediately.

The character class, the capturing group and  `$1` , the quantifier and the cursor are standard rule syntax (the spec's [Transform Syntax Characters](https://www.unicode.org/reports/tr35/tr35-general.html#Transform_Syntax_Characters) table).

You can run this machine with [uts35.py](https://seriot.ch/computation/uts35/uts35.py) â [collatz.txt](https://seriot.ch/computation/uts35/collatz.txt) is the rules above with the  `|`  deleted, so each pass performs exactly one tag step. From  `aaa` , the run replicates the worked example on the Wikipedia [tag system](https://en.wikipedia.org/wiki/Tag_system) page ( `aaa` ,  `abc` ,  `cbc` ,  `caaa` ,  `aaaaa` , ...) with the values appearing as runs of  `a` s. The same rules also run with no Python at all, through ICU's stock  `uconv`  ([uts35.sh](https://seriot.ch/computation/uts35/uts35.sh)).
 ` `% python3 uts35.py collatz.txt aaa
ICU 78.3
  0 - Maaa         # 3
  1 - Mabc
  2 - Mcbc
  3 - Mcaaa
  4 - Maaaaa       # 5
  5 - Maaabc
  6 - Mabcbc
  7 - Mcbcbc
  8 - Mcbcaaa
  9 - Mcaaaaaa
 10 - Maaaaaaaa    # 8
 11 - Maaaaaabc
 12 - Maaaabcbc
 13 - Maabcbcbc
 14 - Mbcbcbcbc
 15 - Mbcbcbca
 16 - Mbcbcaa
 17 - Mbcaaa
 18 - Maaaa        # 4
 19 - Maabc
 20 - Mbcbc
 21 - Mbca
 22 - Maa          # 2
 23 - Mbc
 24 - Ma           # 1
` ` 

###  4. Correctness and Universality

- At most one rule matches. There is exactly one marker. The letter after it selects the rule.  `([abc]*)`  captures all remaining letters.

- One rewrite is exactly one tag step. The rule for letter  `x`  matches precisely when the marker faces  `x`  plus at least one more letter. The replacement constructs the next configuration.

- Halting corresponds. Every rule requires two letters after the marker, so  `Ma`  and  `M`  are fixed points. The transform terminates exactly when the tag system halts.

Together, by induction: after k rewrites the string is exactly  `M`  followed by the tag system's word after k steps, and the transform reaches a fixed point exactly when the tag system halts. Nothing here is specific to Collatz. One rule per letter compiles any 2-tag system with alphabet Î£ and productions P:
 ` `M x [Î£] ([Î£]*) > | M $1 P(x) ;
` ` 

A universal 2-tag system therefore yields a fixed rule file that simulates any Turing machine, with the machine and its input encoded in the initial word.

###  5. ICU's Rewrite Guard

ICU stops each  `transliterate()`  call after 16 rewrites per input UTF-16 code unit ( `loopLimit = span << 4`  in [rbt.cpp](https://github.com/unicode-org/icu/blob/main/icu4c/source/i18n/rbt.cpp); the Java port has the [same guard](https://github.com/unicode-org/icu/blob/main/icu4j/main/translit/src/main/java/com/ibm/icu/text/RuleBasedTransliterator.java)). However, the specification itself defines no limit. The guard is ICU's pragmatic addition to keep every call bounded. Here, each rewrite is a full tag step, so the guard can only interrupt between steps â calling  `transliterate()`  repeatedly until the string stops changing loses nothing. (For these machines an unchanged string means no rule matched; in general a nonhalting system can cycle back to the same string, so equality alone is not a halting test.)

###  6. Demonstration: Rule 110

The reduction above establishes universality. The constructions in this section and the next are not part of the main proof; they show the language is comfortably programmable beyond the minimal encoding.

The rule language is not limited to tag systems. [rule110.txt](https://seriot.ch/computation/uts35/rule110.txt) implements the [Rule 110](https://en.wikipedia.org/wiki/Rule_110) cellular automaton in 14 rules. Cells are written  `.`  (0) and  `*`  (1). A head carries the previous two cells and rewrites each cell in place. One pass is one generation; each generation consumes one fuel cell  `g` , leaving an  `s` , and the run halts by itself when the fuel is out.

Rule 110 is itself proven universal ([Cook, 2004](https://www.complex-systems.com/abstracts/v15_i01_a01/)), so the update rule implemented here is, in principle, all the computational power one needs â but this fuel-bounded program runs a prescribed number of generations, so it is a demonstration, not a second proof.
 ` `python3 uts35.py rule110.txt "ggggggggg*"
ICU 78.3
  0 - Mggggggggg*
  1 - Mggggggggs**.
  2 - Mgggggggss***..
  3 - Mggggggsss**.*...
  4 - Mgggggssss*****....
  5 - Mggggsssss**...*.....
  6 - Mgggssssss***..**......
  7 - Mggsssssss**.*.***.......
  8 - Mgssssssss*******.*........
  9 - Msssssssss**.....***.........
` ` 

###  7. Demonstration: Prime Numbers Generator

[primes.txt](https://seriot.ch/computation/uts35/primes.txt) is Wolfram's real-time prime-generating cellular automaton (A New Kind of Science, [p. 640](https://www.wolframscience.com/nks/p640--computations-in-cellular-automata/)); 16 states ( `0` - `f` ) and 223 transform rules. The input word is the fuel followed by the automaton's initial configuration,  `0a048` . The first cell after the fuel is  `0`  exactly at prime ticks (t > 1).
 ` `% python3 uts35.py primes.txt gggggggggggg0a048
ICU 78.3
  0 - Mgggggggggggg0a048
  1 - Mgggggggggggs9604d7
  2 - Mggggggggggss06f5d80
  3 - Mgggggggggsss0ad3d870
  4 - Mggggggggssss96fc0d700
  5 - Mgggggggsssss0adb008000
  6 - Mggggggssssss96fad087000
  7 - Mgggggsssssss0a960f870000
  8 - Mggggssssssss9af6f01700000
  9 - Mgggsssssssss9adad018000000
 10 - Mggssssssssss96f60f187000000
 11 - Mgsssssssssss0a06f02870000000
 12 - Mssssssssssss96fad02d700000000
` ` 

###  8. Note on Security

This is a result about computability, not a security disclosure. None of it makes ordinary Unicode text executable: stock ICU caps every  `transliterate()`  call at 16 rewrites per code point, so a single call always returns. What is universal here is a custom rule file driven under unbounded re-invocation.

The surface is therefore narrow. Accepting a rule file from an untrusted source is accepting an untrusted program. The risk is nontermination and resource exhaustion. ICU's per-call guard already contains the nontermination, though a single bounded call can still be costly. Reimplementations, however, do not always carry the guard over: ICU4X's experimental Rust [transliterator](https://github.com/unicode-org/icu4x/blob/main/components/experimental/src/transliterate/transliterator/mod.rs) and Twitter's Ruby [twitter-cldr](https://github.com/twitter/twitter-cldr-rb/blob/master/lib/twitter_cldr/transforms/conversion_rule_set.rb) both implement the revisiting cursor and iterate with no rewrite bound.

###  9. Conclusion

Transliteration rules were designed to turn "Ã©" into "e". Three lines of them can compute the Collatz function.

Unbounded rewriting with a revisiting cursor is an old recipe for universality. The surprise is that it lives in one corner of the Unicode specification, whose core algorithms are all deliberately bounded, and which never mentions the possibility.

###  10. Appendix: Files

- [collatz.txt](https://seriot.ch/computation/uts35/collatz.txt) â the three-rule Collatz machine (one tag step per pass)

- [rule110.txt](https://seriot.ch/computation/uts35/rule110.txt) â Rule 110 in 14 rules

- [primes.txt](https://seriot.ch/computation/uts35/primes.txt) â Wolfram's prime-generating cellular automaton in 223 rules

- [uts35.py](https://seriot.ch/computation/uts35/uts35.py) â runner, PyICU

- [uts35.sh](https://seriot.ch/computation/uts35/uts35.sh) â runner, ICU's stock  `uconv` , no Python

- [test.sh](https://seriot.ch/computation/uts35/test.sh) â self checks

Environment: ICU 78.3, PyICU 2.16.2, macOS; also verified with ICU 72.1 on Debian 12; July 2026
