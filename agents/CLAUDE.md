# `agents/` — The Bimodal Digest Engine

This folder is the Python/PydanticAI backend of OS Pulse. It fetches raw
activity from open-source projects (GitHub PRs, Sourceware public-inbox mailing
lists, bare Git repos), digests it into typed Pydantic models via LLM calls on
OpenRouter, and writes Markdown files into `web/src/content/` for the Astro UI
to render.

This doc is the map of how the pieces wire together. For project-wide rules
(budget caps, storage format, etc.) see the repo-root `CLAUDE.md`.

---

## Mental Model: Two Agents, One Pipeline

The engine is **bimodal** — two agents with different jobs share the same
infrastructure:

| Agent | Handles | Output Model | Source data |
|-------|---------|--------------|-------------|
| **Lab** (`discussion_agent.py`) | In-flight proposals — PRs, mailing-list RFCs | `DiscussionDigest` | `RawDiscussion` |
| **Factory** (`landing_agent.py`) | Landed work — merged commits | `LandingDigest` | `RawCommit` |

The Lab is about *what is being debated*; the Factory is about *what shipped*.
Both share the `BimodalBase` fields (`project`, `subsystem`, `patch_id`) so the
two sides can be cross-referenced via `patch_id` or explicit trailers.

---

## Data Flow

```
sources.yml
    │
    ▼
main.py ─── builds adapters ──► IngestionEngine
                                     │
                       ┌─────────────┴────────────┐
                       ▼                          ▼
                 RawDiscussion[]             RawCommit[]
                       │                          │
                       ▼                          ▼
              discussion_agent           landing_agent
              (Gemini Flash,             (Gemini Flash, batch 8)
               batch 10)                         │
                       │                 impact_score ≥ 9?
                       │                         │ yes
                       │                 rerun with Sonnet 4.5
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

Every run is initiated by `python -m agents.main --since-hours 24` (see
`.github/workflows/daily-digest.yml` for the scheduled invocation).

---

## Directory Map

```
agents/
├── main.py                 # CLI entry point, wires everything together
├── sources.yml             # Declarative list of sources to pull from
├── requirements.txt        # Python deps (pydantic-ai, httpx, yaml, …)
│
├── adapters/               # Platform-specific fetchers (implement Protocols)
│   ├── __init__.py         # DiscussionSource / CommitSource Protocols
│   ├── github.py           # GitHub REST API (PRs + commits)
│   ├── public_inbox.py     # Sourceware mailing-list mirrors (mbox)
│   └── plain_git.py        # Any bare Git repo (e.g. Torvalds tree)
│
├── ingestion/
│   └── engine.py           # Fans out to adapters, dedups by id/sha
│
├── models/                 # Typed data shapes
│   ├── base.py             # BimodalBase, ConsensusStatus enum
│   ├── raw.py              # RawDiscussion, RawCommit (source-agnostic)
│   ├── discussion.py       # DiscussionDigest (Lab output)
│   └── landing.py          # LandingDigest (Factory output)
│
├── tools/                  # Small, single-purpose helpers registered with the Agent
│   ├── patch_id.py         # `git patch-id --stable` wrapper (cross-ref key)
│   └── web_search.py       # DuckDuckGo enrichment for cryptic titles
│
├── discussion_agent.py     # Lab — PydanticAI agent over Gemini Flash
├── landing_agent.py        # Factory — Gemini Flash + Sonnet 4.5 premium rerun
├── writer.py               # Serialises digests to Markdown + YAML frontmatter
│
├── cache/                  # Bare clones + mbox cache (gitignored)
├── output/                 # usage.log (token spend audit trail)
└── tests/                  # pytest suite with shared fixtures
```

---

## Layer-by-Layer Walkthrough

### 1. Sources (`sources.yml`)

Declarative. Three source types are recognised:

```yaml
sources:
  - type: github
    owner: gcc-mirror
    repo: gcc

  - type: public_inbox
    discussion_lists: [gcc, libc-alpha]
    cvs_lists: [gcc-cvs, glibc-cvs]
    use_nntp: true        # accepted but ignored; NNTP was removed in Py 3.13

  - type: plain_git
    url: https://git.kernel.org/…/linux.git
    branch: master
```

`main._build_sources()` maps each entry to the matching adapter constructor.
Unknown `type` values log a warning and are skipped — never raise.

### 2. Adapters (`adapters/`)

Each adapter implements one or both of these protocols:

```python
class DiscussionSource(Protocol):
    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]: ...

class CommitSource(Protocol):
    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]: ...
```

| Adapter | Implements | Notes |
|---------|------------|-------|
| `GitHubAdapter` | both | Persistent `httpx.Client`, rate-limit-aware (Retry-After, X-RateLimit-Remaining), Link-header pagination, diff capped at 32 KB, skips PRs >500 changed files. Reads `GITHUB_TOKEN` from env. |
| `PublicInboxAdapter` | both | `git clone --mirror` of `inbox.sourceware.org/{list}/0…9`. Walks all epochs, dedups by message-id. Caches raw mbox to `cache/raw/*.mbox` with 30-day TTL. List names validated against `^[a-z][a-z0-9-]{0,63}$` to prevent git-option injection. |
| `PlainGitAdapter` | commits only | Bare clone into `cache/<repo>.git`. URL scheme allowlisted (`https/http/git/ssh`), branch name regex-validated. All subprocess calls have a 120 s timeout. |

**Security invariant**: anything that goes into a git subprocess is either
validated against a strict regex/allowlist or passed after `--` so git can't
interpret it as an option. Don't relax this.

### 3. `IngestionEngine` (`ingestion/engine.py`)

Fans out across both source lists, catches per-adapter exceptions (so one
broken source doesn't kill the run), and dedups:

- discussions by `RawDiscussion.id` (PR#, Message-ID, …)
- commits by `RawCommit.sha`

Returns `{"discussions": [...], "commits": [...]}`.

### 4. Raw models (`models/raw.py`)

`@dataclass` (not Pydantic) — these are internal and never serialised to disk.
Fields like `source_type` are strings that downstream agents use for heuristics
(`"github_pr"` vs `"public_inbox"` vs `"plain_git"`).

### 5. Agents (`discussion_agent.py`, `landing_agent.py`)

Both follow the same shape:

1. Build an `OpenAIModel` pointed at OpenRouter (`base_url=https://openrouter.ai/api/v1`,
   API key from `OPENROUTER_API_KEY`).
2. Wrap it in a `pydantic_ai.Agent` with `result_type=list[…Digest]` — PydanticAI
   enforces JSON-matches-schema.
3. Register the shared tools: `extract_patch_id`, `search_context`.
4. Render the raw batch to text and run `agent.run_sync(prompt)`.
5. Append `{agent, model, ts, usage}` as a JSON line to `output/usage.log`
   (rotated at 10 MB, one backup kept).
6. On exception, fall back to `_stub_digests()` so the pipeline still produces
   output for downstream processing.

**Batching is load-bearing for the €5/month budget — never replace this with
per-item calls.**

| Agent | Model | Batch | Premium path |
|-------|-------|-------|--------------|
| discussion_agent | `google/gemini-2.0-flash-001` (env: `SUMMARISER_MODEL`) | 10 | none |
| landing_agent | same as above | 8 | `impact_score ≥ 9` → re-run through `anthropic/claude-sonnet-4-5` (env: `BENTO_MODEL`) using the **original** `RawCommit`, not the cheap summary |

The landing agent also runs a deterministic trailer extractor
(`_extract_trailers`) that scans commit messages for
`Closes #N`, `Message-Id:`, `Link:`, `PR N`, `Bugzilla:` and backfills
`discussion_id_link` — only when the LLM left it `None`, so the model can still
override with richer info.

### 6. Tools (`tools/`)

Registered with both agents. Keep them small and side-effect-free.

- **`extract_patch_id(diff_text) -> str | None`** — pipes a diff through
  `git patch-id --stable`. Returns the 40-char hash or `None`. Used to link
  a `DiscussionDigest` (pre-merge patch) to a later `LandingDigest` (merged
  commit) even across platforms.
- **`search_context(query, max_results=5) -> list[str]`** — DuckDuckGo text
  snippets; swallows all errors so the agent keeps going without enrichment.
  `duckduckgo_search` is lazy-imported.

### 7. Digest models (`models/`)

All digests inherit `BimodalBase` → `project`, `subsystem`, `patch_id`.

```python
class DiscussionDigest(BimodalBase):
    discussion_id, source_type, title, proposer,
    consensus: ConsensusStatus,
    sentiment_score: int 1..10,
    technical_tradeoffs: list[str],
    summary, url,
    bugzilla_url: str | None

class LandingDigest(BimodalBase):
    commit_hash, source_type, author,
    impact_score: int 1..10,
    performance_win: bool,
    breaking_change: bool,
    summary,
    discussion_id_link: str | None,   # cross-ref to DiscussionDigest
    bugzilla_pr: int | None,
    url
```

`ConsensusStatus` values: `Proposed`, `Under Review`, `Needs Revision`,
`NACK'd`, `Ready to Land`, `Committed`.

### 8. Writer (`writer.py`)

Serialises each digest to Markdown with YAML frontmatter, consumed by Astro
Content Collections on the web side.

- Discussions → `web/src/content/discussions/YYYY-MM-DD-<slug>-<id_hash>.md`
  (6-char SHA-1 of `discussion_id` appended so same-title same-day posts
  don't collide).
- Landings → `web/src/content/landings/YYYY-MM-DD-<slug>.md` where slug is
  `<subsystem>-<short_sha>`.
- Slug rule: `lowercase`, non-word → `-`, stripped, max 80 chars.

Frontmatter keys exactly match model field names so the Astro schema can
reflect them directly.

---

## Environment Variables

| Var | Purpose | Required? |
|-----|---------|-----------|
| `OPENROUTER_API_KEY` | LLM calls | yes for real runs |
| `GITHUB_TOKEN` | Raise GitHub rate limit from 60→5000/h | strongly recommended |
| `SUMMARISER_MODEL` | Override the cheap model | optional |
| `BENTO_MODEL` | Override the premium re-run model | optional |

All loaded via `python-dotenv` from a gitignored `.env`. **Never commit keys.**

---

## Running It

```bash
# Install
pip install -r agents/requirements.txt

# Dry run — skip LLMs, emit stub digests, test pipeline wiring
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

Fixtures live in `tests/conftest.py`:
`sample_raw_discussion`, `sample_raw_commit`,
`sample_discussion_digest`, `sample_landing_digest`, `tmp_output_dir`.

Covered: adapter HTTP behaviour (respx-mocked), model validation, writer
frontmatter + slug + collision handling. The live LLM path is not tested in CI
(costs tokens); use `--dry-run` for end-to-end wiring tests.

---

## Extending the Engine

**Add a new source type** (e.g. GitLab):
1. Create `adapters/gitlab.py` implementing one or both Protocols.
2. Add a branch in `main._build_sources()` for `type: gitlab`.
3. Add the source entry in `sources.yml`.
4. Add a fixture + test in `tests/test_adapters.py`.
5. Pick a `source_type` string (e.g. `"gitlab_mr"`, `"gitlab"`) and document
   a heuristic for it in both agent system prompts.

**Add a new agent tool**:
1. Drop a module in `tools/` exporting a single typed function.
2. Register it in both agents' `tools=[…]` lists (or just one, if scoped).
3. Keep it pure / failure-tolerant — the agent loop must be able to continue if
   the tool raises.

**Change the output schema**:
1. Edit the Pydantic model in `models/`.
2. Add the new field(s) to the corresponding `write_*` frontmatter dict in
   `writer.py`.
3. Mirror the field in the Astro content schema under
   `web/src/content/config.ts` (or equivalent).
4. Run `pytest agents/tests` — writer tests will flag frontmatter mismatches.

---

## Gotchas & Invariants

- **Budget**: never swap the cheap model out of the batch path. Premium model
  is only for the `impact_score ≥ 9` re-run.
- **Premium re-run uses original `RawCommit`**, not the cheap model's summary
  — preserves context parity.
- **Trailer extraction runs unconditionally** after the cheap pass; it only
  fills `discussion_id_link` when the LLM left it `None`.
- **`source_type` strings are part of the contract** with the agent prompts.
  If you add a new one, update the "Source-type heuristics" block in the
  relevant system prompt.
- **`output/usage.log` is the sole token-spend audit trail.** Don't remove the
  `_append_usage()` calls — the budget cap enforcement depends on it.
- **Adapters must never raise into `IngestionEngine`** for recoverable errors;
  log + return `[]`. The engine does catch exceptions but relying on that
  hides the source of the problem.
