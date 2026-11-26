---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- floating-point
commit_hash: f70c2bf2a6b8adc779f336f528d505228a4c6652
source_type: github
author: Richard Biener
headline: tree-optimization/129043 - loop_niter_by_eval vs. FP
tldr: Correctly handle NaNs in loop iteration count estimation to prevent incorrect
  floating-point comparisons.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `loop_niter_by_eval` function in `tree-ssa-loop-niter.cc` estimates
  loop iterations. It uses `invert_tree_comparison` to rewrite loop exit conditions.
  Previously, it didn't explicitly handle NaNs from floating-point inputs. This commit
  adds `HONOR_NANS` to `invert_tree_comparison` when called from `loop_niter_by_eval`,
  ensuring that the comparison logic correctly accounts for potential NaN inputs,
  which could otherwise lead to incorrect loop bounds or infinite loops.
primer_glossary:
- term: NaN
  definition: Not a Number. A special floating-point value used to represent undefined
    or unrepresentable results, such as the result of 0/0.
- term: loop_niter_by_eval
  definition: A GCC internal function that estimates the number of iterations a loop
    will perform, primarily used for loop optimizations.
- term: invert_tree_comparison
  definition: An internal GCC function that rewrites a comparison expression to its
    logical inverse, useful for transforming loop conditions.
- term: tree-ssa
  definition: A compiler intermediate representation that uses Static Single Assignment
    (SSA) form to simplify analysis and optimization passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f70c2bf2a6b8adc779f336f528d505228a4c6652
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

The `loop_niter_by_eval` function in GCC's tree optimization pass incorrectly assumed it would only encounter integer values. However, floating-point values, including potential NaNs (Not a Number), can arise. This commit modifies `loop_niter_by_eval` to properly indicate the possibility of NaNs when inverting tree comparisons. This ensures that floating-point comparisons are handled correctly, preventing potential misestimations of loop iterations and preserving the accuracy of optimizations.
