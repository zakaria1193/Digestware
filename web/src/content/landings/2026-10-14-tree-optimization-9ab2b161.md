---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
commit_hash: 9ab2b161c7cb19d85f124ec2d30bec89169a4e05
source_type: github
author: Richard Biener
headline: tree-optimization/127811 - revise previous fix for SLP scheduling
tldr: Corrects SLP scheduling to properly handle external vector definitions when
  -fno-trapping-math is enabled.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Revises the SLP vectorizer's handling of external definitions within
  `vect_schedule_slp_node`. When `-fno-trapping-math` is active, external definitions
  can lead to the scheduler incorrectly attempting to insert instructions after a
  throwing external vector definition. This change adjusts the logic to clear `last_stmt`
  for such cases, ensuring correct insertion at the region boundary and aligning with
  the invariant that non-trapping operations should not follow a potentially throwing
  external call.
primer_glossary:
- term: SLP
  definition: Superword-Level Parallelism. A compiler optimization technique that
    exploits the SIMD (Single Instruction, Multiple Data) capabilities of processors
    by parallelizing operations on contiguous data elements.
- term: tree-optimization
  definition: A phase in the GCC compiler where code is represented and optimized
    using an intermediate representation called GENERIC/GIMPLE, which is tree-like.
- term: vectorization
  definition: The process of transforming code to use SIMD instructions, allowing
    a single instruction to operate on multiple data elements simultaneously.
- term: -fno-trapping-math
  definition: A GCC compiler flag that affects how floating-point exceptions (like
    division by zero or overflow) are handled. When enabled, it assumes these exceptions
    do not trap, which can enable more aggressive optimizations.
- term: external definition
  definition: In this context, likely refers to a call to an external function or
    a definition that relies on external linkage, which might have side effects or
    potential to throw exceptions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ab2b161c7cb19d85f124ec2d30bec89169a4e05
date: '2026-10-14'
is_stub: false
stub_reason: ''
---

This commit revises a previous fix for SLP (Superword-Level Parallelism) scheduling to correctly handle external vector definitions when the -fno-trapping-math option is used. The change ensures that the scheduler consistently inserts operations at the region boundary by clearing the last statement when an external definition is encountered, thus preventing incorrect assertions and improving vectorization reliability.
