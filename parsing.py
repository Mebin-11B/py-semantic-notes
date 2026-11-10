"""Turn a markdown file into (metadata, body) and split a body into chunks."""
import re

import config


def parse_frontmatter(text):
    """Tiny YAML-subset parser for the clippings' frontmatter.

    Handles `key: value` lines and `tags:` followed by `  - item` lines.
    Returns (meta_dict, body_without_frontmatter).
    """
    meta = {"tags": []}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end == -1:
        return meta, text
    header, body = text[3:end], text[end + 4:].lstrip("\n")
    key = None
    for line in header.splitlines():
        if re.match(r"^\s+-\s+", line) and key == "tags":
            meta["tags"].append(re.sub(r"^\s+-\s+", "", line).strip().strip("\"'"))
        elif ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip().strip("\"'")
            if key == "tags":
                if val.startswith("["):  # inline list: tags: [a, b]
                    meta["tags"] += [t.strip() for t in val.strip("[]").split(",") if t.strip()]
            else:
                meta[key] = val
    return meta, body


def chunk_text(body, target=config.CHUNK_TARGET):
    """Split on blank lines (paragraphs), then pack paragraphs up to ~target chars.

    Very long paragraphs are cut at sentence boundaries. Simple on purpose.
    """
    pieces = []
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para:
            continue
        while len(para) > target * 1.5:  # oversized paragraph: cut at a sentence end
            cut = para.rfind(". ", 0, target)
            cut = cut + 1 if cut > target // 2 else target
            pieces.append(para[:cut].strip())
            para = para[cut:].strip()
        pieces.append(para)

    chunks, current = [], ""
    for p in pieces:
        if current and len(current) + len(p) > target:
            chunks.append(current)
            current = p
        else:
            current = f"{current}\n\n{p}" if current else p
    if current:
        chunks.append(current)
    return [c for c in chunks if len(c) >= 40] or ([body.strip()] if body.strip() else [])
