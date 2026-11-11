---
project: gcc
subsystem: openmp/c++
patch_id: null
tags:
- OpenMP
- C++
- memory management
commit_hash: 9bafebd00ec54498bcc0adc9a8dbb74c3624dce4
source_type: github
author: Waffl3x
headline: 'OpenMP/C++: Add support for ''omp allocate'' directive'
tldr: C++ support for the OpenMP ALLOCATE directive is now available, enabling explicit
  control over memory allocation for OpenMP-related data.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch adds C++ support for the `omp allocate` directive by introducing
  an `OMP_ALLOCATE` tree code and an 'omp allocate' attribute on `VAR_DECL` nodes.
  It parses clauses and stores them in the new tree code, which is used during substitution.
  Unlike the C front-end, this implementation allows implicit conversions for clause
  arguments, aligning with OpenMP committee clarifications. It defers diagnostics
  for clause arguments in templates until instantiation due to difficulties with pre-instantiation
  implicit conversions. The attribute is carefully handled during parsing to maintain
  order w…
primer_glossary:
- term: omp allocate directive
  definition: An OpenMP directive used to control memory allocation for data, allowing
    specification of memory spaces or strategies.
- term: VAR_DECL
  definition: A tree node in GCC's internal representation representing a variable
    declaration.
- term: tree code
  definition: An internal data type or representation used by the GCC compiler to
    represent various constructs in the source code and intermediate representation.
- term: gimplification
  definition: A compiler phase where the code is transformed into an intermediate
    representation called GIMPLE, which is suitable for optimization.
- term: template instantiation
  definition: The process in C++ where a template (class or function) is compiled
    with specific types or values provided as arguments, generating a concrete class
    or function.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9bafebd00ec54498bcc0adc9a8dbb74c3624dce4
date: '2026-05-05'
is_stub: false
stub_reason: ''
---

This patch introduces support for the OpenMP `allocate` directive in C++. It adds an 'omp allocate' attribute to variables declared within the directive, which is used during lowering to manage data transformations. The implementation introduces a new tree code, `OMP_ALLOCATE`, to store directive clauses and supports implicit conversions for clause arguments, diverging slightly from the C front-end's stricter requirements. This feature allows for finer control over memory allocation in parallel regions.
