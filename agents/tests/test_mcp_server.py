"""MCP surface — tool registration, wiring, and the honesty guarantees.

The tool descriptions are part of the contract: an agent that reads `suspects`
as a diagnosis rather than a set of leads will confidently blame the wrong
commit, so the caveats are asserted here like any other behaviour.
"""

from __future__ import annotations

import json

import pytest

from agents.index.build import build_index
from agents.mcp import server as mcp_server
from agents.tests.test_index_build import DISCUSSION, LANDING, NOISE

EXPECTED_TOOLS = {
    "corpus_info", "search_changes", "find_by_symbol",
    "suspects", "timeline", "get_change", "related_discussion",
}


@pytest.fixture
def server(tmp_path, monkeypatch):
    root = tmp_path / "content"
    (root / "landings").mkdir(parents=True)
    (root / "discussions").mkdir(parents=True)
    (root / "landings" / "a.md").write_text(LANDING, encoding="utf-8")
    (root / "landings" / "noise.md").write_text(NOISE, encoding="utf-8")
    (root / "discussions" / "d.md").write_text(DISCUSSION, encoding="utf-8")
    db = tmp_path / "pulse.db"
    build_index(db, root, embeddings=False)

    monkeypatch.setenv("PULSE_DB", str(db))
    monkeypatch.setattr(mcp_server, "_index", None)  # drop any cached handle
    return mcp_server.build_server()


async def call(server, name, args):
    result = await server.call_tool(name, args)
    assert not result.is_error, result.content[0].text
    if result.structured_content is not None:
        return result.structured_content
    return json.loads(result.content[0].text)


@pytest.mark.asyncio
async def test_every_tool_is_registered(server):
    assert {t.name for t in await server.list_tools()} == EXPECTED_TOOLS


@pytest.mark.asyncio
async def test_every_tool_is_documented(server):
    for tool in await server.list_tools():
        assert tool.description and len(tool.description) > 40, tool.name


@pytest.mark.asyncio
async def test_suspects_description_warns_against_treating_hits_as_proof(server):
    tool = next(t for t in await server.list_tools() if t.name == "suspects")
    assert "NOT A DIAGNOSIS" in tool.description


@pytest.mark.asyncio
async def test_corpus_info_reports_coverage(server):
    info = await call(server, "corpus_info", {})
    assert info["documents_total"] == 3
    assert info["documents_published"] == 2
    assert info["covers_to"] == "2026-09-07"


@pytest.mark.asyncio
async def test_search_changes_returns_results_and_count(server):
    out = await call(server, "search_changes", {"query": "relaxation loop bfd_elf_final_link"})
    assert out["count"] == len(out["results"]) >= 1


@pytest.mark.asyncio
async def test_search_changes_reports_an_honest_miss(server):
    out = await call(server, "search_changes", {"query": "kubernetes ingress controller"})
    assert out["count"] == 0


@pytest.mark.asyncio
async def test_find_by_symbol_round_trips(server):
    out = await call(server, "find_by_symbol", {"symbol": "bfd_elf_final_link"})
    assert out["count"] >= 1


@pytest.mark.asyncio
async def test_suspects_payload_carries_the_caveat(server):
    out = await call(server, "suspects", {"symptom": "linker loops during relaxation"})
    assert "not a causal analysis" in out["caveat"]
    assert "window" in out


@pytest.mark.asyncio
async def test_get_change_hit_and_miss_are_both_explicit(server):
    hit = await call(server, "get_change", {"identifier": "ef840c1"})
    assert hit["found"] is True and hit["body"]
    miss = await call(server, "get_change", {"identifier": "cafebabe"})
    assert miss["found"] is False
    # A miss must not read as "this commit does not exist upstream".
    assert "absence here is not evidence" in miss["note"]


@pytest.mark.asyncio
async def test_timeline_returns_ordered_results(server):
    out = await call(server, "timeline", {"project": "binutils"})
    dates = [r["date"] for r in out["results"]]
    assert dates == sorted(dates)


@pytest.mark.asyncio
async def test_related_discussion_is_callable(server):
    out = await call(server, "related_discussion", {"commit_ref": "ef840c1"})
    assert out["count"] == len(out["results"])
