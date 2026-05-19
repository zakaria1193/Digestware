---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
- bugfix
commit_hash: 1af06a4bfbc04309f944ce50d2ce7a88f5dc150f
source_type: github
author: Andrew Pinski
headline: 'Testsuite: Fix pr112095.c for vector lowering'
tldr: Modifies test case pr112095.c to correctly test vector lowering.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testcase `pr112095.c` checks the behavior of vector lowering, a
  transformation that occurs during the SSA (Static Single Assignment) optimization
  passes. The patch modifies the test to examine the intermediate representation in
  `release_ssa`, which occurs before vector lowering. The expected output is adjusted
  to account for vector returns via memory, and `-Wno-psabi` suppresses warnings about
  the vector argument.
primer_general: Compilers use a series of optimization passes to improve the generated
  code.  Vector lowering is a specific optimization that transforms vector operations
  into simpler scalar operations that the target hardware can efficiently execute.
  This commit modifies a test case to ensure that the vector lowering optimization
  is working correctly by checking the code at an earlier stage of the compilation
  process and accounting for how vector types are handled.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1af06a4bfbc04309f944ce50d2ce7a88f5dc150f
date: '2026-05-18'
is_stub: false
---

The test case `pr112095.c` was updated to accurately test vector lowering in the compiler. The test now examines the state of the code earlier in the compilation process (release_ssa), before vector lowering occurs. Additionally, the test has been updated to correctly match the return values of vector types and avoid warnings related to the psabi.
