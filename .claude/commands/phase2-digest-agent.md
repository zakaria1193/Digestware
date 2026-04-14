# Phase 2 — The Bimodal Agent Engine (PydanticAI)

Build a Python digest engine that ingests Sourceware.org mailing lists via
public-inbox Git mirrors and NNTP, then produces structured Markdown files.
Two specialised PydanticAI agents handle discussions ("Lab") and landed commits
("Factory"), cross-linked via `patch_id` and `message_id`.

---

## Canonical Data Schema (`agents/models/`)

### `agents/models/base.py`
```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ConsensusStatus(str, Enum):
    PROPOSED        = "Proposed"
    UNDER_REVIEW    = "Under Review"
    NEEDS_REVISION  = "Needs Revision"
    NACKED          = "NACK'd"
    READY_TO_LAND   = "Ready to Land"
    COMMITTED       = "Committed"

class BimodalBase(BaseModel):
    project:   str            # e.g. "gcc", "glibc", "binutils"
    subsystem: str            # e.g. "riscv", "libstdc++", "x86-64"
    patch_id:  Optional[str]  # stable git patch-id for cross-referencing
```

### `agents/models/discussion.py`
```python
class DiscussionDigest(BimodalBase):
    message_id:          str
    subject:             str
    proposer:            str
    consensus:           ConsensusStatus
    sentiment_score:     int = Field(..., ge=1, le=10)  # 1=controversial, 10=universal agreement
    technical_tradeoffs: list[str]
    summary:             str
    bugzilla_url:        Optional[str] = None
    sourceware_url:      str   # https://inbox.sourceware.org/{list}/{message_id}/
```

### `agents/models/landing.py`
```python
class LandingDigest(BimodalBase):
    commit_hash:      str
    author:           str
    impact_score:     int = Field(..., ge=1, le=10)
    performance_win:  bool = False
    breaking_change:  bool = False
    summary:          str
    message_id_link:  Optional[str] = None  # Message-Id trailer from commit
    bugzilla_pr:      Optional[int] = None
```

---

## Tasks

### 1. Ingestion layer (`agents/ingestion/`)

**`agents/ingestion/git_mirror.py`**
- Clone public-inbox epoch repos with `git clone --mirror`; `git fetch` on repeat runs.
- Targets:
  - `https://inbox.sourceware.org/gcc/0` (+ /1, /2… for epochs)
  - `https://inbox.sourceware.org/libc-alpha/0`
  - `https://inbox.sourceware.org/gcc-cvs/0`
  - `https://inbox.sourceware.org/glibc-cvs/0`
- Cache to `agents/cache/{list}/{epoch}/`
- Extract messages: `git log --format=%H` → `git show <sha>:m` → parse mbox headers
- Filter by `since_hours: int = 24` on parsed `Date:` header
- Returns `list[dict]` with: `message_id, subject, from_, date, body, diff_text, list_name`

**`agents/ingestion/nntp_reader.py`**
- Groups: `inbox.gcc.gcc`, `inbox.sourceware.libc-alpha`
- Uses stdlib `nntplib.NNTP` (available in Python 3.12)
- Fetches last 50 articles per group, parses headers
- Returns same dict schema as `git_mirror.py`
- Graceful fallback: NNTP unreachable → returns `[]` + logs warning

**`agents/ingestion/sync.py`** — `SourcewareSync`
- Orchestrates both strategies
- Deduplicates by `message_id`
- Saves raw bytes to `agents/cache/raw/{message_id}.mbox`
- Returns `{"discussions": [...], "cvs_commits": [...]}`

### 2. Tools (`agents/tools/`)

**`agents/tools/patch_id.py`**
- `extract_patch_id(diff_text: str) -> Optional[str]`
- Pipes diff through `git patch-id --stable` via subprocess
- Returns hex id or None if not a valid patch

**`agents/tools/web_search.py`**
- `search_context(query: str) -> list[str]`
- Returns top-5 DuckDuckGo snippets via `DDGS().text(query, max_results=5)`
- Called only for cryptic subjects (< 20 words, no subsystem keyword)

### 3. Agents

**`agents/discussion_agent.py`**
- `Agent[None, list[DiscussionDigest]]` on OpenRouter
- Model: `google/gemini-2.0-flash-001`
- System prompt instructs the agent to:
  - Detect ACK/NACK patterns in thread body → set `ConsensusStatus`
  - Call `patch_id` tool on embedded diff → populate `patch_id`
  - Score `sentiment_score` based on reply tone and agreement level
  - Extract concrete `technical_tradeoffs` as a string list
- Registered tool: `web_search` for context on cryptic subjects
- **Batching**: 10 threads per LLM call (one call returns a list)

**`agents/landing_agent.py`**
- `Agent[None, list[LandingDigest]]` on OpenRouter
- Model: `google/gemini-2.0-flash-001`; re-run with `anthropic/claude-sonnet-4-5` if `impact_score >= 9`
- System prompt instructs the agent to:
  1. Scan commit message for `Message-Id:` or `Link:` trailers → `message_id_link`
  2. If missing, search body for `PR \d+` → `bugzilla_pr`
  3. Set `performance_win=True` if commit cites benchmark improvements
  4. Set `breaking_change=True` if ABI/API change is mentioned
- **Batching**: 15 commits per LLM call

Both agents: capture `result.usage()` → append JSON line to `agents/output/usage.log`

### 4. Markdown writer (`agents/writer.py`)
- `write_discussion(d: DiscussionDigest, output_dir: Path) -> Path`
  → `web/src/content/discussions/YYYY-MM-DD-<slug>.md`
- `write_landing(l: LandingDigest, output_dir: Path) -> Path`
  → `web/src/content/landings/YYYY-MM-DD-<slug>.md`
- Slug: `re.sub(r'[^\w]+', '-', subject.lower()).strip('-')`
- Format: YAML frontmatter (all model fields) + blank line + `summary` as prose body
- `log_usage(usage, log_path)` → JSON-lines append to `agents/output/usage.log`

### 5. Entry point (`agents/main.py`)
- CLI: `python -m agents.main --since-hours 24 [--no-nntp] [--dry-run]`
- `load_dotenv()` reads `OPENROUTER_API_KEY` from `.env`
- Orchestrates: `SourcewareSync.run()` → `DiscussionAgent` batches → `LandingAgent` batches → `write_*()`
- Prints summary: N discussions, N landings written

### 6. Tests (`agents/tests/`)
- `conftest.py` — fixtures: `sample_discussion_digest`, `sample_landing_digest`, `sample_raw_message`, `tmp_output_dir`
- `test_models.py` — validate both schemas; `ConsensusStatus` enum; `sentiment_score`/`impact_score` bounds
- `test_writer.py` — frontmatter keys, file path pattern, slug sanitisation
- `test_ingestion.py` — mock `git show` output → assert message dict; NNTP fallback on connection error

### 7. Config (`pyproject.toml` at repo root)
```toml
[tool.ruff]
target-version = "py312"
select = ["E", "F", "I"]

[tool.pytest.ini_options]
testpaths = ["agents/tests"]

[tool.pyright]
pythonVersion = "3.12"
```

Add `respx>=0.21.0` to `agents/requirements.txt`.
Add `agents/cache/` directory with `.gitkeep`.
Add `agents/cache/**/*.mbox` to `.gitignore`.

---

## Budget Rule
Use `google/gemini-2.0-flash-001` for ALL bulk calls.
Reserve `anthropic/claude-sonnet-4-5` only for `LandingDigest` items with `impact_score >= 9`.
Never call the LLM per-item — always batch (10 discussions / 15 commits per call).
Log token usage after every agent run to `agents/output/usage.log`.

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
