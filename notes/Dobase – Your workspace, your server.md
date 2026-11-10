---
title: "Dobase – Your workspace, your server"
url: https://dobase.co/
clipped: 2026-06-17 01:26:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - Self-Hosting
  - Open Source Workspace
  - Ruby on Rails
  - SQLite Database
  - Data Privacy
  - Sovereign Software
related:
  - '[[AI is killing B2B SaaS]]'
  - '[[From Supabase to Clerk to Better Auth]]'
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Dobase is a self-hosted, open-source collaborative workspace platform designed with a minimal Rails, SQLite, and Docker stack to prioritize user privacy.
>
> **Key points:**
> - Runs on a single VPS with zero analytics, tracking, or third-party sharing.
> - Employs a simplified, lightweight stack: one Ruby on Rails application, one SQLite database, and one Docker container.
> - Features real-time collaboration with modular tools like Kanban boards, calendars, document editors, task lists, and file storage.
> - Aims to offer a sovereign alternative to bloated, unified SaaS platforms by allowing users to install only what they need.
>
> **Concept links:** [[Self-Hosting]], [[Open Source Workspace]], [[Ruby on Rails]], [[SQLite Database]], [[Data Privacy]], [[Sovereign Software]]
>
> **Suggested connections:**
> - [[AI is killing B2B SaaS]] — provides a counter-example of a self-hosted alternative to SaaS giants.
> - [[From Supabase to Clerk to Better Auth]] — contrasts minimal self-hosted stacks (SQLite/Rails) with complex modern cloud auth/database setups.
<!-- ai-summary:end -->

# [Dobase – Your workspace, your server](https://dobase.co/)

## Digest Summary
Dobase is a self‑hosted, open‑source workspace platform designed to run on a single VPS using a minimal stack: one Ruby on Rails application, one SQLite database, and one Docker container. It emphasizes data privacy—no analytics, tracking, or third‑party sharing—and allows users to install only the tools they need. Core functionality includes real‑time collaboration across multiple modules such as a Kanban board, email client, team chat, calendar, rich‑text document editor, task lists, and file storage. The interface supports features like due dates, assignee assignment, threaded conversations, file sharing, command‑palette navigation, and detailed card views with comments and attachments. Users can invite collaborators, add custom tools, and navigate via a command palette, providing a modular, privacy‑focused alternative to cloud‑based workspaces.

## Discussion Summary
The feedback criticizes integrated platforms like Clickup for being cumbersome, especially when switching between chat, tickets, and documentation within a single interface, and expresses a preference for dedicated, separate applications for each function. It also notes concerns about the reliability of AI‑generated commit logs and the difficulty of deploying sovereign, open‑source alternatives, hoping for simpler hosting solutions similar to WordPress. Additionally, there is a request for the ability to drag emails onto kanban or todo items and access the original message directly from the task.

---

## Full Article

Your data, your rules.
----------------------

Dobase runs on your server. No analytics, no tracking, no third-party data sharing. One Rails app, one SQLite database, one Docker container. That is the entire stack.

* Self-hosted on any VPS
* Fully open source
* Real-time collaboration built in
* Install only the tools you need