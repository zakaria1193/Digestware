"""Retrieval over the Pulse index.

Deliberately contains **no LLM calls**. The MCP server is a thin shell over this
module, so every query an agent makes costs nothing and the €5/month budget is
unaffected by usage. The calling agent supplies the reasoning; this supplies
evidence with citations.

Retrieval is hybrid:

* **Lexical (FTS5/BM25)** is the primary channel. Queries in this domain carry
  literal identifiers — ``bfd_elf_final_link``, ``-fipa-sra``, ``tc-z80.c`` —
  and the index tokenizer is configured to keep them intact.
* **Vector cosine** is the recall net for the case where someone can only
  describe a symptom ("linker hangs on compressed instructions") in words that
  appear nowhere in the article.
* **Symbol overlap** is an exactness bonus: a document that literally names the
  identifier you asked about outranks one that merely reads similarly.

The three are combined with Reciprocal Rank Fusion, which needs no score
calibration between channels — a standing problem when mixing BM25 magnitudes
with cosine similarities.
"""

from __future__ import annotations

import json
import logging
import math
import re
import sqlite3
from datetime import date, datetime, timezone
from pathlib import Path

from agents.index import DEFAULT_DB_PATH
from agents.index.symbols import extract_symbols, normalise_symbol

logger = logging.getLogger(__name__)

# RRF's damping constant. The canonical value is 60, tuned for fusing long
# result lists where heavy smoothing is wanted. That is wrong here: at k=60 the
# 1st and 3rd results differ by ~3%, so the small metadata boosts applied after
# fusion (impact, recency) decide the order and retrieval quality stops
# mattering. A smaller k keeps genuine rank differences visible above them.
_RRF_K = 12

# How deep each channel ranks before fusion. Wider than the result limit so a
# document ranked poorly by one channel can still be rescued by another.
_CHANNEL_DEPTH = 120

# An article that literally names the identifier from a stack trace is stronger
# evidence than one that merely reads similarly, so the symbol channel carries
# real weight rather than acting as a tie-breaker.
_WEIGHTS = {"lexical": 0.45, "vector": 0.25, "symbol": 0.30}

# A document must carry at least this share of the query's IDF mass to count as
# a lexical hit. Tuned on the real corpus: high enough that "PE section limit"
# stops matching every article containing "section", low enough that a genuine
# hit missing one incidental word still ranks.
_COVERAGE_FLOOR = 0.45

# FTS5 treats these as syntax; a user pasting a linker error must not produce a
# malformed-query exception.
_FTS_TOKEN_RE = re.compile(r"[A-Za-z0-9_.+-]+")


class IndexUnavailable(RuntimeError):
    """The index file is missing or has no documents."""


def _fts_match_query(text: str) -> str:
    """Turn free text into a safe FTS5 MATCH expression.

    Each token is double-quoted (making it a literal, not an operator) and the
    tokens are OR-ed, letting BM25 rank by how many of them a document matches
    rather than requiring all of them.
    """
    tokens = [t for t in _FTS_TOKEN_RE.findall(text) if len(t) > 1]
    if not tokens:
        return ""
    quoted = [f'"{t}"' for t in dict.fromkeys(tokens)]
    return " OR ".join(quoted)


def _rrf(ranked_ids: list[int]) -> dict[int, float]:
    """Reciprocal-rank scores for one channel's ordered result list."""
    return {doc_id: 1.0 / (_RRF_K + rank) for rank, doc_id in enumerate(ranked_ids, start=1)}


class PulseIndex:
    """Read-only query interface over ``pulse.db``."""

    def __init__(self, db_path: Path | str = DEFAULT_DB_PATH) -> None:
        self.db_path = Path(db_path)
        if not self.db_path.exists():
            raise IndexUnavailable(
                f"No index at {self.db_path}. Build one with "
                "`python -m agents.index.build --full [--no-embeddings]`."
            )
        # Read-only URI so a query process can never corrupt the index a
        # concurrent nightly build is writing.
        self._conn = sqlite3.connect(
            f"file:{self.db_path}?mode=ro", uri=True, check_same_thread=False
        )
        self._conn.row_factory = sqlite3.Row
        self._meta = {r["key"]: r["value"] for r in self._conn.execute("SELECT * FROM meta")}
        if int(self._meta.get("doc_count", 0)) == 0:
            raise IndexUnavailable(f"Index at {self.db_path} is empty.")
        self._vectors: tuple | None = None

    def close(self) -> None:
        self._conn.close()

    # ── metadata ─────────────────────────────────────────────────────────────

    def corpus_info(self) -> dict:
        """Coverage and freshness, so a caller can tell when to *not* answer."""
        by_project = {
            r["project"]: r["n"]
            for r in self._conn.execute(
                "SELECT project, COUNT(*) n FROM docs WHERE is_stub = 0 "
                "GROUP BY project ORDER BY n DESC"
            )
        }
        by_kind = {
            r["kind"]: r["n"]
            for r in self._conn.execute(
                "SELECT kind, COUNT(*) n FROM docs WHERE is_stub = 0 GROUP BY kind"
            )
        }
        return {
            "documents_total": int(self._meta.get("doc_count", 0)),
            "documents_published": int(self._meta.get("published_count", 0)),
            "covers_from": self._meta.get("date_min", ""),
            "covers_to": self._meta.get("date_max", ""),
            "by_project": by_project,
            "by_kind": by_kind,
            "embeddings": {
                "enabled": self._meta.get("embeddings_enabled") == "1",
                "count": int(self._meta.get("embedding_count", 0)),
                "model": self._meta.get("embedding_model", ""),
            },
            "built_at": self._meta.get("built_at", ""),
            "note": (
                "Digest articles summarising GCC/binutils commits and mailing-list "
                "threads. Contains no diffs or test results — treat every hit as a "
                "lead to verify upstream, never as proof."
            ),
        }

    # ── filtering ────────────────────────────────────────────────────────────

    def _filter_sql(
        self,
        *,
        project: str | None = None,
        subsystem: str | None = None,
        kind: str | None = None,
        since: str | None = None,
        until: str | None = None,
        outcome: str | None = None,
        min_impact: int | None = None,
        include_stubs: bool = False,
    ) -> tuple[str, list]:
        clauses: list[str] = []
        params: list = []
        if not include_stubs:
            # Stub digests are the pipeline's noise bucket ("Daily bump.",
            # "Update BFD version date") and are hidden on the public site too.
            clauses.append("d.is_stub = 0")
        if project:
            clauses.append("d.project = ?")
            params.append(project)
        if subsystem:
            # Substring, not equality: callers think in areas ("bfd", "ipa"),
            # while the field holds a specific path ("binutils/bfd").
            clauses.append("d.subsystem LIKE ?")
            params.append(f"%{subsystem}%")
        if kind:
            clauses.append("d.kind = ?")
            params.append(kind)
        if since:
            clauses.append("d.date >= ?")
            params.append(since[:10])
        if until:
            clauses.append("d.date <= ?")
            params.append(until[:10])
        if outcome:
            clauses.append("d.outcome = ?")
            params.append(outcome)
        if min_impact is not None:
            clauses.append("d.impact_score >= ?")
            params.append(min_impact)
        return (" AND ".join(clauses) or "1=1"), params

    def _candidate_ids(self, where: str, params: list) -> set[int]:
        return {
            int(r["id"]) for r in self._conn.execute(f"SELECT d.id FROM docs d WHERE {where}", params)
        }

    # ── channels ─────────────────────────────────────────────────────────────

    def _term_hits(self, token: str) -> set[int]:
        """Documents containing one literal token."""
        try:
            rows = self._conn.execute(
                "SELECT doc_id FROM docs_fts WHERE docs_fts MATCH ?", (f'"{token}"',)
            ).fetchall()
        except sqlite3.OperationalError as exc:
            logger.warning("FTS term query failed for %r: %s", token, exc)
            return set()
        return {int(r["doc_id"]) for r in rows}

    def _lexical(self, text: str, allowed: set[int]) -> list[int]:
        """Rank by IDF-weighted query-term coverage, then BM25.

        Plain OR-of-terms ranking is what makes a naive FTS search feel broken
        on this corpus: ask for "THP segment alignment" when the corpus has no
        THP content and BM25 will still hand back whatever mentions "alignment",
        presented as a confident match. Weighting each term by its inverse
        document frequency means the rare, discriminating word carries the
        result, and a document that misses every rare term is dropped rather
        than dressed up as a hit.
        """
        tokens = [t for t in dict.fromkeys(_FTS_TOKEN_RE.findall(text.casefold())) if len(t) > 1]
        if not tokens:
            return []

        total_docs = max(int(self._meta.get("doc_count", 1)), 1)
        coverage: dict[int, float] = {}
        best_possible = 0.0
        for token in tokens:
            hits = self._term_hits(token) & allowed
            # A term that appears nowhere still counts toward the target. This
            # is the difference between "no good match" and confident nonsense:
            # ask for "THP segment alignment" in a corpus with no THP content
            # and the two absent terms hold the bar above anything that merely
            # mentions "segment", so the query correctly returns nothing.
            idf = math.log(1 + total_docs / max(len(hits), 1))
            best_possible += idf
            for doc_id in hits:
                coverage[doc_id] = coverage.get(doc_id, 0.0) + idf

        if not coverage:
            return []

        # Keep only documents carrying a real share of the query's information.
        # Single-term queries have nothing to be partial about, so the floor
        # only applies once there is more than one term to cover.
        floor = best_possible * _COVERAGE_FLOOR if len(tokens) > 1 else 0.0
        qualified = [d for d, c in coverage.items() if c >= floor]
        if not qualified:
            return []

        # BM25 breaks ties within an equal-coverage band (it accounts for term
        # frequency and document length, which coverage alone ignores).
        bm25_rank: dict[int, int] = {}
        match = _fts_match_query(text)
        if match:
            try:
                for rank, row in enumerate(self._conn.execute(
                    "SELECT doc_id FROM docs_fts WHERE docs_fts MATCH ? "
                    "ORDER BY bm25(docs_fts) LIMIT ?",
                    (match, _CHANNEL_DEPTH * 8),
                )):
                    bm25_rank[int(row["doc_id"])] = rank
            except sqlite3.OperationalError as exc:
                logger.warning("FTS query failed for %r: %s", text, exc)

        qualified.sort(key=lambda d: (-coverage[d], bm25_rank.get(d, 1 << 30), d))
        return qualified[:_CHANNEL_DEPTH]

    def _load_vectors(self):
        """Load all embeddings once as a normalised matrix (lazy, cached)."""
        if self._vectors is not None:
            return self._vectors
        import numpy as np

        rows = self._conn.execute(
            "SELECT doc_id, dim, vector FROM embeddings ORDER BY doc_id"
        ).fetchall()
        if not rows:
            self._vectors = ([], None)
            return self._vectors
        dim = int(rows[0]["dim"])
        usable = [r for r in rows if int(r["dim"]) == dim]
        matrix = np.frombuffer(b"".join(r["vector"] for r in usable), dtype="<f4").reshape(
            len(usable), dim
        )
        self._vectors = ([int(r["doc_id"]) for r in usable], matrix)
        return self._vectors

    def _vector(self, text: str, allowed: set[int]) -> list[int]:
        if self._meta.get("embeddings_enabled") != "1":
            return []
        doc_ids, matrix = self._load_vectors()
        if matrix is None:
            return []
        try:
            import numpy as np

            from agents.index.embed import build_provider

            query_vec = build_provider().embed([text])[0]
        except Exception as exc:  # noqa: BLE001 — vectors are a bonus channel
            # A missing key or a provider outage must degrade to lexical-only
            # rather than failing the whole query.
            logger.warning("Vector channel unavailable (%s) — lexical only", exc)
            return []
        q = np.asarray(query_vec, dtype="float32")
        norm = float(np.linalg.norm(q))
        if norm == 0:
            return []
        # Stored vectors are already L2-normalised, so this dot product is cosine.
        scores = matrix @ (q / norm)
        order = scores.argsort()[::-1]
        ranked: list[int] = []
        for idx in order:
            doc_id = doc_ids[int(idx)]
            if doc_id in allowed:
                ranked.append(doc_id)
                if len(ranked) >= _CHANNEL_DEPTH:
                    break
        return ranked

    def _symbol_matches(self, text: str, allowed: set[int]) -> tuple[list[int], dict[int, list[str]]]:
        """Rank documents by how many query identifiers they literally contain."""
        keys = {sym for sym, _display, _kind in extract_symbols(text)}
        keys.add(normalise_symbol(text))
        keys = {k for k in keys if k}
        if not keys:
            return [], {}
        placeholders = ", ".join("?" for _ in keys)
        rows = self._conn.execute(
            f"SELECT doc_id, display FROM symbols WHERE symbol IN ({placeholders})",
            list(keys),
        ).fetchall()
        hits: dict[int, list[str]] = {}
        for row in rows:
            doc_id = int(row["doc_id"])
            if doc_id in allowed:
                hits.setdefault(doc_id, []).append(row["display"])
        ranked = sorted(hits, key=lambda d: (-len(hits[d]), d))[:_CHANNEL_DEPTH]
        return ranked, hits

    # ── public search ────────────────────────────────────────────────────────

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
        use_vectors: bool = True,
        recency_window_days: int | None = None,
        collapse_series: bool = True,
        **filters,
    ) -> list[dict]:
        """Hybrid search. Returns result dicts ordered best-first."""
        where, params = self._filter_sql(**filters)
        allowed = self._candidate_ids(where, params)
        if not allowed:
            return []

        lexical = self._lexical(query, allowed)
        vector = self._vector(query, allowed) if use_vectors else []
        symbol_ranked, symbol_hits = self._symbol_matches(query, allowed)

        scores: dict[int, float] = {}
        channels: dict[int, list[str]] = {}
        for name, ranked in (
            ("lexical", lexical), ("vector", vector), ("symbol", symbol_ranked)
        ):
            for doc_id, rr in _rrf(ranked).items():
                scores[doc_id] = scores.get(doc_id, 0.0) + _WEIGHTS[name] * rr
                channels.setdefault(doc_id, []).append(name)

        if not scores:
            return []

        rows = self._rows_by_id(list(scores))
        results = []
        for doc_id, score in scores.items():
            row = rows.get(doc_id)
            if row is None:
                continue
            # An exact identifier match is evidence about *this* symptom and is
            # exempt from recency shading; similarity-only matches are not.
            if recency_window_days and not symbol_hits.get(doc_id):
                score *= _recency_factor(row["date"], recency_window_days)
            # A change flagged breaking, or scored as high-impact, is a
            # marginally more plausible cause than a routine tidy-up. These are
            # deliberately small: they are priors about a document, not evidence
            # about the query, and must never reorder a clearly better match.
            if row["breaking_change"]:
                score *= 1.10
            if (row["impact_score"] or 0) >= 7:
                score *= 1.05
            results.append(
                self._to_result(row, score=score, channels=channels.get(doc_id, []),
                                matched_symbols=symbol_hits.get(doc_id, []))
            )
        results.sort(key=lambda r: r["score"], reverse=True)
        if collapse_series:
            results = _collapse_series(results)
        return results[:limit]

    def suspects(
        self,
        symptom: str,
        *,
        since: str | None = None,
        until: str | None = None,
        subsystems: list[str] | None = None,
        symbols: list[str] | None = None,
        limit: int = 12,
        **filters,
    ) -> dict:
        """Rank likely-related changes for a regression symptom.

        Returns *leads*, not a verdict: the corpus has no diffs or test results,
        so nothing here can establish causation. Each candidate carries the
        upstream URL so the caller can go and check.
        """
        window_days = _days_between(since, until)
        query = " ".join([symptom, *(symbols or [])])

        pools: list[list[dict]] = []
        for subsystem in subsystems or [None]:
            pools.append(
                self.search(
                    query,
                    limit=limit * 2,
                    since=since,
                    until=until,
                    subsystem=subsystem,
                    recency_window_days=window_days,
                    **filters,
                )
            )

        merged: dict[str, dict] = {}
        for pool in pools:
            for item in pool:
                prior = merged.get(item["path"])
                if prior is None or item["score"] > prior["score"]:
                    merged[item["path"]] = item
        candidates = sorted(merged.values(), key=lambda r: r["score"], reverse=True)[:limit]

        for item in candidates:
            item["why"] = _explain(item)

        return {
            "symptom": symptom,
            "window": {"since": since or self._meta.get("date_min", ""),
                       "until": until or self._meta.get("date_max", "")},
            "candidates": candidates,
            "caveat": (
                "These are leads ranked by textual and semantic similarity to the "
                "symptom, not a causal analysis. This corpus holds digest articles, "
                "not diffs or test results. Verify each candidate against the real "
                "repository (git show <sha>) before acting on it."
            ),
        }

    def find_by_symbol(self, symbol: str, *, limit: int = 20, **filters) -> list[dict]:
        """Exact identifier lookup — the fast path before falling back to search."""
        key = normalise_symbol(symbol)
        where, params = self._filter_sql(**filters)
        rows = self._conn.execute(
            f"SELECT d.*, s.display, s.kind AS symbol_kind FROM symbols s "
            f"JOIN docs d ON d.id = s.doc_id WHERE s.symbol = ? AND {where} "
            f"ORDER BY d.date DESC LIMIT ?",
            [key, *params, limit],
        ).fetchall()
        return [
            self._to_result(r, score=1.0, channels=["symbol"], matched_symbols=[r["display"]])
            for r in rows
        ]

    def timeline(
        self, *, subsystem: str | None = None, series_id: str | None = None,
        limit: int = 40, **filters,
    ) -> list[dict]:
        """Chronological narrative for a subsystem or patch series."""
        where, params = self._filter_sql(subsystem=subsystem, **filters)
        if series_id:
            where += " AND d.series_id = ?"
            params.append(series_id)
        rows = self._conn.execute(
            f"SELECT d.* FROM docs d WHERE {where} ORDER BY d.date ASC, d.id ASC LIMIT ?",
            [*params, limit],
        ).fetchall()
        return [self._to_result(r, score=0.0, channels=[], matched_symbols=[]) for r in rows]

    def get_change(self, identifier: str) -> dict | None:
        """Fetch one document by path, commit SHA (or prefix), or discussion id."""
        ident = identifier.strip()
        row = self._conn.execute(
            "SELECT * FROM docs WHERE path = ? OR commit_hash = ? OR discussion_id = ? "
            "OR url = ? LIMIT 1",
            (ident, ident, ident, ident),
        ).fetchone()
        if row is None and re.fullmatch(r"[0-9a-f]{7,40}", ident):
            row = self._conn.execute(
                "SELECT * FROM docs WHERE commit_hash LIKE ? LIMIT 1", (f"{ident}%",)
            ).fetchone()
        if row is None:
            return None
        result = self._to_result(row, score=1.0, channels=[], matched_symbols=[])
        result["body"] = row["body"]
        result["symbols"] = [
            {"symbol": r["display"], "kind": r["kind"]}
            for r in self._conn.execute(
                "SELECT display, kind FROM symbols WHERE doc_id = ? ORDER BY kind, display",
                (row["id"],),
            )
        ]
        return result

    def related_discussion(self, commit_ref: str, *, limit: int = 5) -> list[dict]:
        """Find the mailing-list thread behind a landed commit.

        ``discussion_id_link`` is unpopulated across the corpus today, so this
        walks the signals that *are* present: the shared ``series_id`` first,
        then identifier overlap between the two documents.
        """
        landing = self.get_change(commit_ref)
        if landing is None:
            return []
        if landing.get("series_id"):
            rows = self._conn.execute(
                "SELECT * FROM docs WHERE kind = 'discussion' AND series_id = ? "
                "ORDER BY date ASC LIMIT ?",
                (landing["series_id"], limit),
            ).fetchall()
            if rows:
                return [self._to_result(r, score=1.0, channels=["series_id"],
                                        matched_symbols=[]) for r in rows]
        return self.search(
            f"{landing['headline']} {landing.get('tldr', '')}",
            kind="discussion", project=landing.get("project"), limit=limit,
        )

    # ── shaping ──────────────────────────────────────────────────────────────

    def _rows_by_id(self, ids: list[int]) -> dict[int, sqlite3.Row]:
        if not ids:
            return {}
        placeholders = ", ".join("?" for _ in ids)
        return {
            int(r["id"]): r
            for r in self._conn.execute(f"SELECT * FROM docs WHERE id IN ({placeholders})", ids)
        }

    @staticmethod
    def _to_result(row, *, score: float, channels: list[str], matched_symbols: list[str]) -> dict:
        return {
            "path": row["path"],
            "kind": row["kind"],
            "project": row["project"],
            "subsystem": row["subsystem"],
            "headline": row["headline"],
            "tldr": row["tldr"],
            "date": row["date"],
            "url": row["url"],
            "commit_hash": row["commit_hash"],
            "discussion_id": row["discussion_id"],
            "series_id": row["series_id"],
            "outcome": row["outcome"],
            "impact_score": row["impact_score"],
            "breaking_change": bool(row["breaking_change"]),
            "tags": json.loads(row["tags"] or "[]"),
            "authors": json.loads(row["authors"] or "[]"),
            "score": round(score, 6),
            "matched_via": channels,
            "matched_symbols": sorted(set(matched_symbols))[:8],
        }


def _recency_factor(doc_date: str, window_days: int) -> float:
    """Gentle decay toward the *end* of the search window.

    Within a window the later changes are the better suspects, but only mildly:
    the caller already chose the window, so everything in it is a candidate.
    The half-life is the full window rather than half of it — at half-window it
    was strong enough to bury an article naming the exact symbol from the
    symptom under newer, vaguer matches, which is the opposite of useful.
    """
    parsed = _parse_date(doc_date)
    if parsed is None or window_days <= 0:
        return 1.0
    age = (datetime.now(tz=timezone.utc).date() - parsed).days
    return 0.5 ** (max(age, 0) / max(window_days, 1))


def _parse_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value[:10])
    except (ValueError, TypeError):
        return None


def _days_between(since: str | None, until: str | None) -> int | None:
    start, end = _parse_date(since or ""), _parse_date(until or "")
    if start is None:
        return None
    end = end or datetime.now(tz=timezone.utc).date()
    return max((end - start).days, 1)


_VERSION_MARKER_RE = re.compile(r"\b[vV]\d+\b|\[[^\]]*\]|\(\d+/\d+\)")


def _series_key(item: dict) -> str:
    """Identity of the underlying story, for de-duplicating re-postings.

    ``series_id`` would be the right field, but the ingest populates it on only
    ~1% of landings and ~21% of discussions, so relying on it alone collapses
    almost nothing. The fallback is the normalised headline within a project,
    which is what actually distinguishes a v2 re-post or a cross-posted thread
    from a genuinely different change.
    """
    if item.get("series_id"):
        return f"sid:{item['series_id']}"
    headline = _VERSION_MARKER_RE.sub(" ", item.get("headline", ""))
    headline = re.sub(r"[^a-z0-9]+", " ", headline.casefold()).strip()
    if not headline:
        return ""
    return f"{item.get('project', '')}:{headline}"


def _collapse_series(results: list[dict]) -> list[dict]:
    """Keep the best-scoring document per patch series.

    A v1/v2/v3 posting of the same patch, or a thread re-sent to two lists,
    produces several near-identical articles. Left alone they fill a result
    page with one story. The dropped siblings are not lost — they are listed
    under ``other_in_series`` on the survivor so the caller can still see the
    full arc, and ``timeline(series_id=...)`` returns all of them in order.
    """
    kept: list[dict] = []
    by_series: dict[str, dict] = {}
    for item in results:
        series = _series_key(item)
        if not series:
            kept.append(item)
            continue
        leader = by_series.get(series)
        if leader is None:
            item["other_in_series"] = []
            by_series[series] = item
            kept.append(item)
        else:
            leader["other_in_series"].append(
                {"path": item["path"], "date": item["date"], "url": item["url"]}
            )
    return kept


def _explain(item: dict) -> str:
    """One line saying why this candidate surfaced — never why it is guilty."""
    reasons = []
    if item["matched_symbols"]:
        reasons.append("mentions " + ", ".join(item["matched_symbols"][:3]))
    if "lexical" in item["matched_via"]:
        reasons.append("wording overlaps the symptom")
    if "vector" in item["matched_via"]:
        reasons.append("semantically similar")
    if item["breaking_change"]:
        reasons.append("flagged as a breaking change")
    if (item["impact_score"] or 0) >= 7:
        reasons.append(f"high impact ({item['impact_score']}/10)")
    if item["subsystem"]:
        reasons.append(f"in {item['subsystem']}")
    return "; ".join(reasons) or "matched the query"


def open_index(db_path: Path | str = DEFAULT_DB_PATH) -> PulseIndex:
    return PulseIndex(db_path)
