---
title: "Lily Programming Language"
url: https://lily-lang.org
clipped: 2026-06-17 01:48:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Lily Programming Language](https://lily-lang.org)

## Digest Summary
Lily is a statically‑typed language that uses an interpreter as a reference implementation. Memory is managed primarily through reference counting, with a garbage‑collection fallback. Core language features include built‑in template mode, C embedding/extending, single‑inheritance classes, exceptions, generics, and algebraic data types; `Option` and `Result` types are provided by default. The example demonstrates these capabilities by defining a dictionary of arithmetic operators, a function `rpn` that parses a space‑separated string into Reverse Polish Notation, and uses pattern matching, optional parsing, stack manipulation, and exception handling. `rpn` returns a `Result` containing either a success with a list of integers or a failure with an error message, handling cases such as stack underflow, invalid operators, division by zero, and unexpected errors. Sample calls illustrate successful evaluations and error responses.

## Discussion Summary
Please provide the comments you would like summarized.

---

## Full Article

Lily is **statically-typed**, with an interpreter as a reference. Lily uses
**reference counting** for memory management with **garbage collection** as a
fallback.

Key features of Lily:

* Embed/extend in C
* Single-inheritance classes
* Exceptions
* Generics
* Algebraic data types (with `Option` and `Result` predefined).

Here's a small example showing most of Lily's features:

```
var math_ops = ["+" => (|a: Integer, b: Integer| a + b),
                "-" => (|a, b| a - b),
                "*" => (|a, b| a * b),
                "/" => (|a, b| a / b)]

define rpn(input: String): Result[String, List[Integer]]
{
    var values = input.split(" ")
    var stack: List[Integer] = []

    for v in values: {
        with v.parse_i() as Some(s): {
            s |> stack.push
        else:
            if stack.size() < 2: {
                return Failure("Stack underflow.")
            }

            var right = stack.pop()
            var left = stack.pop()
            try: {
                var op_fn = math_ops[v]
                var op_value = op_fn(left, right)
                stack.push(op_value)
            except KeyError:
                return Failure("Invalid operation {}.".format(v))
            except DivisionByZeroError:
                return Failure("Attempt to divide by zero.")
            except Exception:
                return Failure("Unexpected error from op {}.".format(v))
            }
        }
    }

    return Success(stack)
}

print("1 2 3 4 * + -"  |> rpn) # Success([-13])
print("2 2 2 2 * *"    |> rpn) # Success([2, 8])
print("*"              |> rpn) # Failure("Stack underflow.")
print("1 2 ?"          |> rpn) # Failure("Invalid operation ?.")
```