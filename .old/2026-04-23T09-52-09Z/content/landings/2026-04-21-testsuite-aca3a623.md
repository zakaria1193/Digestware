---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- vectorization
- complex arithmetic
- optimization
commit_hash: aca3a6235baad23e7156ee8c80c0b7433a2ddfab
source_type: github
author: Alexandre Oliva
headline: 'Testsuite: Updates ARM fast-math-complex tests to remove COMPLEX_ADD_ROT270
  expectation'
tldr: Updates ARM's fast-math-complex tests to no longer expect `COMPLEX_ADD_ROT270`
  due to changes in vectorization and dead code elimination.
why_it_matters: Ensures that the ARM vectorization tests remain accurate and reliable
  after changes to compiler options and optimization passes.
impact_score: 4
impact_rationale: Updates tests to reflect changes in compiler behavior due to vectorization
  and optimization.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The ARM backend''s vectorization of complex arithmetic relies on recognizing
  specific patterns like `COMPLEX_ADD_ROT270`. Changes in `arm_v8_3a_complex_neon`
  options and `vect_complex_add_{float,double}` functions, combined with reassocation
  during optimization, made this pattern unrecognizable, leading to test failures.
  Search terms: "GCC IPA-SRA inter-procedural scalar replacement"'
primer_general: 'GCC uses vectorization to improve performance by performing operations
  on multiple data elements simultaneously. The ARM architecture has specific vector
  instructions that can be used for complex number arithmetic. This commit updates
  the test suite to align with changes in how the compiler optimizes complex number
  operations on ARM processors. Specifically, due to changes in optimization and vectorization,
  the tests no longer expect a specific pattern (`COMPLEX_ADD_ROT270`). Search terms:
  "GCC IPA-SRA inter-procedural scalar replacement"'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aca3a6235baad23e7156ee8c80c0b7433a2ddfab
date: '2026-04-21'
---

The ARM fast-math-complex tests (`fast-math-complex-mls-{float,double}.c`) were failing due to changes in the `arm_v8_3a_complex_neon` options and the `vect_complex_add_{float,double}` functions. These changes, combined with reassociation, caused the `ADD_ROT270` pattern to become unrecognizable after complex lowering. Dead code elimination (DCE) further removed the original complex assignments, exacerbating the issue. This commit updates the tests to reflect these changes and remove the expectation of `COMPLEX_ADD_ROT270`.
