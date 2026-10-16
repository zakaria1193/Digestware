---
project: gcc
subsystem: optabs
patch_id: null
tags:
- vectorization
- optabs
- gcc
- bugfix
commit_hash: caab3df20accebf99913287c148ed64ea809fb9b
source_type: github
author: Igor Shevlyakov
headline: 'optabs: Fix constant permute selectors for wide inputs'
tldr: Corrects vector permute index generation for inputs wider than the result.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `expand_vec_perm_const` function in `optabs.cc` previously constructed
  permute indices based on the *result* mode's element count. When `VEC_PERM_EXPR`
  inputs were wider than the result, and a constant selector was used, indices beyond
  `2 * result_length` would incorrectly wrap into the first input. This commit modifies
  the index generation to use the *input* mode's element count, aligning with how
  `tree_to_vec_perm_indices` operates and fixing erroneous code generation for widening
  permutes.
primer_glossary:
- term: optabs
  definition: A subsystem in GCC that maintains tables of operations (op-tables) for
    different machine modes and targets, used for instruction selection.
- term: VEC_PERM_EXPR
  definition: A GCC intermediate representation (tree) representing a vector permute
    operation, which rearranges elements within vectors.
- term: vector permute
  definition: An operation that rearranges elements within one or more vectors according
    to a specified index set.
- term: selector
  definition: In the context of `VEC_PERM_EXPR`, a set of indices that dictate how
    elements from input vectors are combined to form the output vector.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/caab3df20accebf99913287c148ed64ea809fb9b
date: '2026-10-07'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in `optabs.cc` where constant vector permute operations with inputs wider than the result mode were generating incorrect selectors. The issue caused indices to wrap around, leading to wrong code generation. The fix ensures that permute indices are built using the input mode's element count, preventing incorrect behavior and improving the reliability of vector permute operations, especially for targets that might support such widening operations.
