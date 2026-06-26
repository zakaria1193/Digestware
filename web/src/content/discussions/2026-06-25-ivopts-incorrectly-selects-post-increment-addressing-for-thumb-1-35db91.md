---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- arm
- thumb-1
- optimization
- ivopts
discussion_id: CAFiYyc2QfNn-bgjbvvfuJCzyiULfocxfEy_gTYwJqU9dwL0aBA@mail.gmail.com
source_type: public_inbox
title: 'Re: IVOPTs incorrectly selects post-increment addressing for Thumb-1'
headline: IVOPTs incorrectly selects post-increment addressing for Thumb-1
tldr: GCC's IVOPTs pass generates suboptimal code for Thumb-1 targets by incorrectly
  selecting post-increment addressing, leading to inefficient loops.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Performance degradation for Thumb-1 code due to suboptimal addressing mode selection.
- Complexity in compiler's cost model for different ARM architectures and addressing
  modes.
- Potential for increased code size due to less efficient instruction sequences.
exchanges: []
primer_expert: The `IVOPTs` pass in GCC is a crucial component for optimizing loops
  by analyzing and transforming induction variables. This bug report points to a specific
  deficiency in how `IVOPTs` interacts with the ARM backend's addressing mode selection
  for Thumb-1 targets, which use the `ARM_AUTOINC_VALID_FOR_MODE_P` macro to determine
  valid auto-increment capabilities. The core issue likely lies within the cost model
  used by `IVOPTs` failing to accurately reflect the true cost of post-increment addressing
  on Thumb-1.
primer_general: Compilers like GCC try to make your code run faster by optimizing
  it. One common optimization is for 'loops' (code that repeats many times). Inside
  loops, variables often change in a predictable way, like counting up by one each
  time. The compiler has a special part called 'IVOPTs' (Induction Variable Optimizations)
  that looks for these patterns and tries to generate more efficient machine instructions.
  This particular discussion highlights a problem where, for a specific type of ARM
  processor called 'Thumb-1', the compiler is choosing a less efficient way to access
  memory inside loops. It's using something called 'post-increment addressing' (where
  the memory address is updated *after* the data is fetched), but this isn't always
  the best choice for Thumb-1, leading to slower code than necessary.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc2QfNn-bgjbvvfuJCzyiULfocxfEy_gTYwJqU9dwL0aBA@mail.gmail.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion addresses an issue where GCC's induction variable optimisations (IVOPTs) generate suboptimal code for Thumb-1 architecture. Specifically, the compiler incorrectly selects post-increment addressing for simple loops, even when it results in less efficient code. The core problem is that `ARM_AUTOINC_VALID_FOR_MODE_P` is enabled for Thumb-1, but IVOPTs fails to account for the resulting performance implications.
