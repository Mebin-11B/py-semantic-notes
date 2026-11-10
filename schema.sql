-- PySemantic Notes: relational schema (SQLite).
-- Run automatically by db.init_db(). Inspect with: sqlite3 data/notes.db

PRAGMA foreign_keys = ON;

-- One row per note (an Obsidian clipping).
CREATE TABLE IF NOT EXISTS notes (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    slug         TEXT    NOT NULL UNIQUE,      -- URL-safe id, e.g. "15-years-of-forking"
    title        TEXT    NOT NULL,
    url          TEXT,                         -- original web page (from frontmatter)
    source       TEXT,                         -- e.g. "HackerNews Digest"
    clipped_at   TEXT,                         -- when it was clipped (from frontmatter)
    body         TEXT    NOT NULL,             -- markdown body, frontmatter stripped
    content_hash TEXT    NOT NULL,             -- sha256 of title+body; detects changes
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
-- vector_id is the foreign key into the vector DB ("<note_id>:<chunk_index>").
CREATE TABLE IF NOT EXISTS chunks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    note_id     INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    text        TEXT    NOT NULL,
    vector_id   TEXT    NOT NULL UNIQUE,
    UNIQUE (note_id, chunk_index)
);

-- Light audit trail of searches (a second "relation" to show in the demo).
CREATE TABLE IF NOT EXISTS search_log (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    query      TEXT NOT NULL,
    mode       TEXT NOT NULL,                  -- 'semantic' | 'keyword' | 'hybrid'
    n_results  INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_chunks_note   ON chunks(note_id);
CREATE INDEX IF NOT EXISTS idx_note_tags_tag ON note_tags(tag_id);

-- Full-text index (keyword search) over title + body. Kept in sync by triggers.
CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(
    title, body, content='notes', content_rowid='id'
);

CREATE TRIGGER IF NOT EXISTS notes_ai AFTER INSERT ON notes BEGIN
    INSERT INTO notes_fts(rowid, title, body) VALUES (new.id, new.title, new.body);
END;
CREATE TRIGGER IF NOT EXISTS notes_ad AFTER DELETE ON notes BEGIN
    INSERT INTO notes_fts(notes_fts, rowid, title, body) VALUES ('delete', old.id, old.title, old.body);
END;
CREATE TRIGGER IF NOT EXISTS notes_au AFTER UPDATE ON notes BEGIN
    INSERT INTO notes_fts(notes_fts, rowid, title, body) VALUES ('delete', old.id, old.title, old.body);
    INSERT INTO notes_fts(rowid, title, body) VALUES (new.id, new.title, new.body);
END;
