---
title: "Prolog Coding Horror"
url: https://www.metalevel.at/prolog/horror
clipped: 2026-06-17 01:01:11
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Prolog
  - Declarative Programming
  - Constraint Logic Programming
  - Antipatterns
  - CLP(FD)
  - Purity
related:
  - "[[Understanding the Go Runtime The Scheduler]]"
  - "[[Six-decade math puzzle solved by Korean mathematician]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article highlights common Prolog antipatterns like impure constructs, global state, and low-level arithmetic, advocating for pure declarative programming.
>
> **Key points:**
> - Using impure constructs like cuts (`!`), `var/1`, or `is/2` leads to loss of solutions and instantiation errors in general queries.
> - Modifying the global database using `assertz/1` and `retract/1` introduces hidden operational dependencies.
> - Impure I/O (like terminal printing) breaks relational logic and prevents writing automated tests.
> - Utilizing constraint-logic programming (CLP(FD)) constraints like `#>` and `#=` yields relational, fully general programs.
>
> **Concept links:** [[Prolog]], [[Declarative Programming]], [[Constraint Logic Programming]], [[Antipatterns]], [[CLP(FD)]], [[Purity]]
>
> **Suggested connections:**
> - [[Understanding the Go Runtime The Scheduler]] — related low-level computing concepts.
> - [[Six-decade math puzzle solved by Korean mathematician]] — related mathematical logic.
<!-- ai-summary:end -->

# [Prolog Coding Horror](https://www.metalevel.at/prolog/horror)

## Digest Summary
The page critiques common Prolog antipatterns and demonstrates how impurity and outdated constructs hinder declarative programming. Key issues listed are: loss of solutions (incorrect or missing answers), reliance on global state, impure I/O (e.g., `format/2` within predicates), and use of low‑level arithmetic (`is/2`) that forces procedural evaluation. An example, `horror_factorial/2`, uses `is/2` and a cut, causing instantiation errors and limiting query generality. A pure alternative replaces `is/2` with constraint‑logic programming operators (`#>`, `#=`) and omits cuts, yielding a relational factorial that correctly enumerates all solutions (`N=0,1,2,…`). The author concludes that adopting pure, constraint‑based definitions eliminates these “horrors” and restores declarative debugging capabilities.

## Discussion Summary
The comments express enthusiasm for Prolog, highlighting its intellectual appeal and recommending further reading on meta‑interpreters and the four‑port model. There is curiosity about practical, real‑world applications, with some perceiving it as niche or esoteric compared to other languages. A discussion of tolerance for partially correct answers reflects a theoretical openness, while newer “LLM‑augmented” Prolog systems are viewed skeptically, considered imprecise and overhyped. Overall, the sentiment balances appreciation for Prolog’s concepts with cautious doubt about its contemporary extensions.

---

## Full Article

Prolog Coding Horror
====================

  

I seemed to hear the whispered cry, "The horror! The horror!"
  
(Joseph Conrad, *Heart of Darkness*)

  
  


Why are you here?
-----------------

As a Prolog programmer, you likely have a rebellious streak
in you. In many cases, this is what it takes to guide you
away from how an entire industry currently tries to solve
problems. To focus on what lies *beyond*.
  
  
The point of this page is to show you where following this streak
is likely *not* a good idea because the cost
is high, and there is no benefit to it.
  
  
A small number of rules suffices to write great
Prolog code. Breaking them will result in programs that are
defective in one or more ways.
  
  

|  |  |
| --- | --- |
| *Video*: | [Prolog Antipatterns](https://www.metalevel.at/prolog/videos/antipatterns) |

The horror: Losing solutions
----------------------------

A Prolog program that *terminates* and is acceptably
efficient can be *defective* in two major ways:

1. It reports *wrong* answers.
2. It *fails to report* intended solutions.

Which of these cases is worse? Think about this!
  
  
Suppose a program is defective *only* in the first way. Is
there anything you can do to still obtain only correct results?
Then, suppose a program is defective *only* in the second
way. What are your options to somehow still obtain all solutions
that were intended?
  
  
The primary means to make your programs defective in
the *second* way is to use *impure*
and *non-monotonic* language constructs. Examples of this
are !/0, (->)/2 and var/1. A
declarative way out is to use [clean](https://www.metalevel.at/prolog/data#clean)
data structures, *constraints*
like [dif/2](https://www.metalevel.at/prolog/concepts#builtins), and
meta-predicates
like [**if\_/3**](https://www.metalevel.at/prolog/metapredicates#if_3).

The horror: Global state
------------------------

As a beginner, you will be tempted to modify
the [global database](https://www.metalevel.at/prolog/global) in Prolog. This
introduces *implicit dependencies* within your programs.
By "implicit", I mean that there is nothing in your program
that *enforces* these dependencies. For example, if you use
such predicates in a different order than intended, they may
unexpectedly fail or yield strange results.
  
  
The primary means to make your programs defective in this way is
to use predicates like assertz/1
and retract/1. A declarative way out is to use
predicate *arguments*
or [semicontext notation](https://www.metalevel.at/prolog/dcg#semicontext) to
thread the state through.

The horror: Impure output
-------------------------

As a beginner, you will sometimes be tempted to *print*
answers on the system terminal instead of letting the toplevel
report them. For example, your programs may contain code
like this:

```
solve :-
        solution(S),
        format("the solution is: ~q\n", [S]).
```

A major drawback of this approach is that *you cannot easily
reason about such output*, since it only occurs on the system
terminal and is not available as a Prolog term within your
program. Therefore, you will not write test cases for such output,
increasing the likelihood of introducing changes that break such
predicates. Another severe shortcoming is that this prevents you
to use the code as a true *relation*.
  
  
To benefit from the full generality of relations, *describe*
a solution with Prolog code, and *let the toplevel do the
printing*:

```
solution(S) :-
        constraint_1(S),
        etc.
```

Sometimes, you may want special formatting. In such case, you can
still describe the output in a pure way, using for example the
nonterminal [**format\_//2**](https://www.metalevel.at/prolog/dcg#output).
This makes test cases easy to write.

The horror: Low-level language constructs
-----------------------------------------

Some Prolog programmers may see little reason to use more recent
language constructs. For example, CLP(FD) constraints have only
been widely available for about 20 years, which is
a *comparatively* recent development for Prolog. If you
think that low-level constructs have served you well, why bother
learning newer material? The fact that millions of students
were *not* well served by lower-level constructs need not
concern you.
  
  
Unfortunately, sticking to low-level constructs comes at a high
price: It makes the language harder to teach, harder to learn and
harder to understand than necessary. It requires students to learn
declarative and operational semantics essentially *at the same
time*, which is too much at once in almost all cases.
  
  
The primary means to make Prolog harder to teach than necessary is
to introduce beginners to low-level predicates for arithmetic
like (is)/2, (=:=)/2 and (>)/2. A
declarative way out is to *teach constraints
instead*. See [**declarative integer
arithmetic**](https://www.metalevel.at/prolog/clpfd).

Horror factorial
----------------

To see some of these defects exemplified, behold the ***horror
factorial***:

```
horror_factorial(0, 1) :- !.
horror_factorial(N, F) :-
        N > 0,
        N1 is N - 1,
        horror_factorial(N1, F1),
        F is N*F1.
```

Observe the horror of *losing solutions* when posting
the [most general query](https://www.metalevel.at/prolog/concepts#toplevel):

```
?- horror_factorial(N, F).
   N = 0, F = 1.
```

The version without !/0 is almost as horrendous:

```
horror_factorial(0, 1).
horror_factorial(N, F) :-
        N > 0,
        N1 is N - 1,
        horror_factorial(N1, F1),
        F is N*F1.
```

The horror of low-level language constructs prevails:

```
?- horror_factorial(N, F).
   N = 0, F = 1
;  caught: error(instantiation_error,'(is)'/2)
```

If you accept this, you are

* limited by using outdated language constructs.
* mistaking relations for functions.
* not caring about the most general query.
* preventing [declarative debugging](https://www.metalevel.at/prolog/debugging) by using impure constructs.

A way out: Purity
-----------------

To stop the horror, stay in the [pure](https://www.metalevel.at/prolog/purity)
monotonic subset of Prolog.
  
  
Start small. For example, instead of low-level integer arithmetic,
use a more declarative alternative:

```
horror_factorial(0, 1) :- !.
horror_factorial(N, F) :-
        N #> 0,
        N1 #= N - 1,
        horror_factorial(N1, F1),
        F #= N*F1.
```

Still better than nothing. Then, remove the !/0:

```
n_factorial(0, 1).
n_factorial(N, F) :-
        N #> 0,
        N1 #= N - 1,
        n_factorial(N1, F1),
        F #= N*F1.
```

This version also works for the *most general* query:

```
?- n_factorial(N, F).
   N = 0, F = 1
;  N = 1, F = 1
;  N = 2, F = 2
;  N = 3, F = 6
;  ... .
```

That's quite good: A few simple changes have led to a quite
general logic program.

Conclusion
----------

In summary, I recommend you *rebel where it makes sense*,
and *only* there.
  
  
It is ill-directed rebellion to cling to outdated features, for
life is not lived backwards nor tarries in yesterday.
  
  
Use declarative constructs in your Prolog programs to make them
more general while retaining acceptable performance.
  
  
  
**[More about Prolog](https://www.metalevel.at/prolog)**
  
  
  
**[Main page](https://www.metalevel.at/)**