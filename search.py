"""Three ways to search, all returning one result per note.

keyword  -> SQLite FTS5 (BM25 ranking)             [SQL database]
semantic -> nearest chunks in ChromaDB             [vector database]
hybrid   -> both, merged with Reciprocal Rank Fusion
"""
import html
import re

from markupsafe import Markup

import db
import embeddings
import vectorstore


def _fts_query(q):
    words = re.findall(r"\w+", q)
    return " OR ".join(f'"{w}"' for w in words)


def keyword(con, q, limit=20):
    fts = _fts_query(q)
    if not fts:
        return []
    rows = con.execute(
        "SELECT n.id, n.slug, n.title, n.url, n.source, "
        "snippet(notes_fts, 1, '<mark>', '</mark>', ' … ', 24) AS snippet "
        "FROM notes_fts JOIN notes n ON n.id = notes_fts.rowid "
        "WHERE notes_fts MATCH ? ORDER BY bm25(notes_fts, 5.0, 1.0) LIMIT ?",
        (fts, limit)).fetchall()
    return [dict(r, score=None) for r in rows]


def semantic(con, q, limit=20):
    hits = vectorstore.query(embeddings.embed_query(q), n=limit * 3)
    seen, out = set(), []
    for h in hits:                       # chunks arrive best-first; keep best per note
        nid = h["meta"]["note_id"]
        if nid in seen:
            continue
        seen.add(nid)
        note = con.execute("SELECT id, slug, title, url, source FROM notes WHERE id=?",
                           (nid,)).fetchone()
        if note:
            out.append(dict(note, snippet=h["text"][:300].replace("\n", " ") + " …",
                            score=h["score"]))
    return out[:limit]


def hybrid(con, q, limit=20, k=60):
    merged = {}
    for results in (keyword(con, q, limit), semantic(con, q, limit)):
        for rank, r in enumerate(results):
            entry = merged.setdefault(r["id"], dict(r, rrf=0.0))
            entry["rrf"] += 1.0 / (k + rank + 1)
            if r["score"] is not None:
                entry["score"] = r["score"]
    return sorted(merged.values(), key=lambda r: -r["rrf"])[:limit]


def run(con, q, mode, log=True):
    results = {"keyword": keyword, "semantic": semantic, "hybrid": hybrid}[mode](con, q)
    for r in results:
        # escape everything, then re-enable only the <mark> tags FTS5 added
        r["snippet_html"] = Markup(html.escape(r["snippet"])
                                   .replace("&lt;mark&gt;", "<mark>").replace("&lt;/mark&gt;", "</mark>"))
        r["tags"] = db.note_tags(con, r["id"])
    if log:
        con.execute("INSERT INTO search_log(query, mode, n_results) VALUES (?,?,?)",
                    (q, mode, len(results)))
        con.commit()
    return results
