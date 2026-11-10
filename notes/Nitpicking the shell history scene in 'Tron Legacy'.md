---
title: "Nitpicking the shell history scene in 'Tron: Legacy'"
url: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/
clipped: 2026-06-17 00:56:15
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hacking culture
  - solaris os
  - technical accuracy
related:
  - "[[Hammerspoon]]"
  - "[[U+237C ⍼ Is Azimuth]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Critically analyzes the Unix command history sequence shown in Tron: Legacy, identifying a blend of genuine commands, kernel indicators, and cinematic shortcuts.
>
> **Key points:**
> - Performs a detailed breakdown of Sam Flynn's hacking sequence on his father's terminal in Tron: Legacy.
> - Identifies references to SolarOS (Solaris) and shows how process lists reveal a Linux kernel underneath.
> - Explains how commands like whoami, uname, and configure are used realistically but contain movie-specific shortcuts.
> - Discusses the film's efforts to portray authentic Unix tools compared to typical Hollywood interface tropes.
>
> **Concept links:** [[Cinematic Computers]], [[Solaris OS]], [[Linux Commands]], [[Hacking Culture]], [[Technical Accuracy]]
>
> **Suggested connections:**
> - [[Hammerspoon]] — connects to configuring custom shell and operating system environments.
> - [[U+237C ⍼ Is Azimuth]] — links to the forensic investigation of obscure technical symbols and details.
<!-- ai-summary:end -->

# [Nitpicking the shell history scene in 'Tron: Legacy'](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/)

## Digest Summary
The article analyses the Unix‑like shell screenshot shown when Sam Flynn accesses his father’s computer in *Tron: Legacy*. The transcript begins with `whoami` (yielding “flynn”), `uname -a` (reporting “SolarOS 4.0.1 … sun4m i386”), and a failed `login -n root` followed by a successful `login: backdoor`, which uses UID 0 and sets the home directory to “/”. The history is displayed via a custom `bin/history` script rather than the builtin `history`, implying the filmmakers scripted the output. The OS name “SolarOS” and the `sun4m` identifier suggest a deliberately altered Solaris, but other commands (`top`, `iostat`, `cat /proc/meminfo`) and process names (kthreadd, scsi_eh_…, migration) reveal a Linux kernel underneath. The command sequence shows a non‑standard `./configure -o test.cfg` followed by `make` and `make install`, indicating a bespoke configuration script for the “LLL laser” controller rather than a typical Autoconf workflow. Overall, the scene mixes realistic Unix commands with several anachronisms and scripted shortcuts to convey plausible system activity.

## Discussion Summary
Comments collectively praise the film’s authentic Unix‑style hacking sequence, noting specific details such as Emacs versus vi, realistic login prompts, and accurate use of kill commands, while also offering technical nitpicks about user names, file paths, and OS distinctions. Viewers express personal nostalgia and credit the scene for inspiring deeper interest in computing. Parallel discussion addresses copyright concerns, describing a shift from YouTube to a personal site under fair‑use arguments. Some criticism targets later installments for abandoning the realistic terminal portrayal, yet overall sentiment remains appreciative of the original’s technical fidelity and production craftsmanship.

---

## Full Article

Nitpicking the shell history scene in Tron: Legacy
==================================================

[Simon Tatham, 2026-05-28]

Introduction
------------

In the 2010 film Tron: Legacy, there's a scene
where the main character Sam Flynn sits down at a computer in
his fatherâs study, and types some commands to try to figure out
what Flynn senior had last been working on, before mysteriously
disappearing.

When I first watched the film (conveniently, already on DVD), I
paused it so that I could have a close look at the text on the
computer screen. What can I say? Iâm that kind of geek.

The Tron film series as a whole is based on
some *completely* ludicrous premises about how computers
work. So I wasnât expecting realism; more likely I thought it
would be hilarious fake-computerese nonsense made up entirely by
movie people. In fact I saw an *almost* plausible Unix
shell transcript, whose contents made sense in the context of
the film plot â albeit with a couple of nits that jumped out at
me immediately.

This year, I remembered that scene, and thought it might make a
good learning exercise for a junior colleague: letâs look at
that still image together and see how much we can understand
about it. Can we find all the outright errors? Disregarding
things weâve definitely decided are errors, what can we infer
from the rest of it about the computer system and what the
Flynns (both of them) are doing with it?

I hoped this might be fun, interesting, and/or educational. It
succeeded at all three, beyond my hopes! Instead of the half
hour Iâd guessed, we spent a whole day on it, on and off
(exchanging Slack messages, in between other work), and squeezed
a lot more juice out of it than Iâd realised was there to be
squozen. By the end of the exercise, Iâd decided one of my own
initial complaints was wrong (but found another to replace it),
and Iâd learned some new things myself. And I ended up more
impressed than Iâd started, with whoever constructed that
screenshot.

So, since it ended up being that much fun, hereâs a writeup, so
that if youâre the same kind of geek as me, you can share the
enjoyment!

Spoilers
--------

This article will include a minor spoiler for a thing that
happens in the film. But it wonât be anything you couldnât
easily have guessed was going to appear *somewhere* in
the film, just from having watched the original 1982 film that
this is a sequel to, Tron itself. In any case,
even Tron: Legacy is 16 years old by now and
another Tron film has come out since, so if you
care about spoilers for it at all, youâve probably already seen
it.

More to the point, when I set this exercise to my colleague, it
was intended as an educational puzzle â the point was
to *work out* the answers, not just hear them in the form
of a lecture. So Iâm going to take care not to spoil that
puzzle. In this article Iâll present all the answers I have, but
theyâre below a `<details>` fold, so you can
examine the transcript yourself before clicking through, and see
how much you can get from it yourself.

The screenshot
--------------

Of course I have to start by showing a still image from the
film. My understanding (though I am not a lawyer) is that this
should be justifiable under copyright law.
However, of course, I donât have the resources to defend myself
in a serious fight against Disney, so if they should demand that
I take the image down, Iâll have no choice but to do so.

![](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/screenshot.webp)

The smears in front of the text, and the uneven background
colour behind it, are because the screen is a reflective desk
surface which had a thick layer of dust all over it until a
moment ago; just before Sam sat down, we saw him wipe some of
the dust off.

When Sam arrived, the main shell window on the right was empty.
Everything shown in it here is commands he typed himself just
now, and the computerâs responses to those commands.

### Text transcript

Iâve typed this out by hand so that you donât have to: hereâs a
text transcript of the session in that main shell window.

```
$ whoami
flynn
$ uname -a
SolarOS 4.0.1 Generic_50203-02 sun4m i386
Unknown.Unknown
$ login -n root
Login incorrect
login: backdoor
No home directory specified in password file!
Logging in with home=/
# bin/history
  488  cd /opt/LLL/controller/laser/
  489  vi LLLSDLaserControl.c
  490  make
  491  make install
  492  ./sanity_check
  493  ./configure -o test.cfg
  494  vi test.cfg
  495  vi ~/last_will_and_testament.txt
  496  cat /proc/meminfo
  497  ps -a -x -u
  498  kill -9 2207
  499  kill 2208
  500  ps -a -x -u
  501  touch /opt/LLL/run/ok
  502  LLLSDLaserControl -ok 1
#
```

What can we observe from this screenshot?
-----------------------------------------

If youâre up for trying this exercise yourself, have a good
look at the image above, and see what you can see. When youâre
ready, click through the cut below, and youâll see a list of
topics to think about. If those give you useful hints, youâve
got another chance to think harder about each one, before you
open each topic in turn to see the thoughts we had about it.

Topic list

The command that prints the shell history

This was the very first thing that jumped out at me when
I first watched this film and paused the DVD. Sam requests
the shell history by running `bin/history`
instead of just `history`. Why?

I canât see any possible way that makes sense on real
Unix. Shell history is stored in data structures inside
the shell process itself, so the `history`
command must be a shell builtin, in order to read out
those structures. Even if you only wanted to read out the
version of the history stored in a disk file, the name and
location of that file varies with the shell and its
configuration, so an external command that
did *that* would still be very difficult to get
right.

My conclusion at the time â and it still seems fairly
plausible to me now â is that this is revealing the
technique the filmmakers used to present their fake
plot-related shell history. (Like an accidental visible
wire, in wire-fu.) I think this shell session was
generated by typing commands into a real, carefully
configured, Unix machine, and `bin/history` was
a simple shell script that prints *that* history in
place of whatever more boring thing existed in the real
shell.

(Note, in particular, that the history doesnât end with
the command `bin/history`! When you run a real
shell history command, generally the output ends with the
very `history` command you just typed, because
itâs been inserted into the history list before the
history list is read back out.)

Supposing Iâm right, this could have been done better, by
wrapping the `history` shell builtin with an
alias or function. Then the user could have typed
plain `history`, and it still could have been
made to produce this carefully constructed output.

(The same argument doesnât apply to other commands Sam
types in this session, like `uname`, because
those arenât shell builtins: theyâre found
on `PATH`, so you can override them by putting
your own directory earlier on `PATH`. So my
guess is that whoever set up this scene knew how to do
that, but didnât know how to do aliases.)


The account setup on the computer

The first thing Sam sees is a shell prompt, not a login
prompt: Flynn had left himself logged in. So he starts by
running `whoami`, to determine who he was
logged in *as*. The computer
prints `flynn`, presumably an unprivileged user
account. Thatâs no good â Sam knows heâs going to need to
be root to investigate properly. He tries to log in
as `root`, but fails, so he
tries `backdoor` instead, which succeeds.

A natural question is: if `root`
and `backdoor` are separate accounts, isnât he
about to list the shell history from the wrong one? Surely
Flynn was logged in as `root` to do whatever he
was doing.

But we can see that the `backdoor` account has
user id 0, the same as `root`, because after
Sam successfully logs in as `backdoor`, the
shell prompt is a `#` instead of
a `$`. That typically happens when the shell
detects that itâs running as the root uid.
So `backdoor` and `root` share a
uid, and so itâs reasonable to guess that they share a
home directory and shell history too.

We also see that `backdoor`âs home directory
is taken by `login` to be the VFS
root, `/`, because nothing better is specified
in `/etc/passwd`. So presumably the shell just
read a history file from the VFS root: something like
`/.bash_history`, or at
least `/.something_history` (I donât
think thereâs much evidence of exactly what shell this
is). Itâs fairly plausible that `root` also has
its home directory set to `/`; thatâs not the
default on Linux, which gives `root` a proper
home directory of its own, but it was certainly pretty
common on proprietary Unixes I used in the 1990s.

So that all hangs together: Flynn ran those commands
as `root`, and by a slightly roundabout route,
Sam might indeed have logged in to an account that can
list them in a natural way.

(Iâm also a bit suspicious of the use
of `login` to switch user from within an
existing login session; one would expect
perhaps `su`? To do this
job, `/bin/login` would need to be setuid, and
it certainly isnât on Linux â it expects to be invoked by
programs like `getty` or
(historically) `telnetd`, which are already
root when they run it. *Perhaps* Solaris (or
SolarOS) is different? But it seems unlikely.)

Finally, why is there a `backdoor` account
anyway? Normally you make one of those if you have access
to a system but are worried that someone will try to take
that access away from you (and are unscrupulous). A hacker
worried their original entry route will be closed off, or
one of the people with root on a system, worrying that the
other(s) will take their access away. In this case, itâs
Flynnâs own machine; who was he expecting to lock him out
of it, to need a back door to get back in?

We could simply appeal to Scriptwritersâ Shortcuts:
sometimes systems have back doors, so you can assume there
is one if the plot requires it, and nobody needs to
provide an in-world explanation. But we
mostly *havenât* had to use that kind of non-answer
in this exercise, so Iâd rather not. I think a perfectly
good in-world explanation is that *Sam* made the
back door, without his dadâs knowledge. Perhaps Flynn
trusted his son with root on the same machine (plausible
â *my* dad trusted me, when we shared a Linux
system), but Sam had some reason to suspect that Flynn was
becoming secretive and mysterious, and anticipated that
Flynn might close off the root account to try to hide what
he was up to. And it looks as if that *did* happen,
because we can see that Sam initially *expected* to
be able to log in as proper `root`, and only
used the back door once he found he couldnât do that.
Apparently he knew his father well, and was right to
suspect!


What flavour of Unix is this, anyway?

Another initial investigatory command Sam runs
is `uname -a`, to check exactly what kind of
Unix system heâs looking at. You could imagine that that
might change his choice of subsequent commands to type, if
heâs enough of a Unix generalist to know which OSes spell
which detailed things differently.

The operating system name printed by `uname`
is âSolarOSâ. Thatâs not a real OS name, but it looks a
lot like a mixture of *SunOS* and *Solaris*,
two names for the range of proprietary Unixes from Sun
Microsystems. I speculate that the very slight change of
name might have been deliberate, to avoid a trademark
quibble from Sun?

The appearance of `sun4m` later in
the `uname` output supports this theory. And
the overall format of the `uname` string is
pretty close to real Solaris examples I found on web pages
(alas, I donât have access to an actual Solaris machine to
check with). I found this, for example, on one web page:

```
# uname -a
SunOS storage1 5.10 Generic_125101-09 i86pc i386 i86pc
```

That `Generic_125101-09` is a pretty close
match to the `Generic_50203-02` in the film;
Iâd guess itâs something like the kernel version number.
The rest is fairly close too (although the host name
field `storage1` in the real output seems to
have no analogue in the film version). So it looks as if
this is *supposed* to be a depiction of a
(prudently renamed) Solaris.

However, the shell windows on the left make this look
like a superficial imitation! The top left shell window is
showing the output of `top` in exactly the
Linux style, and not only that, the list of process names
down the right-hand column is characteristically Linuxish.
Even though we can only see the first four letters of each
process, we can see things that look suspiciously
like `kthreadd`, `scsi_eh_something`, `migration`, `ksoftirqd`,
and `watchdogd`. All of those are process names
internal to the Linux kernel. Meanwhile, the bottom left
window is showing what looks like the output
of `iostat`, and again, it looks much more like
the Linux style of `iostat` than the Solaris
style.

So I think this is *supposed* to be a Solaris
machine, within the story â but the actor playing the part
is a Linux machine, and the costume and makeup department
missed a few bits.

Also, I think the appearance
of *both* `sun4m` and `i386`
in the `uname` output is another goof. Solaris
does run on x86 hardware, but `sun4m` is a
class of SPARC-based hardware. The real
Solaris `uname` output I show above prints the
identifier `i86pc` in the âplatform nameâ slot
where the film had `sun4m`.

Another hint of Linux is the `cat
/proc/meminfo` in the shell history on the right. As
far as I can tell from Solaris man pages on the web,
Solaris does *have* a `/proc` special
filesystem, but itâs not exactly like Linuxâs, and in
particular, doesnât have `meminfo` or anything
like it. (In fact, from the man pages I found,
the *only* things that live in
Solaris `/proc` are numbered directories
corresponding to running processes, and
the `self` symlink.)


The âconfigureâ command in the shell history

When I paused the DVD while watching the film, I
immediately noticed that there were three
commands `make`, `make install`, and
(after one intervening command) `./configure`.
âHang on,â I thought, âthose are in the wrong order!
Everyone knows that `./configure` comes
first, *before* `make`.â

But I was wrong! I hadnât looked closely enough, and Iâm
glad that this yearâs exercise made me spot my hasty
misjudgment.

The sequence
â`./configure`, `make`, `make
install`â is correct *if* the configure
script was generated by Autoconf, because if so, then its
job is to create the `Makefile` which the
subsequent `make` command will read. But in
this case, itâs clear that thatâs not what this script is
doing. Itâs being run with the arguments `-o
test.cfg`. Autoconf-generated configure scripts
donât have a `-o` option at all â so this isnât
an Autoconf-generated script. Itâs some completely
different thing, which shares a name with Autoconfâs
output by pure coincidence.

In fact, it looks to me as if *this* configure
script is part of the âlaser controllerâ software package
that Flynn was working with. Itâs plausible for a software
package that requires a complicated configuration file to
provide a script that generates one automatically, perhaps
intended as a starting point for user editing. Here, we
see Flynn running such a script to generate a starting
file `test.cfg`, and indeed immediately editing
it with `vi` to adjust whatever parts of it the
automatic configurer got wrong.

On the other hand, itâs not clear *why* Flynn did
this, because I highly doubt that the âliveâ run of the
laser controller at the end of the shell history was using
that configuration file. Itâs in the source code
directory, and Flynn called it `test.cfg`,
which doesnât sound like a file name or path that the real
software would read by default. After editing it, he
didnât copy it to any more official location (like
maybe `/opt/LLL/etc`?), and he didnât run the
final laser command with any option pointing at it by
pathname.

I think thatâs an error: surely, if Flynn went to the
trouble of making and editing a shiny new config file, he
should have finished up by telling the program to actually
use it. On the other hand, maybe this isnât an error on the
part of the *filmmakers*; maybe theyâre
intentionally depicting a shell history in which Flynn was
a bit distracted, or rushed, and didnât quite do everything
right! *Real* usersâ shell histories are full of
errors, after all.


Killing some processes to free up memory

Apparently the laser control software needs a lot of free
memory, because in commands 496â500, it looks as if Flynn
is freeing some up. First he checks how much free memory
there is using `cat /proc/meminfo` (although
see above for another note about that command); apparently
he didnât like what he saw, because the next thing he does
is to run `ps` to list the processes, and then
issue a couple of `kill` commands. Presumably
he got those pids out of the `ps` listing, and
presumably they corresponded to processes he thought were
likely to be memory hogs. Finally, he
runs `ps` *again*, to check the
processes he killed are really gone.

I think if Iâd been in his position, my final command
would have been another `cat /proc/meminfo`,
instead of (or maybe as well as) another `ps`.
The ultimate aim of this activity isnât to kill processes;
itâs to free up memory. If the laser program needs memory,
make sure the memory *really has* been freed up
before you run it!

But, as in a previous section, I think this can
reasonably be imagined as an in-universe mistake â a piece
of carelessness on *Flynnâs* part, faithfully
depicted by the filmmakers, and not an error on the part
of the filmmakers themselves. Heâs certainly nervous, and
quite possibly rushed, or distracted, or excited.


Double safety-catch on the laser-control software

Before he runs the laser program, Flynn
runs `touch` on a
file `/opt/LLL/run/ok`. The nominal purpose
of `touch` is to update a fileâs timestamp, but
if you run it on a file that doesnât exist already, a side
effect is to create that file. Presumably, this
file `/opt/LLL/run/ok` *didnât* exist
already, and Flynnâs purpose here is to create it. Also
presumably, heâs creating it because the laser control
software will refuse to actually control the laser if that
file doesnât exist. Itâs a safety catch, to make it less
likely that the laser is activated by accident.

In addition to this safety catch, thereâs a second one:
when Flynn runs the laser controller in his final command,
he *also* has to give the option `-ok
1`. This laser program demands *two*
different ways of saying âyes, I really mean itâ before it
will do anything.

Both of these safety-catch techniques are seen in real
Unix software. Git, in particular, uses both, in different
parts of its sprawling feature
set. `git-daemon` wonât serve a Git repository
over HTTP unless thereâs a
file `git-daemon-export-ok` in the repository
directory; `git-clean`, which deletes files,
wonât delete them for real unless you give it
the `-f` option on the command line.

Even with both of these safety catches, I donât know if
this laser software would meet the requirements of serious
safety standards such as ISO 26262. You can certainly see
things that might still manage to go wrong. Once youâve
used a command-line âyes I mean itâ option, itâs in your
shell history (as we see here!), so that recalling and
re-running the same command doesnât need repeated
confirmation. And once youâve made that file in the
programâs `run` directory, it stays there.

(Or does it? You might imagine that the laser
software *deletes* `/opt/LLL/run/ok`, as
a side effect of actually activating the laser. Then
you *would* need at least one repeated confirmation
â youâd have to re-create the `ok` file every
time you used the laser. But in fact the next thing Sam
does, after this shot, is to re-run the final command
â`LLLSDLaserControl -ok 1`â to see what it does
â and it turns out that it *does* still activate
the laser, without him having had to recreate
the `ok` file.)

But then, we shouldnât expect this software to be safe by
Serious Business standards. Itâs not clear whether Flynn
wrote it himself or got someone else to help, but he did
all of this in secret, so itâs definitely âone or two
people coding in a basementâ style software. Nobody is
insisting that it be certified to industry-standard levels
of safety. Flynn is only trying to satisfy
his *own* standards of caution, which donât look
all that cautious.


Last will and testament

Before firing the laser, Flynn edits a file
called `~/last_will_and_testament.txt`. Even if
you knew nothing about the film other than this
screenshot, that would suggest that whatever heâs about to
do with the laser is dangerous to him personally.

In fact (and this is where knowledge of the rest of the
film comes in) heâs going to fire the laser *at
himself*, disappearing his physical body completely
and digitising it into a piece of sentient computer
software, in the same way that it was done to him in the
original Tron. This time heâs doing it of his
own free will, instead of the hostile Master Control
Program doing it to him nonconsensually, so he has time to
prepare. Probably thereâs a risk that the digitisation
fails, leaving him simply dead; and *definitely*
thereâs a risk that he might successfully enter the
software world but find it hard to get out again. (It was
hard to get out in the first film, after all.) Either way,
heâs prudently putting his IRL affairs in order.

But Iâm not sure heâs thinking all that clearly. Surely a
will needs to be signed, witnessed, and
left *somewhere* that people can actually find it
after your death? I certainly wouldnât want to entrust my
own affairs to the offchance that someone going through my
computer after my death might find a file called âwillâ in
my home directory. If nothing else, wouldnât they need my
will to get probate in order to *search* my home
directory in the first place?

(Also, this isnât even `flynn`âs home
directory; itâs `root`âs home directory, and by
the analysis in a previous section, it seems likely that
thatâs `/`. Not the most obvious place to look
for a will, even *after* youâve got access to the
deceasedâs machine.)

On the other hand, Sam is quite likely Flynnâs executor,
and as we see here, he *has* found the will. Even
so, good luck persuading anyone that itâs valid without
signature or witnesses!

(On the *other* other hand, he only found it by
using the `backdoor` account, and â again by
analysis in a previous section â itâs possible that Flynn
didnât know Sam could do that. So it doesnât seem too
plausible that that was the method by which
Flynn *intended* Sam to find his will.)

But â yet again â all of this could quite plausibly be
legitimate in-universe mistakes by Flynn himself, and need
not be an error by the filmmakers. I expect if I were
about to perform a life-threatening and untested procedure
on myself and not even tell anyone in advance, I wouldnât
be thinking all that clearly either!


Text rendering in the terminal windows

Everything up to here has been focusing on *what*
the text says. But thereâs one last oddity: *how*
it says it.

In a typical terminal window, text is in a fixed-width
font. But in the main terminal window in our screenshot
here, the text is in a variable-pitch font. You can see
that most clearly in the lines âLogin incorrectâ followed
by âlogin: backdoorâ. In a fixed-pitch font, the âoginâ of
âloginâ would line up vertically between the two lines.
But here, theyâre offset from each other, because the
capital and lowercase L are different widths:

![](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/alignment.webp)

Also, the text has been word-wrapped, which isnât usual.
In normal terminals, if a simple command-line program
writes a line of text straight to `stdout`
which exceeds the terminal width, the terminal will either
(occasionally) overprint all the excess characters on top
of each other in the right margin, or (more usually) wrap
to the next line at *exactly* the right margin,
without concern for word boundaries â a long word will be
split across lines wherever it meets the margin, without
even the dignity of a hyphen.

`uname -a` normally produces all its output on
a single line, so the â`Unknown.Unknown`â was
probably meant to be on the same line as the rest of it.
(Indeed, we can see another copy of that same text in the
bottom left terminal window, and there it *is* all
on one line, since that window is wider.) But that final
word has been moved to the next line *as a whole*,
even though thereâs plenty of space left before the right
margin.

![](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/wrapping.webp)

I have *no* idea whatâs going on here. What
behaves enough like a Unix terminal program that you can
run a shell session in it, but uses a proportional font
and automatically word-wraps? I suppose itâs possible that
Emacs `M-x shell` could be reconfigured into
that mode via a lot of work with custom face
configurations and `visual-line-mode` â but
thereâs no emacs status bar here, so it canât
be *exactly* that.

Of course, this is an imitation of a Unix system in a
film. So thereâs no requirement for it to behave exactly
like real Unix systems. But on the other hand, in a
previous section I spotted at least one clue in this
screenshot that suggests there *might* have been a
real Unix system involved here, used as the easiest way to
make all these commands deliver the right responses. So
maybe there really is a weird proportional-width
word-wrapping terminal program that Iâve never
encountered?

But if so â¦ itâs not being used *consistently*
within this screenshot. The top *left* terminal
window, showing the output of `top`, is in what
looks like a very similar font, but it *is*
fixed-pitch. You can see that the four visible characters
of each process name line up in nice columns, whether or
not theyâre narrow letters like `i`
or `l` â in this window, those letters have
plenty of blank space around them, unlike in the main
window. Compare the âinâ of `init` here with
the âinâ of âloginâ above:

![](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/top.webp)

So the three windows arenât all behaving the same
way as each other!

Summary
-------

There was a lot to see in this transcript! And quite a lot of
it had good explanations, within the filmâs universe. There are
a few things Iâd class as outright errors by the filmmakers, but
a lot more things that make perfect sense. And, somewhere in
between, some things that *could* be filmmaker mistakes,
but are also quite plausible as errors on Flynnâs part.

Apart from a lot of specific knowledge about Unix, the other
main thing I think this exercise was good for is: reading a
thing in detail, and avoiding the temptation to skip over things
that *look plausible* but youâre not sure theyâre right.
In this screenshot, there are definitely some things
that *arenât* right â but also, if you examine the whole
thing in the level of detail that catches those, you find a lot
of other things that *are* right, but werenât obvious.

Iâll finish up by summarising which things I think are which.
Of course, this section contains spoilers for *all* of
the above.

Whatâs an error and whatâs not

**Mistakes by the filmmakers**: I stand by my
original judgment, from the first time I saw this scene,
that `bin/history` is *just wrong*. Iâm
suspicious of `/bin/login` working in this
situation. Iâm very dubious about `uname`
reporting both `sun4m` and `i386` on
the same machine. And finally, it seems clear that
theyâve *tried* to make the OS look like Solaris (or
its fictional renaming SolarOS), because the `uname
-a` output is not like any real Unix and must have
been deliberately made up; but in that case, having so many
Linuxisms all over the rest of the screen seems like an
avoidable mistake.

**Mistakes by Flynn** (plausibly): I think he
should have re-checked `/proc/meminfo` after
killing processes (even though that file doesnât really
exist on Solaris). He surely should have done something
more sensible with his last will and testament. And I think
he accidentally ran the laser control software with its
default configuration and not the one heâd carefully created
just beforehand (but, luckily, apparently that didnât cause
a problem). But Iâm prepared to accept all of those as
consequences of a highly distracted state of mind!

**No idea at all**: I donât have any good
answer to the inconsistently proportional font in the
terminal windows. I canât think of a way (or a reason)
someone might have done that on purpose, *or* a way
it might have happened by accident. It baffles me.

**Perfectly sensible**: pretty much everything
else! It makes sense that Sam had that back door account but
only tried it once real `root` didnât let him in.
Some serious thought was put into the shell history,
including little details like needing to free up some
memory, the âwrite a configuration file and then edit itâ
operation, and the dangerous laser software having a double
safety catch.

None of those fine details is *necessary* to the
thing thatâs happening in the plot. All thatâs really needed
is that Sam found his dad had run a mysterious command with
âlaserâ in the name, and ran it again to see what would
happen. All of this is bonus extra content just for people
like me who pause to examine it in detail. And mostly,
pretty well done!

**One last thing**: if the laser command run
as root causes the laser behind the computer chair to fire
and digitise the person sitting in it, how come the
computer *wasnât* left logged in
as `root`, with the shell history already visible
on the screen, and no need to run `history` to
find it out? How come Sam only found a clear terminal window
logged in as a mere unprivileged user account? Of course
this *could* be just another mistake â¦ but perhaps
the answer is that that window doesnât contain
the *same* terminal session that Flynn ran the real
command in. Perhaps thereâs a cunning system that times out
unattended root logins after a while?

Finally: thereâs a lot of analysis here, but Iâm not
overconfident enough to imagine that Iâve *definitely*
got all of it. Maybe someone else will be able to find something
we still missed!

Addendum: thoughts from the Internet
------------------------------------

Discussion after I published this article did indeed suggest a
few more points that my colleague and I didnât think of.

Just so nobody feels a need to tell me the *same*
extra thoughts again, Iâll list them here, under another cut.
But I havenât edited any of the text *above* this
appendix: mistakes in my own analysis are still there, and I
wonât try to pretend I never made them.

Things other people pointed out to me

**Saving and printing
within `vi`**. It didnât occur to us that
when you edit a file using `vi`, you can issue
commands *within* the editor that save it to a
different pathname, or pipe it to an external command.
Operations within the editor like that wouldnât show up in
the shell history, but it doesnât mean they didnât happen.
So maybe Flynn *was* using his newly created laser
configuration file after all â maybe he ran something like
`:w /opt/LLL/etc/laser.cfg`
within `vi` to save it to the right location.
Similarly, maybe he did do the right thing with his will â
he could have piped it straight to a printing tool
like `lpr` from within the editor, and then done
something sensible with the paper copy.

**`login` *can* be setuid**.
My own Linux prejudice was showing. `/bin/login`
isnât setuid on Linux, but it is on other Unixes, including
FreeBSD and NetBSD.
A [followup
blog post](https://utcc.utoronto.ca/~cks/space/blog/unix/SuAsLoginReplacement) by Chris Siebenmann goes into the history of
this, in particular that in older Unix, youâd choose
between `login` and `su` based on
whether you wanted a completely fresh shell environment or
wanted the root process to inherit the state of your current
one.

**An article by the Tron: Legacy visual
effects artist Josh Nimoy**
exists! [Link
to article](https://jtnimoy.cc/item.php%3Fhandle=14881671-tron-legacy.html). Alas, it doesnât directly
discuss *this* scene, but itâs still interesting. In
particular, it mentions the use of emacs and
its `eshell` mode to create recordings of shell
sessions.

**Stop-motion replay?** That article by Josh
Nimoy mentions *recording* shell sessions for use in
the scenes being filmed. I received a suggestion (from
someone who had apparently read another article I havenât
seen) that those recordings might have been manually
replayed one frame at a time by someone else â the digital
analogue of stop-motion animation, where you carefully
position everything for the next frame and then take the
picture. So maybe the text in this scene *does* come
from a real shell session (making my speculation
about `bin/history` still reasonable), but it
might have been recorded in advance, and replayed by pasting
it a bit at a time into some application more like a text
editor. That would explain the word-wrapping and
proportional font. (And the window showing `top`
is different on purpose, because `top`âs output
is in columns and they needed it to line up.)

However, as another responder points out, the menu bar
along the top of the shell window looks like one from a
terminal application, not a text editor. In fact, itâs
exactly the same sequence of menu names (âFileâ, âEditâ,
âViewâ, âTerminalâ, âTabsâ, âHelpâ) seen
in `xfce4-terminal`.
But `xfce4-terminal` is a perfectly normal
terminal application which doesnât let you use a
proportional font. So perhaps the recording is being
replayed in a *slightly customised* text editor with
the menu bar tweaked for realism!

**LLL easter egg**. Parts of the
original Tron were shot in Lawrence Livermore
Laboratory. In-story, it was representing a corporate
facility owned by the fictional ENCOM corporation, but
really it was LLL. The letters `LLL` in the name
of the laser control software are surely a shoutout to
that.

[1.](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/#footnote-fair) Iâm
sitting in the UK as I write this. Under UK law, I believe this
should constitute fair dealing: the purpose is quotation for
criticism and review, and this single screen capture is in no
way an alternative to paying to see the original film. The film
comes from the USA, and under USA law I think it similarly
constitutes fair use: itâs for non-profit educational purposes,
the amount of the full work used is extremely small, and the
effect on the value of the full work negligible.