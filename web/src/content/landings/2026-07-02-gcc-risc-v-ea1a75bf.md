---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- optimization
- compiler
commit_hash: ea1a75bfd580788b6c1f0a772051797bbddedf82
source_type: github
author: Jeff Law
headline: RISC-V ADD synthesis exploits new instructions and costs.
tldr: RISC-V compiler can now synthesize ADD instructions more efficiently using new
  patterns and cost models.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'RISC-V instruction selection for ADD instructions. Exploits `add.uw`
  for constants with zero upper 32 bits and sign bit set. Recognizes `INT_MIN + X`
  as `binvi(X)` followed by `add` (which Combine folds). Replaces `riscv_const_insns`
  cost model with `riscv_integer_cost` for proper cost comparison.


  Fixes xfail for xor-synthesis-2.c.'
primer_glossary:
- term: add.uw
  definition: A RISC-V instruction that performs an unsigned addition with a zero-extended
    32-bit immediate.
- term: binvi
  definition: A RISC-V instruction that performs a bitwise inversion with a zero-extended
    32-bit immediate. It can be used to implement the addition of INT_MIN by flipping
    the sign bit.
- term: RISC-V instruction synthesis
  definition: The process by which the compiler generates machine instructions from
    intermediate representations, aiming for efficiency and correctness for the target
    architecture.
- term: riscv_integer_cost
  definition: A cost function used in the RISC-V GCC backend to estimate the performance
    cost of generating integer instructions.
- term: riscv_const_insns
  definition: An older cost function that clamped instruction costs, potentially leading
    to suboptimal instruction selection.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea1a75bfd580788b6c1f0a772051797bbddedf82
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

GCC's RISC-V backend gains improved ADD instruction synthesis. It now leverages the `add.uw` instruction for specific constant patterns and recognizes INT_MIN additions as a `binvi` operation. This change also refactors the cost model to use `riscv_integer_cost` over `riscv_const_insns`, enabling better selection of cheaper instructions when multiple options exist.
