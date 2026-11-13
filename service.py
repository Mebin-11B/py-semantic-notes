"""Business logic that keeps SQLite and ChromaDB in step.

Every write goes: SQLite (source of truth) -> chunk -> embed -> ChromaDB.
Chunking (cheap) and embedding (slow) are separate steps so a bulk import can
write all the SQL first and embed afterwards.
"""
import db
import embeddings
import parsing
import vectorstore


def chunk_note(con, note_id):
    """Re-split a note's body into chunk rows. Marks the note 'pending' for embedding."""
    note = con.execute("SELECT title, body FROM notes WHERE id=?", (note_id,)).fetchone()
    lines = parsing.normalize_lines(note["body"].split("\n"))
    db.replace_chunks(con, note_id, parsing.chunks_for(note["title"], lines))


def embed_payload(con, note_id):
    """The texts to embed for one note: every chunk, then the whole-note text (last)."""
    note = con.execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
    chunks = db.chunks_of(con, note_id)
    texts = [parsing.embed_text(note["title"], c["heading_path"], c["text"]) for c in chunks]
    concepts = [c.strip() for c in note["concepts"].split(",") if c.strip()]
    texts.append(parsing.note_embed_text(note["title"], note["summary"], concepts,
                                         db.note_tags(con, note_id)))
    return note, chunks, texts


def store_vectors(con, note, chunks, vectors):
    """Write one note's vectors to ChromaDB (replacing any old ones) and mark it done."""
    vectorstore.delete_note(note["id"], [c["vector_id"] for c in chunks])
    if chunks:
        vectorstore.add_chunks(
            [c["vector_id"] for c in chunks], vectors[:-1], [c["text"] for c in chunks],
            [{"note_id": note["id"], "slug": note["slug"], "title": note["title"],
              "chunk_index": c["chunk_index"]} for c in chunks])
    vectorstore.add_note_vector(note["id"], vectors[-1], note["title"])
    con.execute("UPDATE notes SET embed_state='done' WHERE id=?", (note["id"],))


def embed_note(con, note_id):
    note, chunks, texts = embed_payload(con, note_id)
    store_vectors(con, note, chunks, embeddings.embed_documents(texts))
    return len(chunks)


def index_note(con, note_id):
    chunk_note(con, note_id)
    return embed_note(con, note_id)


def _summary(body):
    return parsing.extract_section(body.split("\n"), 0, "digest summary", 2000)


def create(con, title, body, url=None, source=None, tags=()):
    note_id = db.create_note(con, title, body, url, source, None, tags, summary=_summary(body))
    index_note(con, note_id)
    return note_id


def update(con, note, title, body, url, source, tags):
    changed = db.content_hash(title, body) != note["content_hash"]
    tags_changed = sorted(tags) != sorted(db.note_tags(con, note["id"]))
    db.update_note(con, note["id"], title, body, url, source, tags, _summary(body))
    if changed:                      # text changed: re-chunk and re-embed everything
        index_note(con, note["id"])
    elif tags_changed:               # only the note-level vector includes tags
        embed_note(con, note["id"])


def delete(con, note):
    vectorstore.delete_note(note["id"], db.chunk_vector_ids(con, note["id"]))   # vector DB
    db.delete_note(con, note["id"])                                            # SQL (cascades)
