---
title: "Clojure Hosted on Go"
url: https://github.com/glojurelang/glojure
clipped: 2026-08-31 12:22:54
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Clojure Hosted on Go](https://github.com/glojurelang/glojure)

## Digest Summary
Glojure is an early‑stage interpreter that runs Clojure code on the Go runtime, enabling direct use of Go libraries from Clojure and vice versa. It requires Go 1.19+ (minimum 1.24) and is installed via `go install github.com/glojurelang/glojure/cmd/glj@latest`. The `glj` command provides a REPL with vi/emacs editing modes, multiline editing, tab completion, persistent history, and job control. Expressions can be evaluated interactively, with `-e` for one‑liners, or by running `.glj` scripts; scripts can be compiled into standalone executables.

Glojure can also be embedded in Go programs using the `runtime.ReadEval` API, allowing Go functions to be exposed as Clojure vars and Clojure functions to be invoked from Go. By default it interoperates with many Go standard‑library packages (e.g., fmt, net/http, time). Additional packages can be made available through a generated “package map” using the `gen-import-interop` tool.

Typical use cases include standalone Clojure scripts, interactive development, and adding scriptable extensions to Go applications while retaining Go’s performance.

---

## Full Article

[Skip to content](https://github.com/glojurelang/glojure#start-of-content)

      
    
      
      

  
  
  

      

          

                

  
  
  

      
  
        
        You signed in with another tab or window. Reload to refresh your session.
        You signed out in another tab or window. Reload to refresh your session.
        You switched accounts on another tab or window. Reload to refresh your session.

      
Dismiss alert

  

    

  

    

  
    

  
    
      
    
    
      
      {{ message }}

    
  

  

    

  
        
    
      
      
    

      
  
  
    
  
    
      

      

###         Uh oh!

      

        

There was an error while loading. Please reload this page.

  
  

    

  

  

      

        
            
  
      
    
    
      [glojurelang](https://github.com/glojurelang)    
    /
    
      [glojure](https://github.com/glojurelang/glojure)
    

    Public
  

        

        
            
    
      

  
- 
            [Notifications](https://github.com/login?return_to=%2Fglojurelang%2Fglojure)    You must be signed in to change notification settings

  

  
- 
          [Fork
    16](https://github.com/login?return_to=%2Fglojurelang%2Fglojure)
  

  
- 
        
        [Star
          724](https://github.com/login?return_to=%2Fglojurelang%2Fglojure)
  

        
      

        

          

  
  

    
    

    
      
    

  
  
     main[Branches](https://github.com/glojurelang/glojure/branches)[Tags](https://github.com/glojurelang/glojure/tags)Go to fileCodeOpen more actions menu

## Latest commit

 

## History

[715 Commits](https://github.com/glojurelang/glojure/commits/main/)715 Commits

## Folders and files

NameNameLast commit messageLast commit date[.claude](https://github.com/glojurelang/glojure/tree/main/.claude)[.claude](https://github.com/glojurelang/glojure/tree/main/.claude)  [.github/workflows](https://github.com/glojurelang/glojure/tree/main/.github/workflows)[.github/workflows](https://github.com/glojurelang/glojure/tree/main/.github/workflows)  [benchmark](https://github.com/glojurelang/glojure/tree/main/benchmark)[benchmark](https://github.com/glojurelang/glojure/tree/main/benchmark)  [cmd](https://github.com/glojurelang/glojure/tree/main/cmd)[cmd](https://github.com/glojurelang/glojure/tree/main/cmd)  [doc](https://github.com/glojurelang/glojure/tree/main/doc)[doc](https://github.com/glojurelang/glojure/tree/main/doc)  [internal](https://github.com/glojurelang/glojure/tree/main/internal)[internal](https://github.com/glojurelang/glojure/tree/main/internal)  [nix](https://github.com/glojurelang/glojure/tree/main/nix)[nix](https://github.com/glojurelang/glojure/tree/main/nix)  [pkg](https://github.com/glojurelang/glojure/tree/main/pkg)[pkg](https://github.com/glojurelang/glojure/tree/main/pkg)  [scripts](https://github.com/glojurelang/glojure/tree/main/scripts)[scripts](https://github.com/glojurelang/glojure/tree/main/scripts)  [test/glojure/test_glojure](https://github.com/glojurelang/glojure/tree/main/test/glojure/test_glojure)[test/glojure/test_glojure](https://github.com/glojurelang/glojure/tree/main/test/glojure/test_glojure)  [.envrc](https://github.com/glojurelang/glojure/blob/main/.envrc)[.envrc](https://github.com/glojurelang/glojure/blob/main/.envrc)  [.gitignore](https://github.com/glojurelang/glojure/blob/main/.gitignore)[.gitignore](https://github.com/glojurelang/glojure/blob/main/.gitignore)  [CODEOWNERS](https://github.com/glojurelang/glojure/blob/main/CODEOWNERS)[CODEOWNERS](https://github.com/glojurelang/glojure/blob/main/CODEOWNERS)  [LICENSE.md](https://github.com/glojurelang/glojure/blob/main/LICENSE.md)[LICENSE.md](https://github.com/glojurelang/glojure/blob/main/LICENSE.md)  [Makefile](https://github.com/glojurelang/glojure/blob/main/Makefile)[Makefile](https://github.com/glojurelang/glojure/blob/main/Makefile)  [README.md](https://github.com/glojurelang/glojure/blob/main/README.md)[README.md](https://github.com/glojurelang/glojure/blob/main/README.md)  [go.mod](https://github.com/glojurelang/glojure/blob/main/go.mod)[go.mod](https://github.com/glojurelang/glojure/blob/main/go.mod)  [go.sum](https://github.com/glojurelang/glojure/blob/main/go.sum)[go.sum](https://github.com/glojurelang/glojure/blob/main/go.sum)  [shell.nix](https://github.com/glojurelang/glojure/blob/main/shell.nix)[shell.nix](https://github.com/glojurelang/glojure/blob/main/shell.nix)  View all files

## Repository files navigation

# Glojure

[Try it in your browser!](https://glojurelang.github.io/glojure/)

Gopher image derived from [@egonelbre](https://github.com/egonelbre/gophers), licensed under [Creative Commons 1.0 Attributions license](https://creativecommons.org/licenses/by/1.0/).

Glojure is an interpreter for
[Clojure](https://clojure.org/), hosted on Go. Glojure provides
easy access to Go libraries, similar to how Clojure provides easy
access to Java frameworks.

Glojure is in early development; expect bugs, missing features,
and limited performance. Backwards compatibility is not
guaranteed until a v1 release. That said, it is used successfully
in hobby projects and runs a significant subset of
the (transformed) core Clojure library.

Note that unlike most other Go implementations of Clojure, Glojure is
a "hosted" language - a term used to describe languages that are
implemented in terms of a host language (in this case, Go). This means
that all Go values can be used as Glojure values and vice versa.

## Prerequisites

Before you get started with Glojure, make sure you have installed
and have knowledge of Go (version 1.24 or higher).

## Installation

Glojure is currently available from source for all platforms where Go
can run, and it requires at least go 1.24.

Install it with the  `go install`  command:
 ` `$ go install github.com/glojurelang/glojure/cmd/glj@latest
` ` 

After installation, you can start the REPL (Read-Eval-Print-Loop) with
the  `glj`  command:
 ` `$ glj
user=> (println "Hello, world!")
Hello, world!
nil
user=>
` ` 

## Usage

Glojure can be used in two ways: as a standalone command-line tool ( `glj` ) or
embedded within Go applications.

### Using the  `glj`  Command

The  `glj`  command provides a traditional Clojure development experience:

Show the help:
 ` `$ glj --help   # or glj -h
` ` 

Show the version:
 ` `$ glj --version
glojure v0.3.0
` ` 

Start a REPL (interactive session):
 ` `user=> *glojure-version*
{:major 0, :minor 3, :incremental 0, :qualifier nil}
$ glj
user=> (+ 1 2 3)
6
user=> (println "Hello from Glojure!")
Hello from Glojure!
nil
` ` 

#### REPL Features

The interactive REPL includes:

- Vi and emacs editing modes -- vi is the default; configure via
 `~/.inputrc` 

- Multiline editing -- incomplete expressions continue on the next
line with auto-indent

- Tab completion -- symbols, namespaces, and aliases with
descriptive labels

- Smart indentation -- Tab inserts 2 spaces; Backspace removes a
full indent level

- Persistent history -- saved to  `~/.glj_history`  across sessions

- Bracketed paste -- paste blocks of code instantly

- Job control -- Ctrl+Z suspends,  `fg`  resumes cleanly

- Interrupt -- Ctrl+C cancels input or interrupts evaluation

Evaluate expressions:
 ` `$ glj -e '(println "Hello, World!")'
Hello, World!
$ glj -e '(apply + (range 3 10))'
42
$ glj -e '
(defn factorial [n] (if (<= n 1) 1 (* n (factorial (dec n)))))
(factorial 5)'
120
` ` 

Run a Clojure script:
 `;; hello.glj
(println "Hello," (first *command-line-args*))` 
 ` `$ glj hello.glj World
Hello, World
` ` 

Create executable programs:
 `;; server.glj
(ns example.server)

(defn echo-handler
  [w r]
  (io.Copy w (.Body r))
  nil)

(net:http.Handle "/" (net:http.HandlerFunc echo-handler))
(println "Server starting on :8080...")
(net:http.ListenAndServe ":8080" nil)` 
 ` `$ glj server.glj
Server starting on :8080...
` ` 

#### Dynamic dependencies

Glojure embeds the ClojureStar dependency facade and Grenadine resolver. A
script can acquire a Maven library and import its namespace without a JVM:
 `(require '[clojurestar.deps :refer [require-deps]])

(require-deps
 ["mvn:dev.weavejester/medley@1.10.0/medley.core" :as medley])

(println (medley/index-by :id [{:id 1} {:id 2}]))` 

Literal libspec vectors do not need quoting; quoted vectors remain supported.
 `require-deps`  accepts Maven, Gist, and GitHub source-file coordinates, with  `:as`  or an explicit
 `:refer [...]`  list. Use  `clojurestar.deps/add-deps`  or  `glojure.deps` 
for deps.edn-style Maven, Git, and local coordinates.
A pinned Gist file accepts either  `gist:<owner>/<id>/<file>@<revision>`  or
 `gist:<owner>/<id>/<revision>/<file>` ; both forms use the same cache entry.
A GitHub source file accepts either
 `github:<owner>/<repo>/<ref>/<path.clj|cljc>`  or the equivalent
 `github:<owner>/<repo>/blob/<ref>/<path.clj|cljc>`  form. Refs occupy one path
segment; full commit SHAs reuse persistent cache while named refs refresh in a
new process. Selected files must be self-contained and begin with an  `ns`  form.

The Maven repository is selected in this order:

- explicit  `:mvn/local-repo`  or  `:local-repo` ;

-  `GLOJURE_MAVEN_REPOSITORY` ;

-  `GRENADINE_MAVEN_REPOSITORY` ;

-  `$HOME/.m2/repository` .

The Git, Gist, and GitHub source cache root uses explicit  `:gitlibs/dir`  or  `:gitlibs-dir` , then
 `GLOJURE_GITLIBS_DIR` ,  `GRENADINE_GITLIBS_DIR` ,  `GITLIBS` , and finally
 `$HOME/.gitlibs` . Gist and GitHub source are stored under  `gist/`  and
 `github/`  in that root;
 `require-deps`  also accepts  `:cache-dir`  as a compatibility alias.

Glojure supplies  `org.clojure/clojure`  and  `org.clojure/clojurescript` , so
those coordinates are terminal: their artifacts and transitive dependencies
are not acquired. Explicit dependencies such as  `org.clojure/spec.alpha` 
remain ordinary coordinates, subject to Glojure's source compatibility.

### Embedding Glojure in Go Applications

You can also embed Glojure as a scripting language within your Go applications.
This is useful when you want to:

- Add scriptable configuration to your Go application

- Allow users to extend your application with Clojure plugins

- Mix Go's performance with Clojure's expressiveness

- Control the execution environment (custom I/O, sandboxing)

#### Compact AOT executables

Applications that ship precompiled namespace loaders can omit development-only
runtime features:
 `go build -trimpath -tags glj_aot_runtime -ldflags="-s -w" ./cmd/myapp` 

The  `glj_aot_runtime`  tag retains evaluation,  `clojure.core` , and file I/O
support required by core functions such as  `slurp`  and  `spit` . It omits the Go
source generator, the broad default Go export registry, fallback standard
library source, HTTP URL I/O, and precompiled loaders for optional namespaces.
Import every precompiled application or optional standard-library namespace
used by the executable:
 `import (
    _ "example.com/myapp/generated/example/app"
    _ "github.com/glojurelang/glojure/pkg/stdlib/clojure/string"
)` 

Programs that use  `slurp`  with HTTP URLs can link that support explicitly:
 `import _ "github.com/glojurelang/glojure/pkg/stdlib/glojure/go/io/http"` 

Programs that dynamically access the default Go exports can opt back in with a
blank import of  `github.com/glojurelang/glojure/pkg/gen/gljimports` . Generate
new loaders with a normal development build; compact runtime builds
intentionally reject  `(compile ...)` .

Basic embedding example:
 `package main

import (
    "fmt"
    _ "github.com/glojurelang/glojure/pkg/glj"  // Initialize Glojure
    "github.com/glojurelang/glojure/pkg/runtime"
)

func main() {
    // Evaluate Clojure code
    result := runtime.ReadEval(`
        (defn factorial [n]
          (if (<= n 1)
            1
            (* n (factorial (dec n)))))
        (factorial 5)
    `)
    fmt.Printf("5! = %v\n", result) // 5! = 120
}` 

Calling Go from Clojure and vice versa:
 `package main

import (
    "fmt"
    "github.com/glojurelang/glojure/pkg/glj"
    "github.com/glojurelang/glojure/pkg/runtime"
)

// Define a Go function
func greet(name string) string {
    return fmt.Sprintf("Hello, %s from Go!", name)
}

func main() {
    // Make the Go function available to Clojure
    runtime.ReadEval(`(def greet-from-go nil)`) // placeholder
    greetVar := glj.Var("user", "greet-from-go")
    greetVar.SetRoot(greet)

    // Use it from Clojure
    result := runtime.ReadEval(`(greet-from-go "Clojure")`)
    fmt.Println(result) // "Hello, Clojure from Go!"

    // Call a Clojure function from Go
    runtime.ReadEval(`(defn add [x y] (+ x y))`)
    addFn := glj.Var("user", "add")
    sum := addFn.Invoke(10, 32)
    fmt.Printf("Sum: %v\n", sum) // Sum: 42
}` 

Accessing your own Go packages:

When embedding Glojure, you can also expose your own Go packages or additional standard library packages using the package map approach described in the [Accessing additional Go packages](https://github.com/glojurelang/glojure#accessing-additional-go-packages) section below. This allows embedded Clojure code to access any Go packages you choose to expose:
 `import (
    _ "github.com/glojurelang/glojure/pkg/glj"
    _ "your.app/gljimports" // Your generated package map
)

// Now Clojure code can access your exposed packages
runtime.ReadEval(`
    (your$package.YourFunction "arg")
    (another$package.Method)
`)` 

### When to Use Each Approach

Use  `glj`  command for:

- Writing standalone Clojure programs

- Interactive development with the REPL

- Running Clojure scripts

- Evaluating expressions directly from the command line

- Learning Clojure with Go interop

Embed Glojure for:

- Adding scripting to an existing Go application

- Building a platform that users extend with Clojure

- Custom control over the Glojure execution environment

- Mixing Go and Clojure in a single binary

### Interop

Glojure ships with interop with many standard library packages
out-of-the-box.  Go package names are munged to avoid ambiguity with
the use of  `/`  to refer to namespaced symbols; instances of  `/`  in
package names are replaced with  `:` . Here's a simple example:
 `user=> (println (fmt.Sprintf "A couple of HTTP methods: %v" [net:http.MethodGet net:http.MethodPost]))
A couple of HTTP methods: ["GET" "POST"]
nil` 

The following standard library packages are included by default:

-  `bytes` 

-  `context` 

-  `errors` 

-  `flag` 

-  `fmt` 

-  `io` 

-  `io/fs` 

-  `io/ioutil` 

-  `math` 

-  `math/big` 

-  `math/rand` 

-  `net/http` 

-  `os` 

-  `os/exec` 

-  `os/signal` 

-  `path/filepath` 

-  `reflect` 

-  `regexp` 

-  `runtime/debug` 

-  `sort` 

-  `strconv` 

-  `strings` 

-  `sync` 

-  `sync/atomic` 

-  `time` 

-  `unicode` 

To expose additional packages, you must generate a "package map" and compile your own executable
that imports both your package map and the Glojure API. See the section below for more details.

Expect improvements to both the availability of standard library packages and interop workflows.

#### Accessing additional Go packages

The  `gen-import-interop`  can be used to emit the contents of a .go file
that will export a function that can be used to add the exports of
additional packages to the Glojure package map.
 ` `$ go run github.com/glojurelang/glojure/cmd/gen-import-interop \
     -packages=:comma-separated-package-list: \
     > your/package/gljimports/my_package_map.go
` ` 

Then, in your own program:
 `package main

import (
	// Add your packages' exports to the pkgmap.
	_ "your.package/gljimports"
)

// ...` 

## Differences from Clojure

### Numbers

Clojure Type
Glojure Type
Notes

 `long` 
 `int64` 

 `double` 
 `float64` 

 `float` 
 `float32` 

 `byte` 
 `byte` 
Note that Go bytes are unsigned, whereas JVM bytes are signed.

 `short` 
 `int16` 

 `int` 
 `int` 
Note that JVM ints are 32-bit, whereas Go ints are 32- or 64-bit depending on the platform.

 `char` 
 `lang.Char` 
The Glojure type is a tagged rune ( `type Char rune` ). JVM chars are 16-bit whereas Go runes are 32-bit.

 `BigInt` 
 `*lang.BigInt` 
The Glojure type wraps  `*big.Int` .

 `BigDecimal` 
 `*lang.BigDecimal` 
The Glojure type wraps  `*big.Float` .

 `Ratio` 
 `*lang.Ratio` 
The Glojure type wraps  `*big.Rat` .

 `BigInteger` 
 `*big.Int` 
Native JVM BigInteger corresponds to  `*big.Int` .

## Comparisons to other Go ports of Clojure

Aspect
Glojure
[Joker](https://github.com/candid82/joker)
[let-go](https://github.com/nooga/let-go)

Hosted[1](https://github.com/glojurelang/glojure#user-content-fn-1-74b4d3dba7a39bae1d6cea68c079061e)
Yes
No
No

Extensible Go interop
Yes
No
No

Concurrency
Yes
Yes (with GIL)
Yes

Clojure tooling (e.g. linter)
No
Yes
No

Execution
Tree-walk interpreter
Tree-walk interpreter
Bytecode Interpreter

If you'd like to see another port in this table, or if you believe
there is an error in it, please file an issue or open a pull request!

## Footnotes

- 

What does it mean to be a hosted
language? For Clojure on the JVM, it means that all Java values are
also Clojure values, and vice versa. Glojure strives to maintain the
same relationship with Go. [↩](https://github.com/glojurelang/glojure#user-content-fnref-1-74b4d3dba7a39bae1d6cea68c079061e)

## About

Clojure interpreter hosted on Go, with extensible interop support.

### Resources

[Readme](https://github.com/glojurelang/glojure#readme-ov-file)[EPL-1.0 license](https://github.com/glojurelang/glojure#EPL-1.0-1-ov-file)[Activity](https://github.com/glojurelang/glojure/activity)[Custom properties](https://github.com/glojurelang/glojure/custom-properties)

### Stars

724 stars

### Watchers

8 watching

### Forks

[16 forks](https://github.com/glojurelang/glojure/forks)[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fglojurelang%2Fglojure&report=glojurelang+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

   

  

    
  

  

          

    

  
    
    
      
    
    You can’t perform that action at this time.
