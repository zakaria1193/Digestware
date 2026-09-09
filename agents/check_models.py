"""Verify every configured model slug exists on OpenRouter, before spending.

Model slugs are strings, and a wrong one fails only at request time — after
the run has already paid for everything leading up to it. This project has
been bitten repeatedly: ``google/gemini-2.0-flash-001`` was retired upstream
and started returning 404 "No endpoints found", and — found by this module on
its very first real run — ``anthropic/claude-sonnet-4-5`` had **never
existed**. It is the premium re-run model for every `impact_score >= 9`
landing, so months of high-impact commits had been silently falling back to
the cheap summary with nothing anywhere saying so. The correct name uses a
dot: ``anthropic/claude-sonnet-4.5``.

``/models`` is a free, unauthenticated listing. Checking it takes a second and
turns a class of expensive, late, confusing failures into an immediate one
with a suggestion attached:

    python -m agents.check_models

Exits 0 when every slug resolves, 1 otherwise. Wire it into CI *before* any
step that spends tokens.
"""

from __future__ import annotations

import sys

import httpx

from agents._openrouter import (
    BASE_URL,
    DEFAULT_LESSON_RESEARCH_MODEL,
    DEFAULT_LESSON_WRITER_MODEL,
    DEFAULT_PREMIUM_MODEL,
    DEFAULT_SUMMARISER_MODEL,
    fetch_models,
    model_from_env,
)

#: `(env var, default)` for every model this codebase can call. Add a row here
#: when you add a model; the preflight then covers it for free.
CONFIGURED: list[tuple[str, str]] = [
    ("SUMMARISER_MODEL", DEFAULT_SUMMARISER_MODEL),
    ("BENTO_MODEL", DEFAULT_PREMIUM_MODEL),
    ("LESSON_RESEARCH_MODEL", DEFAULT_LESSON_RESEARCH_MODEL),
    ("LESSON_WRITER_MODEL", DEFAULT_LESSON_WRITER_MODEL),
]


def fetch_available(client: httpx.Client | None = None) -> set[str]:
    """Every model id OpenRouter currently serves."""
    return {
        entry["id"]
        for entry in fetch_models(client)
        if isinstance(entry.get("id"), str)
    }


def _family(slug: str) -> str:
    """The distinguishing word in a model name — `sonnet` in claude-sonnet-4-5.

    Vendor and common prefixes (`claude`, `gemini`, `gpt`) are shared across a
    vendor's whole catalogue, so they identify nothing. The next token is what
    tells one family from another.
    """
    name = slug.split("/")[-1]
    parts = [p for p in name.replace(".", "-").split("-") if p and not p.isdigit()]
    generic = {"claude", "gemini", "gpt", "llama", "mistral", "preview", "latest"}
    for part in parts:
        if part not in generic:
            return part
    return parts[0] if parts else name


def suggest(slug: str, available: set[str]) -> list[str]:
    """Plausible replacements for a slug that doesn't resolve.

    **Same family first, then same vendor.** A wrong slug is nearly always
    version drift within one family — `claude-sonnet-4-5` vs
    `claude-sonnet-4.5` — so the sibling versions are the answer. Ranking by
    vendor alone is not enough: `anthropic/*` is dozens of models, and an
    alphabetical cut at fifteen stops before `sonnet` ever appears. That is
    exactly what happened the first time this fired, leaving the replacement
    to be inferred from a naming convention instead of simply read.
    """
    vendor = slug.split("/", 1)[0]
    family = _family(slug)
    same_vendor = sorted(m for m in available if m.startswith(f"{vendor}/"))

    same_family = [m for m in same_vendor if family in m]
    rest = [m for m in same_vendor if family not in m]
    if same_family or rest:
        return same_family + rest

    return sorted(m for m in available if family and family in m)


def check(available: set[str] | None = None) -> list[str]:
    """Return the configured slugs that OpenRouter does not serve."""
    available = available if available is not None else fetch_available()
    missing: list[str] = []
    for env_var, default in CONFIGURED:
        slug = model_from_env(env_var, default)
        status = "ok" if slug in available else "MISSING"
        print(f"  [{status:>7}] {env_var:<22} {slug}")
        if slug not in available:
            missing.append(slug)
    return missing


def main() -> int:
    print(f"Checking configured model slugs against {BASE_URL}/models …")
    try:
        available = fetch_available()
    except Exception as exc:                     # noqa: BLE001
        # Never block a run on the checker itself being unable to reach the
        # listing — that would make a network blip worse than the bug this
        # guards against.
        print(f"::warning::could not reach the model listing ({exc}) — skipping")
        return 0

    print(f"OpenRouter currently serves {len(available)} models.\n")
    missing = check(available)
    if not missing:
        print("\nAll configured models resolve.")
        return 0

    print(f"\n::error::{len(missing)} configured model slug(s) do not exist.")
    for slug in missing:
        options = suggest(slug, available)
        print(f"\n  {slug} is not served by OpenRouter.")
        if options:
            print("  Closest available:")
            for option in options[:25]:
                print(f"    - {option}")
        else:
            print("  No similar model ids found.")
    print(
        "\nFix the default in agents/_openrouter.py, or set the matching "
        "env var / repo variable to a slug from the list above."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
