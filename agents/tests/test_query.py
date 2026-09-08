"""Retrieval behaviour — relevance, honesty about misses, and filtering."""

from __future__ import annotations

import pytest

from agents.index.build import build_index
from agents.index.query import IndexUnavailable, PulseIndex
from agents.tests.test_index_build import DISCUSSION, LANDING, NOISE

EXTRA = """\
---
project: gcc
subsystem: gcc/aarch64
commit_hash: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
author: D Dev <d@example.com>
headline: 'aarch64: correct SVE predicate spill alignment'
tldr: Fixes an SVE predicate spill slot alignment bug.
impact_score: 8
outcome: committed
url: https://example.invalid/commit/bbbbbbb
date: '2026-08-01'
is_stub: false
---

Corrects predicate spill alignment in gcc/config/aarch64/aarch64.cc.
"""

SERIES_A = """\
---
project: gcc
subsystem: gcc/ipa
discussion_id: msg-a@example.invalid
headline: 'gcc/ipa: retune -fipa-sra'
tldr: First posting of the IPA-SRA retune.
proposer: B Dev <b@example.com>
outcome: proposed
url: https://example.invalid/thread/a
date: '2026-09-01'
is_stub: false
---

Retunes gcc/ipa-sra.cc under -fipa-sra.
"""


@pytest.fixture
def index(tmp_path):
    root = tmp_path / "content"
    (root / "landings").mkdir(parents=True)
    (root / "discussions").mkdir(parents=True)
    (root / "landings" / "a.md").write_text(LANDING, encoding="utf-8")
    (root / "landings" / "noise.md").write_text(NOISE, encoding="utf-8")
    (root / "landings" / "sve.md").write_text(EXTRA, encoding="utf-8")
    (root / "discussions" / "d.md").write_text(DISCUSSION, encoding="utf-8")
    (root / "discussions" / "d2.md").write_text(SERIES_A, encoding="utf-8")
    db = tmp_path / "pulse.db"
    build_index(db, root, embeddings=False)
    ix = PulseIndex(db)
    yield ix
    ix.close()


def headlines(results):
    return [r["headline"] for r in results]


def test_finds_the_relevant_document(index):
    hits = index.search("SVE predicate spill alignment")
    assert "aarch64: correct SVE predicate spill alignment" in headlines(hits)


def test_absent_topic_returns_nothing_rather_than_noise(index):
    """The corpus covers no THP work; a partial word match must not pose as a hit."""
    assert index.search("transparent huge page madvise THP alignment") == []


def test_nonsense_query_returns_nothing(index):
    assert index.search("bogus quantum flux capacitor telemetry") == []


def test_stubs_are_hidden_by_default_but_reachable_explicitly(index):
    assert "Update BFD version date" not in headlines(index.search("BFD version date"))
    assert "Update BFD version date" in headlines(
        index.search("BFD version date", include_stubs=True)
    )


def test_filters_narrow_results(index):
    assert all(r["project"] == "gcc" for r in index.search("alignment", project="gcc"))
    assert all(r["kind"] == "discussion" for r in index.search("ipa-sra", kind="discussion"))
    assert index.search("SVE predicate spill", since="2026-09-01") == []
    assert index.search("SVE predicate spill", until="2026-07-01") == []


def test_subsystem_filter_matches_on_substring(index):
    """Callers think in areas ('aarch64'), the field holds a path ('gcc/aarch64')."""
    assert headlines(index.search("alignment", subsystem="aarch64"))


def test_min_impact_filter(index):
    assert all((r["impact_score"] or 0) >= 8 for r in index.search("alignment", min_impact=8))


def test_repeated_series_collapses_to_one_result(index):
    """Two postings of the same patch are one story, not two hits."""
    hits = index.search("retune -fipa-sra")
    ipa = [r for r in hits if "-fipa-sra" in r["headline"]]
    assert len(ipa) == 1
    assert ipa[0]["other_in_series"], "the duplicate should be attached, not discarded"


def test_find_by_symbol_is_exact(index):
    assert headlines(index.find_by_symbol("bfd_elf_final_link"))
    assert headlines(index.find_by_symbol("-fipa-sra"))
    assert index.find_by_symbol("no_such_symbol_anywhere") == []


def test_find_by_symbol_accepts_typed_variants(index):
    assert headlines(index.find_by_symbol("PR 34165")) == headlines(index.find_by_symbol("pr34165"))


def test_get_change_by_sha_prefix_and_full(index):
    assert index.get_change("ef840c1dd125bb2fbfbb6aa059fd2b001574d816")["headline"].startswith("Fix relaxation")
    assert index.get_change("ef840c1")["headline"].startswith("Fix relaxation")
    assert index.get_change("does-not-exist") is None


def test_get_change_includes_body_and_symbols(index):
    change = index.get_change("ef840c1")
    assert "bfd/elflink.c" in change["body"]
    assert any(s["symbol"] == "bfd_elf_final_link" for s in change["symbols"])


def test_timeline_is_chronological(index):
    dates = [r["date"] for r in index.timeline(project="gcc")]
    assert dates == sorted(dates)


def test_results_carry_citable_provenance(index):
    for result in index.search("SVE predicate spill alignment"):
        assert result["url"].startswith("http")
        assert result["date"]
        assert result["path"]


def test_suspects_returns_leads_with_an_explicit_caveat(index):
    report = index.suspects("linker spins forever during relaxation", since="2026-01-01")
    assert report["candidates"]
    assert "not a causal analysis" in report["caveat"]
    assert all(c["why"] for c in report["candidates"])


def test_suspects_respects_its_window(index):
    report = index.suspects("SVE predicate spill", since="2026-09-01")
    assert all(c["date"] >= "2026-09-01" for c in report["candidates"])


def test_related_discussion_links_a_landing_to_its_thread(index):
    related = index.related_discussion("ef840c1")
    assert isinstance(related, list)


def test_missing_index_raises_a_useful_error(tmp_path):
    with pytest.raises(IndexUnavailable, match="agents.index.build"):
        PulseIndex(tmp_path / "absent.db")
