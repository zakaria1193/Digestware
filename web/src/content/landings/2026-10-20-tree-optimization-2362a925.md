---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- openmp
- vectorization
- codegen
commit_hash: 2362a925323974dcf00b0bf57ab246e5efcdb2b6
source_type: github
author: Richard Biener
headline: Fix OpenMP simdclone call codegen for array results
tldr: Corrects an accounting error in OpenMP simdclone calls when the result type
  differs from the vector type, specifically for array cases.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a bug in `vectorizable_simd_clone_call` within
  `tree-vect-stmts.cc`. Specifically, when emitting a `simdclone` call where the result
  type is an array and differs from the chosen vector type, the accounting for the
  materialized vector CTOR was incorrect. The change simplifies this accounting logic
  to fix the issue, alongside a new test case (`vect-simd-21.c`).
primer_glossary:
- term: simdclone
  definition: A compiler intrinsic or construct related to OpenMP SIMD operations.
    It likely involves cloning or adapting code for SIMD execution, possibly handling
    cases where the target SIMD vector width differs from the desired operation width.
- term: Vector CTOR
  definition: A constructor for a vector type. In the context of GCC's intermediate
    representation (GIMPLE or Tree), this refers to the code generated to create or
    initialize a vector data type, often used when converting between different vector
    representations or types.
- term: Tree Optimization
  definition: A phase in the GCC compiler pipeline that operates on an intermediate
    representation called 'tree'. This phase performs various optimizations, including
    loop transformations, constant propagation, and vectorization, before the code
    is lowered to GIMPLE or machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2362a925323974dcf00b0bf57ab246e5efcdb2b6
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

A code generation issue in OpenMP `simdclone` calls has been fixed. When the result type of a `simdclone` call differs from the vector type used internally, the compiler needs to materialize a vector constructor (CTOR). The previous implementation incorrectly accounted for this CTOR, particularly in array scenarios. This commit simplifies that accounting to resolve the bug and includes a new test case.
