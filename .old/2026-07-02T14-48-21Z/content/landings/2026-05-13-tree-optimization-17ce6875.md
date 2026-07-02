---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- alignment
- tree-ssa
commit_hash: 17ce6875a08253fb02580bd365a4528e9225efb9
source_type: github
author: Richard Biener
headline: Preserve alignment of access during address forwarding.
tldr: GCC now preserves the alignment of memory accesses when forwarding addresses
  during tree optimization.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The tree-ssa-forwprop pass in GCC optimizes expressions by propagating
  address expressions. This commit fixes an issue where the alignment of the original
  memory access was not preserved during address forwarding. The fix ensures that
  the correct alignment is maintained, preventing potential misalignments. The relevant
  code changes are in `tree-ssa-forwprop.cc` within the `forward_propagate_addr_expr_1`
  function.
primer_general: GCC's tree optimization phase aims to improve the efficiency of generated
  code by transforming the program's abstract syntax tree (AST). Address forwarding
  is a technique where the compiler replaces a memory access with a direct pointer
  to the data. Memory alignment is crucial for performance; misaligned accesses can
  lead to significant slowdowns, especially on architectures that penalize them. This
  change ensures that the compiler maintains correct memory alignment during address
  forwarding, leading to more efficient code execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/17ce6875a08253fb02580bd365a4528e9225efb9
date: '2026-05-13'
is_stub: false
---

GCC's tree-ssa-forwprop pass now preserves the alignment of memory accesses when forwarding addresses. This prevents the optimizer from picking up the alignment of parts of the forwarded address instead of the original access. A new test case, gcc.dg/pr125206.c, validates this fix.
