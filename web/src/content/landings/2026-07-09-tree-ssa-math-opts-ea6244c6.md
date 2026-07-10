---
project: gcc
subsystem: tree-ssa-math-opts
patch_id: null
tags:
- optimization
- aarch64
- floating-point
- fma
commit_hash: ea6244c6f8db7663aca4e684c3105325d8282ede
source_type: github
author: Philipp Tomsich
headline: GCC separates FMA deferral control for optimizations
tldr: GCC introduces a new parameter to control FMA deferral independently from reassoc
  reordering, benefiting targets like AArch64.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `param_avoid_fma_max_bits` previously gated both the widening_mul
  FMA-deferring transform (leaving FMUL + FADD) and the reassoc loop-carried-FMA reordering.
  This commit separates these into two parameters: `param_avoid_fma_max_bits` for
  reassoc reordering and a new `param_widening_mul_defer_fma` for the multiply-add
  deferral. This allows targets, like AArch64 with `AVOID_CROSS_LOOP_FMA`, to selectively
  disable FMA deferral without impacting FMA reassoc reordering, improving performance
  for FP reductions.'
primer_glossary:
- term: FMA
  definition: Fused Multiply-Add, an instruction that performs a multiplication and
    an addition in a single operation, often with higher precision and performance
    than separate operations.
- term: tree-ssa-math-opts
  definition: A GCC optimization pass that operates on the SSA (Static Single Assignment)
    form of the intermediate representation to perform various arithmetic optimizations,
    including those related to floating-point operations.
- term: reassoc reordering
  definition: An optimization that reassociates arithmetic operations to potentially
    improve performance or enable other optimizations. In this context, it refers
    to reordering FMA operations.
- term: SSA form
  definition: Static Single Assignment form is an intermediate representation in compilers
    where every variable is assigned a value only once. This simplifies many data-flow
    analyses and optimizations.
- term: AArch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and servers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea6244c6f8db7663aca4e684c3105325d8282ede
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

GCC's tree-ssa-math-opts pass now allows finer control over floating-point fused multiply-add (FMA) optimizations. A new parameter, `widening-mul-defer-fma`, is introduced to gate the deferral of multiply-accumulate operations, separate from the `avoid-fma-max-bits` parameter which controls reassoc reordering. This change prevents performance regressions on targets like AArch64, where disabling reassoc reordering to avoid FMA also unnecessarily disabled other beneficial optimizations.
