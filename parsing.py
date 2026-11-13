"""Markdown clipping -> metadata + chunks.

A faithful Python port of the original app's parser and chunker, because chunk
quality is the biggest driver of search quality:

  * markdown-aware: paragraphs, headings and fenced code blocks are never cut
    in the middle (except one gigantic line, which is cut at sentence ends)
  * every chunk remembers its heading breadcrumb ("Full Article > Setup")
  * the text that gets EMBEDDED is  "<title> > <breadcrumb> \n\n <chunk>",
    so a fragment carries the context of the note it came from
  * binary junk and tiny fragments are dropped or merged
"""
import re
import unicodedata

import yaml

import config

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
PLAIN_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
MD_LINK_HEADING_RE = re.compile(r"^#\s+\[(.+?)\]\((\S+?)\)\s*$")
WIKILINK_RE = re.compile(r"^\[\[(.+?)\]\]$")


def blen(s):
    """Length in bytes (the original measures chunk sizes in bytes)."""
    return len(s.encode("utf-8", "replace"))


# ── parsing a whole file ────────────────────────────────────────────────────

class _Loader(yaml.SafeLoader):
    pass


# keep "2026-08-31 12:22:52" as a string instead of turning it into a datetime
_Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def normalize_lines(lines):
    """Strip control characters and trailing whitespace, without moving any line."""
    out = []
    for line in lines:
        line = "".join(c for c in line if c == "\t" or (ord(c) >= 0x20 and ord(c) != 0x7F))
        out.append(line.rstrip(" \t ﻿"))
    return out


def clean_title(s):
    return " ".join(str(s).strip().strip("\"'").split())


def _as_list(v):
    if v is None:
        return []
    items = v if isinstance(v, list) else str(v).split(",")
    out = []
    for e in items:
        s = str(e).strip()
        m = WIKILINK_RE.match(s)
        s = m.group(1) if m else s
        if s and s != "None":
            out.append(s)
    return out


def extract_section(lines, start, name, max_chars):
    """Text under the first heading called `name`, up to the next heading."""
    parts, inside = [], False
    for line in lines[start:]:
        t = line.strip()
        m = PLAIN_HEADING_RE.match(t)
        if m and t.startswith("#"):
            if inside:
                break
            inside = m.group(1).strip().lower() == name
            continue
        if inside and t:
            parts.append(t)
            if sum(len(p) + 1 for p in parts) >= max_chars:
                break
    return " ".join(parts)[:max_chars]


def parse_note(text, fallback_title="note"):
    """-> dict(title, url, source, clipped_at, tags, concepts, summary, lines)

    `lines` is the body (frontmatter removed), normalised, ready for chunk_lines().
    """
    lines = normalize_lines(text.replace("\r\n", "\n").split("\n"))
    fm, body_start = {}, 0
    if lines and lines[0].strip() == "---":
        for i in range(1, min(len(lines), 202)):
            if lines[i].strip() == "---":
                try:
                    fm = yaml.load("\n".join(lines[1:i]), Loader=_Loader) or {}
                except yaml.YAMLError:
                    fm = {}
                fm = fm if isinstance(fm, dict) else {}
                body_start = i + 1
                break
    body = lines[body_start:]

    def s(key):
        v = fm.get(key)
        return "" if v is None else str(v).strip()

    title, url = clean_title(s("title")), s("url") or s("source_url")
    for line in body[:20]:                       # fallbacks: "# [title](url)" line, then any H1
        line = line.strip()
        if not line:
            continue
        m = MD_LINK_HEADING_RE.match(line)
        if m:
            title = title or clean_title(m.group(1))
            url = url or m.group(2)
        elif line.startswith("# ") and not title:
            m = PLAIN_HEADING_RE.match(line)
            title = clean_title(m.group(1)) if m else title
        break
    return {
        "title": title or fallback_title,
        "url": url or None,
        "source": s("source") or None,
        "clipped_at": s("clipped") or s("created") or None,
        "tags": _as_list(fm.get("tags")),
        "concepts": _as_list(fm.get("concepts")),
        "summary": extract_section(body, 0, "digest summary", 2000),
        "lines": body,
    }


# ── chunking ────────────────────────────────────────────────────────────────

def section_kind(heading):
    h = heading.lower().strip()
    if "digest summary" in h:
        return "summary"
    if "discussion summary" in h:
        return "discussion"
    if "full article" in h:
        return "article"
    return ""


def strip_links(s):
    while True:
        i = s.find("](")
        if i < 0:
            break
        j, k = s.rfind("[", 0, i), s.find(")", i)
        if j < 0 or k < 0:
            break
        s = s[:j] + s[j + 1:i] + s[k + 1:]
    return s.strip()


def is_garbage(text):
    """Mostly replacement characters / odd symbols = a binary file pasted as text."""
    total = bad = 0
    for ch in text:
        if ch in "\n \t":
            continue
        total += 1
        if ch == "�" or unicodedata.category(ch)[0] not in "LNPS" or unicodedata.category(ch) in ("No", "Nl") and False:
            bad += 1
    return total >= 20 and bad / total > 0.05


def split_long_text(s, target, mx):
    """Cut one huge line at sentence ends (works on bytes, never splits a character)."""
    b, out = s.encode("utf-8", "replace"), []
    while len(b) > mx:
        cut = -1
        for i in range(target, min(mx, len(b) - 1)):
            if b[i:i + 1] in (b".", b"!", b"?", b";") and b[i + 1:i + 2] in (b" ", b"\t"):
                cut = i + 1
                break
        if cut < 0:
            for i in range(mx - 1, target // 2, -1):
                if b[i:i + 1] in (b" ", b"\t"):
                    cut = i
                    break
        if cut < 0:
            cut = mx
            while cut > 0 and (b[cut] & 0xC0) == 0x80:
                cut -= 1
        out.append(b[:cut].rstrip(b" \t").decode("utf-8", "replace"))
        b = b[cut:].lstrip(b" \t")
    if b.strip():
        out.append(b.decode("utf-8", "replace"))
    return out


def split_blocks(lines):
    """Group lines into ('para'|'heading'|'fence') blocks."""
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = FENCE_RE.match(line)
        if m:
            fence, start, size = m.group(1), i, blen(line)
            i += 1
            while i < n:
                size += blen(lines[i]) + 1
                if lines[i].strip().startswith(fence):
                    break
                i += 1
            i = min(i, n - 1)
            blocks.append(dict(kind="fence", start=start, end=i, size=size))
            i += 1
            continue
        m = HEADING_RE.match(line)
        if m:
            text = m.group(2).strip()
            if not text:                     # the clipper sometimes puts the text on the next line
                for j in range(i + 1, min(i + 4, n)):
                    t = lines[j].strip()
                    if not t:
                        continue
                    if not HEADING_RE.match(lines[j]) and not FENCE_RE.match(lines[j]) and blen(t) <= 120:
                        text = strip_links(t)
                    break
            blocks.append(dict(kind="heading", start=i, end=i, size=blen(line), level=len(m.group(1)), text=text))
            i += 1
            continue
        start, size = i, 0
        while i < n:
            if not lines[i].strip() or HEADING_RE.match(lines[i]) or FENCE_RE.match(lines[i]):
                break
            size += blen(lines[i]) + 1
            i += 1
        blocks.append(dict(kind="para", start=start, end=i - 1, size=size))
    return blocks


class _Packer:
    def __init__(self, lines, target, mx, mn):
        self.lines, self.target, self.max, self.min = lines, target, mx, mn
        self.out, self.headings, self.section = [], [""] * 6, ""
        self.cur_start, self.cur_end, self.cur_size = -1, 0, 0
        self.cur_head = self.cur_sect = ""

    def heading_path(self):
        parts = [h for h in self.headings if h]
        if parts and parts[0].startswith("["):   # the clipper's H1 is the title as a link
            parts = parts[1:]
        return " › ".join(parts)

    def set_heading(self, level, text):
        level = min(max(level, 1), 6)
        self.headings[level - 1] = text
        for l in range(level, 6):
            self.headings[l] = ""
        k = section_kind(text)
        if k:
            self.section = k

    def add(self, b):
        if self.cur_start < 0:
            self.cur_start, self.cur_head, self.cur_sect, self.cur_size = b["start"], self.heading_path(), self.section, 0
        if b["start"] > self.cur_end + 1 and self.cur_size > 0:
            self.cur_size += b["start"] - self.cur_end - 1
        self.cur_end = b["end"]
        self.cur_size += b["size"]

    def flush(self):
        if self.cur_start < 0:
            return
        self.emit(self.cur_start + 1, self.cur_end + 1, "\n".join(self.lines[self.cur_start:self.cur_end + 1]))
        self.cur_start, self.cur_size = -1, 0

    def emit(self, start_line, end_line, text):
        if not text.strip() or is_garbage(text):
            return
        if blen(text.strip()) < self.min and self.out:
            prev = self.out[-1]               # too small alone: glue onto the previous chunk
            verbatim = prev["text"] == "\n".join(self.lines[prev["start_line"] - 1:prev["end_line"]])
            if verbatim and prev["end_line"] < start_line and start_line - prev["end_line"] <= 3:
                merged = "\n".join(self.lines[prev["start_line"] - 1:end_line])
                if not is_garbage(merged) and blen(merged) <= self.max + blen(text) + 8:
                    prev["text"], prev["end_line"] = merged, end_line
                    return
        self.out.append(dict(start_line=start_line, end_line=end_line, section=self._sect(),
                             heading_path=self._head(), text=text))

    def _sect(self):
        return self.cur_sect if self.cur_start >= 0 else self.section

    def _head(self):
        return self.cur_head if self.cur_start >= 0 else self.heading_path()

    def emit_with(self, start_line, end_line, text, head, sect):
        if text.strip() and not is_garbage(text):
            self.out.append(dict(start_line=start_line, end_line=end_line, section=sect,
                                 heading_path=head, text=text))

    def add_oversized(self, b):
        head, sect, start, size = self.heading_path(), self.section, b["start"], 0
        for i in range(b["start"], b["end"] + 1):
            l = blen(self.lines[i]) + 1
            if l > self.max:
                if i > start:
                    self.emit_with(start + 1, i, "\n".join(self.lines[start:i]), head, sect)
                for piece in split_long_text(self.lines[i], self.target, self.max):
                    self.emit_with(i + 1, i + 1, piece, head, sect)
                start, size = i + 1, 0
                continue
            if size + l > self.max and i > start:
                self.emit_with(start + 1, i, "\n".join(self.lines[start:i]), head, sect)
                start, size = i, 0
            size += l
        if start <= b["end"]:
            self.emit_with(start + 1, b["end"] + 1, "\n".join(self.lines[start:b["end"] + 1]), head, sect)


def chunk_lines(lines, target=config.CHUNK_TARGET, mx=config.CHUNK_MAX, mn=config.CHUNK_MIN):
    """Body lines -> list of dicts(text, heading_path, section, start_line, end_line)."""
    p = _Packer(lines, target, mx if mx >= target else target + target // 2, mn)
    for b in split_blocks(lines):
        if b["kind"] == "heading":
            if p.cur_start >= 0 and p.cur_size >= target // 3:
                p.flush()                      # a heading closes a well-filled chunk
            p.set_heading(b["level"], b["text"])
            small = p.cur_start < 0 or p.cur_size < target // 3
            p.add(b)
            if small:
                p.cur_head, p.cur_sect = p.heading_path(), p.section
        else:
            if b["size"] > p.max:
                p.flush()
                p.add_oversized(b)
                continue
            if p.cur_start >= 0 and p.cur_size + b["size"] > p.max:
                p.flush()
            p.add(b)
            if p.cur_size >= target:
                p.flush()
    p.flush()
    return p.out


def collapse_whitespace(text):
    out, blank = [], False
    for line in text.split("\n"):
        t = line.strip()
        if not t:
            if not blank and out:
                out.append("")
            blank = True
            continue
        blank = False
        out.append(t)
    return "\n".join(out).strip()


def embed_text(title, heading_path, text):
    """Exactly what is sent to the embedding model for one chunk."""
    head = f"{title} › {heading_path}" if heading_path else title
    return f"{head}\n\n{collapse_whitespace(text)}"


def note_embed_text(title, summary, concepts, tags):
    """What is embedded for the whole-note vector (title + digest + concepts + tags)."""
    s = title
    if summary:
        s += "\n\n" + summary
    if concepts:
        s += "\n\nConcepts: " + ", ".join(concepts)
    if tags:
        s += "\nTags: " + ", ".join(tags)
    return s
