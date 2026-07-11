---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- vector
- aarch64
- pattern matching
commit_hash: 0ac16fdbee1509efe9cbdee89ae9fa7be9b87e78
source_type: github
author: Pengfei Li
headline: 'match.pd: Eliminate dead operand in vector permute and insert patterns'
tldr: Optimizes vector permute and insert operations on AArch64 by avoiding unnecessary
  zero-vector materialization.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change affects `gcc/match.pd` by introducing a new pattern for
  vector `VEC_PERM_EXPR` followed by `BIT_INSERT_EXPR`. It targets cases where the
  `VEC_PERM_EXPR`'s result is effectively a permutation of a single input vector,
  often used to create space for an insertion. The new pattern detects when the second
  operand of `VEC_PERM_EXPR` (the permutation mask) is effectively unused, and if
  the permutation is still valid, it replaces the unused input vector operand with
  itself. This specifically avoids materializing placeholder zero vectors for the
  permute operation on targets like AArch64, l…
primer_glossary:
- term: VEC_PERM_EXPR
  definition: A GIMPLE expression representing a vector permutation. It rearranges
    elements within a vector or combines elements from multiple vectors according
    to a specified mask.
- term: BIT_INSERT_EXPR
  definition: A GIMPLE expression that inserts bits from a source into a destination
    vector at a specified position. This is often used for manipulating individual
    elements or sub-elements within vectors.
- term: match.pd
  definition: A file containing pattern matching definitions used by GCC's internal
    representation (RTL) to optimize code. These patterns describe common instruction
    sequences and allow the compiler to replace them with more efficient ones.
- term: AArch64
  definition: The 64-bit ARM architecture, widely used in mobile devices and increasingly
    in servers and desktops. GCC supports code generation for this architecture.
- term: GIMPLE
  definition: GCC's internal representation (IR) used between the front-end and the
    RTL optimizer. It's a three-address code form designed for easier optimization
    analysis.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ac16fdbee1509efe9cbdee89ae9fa7be9b87e78
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This commit optimizes vector permute and insert operations, particularly for AArch64, by eliminating a dead operand. When a vector is shifted and a new element is inserted, the previous GCC code generated an unnecessary zero vector. The new `match.pd` pattern detects when the permute's result only depends on one source operand and replaces the unused operand with that source, avoiding the creation of a temporary zero vector and producing more efficient machine code.
