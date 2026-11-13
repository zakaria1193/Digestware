---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- SLP
- GCC
commit_hash: a1fc780b5acca7c6dd9322a450953a434f0c418c
source_type: github
author: Richard Biener
headline: 'tree-optimization: Refine PR127811 fix for extern vector defs'
tldr: Improves handling of external vector definitions in SLP vectorization.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp_node` function in `tree-vect-slp.cc` is modified
  to relocate the fixup logic for extern vector definitions. This change aims to integrate
  it more correctly within the SLP vectorization pass, particularly concerning internal
  permute nodes. Additionally, this commit ensures that a statement-based dominance
  check, which failed in the test case for PR128347, is now correctly handled, preventing
  incorrect vectorization decisions.
primer_glossary:
- term: SLP vectorization
  definition: Superword-Level Parallelism vectorization, a compiler optimization that
    identifies opportunities to perform the same operation on multiple data items
    simultaneously using SIMD instructions.
- term: dominance check
  definition: In compiler theory, a check to determine if one part of the code always
    executes before another part.
- term: permute node
  definition: An internal representation in the compiler's intermediate language that
    signifies a data reordering or permutation operation, often used in vectorization.
- term: extern vector def
  definition: A definition related to external vector types or variables within the
    compiler's internal representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a1fc780b5acca7c6dd9322a450953a434f0c418c
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit refines the fix for PR127811 by moving the handling of extern vector definitions within internal permute nodes to a more appropriate location in the SLP (Short for 'Superword-Level Parallelism') vectorization process. It also addresses a failing statement-based dominance check identified in PR128347, ensuring more robust vectorization.
