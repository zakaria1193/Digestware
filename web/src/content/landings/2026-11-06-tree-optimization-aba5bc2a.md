---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- alias analysis
- store merging
commit_hash: aba5bc2ace29a112f38597a3256ec8066a464ce3
source_type: github
author: Richard Biener
headline: Fix store-merging to disregard TBAA when disambiguating against calls
tldr: Improves store-merging by correctly ignoring TBAA when disambiguating memory
  operations against function calls.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR tree-optimization/128463 by refining how alias
  analysis interacts with store-merging, specifically concerning calls. The `pass_store_merging::terminate_all_aliasing_chains`
  and `stmts_may_clobber_ref_p` functions are simplified to ensure that TBAA information
  is not used when disambiguating whether a statement may clobber a reference against
  a function call. The rationale is that when sinking loads or stores across stores,
  TBAA should not be considered for this particular check, as it can lead to overly
  conservative aliasing assumptions and hinder store-merging.
primer_glossary:
- term: store-merging
  definition: An optimization pass in GCC that attempts to combine multiple store
    operations to the same memory location into a single store, reducing memory traffic.
- term: TBAA (Tree-based Alias Analysis)
  definition: A compiler technique that analyzes memory access patterns to determine
    if different memory references might point to the same location (aliasing). TBAA
    uses a tree-like structure to represent type information and resolve potential
    aliases.
- term: disambiguate
  definition: To determine whether two memory accesses are guaranteed to refer to
    different memory locations.
- term: sinking loads or stores
  definition: An optimization technique where memory read (load) or write (store)
    operations are moved to a later point in the program's execution, often across
    other operations, to enable other optimizations.
- term: gimple-ssa-store-merging.cc
  definition: A GCC source file implementing the store-merging optimization pass within
    the GIMPLE SSA (Static Single Assignment) intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aba5bc2ace29a112f38597a3256ec8066a464ce3
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This commit corrects an issue in GCC's store-merging optimization where the analysis failed to disregard Tree-based Alias Analysis (TBAA) information when disambiguating memory stores against function calls. This led to incorrect aliasing decisions. The fix modifies `stmt_may_clobber_ref_p_1` to ensure that TBAA is not used in these specific disambiguation scenarios, particularly when sinking loads or stores across stores. This improves the accuracy of alias analysis and store-merging, potentially enabling more aggressive optimizations.
