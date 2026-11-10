---
title: "pg_durable: Microsoft open sources in-database durable execution"
url: https://github.com/microsoft/pg_durable
clipped: 2026-06-17 00:51:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Databases
  - PostgreSQL
  - Durable Execution
  - Rust Extensions
  - Workflow Orchestration
  - Systems Architecture
related:
  - "[[Show HN LocalGPT – A local-first AI assistant in Rust with persistent memory]]"
  - "[[A decade of Docker containers]]"
  - "[[Losing 1½ Million Lines of Go]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** Microsoft has open-sourced pg_durable, a PostgreSQL extension written in Rust that enables durable, checkpointed execution of long-running SQL workflows directly inside the database.
>
> **Key points:**
> - pg_durable is written using the pgrx framework and runs entirely within the PostgreSQL process, bypassing the need for external queues (like Celery or Redis) or orchestrators (like Temporal).
> - Workflows are defined in SQL using composable operators (`|=>` and `~>`) that establish directed graphs of execution steps.
> - The extension integrates `duroxide`, a Rust-based durable task framework, and `duroxide-pg` to checkpoint progress and resume execution seamlessly after database restarts or crashes.
> - Security and isolation are maintained using Row-Level Security (RLS) on user variable namespaces and submission instances, managed by a superuser background worker.
> - While developers appreciate the architectural simplification of keeping compute close to data, critics raise concerns regarding database lock scaling, debugging overhead, and version control of in-database logic.
>
> **Concept links:** [[Databases]], [[PostgreSQL]], [[Durable Execution]], [[Rust Extensions]], [[Workflow Orchestration]], [[Systems Architecture]]
>
> **Suggested connections:**
> - [[Show HN LocalGPT – A local-first AI assistant in Rust with persistent memory]] — Discusses SQLite and embedded databases in Rust.
> - [[A decade of Docker containers]] — Relates to system architecture, deployment, and infrastructure simplification.
> - [[Losing 1½ Million Lines of Go]] — Case study on microservices vs monoliths and database architecture choices.
<!-- ai-summary:end -->

# [pg_durable: Microsoft open sources in-database durable execution](https://github.com/microsoft/pg_durable)

## Digest Summary
pg_durable is a PostgreSQL extension (built with pgrx) that enables durable, fault‑tolerant execution of long‑running SQL workflows inside the database. Users define a function as a directed graph of composable SQL steps using operators such as `|=>` and `~>`, start it with `df.start(...)`, and the background worker checkpoints each step via the Rust‑based durable task framework duroxide and its PostgreSQL state provider duroxide‑pg. On crashes, restarts, or step failures execution resumes from the last checkpoint, eliminating external cron jobs, workers, queues, or orchestrators (e.g., Airflow, Temporal). The extension ships as Debian packages for PostgreSQL 17/18 and can be installed by adding `pg_durable` to `shared_preload_libraries`, restarting, and running `CREATE EXTENSION pg_durable;`. Access is controlled via RLS; privileges must be granted explicitly (e.g., `df.grant_usage`). Development tools include a VS Code dev container, scripts for local cluster start, and two test suites: fast pg_regress tests and comprehensive E2E tests. The project is preview‑stage, open‑source under the PostgreSQL License, and integrated in Azure HorizonDB.

## Discussion Summary
The comments express cautious interest in using PostgreSQL‑based queues, noting the appeal of a single data system and appreciating community contributions, while many raise practical concerns about embedding workflow logic in the database. Frequent criticisms include difficulty with unit testing, version control, observability, and scaling pressure on PostgreSQL, especially compared to established orchestration tools like Airflow or Temporal. Several users question the fit for heterogeneous environments, Azure limitations, and the lack of features such as high‑dimensional vector search. Overall, the sentiment leans toward skepticism, with limited enthusiasm contingent on clearer tooling, robustness, and demonstrable advantages over external solutions.

---

## Full Article

Long-running, fault-tolerant SQL functions for teams that already keep their state in Postgres and want to stop stitching together cron jobs, workers, queues, and status tables to make background work reliable. Define the workflow in SQL, let pg\_durable checkpoint each step, and resume after crashes, restarts, or failed steps.

Durable execution is now a standard industry pattern, and pg\_durable brings it inside Postgres with no extra service infrastructure required. Part of our mission to bring compute close to data.

> [![Azure HorizonDB logo](https://camo.githubusercontent.com/1c93a5f5b8a42b3de37404ac4417fc60e67740dd66ae5d2cca415fb6f8b98b1d/68747470733a2f2f63646e2d64796e6d656469612d312e6d6963726f736f66742e636f6d2f69732f636f6e74656e742f6d6963726f736f6674636f72702f313337343835302d49636f6e2d4865726f2d486f72697a6f6e44422d32347832343f7265734d6f64653d736861727032266f705f75736d3d312e352c302e36352c31352c30267769643d3438266865693d343826716c743d313030266669743d636f6e73747261696e)](https://camo.githubusercontent.com/1c93a5f5b8a42b3de37404ac4417fc60e67740dd66ae5d2cca415fb6f8b98b1d/68747470733a2f2f63646e2d64796e6d656469612d312e6d6963726f736f66742e636f6d2f69732f636f6e74656e742f6d6963726f736f6674636f72702f313337343835302d49636f6e2d4865726f2d486f72697a6f6e44422d32347832343f7265734d6f64653d736861727032266f705f75736d3d312e352c302e36352c31352c30267769643d3438266865693d343826716c743d313030266669743d636f6e73747261696e) **Try pg\_durable now in [Azure HorizonDB](https://aka.ms/AzureHorizonDB),** Microsoft's new PostgreSQL cloud service engineered for performance and built with [pg\_durable inside](https://aka.ms/horizondb_pg_durable)

* Backend and data engineers who want workflows to live next to the data they touch.
* DBAs and SREs automating runbooks that must survive restarts and be auditable in SQL.
* Teams building data or AI pipelines that need durable execution per row, document, or batch.

A pg\_durable function is a graph of SQL steps that PostgreSQL executes and checkpoints as it goes. If the database crashes, restarts, or a step fails, execution resumes from the last durable checkpoint instead of making you reconstruct state by hand.

### Workloads this is useful for

* Vector embedding pipelines: chunk, call an embedding API, and upsert into `pgvector`.
* Ingest pipelines: stage, deduplicate, transform, and publish large batches.
* Scheduled maintenance: detect bloat, notify, wait for approval, then run the next action.
* Fan-out aggregation: run independent queries in parallel, then join the results.
* External API workflows: enrichment, classification, and webhook-style calls from SQL.

### What you're probably doing today instead

* `pg_cron` plus a jobs table, status columns, retry counters, and a polling worker.
* An external orchestrator such as Airflow, Temporal, Step Functions, or Argo calling back into Postgres.
* A queue plus workers plus a separate state table to coordinate retries and partial completion.
* A `plpgsql` procedure that works until a crash or long-running transaction forces you to start over.

* A restart in the middle of a long job means rerunning work that already succeeded.
* One failed row or one failed API call turns into manual cleanup and uncertain replay.
* Long transactions hold locks, grow WAL, and make batch jobs fragile at larger scale.
* Parallel work in the app tier creates more places for partial-failure bugs and drift.
* The workflow logic ends up spread across SQL, workers, queues, dashboards, and status tables.

### What changes in your architecture

* The workflow definition moves into SQL and starts with `df.start(...)`.
* Retry state, progress tracking, and checkpointing move into Postgres instead of bespoke app code.
* Some app-tier workers, queue consumers, or scheduler glue can disappear entirely.
* Operational visibility comes from Postgres tables such as `df.instances`, using the same auth and backup model as your data.

* The job is already a single `INSERT ... SELECT` or one ordinary SQL statement.
* You need sub-millisecond synchronous request handling rather than durable background execution.
* You cannot install extensions or run a background worker in your Postgres environment.
* The workflow mostly lives outside Postgres and spans many heterogeneous systems.
* You need arbitrary application logic that does not map cleanly to SQL steps, branching, loops, or HTTP calls.

1. Define a workflow in SQL using composable operators such as `~>` and `|=>`.
2. Start it with `df.start()` and get back an instance ID.
3. Let the runtime execute each step durably with checkpointing between steps.
4. Query status and results from PostgreSQL while the workflow runs or after it completes.

The model is intentionally SQL-shaped. If a step needs arbitrary code, a non-HTTP SDK, or rich in-memory control flow, you may need to wrap that logic in a SQL function, expose it behind an HTTP endpoint for `df.http()`, or use a general-purpose orchestrator for that part of the system.

* **Durable** — Function state persists to PostgreSQL. Survives crashes, restarts, and failovers.
* **SQL-native** — Define functions in SQL using composable operators.
* **Database-aware** — First-class primitives for scheduling, conditions, and parallel execution.
* **Zero infrastructure** — Runs as a PostgreSQL extension. No Redis, no Temporal, no external services.

```
-- A durable function that processes data in steps
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```

Tagged releases publish Debian packages for PostgreSQL 17 and 18 on amd64 from the GitHub release assets. Packages are named `pg-durable-postgresql-<PG major>_<pg_durable version>-1_<arch>.deb` and install the extension library, control file, and SQL upgrade files into the matching PostgreSQL installation directories.

Tagged releases also publish a ready-to-run Docker image (`linux/amd64`) for PostgreSQL 17 and 18 to GitHub Container Registry: `ghcr.io/microsoft/pg_durable`. The image installs the released Debian package on top of the official `postgres` image. Each release publishes immutable `X.Y.Z-pg<major>` and `vX.Y.Z-pg<major>` tags (for example `0.2.2-pg17`, `0.2.2-pg18`); the highest stable release additionally updates the floating `pg<major>` tags, and the default major (`pg17`) also updates `latest`. The PG major version is part of every tag so multiple PostgreSQL versions can be published alongside each other. Browse all published images and tags at <https://github.com/microsoft/pg_durable/pkgs/container/pg_durable>.

> **Warning:** The published Docker image is intended for **evaluating and learning pg\_durable only — do not use it in production.** It enables superuser durable instances for a frictionless out-of-the-box demo. Its HTTP egress policy is whatever the released Debian package was built with (`http-allow-azure-domains` — Azure domains only). Multi-arch (`linux/arm64`) images are not published yet; they will follow once arm64 Debian packages are available.

Run the published image — PostgreSQL 17 and 18 can run side by side on different host ports:

```
# PostgreSQL 17 (the `latest` tag also points at the newest PG17 release)
docker run -d --name pg_durable_pg17 \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=secret \
  ghcr.io/microsoft/pg_durable:pg17

# PostgreSQL 18 (run alongside PG17 on a different host port)
docker run -d --name pg_durable_pg18 \
  -p 5433:5432 \
  -e POSTGRES_PASSWORD=secret \
  ghcr.io/microsoft/pg_durable:pg18

# Connect with psql (PG17 on 5432, PG18 on 5433)
psql "postgresql://postgres:secret@localhost:5432/postgres"
psql "postgresql://postgres:secret@localhost:5433/postgres"
```

The extension is preloaded and created in the `postgres` database on first init. `POSTGRES_DB` is ignored — pg\_durable always installs into `postgres` so the extension and the background worker never target different databases. For reproducible deployments, pin an immutable `X.Y.Z-pg<major>` tag (for example `0.2.2-pg17`) rather than the floating `pg<major>`/`latest` tags; immutable tags are never overwritten once published.

After installing a package, add `pg_durable` to `shared_preload_libraries`, restart PostgreSQL, and create the extension in the configured pg\_durable database:

```
CREATE EXTENSION pg_durable;
```

The default pg\_durable database is `postgres`; see [User Guide](https://github.com/microsoft/pg_durable/blob/main/USER_GUIDE.md) for background worker configuration and privilege setup.

Each release also publishes source archives for building from source and a `SHA256SUMS` file for verifying downloaded assets.

* PostgreSQL 17 or 18
* Rust (nightly)
* [cargo-pgrx](https://github.com/pgcentralfoundation/pgrx) 0.16.1

The main branch prebuild installs PostgreSQL 17, builds `pg_durable`, and prepares a local cluster under `~/.pgrx` with the extension ready. PostgreSQL is not left running, so start it when you begin working.

```
# Start PostgreSQL
./scripts/pg-start.sh

# Connect
~/.pgrx/17.*/pgrx-install/bin/psql -h localhost -p 28817 -d postgres
```

On a branch without a ready prebuild, run `pg-start.sh` — it will build and install the extension on first run (expect a few minutes):

A VS Code Dev Container (`.devcontainer/`) provides Rust, cargo-pgrx, and PostgreSQL 17 pre-installed. For a bare local machine, install the toolchain first by following the steps in `.devcontainer/onCreateCommand.sh`.

```
# Build, initialize PostgreSQL, and install the extension
# This takes a while - go do something else
./scripts/pg-start.sh

# Connect to the local pgrx PostgreSQL instance
~/.pgrx/17.*/pgrx-install/bin/psql -h localhost -p 28817 -d postgres
```

`pg-start.sh` bootstraps new local data directories with a `postgres` superuser and also creates a matching superuser role for the current OS user, so default local `psql` usage continues to work. Use `-U postgres` if you want to force the canonical bootstrap role explicitly.

To run the prebuilt published image, see the [Packages](https://github.com/microsoft/pg_durable#packages) section. For local development and testing, build and run from source:

```
# Build and test (source Dockerfile — compiles the extension)
./scripts/test-e2e-docker.sh --rebuild

# Optional: Deploy to ACR (for a custom PG17 image with pg_durable baked-in)
./scripts/deploy-acr.sh
```

> The published GHCR image installs the released `.deb` on top of the official `postgres` image; the source `Dockerfile` used here compiles the extension and is meant for CI and local development. They are different artifacts.

`CREATE EXTENSION pg_durable` does **not** grant any privileges to `PUBLIC`. After installing the extension, the admin must explicitly grant access to application roles. Row-level security (RLS) ensures each user can only see and manage their own durable function instances and nodes.

**Grant privileges to an application role:**

```
-- Grant to specific roles after CREATE EXTENSION
SELECT df.grant_usage('app_role');
```

Alternatively, create an indirection role and grant membership to application roles:

```
-- Create a shared role for pg_durable access
CREATE ROLE pg_durable_user NOLOGIN;
SELECT df.grant_usage('pg_durable_user');

-- Grant membership to application roles
GRANT pg_durable_user TO app_backend, etl_service;
```

> See the [User Guide — Privilege Grants](https://github.com/microsoft/pg_durable/blob/main/USER_GUIDE.md#privilege-grants) section for the full list of individual grants, revoking access, and hardening upgraded installs.

> **Note:** `GRANT EXECUTE ON ALL FUNCTIONS` only applies to functions that exist when the grant runs. After upgrading pg\_durable with `ALTER EXTENSION pg_durable UPDATE`, re-run `df.grant_usage('role')` (or re-issue the manual grants) so new functions are accessible.

**Key points:**

* The background worker role (`pg_durable.worker_role` GUC, default: `postgres`) **must be a superuser** — it bypasses RLS to manage all users' instances
* Users get `SELECT` + `INSERT` on `df.instances` / `df.nodes`, column-level `UPDATE (status, updated_at)` on instances for `df.cancel()`
* Identity column (`submitted_by`) cannot be modified by users
* **`df.vars` uses per-user scoping** — each user has their own variable namespace via an `owner` column and RLS. Superusers bypass RLS but DSL functions still scope to the calling user via explicit filters. Avoid storing secrets in plain text

All pull requests must pass the following checks before merging:

1. **Format Check** — `cargo fmt --check`
2. **Clippy & Tests** — `cargo clippy`, unit tests (`cargo pgrx test pg17`), pg\_regress tests, and E2E tests

The CI workflow is defined in [.github/workflows/ci.yml](https://github.com/microsoft/pg_durable/blob/main/.github/workflows/ci.yml). It uses pgrx to download and manage PostgreSQL.

pg\_durable has two test suites:

### pg\_regress Tests (Standard PostgreSQL Regression Tests)

Fast, deterministic tests for core DSL functionality using PostgreSQL's standard testing framework.
Test SQL lives in `sql/`, expected output in `expected/`, and PGXS is configured in the root `Makefile`.

```
make test-regress          # full reset + run
make installcheck          # run only (PostgreSQL must already be running)
```

### E2E Tests (Comprehensive Scenario Tests)

Complex local integration tests with pgrx PostgreSQL:

```
./scripts/test-e2e-local.sh                                                  # All local SQL E2E tests, including special restart/config phases
./scripts/test-e2e-local.sh 04_parallel                                      # Specific test
./scripts/test-e2e-local.sh --default-build-phases                            # Only the default-build phase group
```

See [tests/e2e/](https://github.com/microsoft/pg_durable/blob/main/tests/e2e) for details.

* [User Guide](https://github.com/microsoft/pg_durable/blob/main/USER_GUIDE.md) — Complete usage guide with examples
* [MVP Guide](https://github.com/microsoft/pg_durable/blob/main/docs/pg_durable_mvp.md) — Implementation details and internals
* [Examples](https://github.com/microsoft/pg_durable/blob/main/examples/README.md) — Example conventions and smoke-check guidance

pg\_durable is a PostgreSQL extension (built with [pgrx](https://github.com/pgcentralfoundation/pgrx)) — everything runs inside the PostgreSQL server, no external services. The extension exposes a SQL DSL for building function graphs and registers a background worker that executes them durably on top of two lower-level Rust libraries:

* [duroxide](https://github.com/microsoft/duroxide) — a durable task framework providing the orchestration runtime (deterministic replay, checkpoints, sub-orchestrations, timers).
* [duroxide-pg](https://github.com/microsoft/duroxide-pg) — a PostgreSQL-backed state provider for duroxide. It persists runtime state (instances, history, work queues) in a dedicated `duroxide.*` schema owned by the extension.

```
┌────────────────────────────────────────────────────────────────────┐
│                             PostgreSQL                             │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                 pg_durable extension (pgrx)                  │  │
│  │                                                              │  │
│  │  SQL DSL     'sql' |=> 'name' ~> 'sql2'                      │  │
│  │              df.if() | df.join() | df.loop()                 │  │
│  │                                                              │  │
│  │  Background worker (hosts the duroxide runtime in-process)   │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │  duroxide        (orchestration runtime)               │  │  │
│  │  │  ┌──────────────────────────────────────────────────┐  │  │  │
│  │  │  │  duroxide-pg   (PostgreSQL state provider)       │  │  │  │
│  │  │  └──────────────────────────────────────────────────┘  │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                    │
│  Schemas                                                           │
│    df.*         DSL graphs (nodes, instances, vars)                │
│    duroxide.*   runtime state (owned by duroxide-pg)               │
└────────────────────────────────────────────────────────────────────┘
```

If you'd rather author durable functions in Rust, Python, or Node while still persisting state in PostgreSQL, you can use duroxide and duroxide-pg directly from your host language — pg\_durable is what you'd build on top of that pair when you'd prefer authoring in SQL.

**Preview** - This project is currently in preview.

Use GitHub Issues for bug reports and feature requests. Do not report security vulnerabilities through public GitHub issues; follow the instructions in [SECURITY.md](https://github.com/microsoft/pg_durable/blob/main/SECURITY.md) instead.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or comments.

Microsoft takes the security of our software products and services seriously. Please do not report security vulnerabilities through public GitHub issues. See [SECURITY.md](https://github.com/microsoft/pg_durable/blob/main/SECURITY.md) for security reporting instructions.

pg\_durable does not send telemetry to Microsoft.

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos is subject to those third-party policies.

PostgreSQL License