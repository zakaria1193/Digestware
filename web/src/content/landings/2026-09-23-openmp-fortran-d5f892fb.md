---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- fortran
- openmp
- testing
commit_hash: d5f892fb06695ad740c6bdeef14e9b5ae6dc74bc
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Add test for comma between directive and clause'
tldr: Adds a test case to verify that OpenMP directives in Fortran correctly accept
  a comma before clauses.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a regression test for Fortran OpenMP directives. It
  specifically targets the syntax change introduced in r17-4506-gb28a16af7fa7fe, which
  allows a comma to appear between an OpenMP directive keyword (e.g., !$OMP) and its
  subsequent clauses. The test ensures this syntactic flexibility is correctly accepted
  by the gfortran parser.
primer_glossary:
- term: OpenMP
  definition: A directive-based API for shared-memory multiprocessing programming.
    It allows developers to insert pragmas into C, C++, and Fortran code to specify
    parallel regions.
- term: Fortran
  definition: A high-level programming language used primarily for numerical and scientific
    computing. GCC's `gfortran` is its Fortran compiler.
- term: Directive
  definition: In OpenMP, a pragma or comment that instructs the compiler on how to
    parallelize the code.
- term: Clause
  definition: An option or argument that modifies the behavior of an OpenMP directive,
    such as specifying loop iteration schedules or data sharing attributes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d5f892fb06695ad740c6bdeef14e9b5ae6dc74bc
date: '2026-09-23'
is_stub: true
stub_reason: low_score
---

A new test case, directive-comma-clause.f90, has been added to the Fortran test suite. This test specifically verifies the correct parsing and handling of comma separation between OpenMP directives and their clauses, ensuring compliance with the OpenMP standard for Fortran.
