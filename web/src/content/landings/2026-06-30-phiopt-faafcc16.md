---
project: gcc
subsystem: phiopt
patch_id: null
tags:
- phiopt
- optimization
- memory management
- bugfix
commit_hash: faafcc163b261d640aad43dacc645fbc43db757c
source_type: github
author: Andrew Pinski
headline: 'phiopt: use remove_phi_node instead of gsi_remove for phi node [PR125961]'
tldr: GCC's phiopt pass now correctly reuses phi nodes for efficiency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit resolves PR tree-optimization/125961 by correcting the
  deallocation and reuse of phi nodes within the `tree-ssa-phiopt.cc` pass. It replaces
  calls to `gsi_remove` with `remove_phi_node` in `factor_out_conditional_operation`
  and `factor_out_conditional_load`. `gsi_remove` only removes the node from the basic
  block's instruction list but does not free its memory, leading to a leak until the
  next GC pass. `remove_phi_node` correctly handles deallocation and allows immediate
  reuse of the phi node, improving SSA form manipulation efficiency.
primer_general: In the GCC compiler, an optimization phase called `phiopt` deals with
  'phi nodes,' which are special constructs used in intermediate code to represent
  values that can come from different code paths. This commit fixes a bug where these
  phi nodes were not being properly cleaned up after use. Instead of being immediately
  discarded and made available for reuse, they were temporarily kept in memory, leading
  to a form of memory leak during compilation. The fix ensures that phi nodes are
  correctly managed, allowing them to be reused more efficiently, which can lead to
  faster compilation times for complex code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/faafcc163b261d640aad43dacc645fbc43db757c
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

The `phiopt` optimization pass in GCC has been corrected to properly reuse phi nodes, preventing memory leaks and improving efficiency. Previously, it used `gsi_remove` which did not immediately free the phi node, causing it to be temporarily leaked until the next garbage collection. This commit replaces `gsi_remove` with `remove_phi_node` in two critical areas of `phiopt`. This ensures that phi nodes are correctly deallocated and can be immediately reused, addressing PR tree-optimization/125961.
