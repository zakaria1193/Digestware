---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- integer
- match.pd
commit_hash: 7bceace5d3b68d0cf0f3917f71e2cf66e5a3267b
source_type: github
author: Daniel Barboza
headline: 'match.pd: Simplify signed (A << N) >> N to A.'
tldr: New pattern simplifies signed left-shift followed by right-shift to the original
  value, enabling earlier optimization.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change introduces a new GIMPLE-level pattern in `match.pd` to
  simplify `(A << N) >> N` for signed types. Previously, this simplification was only
  present at the RTL level. The pattern is restricted to signed types because the
  sign extension behavior of arithmetic right shifts ensures the identity holds, whereas
  for unsigned types, other patterns already exist. This moves the optimization earlier
  in the compilation flow, potentially enabling further GIMPLE-level optimizations.
primer_glossary:
- term: match.pd
  definition: A file within GCC that defines pattern-matching rules for simplifying
    intermediate representations of the code.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used in GCC
    that describes operations at the instruction level, closer to machine code.
- term: GIMPLE
  definition: GNU Intermediate Representation Form for Expressions, a higher-level,
    three-address-code intermediate representation used in GCC for optimizations.
- term: sign extension
  definition: When a signed number is converted to a wider integer type, the most
    significant bit (the sign bit) is copied to all the newly-added high-order bits
    to preserve the number's sign and value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7bceace5d3b68d0cf0f3917f71e2cf66e5a3267b
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

A new pattern in `match.pd` now simplifies signed expressions of the form `(A << N) >> N` to `A` earlier in the optimization pipeline (GIMPLE instead of just RTL). This transformation is valid because right-shifting a signed integer preserves its sign bit. Previously, this optimization was only performed at the RTL level, limiting its opportunity.
