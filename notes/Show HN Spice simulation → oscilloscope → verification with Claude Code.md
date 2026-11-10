---
title: "Show HN: Spice simulation → oscilloscope → verification with Claude Code"
url: https://lucasgerads.com/blog/lecroy-mcp-spice-demo/
clipped: 2026-06-17 01:16:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - hardware development
  - spice simulation
  - oscilloscope integration
  - large language models
  - automated hardware validation
related:
  - "[[Automated Hardware Validation]]"
  - "[[Large Language Models]]"
  - "[[Spice Simulation]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Integrating Claude Code with an oscilloscope and SPICE simulator enables a closed-loop hardware development workflow that streamlines model validation, firmware testing, and data analysis.
>
> **Key points:**
> - The author integrated Claude Code with hardware testing tools (oscilloscope, SPICE simulator) to overcome limitations in using natural language for circuit design.
> - Practical guidelines include providing explicit wiring connections to the LLM and structuring MCU commands via a unified Makefile (build, flash, ping, erase).
> - Discussion emphasizes enthusiasm for automated hardware workflows while warning against LLM hallucinations and unrealistic design specifications.
>
> **Concept links:** [[Hardware Development]], [[Spice Simulation]], [[Oscilloscope Integration]], [[Large Language Models]], [[Automated Hardware Validation]]
>
> **Suggested connections:**
> - [[Automated Hardware Validation]] — how LLMs can assist in testing physical systems.
> - [[Large Language Models]] — general applicability to software/hardware engineering and automation.
> - [[Spice Simulation]] — the role of circuit simulation in modern design pipelines.
<!-- ai-summary:end -->

# [Show HN: Spice simulation → oscilloscope → verification with Claude Code](https://lucasgerads.com/blog/lecroy-mcp-spice-demo/)

## Digest Summary
The author experimented with Claude Code for hardware development, finding natural‑language prompts adequate for simple circuits but cumbersome for complex designs. To improve feedback, he integrated Claude with an oscilloscope and a SPICE simulator, enabling rapid validation of SPICE models, embedded firmware, and data analysis (e.g., time‑axis normalization and alignment). A minimal demo circuit and MCU illustrate a workflow that scales to larger projects. Key practical guidelines emerged:

- **Oscilloscope use**: Claude cannot infer the physical wiring; provide explicit connection details, keep measurement data current, and avoid feeding raw traces directly—store data in files for indirect access.  
- **Microcontroller integration**: Supply a complete pin‑out/pin‑mux map, and use a Makefile exposing standard commands (build, flash, ping, erase) that Claude should invoke rather than constructing ad‑hoc commands.  

These practices streamline iterative design, testing, and analysis with Claude Code.

## Discussion Summary
The comments express mixed feelings about using large language models for circuit design. They note that combining LLMs with visual tools like mermaid diagrams can simplify description and modification of circuits, and that integrating models with hardware such as jumperless systems offers a promising closed‑loop workflow. However, there are concerns about reliability: an LLM (Claude Opus) generated unrealistic board specifications that failed in practice, requiring manual correction and verification. Overall, the discussion balances enthusiasm for automation with caution about hallucination and the need for human oversight.

---

## Full Article

I have been experimenting with using Claude Code for hardware development over the past few weeks. I looked at some projects that use Claude similarly to how one would in software development: Write a prompt in natural language, let Claude create a circuit. I found it somewhat tricky to express what I want to build in plain English. It worked fine for trivial circuits but became difficult for more complex designs. I also realized that Claude Code really shines when it can get immediate feedback.

So I tried a different approach: give Claude access to my oscilloscope and a SPICE simulator. This has become extremely valuable for validating SPICE circuits and models, embedded programming, and data analysis. In particular the data analysis had been very tedious before: normalizing the time axis, aligning data, and so on. Usually I would just eyeball it.

Below is a deliberately simple demo showcasing my setup and workflow. The circuit and MCU are trivial. The point is to illustrate the approach, which scales well to much more complex circuits and real embedded projects.

VIDEO

A few lessons learned:

**Oscilloscope**

* Claude doesn't see your physical setup. Don't let it guess what is connected where.
* Make sure Claude never gets stale measurement data.
* Don't dump raw data into Claude's context. Save it to a file and let Claude interact with it indirectly.

**Microcontroller**

* Give Claude a pinout/pinmux map explicitly.
* Prepare a Makefile that exposes functions like build, flash, ping, and erase, and encourage Claude to rely on it. Claude should not construct these commands on the fly.

**Repos**