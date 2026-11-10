---
title: "Reports of code's death are greatly exaggerated"
url: https://stevekrouse.com/precision
clipped: 2026-06-17 01:28:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Abstraction
  - Software Architecture
  - Vibe Coding
  - Artificial General Intelligence
  - Programming Language Theory
  - Cognitive Load
related:
  - "[[Using AI to write better code more slowly]]"
  - "[[Chroma Context-1 Training a Self-Editing Search Agent]]"
  - "[[How to Code Claude Code in 200 Lines of Code]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Steve Krouse argues that code and precise abstractions are not dead, showing how AI-driven "vibe coding" leads to leaky abstractions at scale, and explaining that AGI will be used to design better formal abstractions rather than replace coding.
>
> **Key points:**
> - "Vibe coding" (using AI to convert English to code) creates an illusion of precision but leads to buggy, leaky abstractions when projects scale or handle high-complexity features.
> - Abstraction is a necessary tool to compress complexity to fit the human cognitive limit (7 ± 2 items), creating new semantic levels for absolute precision.
> - As AI tools approach AGI, developers will use them to build better libraries and solve hard architectural and abstraction problems, rather than just producing low-quality "slop."
> - The essay analogizes programming to writing, pointing out that natural language lacks the inherent precision of formal algebraic signs or structured code necessary for complex computation.
> - Prominent computing figures (Dijkstra, Hoare, Babbage) are cited to emphasize how formal notations and succinctness enable minds to master infinite complexity.
>
> **Concept links:** [[Abstraction]], [[Software Architecture]], [[Vibe Coding]], [[Artificial General Intelligence]], [[Programming Language Theory]], [[Cognitive Load]]
>
> **Suggested connections:**
> - [[Using AI to write better code more slowly]] — Explores a similar topic of how AI affects code quality and developer workflows.
> - [[Chroma Context-1 Training a Self-Editing Search Agent]] — Explores the practical design of AI agents dealing with code editing and reasoning.
> - [[How to Code Claude Code in 200 Lines of Code]] — A direct example of concrete code versus high-level agentic abstraction.
<!-- ai-summary:end -->

# [Reports of code's death are greatly exaggerated](https://stevekrouse.com/precision)

## Digest Summary
The essay argues that code is far from obsolete, emphasizing that precise specifications remain essential despite the allure of “vibe coding” aided by AI. It notes that natural‑language prompts can quickly generate runnable code, but such abstractions mask underlying complexity that emerges at scale, especially in features like live collaborative editors, which historically prove difficult to implement correctly. The author highlights abstraction as the key technique for managing limited human cognitive capacity (≈7 simultaneous items), citing Dijkstra’s view that abstractions create new, precisely defined semantic levels. Examples include refined Slack notification flow diagrams and functional programming concepts such as functional reactive programming. The piece predicts that as AI advances toward AGI, it will be leveraged to create better abstractions and solve hard engineering problems rather than replace coding entirely. Personal anecdotes about using Opus 4.6 to resolve React Router issues and criticism of claims that coding is dead reinforce the central claim: AI will augment, not eliminate, the craft of writing precise, maintainable software.

## Discussion Summary
Comments reflect a mixed view of AI‑generated code. Many acknowledge AI’s ability to handle routine tasks, produce prototypes, write tests and accelerate development, but stress that it remains centered on existing patterns and lacks true critical thinking or innovation. Concerns recur about overreliance, loss of architectural insight, “comprehension debt,” and vendor lock‑in, while others argue that code will persist as a precise medium even as higher‑level specifications grow. Overall the consensus is that AI will augment programmers and shift abstraction levels, not replace human expertise.

---

## Full Article

March, 21 2026

[A sufficiently detailed spec is code](https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code)
begins with this lovely comic:

![image.png](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/f7e9e621-0fad-4c3a-a65b-d16832c02b00/public)

There is a profound tension here: english specifications *intuitively feel*
precise until you learn better from bitter experience. (It's all in that facial
expression of the last frame.)

> "Everything is vague to a degree you do not realize till you have tried to
> make it precise."
>
> – Bertrand Russel

Programming, like writing, is an activity, where one iteratively sharpens what
they're doing as they do it. (You wouldn't believe how many drafts I've written
of this essay.)

AI helps you with this, because it – increasingly instantly and well – turns
English into running code. You can then react to it – "move the button there;
make it bluer" – to get incrementally more precise about what you want.

This is why "vibe coding" is such a perfect phraseology: you stay operating at
the level of your English-level vibes while reacting to the AI-created artifacts
that help you sharpen your thinking.

But, vibe coding gives the illusion that your vibes are precise abstractions.
They will feel this way right up until they
[leak](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/),
which will happen when you add enough features or get enough scale. Unexpected
behaviors (bugs) that
[emerge from lower levels of abstraction](https://worrydream.com/LadderOfAbstraction/)
that you don't understand will sneak up on you and wreck your whole day.

This was Dan Shipper's experience when his
[vibe-coded text-editor app went viral, and then went down](https://every.to/chain-of-thought/when-your-vibe-coded-app-goes-viral-and-then-goes-down).
As it turns out, "live collaboration is just insanely hard."

"Live collaboration" *intuitively feels* like a perfectly precise specification.
We've all used Google Docs, Notion, etc so it *feels* precisely spec'd. It's
incredibly hard a priori to see what this is not the case.

The only reason that I personally know otherwise is that I tried to add a
collaborative text editor to a product I was working on 10 years ago, and it was
an unexpected nightmare of complexity.

What was hard about it? I don't remember! That's part of the problem! Complexity
can be incredibly boring, unpleasant to think about, and hard to remember all
the details and edge cases. For example, the classic flowchart of how Slack
decides when to send you a notification:

![image.png](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/4370b0ce-5657-4edc-9077-25751bbdd500/public)

But, this isn't the end of the story either. We are blessed with an extremely
powerful tool to master complexity.

There is a fundamental limit in the human brain. We can only think of 7 (plus or
minus 2) things at a time. So the **only way** to think about more than 7 things
is to *compress* multiple things into a single thing. Happily, we can do this
recursively, indefinitely, which is why humans can master unlimited complexity.
That compression step is called *abstraction*.

> The purpose of abstraction is not to be vague, but to create a new semantic
> level in which one can be absolutely precise.
>
> — Edsger Dijkstra

For example, Sophie Alpert used clever abstraction to
[refactor the Slack diagram to this much simpler one](https://sophiebits.com/2024/10/30/everyone-is-wrong-about-that-slack-flowchart):

This is the best part of programming: coming up with increasingly good
abstractions to help us master complexities. My favorite examples of this are
functional programming concepts, like functional reactive programming, which
[I wrote a wonderful essay on](https://futureofcoding.github.io/futureofcoding.org/essays/dctp).

So yes, collaborative text editors are fundamentally complex, but that just
means that we're continually in search of better abstractions to help us master
complexities, like ReactJS or TailwindCSS did in their respective domains.

But let's play this out 1, 2, 5, 10, 100 years. AI is getting
better/faster/cheaper at incredible rates, but regardless of *when*, unless you
believe in magic, it's only a matter of time until we reach the point at which
machine intelligence is indistinguishable from human intelligence. We call that
point AGI.

It may seem like an AGI world is a vibe world. If anyone can afford 100
Karpathy-level geniuses for $1000 / month, why ever trouble yourself with any
troublesome details? Just have your army of Karpathys handle them for you.

This is such a joke to me. This is *clearly* only something you'd think in the
abstract, before this technology arrived.

If you told me that I had access to that level of intelligence, there is zero
part of me that is going to use it to ship *more* slop. Are you freaking
kidding?? Of course not.

I think we're confused because we (incorrectly) think that code is only for the
software it produces. It's only partly about that. The code itself is also a
centrally important artifact. When done right, it's poetry. And I'm not just
saying this because I have Stockholmn Syndrome or a vested interest in it – like
a horse jockey might in the face of cars being invented.

I think this is a lot clearer if you make an analogy to writing. Isn't it
fucking telling that nobody is talking about "vibe writing"?

We're not confused with writing because there's nothing mystical about
syntactically correct sentences in the same way there is about running code.
Nobody is out there claiming that ChatGPT is putting the great novelists or
journalists out of jobs. We all know that's nonsense.

Until we get AGI. Then, by definition, machines will write amazing non-slop and
it'll be glorious.

The same exact situation is true for coding. AI produces (increasingly less)
shitty code. We all know this. We all work around this limitation. We use AI
in spite of the bad code.

As Simon Willison says,
[AI should help us produce better code](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/).
And when we have AGI this will be easy.

When we have AGI, the *very first* things we will use it on will be our hardest
abstraction problems. We will use it to help us make better abstractions so that
we can better understand and master complexity.

You might think the need for good code goes away as AIs get smarter, but that's
like using ChatGPT to write more slop. When we get AGI, we will use them to make
better abstractions, better collaborative text editor libraries, etc.

For example, my favorite success story with Opus 4.6 was that it helped
me with my dream full-stack react framework for Val Town. It one-shot solved
[my list of unsolved problems](https://www.val.town/x/stevekrouse/reactRouter7Example/branch/main/version/164/code/react-router-questions.md)
that I had with getting React Router 7 to work full-stack in Val Town. The
result is my nascent [vtrr](https://www.val.town/x/stevekrouse/vtrr) framework.
I'm particularly proud of this 50 line full-stack react app demo in
[a single file](https://www.val.town/x/stevekrouse/vtrr/code/demos/hello-world.tsx):

![Screenshot 2026-03-21 at 18.48.14@2x.png](https://imagedelivery.net/iHX6Ovru0O7AjmyT5yZRoA/448cbc3e-a196-4d2f-7f96-6b0dcf822200/public)

If you know of any other snippet of code that can master all that complexity as
beautifully, I'd love to see it.

It seems like 99% of society has agreed that code is dead. Just yesterday I was
listening to podcaster Sam Harris of all people confidently talking about how everyone agrees
coding is dead, and that nobody should learn to code anymore.

This is so sad. It's the same as thinking storytelling is dead at the invention
of the printing press. No you dummies, code is just getting started. AI is going
to be such a boon for coding.

I have so much more to say on this topic, but this essay is already 3x longer
than I wanted it to be. I'll stop here and leave you with some of my favorite
quotes on formalism.

> Instead of regarding the obligation to use formal symbols as a burden, we
> should regard the convenience of using them as a privilege: thanks to them,
> school children can learn to do what in earlier days only genius could
> achieve.
>
> When all is said and told, the "naturalness" with which we use our native
> tongues boils down to the ease with which we can use them for making
> statements the nonsense of which is not obvious.
>
> – Edsger W.Dijkstra,
> [On the foolishness of "natural language programming"](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)

> There are two ways of constructing a software design: One way is to make it so
> simple that there are obviously no deficiencies, and the other way is to make
> it so complicated that there are no obvious deficiencies.
>
> –
> [Tony Hoare](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/tony-hoare/index.html),
> [h/t Paul Buchheit](https://news.ycombinator.com/item?id=47325225)

> The quantity of meaning compressed into a small space by algebraic signs, is
> another circumstance that facilitates the reasonings we are accustomed to
> carry on by their aid."
>
> – Charles Babbage, quoted in Iverson's Turing Award Lecture, quoted in
> [Succinctness is Power by Paul Graham](https://paulgraham.com/power.html)