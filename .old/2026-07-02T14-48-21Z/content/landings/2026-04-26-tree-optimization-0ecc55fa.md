---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- ice
- loop optimization
- simd
commit_hash: 0ecc55faf01e4ebd674d8e1a41712c9762c521aa
source_type: github
author: Richard Biener
headline: 'Tree-optimization: Fixed ICE with recurrence vectorization.'
tldr: The compiler avoids an internal compiler error (ICE) during recurrence vectorization
  by properly guarding against hitting the last statement when searching for…
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR125019, which exposed an ICE in `tree-vect-loop.cc`
  related to recurrence vectorization. Specifically, the `vectorizable_recurr` function
  was missing a check that could cause it to access memory beyond the bounds of the
  loop's statements. This commit adds the missing check. The testcase is `gcc.dg/pr125019.c`.
primer_general: Vectorization is a compiler optimization technique that converts scalar
  operations (operating on single values) into vector operations (operating on multiple
  values simultaneously). This can significantly improve performance on processors
  with SIMD (Single Instruction, Multiple Data) capabilities. Recurrence vectorization
  is a specific type of vectorization that deals with loops where the current iteration
  depends on previous iterations. This commit fixes a bug where the compiler would
  crash (ICE) during recurrence vectorization due to an out-of-bounds memory access.
  The fix ensures that the compiler can correctly vectorize loops with recurrences,
  leading to improved performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ecc55faf01e4ebd674d8e1a41712c9762c521aa
date: '2026-04-26'
---

This commit fixes an internal compiler error (ICE) that could occur during recurrence vectorization. The issue was an oversight in a previous fix (PR124677) that didn't properly guard against hitting the last statement when searching for an insertion point in the loop. This commit adds the missing guard, preventing the ICE. A new testcase was added to reproduce and verify the fix.
