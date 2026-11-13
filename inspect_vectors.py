"""Peek inside the vector database.

    python inspect_vectors.py                    # summary + first 3 vectors
    python inspect_vectors.py --note <slug>      # all vectors of one note
    python inspect_vectors.py --query "text"     # nearest chunks (shows distances)
"""
import argparse

import db
import embeddings
import vectorstore


def show(ids, docs, metas, embs=None):
    for i, (vid, doc, meta) in enumerate(zip(ids, docs, metas)):
        print(f"\nid        : {vid}")
        print(f"metadata  : {meta}")
        print(f"document  : {doc[:120]!r}...")
        if embs is not None:
            v = embs[i]
            print(f"embedding : {len(v)} floats, first 6 = {[round(float(x), 4) for x in v[:6]]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note")
    ap.add_argument("--query")
    args = ap.parse_args()
    col = vectorstore.collection()
    notes_col = vectorstore.notes_collection()
    print(f"collection '{col.name}': {col.count()} chunk vectors")
    print(f"collection '{notes_col.name}': {notes_col.count()} note vectors (one per note)")
    print(f"configuration: {col.configuration_json}")

    if args.query:
        qvec = embeddings.embed_query(args.query)
        res = col.query(query_embeddings=[qvec], n_results=5, include=["documents", "metadatas", "distances"])
        for vid, doc, meta, dist in zip(res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]):
            print(f"\nsimilarity {1 - dist:.3f}  {vid}  {meta['title']}")
            print("   ", doc[:150].replace("\n", " "))
    elif args.note:
        with db.connect() as con:
            note = db.get_note(con, args.note)
        got = col.get(where={"note_id": note["id"]}, include=["documents", "metadatas", "embeddings"])
        show(got["ids"], got["documents"], got["metadatas"], got["embeddings"])
    else:
        got = col.get(limit=3, include=["documents", "metadatas", "embeddings"])
        show(got["ids"], got["documents"], got["metadatas"], got["embeddings"])


if __name__ == "__main__":
    main()
