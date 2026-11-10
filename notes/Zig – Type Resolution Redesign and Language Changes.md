---
title: "Zig – Type Resolution Redesign and Language Changes"
url: https://ziglang.org/devlog/2026/#2026-03-10
clipped: 2026-06-17 01:34:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Zig – Type Resolution Redesign and Language Changes](https://ziglang.org/devlog/2026/#2026-03-10)

## Digest Summary
The recent Zig devlog details a major 30 k‑line PR that overhauled the compiler’s internal type‑resolution, making it lazy: fields of never‑instantiated types aren’t examined, allowing constructs like `std.Io.Writer` to compile without pulling in unrelated `std.Io` code. Dependency‑loop diagnostics have been improved to show exact source locations and the loop length, aiding quick resolution. Incremental compilation received extensive bug fixes and elimination of “over‑analysis” cases, yielding noticeably faster rebuilds. Dozens of additional bug fixes, niche language tweaks, and performance optimizations accompany the change. 

The log also introduces experimental I/O backends (`std.Io.Evented` and `std.Io.Threaded`) based on userspace stack switching (fibers/green threads). Example programs demonstrate swapping the I/O implementation while keeping identical application logic, with `strace` output showing successful execution via `io_uring`. Using `std.Io.Evented` for the compiler works but currently incurs an unresolved performance regression. Overall, the changes streamline type handling, enhance error reporting, and expand I/O flexibility in Zig.

## Discussion Summary
No comments were provided, so there is no content to analyze or summarize.

---

## Full Article

This page contains a curated list of recent changes to main branch Zig.

May 30, 2026

Author: Matthew Lugg

Iâve spent the past few weeks working on our new ELF linker which debuted in Zig 0.16.0. At the time of the 0.16.0 release, this linker implementation was in its fairly early stages, and only really supported linking Zig-only code without any external libraries (even libc)âhence why it was (and still is) disabled by default (it can be enabled with `-fnew-linker`). However, quite a lot of progress has been made since that initial release!

Hereâs a nice milestoneâas of [my latest PR](https://codeberg.org/ziglang/zig/pulls/35533), the new ELF linker is capable of building the self-hosted Zig compiler with LLVM and LLD libraries enabled, a task which requires quite a few features under the hood.

```
[mlugg@nebula master]$ 
[mlugg@nebula master]$ zig build -Dno-lib -Dnew-linker -Denable-llvm
[mlugg@nebula master]$ 
[mlugg@nebula master]$ ./zig-out/bin/zig build-exe ~/hello.zig -fllvm -flld
[mlugg@nebula master]$ ./hello
Hello, World!
[mlugg@nebula master]$
```

Of course, an ELF linker isnât necessarily the most exciting thing in the world, which is why the headline feature of this new linker is its support for fast incremental compilation. After the recent enhancements, it is now possible (on x86\_64 Linux) to perform incremental rebuilds while linking external libraries, C sources, etcâwithout any additional performance overhead! Hereâs a clip of me trying it out on [Andrewâs Tetris clone](https://github.com/andrewrk/tetris):

[

](/devlog/2026/elf2-tetris-incremental.mp4)


A few silly changes to Andrewâs Tetris clone being built in around 30ms each.

Oh, and fast incremental rebuilds also work nicely on the Zig compiler itself:

```
[mlugg@nebula master]$ zig build -Dno-lib -Denable-llvm -fincremental --watch
Build Summary: 4/4 steps succeeded
install success
ââ install zig success
   ââ compile exe zig Debug native success 36s

Build Summary: 4/4 steps succeeded
install success
ââ install zig success
   ââ compile exe zig Debug native success 244ms

Build Summary: 4/4 steps succeeded
install success
ââ install zig success
   ââ compile exe zig Debug native success 228ms

Build Summary: 4/4 steps succeeded
install success
ââ install zig success
   ââ compile exe zig Debug native success 288ms

Build Summary: 4/4 steps succeeded
install success
ââ install zig success
   ââ compile exe zig Debug native success 283ms
```

The biggest missing feature of this linker implementation right now is that it still does not yet support generating DWARF debug information for Zig codeâthatâs definitely my next priority. But even without that support, itâs amazing just how useful instant rebuilds can be, for example in any situation where youâre doing a lot of print debugging.

If youâre using the master branch of Zig and youâre on x86\_64 Linux, consider trying out incremental compilation with the new ELF linker if it previously wasnât working with your project! I expect many codebases to already work great with it, unlocking the ability to rebuild your project in milliseconds. Of course, if you come across any bugs, please do [open an issue](https://codeberg.org/ziglang/zig/issues).

And if youâre currently sticking to tagged releases of Zig, donât worryâas Andrew mentioned in his last devlog, Zig 0.17.0 is just around the corner, so it wonât be long before you can try this too!

May 26, 2026

Author: Andrew Kelley

Big branch just landed: [separate the maker process from the configurer process](https://codeberg.org/ziglang/zig/pulls/35428)

This devlog entry is essentially a preview of the upcoming release notes, but serves as an advanced notice to those who want to help test out the new features and provide feedback that will guide the Zig project moving forward.

Before, `build.zig` files plus the build system implementation were all compiled into one bloated process, in Debug mode. After `build.zig` logic finished constructing a build graph in memory, the âbuild runnerâ code executed it.

Now, `build.zig` files are compiled into a small process (the âconfigurerâ) in debug mode. After this logic finishes constructing a build graph in memory, it is serialized to a binary configuration file. The parent `zig build` process is aware of this file and caches it for next time. While waiting for all that, it asynchronously compiles the build graph execution process (the âmakerâ) in release mode. Once the configuration file is available and the maker process is finished compiling, the maker process is executed, passing it the configuration file. The maker process only needs to be compiled once per `zig version` thanks to the global cache. The maker process then executes the build graph, which is contained within the serialized configuration file.

The primary motivation of this change was to make `zig build` faster, in three ways:

1. Only the userâs `build.zig` logic will be compiled with each change, rather than the entire build system along with it. This is starting to become more valuable now that we have introduced `--watch`, `--fuzz` and `--webui`. The build system can grow more features without making `zig build` take longer.
2. Now the build system can skip rerunning the `build.zig` logic entirely when it knows nothing will change, for example if you add `-freference-trace` to your `zig build` command line, it now avoids re-running your `build.zig` logic redundantly, using the same configuration as last time.
3. Now the process that actually executes the build graph is compiled with optimizations enabled.

To demonstrate points 2 and 3, here is the difference between running `zig build --help` before and after:

```
Benchmark 1 (34 runs): master/zig build -h
  measurement          mean Â± Ï            min â¦ max           outliers         delta
  wall_time           150ms Â± 5.52ms     145ms â¦  165ms          4 (12%)        0%
  peak_rss           84.8MB Â±  275KB    84.2MB â¦ 85.1MB          0 ( 0%)        0%
  cpu_cycles          593M  Â± 4.01M      588M  â¦  608M           2 ( 6%)        0%
  instructions        995M  Â± 52.5K      995M  â¦  995M           0 ( 0%)        0%
  cache_references   25.8M  Â±  165K     25.4M  â¦ 26.1M           0 ( 0%)        0%
  cache_misses        651K  Â± 20.1K      619K  â¦  697K           0 ( 0%)        0%
  branch_misses       918K  Â± 7.44K      906K  â¦  935K           0 ( 0%)        0%
Benchmark 2 (348 runs): branch/zig build -h
  measurement          mean Â± Ï            min â¦ max           outliers         delta
  wall_time          14.3ms Â±  744us    13.2ms â¦ 23.3ms          8 ( 2%)        â¡- 90.4% Â±  0.4%
  peak_rss           78.5MB Â±  562KB    77.1MB â¦ 81.4MB          7 ( 2%)        â¡-  7.4% Â±  0.2%
  cpu_cycles         24.1M  Â±  821K     22.8M  â¦ 27.1M           3 ( 1%)        â¡- 95.9% Â±  0.1%
  instructions       43.7M  Â± 23.8K     43.7M  â¦ 43.8M          56 (16%)        â¡- 95.6% Â±  0.0%
  cache_references   1.46M  Â± 14.6K     1.40M  â¦ 1.50M          19 ( 5%)        â¡- 94.3% Â±  0.1%
  cache_misses        142K  Â± 4.87K      127K  â¦  157K           2 ( 1%)        â¡- 78.1% Â±  0.4%
  branch_misses       126K  Â± 1.37K      120K  â¦  129K          12 ( 3%)        â¡- 86.3% Â±  0.1%
```

Itâs dramatic because before, `build.zig` logic was being executed with each `zig build` command, but now, the build system uses the cached, serialized configuration instead.

Aside from performance, I expect third-party tooling such as ZLS to benefit from consuming the serialized configuration file rather than maintaining a fork of the build runner.

This changeset heavily reworks the internal mechanism of the zig build system, however, it is mostly non-breaking from an API perspective, with the exceptions noted in the PR linked above.

For most people Iâm guessing this is the main breaking change theyâll hit:

```
if (b.args) |args| {
    run_cmd.addArgs(args);
}
```

â¬ï¸

```
run_cmd.addPassthruArgs();
```

This removes a capability from build scripts since they can no longer observe those arguments. In exchange, it means that when changing those arguments, build scripts no longer must be rebuilt from source.

If youâre someone who wants to influence the direction of Zig, this is a good time to upgrade your projects to the development version and try out these changes. Weâll be releasing 0.17.0 within a couple weeks from now. However, if you donât have time, and you find out that 0.17.0 broke your build, donât worry, there will be plenty of opportunity to get fixes in for the 0.17.1 tag as well.

April 08, 2026

Author: Matthew Lugg

Iâve been spending a bit of time working on personal projects after merging my [type resolution changes](https://ziglang.org/devlog/2026/#2026-03-10) last month, but I did find the time recently to make some improvements to the LLVM codegen backend. This involved a few different enhancements with various goals, but one nice user-facing change was that I managed to get incremental compilation working with the LLVM backend.

Sadly this canât do anything to speed up the dreaded LLVM Emit Object: that time is entirely down to LLVM. However, what incremental compilation *does* help with is minimizing the time spent in the actual Zig compiler code, which means that if your code has compile errors (so âLLVM Emit Objectâ will be skipped), youâll usually get those errors very quickly. (Of course, it does still give you a *slight* speed-up in successful builds too.)

This support is available in master branch builds right now, and will be in the 0.16.0 release (which weâll be tagging very soon).

For anyone who still hasnât tried it, especially if youâre using Zigâs master branch, please do try out incremental compilation by passing `-fincremental --watch` to `zig build`! The Zig core team have benefited from incremental compilation in our workflows for a good year now, and weâre also hearing good things from users. The feature is relatively stable at this point, and people are often surprised how much time they can save just by getting up-to-date compile errors in milliseconds rather than seconds.

I havenât really personally used incremental compilation with the LLVM backend, but all of the incremental test coverage in CI is now enabled for the LLVM backend, and Iâve had positive feedback from users, so itâs definitely worth giving a shot. As always, if you encounter bugs in incremental compilation, please report them if you can!

Thank you, and I hope you find this useful :)

March 10, 2026

Author: Matthew Lugg

Today, [I merged a 30,000 line PR](https://codeberg.org/ziglang/zig/pulls/31403) after two (arguably three) months of work. The goal of this branch was to rework the Zig compilerâs internal type resolution logic to a more logical and straightforward design. Itâs a quite exciting change for me personally, because it allowed me to clean up a bunch of the compiler guts, but it also has some nice user-facing changes which you might be interested in!

For one thing, the Zig compiler is now lazier about analyzing the fields of types: if the type is never initialized, then thereâs no need for Zig to care what that type âlooks likeâ. This is important when you have a type which doubles as a namespace, a common pattern in modern Zig. For instance, when using `std.Io.Writer`, you donât want the compiler to also pull in a bunch of code in `std.Io`! Hereâs a straightforward example:

```
const Foo = struct {
    bad_field: @compileError("i am an evil field, muahaha"),
    const something = 123;
};
comptime {
    _ = Foo.something; 
}
```

Previously, this code emitted a compile error. Now, it compiles just fine, because Zig never actually looks at the `@compileError` call.

Another improvement weâve made is in the âdependency loopâ experience. Anyone who has encountered a dependency loop compile error in Zig before knows that the error messages for them are entirely unhelpfulâbut thatâs now changed! If you encounter one (which is also a bit less likely now than it used to be), youâll get a detailed error message telling you exactly where the dependency loop comes from. Check it out:

```
const Foo = struct { inner: Bar };
const Bar = struct { x: u32 align(@alignOf(Foo)) };
comptime {
    _ = @as(Foo, undefined);
}
```

```
$ zig build-obj repro.zig
error: dependency loop with length 2
    repro.zig:1:29: note: type 'repro.Foo' depends on type 'repro.Bar' for field declared here
    const Foo = struct { inner: Bar };
                                ^~~
    repro.zig:2:44: note: type 'repro.Bar' depends on type 'repro.Foo' for alignment query here
    const Bar = struct { x: u32 align(@alignOf(Foo)) };
                                               ^~~
    note: eliminate any one of these dependencies to break the loop
```

Of course, dependency loops can get much more complicated than this, but in every case Iâve tested, the error message has had enough information to easily see whatâs going on.

Additionally, this PR made big improvements to the Zig compilerâs âincremental compilationâ feature. The short version is that it fixed a huge amount of known bugs, but in particular, âover-analysisâ problems (where an incremental update did more work than should be necessary, sometimes by a big margin) should finally be all but eliminatedâmaking incremental compilation significantly faster in many cases! If youâve not already, consider [trying out incremental compilation](https://ziglang.org/download/0.15.1/release-notes.html#Incremental-Compilation): it really is a lovely development experience. This is for sure the improvement which excites me the most, and a large part of what motivated this change to begin with.

There are a bunch more changes that come with this PRâdozens of bugfixes, some small language changes (mostly fairly niche), and compiler performance improvements. Itâs far too much to list here, but if youâre interested in reading more about it, you can take a look at [the PR](https://codeberg.org/ziglang/zig/pulls/31403) on Codebergâand of course, if you encounter any bugs, please do open an issue. Happy hacking!

February 13, 2026

Author: Andrew Kelley

As we approach the end of the 0.16.0 release cycle, Jacob has been hard at work, bringing `std.Io.Evented` up to speed with all the latest API changes:

Both of these are based on userspace stack switching, sometimes called âfibersâ, âstackful coroutinesâ, or âgreen threadsâ.

They are now **available to tinker with**, by constructing oneâs application using `std.Io.Evented`. They should be considered **experimental** because there is important followup work to be done before they can be used reliably and robustly:

With those caveats in mind, it seems we are indeed reaching the Promised Land, where Zig code can have Io implementations effortlessly swapped out:

```
const std = @import("std");

pub fn main(init: std.process.Init.Minimal) !void {
    var debug_allocator: std.heap.DebugAllocator(.{}) = .init;
    const gpa = debug_allocator.allocator();

    var threaded: std.Io.Threaded = .init(gpa, .{
        .argv0 = .init(init.args),
        .environ = init.environ,
    });
    defer threaded.deinit();
    const io = threaded.io();

    return app(io);
}

fn app(io: std.Io) !void {
    try std.Io.File.stdout().writeStreamingAll(io, "Hello, World!\n");
}
```

```
$ strace ./hello_threaded
execve("./hello_threaded", ["./hello_threaded"], 0x7ffc1da88b20 /* 98 vars */) = 0
mmap(NULL, 262207, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f583f338000
arch_prctl(ARCH_SET_FS, 0x7f583f378018) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
sigaltstack({ss_sp=0x7f583f338000, ss_flags=0, ss_size=262144}, NULL) = 0
sched_getaffinity(0, 128, [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]) = 8
rt_sigaction(SIGIO, {sa_handler=0x1019d90, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=0x1019d90, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=0}, 8) = 0
writev(1, [{iov_base="Hello, World!\n", iov_len=14}], 1Hello, World!
) = 14
rt_sigaction(SIGIO, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, NULL, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10328c0}, NULL, 8) = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

Swapping out only the I/O implementation:

```
const std = @import("std");

pub fn main(init: std.process.Init.Minimal) !void {
    var debug_allocator: std.heap.DebugAllocator(.{}) = .init;
    const gpa = debug_allocator.allocator();

    var evented: std.Io.Evented = undefined;
    try evented.init(gpa, .{
        .argv0 = .init(init.args),
        .environ = init.environ,
        .backing_allocator_needs_mutex = false,
    });
    defer evented.deinit();
    const io = evented.io();

    return app(io);
}

fn app(io: std.Io) !void {
    try std.Io.File.stdout().writeStreamingAll(io, "Hello, World!\n");
}
```

```
execve("./hello_evented", ["./hello_evented"], 0x7fff368894f0 /* 98 vars */) = 0
mmap(NULL, 262215, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4c28000
arch_prctl(ARCH_SET_FS, 0x7f70a4c68020) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
sigaltstack({ss_sp=0x7f70a4c28008, ss_flags=0, ss_size=262144}, NULL) = 0
sched_getaffinity(0, 128, [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]) = 8
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4c27000
mmap(0x7f70a4c28000, 548864, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f70a4ba1000
io_uring_setup(64, {flags=IORING_SETUP_COOP_TASKRUN|IORING_SETUP_SINGLE_ISSUER, sq_thread_cpu=0, sq_thread_idle=1000, sq_entries=64, cq_entries=128, features=IORING_FEAT_SINGLE_MMAP|IORING_FEAT_NODROP|IORING_FEAT_SUBMIT_STABLE|IORING_FEAT_RW_CUR_POS|IORING_FEAT_CUR_PERSONALITY|IORING_FEAT_FAST_POLL|IORING_FEAT_POLL_32BITS|IORING_FEAT_SQPOLL_NONFIXED|IORING_FEAT_EXT_ARG|IORING_FEAT_NATIVE_WORKERS|IORING_FEAT_RSRC_TAGS|IORING_FEAT_CQE_SKIP|IORING_FEAT_LINKED_FILE|IORING_FEAT_REG_REG_RING|IORING_FEAT_RECVSEND_BUNDLE|IORING_FEAT_MIN_TIMEOUT|IORING_FEAT_RW_ATTR|IORING_FEAT_NO_IOWAIT, sq_off={head=0, tail=4, ring_mask=16, ring_entries=24, flags=36, dropped=32, array=2112, user_addr=0}, cq_off={head=8, tail=12, ring_mask=20, ring_entries=28, overflow=44, cqes=64, flags=40, user_addr=0}}) = 3
mmap(NULL, 2368, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_POPULATE, 3, 0) = 0x7f70a4ba0000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_SHARED|MAP_POPULATE, 3, 0x10000000) = 0x7f70a4b9f000
io_uring_enter(3, 1, 1, IORING_ENTER_GETEVENTS, NULL, 8Hello, World!
) = 1
io_uring_enter(3, 1, 1, IORING_ENTER_GETEVENTS, NULL, 8) = 1
munmap(0x7f70a4b9f000, 4096)            = 0
munmap(0x7f70a4ba0000, 2368)            = 0
close(3)                                = 0
munmap(0x7f70a4ba1000, 548864)          = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

Key point here being that the `app` function is identical between those two snippets.

Moving beyond Hello World, the Zig compiler itself works fine using `std.Io.Evented`, both with io\_uring and with GCD, but as mentioned above, there is a not-yet-diagnosed performance degradation when doing so.

Happy hacking,

Andrew

February 06, 2026

Author: Andrew Kelley

If you have a Zig project with dependencies, two big changes just landed which I think you will be interested to learn about.

Fetched packages are now stored *locally* in the `zig-pkg` directory of the project root (next to your `build.zig` file).

For example here are a few results from [awebo](https://codeberg.org/awebo-chat/awebo) after running `zig build`:

```
$ du -sh zig-pkg/*
13M    freetype-2.14.1-alzUkTyBqgBwke4Jsot997WYSpl207Ij9oO-2QOvGrOi
20K    opus-0.0.2-vuF-cMAkAADVsm707MYCtPmqmRs0gzg84Sz0qGbb5E3w
4.3M   pulseaudio-16.1.1-9-mk_62MZkNwBaFwiZ7ZVrYRIf_3dTqqJR5PbMRCJzSuLw
5.2M   uucode-0.1.0-ZZjBPvtWUACf5dqD_f9I37VGFsN24436CuceC5pTJ25n
728K   vaxis-0.5.1-BWNV_AxECQCj3p4Hcv4U3Yo1WMUJ7Z2FUj0UkpuJGxQQ
```

It is highly recommended to add this directory to the project-local source control ignore file (e.g. `.gitignore`). However, by being outside of `.zig-cache`, it provides the possibility of distributing self-contained source tarballs, which contain all dependencies and therefore can be used to build offline, or for archival purposes.

Meanwhile, an *additional* copy of the dependency is cached globally. After filtering out all the unused files based on the `paths` filter, the contents are recompressed:

```
$ du -sh ~/.cache/zig/p/*
2.4M    freetype-2.14.1-alzUkTyBqgBwke4Jsot997WYSpl207Ij9oO-2QOvGrOi.tar.gz
4.0K    opus-0.0.2-vuF-cMAkAADVsm707MYCtPmqmRs0gzg84Sz0qGbb5E3w.tar.gz
636K    pulseaudio-16.1.1-9-mk_62MZkNwBaFwiZ7ZVrYRIf_3dTqqJR5PbMRCJzSuLw.tar.gz
880K    uucode-0.1.0-ZZjBPvtWUACf5dqD_f9I37VGFsN24436CuceC5pTJ25n.tar.gz
120K    vaxis-0.5.1-BWNV_BFECQBbXeTeFd48uTJRjD5a-KD6kPuKanzzVB01.tar.gz
```

The motivation for this change is to make it easier to tinker. Go ahead and edit those files, see what happens. Swap out your package directory with a git clone. Grep your dependencies all together. Configure your IDE to auto-complete based on the `zig-pkg` directory. [Run baobab on your dependency tree](https://codeberg.org/awebo-chat/awebo/issues/61). Furthermore, by having the global cache have compressed files instead makes it easier to share that cached data between computers. In the future, [it is planned to support peer-to-peer torrenting of dependency trees](https://github.com/ziglang/zig/issues/23236). By recompressing packages into a canonical form, this will allow peers to share Zig packages with minimal bandwidth. I love this idea because it simultaneously provides resilience to network outages, as well as a popularity contest. Find out which open source packages are popular based on number of seeders!

The second change here is the addition of the `--fork` flag to `zig build`.

In retrospect, it seems so obvious, I donât know why I didnât think of it since the beginning. It looks like this:

```
zig build --fork=[path]
```

This is a **project override** option. Given a path to a source checkout of a project, all packages matching that project across the entire dependency tree will be overridden.

Thanks to the fact that package content hashes include name and fingerprint, **this resolves before the package is potentially fetched**.

This is an easy way to temporarily use one or more forks which are in entirely separate directories. You can iterate on your entire dependency tree until everything is working, while using comfortably the development environment and source control of the dependency projects.

The fact that it is a CLI flag makes it appropriately ephemeral. The moment you drop the flags, youâre back to using your pristine, fetched dependency tree.

If the project does not match, an error occurs, preventing confusion:

```
$ zig build --fork=/home/andy/dev/mime
error: fork /home/andy/dev/mime matched no mime packages
$
```

If the project does match, you get a reminder that you are using a fork, preventing confusion:

```
$ zig build --fork=/home/andy/dev/dvui
info: fork /home/andy/dev/dvui matched 1 (dvui) packages
...
```

This functionality is intended to enhance the workflow of dealing with ecosystem breakage. I already tried it a bit and found it to be quite pleasant to work with. The new workflow goes like this:

1. Fail to build from source due to ecosystem breakage.
2. Tinker with `--fork` until your project works again. During this time you can use the actual upstream source control, test suite, `zig build test --watch -fincremental`, etc.
3. Now you have a new option: be selfish and just keep working on your own stuff, or you can proceed to submit your patches upstream.

â¦and you can probably skip the step where you switch your `build.zig.zon` to your fork unless you expect upstream to take a long time to merge your fixes.

February 03, 2026

Author: Andrew Kelley

The Windows operating system provides a large ABI surface area for doing things in the kernel. However, not all ABIs are created equally. As Casey Muratori points out in his lecture, [The Only Unbreakable Law](https://www.youtube.com/watch?v=5IUj1EZwpJY), the organizational structure of software development teams has a direct impact on the structure of the software they produce.

The DLLs on Windows are organized into a heirarchy, with some of the APIs being high-level wrappers around lower-level ones. For example, whenever you call functions of `kernel32.dll`, ultimately, the actual work is done by `ntdll.dll`. You can observe this directly by using ProcMon.exe and examining stack traces.

What weâve learned empirically is that the ntdll APIs are generally well-engineered, reasonable, and powerful, but the kernel32 wrappers introduce unnecessary heap allocations, additional failure modes, unintentional CPU usage, and bloat.

This is why the Zig standard library policy is to [Prefer the Native API over Win32](https://codeberg.org/ziglang/zig/issues/31131). Weâre not quite there yet - we have plenty of calls into kernel32 remaining - but weâve taken great strides recently. Iâll give you two examples.

Example 1: Entropy
------------------

According to the official documentation, Windows does not have a straightforward way to get random bytes.

[Many projects including Chromium, boringssl, Firefox, and Rust](https://github.com/rust-random/rand/issues/111) call `SystemFunction036` from `advapi32.dll` because it worked on versions older than Windows 8.

Unfortunately, starting with Windows 8, the first time you call this function, it dynamically loads `bcryptprimitives.dll` and calls [ProcessPrng](https://learn.microsoft.com/en-us/windows/win32/seccng/processprng). If loading the DLL fails (for example due to an overloaded system, which we have observed on Zig CI several times), it returns error 38 (from a function that has `void` return type and is documented to never fail).

The first thing `ProcessPrng` does is heap allocate a small, constant number of bytes. If this fails it returns `NO_MEMORY` in a `BOOL` (documented behavior is to never fail, and always return `TRUE`).

`bcryptprimitives.dll` apparently also runs a test suite every time you load it.

All that `ProcessPrng` is *really* doing is `NtOpenFile` on `"\\Device\\CNG"` and reading 48 bytes with `NtDeviceIoControlFile` to get a seed, and then initializing a per-CPU AES-based CSPRNG.

So the dependency on `bcryptprimitives.dll` and `advapi32.dll` can both be avoided, and the nondeterministic failure and latencies on first RNG read can also be avoided.

Example 2: NtReadFile and NtWriteFile
-------------------------------------

`ReadFile` looks like this:

```
pub extern "kernel32" fn ReadFile(
    hFile: HANDLE,
    lpBuffer: LPVOID,
    nNumberOfBytesToRead: DWORD,
    lpNumberOfBytesRead: ?*DWORD,
    lpOverlapped: ?*OVERLAPPED,
) callconv(.winapi) BOOL;
```

`NtReadFile` looks like this:

```
pub extern "ntdll" fn NtReadFile(
    FileHandle: HANDLE,
    Event: ?HANDLE,
    ApcRoutine: ?*const IO_APC_ROUTINE,
    ApcContext: ?*anyopaque,
    IoStatusBlock: *IO_STATUS_BLOCK,
    Buffer: *anyopaque,
    Length: ULONG,
    ByteOffset: ?*const LARGE_INTEGER,
    Key: ?*const ULONG,
) callconv(.winapi) NTSTATUS;
```

As a reminder, *the above function is implemented by calling the below function*.

Already we can see some nice things about using the lower level API. For instance, the *real* API simply gives us the error code as the return value, while the kernel32 wrapper hides the status code somewhere, returns a `BOOL` and then requires you to call `GetLastError` to find out what went wrong. Imagine! Returning a value from a function ð

Furthermore, `OVERLAPPED` is a fake type. The Windows kernel doesnât actually know or care about it at all! The actual primitives here are events, APCs, and `IO_STATUS_BLOCK`.

If you have a synchronous file handle, then `Event` and `ApcRoutine` must be `null`. You get the answer in the `IO_STATUS_BLOCK` immediately. If you pass an APC routine here then some old bitrotted 32-bit code runs and you get garbage results.

On the other hand if you have an asynchronous file handle, then you need to either use an `Event` or an `ApcRoutine`. `kernel32.dll` uses events, which means that itâs doing extra, unnecessary resource allocation and management just to read from a file. Instead, Zig now passes an APC routine and then calls `NtDelayExecution`. This integrates seamlessly with cancelation, making it possible to cancel tasks while they perform file I/O, regardless of whether the file was opened in synchronous mode or asynchronous mode.

For a deeper dive into this topic, please refer to this issue:

[Windows: Prefer the Native API over Win32](https://codeberg.org/ziglang/zig/issues/31131)

January 31, 2026

Author: Andrew Kelley

Over the past month or so, several enterprising contributors have taken an interest in the [zig libc subproject](https://codeberg.org/ziglang/zig/issues/30978). The idea here is to incrementally delete redundant code, by providing libc functions as Zig standard library wrappers rather than as vendored C source files. In many cases, these functions are one-to-one mappings, such as `memcpy` or `atan2`, or trivially wrap a generic function, like `strnlen`:

```
fn strnlen(str: [*:0]const c_char, max: usize) callconv(.c) usize {
    return std.mem.findScalar(u8, @ptrCast(str[0..max]), 0) orelse max;
}
```

So far, roughly 250 C source files have been deleted from the Zig repository, with 2032 remaining.

With each function that makes the transition, Zig gains independence from third party projects and from the C programming language, compilation speed improves, Zigâs installation size is simplified and reduced, and user applications which statically link libc enjoy reduced binary size.

Additionally, a [recent enhancement](https://codeberg.org/ziglang/zig/pulls/31037) now makes zig libc share the Zig Compilation Unit with other Zig code rather than being a separate static archive, linked together later. This is one of the advantages of Zig having an integrated compiler and linker. When the exported libc functions share the ZCU, redundant code is eliminated because functions can be optimized together. Itâs kind of like enabling LTO (Link-Time Optimization) across the libc boundary, except itâs done properly in the frontend instead of too late, in the linker.

Furthermore, when this work is combined with the recent [std.Io changes](https://codeberg.org/ziglang/zig/issues/30150), there is potential for users to seamlessly control how libc performs I/O - for example forcing all calls to `read` and `write` to participate in an io\_uring event loop, even though that code was not written with such use case in mind. Or, [resource leak detection](https://codeberg.org/ziglang/zig/pulls/30788) could be enabled for third-party C code. For now this is only a vaporware idea which has not been experimented with, but the idea intrigues me.

Big thanks to Szabolcs Nagy for [libc-test](https://wiki.musl-libc.org/libc-test.html). This project has been a huge help in making sure that we donât regress any math functions.

As a reminder to our users, now that Zig is transitioning to being the static libc provider, if you encounter issues with the musl, mingw-w64, or wasi-libc libc functionality provided by Zig, **please file bug reports in Zig first** so we donât annoy maintainers for bugs that are in Zig, and no longer vendored by independent libc implementation projects.

The very same day I sat at home writing this devlog like a coward, less than five miles away, [armed forces who are in my city against the will of our elected officials shot tear gas, unprovoked, at peaceful protestors](https://www.kptv.com/2026/01/31/live-labor-unions-rally-march-portland-ice-facility-protest/). Next time I hope to have the courage to join my neighbors, and I hope to not get shot like [Alex Pretti](https://en.wikipedia.org/wiki/Killing_of_Alex_Pretti) and [RenÃ©e Good](https://en.wikipedia.org/wiki/Killing_of_Ren%C3%A9e_Good).