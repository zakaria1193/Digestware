---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- middle-end
commit_hash: 1bcce941ebbb9ad97997a86432da88c8a9117d4b
source_type: github
author: Kyrylo Tkachov
headline: Use conservative store semantics for MEM_NOTRAP
tldr: Ensures correct non-trapping information by defaulting to conservative store
  semantics and re-evaluating loads.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `set_mem_attributes` function in `emit-rtl.cc` previously determined
  `MEM_NOTRAP` solely based on `tree_could_trap_p`, which implies a load. This commit
  introduces `MAY_STORE_P` and uses `lhs_could_trap_p` when `MAY_STORE_P` is true,
  making the attribute setting more robust for stores. `MAY_STORE_P` defaults to true
  to prevent unsafe `MEM_NOTRAP` claims. For loads expanded with `EXPAND_MEMORY` or
  `EXPAND_STACK_PARM`, `MEM_NOTRAP` is recomputed later to preserve precision.
primer_glossary:
- term: MEM_NOTRAP
  definition: A flag indicating that a memory access is guaranteed not to trap (e.g.,
    cause a segmentation fault or other exception). This allows the compiler to perform
    more aggressive optimizations, such as reordering or eliminating the access.
- term: lhs_could_trap_p
  definition: A function that checks if the left-hand side (LHS) of an expression
    or assignment could potentially trap. This is used to determine if a memory access
    might cause an exception.
- term: tree_could_trap_p
  definition: A GCC internal function that determines if a tree node (representing
    an expression or operation) could potentially cause a trap or exception during
    evaluation.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used internally
    by GCC to represent operations on registers and memory before final machine code
    generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1bcce941ebbb9ad97997a86432da88c8a9117d4b
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This commit refines how the `MEM_NOTRAP` attribute is handled, particularly for stores. Previously, `set_mem_attributes` derived `MEM_NOTRAP` from `tree_could_trap_p`, which describes loads. This could incorrectly mark stores to unwritable memory as non-trapping. The changes introduce `MAY_STORE_P` and use `lhs_could_trap_p` for stores, defaulting `MAY_STORE_P` to true. This makes the handling more conservative for stores and ensures that loads expanded with non-normal modifiers have their `MEM_NOTRAP` recomputed later.
