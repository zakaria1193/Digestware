---
project: gcc
subsystem: tree-data-ref
patch_id: null
tags:
- optimization
- alias analysis
- vectorization
- points-to analysis
commit_hash: 5a3ad9374a73df7df7e8a00b1c06fbf30ad7298c
source_type: github
author: Philipp Tomsich
headline: Tree-data-ref uses points-to info for alias analysis.
tldr: Improves alias analysis accuracy by using points-to information for SSA names.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-data-ref` pass uses SSA names to represent memory locations.
  When pointer SSA names (`SSA_NAME_PTR_INFO`) are created late in the optimization
  pipeline (e.g., by PRE re-materialization), they might not have points-to information.
  The `dr_may_alias_p` function, when evaluating `DR_BASE_OBJECT`, would previously
  fall back to a less precise alias check. This change modifies `dr_may_alias_p` to
  consult the `DR_PTR_INFO` associated with the data references, which stores the
  result of the points-to analysis. This allows for more accurate alias queries, particularly
  for cross-iteration ana…
primer_glossary:
- term: tree-data-ref
  definition: A GCC internal pass that analyzes and manipulates data references within
    the compiler's intermediate representation (tree).
- term: alias analysis
  definition: The process of determining whether two or more memory accesses might
    refer to the same memory location.
- term: SSA name
  definition: Static Single Assignment form names, a representation where each variable
    has a single definition.
- term: points-to analysis
  definition: A static analysis technique that determines the set of memory locations
    a pointer can possibly refer to.
- term: DR_PTR_INFO
  definition: A data structure within the tree-data-ref pass that stores points-to
    information for pointer SSA names.
- term: PRE
  definition: Partial Redundancy Elimination, a compiler optimization pass.
- term: vectorization
  definition: The process of transforming a program to use SIMD (Single Instruction,
    Multiple Data) instructions, allowing multiple data elements to be processed in
    parallel.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5a3ad9374a73df7df7e8a00b1c06fbf30ad7298c
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

This commit enhances the `dr_may_alias_p` function in tree-data-ref by utilizing points-to information stored in `DR_PTR_INFO`. This addresses an issue where pointer SSA names created after the last points-to computation lacked this information, leading to overly conservative alias analysis. By intersecting the new points-to solutions with existing ones, the accuracy of alias checks is improved, reducing runtime and enabling better vectorization, as demonstrated on SPEC CPU 2026's 722.palm_r.
