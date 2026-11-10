---
title: "Biology is a Burrito: A text- and visual-based journey through a living cell"
url: https://burrito.bio/essays/biology-is-a-burrito
clipped: 2026-06-17 01:10:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Biology is a Burrito: A text- and visual-based journey through a living cell](https://burrito.bio/essays/biology-is-a-burrito)

## Digest Summary
E. coli’s genome, if stretched, is ~1,000 × longer than the micrometer‑scale cell that contains it; a billion descendants could span the Earth‑Moon distance. The cell’s interior is ~70 % water, 30 % macromolecules (proteins, RNA, lipids), with DNA comprising ~1 % of mass, yet all fit within a volume ≈ 10⁻¹⁵ L. E. coli carries ~4,400 genes; ~25 % are actively transcribed. RNA polymerase moves ~40 bases s⁻¹, making an RNA in <30 s with ≈1 error per 10⁵ bases. Ribosomes translate an average protein in ~24 s; a cell harbors 3–4 million proteins. Small molecules diffuse ≈1 cm s⁻¹, whereas proteins travel only a few micrometers per second, setting an upper size limit for cells. Even at 0.5 mM substrate (1 per 10⁵ water molecules), enzymes encounter ~5 × 10⁵ substrate collisions s⁻¹. These quantitative facts illustrate that cellular biochemistry operates in an extremely crowded, dynamic environment, and that mathematical analysis is essential for understanding biological rates, efficiencies, and constraints.

## Discussion Summary
The comments convey strong admiration for the complexity and precision of cellular processes, especially DNA transcription, describing the depiction as beautiful and reminiscent of high‑fidelity 3D animations. Readers express enthusiasm for integrating quantitative, mathematical thinking into biology education and appreciate the detailed, awe‑inspiring nature of the work. Several commenters suggest that an animated video would communicate the material more effectively than text alone, indicating a preference for visual formats to capture the subject’s passion and intricacy.

---

## Full Article

A bacterium's genome, pulled into a straight thread, is nearly 1,000 times longer than
the cell from which it came. If you placed one *E. coli* into a gallon-sized jug with some nutrients
and waited a few hours, the genomes of its descendants, placed end-to-end, would
[reach
to the moon and back](https://twitter.com/NikoMcCarty/status/1630213701272842244)...several times.[1](https://burrito.bio/essays/biology-is-a-burrito#fn1)

One rarely pauses to ponder how so much DNA — let alone sugars, proteins, lipids, and
other molecules — can fit inside such a small vessel. A typical *E. coli* cell,
after all, measures about one micrometer across. Its entire volume is 100 times smaller
than that of a red blood cell, and about 100 million times smaller than a grain of sand.

The truth is that biochemistry textbooks often depict cells as spacious places, where
molecules float in secluded harmony. "But a cell looks more like a burrito," says
[Michael
Elowitz](https://www.bbe.caltech.edu/people/michael-b-elowitz), a biologist at Caltech. All the biochemicals are pushed together, bumping
into each other.

It's a wonder that anything gets done inside of living cells at all,
for they are
[fast
and crowded places](https://www.righto.com/2011/07/cells-are-very-fast-and-crowded-places.html). A painting by
[David
Goodsell](https://en.wikipedia.org/wiki/David_Goodsell), a biologist in San Diego who moonlights as an illustrator, enamors because
it conveys this denseness in visual form.

![Watercolor cross-section of an E. coli cell by David Goodsell, showing the densely packed interior with the lipid membrane in green, proteins in purple and blue, and DNA in yellow-orange.](https://burrito.bio/images/goodsell-ecoli.jpg)


A watercolor cross-section of *E. coli*, by David Goodsell. The green band is the cell membrane; purple and blue shapes are proteins; the yellow tangle is DNA.

Such paintings are beautiful, but ultimately simplistic. They are snapshots of cells at
a single moment in time. Paintings can *hint* at complexity, but don't convey the
intense dynamics of a living cell. All of our scientific methods to study life, similarly,
demand that cells be killed or frozen before a microscopic image is taken. Therefore,
mathematics and words are our best tools to understand the active chaos
of living cells.

For many years, I had an intense aversion to mathematics. Biology was my refuge because
it was simple: Read the textbook, memorize the facts, and ace the exam. (The only reason
I majored in biochemistry as a college student was because it didn't have a multivariable
calculus requirement.) But then, I started a Ph.D. in Bioengineering at Caltech and
landed in
[Rob
Phillips' lab](https://www.rpgroup.caltech.edu/personal_pages/rob/index.html). Rob is a master of physical biology; a person who
has spent decades building a numerical intuition for biology.

And suddenly, I was thrown into the deep end of biophysics. I took courses like
*Physical Biology of the Cell* and wrote out statistical mechanics equations on
big whiteboards. I felt like a real biologist for the first time, because suddenly I
could think of a question — like "How many ribosomes does a typical *E. coli*
cell have?" — and figure it out from scratch, using little more than scribbled equations.
It was a joy, at last, to finally grasp the "numbers of
biology."[2](https://burrito.bio/essays/biology-is-a-burrito#fn2)

Without mathematics, biology is naked; one can only comprehend it at arm's length. But
with numbers, living cells come alive. Mathematics enables one to see a Goodsell painting
with fresh eyes.

Just consider the Central Dogma. Students learn the basics through words: DNA is
transcribed to RNA, which is translated into proteins. But what does
this really mean? How fast does DNA become RNA, or RNA a protein? How many proteins are
in a cell, and how *fast* do they fold and move? Doing these calculations reveals
both the beauty and weirdness of life at the smallest scales. It lends
a deeper appreciation to biology. And all we need to do it is a pencil and paper.

But first, some background. A microbe's guts are a veritable Times Square, crowded with
sugars, proteins, and water molecules that ricochet and smash into each other billions of
times each second. Space is limited. A bacterium's insides are
[70
percent water](https://bionumbers.hms.harvard.edu/bionumber.aspx?s=n&v=5&id=101851) by mass, and the other
[30
percent](http://book.bionumbers.org/what-is-the-macromolecular-composition-of-the-cell/) is dominated by proteins first, followed by RNA and lipids. DNA accounts for
just one percent of a cell's mass. And all of this *stuff* fits inside a volume
that is one-quadrillionth the size of a liter. (About 500 billion microbes fit inside of
an aspirin tablet!)

Now let's think about the transcription of DNA into RNA. A typical *E. coli* has
[4,400
genes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC56896/) in total. At any given moment, about
[25
percent](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=111605&ver=1) of these genes are being copied into RNA by a large protein called RNA
polymerase. Each polymerase protein grabs onto the DNA and zips along its length at
breakneck speeds, converting about
[40
bases](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=108488&ver=3) of DNA into its corresponding RNA each second. If an RNA polymerase were scaled
up to the size of a human, it would move twice as fast as Usain Bolt's record-setting
pace in a 100-meter
dash.[3](https://burrito.bio/essays/biology-is-a-burrito#fn3)
The polymerase only makes about
[one
mistake](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=105212&ver=16) every 100,000 bases.

Fewer than 30 seconds pass from the time polymerase binds to the DNA to the time it
makes a full RNA. As soon as the RNA is finished, it is released by the protein and
diffuses, or floats, away. A small army of ribosomes quickly swoops in and grabs it.
The ribosomes read the letters in the RNA sequence — three at a time — and convert them
into amino acids in a growing
protein.

Ribosomes also move quickly; they make an average-sized protein from RNA in just
[24
seconds](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=100233&ver=8). A single ribosome could translate the first Harry Potter book in
two-and-a-half hours while making just three dozen typos along the
way.[4](https://burrito.bio/essays/biology-is-a-burrito#fn4)

When a ribosome finishes this task, its jaws unclench and the new protein is released.
At any given time, a typical bacterial cell has
[three
or four million](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=115702&ver=1) proteins floating around, each responsible for breaking down sugar,
copying DNA, sending signals to nearby cells, and much more. A living cell is an
autonomous factory, where machines build machines that build themselves.

At the small scales in which proteins exist, even a subtle difference between two
molecules can make a big difference. Diffusion is one example of this. Small molecules,
such as water or ions, diffuse quickly, migrating about one centimeter per second. (In
other words, these molecules travel the length of ten thousand bacterial cells in the
span of one second.) But large proteins move more slowly — only a few micrometers
(one-millionth of a meter) in the same second. A rule of thumb is that, for a molecule
to move twice as far, it takes four times as long. Molecules don't move in straight
lines, but jostle about in three dimensions. Diffusion is described in units of
length2/time, meaning it takes a protein 10 milliseconds
to move across a cell, but
[20
days](http://book.bionumbers.org/what-are-the-time-scales-for-diffusion-in-cells/) to travel one centimeter.

Diffusion sets an upper limit on a cell's
size.[5](https://burrito.bio/essays/biology-is-a-burrito#fn5)
If a cell is too small, not enough "stuff" fits inside and evolution is constrained.
If a cell is too large, nothing ever gets done because proteins cannot reach their
destinations. Life is a search for many little optima.

As proteins move through a cell, they are also bombarded by water, sugars, and other
proteins. Every protein collides with millions of molecules every second, and its
corresponding substrate — the molecule it means to find — is vanishingly rare. In
biology textbooks, one often reads sentences like, "A protein's substrate has a
concentration of 0.5 millimolar." All this means is that there's one substrate for
every 100,000 water molecules. And yet, even at this sparse dilution, the enzyme will
find, and collide with, about
[500,000
substrates](https://www.cell.com/fulltext/S0092-8674(00)80922-8) every
second![6](https://burrito.bio/essays/biology-is-a-burrito#fn6)

Cells are chaotic swarms of energy and fortuitous accidents. The Central Dogma sounds
simple in words, but is a miracle in reality. It's a wonder that cells get anything
done at all.

The first time I did these calculations, I felt an intense appreciation for biology.
And now, I want everyone else to feel the same. We ought to teach students of biology to think
as mathematicians: to carefully quantify biology, to think in absolute units, and to
develop a
[feeling
for the organism](https://us.macmillan.com/books/9780805074581/afeelingfortheorganism10thaniversaryedition).

Throughout this essay, I've depicted cells as dense blobs filled with lots of
*stuff*. This insinuates that, if one studied everything in a cell and
tallied all of its components, then perhaps we'd have a complete knowledge of biology.
But this isn't true.

Some proteins
["moonlight"](https://royalsocietypublishing.org/doi/10.1098/rstb.2016.0523)
in the cell. They carry out one function when their substrate is around, and do something
entirely different when it isn't. Many protein signaling pathways also play a specific
role in one type of cell, and something different in another. Biology is infinitely
weird, and if we ever plan to master it, we will need new scientific methods to measure
protein dynamics and interaction strengths.

When COVID came in 2020, I left my Ph.D. and moved to New York to study journalism. I
fell out of contact with Rob, but my appreciation for biological numbers remained. I
still enjoy jotting down calculations in the margins of books. And every day, I feel
grateful that I get to learn about biology, a field that is far stranger than anything
one could see while scuba diving or traveling to Mars. It is still difficult for me to
imagine the microscopic world when my mind and experiences are almost wholly confined to
the macroscopic world. But a pen, paper, and imagination seem to suffice.