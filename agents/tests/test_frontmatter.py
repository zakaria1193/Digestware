"""Tests for the shared frontmatter splitter.

The regression these guard: a value containing `---` used to be treated as the
closing fence by `text.split("---", 2)`, truncating the frontmatter and
silently dropping every key after it.
"""

from __future__ import annotations

import pytest

from agents.tools.frontmatter import (
    dump_frontmatter,
    load_frontmatter,
    render,
    split_frontmatter,
)


# The real-world file that broke the Cloudflare Pages build: `---` appears
# inside `primer_expert`, and `url`/`date` come after it.
def _split(text: str) -> tuple[str, str]:
    """`split_frontmatter` with the None case asserted away."""
    parsed = split_frontmatter(text)
    assert parsed is not None
    return parsed


def _load(text: str) -> tuple[dict, str]:
    """`load_frontmatter` with the None case asserted away."""
    parsed = load_frontmatter(text)
    assert parsed is not None
    return parsed


DOC_WITH_INLINE_MARKER = """---
project: binutils
primer_expert: The changes involve correcting indentation, ensuring proper
  document start markers (`---`), and fixing whitespace errors.
url: https://example.com/a
date: 2026-07-28
---

Body text.
"""


class TestSplitFrontmatter:
    def test_simple_document(self):
        fm, body = _split("---\nkey: value\n---\n\nBody.\n")
        assert fm == "key: value\n"
        assert body == "\nBody.\n"

    def test_inline_marker_is_not_a_fence(self):
        fm, _body = _split(DOC_WITH_INLINE_MARKER)
        assert "url: https://example.com/a" in fm
        assert "date: 2026-07-28" in fm

    def test_body_containing_marker_is_untouched(self):
        text = "---\nkey: value\n---\n\nA line.\n\n---\n\nAnother line.\n"
        fm, body = _split(text)
        assert fm == "key: value\n"
        assert body == "\nA line.\n\n---\n\nAnother line.\n"

    @pytest.mark.parametrize(
        "text",
        [
            "no frontmatter at all\n",
            "---\nkey: value\nnever closed\n",
            "\n---\nkey: value\n---\n",  # fence must open the file
        ],
    )
    def test_rejects_unfenced_documents(self, text):
        assert split_frontmatter(text) is None


class TestLoadFrontmatter:
    def test_keys_after_inline_marker_survive(self):
        fm, body = _load(DOC_WITH_INLINE_MARKER)
        assert fm["url"] == "https://example.com/a"
        assert str(fm["date"]) == "2026-07-28"
        assert "`---`" in fm["primer_expert"]
        assert body.strip() == "Body text."

    def test_malformed_yaml_returns_none(self):
        assert load_frontmatter("---\nkey: [unclosed\n---\n\nBody.\n") is None

    def test_non_mapping_returns_none(self):
        assert load_frontmatter("---\n- a\n- b\n---\n\nBody.\n") is None


class TestRoundTrip:
    def test_render_preserves_body_and_survives_reparse(self):
        fm, body = _load(DOC_WITH_INLINE_MARKER)
        fm["is_stub"] = True
        reparsed, reparsed_body = _load(render(fm, body))
        assert reparsed == fm
        assert reparsed_body == body

    def test_value_containing_marker_is_quoted_on_dump(self):
        # An *unindented* `---` line inside the emitted YAML would read as a
        # document separator — exactly how the original corruption happened.
        # PyYAML quotes and indents the value, so no line starts at column 0.
        dumped = dump_frontmatter({"note": "before\n---\nafter", "url": "u"})
        assert not any(line.startswith("---") for line in dumped.splitlines())
        reparsed, _ = _load(f"---\n{dumped}---\n\nBody.\n")
        assert reparsed["note"] == "before\n---\nafter"
        assert reparsed["url"] == "u"

    def test_dump_preserves_key_order(self):
        fm = {"z": 1, "a": 2, "m": 3}
        assert list(_load(render(fm, "\nBody.\n"))[0]) == ["z", "a", "m"]
