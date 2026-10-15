---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- floating-point
commit_hash: 195bc16864c5f75a03e631049f22a3fd0d1d7367
source_type: github
author: Richard Biener
headline: tree-optimization/127876 - wrong code with conditional float reduction
tldr: Fixes incorrect code generation for conditional floating-point reductions involving
  vectorization.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Fixes a bug in `tree-vect-loop.cc:vectorizable_reduction` where conditional
  reductions of the form `r = <cond> ? r : CST` were vectorized incorrectly. The previous
  implementation performed a reduction on a vector mixed with the initial constant
  value and the reduction constant, followed by a MAX/MIN operation. This logic is
  flawed when the initial value equals the reduction constant or when dealing with
  floating-point special values like `-0.0` or `NaN`. The corrected code now uses
  explicit `LT/GT` comparisons to establish the condition for the reduction, ensuring
  correctness for all scalar a…'
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler where code is represented and optimized
    using an intermediate representation called GENERIC/GIMPLE, which is tree-like.
- term: vectorization
  definition: The process of transforming code to use SIMD instructions, allowing
    a single instruction to operate on multiple data elements simultaneously.
- term: reduction
  definition: An operation that combines elements of a sequence into a single value,
    such as sum, product, minimum, or maximum.
- term: conditional reduction
  definition: A reduction operation where the operation is only applied if a certain
    condition is met, or where the initial value is conditionally chosen.
- term: floating-point
  definition: A data type representing real numbers, with limitations in precision
    and special values like infinity and NaN (Not a Number).
- term: NaN
  definition: Not a Number. A special floating-point value indicating an undefined
    or unrepresentable result, often resulting from operations like 0/0.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/195bc16864c5f75a03e631049f22a3fd0d1d7367
date: '2026-10-14'
is_stub: false
stub_reason: ''
---

This commit corrects erroneous code generation for conditional floating-point reductions of the form `r = <cond> ? r : CST` when vectorization is applied. Previously, the compiler would reduce a mixed vector of initial constant values and the constant reduction value, performing a final MAX or MIN reduction. This approach failed when the initial and reduced values compared equal, and also did not correctly handle special floating-point values like -0.0 or NaNs. The fix uses explicit Less Than (LT) or Greater Than (GT) checks to ensure correctness across these cases.
