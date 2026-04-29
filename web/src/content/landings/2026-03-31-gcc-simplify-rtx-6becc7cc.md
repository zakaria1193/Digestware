---
project: gcc
subsystem: gcc/simplify-rtx
patch_id: null
tags:
- optimization
- risc-v
- compiler
commit_hash: 6becc7cc2c06b3941d829e08100a6ff70cc55262
source_type: github
author: Bohan Lei
headline: Simplify RTX comparisons of bitwise operations with constants.
tldr: GCC now simplifies certain comparisons involving bitwise AND/OR operations with
  constants, potentially fixing an ICE on RISC-V.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The simplify-rtx pass in GCC aims to simplify RTL expressions. This
  patch modifies ``simplify_relational_operation_1`` function to handle specific patterns
  involving comparisons of bitwise AND/OR operations with constants. The goal is to
  optimize these expressions before instruction splitting, potentially avoiding issues
  like the reported ICE on RISC-V related to instruction condition changes.
primer_general: The "simplify-rtx" pass in GCC is responsible for simplifying Register
  Transfer Language (RTL) expressions, an intermediate representation used during
  compilation. This pass identifies opportunities to rewrite complex expressions into
  simpler, equivalent forms, leading to more efficient code generation. This patch
  focuses on simplifying comparisons involving bitwise AND/OR operations with constant
  values, allowing GCC to optimize code that uses these patterns.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6becc7cc2c06b3941d829e08100a6ff70cc55262
date: '2026-03-31'
---

This patch introduces simplifications for expressions of the form ``(cmp (and/ior x C1) C2)`` within GCC's simplify-rtx pass. By analyzing the relationships between the constants C1 and C2, the compiler can determine cases where the comparison can never be true, allowing for optimization. This change addresses a reported internal compiler error (ICE) on RISC-V and improves code generation in specific scenarios.
