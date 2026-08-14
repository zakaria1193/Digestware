---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- dead code
- tree-ssa
commit_hash: 864a0748f3e9fdd1505a26002bd348a95ed3076a
source_type: github
author: Kael Andrew Alonzo Franco
headline: Dead code removed from tree-ssa-forwprop.cc
tldr: Dead code eliminated from `tree-ssa-forwprop.cc` related to COND_EXPR handling.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes dead code from `simplify_builtin_call` in `tree-ssa-forwprop.cc`
  as per PR tree-optimization/120582. The condition `COND_EXPR` is always an `SSA_NAME`
  or a constant in this specific usage context, rendering the subsequent code path
  unreachable. Removing this dead code simplifies the pass and reduces potential for
  future maintenance errors.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where optimizations are performed on the 'tree' intermediate
    representation, which is a higher-level representation than RTL.
- term: SSA_NAME
  definition: Static Single Assignment name. A variable in the SSA form, where each
    variable is assigned exactly once.
- term: COND_EXPR
  definition: A GCC internal representation for a conditional expression (ternary
    operator or if-then-else structure).
- term: forward propagation
  definition: An optimization technique where values computed on one path are propagated
    forward to subsequent uses, potentially enabling further simplifications.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/864a0748f3e9fdd1505a26002bd348a95ed3076a
date: '2026-08-13'
is_stub: true
stub_reason: low_score
---

Dead code has been removed from the `tree-ssa-forwprop.cc` file. The eliminated code was deemed unnecessary because `COND_EXPR` in this context is always either an `SSA_NAME` or a constant, making the specific conditional logic redundant. This cleanup simplifies the compiler's internal representation and maintenance.
