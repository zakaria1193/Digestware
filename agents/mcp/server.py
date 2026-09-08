"""Pulse MCP server — the digest corpus as a tool for debugging agents.

    python -m agents.mcp.server

Register with Claude Code:

    claude mcp add pulse -- /path/to/python -m agents.mcp.server

Every tool is a read-only query against ``agents/index/pulse.db``. There are no
LLM calls in this process, so serving queries costs nothing and cannot affect
the project's €5/month budget however heavily an agent uses it.

What this corpus is, and what it is not: it holds *digest articles* about GCC
and binutils commits and mailing-list threads — headline, plain-English summary,
subsystem, outcome, participants, upstream URL. It holds no diffs, no test
results, and no build metadata. It can therefore point an agent at plausible
changes and at the discussion around them; it cannot establish that any of them
caused a regression. The tool descriptions say so, because a model that treats a
similarity hit as a verdict will confidently blame the wrong commit.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Annotated, Any

from pydantic import Field

from agents.index import DEFAULT_DB_PATH
from agents.index.query import IndexUnavailable, PulseIndex

logger = logging.getLogger(__name__)

INSTRUCTIONS = """\
Pulse indexes daily digest articles about GCC and binutils — landed commits and
mailing-list discussions — with subsystem, outcome, participants and upstream URLs.

Use it to find *what changed and what people said about it*: recent activity in a
subsystem, the argument behind a design, who reviews an area, or candidate changes
related to a regression symptom.

It contains no diffs, test results or build logs, so it cannot prove causation.
Treat every hit as a lead to verify upstream (`git show <sha>`), and cite the URL
each result carries. Call `corpus_info` first if you need to know whether the
corpus even covers the period or project in question — it is not a substitute for
`git log`, and answering from it about an uncovered project would be a guess.
"""

_index: PulseIndex | None = None


def get_index() -> PulseIndex:
    """Open the index on first use so an import never touches the disk."""
    global _index
    if _index is None:
        db_path = Path(os.environ.get("PULSE_DB", DEFAULT_DB_PATH))
        _index = PulseIndex(db_path)
    return _index


def build_server():
    from mcp.server.mcpserver import MCPServer

    server = MCPServer(name="pulse", instructions=INSTRUCTIONS)

    @server.tool()
    def corpus_info() -> dict:
        """Coverage of the Pulse corpus: projects, date range, counts, freshness.

        Call this before answering a question that depends on the corpus being
        complete. If the project or time period asked about is not covered, say
        so rather than answering from partial data.
        """
        return get_index().corpus_info()

    @server.tool()
    def search_changes(
        query: Annotated[
            str, Field(description="Free text; include exact identifiers when known.")
        ],
        project: Annotated[str | None, Field(description="'gcc' or 'binutils'.")] = None,
        subsystem: Annotated[
            str | None, Field(description="Substring, e.g. 'bfd', 'ipa', 'aarch64'.")
        ] = None,
        kind: Annotated[
            str | None, Field(description="'landing' (commit) or 'discussion' (thread).")
        ] = None,
        since: Annotated[str | None, Field(description="ISO date lower bound, YYYY-MM-DD.")] = None,
        until: Annotated[str | None, Field(description="ISO date upper bound, YYYY-MM-DD.")] = None,
        outcome: Annotated[
            str | None,
            Field(description="proposed|under_review|needs_revision|nackd|ready|"
                              "committed|withdrawn|stalled"),
        ] = None,
        min_impact: Annotated[int | None, Field(description="Minimum impact score, 1-10.")] = None,
        limit: Annotated[int, Field(description="Max results.", ge=1, le=50)] = 10,
    ) -> dict:
        """Search GCC/binutils digest articles. The general-purpose entry point.

        Combines exact-term matching, semantic similarity and identifier lookup.
        An empty result means the corpus has nothing matching — report that
        rather than loosening the query until something appears.
        """
        results = get_index().search(
            query, limit=limit, project=project, subsystem=subsystem, kind=kind,
            since=since, until=until, outcome=outcome, min_impact=min_impact,
        )
        return {"query": query, "count": len(results), "results": results}

    @server.tool()
    def find_by_symbol(
        symbol: Annotated[
            str,
            Field(description="Exact identifier: function, file path, flag, "
                              "relocation or PR number."),
        ],
        project: Annotated[str | None, Field(description="'gcc' or 'binutils'.")] = None,
        limit: Annotated[int, Field(ge=1, le=50)] = 20,
    ) -> dict:
        """Find articles literally mentioning one identifier.

        Accepts `bfd_elf_final_link`, `gcc/ipa-sra.cc`, `-fipa-sra`,
        `R_AARCH64_TLSDESC`, `PR34165`. Prefer this over `search_changes` when
        you have an exact name — it is a lookup, not a ranking.
        """
        results = get_index().find_by_symbol(symbol, limit=limit, project=project)
        return {"symbol": symbol, "count": len(results), "results": results}

    @server.tool()
    def suspects(
        symptom: Annotated[
            str,
            Field(description="What broke, in prose. Paste the diagnostic or "
                              "describe the misbehaviour."),
        ],
        since: Annotated[
            str | None,
            Field(description="Start of the window when it last worked, YYYY-MM-DD."),
        ] = None,
        until: Annotated[
            str | None, Field(description="End of the window, YYYY-MM-DD.")
        ] = None,
        subsystems: Annotated[
            list[str] | None,
            Field(description="Optional subsystems to focus on, e.g. ['bfd','ld']."),
        ] = None,
        symbols: Annotated[
            list[str] | None,
            Field(description="Exact identifiers from the failure: functions, files, flags."),
        ] = None,
        project: Annotated[str | None, Field(description="'gcc' or 'binutils'.")] = None,
        limit: Annotated[int, Field(ge=1, le=30)] = 12,
    ) -> dict:
        """Rank changes plausibly related to a regression symptom, newest-weighted.

        Returns LEADS, NOT A DIAGNOSIS. Ranking is textual and semantic
        similarity to the symptom — the corpus has no diffs or test results, so
        nothing here can establish that a change caused anything. Present the
        candidates as things to check, verify each with `git show <sha>` against
        the real repository, and never tell the user a commit is the culprit on
        this evidence alone.
        """
        return get_index().suspects(
            symptom, since=since, until=until, subsystems=subsystems,
            symbols=symbols, limit=limit, project=project,
        )

    @server.tool()
    def timeline(
        subsystem: Annotated[
            str | None, Field(description="Substring, e.g. 'bfd', 'aarch64'.")
        ] = None,
        series_id: Annotated[
            str | None, Field(description="Group a single patch series.")
        ] = None,
        project: Annotated[str | None, Field(description="'gcc' or 'binutils'.")] = None,
        since: Annotated[str | None, Field(description="ISO date lower bound.")] = None,
        until: Annotated[str | None, Field(description="ISO date upper bound.")] = None,
        limit: Annotated[int, Field(ge=1, le=100)] = 40,
    ) -> dict:
        """Chronological activity for a subsystem or patch series, oldest first.

        Use when the question is "what has been going on in this area", or to
        follow one proposal from first posting through review to landing.
        """
        results = get_index().timeline(
            subsystem=subsystem, series_id=series_id, project=project,
            since=since, until=until, limit=limit,
        )
        return {"count": len(results), "results": results}

    @server.tool()
    def get_change(
        identifier: Annotated[
            str,
            Field(description="Commit SHA (full or 7+ char prefix), discussion id, "
                              "article path, or upstream URL."),
        ],
    ) -> dict[str, Any]:
        """Fetch one article in full: frontmatter, body, and extracted identifiers."""
        result = get_index().get_change(identifier)
        if result is None:
            return {"found": False, "identifier": identifier,
                    "note": "No article for that identifier. The corpus does not "
                            "cover every commit — absence here is not evidence."}
        return {"found": True, **result}

    @server.tool()
    def related_discussion(
        commit_ref: Annotated[
            str, Field(description="Commit SHA or article path of a landed change.")
        ],
        limit: Annotated[int, Field(ge=1, le=20)] = 5,
    ) -> dict:
        """Find the mailing-list thread behind a landed commit.

        Matches on shared patch series first, then on subject and identifier
        overlap. The link is inferred, not recorded upstream, so confirm the
        thread really is about the commit before relying on it.
        """
        results = get_index().related_discussion(commit_ref, limit=limit)
        return {"commit_ref": commit_ref, "count": len(results), "results": results}

    return server


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    try:
        get_index()
    except IndexUnavailable as exc:
        # stdio is the protocol channel — diagnostics must go to stderr.
        print(f"pulse: {exc}", file=sys.stderr)
        return 1
    build_server().run(transport="stdio")
    return 0


if __name__ == "__main__":
    sys.exit(main())
