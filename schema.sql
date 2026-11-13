-- PySemantic Notes: relational schema (SQLite).
-- Run automatically by db.init_db(). Inspect with: sqlite3 data/notes.db

PRAGMA foreign_keys = ON;

-- One row per note (an Obsidian clipping).
CREATE TABLE IF NOT EXISTS notes (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    slug         TEXT    NOT NULL UNIQUE,      -- URL-safe id, e.g. "15-years-of-forking"
    path         TEXT    UNIQUE,               -- source file in notes/ (NULL for notes created in the UI)
    title        TEXT    NOT NULL,
    url          TEXT,                         -- original web page (from frontmatter)
    source       TEXT,                         -- e.g. "HackerNews Digest"
    clipped_at   TEXT,                         -- when it was clipped (from frontmatter)
    summary      TEXT    NOT NULL DEFAULT '',  -- the "Digest Summary" section, if the note has one
    concepts     TEXT    NOT NULL DEFAULT '',  -- comma separated, from frontmatter
    body         TEXT    NOT NULL,             -- markdown body, frontmatter stripped
    content_hash TEXT    NOT NULL,             -- sha256 of title+body; detects changes
    embed_state  TEXT    NOT NULL DEFAULT 'pending'
                 CHECK (embed_state IN ('pending', 'done')),   -- vectors up to date?
    created_at   TEXT    NOT NULL DEFAULT (datetime('now')),
    updated_at   TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- Tags: many-to-many with notes through the note_tags junction table.
CREATE TABLE IF NOT EXISTS tags (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS note_tags (
    note_id INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    tag_id  INTEGER NOT NULL REFERENCES tags(id)  ON DELETE CASCADE,
    PRIMARY KEY (note_id, tag_id)
);

-- Each note is split into chunks; each chunk gets one vector in ChromaDB.
-- vector_id is the key into the vector DB ("<note_id>:<chunk_index>").
CREATE TABLE IF NOT EXISTS chunks (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    note_id      INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    chunk_index  INTEGER NOT NULL,
    section      TEXT    NOT NULL DEFAULT '',  -- 'summary' | 'discussion' | 'article' | ''
    heading_path TEXT    NOT NULL DEFAULT '',  -- breadcrumb, e.g. "Full Article › Setup"
    start_line   INTEGER NOT NULL,
    end_line     INTEGER NOT NULL,
    text         TEXT    NOT NULL,
    vector_id    TEXT    NOT NULL UNIQUE,
    UNIQUE (note_id, chunk_index)
);

-- Light audit trail of searches.
CREATE TABLE IF NOT EXISTS search_log (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    query      TEXT NOT NULL,
    mode       TEXT NOT NULL,                  -- 'semantic' | 'keyword' | 'hybrid'
    n_results  INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_chunks_note   ON chunks(note_id, chunk_index);
CREATE INDEX IF NOT EXISTS idx_note_tags_tag ON note_tags(tag_id);

-- ── Full-text indexes (FTS5, with the Porter stemmer: "databases" matches "database") ──

-- One row per CHUNK: text, plus the note's title and the chunk's heading.
-- Filled by trigger from chunks; the title comes from a sub-select on notes.
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    text, title, heading, tokenize = 'porter unicode61'
);
CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
    INSERT INTO chunks_fts(rowid, text, title, heading)
    VALUES (new.id, new.text, (SELECT title FROM notes WHERE id = new.note_id), new.heading_path);
END;
CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
    DELETE FROM chunks_fts WHERE rowid = old.id;
END;

-- One row per NOTE: title, digest summary, concepts. Title words repeated in
-- every chunk row look "common" to BM25, so "find the note about X" needs this.
CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(
    title, summary, concepts, content = 'notes', content_rowid = 'id',
    tokenize = 'porter unicode61'
);
CREATE TRIGGER IF NOT EXISTS notes_ai AFTER INSERT ON notes BEGIN
    INSERT INTO notes_fts(rowid, title, summary, concepts) VALUES (new.id, new.title, new.summary, new.concepts);
END;
CREATE TRIGGER IF NOT EXISTS notes_ad AFTER DELETE ON notes BEGIN
    INSERT INTO notes_fts(notes_fts, rowid, title, summary, concepts) VALUES ('delete', old.id, old.title, old.summary, old.concepts);
END;
CREATE TRIGGER IF NOT EXISTS notes_au AFTER UPDATE ON notes BEGIN
    INSERT INTO notes_fts(notes_fts, rowid, title, summary, concepts) VALUES ('delete', old.id, old.title, old.summary, old.concepts);
    INSERT INTO notes_fts(rowid, title, summary, concepts) VALUES (new.id, new.title, new.summary, new.concepts);
END;
