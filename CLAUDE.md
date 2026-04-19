# OS Pulse — Project Brain

## What This Is
A monorepo that fetches, digests, and publishes a daily "Bento" of open-source OS-level changes
(GCC, binutils, kernel patches, etc.) as a beautiful web feed and newsletter.

## Monorepo Layout
```
Digestware/
├── agents/          # Python — PydanticAI digest engine
│   ├── tools/       # individual tool modules (git fetch, web search, …)
│   ├── models/      # Pydantic output schemas (BentoDigest, …)
│   └── output/      # local Markdown output for dev/testing
├── web/             # Astro 6 — Bento Grid + Pulse Stream UI
│   └── src/
│       ├── content/digests/   # Markdown files written by the agent
│       ├── pages/
│       ├── components/
│       └── layouts/
├── .github/workflows/         # GitHub Actions (daily-digest.yml)
└── CLAUDE.md
```

## Technology Stack
| Layer | Choice | Why |
|-------|--------|-----|
| AI runtime | PydanticAI | Typed, structured output; easy tool registration |
| LLM provider | OpenRouter | Model-agnostic, pay-per-token |
| Cheap summariser model | `google/gemini-2.0-flash-001` or `mistralai/mistral-small` | Near-zero cost for bulk work |
| Premium model (Bento logic) | `anthropic/claude-sonnet-4-5` | Only for final ranking / formatting |
| Frontend | Astro 6 + Tailwind 4 | Static-first, Content Collections, fast |
| Newsletter | Resend API + React Email | Developer-friendly, generous free tier |
| Storage | Markdown files in Git | Zero infra cost, version-controlled history |

## Budget Constraints — HARD LIMITS
- **Total AI spend: ≤ €5 / month**
- Use cheap models for ALL bulk operations (commit fetching, summarisation, search).
- Reserve premium models only for the final Bento ranking step.
- Always batch requests; never call the LLM per-commit when a batch is possible.
- Log token usage after every agent run to `agents/output/usage.log`.

## Coding Conventions
- **Python**: 3.12+, `ruff` for linting, `pyright` for type checking, `pytest` for tests.
- **TypeScript/Astro**: strict mode, Prettier for formatting.
- **No secrets in code**: use `.env` (gitignored) and GitHub Actions secrets.
- Prefer composition over inheritance.
- Keep agent tools small and single-purpose.

## Key Data Model
```python
class BentoDigest(BaseModel):
    title: str
    subsystem: str          # e.g. "gcc/ipa", "binutils/ld", "kernel/mm"
    impact_score: int       # 1–10
    summary: str            # 2–4 sentences, plain English
    is_bento_worthy: bool   # True → appears in top Bento Grid
    commit_sha: str
    source_url: str
    date: datetime
```

## Output Convention
Agent writes Markdown files to `web/src/content/digests/YYYY-MM-DD-<slug>.md`
with full frontmatter matching `BentoDigest` fields.

## Article Writing Conventions
When writing articles from mailing-list exchanges, commit messages, or other
technical source material:

- **Stay technically precise.** Preserve exact filenames, function names, macro
  names, struct/field names, flag names (e.g. `-fipa-sra`, `CONFIG_SLUB`),
  commit SHAs, symbol names, and ABI/ISA terminology verbatim. Do not
  paraphrase identifiers. Quote the relevant snippet when it clarifies intent.
- **Link the code.** Reference paths in the original repo (e.g.
  `gcc/ipa-sra.cc`, `mm/slub.c`) so experts can jump straight to the source.
- **Mandatory section — "What is this even about?"** Every technical article
  MUST include a section with that exact heading, aimed at a competent software
  engineer who lacks this specific subsystem's context. It should briefly
  explain the subsystem, the problem space, and any jargon the rest of the
  article assumes (3–6 sentences; no hand-waving, no dumbing down — just
  context).
- Place the "What is this even about?" section near the top, after the lede
  and before the deep-dive.

## What Claude Should NOT Do
- Do not add features beyond the current phase.
- Do not change the storage format (stay Markdown).
- Do not use any LLM provider other than OpenRouter.
- Do not install heavy ML frameworks (torch, transformers, etc.).
- Do not hardcode API keys or tokens anywhere.
