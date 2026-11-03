---
project: gcc
subsystem: bb-reorder
patch_id: null
tags:
- bb-reorder
- compiler parameter
- target specific
commit_hash: b2c1ee0989bb010143e8eb5d931ffc28bb1aca7c
source_type: github
author: Kyrylo Tkachov
headline: bb-reorder respects max-goto-duplication-insns budget without instruction
  lengths
tldr: The computed goto duplication pass now correctly respects the `max-goto-duplication-insns`
  parameter even on targets lacking instruction length attributes.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `pass_duplicate_computed_gotos` in `bb-reorder.cc` previously relied
  on `get_attr_min_length` to determine the cost of duplicating basic blocks. On targets
  where `get_attr_min_length` returns 0 (due to lack of length attributes), the `duplication_size`
  and thus the `max-goto-duplication-insns` budget became effectively infinite. This
  commit introduces `duplication_unit` and `duplication_size` helpers that count one
  unit per instruction (excluding debug insns) on these problematic targets, ensuring
  the `max-goto-duplication-insns` parameter is correctly enforced. Targets with existing
  leng…
primer_glossary:
- term: bb-reorder
  definition: A GCC pass that reorders basic blocks within a function to improve instruction
    cache locality and other performance characteristics.
- term: computed goto
  definition: A control flow mechanism where the target of a jump is determined at
    runtime by an expression, rather than being a statically known label.
- term: basic block
  definition: A sequence of instructions with a single entry point and a single exit
    point. Control flow only enters at the beginning and leaves at the end.
- term: instruction length attribute
  definition: A target-specific attribute that defines the size (in bytes) of machine
    instructions. This is used by the compiler for various analyses and optimizations.
- term: max-goto-duplication-insns
  definition: A GCC parameter that limits the maximum number of instructions in a
    basic block that can be duplicated by the `duplicate_computed_gotos` pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b2c1ee0989bb010143e8eb5d931ffc28bb1aca7c
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This commit fixes an issue where the `duplicate_computed_gotos` pass ignored the `max-goto-duplication-insns` parameter on targets lacking instruction length attributes. On such targets, instruction lengths were reported as zero, causing the pass to treat all blocks as costing zero and effectively disabling the budget. The fix introduces `duplication_unit` and `duplication_size` functions to count one unit per active instruction on these targets, ensuring the parameter is respected. This corrects the behavior for targets like c6x, ia64, and m68k, preventing excessive block duplication and ensuring the parameter's intended effect.
