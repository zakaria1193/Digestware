---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- compiler
- language feature
commit_hash: a39d268ced985763ac84ba87c243d44f79dd304a
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Accept optional constant boolean expressions for clauses'
tldr: Fortran OpenMP now supports optional constant logical expressions for clauses,
  allowing dynamic enablement/disablement.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit enhances the Fortran frontend's OpenMP clause parsing to
  support the OpenMP 6 feature of optional constant logical expressions for clauses
  like `atomic`, `flush`, `memorder`, and `requires`. New parsing functions `gfc_match_boolean_clause`
  and `gfc_match_dupl_branch_clause` are introduced. The `gfc_omp_requires_kind` enum
  is extended with `OMP_REQ_NONE`. This allows clauses to be conditionally enabled
  or disabled via compile-time constants, affecting behavior for diagnostics and clause
  group logic. Support for variable arguments in clauses like `nowait` is deferred.
primer_glossary:
- term: OpenMP
  definition: Open Multi-Processing. An API for parallel programming that supports
    shared-memory multiprocessing programming in C, C++, and Fortran.
- term: Fortran
  definition: A high-level programming language commonly used for scientific and numerical
    computation. GCC's gfortran compiler implements the Fortran standard.
- term: clause
  definition: In OpenMP directives, a clause specifies optional parameters or behavior
    modifiers. Examples include `private`, `shared`, `nowait`, etc.
- term: constant logical expression
  definition: A boolean expression whose value is fixed at compile time, such as `.true.`
    or `.false.`.
- term: VLA
  definition: Variable Length Array. An array whose size is determined at runtime,
    not compile time. This can be used in C99 and later standards, and also in Fortran.
- term: diagnostics
  definition: Compiler messages that report errors, warnings, or informational notes
    to the user during the compilation process.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a39d268ced985763ac84ba87c243d44f79dd304a
date: '2026-09-26'
is_stub: false
stub_reason: ''
---

OpenMP 6 introduces the ability to use optional constant logical expressions with clauses that do not typically take arguments. This allows programmers to enable or disable OpenMP features at compile time using `.true.` or `.false.` constants. While for some clauses `.false.` means the clause is absent, for others it means the feature is present but inactive, which affects diagnostics. The implementation currently focuses on Fortran and supports most clauses, with exceptions for mandatory clauses and those already accepting non-constant arguments.
