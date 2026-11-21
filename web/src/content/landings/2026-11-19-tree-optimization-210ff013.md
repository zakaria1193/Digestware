---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- TBAA
- compiler correctness
- PHI node
commit_hash: 210ff013a2e14b94d0b3e5e645ab6b69847e06ef
source_type: github
author: Kyrylo Tkachov
headline: Ensure initializers are TBAA-equivalent for looparound PHI nodes.
tldr: Fixes looparound PHI nodes to ensure initializers are TBAA-compatible.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-predcom.cc`, the `pcom_worker::valid_initializer_p` function
  previously accepted a preheader load feeding a looparound PHI as an initializer
  without verifying its TBAA equivalence to the chain root. This commit introduces
  `refs_tbaa_equivalent_p` to check this property symmetrically and requires its use
  in `valid_initializer_p`. This prevents the loop from using a stale initializer
  value if other memory accesses within the loop fall into different TBAA alias sets,
  correctly handling cases where the initializer and the chain root are not identical
  for TBAA.
primer_glossary:
- term: TBAA
  definition: Thread-Behavior-Access-Alias analysis, a compiler technique to determine
    if memory accesses can alias (refer to the same memory location), crucial for
    optimizations.
- term: PHI node
  definition: A control flow graph construct representing a value that can come from
    multiple predecessors; used to merge values from different code paths.
- term: looparound PHI
  definition: A specific type of PHI node used in loops where the value at the end
    of an iteration is used as the input for the next iteration's PHI node.
- term: alias set
  definition: A group of memory locations that the compiler assumes might be accessed
    by the same pointer, used in alias analysis.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/210ff013a2e14b94d0b3e5e645ab6b69847e06ef
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This change addresses a correctness issue in the `tree-predcom` optimization pass related to looparound PHI nodes and Thread-Behavior-Access-Alias (TBAA) analysis. Previously, the pass accepted an initializer for a looparound PHI that was not equivalent to the chain root for TBAA purposes. This could lead to incorrect program behavior, especially when memory locations are accessed through different alias sets within a loop. The fix ensures that the initializer and the chain root are confirmed to be TBAA-equivalent.
