# Plan — Lift Agent Output Quality to a WSJ-for-Devs Standard

## Context
A PM-style read of `web/src/content/landings/` and `web/src/content/discussions/`
shows the pipeline works end-to-end but the **content is not publishable** for a
WSJ-style open-source dev journal. Symptoms across ~60 sampled files:

- **Landings** are raw commit-message fragments, truncated mid-sentence, with
  `subsystem: unknown` on every file, `impact_score: 5` for ~90% of items,
  `patch_id / discussion_id_link / bugzilla_pr` null on **every** file, and
  zero-value noise commits ("Daily bump.") shipped as articles.
- **Discussions** use raw mailing-list subjects as titles (`[PATCH v3 4/8] …`,
  leading `Re:`), dump quoted email threads as the body ("On Thu, Apr 16 … wrote:"),
  carry `consensus: Proposed` even when the filename says `commited`, have
  `technical_tradeoffs: []` everywhere, and fragment a single patch series into
  5–8 near-identical articles.
- **No "why should a dev care?" framing, no outcome signal, no editorial voice**,
  no tags/topic taxonomy, no TLDR, no hero media hooks — nothing a Bento/Pulse
  Stream UI can present as a premium feed.

This plan targets the agents (`landing_agent.py`, `discussion_agent.py`),
shared schema (`models/`), writer (`writer.py`), and ingestion filtering —
keeping within the €5/mo budget by preserving batching and the cheap-model
default path.

## Goals
1. **Every published article is readable by a working dev unfamiliar with the subsystem.**
2. **Titles, subsystems, and slugs are human-meaningful** (no `unknown`, no `[PATCH v3 4/8]`, no raw `Re:`).
3. **Impact / sentiment scores vary meaningfully**; low-value noise is filtered.
4. **Patch series and reply threads are de-duplicated** into one story.
5. **Rich metadata supports a Bento/WSJ-style UI** (TLDR, tags, outcome, stakes).
6. **No budget regression**: still batched, still cheap-model-first, premium only for impact_score ≥ 9.

---

## Workstreams

### WS1 — Schema upgrades (`agents/models/`)
Add the fields the UI needs and the agents will now emit. Mirror in the Astro
content config.

- `agents/models/base.py`: add `tags: list[str]` (free-form topic tags, max 5)
  on `BimodalBase`.
- `agents/models/landing.py` (`LandingDigest`): add
  - `headline: str` — human-readable title (not the raw commit subject line)
  - `tldr: str` — one sentence, ≤ 140 chars
  - `why_it_matters: str` — 1–2 sentences, dev-facing stakes
  - Keep existing `summary` as the 2–4 sentence body.
- `agents/models/discussion.py` (`DiscussionDigest`): add
  - `headline: str` — translated title (strip `Re:` / `[PATCH …]` / version tags)
  - `tldr: str`
  - `stakes: str` — why the proposal matters
  - `series_id: str | None` — groups N-of-M patches into one story
  - `series_role: Literal["cover", "reply", "standalone"] | None`
  - `outcome: Literal["proposed","under_review","needs_revision","nackd","ready","committed","withdrawn","stalled"]`
    — replace the LLM-guessed `consensus` single status with a richer enum
    backed by deterministic signals (see WS3).
- Update `writer.py` frontmatter builders to emit the new fields (lines 75–89
  and 109–123) and mirror the schema in `web/src/content/config.ts`.

### WS2 — Ingestion-side noise filter (`agents/ingestion/engine.py`)
Drop items before we pay to digest them. Cheap deterministic rules:

- Commits whose message matches `^(Daily bump\.|Update copyright years|Regenerate .*|Bump version)$`
  or `^Merge (branch|tag|pull)` → dropped unless they touch security-relevant paths.
- Commits with `files_changed == 0` or only `.po`/`ChangeLog` edits → dropped.
- Discussions whose body is < 200 chars and has no diff → dropped (pings, "+1",
  empty re-send).

Log counts under `output/usage.log` so the filter is observable.

### WS3 — Series grouping & outcome derivation (new `agents/tools/series.py`)
Already have `series_aware_batches`; extend it to *collapse* a series into a
single article rather than just batch-co-locating it.

- Detect series from subject regex `\[(?:RFC\s+)?PATCH(?:\s+v\d+)?\s+(\d+)/(\d+)\]`
  and from `In-Reply-To:` chains for public_inbox.
- Keep only the cover letter (`0/N`) OR the latest `vN 0/N` as the canonical
  story; other parts become `series_parts: list[{title, url}]` metadata on the
  canonical item.
- Derive `outcome` deterministically from signals *before* the LLM runs:
  - filename/subject tag `[committed]` → `committed`
  - `NACK`/`Nacked-by:` in any reply → `nackd`
  - `Reviewed-by:` or `LGTM` + no newer version → `ready`
  - last activity > 60 days, no merge → `stalled`
  - default: `proposed`.
- Pass `outcome` as an input hint so the LLM narrates, not guesses.

### WS4 — Subsystem extraction, deterministic-first (`agents/tools/subsystem.py`, new)
Never write `subsystem: unknown` again.

- Regex subject/commit-title parser first:
  - `^(?P<sub>[a-z0-9/+_.-]+):\s` → captures `middle-end`, `gcc/ipa`, `tests/elf`, `malloc`, etc.
  - Fallback to top-level changed directory from `diff_stat` (`gcc/`, `libc/`, `ld/`).
- Project-specific allowlist per source in `sources.yml` (e.g. for glibc:
  `malloc, nptl, math, elf, stdio, string, sysdeps, nss, locale, tests`).
- Only call the LLM for subsystem when both fail; then validate the LLM answer
  against the allowlist and reject free-form answers.
- Applied in `landing_agent._apply_trailers` area (after LLM output, before writer).

### WS5 — Prompt rewrites (`landing_agent.py:57–75`, `discussion_agent.py:29–43`)
Replace minimal prompts with style-guided prompts. Keep JSON-only output.

Key additions for **both** prompts:
- Audience: "A working systems developer who does not specialise in this
  subsystem. They should understand the change in under 30 seconds."
- Writing style: active voice, concrete verbs, no filler ("In a nutshell",
  "This patch aims to…", "See commit message"). No bracketed mailing-list
  artefacts in headlines. No leading `Re:`.
- Impact/sentiment rubric with anchored examples:
  - 9–10: CVE, ABI break, perf ≥ 10%, new arch/language feature.
  - 7–8: user-visible feature, non-trivial optimisation, toolchain policy.
  - 4–6: refactor, internal API, test infra, bugfix without user impact.
  - 1–3: typo, comment, docs, cosmetic.
  - Require a one-line justification → new `impact_rationale: str` field (WS1 addendum).
- Require `headline`, `tldr`, `why_it_matters`/`stakes`, `summary`, `tags` as
  separate fields (schema-enforced).
- Forbid echoing quoted email lines (`^>`, `On … wrote:`) into the body.

### WS6 — Body rendering discipline (`writer.py` + agents)
- Agents return `summary` only (prose, 2–4 sentences). Raw email quoting or
  commit message text is never copied verbatim into `summary`.
- `writer.py` sanity-checks body before writing: reject if
  - ends mid-word / with a trailing dangling `[` or `(`
  - starts with `Re:` / `>` / `On … wrote:`
  - < 30 words or > 250 words
  On reject, fall back to stub message `"Summary unavailable — see source link."`
  and log — better a visible gap than a broken article.
- Extend `_stub_digests` in both agents to populate the new required fields
  (`headline` = cleaned title, `tldr` = first sentence, `outcome` = derived).

### WS7 — De-duplication across reply threads (`agents/dedup.py`)
Current dedup is by `discussion_id` / `commit_hash`. Add:
- Index by `series_id` — second-and-later hits are stored as `series_parts`
  pointers on the canonical file, not as new files.
- Index by `patch_id` (already computed) so `DiscussionDigest` → `LandingDigest`
  cross-links are populated in the writer, not guessed.

### WS8 — Tests (`agents/tests/`)
- `test_noise_filter.py`: "Daily bump." and copyright-year commits are dropped.
- `test_subsystem_extract.py`: 20 real commit subjects → correct subsystem,
  never `unknown`.
- `test_series_collapse.py`: `[PATCH 0/5]`…`[PATCH 5/5]` collapse to one item
  with 5 `series_parts`.
- `test_writer_reject.py`: truncated / `Re:`-prefixed / too-short bodies are
  rejected and the stub body is written.
- `test_prompts.py` (golden): snapshot of rendered system prompts so prompt
  drift is a reviewable diff.

---

## Critical files to modify
- `agents/models/base.py`, `agents/models/landing.py`, `agents/models/discussion.py` (WS1)
- `agents/ingestion/engine.py` (WS2)
- `agents/tools/series.py` *(new)*, `agents/tools/subsystem.py` *(new)* (WS3, WS4)
- `agents/landing_agent.py` — prompt (L57–75), batch render (L122–139), trailer apply (L289–328), stubs (L392–406) (WS5, WS6)
- `agents/discussion_agent.py` — prompt (L29–43), batch render (L47–66), stubs (L190–209) (WS5, WS6)
- `agents/writer.py` — frontmatter dicts (L75–89, L109–123), new body validator (WS1, WS6)
- `agents/dedup.py` — series/patch_id indices (WS7)
- `web/src/content/config.ts` — Astro schema mirror for new fields (WS1)
- `agents/tests/…` (WS8)

## Reuses existing code (do not reimplement)
- `agents/tools/series_grouping.py::series_aware_batches` — extend, don't replace.
- `agents/landing_agent.py::_extract_trailers` + `_apply_trailers` — already
  deterministic; feed their outputs as LLM hints (WS3).
- `agents/tools/patch_id.py::extract_patch_id` — use as the cross-index key in
  dedup (WS7).
- `agents/_retry.py::retry_with_backoff` and `agents/usage_log.py::append_usage`
  — all new LLM calls must route through these.

## Budget guardrails (HARD)
- No per-item LLM calls. All new prompts stay inside the existing batched
  calls (15 commits, 10 discussions).
- Subsystem/outcome/series detection is deterministic first; LLM fallback is
  capped at ~10% of items via the allowlist check.
- Premium model still gated on `impact_score ≥ 9`. New `impact_rationale`
  must not raise average token count by > 15% (enforce in test).

## Verification
1. `pytest agents/tests -q` — all new tests green; existing tests still pass.
2. Dry run: `python -m agents.main --since-hours 24 --dry-run` — confirm stub
   digests now carry `headline`, `tldr`, `outcome`, no `subsystem: unknown`.
3. Live run on a recent 24 h window. Success criteria on the produced files:
   - 0 files with `subsystem: unknown`
   - 0 files whose body ends mid-word or starts with `Re:`/`>`
   - `impact_score` distribution spans ≥ 4 distinct values
   - `Daily bump.`-style commits do not appear
   - Any `[PATCH N/M]` series produces exactly 1 file with populated `series_parts`
   - `technical_tradeoffs` non-empty on ≥ 50% of discussion digests
4. Spot-read 10 random files as a non-specialist dev: each should be
   understandable in ≤ 30 seconds. If not, tighten the prompt rubric.
5. `tail -n 50 agents/output/usage.log` — daily token spend unchanged within
   ±15% of baseline.
