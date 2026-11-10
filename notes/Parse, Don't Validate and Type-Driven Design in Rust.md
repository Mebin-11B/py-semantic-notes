---
title: "Parse, Don't Validate and Type-Driven Design in Rust"
url: https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/
clipped: 2026-06-17 01:41:58
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Parse, Don't Validate and Type-Driven Design in Rust](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/)

## Digest Summary
The post explains the “parse‑don’t‑validate” pattern in Rust, advocating that invariants be encoded at the type level rather than checked at runtime. Using division as a running example, it shows how a plain `fn divide(a: i32, b: i32) -> i32` can panic on zero, while a fallible version returning `Option` merely signals failure. The author then introduces newtype wrappers—e.g., `NonZeroF32` and `NonEmptyVec`—whose private fields force construction through fallible constructors (`NonZeroF32::new`, `NonEmptyVec::try_from`). Once created, these types guarantee the invariant (non‑zero, non‑empty) and can be used directly in functions, eliminating repeated runtime checks and allowing the compiler to enforce correctness. The article contrasts weakening return types (Option/Result) with strengthening parameter types, demonstrating reduced boilerplate, better refactor safety, and potential performance gains. It also outlines how these wrappers integrate with common Rust APIs (e.g., `Result`, `Box`).

## Discussion Summary
The discussion acknowledges the value of “parse, don’t validate” when invariants can be encoded directly in types, citing examples such as non‑empty vectors and dependent typing, but criticizes the article’s division‑by‑zero case as poorly chosen and impractical for many languages. Many points argue that validation remains necessary for complex constraints and that excessive newtype abstractions can add unnecessary complexity, especially in Rust. Overall, the sentiment is mixed: the principle is useful when feasible, yet over‑reliance on type‑level guarantees is seen as cumbersome.

---

## Full Article

Parse, don't Validate and Type-Driven Design in Rust
====================================================

**Reading time:** 17 min read

 

---

Table of Contents
-----------------

[1.3](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#maxims-of-type-driven-design)

Maxims of Type Driven Design

---

     ![A gavel. Photo by the Tingey Injury Law Firm.](https://www.harudagondi.space/uploads/parse-dont-validate/tingey-injury-law-firm-veNb0DDegzE-unsplash.jpg)  

Photo by the [Tingley Injury Law Firm](https://unsplash.com/@tingeyinjurylawfirm).

 

In the Rust Programming Language Community Server, thereâs tag named `-parse-dont-validate` which links to an [article](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) about the concept of avoiding validation functions and encoding invariants in the type level instead. I usually recommend it to beginners/intermediates to Rust who are struggling with designing APIs.

The only problem is that it uses Haskell to explain its concepts.

Yeah, itâs *fine*, but for beginners unfamiliar with the functional paradigm, it might not be so approachable. And so I wanted so write a blog post about this pattern but in a rather Rust-centric way. So letâs start!

Dividing by zero [#](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#dividing-by-zero)
-----------------------------------------------------------------------------------------------------------------------------

One basic example I can give is a function that divides a number by another number.

```
fn divide(a: i32, b: i32) -> i32 {
```

This is fine, but unfortunately it can panic when `b` has the value of zero:

This gives an [error](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=06b95e79e3958fd10478f0a4bb75e8fb):

```
Compiling playground v0.0.1 (/playground)



Finished `dev` profile [unoptimized + debuginfo] target(s) in 1.28s



Running `target/debug/playground`



thread 'main' (41) panicked at src/main.rs:2:5:



attempt to divide by zero



note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Thatâs fine and dandy if we want erroneous values to fail loudly at runtime, but what if we want stronger guarantees? This is especially important when some operations donât fail loudly, like the following:

```
fn divide_floats(a: f32, b: f32) -> f32 {



dbg!(divide_floats(a, b));
```

```
Compiling playground v0.0.1 (/playground)



Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.62s



Running `target/debug/playground`



[src/main.rs:8:2] divide_floats(a, b) = inf
```

Thereâs no error! But do we want that?

We could add an `assert!` in the `divide_floats` function to emulate typical integer division behavior.

```
fn divide_floats(a: f32, b: f32) -> f32 {



assert_ne!(b, 0.0, "Division by zero is not allowed.");
```

```
Compiling playground v0.0.1 (/playground)



Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.65s



Running `target/debug/playground`



thread 'main' (32) panicked at src/main.rs:2:5:



assertion `left != right` failed: Division by zero is not allowed.
```

Cute! But thereâs still a problem of running into panics only at runtime. My beef with Python (or any other dynamic language for that matter) is that a lot of errors only arises when you run the program. Thatâs why theyâre adding typechecking to these languages: people want to bubble some mistakes to compile-time (or typecheck-time, whatever). We can use Rustâs rich type system to communicate these errors at build time.

One way, which I think is the more common way as people are more familiar with it is the idea of fallible functions, which return either an `Option` or a `Result`.

```
fn divide_floats(a: f32, b: f32) -> Option<f32> {
```

This is a fine way to do things, as it communicates that (1) the function can fail, and (2) you can handle the failing case after. â â Of course, `catch_unwind` exists, but Iâm pretending that it doesnât.  To me, the functionâs invariants (`b` must not be zero) is encoded after-the-fact, aka in the return type `Option<T>`. This implies to me that the invariants could be encoded before-the-fact, aka in the function parameters. But what would that look like?

Enter the newtype pattern.

Say, letâs have a type that is something like `f32`, but itâs guaranteed to never be zero. Weâll name it `NonZeroF32`:

This struct only contains a single field `f32`. The semantics of the type understood from the name is that itâs just like a normal `f32`, but does not allow the value of zero. How do we guarantee this? Since rust does encapsulation at the module level, we make this type public while have its field private.

```
pub struct NonZeroF32(f32);
```

Then, the only way to construct this type is via a fallible constructor function:

```
fn new(n: f32) -> Option<NonZeroF32> {
```

Remember to add some convenience traits.

```
impl Add for NonZeroF32 { ... }



impl Add<f32> for NonZeroF32 { ... }



impl Add<NonZeroF32> for f32 { ... }



// and a bunch of other operators...
```

We can then use this in our `divide_floats` function.

```
fn divide_floats(a: f32, b: NonZeroF32) -> f32 {
```

There is an interesting implication in this pattern.

In the second version of `divide_floats`, we changed the return type from `f32` to `Option<f32>` just to avoid the panics. As described in the original article by Alexis King, this is a *weakening* of the return type, and the functionâs promise. We temper the callerâs expectation by saying that yes, this function can fail in some way, and you have to account for that. And that weakening is described in the type system via the `Option` enum.

In the third iteration of `divide_floats`, we change our perspective and ask ourselves âinstead of weakening the return type, what if we *strengthen* the function parameters?â We communicated that via accepting a `NonZeroF32`. Instead of having the validation code in our functions, we instead push that responsibility to the caller. The validation now happens before the function execution.

To see the advantage of pushing the validation forward to the user, letâs say we have another function like so:

```
// The quadratic formula!



fn roots(a: f32, b: f32, c: f32) -> [f32; 2] {



// For the sake of demonstration we will be ignoring complex roots



let discriminant = b * b - 4 * a * c;



-b + discriminant.sqrt() / (2 * a),



-b - discriminant.sqrt() / (2 * a),
```

This function can fail if the discriminant is negative (which we will be ignoring in this contrived example), and if `a` is zero. The two ways of going about this can be written as follows:

```
fn try_roots(a: f32, b: f32, c: f32) -> Option<[f32; 2]> {



if a == 0 { return None; }



fn newtyped_roots(a: NonZeroF32, b: f32, c: f32) -> [f32; 2] {
```

The `Option` version has me duplicating the conditional for at least two different functions, which might be icky if you are a DRY-hard. Also, not only the function has to validate if the float can be zero, the *caller* must then validate again by matching on the returned `Option`. That seems redundant. It would be ideal if we only need to check only once.

```
let roots = try_roots(5, 4, 7); // `try_roots` does a validation check



// and then we validate it again by matching on the result



Some(result) => do_something(),



None => { handle_error(); return },
```

The `NonZeroF32` version can help with that as validation happens before, and happens once, instead of twice.

```
// Handle the special case once



let Some(a) = NonZeroF32::new(5) else {



// `newtyped_roots` does not need to handle it again,



// indicated by the function not needing to return



// an `Option` and us handling the result.



let [root1, root2] = newtyped_roots(a, 4, 7);
```

Moving away from the `divide_floats`, letâs now use an example from the original blog post, converted to Rust:

```
fn get_cfg_dirs() -> Result<Vec<PathBuf>, Box<dyn Error>> {



let cfg_dirs_string = std::env::var("CONFIG_DIRS")?;



let cfg_dirs_list = cfg_dirs_string.split(',')



.collect::<Vec<PathBuf>>();



if cfg_dirs_list.is_empty() {



return Err("CONFIG_DIRS cannot be empty".into());



fn main() -> Result<(), Box<dyn Error>> {



let cfg_dirs = get_cfg_dirs()?;



Some(cache_dir) => init_cache(cache_dir),



None => unreachable!("should never happen; already checked configDirs is non-empty"),
```

Notice the following:

1. We checked if `cfg_dirs_list` is empty in the `get_cfg_dirs` function. Then, we still had to âcheckâ it again in the `main` function by matching on `cfg_dirs.first()`. The `Vec` was known to be nonempty, do we have to check it again? Consequently, doesnât this have an impact on performance, especially if we have to check it again and again and again?
2. The original post raised a good point about resilience to refactors. If for some reason the `is_empty` gets refactored out for some reason, and the programmer forgot to update `main`, then the `unreachable!` branch might actually get reached and explode your computer or whatever.

If we instead had a special `NonEmptyVec<T>` newtype (well, not exactly special) where its existence guarantees that the Vec is never empty, we could do

```
struct NonEmptyVec<T>(T, Vec<T>);



// Notice that we don't need to return an `Option`



fn first(&self) -> &T { ... }



fn get_cfg_dirs() -> Result<NonEmptyVec<PathBuf>, Box<dyn Error>> {



let cfg_dirs_string = std::env::var("CONFIG_DIRS")?;



let cfg_dirs_list = cfg_dirs_string.split(',')



.collect::<Vec<PathBuf>>();



// We parse the `Vec` into a more structured type



let cfg_dirs_list = NonEmptyVec::try_from(cfg_dirs_list)?;



fn main() -> Result<(), Box<dyn Error>> {



let cfg_dirs = get_cfg_dirs()?;



// Notice that we don't have to check again if the `Vec`



// was empty, since we guarantee that via the `NonEmptyVec` type



init_cache(cfg_dirs.first());
```

In this context, we can call `NonZeroF32::new` and `NonEmptyVec::try_from` *parsing* functions, since they validate and convert the less semantic type to a type with more meaning imbued into it. That is, nonzeroness of a float and nonemptiness of a `Vec` is now encoded into a type. You can just see the word `NonZeroF32` and therefore understand that going forward it is always be an `f32` that is never zero.

Validation and checking functions on the other hand, well, just validate the value and leave the type as that. If I have a `is_nonzero(f32) -> bool` function, then thereâs not really much of a readable difference between an `f32` that has `is_nonzero` called on it versus and an `f32` that hasnât.

```
fn is_nonzero(n: f32) -> bool;



fn to_nonzero(n: f32) -> Option<NonZeroF32>;
```

By taking advantage of the existence of a nominative type system, we can communicate that this `f32` is not zero by *parsing* it to a new type, as opposed to just *validating* it. If you only validate it, then you still canât tell if `f32` was nonzero unless you dig through the code. However, if you parsed it, you can say itâs always be nonzero if you see `NonZeroF32` in your code.

Examples in the wild [#](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#examples-in-the-wild)
-------------------------------------------------------------------------------------------------------------------------------------

Of course, the above examples are very much contrived, but is there an instance where creating newtypes is helpful? Yes. In fact, most people have used it. Itâs called a `String`.

If we dig into the internals, [`String`](https://doc.rust-lang.org/src/alloc/string.rs.html#360) is just a newtype over the `Vec<u8>` type:

```
#[derive(PartialEq, PartialOrd, Eq, Ord)]



#[stable(feature = "rust1", since = "1.0.0")]
```

Itâs parsing function is [`String::from_utf8`](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8), which contains the validation code for checking if the byte vector is valid UTF-8.

```
#[stable(feature = "rust1", since = "1.0.0")]



#[rustc_diagnostic_item = "string_from_utf8"]



pub fn from_utf8(vec: Vec<u8>) -> Result<String, FromUtf8Error> {



match str::from_utf8(&vec) {



Ok(..) => Ok(String { vec }),



Err(e) => Err(FromUtf8Error { bytes: vec, error: e }),
```

So instead of passing around a `Vec<u8>` around and validating all over the place, just parse into a `String` and you can be assured with having a type-safe `String` with all the convenience functions you can get.

Another example is `serde_json`. In Python, `json.loads` simply give you a dictionary. This is fine, especially if the data is sufficiently arbitrary, but if you have a schema and a type system, itâs better to let the type system do the work of parsing `json`.

In our terminology, validation looks like this:

```
use serde_json::{from_str, Value};



const SAMPLE_JSON: &str = r#"{ "foo": 1, "bar": [1, 2, 3] }"#;



let json = from_str::<Value>(SAMPLE_JSON)



let first_elem = json.get("bar")



.and_then(|bar| bar.get(0))



// do stuff with `first_elem`
```

Thatâs two `unwrap`s! One for checking if the string is valid json and the other is for checking if the `bar` field exists. Now consider this example where we use the parsing mechanic instead via types and the `Deserialize` derive macro.

```
fn first_elem(&self) -> i32 {



self.bar[0] // does not panic, by definition



let json = from_str::<Sample>(SAMPLE_JSON).unwrap();



let first_elem = json.first_elem();



// do stuff with `first_elem`
```

Since we deserialized the `json` file into an actual type, we can safely make these guarantees:

1. The `foo` and `bar` always exist in the `json` string we parse.
2. `foo` always has an integer value.
3. `bar` is always an array of three integers.
4. `first_elem` will never panic since all elements of an array is always initialized, and indexing into the first the element of a nonzero-length array will always be successful.

The only point of failure here is pushed upfront, where the `from_str` happens. After that point, thereâs not really much error handling to be done here, since the validation is now represented at the type level instead of at the function level.

Maxims of Type Driven Design [#](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#maxims-of-type-driven-design)
-----------------------------------------------------------------------------------------------------------------------------------------------------

With that said, what lessons can we learn from here? Turns out, most functional language programmers already have learned several lessons, and Rust is not much different in terms of applying such FP concepts to the language.

First lesson we can learn is that **we should make illegal states unrepresentable**.

What do we mean by that?

To refer back to the `NonZeroF32` and `NonEmptyVec` examples, we say the state of being zero is illegal for `NonZeroF32` and the state of being empty is illegal for `NonEmptyVec`. And as illegal states, they cannot be represented in such types. Thatâs why the only constructors available for these types are fallible; the value either parsed successfully, or it failed and does not return the new types.

If we only do validation, like checking if `f32` is nonzero for example, then the illegal state can still be represented. Thereâs a small possible that the value is zero, especially after some refactors when the conditional checks are accidentally or intentionally removed in some places.

This reminds me of how other languages use integers as sentinel values. Given this code snippet from [Wikipedia](https://en.wikipedia.org/wiki/Sentinel_value):

```
int find(int arr[], size_t len, int val) {



for (int i = 0; i < len; i++) {
```

The error is returned as `-1`, since indexing arrays is only valid for nonnegative integers. Seems weird as (1) the numbers -2 and below *can* exist, but not actually valid, and (2) treating certain values as special seems too error-prone, as in the future it could be that negative number can become semantically valid.

Second lesson we can learn is that **proving invariants should be done as early as possible**.

Thereâs this concept called [*shotgun parsing*](http://langsec.org/papers/langsec-cwes-secdev2016.pdf) where the linked paper describes it as follows:

> Shotgun Parsing: Shotgun parsing is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing codeâthrowing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the âbadâ cases.

Essentially, it describes the problem of usage of data without previous validation of its entirety of data. You could act on a part of the data that is validated beforehand, but discover that another part of the data is invalid.

The paper mentions [CVE-2016-0752](https://nvd.nist.gov/vuln/detail/CVE-2016-0752), which is a bug that allows attackers to read arbitrary files because you can use `..` in the input. The paper argues that treating validation as emergent and not deliberate can lead to security bugs like these.

If we treat validation as deliberate, then it should happen as early as possible and as comprehensive as possible. By parsing first, every invariant can be proven first before executing on said data.

I remember this [video](https://youtu.be/ViPNHMSUcog) about lambda calculus. It concludes that types can be represented as propositions in logic, and terms as proofs. I recommend watching the video, as it is eye-opening to me and maybe it can help you realize some things too.

Fundamentally, if your program typechecks properly, then you can say that the proof is correct. Thank you Curry-Howard Correspondence. There are proof assistant programming languages that can help with this like [Lean](https://lean-lang.org/) and [Agda](https://wiki.portal.chalmers.se/agda/pmwiki.php), but you can emulate this in Rust anyway. Thatâs how some weird libraries like the [typenum](https://crates.io/crates/typenum) crate work.

```
use typenum::*; // 1.19.0



type Lhs = <P3 as Add<P4>>::Output;



type Result = <Lhs as Same<Rhs>>::Output;



pub fn is_proof_correct()
```

This is a simple [program](https://play.rust-lang.org/?version=stable&mode=debug&edition=2024&gist=ed2a899a9bd9806f655df5623581ad97) in Rust where I check if `3 + 4` is equal to `8`. Obviously this is not correct, and so it will appropriately give you a compile error.

```
Compiling playground v0.0.1 (/playground)



error[E0277]: the trait bound `PInt<UInt<UInt<UInt<UTerm, B1>, B1>, B1>>: Same<PInt<UInt<..., ...>>>` is not satisfied



|     ^^^^^^ unsatisfied trait bound



= help: the trait `typenum::Same<PInt<UInt<UInt<UInt<UInt<UTerm, B1>, B0>, B0>, B0>>>` is not implemented for `PInt<UInt<UInt<UInt<UTerm, B1>, B1>, B1>>`



= note: the full name for the type has been written to '/playground/target/debug/deps/playground-e4f34f6f1769e3b6.long-type-6323804316620900.txt'



= note: consider using `--verbose` to print the full type name to the console



For more information about this error, try `rustc --explain E0277`.



error: could not compile `playground` (lib) due to 1 previous error
```

So sad that the error message is dogshit. Such is life.

What can we do? [#](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#what-can-we-do)
--------------------------------------------------------------------------------------------------------------------------

There are some recommendations I usually say to people on the RPLCS discord server, adapted from the original blog post.

First, just because a function accepts a type doesnât mean you have to use it in your structs, nor have to perpetually represent it as that type. For example, letâs say we have a third party library function that looks like this.

```
fn set_lightbulb_state(is_on: bool) {}
```

You *donât* have to store `bool` in your `App`/`Context` struct like `App { lightbulb_state: bool }`. Thatâs confusing. Iâd rather have you define a separate enum with more semantics imbued into it, like:

```
impl From<LightBulbState> for bool { ... }



lightbulb_state: LightBulbState



set_lightbulb_state(app.lightbulb_state.into());
```

Yeah, people can say it gets more verbose, but I rather care more about correctness instead. Sorry.

Second, I sometimes get suspicious about these kind of APIs:

```
fn do_something_fallible(data: &Thing) -> Result<(), MyError> {}



fn verify(data: &Thing) -> bool {}
```

If I see the function body does not do anything side-effectful, then itâs probable that parsing can help here turning `Thing` into a more structured datatype. And even for side-effectful stuff, there are some types that better represent certain situations, like infinite loop function representing their return types as `Result<!, MyError>` or `Result<Infallible, MyError>`.

Conclusion [#](https://www.harudagondi.space/blog/parse-dont-validate-and-type-driven-design-in-rust/#conclusion)
-----------------------------------------------------------------------------------------------------------------

I love creating more types. Five million types for everyone please.

I think itâs interesting that thereâs a lot of instances where types drive the design of Rust programs. Like how `Vec` has four layers of newtypes plus an additional field. `sqlx` generate anonymous structs in their `query!` macros. `bon` is a macro crate that converts functions into compile-time builders via types.

Of course, not everything is solvable via types. But personally I think pushing your verification code to types can help your code become clearer and more robust. Let the type system handle the validation for you. It exists, so might as well use it to its fullest extent.

Iâd like to thank Alexis King for this [article](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) where I first encountered this idea. Iâd love to follow up on this topic with an extension on this [sequel](https://lexi-lambda.github.io/blog/2020/11/01/names-are-not-type-safety/), and maybe recontextualizing in Rust via the `unsafe` keyword would be helpful.

Of course, newtyping is not the answer to all problems. Due to lack of ergonomic features to allow newtypingâlike [delegation](https://crates.io/crates/delegate)âmany people are somewhat averse to using the pattern. Nevertheless, if someone made a good enough RFC Iâd be happy to see it happen.

Using the type system as a compile-time checker because I want the compiler to help me write my programs is very nice. You should take advantage of the type system too, not many languages have it as good as Rust :)

---

 

---

### Liked this blog post and want some more? Consider donating to support the author!

---

 

---

 

---

 

---