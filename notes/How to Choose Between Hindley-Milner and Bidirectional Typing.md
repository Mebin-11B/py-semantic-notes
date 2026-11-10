---
title: "How to Choose Between Hindley-Milner and Bidirectional Typing"
url: https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/
clipped: 2026-06-17 01:43:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-20
summary_status: done
concepts:
  - type systems
  - type inference
  - bidirectional typing
related:
  - "[[Type Systems]]"
  - "[[Type Inference]]"
  - "[[Bidirectional Typing]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article explains that choosing between Hindley-Milner and bidirectional typing is a false dichotomy because bidirectional typing is a superset of Hindley-Milner that can easily incorporate unification to support generics.
>
> **Key points:**
> - Language developers often view Hindley-Milner and bidirectional typing as mutually exclusive alternatives, which is a false dichotomy.
> - The real decision point is whether the language needs generics, which require a type system with unification to assign and solve type variables.
> - Bidirectional typing can be implemented as a superset of Hindley-Milner by adding a `check` function to an `infer` routine, enabling unification alongside type checking.
> - For learning projects or Domain Specific Languages (DSLs) where generics are unnecessary, a pure bidirectional system with type annotations (and no unification) can significantly reduce complexity.
>
> **Concept links:** [[Type Systems]], [[Type Inference]], [[Hindley-Milner]], [[Bidirectional Typing]], [[Generics]], [[Unification]]
>
> **Suggested connections:**
> - [[Type Systems]] — analysis of different type checking architectures and their implementation details.
> - [[Hindley-Milner]] — traditional algorithm for type inference with let-polymorphism.
> - [[Bidirectional Typing]] — details on how local type information propagation simplifies inference.
<!-- ai-summary:end -->

# [How to Choose Between Hindley-Milner and Bidirectional Typing](https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/)

## Digest Summary
The post argues that choosing between Hindley‑Milner (HM) and bidirectional typing is a false dichotomy; the core decision should be whether the language needs generics. Generics require unification, which is central to HM and can be incorporated into a bidirectional system. Bidirectional typing, by adding a `check` function to an `infer` routine, can support unification and thus all HM features, while also allowing annotations to guide inference and reduce reliance on type variables. Implementing bidirectional typing is shown with simple Rust‑like pseudocode: `infer` returns a type, and `check` either compares for equality or invokes `unify`. The author notes that unification adds complexity but is essential for general‑purpose languages that want type inference without explicit annotations. For learning projects, DSLs, or languages where generics are unnecessary, a pure bidirectional approach with annotations may suffice. In all cases, bidirectional typing can accommodate generics if needed.

## Discussion Summary
The comment recommends replacing a Hindley‑Milner style type system with a compositional type system, arguing that the latter provides significantly clearer explanations of type derivations and error messages. It points to an external presentation that details the compositional approach, suggesting that its structure improves understandability of typing behavior compared with traditional HM inference.

---

## Full Article

This question is common enough you’ve probably heard it posed countless times:
“Should my new programming language use a Hindley-Milner (HM) type system or a Bidirectional (Bidir) one?”
What’s that?
I need to understand friends don’t just bring up type inference in casual conversation?

OK, ouch, fair enough.
But…whatever.
This is my blog.
We’re doing it anyway!
I don’t know what you expected when you clicked on a programming languages blog.

Picking a type system is a real barrier for would be language developers.
Eyes full of trepidation as they navigate the labyrinth of nuanced choice that goes into everything a programming language asks of them.
Which type system to choose is just another quandary in the quagmire as they trudge towards a working prototype.

Its understandable they’d want to make a quick decision and return to marching.
But this is the wrong question to ask.
The question presumes that HM and Bidir are two ends of a spectrum.
On one end you have HM with type variables and unification and all that jazz.
On the other end you have bidirectional typing where annotations decide your types and little inference is involved.
This spectrum, however, is a false dichotomy.

What folks should actually be asking is “Does my language need generics?”.
This question frames the problem around what your language needs, rather than an arbitrary choice between two algorithms of abstract tradeoffs.
Perhaps more importantly, it determines if you’ll need unification or not.

Generics, generally, require a type system that supports unification.
Unification is the process of assigning and solving type variables.
If you’ve ever seen Rust infer a type like `Vec<T>`, that’s unification chugging along.

Note

We don’t have time today. But if you’re interested in how unification works, I have a

[tutorial about it](https://thunderseethe.dev/posts/unification)

.

When facing down designing a type system, knowing if you need unification or not decides a lot for you.
Unification sits center stage in Hindley-Milner.
When you pick HM you pick unification.

The story is more interesting for bidirectional typing.
If you look to the literature, you’ll find plenty of example of bidirectional typing without a unification in sight.
By introducing annotations at key locations, you can type check sophisticated programs with no type variables.
A key insight of bidirectional type is how much you can do without unification.
And don’t get me wrong; it is cool how much it can do.

But this leads to the incorrect perception that bidir *can’t* or *shouldn’t* use unification.
The opposite couldn’t be more true.
Bidirectional typing supports all the same features as HM typing, and more, forming more of a superset relationship.
Unification slots into bidirectional typing like a vim user slots into home row.

This is because bidirectional typechecking is a superset of HM.
Imagine we have some AST (in Rust):

```
enum Ast {
  // some cases, probably
}
```

And we have a Type we’d like to assign to our AST:

```
enum Type {
  // some more cases, possibly
}
```

With an HM system, we provide an `infer` function:

```
fn infer(env: Env, ast: Ast) -> Result<Type, TypeError> {
  // ... not of particular import right now
}
```

Wow, just like that we have a real actual HM type system.

Tip

Please ignore all the details we’re brushing over.

We can imagine we’re doing all sorts of unification in `infer`.
If we want to make that system bidirectional, it’s just a matter of adding a `check` function:

```
fn check(env: Env, ast: Ast, ty: Type) -> Result<(), TypeError> {
  // ... more important right now
}
```

Technically, `check` doesn’t even have to do anything.
A perfectly valid implementation of check would be:

```
fn check(env: Env, ast: Ast, ty: Type) -> Result<(), TypeError> {
  let infer_ty = infer(env, ast);
  if infer_ty == ty {
    Ok(())
  } else {
    Error(TypeError::TypesNotEqual)
  }
}
```

We infer a type for our AST and check that it’s equal to the expected type.
That’s all it takes to be bidirectional.
However, equality is pretty stringent here.
The first time we check a type like `(T, u32)` against a type like `(u32, S)` our entire type inference grinds to a halt.

Instead, let’s slot unification into the same position.
Rather than requiring strict equality, we can loosen `check` to require that our types unify:

```
fn check(env: Env, ast: Ast, ty: Type) -> Result<(), TypeError> {
  let infer_ty = infer(env, ast);
  unify(infer_ty, ty)
}
```

With that modest adjustment, we’re bidirectional and we’re unifying.
Now, of course, once we’ve done that we’re free to make better use of our `check` whenever we like.
Let’s say we happen to know our AST has functions:

```
enum Ast {
  Fun(String, Box<Ast>),
}
```

And we’re good language developers, so of course that means Type gets a function case as well:

```
enum Type {
  Fun(Box<Type>, Box<Type>),
}
```

We return to our check case and notice that, rather than inferring functions, we can take a little shortcut:

```
fn check(env: Env, ast: Ast, ty: Type) -> Result<(), TypeError> {
  match (ast, ty) {
    (Ast::Fun(var, body), Type::Fun(arg, ret)) => {
       check(env.insert(var, *arg), *body, *ret)
    }
    (ast, ty) => {
      let infer_ty = infer(env, ast);
      unify(infer_ty, ty)
    }
  }
}
```

But the point is we don’t have to.
If you are going to choose a Hindley-Milner type system, you might as well add four lines of code and make it a bidirectional system.
Its free real estate.

Okay so you’re sold on bidirectional typing.
I can see it in your eyes.
Let’s return to our underlying question “should I support generics or not?”.
Unification is a daunting task.
When does it make sense and when does it not?

Unification is great when you don’t want to have to spell out the type of every variable in your program.
It’s even wormed it’s way into older language likes Java and C++ because it’s so handy to not have to spell out types.
Even Go, a diehard in the anti-generics camp, finally capitulated and added generics.
Anyone aiming to make a general purpose programming language should consider generics a must.
But, that’s not every language’s goal.

A lot of people embark on making a programming language as a learning exercise.
In those cases unification can present a bundle of extra complexity that doesn’t really teach you anything about what you want to learn.
If you’re interested in learning about type systems, unification is a must.
But if you just need some types so you can emit code later, that is a great time to look at bidirectional type systems that don’t use unification and require type annotations.

Or perhaps your language isn’t general purpose and you’re after a Domain Specific Language perfectly suited to your niche.
DSLs don’t have to cover all of computation and can eschew generics to reduce surface area and concepts in the language, depending on use case.
With the warning that successful DSLs grow up to become general purpose programming languages, looking at you awk, and then you really hurt for the lack of features.

Regardless of where your aims, the real question you should be asking yourself is “Do I want generics or not?”.
Whatever your answer, bidirectional typing has got you covered.