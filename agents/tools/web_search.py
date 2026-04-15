"""web_search — Gemini grounded search enrichment tool for cryptic commit/discussion titles.

Returns up to max_results text snippets grounded by Google Search via the Gemini API.
The model uses its native search tool to find and synthesise information rather than
returning raw results, so the snippets are already contextualised by an AI.

Called only when the title is short (< 20 words) or lacks a recognisable subsystem
keyword so the downstream LLM has enough context to produce a meaningful summary.
"""

import logging
import os

logger = logging.getLogger(__name__)

# Model used for search grounding — intentionally separate from SUMMARISER_MODEL
# so the search step can be tuned independently.
_SEARCH_MODEL = "gemini-2.0-flash"


def search_context(query: str, max_results: int = 5) -> list[str]:
    """Return up to *max_results* Gemini-grounded search snippets for *query*.

    Uses Gemini's native Google Search tool so the results are AI-synthesised
    rather than raw page snippets.  Falls back to an empty list on any error
    so the agent can continue without web enrichment.
    """
    if not query or not query.strip():
        return []
    try:
        from google import genai  # lazy import — not always installed
        from google.genai import types

        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            logger.warning("GEMINI_API_KEY not set; web enrichment disabled")
            return []

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=_SEARCH_MODEL,
            contents=(
                f"Search for concise technical context about: {query}. "
                "Return key facts as short bullet points."
            ),
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                max_output_tokens=512,
            ),
        )

        snippets: list[str] = []

        # Primary: extract source titles from grounding metadata (one per citation)
        if response.candidates:
            metadata = getattr(response.candidates[0], "grounding_metadata", None)
            if metadata:
                for chunk in (metadata.grounding_chunks or [])[:max_results]:
                    web = getattr(chunk, "web", None)
                    title = web and getattr(web, "title", None)
                    if title:
                        snippets.append(title)

        # Fallback: split the AI-generated answer into paragraph-level snippets
        if not snippets and response.text:
            lines = [ln.strip() for ln in response.text.split("\n") if ln.strip()]
            snippets = lines[:max_results]

        return snippets[:max_results]

    except ImportError:
        logger.warning("google-genai not installed; web enrichment disabled")
        return []
    except Exception as exc:
        logger.warning("Gemini search failed for %r: %s", query, exc)
        return []
