---
title: "Artificial-life: A simple (300 lines of code) reproduction of Computational Life"
url: https://github.com/Rabrg/artificial-life
clipped: 2026-06-17 01:35:06
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Artificial Life
  - Brainfuck Language
  - Genetic Algorithms
  - Evolutionary Simulation
  - Cellular Automata
related:
  - "[[Artificial Life]]"
  - "[[Brainfuck Language]]"
  - "[[Genetic Algorithms]]"
  - "[[Evolutionary Simulation]]"
  - "[[Cellular Automata]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A 300-line Brainfuck-based program simulates a grid of self-replicating artificial life that spontaneously emerges and competes for survival.
>
> **Key points:**
> - The project reproduces a research paper on how well-formed self-replicating programs emerge from simple local interactions.
> - A 240x135 grid is initialized with random Brainfuck-like code tapes that interact, mutate, and run for up to 8192 steps per iteration.
> - Self-replicating programs naturally emerge and spread over neighboring cells, mimicking biological evolution and competitive dominance.
> - Visual representations render instructions as colored pixels, showing the rapid colonization of the grid by the most efficient replicators.
>
> **Concept links:** [[Artificial Life]], [[Brainfuck Language]], [[Genetic Algorithms]], [[Evolutionary Simulation]], [[Cellular Automata]]
>
> **Suggested connections:**
> - [[Cellular Automata]] — how local state rules and grid interactions produce complex emergent behaviors.
> - [[Genetic Algorithms]] — modeling natural selection and code optimization through random mutation and replication.
<!-- ai-summary:end -->

# [Artificial-life: A simple (300 lines of code) reproduction of Computational Life](https://github.com/Rabrg/artificial-life)

## Digest Summary
A 300‑line Python implementation reproduces the experiment from “Computational Life: How Well‑formed, Self‑replicating Programs Emerge from Simple Interaction.” The simulation creates a 240 × 135 cellular grid where each 8 × 8 block encodes a 64‑instruction Brainfuck‑like program. Programs are initialized randomly; each iteration randomly pairs neighboring programs, concatenates their instruction tapes, and executes the combined program for up to 2¹³ steps. During execution, instructions can loop and mutate the tapes, enabling programs to modify themselves and their neighbor’s code. After execution, the tape is split back into the original two programs. The system observes spontaneous emergence of self‑replicating programs that copy themselves onto adjacent tapes; these replicators proliferate across the grid. Over time a more efficient replicator evolves and eventually dominates the entire population. Visualizations map each instruction to a unique color, with black pixels representing raw data cells. The demo shows early emergence of a replicator followed by its replacement by a higher‑efficiency variant.

## Discussion Summary
The discussion centers on fascination with the simulation’s emergence of dominant species and a desire to increase ecological complexity to prevent single‑species takeover, mirroring real‑world biodiversity. Commenters express appreciation for the code’s elegance and draw parallels to past genetic‑programming work and recent AI self‑replication studies, noting similar dynamics of efficient replicators outcompeting others. Several participants propose experimental extensions, such as alternative character encodings and varying no‑op frequencies, while questioning whether the current self‑replicating mechanisms represent a theoretical optimum. Overall, the tone is inquisitive and constructive.

---

## Full Article

A simple (300 lines of code) reproduction of [Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction](https://arxiv.org/abs/2406.19108).

A 240x135 grid of 64 instruction-length [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)-like programs are randomly initialized. Every iteration, neighboring programs are randomly paired, have their instruction tapes concattenated together, and are run for a maximum of $2^{13}$ steps. Once execution completes, the tapes are split back apart. The instructions are such that they can loop and mutate the instruction tapes (programs) themselves. As found in the paper, self-replicating programs that copy themselves over their neighbor's tape often spontaneously emerge, which soon spread to take over the entire grid.

Every pixel is an instruction; each instruction has a unique color, while black represents a value on the tape that is raw data storage / not an instruction. Every 8x8 section of pixels represents a single program.

In this run, a self-replicator emerges relatively early on into the run and soon takes over most of the grid, until a more efficient self-replicator evolves and takes over everything.

[![Example](https://github.com/Rabrg/artificial-life/raw/main/universe.gif)](https://github.com/Rabrg/artificial-life/blob/main/universe.gif)