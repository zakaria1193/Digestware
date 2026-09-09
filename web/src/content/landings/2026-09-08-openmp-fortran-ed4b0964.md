---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- OpenMP
- Fortran
- compiler-frontend
commit_hash: ed4b096464cd751c3a8af378a0f9724b55532621
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Support underscore variant of directive names'
tldr: Fortran OpenMP directive names with underscores are now supported in `assume`
  clauses and as modifiers in `if` clauses.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Adds underscore variants for OpenMP directive names (e.g., `declare_mapper`,
  `target_data`) to `gfc_omp_directives` and handles `target_...` as modifiers in
  the `if` clause, fulfilling OpenMP 5.x features for Fortran. Supports these in `assume`
  statement's `absent` and `contains` clauses.
primer_glossary:
- term: OpenMP
  definition: A standardized API for shared-memory parallel programming. It uses directives
    and clauses to specify parallelism, data sharing, and offload behavior.
- term: Fortran
  definition: A high-level programming language commonly used for numerical and scientific
    computation. GCC's `gfortran` compiler supports OpenMP directives within Fortran
    code.
- term: directive name
  definition: The specific keyword identifying an OpenMP construct (e.g., `parallel`,
    `for`, `target`).
- term: assume statement
  definition: A Fortran statement that allows programmers to provide information to
    the compiler that it can use for optimization or to check for consistency. In
    this context, it's used for compiler directives related to OpenMP.
- term: if clause
  definition: An OpenMP clause that specifies a conditional execution for a directive.
    The condition is evaluated at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ed4b096464cd751c3a8af378a0f9724b55532621
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch enhances the Fortran front-end to support underscore variants of multi-word OpenMP directive names, aligning with recent OpenMP specification updates. These underscored directive names, such as `declare_mapper` and `target_data`, are now recognized within the `absent` and `contains` clauses of `assume` statements. Additionally, directive name modifiers like `target_...` can now be correctly handled within the `if` clause. A new test case verifies this functionality.
