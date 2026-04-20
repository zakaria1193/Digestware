---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- bitint
- riscv
- code generation
- bugfix
commit_hash: 9ad67f1d996700bdba62092ec15e249387c844df
source_type: github
author: Jakub Jelinek
headline: 'Bitintlower: Padding bit fixes, part 3 [PR123635]'
tldr: Fixes issues in bitint lowering related to padding bits, shift operations, and
  multiplication, resolving failures on RISC-V.
why_it_matters: Corrects critical bugs in bitint lowering, ensuring correct code generation
  for extended bit integers, particularly on RISC-V architectures.
impact_score: 7
impact_rationale: Fixes bugs related to bitint lowering, a relatively new feature,
  which directly impacts code generation.
performance_win: false
breaking_change: false
outcome: committed
primer: Bitint lowering is a compiler pass that transforms operations on bit-fields
  (integers with a specified number of bits) into sequences of machine instructions.  When
  the bit-field size exceeds the machine's native word size, the compiler must synthesize
  multi-word operations.  Padding bits are extra bits added to ensure proper alignment
  or to fill out a partial word.  Proper handling of padding bits during operations
  like shifting and multiplication is crucial for correctness.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ad67f1d996700bdba62092ec15e249387c844df
date: '2026-04-20'
---

This commit fixes several issues in the bitint lowering pass, specifically related to padding bits and shift operations.  It corrects loop conditions in `lower_shift_stmt`, uses signed RSHIFT_EXPR instead of unsigned in `lower_shift_stmt` and `lower_float_conv_stmt`, and clears padding bits after libgcc calls in `lower_muldiv_stmt` for unsigned MULT_EXPR. These fixes resolve failures observed on riscv64-linux.
