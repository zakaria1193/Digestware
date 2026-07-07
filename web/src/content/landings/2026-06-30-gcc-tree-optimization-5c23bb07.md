---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- pass removal
commit_hash: 5c23bb074af23f00dd3fe1745b9dd99245fa4bba
source_type: github
author: Kyrylo Tkachov
headline: Remove path-splitting pass, deprecate -fsplit-paths
tldr: GCC removes the path-splitting optimization pass and deprecates its associated
  flag due to negative interactions with other optimizations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `pass_split_paths` pass aimed to improve instruction-level parallelism
  by duplicating basic blocks in IF-THEN-ELSE structures feeding into loop latches.
  However, its heuristic-driven approach frequently hindered subsequent optimizations
  such as load commoning and if-conversion, and could negatively impact loop unrolling.
  Its removal and the deprecation of `-fsplit-paths` simplify the optimization pipeline
  and resolve issues reported in PR120892, while retaining `param_max_jump_thread_duplication_stmts`
  for shared use.
primer_glossary:
- term: pass_split_paths
  definition: An optimization pass in GCC that duplicates basic blocks in control
    flow graphs to improve instruction scheduling, particularly around loop constructs.
    It has been removed due to negative interactions with other optimization passes.
- term: -fsplit-paths
  definition: A GCC command-line option that enabled the path-splitting optimization
    pass. This option is now deprecated and has no effect.
- term: if-conversion
  definition: An optimization technique that transforms conditional branches into
    predicated instructions, allowing for more straightforward instruction scheduling
    and execution.
- term: loop unrolling
  definition: An optimization that replicates the body of a loop multiple times to
    reduce loop overhead and increase instruction-level parallelism.
- term: common subexpression elimination
  definition: An optimization that identifies and eliminates redundant computations
    of the same expression within a program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5c23bb074af23f00dd3fe1745b9dd99245fa4bba
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

The `pass_split_paths` optimization pass, which duplicated loop bodies to optimize control flow, has been removed from GCC. This pass often interfered with crucial optimizations like loop unrolling and if-conversion by duplicating code before common subexpression elimination and other passes could run. The associated `-fsplit-paths` option is now deprecated and does nothing, though it is still accepted for backward compatibility.
