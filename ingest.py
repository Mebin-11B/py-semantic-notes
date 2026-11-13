"""Import the markdown files in notes/ into SQLite + ChromaDB.

    python ingest.py --limit 200     # quick demo subset
    python ingest.py                 # everything (~2400 notes)
    python ingest.py --reset         # wipe both databases first

Two phases, so you can watch each one:
  1. parse + chunk every file into SQLite   (seconds)   -> notes.embed_state = 'pending'
  2. embed pending notes, write ChromaDB    (slow part) -> notes.embed_state = 'done'

Safe to stop and re-run: finished notes are skipped, pending ones resume.
"""
import argparse
import shutil
import time
from concurrent.futures import ThreadPoolExecutor

import config
import db
import embeddings
import parsing
import service


def import_files(con, files):
    added = skipped = 0
    for path in files:
        p = parsing.parse_note(path.read_text(errors="replace"), fallback_title=path.stem)
        body = "\n".join(p["lines"])
        rel = path.name
        row = con.execute("SELECT * FROM notes WHERE path=?", (rel,)).fetchone()
        if row and row["content_hash"] == db.content_hash(p["title"], body):
            skipped += 1
            continue
        if row:                                   # file changed since last import: replace the note
            service.delete(con, row)
        note_id = db.create_note(con, p["title"], body, p["url"], p["source"], p["clipped_at"],
                                 p["tags"], p["summary"], p["concepts"], path=rel)
        db.replace_chunks(con, note_id, parsing.chunks_for(p["title"], p["lines"]))
        added += 1
    con.commit()
    return added, skipped


def embed_pending(con, workers=3):
    pending = [r[0] for r in con.execute("SELECT id FROM notes WHERE embed_state='pending' ORDER BY id")]
    if not pending:
        return 0
    start = time.time()

    def work(note_id):                            # runs in a thread: only talks to Ollama
        with db.connect() as c:
            note, chunks, texts = service.embed_payload(c, note_id)
        return note, chunks, embeddings.embed_documents(texts)

    with ThreadPoolExecutor(workers) as pool:     # results come back in order; we write sequentially
        for n, (note, chunks, vectors) in enumerate(pool.map(work, pending), 1):
            service.store_vectors(con, note, chunks, vectors)
            con.commit()
            if n % 25 == 0 or n == len(pending):
                rate = n / (time.time() - start)
                print(f"embedded {n}/{len(pending)}  ({rate:.1f} notes/s, "
                      f"~{(len(pending) - n) / rate / 60:.0f} min left)", flush=True)
    return len(pending)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only import the first N files")
    ap.add_argument("--reset", action="store_true", help="delete data/ first")
    ap.add_argument("--workers", type=int, default=3, help="parallel embedding requests")
    args = ap.parse_args()

    if args.reset and config.DATA_DIR.exists():
        shutil.rmtree(config.DATA_DIR)
    db.init_db()
    files = sorted(config.NOTES_DIR.glob("*.md"))[: args.limit]
    with db.connect() as con:
        t = time.time()
        added, skipped = import_files(con, files)
        print(f"phase 1: {added} notes parsed + chunked, {skipped} unchanged ({time.time() - t:.0f}s)")
        n_pending = con.execute("SELECT COUNT(*) FROM notes WHERE embed_state='pending'").fetchone()[0]
        print(f"phase 2: embedding {n_pending} notes")
        embed_pending(con, args.workers)
    print("done")


if __name__ == "__main__":
    main()
