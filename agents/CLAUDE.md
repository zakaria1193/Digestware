# `agents/` — The Bimodal Digest Engine

This folder is the Python/PydanticAI backend of OS Pulse. It fetches raw
activity from open-source projects (GitHub PRs, Sourceware public-inbox mailing
lists, bare Git repos), digests it into typed Pydantic models via LLM calls on
OpenRouter, and writes Markdown files into `web/src/content/` for the Astro UI
to render.

This doc is the map of how the pieces wire together. For project-wide rules
(budget caps, storage format, etc.) see the repo-root `CLAUDE.md`.

---

## Mental Model: Two Agents, One Pipeline (plus a weekly essayist)

The engine is **bimodal** — two agents with different jobs share the same
infrastructure:

| Agent | Handles | Output Model | Source data |
|-------|---------|--------------|-------------|
| **Lab** (`discussion_agent.py`) | In-flight proposals — PRs, mailing-list RFCs | `DiscussionDigest` | `RawDiscussion` |
| **Factory** (`landing_agent.py`) | Landed work — merged commits | `LandingDigest` | `RawCommit` |

The Lab is about *what is being debated*; the Factory is about *what shipped*.
Both share the `BimodalBase` fields (`project`, `subsystem`, `patch_id`) so the
two sides can be cross-referenced via `patch_id` or explicit trailers.

Sitting on top of both is a third, deliberately different producer:

| Agent | Handles | Output Model | Source data |
|-------|---------|--------------|-------------|
| **Lesson** (`lesson_agent.py`) | One landed commit per ISO week, projects alternating | `LessonDigest` | A `LandingDigest` on disk + the project's **real source tree** |

The Lab and the Factory *report* — a headline, a ≤160-char TL;DR, 2–4
sentences, written from a commit message or an email thread. The Lesson
*teaches*: it picks the week's most instructive commit and explains the concept
behind it with the actual GCC/binutils source open, quoting real files at the
exact revision. It is the only long-form prose on the site, and the only agent
that reads code rather than text about code.

That difference drives everything else about it — see **The Lesson Stage**.

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
                                                        │
                                        (reads them back, once a week)
                                                        ▼
                                              lesson_picker.py
                                          ranks the ISO week's landings
                                                        │
                                                   LessonSubject
                                                        │
                                    ┌───────────────────┴──────────────────┐
                                    ▼                                      ▼
                          run_research()  ◄── source_repo.py ──►   run_writer()
                       (cheap model, 16 tool calls,            (Opus, ONE call,
                        reads the real source tree)             no tools)
                                    │                                      │
                                    └────► LessonResearch ─────────────────┘
                                                        │
                                                  LessonDigest
                                                        ▼
                                          web/src/content/lessons/
                                            <week-end>-<project>-<slug>.md
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
│   ├── landing.py          # LandingDigest (Factory output)
│   ├── lesson.py           # LessonDigest + LessonResearch (Lesson output/dossier)
│   └── draft.py            # lenient twins of those, used as agent output_types
│
├── tools/                  # Small, single-purpose helpers registered with the Agent
│   ├── patch_id.py         # `git patch-id --stable` wrapper (cross-ref key)
│   ├── web_search.py       # Gemini-grounded enrichment for cryptic titles
│   └── source_repo.py      # Read-only navigator over a bare, blobless clone
│
├── discussion_agent.py     # Lab — PydanticAI agent over Gemini Flash
├── landing_agent.py        # Factory — Gemini Flash + Sonnet 4.5 premium rerun
├── budget.py               # Month-to-date spend + the EUR 5/month guard
├── check_models.py         # Preflight: do the configured model slugs exist?
├── lesson_picker.py        # Deterministic weekly subject selection (no LLM)
├── lesson_topics.py        # Editorial remit — which subsystems may be taught
├── lesson_agent.py         # Lesson — cheap explorer + Opus writer (two stages)
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
| discussion_agent | `google/gemini-2.5-flash-lite` (env: `SUMMARISER_MODEL`) | 10 | none |
| landing_agent | same as above | 8 | `impact_score ≥ 9` → re-run through `anthropic/claude-sonnet-4.5` (env: `BENTO_MODEL`) using the **original** `RawCommit`, not the cheap summary |

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

## The Lesson Stage

Runs last (STEP 6 in `main.py`), after the landings it reads have been written.
Skippable with `--skip-lesson`; runnable on its own with `--lesson-only`.

### Weekly, enforced by idempotence rather than a schedule

The job runs **nightly**, but produces **one lesson per ISO week, total** —
not one per project. There is no day-of-week check anywhere. Instead
`existing_lesson_for_week()` looks for any lesson whose `lesson_id` ends in
this week's key (`"…:2026-W36"`) and skips if it finds one. The first run of a
new week writes the lesson; the other six are no-ops.

**Projects alternate.** The article is written by a premium model, so volume is
the dominant cost lever; gcc and binutils take turns rather than each getting a
weekly piece. `project_for_week()` derives whose turn it is from the Monday's
ordinal — deterministic, stateless, and free of the year-boundary seam that
`iso_week % n` has (a 53-week year would otherwise hand the same project two
weeks running).

Rotation is a preference, not a straitjacket: if the week's project has no
eligible landing — or its mirror is unreachable — `_run_lesson_step` falls
through to the others rather than burning the slot. Whoever writes it takes the
week. Watch for a repeated `"Lesson skipped for X — source repo unavailable"`
in the nightly logs: that means the rotation is silently degrading to a single
project.

### Source access degrades in three grades, not two

`SourceRepo.ensure()` treats "cannot reach the mirror" and "have no source" as
different problems, because they are:

| State | Behaviour |
|---|---|
| Clone present, `git fetch` succeeds | Normal. |
| Clone present, **fetch fails** | `is_stale = True`. Reads are served from the cached objects, which hold the project's whole history up to the last successful fetch. |
| Clone present but **not a readable git repo** | Discarded and re-cloned. An interrupted clone answers every read with `[error]`; serving that as "cached state" produces a confidently wrong article. |
| **No clone** and cloning fails | `SourceRepoError` — the only genuinely fatal case. |

A stale clone would still lose the week on its own, because `pick_subject`
filters candidates through `resolve()` and the newest commits aren't in there.
So `_run_lesson_step` passes `fallback_weeks=4` when `repo.is_stale`, and the
picker walks backwards until it finds a commit the clone actually has. An
unreachable mirror therefore costs *freshness*, not the article.

Two boundaries keep that honest. It triggers **only when the target week had
candidates that failed to resolve** — never on a week with nothing eligible,
since an empty week is a quiet week and reaching into the past to fill it would
be dishonest. And the subject is **rebased onto the target week**
(`dataclasses.replace(subject, week=week)`): `lesson_id`, the week range and the
sort date all still name the published week, and only `commit_date` reveals the
subject is older.

This is deliberate and has a useful property: it **self-heals**. If Monday's
run fails, Tuesday's picks the same week up. A cron expression pinned to Monday
would simply lose that week.

The target is always the most recent **complete** Mon–Sun week
(`previous_complete_week()`). Targeting the current week would mean the Monday
02:00 run choosing from a pool of roughly nothing.

### Selection is deterministic — no LLM

`lesson_picker.py` reads landing frontmatter and ranks: impact score first,
then a subsystem the last four lessons haven't covered, then recency. Score
floor is 6 (higher than the daily version's 5 — a week's pool is ~10× a day's,
so we can afford to be pickier). Stubs and spam are excluded, mirroring
`web/src/lib/visibility.ts`.

A candidate is only viable if its SHA resolves in the mirror. Mirror lag is
routine, so the picker walks the ranked list and takes the first commit it can
actually read — a miss is never a failure.

### The editorial remit — `lesson_topics.py`

A high impact score is not the same as being worth teaching. The corpus
carries every GCC front end and forty binutils targets; `cobol` and `fortran`
alone are ~180 of the GCC landings on disk, and the first real run duly picked
`gcc/cobol` and `gcc/alpha`. The policy, set by the project owner:

* **GCC languages: C, C++, Ada, Rust only.** COBOL, Fortran, Go, D, Modula-2
  and Objective-C are out.
* **Architectures: Arm/AArch64, x86, POWER, RISC-V.** Alpha, Xtensa, SH, AVR,
  s390, LoongArch, z80 and the rest are out — a lesson on an ISA nobody can
  run teaches nothing.
* **No housekeeping** — testsuite-only churn, MAINTAINERS, translations, CI.

Everything that is neither language- nor architecture-specific — the middle
end, `tree-optimization`, `libstdc++`, `bfd`, `ld`, `gas` — is always fair
game, and that is where most of the instructive work lives.

The whole policy is four frozensets at the top of `lesson_topics.py`; widen
the remit by editing `BIG_ARCHES`, not the picker. Note that a token absent
from `KNOWN_ARCHES` is *not* arch-gated at all, so a brand-new port stays
publishable until someone lists it.

### Reading the source — `tools/source_repo.py`

    git clone --bare --filter=blob:none -- <mirror-url> agents/cache/<name>.git

**Bare** means no working tree (GCC is ~2 GB checked out). **Blobless** means
commits and trees now, file contents only for the handful of files actually
opened — measured at ~640 MB for GCC, which fits the CI cache. Reads are served
by git itself, pinned to one commit:

    git show <sha>:<path>            the file exactly as it was
    git grep -n <pat> <sha> -- ...   a search of the tree at that commit

So the agent never fetches a sourceware page, never scrapes, and never sees a
file from a different revision than the one it is writing about.

Repos are declared under a **`source_repos:`** block in `sources.yml` — kept
separate from `sources:` because these are *read*, not *ingested*.

### Two stages, and why

| Stage | Model | Shape | Output |
|-------|-------|-------|--------|
| `run_research()` | `LESSON_RESEARCH_MODEL` (cheap reasoning tier) | many turns, repo tools, 16-call cap | `LessonResearch` — verbatim source excerpts + notes |
| `run_writer()` | `LESSON_WRITER_MODEL` (Opus tier) | **one** call, no tools | `LessonDigest` |

The split is a cost decision. A multi-turn agent resends its whole conversation
every turn, so spend grows *quadratically* with tool calls — the worst possible
shape to pay premium rates for. Running Opus through the exploration loop costs
several euro per article against a €5/month ceiling. Exploring cheaply and
writing once buys the same prose for roughly a sixth of that.

It has a second effect worth knowing: **the writer never opens a file.**
Everything it may assert has to be in the dossier, which is why excerpts are
stored verbatim rather than summarised — a paraphrase there becomes a wrong
identifier in the published article. `_drop_unread_code_refs()` then re-checks
every path the writer cites against the real tree and drops what isn't there.

Both calls log to `output/usage.log` under distinct agent names
(`lesson_research`, `lesson_writer`) so the two-stage cost is separable.

---

## The Budget Guard

The project ceiling is **EUR 5/month**, and until now that was only a comment:
tokens were logged, money was never counted. `budget.py` closes the loop.

    usage.log (tokens per call)  x  OpenRouter /models (price per token)
        ->  month-to-date USD  ->  "can we afford another lesson?"

`_run_lesson_step` calls `can_afford()` **before** cloning or calling a model.
Checking after the fact would permit exactly one unbounded overshoot, and the
lesson is the single most expensive call this project makes. When the month is
spent the step logs the two numbers and returns 0; lessons resume on the 1st.

The guard is scoped to lessons on purpose — the digests are the product, the
lesson is the garnish, so it is the right thing to drop first. `can_afford()`
makes a digest-side guard a two-line change if that ever becomes necessary.

Two properties keep it honest:

- **Unknowns are expensive.** A model missing from the price listing, or a call
  whose token counts came back null, is charged at a deliberately pessimistic
  rate. A guard that prices what it doesn't recognise at zero has stopped
  guarding without telling anyone.
- **The cap is USD 5 for a EUR 5 limit.** OpenRouter bills in dollars and USD 5
  is below EUR 5 at any plausible rate, so no exchange rate is needed and the
  error is on the safe side.

**`agents/output/usage.log` is committed, not ignored** — that is load-bearing,
not an oversight. A CI runner starts with a clean tree, so an ignored ledger
would make every run compute a spend of zero and the cap would never bind.

`check_models.py` is the companion preflight: it verifies every configured slug
against the free `/models` listing before anything spends, and prints the
closest available names on a miss. A wrong slug otherwise fails only at request
time, after the run has paid for everything leading up to it.

---

## Environment Variables

| Var | Purpose | Required? |
|-----|---------|-----------|
| `OPENROUTER_API_KEY` | LLM calls | yes for real runs |
| `GITHUB_TOKEN` | Raise GitHub rate limit from 60→5000/h | strongly recommended |
| `SUMMARISER_MODEL` | Override the cheap model | optional |
| `BENTO_MODEL` | Override the premium re-run model | optional |
| `LESSON_RESEARCH_MODEL` | Override the lesson's source-exploration model | optional |
| `LESSON_WRITER_MODEL` | Override the lesson's article-writing model | optional |
| `MONTHLY_BUDGET_USD` | Override the $5 monthly cap (testing) | optional |
| `LESSON_COST_ESTIMATE_USD` | Override the assumed per-lesson cost | optional |

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

# Lesson only, against the content already on disk (no ingestion, no digests).
# Defaults to the newest complete ISO week; --lesson-week pins one explicitly.
python -m agents.main --lesson-only
python -m agents.main --lesson-only --lesson-project gcc --lesson-week 2026-W36

# The same thing in CI: the Nightly Digest workflow takes `lesson_only` and
# `lesson_weeks` dispatch inputs. `lesson_weeks: 2` writes the last two
# complete weeks (one lesson each, projects alternating). Default is 1 —
# each lesson is a premium-model call, so a dispatch asking for four spends
# roughly a third of the month's AI budget in one run.
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

For the lesson stage specifically:
`test_source_repo.py` (git-option injection, the unscoped-grep refusal, output
caps), `test_lesson_picker.py` (ISO-week arithmetic including year rollovers,
ranking, the idempotence guard), `test_lesson_writer.py` (long-form bodies pass
while the truncation and quoted-email detectors still fire), and
`test_lesson_agent.py` (forced identity fields, the fabricated-path guard, the
tool budget). Git is mocked throughout; one real-clone integration test in
`test_source_repo.py` is opt-in via `RUN_GIT_TESTS=1` since it needs network
and hundreds of MB.

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
4. If the field is *required* there, add it to `_REQUIRED` in
   `tools/validate_content.py` — that gate is what stops malformed frontmatter
   from taking the Cloudflare Pages build down. Date-typed fields also go in
   `_EXTRA_DATE_FIELDS`.
5. Run `pytest agents/tests` — writer tests will flag frontmatter mismatches.

**Add a project to the lesson rotation**:
1. Add it to the `source_repos:` block in `sources.yml` with a git mirror URL
   that carries the same SHAs as the project's canonical repo (otherwise
   `SourceRepo.resolve()` will never match a landing).
2. Nothing else — `_run_lesson_step()` iterates whatever `load_source_repos()`
   returns. A project with landings but no source repo simply gets no lesson.

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

### Lesson-specific

- **`grep_repo` must never run unscoped.** It rejects an empty pathspec by
  design. On a blobless clone a tree-wide grep lazily faults in *every blob in
  the repository* — the one way this design becomes slow and expensive. The
  agent is seeded with the directories the commit's own diff touched.
- **The weekly cadence lives in the idempotence guard, not a schedule.** Don't
  "fix" the nightly invocation by adding a day-of-week condition — you'd lose
  the self-healing property and gain nothing.
- **That guard is week-scoped, not project-scoped.** `existing_lesson_for_week`
  asks "does *any* project have this week's lesson?" Narrowing it back to one
  project would let the second project write a second lesson the same week and
  double the premium-model bill — the exact thing the alternation exists to
  avoid.
- **A repeated "source repo unavailable" warning means the rotation has
  silently collapsed.** The fallback keeps a week from being wasted when one
  project's mirror is unreachable, which is right — but if it fires every week,
  one project is quietly never getting a lesson. Check the nightly logs.
- **The writer's citations are verified, not trusted.** It works entirely from
  the dossier and never opens a file, so `_drop_unread_code_refs()` checks
  every `code_tour` path against the tree. Removing that check is how a
  fabricated file reference reaches the published page. `/admin/lessons` has a
  "no code tour" filter precisely to surface this failure.
- **Excerpts in the dossier are verbatim.** They are the writing model's only
  view of the source; summarising them there produces paraphrased identifiers
  in the article, which the root CLAUDE.md's article conventions forbid.
- **The lesson step must never fail the nightly run.** It is wrapped in
  `try/except` in `main.py` and `continue-on-error` in the workflow. A clone
  failure or a model outage degrades to a stub, not a lost digest.
- **A `lesson_id` always names the week being published, never the subject's
  week.** The stale-clone fallback can teach a commit from three weeks ago, but
  the lesson is still filed under the target week. If the identity moved with
  the subject, `existing_lesson_for_week` would stop matching and the nightly
  step would rewrite — and re-bill — the same lesson every night.
- **Don't widen the stale-clone fallback to fire on an empty week.** It exists
  for source-access failure. A week with no eligible landings should produce no
  lesson; backfilling one from an older commit would misrepresent the week.
- **`_MAX_TOOL_CALLS` is the primary cost lever.** Lower it before reaching for
  a cheaper writing model; Opus-level prose for the lesson is a requirement,
  not a default. Verify real spend in the `lesson_research` / `lesson_writer`
  rows of `output/usage.log`.
- **A lesson's `date` is the END of the week it covers**, not the commit's
  date — so it sorts with its week. `commit_date` carries the real landing
  date for display. Three separate date fields, three separate facts.
- **A stub never claims its week.** Both week guards skip `is_stub: true`, and
  `recent_subsystems` ignores stubs too. A stub records a *failed* run; if it
  counted as a lesson, one bad night would burn that week permanently — the
  exact opposite of the self-healing the nightly cadence is built on. A
  successful retry deletes the stub it supersedes (`_drop_superseded_stubs`).
- **Never resolve a model name with `os.environ.get(KEY, DEFAULT)`.** Use
  `model_from_env()`. GitHub Actions exports an unset `${{ vars.X }}` as
  *present and empty*, so the plain form yields `""`, and an empty slug fails
  every request. That is what turned the first real lesson run into two
  `research_failed` stubs behind a green checkmark.
  `test_model_from_env.py` fails the build if any `agents/*.py` regresses.
- **`continue-on-error` plus stub-on-failure can hide a total failure.** The
  step goes green and commits placeholder articles. When a run "succeeds",
  check `is_stub` in the output before believing it.
- **The writer sends an explicit `max_tokens` (`LESSON_WRITER_MAX_TOKENS`) and
  must keep doing so.** OpenRouter doesn't bill the reservation but it does
  *reserve* against the key's balance and returns a hard 402 when the balance
  can't cover it. With no cap the model's own ceiling applies — 65536 tokens
  for claude-opus-5 — which is unaffordable on a nearly-spent key, so every
  writer call fails before generating a single token. That is what stubbed the
  2026-09-13 and -14 lessons. A lesson tops out around 13k tokens; the cap is
  headroom, not a quality lever.
- **A null is not a validation failure for the dossier.** `LessonResearch`
  drops explicit `null`s for fields that have defaults, because a model
  answering `"external_context": null` means "found nothing" and a
  ValidationError there is non-retryable — it costs the whole week's lesson.
  Required identity fields still reject a null.
- **Neither lesson stage parses JSON out of a model's prose.** Both use a
  PydanticAI `output_type`, like the discussion and landing agents, so
  *encoding* is the provider's job. That is not cosmetic: the dossier carries a
  raw diff and verbatim C, and hand-encoding those into JSON strings is what
  killed two of the four stubs on disk (`Invalid \escape`,
  `Expecting ',' delimiter`), thousands of characters in, after the whole
  research loop had been paid for. Don't go back to `output_type=str` plus a
  brace scanner.
- **The `output_type` is the lenient draft, never the strict model.** The caps
  in `models/lesson.py` are *repairs* applied after generation
  (`_clamp_to_schema`, `_repair_lesson_item`), not requirements the model has
  to satisfy — `read_file` hands back 8192 bytes where `SourceExcerpt.code`
  caps at 6000, so a model that copies an excerpt verbatim, exactly as
  instructed, overruns. Put those caps in the schema and a trim becomes a
  validation failure and a paid reprompt. `models/draft.py` derives the twins;
  `test_research_draft_mirrors_the_strict_model` fails if they ever drift.
- **The writer is not asked to echo identity.** `LessonDraft` omits every field
  `_repair_lesson_item` forces from the subject (commit hash, project, url, the
  three dates). Adding them back spends tokens on values a typo would
  mislabel the whole article with.
- **A nullable-everything schema is an invitation the model will take.** The
  draft strips length *caps*, not *obligations*. When every dossier field was
  nullable, the explorer read the schema as "the two identity fields are a
  complete answer", returned after one tool call and 53 tokens, and the writer
  spent $0.08 of Opus truthfully explaining that it had no evidence — an
  article with `is_stub: false`, committed, one merge from the front page.
  Under `output_type=str` the prompt carried that obligation; with a schema,
  the schema carries it. `LESSON_RESEARCH_REQUIRED` in `models/lesson.py` is
  what keeps the diff and the excerpts non-optional.
- **An empty dossier must fail as a stub, never as an article.** The writer
  never opens a file, so with nothing to work from it does not error — it
  writes *about* having nothing, at length and in good faith, and that passes
  every downstream check. `_assert_dossier_has_evidence` rejects a dossier with
  no excerpts, or with neither a diff nor a commit message, so the failure
  reads as the stage-1 failure it is. It raises `ValueError`, which *is*
  retried: unlike a schema mismatch, an explorer that returned early often does
  the work on a second ask, and stage 1 is the cheap tier.
- **Nothing diagnostic may sit between the pipeline and the commit step.** The
  `lesson-run` artifact upload is `continue-on-error` for this reason: it runs
  *before* validate → build → commit, and when the account's artifact storage
  quota filled up it failed the job and threw away two nights of digests. A
  log file must never be able to block publishing content.
- **Never let the budget guard price something at zero.** An unknown model or a
  null token count must be charged at the pessimistic rate in `budget.py`.
  Failing toward "free" silently disables the cap, which is worse than having
  no guard at all because it looks like one.
- **`agents/output/usage.log` must stay committed.** Re-adding it to
  `.gitignore` makes every CI run see a month-to-date spend of zero and the
  EUR 5 cap stops binding entirely.
