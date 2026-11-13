# PySemantic Notes

A small Python clone of [SemanticNotes](https://semantic.mebin.in): a CRUD notes app with a
**SQLite** database (notes, tags, chunks, full-text index) and a **ChromaDB** vector database
for **semantic search**. Built for a DBMS course mini project.

**Stack:** Flask · SQLite (+FTS5) · ChromaDB · Ollama (`nomic-embed-text`) · plain HTML/CSS

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ollama pull nomic-embed-text      # Ollama must be running
python ingest.py --limit 200      # import 200 of the 2,369 notes (~30 s); omit --limit for all (~7 min with a GPU)
python app.py                     # http://127.0.0.1:5000
python eval.py                    # recall@3/@10 of keyword / semantic / hybrid search
```

**Full documentation (architecture, schema, how to inspect both databases, demo script,
viva Q&A): [`docs/context.md`](docs/context.md).**
