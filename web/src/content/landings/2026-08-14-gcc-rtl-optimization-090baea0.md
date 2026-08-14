---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- optimization
- rtl
- vectorization
- dead code elimination
commit_hash: 090baea02d768ff884d1b326d6bf7d57cfcc1231
source_type: github
author: Jeff Law
headline: Ext-dce handles vector modes more conservatively
tldr: Extended dead code elimination now conservatively handles vector modes to prevent
  incorrect removal of code.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit revises vector mode handling in `ext-dce`, specifically
  addressing PR rtl-optimization/126426. The issue stemmed from `GET_MODE_INNER` incorrectly
  reporting the liveness of bits for vector types (e.g., V2HI). Instead of `0xffff`,
  it should consider all bits (e.g., `0xffffffff`). The fix involves a more conservative
  approach, particularly in `carry_backpropagate`, where vector modes are currently
  handled by broadcasting element liveness across the vector, avoiding incorrect dead
  code elimination that could remove extensions.
primer_glossary:
- term: ext-dce
  definition: Extended Dead Code Elimination. A compiler optimization pass that removes
    code that does not affect the program's outcome.
- term: vector mode
  definition: A data type in GCC's RTL (Register Transfer Language) that represents
    multiple elements of a smaller data type packed together, often used for SIMD
    operations.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used by GCC
    to represent program code during optimization.
- term: liveness analysis
  definition: A data-flow analysis technique that determines which variables hold
    values that might be used in the future. This information is used for optimizations
    like dead code elimination and register allocation.
- term: GET_MODE_INNER
  definition: A GCC internal macro used to get the mode of the inner elements of a
    vector or complex type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/090baea02d768ff884d1b326d6bf7d57cfcc1231
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

The extended dead code elimination (ext-dce) pass has been updated to handle vector modes more conservatively. A previous flaw in determining live bits for vector types led to the incorrect removal of code, specifically extensions, because the compiler wrongly assumed certain bits were never read. This change ensures more accurate liveness analysis for vector operations, preventing such optimizations from removing necessary code.
