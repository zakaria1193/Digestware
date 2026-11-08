---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- middle-end
- math
- fortran
commit_hash: 2abc365bf623d42d6f50fe532117012890b30602
source_type: github
author: Roger Sayle
headline: Fix GCC pow folding for edge cases and errno handling.
tldr: GCC's power function folding is corrected for edge cases and improved to handle
  errno correctly.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's `match.pd` and `real.cc` are updated to correct `pow` folding.
  The transformation `pow(x,-1) -> 1/x` is now guarded by `!flag_errno_math` to prevent
  incorrect folding when `errno` may be set. Additionally, `real_isoddinteger` has
  been fixed to correctly identify odd integers by ensuring fractional bits are zero.
  These changes resolve PR tree-optimization/128135 and PR middle-end/128138.
primer_glossary:
- term: folding
  definition: In compilers, 'folding' refers to the optimization of replacing an expression
    with its computed constant value at compile time.
- term: pow()
  definition: The standard C math library function that computes a base to the power
    of an exponent (base^exponent).
- term: errno
  definition: A global integer variable in C that holds the error number set by system
    calls and some library functions, indicating the cause of a failure.
- term: flag_errno_math
  definition: A compiler flag or internal state indicating whether math functions
    in the compiled code are expected to set the 'errno' variable.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC
    to represent code before it is translated into machine code.
discussion_id_link: github:gcc-mirror/gcc#128135
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2abc365bf623d42d6f50fe532117012890b30602
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

This commit addresses two issues in GCC's middle-end optimization related to the `pow()` function. It corrects inaccuracies in folding `pow(-Inf, x)` and resolves an older math-errno issue. The fix ensures that `pow(x,-1)` is only transformed when `flag_errno_math` is false, preventing incorrect transformations when errno might be updated.
