---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- alias analysis
commit_hash: 3a4787033e4b5dea2d1f7a6b30d4c85a00b7b91d
source_type: github
author: Richard Biener
headline: FRE optimization improved by avoiding duplicate PHI argument processing
tldr: Fixes a bug in FRE optimization where duplicate PHI arguments caused redundant
  work and potential failures in alias analysis.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit, related to PR127693, refines the `get_continuation_for_phi`
  function in `tree-ssa-alias.cc`. When processing PHI arguments, especially in the
  context of walking a backedge with a translated reference (where `abort_on_visited`
  is true), duplicate arguments could lead to unnecessary re-computation or premature
  aborts. The fix introduces sorting of PHI arguments and processing unique pairs,
  using a new `cmp_intpair` helper, to prevent redundant work and ensure correctness.
primer_glossary:
- term: FRE
  definition: Frequently Re-computed Expression, an optimization pass that identifies
    and hoists expressions computed multiple times within a loop to be computed only
    once outside the loop.
- term: PHI node
  definition: In SSA form, a special node that represents the merging of values from
    different control flow paths. It takes multiple arguments, each corresponding
    to a predecessor block.
- term: SSA (Static Single Assignment)
  definition: An intermediate representation form used by compilers where each variable
    is assigned a value exactly once. This simplifies many data-flow analyses and
    optimizations.
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
url: https://github.com/gcc-mirror/gcc/commit/3a4787033e4b5dea2d1f7a6b30d4c85a00b7b91d
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This commit is part of a fix for missed FRE optimizations in loops (PR127693). It addresses an issue where `get_continuation_for_phi` was called with duplicate PHI arguments when walking a backedge with a translated reference. By sorting PHI arguments and processing only unique ones, this patch avoids redundant work and prevents the `abort_on_visited` flag from tripping incorrectly, thereby enabling more FRE optimizations.
