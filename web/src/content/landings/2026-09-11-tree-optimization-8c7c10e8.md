---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- compiler bug
- ICE
commit_hash: 8c7c10e82d661785181f199fdc6b24890b30a54e
source_type: github
author: Richard Biener
headline: Tree optimizer fixes ICE with lane-reducing reduction.
tldr: Tree optimizer corrects loop mask registration in lane-reducing reductions,
  fixing an ICE and a loop mask issue.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR tree-optimization/127310 is fixed by reordering operations within
  `vectorizable_lane_reducing` in `tree-vect-loop.cc`. The costing logic, which adjusts
  `ncopies_for_cost`, is now applied *after* the loop masks are registered. Previously,
  `ncopies_for_cost` was modified before being used for mask registration, leading
  to incorrect masks and an ICE. A new test case `vect-pr127310.c` is added to verify
  this fix.
primer_glossary:
- term: tree-optimization
  definition: An intermediate representation (IR) and optimization framework within
    GCC. It manipulates code in a tree-like structure to perform various optimizations
    before generating machine code.
- term: ICE (Internal Compiler Error)
  definition: An unexpected error that occurs within the compiler itself, halting
    the compilation process. These are typically bugs in the compiler that need to
    be fixed by the developers.
- term: lane-reducing reduction
  definition: A type of loop-carried dependency operation in vectorized code where
    multiple lanes (parallel processing units) contribute to a single accumulating
    result, such as a sum or maximum.
- term: loop mask registration
  definition: The process of associating a mask (a bitmask indicating active elements
    or lanes) with a loop iteration or vectorized operation, used to control which
    parts of the computation are active.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8c7c10e82d661785181f199fdc6b24890b30a54e
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

An internal compiler error (ICE) related to lane-reducing reductions has been fixed in the tree optimizer. The issue stemmed from the costing code adjusting `ncopies_for_cost` before it was used for loop mask registration. This change ensures that loop mask registration occurs after costing, resolving the ICE and correcting incorrect loop mask behavior.
