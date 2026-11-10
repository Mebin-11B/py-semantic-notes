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
    print(f"collection '{col.name}': {col.count()} vectors, metric = {col.metadata}")

    if args.query:
        for h in vectorstore.query(embeddings.embed_query(args.query), n=5):
            print(f"\nsimilarity {h['score']:.3f}  {h['vector_id']}  {h['meta']['title']}")
            print("   ", h["text"][:150].replace("\n", " "))
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
