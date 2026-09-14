"""Shared OpenRouter client factory.

All LLM and AI-powered calls in this codebase go through OpenRouter.
This module is the single place that knows the base URL and reads the key,
so neither ever needs to be repeated elsewhere.
"""

import os

from openai import OpenAI
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.settings import ModelSettings

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
DEFAULT_PREMIUM_MODEL = "anthropic/claude-sonnet-4.5"

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
# VERIFIED 2026-09-09 against https://openrouter.ai/api/v1/models: this slug is
# served. `python -m agents.check_models` re-checks it (and every other
# configured slug) before any step that spends tokens, so a provider-side
# rename fails in seconds rather than after a paid loop. That preflight is how
# `anthropic/claude-sonnet-4-5` was caught: it had never existed, so every
# premium digest re-run had been silently falling back to the cheap summary.
DEFAULT_LESSON_WRITER_MODEL = "anthropic/claude-opus-5"

# OpenRouter does not bill max_tokens — but it does *reserve* against it, and
# rejects the request outright with a 402 when the key's remaining balance
# cannot cover the reservation. Sending no max_tokens means the model's own
# ceiling applies, which for claude-opus-5 is 65536 output tokens; with a
# nearly-spent balance that is an unaffordable reservation and every writer
# call fails before a single token is generated. That is exactly what turned
# the 2026-09-13 and -14 lessons into `writer_failed` stubs: "You requested up
# to 65536 tokens, but can only afford 49590."
#
# A lesson cannot approach that ceiling anyway. LessonDigest caps the article
# at 8 sections x 4000 chars plus the surrounding fields — roughly 45k
# characters, ~13k tokens of JSON at the absolute maximum. 20000 leaves ample
# headroom while cutting the reservation to under a third, so the call fits in
# a balance that the unbounded default does not. Raise it only if a real
# article is ever observed truncating.
LESSON_WRITER_MAX_TOKENS = 9000
# 20000 until 2026-09-14, when the key's balance stopped covering the
# reservation: "You requested up to 20000 tokens, but can only afford 10383",
# then 9840 once a larger dossier raised the input side of the same sum.
# The measured size of a real, complete six-section lesson is 7832 output
# tokens, so 10000 keeps ~28% headroom over observed while fitting what the
# balance allows. This number tracks a balance, not a quality decision — put it
# back up once the key is topped up, and read the 402's "can only afford N"
# rather than guessing if it bites again.


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


MODELS_TIMEOUT = 30


def fetch_models(client: object | None = None) -> list[dict]:
    """Every model OpenRouter currently serves, with its per-token pricing.

    ``/models`` is free and needs no key. Two callers depend on it: the slug
    preflight (``agents.check_models``) and the budget ledger
    (``agents.budget``), which prices ``output/usage.log`` from the
    ``pricing`` block each entry carries. It lives here because this module is
    the single place that knows the base URL.

    Raises on transport or HTTP errors — callers decide whether that is fatal.
    """
    import httpx

    owns_client = client is None
    http = client if client is not None else httpx.Client(timeout=MODELS_TIMEOUT)
    try:
        response = http.get(f"{BASE_URL}/models")  # type: ignore[attr-defined]
        response.raise_for_status()
        payload = response.json()
    finally:
        if owns_client:
            http.close()  # type: ignore[attr-defined]
    data = payload.get("data", [])
    return [entry for entry in data if isinstance(entry, dict)]


def build_model(model_name: str, *, max_tokens: int | None = None) -> OpenAIChatModel:
    """Return a PydanticAI OpenAIChatModel routed through OpenRouter.

    ``max_tokens`` caps the output reservation. See LESSON_WRITER_MAX_TOKENS
    for why that matters on OpenRouter even though the reservation itself is
    never billed.
    """
    provider = OpenAIProvider(base_url=BASE_URL, api_key=_api_key())
    settings = ModelSettings(max_tokens=max_tokens) if max_tokens else None
    return OpenAIChatModel(model_name, provider=provider, settings=settings)


def build_client() -> OpenAI:
    """Return a raw OpenAI client routed through OpenRouter."""
    return OpenAI(base_url=BASE_URL, api_key=_api_key())
