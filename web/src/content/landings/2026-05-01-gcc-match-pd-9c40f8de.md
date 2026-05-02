---
project: gcc
subsystem: gcc/match.pd
patch_id: null
tags:
- optimization
- bit manipulation
commit_hash: 9c40f8de18908bd0e09dafd5e21895d285044e11
source_type: github
author: Daniel Henrique Barboza
headline: 'Match.pd: Implement `(A>>C) != (B>>C) -> (A^B) >= (1<<C)` transformation.'
tldr: The compiler now optimizes `(A>>C) != (B>>C)` into `(A^B) >= (1<<C)`, potentially
  improving performance.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: '`match.pd` defines peephole optimizations on GIMPLE IR. This commit
  implements a transformation which turns a comparison of two right-shifted values
  into an XOR followed by a comparison.  The transformation includes checks to ensure
  the shift amount is valid and the types are compatible. `type_has_mode_precision_p`
  checks if the type has a specific mode precision, and `types_match` simplifies type
  comparison.'
primer_general: Compilers optimize code by transforming expressions into equivalent
  but more efficient forms. This commit adds a pattern that transforms a comparison
  of two right-shifted values. Right bit shifts can be slow, and this transformation
  replaces them with a bitwise XOR and a comparison; on some architectures, this is
  substantially faster. The compiler has been made aware of this equivalence and can
  now automatically apply it where appropriate.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9c40f8de18908bd0e09dafd5e21895d285044e11
date: '2026-05-01'
---

A new pattern is added to `match.pd` that transforms `(A>>C) != (B>>C)` into `(A^B) >= (1<<C)` and its counterpart `(A>>C) == (B>>C) -> (A^B) < (1<<C)`. This optimization can improve performance by replacing right bit shifts and comparisons with a bitwise XOR and a comparison. Checks ensure that the shift amount is not negative and does not exceed the type size.
