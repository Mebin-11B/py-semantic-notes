"""Hybrid retrieval: a Python port of the original app's ranking pipeline.

Four ranked candidate lists ("channels") are fused with weighted Reciprocal
Rank Fusion (RRF):

  lexical  SQLite FTS5 over chunk text/title/heading (BM25, stemmed)   [SQL]
  title    SQLite FTS5 over note title/summary/concepts                [SQL]
  vector   nearest chunk vectors in ChromaDB                           [vector DB]
  note     nearest whole-note vectors in ChromaDB                      [vector DB]

RRF: each list gives a candidate  weight / (60 + rank).  Scores add up, so a
chunk that several channels agree on wins. Rank-based, so BM25 scores and
cosine similarities never have to be put on the same scale.

Modes:  hybrid = all four   |   semantic = vector + note   |   keyword = lexical + title
"""
import html
import re

import db
import embeddings
import vectorstore

RRF_K = 60.0
LEXICAL_TOP_K = 40
VECTOR_TOP_K = 40
NOTE_TOP_K = 10
RESULT_LIMIT = 12

STOPWORDS = set("""the and for that this with what whats what's which when where how does did are was were have
has had from about into your you can could would should why who best there their then than some any all not but its
it's our out use using used like just most more one two also between tell know saved save note notes clipped read
pick choose good new want need get say says said i me my a an of to in on is it be as at by or if do vs""".split())


def fts_query(q):
    """Natural-language question -> FTS5 query: quoted tokens, stopwords dropped, OR-ed.

    OR (not AND) so that one rare, discriminating word can carry the match; BM25
    then ranks chunks containing more / rarer words higher.
    """
    terms, every = [], []
    for f in q.split():
        f = f.strip("\"'.,;:!?()[]{}<>").replace('"', "")
        if not f:
            continue
        every.append(f'"{f}"')
        if f.lower() not in STOPWORDS:
            terms.append(f'"{f}"')
    return " OR ".join(terms or every)


def terms_of(q):
    """Content words of the query, used to pick and highlight the snippet."""
    out = []
    for f in re.split(r"[^\w'\-]+", q.lower()):
        f = f.strip("'-_").replace("'", "")
        if len(f) >= 3 and f not in STOPWORDS and f not in out:
            out.append(f)
    return out


def lexical(con, q, limit):
    fq = fts_query(q)
    if not fq:
        return []
    rows = con.execute("SELECT rowid, bm25(chunks_fts, 1.0, 3.0, 2.0) AS s FROM chunks_fts "
                       "WHERE chunks_fts MATCH ? ORDER BY s LIMIT ?", (fq, limit)).fetchall()
    return [(r["rowid"], -r["s"]) for r in rows]        # bm25 is lower-is-better: negate


def title_search(con, q, limit):
    fq = fts_query(q)
    if not fq:
        return []
    rows = con.execute("SELECT rowid, bm25(notes_fts, 4.0, 1.0, 2.0) AS s FROM notes_fts "
                       "WHERE notes_fts MATCH ? ORDER BY s LIMIT ?", (fq, limit)).fetchall()
    return [(r["rowid"], -r["s"]) for r in rows]


def _chunks_by_id(con, ids):
    ids = list(ids)
    if not ids:
        return {}
    rows = con.execute(
        "SELECT c.*, n.slug, n.title, n.url FROM chunks c JOIN notes n ON n.id = c.note_id "
        f"WHERE c.id IN ({','.join('?' * len(ids))})", ids).fetchall()
    return {r["id"]: r for r in rows}


def search(con, q, mode="hybrid"):
    """-> (results, notice). Results: one dict per note, best first, score 0..1."""
    notice = None
    use_lex, use_vec = mode in ("hybrid", "keyword"), mode in ("hybrid", "semantic")
    cands = {}                                   # chunk id -> {score, channels}

    def add(cid, weight, rank, channel):
        c = cands.setdefault(cid, {"score": 0.0, "channels": []})
        c["score"] += weight / (RRF_K + rank)
        if channel not in c["channels"]:
            c["channels"].append(channel)

    title_hits, note_hits = [], []
    if use_lex:
        lex = lexical(con, q, LEXICAL_TOP_K)
        top = lex[0][1] if lex else 0
        for i, (cid, s) in enumerate(lex):
            # BM25's magnitude encodes rarity; keep some of it: top hit weighs 1.5, the tail ~0.7
            add(cid, 0.7 + 0.8 * (s / top) if top > 0 else 1.0, i + 1, "lexical")
        title_hits = [nid for nid, _ in title_search(con, q, NOTE_TOP_K)]
    if use_vec:
        try:
            qvec = embeddings.embed_query(q)
            vec = vectorstore.query_chunks(qvec, VECTOR_TOP_K)
            if vec:
                id_of = {r["vector_id"]: r["id"] for r in con.execute(
                    f"SELECT id, vector_id FROM chunks WHERE vector_id IN ({','.join('?' * len(vec))})",
                    [v for v, _ in vec])}
                for i, (vid, _) in enumerate(vec):
                    if vid in id_of:
                        add(id_of[vid], 1.0, i + 1, "vector")
            note_hits = [int(i) for i, _ in vectorstore.query_notes(qvec, NOTE_TOP_K)]
        except Exception as e:                   # Ollama away: fall back to lexical only
            if mode == "semantic":
                raise
            notice = f"Semantic search unavailable ({str(e)[:100]}); showing keyword results."
    if not cands and not note_hits and not title_hits:
        return [], notice

    chunk_map = _chunks_by_id(con, cands)
    by_note = {}
    for c in chunk_map.values():
        by_note.setdefault(c["note_id"], []).append(c["id"])

    # Note-level channels: a retrieved chunk whose note ranked as a whole gets a bonus;
    # a top note with no retrieved chunk contributes its first chunk (often the summary),
    # so broad or title-shaped questions still surface the right note.
    for name, weight, ranks in (("note", 0.9, note_hits), ("title", 1.1, title_hits)):
        for rank, note_id in enumerate(ranks, 1):
            if note_id in by_note:
                for cid in by_note[note_id]:
                    add(cid, weight * 0.8, rank, name)
                continue
            first = con.execute(
                "SELECT c.*, n.slug, n.title, n.url FROM chunks c JOIN notes n ON n.id=c.note_id "
                "WHERE c.note_id=? ORDER BY c.chunk_index LIMIT 1", (note_id,)).fetchone()
            if first:
                chunk_map[first["id"]] = first
                by_note[note_id] = [first["id"]]
                add(first["id"], weight, rank, name)

    hits = sorted(((cid, c) for cid, c in cands.items() if cid in chunk_map),
                  key=lambda h: (-h[1]["score"], h[0]))
    return group_by_note(con, chunk_map, hits, terms_of(q)), notice


def group_by_note(con, chunk_map, hits, terms):
    """Fold chunk hits into one row per note (extra matching chunks add a little)."""
    agg, order = {}, []
    for cid, h in hits:
        ch = chunk_map[cid]
        a = agg.get(ch["note_id"])
        if a is None:
            a = agg[ch["note_id"]] = {"best": ch, "best_score": h["score"], "score": h["score"],
                                      "n": 0, "channels": set()}
            order.append(ch["note_id"])
        a["n"] += 1
        if a["n"] > 1 and a["score"] < 1.5 * a["best_score"]:
            a["score"] += 0.12 * h["score"]   # never more than half again the best chunk
        a["channels"].update(h["channels"])
    out = []
    for nid in order:
        a, ch = agg[nid], agg[nid]["best"]
        out.append({
            "id": nid, "slug": ch["slug"], "title": ch["title"], "url": ch["url"],
            "section": ch["section"], "heading": ch["heading_path"], "matched": a["n"],
            "channels": sorted(a["channels"]), "score": a["score"],
            "snippet": snippet(ch["text"], terms), "tags": db.note_tags(con, nid)})
    out.sort(key=lambda r: -r["score"])           # stable: ties keep best-chunk order
    out = out[:RESULT_LIMIT]
    if out:
        top = out[0]["score"]
        for r in out:
            r["score"] /= top
    return out


# ── snippets ────────────────────────────────────────────────────────────────

def strip_markdown(s):
    s = re.sub(r"<!--.*?-->|<!--.*$|^.*?-->", " ", s)
    s = re.sub(r"!\[[^\]]*\]", " ", s)
    s = re.sub(r"\(\s*https?://[^)\s]*\)?", "", s)
    s = re.sub(r"https?://\S+", "", s)
    for a in ("**", "__", "`", "> ", "# ", "[[", "]]", "[", "]"):
        s = s.replace(a, "")
    s = re.sub(r"(^|\s)([*\-+]|\d+\.)\s+", " ", s)
    s = re.sub(r"(^|\s)#+\s*", " ", s)
    if s.count("|") >= 3:
        s = s.replace("|", " ").replace("---", " ")
    return re.sub(r"\s+", " ", s).strip()


def snippet(text, terms, width=240):
    """A window of the chunk around the first query term, as HTML with <mark>s."""
    lower = text.lower()
    best = min((i for i in (lower.find(t) for t in terms) if i >= 0), default=0)
    start = max(best - width // 3, 0)
    while 0 < start < len(text) and not text[start].isspace():
        start -= 1
    end = min(start + width, len(text))
    while end < len(text) and not text[end].isspace():
        end += 1
    s = strip_markdown(re.sub(r"\s+", " ", text[start:end]))
    s = ("…" if start > 0 else "") + s + ("…" if end < len(text) else "")
    s = html.escape(s)
    if terms:
        s = re.sub(r"(?i)\b(" + "|".join(re.escape(t) for t in terms) + r")\w*", r"<mark>\g<0></mark>", s)
    return s


def run(con, q, mode, log=True):
    """Search and (optionally) record it in search_log. -> (results, notice)"""
    results, notice = search(con, q, mode)
    if log:
        con.execute("INSERT INTO search_log(query, mode, n_results) VALUES (?,?,?)",
                    (q, mode, len(results)))
        con.commit()
    return results, notice
