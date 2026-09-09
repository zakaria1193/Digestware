"""SourceRepo — read-only navigation of a project's real source tree.

The lesson agent needs to *read the code*, not just the commit message. This
module gives it a local, offline view of the upstream tree:

    git clone --bare --filter=blob:none -- <mirror-url> agents/cache/<name>.git

A **bare, blobless** clone is the whole trick. Bare means no working tree to
check out (GCC is ~2 GB checked out; we never pay that). Blobless means the
clone carries commits and trees but downloads file *contents* lazily, only for
the handful of files the agent actually opens. Measured: GCC lands at ~640 MB,
which fits the CI cache comfortably and survives between nightly runs.

Every read is pinned to one commit-ish and served by git itself:

    git show <sha>:<path>          →  the file exactly as it was at that commit
    git grep -n <pat> <sha> -- ... →  a search of the tree at that commit

So the agent never fetches a sourceware web page, never scrapes, and never sees
a file from a different revision than the one it is writing about.

Security: URLs, branches, SHAs and pathspecs are validated against strict
allowlists before reaching a subprocess (git happily reads a leading ``-`` as
an option, e.g. ``--upload-pack=``). URL/branch validation is shared with
``agents.adapters.plain_git`` rather than duplicated.

Cost: ``grep_repo`` REFUSES an unscoped search. On a blobless clone a
tree-wide grep would lazily fault in every blob in the repository — the one
way this design becomes slow and expensive. Callers must name a pathspec; the
agent is seeded with the directories the commit's own diff touched.
"""

from __future__ import annotations

import logging
import re
import shutil
import subprocess
from pathlib import Path

from agents.adapters.plain_git import (
    GIT_TIMEOUT,
    validate_branch_name,
    validate_repo_url,
)

logger = logging.getLogger(__name__)

# Hard cap on the bytes any single tool call returns to the model. Keeps one
# runaway `git show` on a 40k-line file from eating the context window (and
# the token budget) in a single turn.
MAX_OUTPUT_BYTES = 8_192
_TRUNCATION_MARKER = "\n… [truncated — narrow the range or pathspec]"

# Lines returned by a single read_file call when the caller gives no range.
DEFAULT_READ_LINES = 120
MAX_READ_LINES = 400
MAX_GREP_HITS = 60

_SHA_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")
# Pathspecs are repo-relative POSIX paths, optionally with a `*` glob. No
# leading dash (git would read it as an option) and no `..` traversal.
_PATHSPEC_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9._/*+-]{0,255}$")


class SourceRepoError(RuntimeError):
    """Raised when the repo cannot be prepared (clone/fetch failure)."""


def validate_sha(sha: str) -> None:
    if not _SHA_RE.match(sha or ""):
        raise ValueError(f"Unsafe commit sha {sha!r}: must match {_SHA_RE.pattern}")


def validate_pathspec(path: str) -> None:
    if not _PATHSPEC_RE.match(path or ""):
        raise ValueError(
            f"Unsafe path {path!r}: must be a repo-relative path matching "
            f"{_PATHSPEC_RE.pattern}"
        )
    if ".." in path:
        raise ValueError(f"Unsafe path {path!r}: '..' traversal is not allowed")


def _cap(text: str) -> str:
    """Truncate *text* to MAX_OUTPUT_BYTES, appending a visible marker."""
    encoded = text.encode("utf-8", errors="replace")
    if len(encoded) <= MAX_OUTPUT_BYTES:
        return text
    clipped = encoded[:MAX_OUTPUT_BYTES].decode("utf-8", errors="ignore")
    return clipped + _TRUNCATION_MARKER


class SourceRepo:
    """A bare, blobless clone of one upstream project, read at one commit.

    Instances are cheap; ``ensure()`` does the (idempotent) clone-or-fetch and
    must be called before any read.
    """

    def __init__(
        self,
        project: str,
        repo_url: str,
        branch: str = "master",
        cache_dir: Path | None = None,
    ) -> None:
        validate_repo_url(repo_url)
        validate_branch_name(branch)
        self.project = project
        self.repo_url = repo_url
        self.branch = branch
        self._cache_dir = Path(cache_dir) if cache_dir else Path("agents/cache")
        safe_name = repo_url.rstrip("/").split("/")[-1]
        if not safe_name.endswith(".git"):
            safe_name += ".git"
        # Deliberately the same naming scheme PlainGitAdapter uses, so a repo
        # already cloned for ingestion is reused instead of cloned twice.
        self.path = self._cache_dir / safe_name

        # Set by ensure() when the clone is on disk but could not be refreshed.
        # Callers use this to widen their commit search rather than give up:
        # a clone that is a few days behind still explains code perfectly well,
        # it just cannot see the newest commits. See `main._run_lesson_step`.
        self.is_stale = False
        self.last_fetch_error: str | None = None

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def is_usable(self) -> bool:
        """True when ``self.path`` is a git repository we can actually read.

        Existence is not enough. An interrupted clone (a killed CI job, a
        cache restored mid-write) leaves a directory that looks like a clone
        and answers every read with an error. Trusting it is worse than having
        no clone at all: we would skip the re-clone, log "using cached state",
        and hand the model a dossier of `[error]` strings.
        """
        if not self.path.is_dir():
            return False
        try:
            self._git(["rev-parse", "--git-dir"])
            return True
        except (
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
            OSError,
        ):
            return False

    def ensure(self) -> None:
        """Clone the repo if absent, otherwise fetch. Idempotent.

        Failure is graded, not binary:

        * **Fetch fails over a good clone** → not an error. ``is_stale`` is
          set and the cached objects are served as-is. The clone still holds
          every commit up to the last successful fetch, which is the whole
          history bar a few days — plenty to teach from.
        * **No clone, or an unusable one we cannot replace** → ``SourceRepoError``.
          There is genuinely nothing to read.
        """
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            if self.is_usable():
                try:
                    self._git(["fetch", "--quiet", "origin"])
                    logger.debug("source_repo: fetched %s", self.repo_url)
                except (
                    subprocess.CalledProcessError,
                    subprocess.TimeoutExpired,
                ) as exc:
                    self.is_stale = True
                    self.last_fetch_error = str(exc)
                    logger.warning(
                        "source_repo: fetch failed for %s (%s) — falling back to "
                        "the cached clone, which may not have this week's commits",
                        self.repo_url,
                        exc,
                    )
                return

            logger.warning(
                "source_repo: %s exists but is not a readable git repo — "
                "discarding it and cloning fresh",
                self.path,
            )
            try:
                shutil.rmtree(self.path)
            except OSError as exc:
                raise SourceRepoError(
                    f"{self.path} is unusable and could not be removed: {exc}"
                ) from exc

        logger.info(
            "source_repo: blobless bare clone %s → %s", self.repo_url, self.path
        )
        try:
            self._git(
                [
                    "clone",
                    "--bare",
                    "--filter=blob:none",
                    "--quiet",
                    "--",
                    self.repo_url,
                    str(self.path),
                ],
                cwd=None,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            raise SourceRepoError(
                f"could not clone {self.repo_url}: {exc}"
            ) from exc

    def resolve(self, sha: str) -> bool:
        """True when *sha* exists in this clone.

        Mirror lag is routine — a commit can be on the mailing list minutes
        before it reaches the GitHub mirror. A miss means "pick a different
        subject", never a pipeline failure.
        """
        try:
            validate_sha(sha)
        except ValueError:
            return False
        try:
            self._git(["cat-file", "-e", f"{sha}^{{commit}}"])
            return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return False

    # ------------------------------------------------------------------
    # Read API — each method below is bound as an agent tool
    # ------------------------------------------------------------------

    def show_commit(self, sha: str) -> str:
        """Full commit message plus diffstat and patch, capped."""
        validate_sha(sha)
        out = self._git_or_msg(
            ["show", "--stat", "--patch", "--no-color", sha, "--"]
        )
        return _cap(out)

    def changed_paths(self, sha: str) -> list[str]:
        """Repo-relative paths the commit touched (deterministic, not a tool)."""
        validate_sha(sha)
        try:
            out = self._git(
                ["diff-tree", "--no-commit-id", "--name-only", "-r", sha]
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return []
        return [ln.strip() for ln in out.splitlines() if ln.strip()]

    def changed_dirs(self, sha: str) -> list[str]:
        """Distinct directories the commit touched — the default grep scope."""
        dirs: list[str] = []
        for p in self.changed_paths(sha):
            parent = str(Path(p).parent)
            d = "." if parent == "." else parent
            if d not in dirs:
                dirs.append(d)
        return dirs

    def list_dir(self, sha: str, path: str = ".") -> str:
        """List the entries of a directory as it existed at *sha*."""
        validate_sha(sha)
        spec = f"{sha}:" if path in ("", ".") else f"{sha}:{path.rstrip('/')}"
        if path not in ("", "."):
            validate_pathspec(path)
        return _cap(self._git_or_msg(["ls-tree", "--name-only", spec]))

    def read_file(
        self,
        sha: str,
        path: str,
        start_line: int = 1,
        end_line: int | None = None,
    ) -> str:
        """Return a line-numbered slice of *path* as it was at *sha*.

        Paged on purpose: whole files in this codebase run to tens of
        thousands of lines, and the agent should be reading the region it
        cares about, not the file.
        """
        validate_sha(sha)
        validate_pathspec(path)

        try:
            content = self._git(["show", f"{sha}:{path}"])
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            return f"[error] cannot read {path} at {sha[:12]}: {exc}"

        lines = content.splitlines()
        start = max(1, int(start_line))
        if end_line is None:
            end = start + DEFAULT_READ_LINES - 1
        else:
            end = int(end_line)
        end = min(end, start + MAX_READ_LINES - 1, len(lines))

        if start > len(lines):
            return f"[{path}] has {len(lines)} lines; {start} is past the end."

        numbered = "\n".join(
            f"{n:>6}  {lines[n - 1]}" for n in range(start, end + 1)
        )
        header = f"# {path} @ {sha[:12]} — lines {start}-{end} of {len(lines)}\n"
        return _cap(header + numbered)

    def grep_repo(self, sha: str, pattern: str, paths: list[str]) -> str:
        """Search the tree at *sha* for *pattern*, restricted to *paths*.

        ``paths`` is required. An unscoped grep over a blobless clone faults
        in every blob in the repository; scoping is what keeps this cheap.
        """
        validate_sha(sha)
        if not pattern or not pattern.strip():
            return "[error] grep_repo needs a non-empty pattern."
        if not paths:
            return (
                "[error] grep_repo needs at least one path to search under "
                "(e.g. ['gcc/', 'gcc/config/aarch64/']). An unscoped search "
                "of the whole tree is not permitted."
            )
        for p in paths:
            validate_pathspec(p)

        cmd = [
            "grep",
            "--no-color",
            "-n",
            "-I",                       # skip binary files
            f"--max-count={MAX_GREP_HITS}",
            "-e",
            pattern,                    # after -e, never parsed as an option
            sha,
            "--",
            *paths,
        ]
        try:
            out = self._git(cmd)
        except subprocess.CalledProcessError as exc:
            # git grep exits 1 on "no matches" — that is an answer, not a fault.
            if exc.returncode == 1:
                return f"No matches for {pattern!r} under {', '.join(paths)}."
            return f"[error] grep failed: {exc}"
        except subprocess.TimeoutExpired:
            return "[error] grep timed out — narrow the pathspec."

        hits = out.splitlines()[:MAX_GREP_HITS]
        # `git grep <rev>` prefixes every line with "<rev>:"; strip the noise.
        cleaned = [ln[len(sha) + 1:] if ln.startswith(f"{sha}:") else ln for ln in hits]
        return _cap("\n".join(cleaned)) if cleaned else "No matches."

    def find_symbol(self, sha: str, name: str, paths: list[str]) -> str:
        """Locate a function / struct / macro definition by name.

        A convenience wrapper over ``grep_repo`` with a definition-shaped
        pattern, so the agent doesn't have to hand-write one every time.
        """
        if not name or not name.strip():
            return "[error] find_symbol needs a symbol name."
        escaped = re.escape(name.strip())
        pattern = (
            rf"(^|[^A-Za-z0-9_])(#define\s+{escaped}\b"
            rf"|(struct|class|union|enum)\s+{escaped}\b"
            rf"|{escaped}\s*\()"
        )
        return self.grep_repo(sha, pattern, paths)

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _git_or_msg(self, args: list[str]) -> str:
        try:
            return self._git(args)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            return f"[error] git {args[0]} failed: {exc}"

    def _git(self, args: list[str], cwd: Path | None = ...) -> str:  # type: ignore[assignment]
        """Run a git command inside the bare clone and return stdout."""
        repo_cwd = self.path if cwd is ... else cwd
        result = subprocess.run(
            ["git", *args],
            cwd=repo_cwd,
            capture_output=True,
            text=True,
            check=True,
            timeout=GIT_TIMEOUT,
        )
        return result.stdout


def load_source_repos(
    config: dict, cache_dir: Path | None = None
) -> dict[str, SourceRepo]:
    """Build ``{project: SourceRepo}`` from the ``source_repos:`` block of sources.yml.

    Separate from the ``sources:`` block on purpose: those repos are *ingested*
    (commits become articles), these are *read* (code becomes explanation). A
    project can appear in either, both, or neither.
    """
    repos: dict[str, SourceRepo] = {}
    for project, entry in (config.get("source_repos") or {}).items():
        if not isinstance(entry, dict) or not entry.get("url"):
            logger.warning("source_repos.%s: missing 'url' — skipping", project)
            continue
        try:
            repos[project] = SourceRepo(
                project=project,
                repo_url=entry["url"],
                branch=entry.get("branch", "master"),
                cache_dir=cache_dir,
            )
        except ValueError as exc:
            logger.warning("source_repos.%s is invalid (%s) — skipping", project, exc)
    return repos
