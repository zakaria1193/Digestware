---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- vectorization
- optimization
commit_hash: aca3a6235baad23e7156ee8c80c0b7433a2ddfab
source_type: github
author: Alexandre Oliva
headline: 'Testsuite: Update fast-math-complex-mls tests for arm.'
tldr: Updates tests for ARM to avoid expecting COMPLEX_ADD_ROT270 after changes to
  complex number vectorization.
why_it_matters: Ensures that the testsuite remains accurate and reflects the current
  state of the compiler's optimizations, specifically for ARM architecture.
impact_score: 4
impact_rationale: The commit updates tests due to changes in optimization, indicating
  a moderate impact on testsuite accuracy.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses failures in `fast-math-complex-mls-{float,double}.c`
  due to changes in ARM complex number vectorization.  Specifically, the tests no
  longer expect `COMPLEX_ADD_ROT270` due to reassocation and dce after complex lowering
  in the tree-optimization pass.
primer_general: This commit concerns the GCC testsuite, which validates the compiler's
  behavior on different architectures. The tests involve complex number arithmetic
  optimized using vector instructions on ARM processors. Recent changes in how GCC
  handles complex number vectorization require updating the tests to reflect the expected
  output, avoiding false positives.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aca3a6235baad23e7156ee8c80c0b7433a2ddfab
date: '2026-04-21'
---

This commit updates the `fast-math-complex-mls-{float,double}.c` tests for ARM. Changes to `arm_v8_3a_complex_neon` options and `vect_complex_add_{float,double}` enabled the tests, causing failures. The update adjusts the tests to no longer expect `COMPLEX_ADD_ROT270` after complex lowering and dead code elimination.
