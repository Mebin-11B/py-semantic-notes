"""PySemantic Notes: a small Flask app. Run with:  python app.py"""

import markdown
import nh3
from flask import Flask, abort, redirect, render_template, request, url_for

import config
import db
import search
import service
import vectorstore

app = Flask(__name__)
PAGE = 30


@app.template_filter("md")
def render_md(text):
    return nh3.clean(markdown.markdown(text, extensions=["fenced_code", "tables"]))


def split_tags(raw):
    return [t.strip() for t in raw.replace("\n", ",").split(",") if t.strip()]


@app.get("/")
def home():
    q = request.args.get("q", "").strip()
    mode = request.args.get("mode", "hybrid")
    if mode not in ("keyword", "semantic", "hybrid"):
        mode = "hybrid"
    results, error, notice = None, None, None
    with db.connect() as con:
        if q:
            try:
                results, notice = search.run(con, q, mode)
            except Exception as e:  # e.g. Ollama not running
                error = f"Search failed: {e}"
        counts = con.execute("SELECT (SELECT COUNT(*) FROM notes) AS notes, "
                             "(SELECT COUNT(*) FROM tags) AS tags").fetchone()
    return render_template("home.html", q=q, mode=mode, results=results, error=error, notice=notice,
                           counts=counts)


@app.get("/notes")
def notes_list():
    tag = request.args.get("tag")
    page = max(int(request.args.get("page", 1)), 1)
    with db.connect() as con:
        where, args = "", []
        if tag:
            where = ("WHERE n.id IN (SELECT note_id FROM note_tags nt "
                     "JOIN tags t ON t.id=nt.tag_id WHERE t.name=?)")
            args = [tag]
        total = con.execute(f"SELECT COUNT(*) FROM notes n {where}", args).fetchone()[0]
        rows = con.execute(f"SELECT * FROM notes n {where} ORDER BY n.updated_at DESC, n.id DESC "
                           "LIMIT ? OFFSET ?", args + [PAGE, (page - 1) * PAGE]).fetchall()
        notes = [dict(r, tags=db.note_tags(con, r["id"])) for r in rows]
    return render_template("notes.html", notes=notes, tag=tag, page=page, total=total,
                           pages=(total + PAGE - 1) // PAGE)


@app.get("/note/<slug>")
def note_view(slug):
    with db.connect() as con:
        note = db.get_note(con, slug)
        if not note:
            abort(404)
        n_chunks = con.execute("SELECT COUNT(*) FROM chunks WHERE note_id=?", (note["id"],)).fetchone()[0]
        return render_template("note.html", note=note, tags=db.note_tags(con, note["id"]),
                               n_chunks=n_chunks)


@app.route("/new", methods=["GET", "POST"])
def note_new():
    if request.method == "POST":
        title = request.form["title"].strip()
        if not title:
            return render_template("edit.html", note=None, tags="", error="Title is required."), 400
        with db.connect() as con:
            note_id = service.create(con, title, request.form["body"], request.form.get("url") or None,
                                     request.form.get("source") or None, split_tags(request.form["tags"]))
            con.commit()
            slug = con.execute("SELECT slug FROM notes WHERE id=?", (note_id,)).fetchone()[0]
        return redirect(url_for("note_view", slug=slug))
    return render_template("edit.html", note=None, tags="", error=None)


@app.route("/note/<slug>/edit", methods=["GET", "POST"])
def note_edit(slug):
    with db.connect() as con:
        note = db.get_note(con, slug)
        if not note:
            abort(404)
        if request.method == "POST":
            title = request.form["title"].strip() or note["title"]
            service.update(con, note, title, request.form["body"], request.form.get("url") or None,
                           request.form.get("source") or None, split_tags(request.form["tags"]))
            con.commit()
            return redirect(url_for("note_view", slug=slug))
        return render_template("edit.html", note=note, tags=", ".join(db.note_tags(con, note["id"])), error=None)


@app.post("/note/<slug>/delete")
def note_delete(slug):
    with db.connect() as con:
        note = db.get_note(con, slug)
        if not note:
            abort(404)
        service.delete(con, note)
        con.commit()
    return redirect(url_for("notes_list"))


@app.get("/status")
def status():
    with db.connect() as con:
        q = lambda sql: con.execute(sql).fetchall()
        stats = {
            "notes": q("SELECT COUNT(*) FROM notes")[0][0],
            "tags": q("SELECT COUNT(*) FROM tags")[0][0],
            "chunks": q("SELECT COUNT(*) FROM chunks")[0][0],
            "vectors": vectorstore.count(),
            "note_vectors": vectorstore.note_count(),
            "pending": q("SELECT COUNT(*) FROM notes WHERE embed_state='pending'")[0][0],
        }
        top_tags = q("SELECT t.name, COUNT(*) AS n FROM tags t JOIN note_tags nt ON nt.tag_id=t.id "
                     "GROUP BY t.id ORDER BY n DESC LIMIT 15")
        sources = q("SELECT COALESCE(source,'(none)') AS s, COUNT(*) AS n FROM notes GROUP BY s ORDER BY n DESC LIMIT 10")
        recent = q("SELECT query, mode, n_results, created_at FROM search_log ORDER BY id DESC LIMIT 10")
    return render_template("status.html", stats=stats, top_tags=top_tags, sources=sources, recent=recent,
                           model=config.EMBED_MODEL)


if __name__ == "__main__":
    db.init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
