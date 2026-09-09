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

# ── Lesson of the Week ──────────────────────────────────────────────────────
#
# Generating a lesson is split across TWO models, and the split is the whole
# reason the feature fits the budget.
#
# A lesson is written by navigating the project's real source tree: many turns,
# each one resending the entire conversation so far. Token spend therefore
# grows *quadratically* with tool calls — the worst possible shape to pay
# premium rates for. Running a top-tier model through a 16-call loop costs
# several euro per article; the whole project's ceiling is EUR 5/month.
#
# So: a cheap reasoning model does the exploring and hands over a structured
# dossier (agents.models.lesson.LessonResearch), then ONE call to a top-tier
# model turns that dossier into the article. The reader gets premium prose; we
# pay premium rates for a single non-agentic call.
#
# RESEARCH — needs reliable multi-turn tool-calling and enough context to hold
# several source files. The -lite tier used for bulk summarising is not up to
# it. This runs at most twice a week, so the reasoning tier is affordable here
# in a way it never was in the per-article digest path.
DEFAULT_LESSON_RESEARCH_MODEL = "google/gemini-2.5-flash"
#
# WRITER — one call, no tools, no conversation to resend. Opus-tier by explicit
# request: the lesson is the only long-form prose on the site and it is what a
# reader judges the publication by.
#
# BUDGET: ~2 lessons/week is ~8-9 runs/month. Verify real spend in the
# ``lesson_research`` / ``lesson_writer`` rows of agents/output/usage.log
# BEFORE enabling the nightly step. If it overruns, the levers in order are
# (1) _MAX_TOOL_CALLS in lesson_agent.py and (2) the dossier size caps in
# models/lesson.py — which drive the writer's input tokens. Do not silently
# downgrade the writer; Opus-level prose is the requirement.
#
# NOTE: confirm this slug against https://openrouter.ai/api/v1/models before
# the first paid run. Anthropic's own id is ``claude-opus-5``; OpenRouter
# namespaces it under the provider.
DEFAULT_LESSON_WRITER_MODEL = "anthropic/claude-opus-5"


def model_from_env(key: str, default: str) -> str:
    """The model named by env var *key*, falling back to *default*.

    Why this exists instead of ``os.environ.get(key, default)``: that returns
    the default only when the key is **absent**. GitHub Actions sets an
    unconfigured `${{ vars.X }}` as *present and empty*, so the plain form
    yields `""`, and an empty model slug fails every request. That is not
    hypothetical — it is what turned the first real Lesson of the Week run
    into two `research_failed` stubs.

    Treats whitespace-only as unset too, for the same reason.
    """
    value = (os.environ.get(key) or "").strip()
    if not value:
        return default
    return value


def _api_key() -> str:
    return os.environ.get("OPENROUTER_API_KEY", "")


def build_model(model_name: str) -> OpenAIChatModel:
    """Return a PydanticAI OpenAIChatModel routed through OpenRouter."""
    provider = OpenAIProvider(base_url=BASE_URL, api_key=_api_key())
    return OpenAIChatModel(model_name, provider=provider)


def build_client() -> OpenAI:
    """Return a raw OpenAI client routed through OpenRouter."""
    return OpenAI(base_url=BASE_URL, api_key=_api_key())
