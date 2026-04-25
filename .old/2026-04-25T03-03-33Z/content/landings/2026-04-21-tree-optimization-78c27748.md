---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- signed overflow
- dot-product
commit_hash: 78c277483b703383cf12d3a7937570a4314a7124
source_type: github
author: Richard Biener
headline: Fixes Signed Overflow in Emulated Mixed Dot-Product Vectorization.
tldr: The vectorizer avoids signed overflow when biasing the unsigned vector operand
  in emulated mixed dot-product operations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In ``tree-vect-loop.cc``, the ``vect_emulate_mixed_dot_prod`` function
  now performs constant biasing in an unsigned type. This change prevents potential
  signed overflows that could occur when biasing the unsigned vector operand during
  emulated mixed dot-product vectorization.
primer_general: Modern CPUs can perform arithmetic on multiple data items at once;
  this is called SIMD (single instruction multiple data) or "vector" processing.  The
  compiler can automatically transform scalar code to use vector instructions; this
  is called "auto-vectorization".  This commit fixes a bug in the auto-vectorization
  code that could lead to incorrect results when performing dot-product operations
  on mixed signed and unsigned data.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/78c277483b703383cf12d3a7937570a4314a7124
date: '2026-04-21'
---

When emulating mixed dot-product operations, the compiler biases the unsigned vector operand. This commit ensures that the biasing is performed in an unsigned type to avoid potential signed overflows. By performing the constant biasing in an unsigned type, the compiler prevents unexpected behavior due to signed overflow, leading to more reliable and correct code generation for vector operations.
