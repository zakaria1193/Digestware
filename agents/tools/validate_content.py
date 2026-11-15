"""Pre-flight validation of generated Markdown before it reaches the site.

The nightly pipeline commits straight to `master`, and Cloudflare Pages builds
from `master` — so before this existed, a single malformed frontmatter block
took the public site's build down and the only signal was a failed deploy
hours later. This module is the gate: run it after generation and *before*
the commit step, so a bad file fails the pipeline loudly while the damage is
still confined to the runner.

It deliberately duplicates only the load-bearing subset of the Astro schema in
`web/src/content.config.ts` — the fields whose absence breaks the build. It is
a fast smoke test, not a replacement for `astro build`, which CI also runs.

Usage:
    python -m agents.tools.validate_content [--content-root web/src/content]
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

from agents.tools.frontmatter import load_frontmatter

# Fields required by the Astro collection schemas. Keep in sync with
# `web/src/content/config.ts`.
_REQUIRED: dict[str, tuple[str, ...]] = {
    "discussions": ("project", "subsystem", "source_type", "title", "headline",
                    "tldr", "url", "date"),
    "landings": ("project", "subsystem", "source_type", "headline", "tldr",
                 "url", "date"),
    "lessons": ("project", "subsystem", "lesson_id", "commit_hash",
                "source_type", "headline", "hook", "tldr", "concept",
                "url", "week_start", "week_end", "commit_date", "date"),
}

# Date-typed fields beyond `date` itself. These are non-nullable
# `z.coerce.date()` in the Astro schema, so an unparseable value fails the
# build exactly as a bad `date` would.
_EXTRA_DATE_FIELDS: dict[str, tuple[str, ...]] = {
    "lessons": ("week_start", "week_end", "commit_date"),
}


def validate_file(
    path: Path,
    required: tuple[str, ...],
    date_fields: tuple[str, ...] = (),
) -> list[str]:
    """Return a list of human-readable problems with `path` (empty when OK)."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"unreadable: {exc}"]

    parsed = load_frontmatter(text)
    if parsed is None:
        return ["missing or malformed YAML frontmatter"]
    fm, _body = parsed

    problems: list[str] = []
    for key in required:
        if fm.get(key) in (None, ""):
            problems.append(f"missing required field `{key}`")

    url = fm.get("url")
    if isinstance(url, str) and url and not url.startswith(("http://", "https://")):
        problems.append(f"`url` is not an absolute URL: {url!r}")

    for key in ("date", *date_fields):
        if not _is_valid_date(fm.get(key)):
            problems.append(f"`{key}` is not a valid date: {fm.get(key)!r}")

    return problems


def _is_valid_date(value: object) -> bool:
    """Mirror what Astro's `z.coerce.date()` will accept.

    `yaml.safe_load` returns a real `date` for an unquoted `YYYY-MM-DD`, but
    quoted values stay strings — both are fine as long as they parse.
    """
    if value is None:
        return False
    if isinstance(value, (date, datetime)):
        return True
    if isinstance(value, str):
        try:
            datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return False
        return True
    return False


def validate_content_root(content_root: Path) -> dict[Path, list[str]]:
    """Validate every collection file under `content_root`.

    Returns a mapping of offending path → problems. Empty means all good.
    """
    failures: dict[Path, list[str]] = {}
    for subdir, required in _REQUIRED.items():
        date_fields = _EXTRA_DATE_FIELDS.get(subdir, ())
        for path in sorted((content_root / subdir).glob("*.md")):
            problems = validate_file(path, required, date_fields)
            if problems:
                failures[path] = problems
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path("web/src/content"),
        help="Root of the Astro content collections.",
    )
    args = parser.parse_args(argv)

    failures = validate_content_root(args.content_root)
    if not failures:
        print(f"Content OK — no schema problems under {args.content_root}.")
        return 0

    for path, problems in failures.items():
        for problem in problems:
            # `::error::` renders as an annotation in the GitHub Actions UI.
            print(f"::error file={path}::{problem}")
    print(f"\n{len(failures)} file(s) would break the site build.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
