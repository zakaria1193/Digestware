---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- vectorization
- testing
commit_hash: 1fb622222606c1ef960d3fff0b420bb8e7473cff
source_type: github
author: Richard Biener
headline: 'tree-optimization: Add testcase for PR110935'
tldr: A testcase is added for a previously fixed optimization bug (PR110935).
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces a regression test for PR tree-optimization/110935.
  The fix for this bug, which relates to vectorization or SLP optimizations within
  GCC's tree-SSA pipeline, was applied in GCC 16. The new test file, `bb-slp-reduc-pr110935.c`,
  specifically targets the scenario that triggered the original bug, thereby ensuring
  the continued correctness of the relevant optimization passes.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC's optimization pipeline that operates on an intermediate
    representation called GIMPLE (or 'tree'). It performs various optimizations before
    code generation.
- term: PR110935
  definition: Problem Report 110935. This refers to a specific bug that was filed
    and subsequently fixed in the GCC bug tracking system.
- term: vectorization
  definition: An optimization technique that performs the same operation on multiple
    data elements simultaneously, often using special SIMD (Single Instruction, Multiple
    Data) CPU instructions.
- term: SLP
  definition: Superword Level Parallelism. An optimization technique used by compilers
    to find and exploit data-level parallelism in straight-line code by grouping independent
    operations on different data elements into vector instructions.
- term: GIMPLE
  definition: GCC's Intermediate Representation (IR) that represents the program's
    structure in a simplified, three-address-like form. Optimizations operate on this
    representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1fb622222606c1ef960d3fff0b420bb8e7473cff
date: '2026-08-07'
is_stub: true
stub_reason: low_score
---

This commit adds a new test case to verify a fix for bug PR110935 in the GCC tree optimization passes. The bug, which affected vectorization or SLP (Superword Level Parallelism) optimizations, was resolved in GCC 16. The new test case ensures that this specific optimization issue does not reappear.
