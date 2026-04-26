---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- rvv
- vectorization
- optimization
commit_hash: 2aa3beeb892ac38ca5a7ca9e3a25b0eaab567cd5
source_type: github
author: Pan Li
headline: 'RISC-V: Combine vec_duplicate + vmsle.vv to vmsle.vx based on GR2VR costs.'
tldr: The RISC-V backend can now combine vec_duplicate and vmsle.vv instructions into
  a single vmsle.vx instruction, depending on GR2VR cost.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit modifies ``config/riscv/riscv-v.cc`` to combine `vec_duplicate`
  and `vmsle.vv` into `vmsle.vx` when the GR2VR cost is zero. The predicate `ge` is
  added to the swappable cmp operator iterator in ``predicates.md``.  The `get_swapped_cmp_rtx_code`
  function is updated to handle swapped rtx codes.
primer_general: The RISC-V vector extension (RVV) adds support for vector operations,
  improving performance on data-parallel workloads. Compilers can often combine multiple
  instructions into a single instruction to improve efficiency. This commit enables
  the compiler to combine two vector instructions (`vec_duplicate` and `vmsle.vv`)
  into a single instruction (`vmsle.vx`) on RISC-V processors, provided that the cost
  of moving data between general-purpose and vector registers is low enough to make
  the optimization worthwhile.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2aa3beeb892ac38ca5a7ca9e3a25b0eaab567cd5
date: '2026-01-13'
---

The RISC-V backend now combines `vec_duplicate` and `vmsle.vv` instructions into `vmsle.vx` under certain conditions. This optimization depends on the cost of moving data from general-purpose registers to vector registers (GR2VR). When the GR2VR cost is zero, the combination occurs; otherwise, it's rejected.  This reduces the number of instructions, improving performance.
