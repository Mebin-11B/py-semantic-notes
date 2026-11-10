---
title: "Generative art over the years"
url: https://blog.veitheller.de/Generative_art_over_the_years.html
clipped: 2026-06-17 01:19:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Generative art over the years](https://blog.veitheller.de/Generative_art_over_the_years.html)

## Digest Summary
Since 2016 the author has created roughly 114 generative sketches in p5.js, documenting a progression from pure algorithmic exploration to a personal visual vocabulary. Early work centered on mathematical forms—e.g., a 30‑line phyllotaxis spiral using cos, sin, and sqrt—focused on parameter tweaking rather than aesthetics. Dissatisfaction with “clean” outputs led to a greyscale phase emphasizing texture: simulated brush strokes, particle‑based fur, and dense line layering produced material‑like surfaces. This evolved into heuristic material simulators (watercolor washes, dry brush, felt‑tip pen, cracked glaze) that capture characteristic visual traits without physical accuracy. Color theory remains underdeveloped; the author now builds intuition through repeated experimentation and observation. The accumulated techniques form a “vocabulary” that guides compositional decisions, shifting the primary question from “what can I do?” to “what do I want to say?” despite limited time, the practice continues as a low‑pressure, patient creative outlet.

## Discussion Summary
The discussion blends nostalgia for earlier, hands‑on generative‑art experimentation with a sense of displacement caused by AI’s growing capabilities, while simultaneously affirming the value of traditional algorithmic approaches. Contributors recall past tools such as Processing, p5.js, and shader coding, share resources and personal projects, and stress prioritizing visual character over precise physical simulation. Overall, the tone is reflective yet optimistic, emphasizing continued interest in non‑AI generative techniques and community collaboration despite concerns about AI superseding some tasks.

---

## Full Article

Iâve been making generative art on and off since 2016. It started as
a programming exercise and slowly turned into something more personal as
I discovered I can actually express myself visually with it and feel as
if Iâm producing art. I have about 114 sketches in [my p5js account](https://editor.p5js.org/hellerve/sketches) at
this point, and they document part of a journey that I want to try and
put into words.

The short version is: every algorithm I learn becomes a tool I can
reach for later, and over time those tools have accumulated into
something like a vocabulary. I learned about textures, layering, about
colors and positioning through experimentation and creating hundreds of
sketches over the years, in P5.js and other media. The longer version is
what follows.

The beginning: what
does this math look like?
---------------------------------------------

My earliest surviving sketch is a phyllotaxis spiral. If you donât
know what that is, itâs the pattern you see in sunflower heads and pine
cones: you place points along a spiral using the golden angle, and
something surprisingly natural and organic appears. The code is about 30
lines and mostly consists of `cos()`, `sin()`, and
`sqrt()`, decidedly inorganic.

![](https://blog.veitheller.de/assets/genart/phyllotaxis.png)

Fig. 1: An early phyllotaxis spiral, circa 2016.

I remember being genuinely amazed that such a simple formula could
produce something that felt real. And that was more or less the whole
creative process at the time: find an algorithm, tweak parameters until
it looks nice, save it, move on. Iâd learn about these algorithms from
other nerds on the web. The aesthetic decisions were all second to the
math. I didnât choose this shape or that texture, I chose a formula, and
whatever came out was what I got. I also didnât know how to introduce
variance.

Most of my early work looks like this. Mathematical structures
rendered in bright colors or white on a black background. Thereâs a
certain beauty to them, but they feel more like illustrations of
concepts than things I made. I was a programmer first, an artist second
if at all.

Learning to see texture
-----------------------

At some pointâI couldnât tell you exactly whenâI started getting
bored with the clean mathematical look, and I felt guilty for just
stealing formulas other people were using with some variation. I wanted
things that felt more physical, more like they had been made by a hand
rather than a machine.

This is when I started paying attention to texture. I began
simulating brush strokes, experimenting with particle systems to create
the impression of fur or hair, varying line weight and opacity to mimic
the way ink bleeds into paper. Flow fields became a frequent starting
point, not because the math was new to me, but because they created
versatile, beautiful textures.

![](https://blog.veitheller.de/assets/genart/flow.png)

Fig. 2: A flow field with simulated brush strokes. Greyscale, as was my
habit.

This was also my greyscale period, if Iâm being generous enough to
call it that. I avoided color almost entirely, partly as an aesthetic
choice and partly because I simply didnât know how to use it well.
Greyscale was safe, it let me focus on form and texture without having
to make decisions I wasnât equipped to make. In hindsight, this was a
useful constraint. It forced me to get good at the things I could
control, but I also put off learning for way too long.

What lines can do
-----------------

Before I got to materials proper, there was an intermediate step that
I think matters. I started exploring what you could achieve with just
lines. I wasnât simulating anything in particular, just layering and
density and direction. And somehow texture just appeared. It was
magical, and I still get genuine goosebumps when I think about it.

I tried to understand [what other people
were doing](https://www.tylerxhobbs.com/works/slow-lessons), and why it was so much more appealing than my work.

![](https://blog.veitheller.de/assets/genart/frame.png)

Fig. 3: Just lines, as I tried to understand Tyler Hobbsâ work from just
above.

This is where I first noticed that accumulation creates its own
effects. Enough lines drawn close together stop looking like lines and
start looking like a surface. The composition above isnât trying to be
fabric or paper, but it can look that way. The realization that raw
geometric primitives, given enough density and intention, can evoke
physical materials is what eventually pushed me toward explicit material
simulation. I realized that I could almost make pencil sketches.

Simulating materials
--------------------

From lines to materials wasnât a big leap, but it felt like one
conceptually. Instead of asking âwhat does this algorithm look like?â, I
started asking âcan I make this look like watercolor?â or âwhat would a
felt-tip pen do hereâ?

These are very different questions. The first one starts with math
and arrives at an image. The second starts with an image, a feeling,
really, a memory of what watercolor looks like when it pools and dries,
and works backward to the math that might produce it. I wasnât alone [in
this discovery](https://www.tylerxhobbs.com/words/a-guide-to-simulating-watercolor-paint-with-generative-art), as I later learned.

I now have a small library of simulated materials: watercolor washes,
dry brush strokes, felt-tip pens, cracked glaze, pencil fills. None of
them are physically accurate. Iâm not simulating fluid dynamics or
anything like that, I donât need to. Theyâre impressions, heuristics
that capture enough of the character of a material to be convincing and
evoke an emotion.

Building them taught me things. The watercolor algorithm taught me
about layering and transparency, and how colors blend gracefully. The
brush stroke algorithm taught me about pressure, direction, and
variance. The cracked glaze taught me that imperfection adds a layer of
believability and its own structure.

Starting to see color
---------------------

Color remains my weakest area. I have no formal knowledge of color
theory, and as I admitted above, for a long time I avoided the problem
by working almost exclusively in greyscale or with very limited
palettes.

Iâm getting better, slowly. Itâs a matter of developing intuition
through exposure and experimentation. Looking at art I admire, trying to
understand why certain combinations work, and then testing that
understanding in my own sketches over and over. I have no framework for
it, just a growing sense of what feels right. Iâm in a special state of
mind when I create art of any kind, and itâs distinctly different from
engineering (even my typing hands feel different!).

![](https://blog.veitheller.de/assets/genart/collage.webp)

Fig. 4: A more recent piece. Color, simulated material textures, and
compositional intent.

Comparing something like this to the phyllotaxis spiral from 2016
makes the journey clear in a way thatâs hard to see from the inside. I
look at the two pieces and see myself transforming. The early work is
playing with an algorithm. The recent piece is about composition of
shapes, colors, textures, and materials that work together. The
algorithm is still there, but itâs in service of something. Some of the
algorithms are cool, some are terrible, but theyâre not the primary
value.

The vocabulary
--------------

What Iâve come to think of as my âvocabularyâ is really just the slow
accumulation of all these techniques. Each algorithm I learn, each
material I simulate, each failed experiment with color becomes something
I can draw on later. Not every sketch uses every tool, but knowing
theyâre available changes how I think about what to make next. And I
have noticed myself deliberately choosing between maximalism and
minimalism. I still make small pieces with very little going on, but now
itâs a choice.

In the beginning, the question was âwhat can I doâ Now itâs closer to
âwhat do I want to sayâ; not a dramatic transformation, but meaningful.
The tools fade away, and something like a personal aesthetic starts to
emerge. I couldnât describe it precisely if you asked me, but I can feel
it when a piece is working and when it isnât, and that feeling is more
reliable now than it used to be.

Fin
---

I donât make generative art as often as Iâd like. Life is busy in the
way that life is busy when you have a family and a career and a dozen
other things competing for your attention. But the practice persists,
even if itâs slow. A sketch here, an experiment there. Every couple of
years I make books of poems and artwork for my family (something I want
to write about it in the future as well), and that deadline is usually
enough to pull me back in.

I think the thing I value most about this practice is how patient it
is. Thereâs no pressure to ship and no deadline. Just me and a virtual
canvas and a hunger to explore a kind of personal aesthetic.