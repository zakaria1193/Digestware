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
│   ├── index/       # derived SQLite search index over the Markdown corpus
│   ├── mcp/         # MCP server exposing that index to agents
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
| Premium model (Bento logic) | `anthropic/claude-sonnet-5.5` | Only for final ranking / formatting |
| Frontend | Astro 6 + Tailwind 4 | Static-first, Content Collections, fast |
| Newsletter | Resend API + React Email | Developer-friendly, generous free tier |
| Storage | Markdown files in Git | Zero infra cost, version-controlled history |

## Search Index & MCP (`agents/index/`, `agents/mcp/`)
The Markdown corpus doubles as a queryable record of GCC/binutils change history.
`python -m agents.index.build` derives `agents/index/pulse.db` (SQLite + FTS5) from
`web/src/content/**`, and `python -m agents.mcp.server` serves it over MCP so an agent
can search changes, look up identifiers, and pull candidate leads for a regression.

- **The index is derived and disposable.** Markdown remains the sole source of truth;
  nothing in `agents/index/` ever writes back to it, and the `.db` is gitignored.
- **No LLM calls at query time.** The MCP server does retrieval only — the calling
  agent supplies the reasoning — so query volume cannot affect the budget.
- **The corpus holds no diffs or test results.** Tools must present hits as leads to
  verify upstream, never as proof that a change caused a regression.

### Embeddings — the one exception to "OpenRouter only"
OpenRouter exposes no embeddings endpoint, so `agents/index/embed.py` talks to an
OpenAI-compatible `/embeddings` provider configured by `EMBEDDING_BASE_URL` /
`EMBEDDING_MODEL` / `EMBEDDING_API_KEY`. This is the **only** sanctioned non-OpenRouter
provider, it is confined to that one module behind the `EmbeddingProvider` protocol, and
its spend is logged to `agents/output/usage.log` like every other call. All *generation*
still goes through OpenRouter, without exception.

**Cost, and the one thing that controls it.** The corpus is ~1.4M characters (~400k
tokens), so embedding all of it is well under a cent. The nightly run must stay
*incremental* for that to remain true: the CI job restores `pulse.db` from
`actions/cache` and runs the build **without `--full`**, so only files whose content hash
changed are re-embedded — a few thousand tokens a night, flat regardless of how large the
archive grows. Remove the cache step or add `--full` back and every run re-embeds the
entire corpus instead, which costs ~30x more today and scales linearly with the archive.
Set no `EMBEDDING_API_KEY` at all and the build is lexical-only and free.

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
- **`primer_glossary` — "For Context" block (systems programmers who aren't
  toolchain experts).** Rendered as a series of definitions, not prose — an
  array of `{ term, definition }` objects. The reader is a working systems
  programmer: assume they already know pointers, processes, syscalls, the
  stack/heap, and the source → object → binary → runtime pipeline in
  outline. Do NOT define those. Only include toolchain-specific jargon that
  appears in the article and that a systems programmer outside this
  subsystem would not immediately recognise — compiler passes, IR forms,
  ABI/ELF/DWARF terms, subsystem names, flags, data structures. Many items
  are expected — err on the side of more entries, not fewer. Each `term`
  should be the exact name as it appears in the article (e.g. `IPA`, `SRA`,
  `-fipa-sra`, `ELF relocations`, `THP`). Each `definition` should be 1–3
  sentences: what it is, what problem it solves, and where it sits in the
  pipeline when that context matters. Do NOT restate the commit's effect —
  only background. Example frontmatter:
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
- Do not use any LLM provider other than OpenRouter (embeddings excepted — see above).
- Do not install heavy ML frameworks (torch, transformers, etc.).
- Do not hardcode API keys or tokens anywhere.
