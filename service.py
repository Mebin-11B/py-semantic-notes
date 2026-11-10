"""Business logic that keeps SQLite and ChromaDB in step.

Every write goes: SQLite (source of truth) -> chunk -> embed -> ChromaDB.
"""
import db
import embeddings
import parsing
import vectorstore


def index_note(con, note_id):
    """(Re)build the chunks + vectors of one note from its current body."""
    note = con.execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
    vectorstore.delete_ids(db.chunk_vector_ids(con, note_id))      # drop old vectors
    texts = parsing.chunk_text(f"{note['title']}\n\n{note['body']}")
    ids = db.replace_chunks(con, note_id, texts)                   # new SQL rows
    vectors = embeddings.embed_documents(texts)
    metas = [{"note_id": note_id, "slug": note["slug"], "title": note["title"],
              "chunk_index": i} for i in range(len(texts))]
    vectorstore.add_chunks(ids, vectors, texts, metas)             # new vectors
    return len(texts)


def create(con, title, body, url=None, source=None, tags=()):
    note_id = db.create_note(con, title, body, url, source, None, tags)
    index_note(con, note_id)
    return db.get_note(con, db.slugify(title)) or con.execute(
        "SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()


def update(con, note, title, body, url, source, tags):
    changed = db.content_hash(title, body) != note["content_hash"]
    db.update_note(con, note["id"], title, body, url, source, tags)
    if changed:                      # only pay for embedding when the text changed
        index_note(con, note["id"])


def delete(con, note):
    vectorstore.delete_ids(db.chunk_vector_ids(con, note["id"]))   # vector DB
    db.delete_note(con, note["id"])                                # SQL (cascades)
