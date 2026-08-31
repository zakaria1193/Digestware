---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop analysis
commit_hash: ba472b886b31046afba1df687b65bd862b087240
source_type: github
author: Lunex
headline: Fix missing may_be_zero check in final value replacement
tldr: Corrected a scalar evolution analysis to prevent incorrect XOR parity mask computation.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects an issue in `final_value_replacement_loop` within
  `tree-scalar-evolution.cc`. The `analyze_and_compute_bitop_with_inv_effect` function
  was called without guarding on `niter_desc.may_be_zero`. This could lead to incorrect
  calculations if the loop condition allowed for early exit. The change adds a check
  for `integer_zerop(niter_desc.may_be_zero)` to ensure the XOR parity mask is computed
  only when the number of iterations is valid.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where the code is represented and manipulated using an
    intermediate 'tree' structure, allowing for various optimizations.
- term: scalar evolution
  definition: A compiler analysis technique that determines properties of expressions
    involving induction variables in loops, such as their rate of change.
- term: XOR parity mask
  definition: A bitmask used in certain computations, where the parity (evenness or
    oddness) of set bits is determined using the XOR operation. This is often relevant
    in loop analysis or bit manipulation optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ba472b886b31046afba1df687b65bd862b087240
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

The final value replacement pass in the tree optimizer previously failed to check `niter_desc.may_be_zero`. This omission could lead to incorrect computation of the XOR parity mask when a loop might exit on its first iteration. The fix ensures this check is performed, preventing the use of invalid iteration counts.
