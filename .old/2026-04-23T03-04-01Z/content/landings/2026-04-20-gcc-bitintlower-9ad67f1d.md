---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- bitint
- risc-v
- bugfix
- gimple
commit_hash: 9ad67f1d996700bdba62092ec15e249387c844df
source_type: github
author: Jakub Jelinek
headline: 'Bitintlower: Fixes padding bits in shifts and float conversions.'
tldr: Fixes issues with padding bits in shift operations and float conversions for
  extended bit integers, resolving test failures on RISC-V and other architectures.
why_it_matters: Ensures correct behavior of bit integer operations, especially with
  padding, which is important for avoiding unexpected results and security vulnerabilities,
  particularly on architectures like RISC-V, ARM, s390x, and LoongArch.
impact_score: 6
impact_rationale: Fixes incorrect behavior in bit integer operations, resolving test
  failures and improving correctness.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch focuses on `gimple-lower-bitint.cc`, specifically the `bitint_large_huge`
  namespace which handles lowering of extended bit integers. The fixes involve correcting
  loop conditions and signedness in `lower_shift_stmt` and `lower_float_conv_stmt`,
  as well as ensuring padding bits are cleared in `lower_muldiv_stmt`.  These functions
  are part of the bitint lowering pass, which transforms high-level bit integer operations
  into lower-level GIMPLE instructions.
primer_general: Bit integers are integer data types that can have a size that is not
  a standard power of 2 (e.g., 24-bit integers). The `bitintlower` pass in GCC is
  responsible for converting operations on these bit integers into simpler operations
  that can be executed by the target architecture. The conversion process involves
  handling padding bits, which are extra bits added to the bit integer to align it
  to a specific memory boundary. This commit fixes issues related to how these padding
  bits are handled during shift and multiplication operations, which are crucial for
  correct execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ad67f1d996700bdba62092ec15e249387c844df
date: '2026-04-20'
---

This commit addresses failures in the bitintlower pass related to padding bits during shift operations and float conversions. It corrects the loop condition in `lower_shift_stmt`, ensures correct signedness in `RSHIFT_EXPR` for both `lower_shift_stmt` and `lower_float_conv_stmt`, and clears padding bits in `lower_muldiv_stmt` for unsigned multiplication. These changes fix test failures on RISC-V and improve the correctness of bit integer operations on ARM, s390x, and LoongArch architectures.
