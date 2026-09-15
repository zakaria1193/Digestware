---
project: gcc
subsystem: gcc/match-sat-alu.pd
patch_id: null
tags:
- gcc
- optimization
- aarch64
- pattern matching
commit_hash: 2ed77dddba2e7f2d4e45ee8606e9b22acb6fb1f3
source_type: github
author: Kyrylo Tkachov
headline: 'match-sat-alu.pd: Recognize more unsigned saturating subtraction forms'
tldr: Improves recognition of unsigned saturating subtractions with swapped operands
  or reversed conditional arms.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match-sat-alu.pd` file contains patterns for recognizing and optimizing
  arithmetic operations, particularly saturating ones. This patch adds recognition
  for unsigned saturating subtraction (`unsigned_integer_sat_sub`) when the comparison
  operands are commuted (e.g., `a < b` vs `b < a`) or when the conditional branches
  are reversed. This is achieved by modifying the pattern definitions to accept these
  variations, enabling the backend to generate more efficient code by utilizing instructions
  like AArch64's `subs` and `csel` or `UQSUB`.
primer_glossary:
- term: match-sat-alu.pd
  definition: A GCC pattern file used to define patterns for recognizing and optimizing
    saturating arithmetic operations on ALUs (Arithmetic Logic Units).
- term: unsigned saturating subtraction
  definition: An arithmetic operation that subtracts two unsigned integers. If the
    result is less than zero, it clamps to zero; otherwise, it performs the subtraction.
    This prevents underflow.
- term: commuted operands
  definition: When the order of operands in an operation or comparison is swapped
    (e.g., `a - b` becomes `b - a`, or `a < b` becomes `b < a`).
- term: conditional select (CSEL)
  definition: An instruction that selects between two source operands based on a condition
    code and writes the result to a destination register.
- term: UQSUB
  definition: An AArch64 instruction for unsigned saturating subtraction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2ed77dddba2e7f2d4e45ee8606e9b22acb6fb1f3
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This commit enhances the recognition of unsigned saturating subtraction operations in GCC. It now correctly identifies forms where the comparison operands or conditional arms are reversed, such as 'B < A ? A - B : 0' or 'A < B ? 0 : A - B'. This allows the compiler to apply more efficient instructions, like AArch64's UQSUB, replacing sequences of comparisons, subtractions, and conditional selects, leading to better code generation.
