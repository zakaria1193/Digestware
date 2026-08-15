---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- performance
commit_hash: dc094853da348f705f95ed0a863feeeea3cd52c9
source_type: github
author: Andrew MacLeod
headline: Use logical depth limit in fast VRP
tldr: Limits fast VRP iterations using logical depth to prevent exponential blow-up.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `gori_name_helper` in `gimple-range-gori.cc` now uses a `logical_depth`
  counter to limit the number of iterations. Fast VRP, particularly when dealing with
  complex control flow or deeply nested expressions, can exhibit exponential behavior.
  This change introduces a bound based on the `logical_depth` to cap the analysis
  depth, preventing excessive runtime and potential hangs on pathological cases, aligning
  it with the `logical_depth` limits used elsewhere in the optimization passes.
primer_glossary:
- term: Value Range Propagation (VRP)
  definition: A compiler optimization pass that determines the possible range of values
    for variables at different points in the program. This information is used to
    simplify expressions and perform other optimizations.
- term: fast VRP
  definition: A variant of Value Range Propagation that aims for quicker analysis,
    potentially at the cost of some precision, often used in critical optimization
    paths.
- term: logical_depth
  definition: A parameter or counter used in compiler analysis to limit the depth
    of recursion or iteration in certain complex operations, preventing excessive
    resource consumption.
- term: exponential behaviour
  definition: A situation where the runtime or resource usage of an algorithm grows
    exponentially with the input size, often leading to performance issues or system
    hangs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc094853da348f705f95ed0a863feeeea3cd52c9
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This commit enhances the fast Value Range Propagation (VRP) analysis by incorporating a `logical_depth` limit. This limit is crucial for preventing potentially exponential execution time in complex scenarios. By constraining the analysis depth, the compiler avoids excessive computation, ensuring faster and more predictable optimization performance.
