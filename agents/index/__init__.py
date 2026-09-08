"""Pulse index — a derived, disposable SQLite view over the Markdown corpus.

The Markdown under ``web/src/content/`` remains the sole source of truth (per
root CLAUDE.md). Nothing here ever writes back to it. The index is rebuilt from
those files by ``python -m agents.index.build`` and can be deleted at any time
without data loss.
"""

from pathlib import Path

# Anchored to the package root — independent of cwd, matching agents/usage_log.py.
_INDEX_ROOT = Path(__file__).resolve().parent
REPO_ROOT = _INDEX_ROOT.parent.parent
DEFAULT_DB_PATH = _INDEX_ROOT / "pulse.db"
SCHEMA_PATH = _INDEX_ROOT / "schema.sql"
CONTENT_ROOT = REPO_ROOT / "web" / "src" / "content"

# Collection directory -> `kind` value stored on each row.
COLLECTIONS = {"landings": "landing", "discussions": "discussion"}
