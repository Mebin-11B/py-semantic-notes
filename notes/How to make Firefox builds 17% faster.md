---
title: "How to make Firefox builds 17% faster"
url: https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/
clipped: 2026-06-17 01:17:55
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How to make Firefox builds 17% faster](https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/)

## Digest Summary
The post describes adding a Lua‑based wrapper to Mozilla’s **buildcache** so that the Firefox WebIDL binding generation step can be cached. The WebIDL step runs `python3 -m mozbuild.action.webidl`, producing thousands of deterministic C++ files on every clobber build, making it suitable for caching. A small change in `dom/bindings/Makefile.in` conditionally passes `$(CCACHE)` (the buildcache command wrapper) to the `py_action` macro, causing the Python action to be invoked as `buildcache python3 …`. The accompanying `webidl.lua` script tells buildcache how to recognize the command, enumerate its input `.webidl` files and Python scripts (via `file‑lists.json` and `codegen.json`), and list its generated outputs, enabling direct‑mode hashing of inputs.

Benchmarking shows a warm build time reduction from ~5 min 35 s to 1 min 12 s, with the WebIDL cache shaving an additional ~15 s. Setup requires cloning the `buildcache‑wrappers` repository and adding its path to `~/.buildcache/config.json` or the `BUILDCACHE_LUA_PATH` environment variable, with a large `max_local_entry_size` to accommodate big Rust crate entries. The author plans to apply the same approach to other deterministic code‑generation steps in the Firefox build.

## Discussion Summary
The comments express mixed reactions to build‑caching efforts. Contributors note difficulties with caching Rust procedural macros and Windows builds, citing non‑determinism and low cache‑hit rates. Some argue that adding a cache layer is a temporary fix compared to improving the underlying build system, while others point out measurable gains such as a 17 % reduction in code size or faster compilation with tools like ccache. There is also skepticism about focusing on performance when broader concerns, such as user adoption, are seen as more critical.

---

## Full Article

In the [previous post](https://blog.farre.se/posts/2026/04/09/buildcache-with-mach/), I mentioned that buildcache has some unique properties compared to ccache and sccache. One of them is its [Lua plugin system](https://gitlab.com/bits-n-bites/buildcache/-/blob/master/doc/lua.md), which lets you write custom wrappers for programs that aren’t compilers in the traditional sense. With [Bug 2027655](https://bugzilla.mozilla.org/show_bug.cgi?id=2027655) now merged, we can use this to cache Firefox’s WebIDL binding code generation.

What’s the WebIDL step?
-----------------------

When you build Firefox, one of the earlier steps runs `python3 -m mozbuild.action.webidl` to generate C++ binding code from hundreds of `.webidl` files. It produces thousands of output files: headers, cpp files, forward declarations, event implementations, and so on. The step isn’t terribly slow on its own, but it runs on every clobber build, and the output is entirely deterministic given the same inputs. That makes it a perfect candidate for caching.

The problem was that the compiler cache was never passed to this step. Buildcache was only wrapping actual compiler invocations, not the Python codegen.

The change
----------

The fix in [Bug 2027655](https://bugzilla.mozilla.org/show_bug.cgi?id=2027655) is small. In `dom/bindings/Makefile.in`, we now conditionally pass `$(CCACHE)` as a command wrapper to the `py_action` call:

```
WEBIDL_CCACHE=
ifdef MOZ_USING_BUILDCACHE
WEBIDL_CCACHE=$(CCACHE)
endif

webidl.stub: $(codegen_dependencies)
	$(call py_action,webidl $(relativesrcdir),$(srcdir),,$(WEBIDL_CCACHE))
	@$(TOUCH) $@
```

The `py_action` macro in `config/makefiles/functions.mk` is what runs Python build actions. The ability to pass a command wrapper as a fourth argument was also introduced in this bug. When buildcache is configured as the compiler cache, this means the webidl action is invoked as `buildcache python3 -m mozbuild.action.webidl ...` instead of just `python3 -m mozbuild.action.webidl ...`. That’s all buildcache needs to intercept it.

Note the `ifdef MOZ_USING_BUILDCACHE` guard. This is specific to buildcache because ccache and sccache don’t have a mechanism for caching arbitrary commands. Buildcache does, through its Lua wrappers.

The Lua wrapper
---------------

Buildcache’s Lua plugin system lets you write a script that tells it how to handle a program it doesn’t natively understand. The wrapper for WebIDL codegen, [webidl.lua](https://github.com/farre/buildcache-wrappers/blob/main/mozilla/webidl.lua), needs to answer a few questions for buildcache:

* **Can I handle this command?** Match on `mozbuild.action.webidl` in the argument list.
* **What are the inputs?** All the `.webidl` source files, plus the Python codegen scripts. These come from `file-lists.json` (which `mach` generates) and `codegen.json` (which tracks the Python dependencies from the previous run).
* **What are the outputs?** All the generated binding headers, cpp files, event files, and the codegen state files. Again derived from `file-lists.json`.

With that information, buildcache can hash the inputs, check the cache, and either replay the cached outputs or run the real command and store the results.

The wrapper uses buildcache’s `direct_mode` capability, meaning it hashes input files directly rather than relying on preprocessed output. This is the right approach here since we’re not dealing with a C preprocessor but with a Python script that reads `.webidl` files.

Numbers
-------

Here are build times for `./mach build` on Linux, comparing compiler cachers. Each row shows a clobber build with an empty cache (cold), followed by a clobber build with a filled cache (warm):

| tool | cold | warm | with plugin |
| --- | --- | --- | --- |
| none | 5m35s | n/a | n/a |
| ccache | 5m42s | 3m21s | n/a |
| sccache | 9m38s | 2m49s | n/a |
| buildcache | 5m43s | 1m27s | 1m12s |

The “with plugin” column is buildcache with the `webidl.lua` wrapper active. It shaves another 15 seconds, bringing the total down to 1m12s. Not a revolutionary improvement on its own, but it demonstrates the mechanism. The WebIDL step is just the first Python action to get this treatment; there are other codegen steps in the build that could benefit from the same approach.

More broadly, these numbers show buildcache pulling well ahead on warm builds. Going from a 5m35s clean build to a 1m12s cached rebuild is a nice improvement to the edit-compile-test cycle.

These are single runs on one machine, not rigorous benchmarks, but the direction is clear enough.

Setting it up
-------------

If you’re already using buildcache with `mach`, the Makefile change is available when updating to today’s central. To enable the Lua wrapper, clone the [buildcache-wrappers](https://github.com/farre/buildcache-wrappers) repo and point buildcache at it via `lua_paths` in `~/.buildcache/config.json`:

```
{
"lua_paths": ["/path/to/buildcache-wrappers/mozilla"],
"max_cache_size": 10737418240,
"max_local_entry_size": 2684354560
}
```

Alternatively, you can set the `BUILDCACHE_LUA_PATH` environment variable. A convenient place to do that is in your mozconfig:

```
mk_add_options "export BUILDCACHE_LUA_PATH=/path/to/buildcache-wrappers/mozilla/"
```

The large `max_local_entry_size` (2.5 GB) is needed because some Rust crates produce very large cache entries.

What’s next
-----------

The Lua plugin system is the interesting part here. The WebIDL wrapper is a proof of concept, but the same technique applies to any deterministic build step that takes known inputs and produces known outputs. There are other codegen actions in the Firefox build that could get the same treatment, and I plan to explore those next.

#### Notes