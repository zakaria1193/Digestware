---
project: gcc
subsystem: gcc/widening_mul
patch_id: null
tags:
- optimization
- gcc
- compiler bug
- integer
commit_hash: a49c114c7b3edd33a6ff2e50e6276ca1fbe8ad83
source_type: github
author: Jakub Jelinek
headline: Fixes ICE in widening multiplication optimization.
tldr: Prevents compiler crash when optimizing certain vector-related multiplication
  checks.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `widening_mul` optimization pass, specifically within `maybe_optimize_guarding_check`
  called by `match_arith_overflow`, was susceptible to an ICE. This was due to repeated
  calls to `mul_stmts.quick_push` on a fixed-size `auto_vec`, leading to buffer overflow
  when the function was invoked more than twice in a loop context. The fix uses `safe_push`
  to ensure that additions to `mul_stmts` are bounds-checked, preventing the overflow
  and ICE.
primer_glossary:
- term: widening_mul
  definition: An optimization that detects and potentially replaces arithmetic operations
    with wider types to avoid overflow, or to optimize checks related to such operations.
- term: ICE
  definition: Internal Compiler Error, a crash within the compiler itself, typically
    due to a bug in the compiler's logic.
- term: maybe_optimize_guarding_check
  definition: A function within GCC's tree-optimization passes that checks and potentially
    optimizes code related to guarding arithmetic operations.
- term: auto_vec
  definition: A dynamic array or vector class in GCC that manages its own memory,
    similar to std::vector in C++.
- term: quick_push
  definition: A method for adding an element to a container (like auto_vec) that assumes
    there is enough space and does not perform bounds checking, for performance.
- term: safe_push
  definition: A method for adding an element to a container that includes bounds checking
    to prevent buffer overflows.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a49c114c7b3edd33a6ff2e50e6276ca1fbe8ad83
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

An Integer Compiler (ICE) in the `maybe_optimize_guarding_check` function, used during widening multiplication optimizations, has been fixed. The issue occurred when the function was called multiple times within a loop, leading to a buffer overflow in a vector used to store multiplication statements. The fix replaces `quick_push` with `safe_push` for adding elements to this vector, preventing the overflow and subsequent crash.
