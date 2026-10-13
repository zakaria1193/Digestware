---
project: gcc
subsystem: gcc/fortran/openmp
patch_id: null
tags:
- fortran
- openmp
- compiler
commit_hash: 1152c67150f4051d1a44ed52e8aafe3c9bbe4eb9
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Restore non-const expr for ''priority'' clause'
tldr: Fortran OpenMP 'priority' clause now accepts non-constant expressions again,
  reverting a change that conformed to a later standard.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `resolve_omp_clauses` function in `openmp.cc` is modified to permit
  non-constant expressions for the 'priority' clause. This partially reverts r17-5077-g8bb7a53a0df5c5,
  addressing OpenMP Issue 5176, which mandated constant expressions for 'priority'
  since OpenMP 5.2, whereas earlier versions (since 4.5) allowed non-constant ones.
  Tests `masked-1.f90` and `taskloop-1.f90` are reverted, and `taskloop-2.f90` is
  updated.
primer_glossary:
- term: OpenMP
  definition: An API for shared-memory parallel programming, primarily used in C,
    C++, and Fortran. It uses directives to specify parallel regions and work-sharing
    constructs.
- term: priority clause
  definition: An OpenMP clause that can be used with directives like 'task' or 'taskloop'
    to suggest a relative execution priority for tasks.
- term: constant expression
  definition: An expression that can be evaluated to a constant value at compile time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1152c67150f4051d1a44ed52e8aafe3c9bbe4eb9
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This commit partially reverts a change that required the 'priority' clause in Fortran OpenMP directives to use a constant expression. The 'priority' clause now accepts non-constant expressions again, aligning with behavior in OpenMP versions prior to 5.2, which is considered a syntax conversion bug.
