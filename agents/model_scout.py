"""Weekly check: is there a newer, cheaper model for any stage?

``agents.check_models`` answers "does every configured slug still exist?".
This answers the next question: "should any of them change?". It is read by
the pjm maintainer on its weekly run, which makes the actual switch.

    python -m agents.model_scout            # markdown report
    python -m agents.model_scout --json     # the same, for a script

**The switch rule** (a candidate is proposed only when all of these hold):

- same vendor and same model family as today's pick (`claude-sonnet`,
  `gemini-flash-lite` …), so quality does not drop: a newer version of the
  same line is at least as good;
- a strictly higher version number (`5.5` beats `5`), so it is newer;
- cheaper *for this stage's own mix* of input and output tokens, measured
  from ``agents/output/usage.log``. The lesson research stage is ~98% input
  and the summariser is ~45% output, so one blended price would pick wrong;
- not a ``:free`` / ``:thinking`` variant, a preview, or a dated snapshot;
- for stages that call tools, it advertises ``tools`` and
  ``structured_outputs``.

Cheaper models from any other family or vendor (DeepSeek, Qwen, Kimi, GLM,
MiniMax, Mistral, Llama … all included) are listed as alternatives when they
were released no earlier than today's pick. They are never marked SWITCH:
"equal quality" across families is a judgement this script cannot make, so
the maintainer makes it from published benchmarks (see agents/CLAUDE.md).

Read-only: no LLM call, no key needed (``/models`` is a public listing), and
it never edits anything. Exits 0 even when the listing is unreachable, so a
network blip cannot fail a maintainer run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

from agents._openrouter import (
    DEFAULT_LESSON_RESEARCH_MODEL,
    DEFAULT_LESSON_WRITER_MODEL,
    DEFAULT_PREMIUM_MODEL,
    DEFAULT_SUMMARISER_MODEL,
    fetch_models,
    model_from_env,
)

USAGE_LOG = Path(__file__).parent / "output" / "usage.log"

#: How many cheaper models from other families to list per stage.
MAX_ALTERNATIVES = 8

#: Used when a stage has no rows in usage.log yet: assume input-heavy.
DEFAULT_INPUT_SHARE = 0.75


@dataclass(frozen=True)
class Stage:
    env_var: str
    default: str
    #: ``agent`` values in usage.log that this stage writes.
    agents: tuple[str, ...]
    #: True when the stage relies on tool calls / structured output.
    needs_tools: bool


STAGES: list[Stage] = [
    Stage("SUMMARISER_MODEL", DEFAULT_SUMMARISER_MODEL,
          ("landing_agent", "discussion_agent", "tag_categorizer"), needs_tools=False),
    Stage("BENTO_MODEL", DEFAULT_PREMIUM_MODEL, ("landing_agent_premium",), needs_tools=False),
    Stage("LESSON_RESEARCH_MODEL", DEFAULT_LESSON_RESEARCH_MODEL, ("lesson_research",), needs_tools=True),
    Stage("LESSON_WRITER_MODEL", DEFAULT_LESSON_WRITER_MODEL, ("lesson_writer",), needs_tools=True),
]

_SKIP_WORDS = ("preview", "exp", "beta", "latest")


def split_slug(slug: str) -> tuple[str, str, tuple[int, ...]]:
    """``anthropic/claude-sonnet-5.5`` -> ``("anthropic", "claude-sonnet", (5, 5))``.

    The family is the name with its version numbers taken out, so
    ``gemini-2.5-flash`` and ``gemini-2.5-flash-lite`` are different families
    (``gemini-flash`` vs ``gemini-flash-lite``), and ``claude-3.5-haiku`` and
    ``claude-haiku-5.5`` are the same one.
    """
    vendor, _, name = slug.partition("/")
    name = name.split(":", 1)[0]
    version = tuple(int(n) for n in re.findall(r"\d+", name))
    words = [w for w in re.split(r"[-.]", name) if w and not w.isdigit()]
    return vendor, "-".join(words), version


def _is_plain(slug: str) -> bool:
    """A stable, paid, undated model id — the only kind we switch to."""
    if ":" in slug:
        return False
    name = slug.split("/", 1)[-1]
    if any(word in name.split("-") for word in _SKIP_WORDS):
        return False
    # Dated snapshots (`-20250514`, `-0827`) pin an old build of a family.
    return not re.search(r"-\d{4,}$", name)


def input_share(stage: Stage, log_path: Path = USAGE_LOG) -> tuple[float, int]:
    """Share of this stage's tokens that are input, and how many calls it is from.

    Every row of the stage counts, whatever model wrote it: the mix is a
    property of the work, not of the model.
    """
    req = resp = calls = 0
    try:
        lines = log_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    for line in lines:
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if not isinstance(row, dict) or row.get("agent") not in stage.agents:
            continue
        req += row.get("request_tokens") or 0
        resp += row.get("response_tokens") or 0
        calls += 1
    if req + resp == 0:
        return DEFAULT_INPUT_SHARE, 0
    return req / (req + resp), calls


def _price(entry: dict) -> tuple[float, float] | None:
    pricing = entry.get("pricing")
    if not isinstance(pricing, dict):
        return None
    try:
        return float(pricing.get("prompt") or 0), float(pricing.get("completion") or 0)
    except (TypeError, ValueError):
        return None


def blended(price: tuple[float, float], share: float) -> float:
    """USD per million tokens at this stage's input/output mix."""
    return (price[0] * share + price[1] * (1 - share)) * 1_000_000


def _created(entry: dict) -> int:
    """Release time (epoch seconds) from the listing; 0 when unknown."""
    value = entry.get("created")
    return value if isinstance(value, int) else 0


def _supports_tools(entry: dict) -> bool:
    params = entry.get("supported_parameters") or []
    return "tools" in params and ("structured_outputs" in params or "response_format" in params)


@dataclass
class Option:
    slug: str
    usd_per_m: float
    prompt_per_m: float
    completion_per_m: float
    saving_pct: float


@dataclass
class StageReport:
    env_var: str
    current: str
    overridden: bool
    input_share: float
    sample_calls: int
    current_usd_per_m: float | None = None
    status: str = "keep"          # keep | switch | missing
    proposal: Option | None = None
    newer_but_dearer: list[Option] = field(default_factory=list)
    cheaper_alternatives: list[Option] = field(default_factory=list)


def scout(stage: Stage, catalogue: dict[str, dict], log_path: Path = USAGE_LOG) -> StageReport:
    current = model_from_env(stage.env_var, stage.default)
    share, calls = input_share(stage, log_path)
    report = StageReport(stage.env_var, current, current != stage.default, round(share, 3), calls)

    entry = catalogue.get(current)
    price = _price(entry) if entry else None
    if price is None:
        report.status = "missing"
        return report
    now = blended(price, share)
    report.current_usd_per_m = round(now, 4)

    vendor, family, version = split_slug(current)
    released = _created(entry or {})

    def option(slug: str, p: tuple[float, float]) -> Option:
        cost = blended(p, share)
        return Option(slug, round(cost, 4), p[0] * 1e6, p[1] * 1e6,
                      round(100 * (now - cost) / now, 1) if now else 0.0)

    cheaper_same: list[Option] = []
    for slug, cand in catalogue.items():
        if slug == current or not _is_plain(slug):
            continue
        p = _price(cand)
        if p is None or (p[0] == 0 and p[1] == 0):
            continue
        if stage.needs_tools and not _supports_tools(cand):
            continue
        c_vendor, c_family, c_version = split_slug(slug)
        opt = option(slug, p)
        if c_vendor == vendor and c_family == family:
            if c_version <= version:
                continue
            (cheaper_same if opt.usd_per_m < now else report.newer_but_dearer).append(opt)
        elif opt.usd_per_m < now and _created(cand) >= released:
            report.cheaper_alternatives.append(opt)

    if cheaper_same:
        # Newest first, then cheapest: when two newer versions both save
        # money, take the newest rather than the last-but-one.
        cheaper_same.sort(key=lambda o: (split_slug(o.slug)[2], -o.usd_per_m), reverse=True)
        report.proposal = cheaper_same[0]
        report.status = "switch"
    report.newer_but_dearer.sort(key=lambda o: o.usd_per_m)
    report.cheaper_alternatives.sort(key=lambda o: o.usd_per_m)
    del report.cheaper_alternatives[MAX_ALTERNATIVES:]
    return report


def scout_all(entries: list[dict], log_path: Path = USAGE_LOG) -> list[StageReport]:
    catalogue = {e["id"]: e for e in entries if isinstance(e.get("id"), str)}
    return [scout(stage, catalogue, log_path) for stage in STAGES]


def _fmt(o: Option) -> str:
    return (f"`{o.slug}` ${o.prompt_per_m:.2f}/${o.completion_per_m:.2f} per M, "
            f"{o.usd_per_m:.3f} blended ({o.saving_pct:+.0f}% saving)")


def render(reports: list[StageReport]) -> str:
    out = ["# Model scout", ""]
    for r in reports:
        head = f"## {r.env_var}: `{r.current}`"
        if r.overridden:
            head += " (set by env / repo variable, not the code default)"
        out.append(head)
        mix = f"{r.input_share:.0%} input over {r.sample_calls} logged calls" if r.sample_calls \
            else f"no logged calls, assuming {r.input_share:.0%} input"
        out.append(f"- Mix: {mix}.")
        if r.status == "missing":
            out.append("- **MISSING** from the OpenRouter listing. Run `python -m agents.check_models`.")
        else:
            out.append(f"- Today: {r.current_usd_per_m:.3f} USD per M tokens at that mix.")
            if r.proposal:
                out.append(f"- **SWITCH** to {_fmt(r.proposal)}.")
            else:
                out.append("- Keep: no newer model of the same family is cheaper.")
            for o in r.newer_but_dearer:
                out.append(f"- Newer but dearer, not proposed: {_fmt(o)}.")
            for o in r.cheaper_alternatives:
                out.append(f"- Cheaper alternative, other family (judge quality first): {_fmt(o)}.")
        out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Is there a newer, cheaper model for any stage?")
    parser.add_argument("--json", action="store_true", help="print JSON instead of markdown")
    args = parser.parse_args(argv)
    try:
        entries = fetch_models()
    except Exception as exc:                     # noqa: BLE001
        print(f"model_scout: could not reach the OpenRouter listing ({exc}); nothing checked.")
        return 0
    reports = scout_all(entries)
    if args.json:
        print(json.dumps([asdict(r) for r in reports], indent=2))
    else:
        print(render(reports))
    return 0


if __name__ == "__main__":
    sys.exit(main())
