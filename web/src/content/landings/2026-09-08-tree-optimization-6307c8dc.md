---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- compiler-error
commit_hash: 6307c8dcb33a391daeafd03e7239f41affde5648
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix ICE in vect_create_constant_vectors'
tldr: Corrects an Internal Compiler Error in vectorization by fixing a node checking
  mismatch.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit fixes an ICE in `vect_slp_analyze_node_operations` (PR
  tree-optimization/127245) by ensuring the correct node is checked. The prior incorrect
  node check, an 'oops', led to a later ICE. The fix adds a check for `vect_get_num_copies_for_invariant`
  on the child node, resolving the mismatch.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A fatal error during compilation that indicates
    a bug within the compiler itself.
- term: vectorization
  definition: An optimization technique that transforms scalar code into vector code,
    allowing the processor to perform the same operation on multiple data elements
    simultaneously.
- term: SLP
  definition: Superword-Level Parallelism. An optimization technique that identifies
    and vectorizes sequences of independent scalar operations that operate on different
    data elements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6307c8dcb33a391daeafd03e7239f41affde5648
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

An Internal Compiler Error (ICE) occurring within the `vect_create_constant_vectors` function has been resolved. The issue stemmed from a mismatch in the node being checked within `vect_slp_analyze_node_operations`, leading to subsequent errors. This fix ensures the correct node is evaluated, preventing the ICE and improving the reliability of the vectorization pass.
