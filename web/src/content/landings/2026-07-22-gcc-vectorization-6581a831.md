---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- vectorization
- bugfix
- optimization
commit_hash: 6581a831fd548819097b1172b9488cd7c7d82a41
source_type: github
author: Richard Biener
headline: Fix SLP scheduling in-region check
tldr: Corrects the check for whether a statement is within the vector region during
  SLP scheduling.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch addresses a flaw in the `vect_schedule_slp_node` function
  within the SLP vectorizer in `tree-vect-slp.cc`. The function incorrectly determines
  if a statement belongs to the loop's vectorizable region by comparing statement
  UIDs with -1. This approach is flawed because UIDs are not guaranteed to be sequential
  or related to loop iterations in a way that -1 can serve as a sentinel value. The
  fix likely involves a more robust method of tracking statement boundaries or loop
  nesting levels to correctly identify statements that should be included in the SLP
  scheduling.
primer_glossary:
- term: SLP scheduling
  definition: Scalar and Vector Linking (SLP) is a loop vectorization technique that
    identifies opportunities to combine scalar operations within a basic block into
    a single vector instruction. SLP scheduling refers to the process of ordering
    these vector operations, considering dependencies and loop structure.
- term: vector region
  definition: In the context of loop vectorization, the 'vector region' refers to
    the part of the code (typically a loop body) that can be transformed to operate
    on multiple data elements simultaneously using vector instructions.
- term: UID
  definition: Unique Identifier. In GCC, UIDs are often assigned to various compiler
    internal nodes, such as statements or expressions, to provide a stable way to
    refer to them.
- term: loop vectorization
  definition: The process of transforming a loop to execute operations on multiple
    data elements in parallel using vector instructions, thereby improving performance
    for data-parallel computations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6581a831fd548819097b1172b9488cd7c7d82a41
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's SLP vectorization pass where the check for a statement being within the vector region was incorrect. Previously, it compared random statement UIDs against -1, which does not work reliably for loop vectorization. The fix ensures accurate identification of statements belonging to the vectorizable region.
