# Agents — The Bimodal Digest Engine

This directory is the Python/PydanticAI backend of **OS Pulse**. It fetches raw
activity from open-source projects (GitHub PRs, Sourceware mailing lists, bare
Git repos), digests it via LLM calls on OpenRouter, and writes typed Markdown
files into `web/src/content/` for the Astro UI to render.

---

## Architecture at a Glance

The engine is **bimodal** — two specialised agents, one shared pipeline:

| Agent | File | Nickname | Handles | Output |
|-------|------|----------|---------|--------|
| Lab | `discussion_agent.py` | "Lab" | In-flight proposals: PRs, mailing-list RFCs | `DiscussionDigest` |
| Factory | `landing_agent.py` | "Factory" | Landed work: merged commits | `LandingDigest` |

The Lab asks *what is being debated*; the Factory asks *what shipped*. Both
share `BimodalBase` fields (`project`, `subsystem`, `patch_id`) so their
outputs can be cross-referenced via a stable git patch-id or explicit commit
trailers.

---

## Data Flow

```
sources.yml
    │
    ▼
main.py ──── builds adapters ──► IngestionEngine
                                      │
                        ┌─────────────┴────────────┐
                        ▼                          ▼
                  RawDiscussion[]            RawCommit[]
                        │                          │
                        ▼                          ▼
               discussion_agent           landing_agent
               (Gemini Flash,             (Gemini Flash, batch 8)
                batch 10)                          │
                        │                  impact_score ≥ 9?
                        │                          │  yes
                        │                  re-run with Sonnet 4.5
                        ▼                          ▼
               DiscussionDigest[]          LandingDigest[]
                        │                          │
                        └──────────┬───────────────┘
                                   ▼
                               writer.py
                                   │
            ┌──────────────────────┴─────────────────────┐
            ▼                                            ▼
web/src/content/discussions/              web/src/content/landings/
  YYYY-MM-DD-<slug>-<id_hash>.md            YYYY-MM-DD-<slug>.md
```

Every run is triggered by `python -m agents.main --since-hours 24` (see
`.github/workflows/daily-digest.yml` for the scheduled CI invocation).

---

## Directory Map

```
agents/
├── main.py                 # CLI entry point — wires everything together
├── sources.yml             # Declarative source list (GitHub, public-inbox, git)
├── requirements.txt        # Python deps (pydantic-ai, httpx, pyyaml, …)
│
├── adapters/               # Platform-specific fetchers (implement Protocols)
│   ├── __init__.py         # DiscussionSource / CommitSource protocols
│   ├── github.py           # GitHub REST API — PRs + commits
│   ├── public_inbox.py     # Sourceware mailing-list mirrors (mbox)
│   └── plain_git.py        # Any bare Git repo (e.g. Torvalds tree)
│
├── ingestion/
│   └── engine.py           # Fans out to adapters, deduplicates by id/sha
│
├── models/                 # Typed data shapes
│   ├── base.py             # BimodalBase, ConsensusStatus enum
│   ├── raw.py              # RawDiscussion, RawCommit (source-agnostic inputs)
│   ├── discussion.py       # DiscussionDigest (Lab output schema)
│   └── landing.py          # LandingDigest (Factory output schema)
│
├── tools/                  # Single-purpose helpers registered with agents
│   ├── patch_id.py         # `git patch-id --stable` wrapper
│   ├── web_search.py       # DuckDuckGo enrichment for cryptic commit titles
│   └── series_grouping.py  # Batch packer that never splits a patch series
│
├── discussion_agent.py     # Lab agent — PydanticAI over Gemini Flash
├── landing_agent.py        # Factory agent — Gemini Flash + Sonnet 4.5 premium
├── writer.py               # Serialises digests to Markdown + YAML frontmatter
│
├── cache/                  # Bare clones + mbox cache (gitignored)
├── output/                 # usage.log — token-spend audit trail
└── tests/                  # pytest suite with shared fixtures
```

---

## Layer-by-Layer Walkthrough

### 1. Sources (`sources.yml`)

Declarative YAML. Three source types are recognised:

```yaml
sources:
  - type: github
    owner: gcc-mirror
    repo: gcc

  - type: public_inbox
    discussion_lists: [gcc, libc-alpha]
    cvs_lists: [gcc-cvs, glibc-cvs]

  - type: plain_git
    url: https://git.kernel.org/…/linux.git
    branch: master
```

`main._build_sources()` maps each entry to the matching adapter constructor.
Unknown `type` values log a warning and are skipped — they never raise.

---

### 2. Adapters (`adapters/`)

Each adapter implements one or both structural subtype protocols:

```python
class DiscussionSource(Protocol):
    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]: ...

class CommitSource(Protocol):
    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]: ...
```

| Adapter | Protocols | Key details |
|---------|-----------|-------------|
| `GitHubAdapter` | both | Persistent `httpx.Client` (TLS reuse). Rate-limit aware via `X-RateLimit-Remaining` and `Retry-After`. Link-header pagination. Diff capped at 32 KB, skips PRs with >500 changed files. |
| `PublicInboxAdapter` | both | `git clone --mirror` of `inbox.sourceware.org/{list}/`. Deduplicates by message-id. 30-day mbox cache in `cache/raw/`. List names validated against `^[a-z][a-z0-9-]{0,63}$` to block git-option injection. |
| `PlainGitAdapter` | commits only | Bare clone into `cache/<repo>.git`. URL scheme allowlisted (`https/http/git/ssh`), branch names regex-validated. All subprocess calls timeout at 120 s. |

**Security invariant**: anything passed to a git subprocess is either validated
against a strict regex/allowlist or placed after `--`. Do not relax this.

---

### 3. IngestionEngine (`ingestion/engine.py`)

```python
class IngestionEngine:
    def __init__(self, discussion_sources, commit_sources): ...
    def run(self, since_hours=24) -> {"discussions": [...], "commits": [...]}
```

Fans out across all sources, catches per-adapter exceptions (one broken source
never kills the run), then deduplicates:

- discussions by `RawDiscussion.id` (PR number, message-id, …)
- commits by `RawCommit.sha`

---

### 4. Raw Models (`models/raw.py`)

Plain `@dataclass` — internal only, never serialised to disk.

```python
@dataclass
class RawDiscussion:
    id: str           # adapter's natural key
    title: str
    body: str
    author: str
    date: datetime
    url: str
    replies: list[dict]
    diff_text: str | None
    source_type: str  # "github_pr" | "public_inbox" | "gitlab_mr"
    metadata: dict    # adapter-specific extras (series_id, labels, …)

@dataclass
class RawCommit:
    sha: str
    author: str
    date: datetime
    message: str
    diff_stat: str | None
    url: str
    source_type: str  # "github" | "public_inbox" | "plain_git"
    metadata: dict
```

`source_type` strings are part of the agent prompt contract — update the
"Source-type heuristics" block in system prompts when adding a new value.

---

### 5. Agents

Both agents follow the same structural shape:

1. Build an `OpenAIModel` pointed at OpenRouter (`base_url=https://openrouter.ai/api/v1`).
2. Wrap it in a `pydantic_ai.Agent` with `result_type=list[…Digest]` — PydanticAI
   validates that every LLM response matches the schema.
3. Register shared tools: `extract_patch_id`, `search_context`.
4. Render each batch to plain text and call `agent.run_sync(prompt)`.
5. Append `{agent, model, ts, usage}` as a JSON line to `output/usage.log`
   (rotated at 10 MB, one backup kept).
6. On any exception fall back to `_stub_digests()` so the pipeline always
   produces output.

**Batching is load-bearing for the €5/month budget — never replace it with
per-item calls.**

#### Lab — `discussion_agent.py`

```python
def run_discussion_agent(
    discussions: list[RawDiscussion],
    project: str = "gcc",
    dry_run: bool = False,
) -> list[DiscussionDigest]:
```

- Model: `google/gemini-2.5-flash-lite` (override via `SUMMARISER_MODEL`)
- Batch size: **10**
- Batches are kept series-aware (`series_aware_batches`) — items sharing a
  `metadata["series_id"]` (e.g., `[PATCH 1/3]`, `[PATCH 2/3]`) are never
  split across batches.
- The system prompt tells the model to infer `ConsensusStatus` from review
  state (`github_pr`) or ACK/NACK email patterns (`public_inbox`).

#### Factory — `landing_agent.py`

```python
def run_landing_agent(
    commits: list[RawCommit],
    project: str = "gcc",
    dry_run: bool = False,
) -> list[LandingDigest]:
```

- Model: `google/gemini-2.5-flash-lite` (override via `SUMMARISER_MODEL`)
- Batch size: **15**
- After the cheap pass, `_extract_trailers()` runs deterministically over every
  original commit message, scanning for:
  `Closes #N`, `Message-Id:`, `Link:`, `PR N`, `Bugzilla: N`.
  It backfills `discussion_id_link` **only when the LLM left it `None`** —
  the model's value is always preferred.
- Items with `impact_score >= 9` are re-run through the premium model
  (`anthropic/claude-sonnet-5.5`, override via `BENTO_MODEL`). The re-run
  receives the **original `RawCommit`** (not the cheap model's summary) to
  preserve full context.

---

### 6. Tools (`tools/`)

Small, typed, side-effect-tolerant helpers registered with both agents.

| Tool | Signature | What it does |
|------|-----------|--------------|
| `extract_patch_id` | `(diff_text: str) -> str \| None` | Pipes a diff through `git patch-id --stable`, returns 40-char hex or `None`. Used to cross-reference pre-merge discussions with landed commits. |
| `search_context` | `(query: str, max_results=5) -> list[str]` | DuckDuckGo text snippets for enriching cryptic commit titles. Swallows all errors gracefully. |
| `series_aware_batches` | `(items, batch_size, series_key) -> list[list]` | Greedy batch packer that never splits a patch series. Items sharing a `series_key()` value are kept together; oversized series are allowed to exceed `batch_size` rather than split. |

---

### 7. Digest Models (`models/`)

All output models inherit from `BimodalBase`:

```python
class BimodalBase(BaseModel):
    project: str
    subsystem: str               # e.g. "gcc/ipa", "kernel/mm"
    patch_id: str | None = None  # stable cross-reference key
```

**`DiscussionDigest`** (Lab output):

```python
class DiscussionDigest(BimodalBase):
    discussion_id: str            # PR#, message-id, …
    source_type: str
    title: str
    proposer: str
    consensus: ConsensusStatus    # Proposed | Under Review | Needs Revision
                                  # | NACK'd | Ready to Land | Committed
    sentiment_score: int          # 1–10
    technical_tradeoffs: list[str]
    summary: str
    url: str
    bugzilla_url: str | None = None
```

**`LandingDigest`** (Factory output):

```python
class LandingDigest(BimodalBase):
    commit_hash: str
    source_type: str
    author: str
    impact_score: int             # 1–10; >= 9 triggers premium re-run; >= 7 is "bento-worthy"
    performance_win: bool = False
    breaking_change: bool = False
    summary: str
    discussion_id_link: str | None = None  # cross-ref to DiscussionDigest
    bugzilla_pr: int | None = None
    url: str
```

---

### 8. Writer (`writer.py`)

Serialises digests to Markdown with YAML frontmatter, consumed by Astro Content
Collections.

```python
write_discussion(d: DiscussionDigest, output_dir=None) -> Path
write_landing(landing: LandingDigest, output_dir=None) -> Path
```

| Type | Output path |
|------|------------|
| Discussion | `web/src/content/discussions/YYYY-MM-DD-<slug>-<id_hash>.md` |
| Landing | `web/src/content/landings/YYYY-MM-DD-<subsystem>-<short_sha>.md` |

Slug rule: lowercase, collapse non-word characters to `-`, strip leading/trailing
dashes, cap at 80 chars. The 6-char SHA-1 suffix on discussion slugs prevents
same-title same-day collisions.

---

### 9. CLI (`main.py`)

```bash
python -m agents.main [--since-hours N] [--dry-run]
```

| Flag | Default | Effect |
|------|---------|--------|
| `--since-hours` | `24` | How far back to fetch from each source |
| `--dry-run` | off | Skip all LLM calls, emit stub digests, validate pipeline wiring |

Exits 0 on success, non-zero on fatal errors.

---

## Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `OPENROUTER_API_KEY` | Authenticates all LLM calls | Yes (for real runs) |
| `GITHUB_TOKEN` | Raises GitHub rate limit 60 → 5 000 req/h | Strongly recommended |
| `SUMMARISER_MODEL` | Overrides the cheap batch model | No |
| `BENTO_MODEL` | Overrides the premium re-run model | No |

All loaded via `python-dotenv` from a gitignored `.env`. **Never commit keys.**

---

## Running

```bash
# Install dependencies
pip install -r agents/requirements.txt

# Dry run — validate pipeline without spending tokens
python -m agents.main --since-hours 24 --dry-run

# Real run
python -m agents.main --since-hours 24
```

Output summary prints discussion count, landing count, and bento-worthy count
(`impact_score >= 7`).

---

## Tests

```bash
pytest agents/tests -q
```

Shared fixtures live in `tests/conftest.py`:
`sample_raw_discussion`, `sample_raw_commit`,
`sample_discussion_digest`, `sample_landing_digest`, `tmp_output_dir`.

Coverage: adapter HTTP behaviour (respx-mocked), model validation,
writer frontmatter / slug / collision handling, series-aware batching.
The live LLM path is not tested in CI (costs tokens); use `--dry-run` for
end-to-end wiring tests.

---

## Key Invariants

- **Budget**: cheap model runs all batches. Premium model (`impact_score >= 9`
  only) is a targeted re-run, not a fallback.
- **Premium re-run uses the original `RawCommit`**, not the cheap model's
  summary — context parity is guaranteed.
- **Trailer extraction is deterministic** and runs unconditionally after the
  cheap pass; it only fills `discussion_id_link` when the LLM left it `None`.
- **Adapters must not raise into `IngestionEngine`** for recoverable errors —
  log and return `[]`. The engine does catch exceptions, but relying on that
  masks root causes.
- **`output/usage.log` is the token-spend audit trail.** Do not remove the
  `_append_usage()` calls.
- **`source_type` strings are part of the agent prompt contract.** Adding a new
  source type requires updating the "Source-type heuristics" block in both
  agent system prompts.

---

## Extending the Engine

**Add a new source type** (e.g. GitLab):
1. Create `adapters/gitlab.py` implementing `DiscussionSource` / `CommitSource`.
2. Add a branch in `main._build_sources()` for `type: gitlab`.
3. Add the entry in `sources.yml`.
4. Add fixtures and tests in `tests/test_adapters.py`.
5. Pick a `source_type` string (e.g. `"gitlab_mr"`) and document its heuristics
   in both agent system prompts.

**Add an agent tool**:
1. Drop a module in `tools/` exporting a single typed function.
2. Register it in both agents' `tools=[…]` lists (or just one if scoped).
3. Keep it pure and failure-tolerant — the agent loop must continue if it raises.

**Change an output schema**:
1. Edit the Pydantic model in `models/`.
2. Add the field(s) to the corresponding frontmatter dict in `writer.py`.
3. Mirror the field in `web/src/content/config.ts`.
4. Run `pytest agents/tests` — writer tests will flag frontmatter mismatches.

---

## Pulse Index & MCP Server (`index/`, `mcp/`)

The Markdown corpus is also a queryable record of GCC/binutils change history.
Two modules turn it into one:

- **`index/`** derives `index/pulse.db` (SQLite + FTS5) from `web/src/content/**`.
- **`mcp/`** serves that database over MCP so an agent can search it.

### Build the index

```bash
python -m agents.index.build --full --no-embeddings   # lexical only, no API key
python -m agents.index.build --full                   # adds semantic search
python -m agents.index.build                          # nightly: only what changed
```

Rebuilding is incremental by content hash, so a nightly run touches the ~34
changed files rather than all ~2,950. `pulse.db` is gitignored: it is derived,
disposable, and regenerable from the Markdown at any time.

**`--full` is for manual rebuilds only.** It deletes the database first, so every
document is re-indexed *and re-embedded*. The nightly workflow deliberately omits it and
restores `pulse.db` from `actions/cache` instead; without a restored database the
content-hash check has nothing to compare against and the whole corpus is re-embedded
every night. That is a cost bug rather than a correctness one, which is exactly why it is
easy to reintroduce unnoticed — `agents/tests/test_index_build.py` pins the behaviour.

If `EMBEDDING_MODEL` changes, the next build discards every stored vector and re-embeds:
vectors from two models are not comparable and rarely share a dimension, so a mixed table
would rank nonsensically or silently drop the minority dimension at query time.

### Run the server

```bash
claude mcp add pulse -- /path/to/python -m agents.mcp.server
```

`PULSE_DB` overrides the database location. Tools exposed:

| Tool | Use it for |
|---|---|
| `corpus_info` | Coverage and freshness — check before answering from the corpus |
| `search_changes` | General hybrid search with project/subsystem/date/outcome filters |
| `find_by_symbol` | Exact lookup of a function, file, flag, relocation or PR number |
| `suspects` | Candidate changes related to a regression symptom, newest-weighted |
| `timeline` | Chronological activity for a subsystem or patch series |
| `get_change` | One article in full, by SHA, discussion id, path or URL |
| `related_discussion` | The mailing-list thread behind a landed commit |

### Design constraints

- **No LLM calls at query time.** The server retrieves; the calling agent
  reasons. Query volume therefore cannot affect the €5/month budget.
- **The corpus has no diffs or test results.** `suspects` returns *leads*, and
  says so in its payload and its tool description. Nothing here can establish
  that a change caused a regression — every hit is something to verify with
  `git show <sha>` upstream.
- **A miss is reported as a miss.** Retrieval weights query terms by inverse
  document frequency and drops documents that miss the rare, discriminating
  ones, so a query about a topic the corpus does not cover returns nothing
  rather than a plausible-looking irrelevance.
- **Embeddings are the one non-OpenRouter provider** (OpenRouter has no
  embeddings endpoint). Confined to `index/embed.py` behind the
  `EmbeddingProvider` protocol, configured by `EMBEDDING_*` env vars, and logged
  to `output/usage.log` like every other call. See root `CLAUDE.md`.

### Known data gaps

`series_id` is populated on only ~1% of landings and ~21% of discussions, and
`patch_id` / `bugzilla_pr` / `discussion_id_link` are null corpus-wide. De-duplication
therefore falls back to a normalised headline key, and `related_discussion` infers
the commit↔thread link rather than reading it. Populating these at ingest —
along with touched files and test names from the diff — is the single biggest
available improvement to `suspects` result quality.
