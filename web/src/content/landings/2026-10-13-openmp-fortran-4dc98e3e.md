---
project: gcc
subsystem: OpenMP/Fortran
patch_id: null
tags:
- openmp
- fortran
- parser
- specification
commit_hash: 4dc98e3ecd1b8ef06ccbff7108523f8a5be8ab30
source_type: github
author: Tobias Burnus
headline: 'OpenMP/Fortran: Disallow severity clause on target/teams'
tldr: 'OpenMP/Fortran: Severity clause is now disallowed on target/teams constructs.'
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes support for the OMP_CLAUSE_SEVERITY in OpenMP target
  and teams constructs within the Fortran frontend. The severity clause was introduced
  in OpenMP TR15 but later removed before OpenMP 6.1 due to inconsistencies in error
  handling. This change ensures the parser and tree representation (`tree-core.h`,
  `tree-pretty-print.cc`) correctly reject this clause for target/teams, while still
  allowing the associated message clause.
primer_glossary:
- term: OpenMP
  definition: A standardized API for shared-memory parallel programming, providing
    directives that can be added to C, C++, and Fortran code to specify parallel regions
    and tasks.
- term: severity clause
  definition: An OpenMP clause that specifies the action to take when an error occurs,
    such as printing a message or terminating execution.
- term: target construct
  definition: An OpenMP construct that offloads computation to a device, such as a
    GPU.
- term: teams construct
  definition: An OpenMP construct that creates a set of teams of threads, allowing
    for nested parallelism.
- term: TR15
  definition: Technical Report 15, an earlier specification document for OpenMP that
    may have contained features not present in the final standard.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4dc98e3ecd1b8ef06ccbff7108523f8a5be8ab30
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

The severity clause for OpenMP target and teams constructs has been disallowed to align with OpenMP specifications (Spec Issue 5010). This change updates the parser and related code to reflect that the severity clause, which previously had inconsistent error termination behavior, is no longer permitted for these constructs, although message clauses remain.
