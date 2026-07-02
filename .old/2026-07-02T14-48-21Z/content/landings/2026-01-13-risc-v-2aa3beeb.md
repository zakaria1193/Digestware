---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
- rvv
- optimization
commit_hash: 2aa3beeb892ac38ca5a7ca9e3a25b0eaab567cd5
source_type: github
author: Pan Li
headline: 'RISC-V: Combine vec_duplicate + vmsle.vv to vmsle.vx based on GR2VR cost'
tldr: GCC now combines RISC-V ``vec_duplicate`` and ``vmsle.vv`` instructions into
  ``vmsle.vx`` when the cost of moving data to vector registers is low enough.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change modifies ``config/riscv/predicates.md`` and ``config/riscv/riscv-v.cc``
  to enable the combination of ``vec_duplicate`` and ``vmsle.vv`` into ``vmsle.vx``
  when the GR2VR cost is zero.  The patch ensures that the swapped RTX code is handled
  correctly.  The optimization is a late-combine that depends on the cost model.
primer_general: Vectorization is a compiler optimization technique that allows performing
  the same operation on multiple data elements simultaneously using vector instructions.  RISC-V
  is a modern instruction set architecture that includes vector extensions (RVV).
  This commit optimizes code generation for RISC-V by combining two vector instructions
  (``vec_duplicate`` and ``vmsle.vv``) into a single, more efficient instruction (``vmsle.vx``).  The
  compiler only performs this optimization when it determines that the cost of moving
  data into vector registers is low enough to make it worthwhile.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2aa3beeb892ac38ca5a7ca9e3a25b0eaab567cd5
date: '2026-01-13'
---

GCC now combines the ``vec_duplicate`` and ``vmsle.vv`` RISC-V vector instructions into a single ``vmsle.vx`` instruction when the cost of transferring data from general-purpose registers to vector registers (GR2VR) is sufficiently low (zero). This optimization reduces the number of instructions executed and improves performance. The compiler makes this decision based on the GR2VR cost, performing the late-combine optimization only when it's beneficial.
