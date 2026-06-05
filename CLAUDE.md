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
| Cheap summariser model | `google/gemini-2.5-flash` or `mistralai/mistral-small` | Near-zero cost for bulk work |
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
- **`primer_expert` — "In Details" block (toolchain folks).** 2–4
  sentences, ≤ 500 chars. Rendered at full opacity as a labelled section.
  Assume the reader already knows compiler passes, ELF/DWARF, relocations,
  PIC/PIE, ABI conventions, libc internals. Do NOT define those. Instead,
  place THIS specific subsystem inside that map: name the concrete file /
  pass / invariant / data structure (e.g. `gcc/ipa-sra.cc` +
  `IPA_PARAM_DESCRIPTOR`), note why a toolchain dev outside this subsystem
  still wouldn't instantly recognise it, and flag non-obvious interactions
  with neighbouring subsystems.
- **`primer_glossary` — Glossary block (devs who are not toolchain experts).**
  An array of `{ term, definition }` objects rendered as a labelled glossary.
  Include every non-obvious component, concept, flag, or subsystem name that
  appears in the article and that a competent software engineer outside the
  toolchain world would not immediately know. Many items are expected — err on
  the side of more entries, not fewer. Each `term` should be the exact name as
  it appears in the article (e.g. `IPA`, `SRA`, `-fipa-sra`, `ELF relocations`,
  `THP`). Each `definition` should be 1–3 sentences: what it is, what problem
  it solves, and where it sits in the pipeline (source → IR → object → binary →
  runtime) when that context matters. Do NOT restate the commit's effect — only
  background. Example frontmatter:
  ```yaml
  primer_glossary:
    - term: "IPA (Interprocedural Analysis)"
      definition: "A family of GCC optimization passes that reason about the whole program rather than one function at a time, allowing the compiler to inline, specialize, or eliminate functions it would otherwise treat as black boxes."
    - term: "SRA (Scalar Replacement of Aggregates)"
      definition: "A compiler pass that breaks up struct and array variables into individual scalar variables so they can be kept in registers, avoiding memory traffic."
  ```

## What Claude Should NOT Do
- Do not add features beyond the current phase.
- Do not change the storage format (stay Markdown).
- Do not use any LLM provider other than OpenRouter.
- Do not install heavy ML frameworks (torch, transformers, etc.).
- Do not hardcode API keys or tokens anywhere.
