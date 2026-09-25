---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- vectorization
- bugfix
commit_hash: b6e2dd90a8de756ac299c38f99418d26e74a5637
source_type: github
author: Andrea Pinski
headline: Clear input arrays in vect-alias-check-ptr-info-2.c
tldr: Initializes arrays in a test case to prevent potential garbage input due to
  uninitialized memory.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect-alias-check-ptr-info-2.c` testcase in the gcc/testsuite/gcc.dg/vect
  directory was susceptible to uninitialized memory reads. This commit explicitly
  initializes the relevant arrays to zero before their use, preventing them from being
  populated with garbage data that could affect the test's outcome. This is a common
  practice for ensuring test case robustness.
primer_glossary:
- term: vectorization
  definition: An optimization technique where the compiler transforms code to perform
    the same operation on multiple data elements simultaneously, often using special
    CPU instructions (SIMD).
- term: testsuite
  definition: A collection of test programs and data used to verify the correctness
    of a compiler or other software tool. GCC has extensive testsuites for different
    language standards, optimizations, and target architectures.
- term: uninitialized arrays
  definition: Arrays whose elements have not been assigned a specific value before
    being accessed. In C and C++, this can lead to unpredictable behavior as they
    may contain 'garbage' data from previously used memory locations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b6e2dd90a8de756ac299c38f99418d26e74a5637
date: '2026-09-24'
is_stub: true
stub_reason: low_score
---

This commit fixes a test case in the vectorization suite by clearing input arrays before they are used. Previously, these arrays were uninitialized, which could lead to unpredictable behavior or incorrect test results. Initializing the arrays ensures the test runs with predictable, valid input.
