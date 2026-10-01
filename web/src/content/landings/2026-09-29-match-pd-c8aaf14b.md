---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- compiler
- correctness
commit_hash: c8aaf14bf6882705d2515a5eb9c15de7f4034c5b
source_type: github
author: Dominic P
headline: 'match.pd: Prevent incorrect folding of minmax(a-c, b) + c'
tldr: Fixes an optimization that incorrectly folded arithmetic involving unsigned
  subtraction that wraps around.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file contains patterns used by GCC's optimization passes
  to simplify expressions. One pattern folds `minmax (a - c, b) + c` into `minmax
  (a, b + c)` if `b + c` does not overflow. This fold is only valid if `a - c` also
  does not wrap. The commit adds a requirement to `range_op_handler(MINUS_EXPR).overflow_free_p`
  for the operands `a` and `c` before applying this fold. This correctly handles cases,
  like the `std::vector::push_back` example, where `a - c` would underflow for unsigned
  types, leading to incorrect results.
primer_glossary:
- term: match.pd
  definition: A file containing pattern matching definitions used by GCC's optimization
    passes to recognize and transform specific code structures.
- term: folding
  definition: An optimization technique where constant expressions are evaluated at
    compile time rather than runtime.
- term: minmax
  definition: An expression that returns the minimum or maximum of two values. GCC
    represents these as `MIN_EXPR` and `MAX_EXPR` in its intermediate representation.
- term: wrap around (overflow/underflow)
  definition: When an arithmetic operation produces a result that exceeds the maximum
    or minimum representable value for its data type. For unsigned types, this wraps
    around the range (e.g., `0 - 1` becomes the maximum unsigned value).
- term: unsigned type
  definition: A data type that can only represent non-negative values. Arithmetic
    operations on unsigned types wrap around on overflow or underflow.
- term: range_op_handler
  definition: A component within GCC's optimization infrastructure that analyzes the
    possible range of values for expressions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c8aaf14bf6882705d2515a5eb9c15de7f4034c5b
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

An optimization pass in GCC's pattern matching (`match.pd`) incorrectly folded expressions of the form `minmax(a - c, b) + c`. This fold was valid only if `a - c` did not wrap around (underflow) for unsigned types. The bug allowed incorrect transformations when `a` was small and `c` was large, leading to different results for the original and optimized expressions. This change adds a check using `range_op_handler` to ensure `a - c` is overflow-free before applying the fold, thus correcting the optimization.
