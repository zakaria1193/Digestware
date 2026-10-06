---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- alias analysis
commit_hash: b4de9d73b47972bc89df288997c8f3a3862bc1b1
source_type: github
author: Richard Biener
headline: FRE optimization improved by fixing aliasing walk logic
tldr: Fixes a bug in alias analysis that caused incorrect handling of PHI nodes, enabling
  more effective loop-invariant code motion.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-alias.cc` and `tree-ssa-alias.h` files implement alias
  analysis. The `get_continuation_for_phi` function, used by FRE, previously aborted
  if it encountered an already visited region when `abort_on_visited` was true, even
  if the current reference translation was different. This commit changes `walk_non_aliased_vuses`
  to clear the visited bitmap upon reference translation instead of tracking it, thus
  removing the need for `abort_on_visited`. This resolves PR127693 by ensuring all
  regions are verified with the current reference, allowing FRE to succeed in loops
  where control flow m…
primer_glossary:
- term: FRE
  definition: Frequently Re-computed Expression, an optimization pass that identifies
    and hoists expressions computed multiple times within a loop to be computed only
    once outside the loop.
- term: Loop-invariant code motion (LICM)
  definition: An optimization that moves computations from inside a loop to the outside
    if their results do not change between loop iterations.
- term: PHI node
  definition: In SSA form, a special node that represents the merging of values from
    different control flow paths. It takes multiple arguments, each corresponding
    to a predecessor block.
- term: Alias analysis
  definition: Compiler analysis that determines whether different memory references
    (pointers or array accesses) might refer to the same memory location.
- term: tree-ssa-alias.cc
  definition: The GCC source file implementing alias analysis on the SSA intermediate
    representation.
- term: get_continuation_for_phi
  definition: A function within GCC's alias analysis that determines the correct value
    for a variable at a PHI node, considering potential aliasing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b4de9d73b47972bc89df288997c8f3a3862bc1b1
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's alias analysis that prevented loop-invariant code motion (LICM) from being applied effectively in certain loop scenarios. The problem occurred when translating aliased uses, causing the `get_continuation_for_phi` function to fail. By clearing the visited bitmap during translation and removing an unnecessary `abort_on_visited` flag, the analysis can now correctly traverse complex control flow, enabling more FRE optimizations.
