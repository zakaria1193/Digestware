---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- SLP
commit_hash: 5e63fb58f84e3ce19cb336710f69094ecbd4b63d
source_type: github
author: Richard Biener
headline: Vector placement improved for live lane extracts
tldr: Vectorizer pre-computes insertion points for SLP nodes, improving feasibility
  checks for live scalar lane extractions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors `tree-vect-slp.cc` to improve the calculation
  of live lane extraction feasibility. It introduces pre-scheduling of SLP nodes to
  determine a more accurate insertion point, which is then used in `vect_bb_slp_mark_live_stmts`
  to refine the vector statement placement constraint. This addresses conservative
  assumptions made previously. The challenges with re-using this pre-schedule for
  actual insertion, such as iterator invalidation due to statement elision, are noted.
  The new `_slp_tree::si` member stores the pre-computed insertion point.
primer_glossary:
- term: SLP
  definition: Superword Level Parallelism, a compiler optimization technique that
    finds instructions operating on scalars that can be vectorized to operate on multiple
    data elements simultaneously.
- term: lane extraction
  definition: The process of extracting a single data element from a vector register.
- term: vector statement placement
  definition: Determining the optimal location within the code to insert vectorized
    instructions.
- term: GIMPLE
  definition: GNU Intermediate Representation, a three-address code form used by GCC
    after initial parsing and before final machine code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e63fb58f84e3ce19cb336710f69094ecbd4b63d
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

This commit improves the vectorizer's ability to determine the feasibility of placing lane extractions for live scalar values. It achieves this by pre-computing an insertion place for all SLP nodes, which is then used to refine the feasibility computation. While re-using this computation for actual insertion is currently problematic due to potential scalar statement elision, this pre-computation validates earlier scheduling decisions and enhances the accuracy of live lane extract placement.
