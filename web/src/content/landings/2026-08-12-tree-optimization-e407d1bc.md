---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- dead code
- tree-ssa
commit_hash: e407d1bc83ae75d8a4ca0b0c04dcf0d843ce1d7a
source_type: github
author: Kael Andrew Alonzo Franco
headline: Dead code removed from gimple-ssa-nonnull-compare.cc
tldr: Dead code eliminated from `gimple-ssa-nonnull-compare.cc` related to COND_EXPR
  handling.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes dead code from the `do_warn_nonnull_compare` function
  in `gimple-ssa-nonnull-compare.cc` as per PR tree-optimization/120580. The `COND_EXPR`
  in this context is always an `SSA_NAME` or a constant, rendering the subsequent
  code unreachable. This removes dead code from the non-null comparison optimization
  pass.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where optimizations are performed on the 'tree' intermediate
    representation, which is a higher-level representation than RTL.
- term: gimple-ssa
  definition: GIMPLE Static Single Assignment. An intermediate representation used
    in GCC, based on SSA form, designed for easier optimization.
- term: COND_EXPR
  definition: A GCC internal representation for a conditional expression (ternary
    operator or if-then-else structure).
- term: SSA_NAME
  definition: Static Single Assignment name. A variable in the SSA form, where each
    variable is assigned exactly once.
- term: non-null comparison
  definition: Analysis performed by the compiler to determine if a pointer is guaranteed
    to be non-null, often used to optimize code that dereferences pointers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e407d1bc83ae75d8a4ca0b0c04dcf0d843ce1d7a
date: '2026-08-12'
is_stub: true
stub_reason: low_score
---

Redundant code has been removed from `gimple-ssa-nonnull-compare.cc`. This cleanup targets logic that was unreachable because `COND_EXPR` in this context is always either an `SSA_NAME` or a constant, making the specific code path unnecessary. The change simplifies the compiler's null pointer comparison analysis.
