---
title: "Guix for Development"
url: https://dthompson.us/posts/guix-for-development.html
clipped: 2026-06-17 01:53:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Guix for Development](https://dthompson.us/posts/guix-for-development.html)

## Digest Summary
Guix is a general‑purpose, functional package manager that can be layered on any Linux distribution or used as a standalone OS. Its `guix shell` command creates temporary, per‑project environments without polluting the system `/usr` tree, effectively acting as a universal virtualenv. When invoked, it reads a `guix.scm` file in the project directory, which declaratively lists all runtime and build‑time dependencies as Scheme code (e.g., Guile 3, SDL2, make, texinfo). Guix then fetches or builds the complete dependency graph, allowing standard commands such as `./configure` and `make` to run inside an isolated shell. Optional flags provide further isolation: `--pure` clears most environment variables, while `--container` executes the shell in separate Linux namespaces. The environment can be integrated with tools like `direnv` (via `eval $(guix shell --search-paths)`) and Emacs (through the direnv extension). The same `guix.scm` can be used with `guix build -f` for reproducible builds or `guix package -f` for installation. The author advocates this workflow for rapid, reproducible development across multiple projects.

## Discussion Summary
Comments express overall enthusiasm for both Guix and Nix as superior tools for deterministic, per‑project dependency management, noting Guix’s appealing Scheme‑based language but questioning its smaller package collection. Users acknowledge recent Guix releases and view the declarative approach as a promising, though not yet mainstream, development trend, while criticizing Docker as a temporary fix. Optimism persists that Guix may eventually dominate, even if widespread adoption remains uncertain, and some suggest the possibility of translating Nix derivations into Guix definitions.

---

## Full Article

[This wonderful
article](https://gexp.no/blog/hacking-anything-with-gnu-guix.html) by
Marius Bakke (thanks for using
[Haunt](https://dthompson.us/projects/haunt.html) btw!) about `guix shell` hit the orange website front page recently. I left a comment
to the effect of âhell yeah I use it for all my projects!â and someone
asked me for an example of what I do. I sent them some links but I
thought hey, this could be a blog post and I haven't written one of
those in *years*!

The tl;dr is that [Guix](https://guix.gnu.org) is a fantastic
developer productivity tool that can easily automate development
environment creation and pre-release build testing and you should give
it a try but if you like what you already use then that's fine, too.

There's gotta be a better way!
------------------------------

This is the âAre you tired of *this*?â part of the infomercial. Read
the next few paragraphs and picture me, in black and white, struggling
to hold a large stack of boxes, all labeled âsoftware.â I continue
struggling to balance the boxes as you read. When you've reached the
last paragraph of the section, I fall over, the boxes land on top of
me and all over the floor, I'm covered in spaghetti, and in an
exasperated voice I shout âThere's gotta be a better way!â

When setting up a new computer for software development, I want to go
from `git clone` to `make` in as little time as possible (adjust that
for your VCS and build system of choice.) In the old days, this meant
manually installing the dependencies through the distro package
manager. If things are organized, the project README will have a list
of what is needed and it's not so bad. If things are less organized,
it's a cycle of installing packages and running `./configure` or
whatever until it succeeds. Hopefully none of the dependencies are
too new to be found in the distro. And when working on multiple
projects, hopefully there's no conflicts between the dependencies
required for each of them, because your development environment is the
entire system and there's no way to isolate different projects from
each other.

Of course, different programming languages provide their own sets of
tools for managing multiple projects. Python has virtualenv, Ruby has
rvm and bundler, Node has nvm and npm, etc. But their domain is
restricted to only the dependencies for that language and their
runtimes. A system package manager is needed to bootstrap their use.

Nowadays it's âjust use Docker.â Docker's take is that all this
package management stuff is just too complicated. Instead, just
create a disk image per project that encapsulates this hodgepodge of
package managers and bespoke, artisinal, small-batch builds that gets
run in isolation via Linux namespace magic. It works, of course, but
I think Dockerfiles are clunky and the rather extreme level of
isolation is usually unnecessary and makes things overly complicated
for projects that need to interact with, say, the windowing system of
the host computer. A lot of people are happy with Docker, though.
Maybe you are, too. That's fine!

What I really want to say is âComputer, provision a development
environment containing Guile 3, SDL2, make, and texinfo!â and have
Majel Barrett-Roddenberry tell me that all of those things have been
made available to me on my host system. No container, no virtual
machine. It shouldn't matter if I have Guile 2 installed system-wide,
Guile 3 should still be what's used in the context of the project.
This is how Guix works and it's very good and cool and I'm going to
tell you all about how I use it.

Two easy payments and one complicated payment
---------------------------------------------

Guix is a general-purpose package manager that can be used on top of
any distro and also *it is a distro*. I use it both on Ubuntu and as
a standalone distro. It takes a few minutes to [install on top of an
existing
distro](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)
but once it's there the magic begins. Software installed with Guix is
not installed globally (`/usr`), which allows it to act like a
`virtualenv` for everything. Guix provides the [guix
shell](https://guix.gnu.org/en/manual/devel/en/html_node/Invoking-guix-shell.html)
tool for creating temporary environments with an arbitrary set of
software inside.

Let's start with a real world example. Here's how to build Guile's
SDL2 bindings from a Git checkout using Guix:

```
git clone https://git.dthompson.us/guile-sdl2.git
cd guile-sdl2
echo $PWD >> $HOME/.config/guix/shell-authorized-directories
guix shell
./configure
make
```

Looks pretty straightforward except for that third line, which
whitelists the project directory as a place that `guix shell` can be
used for security reasons (though I think the potential risk is not
worth this extra step that I'm now burdened with explaining!) I don't
have to look at a `README` to know what software I need to install.
The project is pre-configured to work with Guix and the software it
installs does not affect the whole system.

So what's happening? Well, `guix shell` automatically searches the
current directory for a `guix.scm` file and loads it. Inside that
file is all the information needed to construct an environment that
can build the source code:

```
(use-modules (guix git)
             (guix packages)
             (guix licenses)
             (guix build-system gnu)
             (gnu packages)
             (gnu packages autotools)
             (gnu packages guile)
             (gnu packages pkg-config)
             (gnu packages sdl)
             (gnu packages texinfo))

(package
  (name "guile-sdl2")
  (version "0.7.0")
  (source (git-checkout (url (dirname (current-filename)))))
  (build-system gnu-build-system)
  (arguments
   '(#:make-flags '("GUILE_AUTO_COMPILE=0")
     #:phases
     (modify-phases %standard-phases
       (add-after 'unpack 'bootstrap
         (lambda _ (invoke "sh" "bootstrap"))))))
  (native-inputs (list autoconf automake pkg-config texinfo))
  (inputs (list guile-3.0-latest sdl2 sdl2-image sdl2-mixer sdl2-ttf))
  (synopsis "Guile bindings for SDL2")
  (description "Guile-SDL2 provides pure Guile Scheme bindings to the SDL2 C shared
library via the foreign function interface.")
  (home-page "https://git.dthompson.us/guile-sdl2.git")
  (license lgpl3+))
```

This is what's known as âconfiguration as codeâ and it looks kinda
like a `package.json` (not code) or a `.gemspec` (code) file.
`guix.scm` contains not just inert data, but a small Scheme program
that returns a Guix package. `guix shell` sees to it that all of the
dependencies (listed in the `inputs` and `native-inputs` sections) are
available within the shell session it creates by downloading (or
building, if necessary) the entire dependency tree. Going back to the
earlier example, `./configure` and `make` run in the context of that
new shell session and are thus able to complete successfully.

Should you want/need more isolation from the host system, `guix shell`
has you covered. The `--pure` flag will clear out most existing
environments variables, such as `$PATH`, so that the resulting
environment does not contain pointers to places like `/usr`. For more
Docker-like isolation, the `--container` flag can be used, which will
run the new shell session within a set of Linux namespaces so that the
host system is inaccessible. I rarely use either flag.

`guix shell` runs pretty fast after it downloads all the required
software the first time, and it can be run non-interactively, so it's
pretty handy to use in scripts. It can even be used with
[direnv](https://direnv.net/) by adding this to `.envrc`:

```
eval $(guix shell --search-paths)
```

I'm an Emacs user, so I want to integrate `guix shell` there, as well.
Turns out that's pretty easy via the
[emacs-direnv](https://github.com/wbolster/emacs-direnv) extension.
With `direnv-mode` enabled, I can run `M-x compile`, enter `make` as
the compilation command, and build my project from within Emacs using
the environment built by `guix shell`. Pretty fancy! Thanks to
Andrew Whatson for teaching me about this.

The same `guix.scm` file can be used with more than just `guix shell`.
For example, `guix build -f guix.scm` will build the project from
scratch outside of your project directory, which could reveal issues
like forgetting to commit a new file (something I've done too many
times.) `guix package -f guix.scm` will build *and* install the
package, which could be used to confirm that a ârealâ build works the
same as the version in the development environment.

Supplies are limited, order today!
----------------------------------

I hope this helps someone out there considering a Guix-based
development workflow or is just wondering what the deal is. I haven't
come across too many people in this [wild
world](https://www.youtube.com/watch?v=84Y9PjfLZZE) that use `guix shell` the same way I do, so part of the motivation behind this post
is an attempt to get more Guix users to adopt this pattern.

Oh and finally I should say that I'm not trying to convince anyone to
give up what works for them, be it Docker, Nix, or whatever else. I
don't think anyone is âdoing it wrong.â Use what makes you feel
productive and hack the good hack. This is just how I do it.