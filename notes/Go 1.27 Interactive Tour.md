---
title: "Go 1.27 Interactive Tour"
url: https://victoriametrics.com/blog/go-1-27/index.html
clipped: 2026-08-31 12:22:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Go 1.27 Interactive Tour](https://victoriametrics.com/blog/go-1-27/index.html)

## Digest Summary
Go 1.27 introduces several language and runtime enhancements:

Generic methods: methods can declare their own type parameters independent of the receiver, enabling constructs like func (b Box[T]) Map[U any](f func(T) U) Box[U]. Interfaces still cannot contain generic methods.
Struct literal selectors: promoted fields from embedded structs can be set directly in literals (e.g., User{ID:7, Name:"Mittens}).
Generalized function type inference: generic functions can be used in any context expecting a matching function type (assignments, conversions, composite literals) without explicit type arguments.
Size‑specialized allocation: the compiler emits specialized malloc calls for allocations ≤ 80 bytes, reducing cost up to 30 % (≈ 1 % overall), with a 60 KB binary size increase. Opt‑out via GOEXPERIMENT=nosizespecializedmalloc.
Goroutine labels in tracebacks: runtime/pprof labels now appear in panic, SIGQUIT, and runtime.Stack outputs; disable with GODEBUG=tracebacklabels=0.
Goroutine leak profile: a built‑in runtime/pprof “goroutineleak” profile detects permanently blocked goroutines without experimental flags.
Post‑quantum signatures: new crypto/mldsa implements ML‑DSA (parameter sets 44, 65, 87) and integrates with crypto/x509 and TLS 1.3.
Standard UUID package: uuid supports RFC 9562 parsing, generation (New, NewV4, NewV7), and comparison.
JSON v2 default: encoding/json now runs on the v2 implementation; behavior unchanged, with optional GOEXPERIMENT=nojsonv2 to revert.
Portable SIMD: experimental simd package offers vector‑size‑agnostic SIMD types (Int32s, Float32s, etc.) activated via GOEXPERIMENT=simd.
CutLast functions: strings.CutLast and bytes.CutLast split on the last occurrence of a separator.
Generic hashing: hash/maphash adds Hasher[T] interface (e.g., case‑insensitive string hasher) for custom hash/equality strategies.

---

## Full Article

Ã

## Book a Demo

ð¡ï¸

### Embedded widget blocked

Your privacy settings or an extension blocked the booking widget.[Open booking page](https://meetings.hubspot.com/gregory-zapletnikov/book-a-demo)

If you use a blocker, allow embeds for this site and try again.
- [Blog](https://victoriametrics.com/blog/)/
- Go 1.27 interactive tour

# Go 1.27 interactive tour

- [Go](https://victoriametrics.com/blog/categories/go/)Share:

Go 1.27 is coming soon, so it’s a good time to get a head start on what’s new. The [official release notes](https://go.dev/doc/go1.27) are pretty dry, so here’s a hands-on version with runnable examples showing what changed and how the new behavior works.

A quick credit first: the interactive Go tours were started by [Anton Zhiyanov](https://antonz.org/), who wrote one for every release from Go 1.22 through Go 1.26. He’s [decided to stop](https://antonz.org/on-go-tours/), so we’re picking up where he left off. His earlier tours are all still worth a read:
- [Go 1.22 interactive tour](https://antonz.org/go-1-22/)
- [Go 1.23 interactive tour](https://antonz.org/go-1-23/)
- [Go 1.24 interactive tour](https://antonz.org/go-1-24/)
- [Go 1.25 interactive tour](https://antonz.org/go-1-25/)
- [Go 1.26 interactive tour](https://antonz.org/go-1-26/)

Thanks, Anton.

Before we start digging into the new features, let’s set the context.

This article is based on the official release notes and the Go source code, licensed under the BSD-3-Clause. This is not an exhaustive list; see the [official release notes](https://go.dev/doc/go1.27) for that.

Links point to the documentation (ð), proposals (ð£), most relevant commits (ðð), and authors (ð) for each feature; check them out for motivation, usage, and implementation details. The authors (ð) are the people who contributed to the feature (writing the implementation, the tests, or, for features that graduated from an earlier experiment, the original design), not necessarily a single main author.

Error handling is often skipped to keep the examples short. Don’t do this in production ã

## 

## 

[Generic methods#](https://victoriametrics.com/blog/go-1-27/index.html#generic-methods)

This is the headline of the release. A [method declaration](https://go.dev/ref/spec#Method_declarations) may now declare its own type parameters, independent of the receiver’s. Before Go 1.27, only top-level functions could be generic, so a generic operation on a type had to live as a package-level function instead of a method.

Say we have a generic container and want a  `Map`  operation that can change the element type: ` `type Box[T any] struct{ v T }

// The method declares its own type parameter U (new in Go 1.27).
func (b Box[T]) Map[U any](f func(T) U) Box[U] {
    return Box[U]{v: f(b.v)}
}
` ` 

Now  `Map`  is a method of  `Box`  and can transform an  `int`  box into a  `string`  box: ` `func main() {
    b := Box[int]{v: 21}
    doubled := b.Map(func(n int) int { return n * 2 })
    label := doubled.Map(func(n int) string {
        return fmt.Sprintf("value=%d", n)
    })
    fmt.Println(label.v)
}
` ` 

 ` `value=42
` ` 

There is one important restriction: interfaces still can’t declare type-parameterized methods, and a generic method can’t be used to satisfy an interface. Put a generic method in an interface and the compiler stops you: ` `type Mapper interface {
    Map[U any](f func(int) U) any // interfaces can't declare generic methods
}
` `  ` `interface method must have no type parameters
` ` 
- ð [Generic methods](https://go.dev/ref/spec#Method_declarations)
- ð£ [77273](https://go.dev/issue/77273)
- ðð [524b860](https://github.com/golang/go/commit/524b8606a8), [e84da04](https://github.com/golang/go/commit/e84da0405bcf64c7dbaafb0afc14388049a9b6fc), [e212a16](https://github.com/golang/go/commit/e212a16d1e)
- ð [Robert Griesemer](https://github.com/griesemer), [Mark Freeman](https://github.com/mrkfrmn)

## 

## 

[Struct literal field selectors#](https://victoriametrics.com/blog/go-1-27/index.html#struct-literal-field-selectors)

A key in a [struct literal](https://go.dev/ref/spec#Composite_literals) may now be any valid field selector for the struct type, not just a top-level field name. In practice this means you can set a promoted field (one that comes from an embedded struct) directly, without spelling out the embedded type. ` `type Base struct {
    ID int
}

type User struct {
    Base
    Name string
}
` ` 

Before Go 1.27 you had to write  `User{Base: Base{ID: 7}, Name: "Mittens"}` . Now the promoted  `ID`  works as a key on its own: ` `u := User{ID: 7, Name: "Mittens"}
fmt.Println(u.ID, u.Name)
` ` 

 ` `7 Mittens
` ` 
- ð [Composite literals](https://go.dev/ref/spec#Composite_literals)
- ð£ [9859](https://go.dev/issue/9859)
- ðð [1a8f9d8](https://github.com/golang/go/commit/1a8f9d8141), [9f7e98d](https://github.com/golang/go/commit/9f7e98d263f1e496991110f057763a2b4319e1c1), [30bfe53](https://github.com/golang/go/commit/30bfe53dd7), [e2c1885](https://github.com/golang/go/commit/e2c188568d)
- ð [Robert Griesemer](https://github.com/griesemer), [Cherry Mui](https://github.com/cherrymui)

## 

## 

[Generalized function type inference#](https://victoriametrics.com/blog/go-1-27/index.html#generalized-function-type-inference)

Function type inference has been generalized to apply in all contexts where a generic function is used where a matching function type is expected: not just plain assignment to a variable (which already worked), but also conversions and composite literals. In those cases you previously had to spell out the type arguments by hand.

Take two generic helpers and drop them into a slice whose element type is  `func([]int) int` : ` `func first[T any](s []T) T { return s[0] }
func last[T any](s []T) T  { return s[len(s)-1] }
` `  ` `// The slice's element type drives inference: T=int for each entry.
// Before Go 1.27 this failed with "cannot use generic function
// without instantiation"; you had to write first[int], last[int].
ops := []func([]int) int{first, last}
for _, op := range ops {
    fmt.Println(op([]int{10, 20, 30}))
}
` ` 

 ` `10
30
` ` 
- ð [Assignability](https://go.dev/ref/spec#Assignability)
- ð£ [77245](https://go.dev/issue/77245)
- ðð [ef06728](https://github.com/golang/go/commit/ef067283ce), [f757de8](https://github.com/golang/go/commit/f757de83f4)
- ð [Robert Griesemer](https://github.com/griesemer), [Mark Freeman](https://github.com/mrkfrmn)

## 

## 

[Faster memory allocation#](https://victoriametrics.com/blog/go-1-27/index.html#faster-memory-allocation)

The compiler now generates calls to size-specialized memory allocation routines, cutting the cost of some small (under 80 bytes) allocations by up to 30%. Improvements vary with the workload, but the overall gain is expected to be around 1% in real allocation-heavy programs. The tradeoff is about 60 KB of extra binary size, independent of the workload.

There’s nothing to change in your code; it just gets a little faster. If you need to turn it off, build with  `GOEXPERIMENT=nosizespecializedmalloc` . That opt-out is expected to be removed in Go 1.28.
- ð [Runtime release notes](https://go.dev/doc/go1.27#runtime)
- ð£ [79286](https://go.dev/issue/79286)
- ðð [2a93576](https://github.com/golang/go/commit/2a93576965)
- ð [Michael Matloob](https://github.com/matloob)

## 

## 

[Goroutine labels in tracebacks#](https://victoriametrics.com/blog/go-1-27/index.html#goroutine-labels-in-tracebacks)

For modules whose  `go.mod`  sets Go 1.27 or later, tracebacks now include [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2) goroutine labels in the header line of each goroutine. If you already attach labels for profiling with  `` [pprof.Do](https://pkg.go.dev/runtime/pprof@go1.27rc2#Do), that context now shows up in crash dumps,  `SIGQUIT`  traces, and  `` [runtime.Stack](https://pkg.go.dev/runtime@go1.27rc2#Stack) output too (handy for telling apart otherwise identical goroutines).

Here we attach a label, then dump the current goroutine’s stack to see it in action: ` `ctx := context.Background()
pprof.Do(ctx, pprof.Labels("request", "42"), func(ctx context.Context) {
    buf := make([]byte, 1<<12)
    n := runtime.Stack(buf, false)
    fmt.Printf("%s", buf[:n])
})
` ` 

 ` `goroutine 1 [running] {request: 42}:
main.main.func1(...)
	.../main.go:14 +0x38
runtime/pprof.Do(...)
	.../runtime/pprof/runtime.go:57 +0x8c
main.main()
	.../main.go:12 +0x6c
` ` 

The pointer arguments, offsets, and file paths differ from run to run; what’s new is the  `{request: 42}`  appended right after the goroutine’s  `[running]`  state: its  `pprof`  labels. That same  `{...}`  annotation appears on the header of every labeled goroutine in a panic or  `SIGQUIT`  traceback. You can disable it with  `GODEBUG=tracebacklabels=0`  (the setting was added in Go 1.26). The opt-out is expected to stay indefinitely, in case labels carry sensitive data you don’t want in tracebacks.
- ð [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2)
- ð£ [76349](https://go.dev/issue/76349)
- ðð [3694f33](https://github.com/golang/go/commit/3694f33692), [19c994c](https://github.com/golang/go/commit/19c994cc0c)
- ð [David Finkel](https://github.com/dfinkel)

## 

## 

[Goroutine leak profile#](https://victoriametrics.com/blog/go-1-27/index.html#goroutine-leak-profile)

Go 1.26 introduced a goroutine leak detector as an experiment. In Go 1.27 it graduates to a regular profile:  `` [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2) exposes a  `goroutineleak`  profile that runs a GC cycle to find goroutines that are permanently blocked (leaked) and reports their stacks; no  `GOEXPERIMENT`  needed anymore.

A “leaked” goroutine is one blocked forever on a channel, mutex, or similar, with no way to ever make progress. The classic example is a goroutine that sends to a channel it alone holds, so nobody can ever receive from it: ` `func leak() {
    ch := make(chan int) // only this goroutine ever sees ch
    ch <- 1              // blocks forever: nobody will ever receive
}
` ` 

Start one, let it park, then dump the profile: ` `go leak() // this goroutine can never finish

runtime.Gosched() // let it park on the send

// The GC-backed scan finds goroutines that can never make progress.
pprof.Lookup("goroutineleak").WriteTo(os.Stdout, 1)
` ` 

 ` `goroutineleak profile: total 1
1 @ 0x... 0x... 0x... 0x... 0x...
#	0x...	main.leak+0x27	.../main.go:11
` ` 

The  `total 1`  line says the detector found exactly one leaked goroutine, and the stack pins it to  `main.leak` : the  `ch <- 1`  send that will never complete (the addresses vary from run to run). In a real service you’d usually scrape the  `/debug/pprof/goroutineleak`  [net/http/pprof](https://pkg.go.dev/net/http/pprof@go1.27rc2) endpoint instead of writing to stdout.
- ð [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2)
- ð£ [74609](https://go.dev/issue/74609)
- ðð [253aa2a](https://github.com/golang/go/commit/253aa2a12a), [1644917](https://github.com/golang/go/commit/16449179ec), [afcf04c](https://github.com/golang/go/commit/afcf04cb64)
- ð [Vlad Saioc](https://github.com/VladSaiocUber), [Austin Clements](https://github.com/aclements), [Cherry Mui](https://github.com/cherrymui)

## 

## 

[Post-quantum signatures#](https://victoriametrics.com/blog/go-1-27/index.html#post-quantum-signatures)

The new [crypto/mldsa](https://pkg.go.dev/crypto/mldsa@go1.27rc2) package implements ML-DSA, the post-quantum digital signature scheme specified in [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final). It comes in three parameter sets ( `` [MLDSA44](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA44),  `` [MLDSA65](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA65), and  `` [MLDSA87](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA87)), trading key/signature size for security level. ` `priv, _ := mldsa.GenerateKey(mldsa.MLDSA65())

msg := []byte("victoria metrics")
sig, _ := priv.Sign(rand.Reader, msg, crypto.Hash(0))

fmt.Println("scheme:  ", mldsa.MLDSA65())
fmt.Println("sig size:", mldsa.MLDSA65().SignatureSize())
fmt.Println("verified:", mldsa.Verify(priv.PublicKey(), msg, sig, nil) == nil)
` ` 

 ` `scheme:   ML-DSA-65
sig size: 3309
verified: true
` ` 

ML-DSA support also reaches [crypto/x509](https://pkg.go.dev/crypto/x509@go1.27rc2) (private keys, public keys, and signatures) and [crypto/tls](https://pkg.go.dev/crypto/tls@go1.27rc2) (the new  `` [MLDSA44](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA44),  `` [MLDSA65](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA65), and  `` [MLDSA87](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA87) signature schemes in [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html)).
- ð [crypto/mldsa](https://pkg.go.dev/crypto/mldsa@go1.27rc2)
- ð£ [77626](https://go.dev/issue/77626)
- ðð [7bc111c](https://github.com/golang/go/commit/7bc111c6eb96bd7331f822d29c26b268212c841b)
- ð [Filippo Valsorda](https://github.com/FiloSottile), [Daniel McCarney](https://github.com/cpu)

## 

## 

[The uuid package#](https://victoriametrics.com/blog/go-1-27/index.html#the-uuid-package)

Go finally has a UUID package in the standard library. The new top-level [uuid](https://pkg.go.dev/uuid@go1.27rc2) package generates and parses UUIDs per [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html), using a [cryptographically secure random source](https://pkg.go.dev/crypto/rand@go1.27rc2). Random-component UUIDs are comparable, so you can use  `==`  on them directly. ` `a := uuid.MustParse("f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
fmt.Println("parsed:", a)
fmt.Println("nil:   ", uuid.Nil())
fmt.Println("max:   ", uuid.Max())
` ` 

 ` `parsed: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
nil:    00000000-0000-0000-0000-000000000000
max:    ffffffff-ffff-ffff-ffff-ffffffffffff
` ` 

For generation,  `` [uuid.New()](https://pkg.go.dev/uuid@go1.27rc2#New) picks an algorithm suitable for most uses, while  `` [uuid.NewV4()](https://pkg.go.dev/uuid@go1.27rc2#NewV4) gives a purely random UUID and  `` [uuid.NewV7()](https://pkg.go.dev/uuid@go1.27rc2#NewV7) gives a time-ordered one; the latter is great for database keys because it sorts by creation time. Each call produces a fresh value, so try running this a few times: ` `fmt.Println(uuid.NewV4()) // random
fmt.Println(uuid.NewV7()) // time-ordered
` ` 

- ð [uuid](https://pkg.go.dev/uuid@go1.27rc2)
- ð£ [62026](https://go.dev/issue/62026)
- ðð [2fb2b98](https://github.com/golang/go/commit/2fb2b98da3d7d529e11a94b79372c0309aa05e21)
- ð [Damien Neil](https://github.com/neild)

## 

## 

[JSON v2 by default#](https://victoriametrics.com/blog/go-1-27/index.html#json-v2-by-default)

The long-awaited  `encoding/json/v2`  rewrite has been experimental since Go 1.25. In Go 1.27 the experiment graduates: [encoding/json/v2](https://pkg.go.dev/encoding/json/v2@go1.27rc2) and its low-level companion [encoding/json/jsontext](https://pkg.go.dev/encoding/json/jsontext@go1.27rc2) are now available without the  `GOEXPERIMENT=jsonv2`  build flag. The quieter but bigger change: the classic  `` [encoding/json](https://pkg.go.dev/encoding/json@go1.27rc2) (v1) package is now backed by the v2 implementation under the hood.

The switch is transparent: behavior is preserved (only some error-message text differs), with new [options](https://pkg.go.dev/encoding/json/v2@go1.27rc2#Options) pinning v2 to v1 semantics where they’d otherwise diverge. No migration is required, and  `GOEXPERIMENT=nojsonv2`  restores the original v1 implementation if you hit a compatibility issue.

For the common case, the v2 API mirrors v1 (the import here is  `json "encoding/json/v2"` ): ` `type Point struct {
    X int `json:"x"`
    Y int `json:"y"`
}

data, err := json.Marshal(Point{X: 1, Y: 2})
fmt.Println(string(data), err)
` ` 

 ` `{"x":1,"y":2} <nil>
` ` 

One behavior worth knowing: unlike v1, which always sorts map keys, v2 does not sort them by default; skipping the sort is faster. When you need stable map output (for golden tests, say), pass the  `` [json.Deterministic](https://pkg.go.dev/encoding/json/v2@go1.27rc2#Deterministic) option.
- ð [encoding/json/v2](https://pkg.go.dev/encoding/json/v2@go1.27rc2)
- ð£ [71497](https://go.dev/issue/71497)
- ðð [e62d3e6](https://github.com/golang/go/commit/e62d3e6e89)
- ð [Joe Tsai](https://github.com/dsnet), [Damien Neil](https://github.com/neild)

## 

## 

[Portable SIMD#](https://victoriametrics.com/blog/go-1-27/index.html#portable-simd)

Go 1.27 adds an experimental [simd](https://pkg.go.dev/simd@go1.27rc2) package: portable, vector-size-agnostic SIMD that compiles down to real hardware vector instructions where they’re available and falls back to a pure-Go emulation where they aren’t. It’s off by default; you build with  `GOEXPERIMENT=simd`  to enable it.

The types are named after their element type with an  `s`  suffix ( `` [Int32s](https://pkg.go.dev/simd@go1.27rc2#Int32s),  `` [Float32s](https://pkg.go.dev/simd@go1.27rc2#Float32s),  `` [Float64s](https://pkg.go.dev/simd@go1.27rc2#Float64s), and so on), and their width is deliberately not fixed: a  `Float32s`  might hold 4 lanes on one machine and 16 on another. You load a vector from a slice, operate on it, and store it back, letting the hardware pick the width: ` `a := []float32{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
b := []float32{10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160}

va := simd.LoadFloat32s(a) // reads exactly va.Len() lanes from a
vb := simd.LoadFloat32s(b)

sum := va.Add(vb) // element-wise add, many lanes in one instruction

out := make([]float32, sum.Len())
sum.Store(out)

fmt.Println(out[:4])
` ` 

 ` `[11 22 33 44]
` ` 
- ð [simd](https://pkg.go.dev/simd@go1.27rc2)
- ð£ [78902](https://go.dev/issue/78902)
- ðð [44a4be9](https://github.com/golang/go/commit/44a4be991f), [8d29cf2](https://github.com/golang/go/commit/8d29cf23b1), [48bf922](https://github.com/golang/go/commit/48bf92284c)
- ð [David Chase](https://github.com/dr2chase), [Junyang Shao](https://github.com/JunyangShao), [Cherry Mui](https://github.com/cherrymui)

## 

## 

[Cut around the last separator#](https://victoriametrics.com/blog/go-1-27/index.html#cut-around-the-last-separator)

 `` [strings.Cut](https://pkg.go.dev/strings@go1.27rc2#Cut) (from Go 1.18) splits around the first occurrence of a separator. Go 1.27 adds  `` [strings.CutLast](https://pkg.go.dev/strings@go1.27rc2#CutLast) (and  `` [bytes.CutLast](https://pkg.go.dev/bytes@go1.27rc2#CutLast)) for the last occurrence (a cleaner replacement for many  `` [LastIndex](https://pkg.go.dev/strings@go1.27rc2#LastIndex) dances). ` `before, after, found := strings.CutLast("a/b/c", "/")
fmt.Printf("%q %q %v\n", before, after, found)

before, after, found = strings.CutLast("nosep", "/")
fmt.Printf("%q %q %v\n", before, after, found)
` ` 

 ` `"a/b" "c" true
"nosep" "" false
` ` 

As with  `Cut` , when the separator isn’t found you get the whole input as  `before` , an empty  `after` , and  `found == false` .
- ð [strings.CutLast](https://pkg.go.dev/strings@go1.27rc2#CutLast), [bytes.CutLast](https://pkg.go.dev/bytes@go1.27rc2#CutLast)
- ð£ [71151](https://go.dev/issue/71151)
- ðð [11b596c](https://github.com/golang/go/commit/11b596c22dcabf91f9595da778b00e26f4d661a8)
- ð [qiulaidongfeng](https://github.com/qiulaidongfeng)

## 

## 

[Generic hashing#](https://victoriametrics.com/blog/go-1-27/index.html#generic-hashing)

The  `` [hash/maphash](https://pkg.go.dev/hash/maphash@go1.27rc2) package gains a  `` [Hasher[T]](https://pkg.go.dev/hash/maphash@go1.27rc2#Hasher) interface: a contract that future hash-based data structures (hash tables, Bloom filters, and so on) can use to hash and compare values of a type. It bundles two operations:  `Hash` , which mixes a value into a running hash, and  `Equal` , which compares two values. The rule tying them together is that equal values must hash the same.

There’s a ready-made  `` [ComparableHasher[T]](https://pkg.go.dev/hash/maphash@go1.27rc2#ComparableHasher) (hash by value, equality by  `==` ) for any comparable type, but the interesting part is defining your own. Here’s a case-insensitive string hasher: ` `type ciHasher struct{}

// Equal ignores case; Hash mixes in the lower-cased form, so values
// that are Equal always hash the same.
func (ciHasher) Hash(h *maphash.Hash, s string) { h.WriteString(strings.ToLower(s)) }
func (ciHasher) Equal(x, y string) bool         { return strings.EqualFold(x, y) }
` ` 

Now  `"Go"`  and  `"GO"`  count as equal and hash identically, which plain  `==`  and value hashing can’t do: ` `var h maphash.Hasher[string] = ciHasher{} // plug in the custom strategy

fmt.Println(h.Equal("Go", "GO"), h.Equal("Go", "Rust"))

// Equal values must hash the same, so feed each into a Hash sharing one seed:
seed := maphash.MakeSeed()
var a, b maphash.Hash
a.SetSeed(seed)
b.SetSeed(seed)
h.Hash(&a, "Go")
h.Hash(&b, "GO")
fmt.Println(a.Sum64() == b.Sum64())
` ` 

 ` `true false
true
` ` 
- ð [hash/maphash](https://pkg.go.dev/hash/maphash@go1.27rc2)
- ð£ [70471](https://go.dev/issue/70471)
- ðð [330aec8](https://github.com/golang/go/commit/330aec810997f89262fa04939a00425194e94216)
- ð [Alan Donovan](https://github.com/adonovan)

## 

## 

[Integer division with rounding#](https://victoriametrics.com/blog/go-1-27/index.html#integer-division-with-rounding)

 `` [math/big](https://pkg.go.dev/math/big@go1.27rc2) adds  `` [Int.Divide](https://pkg.go.dev/math/big@go1.27rc2#Int.Divide), which computes a quotient and remainder together with an explicit [rounding mode](https://pkg.go.dev/math/big@go1.27rc2#RoundingMode):  `` [Trunc](https://pkg.go.dev/math/big@go1.27rc2#Trunc),  `` [Floor](https://pkg.go.dev/math/big@go1.27rc2#Floor),  `` [Round](https://pkg.go.dev/math/big@go1.27rc2#Round), or  `` [Ceil](https://pkg.go.dev/math/big@go1.27rc2#Ceil). The classic  `` [Quo](https://pkg.go.dev/math/big@go1.27rc2#Int.Quo)/ `` [Mod](https://pkg.go.dev/math/big@go1.27rc2#Int.Mod) always truncates toward zero, so this fills a real gap for financial and numeric code. ` `x, y := big.NewInt(7), big.NewInt(2)
q, r := new(big.Int), new(big.Int)

q.Divide(x, y, r, big.Ceil)
fmt.Printf("ceil:  q=%s r=%s\n", q, r)

q.Divide(x, y, r, big.Floor)
fmt.Printf("floor: q=%s r=%s\n", q, r)
` ` 

 ` `ceil:  q=4 r=-1
floor: q=3 r=1
` ` 

Notice how the remainder follows the rounding mode: with  `Ceil`  the quotient rounds up to 4, leaving a remainder of â1; with  `Floor`  it rounds down to 3, leaving 1.
- ð [math/big.Int.Divide](https://pkg.go.dev/math/big@go1.27rc2#Int.Divide)
- ð£ [76821](https://go.dev/issue/76821)
- ðð [8f7f951](https://github.com/golang/go/commit/8f7f951965120878db5158f543b88b8c0cd2323d)
- ð [Armin GÃ¼nther](https://github.com/arminguenther)

## 

## 

[Random numbers, your type#](https://victoriametrics.com/blog/go-1-27/index.html#random-numbers-your-type)

 `` [math/rand/v2](https://pkg.go.dev/math/rand/v2@go1.27rc2) has had a top-level generic  `` [N](https://pkg.go.dev/math/rand/v2@go1.27rc2#N) function since Go 1.22. Go 1.27 adds it as a method,  `` [(*Rand).N](https://pkg.go.dev/math/rand/v2@go1.27rc2#Rand.N), so you can draw a bounded random number of any integer or duration type from your own  `*Rand`  source. ` `r := rand.New(rand.NewPCG(1, 2)) // fixed seed â reproducible
fmt.Println(r.N(100))            // int in [0, 100)
` ` 

 ` `76
` ` 
- ð [rand.Rand.N](https://pkg.go.dev/math/rand/v2@go1.27rc2#Rand.N)
- ð£ [77853](https://go.dev/issue/77853)
- ðð [e0a8616](https://github.com/golang/go/commit/e0a8616941e4eccde231f33cbcf3710896ba5a9b)
- ð [qiulaidongfeng](https://github.com/qiulaidongfeng)

## 

## 

[Sleep in synthetic time#](https://victoriametrics.com/blog/go-1-27/index.html#sleep-in-synthetic-time)

 `` [testing/synctest](https://pkg.go.dev/testing/synctest@go1.27rc2) (stable since Go 1.25) lets you test concurrent code against a fake clock. Go 1.27 adds a  `` [Sleep](https://pkg.go.dev/testing/synctest@go1.27rc2#Sleep) helper that combines  `` [time.Sleep](https://pkg.go.dev/time@go1.27rc2#Sleep) with  `` [synctest.Wait](https://pkg.go.dev/testing/synctest@go1.27rc2#Wait): advance the bubble’s synthetic clock and then wait for all goroutines to settle, in one call.

Inside a bubble the  `` [time](https://pkg.go.dev/time@go1.27rc2) package uses a fake clock, so a two-second sleep returns instantly;  `synctest.Sleep`  also waits for the background goroutine to finish before moving on: ` `t := &testing.T{} // in real code, use the *testing.T your test receives
synctest.Test(t, func(t *testing.T) {
    start := time.Now()
    go func() {
        time.Sleep(time.Second)
        fmt.Println("worker woke at", time.Since(start))
    }()

    // Advance fake time by 2s AND wait for goroutines to settle, in one call.
    synctest.Sleep(2 * time.Second)
    fmt.Println("main advanced", time.Since(start))
})
` ` 

 ` `worker woke at 1s
main advanced 2s
` ` 

Both durations are exact; no real time passes. It’s a small convenience, but it removes a common two-line boilerplate from almost every  `synctest` -based test. (The bare  `&testing.T{}`  above is only to make the snippet self-contained; in a real test  `synctest.Sleep`  lives inside a  `func TestXxx(t *testing.T)`  and you pass that  `t` .)
- ð [synctest.Sleep](https://pkg.go.dev/testing/synctest@go1.27rc2#Sleep)
- ð£ [77169](https://go.dev/issue/77169)
- ðð [8ac41b5](https://github.com/golang/go/commit/8ac41b52c4b7a6ab9c41d008abbe254270200b8e)
- ð [Damien Neil](https://github.com/neild)

## 

## 

[In-memory test servers#](https://victoriametrics.com/blog/go-1-27/index.html#in-memory-test-servers)

 `` [httptest.NewTestServer](https://pkg.go.dev/net/http/httptest@go1.27rc2#NewTestServer) creates an  `` [httptest.Server](https://pkg.go.dev/net/http/httptest@go1.27rc2#Server) backed by an in-memory fake network instead of a real TCP listener. No real ports are involved, and it registers its own cleanup via  `` [t.Cleanup](https://pkg.go.dev/testing@go1.27rc2#T.Cleanup), so there’s no  `defer srv.Close()`  to remember. It also pairs with  `` [testing/synctest](https://pkg.go.dev/testing/synctest@go1.27rc2), letting HTTP round-trips run in synthetic time for faster, fully deterministic tests. ` `t := &testing.T{} // in real code, use the *testing.T your test receives
handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "hello from the in-memory server")
})

srv := httptest.NewTestServer(t, handler) // in-memory network, auto-cleanup
resp, _ := srv.Client().Get(srv.URL)      // no real TCP port
body, _ := io.ReadAll(resp.Body)
fmt.Print(string(body))
` ` 

 ` `hello from the in-memory server
` ` 

The request never touches the network stack;  `` [srv.Client()](https://pkg.go.dev/net/http/httptest@go1.27rc2#Server.Client) is wired straight to the handler over an in-process pipe. (As with the previous example, the bare  `&testing.T{}`  is only to keep the snippet self-contained; in a real test you’d pass the  `t`  from your  `func TestXxx(t *testing.T)` .)
- ð [httptest.NewTestServer](https://pkg.go.dev/net/http/httptest@go1.27rc2#NewTestServer)
- ð£ [76608](https://go.dev/issue/76608)
- ðð [813b317](https://github.com/golang/go/commit/813b317cc9), [a871fd3](https://github.com/golang/go/commit/a871fd3732)
- ð [Damien Neil](https://github.com/neild)

## 

## 

[Unicode 17#](https://victoriametrics.com/blog/go-1-27/index.html#unicode-17)

The  `` [unicode](https://pkg.go.dev/unicode@go1.27rc2) package and the rest of the standard library have been upgraded from [Unicode 15](https://www.unicode.org/versions/Unicode15.0.0/) to [Unicode 17](https://www.unicode.org/versions/Unicode17.0.0/), picking up new scripts, characters, and properties.

To see the jump in action, take ð« (U+1FADC “root vegetable”), which was added in [Unicode 16.0](https://www.unicode.org/versions/Unicode16.0.0/). On Go’s old Unicode 15 data it was an unassigned code point, so  `` [IsSymbol](https://pkg.go.dev/unicode@go1.27rc2#IsSymbol) and  `` [IsGraphic](https://pkg.go.dev/unicode@go1.27rc2#IsGraphic) both returned  `false` ; now it’s a recognized symbol: ` `fmt.Println("Unicode", unicode.Version)

r := 'ð«' // U+1FADC "root vegetable", added in Unicode 16.0
fmt.Printf("%#U  symbol=%v graphic=%v\n", r, unicode.IsSymbol(r), unicode.IsGraphic(r))
` ` 

 ` `Unicode 17.0.0
U+1FADC 'ð«'  symbol=true graphic=true
` ` 

On Go 1.26 the very same code prints  `Unicode 15.0.0`  and  `U+1FADC symbol=false graphic=false` ; the code point isn’t even printable, so  `%#U`  omits the glyph.
- ð [unicode](https://pkg.go.dev/unicode@go1.27rc2)
- ð£ [77266](https://go.dev/issue/77266)
- ðð [dd39dfb](https://github.com/golang/go/commit/dd39dfb534)
- ð [Russ Cox](https://github.com/rsc)

## 

## 

[Other notable changes#](https://victoriametrics.com/blog/go-1-27/index.html#other-notable-changes)

A few smaller changes that are easy to miss but can affect real code:
-  `time`  channels are now always unbuffered. Following the timer rework in Go 1.23, the channels returned by  `` [time.After](https://pkg.go.dev/time@go1.27rc2#After),  `` [time.NewTimer](https://pkg.go.dev/time@go1.27rc2#NewTimer),  `` [time.NewTicker](https://pkg.go.dev/time@go1.27rc2#NewTicker), and friends are now synchronous in every case. The  `asynctimerchan`  GODEBUG that restored the old buffered behavior has been removed, so if you relied on  `asynctimerchan=1` , that escape hatch is gone.
-  `` [http.Response.Body](https://pkg.go.dev/net/http@go1.27rc2#Response) drains itself on  `Close` . For HTTP/1, closing the body now reads and discards any unread content (up to a conservative limit) so the connection can be reused. For most programs this is a transparent win; if you were leaning on an early  `Close`  to abort a large download, set  `` [Transport.DisableKeepAlives](https://pkg.go.dev/net/http@go1.27rc2#Transport) to opt out.
- HTTP/2 servers honor client priorities. The server now understands [RFC 9218](https://www.rfc-editor.org/rfc/rfc9218.html) priority signals and serves higher-priority streams first. Set  `` [Server.DisableClientPriority = true](https://pkg.go.dev/net/http@go1.27rc2#Server) to restore the old round-robin behavior.
-  `` [crypto/x509](https://pkg.go.dev/crypto/x509@go1.27rc2) honors  `SSL_CERT_FILE`  and  `SSL_CERT_DIR`  on Windows and macOS. When either is set,  `` [SystemCertPool](https://pkg.go.dev/crypto/x509@go1.27rc2#SystemCertPool) loads roots from disk and uses Go’s own verifier instead of the platform APIs (disable with  `GODEBUG=x509sslcertoverrideplatform=0` ).

## 

## 

[Tooling#](https://victoriametrics.com/blog/go-1-27/index.html#tooling)

A grab bag of  `` [go command and toolchain improvements](https://go.dev/doc/go1.27#tools):
-  `go test`  runs the  `stdversion`  vet check by default. It reports uses of standard library symbols that are newer than the Go version declared in your  `go.mod` , catching accidental “works on my machine” version drift.
-  `go doc pkg@version` . You can now ask for documentation at a specific module version, e.g.  `go doc example.com/mod@v1.2.3`  ([proposal 63696](https://go.dev/issue/63696)).
-  `go doc -ex` . The new  `-ex`  flag lists a package’s runnable examples ( `go doc -ex bytes` ). To print one example’s source, name it directly, e.g.  `go doc bytes.ExampleBuffer` .
-  `go fix`  gains new modernizers. The  `atomictypes` ,  `embedlit` ,  `slicesbackward` , and  `unsafefuncs`  analyzers rewrite older patterns to their modern equivalents. (The  `waitgroup`  analyzer was renamed to  `waitgroupgo` , and  `fmtappendf`  was dropped.)
-  `go mod tidy`  tidies  `require`  blocks. For modules on  `go 1.27`  or later, it now merges scattered  `require`  blocks into the canonical two (one for direct and one for indirect dependencies) while preserving attached comments.
-  `go tool trace -http=:6060`  binds to localhost. When given only a port, the trace UI now listens on localhost only, matching  `go tool pprof` . Pass an explicit address to listen more broadly.
- The  `go`  command dropped support for the Bazaar (bzr) version control system ([proposal 78090](https://go.dev/issue/78090)).
- Response files ( `@file` ) are now supported by the  `compile` ,  `link` ,  `asm` ,  `cgo` ,  `cover` , and  `pack`  tools, compatible with GCC’s format (helpful for build systems that hit command-line length limits).

## 

## 

[Hidden gems#](https://victoriametrics.com/blog/go-1-27/index.html#hidden-gems)

Everything above comes from the release notes. But the notes are a curated summary, and roughly 1,600 commits landed between Go 1.26 and Go 1.27. Here are some changes that are worth knowing about:
- 

HTTP/2 is finally a real package. For years,  `` [net/http](https://pkg.go.dev/net/http@go1.27rc2)’s [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html) support lived in  `` [h2_bundle.go](https://github.com/golang/go/blob/go1.26.1/src/net/http/h2_bundle.go): a single 12,226-line file, mechanically generated by concatenating  `` [golang.org/x/net/http2](https://pkg.go.dev/golang.org/x/net/http2) and prefixing every identifier with  `http2` . In Go 1.27 it’s gone, replaced by an actual package,  `` [net/http/internal/http2](https://github.com/golang/go/tree/go1.27rc2/src/net/http/internal/http2).
ð£ [67810](https://go.dev/issue/67810) â¢ ðð [c5f43ab](https://github.com/golang/go/commit/c5f43ab046), [080aa8e](https://github.com/golang/go/commit/080aa8e964)
- 

HTTP/3 is quietly taking shape. Go 1.27 adds unexported, pluggable [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html) hooks to  `net/http` , and teaches much of the  `net/http`  test suite to run against HTTP/3. Nothing is exported yet, so there’s nothing to call, but the scaffolding for a future  `` [http.Transport](https://pkg.go.dev/net/http@go1.27rc2#Transport) that speaks [QUIC](https://www.rfc-editor.org/rfc/rfc9000.html) is now in the tree.
ð£ [77440](https://go.dev/issue/77440) â¢ ðð [0b9bcbc](https://github.com/golang/go/commit/0b9bcbc58c), [96d6d38](https://github.com/golang/go/commit/96d6d38872), [db6661a](https://github.com/golang/go/commit/db6661a2fd)
- 

Three new compiler optimizations, all on by default. A [known bits](https://github.com/golang/go/commit/7a8dcab743) dataflow pass tracks which bits of a value are provably 0 or 1 and folds away the resulting redundancy; [loop-invariant code motion](https://github.com/golang/go/commit/f9f351b130) moves computations whose result never changes out of the loop, so they run once instead of on every iteration; and [switch statements now compile to lookup tables](https://github.com/golang/go/commit/2a902c8a8a) where the cases allow it, including with  `` [fallthrough](https://github.com/golang/go/commit/1f5c165a81).
ðð [7a8dcab](https://github.com/golang/go/commit/7a8dcab743), [f9f351b](https://github.com/golang/go/commit/f9f351b130), [9c688e3](https://github.com/golang/go/commit/9c688e3f4d), [2a902c8](https://github.com/golang/go/commit/2a902c8a8a), [1f5c165](https://github.com/golang/go/commit/1f5c165a81)
- 

The runtime already uses the new SIMD package. The  `` [simd](https://pkg.go.dev/simd@go1.27rc2) package is presented as an experiment for your code, but the standard library is [already a customer](https://github.com/golang/go/commit/2403e594a5): the [Swiss Table](https://go.dev/blog/swisstable) map implementation reimplemented its  `MemHash32` ,  `MemHash64` , and  `StrHash`  functions on top of  `` [simd/archsimd](https://pkg.go.dev/simd/archsimd@go1.27rc2) intrinsics.
ðð [2403e59](https://github.com/golang/go/commit/2403e594a5), [252a8ad](https://github.com/golang/go/commit/252a8adbc0)
- 

Reorganized type metadata in the linker. Type descriptors and itabs moved into a dedicated  `` [.go.type section](https://github.com/golang/go/commit/13096a62e6) with explicit alignment, both  `` [typelinks](https://github.com/golang/go/commit/481ab86aaf) and  `` [itablinks](https://github.com/golang/go/commit/6ef7fe9a48) were removed outright, and descriptor size arithmetic was  `` [centralized in internal/abi](https://github.com/golang/go/commit/3390ec59af). One consequence to watch for:  `` [reflect.typelinks now returns types rather than offsets](https://github.com/golang/go/commit/87fae3622d), and that’s a symbol some libraries reach through  `` [//go:linkname](https://pkg.go.dev/cmd/compile#hdr-Linkname_Directive).
ðð [13096a6](https://github.com/golang/go/commit/13096a62e6), [481ab86](https://github.com/golang/go/commit/481ab86aaf), [6ef7fe9](https://github.com/golang/go/commit/6ef7fe9a48), [3390ec5](https://github.com/golang/go/commit/3390ec59af), [87fae36](https://github.com/golang/go/commit/87fae3622d)
- 

Unsanctioned  `//go:linkname`  gets harder. A new  `` [linknamestd directive](https://github.com/golang/go/commit/46755cb4de) marks linknames that only the standard library may pull,  `` [cmd/link](https://pkg.go.dev/cmd/link) now [checks linkname access to assembly symbols](https://github.com/golang/go/commit/aee6009ba5), and [export linknames were added across the tree](https://github.com/golang/go/commit/4dde0f6c36) for assembly symbols reached from other packages. If you depend on a linkname that Go never blessed, 1.27 is a good release to test against early.
ðð [46755cb](https://github.com/golang/go/commit/46755cb4de), [aee6009](https://github.com/golang/go/commit/aee6009ba5), [4dde0f6](https://github.com/golang/go/commit/4dde0f6c36)
- 

A new experimental map memory layout.  `` [GOEXPERIMENT](https://pkg.go.dev/internal/goexperiment) `=mapsplitgroup`  [changes the layout of a map group](https://github.com/golang/go/commit/5560073398) from interleaved key/value slots ( `KVKVKVKV` ) to split key and value arrays ( `KKKKVVVV` ). It’s off by default.
ðð [5560073](https://github.com/golang/go/commit/5560073398)
- 

 `os.Root`  closed another escape.  `` [ReadDir](https://pkg.go.dev/os@go1.27rc2#Root.ReadDir) and  `Readdir`  [could be used to escape a root](https://github.com/golang/go/commit/657ed934e8). Worth flagging because  `` [os.Root](https://pkg.go.dev/os@go1.27rc2#Root) is young and marketed as a containment boundary.
ðð [657ed93](https://github.com/golang/go/commit/657ed934e8)

## 

## 

[Final thoughts#](https://victoriametrics.com/blog/go-1-27/index.html#final-thoughts)

Go 1.27 is a meaty release whose center of gravity is the type system. A few themes stand out:
- Language: generic methods are the big one (a long-anticipated change that lets generic operations live on the types they belong to), joined by more ergonomic struct literals and broader type inference.
- Performance: size-specialized allocation makes allocation-heavy programs a little faster for free, and an experimental portable  `simd`  package opens the door to explicit vectorization.
- Security: post-quantum ML-DSA signatures land across  `crypto/mldsa` ,  `crypto/x509` , and  `crypto/tls` .
- Quality of life: a standard  `uuid`  package,  `json/v2`  graduating out of the experiment,  `CutLast` , and nicer testing helpers.

All in all, a strong release; a reminder that Go’s “boring on purpose” pace still delivers a lot each cycle.

P.S. Curious how we use Go at scale? The whole [VictoriaMetrics](https://github.com/VictoriaMetrics) stack (metrics, logs, and traces) is written in Go. Browse the [rest of our blog](https://victoriametrics.com/blog) for deep dives into the runtime, the standard library, and performance.
- [go](https://victoriametrics.com/blog/tags/go/)
- [golang](https://victoriametrics.com/blog/tags/golang/)
- [programming](https://victoriametrics.com/blog/tags/programming/)Leave a comment below or [Contact Us](https://victoriametrics.com/contact-us/) if you have any questions![comments powered by Disqus](https://disqus.com)

## You might also like:

- [Go @ VictoriaMetrics](https://victoriametrics.com/blog/categories/go-@-victoriametrics/)
- [Open Source Tech](https://victoriametrics.com/blog/categories/open-source-tech/)

### Understanding Go's sync.Map from API to Hash Trie

Go’s sync.Map now uses a hash trie. This article builds the implementation from a normal map, then explains lock-free reads, fine-grained writer locking, collisions, retries, deletion, Clear, Range, and the trade-offs against map plus RWMutex.
- [Go @ VictoriaMetrics](https://victoriametrics.com/blog/categories/go-@-victoriametrics/)
- [Open Source Tech](https://victoriametrics.com/blog/categories/open-source-tech/)

### Monotonic and Wall Clock Time in the Go time package

Operating systems expose a wall clock that can leap or slew with NTP and a monotonic clock that never runs backward. In Go, only time.Now (might) carries both readings, while values from time.Parse, time.Date, etc., are wall-clock-onlyâso naÃ¯ve equality checks or time.Since on those can mislead when the system clock shifts.
- [Go @ VictoriaMetrics](https://victoriametrics.com/blog/categories/go-@-victoriametrics/)
- [Open Source Tech](https://victoriametrics.com/blog/categories/open-source-tech/)

### Go synctest: Solving Flaky Tests

Traditional concurrent Go tests can be flaky due to non-deterministic scheduler behavior and timing. Go 1.24’s experimental synctest feature provides deterministic testing by running goroutines in isolated ‘bubbles’ where a synthetic clock only advances when all internally managed goroutines are durably blocked.
- [Go @ VictoriaMetrics](https://victoriametrics.com/blog/categories/go-@-victoriametrics/)
- [Open Source Tech](https://victoriametrics.com/blog/categories/open-source-tech/)

### Graceful Shutdown in Go: Practical Patterns

Go applications can implement graceful shutdown by handling termination signals (SIGTERM, SIGINT) via os/signal or signal.NotifyContext. Shutdown must complete within a specified timeout (e.g., Kubernetes’ terminationGracePeriodSeconds)…

## Media viewer

×

- [VictoriaMetrics](https://victoriametrics.com/products/victoriametrics/)
- [LogsQL](https://victoriametrics.com/products/logsql/)
- [VictoriaMetrics Enterprise](https://victoriametrics.com/products/enterprise/)
- [Monitoring of Monitoring](https://victoriametrics.com/products/mom/)
- [VictoriaLogs](https://victoriametrics.com/products/victorialogs/)
- [VictoriaMetrics Cloud](https://victoriametrics.com/products/cloud/)
- [VictoriaTraces](https://docs.victoriametrics.com/victoriatraces/)
- [VictoriaMetrics Anomaly Detection](https://victoriametrics.com/products/enterprise/anomaly-detection/)
- [Metrics QL](https://victoriametrics.com/products/metricsql/)
- [Plans & Features](https://victoriametrics.com/plans-features/)
- [Status Page](https://status.victoriametrics.com/)
- [Community](https://victoriametrics.com/community/)
- [GitHub Repo](https://github.com/VictoriaMetrics/VictoriaMetrics)
- [Blog](https://victoriametrics.com/blog/)
- [Case Studies](https://victoriametrics.com/case-studies/)
- [Security](https://victoriametrics.com/security/)
- [Docs](https://docs.victoriametrics.com/)
- [Careers](https://careers.victoriametrics.com/)
- [Our Customers](https://victoriametrics.com/customers/)
- [News & Articles](https://victoriametrics.com/news/)
- [24hr Support](https://victoriametrics.com/support/)
- [Privacy Policy](https://victoriametrics.com/legal/privacy-policy/)
- [Disclosure Policy](https://victoriametrics.com/legal/disclosure-policy/)
- [Cookie Use Policy](https://victoriametrics.com/legal/cookie-use-policy/)
- [Enterprise Solution Agreement](https://victoriametrics.com/legal/esa/)

Oops, it looks like something went wrong! Please let us know here [Contact Us](https://victoriametrics.com/contact-us/).

© 2019-2026 VictoriaMetrics

Many thanks for signing up for our newsletter. You have been added to our distribution list and you will receive our newsletter accordingly. Note that you can unsubscribe at any time from within the newsletter.Close

Many thanks for submitting our Contact Us form. One of our team members will be in touch shortly to follow up on it with you.Close
