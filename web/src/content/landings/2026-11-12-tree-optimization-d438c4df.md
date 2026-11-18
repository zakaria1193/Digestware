---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- correctness
- loops
commit_hash: d438c4df9c804a865bc3353146d96b44417177a7
source_type: github
author: Kyrylo Tkachov
headline: GCC fixes chrec multiplication across nested loops
tldr: GCC's `chrec_fold_multiply_poly_poly` now correctly scales loop-invariant chrecs
  when multiplying polynomials in nested loops, fixing an access function bug.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects `tree-chrec.cc`'s `chrec_fold_multiply_poly_poly`
  function. When multiplying two polynomial chrecs, `{a, +, b}_1` and `{c, +, d}_2`,
  where loop 1 is outer to loop 2, the outer chrec `{a, +, b}_1` is invariant within
  loop 2. The multiplication should result in `{c*{a, +, b}_1, +, d*{a, +, b}_1}_2`.
  The bug was that the step `d` of the inner chrec was not scaled by the invariant
  outer chrec. This led to an incorrect step in the resulting chrec, causing issues
  like loop interchange breaking memory access analysis for constructs like `a[i*k+j]`
  when loops were over `i` and `k…
primer_glossary:
- term: chrec
  definition: Characterization of recurrence relations, used by GCC to represent arithmetic
    progressions in loop analysis, often for memory access patterns.
- term: poly-poly multiplication
  definition: Multiplying two polynomial expressions together.
- term: nested loops
  definition: A loop structure where one loop is contained entirely within another
    loop.
- term: loop invariant
  definition: An expression or value within a loop that does not change its value
    from one iteration to the next.
- term: loop interchange
  definition: An optimization that swaps the order of nested loops, which can improve
    data locality or expose other optimization opportunities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d438c4df9c804a865bc3353146d96b44417177a7
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

A bug in GCC's handling of 'chrecs' (characterizations of recurrence relations) during polynomial multiplication in nested loops has been fixed. The `chrec_fold_multiply_poly_poly` function previously failed to scale the step of an inner loop's chrec by an outer loop's invariant chrec. This led to incorrect access functions for memory accesses, which could be wrongly optimized or reordered by loop interchange. The fix ensures that the step is correctly scaled in both nested-loop scenarios, resolving the bug and improving the accuracy of loop analysis.
