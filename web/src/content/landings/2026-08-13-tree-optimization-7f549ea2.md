---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- dead code removal
- gcc
commit_hash: 7f549ea2b47a709e9966ce608b92a44f3d2c2353
source_type: github
author: Kael Andrew Alonzo Franco
headline: Remove dead code from gimple.cc
tldr: Removes unreachable code in gimple.cc related to COND_EXPR.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes dead code in gimple.cc related to COND_EXPR. Since
  COND_EXPR is always a SSA_NAME or a constant, the code checking for other possibilities
  was unreachable. This simplifies the `gimple_could_trap_p_1` function.
primer_glossary:
- term: COND_EXPR
  definition: 'A GCC internal representation for conditional expressions, often used
    in GIMPLE. It represents a ternary operation like `condition ? true_val : false_val`.'
- term: SSA_NAME
  definition: In GCC's Static Single Assignment (SSA) form, an SSA_NAME represents
    a variable that has been assigned a value exactly once. It's a core concept for
    many compiler optimizations.
- term: GIMPLE
  definition: GCC's three-address intermediate representation. It's designed to be
    simpler and easier to optimize than the earlier RTL (Register Transfer Language).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f549ea2b47a709e9966ce608b92a44f3d2c2353
date: '2026-08-13'
is_stub: true
stub_reason: low_score
---

Dead code has been removed from gimple.cc, specifically within the gimple_could_trap_p_1 function. This cleanup addresses a situation where COND_EXPR, which is always a SSA_NAME or a constant, made a portion of the code unreachable. The change was tested on x86_64-pc-linux-gnu.
