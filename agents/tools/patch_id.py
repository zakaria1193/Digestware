"""patch_id — extract a stable git patch-id from a diff text.

Pipes the diff through `git patch-id --stable` and returns the 40-char hash,
or None if git is unavailable or the diff is empty/invalid.

This works for diffs from any source type (GitHub PR, public-inbox email, etc.)
because git patch-id operates purely on the diff content.
"""

import logging
import subprocess

logger = logging.getLogger(__name__)


def extract_patch_id(diff_text: str) -> str | None:
    """Return the stable git patch-id for *diff_text*, or None on failure.

    Args:
        diff_text: Raw unified diff (as a string).

    Returns:
        40-character hex string, or None.
    """
    if not diff_text or not diff_text.strip():
        return None
    try:
        result = subprocess.run(
            ["git", "patch-id", "--stable"],
            input=diff_text,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        # Output format: "<patch-id> <commit-id>\n"
        parts = result.stdout.strip().split()
        if parts:
            return parts[0]
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        logger.debug("extract_patch_id failed: %s", exc)
    return None
