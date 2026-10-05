---
project: gcc
subsystem: testsuite/powerpc
patch_id: null
tags:
- testsuite
- powerpc
- VSX
- endianness
commit_hash: a02fa6198b22cdb2656903480fea325fc7f85463
source_type: github
author: Avinash Jayakar
headline: Fix vsx-{load,store}-element tests for powerpc64 BE
tldr: Corrects powerpc64 big-endian VSX load/store element tests by adjusting input
  types to match expected behavior.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: VSX element load/store operations on powerpc64 BE were failing due
  to type boundary crossings yielding different results than LE. This patch adjusts
  test inputs to normalize behavior, ensuring the tests pass by aligning expectations
  with the architecture's behavior across endianness.
primer_glossary:
- term: VSX
  definition: Vector-Scalar Extension, an optional feature for PowerPC processors
    that extends the AltiVec SIMD instruction set with scalar floating-point and integer
    operations.
- term: BE
  definition: Big-Endian, a byte order where the most significant byte is stored at
    the lowest memory address.
- term: LE
  definition: Little-Endian, a byte order where the least significant byte is stored
    at the lowest memory address.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a02fa6198b22cdb2656903480fea325fc7f85463
date: '2026-09-04'
is_stub: true
stub_reason: low_score
---

This commit addresses failures in powerpc64 big-endian VSX load/store element tests, specifically concerning operations that cross type boundaries. The input values and types for tests like `vsx-load-element-extend-int.c` were modified to ensure consistent expected results across little-endian and big-endian systems. Helper functions for verbose output were also corrected.
