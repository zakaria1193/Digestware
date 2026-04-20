---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- bitint
- riscv
- bugfix
commit_hash: 9ad67f1d996700bdba62092ec15e249387c844df
source_type: github
author: Jakub Jelinek
headline: 'Bitintlower: Fixes for padding bits in bit-integer lowering.'
tldr: Fixes issues in bit-integer lowering related to padding bits, ensuring correct
  behavior on RISC-V and other architectures.
why_it_matters: Resolves incorrect code generation for bit-integers, particularly
  when dealing with padding, which could lead to unexpected behavior and incorrect
  results.
impact_score: 6
impact_rationale: Fixes incorrect codegen for bit integers, correcting a functional
  bug.
performance_win: false
breaking_change: false
outcome: committed
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ad67f1d996700bdba62092ec15e249387c844df
date: '2026-04-20'
---

This commit addresses issues related to padding bits in the bitint lowering pass. It fixes incorrect loop conditions in `lower_shift_stmt`, switches to signed RSHIFT_EXPR, and ensures padding bits are cleared for unsigned MULT_EXPR when the precision is not a multiple of the limb precision. These changes resolve failures on riscv64-linux and other targets.
