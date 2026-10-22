---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- undefined behavior
- gimple
commit_hash: f035e26ef7eee00fd0028531b087e4d2b72c6695
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix UB path isolation to correctly associate later UBs'
tldr: Improves the path isolation scheme to correctly track undefined behavior across
  multiple UBs on the same path.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-ssa-isolate-paths.cc` pass aims to isolate code paths to
  simplify analysis, particularly for undefined behavior (UB). Previously, the iteration
  over PHIs and arguments in `find_implicit_erroneous_behavior` led to incorrect association
  of later UBs with incorrectly isolated paths. This patch modifies the iteration
  to traverse edges first, then PHIs, ensuring that all UBs detected on a given edge
  are processed within the context of that single, duplicated path, thus correctly
  associating subsequent UBs with their originating path.
primer_glossary:
- term: Undefined Behavior (UB)
  definition: Program behavior that results from violations of the C/C++ standards,
    for which the standard imposes no requirements. Compilers may assume UB does not
    occur, leading to optimizations that can produce unexpected results if UB is present.
- term: GIMPLE
  definition: GCC's internal representation (IR) for code, which is a three-address
    pseudo-instruction language used for optimizations. It sits between the parsed
    source code and the machine code.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once. This simplifies many optimizations.
- term: PHI node
  definition: In SSA form, a special instruction used at the join of control flow
    paths to select the correct value based on which path was taken to reach that
    point.
- term: NULL dereference
  definition: An attempt to access memory through a pointer that has a value of NULL,
    which is undefined behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f035e26ef7eee00fd0028531b087e4d2b72c6695
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in the `isolate_paths` iteration scheme within `gimple-ssa-isolate-paths.cc` where multiple undefined behaviors (UBs) on the same code path were not correctly associated. The fix changes the discovery of NULL dereferences to iterate over incoming edges (paths) and then PHIs, ensuring that all UBs on a specific path are processed together. This improves the accuracy of UB detection and isolation.
