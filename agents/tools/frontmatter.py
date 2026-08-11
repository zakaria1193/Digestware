"""Shared YAML-frontmatter parsing for the on-disk Markdown content.

`text.split("---", 2)` is *not* a safe way to fence frontmatter. `---` is a
perfectly legal substring of a YAML value — an article about the YAML
document-start marker, a commit that mentions `---` in a diff header, an
em-dash-ish run in prose — and splitting on the first bare occurrence
truncates the block mid-value. When the truncated half is then written back
out, the closing fence lands inside a string and every key after it silently
disappears from the frontmatter, which surfaces much later as an Astro
schema error at build time.

Everything here anchors on `---` alone on its own line, which is the only
form Astro's frontmatter parser treats as a delimiter.
"""
from __future__ import annotations

import re

import yaml

# Opening fence, the YAML block (non-greedy), then a closing fence that must
# start its own line. MULTILINE makes `^` match at line starts; DOTALL lets
# the block and body span newlines.
_FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\n(?P<fm>.*?)^---[ \t]*\n?(?P<body>.*)\Z",
    re.DOTALL | re.MULTILINE,
)


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """Split raw file text into (frontmatter_text, body).

    Returns None when the text has no line-anchored `---` fenced block.
    """
    match = _FRONTMATTER_RE.match(text)
    if match is None:
        return None
    return match.group("fm"), match.group("body")


def load_frontmatter(text: str) -> tuple[dict, str] | None:
    """Parse file text into (frontmatter_dict, body).

    Returns None when there is no fenced block, when the YAML is malformed,
    or when it does not parse to a mapping.
    """
    split = split_frontmatter(text)
    if split is None:
        return None
    fm_text, body = split
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None
    return fm, body


def dump_frontmatter(frontmatter: dict) -> str:
    """Serialise a frontmatter mapping to YAML (no fences).

    Always emits block style with insertion order preserved, so a value
    containing `---` comes back correctly quoted rather than as a bare line
    that would read as a document separator.
    """
    return yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )


def render(frontmatter: dict, body: str) -> str:
    """Re-render a fenced document, preserving `body` verbatim.

    `body` is the remainder as returned by `split_frontmatter` — it already
    carries its own leading blank line, so nothing is inserted here.
    """
    return f"---\n{dump_frontmatter(frontmatter)}---\n{body}"
