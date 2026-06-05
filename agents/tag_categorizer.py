"""Tag categorizer — bucket per-project tags into a fixed taxonomy.

Runs once after the Writer (see agents.main STEP 5) and once at the end of the
nightly workflow. Walks every Markdown file under
``web/src/content/{discussions,landings}/``, groups tags by project, and
asks a cheap LLM to assign each tag to one of:

    architectures | components | topics | news | other

Output: one JSON file per project at
``web/src/data/tag-categories/<project>.json``. The Astro filter-bar consumes
those to group the overflow chips revealed by "Show all" under human-readable
category headers. If a project's JSON is missing the UI degrades gracefully to
the flat behaviour, so this module is best-effort — never raises into main.py.

Model: google/gemini-2.5-flash (cheap, one batched call per project).
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal, cast

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent

from agents._openrouter import DEFAULT_SUMMARISER_MODEL, build_model
from agents._retry import retry_with_backoff
from agents.usage_log import append_usage

logger = logging.getLogger("agents.tag_categorizer")

_DEFAULT_MODEL = DEFAULT_SUMMARISER_MODEL
_DEFAULT_CONTENT_ROOT = Path("web/src/content")
_DEFAULT_OUTPUT_ROOT = Path("web/src/data/tag-categories")

# Closed taxonomy — must stay in sync with CATEGORY_LABELS in
# web/src/pages/[project]/index.astro.
Category = Literal["architectures", "components", "topics", "news", "other"]
CATEGORIES: tuple[Category, ...] = (
    "architectures",
    "components",
    "topics",
    "news",
    "other",
)

_SYSTEM_PROMPT = """\
You are a toolchain-documentation librarian. Given a flat list of free-form
tags used across one open-source toolchain project, assign every tag to
exactly ONE of these buckets:

- architectures  — target CPU / ISA (aarch64, x86, x86-64, arm, risc-v,
                   mips, powerpc, s390, sparc, loongarch, SuperH, avr…)
- components     — internal subsystem, frontend, runtime module, or tool
                   (libstdc++, ipa, sra, ld, bfd, gas, fortran, c++, c,
                   modules, testsuite, gdb, malloc, tree-ssa…)
- topics         — cross-cutting theme or "major line" of work
                   (optimization, security, abi, refactoring, bugfix,
                   performance, regression, build, ci, cleanup, typing)
- news           — announcement, policy, governance, event, release process
                   (release, event, policy, announcement, meeting, vote,
                   licensing)
- other          — anything that clearly does not fit above

RULES:
- Every input tag MUST appear as a key in the output JSON — no omissions.
- Every value MUST be one of:
  "architectures", "components", "topics", "news", "other".
- Do not invent new categories. Do not add explanatory text.
- Output ONLY a single JSON object — no prose, no code fences.
"""


class TagCategorization(BaseModel):
    """Per-project tag → category map, written as JSON to disk."""

    model: str
    generated_at: datetime
    assignments: dict[str, Category] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Frontmatter scan
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_PROJECT_RE = re.compile(r"^project:\s*(\S.*?)\s*$")
_TAGS_EMPTY_RE = re.compile(r"^tags:\s*\[\s*\]\s*$")
_TAGS_BLOCK_RE = re.compile(r"^tags:\s*$")
_TAG_ITEM_RE = re.compile(r"^\s*-\s*(.+?)\s*$")


def _parse_frontmatter_tags(md_path: Path) -> tuple[str | None, list[str]]:
    """Return ``(project, tags)`` from a markdown file's YAML frontmatter.

    Minimal parser — only reads the first ``---`` block and pulls ``project:``
    plus the ``tags:`` list. Avoids pulling PyYAML in just for this pass.
    """
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None, []
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, []
    fm_lines = m.group(1).splitlines()

    project: str | None = None
    for line in fm_lines:
        pm = _PROJECT_RE.match(line)
        if pm:
            project = pm.group(1).strip().strip('"').strip("'")
            break

    tags: list[str] = []
    for i, line in enumerate(fm_lines):
        if _TAGS_EMPTY_RE.match(line):
            break
        if _TAGS_BLOCK_RE.match(line):
            for j in range(i + 1, len(fm_lines)):
                item = _TAG_ITEM_RE.match(fm_lines[j])
                if not item:
                    break
                raw = item.group(1).strip().strip('"').strip("'")
                if raw:
                    tags.append(raw)
            break
    return project, tags


def _collect_tags_by_project(content_root: Path) -> dict[str, list[str]]:
    """Walk discussions + landings; return ``{project: sorted-unique-tags}``."""
    buckets: dict[str, set[str]] = defaultdict(set)
    for sub in ("discussions", "landings"):
        d = content_root / sub
        if not d.is_dir():
            continue
        for md in d.glob("*.md"):
            project, tags = _parse_frontmatter_tags(md)
            if not project:
                continue
            for t in tags:
                buckets[project].add(t)
    return {k: sorted(v, key=str.lower) for k, v in buckets.items()}


# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.IGNORECASE)

# Deterministic fallback used by --dry-run and by the LLM-failure path when
# no previous JSON exists. Intentionally conservative: anything not matched
# here lands in "other" where the real LLM run will fix it up on the next
# workflow invocation. Matching is whole-word (hyphens/slashes count as word
# separators) so "ld" doesn't match "build".
_HEURISTIC_RULES: tuple[tuple[Category, tuple[str, ...]], ...] = (
    ("architectures", (
        "aarch64", "arm64", "arm", "x86-64", "x86_64", "x86", "i386", "i686",
        "amd64", "risc-v", "riscv", "mips", "powerpc", "ppc64", "ppc",
        "s390x", "s390", "sparc", "loongarch", "superh", "sh-elf",
        "avr", "wasm", "hppa", "m68k", "alpha", "nvptx", "bpf", "sve", "sme",
    )),
    ("components", (
        "libstdc++", "libstdc", "glibc", "binutils", "gcc", "g++", "gdb",
        "ipa", "sra", "rtl", "gimple", "tree-ssa", "ld", "bfd", "gas",
        "opcodes", "fortran", "cobol", "rust", "go", "c++", "cplusplus",
        "c", "modules", "testsuite", "malloc", "nptl", "dynamic-linker",
        "assembler", "linker", "frontend", "backend", "middle-end", "driver",
        "preprocessor", "jit", "libgcc", "libgomp", "libatomic", "autofdo",
        "gcov", "lto",
    )),
    ("topics", (
        "optimization", "optimisation", "performance", "perf", "security",
        "cve", "hardening", "abi", "api", "refactor", "refactoring",
        "cleanup", "bugfix", "bug-fix", "regression", "build", "configure",
        "ci", "cd", "typing", "warning", "diagnostic", "diagnostics",
        "documentation", "docs", "flags", "option", "debug", "debugging",
        "testing", "coverage", "stability", "portability", "interoperability",
        "code cleanup", "tree-optimization",
    )),
    ("news", (
        "release", "release candidate", "announcement", "event", "policy",
        "meeting", "vote", "licensing", "license", "governance", "committee",
        "rfc", "draft", "proposal",
    )),
)


def _normalise(text: str) -> str:
    """Lowercase + collapse non-alnum runs to single spaces (keeps ``+`` so
    ``c++`` survives)."""
    return re.sub(r"[^a-z0-9+]+", " ", text.lower()).strip()


def _heuristic_category(tag: str) -> Category:
    norm = _normalise(tag)
    words = set(norm.split())
    for cat, keywords in _HEURISTIC_RULES:
        for kw in keywords:
            kw_norm = _normalise(kw)
            if " " in kw_norm:
                if kw_norm in norm:
                    return cat
            elif kw_norm in words:
                return cat
    return "other"


def _fallback_assignments(tags: list[str]) -> dict[str, Category]:
    return {t: _heuristic_category(t) for t in tags}


def _call_llm(
    model_name: str, project: str, tags: list[str]
) -> dict[str, Category]:
    """Single batched LLM call. Raises on failure (caller handles fallback)."""
    agent: Agent[None, str] = Agent(
        model=build_model(model_name),
        output_type=str,
        system_prompt=_SYSTEM_PROMPT,
    )
    prompt = (
        f"Project: {project}\n"
        f"Tags ({len(tags)}):\n"
        + "\n".join(f"- {t}" for t in tags)
        + "\n\nReturn ONE JSON object whose keys are EXACTLY the tags listed "
        "above (same casing, no extras) and whose values are one of: "
        "architectures, components, topics, news, other."
    )

    def _call() -> dict[str, Category]:
        r = agent.run_sync(prompt)
        append_usage("tag_categorizer", model_name, r.usage())
        text = _FENCE_RE.sub("", r.output.strip())
        data = json.loads(text)
        if not isinstance(data, dict):
            raise ValueError(
                f"LLM did not return a JSON object: {type(data).__name__}"
            )

        valid: set[str] = set(CATEGORIES)
        out: dict[str, Category] = {}
        for t in tags:
            v = data.get(t)
            out[t] = v if isinstance(v, str) and v in valid else "other"  # type: ignore[assignment]
        return out

    return retry_with_backoff(_call, label=f"tag_categorizer/{project}")


# ---------------------------------------------------------------------------
# Previous-file fallback
# ---------------------------------------------------------------------------

def _load_previous(output_path: Path) -> dict[str, Category] | None:
    if not output_path.exists():
        return None
    try:
        raw = json.loads(output_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    prev = raw.get("assignments") if isinstance(raw, dict) else None
    if not isinstance(prev, dict):
        return None
    valid: set[str] = set(CATEGORIES)
    out: dict[str, Category] = {}
    for t, c in prev.items():
        if not isinstance(t, str):
            continue
        out[t] = cast(Category, c) if isinstance(c, str) and c in valid else "other"
    return out


# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------

def _write_atomic(path: Path, payload: TagCategorization) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(
            payload.model_dump(mode="json"),
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def run_tag_categorizer(
    content_root: Path,
    output_root: Path,
    *,
    dry_run: bool = False,
    model_name: str | None = None,
) -> int:
    """Categorize tags per project. Returns number of projects handled."""
    by_project = _collect_tags_by_project(content_root)
    if not by_project:
        logger.info(
            "No tags found under %s — nothing to categorize.", content_root
        )
        return 0

    effective_model = model_name or os.environ.get(
        "SUMMARISER_MODEL", _DEFAULT_MODEL
    )

    handled = 0
    for project, tags in sorted(by_project.items()):
        output_path = output_root / f"{project}.json"
        assignments: dict[str, Category]

        if dry_run or not tags:
            assignments = _fallback_assignments(tags)
            provenance = "dry-run" if dry_run else "empty"
        else:
            try:
                assignments = _call_llm(effective_model, project, tags)
                provenance = effective_model
            except Exception as exc:
                logger.warning(
                    "tag_categorizer: LLM failed for project=%s (%s) — "
                    "falling back to previous JSON or all-other.",
                    project,
                    exc,
                )
                prev = _load_previous(output_path)
                if prev is not None:
                    assignments = {
                        t: prev[t] if t in prev else _heuristic_category(t)
                        for t in tags
                    }
                    provenance = "fallback-previous"
                else:
                    assignments = _fallback_assignments(tags)
                    provenance = "fallback-all-other"

        payload = TagCategorization(
            model=provenance,
            generated_at=datetime.now(tz=timezone.utc),
            assignments=assignments,
        )
        _write_atomic(output_path, payload)

        counts: dict[str, int] = defaultdict(int)
        for c in assignments.values():
            counts[c] += 1
        breakdown = ", ".join(
            f"{c}={counts[c]}" for c in CATEGORIES if counts[c]
        )
        logger.info(
            "tag_categorizer: %s → %d tag(s) via %s (%s)",
            project, len(tags), provenance, breakdown or "empty",
        )
        handled += 1

    return handled


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Categorize per-project tags into the closed taxonomy."
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=_DEFAULT_CONTENT_ROOT,
        help=f"Content root (default: {_DEFAULT_CONTENT_ROOT})",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=_DEFAULT_OUTPUT_ROOT,
        help=f"Output directory (default: {_DEFAULT_OUTPUT_ROOT})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip the LLM call — assign every tag to 'other'.",
    )
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S",
    )

    if not args.dry_run and not os.environ.get("OPENROUTER_API_KEY"):
        logger.error(
            "OPENROUTER_API_KEY is not set. Use --dry-run for a stub run."
        )
        return 2

    handled = run_tag_categorizer(
        args.content_root,
        args.output_root,
        dry_run=args.dry_run,
    )
    logger.info("tag_categorizer: wrote %d project file(s)", handled)
    return 0


if __name__ == "__main__":
    sys.exit(main())
