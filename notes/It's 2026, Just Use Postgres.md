---

title: "It's 2026, Just Use Postgres"
url: https://www.tigerdata.com/blog/its-2026-just-use-postgres
clipped: 2026-06-17 01:48:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - database consolidation
  - postgresql extensions
  - system simplification
  - developer operations
  - database benchmarking
related:
  - "[[Database Consolidation]]"
  - "[[PostgreSQL Extensions]]"
  - "[[System Simplification]]"
  - "[[Developer Operations]]"
  - "[[Database Benchmarking]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The article advocates database consolidation, demonstrating how PostgreSQL extensions (like pgvector, TimescaleDB, and JSONB) can replace specialized databases to reduce operational complexity.
>
> **Key points:**
> - Managing multiple databases (e.g. Redis, MongoDB, Elasticsearch, Kafka) increases cognitive load, synchronization bugs, and downtime risks.
> - Consolidating workloads into PostgreSQL with extensions (pgvector, TimescaleDB, pg_textsearch, pgmq) keeps data under one roof.
> - Single-database architectures are essential in the AI era, where autonomous coding agents need to spin up and tear down test environments easily.
> - Benchmarks show that Postgres extensions, utilizing the same core algorithms as specialized products, deliver competitive performance and significantly lower infrastructure costs.
>
> **Concept links:** [[Database Consolidation]], [[PostgreSQL Extensions]], [[System Simplification]], [[Developer Operations]], [[Database Benchmarking]]
>
> **Suggested connections:**
> - [[PostgreSQL Extensions]] — on using pgvector, TimescaleDB, and JSONB to handle diverse datatypes.
> - [[System Simplification]] — on the operational advantages of reducing system dependencies.
> - [[Developer Operations]] — on creating sandbox environments for engineers and AI agents.
<!-- ai-summary:end -->

# [It's 2026, Just Use Postgres](https://www.tigerdata.com/blog/its-2026-just-use-postgres)

## Digest Summary
PostgreSQL can serve as a single‑system platform for workloads traditionally handled by specialized databases. Extensions provide native functionality equivalent to external tools: pg_textsearch implements BM25 full‑text search; pgvector + pgvectorscale (DiskANN) deliver vector similarity with latency 28× lower and 75 % cheaper than Pinecone; TimescaleDB supplies time‑series partitioning, compression and SQL queries comparable to InfluxDB; JSONB offers document storage and indexing on par with MongoDB; unlogged tables act as in‑memory caches similar to Redis; pgmq provides lightweight message queues replacing Kafka; PostGIS delivers mature GIS capabilities; pg_cron handles scheduled jobs. Consolidating these features in PostgreSQL reduces operational overhead—one backup, monitoring stack, security model, and connection string—while avoiding data‑drift sync jobs and multi‑service coordination, especially important for AI agents that frequently fork test environments. Benchmarks cite 28× lower latency for vector search, comparable or superior performance for time‑series and full‑text search, and cost reductions. The article argues that for ~99 % of companies, PostgreSQL with its ecosystem meets performance, reliability, and scalability needs, reserving separate specialized systems for only the largest, most exotic workloads.

## Discussion Summary
Comments express strong admiration for PostgreSQL’s capabilities, noting its performance, flexibility and extensive ecosystem, but many caution against treating it as a universal solution. Contributors highlight the importance of evaluating use‑cases, pointing to specialized databases such as Redis, ClickHouse, Elasticsearch, SQLite, MySQL and columnar engines for caching, search, time‑series, vector, or simple embedded needs. Operational concerns appear frequently, including tuning complexity, clustering, HA, and resource contention when multiple workloads share a single instance. A recurring theme criticizes overly generic “just use Postgres” advice and the prevalence of AI‑generated posts.

---

## Full Article

Think of your database like your home. Your living room, bedroom, kitchen, garage: each room serves a different purpose, but they're all under one roof. You don't build a restaurant across town because you need to cook dinner. You don't rent a commercial garage to park your car.

Postgres works the same way. Search, vectors, time-series, queues, documents, all rooms in one house. Same roof, foundation, and key.

But specialized database vendors have spent years telling you otherwise. "Use the right tool for the right job," they say. It sounds reasonable and wise. And it sells a lot of databases.

You follow the advice. You adopt Elasticsearch for search, Pinecone for vectors, Redis for caching, MongoDB for documents, Kafka for queues, InfluxDB for time-series. Postgres handles whatever's left.

Congratulations. You now have seven databases to manage. Seven query languages to learn. Seven backup strategies to maintain. Seven security models to audit. Seven monitoring dashboards to watch. And seven things that can break at 3 AM.

When something does break? Good luck spinning up a test environment to reproduce it. You'll need synchronized snapshots across all seven systems, all at the same point in time, with seven services running in your local environment. Let us know how that goes.

The AI Era Changed the Math
---------------------------

Here's what makes this argument different in 2026: AI agents.

Think about what agents need to do. Spin up a test database with production data. Try a fix. Verify it works. Tear it down. With one database, that's a single fork command. Fork it, test it, done.

With seven databases? Now your agent needs to coordinate snapshots across every system, spin up seven services, configure seven connection strings, hope nothing drifts while testing, and tear it all down afterward. That's not a minor inconvenience. It's a research project. And it's why most AI coding agents quietly assume a single-database architecture.

This applies beyond agents. Every on-call engineer who needs a test environment at 3 AM faces the same coordination problem. So does every CI pipeline that needs realistic data, and every team that wants to experiment safely.

And it compounds at the organizational level. When your data lives in one database, a new engineer can understand the entire data model in a day. They can run the full stack locally with a single connection string. They can write a migration, test it against a fork of production, and ship it with confidence. When your data is scattered across seven systems, onboarding alone becomes a multi-week project. "How does search stay in sync with the main database?" is a question that shouldn't require a 45-minute architecture review to answer.

Database consolidation used to be an architectural preference. A nice-to-have. In the AI era, it's becoming a functional requirement. The teams that can fork, test, and iterate on a single database will ship faster than teams coordinating across seven.

The Algorithm Reality
---------------------

Here's what the specialized database vendors don't want you to think too hard about: in most cases, Postgres extensions use the same core algorithms as their products.

| What You Need | Specialized Tool | Postgres Extension | Algorithm | When You Still Need the Specialist |
| --- | --- | --- | --- | --- |
| Full-text search | Elasticsearch | [pg\_textsearch](https://www.tigerdata.com/blog/you-dont-need-elasticsearch-bm25-is-now-in-postgres) | Both use BM25 | You need Kibana dashboards, complex nested aggregations, or cluster-scale search across petabytes |
| Vector search | Pinecone | [pgvectorscale](https://www.tigerdata.com/blog/pgvector-vs-pinecone) | Both use HNSW/DiskANN | You need managed multi-tenant sharding at billions of vectors |
| Time-series | InfluxDB | [TimescaleDB](https://github.com/timescale/timescaledb) | Both use time partitioning | You're in a pure-metrics environment with no relational data and need InfluxDB's specialized ingestion path |
| Documents | MongoDB | JSONB | Both use document indexing | Your entire data model is schemaless and you need MongoDB's change streams ecosystem |
| Caching | Redis | UNLOGGED tables | Both use in-memory storage | You depend on pub/sub, sorted sets, Lua scripting, or sub-millisecond latency on complex data structures |
| Queues | Kafka | [pgmq](https://github.com/tembo-io/pgmq) | Both use message queuing | You're streaming events across dozens of services with consumer groups and multi-datacenter replication |
| Geospatial | Specialized GIS | [PostGIS](https://postgis.net/) | Industry standard since 2001 | There's no tradeoff here. PostGIS is the reference implementation. |

The last column is the important part. Those are real, specific requirements you'll recognize because you hit a concrete wall, not because a vendor's marketing team told you to plan for it.

The benchmarks on the extensions that matter most:

* **pgvectorscale** achieved 28x lower p95 latency and 16x higher throughput than Pinecone at 99% recall on a [50M vector benchmark](https://www.tigerdata.com/blog/pgvector-vs-pinecone)
* **TimescaleDB** matches or beats [InfluxDB](https://www.tigerdata.com/blog/what-influxdb-got-wrong) on time-series workloads while giving you full SQL, JOINs, and ACID guarantees
* **pg\_textsearch** runs the [same BM25 ranking algorithm](https://www.tigerdata.com/blog/you-dont-need-elasticsearch-bm25-is-now-in-postgres) that powers Elasticsearch, natively in Postgres

These extensions aren't new. PostGIS has been in production since 2001. TimescaleDB since 2017. pgvector since 2021. Over [48,000 companies](https://www.aventionmedia.com/technology-installed-base/postgresql-customers-list/) run PostgreSQL, including Netflix, Spotify, Uber, and Discord.

So what are you actually paying for with a specialized database? In most cases: a managed service, a purpose-built UI, and the assumption that you'll outgrow Postgres. For the small percentage of teams that genuinely need cluster-scale Elasticsearch or Kafka-grade event streaming, that's a fair trade. For everyone else, it's an infrastructure tax on a problem they don't have.

The Compounding Costs
---------------------

Even when a specialized database has a genuine edge on a specific benchmark, you're paying for it across every other dimension of your infrastructure.

**Cognitive load.** Your team needs SQL, Redis commands, Elasticsearch Query DSL, MongoDB aggregation pipelines, Kafka consumer patterns, and InfluxDB's query language. That's not specialization. That's fragmentation.

**Data consistency.** Keeping Elasticsearch in sync with Postgres means building sync jobs. Those jobs fail silently. Data drifts. You add reconciliation logic. That fails too. Now you're maintaining data plumbing instead of building the product your company actually sells. We've seen this pattern firsthand: a team adds a second database for one workload, then spends six months building and debugging the sync pipeline between them. The second database solved a performance problem. The sync pipeline created three operational ones.

**SLA math.** Three systems at 99.9% uptime each give you 99.7% combined availability. That's 26 hours of downtime per year instead of 8.7. Every additional system multiplies your failure surface.

**Real cost.** [Plexigrid consolidated from four databases to one](https://www.tigerdata.com/blog/from-4-databases-to-1-how-plexigrid-replaced-influxdb-got-350x-faster-queries-tiger-data) and got 350x faster queries. [Flogistix](https://www.tigerdata.com/blog/how-flogistix-by-flowco-reduced-infrastructure-management-costs-by-66-with-tiger-data) cut database costs by 66%. [Latitude](https://www.tigerdata.com/case-studies/latitude) saved $12,000 per month from compression alone. These savings compound because you're removing entire categories of operational complexity.

Start With Postgres
-------------------

Start with one database. Add complexity only when you've earned the need for it.

Postgres with the right extensions handles search, vectors, time-series, documents, caching, queues, geospatial data, and scheduled jobs. The algorithms match their specialized counterparts. The extensions are battle-tested. And the operational simplicity compounds every month you don't add another system to your stack.

In the AI era, that simplicity is worth more than ever. Every agent, every CI pipeline, every on-call engineer benefits from being able to fork one database instead of coordinating seven.

Most teams adopt specialized databases before they've even tested whether Postgres can handle the workload. They add Elasticsearch because "that's what you use for search," not because they tried pg\_textsearch and found it lacking. They add Redis because "everyone uses Redis for caching," not because UNLOGGED tables couldn't handle their load. The "right tool for the right job" advice sounds wise. But too often, it's a solution to a problem you don't have yet, sold by the people who profit from you having it.

Test the assumption first. Then decide.

For a hands-on guide to setting up each extension with working SQL, read the companion post: [Postgres Extensions Cheat Sheet: Replace 7 Databases With SQL](https://www.tigerdata.com/blog/postgres-extensions-cheat-sheet).

All of these extensions come pre-configured on [Tiger Cloud](https://console.cloud.timescale.com). Create a free database and start building.