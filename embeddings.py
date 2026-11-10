"""Text -> vector, using a local Ollama server (model: nomic-embed-text, 768 dims)."""
import requests

import config


def _embed(texts):
    r = requests.post(f"{config.OLLAMA_URL}/api/embed",
                      json={"model": config.EMBED_MODEL, "input": texts}, timeout=300)
    r.raise_for_status()
    return r.json()["embeddings"]


def embed_documents(texts, batch=32):
    out = []
    for i in range(0, len(texts), batch):
        # long chunks are truncated: nomic's context window is limited
        out += _embed([config.DOC_PREFIX + t[:6000] for t in texts[i:i + batch]])
    return out


def embed_query(text):
    return _embed([config.QUERY_PREFIX + text])[0]
