---
title: "Sqldef: Idempotent schema management tool for MySQL, PostgreSQL, SQLite"
url: https://sqldef.github.io/
clipped: 2026-06-17 01:48:33
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Database Migration
  - Declarative Infrastructure
  - SQL DDL
  - MySQL Database
  - PostgreSQL
related:
  - "[[Database Migration]]"
  - "[[Declarative Infrastructure]]"
  - "[[SQL DDL]]"
  - "[[MySQL Database]]"
  - "[[PostgreSQL]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Sqldef is a database schema migration CLI tool that uses SQL DDL files to generate declarative migrations for databases like MySQL, Postgres, and SQLite.
>
> **Key points:**
> - Sqldef compares the target database state against a desired SQL schema file to generate the required ALTER or CREATE SQL statements.
> - The tool supports multiple relational database systems including MySQL, PostgreSQL, SQLite3, SQL Server, MariaDB, and TiDB.
> - Unlike traditional migration frameworks that require sequence files, it uses standard declarative SQL definitions to manage schema states.
> - Comments highlight its utility for speed, but note challenges managing data migrations, column renames, and complex sequence ordering.
>
> **Concept links:** [[Database Migration]], [[Declarative Infrastructure]], [[SQL DDL]], [[MySQL Database]], [[PostgreSQL]]
>
> **Suggested connections:**
> - [[Database Migration]] — comparing declarative state migration tools (like Sqldef) against imperative, version-based migration files.
> - [[Declarative Infrastructure]] — applying gitops-like declarative state management to database schema configurations.
<!-- ai-summary:end -->

# [Sqldef: Idempotent schema management tool for MySQL, PostgreSQL, SQLite](https://sqldef.github.io/)

## Digest Summary
sqldef is a command‑line interface tool designed to compare (diff) two SQL schema definitions and facilitate migration between relational database management systems using standard SQL Data Definition Language statements. It operates across multiple platforms, explicitly supporting MySQL, MariaDB, TiDB, PostgreSQL, Microsoft SQL Server, and SQLite 3. An online demonstration is provided, allowing users to experiment with schema diffing for MySQL, PostgreSQL, SQLite 3, and SQL Server, with an option to enable DROP statements in the generated migration script. The tool focuses on direct schema comparison without requiring proprietary migration frameworks, leveraging native DDL syntax for consistency across the listed databases.

## Discussion Summary
Comments show a generally favorable view of the tool’s ability to simplify schema changes, with users appreciating its speed for development and reliability for migrations, and many expressing intent to adopt it or share it with teams. At the same time, several points of criticism recur: limited usefulness for non‑empty databases, inadequate handling of data migrations such as column renames or JSONB restructuring, and concerns about future licensing and difficulty with complex migration ordering. Compatibility questions and comparisons to alternative approaches like manual scripts or AI‑generated migrations also appear.

---

## Full Article

sqldef
======

sqldef is a [CLI tool](https://github.com/sqldef/sqldef) for diffing two SQL schemas. You can use it to
manage the migration of RDBMSs using regular SQL DDLs.

Supported databases: MySQL, MariaDB, TiDB, PostgreSQL, SQL Server, and SQLite3.

Online Demo
-----------

MySQL
PostgreSQL
SQLite3
SQL Server

 Enable DROP