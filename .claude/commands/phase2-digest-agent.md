# Phase 2 — The Digest Agent (PydanticAI)

Build the Python engine that fetches OS-level commits, enriches them via web search,
and outputs structured Markdown digests.

## Tasks

### 1. Data model (`agents/models/digest.py`)
Define a `BentoDigest` Pydantic model with these fields:
- `title: str`
- `subsystem: str`  — e.g. `"gcc/ipa"`, `"binutils/ld"`, `"kernel/mm"`
- `impact_score: int`  — 1–10
- `summary: str`  — 2–4 sentences, plain English
- `is_bento_worthy: bool`  — True → appears in the Bento Grid
- `commit_sha: str`
- `source_url: str`
- `date: datetime`

### 2. Tools (`agents/tools/`)
Create two tool modules usable by the PydanticAI agent:

**`agents/tools/git_fetcher.py`**
- Fetch recent commits from GCC and binutils Git mirrors (use `httpx` against
  `https://gcc.gnu.org/git/gcc.git` or the GitHub mirrors).
- Return a list of raw commit dicts: `{sha, author, date, message, diff_stat}`.
- Accept a `since_hours: int` parameter (default 24) to limit the window.

**`agents/tools/web_search.py`**
- Accept a query string and return the top-5 DuckDuckGo snippets.
- Use `duckduckgo-search` (`DDGS().text(query, max_results=5)`).
- Called only when a commit message is cryptic (< 20 words or no subsystem tag).

### 3. Agent (`agents/digest_agent.py`)
Wire everything together with PydanticAI:
- Use `openai` provider pointed at OpenRouter base URL (`https://openrouter.ai/api/v1`).
- **Default model**: `google/gemini-2.0-flash-001` (cheap, bulk summarisation).
- System prompt instructs the agent to: read the commit, optionally call web_search
  for context, then return a `BentoDigest`.
- Run the agent for each commit and collect results.

### 4. Markdown writer (`agents/writer.py`)
- Serialize each `BentoDigest` to a Markdown file:
  - Path: `web/src/content/digests/YYYY-MM-DD-<slug>.md`
  - Frontmatter = all BentoDigest fields as YAML.
  - Body = `summary` as prose.
- Log token usage (prompt + completion) to `agents/output/usage.log` after each batch.

### 5. Entry point (`agents/main.py`)
- CLI: `python -m agents.main --since-hours 24`
- Reads `OPENROUTER_API_KEY` from `.env`.
- Orchestrates: fetch → agent loop → write Markdown.

### 6. Tests (`agents/tests/`)
- `test_digest_model.py` — validate BentoDigest schema with sample data.
- `test_writer.py` — assert correct frontmatter is written.
- Use `pytest`; mock HTTP calls with `respx`.

## Budget Rule
Use `google/gemini-2.0-flash-001` for ALL summarisation calls.
Reserve `anthropic/claude-sonnet-4-5` only if a commit scores ≥ 9 and needs
a polished final summary. Never call LLMs in a per-commit loop without batching.
