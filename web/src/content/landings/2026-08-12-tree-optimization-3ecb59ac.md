---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- dead code removal
- gcc
commit_hash: 3ecb59ac017be96590653ca16cb106c68580a15f
source_type: github
author: Kael Andrew Alonzo Franco
headline: Remove dead code from tree-ssa-math-opts.cc
tldr: Removes unreachable code in tree-ssa-math-opts.cc's arith_overflow_check_p function.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes dead code in tree-ssa-math-opts.cc related to COND_EXPR.
  Since COND_EXPR is always a SSA_NAME or a constant, the code checking for other
  possibilities was unreachable. This simplifies the `arith_overflow_check_p` function.
primer_glossary:
- term: COND_EXPR
  definition: 'A GCC internal representation for conditional expressions, often used
    in GIMPLE. It represents a ternary operation like `condition ? true_val : false_val`.'
- term: SSA_NAME
  definition: In GCC's Static Single Assignment (SSA) form, an SSA_NAME represents
    a variable that has been assigned a value exactly once. It's a core concept for
    many compiler optimizations.
- term: tree-ssa-math-opts.cc
  definition: A GCC source file containing optimizations related to arithmetic operations
    within the Static Single Assignment (SSA) form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3ecb59ac017be96590653ca16cb106c68580a15f
date: '2026-08-12'
is_stub: true
stub_reason: low_score
---

Dead code has been removed from tree-ssa-math-opts.cc, specifically within the arith_overflow_check_p function. This cleanup addresses a situation where COND_EXPR, which is always a SSA_NAME or a constant, made a portion of the code unreachable. The change was tested on x86_64-pc-linux-gnu.
