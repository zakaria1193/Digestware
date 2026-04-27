---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- signed overflow
- dot product
commit_hash: 78c277483b703383cf12d3a7937570a4314a7124
source_type: github
author: Richard Biener
headline: Tree-optimization/124946 - Fix signed overflow with emulated mixed dot-prod
tldr: GCC now avoids signed overflow when biasing unsigned vector operands in emulated
  mixed dot-product operations, improving code correctness.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses a signed overflow issue in the ``vect_emulate_mixed_dot_prod``
  function within GCC's vectorization pass.  When biasing the unsigned vector operand,
  the operation must be performed in an unsigned type to prevent potential signed
  overflow. This fix ensures that the biasing is done correctly, leading to accurate
  results in emulated mixed dot-product operations.
primer_general: Modern CPUs often have specialized instructions for performing mathematical
  operations on multiple data elements simultaneously (vectorization). When the target
  CPU doesn't have direct support for a particular operation (like a mixed dot-product),
  the compiler can emulate it using a sequence of other instructions.  This commit
  fixes a potential overflow issue during this emulation process. By performing calculations
  in an unsigned type, the compiler developers ensure that the results are accurate,
  especially when dealing with large values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/78c277483b703383cf12d3a7937570a4314a7124
date: '2026-04-21'
---

When emulating mixed dot-product operations, GCC now performs constant biasing of the unsigned vector operand in an unsigned type. This change avoids potential signed overflow issues that could occur otherwise. This improves the correctness of the generated code for vectorized loops.
