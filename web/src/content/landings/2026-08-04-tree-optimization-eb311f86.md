---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- loop-optimization
- performance
- code-size
commit_hash: eb311f861255ae1fcaafa3454d4d1d6f1da07497
source_type: github
author: liuhongt
headline: 'tree-optimization: Fold sign-changing conversions in IVOPTS'
tldr: Improved loop invariant code motion by folding sign-changing conversions and
  handling modular arithmetic.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The IVOPTS pass now enables the `ranger` analysis and passes its range
  context information to `tree-affine`. This allows `aff_combination_convert` and
  `expr_to_aff_combination` to fold value-preserving sign changes and modular arithmetic
  into exact arithmetic, which aids affine decomposition. Specifically, it addresses
  cases where conversions created chains hiding outer-loop IV terms. The `get_computation_aff_1`
  function now passes the use statement to `tree-affine`, and `tree_ssa_iv_optimize`
  enables ranger, improving the analysis of loop invariants and reducing code size
  regressions.
primer_glossary:
- term: IVOPTS
  definition: Invariant Code Motion optimization pass in GCC, responsible for moving
    loop-invariant computations out of loops to improve performance.
- term: ranger
  definition: A GCC analysis pass that computes ranges of values for variables, providing
    context for other optimizations.
- term: affine decomposition
  definition: A process in compiler optimization that represents expressions or transformations
    as affine functions (linear functions with a constant offset), useful for analyzing
    loops and memory accesses.
- term: modular arithmetic
  definition: Arithmetic where numbers 'wrap around' after reaching a certain value,
    like calculations with unsigned integers.
- term: loop-invariant
  definition: A computation within a loop whose result does not change with each iteration
    of the loop.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eb311f861255ae1fcaafa3454d4d1d6f1da07497
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This commit enhances the Loop Invariant code Motion (IVOPTS) pass by enabling the 'ranger' analysis to fold sign-changing conversions and modular arithmetic into exact arithmetic. This resolves a code-size regression caused by canonicalizing signed arithmetic to unsigned, which previously hid loop invariant terms. The improvements allow for better affine decomposition and can reduce loop-bound spills, leading to performance gains on various architectures.
