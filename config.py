"""All settings in one place."""
from pathlib import Path

ROOT = Path(__file__).parent
NOTES_DIR = ROOT / "notes"            # the copied Obsidian clippings (.md files)
DATA_DIR = ROOT / "data"              # generated: SQLite file + Chroma folder
SQLITE_PATH = DATA_DIR / "notes.db"
CHROMA_DIR = DATA_DIR / "chroma"
COLLECTION = "note_chunks"

OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"      # 768-dimensional embeddings
DOC_PREFIX = "search_document: "      # nomic wants task prefixes
QUERY_PREFIX = "search_query: "

CHUNK_TARGET = 1800                   # chars per chunk (~450 tokens); same as the original
CHUNK_MAX = 2600
CHUNK_MIN = 40
