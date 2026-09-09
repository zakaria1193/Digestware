# Phase 2 — The Bimodal Agent Engine (PydanticAI)

Build a Python digest engine with a **protocol-based adapter layer** so any
repository source (GitHub, GitLab, Sourceware public-inbox, plain Git) can feed
the same two PydanticAI agents — one for discussions ("Lab"), one for landed
commits ("Factory") — cross-linked via `patch_id`.

---

## Repository layout after Phase 2

```
agents/
├── adapters/               # Source adapters (one per platform)
│   ├── __init__.py         # DiscussionSource + CommitSource Protocols
│   ├── github.py           # GitHubAdapter
│   ├── public_inbox.py     # PublicInboxAdapter (Sourceware)
│   └── plain_git.py        # PlainGitAdapter (commit-only)
├── ingestion/
│   └── engine.py           # IngestionEngine — fan-out across adapters
├── models/
│   ├── raw.py              # RawDiscussion, RawCommit (source-agnostic)
│   ├── base.py             # BimodalBase, ConsensusStatus
│   ├── discussion.py       # DiscussionDigest
│   └── landing.py          # LandingDigest
├── tools/
│   ├── patch_id.py         # git patch-id --stable wrapper
│   └── web_search.py       # DuckDuckGo enrichment
├── discussion_agent.py
├── landing_agent.py
├── writer.py
├── main.py
├── sources.yml             # Declares which adapters to activate
└── tests/
    ├── conftest.py
    ├── test_models.py
    ├── test_writer.py
    └── test_adapters.py
```

---

## 1. Source-agnostic intermediate structs (`agents/models/raw.py`)

All adapters normalise their platform-specific data into these two dataclasses
before anything else in the pipeline sees it.

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class RawDiscussion:
    id: str               # PR number, Message-ID, issue URL — source's natural key
    title: str
    body: str
    author: str
    date: datetime
    url: str
    replies: list[dict]   # comments, review threads, email replies
    diff_text: str | None # patch/diff if attached
    source_type: str      # "github_pr" | "gitlab_mr" | "public_inbox"
    metadata: dict = field(default_factory=dict)  # source-specific pass-through

@dataclass
class RawCommit:
    sha: str
    author: str
    date: datetime
    message: str
    diff_stat: str
    url: str
    source_type: str      # "github" | "gitlab" | "public_inbox" | "plain_git"
    metadata: dict = field(default_factory=dict)
```

---

## 2. Adapter protocols (`agents/adapters/__init__.py`)

```python
from typing import Protocol
from agents.models.raw import RawDiscussion, RawCommit

class DiscussionSource(Protocol):
    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]: ...

class CommitSource(Protocol):
    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]: ...
```

---

## 3. Concrete adapters

### `agents/adapters/github.py` — `GitHubAdapter`
Implements both `DiscussionSource` and `CommitSource`.

```python
class GitHubAdapter:
    def __init__(self, owner: str, repo: str, token: str | None = None): ...
```

- **Discussions** → GitHub REST `GET /repos/{owner}/{repo}/pulls?state=open&sort=updated`
  - Fetch PR body + review comments via `GET /pulls/{pr}/comments`
  - Maps: PR → `RawDiscussion(source_type="github_pr", id=str(pr_number))`
- **Commits** → `GET /repos/{owner}/{repo}/commits?since={since_date}`
  - Maps: commit → `RawCommit(source_type="github")`
- Uses `GITHUB_TOKEN` env var if set (raises rate limit from 60 → 5000 req/hr)
- All HTTP via `httpx.AsyncClient`

### `agents/adapters/public_inbox.py` — `PublicInboxAdapter`
Implements both `DiscussionSource` and `CommitSource`.

```python
class PublicInboxAdapter:
    def __init__(self, discussion_lists: list[str], cvs_lists: list[str],
                 cache_dir: Path, use_nntp: bool = True): ...
```

- **Discussions** (mailing list threads):
  - `git clone --mirror https://inbox.sourceware.org/{list}/0` → cache; `git fetch` on repeat
  - Handle epochs `/0`, `/1`, `/2` automatically
  - `git log --format=%H` → `git show <sha>:m` → parse mbox headers
  - Falls back to NNTP (`nntplib`, stdlib) for real-time when `use_nntp=True`
  - Maps: thread → `RawDiscussion(source_type="public_inbox", id=message_id)`
- **Commits** (CVS notification lists): same mirror approach on `gcc-cvs`, `glibc-cvs`
  - Maps: CVS email → `RawCommit(source_type="public_inbox")`
- Graceful NNTP fallback: unreachable → `[]` + warning log
- Saves raw mbox bytes to `agents/cache/raw/{message_id}.mbox`

### `agents/adapters/plain_git.py` — `PlainGitAdapter`
Implements `CommitSource` only (no PR/discussion concept).

```python
class PlainGitAdapter:
    def __init__(self, repo_url: str, branch: str = "master",
                 cache_dir: Path | None = None): ...
```

- `git clone --bare` on first run; `git fetch` on repeat
- `git log {branch} --since={since_date} --format=...` via subprocess
- Maps: commit → `RawCommit(source_type="plain_git")`

---

## 4. Ingestion engine (`agents/ingestion/engine.py`)

```python
class IngestionEngine:
    def __init__(
        self,
        discussion_sources: list[DiscussionSource],
        commit_sources: list[CommitSource],
    ): ...

    def run(self, since_hours: int = 24) -> dict[str, list]:
        discussions = [d for src in self.discussion_sources
                         for d in src.fetch_discussions(since_hours)]
        commits     = [c for src in self.commit_sources
                         for c in src.fetch_commits(since_hours)]
        # deduplicate by id / sha
        return {"discussions": discussions, "commits": commits}
```

---

## 5. Config (`agents/sources.yml`)

Declares which adapters to activate. `main.py` reads this to wire up `IngestionEngine`.

```yaml
sources:
  - type: github
    owner: gcc-mirror
    repo: gcc

  - type: public_inbox
    discussion_lists: [gcc, libc-alpha]
    cvs_lists: [gcc-cvs, glibc-cvs]
    use_nntp: true

  - type: plain_git
    url: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
    branch: master
```

---

## 6. Output data models (`agents/models/`)

### `agents/models/base.py`
```python
class ConsensusStatus(str, Enum):
    PROPOSED        = "Proposed"
    UNDER_REVIEW    = "Under Review"
    NEEDS_REVISION  = "Needs Revision"
    NACKED          = "NACK'd"
    READY_TO_LAND   = "Ready to Land"
    COMMITTED       = "Committed"

class BimodalBase(BaseModel):
    project:   str
    subsystem: str
    patch_id:  str | None = None   # git patch-id --stable for cross-referencing
```

### `agents/models/discussion.py`
```python
class DiscussionDigest(BimodalBase):
    discussion_id:       str        # adapter's natural key (PR#, message_id, …)
    source_type:         str        # preserved from RawDiscussion
    title:               str
    proposer:            str
    consensus:           ConsensusStatus
    sentiment_score:     int = Field(..., ge=1, le=10)
    technical_tradeoffs: list[str]
    summary:             str
    url:                 str
    bugzilla_url:        str | None = None
```

### `agents/models/landing.py`
```python
class LandingDigest(BimodalBase):
    commit_hash:         str
    source_type:         str        # preserved from RawCommit
    author:              str
    impact_score:        int = Field(..., ge=1, le=10)
    performance_win:     bool = False
    breaking_change:     bool = False
    summary:             str
    discussion_id_link:  str | None = None  # cross-ref back to DiscussionDigest
    bugzilla_pr:         int | None = None
    url:                 str
```

`discussion_id` replaces the old `message_id` / `pr_number` split — the agent
populates it regardless of source type using the `discussion_id` from `RawDiscussion`.

---

## 7. Tools (`agents/tools/`)

**`patch_id.py`** — `extract_patch_id(diff_text: str) -> str | None`
Pipes diff through `git patch-id --stable`; works for any source type.

**`web_search.py`** — `search_context(query: str) -> list[str]`
Top-5 DuckDuckGo snippets. Called for cryptic titles (< 20 words, no subsystem keyword).

---

## 8. Agents

Both agents receive `list[RawDiscussion]` / `list[RawCommit]`. The `source_type`
field is included in the prompt so the model adapts its heuristics:
- `github_pr` → look for review approvals / `changes_requested`
- `public_inbox` → look for ACK / NACK patterns
- `plain_git` → commit-body-only analysis

**`agents/discussion_agent.py`** — `Agent[None, list[DiscussionDigest]]`
- Model: `google/gemini-2.5-flash`
- Registered tools: `web_search`, `patch_id`
- **Batching**: 10 discussions per LLM call

**`agents/landing_agent.py`** — `Agent[None, list[LandingDigest]]`
- Model: `google/gemini-2.5-flash`; re-run with `anthropic/claude-sonnet-4.5` if `impact_score >= 9`
- Scan commit message for `Closes #N`, `Message-Id:`, `Link:`, `PR \d+` trailers
- **Batching**: 15 commits per LLM call

Both agents: capture `result.usage()` → JSON-line append to `agents/output/usage.log`

---

## 9. Writer (`agents/writer.py`)

- `write_discussion(d: DiscussionDigest, output_dir: Path) -> Path`
  → `web/src/content/discussions/YYYY-MM-DD-<slug>.md`
- `write_landing(l: LandingDigest, output_dir: Path) -> Path`
  → `web/src/content/landings/YYYY-MM-DD-<slug>.md`
- Slug: `re.sub(r'[^\w]+', '-', title.lower()).strip('-')`
- Format: YAML frontmatter (all model fields) + blank line + `summary` prose body

---

## 10. Entry point (`agents/main.py`)

```
python -m agents.main --since-hours 24 [--dry-run]
```

1. `load_dotenv()`
2. Parse `agents/sources.yml` → instantiate adapters
3. `IngestionEngine(discussion_sources, commit_sources).run(since_hours)`
4. Batch-run `DiscussionAgent` on discussions
5. Batch-run `LandingAgent` on commits
6. `write_discussion()` / `write_landing()` for each result
7. Print summary: N discussions, N landings (N bento-worthy = score ≥ 7)

---

## 11. Tests (`agents/tests/`)

- `conftest.py` — fixtures: `sample_raw_discussion`, `sample_raw_commit`,
  `sample_discussion_digest`, `sample_landing_digest`, `tmp_output_dir`
- `test_models.py` — schema validation, enum coverage, score bounds
- `test_writer.py` — frontmatter keys, file path pattern, slug sanitisation
- `test_adapters.py`:
  - `test_github_adapter` — mock `httpx` responses (via `respx`) → assert `RawDiscussion` / `RawCommit`
  - `test_public_inbox_adapter` — mock `git show` subprocess output → assert parsing
  - `test_plain_git_adapter` — mock `git log` output → assert `RawCommit`
  - `test_nntp_fallback` — mock NNTP connection failure → returns `[]` without raising
  - `test_engine_deduplication` — same `id` from two sources → appears once

---

## 12. Project config

**`pyproject.toml`** (repo root):
```toml
[tool.ruff]
target-version = "py312"
select = ["E", "F", "I"]

[tool.pytest.ini_options]
testpaths = ["agents/tests"]

[tool.pyright]
pythonVersion = "3.12"
```

**`agents/requirements.txt`** additions:
```
pyyaml>=6.0       # sources.yml parsing
respx>=0.21.0     # HTTP mocking in tests
```

**`.gitignore`** additions:
```
agents/cache/**/*.mbox
agents/cache/**/*.git/
```

Add `agents/cache/` with `.gitkeep`.

---

## Budget Rule
`google/gemini-2.5-flash` for all bulk calls.
`anthropic/claude-sonnet-4.5` only for `LandingDigest` items with `impact_score >= 9`.
Never call LLMs per-item — batch (10 discussions / 15 commits per call).
Log token usage to `agents/output/usage.log` after every run.

---

## Verification
```bash
pip install -r agents/requirements.txt
pytest agents/tests/ -v
python -m agents.main --since-hours 6 --dry-run
python -m agents.main --since-hours 24   # needs OPENROUTER_API_KEY in .env
ls web/src/content/discussions/
ls web/src/content/landings/
cat agents/output/usage.log
```
