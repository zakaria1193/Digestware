---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- bugfix
commit_hash: def63f7c26207e4dfefcf5e92c07ea2582474dc5
source_type: github
author: Richard Biener
headline: Fix uninitialized read of bb_to_rpo in Sccvn
tldr: Corrects an uninitialized read in the Sccvn pass by conservatively handling
  out-of-region edges as backedges.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Sccvn pass in GCC computes the Strongly Connected Components (SCCs)
  of the Value Numbering (VN) graph to optimize loops. This patch fixes a bug in the
  RPO (Reverse Postorder) calculation within Sccvn. The `vn_is_backedge` function
  previously mishandled edges that exited the processed region, leading to an uninitialized
  read of `bb_to_rpo`. The fix ensures that out-of-region edges are conservatively
  treated as backedges, resolving the issue.
primer_glossary:
- term: Sccvn
  definition: A GCC compiler pass that identifies Strongly Connected Components (SCCs)
    in the Value Numbering (VN) graph, primarily used for loop optimizations.
- term: RPO
  definition: Reverse Postorder traversal of a control flow graph. It's an ordering
    of basic blocks used in various compiler optimizations.
- term: BB
  definition: Basic Block. A sequence of instructions with a single entry point and
    a single exit point.
- term: Value Numbering (VN)
  definition: An optimization technique that assigns unique numbers to expressions
    with the same value, allowing the compiler to identify and eliminate redundant
    computations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/def63f7c26207e4dfefcf5e92c07ea2582474dc5
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This change addresses an uninitialized read in the tree-ssa-sccvn.cc file, specifically within the `walk_non_aliased_vuses` function. The issue arose because the walk could proceed outside the intended region, leading to invalid backedge queries. The fix introduces a local BB flag to mark regions and treats edges leaving the region as backedges, except for the entry edge, thus preventing the uninitialized read and ensuring correct RPO computation.
