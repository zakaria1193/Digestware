---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loops
- bugfix
- integer-overflow
commit_hash: 435ff0c5dff136eef427872991398ee09739fa3b
source_type: github
author: Richard Biener
headline: 'Tree optimization: Avoid negating the most negative signed value during
  loop analysis'
tldr: GCC's tree-ssa-loop-niter pass now avoids incorrect negation of the most negative
  signed integer, preventing potential compiler misbehavior with loop iteration…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-loop-niter` pass in GCC is responsible for analyzing
  loops to determine their iteration counts, which is crucial for various loop optimizations.
  This commit addresses a specific edge case in `number_of_iterations_until_wrap`
  related to `PR tree-optimization/125602`. The problem arises when attempting to
  negate the `MIN_INT` value (the most negative signed integer) during iteration count
  analysis, which results in an overflow and incorrect `INTEGER_CST` representation.
  The fix ensures that the negation and conversion to `niter_type` are reordered and
  handled with an assumption ch…
primer_general: 'When a compiler like GCC optimizes your code, it tries to figure
  out how many times a loop will run. This is called ''loop iteration analysis'' and
  helps with many performance improvements. There''s a special problem with signed
  whole numbers (integers): if you try to flip the sign of the most negative possible
  number (like `-2,147,483,648` for a 32-bit integer), it doesn''t have a positive
  equivalent, and the operation can overflow or wrap around, producing an incorrect
  result. This commit fixes a bug in GCC''s loop analysis where it was trying to do
  exactly this. By changing how the compiler calculates loop bounds when dealing with
  negative step values, it avoids this mathematical trap, ensuring your loops are
  correctly analyzed and optimized, preventing crashes or unexpected behavior in your
  programs.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/435ff0c5dff136eef427872991398ee09739fa3b
date: '2026-06-05'
is_stub: false
---

GCC's `number_of_iterations_until_wrap` function, part of the tree-ssa-loop-niter optimization pass, has been improved to prevent the problematic negation of the most negative signed integer value. This issue, identified by PR125602, could lead to incorrect `INTEGER_CST` results during loop analysis. The fix restructures the negation and type conversion logic to avoid this overflow, ensuring accurate calculation of loop bounds and preventing potential miscompilations.
