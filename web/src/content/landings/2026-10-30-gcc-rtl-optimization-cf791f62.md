---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- LRA
- optimization
- rtl
commit_hash: cf791f625f246add50d178e8a466408d17595efc
source_type: github
author: Vladimir N. Makarov
headline: 'LRA: Spill (plus (reg) (const)) for memory constraints'
tldr: The LRA pass can now spill (plus (reg) (const)) expressions when they are constrained
  to memory.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a limitation in GCC's Local Register Allocation
  (LRA) pass, specifically within `lra-constraints.cc`. The Register Transfer Language
  (RTL) expression `(plus (reg) (const))` arises when a register holding a base address
  is combined with a constant offset. If this expression is later constrained to a
  memory operand (e.g., `(mem (plus (reg) (const)))`) and cannot be satisfied by available
  registers, LRA previously lacked the mechanism to spill it. The patch introduces
  `reg_plus_const_p` to detect this pattern and implements spilling logic for such
  cases, improving LRA's abi…
primer_glossary:
- term: LRA
  definition: Local Register Allocation, a phase in the GCC compiler that optimizes
    register usage within a basic block or a small region of code.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC
    to describe machine instructions and operations.
- term: spill
  definition: The process of moving a value from a CPU register to memory when there
    are not enough registers to hold all the live values.
- term: (plus (reg) (const))
  definition: An RTL expression representing an addition operation where one operand
    is a register and the other is a constant. This often corresponds to an address
    calculation.
- term: memory constraint
  definition: In the context of instruction selection or optimization, a requirement
    that an operand must be accessed via memory, rather than directly from a register.
discussion_id_link: github:gcc-mirror/gcc#128251
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cf791f625f246add50d178e8a466408d17595efc
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch enhances the Local Register Allocation (LRA) pass to handle a specific case where an expression of `(plus (reg) (const))` cannot be satisfied by a register and must be stored to memory. Previously, LRA could only spill registers, not these compound memory constraints. The change introduces new logic to identify and spill these memory-constrained expressions, resolving a bug reported in PR 128251.
