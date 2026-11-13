"""ChromaDB wrapper: two persistent collections.

  note_chunks   one vector per chunk   id "<note_id>:<chunk_index>"
                document = the chunk text, metadata = {note_id, slug, title, chunk_index}
  note_vectors  one vector per note    id "<note_id>"
                the "what is this note about" vector (title + digest + concepts + tags)

Both: 768-dim embeddings, cosine distance (similarity = 1 - distance).
The HNSW index is configured for accuracy (high ef_search) because at ~20k
vectors the cost is negligible and we want near-exact nearest neighbours.
"""
import chromadb

import config

_client = None
_cols = {}

HNSW = {"space": "cosine", "ef_construction": 200, "ef_search": 400, "max_neighbors": 32}


def collection(name=config.COLLECTION):
    global _client
    if name not in _cols:
        if _client is None:
            _client = chromadb.PersistentClient(path=str(config.CHROMA_DIR))
        _cols[name] = _client.get_or_create_collection(name, configuration={"hnsw": HNSW})
    return _cols[name]


def notes_collection():
    return collection(config.NOTE_COLLECTION)


def add_chunks(ids, vectors, texts, metadatas):
    collection().upsert(ids=ids, embeddings=vectors, documents=texts, metadatas=metadatas)


def add_note_vector(note_id, vector, title):
    notes_collection().upsert(ids=[str(note_id)], embeddings=[vector],
                              metadatas=[{"note_id": note_id, "title": title}])


def delete_note(note_id, chunk_ids):
    if chunk_ids:
        collection().delete(ids=chunk_ids)
    notes_collection().delete(ids=[str(note_id)])


def query_chunks(vector, n=40):
    """Nearest chunks -> [(vector_id, similarity)], best first."""
    return _query(collection(), vector, n)


def query_notes(vector, n=10):
    """Nearest whole-note vectors -> [(note_id_str, similarity)], best first."""
    return _query(notes_collection(), vector, n)


def _query(col, vector, n):
    n = min(n, col.count())
    if n == 0:
        return []
    res = col.query(query_embeddings=[vector], n_results=n, include=["distances"])
    return [(i, 1 - d) for i, d in zip(res["ids"][0], res["distances"][0])]


def count():
    return collection().count()


def note_count():
    return notes_collection().count()
