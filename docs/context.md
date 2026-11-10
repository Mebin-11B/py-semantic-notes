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
  - **Keyword**: SQL full-text search (SQLite FTS5), matches exact words.
  - **Semantic**: vector database (ChromaDB), matches *meaning* ("cheap models" finds a note about "price per token").
  - **Hybrid** (default): both, merged into one ranking.
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
parsing.py          frontmatter parser + chunker
embeddings.py       text -> 768-number vector (calls Ollama)
vectorstore.py      thin wrapper over ChromaDB (add / delete / query)
service.py          glue: keeps SQLite and ChromaDB consistent on every write
search.py           keyword / semantic / hybrid search
ingest.py           CLI: import notes/*.md into both databases
inspect_vectors.py  CLI: look inside the vector DB
config.py           paths and settings
notes/              the Obsidian clippings (markdown, with frontmatter)
data/               GENERATED (git-ignored): notes.db (SQLite) + chroma/ (vector DB)
templates/ static/  HTML and CSS
```

## 4. How it works

### 4.1 Importing a note (`ingest.py`, and the same path when you click "Save")

```
 notes/foo.md
   │ parsing.parse_frontmatter()   title, url, source, clipped, tags  + markdown body
   ▼
 SQLite  notes row  +  tags / note_tags rows            (db.create_note)
   │ parsing.chunk_text()          body split into ~1500-character chunks on paragraph breaks
   ▼
 SQLite  chunks rows  (id "<note_id>:<chunk_index>")     (db.replace_chunks)
   │ embeddings.embed_documents()  Ollama turns each chunk into 768 floats
   ▼
 ChromaDB  one vector per chunk, same id                 (vectorstore.add_chunks)
```

Why chunks? An embedding captures the meaning of one piece of text. A 5,000-word article
averaged into one vector gets blurry, so each note is cut into ~1500-char pieces and each
piece is embedded separately. The search returns the best-matching chunk per note.

### 4.2 Searching (`search.py`)

- **keyword**: `SELECT ... FROM notes_fts JOIN notes ... WHERE notes_fts MATCH ? ORDER BY bm25(...)`. Pure SQL.
- **semantic**: embed the query with Ollama (with the prefix `search_query: `), ask ChromaDB for
  the nearest chunks by **cosine distance**, keep the best chunk per note. Shown as `sim 0.68`
  (similarity = 1 - cosine distance).
- **hybrid**: run both, then merge with **Reciprocal Rank Fusion**: each result scores
  `1 / (60 + rank)` in every list it appears in; scores add up; sort descending. Notes found by
  *both* methods float to the top. No score normalisation needed.

### 4.3 Update and delete (`service.py`)

- **Create**: SQL insert, then chunk, embed, add vectors.
- **Update**: SQL update. If the text changed (compares the `content_hash` SHA-256), delete the
  old vectors and re-chunk and re-embed; if only tags/URL changed, no embedding cost.
- **Delete**: delete the note's vectors from ChromaDB, then `DELETE FROM notes`; the `chunks` and
  `note_tags` rows disappear through `ON DELETE CASCADE`.
- SQLite is the **source of truth**; ChromaDB can always be rebuilt from it (`python ingest.py --reset`).

## 5. The SQL database (SQLite)

File: `data/notes.db`. Schema: `schema.sql`.

```
 notes 1 ───< note_tags >─── 1 tags        (many-to-many: a note has many tags, a tag has many notes)
   │ 1
   └──< chunks                              (one note has many chunks; chunks.vector_id -> ChromaDB id)
 search_log                                 (standalone audit table)
 notes_fts                                  (FTS5 virtual table mirroring notes.title/body, kept in sync by triggers)
```

| Table | Columns (key ones) | Notes |
|---|---|---|
| `notes` | `id` PK, `slug` UNIQUE, `title`, `url`, `source`, `clipped_at`, `body`, `content_hash`, `created_at`, `updated_at` | one row per note |
| `tags` | `id` PK, `name` UNIQUE | each tag name stored once |
| `note_tags` | `(note_id, tag_id)` composite PK, both FKs | junction table for the M:N relation |
| `chunks` | `id` PK, `note_id` FK, `chunk_index`, `text`, `vector_id` UNIQUE | `UNIQUE(note_id, chunk_index)` |
| `search_log` | `id`, `query`, `mode`, `n_results`, `created_at` | filled on every search |
| `notes_fts` | FTS5 over `title`, `body` | external-content table + 3 triggers (insert/update/delete) |

Design points for the viva:
- **Normalisation**: tags are in their own table with a junction table (no comma-separated
  tag column), so the schema is in 3NF.
- **Foreign keys with `ON DELETE CASCADE`**: SQLite has them off by default; `db.connect()` runs `PRAGMA foreign_keys = ON`.
- **Indexes**: PKs and UNIQUE constraints create indexes automatically; plus `idx_chunks_note`, `idx_note_tags_tag`, and the FTS5 inverted index.
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

-- full-text search, ranked by BM25
SELECT n.title FROM notes_fts JOIN notes n ON n.id = notes_fts.rowid
WHERE notes_fts MATCH 'kernel' ORDER BY bm25(notes_fts) LIMIT 5;

-- what was searched recently
SELECT * FROM search_log ORDER BY id DESC LIMIT 10;
```

## 6. The vector database (ChromaDB)

Folder: `data/chroma/` (a SQLite file `chroma.sqlite3` for metadata plus HNSW index files).
Code: `vectorstore.py`.

**What is stored.** One *collection* named `note_chunks`. Every chunk of every note is one
record:

| Field | Example | Meaning |
|---|---|---|
| `id` | `"5:2"` | `"<note_id>:<chunk_index>"`, equals `chunks.vector_id` in SQLite |
| `embedding` | 768 floats, e.g. `[-0.0129, 0.072, ...]` | meaning of the chunk, from `nomic-embed-text` |
| `document` | `"The exploit works on both github.dev..."` | the chunk text itself |
| `metadata` | `{note_id: 5, slug: "...", title: "...", chunk_index: 2}` | lets us map a hit back to a SQL row |

**Distance metric**: cosine (`hnsw:space = cosine`). Similar meaning -> vectors point the same
way -> small cosine distance. Similarity shown in the UI = `1 - distance`.

**How the link to SQL works**: `chunks.vector_id` (SQL) = Chroma `id`; Chroma `metadata.note_id` = `notes.id`.
There is no foreign-key enforcement across the two systems, so `service.py` writes both in
the same code path (and the Status page shows the two counts so you can spot drift).

**How the index works (one line for the viva)**: Chroma builds an HNSW graph (Hierarchical
Navigable Small World) for approximate nearest-neighbour search: fast, slightly approximate.
With ~20k vectors this is instant.

### How to inspect the vector DB yourself

```bash
source .venv/bin/activate
python inspect_vectors.py                          # count, metric, first 3 vectors (shows 768-d embedding)
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
```

The Status page (`/status`) also shows `chunk rows (SQLite)` vs `vectors (ChromaDB)`; they should be equal.

## 7. How to run the demo

Prerequisites: Python 3.10+, and [Ollama](https://ollama.com) running locally.

```bash
cd py-semantic-notes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

ollama pull nomic-embed-text          # one-time, ~270 MB; Ollama must be running on :11434

python ingest.py --limit 200          # quick: ~4 minutes, 200 notes
# python ingest.py                    # everything: 2,369 notes, ~50 minutes (re-runnable; skips finished notes)

python app.py                         # open http://127.0.0.1:5000
```

Notes on ingest: it prints progress; it is **safe to stop and re-run** (notes already imported
with identical content are skipped); `python ingest.py --reset` deletes `data/` and starts over.
The `--limit` subset is the first N files alphabetically, not random.

### Suggested demo script (5 minutes)

1. **Status page**: show the SQL counts and the vector counts side by side.
2. **Keyword vs semantic**: search `how do I make LLM calls cheaper` in *Keyword* (few or odd hits) and in *Semantic* (relevant notes with different wording). Then *Hybrid*.
3. **CREATE**: "+ New note", write 2 paragraphs about indexes, add tags `dbms, demo`. Search for it semantically.
4. **READ**: open the note; point out "N chunks in vector DB".
5. **UPDATE**: edit the text; explain the hash check and re-embedding.
6. **DELETE**: delete it; check the Status counts both dropped.
7. **Show the databases**: open `data/notes.db` and run the JOIN queries from section 5; run `python inspect_vectors.py --note <slug>`.

## 8. Likely viva questions

- **Why two databases?** SQL is right for structured data, constraints, joins, exact-match and full-text search. A vector DB is right for nearest-neighbour search over embeddings. Each does what the other is bad at.
- **What is an embedding?** A fixed-length list of numbers (768 here) produced by a neural network so that texts with similar meaning land close together in vector space.
- **Why chunk?** One vector per long article is too blurry; chunks give precise matches and let us show the matching passage.
- **How do you keep the two DBs consistent?** SQLite is the source of truth; all writes go through `service.py`, which updates both; ChromaDB is rebuildable from SQLite. (No distributed transaction: a crash between the two writes can leave drift; the Status page exposes it and `ingest.py` repairs it.)
- **What is the M:N relation?** notes <-> tags via the `note_tags` junction table.
- **How does `ON DELETE CASCADE` help?** Deleting a note removes its chunk and tag-link rows automatically.
- **What is FTS5 / BM25?** FTS5 is SQLite's inverted-index full-text engine; BM25 is the ranking function (term frequency, rarity, length).
- **Cosine vs Euclidean?** Cosine compares direction (meaning) and ignores vector length; the standard choice for text embeddings.
- **What is RRF?** Reciprocal Rank Fusion: merge ranked lists by summing `1/(k+rank)`; robust because it ignores raw scores.
- **Limits?** No auth, single user, embedding time dominates import, hybrid ranking is simple, no LLM answers.

## 9. Troubleshooting

| Symptom | Fix |
|---|---|
| "Search failed: ... Connection refused" | Ollama isn't running: `ollama serve` (and `ollama pull nomic-embed-text`) |
| Keyword search works, semantic returns nothing | You haven't run `ingest.py`, or it only imported a few notes |
| Status shows chunk rows != vectors | Re-run `python ingest.py --reset` |
| `sqlite3: command not found` | `sudo apt install sqlite3`, or use `python -m sqlite3 data/notes.db` |
| Start from scratch | `rm -rf data/ && python ingest.py --limit 200` |
