---
project: gcc
subsystem: gcc/match-sat-alu.pd
patch_id: null
tags:
- gcc
- optimization
- aarch64
- pattern matching
commit_hash: 1320bc377dab63d1c9a83662c49d01f3a166332c
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize X - MIN(X, Y) as saturating subtraction'
tldr: Enables recognizing 'X - MIN(X, Y)' as an unsigned saturating subtraction for
  better code generation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch enhances the `unsigned_integer_sat_sub` pattern in `match-sat-alu.pd`
  to recognize the expression form `X - MIN(X, Y)`. This expression is mathematically
  equivalent to an unsigned saturating subtraction. The optimization is gated on the
  `MIN` expression having a single use, ensuring that the `MIN` operation itself is
  removed. The SSA transform `tree-ssa-math-opts.cc` is updated to handle this new
  pattern, report successful replacements, and control the optimization pipeline by
  preventing further transforms after a match. This allows for more aggressive use
  of saturating instruction…
primer_glossary:
- term: match-sat-alu.pd
  definition: A GCC pattern file used to define patterns for recognizing and optimizing
    saturating arithmetic operations on ALUs (Arithmetic Logic Units).
- term: unsigned saturating subtraction
  definition: An arithmetic operation that subtracts two unsigned integers. If the
    result is less than zero, it clamps to zero; otherwise, it performs the subtraction.
    This prevents underflow.
- term: MIN(X, Y)
  definition: An expression that returns the smaller of two values, X and Y.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation used in
    compilers where every variable is assigned a value only once.
- term: tree-ssa-math-opts.cc
  definition: A GCC source file containing optimizations related to mathematical operations
    in the SSA (Static Single Assignment) form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1320bc377dab63d1c9a83662c49d01f3a166332c
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This commit introduces recognition for the pattern 'X - MIN(X, Y)' as an unsigned saturating subtraction in GCC. This form, equivalent to `X - (X < Y ? X : Y)`, can be efficiently translated into a single saturating subtraction instruction on some architectures. The change requires that the MIN operand has only one use to ensure its removal after replacement and updates related optimizers to correctly report replacements and prevent subsequent transformations. This leads to improved code for vector forms, replacing multiple instructions with a single UQSUB on AArch64.
