"""Which commits are worth a Lesson of the Week — an editorial filter.

A lesson is long-form and expensive; the pool it is drawn from is not. In one
week the corpus carries commits for two dozen GCC front ends and forty
binutils targets, and most of them teach a reader nothing they can use. The
editorial line, set by the project owner:

* **GCC: the languages people actually target** — C, C++, Ada, Rust. A deep
  dive into the COBOL lexer or a Fortran intrinsic is not the audience's
  world. (`cobol` and `fortran` are ~180 of the GCC landings on disk, so
  without this filter they win slots regularly.)
* **Architectures: the big, open ones** — Arm/AArch64, x86, POWER, RISC-V.
  A lesson on the Alpha stack-protector patterns or an Xtensa relocation
  teaches an ISA almost nobody can run.

Anything that is neither language- nor architecture-specific — the middle
end, `tree-optimization`, `libstdc++`, `bfd`, `ld`, `gas` — is always fair
game. That is where most of the genuinely instructive work happens.

The lists below are the whole policy, deliberately in one place so the line
can be moved by editing a set rather than by reading the picker.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# The policy
# ---------------------------------------------------------------------------

#: Architectures a lesson may be about. Everything else in KNOWN_ARCHES is
#: rejected. Add to this set to widen the remit (mips, s390 and loongarch are
#: the obvious candidates if the audience ever asks for them).
BIG_ARCHES = frozenset({
    "aarch64", "arm", "arm64",
    "x86", "x86-64", "x86_64", "i386", "i686", "amd64",
    "powerpc", "ppc", "ppc64", "rs6000", "power",
    "riscv", "risc-v", "riscv32", "riscv64",
})

#: Architecture names that appear in this corpus. A subsystem naming one of
#: these is architecture-specific, and is only allowed through if it is also
#: in BIG_ARCHES. Tokens NOT in this set are not treated as architectures at
#: all, so a new port simply isn't arch-gated until it is listed here.
KNOWN_ARCHES = BIG_ARCHES | frozenset({
    "alpha", "m68k", "vax", "cris", "ia64", "sh", "sh64", "hppa", "pa",
    "mips", "sparc", "s390", "s390x", "xtensa", "nios2", "microblaze",
    "rx", "rl78", "h8", "h8300", "avr", "msp430", "tic6x", "c6x", "tilegx",
    "bfin", "frv", "iq2000", "lm32", "moxie", "epiphany", "visium", "pdp11",
    "arc", "csky", "loongarch", "nds32", "or1k", "pru", "spu", "mcore",
    "mmix", "ft32", "gcn", "amdgcn", "nvptx", "xstormy16", "stormy16",
    "m32c", "m32r", "v850", "mep", "picochip", "z80", "mn10300", "avr32",
    "bpf", "kvx", "ia16",
})

#: GCC front ends outside the remit. `gccrs` (Rust) and Ada are deliberately
#: absent — those are wanted.
NICHE_LANGUAGES = frozenset({
    "cobol", "libcobol", "gcobol",
    "fortran", "gfortran", "libgfortran",
    "go", "gccgo", "libgo",
    "d", "gdc", "libphobos",
    "modula2", "m2", "gm2",
    "objc", "obj-c", "obj-c++", "objective-c", "objcp", "libobjc",
    "brig", "hsa",
})

#: Changes that are real but teach nothing: process, CI, translations, and
#: test-only churn. A lesson needs a mechanism to explain.
HOUSEKEEPING = frozenset({
    "testsuite", "maintainers", "maintainer_utils", "contrib", "ci",
    "pre-commit", "build", "doc", "docs", "news", "scripts", "release",
    "version", "po", "translations", "copyright", "gitignore",
})

_SPLIT = re.compile(r"[/,+\s]+")


def _tokens(subsystem: str | None, tags: list[str] | None) -> set[str]:
    """Normalised lowercase tokens from a landing's subsystem and tags.

    Subsystems in this corpus are inconsistent — `gcc/alpha`, `alpha`,
    `alpha/ld`, `binutils/gas,binutils/bfd` all occur — so the string is split
    on separators rather than parsed, and the tags are folded in because they
    often carry the arch or language when the subsystem doesn't.
    """
    raw: list[str] = []
    if subsystem:
        raw.extend(_SPLIT.split(subsystem.lower()))
    for tag in tags or []:
        if isinstance(tag, str):
            raw.extend(_SPLIT.split(tag.lower()))
    return {t.strip(". ") for t in raw if t.strip(". ")}


def rejection_reason(
    subsystem: str | None, tags: list[str] | None = None
) -> str | None:
    """Why this subject is unfit for a lesson, or None if it is fine.

    Returning the reason rather than a bool keeps the picker's log useful —
    "skipped 12 candidates" is not debuggable, "skipped cobol (niche
    language)" is.
    """
    tokens = _tokens(subsystem, tags)
    if not tokens:
        return None

    niche_lang = tokens & NICHE_LANGUAGES
    if niche_lang:
        return f"niche language: {', '.join(sorted(niche_lang))}"

    chores = tokens & HOUSEKEEPING
    if chores:
        return f"housekeeping: {', '.join(sorted(chores))}"

    arches = tokens & KNOWN_ARCHES
    if arches and not (arches & BIG_ARCHES):
        return f"niche architecture: {', '.join(sorted(arches))}"

    return None


def is_lesson_worthy(subsystem: str | None, tags: list[str] | None = None) -> bool:
    """True when a commit in this subsystem may become a lesson."""
    return rejection_reason(subsystem, tags) is None
