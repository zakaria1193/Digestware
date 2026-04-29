---
project: gcc
subsystem: gcc/range-op-float
patch_id: null
tags:
- bugfix
- optimization
- floating-point
commit_hash: 62d5880b9599c3bdbc22b80d522b0bea14f4beaf
source_type: github
author: Jakub Jelinek
headline: 'Range-op-float: Avoid ICE on undefined ranges'
tldr: Fixes an internal compiler error (ICE) that occurs when processing undefined
  ranges in floating-point operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `lower_bound` and `upper_bound` methods on `frange` assert that
  they are not called on `undefined_p` ranges. `operator_not_equal::fold_range` used
  to call `frelop_early_resolve` which indirectly called `empty_range_varying`, but
  this was changed in r14-4153. This commit readds the call to `empty_range_varying`
  to avoid the ICE. Search terms: GCC range-op-float floating point range.'
primer_general: 'GCC uses range analysis to determine the possible values of variables,
  which enables optimizations like dead code elimination and bounds checking. This
  commit fixes a bug in the range analysis for floating-point numbers, where the compiler
  would crash when encountering an undefined range. An undefined range arises when
  the compiler cannot determine the possible values of a variable. The fix ensures
  that the compiler correctly handles these undefined ranges, preventing internal
  errors. Search terms: GCC range-op-float floating point range.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/62d5880b9599c3bdbc22b80bea14f4beaf
date: '2026-04-28'
---

The compiler was crashing due to an incorrect assumption about the availability of lower/upper bounds for undefined ranges. The `operator_not_equal::fold_range` function now calls `empty_range_varying` to handle these cases, preventing the ICE. This issue was introduced in r14-4153 and this commit reverts to the prior behavior.
