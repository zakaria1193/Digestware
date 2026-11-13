---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- optimization
- RTL
- bitwise operations
commit_hash: 7fe2ca4c9333e0d023be08271a51c6769569da3f
source_type: github
author: Xi Ruoyao
headline: 'LoongArch: Fix missed optimization for bitwise OR of AND results'
tldr: Enables optimization for bitwise OR of AND results in LoongArch by factoring
  out common logic.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `loongarch_rtx_costs` function, responsible for calculating the
  cost of various RTL operations on LoongArch, has been updated to better handle patterns
  involving bitwise operations. Specifically, a new helper function, `loongarch_cost_bstrins_for_any_or_plus`,
  is introduced to identify and cost the pattern of a bitwise OR of two bitwise AND
  expressions. This is crucial because the target-independent front-end now prefers
  `plus` over `ior` in certain contexts. By factoring out this logic and calling the
  helper for IOR, XOR, and PLUS, the compiler can correctly cost and optimize such
  sequen…
primer_glossary:
- term: LoongArch
  definition: An open-source RISC-based instruction set architecture (ISA) developed
    by Loongson Technology, primarily for high-performance computing and embedded
    systems.
- term: RTL (Register Transfer Language)
  definition: An intermediate representation used in GCC that describes operations
    on registers and memory. It's a low-level language that is close to machine code
    but is still target-independent to some extent.
- term: IOR
  definition: Bitwise Inclusive OR operation.
- term: AND
  definition: Bitwise AND operation.
- term: Cost model
  definition: A component of the compiler that estimates the performance cost (e.g.,
    execution time, instruction count) of different code sequences or RTL patterns
    on a specific target architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7fe2ca4c9333e0d023be08271a51c6769569da3f
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

An optimization for `bstrins_di_for_ior_mask` in the LoongArch backend was being missed because the target-independent code increasingly preferred `plus` over `ior`. This commit introduces a helper function, `loongarch_cost_bstrins_for_any_or_plus`, to recognize the bitwise OR of two bitwise AND results. This function is now called during cost calculation for IOR, XOR, and PLUS operations, fixing a test failure in `bstrins-3.c`.
