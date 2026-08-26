---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- pointer arithmetic
- tree-optimization
commit_hash: c5d24759ba5e470f6fb75e251b84ec8fcb33db07
source_type: github
author: Richard Biener
headline: Revise (T *)(ptr - ptr_cst) pattern
tldr: Canonicalizes pointer arithmetic patterns for better optimization.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file is being updated to modify the canonicalization
  of the pattern `(T *)(ptr - ptr_cst)`. Previously, this pattern might have been
  avoided or handled indirectly. The revision applies the GENERIC simplification directly
  to the pattern, transforming it into `(T *)ptr p+ cst`. This change aims to ensure
  consistent and predictable representation of pointer arithmetic involving constant
  offsets, facilitating further optimizations.
primer_glossary:
- term: Pointer Arithmetic
  definition: Performing arithmetic operations (like addition or subtraction) on memory
    addresses stored in pointers. The result is a new memory address.
- term: Canonicalization
  definition: The process of transforming an expression or data structure into a standard
    or canonical form, simplifying comparisons and further processing.
- term: GENERIC
  definition: GCC's first intermediate representation (IR), which is language-independent
    and tree-based. It represents the structure of the code before lower-level optimizations.
- term: Tree Optimization
  definition: A phase of the compiler that operates on GCC's intermediate representations
    (like GENERIC or GIMPLE) to improve code performance or reduce its size.
- term: build_fold_addr_expr_with_type
  definition: An internal GCC function likely used to construct expressions representing
    memory addresses with associated types.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c5d24759ba5e470f6fb75e251b84ec8fcb33db07
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

This commit refines a GCC pattern for pointer arithmetic involving type casting. The pattern `(T *)(ptr - ptr_cst)` is now directly canonicalized to `(T *)ptr p+ cst`. This change simplifies the GENERIC representation, allowing subsequent optimizations to more effectively recognize and process pointer arithmetic. The pattern was originally introduced to avoid issues with `build_fold_addr_expr_with_type`, and this revision ensures more robust simplification.
