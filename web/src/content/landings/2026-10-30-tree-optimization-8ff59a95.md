---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- ssa
- reassociation
commit_hash: 8ff59a95b8a24f002072e5ea8797156edeccfb35
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix reassoc for abnormal SSA uses'
tldr: Reassociation pass now correctly handles abnormal SSA uses, preventing issues
  with out-of-SSA coalescing.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-reassoc` pass in GCC is responsible for reordering associative
  operations to improve code. This patch refines the `is_reassociable_op` predicate
  by introducing checks for abnormal SSA uses, specifically within `acceptable_pow_call`
  and `try_special_add_to_ops`. Abnormal SSA uses occur when an SSA value is used
  in a way that violates SSA properties (e.g., before its definition or in a complex
  control flow path). By ensuring these are not rescheduled, the pass avoids breaking
  the out-of-SSA (OOSSA) coalescing pass, which relies on well-formed SSA properties
  for efficient register…
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC that operates on the GIMPLE intermediate representation
    (often referred to as 'tree' representation) to perform various optimizations.
- term: Reassociation
  definition: An optimization technique that changes the grouping of associative operations
    (like addition or multiplication) without changing the result, potentially enabling
    other optimizations or improving instruction scheduling.
- term: SSA
  definition: Static Single Assignment. An intermediate representation property where
    each variable is assigned a value exactly once. This simplifies many analyses
    and optimizations.
- term: Out-of-SSA (OOSSA) coalescing
  definition: A compiler optimization pass that attempts to merge or 'coalesce' variables
    that are no longer strictly in SSA form, aiming to reduce register pressure and
    improve performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8ff59a95b8a24f002072e5ea8797156edeccfb35
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This commit enhances the tree reassociation optimization pass by adding checks to `is_reassociable_op`. These checks ensure that abnormal uses of Static Single Assignment (SSA) values are not rescheduled, which could otherwise break out-of-SSA coalescing. The changes include modifications to `acceptable_pow_call` and `try_special_add_to_ops` in `tree-ssa-reassoc.cc` and add a new test case.
