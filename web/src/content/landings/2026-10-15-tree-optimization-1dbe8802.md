---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- RISC-V
- bugfix
commit_hash: 1dbe8802bdd361e2274d1c0bec5e75e09ad0bc64
source_type: github
author: Kyrylo Tkachov
headline: Correct signed saturating add pattern for X + IMM
tldr: Fixes incorrect folding of signed saturating add operations involving immediate
  values.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `signed_integer_sat_add` pattern in `match-sat-alu.pd` incorrectly
  folded `T SUM = (T)((UT)X + (UT)IMM)` when `(X ^ SUM) & (X ^ C3) < 0`. This condition
  was meant to check if X and IMM have opposite signs, but the `C3 == ~IMM` equality
  was insufficient. The fix replaces it with a direct comparison of the sign bits
  of the two constants, improving correctness for saturating add operations and fixing
  issues in the vectorizer.
primer_glossary:
- term: signed saturating add
  definition: An arithmetic operation that adds two signed numbers. If the result
    exceeds the maximum representable value for the type, it is clamped to the maximum;
    if it falls below the minimum, it is clamped to the minimum. This is also known
    as saturation arithmetic.
- term: vectorizer
  definition: A compiler component that transforms code to use SIMD (Single Instruction,
    Multiple Data) instructions, allowing a single operation to be performed on multiple
    data elements simultaneously for performance gains.
- term: immediate value
  definition: A constant value embedded directly within an instruction, rather than
    being fetched from memory or a register.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1dbe8802bdd361e2274d1c0bec5e75e09ad0bc64
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

A pattern in `match-sat-alu.pd` that folds signed saturating additions of a register to an immediate value has been corrected. The previous check for operand signs was too permissive, leading to incorrect results for certain inputs, notably with the vectorizer. The fix ensures the pattern correctly identifies when the immediate value has the opposite sign of the register operand's sign bit, preventing incorrect saturations.
