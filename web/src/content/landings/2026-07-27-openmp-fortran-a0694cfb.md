---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- optimization
- parallelism
commit_hash: a0694cfb5b488dfeb65623444a14cab57e7df6bd
source_type: github
author: Tobias Burnus
headline: 'OpenMP: Fortran + ME - update for spatial dimensions + message clause'
tldr: Adds 'message' and 'severity' clauses to OpenMP directives in Fortran and updates
  middle-end handling.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Extends OpenMP support in GCC for Fortran by introducing the `message`
  and `severity` clauses to `target`, `teams`, and `parallel` directives. It enhances
  the middle-end processing (`omp-expand.cc`) to handle `dims` and `strict` modifiers
  for team/thread counts, and relocates error reporting from the Fortran parser to
  the middle end.
primer_glossary:
- term: OpenMP
  definition: A widely adopted API for shared-memory parallel programming. It consists
    of a set of compiler directives, library routines, and environment variables.
- term: middle-end
  definition: The part of a compiler that performs optimizations and transformations
    on an intermediate representation (IR) of the code, after the front-end has parsed
    the source code.
- term: spatial dimensions
  definition: In the context of OpenMP, refers to how threads are mapped across multiple
    dimensions, typically used with `teams` and `parallel` directives to control thread
    affinity and distribution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0694cfb5b488dfeb65623444a14cab57e7df6bd
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This commit enhances OpenMP support in the Fortran front-end and middle-end by adding 'message' and 'severity' clauses to target, teams, and parallel directives. It also updates the handling of spatial dimensions ('dims') and strict modifiers for team and thread counts, moving 'sorry, unimplemented' diagnostics to the middle end.
