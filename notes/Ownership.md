---
title: "Ownership"
source: "https://without.boats/blog/ownership/"
author:
published: 2000-06-22
created: 2026-06-01
description:
tags:
  - "clippings"
processed: true
processed_at: 2026-06-01
summary_status: done
concepts:
  - Type Systems
  - Programming Language Design
  - Rust Programming
  - Systems Programming
  - Compilers
related:
  - "Type Systems"
  - "NVlabscuda-oxide cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust..md"
  - "Exceptional engineers.md"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An explainer on how substructural type theory is applied in language design to manage resource ownership, analyzing safety vs. liveness properties, and criticizing Rust's E0509 compiler error.
>
> **Key points:**
> - Explores substructural type systems, clarifying the distinction between normal types, affine types (used at most once, dropping contraction), and linear types (used exactly once, dropping both contraction and weakening).
> - Contrasts safety properties (ensuring bad things like use-after-free don't happen) with liveness properties (ensuring good things like committing or aborting a transaction eventually happen).
> - Critiques Rust's E0509 compiler rule ('cannot move out of type with destructor'), showing how it limits design patterns and forced serde_json into a complex workaround for stack overflow defense.
> - Details the relationship between session types, destructuring, and privacy to enforce liveness guarantees without leaking resources.
> - Outlines the design implications of shared ownership models (like reference counting or garbage collection) and their susceptibility to leaks and reference cycles.
>
> **Concept links:** [[Type Systems]], [[Programming Language Design]], [[Rust Programming]], [[Systems Programming]], [[Compilers]]
>
> **Suggested connections:**
> - [[NVlabscuda-oxide cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust..md]] — connects Rust systems programming and compiler design to advanced type semantics.
> - [[Exceptional engineers.md]] — links first-principles system modeling to the conceptual understanding of programming language design.
<!-- ai-summary:end -->

This post is meant as an explainer about how substructural type theory can be applied in programming language design. Terms like “substructural type theory” tend to scare and confuse programmers who don’t write Haskell on the weekends, so one thing programming language designers should do when thinking about how they will present their language is invent metaphors, even slightly misleading ones, to help more ordinary programmers understand how their language works. One such term is “ownership.”

Not infrequently, objects in a program come to represent something outside of themselves; they are not “pure data” but some kind of resource with identity. A classic example of this might be a sort of handle granting exclusive access to a resource. For this to really work well you want to know that to get that object you had to execute certain code (a “constructor”), that when the object is no longer used some other code will be executed (a “destructor”), and that while the object is in scope, no concurrently executing code also has an object representing the same exclusive resource (that it is not “aliased”). This is what ownership (as presented in Rust, at least) is all about.

I want to demystify ownership and substructural types in the hopes that this will become more common knowledge. Nothing in this post is really groundbreaking - if you’re already “in the know,” it will contain no new information - but it does contain some notes on aspects of Rust’s implementation that I think are incorrect (one of which would even be easy to change).

## Type systems and correctness properties

First, I want to take a step back and examine a more fundamental question. What is a type system for?

Something Graydon Hoare said to me that I like a lot (though I think he was paraphrasing someone else) is that type systems are the parts of formal methods that we’ve figured out how to make easy. That is, a type system is a formal (and hopefully sound) static analysis technique which is automatically applied to your program to verify aspects of its behavior. A valuable distinction has been made in formal analysis between two kinds of properties your program could have:

- **Safety properties,** which are guarantees that “bad things don’t happen” (i.e. your program does not exhibit certain undesirable behavior).
- **Liveness properties,** which are guarantees that “good things do happen” (i.e. your program does exhibit certain desirable behavior).

We usually think of type systems as upholding certain safety properties. For example, if I have a function `fn(String) -> Integer`, the type system will uphold that my program never calls this function with an argument that is not a String (or with two arguments, or zero, etc). But the type system also upholds some liveness properties as well: for example, it upholds that the function *will* return an integer.

However, liveness properties usually have an unfortunate caveat because of the expressiveness of the languages we use. Specifically, almost every widely used programming language is Turing complete, and so we cannot actually guarantee that that function *will* return an integer; it might instead never halt. So liveness properties are usually understood to be caveated that the program will *eventually* do that, where eventually could be indefinitely in the future. Most programming languages also have some ability to abort the program or throw an untyped exception, which is another caveat that has to be made to any guarantee about liveness properties. None of these things are ideal, but that’s the state of the practice right now.

Ownership is a method of extending the type system of a language so that it can be used to establish additional guarantees about safety and liveness properties of programs written in that language, specifically around the number of times a given value will be *used*.

## What are substructural types?

In mathematical logic, there are certain kinds of universal rules that are known as “structural rules” because they are a part of the structure of the logic. There are two in particular that we are interested in learning about today:

- **Weakening** (or “monotonicity of entailment”): If you know that A implies B (`A -> B`), you also know that A and any other fact implies B (e.g. `A, C -> B`). That is, you can ignore unnecessary predicates in a rule.
- **Contraction** (or “idempotency of entailment”): If you know that A multiple times implies B (`A, A -> B`), you also know that A implies B (e.g. `A -> B`). That is, you don’t need multiple of the same predicate in a rule.

You can construct other kinds of logics which don’t include these structural rules. For example, in linear logic, you have neither of these rules: you don’t know that `A, A, C -> B` or `A -> B` just because you know that `A, A -> B`.

It’s also been understood for some time that type theories and mathematical logics have a strong relationship; people who write Haskell on the weekend will talk your ear off about this, this is what they mean when they say “Curry-Howard correspondence.” On this basis, there was some interest in the idea of inventing type systems that also don’t have these structural rules. As it was told to me by Aaron Turon (though I haven’t investigated the history closely), at first this was a purely theoretical effort without any known practical application. However, it has been discovered to be very useful for representing the kinds of objects I’ve described above; those with a meaningful notion of identity.

A “substructural type” is a type which has the equivalent of one or both of these structural rules removed. The way to understand this is that while values of normal types can be used any number of times, values of substructural types are restricted in the number of times they can be used. If the type cannot be “weakened,” it must be used at least once before it goes out of scope. If the type cannot be “contracted,” it cannot be used more than once. Each of these categories of types has a name, which appear in this table:

```fallback
│ WEAKENING? │ CONTRACTION? │ USES
─────────────────┼────────────┼──────────────┼────────────────
                 │            │              │     
    Normal types │ YES        │ YES          │ Any number
                 │            │              │     
    Affine types │ YES        │              │ At most once
                 │            │              │     
  Relevant types │            │ YES          │ At least once
                 │            │              │     
    Linear types │            │              │ Exactly once
```

In current Rust, all types have the law of weakening, but by default types do not have the law of contraction. So most types in Rust are what are called *affine types*, and so they can only be used one or zero times. To use them is to *move* them; not to use them is to *drop* them. This is what we mean by ownership.

Rust also supports normal types, which can be used any number of times; currently these are types that implement `Copy`. As a result, there’s a quirk in Rust in which all normal types must be copyable by executing a memcpy. Other types that would be normal types in other languages implement a trait called `Clone`, which gives them normal type semantics but require you add a call to `clone` any time you want to move them more than once. This is meant to discourage you from performing expensive operations (for example, copying a `String` requires making a new arbitrarily large heap allocation and copying the data to it). However, some memcpys are expensive (large ones) and some non-memcpy copies are cheap (specifically `Rc` and `Arc`). Recently, Niko Matsakis wrote a [post](https://smallcultfollowing.com/babysteps/blog/2024/06/21/claim-auto-and-otherwise/) about changing this so that there isn’t a tight coupling between normal type semantics and memcpy; I think this is a great proposal and I’d like to see this aspect of Rust change.

Returning to the subject of safety and liveness properties, I want to point of what ownership has actually bought us. First, it has bought us a guarantee that the value is not aliased anywhere else in the program. This enables us to mutate it while still enforcing the safety property that we do not have [mutable, aliased state](https://without.boats/blog/references-are-like-jumps). This is a critical feature for Rust’s memory safety and freedom from data races and for making local reasoning tractable.

Also, because the value is known not to be aliased, when it goes out of scope we know we can run its destructor; we can close the file, unlock the mutex, so on. Languages without ownership cannot make this kind of guarantee, because the value could be aliased somewhere else. Some languages have implemented bad, incomplete solutions to this problem (like Python’s `with`), and while they help reduce the number of errors programmers encounter, they don’t entirely solve the issue. For example, it’s still possible in Python for a file opened with a `with` block to escape the with block, because nothing stops you from assigning it to a variable outside of that block.

## Linear types and session types

Rust may have affine types, but it currently doesn’t have types which cannot be weakened; that is, types which must be used at least once. There’s a lot of interest in specifically *linear types*, types which must be used exactly once. This term has been misused by some contributors to the Rust project to a refer to a different idea around leaks (which I’ll return to in the later section of this post on shared ownership), but it has also been used to refer to adding proper linear types to the language, which have also been called “must move” types or “undroppable” types.

Adding linear types to Rust now would be no mean feat, but I want to explain the value they would have in any language. The easiest way to explain how they are useful is to talk about session types.

The idea of session types is to encode the protocol of some concurrently executing process in the type system so that you can only perform operations which are legal based on the state that concurrent process is in. This is basically like encoding a state machine in the language where each state is represented as its own type, and each state transition is a method which returns the type of the next state.

Let’s take a very simple example, a transaction which must be committed or aborted:

```rust
impl Transaction {
    pub fn commit(self) -> TransactionResult;

    pub fn abort(self);
}
```

The problem with a session type like this is that the user can just drop the transaction. You might say in this case that you’ll write a destructor and abort the transaction on drop (I’ll return to that idea in the next section), but you can surely imagine more complex examples in which there isn’t an obvious state transition to perform on drop.

Linear types prevent the problem of dropping a session type because you *must* use the session type. You can use the session type by calling commit or abort, or you can use it by moving it to a new function. But what can that function do? It also can either move it to a new function, or call commit or abort. What you get is a liveness guarantee that eventualy (remember, eventually could be indefinitely in the future), the program will call commit or abort on this transaction.

But its worth going a little deeper, because this will expose a flaw in how Rust has implemented affine types that I’m going to address in the next session. Think about the implementation of commit and abort: they receive an argument `self`, which has the type `Transaction`, which is a linear type. What this means is that these methods *also* need to use the `self` value somehow. But how does this work? Surely it’s not turtles all the way down.

The second part of making linear session types work is destructuring. The transaction type is a struct made up of some set of fields, which themselves are normal or maybe affine types. In each of these methods, what happens is that at some point the transaction type is destructured into its field types; that uses the transaction, but instead of being left with just another value of the transaction type, you’re left with types that you can drop freely. This is the only way to make linear types work at all; otherwise you’d have to save every value of a linear type you ever create and return them from `main`!

However, if the user can destructure a transaction type, you no longer have a liveness guarantee that they will call commit or abort. So the third final piece of making session types with liveness guarantees is that you must use privacy to limit which code can destructure the session type. If the fields of transaction are private, only methods in its own module can destructure it. That way, taking the library that defines the transaction type, you can see that it is only destructured in commit and abort, and so you have a liveness guarantee that in any code based on that library eventually the program will commit or abort any transaction.

## E0509

You can think of types with ownership as a special case of session type which has a valid “default state transition.” This default state transition must transition to `()` (it cannot return an error or any other meaningful value), and it is called whenever the value goes out of scope without calling any of the other transitioning methods (if there even are any). We call this default state transition the *destructor*.

I think this is the right way to think about ownership types: they are just the special case of session types which have a default destructor. Which brings me to a kind of program that the Rust compiler doesn’t accept, and I think the Rust compiler is wrong: it is not possible to destructure a type that has a destructor. The error code for this error is E0509.

If the state transition of a session type is just a method that consumes the session type and destructures it, and the destructor is just an automatic state transition method, then a destructor is also just an automatic destructurer. There’s no reason this should preclude me from also destructuring it another way: it’s perfectly possible to imagine a contract on a type which is “either you destructure this, or you run its destructor.” But there’s no way to express that in Rust today, because if you add a destructor to a type, you cannot destructure it.

E0509 was added in the early days of Rust when I think the theoretical underpinning of move semantics and ownership was less well understood. As far as I can tell, the motivation was that if you add a destructor to a type, you want that destructor to be called, and if you destructure that type then the destructor won’t be called. But the solution then is the same solution for linear types: combine a destructor with privacy so that destructuring isn’t an option for consuming the type.

This is already how almost every type with a destructor actually works (they all have private fields) so the issue rarely comes up. But I have a great example from David Tolnay of a situation in serde\_json in which the library was required to make a bad work-around because it has a type that exactly fits the pattern that E0509 excludes: a type that should be consumed by destructuring it or running its custom destructor.

The type is the `Value` type, which is meant to represent any JSON value. It’s an enum of all the kinds of JSON values (a number, a boolean, an array, etc). You can use it to parse JSON with no expected schema into a value that you can traverse with `match` and so on.

However, JSON is often parsed from untrusted input, and its very plausible to define pathological JSON which would cause the ordinary destructor to overflow its stack. For example, consider the JSON `[[[]]]`. Parsing this to a `Value` will result in an array containing a array containing an array which is empty. With the automatic destructor code that is generated for you, this will perform 3 nested calls to deallocate each array variant. A pathological JSON string would contain enough nested arrays to overflow the stack when destroying a value of that type, so serde\_json’s Value type is meant to have a custom destructor which uses a form of tail call optimization to avoid having the stack space use grow with the depth of the JSON.

The problem is that if you implement this destructor on the `Value` type, now you can’t destructure it: but the whole point of `Value` is to destructure it using `match`! David Tolnay worked around this issue by adding a custom `Array` type instead of using `Vec`, which has the tail call optimizing destructor, but this complicates the API for no good reason. Instead, E0509 should be removed and it should be possible to define a `Value` type with a custom destructor without preventing users from destructuring it.

## Shared ownership and references

Ownership is great, but sometimes you do want to allow an owned value to be aliased. One way to implement this is to have some kind of constructor which takes an affine type and produces a normal type (or an affine type with `Clone` to mimic normal type semantics, in the case of current Rust). This is called “shared ownership.” These shared ownership constructs will do something to track how many aliases there are of that value, and only run the destructor when the last value has gone out of scope.

There are some important caveats to keep in mind if you want to add shared ownership to your language.

First, you must not allow the value being shared with shared ownership to be mutated without synchronization, because that will result in aliased, mutable state. So you will definitely need a story for controlling mutation if you’re going to add this feature.

Second, if your implementation of shared ownership doesn’t perform any kind of cycle breaking (as in the use of reference counted pointers), you will allow scenarios in which reference cycles exist, allowing values to be leaked and their destructors not to be run. This means any liveness guarantee about destructors running (or, for that matter, about linear session type transitions) now has to also be caveated with the possibility of the value being leaked instead. And if your solution breaks cycles but doesn’t guarantee any timeliness about when the value will be deallocated (as in tracing garbage collectors), this likely will cause performance problems for some destructors like mutex lock guards. All in all, this is a pretty fraught feature and you should be careful about adding it.

Rust chose to allow reference counted pointers which do no cycle breaking, so every guarantee based on destructors has to be caveated with the fact that destructors maybe don’t run. There has been interest in changing this so that you can define a type which can’t be leaked (“unforgettable types”), which then can’t be put into a shared ownership construct safely. Like linear types, adding this distinction to the language now would be very challenging, but it is appealing.

One way to allow aliasing a value that doesn’t have the problem of shared ownership is the concept of *references*; a reference operator is a special operator that takes a value but does not count as a move, so the value is still there after the reference is done. A shared reference then can be a normal type, so it can be aliased. You can also add *mutable references*, which are affine types and allow mutation because they aren’t aliased.

If you want to have this feature you need to ensure that the value is not used again while the reference still exists, because this would invalidate that reference. Rust has achieved this by giving its references “lifetimes” and running a “borrow checker” which validates the program using these lifetimes. Incidentally, this solution also prevents cyclic references because of the way that lifetimes work. This is mostly outside of the scope of this blog post, but these features are often discussed together with the concept of ownership under the shared term “ownership and borrowing.”

## Conclusion

This is a new kind of blog post for me. I’m not trying to communicate or explore ideas I have that I think are new, but rather just trying to popularize ideas that I think are old but not as widely known as they should be. I hope it’s enlightening to some readers to have this more grounded understanding of ownership and substructural types.

I can say that I would not design a new programming language without some form of substructural types. The value proposition of safety guarantees about aliasing and liveness guarantees about state transitions just seems way too useful. I hope that we will see these features properly in new languages that emerge.

Finally, it seems like contributors to the Rust project (especially Niko Matsakis) are interested in changing up Rust’s ownership rules in ways that I think, while challenging to implement, would be an improvement. Rust would benefit from having linear types, and from having normal types not be tied to memcpy. A much easier change that should also be considered is removing E0509, which would allow for owned types that can be destructured.