---
project: gcc
subsystem: doc/invoke.texi
patch_id: null
tags:
- doc
- invoke.texi
- openmp
- ompt
commit_hash: 13e2608e6bb6c0b85c55fa9a72e57f0c0e5ba372
source_type: github
author: Tobias Burnus
headline: 'doc/invoke.texi: -fopenmp-ompt - add additional construct'
tldr: Documentation update for -fopenmp-ompt flag now includes 'scope' construct.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This documentation update clarifies that the `-fopenmp-ompt` flag,
  which enables OMPT (OpenMP Tools Interface) support, now also influences the OpenMP
  `scope` construct. Previously, its effect might have been implicitly limited or
  not explicitly stated for `scope`. The change ensures users are aware of the full
  scope of this flag's impact on OpenMP runtime behavior and tracing.
primer_glossary:
- term: -fopenmp-ompt
  definition: A GCC command-line option that enables support for the OpenMP Tools
    Interface (OMPT). OMPT allows external tools, such as debuggers and profilers,
    to interact with and monitor OpenMP runtime execution.
- term: OpenMP 'scope' construct
  definition: An OpenMP construct that defines a region of code where certain variables
    or properties have a specific lifetime or visibility. It can be used for managing
    thread-local storage or other scope-specific features.
- term: OMPT
  definition: OpenMP Tools Interface. A standardized interface that enables tools
    to observe and control OpenMP runtime events and states.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/13e2608e6bb6c0b85c55fa9a72e57f0c0e5ba372
date: '2026-07-22'
is_stub: true
stub_reason: low_score
---

The documentation for GCC's `-fopenmp-ompt` flag has been updated to reflect its extended functionality. Since a recent commit, this flag now also affects the OpenMP 'scope' construct. The documentation has been modified to include this, and directives are now sorted alphabetically for better readability.
