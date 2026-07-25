---
project: gcc
subsystem: target/x86
patch_id: null
tags:
- x86
- optimization
- sse
- avx
commit_hash: d20adcae36e31cb96a9869566a243e3d6f21ab8d
source_type: github
author: Richard Biener
headline: Improve x86 horizontal FP instruction costing.
tldr: Fixes x86 combine optimization for horizontal FP add/sub instructions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch improves how GCC costs certain x86 SSE3/AVX horizontal floating-point
  instructions (`haddv2df3`, `hsubv2df3`, etc.) by introducing a `cost_special` attribute.
  This attribute, set to `haddsub`, allows `ix86_insn_cost` to assign a cost similar
  to a standard ADD instruction. This fixes a hole in the cost model that previously
  prevented `combine` from optimizing certain horizontal reduction patterns, such
  as those found in `pr54400.c`.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures developed by Intel, widely
    used in desktop and server computers.
- term: SSE3
  definition: Streaming SIMD Extensions 3, an instruction set extension for x86 processors
    that added several floating-point and integer processing instructions.
- term: AVX
  definition: Advanced Vector Extensions, an instruction set extension for x86 processors
    that expanded the width of SIMD registers and introduced new instructions.
- term: insn_cost
  definition: A mechanism within the compiler to estimate the execution cost (e.g.,
    cycles) of a specific machine instruction on the target architecture.
- term: combine
  definition: A GCC optimization pass that performs instruction combination and simplification,
    aiming to replace sequences of instructions with equivalent, more efficient ones.
- term: horizontal FP add/sub
  definition: Floating-point addition or subtraction operations that combine elements
    from different lanes of a SIMD vector, as opposed to element-wise operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d20adcae36e31cb96a9869566a243e3d6f21ab8d
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This commit refines the instruction costing for x86's horizontal floating-point add and subtract operations, specifically for SSE3 and AVX instructions. By introducing a new `cost_special` attribute and correctly costing these `hadd`/`hsub` operations, the `combine` optimization pass can now properly identify and recover the single `hadd` instruction in certain reduction patterns. This addresses issues in test cases previously failing due to incorrect cost estimations.
