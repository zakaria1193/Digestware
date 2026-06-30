"""Shared OpenRouter client factory.

All LLM and AI-powered calls in this codebase go through OpenRouter.
This module is the single place that knows the base URL and reads the key,
so neither ever needs to be repeated elsewhere.
"""

import os

from openai import OpenAI
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

BASE_URL = "https://openrouter.ai/api/v1"

# Default model slugs live here — alongside the base URL and key — so a
# provider-side deprecation is a one-line change, not a repo-wide hunt. Both
# are overridable per run via the SUMMARISER_MODEL / BENTO_MODEL env vars.
#
# NOTE: google/gemini-2.0-flash-001 was retired by Google on 2026-06-01
# (OpenRouter then returns 404 "No endpoints found").
#
# We use the *-lite* tier for the bulk summariser path: google/gemini-2.5-flash
# is a reasoning model that emits billed "thinking" tokens by default, which
# blew the €5/month budget (~$3.46 in a single cycle). gemini-2.5-flash-lite is
# the cheap, non-reasoning Flash tier (thinking off by default) — same 1M-token
# context, a fraction of the per-call cost — and is the right fit for the
# high-volume per-item digest work. Premium depth still comes from the Sonnet
# re-run on impact_score >= 9 items.
DEFAULT_SUMMARISER_MODEL = "google/gemini-2.5-flash-lite"
DEFAULT_PREMIUM_MODEL = "anthropic/claude-sonnet-4-5"


def _api_key() -> str:
    return os.environ.get("OPENROUTER_API_KEY", "")


def build_model(model_name: str) -> OpenAIChatModel:
    """Return a PydanticAI OpenAIChatModel routed through OpenRouter."""
    provider = OpenAIProvider(base_url=BASE_URL, api_key=_api_key())
    return OpenAIChatModel(model_name, provider=provider)


def build_client() -> OpenAI:
    """Return a raw OpenAI client routed through OpenRouter."""
    return OpenAI(base_url=BASE_URL, api_key=_api_key())
