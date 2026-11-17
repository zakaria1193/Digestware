---
project: gcc
subsystem: gimple-predicate-analysis
patch_id: null
tags:
- optimization
- bugfix
- gimple
commit_hash: 3e468676c402207ad0e14831084f8dfcdfa61883
source_type: github
author: Sendao Yan
headline: Fix shallow copy of pred_chain in predicate analysis
tldr: Corrects predicate analysis to avoid dangling pointers and double frees from
  shallow copies.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `predicate::simplify_4`, a shallow copy of `m_preds[i]` (a `pred_chain`,
  which is a `vec`) was created. The default copy constructor for `vec` performs a
  shallow copy, sharing the pointer to the underlying elements. Releasing this copy
  frees the buffer, leaving `m_preds[i]` dangling. The subsequent cleanup loop then
  accesses this dangling pointer. The fix ensures `simplify_4` uses the original chain
  and `simplify` correctly handles constant folding of predicates by setting `m_cval`
  to avoid issues when disjunctions become TRUE or contradictions.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation used for optimization.
- term: predicate analysis
  definition: An analysis pass in GCC that determines properties or conditions related
    to program execution, often used for optimization.
- term: pred_chain
  definition: A data structure within GCC's predicate analysis that likely represents
    a chain or sequence of predicates.
- term: NULL_TREE
  definition: A special value in GCC's internal representation indicating an empty
    or absent tree node.
- term: DCE
  definition: Dead Code Elimination, an optimization pass that removes code that does
    not affect the program's output.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3e468676c402207ad0e14831084f8dfcdfa61883
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's `gimple-predicate-analysis.cc` where a shallow copy of a `pred_chain` was causing issues. The copy constructor for `pred_chain` shares the pointer to its elements, leading to a dangling pointer when the copy is released. This could result in a double free or reading from freed memory. The fix modifies `simplify_4` to refer to the chain in place and adjusts `simplify` to correctly set the `m_cval` when a predicate folds to a constant value, resolving latent bugs exposed by recent changes.
