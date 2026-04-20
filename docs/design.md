# Digestware — System Design

## Overview

Digestware fetches, digests, and publishes a daily summary of open-source OS-level changes
(GCC, glibc, binutils, Linux kernel) as a static web feed and per-project RSS stream.

The pipeline runs nightly via GitHub Actions, writes structured Markdown files, and builds
a zero-infrastructure Astro site — all for under €5/month in AI costs.

**Four tracked projects:** `gcc`, `glibc`, `binutils`, `linux`

---

## Monorepo Layout

```
Digestware/
├── agents/                     # Python 3.12 — PydanticAI digest engine
│   ├── main.py                 # CLI entry point
│   ├── sources.yml             # Declarative adapter configuration
│   ├── ingestion/engine.py     # Fan-out, dedup, noise filter
│   ├── discussion_agent.py     # Lab agent (proposals/RFCs → DiscussionDigest)
│   ├── landing_agent.py        # Factory agent (commits → LandingDigest)
│   ├── writer.py               # Markdown + YAML frontmatter serialisation
│   ├── dedup.py                # Post-process deduplication
│   ├── adapters/               # Platform-specific fetchers
│   │   ├── github.py           # GitHub REST API (PRs + commits)
│   │   ├── public_inbox.py     # Sourceware mailing lists (mbox/NNTP)
│   │   └── plain_git.py        # Any bare Git repo (commits only)
│   ├── models/                 # Pydantic schemas
│   │   ├── base.py             # BimodalBase, ConsensusStatus, Outcome
│   │   ├── raw.py              # RawDiscussion, RawCommit (internal)
│   │   ├── discussion.py       # DiscussionDigest output schema
│   │   └── landing.py          # LandingDigest output schema
│   ├── tools/                  # Single-purpose helpers
│   │   ├── patch_id.py         # git patch-id --stable wrapper
│   │   ├── subsystem.py        # Deterministic subsystem extraction
│   │   ├── noise_filter.py     # Filters "Daily bump", empty pings
│   │   ├── series_grouping.py  # Series-aware batch packing
│   │   ├── web_search.py       # DuckDuckGo enrichment
│   │   ├── headline.py         # Subject-line cleaning
│   │   ├── outcome.py          # Discussion state inference
│   │   └── series.py           # Patch series tracking
│   ├── tests/                  # pytest suite (12+ modules)
│   └── output/                 # usage.log audit trail (gitignored)
│
├── web/                        # Astro 6 + Tailwind 4 frontend
│   └── src/
│       ├── config/projects.ts  # Project registry
│       ├── content/
│       │   ├── config.ts       # Astro Content Collections schema
│       │   ├── discussions/    # DiscussionDigest Markdown (agent output)
│       │   └── landings/       # LandingDigest Markdown (agent output)
│       ├── pages/
│       │   ├── index.astro     # Redirect → /gcc/
│       │   └── [project]/      # Per-project feed, discussion, landing, RSS pages
│       ├── layouts/            # PublicLayout, AdminLayout
│       └── components/         # BentoCard, CommitRow
│
├── .github/workflows/
│   ├── daily-digest.yml        # Nightly pipeline (02:00 UTC)
│   ├── ci.yml                  # Push/PR checks
│   └── test.yml                # Reusable test job
│
└── CLAUDE.md                   # Project constraints and conventions
```

---

## Technology Stack

| Layer | Choice | Why |
|-------|--------|-----|
| AI runtime | PydanticAI | Typed structured output; easy tool registration |
| LLM provider | OpenRouter | Model-agnostic, pay-per-token |
| Bulk model | `google/gemini-2.0-flash-001` | ~€0.05/1M tokens — all batch work |
| Premium model | `anthropic/claude-sonnet-4-5` | Only for impact_score ≥ 9 re-runs |
| Frontend | Astro 6 + Tailwind 4 | Static-first, Content Collections, fast |
| Newsletter | Resend API + React Email | Generous free tier |
| Storage | Markdown files in Git | Zero infra cost, version-controlled history |

---

## Bimodal Agent Architecture

Two specialised agents share one ingestion pipeline. They are deliberately separated because
the logic for "what is being proposed?" differs fundamentally from "what shipped?".

| Agent | File | Input | Output | Model | Batch size |
|-------|------|-------|--------|-------|-----------|
| **Lab** | `discussion_agent.py` | `RawDiscussion` | `DiscussionDigest` | Gemini Flash | 10 |
| **Factory** | `landing_agent.py` | `RawCommit` | `LandingDigest` | Gemini Flash → Sonnet 4.5* | 15 |

*Factory re-runs items with `impact_score >= 9` through the premium model using the
original `RawCommit` (not the cheap model's summary) to preserve full context.

Both output models inherit `BimodalBase` (`project`, `subsystem`, `patch_id`) so
discussion and landing records can be cross-referenced via stable git patch-id.

---

## Data Flow

```
sources.yml
    │
    ▼
main.py ──► IngestionEngine
                │
    ┌───────────┴───────────┐
    ▼                       ▼
RawDiscussion[]         RawCommit[]
    │                       │
noise_filter           noise_filter
    │                       │
    ▼                       ▼
discussion_agent       landing_agent
(Gemini Flash,         (Gemini Flash,
 batch 10)              batch 15)
    │                       │
    │               impact_score ≥ 9?
    │                       │
    │               re-run Sonnet 4.5
    │               (original RawCommit)
    ▼                       ▼
DiscussionDigest[]     LandingDigest[]
    │                       │
    └───────────┬───────────┘
                ▼
            writer.py
                │
    ┌───────────┴───────────┐
    ▼                       ▼
web/src/content/        web/src/content/
  discussions/            landings/
  YYYY-MM-DD-<slug>.md    YYYY-MM-DD-<slug>.md
```

---

## Source Adapters

All adapters implement the `DiscussionSource` and/or `CommitSource` protocols from
`adapters/__init__.py` (structural subtyping — no inheritance).

### GitHub (`adapters/github.py`)
- GitHub REST API with persistent `httpx.Client`
- Rate-limit aware: reads `X-RateLimit-Remaining`, backs off on 429/403
- Diffs capped at 32 KB; skips PRs with >500 changed files
- Reads `GITHUB_TOKEN` from env (60 → 5000 req/h)
- Maps: PR → `RawDiscussion`, Commit → `RawCommit`

### PublicInbox (`adapters/public_inbox.py`)
- `git clone --mirror https://inbox.sourceware.org/{list}/` → local cache
- Handles mbox epochs (`/0`, `/1`, `/2`) automatically
- 30-day mbox cache in `agents/cache/raw/`
- List names validated against `^[a-z][a-z0-9-]{0,63}$` to block shell injection
- NNTP fallback with graceful degradation on network errors
- Configured lists: `gcc`, `libc-alpha`, `binutils` (discussion); `gcc-cvs`, `glibc-cvs`, `binutils-cvs` (commits)

### PlainGit (`adapters/plain_git.py`)
- `git clone --bare` on first run; `git fetch` on repeat
- `git log --since={since_date}` via subprocess (120 s timeout)
- URL scheme allowlisted; branch names regex-validated; args placed after `--`
- Configured: Linux kernel (`git.kernel.org`, branch `master`)

---

## Key Data Models

### Internal (never serialised)

```python
@dataclass
class RawDiscussion:
    id: str          # PR number, message-id — source's natural key
    title: str
    body: str
    author: str
    date: datetime
    url: str
    replies: list[dict]
    diff_text: str | None
    source_type: str  # "github_pr" | "public_inbox"
    metadata: dict

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

### Output schemas

```python
class BimodalBase(BaseModel):
    project: str
    subsystem: str
    patch_id: str | None = None  # git patch-id --stable for cross-referencing
    tags: list[str]              # max 5

class DiscussionDigest(BimodalBase):
    discussion_id: str
    headline: str         # ≤80 chars, no "[PATCH]" or "Re:"
    tldr: str             # ≤140 chars, one sentence
    stakes: str           # why a general dev should care
    summary: str          # 2–4 sentences
    proposer: str
    consensus: ConsensusStatus
    outcome: Outcome
    sentiment_score: int  # 1–10 (1=NACK storm, 10=wide approval)
    technical_tradeoffs: list[str]
    series_id: str | None
    url: str
    date: datetime

class LandingDigest(BimodalBase):
    commit_hash: str
    headline: str         # human-readable, not raw commit subject
    tldr: str             # ≤160 chars
    why_it_matters: str   # dev-facing stakes
    impact_score: int     # 1–10 (≥9 → premium re-run; ≥7 → bento-worthy)
    performance_win: bool
    breaking_change: bool
    outcome: Outcome
    discussion_id_link: str | None  # cross-ref to a DiscussionDigest
    url: str
    date: datetime
```

### Enumerations (`models/base.py`)

`ConsensusStatus`: `Proposed` | `Under Review` | `Needs Revision` | `NACK'd` | `Ready to Land` | `Committed`

`Outcome`: `proposed` | `under_review` | `needs_revision` | `nackd` | `ready` | `committed` | `withdrawn` | `stalled`

---

## Budget Constraints (hard limits)

- **Total AI spend: ≤ €5/month**
- Cheap model (`gemini-2.0-flash-001`) for **all** bulk operations
- Premium model (`claude-sonnet-4-5`) only for `impact_score >= 9` re-runs
- **Never call LLMs per-item** — always batch (10 discussions / 15 commits per call)
- Batching is load-bearing: breaking it blows the budget
- Token usage logged to `agents/output/usage.log` (JSON lines, rotated at 10 MB)

---

## Output Convention

Writer (`agents/writer.py`) serialises digests to Markdown with YAML frontmatter consumed
by Astro Content Collections.

| Type | Path pattern |
|------|-------------|
| Discussion | `web/src/content/discussions/YYYY-MM-DD-<slug>-<6-char-id-hash>.md` |
| Landing | `web/src/content/landings/YYYY-MM-DD-<subsystem>-<short-sha>.md` |

Slugs: lowercase, non-word chars collapsed to `-`, max 80 chars. The 6-char id hash in
discussion filenames prevents collisions for same-day same-title items.

Body validation rejects: empty bodies, quoted-email leaks (`Re:`, `>`), mid-word truncations.
Falls back to `"Summary unavailable — see source link."` if validation fails.

---

## GitHub Actions Pipeline

### `daily-digest.yml` (02:00 UTC + manual dispatch)

1. Run CI quality gate (lint, type check, unit tests)
2. Verify `OPENROUTER_API_KEY` secret exists
3. **Purge** existing content (discussions, landings, digests, output logs)
4. Run digest pipeline with backfill widening:
   - 48 h window → retry 168 h → 720 h → 2160 h
   - Stop once ≥5 discussions **and** ≥5 landings are produced
5. Commit generated Markdown to repo via `github-actions[bot]`

Clean-slate before each run eliminates dedup drift; backfill ensures minimum content quality.

### `ci.yml` — push/PR to master → calls `test.yml`

### `test.yml` (reusable)

1. Setup Python 3.12 via `astral-sh/setup-uv`
2. `ruff check agents/`
3. `pyright agents/`
4. `pytest agents/tests -q`

Live LLM paths are **not** tested in CI (costs tokens). Use `--dry-run` for end-to-end wiring.

---

## Security Invariants

1. No hardcoded API keys — `.env` (gitignored) and GitHub Actions secrets only
2. Git injection prevention: list names validated `^[a-z][a-z0-9-]{0,63}$`; branch names regex-validated; subprocess args placed after `--`
3. Adapters catch all recoverable errors internally and return `[]` — one broken source never kills the run
4. Rate-limit awareness: respects `X-RateLimit-Remaining`, `Retry-After`; backs off on 429/403
5. Diff size capped (32 KB per PR); PRs with >500 changed files skipped

---

## Development Conventions

- **Python:** 3.12+, `ruff` (lint), `pyright` (type check), `pytest` (tests)
- **TypeScript/Astro:** strict mode, Prettier formatting
- Composition over inheritance; adapters use structural subtyping (Protocols)
- Keep agent tools small and single-purpose
- No secrets in code
