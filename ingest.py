"""Import the markdown files in notes/ into SQLite + ChromaDB.

    python ingest.py --limit 300     # quick demo subset
    python ingest.py                 # everything (~2400 notes)
    python ingest.py --reset         # wipe both databases first

Safe to re-run: files already imported (same slug) with the same content hash
are skipped, so only new/changed files cost embedding time.
"""
import argparse
import shutil
import time

import config
import db
import parsing
import service


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only import the first N files")
    ap.add_argument("--reset", action="store_true", help="delete data/ first")
    args = ap.parse_args()

    if args.reset and config.DATA_DIR.exists():
        shutil.rmtree(config.DATA_DIR)
    db.init_db()

    files = sorted(config.NOTES_DIR.glob("*.md"))[: args.limit]
    start, added, skipped = time.time(), 0, 0
    with db.connect() as con:
        for n, path in enumerate(files, 1):
            meta, body = parsing.parse_frontmatter(path.read_text(errors="replace"))
            title = meta.get("title") or path.stem
            row = con.execute("SELECT * FROM notes WHERE slug=?", (db.slugify(title),)).fetchone()
            if row and row["content_hash"] == db.content_hash(title, body):
                skipped += 1
                continue
            if row:  # same title, different text: replace
                service.delete(con, row)
            note_id = db.create_note(con, title, body, meta.get("url"), meta.get("source"),
                                     meta.get("clipped"), meta.get("tags", []))
            service.index_note(con, note_id)
            con.commit()
            added += 1
            if n % 25 == 0:
                print(f"{n}/{len(files)}  ({time.time() - start:.0f}s)", flush=True)
    print(f"done: {added} imported, {skipped} skipped, {time.time() - start:.0f}s")


if __name__ == "__main__":
    main()
