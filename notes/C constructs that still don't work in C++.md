---
title: "C constructs that still don't work in C++"
url: https://lospino.so/blog/c-constructs-that-still-dont-work-in-cpp/
clipped: 2026-06-17 00:58:02
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [C constructs that still don't work in C++](https://lospino.so/blog/c-constructs-that-still-dont-work-in-cpp/)

## Digest Summary
- C++20 added designated initializers, but they apply only to direct non‑static members, must follow declaration order, and cannot mix with positional initializers; out‑of‑order, array, and nested designators that C99 allows remain invalid.  
- C23 removes the old “no‑prototype” function syntax; a declaration without a parameter list now behaves like `void f(void)`, matching C++ and causing older C code to fail if it relied on the previous rule.  
- `malloc` still returns `void*` that must be cast in C++, and object lifetime rules differ: C++20 creates implicit‑lifetime objects for trivial aggregates, but constructors, initialization, and exception safety are not provided; proper construction/destruction should use placement‑new or high‑level facilities such as `std::make_unique`.  
- `const_cast` only removes constness from the type system; writing through the resulting pointer is undefined if the original object is truly const.  
- Enumerations: C enumerators have integer type, with an implementation‑defined underlying type; C++ treats enums as distinct types, requiring explicit casts for integer↔enum conversion, and recommends `enum class` for C++ APIs.  
- `restrict` is a C qualifier with no standard C++ equivalent; use compiler‑specific extensions in isolated boundaries if needed.  
- Flexible array members are valid C only; in C++ replace them with `std::vector` or `std::span` and preserve the C layout only at ABI boundaries.  
- Migration guidelines: explicitly label language mode, avoid assuming C works in C++, consider ownership and lifetime, and confine non‑portable extensions to tested, named boundaries.

## Discussion Summary
The comment outlines several incompatibilities that prevent C headers from being directly usable in C++, citing differences in atomic definitions, noreturn syntax, inline semantics, and the absence of anonymous structs in C++. It notes that many of these divergences are intentional from the C++ perspective, though some remain surprising because they disrupt historically common C patterns. The author highlights philosophical shifts such as object‑lifetime handling, stronger type systems, and ABI assumptions, and expresses particular interest in which C features, especially `restrict`, programmers still miss in modern C++.

---

## Full Article

C++ | May 20, 2026

C Constructs That Still Don’t Work in C++ — and a Few That Changed
==================================================================

A 2026 sequel to C Constructs That Don't Work in C++: what still breaks, what C++20 changed, and what C23 changed.

In 2019 I wrote a [short survey of C constructs that do not work in
C++](https://lospino.so/c/c++/programming/developing/software/2019/04/28/c-constructs-that-dont-work-in-cpp.html).
The point was not that C is sloppy or that C++ is superior. The point was that
C++ is not a superset of C, and that C programmers crossing the border should
know where the checkpoints are.

That advice still holds. But the border moved.

C++20 picked up a version of designated initializers. C++20 also repaired some
low-level object-lifetime cases around `malloc` that used to be easy to
describe incorrectly. C23, meanwhile, changed the old empty-parameter-list rule
that made `void f()` mean something dangerously different in C than in C++.

The practical lesson is the same, but sharper: when you discuss C/C++
compatibility, label the language mode. “Valid C” and “valid C++” are not
precise enough anymore. You often need to say C17, C23, C++17, C++20, or
C++23.

I also put the examples behind this post in a small
[companion repository](https://github.com/JLospinoso/c-constructs-still-dont-work-cpp).
The repository is for repeatable checks; its
[Compiler Explorer links](https://github.com/JLospinoso/c-constructs-still-dont-work-cpp/blob/main/docs/godbolt-links.md)
are for quick diagnostics.

Compatibility matrix
--------------------

Here is the short map. Details follow. The point is not just that C++ is not a
superset of C. The point is that some of the canonical examples people still
repeat changed under C++20 or C23, so the correct answer now depends on the
language mode. This table is a map, not a substitute for the examples; on
narrow screens, the sections below are easier to read than the full matrix.

| Status | Construct | C17 | C23 | C++17 | C++20 / C++23 | Practical advice |
| --- | --- | --- | --- | --- | --- | --- |
| Still different | `void*` to object pointer | Implicit conversion from `malloc` is idiomatic C. | Same. | No implicit conversion. | Same. | In C++, do not make `malloc` your default allocation strategy. If you must use it, cast deliberately and handle lifetime deliberately. |
| Changed since 2019 | `malloc` and object lifetime | C allocation creates storage used as objects by C’s rules. | Same broad C model. | Easy to write code that compiles with a cast but has no C++ object lifetime. | Some implicit-lifetime cases are repaired. Constructors still are not called. | Distinguish storage, lifetime, initialization, ownership, and destruction. |
| Still different | Discarding `const` | Constraint violation; compilers often warn. | Same basic concern. | Ill-formed without a cast. | Same. | A cast may compile. It does not make writes to actually-`const` objects defined. |
| Changed in C23 | Enums | Enumerator constants are integer-like; enum objects convert freely enough to surprise C++ programmers. | C23 adds fixed underlying types and more explicit typing rules for enumerators. | Enum types are distinct; `int` to enum is not implicit. | Same; `enum class` remains stricter. | Use `enum class` for C++ APIs. Use plain enums only when ABI or C interop demands it. |
| Changed in C23 | `void f()` | No prototype in the old sense; mismatched calls may compile, but are not defined. | Behaves as though declared with `void`. | Means no parameters. | Same. | For shared headers, still write `void f(void)` in C-facing APIs unless you control the language mode. |
| Changed since 2019 | Designated initializers | Full C-style designated initialization, including out-of-order, array, nested, and mixed forms. | Same family, with C23 evolution elsewhere. | Not standard C++. | Standard, but narrower than C. | Useful in C++20, but only for aggregates, direct members, declaration order, and all-designated clauses. |
| Extension trap | `restrict` | Standard C99 qualifier. | Still standard C, with C23 wording updates. | Not standard C++. | Not standard C++. | Use compiler extensions only behind a portability boundary. |
| Still different | Flexible array members | Standard C99 trailing-array pattern. | Still standard C. | Not standard C++. | Not standard C++. | Keep the C layout at the ABI edge; translate into `span`, `vector`, or an explicit header/payload representation. |

Designated initializers: yes, but not C’s version
-------------------------------------------------

The 2019 post said designated initializers were not available in C++, with a
note that they were likely coming in C++20. That note aged well.

C++20 added designated initializers for aggregate initialization. This is valid
C++20:

```
struct Address {
  const char* street;
  const char* city;
  const char* state;
  int zip;
};

Address white_house{
  .street = "1600 Pennsylvania Avenue NW",
  .city = "Washington",
  .state = "District of Columbia",
  .zip = 20500,
};
```

This is not the same feature C programmers are used to.

C++ designators must name direct non-static data members, and they must appear
in declaration order. That means this out-of-order form remains invalid C++:

```
struct Options {
  int timeout_ms;
  bool verbose = false;
  int retries = 0;
};

Options o{
  .retries = 3,       // invalid C++20: out of declaration order
  .timeout_ms = 5000,
};
```

C also permits patterns that C++ still rejects, including array designators and
nested designators:

```
int table[4] = { [2] = 99 }; // valid C, invalid C++

struct Inner { int value; };
struct Outer { struct Inner inner; };
struct Outer o = { .inner.value = 7 }; // valid C, invalid C++
```

C also lets you mix positional and designated clauses in the same initializer:

```
struct Triple {
  int first;
  int second;
  int third;
};

struct Triple t = { 1, .third = 3 }; // valid C, invalid C++
```

In C++20, the analogous aggregate initialization is ill-formed:

```
struct Triple {
  int first;
  int second;
  int third;
};

Triple t{1, .third = 3}; // invalid C++20: mixed designated and positional clauses
```

This is not arbitrary. C++ has constructors, destructors, default member
initializers, references, and an order-of-initialization model that code can
observe. C-style freedom would collide with the C++ object model.

There are proposals to loosen the C++ rules, including out-of-order designated
initializers and base-class designated initialization. Treat those as proposals.
Do not write portable C++ on the assumption that they have landed.

Rule: C++20 designated initializers are great for plain aggregate configuration
objects. They are not a drop-in replacement for C99 designated initialization.
C++20’s form is not “C designators, now in C++.” It is a constrained
aggregate-initialization feature. The useful mental model is: direct members,
declaration order, and do not mix designated and non-designated clauses.

Empty parameter lists: C moved toward C++
-----------------------------------------

This used to be one of the cleanest examples of C and C++ disagreement.

In C++:

```
void fn();

fn(42); // invalid C++: fn takes no arguments
```

In C17 and earlier, `void fn();` did not provide a prototype. A definition
written `void fn() {}` specified no parameters, but calls made through a
non-prototype declaration were not checked the way C++ programmers expect. Such
a call might compile after default argument promotions, but if the number of
supplied arguments does not match the number of parameters, the behavior is
undefined:

```
void fn() { }

int main(void) {
  fn(42); // may compile in C17 mode; undefined for this definition
}
```

C23 removes the old split: a function declarator without a parameter type list
behaves as if it used `void`, provides a prototype, and the argument count must
agree.

That is a real compatibility improvement. It also creates a migration wrinkle:
older C code may compile in C17 mode and fail in C23 mode. That is good failure,
but it is still failure.

Rule: in C-facing headers, `void fn(void)` remains the least surprising
spelling. In C++-only code, `void fn()` is fine.

`void*`, `malloc`, and the object-lifetime trap
-----------------------------------------------

The simple incompatibility is unchanged. C lets you write this:

```
int* values = malloc(100 * sizeof *values);
```

C++ does not implicitly convert `void*` to `int*`:

```
int* values = std::malloc(100 * sizeof *values); // invalid C++
```

You can cast:

```
auto* values = static_cast<int*>(std::malloc(100 * sizeof(int)));
```

But the cast is not the interesting part. The interesting part is lifetime.

In current C++, the sharp edge is not “`malloc` can never give you objects.”
C++20 narrowed that. Some operations, including C allocation functions, are
specified to implicitly create objects of implicit-lifetime types if doing so
would make the program defined; the draft’s example is essentially a trivial
aggregate returned by `std::malloc` and then assigned through its members. That
repair is deliberately limited: it does not run constructors, initialize scalar
values, establish invariants, or start lifetimes for subobjects that are not
themselves implicit-lifetime types. For non-implicit-lifetime types, storage is
still just storage until construction happens.

So this kind of code is no longer the best scare example in C++20:

```
#include <cstdlib>

struct X {
  int a;
  int b;
};

X* make_x() {
  auto* p = static_cast<X*>(std::malloc(sizeof(X)));
  p->a = 1;
  p->b = 2;
  return p;
}
```

For an implicit-lifetime type like `X`, C++20 repairs the lifetime issue. That
does not make `malloc` idiomatic C++.

The repair does not call constructors. It does not initialize values. It does
not give you exception safety. It does not pair ownership with destruction. It
does not make this OK:

```
#include <cstdlib>
#include <string>

void bad() {
  auto* s = static_cast<std::string*>(std::malloc(sizeof(std::string)));
  *s = "hello"; // undefined behavior: no std::string object was constructed
}
```

The safe low-level C++ spelling is explicit:

```
#include <memory>
#include <new>
#include <string>

void* storage = ::operator new(sizeof(std::string));
auto* s = new (storage) std::string("hello");

std::destroy_at(s);
::operator delete(storage);
```

The better high-level spelling is usually simpler:

```
auto s = std::make_unique<std::string>("hello");
```

Rule: a cast from `void*` is never the whole story. Ask five questions: who owns
the storage, when does the object lifetime begin, how is the object initialized,
who destroys it, and what happens on failure?

`const_cast`: compiles is not the same as defined
-------------------------------------------------

The old post pointed out that C++ forces you to be explicit when discarding
`const`:

```
const int x = 100;
int* p = &x; // invalid C++
```

You can write the cast:

```
const int x = 100;
int* p = const_cast<int*>(&x);
```

But this only removes the type-system barrier. It does not change the object.
Writing through `p` is undefined behavior because `x` is actually a `const`
object.

There is a valid use case:

```
int x = 100;
const int* view = &x;
int* p = const_cast<int*>(view);
*p = 101; // defined: the original object is not const
```

That distinction matters in legacy integration. Sometimes a C API takes `char*`
even though it promises not to mutate the buffer. A `const_cast` at that
boundary can be the least-bad option. Put it at the edge, document it, and keep
it out of the core logic.

Do not use this trick for string literals, memory-mapped read-only storage, or
objects originally declared `const`. If the legacy function actually writes,
the cast only moves the bug.

Rule: `const_cast` is not a permission slip. It is a localized escape hatch.

Enums: less simple than “C uses int”
------------------------------------

The old shorthand “C enum values are backed by `int`” is too compressed for a
2026 version of this article. For C17, the safer shorthand is: enumerator
constants have integer type, while the enumerated type itself is compatible with
an implementation-defined integer type capable of representing its values. C23
makes the model more explicit: every enumeration has an underlying type, a
fixed underlying type can be written, and the type of an enumeration constant
after completion depends on whether the enumeration has a fixed underlying type
and whether the values fit in `int`.

That is still not C++‘s model. In C++, an enumeration is a distinct type. An
unscoped enumerator, or an object of unscoped enumeration type, can participate
in integral promotion or conversion, but an arbitrary integer is not assignable
to the enum without a cast. A scoped enum does not implicitly convert to `int`
or `bool`.

```
enum Mode { off = 0, on = 1 };

int x = on; // OK: unscoped enum to int
Mode m = 1; // invalid C++: int to Mode is not implicit
```

If you need to cross from an integer representation, say so:

```
Mode m = static_cast<Mode>(1);
```

For C++ APIs, prefer scoped enums:

```
enum class Mode : unsigned {
  off = 0,
  on = 1,
};

int x = Mode::on; // invalid C++
auto y = static_cast<unsigned>(Mode::on); // explicit
```

Rule: use plain enums when they are part of a C ABI or when you intentionally
want old enum behavior. Use `enum class` when the enum is a domain type in C++.

`restrict`: a C promise, not a C++ contract
-------------------------------------------

C99 introduced `restrict` so a programmer could promise that a pointer is the
unique access path to an object for a period of execution. That promise can
unlock useful aliasing optimizations. If the promise is false, the behavior is
undefined.

Standard C++ has no `restrict` keyword. GCC and Clang support `__restrict__`
and `__restrict` as extensions. MSVC has `__restrict` for variables and
`__declspec(restrict)` for function declarations and definitions, with
return-value aliasing semantics. Treat all of these as toolchain contracts, not
portable C++ interface design.

Rule: if you need restrict-like semantics in C++, isolate the extension in a
small boundary, test it with the compilers you actually ship, and make the
aliasing precondition impossible to miss.

Flexible array members: keep them at the edge
---------------------------------------------

C99 also standardized flexible array members:

```
struct Packet {
  unsigned length;
  unsigned char payload[];
};
```

This is a good C pattern for a variable-length object with a fixed header and
trailing data. It is not standard C++.

Some C++ compilers accept flexible array members as extensions. That does not
make the code portable C++. It also does not solve the lifetime and ownership
questions that C++ is trying to force into the open.

In C++, usually choose one of these instead:

```
struct Packet {
  unsigned length;
  std::vector<std::byte> payload;
};
```

or, when the storage is owned elsewhere:

```
struct PacketView {
  unsigned length;
  std::span<const std::byte> payload;
};
```

At an ABI boundary, you may need to preserve the C representation. That is
fine. But keep it quarantined. Parse the C layout, validate lengths, then
translate into a C++ representation with explicit ownership or a bounded view.

Rule: flexible array members are a C layout tool. They are not a portable C++
object model.

Migration rules
---------------

When moving C habits into C++, I use these rules:

1. Label the language mode before making the claim.
2. Do not assume “works in C” means “is C++ with warnings.”
3. Do not confuse “compiles with a cast” with “has defined behavior.”
4. Treat `malloc` as storage, not construction.
5. Preserve C layouts at ABI boundaries, then translate into C++ types.
6. Prefer C++ constructs that make ownership and lifetime visible.
7. Use compiler extensions only behind named, tested portability boundaries.

The old lesson still stands: C++ is not a superset of C. The updated lesson is
more precise: the languages increasingly share syntax, but they do not share the
same object model, initialization model, or invariants.

That is where the bugs hide.

References
----------

* Original post: [C Constructs That Don’t Work in C++](https://lospino.so/c/c++/programming/developing/software/2019/04/28/c-constructs-that-dont-work-in-cpp.html)
* Companion examples: [C Constructs That Still Don’t Work in C++ repository](https://github.com/JLospinoso/c-constructs-still-dont-work-cpp)
* C23 working draft: [WG14 N3220](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf)
* C++ aggregate initialization and designated initializers: [C++ draft, dcl.init.aggr](https://eel.is/c++draft/dcl.init.aggr)
* C++ C allocation functions: [C++ draft, c.malloc](https://eel.is/c++draft/c.malloc)
* C++ object model and implicit object creation: [C++ draft, intro.object](https://eel.is/c++draft/basic.memobj)
* C++ object lifetime: [C++ draft, basic.life](https://eel.is/c++draft/basic.life)
* C++ cv-qualification and `const` modification: [C++ draft, dcl.type.cv](https://eel.is/c++draft/dcl.type.cv)
* C++ `const_cast`: [C++ draft, expr.const.cast](https://eel.is/c++draft/expr.const.cast)
* C++ enumeration declarations: [C++ draft, dcl.enum](https://eel.is/c++draft/dcl.enum)
* C17-era no-prototype call behavior: [WG14 N1570, 6.5.2.2 Function calls](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)
* C23 empty parameter list proposal: [WG14 N2841, No function declarators without prototypes](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2841.htm)
* Implicit object creation proposal: [WG21 P0593R6](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p0593r6.html)
* C++ designated initialization proposal: [WG21 P0329R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/p0329r4.pdf)
* GCC C++ restricted pointer extension: [GCC docs, Restricted Pointers](https://gcc.gnu.org/onlinedocs/gcc/Restricted-Pointers.html)
* MSVC `__restrict`: [Microsoft Learn, `__restrict`](https://learn.microsoft.com/en-us/cpp/cpp/extension-restrict?view=msvc-170)
* Out-of-order designated initializer proposal: [WG21 P3405R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3405r0.html)
* Base-class designated initializer proposal: [WG21 P2287R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2287r5.html)
* Secondary reference, C enumerations: [cppreference, C enum](https://en.cppreference.com/w/c/language/enum)
* Secondary reference, C `restrict`: [cppreference, restrict type qualifier](https://en.cppreference.com/w/c/language/restrict)
* Secondary reference, flexible array members: [cppreference, struct declaration](https://en.cppreference.com/w/c/language/struct)