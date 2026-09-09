---
project: gcc
subsystem: backthreader
patch_id: null
tags:
- optimization
- backthreader
- gcc
- performance
commit_hash: e1424f0b30525ced215042169035ff7c1ef5ca9d
source_type: github
author: Aldy Hernandez
headline: Backthreader optimization skips blocks with no inferred ranges.
tldr: Backthreader pass is faster by skipping blocks that have no inferred pointer
  ranges.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `backthreader::thread_blocks()` function, specifically the `path_range_query::adjust_for_non_null_uses`
  method, has been optimized. Instead of iterating over all exit dependencies for
  every block in a path, it now uses a new member `m_pointer_exit_dependencies` to
  store and iterate over only pointer-related dependencies. This optimization also
  allows the pass to quickly skip blocks where no ranges can be inferred by populating
  `m_pointer_exit_dependencies` during `compute_ranges`, reducing redundant oracle
  queries and improving performance by 3.6% on the stage1 .ii corpus.
primer_glossary:
- term: backthreader
  definition: A compiler pass in GCC that analyzes and optimizes code flow, potentially
    related to backward analysis or threading through control flow graphs.
- term: inferred ranges
  definition: Information about the possible values or properties (e.g., pointer non-null
    status) of variables that the compiler deduces during analysis.
- term: inference oracle
  definition: A component within the compiler that provides information or answers
    queries about code properties, such as data ranges or possible values.
- term: control flow graph (CFG)
  definition: A representation of all execution paths in a program, used by compilers
    for analysis and optimization.
- term: stage1 .ii corpus
  definition: A set of C source files preprocessed into '.ii' files, used for testing
    and profiling GCC during its initial compilation stage.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e1424f0b30525ced215042169035ff7c1ef5ca9d
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

The backthreader pass in GCC has been optimized to improve performance. It now efficiently skips blocks that lack inferred pointer ranges, reducing unnecessary work. This change specifically targets `adjust_for_non_null_uses` by collecting pointer dependencies once per path and querying the inference oracle only when necessary, leading to a measurable speedup.
