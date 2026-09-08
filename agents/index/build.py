"""Build the Pulse index from the Markdown corpus.

    python -m agents.index.build [--full] [--no-embeddings] [--db PATH]

The Markdown under ``web/src/content/`` is the source of truth; this reads it and
writes a derived SQLite file that can be deleted and rebuilt at will. Work is
incremental by content hash, so a nightly run re-embeds only the ~30 documents
that actually changed rather than all ~2,950.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sqlite3
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from agents.index import COLLECTIONS, CONTENT_ROOT, DEFAULT_DB_PATH, REPO_ROOT, SCHEMA_PATH
from agents.index.symbols import extract_symbols
from agents.tools.frontmatter import load_frontmatter

logger = logging.getLogger(__name__)


def connect(db_path: Path) -> sqlite3.Connection:
    """Open *db_path*, applying the schema and enabling FK cascades."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    # Off by default in SQLite; without it the ON DELETE CASCADE on symbols and
    # embeddings silently does nothing and stale rows accumulate on re-index.
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    return conn


def _iso_date(value: object) -> str:
    """Normalise a frontmatter date to ``YYYY-MM-DD`` for lexical comparison."""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and value:
        # Frontmatter is day-granular, but tolerate a full timestamp.
        return value.strip()[:10]
    return ""


def _as_list(value: object) -> list:
    return value if isinstance(value, list) else []


def _authors(fm: dict) -> list[str]:
    """Every human named on a document — author/proposer plus thread participants."""
    names: list[str] = []
    for key in ("author", "proposer"):
        value = fm.get(key)
        if isinstance(value, str) and value.strip():
            names.append(value.strip())
    for exchange in _as_list(fm.get("exchanges")):
        if isinstance(exchange, dict):
            name = exchange.get("author")
            if isinstance(name, str) and name.strip():
                names.append(name.strip())
    # Preserve first-seen order; the proposer should stay first.
    return list(dict.fromkeys(names))


def _search_text(fm: dict, body: str) -> str:
    """Assemble the text that FTS5 actually indexes.

    Everything a reader would search by goes in — including the *original*
    mailing-list subject, which often carries the exact `[PATCH v3 4/8]` phrasing
    someone is trying to find again, and the glossary terms, which are where the
    subsystem jargon is spelled out.
    """
    parts: list[str] = []
    for key in ("headline", "title", "tldr", "subsystem", "project", "primer_expert"):
        value = fm.get(key)
        if isinstance(value, str):
            parts.append(value)
    parts.extend(str(t) for t in _as_list(fm.get("tags")))
    parts.extend(str(t) for t in _as_list(fm.get("technical_tradeoffs")))
    for entry in _as_list(fm.get("primer_glossary")):
        if isinstance(entry, dict):
            parts.append(f"{entry.get('term', '')} {entry.get('definition', '')}")
    for exchange in _as_list(fm.get("exchanges")):
        if isinstance(exchange, dict):
            parts.append(str(exchange.get("position", "")))
            parts.append(str(exchange.get("quote") or ""))
    parts.append(body)
    return "\n".join(p for p in parts if p).strip()


def _relative_path(path: Path, content_root: Path) -> str:
    """Stable, portable id for a document.

    Repo-relative when the file lives in the repo (the normal case, and what
    makes the id survive a clone at a different absolute path). Falls back to
    content-root-relative for an out-of-tree --content-root, which is how the
    tests and any external corpus are indexed.
    """
    for base in (REPO_ROOT, content_root.parent, content_root):
        try:
            return str(path.relative_to(base))
        except ValueError:
            continue
    return str(path)


def parse_document(path: Path, kind: str, content_root: Path = CONTENT_ROOT) -> dict | None:
    """Parse one Markdown file into a row dict, or None if unusable."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.warning("index: cannot read %s: %s", path, exc)
        return None

    parsed = load_frontmatter(text)
    if parsed is None:
        logger.warning("index: missing or malformed frontmatter in %s", path)
        return None
    fm, body = parsed

    body = body.strip()
    search_text = _search_text(fm, body)
    return {
        "path": _relative_path(path, content_root),
        "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "kind": kind,
        "project": str(fm.get("project") or ""),
        "subsystem": str(fm.get("subsystem") or ""),
        "commit_hash": fm.get("commit_hash") or None,
        "discussion_id": fm.get("discussion_id") or None,
        "series_id": fm.get("series_id") or None,
        "outcome": fm.get("outcome") or None,
        "impact_score": fm.get("impact_score") if isinstance(fm.get("impact_score"), int) else None,
        "sentiment_score": fm.get("sentiment_score") if isinstance(fm.get("sentiment_score"), int) else None,
        "breaking_change": int(bool(fm.get("breaking_change"))),
        "performance_win": int(bool(fm.get("performance_win"))),
        "is_stub": int(bool(fm.get("is_stub"))),
        "tags": json.dumps([str(t) for t in _as_list(fm.get("tags"))]),
        "authors": json.dumps(_authors(fm)),
        "headline": str(fm.get("headline") or fm.get("title") or ""),
        "tldr": str(fm.get("tldr") or ""),
        "body": body,
        "search_text": search_text,
        "url": str(fm.get("url") or ""),
        "date": _iso_date(fm.get("date")),
    }


_COLUMNS = (
    "path", "content_hash", "kind", "project", "subsystem", "commit_hash",
    "discussion_id", "series_id", "outcome", "impact_score", "sentiment_score",
    "breaking_change", "performance_win", "is_stub", "tags", "authors",
    "headline", "tldr", "body", "search_text", "url", "date",
)


def _upsert(conn: sqlite3.Connection, row: dict) -> int:
    """Insert or update one document row, returning its id."""
    placeholders = ", ".join("?" for _ in _COLUMNS)
    assignments = ", ".join(f"{c}=excluded.{c}" for c in _COLUMNS if c != "path")
    cursor = conn.execute(
        f"INSERT INTO docs ({', '.join(_COLUMNS)}) VALUES ({placeholders}) "
        f"ON CONFLICT(path) DO UPDATE SET {assignments}",
        [row[c] for c in _COLUMNS],
    )
    if cursor.lastrowid:
        existing = conn.execute("SELECT id FROM docs WHERE path = ?", (row["path"],)).fetchone()
        return int(existing["id"])
    return int(conn.execute("SELECT id FROM docs WHERE path = ?", (row["path"],)).fetchone()["id"])


def _reindex_doc(conn: sqlite3.Connection, doc_id: int, row: dict) -> None:
    """Replace the FTS and symbol rows for one document."""
    conn.execute("DELETE FROM docs_fts WHERE doc_id = ?", (doc_id,))
    conn.execute(
        "INSERT INTO docs_fts (doc_id, search_text) VALUES (?, ?)",
        (doc_id, row["search_text"]),
    )
    conn.execute("DELETE FROM symbols WHERE doc_id = ?", (doc_id,))
    conn.executemany(
        "INSERT OR IGNORE INTO symbols (doc_id, symbol, display, kind) VALUES (?, ?, ?, ?)",
        [(doc_id, sym, display, kind) for sym, display, kind in extract_symbols(row["search_text"])],
    )
    # The document text changed, so any stored vector is now for the old text.
    conn.execute("DELETE FROM embeddings WHERE doc_id = ?", (doc_id,))


def iter_documents(content_root: Path):
    """Yield ``(path, kind)`` for every digest Markdown file, in stable order."""
    for directory, kind in COLLECTIONS.items():
        for path in sorted((content_root / directory).glob("*.md")):
            yield path, kind


def build_index(
    db_path: Path = DEFAULT_DB_PATH,
    content_root: Path = CONTENT_ROOT,
    *,
    full: bool = False,
    embeddings: bool = True,
) -> dict:
    """Build or refresh the index. Returns a summary dict."""
    if full and db_path.exists():
        db_path.unlink()

    conn = connect(db_path)
    seen_paths: set[str] = set()
    indexed = skipped = 0
    changed_ids: list[int] = []

    try:
        existing = {
            r["path"]: (r["id"], r["content_hash"])
            for r in conn.execute("SELECT id, path, content_hash FROM docs")
        }

        for path, kind in iter_documents(content_root):
            row = parse_document(path, kind, content_root)
            if row is None:
                continue
            seen_paths.add(row["path"])
            prior = existing.get(row["path"])
            if prior and prior[1] == row["content_hash"]:
                skipped += 1
                continue
            doc_id = _upsert(conn, row)
            _reindex_doc(conn, doc_id, row)
            changed_ids.append(doc_id)
            indexed += 1

        # Files deleted or renamed upstream (the purge workflow does this) must
        # not linger as phantom search hits.
        removed = [p for p in existing if p not in seen_paths]
        conn.executemany("DELETE FROM docs WHERE path = ?", [(p,) for p in removed])
        for p in removed:
            conn.execute("DELETE FROM docs_fts WHERE doc_id = ?", (existing[p][0],))

        conn.commit()

        embedded = 0
        if embeddings:
            embedded = embed_missing(conn)

        _write_meta(conn, embeddings_enabled=embeddings)
        conn.commit()
    finally:
        conn.close()

    return {
        "indexed": indexed,
        "skipped": skipped,
        "removed": len(removed),
        "embedded": embedded,
        "db_path": str(db_path),
    }


def embed_missing(conn: sqlite3.Connection, provider=None) -> int:
    """Embed every document that has no current vector. Returns the count."""
    rows = conn.execute(
        "SELECT d.id, d.headline, d.tldr, d.subsystem, d.body FROM docs d "
        "LEFT JOIN embeddings e ON e.doc_id = d.id WHERE e.doc_id IS NULL"
    ).fetchall()
    if not rows:
        return 0

    if provider is None:
        from agents.index.embed import build_provider

        provider = build_provider()
    from agents.index.embed import pack_vector

    # Lead with subsystem and headline: the embedding should capture "what area
    # of the toolchain is this and what happened", not the prose style.
    texts = [
        f"{r['subsystem']} — {r['headline']}\n{r['tldr']}\n{r['body']}"[:8000] for r in rows
    ]
    logger.info("Embedding %d documents with %s", len(texts), provider.model)
    vectors = provider.embed(texts)

    conn.executemany(
        "INSERT OR REPLACE INTO embeddings (doc_id, model, dim, vector) VALUES (?, ?, ?, ?)",
        [
            (int(row["id"]), provider.model, len(vec), pack_vector(vec))
            for row, vec in zip(rows, vectors)
        ],
    )
    conn.commit()
    return len(vectors)


def _write_meta(conn: sqlite3.Connection, *, embeddings_enabled: bool) -> None:
    """Record corpus coverage so the server can describe (and distrust) itself."""
    stats = conn.execute(
        "SELECT COUNT(*) n, MIN(NULLIF(date,'')) lo, MAX(date) hi FROM docs"
    ).fetchone()
    published = conn.execute("SELECT COUNT(*) n FROM docs WHERE is_stub = 0").fetchone()
    vectors = conn.execute(
        "SELECT COUNT(*) n, MAX(model) model, MAX(dim) dim FROM embeddings"
    ).fetchone()
    values = {
        "doc_count": str(stats["n"]),
        "published_count": str(published["n"]),
        "date_min": stats["lo"] or "",
        "date_max": stats["hi"] or "",
        "embedding_count": str(vectors["n"]),
        "embedding_model": vectors["model"] or "",
        "embedding_dim": str(vectors["dim"] or 0),
        "embeddings_enabled": "1" if embeddings_enabled else "0",
        "built_at": datetime.now(tz=timezone.utc).isoformat(),
    }
    conn.executemany(
        "INSERT INTO meta (key, value) VALUES (?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        list(values.items()),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the Pulse search index.")
    parser.add_argument("--full", action="store_true", help="rebuild from scratch")
    parser.add_argument(
        "--no-embeddings", action="store_true",
        help="lexical-only index (no embedding API key needed)",
    )
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--content-root", type=Path, default=CONTENT_ROOT)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )
    summary = build_index(
        args.db, args.content_root, full=args.full, embeddings=not args.no_embeddings
    )
    logger.info(
        "Index built: %d indexed, %d unchanged, %d removed, %d embedded → %s",
        summary["indexed"], summary["skipped"], summary["removed"],
        summary["embedded"], summary["db_path"],
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
