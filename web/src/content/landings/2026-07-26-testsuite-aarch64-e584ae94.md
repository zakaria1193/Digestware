---
project: gcc
subsystem: testsuite/aarch64
patch_id: null
tags:
- aarch64
- vectorization
- testing
- optimization
commit_hash: e584ae9446b47bf3a06183ebedc4f2ffc53fa02c
source_type: github
author: Kyrylo Tkachov
headline: 'testsuite/aarch64: update the fcmla counts in pr122408_1.f90'
tldr: Adjusts aarch64 Fortran test case to reflect updated fcmla instruction counts
  after optimization changes.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change updates the `pr122408_1.f90` test case for aarch64 to reflect
  changes in `fcmla` instruction counts. The BB SLP (Basic Block Superword Level Parallelism)
  vectorizer, enhanced by commit r17-141-g76b8869f08a6, now better attributes statements
  for SLP pattern matching. This causes previously unprofitable scalar subroutines
  for complex addition/subtraction (`c_add_ab`, `c_sub_ab`) to be vectorized into
  `.COMPLEX_MUL`. Each complex multiply expands to two `fcmla` instructions (`#0`
  and `#90` rotations). This increases the total count of `fcmla` instructions with
  `#0` rotation from two…
primer_glossary:
- term: fcmla
  definition: Fused Complex Multiplication Accumulate. An ARM instruction that performs
    a complex multiplication and adds the result to an accumulator, common in SIMD
    and floating-point operations.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set. GCC supports generating
    code for this architecture.
- term: BB SLP
  definition: Basic Block Superword Level Parallelism. A compiler optimization technique
    that identifies opportunities to vectorize code within a basic block by finding
    identical or similar instruction sequences that can be executed in parallel on
    SIMD hardware.
- term: Vectorization
  definition: The process of transforming scalar code (operating on single data elements)
    into vector code (operating on multiple data elements simultaneously) to improve
    performance on SIMD-capable processors.
- term: regression
  definition: In software development, a regression is a bug that appears in a new
    version of the software which was not present in a previous version. Test cases
    are used to detect regressions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e584ae9446b47bf3a06183ebedc4f2ffc53fa02c
date: '2026-07-26'
is_stub: true
stub_reason: low_score
---

This commit updates the expected counts of `fcmla` instructions in an aarch64 Fortran testcase. A recent optimization pass, 'tree-optimization/124222 - rewrite BB SLP costing scalar coverage', improved loop vectorization for complex multiplication subroutines. This led to the generation of more `fcmla` instructions (specifically using rotation angles #0 and #90) where previously fewer were used. The test case is modified to accurately reflect these new counts, ensuring better regression coverage for complex number computations.
