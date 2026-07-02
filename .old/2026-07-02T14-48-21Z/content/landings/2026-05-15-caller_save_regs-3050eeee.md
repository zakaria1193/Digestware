---
project: gcc
subsystem: caller_save_regs
patch_id: null
tags:
- rtl-optimization
- register allocation
- abi
commit_hash: 3050eeeee4183b9723a1465552b5798a1c21d223
source_type: github
author: H.J. Lu
headline: 'Caller_save_regs: Return the enabled registers.'
tldr: GCC now only considers enabled registers when determining caller-saved registers,
  fixing a potential optimization issue.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `function_abi_aggregator::caller_save_regs` in
  `function-abi.cc` to return the enabled registers. This ensures that only registers
  enabled in the caller are considered as caller-saved.  This correction is necessary
  for proper register allocation and optimization, particularly in scenarios where
  certain registers may be disabled based on the calling convention or target architecture.  This
  fixes PR rtl-optimization/125321.
primer_general: When a function calls another function, some registers need to be
  saved to preserve their values.  These are called caller-saved registers.  This
  commit ensures that GCC only considers registers that are actually available for
  saving when making these decisions. This prevents the compiler from trying to save
  registers that are not enabled, which could lead to incorrect or inefficient code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3050eeeee4183b9723a1465552b5798a1c21d223
date: '2026-05-15'
is_stub: false
---

GCC's `caller_save_regs` function now returns only the enabled registers.  Since a caller can only save a register if it is enabled in the caller, this change ensures that the register allocation process considers only valid registers for saving. This resolves a potential issue where disabled registers might have been incorrectly considered as caller-saved, which could lead to suboptimal code generation.
