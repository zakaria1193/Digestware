---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compile-time
- GORI
- SSA
commit_hash: 16c272814a0b09b859adb10ea760b59f47c993a6
source_type: github
author: Andrew MacLeod
headline: Limit GORI recomputation to a single level
tldr: GORI's range analysis is limited to one level of recomputation to prevent excessive
  compile times.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The GORI analysis pass, specifically `gori_compute::has_edge_range_p`,
  supports backward solving through SSA definitions to recompute operand ranges. This
  commit addresses an exponential complexity issue by removing nested recomputations,
  limiting the analysis to a single recomputation per edge. This optimization targets
  performance issues arising from deep, recursive analysis chains, ensuring that deeper
  queries only refine inputs for the immediate next calculation, not trigger further
  nested solves.
primer_glossary:
- term: GORI
  definition: Generic Optimization Representation Interface. A framework within GCC
    for implementing various compiler optimizations and analyses.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation in compilers
    where every variable is assigned a value exactly once, simplifying many dataflow
    analyses and optimizations.
- term: Range analysis
  definition: A compiler optimization technique that determines the possible range
    of values a variable can take at a particular point in the program. This information
    can be used to eliminate redundant checks or improve code generation.
- term: Compile time
  definition: The time it takes for the compiler to translate source code into executable
    machine code. Optimizations can significantly increase compile time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/16c272814a0b09b859adb10ea760b59f47c993a6
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

The GORI (Generic Optimization Representation Interface) analysis, used for range computations, could previously perform nested recomputations on SSA definitions. This led to combinatorial blow-ups in compile time for complex cases. This patch restricts GORI to a single level of recomputation per edge, significantly improving compile-time performance without impacting its core functionality. A test case for a spurious warning is also removed as a result.
