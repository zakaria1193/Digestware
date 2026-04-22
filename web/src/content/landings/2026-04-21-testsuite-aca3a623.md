---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- vectorization
- complex numbers
commit_hash: aca3a6235baad23e7156ee8c80c0b7433a2ddfab
source_type: github
author: Alexandre Oliva
headline: 'Testsuite: ARM: Update fast-math-complex-mls tests.'
tldr: The fast-math-complex-mls tests for ARM have been updated to reflect changes
  in complex number vectorization.
why_it_matters: Testsuite updates ensure the compiler generates correct code as optimization
  strategies evolve.
impact_score: 4
impact_rationale: Updates test cases to reflect changes in complex number vectorization
  on ARM.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The changes in `arm_v8_3a_complex_neon` options and `vect_complex_add_{float,double}`
  resulted in the compiler no longer recognizing `ADD_ROT270` in `fms_elemconjsnd`
  after complex lowering and dead code elimination. The tests are updated to reflect
  this change in the generated code.
primer_general: When GCC compiles code that uses complex numbers, it can use vectorization
  to perform multiple calculations simultaneously, improving performance. This commit
  updates tests for ARM processors related to this complex number vectorization. The
  tests verify that the compiler correctly optimizes complex number calculations,
  and these changes are necessary as the optimization strategies in GCC evolve.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aca3a6235baad23e7156ee8c80c0b7433a2ddfab
date: '2026-04-21'
---

This commit updates the `fast-math-complex-mls-float.c` and `fast-math-complex-mls-double.c` test cases for ARM. Changes to ARM's complex number vectorization and related options caused these tests to fail. The updates adjust the expected behavior in the tests to account for these changes, specifically related to the recognition of `COMPLEX_ADD_ROT270` after complex lowering and dead code elimination.
