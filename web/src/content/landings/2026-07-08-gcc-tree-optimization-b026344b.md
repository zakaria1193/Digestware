---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- vectorization
- optimization
commit_hash: b026344b5e7bbffc9433e16ebb84ca7e14957c6a
source_type: github
author: Richard Biener
headline: 'GCC: Remove redundant group_size argument from vectorization APIs'
tldr: Vectorization APIs now infer group size from statement vector length, simplifying
  internal data structures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_build_slp_tree*` family of APIs in `tree-vect-slp.cc` previously
  accepted a `group_size` argument. This commit eliminates it, as the information
  is derivable from the `stmt->get_vector_length()`. This refactoring aims to reduce
  redundancy and potentially simplify the SLP (Straight-Line-Progress) vectorizer's
  internal state management.
primer_glossary:
- term: SLP vectorizer
  definition: A compiler optimization pass that identifies sequences of identical
    operations in straight-line code (no branches) and replaces them with a single
    instruction that operates on multiple data elements simultaneously (vectorization).
- term: statement vector length
  definition: Refers to the number of data elements that a single instruction can
    operate on in a vectorized loop or basic block.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b026344b5e7bbffc9433e16ebb84ca7e14957c6a
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit removes the `group_size` argument from several internal vectorization helper functions (e.g., `vect_build_slp_tree*`). This argument was redundant because the statement vector length already implicitly provides this information. The change simplifies the internal data structures used by the vectorizer and improves code clarity.
