---
title: "Show HN: Micasa \u2013 track your house from the terminal"
url: "https://micasa.dev"
clipped: 2026-06-17 01:42:54
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - terminal user interface
  - home automation
  - sqlite database
  - offline-first
related:
  - "[[Personal Knowledge Management]]"
  - "[[Local-First Software]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Micasa is an open-source, keyboard-driven terminal home-management tool using SQLite to track home maintenance, projects, and documents.
>
> **Key points:**
> - Consolidates home maintenance logs, appliances, vendors, and receipts in a single local SQLite database.
> - Features Vim-style keybindings, fuzzy navigation, and auto-computed maintenance schedules.
> - Operates completely offline, prioritizing privacy and portability over cloud solutions.
> - Aims to replace scattered binders and physical documents with structured, searchable logs.
>
> **Concept links:** [[Terminal User Interface]], [[Home Automation]], [[Sqlite Database]], [[Offline-First]]
>
> **Suggested connections:**
> - [[Local-First Software]] — because of Micasa's offline SQLite architecture.
> - [[Terminal User Interface]] — since it uses Vim-style navigation in the terminal.
<!-- ai-summary:end -->

# [Show HN: Micasa – track your house from the terminal](https://micasa.dev)

## Digest Summary
micasa is a terminal‑based home‑management tool that stores maintenance records, projects, incidents, appliances, vendors, quotes, and related documents in a single SQLite file. It provides auto‑computed maintenance schedules, full service histories, warranty tracking, and incident logging with severity and location tags, linking items to vendors and files (manuals, invoices, photos). The interface is keyboard‑driven with Vim‑style modal keys, supporting column sorting, fuzzy navigation, and drill‑down into related records; keybindings are documented in a reference sheet. Installation requires Go 1.25+ (`go install github.com/cpcloud/micasa/cmd/micasa@latest`) or a precompiled binary for Linux, macOS, or Windows (amd64/arm64). Quick start commands include `micasa --demo` for sample data, `micasa` for a new database, and `micasa --print-path` to locate the file. The project aims to replace scattered receipts, binders, and notes with a single, portable database, inspired by the VisiData modal UI paradigm.

## Discussion Summary
The comments convey strong enthusiasm for the project’s TUI design, its simplicity, and the clever use of SQLite, with many users praising its aesthetics and practicality for personal home‑maintenance tracking. Repeated suggestions include adding a web or mobile interface, cloud sync, reminder or email automation, and easier data export, to make the tool accessible to non‑technical household members. Concerns appear around backup safety, reliance on a terminal‑only workflow, and the choice of a relational database versus plain text or spreadsheet alternatives. Overall sentiment is positive, tempered by requests for broader usability features.

---

## Full Article

When did I last change the furnace filter?

Schedules, due dates, full history. Set it and forget it.

What if we finally did the backyard?

Projects from napkin sketch to completion, or graceful abandonment.

How much would it cost to…

Quotes side by side, vendor history, and the math to actually decide.

Who did we use last time?

Every contractor, every quote, every job. All searchable.

How much have I spent on plumbing this year?

Ask a local LLM. Or don't. Offline until you say otherwise.
