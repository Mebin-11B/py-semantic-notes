# PySemantic Notes: everything you need to know

A deliberately small Python clone of *SemanticNotes* (semantic.mebin.in), built as a
DBMS course mini project. It is a **CRUD app over a SQL database** plus a **vector
database** used for **semantic search**. Read this file top to bottom and you can run,
inspect and explain the whole thing.

---

## 1. What the system does

- Stores **notes** (2,369 Obsidian web clippings, copied into `notes/`) in **SQLite**:
  title, URL, source, tags, body text.
- Lets you **Create / Read / Update / Delete** notes in a web UI.
- **Searches** them three ways:
  - **Keyword**: SQL full-text search (SQLite FTS5, stemmed), matches words.
  - **Semantic**: vector database (ChromaDB), matches *meaning* ("cheap models" finds a note about "price per token").
  - **Hybrid** (default): four ranked lists (two SQL, two vector) fused into one ranking. **This is the same ranking pipeline as the original semantic.mebin.in**, ported to Python (see section 4.2 and 4.4).
- A **Status** page shows row counts for SQL and the vector DB side by side, top tags, and recent searches.

What was left out compared with the original (on purpose): login/auth, git sync, and the
LLM "answer with citations" feature. The original is a Go app; this one is Python.

## 2. Tech stack

| Layer | Tech | Why |
|---|---|---|
| Web framework | **Flask** (Jinja2 templates) | smallest Python web stack |
| Relational DB | **SQLite** via the stdlib `sqlite3` | one file, zero setup, plain SQL (no ORM, every query is visible in the code) |
| Full-text search | **SQLite FTS5** | built into SQLite, BM25 ranking |
| Vector DB | **ChromaDB** (embedded, persistent) | Python-native vector DB, stores vectors on disk, HNSW index |
| Embeddings | **Ollama** running `nomic-embed-text` (768 dimensions) | local, free, no API key |
| Front end | plain HTML + CSS, **no JavaScript framework** | `templates/` + `static/style.css` |
| Markdown | `markdown` + `nh3` (sanitiser) | render note bodies safely |

## 3. Project layout

```
app.py              Flask routes (home/search, notes list, view, new, edit, delete, status)
db.py               all SQL: create/update/delete note, tags, chunks
schema.sql          the table definitions (READ THIS FIRST for the DB design)
parsing.py          frontmatter parser + markdown-aware chunker + the text we embed
embeddings.py       text -> 768-number vector (calls Ollama)
vectorstore.py      thin wrapper over ChromaDB (add / delete / query)
service.py          glue: keeps SQLite and ChromaDB consistent on every write
search.py           the ranking pipeline: 4 channels + weighted rank fusion
ingest.py           CLI: import notes/*.md into both databases
inspect_vectors.py  CLI: look inside the vector DB
eval.py             CLI: recall@3 / recall@10 on eval/cases.json (24 real questions)
eval/cases.json     the question set (questions -> note titles that must be found)
config.py           paths and settings
notes/              the Obsidian clippings (markdown, with frontmatter)
data/               GENERATED (git-ignored): notes.db (SQLite) + chroma/ (vector DB)
templates/ static/  HTML and CSS
```

## 4. How it works

### 4.1 Importing a note (`ingest.py`, and the same path when you click "Save")

```
 notes/foo.md
   │ parsing.parse_note()      frontmatter (title, url, source, clipped, tags, concepts) + body
   │                           + the "Digest Summary" section (kept as notes.summary)
   ▼
 SQLite  notes row  +  tags / note_tags rows                          (db.create_note)
   │ parsing.chunks_for()      markdown-aware split, ~1800 chars, with a heading breadcrumb
   ▼
 SQLite  chunks rows  (+ chunks_fts rows, added by a trigger)         (db.replace_chunks)
   │ parsing.embed_text()      "<title> › <breadcrumb>\n\n<chunk text>"
   │ embeddings.embed_documents()   Ollama -> 768 floats per chunk, plus one for the whole note
   ▼
 ChromaDB  note_chunks (one vector per chunk) + note_vectors (one per note)
```

`ingest.py` does this in two phases: (1) parse and chunk every file into SQLite, (2) embed the
notes whose `embed_state` is `pending` (3 parallel requests to Ollama), flipping them to `done`.

**Why these details matter for quality** (all copied from the original app):

- **Chunking respects markdown.** Paragraphs, headings and code fences are never cut in half; a
  heading starts a new chunk once the current one is well filled; chunks have a target of
  1800 characters and a hard max of 2600; tiny fragments are merged into the previous chunk;
  binary junk (a PDF pasted as text) is dropped.
- **Each chunk is embedded together with its context.** The embedded text is
  `Title › Heading breadcrumb` + the chunk. A paragraph that says "it supports three modes" is
  meaningless alone; with the title in front, the embedding knows what "it" is.
- **A second vector per note** (`note_vectors`): title + digest summary + concepts + tags. It
  lets a broad question land on the right *note* even when no single chunk stands out.
- **Notes with no body** (a PDF the clipper could not read) still get one chunk containing the title, so they can be found.
- nomic-embed-text wants task prefixes: documents are embedded as `search_document: ...`, queries as `search_query: ...`.

### 4.2 Searching (`search.py`)

Four ranked lists are produced for a question, then fused:

| Channel | Where | What it ranks |
|---|---|---|
| **lexical** | SQL, `chunks_fts` (FTS5, Porter stemmer, BM25; weights text 1, title 3, heading 2) | chunks containing the question's rare words |
| **title** | SQL, `notes_fts` (title 4, summary 1, concepts 2) | notes *about* the words, even if the body never repeats them |
| **vector** | ChromaDB `note_chunks`, cosine, top 40 | chunks closest in meaning to the question |
| **note** | ChromaDB `note_vectors`, cosine, top 10 | whole notes closest in meaning |

**Weighted Reciprocal Rank Fusion (RRF):** every list gives a candidate `weight / (60 + rank)`,
and the scores add up. A chunk several channels agree on wins, and BM25 scores and cosine
similarities never need to be on the same scale. Weights: vector 1.0; lexical 0.7 to 1.5 (scaled
by how strong the BM25 score is relative to the best hit, because BM25 magnitude encodes
rarity); note and title channels boost chunks already found (x0.8) or contribute the note's
first chunk if none was found (weights 0.9 and 1.1).

**Then chunks are grouped by note:** the note's score is its best chunk plus 12% of each extra
matching chunk (capped at 1.5x the best), so a note matching in several places beats one that
matches once, but a long note cannot drown a short decisive one. Scores are shown relative to the best (1.00).

The query is cleaned for the SQL side: stopwords ("what", "how", "best" ...) are dropped and the
remaining words are OR-ed, so one rare word can carry the match.

Modes in the UI: **hybrid** = all four channels, **semantic** = vector + note only (vector DB
alone), **keyword** = lexical + title only (SQL alone). If Ollama is down, hybrid falls back to keyword with a notice.

### 4.3 Update and delete (`service.py`)

- **Create**: SQL insert, then chunk, embed, add vectors (chunk vectors and the note vector).
- **Update**: SQL update. If the text changed (compares the `content_hash` SHA-256), delete the
  old vectors and re-chunk and re-embed; if only the tags changed, just the note vector is re-embedded (it includes tags); URL/source-only edits cost nothing.
- **Delete**: delete the note's vectors from ChromaDB, then `DELETE FROM notes`; the `chunks` and
  `note_tags` rows disappear through `ON DELETE CASCADE`.
- SQLite is the **source of truth**; ChromaDB can always be rebuilt from it (`python ingest.py --reset`).

### 4.4 Search quality: how it compares with the original

The original (Go + SQLite, semantic.mebin.in) and this clone use the **same embedding model**
(`nomic-embed-text` via Ollama). An earlier version of this clone searched far worse because it
did only one thing: nearest chunk in the vector DB, on naive chunks with no context. Quality came
from the pipeline around the model, which has now been ported. Measured against the running original on this machine,
with the same 2,369 notes:

| | recall@3 | recall@10 |
|---|---|---|
| original app (24-question eval set) | 20/24 | 22/24 |
| this app, **hybrid** | 20/24 | 22/24 |
| this app, keyword only (SQL) | 19/24 | 21/24 |
| this app, semantic only (vector DB) | 18/24 | 20/24 |

Ranking agreement with the original on 96 queries (the 24 eval questions, 40 note titles, 40 natural-language lines from summaries):
**#1 result identical in 100%**, top-3 overlap 99%, top-10 overlap 98%, identical top-10 order in 74%. The rest are small swaps
lower in the list. It is not bit-for-bit identical because ChromaDB's HNSW index is approximate (the original does exact brute-force
cosine) and 7 of 2,369 notes (binary-junk edge cases) chunk slightly differently.

Reproduce it: `python eval.py` (this app, all modes), `python eval.py --original http://127.0.0.1:8090 -v` (also scores the original if it is running locally).
Hybrid beating either half alone is a nice demo point: keyword misses paraphrases, semantic misses exact names, fusion gets both.

## 5. The SQL database (SQLite)

File: `data/notes.db`. Schema: `schema.sql`.

```
 notes 1 ───< note_tags >─── 1 tags        (many-to-many: a note has many tags, a tag has many notes)
   │ 1
   └──< chunks                              (one note has many chunks; chunks.vector_id -> ChromaDB id)
 search_log                                 (standalone audit table)
 chunks_fts                                 (FTS5 over chunk text + note title + heading; filled by a trigger on chunks)
 notes_fts                                  (FTS5 over notes.title/summary/concepts; kept in sync by triggers)
```

| Table | Columns (key ones) | Notes |
|---|---|---|
| `notes` | `id` PK, `slug` UNIQUE, `path` UNIQUE, `title`, `url`, `source`, `clipped_at`, `summary`, `concepts`, `body`, `content_hash`, `embed_state` (CHECK pending/done), timestamps | one row per note |
| `tags` | `id` PK, `name` UNIQUE | each tag name stored once |
| `note_tags` | `(note_id, tag_id)` composite PK, both FKs | junction table for the M:N relation |
| `chunks` | `id` PK, `note_id` FK, `chunk_index`, `section`, `heading_path`, `start_line`, `end_line`, `text`, `vector_id` UNIQUE | `UNIQUE(note_id, chunk_index)` |
| `search_log` | `id`, `query`, `mode`, `n_results`, `created_at` | filled on every search |
| `chunks_fts` | FTS5 over `text`, `title`, `heading`, Porter stemmer | filled by trigger `chunks_ai`, cleared by `chunks_ad` |
| `notes_fts` | FTS5 over `title`, `summary`, `concepts`, Porter stemmer | external-content table + 3 triggers (insert/update/delete) |

Design points for the viva:
- **Normalisation**: tags are in their own table with a junction table (no comma-separated
  tag column), so the schema is in 3NF.
- **Foreign keys with `ON DELETE CASCADE`**: SQLite has them off by default; `db.connect()` runs `PRAGMA foreign_keys = ON`.
- **Indexes**: PKs and UNIQUE constraints create indexes automatically; plus `idx_chunks_note`, `idx_note_tags_tag`, and the FTS5 inverted index.
- **Triggers (5)**: `chunks_ai`/`chunks_ad` keep `chunks_fts` in sync with `chunks`; `notes_ai`/`notes_ad`/`notes_au` keep `notes_fts` in sync with `notes`. A `CHECK` constraint limits `embed_state` to `pending`/`done`.
- **Parameterised queries** (`?` placeholders) everywhere, so there is no SQL injection.

### How to inspect the SQL database yourself

SQLite is one file. Pick any of these:

```bash
# A) Python's built-in shell (works with no installs, from the project folder):
source .venv/bin/activate
python -m sqlite3 data/notes.db
#   (this shell has no .tables/.schema dot-commands; use SQL instead, see below)

# B) The full sqlite3 CLI (recommended; may need installing first):
sudo apt install sqlite3          # Debian/Ubuntu;  macOS: already installed
sqlite3 data/notes.db
sqlite> .tables
sqlite> .schema notes
sqlite> .headers on
sqlite> .mode column

# C) GUI: install "DB Browser for SQLite" and open data/notes.db
```

Handy queries (paste into any of the above):

```sql
-- list tables and their definitions (works in the Python shell too)
SELECT name, type FROM sqlite_master WHERE type IN ('table','view');

-- counts: SQL rows and vectors should match for chunks
SELECT (SELECT COUNT(*) FROM notes) AS notes, (SELECT COUNT(*) FROM tags) AS tags,
       (SELECT COUNT(*) FROM chunks) AS chunks;

-- JOIN across the many-to-many: most used tags
SELECT t.name, COUNT(*) AS n
FROM tags t JOIN note_tags nt ON nt.tag_id = t.id
GROUP BY t.id ORDER BY n DESC LIMIT 10;

-- all tags of one note
SELECT n.title, t.name FROM notes n
JOIN note_tags nt ON nt.note_id = n.id JOIN tags t ON t.id = nt.tag_id
WHERE n.slug = '2025-the-year-in-llms';

-- notes with the most chunks (1-to-many)
SELECT n.title, COUNT(c.id) AS chunks
FROM notes n JOIN chunks c ON c.note_id = n.id
GROUP BY n.id ORDER BY chunks DESC LIMIT 5;

-- full-text search (stemmed: 'databases' also matches 'database'), ranked by BM25
SELECT n.title FROM notes_fts JOIN notes n ON n.id = notes_fts.rowid
WHERE notes_fts MATCH 'database' ORDER BY bm25(notes_fts, 4.0, 1.0, 2.0) LIMIT 5;

-- the best chunks for a word, with their breadcrumb
SELECT c.id, n.title, c.heading_path FROM chunks_fts JOIN chunks c ON c.id = chunks_fts.rowid
JOIN notes n ON n.id = c.note_id WHERE chunks_fts MATCH 'epoll' ORDER BY bm25(chunks_fts, 1.0, 3.0, 2.0) LIMIT 5;

-- notes whose vectors are not up to date yet
SELECT COUNT(*) FROM notes WHERE embed_state = 'pending';

-- what was searched recently
SELECT * FROM search_log ORDER BY id DESC LIMIT 10;
```

## 6. The vector database (ChromaDB)

Folder: `data/chroma/` (a SQLite file `chroma.sqlite3` for metadata plus HNSW index files).
Code: `vectorstore.py`.

**What is stored.** Two *collections*:

`note_chunks`: one record per chunk of every note (about 22,200):

| Field | Example | Meaning |
|---|---|---|
| `id` | `"5:2"` | `"<note_id>:<chunk_index>"`, equals `chunks.vector_id` in SQLite |
| `embedding` | 768 floats, e.g. `[-0.0129, 0.072, ...]` | meaning of `Title › breadcrumb + chunk`, from `nomic-embed-text` |
| `document` | `"The exploit works on both github.dev..."` | the chunk text itself |
| `metadata` | `{note_id: 5, slug: "...", title: "...", chunk_index: 2}` | maps a hit back to SQL rows |

`note_vectors`: one record per note (2,369): `id` = `"<note_id>"`, embedding of *title + digest summary + concepts + tags*,
metadata `{note_id, title}`. Used by the "note" channel of the search.

**Distance metric**: cosine (HNSW configured with `space=cosine`, `ef_construction=200`, `ef_search=400`, `max_neighbors=32`: tuned for accuracy over speed). Similar meaning -> vectors point the same
way -> small cosine distance. Similarity shown in the UI = `1 - distance`.

**How the link to SQL works**: `chunks.vector_id` (SQL) = Chroma `id`; Chroma `metadata.note_id` = `notes.id`; `note_vectors` ids = `notes.id`.
There is no foreign-key enforcement across the two systems, so `service.py` writes both in
the same code path (and the Status page shows the two counts so you can spot drift).

**How the index works (one line for the viva)**: Chroma builds an HNSW graph (Hierarchical
Navigable Small World) for approximate nearest-neighbour search: fast, slightly approximate.
With ~20k vectors this is instant.

### How to inspect the vector DB yourself

```bash
source .venv/bin/activate
python inspect_vectors.py                          # both collections, config, first 3 vectors (shows 768-d embedding)
python inspect_vectors.py --note 2025-the-year-in-llms   # every vector of one note
python inspect_vectors.py --query "stealing tokens"      # nearest chunks + similarity scores
```

Or in a Python REPL:

```python
import vectorstore
col = vectorstore.collection()
col.count()                                           # number of vectors
col.peek(2)                                           # two records
col.get(ids=["5:0"], include=["documents", "metadatas", "embeddings"])
col.get(where={"note_id": 5})                         # all chunks of note 5 (metadata filter)
vectorstore.notes_collection().get(ids=["5"], include=["embeddings", "metadatas"])   # the note-level vector
```

The Status page (`/status`) shows `chunk rows (SQLite)` vs `chunk vectors (ChromaDB)` (should be equal) and `note vectors` (should equal the note count).

## 7. How to run the demo

Prerequisites: Python 3.10+, and [Ollama](https://ollama.com) running locally.

```bash
cd py-semantic-notes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

ollama pull nomic-embed-text          # one-time, ~270 MB; Ollama must be running on :11434

python ingest.py --limit 200          # quick: ~30 seconds, 200 notes
# python ingest.py                    # everything: 2,369 notes, ~7 minutes on a GPU (re-runnable; skips finished notes)

python app.py                         # open http://127.0.0.1:5000
```

Notes on ingest: it prints progress and speed; phase 1 (parse + chunk into SQL) takes seconds, phase 2 (embedding) is the slow part. It is **safe to stop and re-run** (finished notes are skipped, `pending` ones resume); `python ingest.py --reset` deletes `data/` and starts over.
The `--limit` subset is the first N files alphabetically, not random.

### Suggested demo script (5 minutes)

1. **Status page**: show the SQL counts and the vector counts side by side.
2. **Keyword vs semantic vs hybrid**: search `which Linux API tells you when a socket is ready for I/O` in each mode. The result chips (`lexical`, `vector`, `title`, `note`) show which channel found each note. Then run `python eval.py` to show the recall numbers.
3. **CREATE**: "+ New note", write 2 paragraphs about indexes, add tags `dbms, demo`. Search for it semantically.
4. **READ**: open the note; point out "N chunks in vector DB".
5. **UPDATE**: edit the text; explain the hash check and re-embedding.
6. **DELETE**: delete it; check the Status counts both dropped.
7. **Show the databases**: open `data/notes.db` and run the JOIN queries from section 5; run `python inspect_vectors.py --note <slug>`.

## 8. Likely viva questions

- **Why two databases?** SQL is right for structured data, constraints, joins, exact-match and full-text search. A vector DB is right for nearest-neighbour search over embeddings. Each does what the other is bad at.
- **What is an embedding?** A fixed-length list of numbers (768 here) produced by a neural network so that texts with similar meaning land close together in vector space.
- **Why chunk?** One vector per long article is too blurry; chunks give precise matches and let us show the matching passage. We also keep one whole-note vector for broad questions.
- **Why is hybrid better than pure vector search?** Embeddings blur exact names and rare terms ("epoll", "CloudNativePG"); BM25 nails those but misses paraphrases. Fusing ranked lists with RRF gets both. Measured: see 4.4.
- **Why prepend the title to each chunk before embedding?** A chunk alone may not say what it is about; the title and heading breadcrumb give the embedding that context.
- **How do you keep the two DBs consistent?** SQLite is the source of truth; all writes go through `service.py`, which updates both; ChromaDB is rebuildable from SQLite. (No distributed transaction: a crash between the two writes can leave drift; the Status page exposes it and `ingest.py` repairs it.)
- **What is the M:N relation?** notes <-> tags via the `note_tags` junction table.
- **How does `ON DELETE CASCADE` help?** Deleting a note removes its chunk and tag-link rows automatically.
- **What is FTS5 / BM25?** FTS5 is SQLite's inverted-index full-text engine; BM25 is the ranking function (term frequency, rarity, length). We use the Porter stemmer so "databases" matches "database".
- **Where did you use triggers?** Five: they keep the two FTS5 indexes in sync with `notes` and `chunks`.
- **Cosine vs Euclidean?** Cosine compares direction (meaning) and ignores vector length; the standard choice for text embeddings.
- **What is RRF?** Reciprocal Rank Fusion: merge ranked lists by summing `weight/(k+rank)` with k=60; robust because it ignores raw scores.
- **Is HNSW exact?** No, approximate nearest neighbour: much faster at scale, tiny recall loss (we tune `ef_search` high). The original uses exact brute force, which is why top-10 order differs in a few queries.
- **Limits?** No auth, single user, embedding time dominates import, no LLM-written answers, no reranker, approximate (HNSW) vector search.

## 9. Troubleshooting

| Symptom | Fix |
|---|---|
| "Search failed: ... Connection refused" | Ollama isn't running: `ollama serve` (and `ollama pull nomic-embed-text`) |
| Keyword search works, semantic returns nothing | You haven't run `ingest.py`, or it only imported a few notes |
| Status shows chunk rows != vectors, or notes `pending` | Run `python ingest.py` (resumes), or `--reset` for a clean rebuild |
| `sqlite3: command not found` | `sudo apt install sqlite3`, or use `python -m sqlite3 data/notes.db` |
| Start from scratch | `rm -rf data/ && python ingest.py --limit 200` |
