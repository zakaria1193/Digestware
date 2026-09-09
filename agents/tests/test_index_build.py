"""Index building — parsing, incrementality, and cleanup."""

from __future__ import annotations

import sqlite3

import pytest

from agents.index.build import build_index, connect, parse_document

LANDING = """\
---
project: binutils
subsystem: binutils/bfd
tags: [release, binutils]
commit_hash: ef840c1dd125bb2fbfbb6aa059fd2b001574d816
author: A Dev <dev@example.com>
headline: Fix relaxation loop in bfd_elf_final_link
tldr: A linker relaxation loop in bfd/elflink.c no longer spins forever.
impact_score: 7
breaking_change: true
outcome: committed
url: https://example.invalid/commit/ef840c1
date: '2026-09-07'
is_stub: false
---

The loop in bfd/elflink.c calling bfd_elf_final_link now terminates. Fixes PR 34165.
"""

DISCUSSION = """\
---
project: gcc
subsystem: gcc/ipa
discussion_id: msg-1@example.invalid
title: '[PATCH v2 1/3] gcc/ipa: retune -fipa-sra'
headline: 'gcc/ipa: retune -fipa-sra'
tldr: Retunes the IPA-SRA cost model.
proposer: B Dev <b@example.com>
outcome: proposed
impact_score: 5
technical_tradeoffs: ['Code size versus register pressure']
exchanges:
  - author: C Reviewer <c@example.com>
    role: reviewer
    position: Objects that this regresses aarch64 bootstrap.
    quote: This breaks bootstrap on aarch64.
primer_glossary:
  - term: SRA
    definition: Scalar Replacement of Aggregates, a GCC pass.
url: https://example.invalid/thread/1
date: '2026-09-06'
is_stub: false
---

Retunes gcc/ipa-sra.cc under -fipa-sra.
"""

NOISE = """\
---
project: binutils
subsystem: binutils/bfd
commit_hash: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
headline: Update BFD version date
tldr: Routine version bump.
outcome: committed
url: https://example.invalid/commit/aaaaaaa
date: '2026-09-07'
is_stub: true
stub_reason: low_score
---

Routine BFD_VERSION_DATE bump.
"""


@pytest.fixture
def corpus(tmp_path):
    """A miniature web/src/content tree."""
    root = tmp_path / "content"
    (root / "landings").mkdir(parents=True)
    (root / "discussions").mkdir(parents=True)
    (root / "landings" / "2026-09-07-bfd-ef840c1.md").write_text(LANDING, encoding="utf-8")
    (root / "landings" / "2026-09-07-bfd-noise.md").write_text(NOISE, encoding="utf-8")
    (root / "discussions" / "2026-09-06-ipa-sra.md").write_text(DISCUSSION, encoding="utf-8")
    return root


@pytest.fixture
def built(tmp_path, corpus):
    db = tmp_path / "pulse.db"
    summary = build_index(db, corpus, embeddings=False)
    return db, corpus, summary


def test_indexes_every_document(built):
    _db, _corpus, summary = built
    assert summary["indexed"] == 3
    assert summary["skipped"] == 0


def test_frontmatter_maps_onto_columns(built):
    db, _corpus, _ = built
    conn = connect(db)
    row = conn.execute("SELECT * FROM docs WHERE kind = 'landing' AND is_stub = 0").fetchone()
    assert row["project"] == "binutils"
    assert row["commit_hash"] == "ef840c1dd125bb2fbfbb6aa059fd2b001574d816"
    assert row["impact_score"] == 7
    assert row["breaking_change"] == 1
    assert row["date"] == "2026-09-07"
    conn.close()


def test_search_text_includes_thread_and_glossary_content(built):
    """Reviewer positions and glossary terms are searchable, not just the body."""
    db, _corpus, _ = built
    conn = connect(db)
    text = conn.execute("SELECT search_text FROM docs WHERE kind='discussion'").fetchone()[0]
    assert "bootstrap on aarch64" in text          # exchange quote
    assert "Scalar Replacement of Aggregates" in text  # glossary definition
    assert "[PATCH v2 1/3]" in text                # original subject line
    conn.close()


def test_authors_collect_proposer_and_participants(built):
    db, _corpus, _ = built
    conn = connect(db)
    import json
    authors = json.loads(
        conn.execute("SELECT authors FROM docs WHERE kind='discussion'").fetchone()[0]
    )
    assert authors[0].startswith("B Dev")
    assert any("C Reviewer" in a for a in authors)
    conn.close()


def test_symbols_are_extracted_per_document(built):
    db, _corpus, _ = built
    conn = connect(db)
    symbols = {
        r[0] for r in conn.execute(
            "SELECT symbol FROM symbols s JOIN docs d ON d.id = s.doc_id "
            "WHERE d.kind = 'landing' AND d.is_stub = 0"
        )
    }
    assert {"bfd/elflink.c", "bfd_elf_final_link", "pr34165"} <= symbols
    conn.close()


def test_rerun_is_incremental(built):
    db, corpus, _ = built
    again = build_index(db, corpus, embeddings=False)
    assert again["indexed"] == 0
    assert again["skipped"] == 3


def test_edited_file_is_reindexed(built):
    db, corpus, _ = built
    target = corpus / "landings" / "2026-09-07-bfd-ef840c1.md"
    target.write_text(LANDING.replace("Fixes PR 34165.", "Fixes PR 99999."), encoding="utf-8")
    summary = build_index(db, corpus, embeddings=False)
    assert summary["indexed"] == 1
    conn = connect(db)
    symbols = {r[0] for r in conn.execute("SELECT symbol FROM symbols")}
    assert "pr99999" in symbols
    assert "pr34165" not in symbols  # stale symbols must not survive a re-index
    conn.close()


def test_deleted_file_is_purged_from_index_and_fts(built):
    """The purge workflow deletes content; phantom hits must not remain."""
    db, corpus, _ = built
    (corpus / "discussions" / "2026-09-06-ipa-sra.md").unlink()
    summary = build_index(db, corpus, embeddings=False)
    assert summary["removed"] == 1
    conn = connect(db)
    assert conn.execute("SELECT COUNT(*) FROM docs").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM docs_fts").fetchone()[0] == 2
    conn.close()


def test_meta_records_coverage(built):
    db, _corpus, _ = built
    conn = connect(db)
    meta = {r["key"]: r["value"] for r in conn.execute("SELECT * FROM meta")}
    assert meta["doc_count"] == "3"
    assert meta["published_count"] == "2"   # the stub is excluded
    assert meta["date_min"] == "2026-09-06"
    assert meta["date_max"] == "2026-09-07"
    assert meta["embeddings_enabled"] == "0"
    conn.close()


def test_malformed_frontmatter_is_skipped_not_fatal(tmp_path, corpus):
    (corpus / "landings" / "broken.md").write_text("no frontmatter here", encoding="utf-8")
    summary = build_index(tmp_path / "pulse.db", corpus, embeddings=False)
    assert summary["indexed"] == 3


def test_identifier_tokens_survive_fts_tokenisation(built):
    """The whole design rests on `_`, `-` and `.` not splitting tokens."""
    db, _corpus, _ = built
    conn = sqlite3.connect(db)
    for token in ("bfd_elf_final_link", "-fipa-sra", "bfd/elflink.c"):
        hits = conn.execute(
            "SELECT COUNT(*) FROM docs_fts WHERE docs_fts MATCH ?", (f'"{token}"',)
        ).fetchone()[0]
        assert hits >= 1, f"{token} did not survive tokenisation"
    conn.close()


def test_parse_document_returns_none_without_frontmatter(tmp_path):
    path = tmp_path / "x.md"
    path.write_text("plain text", encoding="utf-8")
    assert parse_document(path, "landing") is None


# ── Embedding incrementality ────────────────────────────────────────────────
# The nightly workflow restores a cached pulse.db so the content-hash check can
# skip work. These tests pin the behaviour that makes that worthwhile: without
# them, a regression that re-embeds the whole corpus every night is invisible
# (the index is still correct — it just quietly costs money, growing with the
# archive).

class FakeProvider:
    """Records every text it is asked to embed."""

    def __init__(self, model: str = "fake-embed-1", dim: int = 4) -> None:
        self.model = model
        self.dim = dim
        self.calls: list[list[str]] = []

    def embed(self, texts: list[str]) -> list[list[float]]:
        self.calls.append(list(texts))
        return [[float(i + 1)] * self.dim for i in range(len(texts))]

    @property
    def embedded_count(self) -> int:
        return sum(len(c) for c in self.calls)


def test_embeds_every_document_on_first_run(built):
    from agents.index.build import embed_missing

    db, _corpus, _ = built
    conn = connect(db)
    provider = FakeProvider()
    assert embed_missing(conn, provider) == 3
    assert provider.embedded_count == 3
    conn.close()


def test_second_run_embeds_nothing(built):
    """The whole point of the cache: unchanged documents cost nothing."""
    from agents.index.build import embed_missing

    db, _corpus, _ = built
    conn = connect(db)
    provider = FakeProvider()
    embed_missing(conn, provider)
    provider.calls.clear()

    assert embed_missing(conn, provider) == 0
    assert provider.embedded_count == 0
    conn.close()


def test_only_changed_documents_are_re_embedded(built, corpus):
    """A nightly run must cost the delta, not the corpus."""
    from agents.index.build import embed_missing

    db, _corpus, _ = built
    conn = connect(db)
    provider = FakeProvider()
    embed_missing(conn, provider)
    conn.close()
    provider.calls.clear()

    # One edited file, one brand-new file — the shape of a real nightly run.
    (corpus / "landings" / "2026-09-07-bfd-ef840c1.md").write_text(
        LANDING.replace("Fixes PR 34165.", "Fixes PR 34165 and PR 22222."), encoding="utf-8"
    )
    (corpus / "discussions" / "new.md").write_text(
        DISCUSSION.replace("msg-1@example.invalid", "msg-2@example.invalid"), encoding="utf-8"
    )
    build_index(db, corpus, embeddings=False)

    conn = connect(db)
    assert embed_missing(conn, provider) == 2, "should embed only the changed and the new file"
    conn.close()


def test_changing_embedding_model_discards_incompatible_vectors(built):
    """Vectors from two models are not comparable and rarely share a dimension."""
    from agents.index.build import embed_missing

    db, _corpus, _ = built
    conn = connect(db)
    embed_missing(conn, FakeProvider(model="model-a", dim=4))

    other = FakeProvider(model="model-b", dim=8)
    assert embed_missing(conn, other) == 3, "all documents re-embed under the new model"

    models = {r[0] for r in conn.execute("SELECT DISTINCT model FROM embeddings")}
    dims = {r[0] for r in conn.execute("SELECT DISTINCT dim FROM embeddings")}
    assert models == {"model-b"}
    assert dims == {8}, "no mixed dimensions left behind"
    conn.close()


def test_reindexing_a_document_invalidates_its_vector(built, corpus):
    """A vector for text that no longer exists would be quietly wrong."""
    from agents.index.build import embed_missing

    db, _corpus, _ = built
    conn = connect(db)
    embed_missing(conn, FakeProvider())
    before = conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0]
    conn.close()
    assert before == 3

    (corpus / "landings" / "2026-09-07-bfd-ef840c1.md").write_text(
        LANDING.replace("terminates", "now terminates cleanly"), encoding="utf-8"
    )
    build_index(db, corpus, embeddings=False)

    conn = connect(db)
    assert conn.execute("SELECT COUNT(*) FROM embeddings").fetchone()[0] == 2
    conn.close()
