"""web_search — Gemini grounded search enrichment tool for cryptic commit/discussion titles.

Uses the OpenRouter `:online` model suffix to enable Gemini's native Google Search
grounding.  All traffic goes through OpenRouter via the shared ``agents._openrouter``
client — no separate Gemini API key is required.

Called only when a commit/discussion title is short (< 20 words) or lacks a
recognisable subsystem keyword so the downstream LLM has enough context to produce
a meaningful summary.
"""

import logging

from agents._openrouter import build_client

logger = logging.getLogger(__name__)

# Appending :online tells OpenRouter to enable web-search grounding for this call.
_SEARCH_MODEL = "google/gemini-2.0-flash-001:online"


def search_context(query: str, max_results: int = 5) -> list[str]:
    """Return up to *max_results* Gemini-grounded search snippets for *query*.

    Calls Gemini Flash with OpenRouter's :online grounding so results are
    AI-synthesised rather than raw page snippets.  Falls back to an empty list
    on any error so the agent can continue without web enrichment.
    """
    if not query or not query.strip():
        return []
    try:
        client = build_client()
        response = client.chat.completions.create(
            model=_SEARCH_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Search for concise technical context about: {query}. "
                        "Return key facts as short bullet points."
                    ),
                }
            ],
            max_tokens=512,
        )

        text = (response.choices[0].message.content or "").strip()
        lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
        return lines[:max_results]

    except Exception as exc:
        logger.warning("Gemini online search failed for %r: %s", query, exc)
        return []
