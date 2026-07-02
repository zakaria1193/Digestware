---
project: gcc
subsystem: tree-vrp
patch_id: null
tags:
- optimization
- warning
- strict overflow
- value range propagation
commit_hash: 8c6adf1ab1c9a3f8a95773273cbdd1e9fdd3f264
source_type: github
author: Daniel Barboza
headline: Remove compare_values_warnv function
tldr: The compare_values_warnv function, along with strict overflow warning logic,
  has been removed from the tree-vrp module.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes ``compare_values_warnv`` from ``tree-vrp.cc`` and
  updates its callers (``compare_values`` and ``test_for_singularity``) to remove
  the now-defunct strict overflow checking.  tree-vrp performs value range propagation
  on the GCC IR (``tree``) to enable optimisations. The overflow checking logic was
  triggered during value comparison. This change continues the cleanup of ``Wstrict-overflow``.
primer_general: Value range propagation (VRP) is a compiler optimization technique
  used to determine the possible range of values a variable can hold during program
  execution. This information allows the compiler to perform further optimizations,
  such as dead code elimination or simplification of expressions. This commit removes
  a function related to value comparison and strict overflow warnings within the VRP
  module, as part of a broader effort to deprecate the ``-Wstrict-overflow`` warning.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8c6adf1ab1c9a3f8a95773273cbdd1e9fdd3f264
date: '2026-05-25'
is_stub: false
---

The ``compare_values_warnv`` function has been removed from the tree-vrp module. This function was previously responsible for comparing values and issuing strict overflow warnings. The change also modifies related functions like ``compare_values`` and ``test_for_singularity`` to remove the warning logic. This is part of a larger effort to deprecate the ``-Wstrict-overflow`` warning, which helps simplify the code base.
