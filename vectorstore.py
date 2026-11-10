"""ChromaDB wrapper: one persistent collection holding one vector per chunk.

Stored per vector:
  id        "<note_id>:<chunk_index>"   (matches chunks.vector_id in SQLite)
  embedding 768 floats from nomic-embed-text
  document  the chunk text
  metadata  {note_id, slug, title, chunk_index}
Distance metric: cosine (similarity = 1 - distance).
"""
import chromadb

import config

_collection = None


def collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=str(config.CHROMA_DIR))
        _collection = client.get_or_create_collection(
            config.COLLECTION, metadata={"hnsw:space": "cosine"})
    return _collection


def add_chunks(ids, vectors, texts, metadatas):
    collection().upsert(ids=ids, embeddings=vectors, documents=texts, metadatas=metadatas)


def delete_ids(ids):
    if ids:
        collection().delete(ids=ids)


def query(vector, n=30):
    """Nearest chunks to the query vector -> list of dicts, best first."""
    res = collection().query(query_embeddings=[vector], n_results=n)
    return [
        {"vector_id": i, "text": d, "meta": m, "score": 1 - dist}
        for i, d, m, dist in zip(res["ids"][0], res["documents"][0],
                                 res["metadatas"][0], res["distances"][0])
    ]


def count():
    return collection().count()
