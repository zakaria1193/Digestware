---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- bitwise
- match.pd
commit_hash: 59afbbd3cd6b4348e9badc972eb3f46c2cdd023d
source_type: github
author: Daniel Barboza
headline: 'match.pd: Add patterns for (X ^ Y) & (X | Y) simplification.'
tldr: New match.pd patterns simplify bitwise XOR and AND operations, particularly
  for boolean logic.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit adds new GIMPLE-level `match.pd` patterns to simplify expressions
  involving bitwise XOR (`^`), bitwise OR (`|`), and bitwise AND (`&`). Specifically,
  it targets the simplification of `(X ^ Y) & (X | Y)` to `X ^ Y`, and `(X NE Y) &
  (X | Y)` to `X NE Y`. It also handles cases with chained ORs, such as `(X ^ Y) &
  (Z | X | Y)`. These patterns leverage the fact that if `X != Y`, then `X ^ Y` implies
  `X | Y` (unless `Z` affects it, but the structure of the pattern handles that).
  The patterns are applied at the GIMPLE level.
primer_glossary:
- term: match.pd
  definition: A file within GCC that defines pattern-matching rules for simplifying
    intermediate representations of the code.
- term: GIMPLE
  definition: GNU Intermediate Representation Form for Expressions, a higher-level,
    three-address-code intermediate representation used in GCC for optimizations.
- term: XOR
  definition: Exclusive OR, a bitwise logical operation that outputs true only when
    inputs differ.
- term: bitwise AND
  definition: A bitwise logical operation that outputs true only if both corresponding
    bits of the operands are true.
- term: bitwise OR
  definition: A bitwise logical operation that outputs true if at least one of the
    corresponding bits of the operands is true.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/59afbbd3cd6b4348e9badc972eb3f46c2cdd023d
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

Several new patterns have been added to `match.pd` to simplify bitwise operations. The patterns `(X ^ Y) & (X | Y)` and its variants for boolean logic (using NE instead of XOR) are now simplified to `X ^ Y` (or `X NE Y`). This optimization is based on the principle that if `X != Y`, then `X ^ Y` is true, and `X | Y` will also be true if either `X` or `Y` is true. The patterns also handle chained bitwise ORs.
