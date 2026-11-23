---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- optimization
- if-conversion
commit_hash: 2da8c9ec0b06bf17fc5513ae22abafd0e1bdec18
source_type: github
author: Jiahao Xu
headline: Add RTX costs for `if_then_else' expressions
tldr: Adds cost information for `if_then_else` expressions in LoongArch to enable
  better if-conversion optimizations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `loongarch_rtx_costs` function has been updated to include an entry
  for `IF_THEN_ELSE`. Previously, the middle-end would provide a generic estimate
  for this construct, assuming a cost of 3 instructions (12 units). By defining a
  specific, low cost (1 machine cycle, ignoring the branch taken cost), the backend
  now signals to the middle-end that `if_then_else` structures are cheap. This encourages
  the middle-end's if-conversion passes to transform conditional branches into predicated
  instructions where beneficial.
primer_glossary:
- term: LoongArch
  definition: A RISC instruction set architecture developed in China, designed for
    high performance and efficiency. GCC has a backend for this architecture.
- term: RTX
  definition: Representation Tree. GCC's internal intermediate representation for
    code, used after parsing and before machine code generation.
- term: if_then_else
  definition: A conditional construct in GCC's intermediate representation (RTX) that
    represents an if-then-else statement or a conditional expression.
- term: cost information
  definition: Estimates of the execution cost (in terms of cycles, instructions, or
    other metrics) for various operations or constructs, used by compiler optimization
    passes.
- term: if-conversion
  definition: An optimization technique that transforms conditional control flow (if-statements,
    branches) into predicated instructions or conditional moves, potentially improving
    instruction-level parallelism.
- term: backend
  definition: The part of the compiler responsible for generating machine code for
    a specific target architecture.
- term: middle-end
  definition: The part of the compiler that performs optimizations on the intermediate
    representation (IR) of the code, independent of the target architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2da8c9ec0b06bf17fc5513ae22abafd0e1bdec18
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

The LoongArch backend now defines cost information for `if_then_else` expressions. Without this, the middle-end estimates the cost conservatively. By assigning a cost of a single machine cycle (ignoring branch costs), this change aims to encourage more aggressive if-conversion optimizations, where conditional logic is converted into predicated instructions.
