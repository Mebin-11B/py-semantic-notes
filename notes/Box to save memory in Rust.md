---
title: "Box to save memory in Rust"
url: https://dystroy.org/blog/box-to-save-memory/
clipped: 2026-06-17 01:11:44
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Box to save memory in Rust](https://dystroy.org/blog/box-to-save-memory/)

## Digest Summary
The author reduced a Rust program’s memory use from 895 MB to 420 MB by restructuring deserialized JSON models. The AWS SDK JSON files are parsed into nested “Smithy” structs, many of which contain only optional `String` fields. Because `Option` for non‑pointer types still occupies the full size of `T`, keeping such structs directly in their parents inflated memory. By detecting structs that are empty (all optionals are `None`) and changing their fields to `Option>`, the empty value is stored as a single word pointer, and the heap allocation is avoided unless data exists. Custom Serde deserializers drop empty structs during parsing. This required updating `SmithyReference` and `SmithyShape` to use boxed options and adjusting accessors. Profiling with jemalloc confirmed a 475 MB saving, at the cost of modest CPU overhead and potential heap fragmentation. The technique demonstrates that, in Rust, boxing optional large structs can dramatically cut composite‑struct memory footprints while remaining compatible with Serde.

## Discussion Summary
The discussion emphasizes that Rust’s standard String type is a simple UTF‑8 byte vector, but memory usage can often be reduced by choosing alternatives such as Box, CompactString, or ColdString, depending on typical string lengths. Profiling tools like dhat‑rs are recommended for locating high‑cost allocations, and concerns are raised about potential heap fragmentation and the suitability of certain naming conventions. The overall tone advises cautious, data‑driven optimization rather than premature changes, noting that async state machines can also inflate memory footprints.

---

## Full Article

I saved 475 MB out of the 895 MB used by a real-world Rust program by changing the layout of some structs and the way I was deserializing JSON files.

The real use case
=================

My program deserializes all the JSON files of <https://github.com/awslabs/aws-sdk-rust/tree/main/aws-models> into "Smithy Shape" structs.

Those files contain thousands of structures similar to this one:

```
"com.amazonaws.iam#EnableOrganizationsRootSessionsResponse": {
    "type": "structure",
    "members": {
        "OrganizationId": {
            "target": "com.amazonaws.iam#OrganizationIdType",
            "traits": {
                "smithy.api#documentation": "<p>The unique identifier (ID) of an organization.</p>"
            }
        },
        "EnabledFeatures": {
            "target": "com.amazonaws.iam#FeaturesListType",
            "traits": {
                "smithy.api#documentation": "<p>The features you have enabled for centralized root access.</p>"
            }
        }
    },
    "traits": {
        "smithy.api#output": {}
    }
},
```

As is common in Rust, my program uses the very convenient [serde](https://docs.rs/serde/latest/serde/).

I won't go into every details, but part of the structure needs to be shown at this point for clarity.

Don't read it entirely, just note that it's a bunch of structs containing structs, some optional, with serde attributes:

```
#[derive(Clone, Deserialize, Serialize)]
pub struct SmithyShape {
    #[serde(rename = "type")]
    pub shape_type: SmithyShapeType,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    pub operations: Vec<SmithyReference>,
    #[serde(default)]
    pub members: FxHashMap<String, SmithyReference>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub key: Option<SmithyReference>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub value: Option<SmithyReference>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub member: Option<SmithyReference>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub input: Option<SmithyReference>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub output: Option<SmithyReference>,
    #[serde(default)]
    pub traits: SmithyTraits,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SmithyReference {
    pub target: ShortShapeId,
    #[serde(default)]
    pub traits: SmithyTraits,
}

#[derive(Debug, Clone, Default, Deserialize, Serialize)]
pub struct SmithyTraits {
    #[serde(rename = "smithy.api#title", skip_serializing_if = "Option::is_none")]
    pub title: Option<String>,
    #[serde(rename = "aws.api#service", skip_serializing_if = "Option::is_none")]
    pub service: Option<SmithyServiceTrait>,
    #[serde(
        rename = "smithy.api#sensitive",
        skip_serializing_if = "Option::is_none"
    )]
    pub sensitive: Option<SmithySensitiveTrait>,
    #[serde(
        rename = "smithy.api#documentation",
        skip_serializing_if = "Option::is_none"
    )]
    pub documentation: Option<String>,
    #[serde(rename = "smithy.api#pattern", skip_serializing_if = "Option::is_none")]
    pub pattern: Option<String>,
    #[serde(rename = "aws.iam#iamAction", skip_serializing_if = "Option::is_none")]
    pub iam_action: Option<SmithyIamAction>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct SmithyServiceTrait {
    pub sdk_id: Option<String>,
    pub arn_namespace: Option<String>,
    pub cloud_formation_name: Option<String>,
    pub cloud_trail_event_source: Option<String>,
    pub endpoint_prefix: Option<String>,
}
```

This is some standard looking code, the current practice, but we can also call it naÃ¯ve.
By deserializing this way, the structures were taking 895MB in memory.

An analysis shows that most optional strings are missing, and that's what I leveraged to drastically reduce the memory footprint.
But this requires to have in mind some Rust specificities, so a detour is needed:

About rust structs and memory
=============================

On a 64-bits platform, a word is made of 8 bytes. That's for example the memory needed to store a `usize`.

A String needs 3 words (address of the string, allocated size, and capacity) to which you need to add the allocated space for the string bytes.
That's 24 bytes for a String (you can check it with `dbg!(std::mem::size_of::<String>());`), excluding the actual string content on the heap.

There's a niche compiler optimization which makes an `Option<String>` the same size (basically an option of a pointer type doesn't need an added byte to know whether it's `None` because it's `None` when the pointer is zero).

So the following structure, when all strings are missing (`None`), takes exactly `120` bytes (`5*24`) in memory:

```
pub struct SmithyServiceTrait {
    pub sdk_id: Option<String>,
    pub arn_namespace: Option<String>,
    pub cloud_formation_name: Option<String>,
    pub cloud_trail_event_source: Option<String>,
    pub endpoint_prefix: Option<String>,
}
```

Now to struct composition.

Have a look at a struct "containing" another struct. To simplify, let's imagine it contains our `SmithyServiceTrait` and another field:

```
pub struct Container1 {
    pub some_string: Option<String>,
    #[serde(default)]
    pub trait: SmithyServiceTrait,
}
```

The minimal size is, quite expectedly, `24+120 = 144` bytes.

But our `SmithyShape` only contains optional structs.
What happens if we change our `Container` struct to use an `Option<SmithyServiceTrait>` ?

```
pub struct Container2 {
    pub some_string: Option<String>,
    #[serde(default)]
    pub trait: Option<SmithyServiceTrait>,
}
```

What's the size of a container when both `some_string` and `trait` are `None` ?

It's the same as the one of Container1, there's no memory gain in having an option (in fact, we're even lucky that our `SmithyServiceTrait` which contains only `Option<String>` can allow the compiler to elide the additional byte).

Applying this to our `SmithyTraits`, we see why a standard implementation balloons in memory.

This differs fundamentally from class composition in languages like Java, Python, JavaScript, etc.

In such language, when you have:

```
class Container {
    String someString;
    SmithyServiceTrait trait,
}
```

Then a `null` trait takes only one pointer-sized word in memory.

To allow our Rust `Container` to take only one word for the optional content when there's nothing to store, we need basically to do as is done in the languages we want to mimic: we need to put this content on the heap, outside of the container:

```
pub struct Container3 {
    pub some_string: Option<String>,
    pub trait: Option<Box<SmithyServiceTrait>>,
}
```

Now, when both `some_string` and `trait` are `None`, a container takes only 32 bytes in memory (3 words for the `Option<String>`, one for the `Option<Box<...>>`).

The niche optimization I mentioned before applies to `Option<Box<...>>` too: it doesn't consume more than a simple `Box<...>`.

The changes that recovered the memory
=====================================

Basically, the change consists in

* Detecting when structs are useless (i.e. when all their fields are `None`)
* Making them optional in their parent struct, and moving them to the heap
* Implementing a custom Deserializer to not store empty useless structs

So

```
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SmithyReference {
    pub target: ShortShapeId,
    #[serde(default)]
    pub traits: SmithyTraits,
}
```

becomes

```
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SmithyReference {
    pub target: ShortShapeId,
    #[serde(
        default,
        deserialize_with = "deserialize_boxed_traits",
        serialize_with = "serialize_boxed_traits"
    )]
    pub traits: Option<Box<SmithyTraits>>,
}

fn deserialize_boxed_traits<'de, D: Deserializer<'de>>(
    deserializer: D
) -> Result<Option<Box<SmithyTraits>>, D::Error> {
    let traits = SmithyTraits::deserialize(deserializer)?;
    if traits.is_empty() { // i.e. when all optional strings are none
        Ok(None)
    } else {
        Ok(Some(Box::new(traits)))
    }
}
```

Similarly, `SmithyShape` was changed to replace all `Option<SmithyReference>` by `Option<Box<SmithyReference>>`, some accessors were modified due to options in the way, and that's it, that's how the memory needed to store all deserialized AWS shapes was reduced twofold, sparing 475 MB.

A few notes:

* this deserialization costs more in CPU as the object is deserialized before being discarded. It turns out that the trade-off is a full-win as not having to hunt for memory made the complete task faster even with this added step.
* a lot of boxes means a fragmented heap. In such case it's not a problem but this might be worth keeping in mind.

Verification: Proving the Impact
================================

With experience, you get an intuition of where to save space, and roughly how much.
But to work seriously, you need to check that what you did worked, and verify it was worthwhile.
So you need to measure.

There's no simple and light way in Rust to know the total space taken by a composite object following all pointers.

Here, my solution was to use an allocator which gives information about its state (I used jemalloc because the standard allocator provides limited visibility into internal statistics), and compare the memory used before deserialization to the memory used after.

As I don't always want to use this allocator, I defined a "profile" feature in my Cargo.toml:

```
[features]
profile = ["tikv-jemallocator", "tikv-jemalloc-ctl"]

[dependencies]
tikv-jemallocator = { optional = true, version = "0.6", features = ["stats", "profiling"] }
tikv-jemalloc-ctl = { optional = true, version="0.6", features = ["stats"] }
```

And I declare the use of this allocator in my main.rs:

```
#[cfg(feature = "profile")]
#[global_allocator]
static ALLOC: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;
```

Then, in my function deserializing all those shapes, I do the measures:

```
#[cfg(feature = "profile")]
fn allocated_mb() -> usize {
    tikv_jemalloc_ctl::epoch::advance().unwrap();
    tikv_jemalloc_ctl::stats::allocated::read().unwrap_or(0) / (1024 * 1024)
}

#[cfg(feature = "profile")]
let base = allocated_mb();

... load all the shapes ...

#[cfg(feature = "profile")]
eprintln!(
    "Memory used for the shapes = {} MB (total)",
    allocated_mb() - base
);
```

Tip: [tikv\_jemalloc\_ctl](https://docs.rs/tikv-jemalloc-ctl/latest/tikv_jemalloc_ctl/stats/index.html) exposes many more details that may be interesting to follow in a server application

Conclusion: what's to remember, in a few words
==============================================

Summarized, here's what any Rust developper needs to understand and remember:

* Composite structs can consume significant memory
* It can pay to make a `field: BigStruct` optional by detecting when its content doesn't matter
* A `field: Option<BigStruct>` takes at least the space of the `BigStruct` even when it's `None`
* You can break the chain by boxing with `field: Option<Box<BigStruct>>` (then a `None` takes only a word in the parent struct)
* Those optimizations are still possible when deserializing with Serde