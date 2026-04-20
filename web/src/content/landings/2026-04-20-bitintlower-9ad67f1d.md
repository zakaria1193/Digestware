---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- bitint
- risc-v
- optimization
- code generation
- bugfix
commit_hash: 9ad67f1d996700bdba62092ec15e249387c844df
source_type: github
author: Jakub Jelinek
headline: 'Bitintlower: Padding bit fixes, part 3'
tldr: Fixes issues in bitint lowering related to padding bits, specifically for RISC-V,
  by correcting shift operations and ensuring proper clearing of padding bits.
why_it_matters: Ensures correct code generation and execution for bitint types, especially
  on architectures like RISC-V, addressing failures in test cases.
impact_score: 6
impact_rationale: Fixes correctness issues in bitint lowering, affecting code generation
  on specific architectures.
performance_win: false
breaking_change: false
outcome: committed
primer: Bitint lowering is a compiler optimization that transforms operations on arbitrarily
  sized integer types (bitints) into sequences of operations on machine-sized integers.
  This is necessary because some hardware doesn't directly support bitints.  The lowering
  process must handle padding bits, which are unused bits within the underlying integer
  representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ad67f1d996700bdba62092ec15e249387c844df
date: '2026-04-20'
---

This commit addresses failures in bitint lowering on RISC-V. It corrects the iteration condition in `lower_shift_stmt` and uses signed right shift expressions. It also ensures that padding bits are properly cleared for unsigned multiplication when the precision isn't a multiple of the limb precision.
