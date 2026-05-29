---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
- avx512
- x86_64
commit_hash: 25ab3b4d5c2bb6610520dfa89eb739b24a81a0b9
source_type: github
author: Tamar Christina
headline: 'testsuite: Add AVX512 requirement to a vectorization test.'
tldr: The test case vect-early-break-no-epilog_11.c now requires AVX512 instructions
  on x86_64 to vectorize correctly.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies a test case in `gcc.dg/vect/` to add an AVX512
  requirement on x86_64.  The test relies on AVX512 vector instructions for proper
  execution. Without AVX512, the vectorization may fail. This change affects the testsuite
  infrastructure and its interaction with the x86_64 target.
primer_general: Compilers often include a suite of tests to ensure they are functioning
  correctly. These tests verify that the compiler can correctly translate source code
  into machine code, including optimizations such as vectorization. Vectorization
  is a technique that allows the compiler to perform the same operation on multiple
  data elements simultaneously, improving performance. This commit adds a requirement
  for AVX512 instructions to a specific vectorization test. AVX512 is a set of instructions
  that provides enhanced vector processing capabilities. This ensures that this particular
  test is only run on processors that support AVX512, preventing potential failures
  on older processors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/25ab3b4d5c2bb6610520dfa89eb739b24a81a0b9
date: '2026-05-28'
is_stub: false
---

The test case `vect-early-break-no-epilog_11.c` now requires AVX512 instructions for vectorization on x86_64 architectures.  Without AVX512, the test may not vectorize as intended. This change ensures that the test is only run on systems that support AVX512, preventing false negatives.
