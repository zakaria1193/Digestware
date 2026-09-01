---
project: gcc
subsystem: tree-ssa-forwprop
patch_id: null
tags:
- optimization
- bugfix
- complex numbers
commit_hash: 3f527492135e4bb5d89c24636c89f4d45617164e
source_type: github
author: Daniel Barboza
headline: Do not handle COMPLEX types in simplify_phi_result_movdiv.
tldr: Fixes ICE when optimizing division/modulo on complex numbers.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_phi_result_movdiv` function in `tree-ssa-forwprop.cc`
  handles specific GIMPLE statements involving PHI nodes and division/modulo operations.
  An earlier commit (not provided here) introduced logic that inadvertently triggered
  an integer constant check even when the operands were COMPLEX types. This patch
  adds an `INTEGRAL_TYPE_P` check to filter out complex types, preventing the ICE
  and ensuring the transformation is only applied where it's mathematically sound.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. An unexpected condition encountered by the
    compiler that prevents it from completing the compilation process. It typically
    indicates a bug in the compiler itself.
- term: tree-ssa-forwprop
  definition: The forward propagation pass within GCC's tree-ssa optimization framework.
    It attempts to propagate constants and simplify expressions by moving computations
    closer to their uses.
- term: PHI node
  definition: In SSA form, a PHI node is a special construct used to merge values
    from different control flow paths. It selects one of its arguments based on which
    predecessor block was taken.
- term: COMPLEX types
  definition: Data types representing complex numbers, which consist of a real part
    and an imaginary part. Compilers may have specific intrinsic functions or support
    for arithmetic operations on these types.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3f527492135e4bb5d89c24636c89f4d45617164e
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit prevents an ICE (Internal Compiler Error) in the `simplify_phi_result_movdiv` function within the tree-ssa forward propagation pass. The function was incorrectly attempting to process COMPLEX types for division or modulo operations, which are not designed for them. The fix adds a check to ensure operands are integral types before applying the transformation, filtering out complex types.
