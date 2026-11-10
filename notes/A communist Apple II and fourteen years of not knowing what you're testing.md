---
title: "A communist Apple II and fourteen years of not knowing what you're testing"
url: https://llama.gs/blog/index.php/2026/04/10/friday-archaeology-a-communist-apple-ii-and-fourteen-years-of-not-knowing-what-youre-testing/
clipped: 2026-06-17 01:17:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [A communist Apple II and fourteen years of not knowing what you're testing](https://llama.gs/blog/index.php/2026/04/10/friday-archaeology-a-communist-apple-ii-and-fourteen-years-of-not-knowing-what-youre-testing/)

## Digest Summary
The post contrasts current AI hype with the disciplined practice of reverse engineering. It recounts how Bulgaria’s Pravetz (Правец) computers were built in the 1970s‑80s as Apple II clones: engineers at Sofia’s Institute of Technical Cybernetics copied the 6502‑based design, replaced the ROM and case, added Cyrillic uppercase character encoding, and later integrated Z80 CPUs and CP/M support. By the mid‑1980s Pravetz accounted for ~40 % of personal computers in COMECON, illustrating how detailed schematic replication enabled a national computing base without proprietary access.

The article then describes the ISCAS‑85 benchmark suite, released in 1985 as gate‑level netlists without functional documentation. In 1999, Hayes, Hansen, and Yalcin reverse‑engineered all ten circuits, revealing real hardware functions (e.g., a 27‑channel interrupt controller, an 8‑bit ALU, a 16×16 multiplier). Their work provided functional specifications that improve test generation, synthesis verification, and hierarchical analysis.

Finally, the author links reverse engineering, model‑based diagnosis, and synthesis as mathematically dual problems—each solving for a circuit’s behavior given different fixed variables—arguing that careful analysis yields lasting understanding unlike opaque, resource‑intensive AI development.

## Discussion Summary
The comment expresses enthusiasm for the article’s coverage of Bulgaria’s coordinated approach to reverse‑engineering computing technology, noting its historical significance and the surprising ability to read Bulgarian. It reflects curiosity about the broader impact of such initiatives and highlights interest in evaluating AI agent performance, questioning whether systematic metrics exist beyond informal impressions. Overall, the tone is positive, inquisitive, and focused on both historical context and contemporary measurement challenges.

---

## Full Article

It is Friday. [KPMG](https://www.theregister.com/2026/04/10/ai_roi_kpmg/), the consultancy behemoth that delivers business Venn diagrams for outrageous prices, informs us that 70 percent of UK business leaders will keep spending on AI even when they can’t prove it does anything — the consultancy helpfully suggests we stop calling it “investment” and start calling it a “strategic enabler for enterprise-wide transformation,” which is the corporate equivalent of renaming a hole in the ground a “subterranean opportunity space.”

Meanwhile, [OpenAI has put Stargate UK on ice](https://www.theregister.com/2026/04/09/openai_puts_stargate_uk_on/), citing the cost of electricity and the regulatory environment, mere months after announcing it during a Trump state visit — one assumes the due diligence was conducted with the same rigour as the naming convention.

[AMD’s AI director reports](https://www.theregister.com/2026/04/06/anthropic_claude_code_dumber_lazier_amd_ai_director/) that Claude Code has become “dumber and lazier” since February, based on analysis of 6,852 sessions and 234,760 tool calls, which is the most thorough performance review any AI has received and rather more than most human employees get. One notes that the [AWS CEO, asked whether AI is overhyped](https://www.theregister.com/2026/04/07/aws_garman_humanx_ai_underhyped/), described the question as “one of the funnier questions I get” and then asked a room full of people who had each paid $4,000 to attend an AI conference whether they believed in AI. Asking turkeys to vote on Christmas, as it were.

In this climate of expensive ~~credulity~~ naïveté, I thought we might spend a Friday doing something that we do on Fridays: looking backwards. Reverse engineering — the art of taking something apart to understand what it does — is the intellectual opposite of the current AI approach to technology, which is to build something enormous, declare it transformative, and hope nobody asks what it actually computes.

The Правец (Pravetz): Bulgaria’s Apple II, Give or Take an Iron Curtain
-----------------------------------------------------------------------

I grew up using [Правец](https://en.wikipedia.org/wiki/Pravetz_computers) (Pravetz) computers — forgive the Cyrillic, but we Bulgarians invented the alphabet, even though half the Slavic world claims the credit, and besides, it makes any noun look like classified military hardware. Every Bulgarian of a certain age used one. The Правец 82 was the machine in my school, with its yellow plastic case, black keyboard, red RESET key, and the unmistakable aura of a computer that had been reverse-engineered from a capitalist original by engineers who had never seen Cupertino and didn’t need to.

My first encounter with a personal computer was typing in a BASIC program that drew [Lissajous figures](https://en.wikipedia.org/wiki/Lissajous_curve) in hi-res graphics. I was in the fourth grade. It was 1987. But I am digressing.

![CDN media](https://preview.redd.it/a-brief-history-of-the-bulgarian-personal-computers-imko-v0-0xysb4xiqii61.jpg?width=1214&format=pjpg&auto=webp&s=5af7ef4b6cc57f1a5af09530c4ae8a3e3e553a12)

IMKO-1 PC

The story of the Bulgarian computer is worth telling properly. In 1979, engineer [Ivan Marangozov](https://3seaseurope.com/pravetz-ivan-marangozov-inventor-bulgaria-computer/) at the [Institute of Technical Cybernetics and Robotics](https://en.wikipedia.org/wiki/Pravetz_computers) (ИТКР) in Sofia built the IMKO-1 — the first Bulgarian personal computer. It was a clone of the [Apple II](https://en.wikipedia.org/wiki/Apple_II), and “clone” is doing some diplomatic heavy lifting here: the ROM was identical, the schematics were identical, the [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502) CPU ran at the same 1 MHz. The differences were a metal case that could double as ballast, a linear power supply heavy enough to qualify as exercise equipment, and the replacement of lowercase Latin with uppercase Cyrillic — because behind the Iron Curtain, you didn’t do lowercase. The keyboard used 7 bits for character codes, so Cyrillic overlapped with Latin lowercase. A limitation, but also an engineering decision that had a certain brutal elegance: you get one alphabet at a time, comrade, and you will type in capitals.

The rumours of how this was accomplished are better than the facts. The Bulgarian intelligence services allegedly sent operatives to procure Apple IIs from the West — less James Bond, more cartoon characters getting drunk on capitalist Coca-Cola while trying to buy a computer with a heavy accent and a suitcase full of [leva](https://en.wikipedia.org/wiki/Bulgarian_lev) (the Bulgarian currency, not then known for its convertibility). More interesting is what happened next: an institute in Sofia was reportedly tasked with decapping the ICs, lifting the netlists under a microscope, and reproducing them with socialist lithography — the equipment for which was probably lifted from the Dutch. The reasonable question is why arguably clever people went through all of this when designing an ALU from scratch is not that difficult, but we will leave this armchair philosophy question to the LLMs. They have the confidence for it, if not the answer.

Today, people do this sort of thing voluntarily and for fun. The [6502.org](http://6502.org/) community hosts [dozens of homebrew computer projects](http://6502.org/homebuilt) — enthusiasts building 6502-based machines from scratch on breadboards, complete with VGA output and SD card storage, using parts that are still in production. The [MOnSter 6502](https://monster6502.com/) takes it further: a fully functional 6502 processor built from 3,218 discrete transistors on a circuit board the size of a dinner plate, with LEDs showing the state of every register. What the Bulgarian state did with an institute and a five-year plan, hobbyists now do in garages on weekends.

[Marangozov](https://en.wikipedia.org/wiki/Pravetz_computers) was, depending on your perspective, either rightfully accused of cloning the Apple II or laudably credited with delivering computing to an entire country that couldn’t buy one. The truth is both, and neither is shameful. Apple II schematics were published. Steve Wozniak *intended* the design to be understandable. What Marangozov and his team did was take a published design, source the components (Bulgarian and Soviet clones of American chips — clones all the way down), adapt the character set, and manufacture hundreds of thousands of units that shipped to every school and scientific institute in the [Eastern Bloc](https://en.wikipedia.org/wiki/Eastern_Bloc). By the mid-1980s, Bulgaria was producing 40 percent of the personal computers used in [COMECON](https://en.wikipedia.org/wiki/Comecon) countries. Not bad for a country whose communist leader [Todor Zhivkov](https://en.wikipedia.org/wiki/Todor_Zhivkov) — a peasant’s son turned printer’s apprentice who rose through the party ranks on the strength of Soviet patronage and the convenient absence of anyone more threatening — happened to have been born in the village that gave the computers their name. Правец was a hamlet of no consequence until Zhivkov turned it into a town by decree in the 1960s; by the 1980s it was assembling the flagship technology of the Eastern Bloc. One does not need a diagnostic engine to detect the fault in this particular circuit of patronage.

The later models improved substantially. The Правец 8M integrated a [Z80](https://en.wikipedia.org/wiki/Zilog_Z80) alongside the 6502, letting it run [CP/M](https://en.wikipedia.org/wiki/CP/M). The 8A was a proper [Apple IIe](https://en.wikipedia.org/wiki/Apple_IIe) clone with expandable memory. The military version had an integrated terminal design, because of course it did. There was even a Правец 8D, which broke ranks entirely — it was a clone of the British [Oric Atmos](https://en.wikipedia.org/wiki/Oric_Atmos), presumably because even Bulgarian engineers sometimes want variety.

The point is not that Bulgaria copied Apple. The point is that reverse engineering — understanding a design well enough to reproduce and adapt it — was how an entire generation of engineers learned computing. We didn’t have access to Stanford or MIT. We had schematics, soldering irons, and a cheerful disregard for intellectual property law that was, in fairness, philosophically consistent with the economic system. The Правец was my first computer. Everything I know about hardware starts there: with a 6502, 48 kilobytes of RAM, and a cassette recorder that worked when it felt like it.

Hayes and the ISCAS Circuits: What Were They For?
-------------------------------------------------

Now here is a story about reverse engineering that is less well-known outside the EDA community but is, in its own way, just as delightful.

The [ISCAS-85 benchmarks](https://en.wikipedia.org/wiki/ISCAS) are the standard test circuits for digital design research. If you work on test generation, fault diagnosis, synthesis, or timing analysis, you have used them. They were released by [Franc Brglez](https://en.wikipedia.org/wiki/ISCAS) and Hisashi Fujiwara in 1985 as a “neutral netlist of 10 combinational benchmark circuits” — gate-level descriptions of real circuits, stripped of context, for the research community to use as common benchmarks.

There was just one problem. Nobody told the research community what the circuits *did*.

For fourteen years, thousands of researchers ran experiments on c432, c499, c880, c1355, c2670, c3540, c5315, c6288, and c7552. They generated test patterns for them. They diagnosed faults in them. They timed them, synthesized them, mapped them to FPGAs. They published papers about them. And nobody — *nobody* — knew what these circuits were actually supposed to compute.

Then in 1999, [Mark Hansen, Hakan Yalcin, and John P. Hayes](https://ieeexplore.ieee.org/document/785838/) at the University of Michigan did what should have been done from the start. They reverse-engineered the lot. Their paper, “[Unveiling the ISCAS-85 Benchmarks: A Case Study in Reverse Engineering](https://dl.acm.org/doi/abs/10.1109/54.785838),” published in IEEE Design & Test, is a masterpiece of detective work. They took each gate-level netlist, partitioned it into standard RTL blocks, identified the function of each block, and reconstructed the high-level architecture. The methodology was elegantly practical: Hayes assigned each circuit to a PhD student. Cheap labour, and almost certainly cheaper per insight than an LLM.

The results were revelatory. c432 turned out to be a [27-channel interrupt controller](https://tumbleweed.nu/r/iscas.restore/doc/trunk/c432.html). c880 was an [8-bit ALU](https://tumbleweed.nu/r/iscas.restore/doc/trunk/c880.html). c6288 was a [16×16 multiplier](https://tumbleweed.nu/r/iscas.restore/doc/trunk/c6288.html). c7552 was a [32-bit adder/comparator](https://tumbleweed.nu/r/iscas.restore/doc/trunk/c7552/c7552.html). c499 and c1355 were both [32-bit single-error-correcting circuits](https://tumbleweed.nu/r/iscas.restore/doc/trunk/c499.html) — the same function, different implementations. These weren’t abstract mathematical constructs. They were real designs, ripped from real hardware, and for a decade and a half the research community had been studying them the way archaeologists study pottery shards: knowing the shape but not the purpose.

Hayes’s contribution is profound and under-appreciated. By recovering the behavioral specifications, he gave the community something it had never had: the ability to test at the functional level, to verify synthesis results against intended behaviour, to use hierarchical structure for more efficient test generation. The [high-level models](https://tumbleweed.nu/r/iscas.restore/) are still available, complete with annotated schematics and structural Verilog, and they remain useful tools nearly three decades later.

Why This Matters
----------------

There is a thread connecting the Правец, the ISCAS reversal, and the work I’ve been doing with [LyDiA](https://gitlab.llama.gs/constraints/lydia) and [qbf-designer](https://gitlab.llama.gs/logic/qbf-designer).

Reverse engineering is synthesis in reverse. When Hayes looked at c6288 and deduced it was a multiplier, he was doing — by hand, with extraordinary patience — what a diagnostic engine does automatically: given a circuit and its behaviour, determine its function. When Marangozov looked at the Apple II and built the IMKO-1, he was doing technology transfer through structural analysis. And when [Johan de Kleer](https://dekleer.org/) described synthesis as “diagnosing a circuit into existence,” he was observing that the mathematical machinery is the same in both directions. Start with a broken specification (nothing works, every gate is “faulty”), and ask: what collection of “repairs” (gate placements) would make the circuit compute the desired function?

This is the ∃∀ structure I discussed in [Diagnosing Circuits into Existence](https://llama.gs/blog/index.php/2026/04/06/diagnosing-circuits-into-existence/) — the same quantifier alternation, the same miter-based equivalence checking, the same PSPACE-hard satisfaction problems. Diagnosis, synthesis, and reverse engineering are three faces of the same formal object. The only difference is which variables you fix and which you solve for.

The ISCAS-85 benchmarks are, incidentally, the circuits that LyDiA diagnoses. When I demonstrate model-based diagnosis on c432, I am diagnosing a 27-channel interrupt controller — I just didn’t know that for the first several years of my PhD. Thank you, Professor Hayes.

The Moral
---------

The current approach to technology is to build something forward: throw compute at a model, train it on everything, and see what comes out. Reverse engineering goes the other way: take something that exists, understand its structure, and extract meaning. One approach requires billions of dollars and produces systems that cannot explain themselves. The other requires patience and produces understanding.

Bulgaria built a computer industry on reverse engineering. Hayes rebuilt the foundations of benchmark-driven EDA research by reversing fourteen-year-old circuits. I am building a company on the formal connection between taking circuits apart and putting them together.

None of this requires a strategic enabler for enterprise-wide transformation. It requires mathematics, a soldering iron, and the willingness to look at something carefully until you understand what it does.

Happy Friday. The circuits do not hallucinate.