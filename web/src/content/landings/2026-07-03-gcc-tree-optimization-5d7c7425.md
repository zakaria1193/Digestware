---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- compiler
- optimization
commit_hash: 5d7c74258d3a4b95cd5022acd5fa51381d922a40
source_type: github
author: Philipp Tomsich
headline: Use target-independent types for carry overflow checks
tldr: Ensures target-independent carry overflow checks by using predefined width types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR tree-optimization/124545 highlighted an issue where uns_carry()
  used fixed-size integer types (unsigned int, unsigned long) that caused failures
  on ILP32 targets. This commit replaces these with target-independent width types
  (__UINT32_TYPE__, __UINT64_TYPE__) to ensure consistent behavior. The test case
  `pr124545-2.c` is updated to reflect this.
primer_glossary:
- term: tree-optimization
  definition: A major optimization phase in GCC that operates on the compiler's intermediate
    representation (GIMPLE or GENERIC trees) to perform high-level code transformations.
- term: ILP32
  definition: A data model for 32-bit systems where integers (int), long integers
    (long), and pointers (pointers) are all 32 bits wide. This contrasts with LP64
    (64-bit) where `long` and pointers are 64 bits.
- term: __UINT32_TYPE__
  definition: A predefined macro in C/C++ that expands to the correct unsigned integer
    type for 32 bits on the target architecture. Similarly, __UINT64_TYPE__ for 64
    bits.
- term: carry overflow
  definition: An arithmetic condition where the result of an addition or multiplication
    is too large to fit into the destination type, and the excess value 'carries over'
    to a higher-order bit.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5d7c74258d3a4b95cd5022acd5fa51381d922a40
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

The `uns_carry()` helper function in GCC's tree-optimization passes previously used fixed-width types (`unsigned int` and `unsigned long`) for its narrow and wide type comparisons. This commit modifies the helper to use `__UINT32_TYPE__` and `__UINT64_TYPE__` instead. This change makes the comparison target-independent, resolving issues on ILP32 (32-bit) targets where `unsigned long` might not be wider than `unsigned int`, ensuring the test suite accurately reflects carry behavior across different architectures.
