"""web_search — DuckDuckGo enrichment tool for cryptic commit/discussion titles.

Returns up to 5 result snippets. Called only when the title is short
(< 20 words) or lacks a recognisable subsystem keyword so the LLM has
enough context to produce a meaningful summary.
"""

import logging

logger = logging.getLogger(__name__)


def search_context(query: str, max_results: int = 5) -> list[str]:
    """Return up to *max_results* DuckDuckGo text snippets for *query*.

    Falls back to an empty list on any error so the agent can continue
    without web enrichment.
    """
    if not query or not query.strip():
        return []
    try:
        from duckduckgo_search import DDGS  # lazy import — not always installed

        snippets: list[str] = []
        with DDGS() as ddgs:
            for result in ddgs.text(query, max_results=max_results):
                body = result.get("body") or result.get("snippet") or ""
                if body:
                    snippets.append(body)
        return snippets[:max_results]
    except ImportError:
        logger.warning("duckduckgo-search not installed; web enrichment disabled")
        return []
    except Exception as exc:
        logger.warning("DuckDuckGo search failed for %r: %s", query, exc)
        return []
