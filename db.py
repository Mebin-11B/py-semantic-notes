"""SQLite access layer: plain SQL, no ORM, so every query is visible."""
import hashlib
import re
import sqlite3

import config


def connect():
    config.DATA_DIR.mkdir(exist_ok=True)
    con = sqlite3.connect(config.SQLITE_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db():
    with connect() as con:
        con.executescript((config.ROOT / "schema.sql").read_text())


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:80] or "note"


def content_hash(title, body):
    return hashlib.sha256((title + "\n" + body).encode()).hexdigest()


def unique_slug(con, title):
    base, slug, n = slugify(title), slugify(title), 2
    while con.execute("SELECT 1 FROM notes WHERE slug=?", (slug,)).fetchone():
        slug = f"{base}-{n}"
        n += 1
    return slug


def set_tags(con, note_id, tags):
    """Replace a note's tags (upserts into tags, rewrites note_tags rows)."""
    con.execute("DELETE FROM note_tags WHERE note_id=?", (note_id,))
    for name in dict.fromkeys(t.strip() for t in tags if t.strip()):
        con.execute("INSERT OR IGNORE INTO tags(name) VALUES (?)", (name,))
        tag_id = con.execute("SELECT id FROM tags WHERE name=?", (name,)).fetchone()[0]
        con.execute("INSERT INTO note_tags(note_id, tag_id) VALUES (?,?)", (note_id, tag_id))


def create_note(con, title, body, url=None, source=None, clipped_at=None, tags=()):
    slug = unique_slug(con, title)
    cur = con.execute(
        "INSERT INTO notes(slug,title,url,source,clipped_at,body,content_hash) VALUES (?,?,?,?,?,?,?)",
        (slug, title, url, source, clipped_at, body, content_hash(title, body)),
    )
    set_tags(con, cur.lastrowid, tags)
    return cur.lastrowid


def update_note(con, note_id, title, body, url, source, tags):
    con.execute(
        "UPDATE notes SET title=?, body=?, url=?, source=?, content_hash=?, "
        "updated_at=datetime('now') WHERE id=?",
        (title, body, url, source, content_hash(title, body), note_id),
    )
    set_tags(con, note_id, tags)


def delete_note(con, note_id):
    # chunks, note_tags rows go away through ON DELETE CASCADE
    con.execute("DELETE FROM notes WHERE id=?", (note_id,))


def get_note(con, slug):
    return con.execute("SELECT * FROM notes WHERE slug=?", (slug,)).fetchone()


def note_tags(con, note_id):
    rows = con.execute(
        "SELECT t.name FROM tags t JOIN note_tags nt ON nt.tag_id=t.id "
        "WHERE nt.note_id=? ORDER BY t.name", (note_id,))
    return [r["name"] for r in rows]


def replace_chunks(con, note_id, texts):
    """Rewrite a note's chunk rows. Returns the vector ids (one per chunk)."""
    con.execute("DELETE FROM chunks WHERE note_id=?", (note_id,))
    ids = []
    for i, text in enumerate(texts):
        vid = f"{note_id}:{i}"
        con.execute("INSERT INTO chunks(note_id,chunk_index,text,vector_id) VALUES (?,?,?,?)",
                    (note_id, i, text, vid))
        ids.append(vid)
    return ids


def chunk_vector_ids(con, note_id):
    return [r[0] for r in con.execute("SELECT vector_id FROM chunks WHERE note_id=?", (note_id,))]
