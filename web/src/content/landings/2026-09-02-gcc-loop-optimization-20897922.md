---
project: gcc
subsystem: gcc/loop-optimization
patch_id: null
tags:
- loop-optimization
- optimization
- pointer-arithmetic
commit_hash: 20897922c9b4b63333615ec01d92fcc5a5a771ea
source_type: github
author: Richard Biener
headline: Loop invariant code motion honors -fwrapv-pointer
tldr: Loop invariant analysis now correctly considers pointer wrapping behavior when
  `-fwrapv-pointer` is enabled.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `nowrap_type_p` predicate, crucial for several loop optimizations
  like IVOPTs and loop iteration counting, failed to account for the `-fwrapv-pointer`
  flag. It incorrectly treated all `POINTER_TYPE_P` as non-wrapping. This change modifies
  the predicate to respect the flag, ensuring accurate analysis when pointer arithmetic
  might wrap around.
primer_glossary:
- term: -fwrapv-pointer
  definition: A GCC flag that instructs the compiler to assume that signed integer
    arithmetic, including pointer arithmetic, wraps around on overflow, matching the
    behavior of two's complement arithmetic.
- term: IVOPTs
  definition: Loop Invariant Code Motion optimizations. These passes identify expressions
    within loops whose values do not change with each iteration and move them outside
    the loop to reduce redundant computations.
- term: niter analysis
  definition: Analysis performed by the compiler to determine the number of iterations
    a loop is expected to execute. This information is used to guide other optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/20897922c9b4b63333615ec01d92fcc5a5a771ea
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

The `nowrap_type_p` function, used by loop invariant optimization (IVOPTs) and loop iteration analysis, incorrectly assumed pointer types never wrap. This commit updates `tree-ssa-loop-niter.cc` to properly honor the `-fwrapv-pointer` flag, ensuring that pointer arithmetic is analyzed with the correct wrapping semantics. Two test cases are added to verify this correction.
