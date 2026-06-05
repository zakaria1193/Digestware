"""Shared OpenRouter client factory.

All LLM and AI-powered calls in this codebase go through OpenRouter.
This module is the single place that knows the base URL and reads the key,
so neither ever needs to be repeated elsewhere.
"""

import os

from openai import OpenAI
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

BASE_URL = "https://openrouter.ai/api/v1"

# Default model slugs live here — alongside the base URL and key — so a
# provider-side deprecation is a one-line change, not a repo-wide hunt. Both
# are overridable per run via the SUMMARISER_MODEL / BENTO_MODEL env vars.
#
# NOTE: google/gemini-2.0-flash-001 was retired by Google on 2026-06-01
# (OpenRouter then returns 404 "No endpoints found"). google/gemini-2.5-flash
# is the documented 1:1 replacement — same cheap Flash tier, 1M-token context.
DEFAULT_SUMMARISER_MODEL = "google/gemini-2.5-flash"
DEFAULT_PREMIUM_MODEL = "anthropic/claude-sonnet-4-5"


def _api_key() -> str:
    return os.environ.get("OPENROUTER_API_KEY", "")


def build_model(model_name: str) -> OpenAIModel:
    """Return a PydanticAI OpenAIModel routed through OpenRouter."""
    provider = OpenAIProvider(base_url=BASE_URL, api_key=_api_key())
    return OpenAIModel(model_name, provider=provider)


def build_client() -> OpenAI:
    """Return a raw OpenAI client routed through OpenRouter."""
    return OpenAI(base_url=BASE_URL, api_key=_api_key())
