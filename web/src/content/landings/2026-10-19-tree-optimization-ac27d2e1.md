---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- STRING_CST
commit_hash: ac27d2e11708eb999fab1b26c053df4f3bd8fd0c
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix loop iteration count with STRING_CST'
tldr: Corrects loop iteration analysis by simulating string constant comparisons in
  uint8_t.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `loop_niter_by_eval` function estimates loop iteration counts.
  This change addresses a bug where simulating iteration over a `STRING_CST` (e.g.,
  in a loop that terminates based on string length or content) caused a sign-extension
  issue. The fix modifies the function to perform the comparison of the `STRING_CST`
  element against the loop's terminating constant in `uint8_t` type, resolving the
  sign issue and ensuring correct iteration count estimation for such loops.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC's compilation pipeline that optimizes the intermediate
    representation (tree) of the code.
- term: loop_niter_by_eval
  definition: A function within GCC's loop optimization passes that attempts to evaluate
    and determine the number of iterations a loop will execute.
- term: STRING_CST
  definition: GCC's internal representation for a string constant.
- term: sign-extension
  definition: The process of preserving the sign of a number when converting it to
    a larger data type by padding with copies of the most significant bit.
- term: uint8_t
  definition: An unsigned integer type that occupies exactly 8 bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ac27d2e11708eb999fab1b26c053df4f3bd8fd0c
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit fixes a sign-extension issue in GCC's loop iteration analysis, specifically within the `loop_niter_by_eval` function. The problem occurred when simulating iterations over a `STRING_CST`. The fix ensures that the comparison of the `STRING_CST` element with the terminating constant is performed using `uint8_t` type, preventing incorrect sign extensions and ensuring accurate loop iteration counts, resolving PR127966.
