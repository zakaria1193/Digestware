---
project: gcc
subsystem: openmp/fortran
patch_id: null
tags:
- openmp
- fortran
- gpu
- parallelism
commit_hash: 3611bdfdc270c16f1317bb2c951909ef2cb99769
source_type: github
author: Tobias Burnus
headline: OpenMP/Fortran clauses target-consistent and dyn_groupprivate now evaluated
  on host
tldr: Evaluates num_teams, thread_limit, and dyn_groupprivate clauses on the host
  for OpenMP/Fortran target regions, aligning with recent specification changes.
impact_score: 6
performance_win: false
breaking_change: true
outcome: committed
primer_expert: 'This change affects the OpenMP runtime and Fortran frontend, specifically
  within the `gimplify.cc` and `openmp.cc` files. It modifies how `num_teams`, `thread_limit`,
  and `dyn_groupprivate` clauses are processed for `target` and `teams` constructs.
  The core issue addressed is the timing of expression evaluation: ensuring these
  clauses are evaluated on the host prior to kernel launch to maintain target consistency,
  as dictated by OpenMP 5.0/6.0 specifications. This impacts the interaction between
  host and device execution contexts for parallel regions.'
primer_glossary:
- term: target region
  definition: An OpenMP construct that specifies a region of code to be executed on
    a target device, such as a GPU. It allows for offloading computation.
- term: teams construct
  definition: An OpenMP construct that creates a set of teams of threads, allowing
    for nested parallelism and flexible thread management.
- term: num_teams clause
  definition: An OpenMP clause that specifies the number of teams to be created for
    a `teams` construct.
- term: thread_limit clause
  definition: An OpenMP clause that specifies the maximum number of threads per team.
- term: dyn_groupprivate
  definition: An OpenMP clause that provides private variables for each thread within
    a dynamic group, typically used with `teams` constructs.
- term: target consistent
  definition: Refers to clauses whose values must be the same whether evaluated on
    the host or the device. This ensures predictable behavior across different execution
    environments.
- term: gimplify.cc
  definition: A GCC source file containing the gimplification pass, which converts
    the compiler's intermediate representation (tree) into GENERIC and GIMPLE forms
    for further optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3611bdfdc270c16f1317bb2c951909ef2cb99769
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This commit ensures that OpenMP clauses like `num_teams` and `thread_limit` within `target` regions, and `dyn_groupprivate`, are evaluated on the host. This aligns with OpenMP 5.0 and 6.0 specifications which mandate host evaluation for consistency, especially when launching GPU kernels. Previously, these evaluations sometimes occurred too late or on the device, potentially leading to incorrect behavior. The change enhances correctness and adheres to evolving OpenMP standards.
