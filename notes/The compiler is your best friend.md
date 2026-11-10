---
title: "The compiler is your best friend"
url: https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it
clipped: 2026-06-17 02:05:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The compiler is your best friend](https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it)

## Digest Summary
The script explains how compilers transform source code—parsing, type‑checking, optimizing, and generating output—and why treating them as allies prevents runtime failures. It contrasts ahead‑of‑time compilation (e.g., Rust’s ownership and borrow checking that eliminate memory‑safety bugs) with just‑in‑time compilation in Java, where bytecode is later optimized by the JVM, and transpilation in TypeScript, which adds a structural type system to JavaScript while preserving gradual typing. The discussion highlights self‑hosting and bootstrapping as milestones for language maturity. The second part critiques common “lies” developers tell compilers: treating nullable values as non‑null, ignoring unchecked exceptions, and using unsafe casts. These practices hide runtime hazards from static analysis, leading to NullPointerExceptions, unexpected exceptions, and brittle code. Emphasizing accurate compile‑time information—precise types, nullability annotations, and avoiding casts—lets the compiler enforce safety and improves reliability across codebases of any size.

## Discussion Summary
Comments emphasize a desire to separate pure business logic from side‑effects, noting functional‑core‑imperative‑shell designs are conceptually appealing yet often hard to apply in real code. Opinions on error handling split between using asserts and logging versus letting programs crash, with many viewing explicit checks as basic practice. Rust’s safety and memory management receive praise, though its “zero‑cost” claim and broader hype are questioned, while C++’s standard library is seen as mitigating memory pain. Strong typing and compiler checks are valued, but growing toolchain complexity, documentation gaps and perceived bloat generate frustration.

---

## Full Article

Note: this is a "script" for a podcast that I recently recorded, as such it's more conversational and less technical than the usual content of this blog. Not a single code block in sight...

Prologue
--------

Imagine you wake up one night to find out that production is crashing. It takes you a while to unearth the root cause. It turns out to be a null pointer exception deep inside a service. It crashed the whole system. How did it get there? Where did it come from?

Now imagine a different story. One day a developer had to struggle for a whole of 20 minutes fixing some informative compilation errors. And that's it, that's the whole story. Nobody had to wake up at night, production never crashed.

One of these stories is a story of lies and deceit, the other a story of dialogue and cooperation. Today we will learn how to stop lying to the compiler, and how to get a good night's sleep.

Part I: The Compiler
--------------------

(If you're familiar at high-level with how compilers work, feel free to skip to the next [part](https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it#part-ii-lying-to-the-compiler))

But first things first. What is a compiler?

In the broadest sense, a compiler is a function, that takes an input in one format and produces an output in another format. This definition is so broad as to be useless... Although, if you take this definition seriously, it has some interesting implications on how we approach solving problems in everyday code. But I digress.

Let's try again, more concretely this time. A typical compiler takes source code in some programming language and produces an output in some other language. For example, a C compiler takes files written in C, and produces assembly code.

A typical compiler pipeline might have the following steps:

1. Parsing the source code into an intermediate representation, an abstract syntax tree (AST)
2. Typechecking the code, make sure that all the types line up
3. Optimization, going over the AST and finding opportunities to make the code more efficient
4. Code generation, converting the AST into the output format, like machine code.

As we will soon see, the typechecking step is probably the most relevant for most developers.

Like most things, nothing is that simple. Different languages have differently flavored compilers, doing a wide range of things. This is not a thorough review on all things compilers, so instead, let's take a sample of languages and see what kind of compilers they have.

### Rust

Rust is similar to C, in that it compiles directly to machine code. To distinguish this "classic" compiler from the rest, we call this style an "ahead of time" compiler. This means that everything that the compiler does starts and ends before runtime. Once we created the binary output, the work of the compiler is done.

But, this doesn't mean that the job of the compiler is easy. Rust is quite sophisticated, apart from parsing the source code the compiler needs to do things like macro expansion, type checking, borrow checking, and lots, and lots of optimizations.

Optimization, and generally performance is a common benefit of using compiled languages. Compiled languages tend to be faster than languages that don't use a classic compiler, but are instead dynamically interpreted on the fly (like Python). And Rust is famous for its optimizations in the style of "zero cost abstractions".

Zero cost abstraction means that despite Rust being a low-level language, in many cases one can write pretty high-level code and still get the performance of handwritten low-level code. This is possible because the compiler analyzes the code, and manages to translate a high-level construct like `map` on an iterator into a low-level, fast loop. This includes optimizations like inlining and loop fusion.

As a developer writing in Rust though, the thing that you would notice the most during development is all the memory safety checks the compiler does for you at every step.

Rust makes it possible to safely manage memory without using a garbage collector, probably one of the biggest pain points of using low-level languages like C and C++. It boils down to the fact that many of the common memory issues that we can experience, things like dangling pointers, double freeing memory, and data races, all stem from the same thing: uncontrolled sharing of mutable state. For example, if two different variables share a pointer to the same data, if one of them frees the pointer, the other will end up with an invalid pointer without knowing it. Likely breaking something upon pointer dereference.

So Rust forbids us from freely sharing pointers. Each pointer has exactly one owner at every moment of time. Once the owner goes out of scope, memory is freed automatically. Since there are no other owners, this is safe and cannot lead to dangling pointers and the like.

What makes Rust special is that all of this happens at compile-time. The compiler tracks pointer ownership, using something called a borrow checker, forbidding us from doing anything that violates the single ownership of pointers. Memory unsafe code will simply fail to compile.

Rust's powerful type system is one very compelling (and painful) reason to use it. A broken elevator and walking 21 floors up the stairs can really motivate you to invent such a safe language.

Then we have Java.

### Java

People often think of Java as a static, compiled language. But actually, the Java compiler doesn't produce machine code. Instead, it produces bytecode. An intermediate (stack-based) language that is then *dynamically* interpreted by the Java Virtual Machine (JVM) when the bytecode is executed.

The reason for going through all this trouble is portability. By using intermediate bytecode, Java can be compiled once on any platform, but then executed on any other platform that has an implementation of the JVM. That's cool and all, but didn't we just say that interpreted languages are slow?

True, in the early days of Java, people were worried that running such a "dynamic" language will be too slow to be useful, and surely will never be able to compete with something like C++. And that's why we have "just in time" compilation. Or JIT for short.

The Java compiler does a lot less than Rust's. The translation from Java to bytecode is comparatively simple. The compiler doesn't make optimizations as far reaching as the Rust compiler. And if we left things that way Java would indeed be quite slow.

The real fun begins at runtime. The Java runtime has a JIT compiler enabled. The JIT compiler monitors the execution of the bytecode, as it gets slowly interpreted step by step. After a while, the JIT starts recognizing various hotspots in the code, like long loops, or common branching points. It then takes the bytecode for the hotspot and compiles it down to an efficient machine code representation. From that point onwards, that segment of code should run much more quickly.

Like a sophisticated ahead of time (AOT) compiler, the JIT compiler can apply nontrivial optimizations to the code. But unlike an AOT compiler, the JIT compiler has access to the actual usage patterns at runtime. Meaning that it can be more aggressive in optimizing the real bottlenecks in code. Things like dynamic dispatch in an object-oriented class hierarchy can be converted to static dispatch at runtime.

If you ever wondered why your JVM app takes time to "warm up" before it's actually fast, the JIT compiler is your answer. It takes time for the JIT compiler to recognize and compile the actual hotspots in code.

These days, Java has an AOT compiler as well, called Graal. As a result we can use the very same Java code and produce two completely different artifacts, either in bytecode or machine code (with some limitations).

More generally compilers can have more than one compilation target, or "backends". For example, both Scala and Kotlin can be compiled to either JVM bytecode, JavaScript, and native machine code. To support such use cases, and to avoid repetition between different backends, the compiler will have some intermediate representation of the language that is being compiled, the AST. This way, most of the compiler's work like parsing, typechecking, and various optimizations can produce one AST, but then that one AST can be converted into different outputs.

Despite all that complex work being done by the various compilers, most of the interaction that Java programmers have with the compiler is with the type checker. Java's type-system is not nearly as strict as Rust's, often being more annoying than helpful. So it's not uncommon for us the developers to "know better" than the compiler and use a cast every now and then. These are the first signs of trouble...

Seeing that a compiler can be quite the complex beast, you would be quite correct in asking:

### Aside: Who Compiles the Compilers?

Or more specifically, in what language is the compiler written? It would seem natural for the developers of a new language X to write the compiler in X. Surely it's their favorite language. At the very least, it's a good idea for them to dogfood their own creation.

Among people who write compilers, writing the compiler in the very same language it's supposed to compile is considered an important milestone. It shows that the language is mature enough to be able to implement such a complex piece of code. When a language does it, it is said to be "self-hosting".

Here we have a paradox. If I have a compiler written in X, to be able to use it I first need to compile it, and for that I need a compiler for language X. But I don't have one compiled, I need to compile it first... And so we find ourselves with a chicken and egg problem.

The way to get out of this conundrum is by a procedure called "bootstrapping". Here things are going to get a bit meta.

It goes like this. First write a compiler in language X, the "bootstrapp**ed** compiler". Ideally you do that using as few features of X as possible. Then choose another existing language Y (can be assembly or some high-level language), and write a compiler for X in Y, the "bootstrapp**ing** compiler". It doesn't have to handle all of the features of X, only the ones that were used in the code for the bootstrapp**ed** compiler. Once you run the bootstrapp**ing** compiler on the code for the bootstrapp**ed** compiler, congratulations, you now have a brand new self-hosting compiler for X. From this point onwards, you can improve the compiler and add features to it all without leaving the comfort of your favorite language X.

We can follow this process with the Rust compiler. Originally, it was written in the OCaml language. But the current Rust compiler was rewritten in Rust, which makes it a proper self-hosting compiler.

This is all good and well, but most of the time us simple developers don't really care about the language the compiler uses, we just need it to compile code. The reason I'm telling you all this is that it gives us an interesting insight into the development of programming languages.

The people who write compilers are usually the same people that design the language itself. And most of what they do all day long is writing compiler code. This might skew their incentives. They really enjoy using languages that are a good fit for writing compilers. Even more so, since in the early stages of a new language the compiler is probably the biggest piece of code written in it. That's the chance for the new language to really shine.

We shouldn't be surprised then, to find that many new languages tend to accumulate features that are very convenient for compiler writers. Things like pattern matching, and implicit parameters.

But seeing how compilers are not very representative of the code most of us write daily, this might not be the best way to spend the complexity budget when designing a new language. Lucky for us, some of those features are useful for plain-old, boring business code as well. Especially code written in the functional style.

Let's wrap up this exploration of compilers with one more language.

### TypeScript

The TypeScript compiler is special in that the target is not a low-level format like assembly and bytecode, but instead another high-level language, JavaScript. Although definitions are a bit fluid, but in this case we say that the TypeScript compiler is actually a "transpiler". Even more curiously, since JavaScript is a strict subset of TypeScript, we can say that TypeScript is compiling into itself.

There are two main reasons to want to do that: nicer syntax for various features of JavaScript (like classes and enums), and the type-system that TypeScript adds on top of JavaScript.

Microsoft, who developed TypeScript, was motivated by the pain they experienced when scaling large JavaScript codebases. Adding a robust type-system to a language makes it much easier to tame large codebases over time (things like refactoring become safer). We can see the same trend with Dropbox investing in Mypy, an optional type checker for Python, to help scaling their Python codebase.

Adding a type-system to an existing programming language is very different from designing a language with types from the ground up. With an existing language you must be able to add types to as much existing code as possible. And codebases in dynamic language sure do tend to be... Dynamic.

To mitigate this, TypeScript uses gradual typing. With gradual typing you don't have to add types to the whole codebase all at once, like you would in, say, Java. Instead, you can do it gradually, and the compiler verifies that whatever is annotated is consistent with itself, and ignores the rest. This smoothes migration from an untyped code and mindset to a typed one.

There is also the question of which type system is most appropriate for an ex-dynamic language. Did you know that type-systems come in different flavors? Most mainstream languages use "nominal" type-systems. This means that each type gets a unique name, and types that have different names are treated as distinct types by the compiler. In contrast, TypeScript uses a "structural" type-system. Two types are considered the same if they have the same structure, e.g., the same fields and methods. The name of the type doesn't matter.

Structural typing seems to be better suited when gradually typing a dynamic language. "If it walks like a duck and quacks like a duck, then it must be a duck" is a common viewpoint in dynamic languages, and structural typing is the way to capture this mindset with types.

In a curious turn of events, TypeScript and Mypy went the other way around with bootstrapping and self-hosting. The current TypeScript compiler is self-hosting, but a rewrite in Go is in the works. In Mypy, the compiler was rewritten from plain Python into a special almost-Python dialect that compiles directly to C. The motivation for both rewrites is performance. Turns out that it's difficult to get a sufficiently fast compiler that can quickly process large codebases in dynamic runtimes like JavaScript and Python.

Like before, we can't help but notice that the type-system is the main interface between the developer and the compiler. In the case of TypeScript I would say that it's also the main reason to even want to use the language.

And yet, so many developers hate the compiler. It seems that all it does is yell at us about trivialities like "string is not int" and such. Is it worth bothering with a compiled language just for that?

Part II: Lying to the Compiler
------------------------------

The compiler is always angry. It's always yelling at us for no good reason. It's only happy when we surrender to it and do what it tells us to do. Why do we agree to such an abusive relationship?

And for someone who yells that much, it's not even that smart. Remember all the times when the compiler yelled at you something about a type mismatch, but turns out that you were right and the compiler was wrong? In the end you had to use a cast (or mark something as `any`) just to shut the compiler up.

We can solve these issues by quitting the relationship, and jumping ship to a dynamic language. I suspect that compiler abuse is why in the past Python grew in popularity compared to Java (that, and Java's verbosity). But we just saw that even in historically dynamic languages, like JavaScript and Python, there's a trend towards a more static, more compiler-centric way of writing code. These days Python has not just one, but *multiple* competing tools for typechecking (mypy, pyright, pyrefly, ty). Why do people lean that way?

Maybe it's performance. We talked before about how compiled languages tend to be faster than dynamic languages. But that doesn't seem quite right. In many contexts, where the language's performance is not the bottleneck, people will still use types. And TypeScript, for example, doesn't give us a runtime performance benefit, all the type information is discarded after compilation. Are people really just that masochistic?

Maybe Rust is the answer. Rust's compiler brings significant improvements in code safety where memory management is involved. True, its compiler is even more difficult to satisfy than average, but it solves a very tangible problem that would be very difficult to safely solve otherwise. Still, most of us don't write low-level code, and we mostly use garbage-collected, memory-safe languages. Not many mainstream languages have a type-system that is as powerful as Rust's, so we don't usually get that much extra safety.

We can imagine that in very large codebases, like the ones managed by Microsoft and Dropbox, there's some magical advantage to having types checked by the compiler (we mentioned safer refactoring before), despite the obvious pains. But most of us don't maintain code that large, why bother with types then?

It seems that all the compiler can do for us is act as simple, and not very reliable, guard rails. Sure it would sometimes notice that this or that int is actually a string. But if that's all it can do for us, then we might as well write a couple of unit tests, and remove this nuisance from our lives.

### The Lies

I think that this is a false premise. The compiler is actually much more useful and powerful than it might appear. So useful in fact, that relying on it is beneficial in any codebase, large and small. The problem is that we are used to lie to the compiler all the time, in return all it can do for us is yell about strings not being ints and do little else.

What do I mean by lying to the compiler?

The compiler, or rather the type-system, is only aware of things that are known at compile-time. A "lie" would be to write code that communicates one thing at compile-time while doing something else at runtime. On the other hand, the more facts that we can truthfully state to the compiler at compile-time, the more useful the compiler can be. But first, let's see some concrete examples of lies.

### Null

When we say that some variable `x` is a string. What do we mean by that? It means that the runtime values that `x` can take are things "a", "ab", "abc", and many other reasonable strings. This also means that we can apply various methods to `x` like `substring` or `endsWith`. Unfortunately, in most modern languages this also means that at runtime it can be `null`.

Unlike the other non-null values, you cannot call `substring` or any other method on `null`. Calling a method on `null` will trigger an `NullPointerException`, possibly far away in code and time from where that `null` was created. We could adopt a policy of "defensive programming" checking for `null` every step of the way. But in practice nobody does that. Instead, in many places in our code we implicitly *assume* that values are non-null unless stated otherwise (in a comment that nobody actually reads).

This is one of the most common lies we tell the compiler. We state that something is a valid string, but at runtime it can just as well be `null`. In most mainstream languages the compiler cannot distinguish between nullable and non-nullable values. And so it cannot help us out when our nullability assumptions turn out to be wrong. That's when things crash.

How many times did you find yourself setting something to `null` because you couldn't come up with something better, only to discover that some other place starts crashing?

### Exceptions

Speaking of crashing, another source of lies we tell the compiler are exceptions. More specifically, unchecked exceptions.

If we write that some method returns string, what do we mean by this? Ideally, we mean that every time we call the method a string value will be returned. But in reality, there's another, sneaky way of returning from a method: we can throw an exception.

Similar to `null`, unchecked exceptions might be discovered away from the origin (although not as bad as `null`, they have to walk up the stack, and are not stored as data). And similar to `null` the compiler won't track them for us. If we don't go into a full defensive mode, we're assuming that the code is exception-free, and assumptions tend to break over time. But we lied to the compiler, so it won't be there to help when they finally break.

How many times did you leave a comment on some branch of code stating "this CANNOT happen" and thrown an exception? Did you ever find yourself surprised when eventually it *did* happen? I know I did, since then I at least add some logs even if I think I'm sure that it really cannot happen.

### Casts

So far things happened by accident, due to implicit assumptions being broken. But sometimes we are smarter than the compiler. Sometimes we know better and we can force the compiler to obey. We can use type casting.

Suppose that there's some interface, let's call it `Animal`. And it has two different implementations: `Cat` and `Dog`. Sorry for the cliche example, it's difficult to be original without written code.

Now we are working on some code that got an `Animal` argument, call it `x`. In this particular flow we know for certain that `x` must be a `Dog`. We can follow the code ourselves and show that `x` is unquestionably a `Dog`. So we want to use `Dog`-specific methods. But the silly compiler won't let us. It only knows about `Animal` methods.

The compiler won't budge, and we won't budge. So we take out our hammer, and use a cast. Now `x` is a `Dog`, and the compiler doesn't argue anymore. All is well, until some new feature request that requires supporting `Cat`s in our flow. When we make the change, we forget about that cast we did a while ago to make things work, and the code explodes.

The compiler didn't help us because we silenced it by lying to it. There are two lies going on here, why wasn't the initial type precise enough? If we can see that it must be `Dog`, why weren't we able to show that to the compiler? Then there's the cast itself, which blatantly tells one thing to the compiler (`x` is a `Dog`), when the reality might be something else (`x` is a `Cat`).

How often do you think you know better than the compiler?

### Side-Effects

Up until now the examples are quite obvious lies. We all feel a bit dirty when doing a cast, or throwing a runtime exception with the comment "this should NEVER happen". But here's a more subtle example.

Let's say there's a function called `foo`. When we see that `foo` takes no arguments and returns `void`, what can we say about what `foo` does without looking at its implementation? Nothing really. It's clearly doing something, and that something is not reflected in its inputs or outputs. We can only conclude that the function is doing some kind of side-effect, like changing a variable or writing to a file.

Just like us, the compiler doesn't know anything useful about `foo` either. So we have a function that is clearly doing something important, otherwise it won't be there. But all we tell the compiler is that "nope, move along, nothing interesting to see here". But that's a blatant lie, something interesting is going on here, but the type of `foo` doesn't reflect that.

The compiler gets so confused that even if we comment out a call to `foo` it won't complain, it's as if it doesn't even know it exists.

If you look at a typical codebase, many, many functions return void. Every time we do that we prevent the compiler from knowing something useful about the flow of the code.

With all these lies all over the place, it's no wonder that the compiler is not particularly useful. What happens if we stop lying to it?

Part III: No More Lies
----------------------

If we want develop a serious, constructive relationship with the compiler, we must first stop lying to it. Only then can we open channels for serious dialogue.

We are so used to using `null`, exceptions, casting, and side-effects, that at first sight it might seem impossible to give those up.

But that's just an illusion.

### Null

Some languages like Rust and Haskell have no `null` at all. Can you imagine what it's like to work that way?

Liberating, that's how it feels. You no longer have to keep worrying about an accidental `null` slipping through, because there aren't any. But, you might ask, what if something *really is* missing, how do I represent that without `null`?

In a world without `null` there are a number of ways to represent a thing that might be missing. The most common one is to use something like an `Option` type, that can be in one of two states, present with a value, or missing. When you want say that a `String` might not exist you use the type "option-of-`String`". And that makes all the difference to the compiler.

Now the compiler knows what's going on, since option-of-`String` is a distinct type from just `String`, it's no longer possible to call `String` methods, like `substring`, on it. Every time you deal with an option-of-`String` value the compiler will helpfully remind you to deal with the possibility that the value is missing.

On the flip side of that, now every time you have a `String` value you no longer have to worry that it might be missing. You can just use it without any defensive programming involved. And if you mistakenly break the rules and try to assign an option value to a non-option value the compiler will point that out and force you to think whether that's what you really want and what the consequences across the codebase will be.

Some languages, like Typescript and Kotlin have builtin support for nullable values. If you mark a `String` as nullable, it will become a distinct type from a plain `String`, giving us similar benefits to `Option`. In Java we can emulate something similar with `Nullable` and `Nonnull` annotation. But that requires some additional tooling to make it work.

What all those approaches have in common is that all of them involve the compiler. Instead of hiding our assumptions from the compiler we make them explicit in a way that the type-system can track.

We can do the same with exceptions.

### Exceptions

I'm personally not aware of languages that completely remove exceptions from the language. But working mostly without exceptions, at least as a convention, is definitely possible.

Inspired by the `null` case, we can take a similar approach with exceptions and make them explicit in our types.

The most common way to do that is to use another container type like `Result` or `Try`. A return type like "result-of-`String`" means that we can have one of two cases, either a success with a `String` value, or a failure with some exception.

This approach makes it explicit to both us and the compiler what's going in a function. Now the compiler can track possible errors for us, and force us to deal with them as appropriate. And if we change some piece of code from `String` to "result-of-`String`", the compiler will helpfully shows where this needs to be handled.

In Java we can take an alternative approach and use checked exceptions. But industry experience over the years seems to indicate that people don't enjoy using them. It's probably a matter of ergonomics. Using a wrapper type instead might be a more ergonomic alternative.

While avoiding nulls and exceptions is fairly straightforward, casts can be trickier.

### Casts

Unless forced to by some external library, I think that the presence of casts in our code should be considered a design smell. My first (possibly controversial) suggestion would be to configure your tooling to just forbid them by default.

When feeling the need to use a cast, we should consider whether the current design is doing a good job of reflecting our intentions. Recall that when doing a cast we can ask one of two questions, why was the type not precise enough to begin with? And why do we need to cast here?

There's no generic answer to these questions, but finding a good answer to either of them will make the compiler's life easier.

Some times the solution would be to add more methods on a parent interface (like `Animal`). Some times you might discover that you could've started out with the more specific type (`Dog`, for example) from the very beginning.

Another class of solutions is to remodel the problem from using open interfaces to using sealed/union types. Many modern languages support them. Using sealed types retains some of the flexibility of using open interfaces, but still allows the compiler to be in the loop. Instead of blindly assuming that some case is true, we can safely match on the sealed type and the compiler will gladly inform us about all the cases we must handle at this point. Some languages can even magically auto-complete all the relevant cases.

As code evolves, the compiler will keep track of the cases over time. And if something changed in the sealed type, the compiler will tell us about all the locations where the new case should be handled. Giving us a chance to handle whatever new logic that was added, before it crashes at runtime. Something that it was powerless to do when you used a plain cast.

Now for the thorniest issue of them all.

### Side-Effects

Software exists to make side-effects, otherwise we would just have overheating boxes without any useful output. So side-effects cannot be completely eliminated from code. But they can be better managed.

This is even a deeper design issue than casting, and there isn't a one size fits all solution. My suggestion would be to separate as much pure computation from side-effects as possible.

In practical terms that would mean that every time you see a void return, or something that performs some side-effects mixed with other useful computation, you try to extract a pure function, with well-defined inputs and outputs, that only does computation, and another function that does the side-effects (similar to the Command Query Separation principle).

A common pattern would be to separate pure business logic from data fetching/writing. So instead of intertwining database calls with computation, you split into three separate phases: fetch, compute, store (a tiny ETL). First fetch all the data you need from a database, then you pass it to a (pure) function that produces some output, then pass the output of the pure function to a store procedure.

Now instead of having one big flow that takes no inputs and produces no outputs, you have three building blocks, and one of them has well-defined inputs and outputs. Not only is having this separation makes it easier to focus on your business logic, especially when writing tests. But now that we have inputs and outputs the compiler can follow along as well and help out.

Taking these ideas seriously leads us toward architectures that are known as "functional core, imperative shell". Within the functional core the compiler is much more useful, because it has actual types for inputs and outputs that it can follow and enforce. More "interesting stuff" is happening within the knowledge of the compiler.

Let's see what happens when we maximize that knowledge.

Part IV: The Compiler as Our Friend
-----------------------------------

Okay, so we stopped lying to the compiler as much as we can, and we are already seeing some gains in safety. No more null pointers, surprising exceptions, or fragile code. We can stop here and pat ourselves on our backs.

But we can do even better. Not lying is just the first step in a productive relationship. The next step would be to start sharing knowledge. The simplest way to start doing that is to sprinkle our code with more types.

### Typed wrappers

When we use a string or an int in our code, what do they actually mean? Rarely is it just an arbitrary number or some raw text. Usually they represent some concept like a user ID or a file name. The thing is that this special meaning of the int or string are not reflected anywhere outside our head, or maybe a comment.

As time goes by we have more and more different meanings that an int can take in our system. Maybe it's an app ID, or a post ID, or a feed ID? Who knows. And so confusion arises, you start mixing up your ints, weird bugs creep up.

While this is happening, the compiler remains silent, "an int is an int, what can you do...". We didn't share our knowledge with the compiler, we have no one to blame.

The fix is simple: use small, typed wrappers, sometimes called "tiny types". Each concept you have in your system deserves to have a unique type, something for the compiler to hold on to. So you would have a `UserID` type, an `AppID` type, and so on. Underneath they might all be simple ints, but now both you and, more importantly, the compiler can distinguish the different concepts in code.

The difference might seem small, but the consequences are far reaching. Extra safety, the compiler will no longer let us confuse the different ints, is just the beginning.

Once the compiler gained knowledge of a concept you can use it for various tasks. For example, suppose you want to find out where are all the usages of user IDs in code. If we were still using ints, asking the compiler for all usages of the type int is meaningless, there are too many of those and they mean different things. Searching variable names is easy, but the results might not be complete. But if we have a dedicated type for `UserID`, that's easy, just ask your editor to find usages of the type and you get the precise results you need. The compiler keeps track.

For the same reasons, refactoring becomes easy. You want to change the representation of the `UserID`? Add some extra salt for security? No need to search for all the relevant ints and pray for the best. Modify the type and follow the compilation errors. Done.

Need some special validation for user IDs? Hide the constructor of `UserID`, add an alternative "smart" constructor, follow compilation errors. Done. No need to chase different ints across the system.

And for us humans, descriptive, domain-specific types make function signatures more readable, both for developers and for the occasional stakeholder. What's not to like about it?

Simple typed wrappers are, well, simple. But sometimes we need more sophisticated types to express ourselves to the compiler.

### Union Types

Did you ever stumble on a class `Foo` that has too many fields with a long comment that explains something along the lines of "if field `a` is `true` then fields `b` and `c` must not be `null`". And so on and so forth for a few more different conditions?

Then when you actually start trusting `Foo`'s comment and check that `a` is `true`, you discover, with a production null pointer exception, that `b` was actually `null`.

To describe this more formally, `Foo` had some invariants, and those invariants were violated. Not every combination of field values makes sense for our application.

How much nicer it would if the compiler could tell us "hey, look here, this invariant breaks if you use this set of field values"? Unfortunately, most compilers are incapable of expressing invariants that depend in such a way on runtime values.

The solution to many such problems is to remodel the type to better reflect the invariants that we want to encode, in such a way that the compiler will be able to follow along and only allow for legal combinations.

One of the most versatile tools for this is to use union, or sealed types (enums in some languages). With a union type we create one variant per case. And each case can only have a legal combination of values. So the case where `a` is true will become one variant with two non-nullable fields `b` and `c`. And that's it.

The advantage of taking this approach is that the union type doesn't even allow us to write down an invalid combination. You can only choose from valid ones, anything else is a compilation error.

The way you work with union types is that every time you need to access some data you need to match on the value. And then you act according to the case you're on. If you're in case `a`, you're *guaranteed* to have the `b` and `c` values. The compiler makes sure they are consistently there no matter how you got to this point of code.

This can make union types more powerful than tests that check invariants. Unlike a unit test, which can only test for a specific code paths you currently know about, the compiler can track *all* code paths, now and forever.

As mentioned before, in some languages the compiler can auto-complete the different cases relevant for the point in code you're at. Sometimes it feels like the code is writing itself, you just have to fill in the blanks.

When the code evolves over time and more cases are added, the compiler will notify you about all the relevant places where you need to update the logic to handle new cases. This is a great way to assess the consequences of changes you're about to make and help you with decisions at the design phase.

Using union types this way is a great way to model alternative states in code, and it's part of a more general approach to programming where you strive to "make illegal states unrepresentable". That is, encode your invariants as facts that the compiler can enforce and makes it impossible to even *write* code that will break those invariants.

This opens up a whole new way of approaching types.

### Typed Guarantees

We are used to think about types as just a way to distinguish different values. This one's a string, that one an int. But as we rely more on the compiler to help us we can start thinking about types as guarantees that we want from the type-system. Or facts that we expect to hold, and that the compiler should verify *for* us.

A common scenario is that we want to make sure that the list we got as an argument contains at least one item. A classic example is when we need to compute some average, it's undefined for empty lists. Or choose a payment method in a payments system, you must have at least one to be able to proceed.

What we could do is revert to defensive programming, check the list before proceeding, and throw an exception if it's empty. But being defensive all the time is tedious (and eventually you forget about it), and we are back to lying to the compiler. Instead, we can signal our intentions with a type: `NonEmptyList`, a list type that cannot be even constructed without at least one element (some languages have it builtin, but it's also easy to implement in a library).

Not only does this communicate our intent to our callers better than any comment can do, but it also forces the compiler to make sure that nobody can call us with an illegal value. Once we encoded a guarantee as a type, we don't have to worry about it anymore. No defensive programming, no need to write extra tests for it. No more fear that some future refactor will break our invariants.

Once we start thinking about guarantees the compiler can make for us, the opportunities are endless. You can come up with a type for pretty much anything (within reason):

* `PositiveNumber`, how much code that we write would be invalid if it got a negative number?
* `AgeOver18`, maybe it's mission critical to limit certain flows based on user data
* `SortedByPriority`, because it might be expensive to re-sort stuff just to be defensive

And the list goes on, for almost any kind of custom validation logic you might want. Some can be encoded with union types, some might require techniques like smart constructors. You don't have to get too fancy for this to become a valuable tool.

Once you start sprinkling these types around, not only is the intent of the code becomes clearer, but the compiler can help verify that everything is consistent, and that any new code knows what it's required to do.

With enough types in place you might get the feeling that "if it compiles, ship it".

### Dialogue

In the prologue we saw what I think is a fairly common story, `null` unexpectedly crashing a production system. But we can make this story very concrete. I'm sure that many of us felt the Google Cloud outage in June 2025. So many services around the world were affected that it was very hard to miss.

From the [incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) we learn that the root cause of it all was a `null` value where it was unexpected (along with some other operational compounding issues, like a lack of randomized backoff). And it's not really surprising. We saw that `null`s are lies that we tell the compiler, values that it cannot track for us. In a large enough system, you are bound to lose track of them.

With the lessons that we learned, can we imagine another outcome? An outcome that doesn't involve a big chunk of the internet crashing?

So we already know that using `null` is lying to the compiler. If we are motivated enough we will never use a `null` in our code, opting instead for something that the compiler can track, an option-like type. The first step of not lying to the compiler might be the most difficult one, but once we take it a whole new world opens up for us.

The incident report mentions some "unintended blank fields" in `Policy` datatype that triggered the whole thing. Although I don't know the actual details, let's imagine that those fields used to be non-empty and now we want to open the possibility for making them empty. But we no longer have `null` at our disposal, what do we do? We change the type of the fields to be "option-of-X", and run the compiler. This is where the magic of dialogue starts to shine.

In a large codebase and a central entity like `Policy` you can imagine that you'll have many compilation errors the moment you set some fields to be optional. That sounds scary, but that's way better than `null` silently propagating all over the code and not knowing the consequences. With the compilation errors you now have a full report of all the code sites you need to reconsider.

You start going over them, one by one, fixing the errors. But the more errors you fix the more you feel that something's not right. Adapting the code feels like too much effort, too hacky, "a maze of twisty little ifs, all alike". That's the compiler trying to tell you something:

> Maybe you need to reconsider the design?

And that's what you do, with all those changes that you had to make it becomes more obvious that these are not just fields that you made optional, what you really did is uncover a new flow in the system, with new rules. In the old flow the fields really are mandatory, in the new flow they are no longer needed. So you combined the two flows and made the fields optional. But by just setting the fields to be options the new flow becomes implicit in a combination of empty values and flags, something that the compiler can't track, and is not apparent when reading the code.

Instead of riding on the existing flow and tweaking it, you can make things explicit and turn `Policy` into a union type. If it already was a union, you add another case to describe the new flow, and you compile again. There are still many compilation errors, matches that are incomplete, but now they are telling you something different:

> If you want to support this new flow, here are all the things you need to consider

And that's what you do reviewing the compilation errors and figuring out what the new flow implies at each site. Maybe along the way you discover that the new `Policy` type requires different validations that you didn't think of before. As a result in the new `Policy` you start using a `NonEmptyList` of `AvailabilityZone`s which guarantees that you can't run the new flow without at least one applicable `AvailabilityZone`. (Of course `AvailabilityZone` is not some plain string, you have a dedicated type that tells you exactly what it means and gets validates accordingly.)

You compile again and somewhere along the edges of the system where you process user input the compiler tells you:

> Listen, I don't have any way to prove that you actually have at least on availability zone provided by the user

And the compiler is right, if you were just using a regular list to represent the availability zones you would've missed this. Input processing happens far away from where we actually require the availability zones to not be empty and your unit tests missed this. So you add the appropriate user input validation. And lo and behold, it compiles. Ship it!

Yes, you struggled with the compiler, and yes it took some time. But guess who's getting good night's sleep tonight?